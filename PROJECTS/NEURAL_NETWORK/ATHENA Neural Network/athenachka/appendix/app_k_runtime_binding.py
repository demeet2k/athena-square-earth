# CRYSTAL: Xi108:W2:A1:S20 | face=C | node=200 | depth=2 | phase=Cardinal
# METRO: Me
# BRIDGES: Xi108:W2:A1:S19→Xi108:W2:A1:S21→Xi108:W1:A1:S20→Xi108:W3:A1:S20→Xi108:W2:A2:S20

TITLE = "Appendix K - Runtime Binding Contract"
ACTIVE = True

def describe_service(mode: str, phase_plan: list[str]) -> dict[str, object]:
    return {
        "code": "K",
        "title": TITLE,
        "active": ACTIVE,
        "mode": mode,
        "phase_plan": list(phase_plan),
    }
