# CRYSTAL: Xi108:W2:A7:S25 | face=F | node=304 | depth=2 | phase=Mutable
# METRO: Me,T
# BRIDGES: Xi108:W2:A7:S24→Xi108:W2:A7:S26→Xi108:W1:A7:S25→Xi108:W3:A7:S25→Xi108:W2:A6:S25→Xi108:W2:A8:S25

from __future__ import annotations

import sys
from pathlib import Path

WORKSPACE_ROOT = Path(__file__).resolve().parents[2]
if str(WORKSPACE_ROOT) not in sys.path:
    sys.path.insert(0, str(WORKSPACE_ROOT))

from self_actualize.runtime.derive_void_ch11_ok_theorem import main  # noqa: E402

if __name__ == "__main__":
    raise SystemExit(main())
