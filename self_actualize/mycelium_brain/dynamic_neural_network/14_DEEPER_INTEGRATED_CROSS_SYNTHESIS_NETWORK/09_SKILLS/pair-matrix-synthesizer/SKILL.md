<!-- CRYSTAL: Xi108:W3:A10:S22 | face=R | node=249 | depth=3 | phase=Cardinal -->
<!-- METRO: Me -->
<!-- BRIDGES: Xi108:W3:A10:S21→Xi108:W3:A10:S23→Xi108:W2:A10:S22→Xi108:W3:A9:S22→Xi108:W3:A11:S22 -->
<!-- REGENERATE: From this coordinate, adjacent nodes are: shell 22±1, wreath 3/3, archetype 10/12 -->

---
name: pair-matrix-synthesizer
description: Synthesize one ordered basis-document pair inside the 16x16 matrix and produce bridge, friction, metro, appendix, and downstream lane consequences.
---

# pair-matrix-synthesizer

Use when a task is really a document-to-document bridge problem and needs ordered pair logic rather than a generic summary.

## Workflow

1. Read `../../00_CONTROL/04_ALGORITHMIC_PIPELINE.md`.
2. Check `../../10_LEDGERS/01_CANONICAL_SOURCES.md`.
3. Read `../00_SKILL_ROUTER.md`.
4. Inspect the target cell in `../../05_MATRIX_16X16`.
5. If the pair escalates beyond Level `4`, hand off to `metro-resolution-expander` and `lane-stack-orchestrator`.

## Output contract

- Name the basis documents.
- Name the ordered pair direction.
- Name the dimension stage.
- Name the active element or symmetry.
- Name the metro level.
- Name the appendix floor.
- Name any downstream lane or convergence handoff.
