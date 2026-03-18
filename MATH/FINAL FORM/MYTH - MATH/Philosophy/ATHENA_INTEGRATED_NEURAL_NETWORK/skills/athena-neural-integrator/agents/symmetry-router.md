<!-- CRYSTAL: Xi108:W3:A5:S17 | face=S | node=141 | depth=3 | phase=Cardinal -->
<!-- METRO: Me -->
<!-- BRIDGES: Xi108:W3:A5:S16→Xi108:W3:A5:S18→Xi108:W2:A5:S17→Xi108:W3:A4:S17→Xi108:W3:A6:S17 -->
<!-- REGENERATE: From this coordinate, adjacent nodes are: shell 17±1, wreath 3/3, archetype 5/12 -->

# Symmetry Router

Package-local companion under `skills/athena-neural-integrator/agents/`.

## When To Use

Use when the request asks for fire, water, air, earth, any two-way or three-way symmetry, the tetradic closure, or the symmetry zero point.

## Primary Artifacts

- `00_CONTROL/02_SYMMETRY_AND_OBSERVER_LAW.md`
- `SYMMETRY_STACK/00_symmetry_index.md`
- `FIRE/00_fire_index.md`

## Escalation Rule

Escalate to `metro-router.md` only after the user is asking for lines, hubs, clusters, attractors, or route-level synthesis.

## Guardrail

This router is package-local only. It complements the main package skill and must not be treated as a separate root skill tree.
