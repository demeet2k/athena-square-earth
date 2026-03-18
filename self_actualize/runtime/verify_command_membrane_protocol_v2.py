# CRYSTAL: Xi108:W2:A10:S28 | face=F | node=396 | depth=2 | phase=Mutable
# METRO: Me,Cc
# BRIDGES: Xi108:W2:A10:S27→Xi108:W2:A10:S29→Xi108:W1:A10:S28→Xi108:W3:A10:S28→Xi108:W2:A9:S28→Xi108:W2:A11:S28

from __future__ import annotations

import json
import sys
from pathlib import Path

if __package__ in {None, ""}:
    ROOT = Path(__file__).resolve().parents[2]
    if str(ROOT) not in sys.path:
        sys.path.insert(0, str(ROOT))
    from self_actualize.runtime.verify_command_membrane_protocol import verify_command_membrane_protocol
else:
    from .verify_command_membrane_protocol import verify_command_membrane_protocol

def main() -> int:
    result = verify_command_membrane_protocol()
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0 if result.get("truth") == "OK" else 1

if __name__ == "__main__":
    raise SystemExit(main())
