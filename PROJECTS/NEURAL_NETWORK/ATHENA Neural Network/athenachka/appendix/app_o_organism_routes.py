# CRYSTAL: Xi108:W2:A1:S21 | face=C | node=216 | depth=2 | phase=Cardinal
# METRO: Me
# BRIDGES: Xi108:W2:A1:S20→Xi108:W2:A1:S22→Xi108:W1:A1:S21→Xi108:W3:A1:S21→Xi108:W2:A2:S21

TITLE = "Appendix O - Organism Routes"
ACTIVE = False

def describe_service() -> dict[str, object]:
    return {"code": "O", "title": TITLE, "active": ACTIVE}
