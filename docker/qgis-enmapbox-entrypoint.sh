#!/usr/bin/env bash
set -euo pipefail

profile_name="${QGIS_PROFILE:-EnMAP-Box}"

if [[ "$#" -eq 0 || "${1}" == "qgis" ]]; then
    if [[ "$#" -gt 0 ]]; then
        shift
    fi

    exec qgis --profile "${profile_name}" "$@"
fi

exec "$@"
