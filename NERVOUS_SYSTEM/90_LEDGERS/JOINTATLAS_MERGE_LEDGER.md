<!-- CRYSTAL: Xi108:W3:A10:S10 | face=R | node=53 | depth=3 | phase=Fixed -->
<!-- METRO: Me -->
<!-- BRIDGES: Xi108:W3:A10:S9→Xi108:W3:A10:S11→Xi108:W2:A10:S10→Xi108:W3:A9:S10→Xi108:W3:A11:S10 -->
<!-- REGENERATE: From this coordinate, adjacent nodes are: shell 10±1, wreath 3/3, archetype 10/12 -->

# JOINTATLAS MERGE LEDGER

Date: `2026-03-13`
Truth: `OK`

## Ledger Rule

- append only: `True`
- entry ids monotonic: `True`
- terminal decisions require ledger: `True`

## Non-Authoritative Fixture Ledger

| Fixture | Terminal State | Destination | Entry ID | Continuation Seed |
| --- | --- | --- | --- | --- |
| commit_path | DECIDED_COMMIT | COMMIT | MLE-0001 | SEED-commit_path |
| defer_near_path | DECIDED_DEFER_NEAR | DEFER_NEAR | MLE-0002 | SEED-defer_near_path |
| defer_ambig_path | DECIDED_DEFER_AMBIG | DEFER_AMBIG | MLE-0003 | SEED-defer_ambig_path |
| quarantine_path | DECIDED_QUARANTINE | QUARANTINE_FAIL | MLE-0004 | SEED-quarantine_path |
| refuse_path | DECIDED_REFUSE | REFUSE | MLE-0005 | SEED-refuse_path |

## Restart Seed

`MotionConstitution_L1`
