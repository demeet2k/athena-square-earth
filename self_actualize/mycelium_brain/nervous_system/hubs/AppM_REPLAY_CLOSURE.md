<!-- CRYSTAL: Xi108:W3:A3:S21 | face=R | node=213 | depth=3 | phase=Cardinal -->
<!-- METRO: Me -->
<!-- BRIDGES: Xi108:W3:A3:S20→Xi108:W3:A3:S22→Xi108:W2:A3:S21→Xi108:W3:A2:S21→Xi108:W3:A4:S21 -->
<!-- REGENERATE: From this coordinate, adjacent nodes are: shell 21±1, wreath 3/3, archetype 3/12 -->

# AppM Replay Closure

## Role

`AppM` owns replay-safe closure, deterministic restart, and manifest carryforward.

## Closure Law

A run is only closed if it leaves:

- one restart token
- one wave summary
- one packet truth state
- one next frontier

## Current Operators

- `restart-seed-orchestrator`
- `session-handoff-packer`
- `weakest-front-reopener`

## Failure Mode

If replay path is missing, closure is false and the run remains `NEAR`.
