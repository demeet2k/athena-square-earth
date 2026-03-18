# CRYSTAL: Xi108:W2:A1:S25 | face=F | node=302 | depth=2 | phase=Mutable
# METRO: Me
# BRIDGES: Xi108:W2:A1:S24→Xi108:W2:A1:S26→Xi108:W1:A1:S25→Xi108:W3:A1:S25→Xi108:W2:A2:S25

from __future__ import annotations

import sys
from pathlib import Path

WORKSPACE_ROOT = Path(__file__).resolve().parents[2]
if str(WORKSPACE_ROOT) not in sys.path:
    sys.path.insert(0, str(WORKSPACE_ROOT))

from self_actualize.runtime.derive_bruno_b12_operator_table import main  # noqa: E402

if __name__ == "__main__":
    raise SystemExit(main())
