<!-- CRYSTAL: Xi108:W3:A11:S11 | face=R | node=61 | depth=3 | phase=Fixed -->
<!-- METRO: Me -->
<!-- BRIDGES: Xi108:W3:A11:S10→Xi108:W3:A11:S12→Xi108:W2:A11:S11→Xi108:W3:A10:S11→Xi108:W3:A12:S11 -->
<!-- REGENERATE: From this coordinate, adjacent nodes are: shell 11±1, wreath 3/3, archetype 11/12 -->

# Phase 6 Wave 2 Capsule Densification

Date: `2026-03-13`
Verdict: `IN PROGRESS`
Docs gate: `BLOCKED`

Phase 6 turns the second-wave bridge families into atlas-backed capsule bundles while keeping
`Stoicheia` and `CLEAN` reserve-thin.

## Operating Law

`atlas refresh -> baseline witness/fabric snapshot -> wave2 bundle writeback -> runtime support writeback -> atlas refresh -> semantic/fabric rerun -> runtime verification`

## Target Families

- `qshrink`
- `athena_fleet`
- `games`
- `identity`
- `orgin`

## Honest Scope

- Google Docs ingress remains `BLOCKED`
- reserve shelves remain explicitly reserve-thin
- graph growth stays minimal and interface-driven
