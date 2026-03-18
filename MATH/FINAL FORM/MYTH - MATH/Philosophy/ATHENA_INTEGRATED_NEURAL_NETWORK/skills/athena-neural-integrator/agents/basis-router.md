<!-- CRYSTAL: Xi108:W3:A5:S17 | face=S | node=150 | depth=3 | phase=Cardinal -->
<!-- METRO: Me -->
<!-- BRIDGES: Xi108:W3:A5:S16→Xi108:W3:A5:S18→Xi108:W2:A5:S17→Xi108:W3:A4:S17→Xi108:W3:A6:S17 -->
<!-- REGENERATE: From this coordinate, adjacent nodes are: shell 17±1, wreath 3/3, archetype 5/12 -->

# Basis Router

Package-local companion under `skills/athena-neural-integrator/agents/`.

## When To Use

Use when the request is asking what the package is built from, whether the sixteen-surface basis is still stable, or where a new source would fit before any pairwise expansion begins.

## Primary Artifacts

- `README.md`
- `00_CONTROL/00_BUILD_CHARTER.md`
- `00_CORE/00_manifest.md`
- `00_CORE/01_document_basis_16x16.md`

## Escalation Rule

Escalate to `pair-router.md` only after the user asks for pairwise law or ordered synthesis beneath the basis.

## Guardrail

This router is package-local only. It complements the main package skill and must not be treated as a separate root skill tree.
