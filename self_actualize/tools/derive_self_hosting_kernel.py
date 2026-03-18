# CRYSTAL: Xi108:W2:A1:S30 | face=F | node=465 | depth=2 | phase=Mutable
# METRO: Me
# BRIDGES: Xi108:W2:A1:S29→Xi108:W2:A1:S31→Xi108:W1:A1:S30→Xi108:W3:A1:S30→Xi108:W2:A2:S30

from pathlib import Path
import sys

WORKSPACE_ROOT = Path(__file__).resolve().parents[2]
if str(WORKSPACE_ROOT) not in sys.path:
    sys.path.insert(0, str(WORKSPACE_ROOT))

from self_actualize.runtime.derive_self_hosting_kernel import main

if __name__ == "__main__":
    raise SystemExit(main())
