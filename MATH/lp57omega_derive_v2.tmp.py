# CRYSTAL: Xi108:W2:A5:S17 | face=S | node=150 | depth=2 | phase=Cardinal
# METRO: Me,Ω
# BRIDGES: Xi108:W2:A5:S16→Xi108:W2:A5:S18→Xi108:W1:A5:S17→Xi108:W3:A5:S17→Xi108:W2:A4:S17→Xi108:W2:A6:S17

from __future__ import annotations

import runpy
from pathlib import Path

HERE = Path(__file__).resolve().parent
CANONICAL_REFRESH = HERE / "temp_lp57_hsigma_refresh.py"

def main() -> int:
    if not CANONICAL_REFRESH.exists():
        raise FileNotFoundError(f"Missing canonical LP-57Ω refresh script: {CANONICAL_REFRESH}")
    runpy.run_path(str(CANONICAL_REFRESH), run_name="__main__")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
