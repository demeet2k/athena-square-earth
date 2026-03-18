# CRYSTAL: Xi108:W2:A3:S27 | face=F | node=366 | depth=2 | phase=Mutable
# METRO: Me
# BRIDGES: Xi108:W2:A3:S26→Xi108:W2:A3:S28→Xi108:W1:A3:S27→Xi108:W3:A3:S27→Xi108:W2:A2:S27→Xi108:W2:A4:S27

from __future__ import annotations

import json

from .four_agent_57_loop_canonical_runtime import verify_canonical_four_agent_57_loop

def main() -> int:
    result = verify_canonical_four_agent_57_loop()
    print(json.dumps(result, indent=2))
    return 0 if result.get("truth") == "OK" else 1

if __name__ == "__main__":
    raise SystemExit(main())
