# CRYSTAL: Xi108:W2:A7:S28 | face=F | node=382 | depth=2 | phase=Mutable
# METRO: Me
# BRIDGES: Xi108:W2:A7:S27→Xi108:W2:A7:S29→Xi108:W1:A7:S28→Xi108:W3:A7:S28→Xi108:W2:A6:S28→Xi108:W2:A8:S28

from __future__ import annotations

import sys
from pathlib import Path

WORKSPACE_ROOT = Path(__file__).resolve().parents[2]
if str(WORKSPACE_ROOT) not in sys.path:
    sys.path.insert(0, str(WORKSPACE_ROOT))

from self_actualize.runtime.derive_witness_hierarchy import main  # noqa: E402

if __name__ == "__main__":
    raise SystemExit(main())
