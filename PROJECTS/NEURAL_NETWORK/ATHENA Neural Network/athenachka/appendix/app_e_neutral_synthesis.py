# CRYSTAL: Xi108:W2:A1:S20 | face=C | node=208 | depth=2 | phase=Cardinal
# METRO: Me
# BRIDGES: Xi108:W2:A1:S19→Xi108:W2:A1:S21→Xi108:W1:A1:S20→Xi108:W3:A1:S20→Xi108:W2:A2:S20

TITLE = "Appendix E - Neutral Synthesis Grammar"
ACTIVE = True

def describe_service(trace: dict[str, object] | None = None) -> dict[str, object]:
    trace = trace or {}
    return {
        "code": "E",
        "title": TITLE,
        "active": ACTIVE,
        "neutral_summary": {
            "prediction": trace.get("legacy_prediction"),
            "confidence": trace.get("legacy_confidence"),
            "candidate_count": len(trace.get("hypotheses", [])),
        },
    }
