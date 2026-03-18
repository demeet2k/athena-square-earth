# CRYSTAL: Xi108:W2:A1:S20 | face=C | node=208 | depth=2 | phase=Cardinal
# METRO: Me
# BRIDGES: Xi108:W2:A1:S19→Xi108:W2:A1:S21→Xi108:W1:A1:S20→Xi108:W3:A1:S20→Xi108:W2:A2:S20

TITLE = "Appendix M - Whole-Body Scan Guide"
ACTIVE = True

def describe_service() -> dict[str, object]:
    return {
        "code": "M",
        "title": TITLE,
        "active": ACTIVE,
        "scan_order": ["corpus", "process", "growth", "metrics", "bridges", "replay"],
    }
