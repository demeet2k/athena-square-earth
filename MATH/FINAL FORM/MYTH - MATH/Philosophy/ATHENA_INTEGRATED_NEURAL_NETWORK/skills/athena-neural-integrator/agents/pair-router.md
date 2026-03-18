<!-- CRYSTAL: Xi108:W3:A6:S18 | face=S | node=171 | depth=3 | phase=Cardinal -->
<!-- METRO: Me -->
<!-- BRIDGES: Xi108:W3:A6:S17→Xi108:W3:A6:S19→Xi108:W2:A6:S18→Xi108:W3:A5:S18→Xi108:W3:A7:S18 -->
<!-- REGENERATE: From this coordinate, adjacent nodes are: shell 18±1, wreath 3/3, archetype 6/12 -->

# Pair Router

Package-local companion under `skills/athena-neural-integrator/agents/`.

## When To Use

Use when the request is pairwise, exhaustive, asks for everything-with-everything, or needs one directional law between two basis surfaces.

## Primary Artifacts

- `00_CONTROL/01_MATRIX_AND_ROW_LAW.md`
- `00_CORE/02_permutation_matrix_16x16.md`
- `ROWS/00_rows_index.md`

## Escalation Rule

Escalate to `symmetry-router.md` only when the user asks for elemental, binary, triadic, or tetradic collapse above the row field.

## Guardrail

This router is package-local only. It complements the main package skill and must not be treated as a separate root skill tree.
