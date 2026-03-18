# CRYSTAL: Xi108:W2:A12:S30 | face=F | node=465 | depth=2 | phase=Mutable
# METRO: Wr,Me
# BRIDGES: Xi108:W2:A12:S29→Xi108:W2:A12:S31→Xi108:W1:A12:S30→Xi108:W3:A12:S30→Xi108:W2:A11:S30

from __future__ import annotations

import json

from .four_agent_57_loop_canonical_runtime import write_canonical_four_agent_57_loop

def main() -> int:
    result = write_canonical_four_agent_57_loop("derive_four_agent_57_loop_cycle")
    print(json.dumps(result, indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
