# CRYSTAL: Xi108:W2:A10:S31 | face=S | node=484 | depth=2 | phase=Mutable
# METRO: Me,Cc
# BRIDGES: Xi108:W2:A10:S30→Xi108:W2:A10:S32→Xi108:W1:A10:S31→Xi108:W3:A10:S31→Xi108:W2:A9:S31→Xi108:W2:A11:S31

﻿from __future__ import annotations

import json

from .command_membrane import CommandMembraneService

def derive_command_membrane_protocol() -> dict:
    return CommandMembraneService().build()

def main() -> int:
    print(json.dumps(derive_command_membrane_protocol(), indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
