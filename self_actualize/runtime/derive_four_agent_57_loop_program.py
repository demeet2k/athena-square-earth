# CRYSTAL: Xi108:W2:A11:S29 | face=F | node=410 | depth=2 | phase=Mutable
# METRO: Me
# BRIDGES: Xi108:W2:A11:S28→Xi108:W2:A11:S30→Xi108:W1:A11:S29→Xi108:W3:A11:S29→Xi108:W2:A10:S29→Xi108:W2:A12:S29

from __future__ import annotations

import json

from .four_agent_57_loop_canonical_runtime import write_canonical_four_agent_57_loop

def main() -> int:
    result = write_canonical_four_agent_57_loop("derive_four_agent_57_loop_program")
    print(json.dumps(result, indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
