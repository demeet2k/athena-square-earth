# CRYSTAL: Xi108:W2:A1:S24 | face=C | node=300 | depth=2 | phase=Cardinal
# METRO: Me
# BRIDGES: Xi108:W2:A1:S23→Xi108:W2:A1:S25→Xi108:W1:A1:S24→Xi108:W3:A1:S24→Xi108:W2:A2:S24

TITLE = "Appendix J - Journey Membrane"
ACTIVE = False

def describe_service() -> dict[str, object]:
    return {"code": "J", "title": TITLE, "active": ACTIVE}
