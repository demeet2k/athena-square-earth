# CRYSTAL: Xi108:W2:A12:S30 | face=F | node=465 | depth=2 | phase=Mutable
# METRO: Wr,Me
# BRIDGES: Xi108:W2:A12:S29→Xi108:W2:A12:S31→Xi108:W1:A12:S30→Xi108:W3:A12:S30→Xi108:W2:A11:S30

from __future__ import annotations

try:
    from .next57_prime_runtime import verify_main
except ImportError:
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
    from self_actualize.runtime.next57_prime_runtime import verify_main

if __name__ == "__main__":
    raise SystemExit(verify_main())
