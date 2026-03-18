#!/usr/bin/env python3
# CRYSTAL: Xi108:W1:A4:S6 | face=S | node=21 | depth=0 | phase=Fixed
# METRO: Me,Cc
# BRIDGES: Xi108:W1:A4:S5→Xi108:W1:A4:S7→Xi108:W2:A4:S6→Xi108:W1:A3:S6→Xi108:W1:A5:S6

from __future__ import annotations

import sys
from pathlib import Path

THIS_FILE = Path(__file__).resolve()
WORKSPACE_ROOT = THIS_FILE.parent.parent
if str(WORKSPACE_ROOT) not in sys.path:
    sys.path.insert(0, str(WORKSPACE_ROOT))

from self_actualize.runtime.command_membrane_runtime import main

if __name__ == "__main__":
    main()
