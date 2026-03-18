# CRYSTAL: Xi108:W2:A12:S30 | face=F | node=465 | depth=2 | phase=Mutable
# METRO: Me
# BRIDGES: Xi108:W2:A12:S29→Xi108:W2:A12:S31→Xi108:W1:A12:S30→Xi108:W3:A12:S30→Xi108:W2:A11:S30

from __future__ import annotations

import sys
from pathlib import Path

WORKSPACE_ROOT = Path(__file__).resolve().parents[2]
if str(WORKSPACE_ROOT) not in sys.path:
    sys.path.insert(0, str(WORKSPACE_ROOT))

from self_actualize.runtime.derive_adventurer_quest_loop import main  # noqa: E402

if __name__ == "__main__":
    raise SystemExit(main())
