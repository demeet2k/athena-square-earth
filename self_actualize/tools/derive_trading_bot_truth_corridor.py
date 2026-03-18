# CRYSTAL: Xi108:W2:A5:S29 | face=F | node=428 | depth=2 | phase=Mutable
# METRO: Me,T
# BRIDGES: Xi108:W2:A5:S28→Xi108:W2:A5:S30→Xi108:W1:A5:S29→Xi108:W3:A5:S29→Xi108:W2:A4:S29→Xi108:W2:A6:S29

from __future__ import annotations

import sys
from pathlib import Path

WORKSPACE_ROOT = Path(__file__).resolve().parents[2]
if str(WORKSPACE_ROOT) not in sys.path:
    sys.path.insert(0, str(WORKSPACE_ROOT))

from self_actualize.runtime.derive_trading_bot_truth_corridor import main  # noqa: E402

if __name__ == "__main__":
    raise SystemExit(main())
