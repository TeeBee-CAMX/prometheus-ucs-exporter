#!/usr/bin/env python3
# 01/2026 TeeBeeCAMX

# SPDX-FileCopyrightText: 2022 2022 Marshall Wace <opensource@mwam.com>
#
# SPDX-License-Identifier: GPL-3.0-only

from fastapi import BackgroundTasks, FastAPI, Query, Response
import logging
import sys
import os
from prometheus_client import Counter, Gauge, REGISTRY, PROCESS_COLLECTOR, PLATFORM_COLLECTOR, GC_COLLECTOR
from prometheus_client.openmetrics.exposition import generate_latest, CONTENT_TYPE_LATEST
from ucsmsdk.ucshandle import UcsHandle
from ucs.computecapacity import ComputeCapacity
from ucs.ethernet import Ethernet
from ucs.fan import Fan
from ucs.faults import Faults
from ucs.fibrechannel import FibreChannel
from ucs.memerror import MemError
from ucs.power import Power
from ucs.swsystem import SwSystem
from ucs.temperature import Temperature
from ucs.vnic import Vnic

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Disable default Python/process/platform metrics collectors:
# - PROCESS_COLLECTOR -> process_* (e.g. process_open_fds)
# - PLATFORM_COLLECTOR -> python_info, process_* helpers, etc.
# - GC_COLLECTOR -> python_gc_* metrics
for _collector in (PROCESS_COLLECTOR, PLATFORM_COLLECTOR, GC_COLLECTOR):
    try:
        REGISTRY.unregister(_collector)
    except Exception:
        pass

# ---- OpenMetrics UNIT injection (best-effort) ----
# Prometheus is strict: if a UNIT line is present, the unit MUST be a suffix of the metric family name.
# We therefore only emit UNIT for families whose names already end with a known unit suffix.
_UNIT_SUFFIXES = {
    "bytes": "bytes",
    "seconds": "seconds",
    "celsius": "celsius",
    "fahrenheit": "fahrenheit",
    "rpm": "rpm",
    "watts": "watts",
    "volts": "volts",
    "amperes": "amperes",
    "percent": "percent",
    "ratio": "ratio",
    "count": "count",
    "requests": "requests",
    "errors": "errors",
    "fds": "fds",
    # Non-standard but commonly used in exporters; only emitted when it already matches the suffix:
    "mbytes": "mbytes",
    "gbytes": "gbytes",
    "tbytes": "tbytes",
    "kbytes": "kbytes",
    "mib": "mib",
    "gib": "gib",
    "tib": "tib",
    "kb": "kb",
    "mb": "mb",
    "gb": "gb",
    "tb": "tb",
    "terabytes": "terabytes",
    "gigabytes": "gigabytes",
    "megabytes": "megabytes",
}

def _infer_unit_from_family_name(family: str) -> str | None:
    # unit is taken from the last underscore segment; we only accept it if it is in our allowlist
    # AND it is an actual suffix (Prometheus/OpenMetrics compatibility).
    if "_" not in family:
        return None
    suffix = family.rsplit("_", 1)[-1]
    return _UNIT_SUFFIXES.get(suffix)

def _inject_unit_lines(openmetrics_text: str) -> str:
    """
    Insert '# UNIT <family> <unit>' lines right after TYPE lines (if missing)
    for any family where we can safely infer a unit from the family name suffix.
    """
    lines = openmetrics_text.splitlines()
    out: list[str] = []
    current_family: str | None = None
    seen_unit_for_family = False
    for line in lines:
        if line.startswith("# HELP "):
            # new family starts
            current_family = line.split(" ", 2)[2].split(" ", 1)[0]  # '# HELP <name> ...'
            seen_unit_for_family = False
            out.append(line)
            continue

        if line.startswith("# UNIT "):
            seen_unit_for_family = True
            out.append(line)
            continue

        if line.startswith("# TYPE "):
            out.append(line)
            if current_family and not seen_unit_for_family:
                unit = _infer_unit_from_family_name(current_family)
                if unit:
                    out.append(f"# UNIT {current_family} {unit}")
                    seen_unit_for_family = True
            continue

        out.append(line)

    # ensure trailing newline like prometheus_client outputs
    return "\n".join(out) + ("\n" if not openmetrics_text.endswith("\n") else "")
# ---- End UNIT injection ----
# ---- Drop unwanted metric families (text-level filter; keeps output valid) ----
# Some prometheus_client versions auto-emit *_total / *_created for Counters and may
# keep them registered across reloads. If you want to hide a metric completely,
# the safest minimal approach is to filter it out of the exposition text.
_DROP_FAMILY_PREFIXES = ("ucs_exporter_failure",)

def _drop_metric_families_from_text(exposition_text: str, prefixes=_DROP_FAMILY_PREFIXES) -> str:
    lines = exposition_text.splitlines()
    out: list[str] = []
    for line in lines:
        # Drop samples (including *_total / *_created) and their metadata lines.
        if line.startswith(prefixes):
            continue
        if line.startswith("# HELP ") or line.startswith("# TYPE ") or line.startswith("# UNIT "):
            # metadata line looks like: '# HELP <name> ...' etc.
            parts = line.split(" ", 3)
            if len(parts) >= 3:
                name = parts[2]
                if name.startswith(prefixes):
                    continue
        out.append(line)
    return "\n".join(out) + ("\n" if exposition_text.endswith("\n") else "")
# ---- End drop filter ----


app = FastAPI(
    title="ucs-exporter",
    description="Prometheus exporter for Cisco UCSM.",
    openapi_tags=[
        {"name": "healthz", "description": "Endpoints for checking health",},
        {"name": "metrics", "description": "Endpoints for fetching metrics",},
    ],
)
def get_required_env(env_name):
    """Look up and return an environmental variable, or fail if not found."""
    if env_name not in os.environ:
        sys.stderr.write(
            ("Oops, looks like you haven't set %s, please do that"
             " and then try running the script again\n") % env_name)
        sys.exit(2)
    else:
        return os.environ[env_name]

username = get_required_env('PROM_UCS_USERNAME')
password = get_required_env('PROM_UCS_PASSWORD')

failure_metric = Counter("ucs_exporter_failure", "Failure counter indicating issues")

ready_domains = {}

@app.get(
    "/healthz",
    tags=["health"],
    description="Health check endpoint, returns 'OK' when healthy",
)
async def healthz():
    return "OK"

@app.get(
    "/metrics",
    tags=["metrics"],
    description="Prometheus metrics endpoint",
    responses={
        200: {
            "description": "Successful response for UCSM request. The data comes from UCSM.",
            "content": {
                "text/plain": {
                    "example": {
                        'ucs_eth_err_xmit{blade="None",chassis="chassis-1",domain="domainname",pc_label="A",pc_name="pc-11",port="port-4",rack="None",slot="slot-1",switch="switch-A"} 0.0'
                        '\nucs_eth_err_xmit{blade="None",chassis="chassis-1",domain="domainname",pc_label="A",pc_name="pc-11",port="port-4",rack="None",slot="slot-2",switch="switch-A"} 0.0'
                    }
                }
            }
        }
    }
)
async def metrics(
    response: Response,
    background_tasks: BackgroundTasks,
    domain: str = Query(None, title='The UCSM domain'),
):
    # We fetch the latest metrics in the background since the UCSM API
    # is slow to respond.
    background_tasks.add_task(fetch_metrics, domain)
    # Return a 503 Service Unavailable if the metrics haven't been scraped
    # yet for this domain to prevent drops in metrics during deployment.
    if ready_domains.get(domain, False):
        raw = generate_latest(REGISTRY)
        text = raw.decode("utf-8", errors="replace")
        text = _drop_metric_families_from_text(text)
        text = _inject_unit_lines(text)
        return Response(content=text.encode("utf-8"), status_code=200, media_type=CONTENT_TYPE_LATEST)
    else:
        return Response(content=f"Not yet scraped {domain}...", status_code=503, media_type=CONTENT_TYPE_LATEST)


def fetch_metrics(domain):
    try:
        handle = UcsHandle(domain, username, password)
        handle.login()
        stats = handle.query_classids([
            'ComputeMbPowerStats',
            'ProcessorEnvStats',
            'AdaptorVnicStats',
            'EtherRxStats',
            'EtherTxStats',
            'EquipmentFanStats',
            'SwSystemStats',
            'MemoryErrorStats',
            'FcStats',
            'EtherErrStats',
            'FabricComputeSlotEp',
            'ComputeBlade',
            'ComputeRackUnit',
            'FaultInst',
        ])
        handle.logout()

        ComputeCapacity(domain).generate_metrics(stats)
        Faults(domain).generate_metrics(stats)
        Power(domain).generate_metrics(stats)
        Temperature(domain).generate_metrics(stats)
        Ethernet(domain).generate_metrics(stats)
        Fan(domain).generate_metrics(stats)
        SwSystem(domain).generate_metrics(stats)
        MemError(domain).generate_metrics(stats)
        FibreChannel(domain).generate_metrics(stats)
        Vnic(domain).generate_metrics(stats)
        ready_domains[domain] = True
    except Exception as e:
        logging.error(f"Internal server error {e}")
        failure_metric.inc()
        raise e
