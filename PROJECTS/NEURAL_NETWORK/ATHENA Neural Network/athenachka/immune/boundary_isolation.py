# CRYSTAL: Xi108:W2:A1:S19 | face=C | node=183 | depth=2 | phase=Cardinal
# METRO: Me
# BRIDGES: Xi108:W2:A1:S18→Xi108:W2:A1:S20→Xi108:W1:A1:S19→Xi108:W3:A1:S19→Xi108:W2:A2:S19

from __future__ import annotations

def verify_boundary(contradictions: dict[str, object], state) -> dict[str, object]:
    quarantined = bool(contradictions.get("quarantined"))
    boundary = {
        "hausdorff_boundary": "sealed" if quarantined else "open",
        "logic_wall": "strict",
        "quarantine_flux": 0.0,
        "paraconsistent_zone": "active" if quarantined else "dormant",
        "checkpoint_id": state.checkpoint_id,
    }
    return boundary
