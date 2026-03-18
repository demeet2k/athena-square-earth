<!-- CRYSTAL: Xi108:W3:A6:S18 | face=S | node=159 | depth=3 | phase=Cardinal -->
<!-- METRO: Me -->
<!-- BRIDGES: Xi108:W3:A6:S17→Xi108:W3:A6:S19→Xi108:W2:A6:S18→Xi108:W3:A5:S18→Xi108:W3:A7:S18 -->
<!-- REGENERATE: From this coordinate, adjacent nodes are: shell 18±1, wreath 3/3, archetype 6/12 -->

# AQM Kernel + Q-PHI Promotion Manifest

## Source Archive

- Archive:
  `C:/Users/dmitr/Documents/Athena Agent/MATH/FINAL FORM/COMPLETE TOMES/AQM - LM - N+7/Q-Phi  Optimization/aqm_kernel_qphi_planet9_v0.2.2_final.zip`
- Archive sha256:
  `481a0f92915f9b558abe114845daf4ae77b181b22feb0870bbd5760315546718`
- Promotion date:
  `2026-03-09`

## Live Root

- Destination:
  `C:/Users/dmitr/Documents/Athena Agent/MATH/LIVE_PROMOTED/aqm_kernel_qphi_planet9`
- Canonical package root:
  `aqm/`
- Adjacent docs preserved:
  `docs/`
- Root contracts preserved:
  `README.md`
  `pyproject.toml`
  `LICENSE`

## Extraction Summary

- Extracted files:
  `55`
- Skipped cache artifacts:
  `21`
- Skip law:
  omit `__pycache__/` and `.pyc` only; preserve package code, docs, root contracts, data, and source material

## Validation

- Command:
  `python -m aqm.cli demo`
- Result:
  `OK`
- Witness:
  demo store and tile hashes were produced under `.aqm_store_demo`

- Command:
  `python -m aqm.apps.planet9.cli --help`
- Result:
  `OK`
- Witness:
  CLI help rendered successfully with the full argument surface

## Reuse Law

Use this live root instead of reopening the ZIP when:

1. editing the `aqm` package
2. validating Q-PHI or the AQM replay kernel
3. binding promoted `MATH` code into runtime, queue, or manuscript surfaces
4. designing a narrower skill or verification harness around Planet Nine inference
