# CRYSTAL: Xi108:W2:A3:S27 | face=F | node=360 | depth=2 | phase=Mutable
# METRO: Me,Bw,✶
# BRIDGES: Xi108:W2:A3:S26→Xi108:W2:A3:S28→Xi108:W1:A3:S27→Xi108:W3:A3:S27→Xi108:W2:A2:S27→Xi108:W2:A4:S27

from __future__ import annotations

import sys
from pathlib import Path

WORKSPACE_ROOT = Path(__file__).resolve().parents[2]
if str(WORKSPACE_ROOT) not in sys.path:
    sys.path.insert(0, str(WORKSPACE_ROOT))

from self_actualize.runtime.derive_qshrink_connectivity_fractal import main  # noqa: E402

if __name__ == "__main__":
    raise SystemExit(main())
