#!/usr/bin/env python3
"""Minimal EnMAP-Box smoke test for the Docker image."""

from __future__ import annotations

import os
import sys
from pathlib import Path

PLUGIN_ROOT = Path(
    os.environ.get(
        "ENMAPBOX_PLUGIN_ROOT",
        "/home/enmapbox/.local/share/QGIS/QGIS3/profiles/EnMAP-Box/python/plugins/enmapboxplugin",
    )
)

if str(PLUGIN_ROOT) not in sys.path:
    sys.path.insert(0, str(PLUGIN_ROOT))

from enmapbox.testing import start_app
from enmapbox import initAll
from enmapbox.gui.enmapboxgui import EnMAPBox


def main() -> int:
    app = start_app()
    initAll()
    enmapbox = EnMAPBox(None)
    print("EnMAP-Box initialized successfully")
    print(f"Plugin root: {PLUGIN_ROOT}")
    print(f"Instance type: {type(enmapbox).__name__}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

