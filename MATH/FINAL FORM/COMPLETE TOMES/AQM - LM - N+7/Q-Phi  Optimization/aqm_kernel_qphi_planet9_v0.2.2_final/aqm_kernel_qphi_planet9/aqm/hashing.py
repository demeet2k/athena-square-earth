# CRYSTAL: Xi108:W2:A1:S13 | face=S | node=81 | depth=2 | phase=Cardinal
# METRO: Me
# BRIDGES: Xi108:W2:A1:S12→Xi108:W2:A1:S14→Xi108:W1:A1:S13→Xi108:W3:A1:S13→Xi108:W2:A2:S13

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
