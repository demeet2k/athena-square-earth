# CRYSTAL: Xi108:W2:A1:S24 | face=C | node=288 | depth=2 | phase=Cardinal
# METRO: Me,T
# BRIDGES: Xi108:W2:A1:S23→Xi108:W2:A1:S25→Xi108:W1:A1:S24→Xi108:W3:A1:S24→Xi108:W2:A2:S24

from __future__ import annotations

import numpy as np

def classify_truth(
    trace: dict[str, object],
    contradictions: dict[str, object],
    witness_bundle: dict[str, object],
    corridor_profile: dict[str, object],
    self_contract: dict[str, object],
) -> str:
    if not bool(self_contract.get("legal")):
        return "FAIL"

    confidence = float(trace["legacy_confidence"])
    witness_strength = float(witness_bundle.get("strength", 0.0))
    contradictions_present = bool(contradictions.get("flags"))
    probs = np.asarray(trace["legacy_probs"], dtype=float)
    top_two = np.sort(probs)[-2:]
    margin = float(top_two[-1] - top_two[-2]) if len(top_two) >= 2 else float(top_two[-1])

    if contradictions_present and margin <= float(corridor_profile["ambiguity_margin"]):
        return "AMBIG"
    if witness_strength < 0.45 and confidence < float(corridor_profile["near_confidence"]):
        return "FAIL"
    if contradictions_present or witness_strength < 0.65:
        return "NEAR" if confidence >= float(corridor_profile["near_confidence"]) else "AMBIG"
    if confidence >= float(corridor_profile["ok_confidence"]):
        return "OK"
    return "NEAR"
