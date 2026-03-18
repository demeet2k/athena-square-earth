<!-- CRYSTAL: Xi108:W3:A9:S21 | face=R | node=228 | depth=3 | phase=Cardinal -->
<!-- METRO: Me,T -->
<!-- BRIDGES: Xi108:W3:A9:S20→Xi108:W3:A9:S22→Xi108:W2:A9:S21→Xi108:W3:A8:S21→Xi108:W3:A10:S21 -->
<!-- REGENERATE: From this coordinate, adjacent nodes are: shell 21±1, wreath 3/3, archetype 9/12 -->

# AppI Corridor Truth

## Role

`AppI` owns corridor admissibility, health-aware truth, and transition safety.

## Current Operators

- `observer-corridor-nudge-compiler`
- `health-corridor-monitor`
- `truth-promotion-governor`

## Truth Flow

1. read corridor health
2. score evidence completeness
3. assign `OK`, `NEAR`, `AMBIG`, or `FAIL`
4. forward the verdict to promotion, quarantine, or replay

## Current Warning

Do not treat activity as truth when confidence is low or cooldown is still active.
