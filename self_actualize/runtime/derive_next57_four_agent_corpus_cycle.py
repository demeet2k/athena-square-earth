# CRYSTAL: Xi108:W2:A3:S27 | face=F | node=360 | depth=2 | phase=Mutable
# METRO: Wr,Me
# BRIDGES: Xi108:W2:A3:S26→Xi108:W2:A3:S28→Xi108:W1:A3:S27→Xi108:W3:A3:S27→Xi108:W2:A2:S27→Xi108:W2:A4:S27

from __future__ import annotations

try:
    from .next57_prime_runtime import main
except ImportError:
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
    from self_actualize.runtime.next57_prime_runtime import main

if __name__ == "__main__":
    raise SystemExit(main())
