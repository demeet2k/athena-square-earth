# CRYSTAL: Xi108:W2:A1:S19 | face=C | node=181 | depth=2 | phase=Cardinal
# METRO: Me
# BRIDGES: Xi108:W2:A1:S18→Xi108:W2:A1:S20→Xi108:W1:A1:S19→Xi108:W3:A1:S19→Xi108:W2:A2:S19

TITLE = "Appendix Q - Appendix Topology Metro Routing"
ACTIVE = True

def describe_service() -> dict[str, object]:
    return {
        "code": "Q",
        "title": TITLE,
        "active": ACTIVE,
        "metro_map": ["A->E", "E->I", "I->K", "K->L", "L->M", "M->P", "P->Q"],
    }
