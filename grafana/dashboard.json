{
  "annotations": {
    "list": [
      {
        "builtIn": 1,
        "datasource": {
          "uid": "-- Grafana --"
        },
        "enable": true,
        "hide": true,
        "iconColor": "rgba(0, 211, 255, 1)",
        "name": "Annotations & Alerts",
        "target": {
          "limit": 100,
          "matchAny": false,
          "tags": [],
          "type": "dashboard"
        },
        "type": "dashboard"
      }
    ]
  },
  "description": "Metrics pulled from each UCS domain by the ucs-exporter.",
  "editable": true,
  "fiscalYearStartMonth": 0,
  "graphTooltip": 0,
  "id": 0,
  "links": [],
  "panels": [
    {
      "collapsed": false,
      "gridPos": {
        "h": 1,
        "w": 24,
        "x": 0,
        "y": 0
      },
      "id": 45,
      "panels": [],
      "title": "Faults",
      "type": "row"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${Cluster}"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [],
          "noValue": "0",
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": 0
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 4,
        "w": 3,
        "x": 0,
        "y": 1
      },
      "id": 47,
      "options": {
        "colorMode": "value",
        "graphMode": "none",
        "justifyMode": "auto",
        "orientation": "auto",
        "percentChangeColorMode": "standard",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": false
        },
        "showPercentChange": false,
        "textMode": "auto",
        "wideLayout": true
      },
      "pluginVersion": "12.3.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${Cluster}"
          },
          "editorMode": "code",
          "exemplar": true,
          "expr": "sum by (domain, severity, type) (ucs_faults_count{domain=~\"${domain}\",severity=~\"critical\",type=\"management\"})",
          "interval": "",
          "legendFormat": "{{domain}} {{severity}} {{type}}",
          "range": true,
          "refId": "A"
        }
      ],
      "title": "Critical Faults",
      "transparent": true,
      "type": "stat"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${Cluster}"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [],
          "noValue": "0",
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": 0
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 4,
        "w": 3,
        "x": 3,
        "y": 1
      },
      "id": 48,
      "options": {
        "colorMode": "value",
        "graphMode": "none",
        "justifyMode": "auto",
        "orientation": "auto",
        "percentChangeColorMode": "standard",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": false
        },
        "showPercentChange": false,
        "textMode": "auto",
        "wideLayout": true
      },
      "pluginVersion": "12.3.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${Cluster}"
          },
          "editorMode": "code",
          "exemplar": true,
          "expr": "sum by (domain, severity, type) (ucs_faults_count{domain=~\"${domain}\",severity=~\"major\",type=\"management\"})",
          "interval": "",
          "legendFormat": "{{domain}} {{severity}} {{type}}",
          "range": true,
          "refId": "A"
        }
      ],
      "title": "Major Faults",
      "transparent": true,
      "type": "stat"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${Cluster}"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [],
          "noValue": "0",
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": 0
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 4,
        "w": 3,
        "x": 6,
        "y": 1
      },
      "id": 49,
      "options": {
        "colorMode": "value",
        "graphMode": "none",
        "justifyMode": "auto",
        "orientation": "auto",
        "percentChangeColorMode": "standard",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": false
        },
        "showPercentChange": false,
        "textMode": "auto",
        "wideLayout": true
      },
      "pluginVersion": "12.3.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${Cluster}"
          },
          "editorMode": "code",
          "exemplar": true,
          "expr": "sum by (domain, severity, type) (ucs_faults_count{domain=~\"${domain}\",severity=~\"minor\",type=\"management\"})",
          "interval": "",
          "legendFormat": "{{domain}} {{severity}} {{type}}",
          "range": true,
          "refId": "A"
        }
      ],
      "title": "Minor Faults",
      "transparent": true,
      "type": "stat"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${Cluster}"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [],
          "noValue": "0",
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": 0
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 4,
        "w": 3,
        "x": 9,
        "y": 1
      },
      "id": 50,
      "options": {
        "colorMode": "value",
        "graphMode": "none",
        "justifyMode": "auto",
        "orientation": "auto",
        "percentChangeColorMode": "standard",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": false
        },
        "showPercentChange": false,
        "textMode": "auto",
        "wideLayout": true
      },
      "pluginVersion": "12.3.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${Cluster}"
          },
          "editorMode": "code",
          "exemplar": true,
          "expr": "sum by (domain, severity, type) (ucs_faults_count{domain=~\"${domain}\",severity=~\"warning\",type=\"management\"})",
          "interval": "",
          "legendFormat": "{{domain}} {{severity}} {{type}}",
          "range": true,
          "refId": "A"
        }
      ],
      "title": "Warning Faults",
      "transparent": true,
      "type": "stat"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${Cluster}"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisBorderShow": false,
            "axisCenteredZero": false,
            "axisColorMode": "text",
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "barWidthFactor": 0.6,
            "drawStyle": "line",
            "fillOpacity": 0,
            "gradientMode": "none",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "insertNulls": false,
            "lineInterpolation": "linear",
            "lineWidth": 1,
            "pointSize": 1,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "auto",
            "showValues": false,
            "spanNulls": false,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "mappings": [],
          "noValue": "0",
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": 0
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 4,
        "w": 11,
        "x": 13,
        "y": 1
      },
      "id": 51,
      "options": {
        "legend": {
          "calcs": [],
          "displayMode": "list",
          "placement": "bottom",
          "showLegend": true
        },
        "tooltip": {
          "hideZeros": false,
          "mode": "single",
          "sort": "none"
        }
      },
      "pluginVersion": "12.3.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${Cluster}"
          },
          "editorMode": "code",
          "exemplar": true,
          "expr": "sum by (severity) (ucs_faults_count{domain=~\"${domain}\",severity=~\"critical|major|minor|warning\",type=\"management\"})",
          "interval": "",
          "legendFormat": "{{domain}} {{severity}} {{type}}",
          "range": true,
          "refId": "A"
        }
      ],
      "title": "Faults",
      "transparent": true,
      "type": "timeseries"
    },
    {
      "collapsed": false,
      "gridPos": {
        "h": 1,
        "w": 24,
        "x": 0,
        "y": 5
      },
      "id": 39,
      "panels": [],
      "title": "Capacity",
      "type": "row"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${Cluster}"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "continuous-GrYlRd"
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": 0
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          },
          "unit": "percent"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 8,
        "w": 12,
        "x": 0,
        "y": 6
      },
      "id": 43,
      "options": {
        "displayMode": "basic",
        "legend": {
          "calcs": [],
          "displayMode": "list",
          "placement": "bottom",
          "showLegend": false
        },
        "maxVizHeight": 300,
        "minVizHeight": 16,
        "minVizWidth": 8,
        "namePlacement": "auto",
        "orientation": "horizontal",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": false
        },
        "showUnfilled": true,
        "sizing": "auto",
        "valueMode": "color"
      },
      "pluginVersion": "12.3.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${Cluster}"
          },
          "editorMode": "code",
          "exemplar": true,
          "expr": "(sum by (domain, class) (ucs_slots_equipped_count{domain=~\"${domain}\"}) / sum by (domain, class) (ucs_slots_count{domain=~\"${domain}\"})) * 100",
          "hide": false,
          "interval": "",
          "legendFormat": "{{domain}}",
          "range": true,
          "refId": "C"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${Cluster}"
          },
          "exemplar": true,
          "expr": "(sum by (class) (ucs_slots_equipped) / sum by (class) (ucs_slots_total)) * 100",
          "hide": false,
          "interval": "",
          "legendFormat": "All domains",
          "refId": "A"
        }
      ],
      "title": "Blade slots usage (percent)",
      "transparent": true,
      "type": "bargauge"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${Cluster}"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisBorderShow": false,
            "axisCenteredZero": false,
            "axisColorMode": "text",
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "barWidthFactor": 0.6,
            "drawStyle": "line",
            "fillOpacity": 0,
            "gradientMode": "opacity",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "insertNulls": false,
            "lineInterpolation": "linear",
            "lineWidth": 1,
            "pointSize": 1,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "auto",
            "showValues": false,
            "spanNulls": false,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": 0
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 8,
        "w": 12,
        "x": 12,
        "y": 6
      },
      "id": 41,
      "options": {
        "legend": {
          "calcs": [
            "max",
            "lastNotNull"
          ],
          "displayMode": "table",
          "placement": "bottom",
          "showLegend": true,
          "sortBy": "Last",
          "sortDesc": true
        },
        "tooltip": {
          "hideZeros": false,
          "mode": "single",
          "sort": "none"
        }
      },
      "pluginVersion": "12.3.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${Cluster}"
          },
          "editorMode": "code",
          "exemplar": true,
          "expr": "sum by (domain, class) (ucs_cpu_cores_count{domain=~\"${domain}\"})",
          "interval": "",
          "legendFormat": "{{domain}} {{class}} cores",
          "range": true,
          "refId": "A"
        }
      ],
      "title": "CPU cores count",
      "transparent": true,
      "type": "timeseries"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${Cluster}"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisBorderShow": false,
            "axisCenteredZero": false,
            "axisColorMode": "text",
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "barWidthFactor": 0.6,
            "drawStyle": "line",
            "fillOpacity": 0,
            "gradientMode": "opacity",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "insertNulls": false,
            "lineInterpolation": "linear",
            "lineWidth": 1,
            "pointSize": 1,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "auto",
            "showValues": false,
            "spanNulls": false,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": 0
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          },
          "unit": "decmbytes"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 8,
        "w": 12,
        "x": 0,
        "y": 14
      },
      "id": 42,
      "options": {
        "legend": {
          "calcs": [
            "max",
            "lastNotNull"
          ],
          "displayMode": "table",
          "placement": "bottom",
          "showLegend": true,
          "sortBy": "Last",
          "sortDesc": true
        },
        "tooltip": {
          "hideZeros": false,
          "mode": "single",
          "sort": "none"
        }
      },
      "pluginVersion": "12.3.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${Cluster}"
          },
          "editorMode": "code",
          "exemplar": true,
          "expr": "sum by (domain, class) (ucs_mem_megabytes{domain=~\"${domain}\"})",
          "interval": "",
          "legendFormat": "{{domain}} {{class}}s total ram",
          "range": true,
          "refId": "A"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${Cluster}"
          },
          "exemplar": true,
          "expr": "sum by (domain, class) (ucs_mem_available_total{domain=~\"${domain}\"})",
          "hide": false,
          "interval": "",
          "legendFormat": "{{domain}} {{class}}s available ram",
          "refId": "B"
        }
      ],
      "title": "Memory available",
      "transparent": true,
      "type": "timeseries"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${Cluster}"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisBorderShow": false,
            "axisCenteredZero": false,
            "axisColorMode": "text",
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "barWidthFactor": 0.6,
            "drawStyle": "line",
            "fillOpacity": 0,
            "gradientMode": "opacity",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "insertNulls": false,
            "lineInterpolation": "linear",
            "lineWidth": 1,
            "pointSize": 1,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "auto",
            "showValues": false,
            "spanNulls": false,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": 0
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 8,
        "w": 12,
        "x": 12,
        "y": 14
      },
      "id": 40,
      "options": {
        "legend": {
          "calcs": [
            "max",
            "last"
          ],
          "displayMode": "table",
          "placement": "bottom",
          "showLegend": true,
          "sortBy": "Last",
          "sortDesc": true
        },
        "tooltip": {
          "hideZeros": false,
          "mode": "single",
          "sort": "none"
        }
      },
      "pluginVersion": "12.3.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${Cluster}"
          },
          "editorMode": "code",
          "exemplar": true,
          "expr": "sum by (domain, class) (ucs_servers_count{domain=~\"${domain}\"})",
          "interval": "",
          "legendFormat": "{{domain}} {{class}}s",
          "range": true,
          "refId": "A"
        }
      ],
      "title": "Server count",
      "transparent": true,
      "type": "timeseries"
    },
    {
      "collapsed": false,
      "gridPos": {
        "h": 1,
        "w": 24,
        "x": 0,
        "y": 22
      },
      "id": 14,
      "panels": [],
      "title": "Network",
      "type": "row"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${Cluster}"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisBorderShow": false,
            "axisCenteredZero": false,
            "axisColorMode": "text",
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "barWidthFactor": 0.6,
            "drawStyle": "line",
            "fillOpacity": 0,
            "gradientMode": "none",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "insertNulls": false,
            "lineInterpolation": "linear",
            "lineWidth": 1,
            "pointSize": 1,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "auto",
            "showValues": false,
            "spanNulls": false,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": 0
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          },
          "unit": "bytes"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 8,
        "w": 12,
        "x": 0,
        "y": 23
      },
      "id": 8,
      "options": {
        "legend": {
          "calcs": [
            "min",
            "mean",
            "max"
          ],
          "displayMode": "table",
          "placement": "bottom",
          "showLegend": true,
          "sortBy": "Max",
          "sortDesc": false
        },
        "tooltip": {
          "hideZeros": false,
          "mode": "single",
          "sort": "none"
        }
      },
      "pluginVersion": "12.3.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${Cluster}"
          },
          "editorMode": "code",
          "exemplar": true,
          "expr": "sum by (domain, pc_label, pc_name) (rate(ucs_ether_stats_rx_bytes{domain=~\"${domain}\"}[10m]))",
          "interval": "",
          "legendFormat": "{{domain}} {{pc_label}} {{pc_name}}",
          "range": true,
          "refId": "A"
        }
      ],
      "title": "Ethernet bytes received",
      "transparent": true,
      "type": "timeseries"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${Cluster}"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisBorderShow": false,
            "axisCenteredZero": false,
            "axisColorMode": "text",
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "barWidthFactor": 0.6,
            "drawStyle": "line",
            "fillOpacity": 0,
            "gradientMode": "none",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "insertNulls": false,
            "lineInterpolation": "linear",
            "lineWidth": 1,
            "pointSize": 5,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "never",
            "showValues": false,
            "spanNulls": false,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": 0
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          },
          "unit": "bytes"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 8,
        "w": 12,
        "x": 12,
        "y": 23
      },
      "id": 21,
      "options": {
        "legend": {
          "calcs": [
            "min",
            "mean",
            "max"
          ],
          "displayMode": "table",
          "placement": "bottom",
          "showLegend": true
        },
        "tooltip": {
          "hideZeros": false,
          "mode": "single",
          "sort": "none"
        }
      },
      "pluginVersion": "12.3.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${Cluster}"
          },
          "editorMode": "code",
          "exemplar": true,
          "expr": "sum by (domain, pc_label, pc_name) (rate(ucs_ether_stats_tx_bytes{domain=~\"${domain}\"}[10m]))",
          "interval": "",
          "legendFormat": "{{domain}} {{pc_label}} {{pc_name}}",
          "range": true,
          "refId": "A"
        }
      ],
      "title": "Ethernet bytes transmitted",
      "transparent": true,
      "type": "timeseries"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${Cluster}"
      },
      "description": "",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisBorderShow": false,
            "axisCenteredZero": false,
            "axisColorMode": "text",
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "barWidthFactor": 0.6,
            "drawStyle": "line",
            "fillOpacity": 0,
            "gradientMode": "none",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "insertNulls": false,
            "lineInterpolation": "linear",
            "lineWidth": 1,
            "pointSize": 1,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "auto",
            "showValues": false,
            "spanNulls": false,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": 0
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          },
          "unit": "short"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 8,
        "w": 12,
        "x": 0,
        "y": 31
      },
      "id": 4,
      "options": {
        "legend": {
          "calcs": [
            "mean",
            "max"
          ],
          "displayMode": "table",
          "placement": "bottom",
          "showLegend": true,
          "sortBy": "Max",
          "sortDesc": true
        },
        "tooltip": {
          "hideZeros": false,
          "mode": "single",
          "sort": "none"
        }
      },
      "pluginVersion": "12.3.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${Cluster}"
          },
          "editorMode": "code",
          "exemplar": true,
          "expr": "sum by (domain, rack, chassis, blade) (rate(ucs_vnic_stats_rx_packets_count{domain=~\"${domain}\",chassis=~\"${chassis}\",rack=~\"${rack}\",blade=~\"${blade}\"}[10m]))",
          "interval": "",
          "legendFormat": "{{domain}}  {{rack}} {{chassis}} {{blade}}",
          "range": true,
          "refId": "A"
        }
      ],
      "title": "HBA Statistics for VNIC in Packets Received",
      "transparent": true,
      "type": "timeseries"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${Cluster}"
      },
      "description": "",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisBorderShow": false,
            "axisCenteredZero": false,
            "axisColorMode": "text",
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "barWidthFactor": 0.6,
            "drawStyle": "line",
            "fillOpacity": 0,
            "gradientMode": "none",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "insertNulls": false,
            "lineInterpolation": "linear",
            "lineWidth": 1,
            "pointSize": 1,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "auto",
            "showValues": false,
            "spanNulls": false,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": 0
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          },
          "unit": "short"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 8,
        "w": 12,
        "x": 12,
        "y": 31
      },
      "id": 22,
      "options": {
        "legend": {
          "calcs": [
            "mean",
            "max"
          ],
          "displayMode": "table",
          "placement": "bottom",
          "showLegend": true,
          "sortBy": "Max",
          "sortDesc": true
        },
        "tooltip": {
          "hideZeros": false,
          "mode": "single",
          "sort": "none"
        }
      },
      "pluginVersion": "12.3.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${Cluster}"
          },
          "editorMode": "code",
          "exemplar": true,
          "expr": "sum by (domain, rack, chassis, blade) (rate(ucs_vnic_stats_tx_packets_count{domain=~\"${domain}\",chassis=~\"${chassis}\",rack=~\"${rack}\",blade=~\"${blade}\"}[10m]))",
          "interval": "",
          "legendFormat": "{{domain}}  {{rack}} {{chassis}} {{blade}}",
          "range": true,
          "refId": "A"
        }
      ],
      "title": "HBA Statistics for VNIC in Packets Transmitted",
      "transparent": true,
      "type": "timeseries"
    },
    {
      "collapsed": false,
      "gridPos": {
        "h": 1,
        "w": 24,
        "x": 0,
        "y": 39
      },
      "id": 16,
      "panels": [],
      "title": "Temperature / Fan speed",
      "type": "row"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${Cluster}"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisBorderShow": false,
            "axisCenteredZero": false,
            "axisColorMode": "text",
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "barWidthFactor": 0.6,
            "drawStyle": "line",
            "fillOpacity": 0,
            "gradientMode": "none",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "insertNulls": false,
            "lineInterpolation": "linear",
            "lineWidth": 1,
            "pointSize": 1,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "auto",
            "showValues": false,
            "spanNulls": false,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": 0
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          },
          "unit": "celsius"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 8,
        "w": 12,
        "x": 0,
        "y": 40
      },
      "id": 11,
      "options": {
        "legend": {
          "calcs": [
            "max",
            "lastNotNull"
          ],
          "displayMode": "table",
          "placement": "bottom",
          "showLegend": true,
          "sortBy": "Last *",
          "sortDesc": true
        },
        "tooltip": {
          "hideZeros": false,
          "mode": "single",
          "sort": "none"
        }
      },
      "pluginVersion": "12.3.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${Cluster}"
          },
          "editorMode": "code",
          "exemplar": true,
          "expr": "max by (domain, chassis, rack, blade) (max_over_time(ucs_server_temperature_celsius{domain=~\"${domain}\",chassis=~\"${chassis}\",rack=~\"${rack}\",blade=~\"${blade}\"}[10m]))",
          "interval": "",
          "legendFormat": "{{domain}} {{chassis}} {{rack}} {{blade}}",
          "range": true,
          "refId": "A"
        }
      ],
      "title": "Temperature",
      "transparent": true,
      "type": "timeseries"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${Cluster}"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisBorderShow": false,
            "axisCenteredZero": false,
            "axisColorMode": "text",
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "barWidthFactor": 0.6,
            "drawStyle": "line",
            "fillOpacity": 0,
            "gradientMode": "opacity",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "insertNulls": false,
            "lineInterpolation": "linear",
            "lineWidth": 1,
            "pointSize": 1,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "auto",
            "showValues": false,
            "spanNulls": false,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": 0
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          },
          "unit": "rotrpm"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 8,
        "w": 12,
        "x": 12,
        "y": 40
      },
      "id": 20,
      "options": {
        "legend": {
          "calcs": [
            "mean",
            "max"
          ],
          "displayMode": "table",
          "placement": "bottom",
          "showLegend": true,
          "sortBy": "Max",
          "sortDesc": true
        },
        "tooltip": {
          "hideZeros": false,
          "mode": "single",
          "sort": "none"
        }
      },
      "pluginVersion": "12.3.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${Cluster}"
          },
          "editorMode": "code",
          "exemplar": true,
          "expr": "max by (domain, chassis) (avg_over_time(ucs_fan_speed_rpm{domain=~\"${domain}\",chassis=~\"${chassis}\"}[10m]))",
          "interval": "",
          "legendFormat": "{{domain}} {{chassis}}",
          "range": true,
          "refId": "A"
        }
      ],
      "title": "Fan speed",
      "transparent": true,
      "type": "timeseries"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${Cluster}"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "continuous-GrYlRd"
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": 0
              }
            ]
          },
          "unit": "celsius"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 10,
        "w": 24,
        "x": 0,
        "y": 48
      },
      "id": 37,
      "options": {
        "displayMode": "basic",
        "legend": {
          "calcs": [],
          "displayMode": "list",
          "placement": "bottom",
          "showLegend": false
        },
        "maxVizHeight": 300,
        "minVizHeight": 16,
        "minVizWidth": 8,
        "namePlacement": "auto",
        "orientation": "horizontal",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": false
        },
        "showUnfilled": true,
        "sizing": "auto",
        "text": {},
        "valueMode": "color"
      },
      "pluginVersion": "12.3.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${Cluster}"
          },
          "editorMode": "code",
          "exemplar": true,
          "expr": "max by (domain, chassis, rack, blade) (ucs_server_temperature_celsius{domain=~\"${domain}\",chassis=~\"${chassis}\",rack=~\"${rack}\",blade=~\"${blade}\"})",
          "format": "time_series",
          "interval": "",
          "legendFormat": "{{domain}} {{chassis}} {{rack}} {{blade}}",
          "range": true,
          "refId": "A"
        }
      ],
      "title": "Temperature",
      "transparent": true,
      "type": "bargauge"
    },
    {
      "collapsed": false,
      "gridPos": {
        "h": 1,
        "w": 24,
        "x": 0,
        "y": 58
      },
      "id": 26,
      "panels": [],
      "title": "System software",
      "type": "row"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${Cluster}"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisBorderShow": false,
            "axisCenteredZero": false,
            "axisColorMode": "text",
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "barWidthFactor": 0.6,
            "drawStyle": "line",
            "fillOpacity": 0,
            "gradientMode": "none",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "insertNulls": false,
            "lineInterpolation": "linear",
            "lineWidth": 1,
            "pointSize": 1,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "auto",
            "showValues": false,
            "spanNulls": false,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": 0
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          },
          "unit": "percentunit"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 8,
        "w": 12,
        "x": 0,
        "y": 59
      },
      "id": 28,
      "options": {
        "legend": {
          "calcs": [
            "mean",
            "max"
          ],
          "displayMode": "table",
          "placement": "bottom",
          "showLegend": true,
          "sortBy": "Max",
          "sortDesc": true
        },
        "tooltip": {
          "hideZeros": false,
          "mode": "single",
          "sort": "none"
        }
      },
      "pluginVersion": "12.3.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${Cluster}"
          },
          "editorMode": "code",
          "exemplar": true,
          "expr": "avg by (domain, switch) (avg_over_time(ucs_cpu_load_ratio{domain=~\"${domain}\"}[10m]))",
          "interval": "",
          "legendFormat": "{{domain}} {{switch}}",
          "range": true,
          "refId": "A"
        }
      ],
      "title": "User CPU load",
      "transparent": true,
      "type": "timeseries"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${Cluster}"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisBorderShow": false,
            "axisCenteredZero": false,
            "axisColorMode": "text",
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "barWidthFactor": 0.6,
            "drawStyle": "line",
            "fillOpacity": 0,
            "gradientMode": "none",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "insertNulls": false,
            "lineInterpolation": "linear",
            "lineWidth": 1,
            "pointSize": 1,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "auto",
            "showValues": false,
            "spanNulls": false,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": 0
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          },
          "unit": "percent"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 8,
        "w": 12,
        "x": 12,
        "y": 59
      },
      "id": 30,
      "options": {
        "legend": {
          "calcs": [
            "lastNotNull",
            "max",
            "mean"
          ],
          "displayMode": "table",
          "placement": "bottom",
          "showLegend": true,
          "sortBy": "Max",
          "sortDesc": true
        },
        "tooltip": {
          "hideZeros": false,
          "mode": "single",
          "sort": "none"
        }
      },
      "pluginVersion": "12.3.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${Cluster}"
          },
          "editorMode": "code",
          "exemplar": true,
          "expr": "(100 * avg by (domain, switch) (avg_over_time(ucs_kernel_mem_free_megabytes{domain=~\"${domain}\"}[10m])) / avg by (domain, switch) (avg_over_time(ucs_kernel_mem_total_megabytes[10m])))",
          "interval": "",
          "legendFormat": "{{domain }} {{switch}}",
          "range": true,
          "refId": "A"
        }
      ],
      "title": "Kernel Memory Usage Percent",
      "transparent": true,
      "type": "timeseries"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${Cluster}"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisBorderShow": false,
            "axisCenteredZero": false,
            "axisColorMode": "text",
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "barWidthFactor": 0.6,
            "drawStyle": "line",
            "fillOpacity": 0,
            "gradientMode": "none",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "insertNulls": false,
            "lineInterpolation": "linear",
            "lineWidth": 1,
            "pointSize": 1,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "auto",
            "showValues": false,
            "spanNulls": false,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": 0
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          },
          "unit": "decmbytes"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 8,
        "w": 12,
        "x": 0,
        "y": 67
      },
      "id": 33,
      "options": {
        "legend": {
          "calcs": [
            "lastNotNull",
            "max",
            "mean"
          ],
          "displayMode": "table",
          "placement": "bottom",
          "showLegend": true,
          "sortBy": "Last *",
          "sortDesc": false
        },
        "tooltip": {
          "hideZeros": false,
          "mode": "single",
          "sort": "none"
        }
      },
      "pluginVersion": "12.3.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${Cluster}"
          },
          "editorMode": "code",
          "exemplar": true,
          "expr": "avg by (domain, switch) (avg_over_time(ucs_mem_available_megabytes{domain=~\"${domain}\"}[10m]))",
          "interval": "",
          "legendFormat": "{{domain }} {{switch}}",
          "range": true,
          "refId": "A"
        }
      ],
      "title": "Memory available",
      "transparent": true,
      "type": "timeseries"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${Cluster}"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisBorderShow": false,
            "axisCenteredZero": false,
            "axisColorMode": "text",
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "barWidthFactor": 0.6,
            "drawStyle": "line",
            "fillOpacity": 0,
            "gradientMode": "none",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "insertNulls": false,
            "lineInterpolation": "linear",
            "lineWidth": 1,
            "pointSize": 1,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "auto",
            "showValues": false,
            "spanNulls": false,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": 0
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          },
          "unit": "decmbytes"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 8,
        "w": 12,
        "x": 12,
        "y": 67
      },
      "id": 34,
      "options": {
        "legend": {
          "calcs": [
            "lastNotNull",
            "max",
            "mean"
          ],
          "displayMode": "table",
          "placement": "bottom",
          "showLegend": true,
          "sortBy": "Last *",
          "sortDesc": false
        },
        "tooltip": {
          "hideZeros": false,
          "mode": "single",
          "sort": "none"
        }
      },
      "pluginVersion": "12.3.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${Cluster}"
          },
          "editorMode": "code",
          "exemplar": true,
          "expr": "avg by (domain, switch) (avg_over_time(ucs_mem_cached_megabytes{domain=~\"${domain}\"}[10m]))",
          "interval": "",
          "legendFormat": "{{domain }} {{switch}}",
          "range": true,
          "refId": "A"
        }
      ],
      "title": "Memory cached",
      "transparent": true,
      "type": "timeseries"
    },
    {
      "collapsed": false,
      "gridPos": {
        "h": 1,
        "w": 24,
        "x": 0,
        "y": 75
      },
      "id": 24,
      "panels": [],
      "title": "Memory errors",
      "type": "row"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${Cluster}"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisBorderShow": false,
            "axisCenteredZero": false,
            "axisColorMode": "text",
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "barWidthFactor": 0.6,
            "drawStyle": "line",
            "fillOpacity": 35,
            "gradientMode": "none",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "insertNulls": false,
            "lineInterpolation": "linear",
            "lineWidth": 1,
            "pointSize": 1,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "auto",
            "showValues": false,
            "spanNulls": false,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": 0
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 8,
        "w": 24,
        "x": 0,
        "y": 76
      },
      "id": 36,
      "options": {
        "legend": {
          "calcs": [
            "lastNotNull"
          ],
          "displayMode": "table",
          "placement": "bottom",
          "showLegend": true,
          "sortBy": "Last *",
          "sortDesc": true
        },
        "tooltip": {
          "hideZeros": false,
          "mode": "single",
          "sort": "none"
        }
      },
      "pluginVersion": "12.3.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${Cluster}"
          },
          "editorMode": "code",
          "exemplar": true,
          "expr": "sum by (domain, rack, chassis, blade) (ucs_address_parity_errors_count{domain=~\"${domain}\",chassis=~\"${chassis}\",rack=~\"${rack}\",blade=~\"${blade}\"})",
          "interval": "",
          "intervalFactor": 1,
          "legendFormat": "{{domain}}  {{rack}} {{chassis}} {{blade}}",
          "range": true,
          "refId": "A"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${Cluster}"
          },
          "exemplar": true,
          "expr": "sum by (domain, rack, chassis, blade) (ucs_ecc_singlebit_errors{domain=~\"${domain}\",chassis=~\"${chassis}\",rack=~\"${rack}\",blade=~\"${blade}\"})",
          "hide": false,
          "interval": "",
          "intervalFactor": 1,
          "legendFormat": "{{domain}}  {{rack}} {{chassis}} {{blade}} ecc_singlebit_errors ",
          "refId": "B"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${Cluster}"
          },
          "exemplar": true,
          "expr": "sum by (domain, rack, chassis, blade) (ucs_ecc_multibit_errors{domain=~\"${domain}\",chassis=~\"${chassis}\",rack=~\"${rack}\",blade=~\"${blade}\"})",
          "hide": false,
          "interval": "",
          "legendFormat": "{{domain}}  {{rack}} {{chassis}} {{blade}} ecc_multibit_errors",
          "refId": "C"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${Cluster}"
          },
          "exemplar": true,
          "expr": "sum by (domain, rack, chassis, blade) (ucs_mismatch_errors{domain=~\"${domain}\",chassis=~\"${chassis}\",rack=~\"${rack}\",blade=~\"${blade}\"})",
          "hide": false,
          "interval": "",
          "legendFormat": "{{domain}}  {{rack}} {{chassis}} {{blade}} mismatch_errors",
          "refId": "D"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${Cluster}"
          },
          "exemplar": true,
          "expr": "sum by (domain, rack, chassis, blade) (ucs_dram_write_data_correctable_crc_errors{domain=~\"${domain}\",chassis=~\"${chassis}\",rack=~\"${rack}\",blade=~\"${blade}\"})",
          "hide": false,
          "interval": "",
          "legendFormat": "{{domain}}  {{rack}} {{chassis}} {{blade}} dram_write_data_correctable_crc_errors",
          "refId": "E"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${Cluster}"
          },
          "exemplar": true,
          "expr": "sum by (domain, rack, chassis, blade) (ucs_dram_write_data_un_correctable_crc_errors{domain=~\"${domain}\",chassis=~\"${chassis}\",rack=~\"${rack}\",blade=~\"${blade}\"})",
          "hide": false,
          "interval": "",
          "legendFormat": "{{domain}}  {{rack}} {{chassis}} {{blade}} dram_write_data_un_correctable_crc_errors",
          "refId": "F"
        }
      ],
      "title": "Memory errors",
      "transparent": true,
      "type": "timeseries"
    },
    {
      "collapsed": false,
      "gridPos": {
        "h": 1,
        "w": 24,
        "x": 0,
        "y": 84
      },
      "id": 18,
      "panels": [],
      "title": "Power consumption",
      "type": "row"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${Cluster}"
      },
      "description": "",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisBorderShow": false,
            "axisCenteredZero": false,
            "axisColorMode": "text",
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "barWidthFactor": 0.6,
            "drawStyle": "line",
            "fillOpacity": 0,
            "gradientMode": "none",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "insertNulls": false,
            "lineInterpolation": "linear",
            "lineWidth": 1,
            "pointSize": 1,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "auto",
            "showValues": false,
            "spanNulls": false,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": 0
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          },
          "unit": "amp"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 8,
        "w": 12,
        "x": 0,
        "y": 85
      },
      "id": 10,
      "options": {
        "legend": {
          "calcs": [
            "min",
            "max",
            "lastNotNull"
          ],
          "displayMode": "table",
          "placement": "bottom",
          "showLegend": true,
          "sortBy": "Last *",
          "sortDesc": true
        },
        "tooltip": {
          "hideZeros": false,
          "mode": "single",
          "sort": "none"
        }
      },
      "pluginVersion": "12.3.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${Cluster}"
          },
          "editorMode": "code",
          "exemplar": true,
          "expr": "sum by (domain, chassis, blade) (ucs_compute_mb_input_current_amperes{domain=~\"${domain}\",chassis=~\"${chassis}\",rack=~\"${rack}\",blade=~\"${blade}\"})",
          "interval": "",
          "legendFormat": "{{domain}} {{chassis}} {{blade}}",
          "range": true,
          "refId": "A"
        }
      ],
      "title": "Input current (A)",
      "transparent": true,
      "type": "timeseries"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${Cluster}"
      },
      "description": "",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisBorderShow": false,
            "axisCenteredZero": false,
            "axisColorMode": "text",
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "barWidthFactor": 0.6,
            "drawStyle": "line",
            "fillOpacity": 0,
            "gradientMode": "none",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "insertNulls": false,
            "lineInterpolation": "linear",
            "lineWidth": 1,
            "pointSize": 5,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "never",
            "showValues": false,
            "spanNulls": false,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": 0
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          },
          "unit": "watt"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 8,
        "w": 12,
        "x": 12,
        "y": 85
      },
      "id": 12,
      "options": {
        "legend": {
          "calcs": [
            "min",
            "mean",
            "max"
          ],
          "displayMode": "table",
          "placement": "bottom",
          "showLegend": true,
          "sortBy": "Max",
          "sortDesc": true
        },
        "tooltip": {
          "hideZeros": false,
          "mode": "single",
          "sort": "none"
        }
      },
      "pluginVersion": "12.3.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${Cluster}"
          },
          "editorMode": "code",
          "exemplar": true,
          "expr": "max by (domain, chassis) (max_over_time(ucs_compute_mb_consumed_power_watts{domain=~\"${domain}\",chassis=~\"${chassis}\",blade=~\"${blade}\",rack=~\"${rack}\"}[10m]))",
          "interval": "",
          "legendFormat": "{{domain}} {{chassis}}",
          "range": true,
          "refId": "A"
        }
      ],
      "title": "Power consumed (Watts)",
      "transparent": true,
      "type": "timeseries"
    }
  ],
  "preload": false,
  "refresh": "1m",
  "schemaVersion": 42,
  "tags": [],
  "templating": {
    "list": [
      {
        "current": {
          "text": "prometheus",
          "value": "cf5j7d42byqyoc"
        },
        "includeAll": false,
        "name": "Cluster",
        "options": [],
        "query": "prometheus",
        "refresh": 1,
        "regex": "",
        "type": "datasource"
      },
      {
        "allValue": ".+",
        "current": {
          "text": "All",
          "value": "$__all"
        },
        "datasource": {
          "type": "prometheus",
          "uid": "${Cluster}"
        },
        "definition": "label_values(ucs_vnic_stats_rx, domain)",
        "includeAll": true,
        "name": "domain",
        "options": [],
        "query": {
          "query": "label_values(ucs_vnic_stats_rx, domain)",
          "refId": "StandardVariableQuery"
        },
        "refresh": 2,
        "regex": "/^[-a-zA-Z0-9]*$/",
        "sort": 1,
        "type": "query"
      },
      {
        "allValue": ".+",
        "current": {
          "text": "All",
          "value": "$__all"
        },
        "datasource": {
          "type": "prometheus",
          "uid": "${Cluster}"
        },
        "definition": "label_values(ucs_vnic_stats_rx, rack)",
        "includeAll": true,
        "name": "rack",
        "options": [],
        "query": {
          "query": "label_values(ucs_vnic_stats_rx, rack)",
          "refId": "StandardVariableQuery"
        },
        "refresh": 2,
        "regex": "",
        "sort": 3,
        "type": "query"
      },
      {
        "allValue": ".+",
        "current": {
          "text": "All",
          "value": "$__all"
        },
        "datasource": {
          "type": "prometheus",
          "uid": "${Cluster}"
        },
        "definition": "label_values(ucs_vnic_stats_rx, chassis)",
        "includeAll": true,
        "name": "chassis",
        "options": [],
        "query": {
          "query": "label_values(ucs_vnic_stats_rx, chassis)",
          "refId": "StandardVariableQuery"
        },
        "refresh": 2,
        "regex": "",
        "sort": 3,
        "type": "query"
      },
      {
        "allValue": ".+",
        "current": {
          "text": "All",
          "value": "$__all"
        },
        "datasource": {
          "type": "prometheus",
          "uid": "${Cluster}"
        },
        "definition": "label_values(ucs_vnic_stats_rx, blade)",
        "includeAll": true,
        "multi": true,
        "name": "blade",
        "options": [],
        "query": {
          "query": "label_values(ucs_vnic_stats_rx, blade)",
          "refId": "StandardVariableQuery"
        },
        "refresh": 2,
        "regex": "",
        "sort": 3,
        "type": "query"
      }
    ]
  },
  "time": {
    "from": "now-3h",
    "to": "now"
  },
  "timepicker": {},
  "timezone": "",
  "title": "Cisco UCS",
  "uid": "BXG5Mes7z",
  "version": 20
}
