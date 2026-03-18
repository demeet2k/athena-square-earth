# CRYSTAL: Xi108:W2:A10:S25 | face=F | node=310 | depth=2 | phase=Mutable
# METRO: Me,Cc
# BRIDGES: Xi108:W2:A10:S24→Xi108:W2:A10:S26→Xi108:W1:A10:S25→Xi108:W3:A10:S25→Xi108:W2:A9:S25→Xi108:W2:A11:S25

from __future__ import annotations

import sys
from pathlib import Path

if __package__ in {None, ""}:
    ROOT = Path(__file__).resolve().parents[2]
    if str(ROOT) not in sys.path:
        sys.path.insert(0, str(ROOT))
    from self_actualize.runtime.command_membrane_entrypoint import main
else:
    from .command_membrane_entrypoint import main

if __name__ == "__main__":
    raise SystemExit(main())
