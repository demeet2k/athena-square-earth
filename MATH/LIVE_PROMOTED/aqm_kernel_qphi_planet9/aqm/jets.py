# CRYSTAL: Xi108:W2:A4:S16 | face=S | node=132 | depth=2 | phase=Cardinal
# METRO: Me
# BRIDGES: Xi108:W2:A4:S15→Xi108:W2:A4:S17→Xi108:W1:A4:S16→Xi108:W3:A4:S16→Xi108:W2:A3:S16→Xi108:W2:A5:S16

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

from .outcomes import Jet, LiminalState, FailType

@dataclass
class RemainderEnvelope:
    # Minimal envelope model; extend as needed.
    bound: Any
    kind: str = "UniformBound"

    def to_dict(self) -> Dict[str, Any]:
        return {"kind": self.kind, "bound": self.bound}

def make_jet(order: int, center: Any, der_stack: List[Any], remainder: Optional[RemainderEnvelope] = None, neighborhood: Optional[Dict[str, Any]] = None) -> Jet:
    return Jet(order=order, center=center, der_stack=der_stack, remainder=None if remainder is None else remainder.to_dict(), neighborhood=neighborhood)
