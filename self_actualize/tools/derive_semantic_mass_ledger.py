# CRYSTAL: Xi108:W2:A4:S28 | face=F | node=390 | depth=2 | phase=Mutable
# METRO: Me
# BRIDGES: Xi108:W2:A4:S27→Xi108:W2:A4:S29→Xi108:W1:A4:S28→Xi108:W3:A4:S28→Xi108:W2:A3:S28→Xi108:W2:A5:S28

from __future__ import annotations

import sys
from pathlib import Path

WORKSPACE_ROOT = Path(__file__).resolve().parents[2]
if str(WORKSPACE_ROOT) not in sys.path:
    sys.path.insert(0, str(WORKSPACE_ROOT))

from self_actualize.runtime.derive_semantic_mass_ledger import main  # noqa: E402

if __name__ == "__main__":
    raise SystemExit(main())
