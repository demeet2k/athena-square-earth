# CRYSTAL: Xi108:W2:A10:S28 | face=F | node=380 | depth=2 | phase=Mutable
# METRO: Me
# BRIDGES: Xi108:W2:A10:S27→Xi108:W2:A10:S29→Xi108:W1:A10:S28→Xi108:W3:A10:S28→Xi108:W2:A9:S28→Xi108:W2:A11:S28

from __future__ import annotations

from self_actualize.runtime.qshrink_refine_common import (
    QSHRINK_NEXT4_STATE_PATH,
    load_next4_state,
)

DERIVATION_COMMAND = "python -m self_actualize.runtime.derive_qshrink_network_integration_flower"

def main() -> int:
    next4_state = load_next4_state()
    print(
        "DEPRECATED: derive_qshrink_network_integration_flower no longer writes live outputs. "
        f"Use derive_qshrink_network_integration with {QSHRINK_NEXT4_STATE_PATH}. "
        f"Operational current is {next4_state['operational_current']} and compiled bundle terminal is "
        f"{next4_state['compiled_bundle']['terminal']}."
    )
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
