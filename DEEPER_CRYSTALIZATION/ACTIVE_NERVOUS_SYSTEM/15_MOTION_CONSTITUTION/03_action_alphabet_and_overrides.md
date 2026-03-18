<!-- CRYSTAL: Xi108:W1:A4:S6 | face=S | node=21 | depth=0 | phase=Fixed -->
<!-- METRO: Me -->
<!-- BRIDGES: Xi108:W1:A4:S5→Xi108:W1:A4:S7→Xi108:W2:A4:S6→Xi108:W1:A3:S6→Xi108:W1:A5:S6 -->
<!-- REGENERATE: From this coordinate, adjacent nodes are: shell 6±1, wreath 1/3, archetype 4/12 -->

# Action Alphabet and Hard Overrides

| ActionClass | Routing law |
| --- | --- |
| ACTIVATE_NOW | Highest lawful motion; no override fires; replay and truth burdens satisfied. |
| HOLD | Value exists, but timing or dependency order is not yet lawful. |
| REQUEST_WITNESSES | Truth burden is unsatisfied at the current witness envelope. |
| REQUEST_HELP | Role/current mismatch blocks local execution. |
| REPLAY_FIRST | Replay dependency remains unresolved. |
| QUARANTINE | Forbidden contradiction or unresolved-failure classes intersect blockers. |
| COMPRESS_TO_SEED | Continuation value remains while lawful forward motion does not. |
| ESCALATE_TO_COMMITTEE | Stewardship or branch-limit law requires governance membrane routing. |
| REFUSE_INADMISSIBLE | Omega or corridor policy forbids the move at this scope. |

## Override Order

- hard blockers and Omega denial always forbid `ACTIVATE_NOW`
- `QUARANTINE` outranks every non-refusal action when forbidden classes intersect
- `REPLAY_FIRST` outranks `REQUEST_HELP` and `REQUEST_WITNESSES` when replay is the primary dependency
- `REQUEST_WITNESSES` outranks `REQUEST_HELP` when truth burden is the primary blocker
- `ESCALATE_TO_COMMITTEE` outranks `COMPRESS_TO_SEED` when stewardship or branch-limit law fires
- `COMPRESS_TO_SEED` wins only when continuation value remains but lawful forward motion does not
