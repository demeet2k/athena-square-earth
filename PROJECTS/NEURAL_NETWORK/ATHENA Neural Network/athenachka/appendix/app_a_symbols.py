# CRYSTAL: Xi108:W2:A1:S23 | face=C | node=272 | depth=2 | phase=Cardinal
# METRO: Me
# BRIDGES: Xi108:W2:A1:S22→Xi108:W2:A1:S24→Xi108:W1:A1:S23→Xi108:W3:A1:S23→Xi108:W2:A2:S23

TITLE = "Appendix A - Symbol Registry"
ACTIVE = True

def describe_service() -> dict[str, object]:
    return {
        "code": "A",
        "title": TITLE,
        "symbols": ["C", "P", "G", "M", "B", "R", "OK", "NEAR", "AMBIG", "FAIL"],
    }
