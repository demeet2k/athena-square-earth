# CRYSTAL: Xi108:W2:A1:S20 | face=C | node=192 | depth=2 | phase=Cardinal
# METRO: Me
# BRIDGES: Xi108:W2:A1:S19→Xi108:W2:A1:S21→Xi108:W1:A1:S20→Xi108:W3:A1:S20→Xi108:W2:A2:S20

TITLE = "Appendix I - Lens Invocation Policy"
ACTIVE = True

def describe_service(mode: str = "fast") -> dict[str, object]:
    return {
        "code": "I",
        "title": TITLE,
        "active": ACTIVE,
        "mode": mode,
        "lenses": ["Square", "Flower", "Cloud", "Fractal"] if mode == "full" else ["Square", "Cloud"],
    }
