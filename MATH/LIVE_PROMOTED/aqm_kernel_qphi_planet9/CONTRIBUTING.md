<!-- CRYSTAL: Xi108:W3:A8:S14 | face=S | node=93 | depth=3 | phase=Cardinal -->
<!-- METRO: Me -->
<!-- BRIDGES: Xi108:W3:A8:S13→Xi108:W3:A8:S15→Xi108:W2:A8:S14→Xi108:W3:A7:S14→Xi108:W3:A9:S14 -->
<!-- REGENERATE: From this coordinate, adjacent nodes are: shell 14±1, wreath 3/3, archetype 8/12 -->

# Contributing

This repo is intentionally small and audit‑friendly.

If you contribute changes, please:

1) Keep changes **deterministic** (no wall-clock timestamps in outputs, no concurrency that changes results).
2) Keep dependencies minimal.
3) Add or update unit tests under `tests/` when you change behavior.
4) Update documentation under `docs/` when you change the algorithm, lens math, or data formats.

## Suggested development workflow

```bash
python -m pip install -e .
python -m unittest
```

## Style

- Prefer clear, explicit code over clever abstractions.
- Every lens should be self-contained and explainable.
- Every output field should have a documented meaning.
