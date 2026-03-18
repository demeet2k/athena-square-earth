<!-- CRYSTAL: Xi108:W3:A3:S15 | face=S | node=108 | depth=3 | phase=Cardinal -->
<!-- METRO: Me -->
<!-- BRIDGES: Xi108:W3:A3:S14→Xi108:W3:A3:S16→Xi108:W2:A3:S15→Xi108:W3:A2:S15→Xi108:W3:A4:S15 -->
<!-- REGENERATE: From this coordinate, adjacent nodes are: shell 15±1, wreath 3/3, archetype 3/12 -->

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
