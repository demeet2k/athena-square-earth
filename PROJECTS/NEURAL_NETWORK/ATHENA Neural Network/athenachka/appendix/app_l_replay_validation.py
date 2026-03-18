# CRYSTAL: Xi108:W2:A1:S20 | face=C | node=206 | depth=2 | phase=Cardinal
# METRO: Me
# BRIDGES: Xi108:W2:A1:S19→Xi108:W2:A1:S21→Xi108:W1:A1:S20→Xi108:W3:A1:S20→Xi108:W2:A2:S20

from __future__ import annotations

from ..contracts import stable_hash

TITLE = "Appendix L - Replay Validation Harness"
ACTIVE = True

def build_replay_signature(payload: dict[str, object]) -> str:
    return stable_hash(payload)

def describe_service(payload: dict[str, object] | None = None) -> dict[str, object]:
    payload = payload or {}
    return {
        "code": "L",
        "title": TITLE,
        "active": ACTIVE,
        "signature": build_replay_signature(payload),
    }
