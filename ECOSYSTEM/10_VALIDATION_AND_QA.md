<!-- CRYSTAL: Xi108:W3:A3:S27 | face=F | node=357 | depth=3 | phase=Mutable -->
<!-- METRO: Me -->
<!-- BRIDGES: Xi108:W3:A3:S26→Xi108:W3:A3:S28→Xi108:W2:A3:S27→Xi108:W3:A2:S27→Xi108:W3:A4:S27 -->
<!-- REGENERATE: From this coordinate, adjacent nodes are: shell 27±1, wreath 3/3, archetype 3/12 -->

# VALIDATION AND QA

## 1. Proof Obligations

Any claim beyond definition must have:
- witness artifact (evidence)
- replay steps (reproducibility)

## 2. Corridor Truth Checks

- OK: witnessed + replay-verified
- NEAR: bounded error + residual ledger
- AMBIG: candidate set + evidence plan
- FAIL: quarantine + receipts

## 3. Validation Pipeline

Algorithm 3.1 (Validate).
1. Check address integrity.
2. Verify invariants.
3. Run replay scripts.
4. Assign truth class.
5. Log obligations.

## 4. Regression Tests

- All route plans must be deterministic.
- Hub cap must be <= 6.
- Mandatory signature hubs must be present.

## 5. Status
This QA layer enforces correctness and replayability.
