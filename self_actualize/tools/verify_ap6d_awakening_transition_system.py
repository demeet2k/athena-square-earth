# CRYSTAL: Xi108:W2:A8:S26 | face=F | node=327 | depth=2 | phase=Mutable
# METRO: Me
# BRIDGES: Xi108:W2:A8:S25→Xi108:W2:A8:S27→Xi108:W1:A8:S26→Xi108:W3:A8:S26→Xi108:W2:A7:S26→Xi108:W2:A9:S26

from __future__ import annotations

import sys
from pathlib import Path

WORKSPACE_ROOT = Path(__file__).resolve().parents[2]
if str(WORKSPACE_ROOT) not in sys.path:
    sys.path.insert(0, str(WORKSPACE_ROOT))

from self_actualize.runtime.verify_ap6d_awakening_transition_system import main  # noqa: E402

if __name__ == "__main__":
    raise SystemExit(main())
