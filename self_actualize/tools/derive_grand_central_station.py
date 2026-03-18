# CRYSTAL: Xi108:W2:A11:S29 | face=F | node=423 | depth=2 | phase=Mutable
# METRO: Me
# BRIDGES: Xi108:W2:A11:S28→Xi108:W2:A11:S30→Xi108:W1:A11:S29→Xi108:W3:A11:S29→Xi108:W2:A10:S29→Xi108:W2:A12:S29

from pathlib import Path
import sys

WORKSPACE_ROOT = Path(__file__).resolve().parents[2]
if str(WORKSPACE_ROOT) not in sys.path:
    sys.path.insert(0, str(WORKSPACE_ROOT))

from self_actualize.runtime.derive_grand_central_station import main

if __name__ == "__main__":
    raise SystemExit(main())
