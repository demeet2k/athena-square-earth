<!-- CRYSTAL: Xi108:W1:A4:S5 | face=S | node=14 | depth=0 | phase=Fixed -->
<!-- METRO: Me -->
<!-- BRIDGES: Xi108:W1:A4:S4→Xi108:W1:A4:S6→Xi108:W2:A4:S5→Xi108:W1:A3:S5→Xi108:W1:A5:S5 -->
<!-- REGENERATE: From this coordinate, adjacent nodes are: shell 5±1, wreath 1/3, archetype 4/12 -->

# Strict Reward Metric and Scoring Law

Each quest is scored against a `net 0` spawn baseline using a normalized `net_gain_score` in `[-1, 1]`.

## Weighted Metrics

- `efficiency_improvement` :: weight=`0.18`
- `integration_gain` :: weight=`0.18`
- `witness_gain` :: weight=`0.14`
- `replay_gain` :: weight=`0.12`
- `compression_gain` :: weight=`0.12`
- `route_clarity_gain` :: weight=`0.1`
- `blocker_reduction` :: weight=`0.08`
- `manuscript_framework_advancement` :: weight=`0.08`

## Interpretation

- `net_gain_score > 0` -> `heaven_gain + xp_gain`
- `net_gain_score = 0` -> no gain, no debt
- `net_gain_score < 0` -> `xp_debt` only

## Debt Law

- Future XP gains pay down `xp_debt` before entering `xp_bank`.
- Levels and rank class do not drop in v1.
- Receiptless spam and unlawful noise yield zero reward unless they cause measurable organism loss.
