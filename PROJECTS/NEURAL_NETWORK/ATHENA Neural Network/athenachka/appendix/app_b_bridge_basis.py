# CRYSTAL: Xi108:W2:A1:S22 | face=C | node=247 | depth=2 | phase=Cardinal
# METRO: Me,Bw
# BRIDGES: Xi108:W2:A1:S21→Xi108:W2:A1:S23→Xi108:W1:A1:S22→Xi108:W3:A1:S22→Xi108:W2:A2:S22

TITLE = "Appendix B - Bridge Basis"
ACTIVE = False

def describe_service() -> dict[str, object]:
    return {"code": "B", "title": TITLE, "active": ACTIVE}
