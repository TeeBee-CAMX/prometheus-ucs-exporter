# 01/2026 TeeBeeCAMX
# SPDX-FileCopyrightText: 2022 2022 Marshall Wace <opensource@mwam.com>
#
# SPDX-License-Identifier: GPL-3.0-only

DEFAULT_LABELS = {
    'domain': 'None',
    'rack': 'None',
    'chassis': 'None',
    'blade': 'None'
}

def setup_labels(domain):
    labels = DEFAULT_LABELS.copy()
    labels['domain'] = domain
    return labels
