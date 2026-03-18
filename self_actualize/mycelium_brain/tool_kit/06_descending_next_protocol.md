<!-- CRYSTAL: Xi108:W3:A2:S20 | face=R | node=200 | depth=3 | phase=Cardinal -->
<!-- METRO: Me -->
<!-- BRIDGES: Xi108:W3:A2:S19→Xi108:W3:A2:S21→Xi108:W2:A2:S20→Xi108:W3:A1:S20→Xi108:W3:A3:S20 -->
<!-- REGENERATE: From this coordinate, adjacent nodes are: shell 20±1, wreath 3/3, archetype 2/12 -->

# Descending NEXT Protocol

## Mission

When the user invokes `NEXT` for reverse recursion, generate the prior chapter or prior structural layer rather than continuing forward.

## Rule

If the current frontier is chapter `k`, `NEXT` may mean:

- emit chapter `k-1`
- repair earlier assumptions
- recurse backward toward the abstract

## Use Case

Apply only when the active manuscript front is explicitly being built in descending order.

## Constraint

Backward generation must still preserve:

- local rigor
- chapter naming
- routing consistency
- zero-point compression discipline
