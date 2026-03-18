<!-- CRYSTAL: Xi108:W3:A5:S23 | face=R | node=265 | depth=3 | phase=Cardinal -->
<!-- METRO: Me,T -->
<!-- BRIDGES: Xi108:W3:A5:S22→Xi108:W3:A5:S24→Xi108:W2:A5:S23→Xi108:W3:A4:S23→Xi108:W3:A6:S23 -->
<!-- REGENERATE: From this coordinate, adjacent nodes are: shell 23±1, wreath 3/3, archetype 5/12 -->

# Phase 5 Atlas Truth And Capsule Metabolism Runtime

Date: `2026-03-13`
Docs gate: `BLOCKED`
Scope: `local-corpus`

This runtime mirror tracks the dual-track Phase 5 pass:

- atlas truth refresh
- capsule metabolism for the first four thin families

## Status

- verdict: `COMPLETE`
- indexed witness after refresh: `7559`
- first-wave families deepened: `math`, `voynich`, `ecosystem`, `published_books`
- docs gate: `BLOCKED`

## Verification

- `python -m self_actualize.runtime.verify_runtime_waist`
- `python -m self_actualize.runtime.verify_atlasforge_runtime_lane`
- `python -m self_actualize.runtime.verify_aqm_runtime_lane`

## Regeneration

```powershell
python -m self_actualize.runtime.derive_phase5_atlas_truth_and_capsule_metabolism
```
