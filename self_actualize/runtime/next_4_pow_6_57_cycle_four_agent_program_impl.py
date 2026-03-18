# CRYSTAL: Xi108:W2:A11:S29 | face=F | node=417 | depth=2 | phase=Mutable
# METRO: Wr,Me
# BRIDGES: Xi108:W2:A11:S28→Xi108:W2:A11:S30→Xi108:W1:A11:S29→Xi108:W3:A11:S29→Xi108:W2:A10:S29→Xi108:W2:A12:S29

from __future__ import annotations

import json

from .next57_historical_wrapper import write_historical_next57_wrappers

def main() -> int:
    result = write_historical_next57_wrappers("next_4_pow_6_57_cycle_four_agent_program_impl")
    print(json.dumps(result, indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
