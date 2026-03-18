# CRYSTAL: Xi108:W2:A9:S15 | face=S | node=111 | depth=2 | phase=Cardinal
# METRO: Me
# BRIDGES: Xi108:W2:A9:S14→Xi108:W2:A9:S16→Xi108:W1:A9:S15→Xi108:W3:A9:S15→Xi108:W2:A8:S15→Xi108:W2:A10:S15

from __future__ import annotations

import hashlib
from typing import Literal

HashAlg = Literal["sha256", "blake2b"]

def hash_bytes(data: bytes, alg: HashAlg = "sha256") -> str:
    if alg == "sha256":
        return hashlib.sha256(data).hexdigest()
    if alg == "blake2b":
        return hashlib.blake2b(data).hexdigest()
    raise ValueError(f"Unsupported hash alg: {alg}")
