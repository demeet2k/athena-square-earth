# CRYSTAL: Xi108:W2:A4:S28 | face=F | node=386 | depth=2 | phase=Mutable
# METRO: Me
# BRIDGES: Xi108:W2:A4:S27→Xi108:W2:A4:S29→Xi108:W1:A4:S28→Xi108:W3:A4:S28→Xi108:W2:A3:S28→Xi108:W2:A5:S28

from __future__ import annotations

from self_actualize.runtime.qshrink_refine_common import (
    QSHRINK_NEXT4_STATE_PATH,
    default_next4_state,
    utc_now,
    write_json,
)

DERIVATION_COMMAND = "python -m self_actualize.runtime.derive_qshrink_next4_state"

def build_payload() -> dict:
    payload = default_next4_state()
    payload["generated_at"] = utc_now()
    payload["derivation_command"] = DERIVATION_COMMAND
    payload["truth"] = "OK" if payload["docs_gate_status"] == "BLOCKED" else "NEAR"
    payload["authority_basis"] = [
        "dual-track-canonicalization",
        "q42-qshrink-next4",
        "docs-gate-honesty",
    ]
    return payload

def main() -> int:
    payload = build_payload()
    write_json(QSHRINK_NEXT4_STATE_PATH, payload)
    print(f"Wrote {QSHRINK_NEXT4_STATE_PATH}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
