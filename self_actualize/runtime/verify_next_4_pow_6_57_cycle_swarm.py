# CRYSTAL: Xi108:W2:A5:S30 | face=F | node=459 | depth=2 | phase=Mutable
# METRO: Wr,Me
# BRIDGES: Xi108:W2:A5:S29→Xi108:W2:A5:S31→Xi108:W1:A5:S30→Xi108:W3:A5:S30→Xi108:W2:A4:S30→Xi108:W2:A6:S30

from __future__ import annotations

import json

from .canonical_four_agent_57_loop import verify_canonical_four_agent_57_loop

def main() -> int:
    result = verify_canonical_four_agent_57_loop()
    print(json.dumps(result, indent=2))
    return 0 if result.get("truth") == "OK" else 1

if __name__ == "__main__":
    raise SystemExit(main())
