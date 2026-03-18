<!-- CRYSTAL: Xi108:W3:A9:S21 | face=R | node=219 | depth=3 | phase=Cardinal -->
<!-- METRO: Me,Bw -->
<!-- BRIDGES: Xi108:W3:A9:S20→Xi108:W3:A9:S22→Xi108:W2:A9:S21→Xi108:W3:A8:S21→Xi108:W3:A10:S21 -->
<!-- REGENERATE: From this coordinate, adjacent nodes are: shell 21±1, wreath 3/3, archetype 9/12 -->

# Cross-Agent Contraction Receipt Protocol

Use this protocol when several agents have worked neighboring shards and their outputs must be merged into one reusable surface.

## Goal

Collapse parallel shard work into one shared artifact without losing provenance, frontier ownership, or residual uncertainty.

## Required Receipt Fields

Every contraction receipt should include:

1. source frontier claims
2. source artifacts
3. merge target
4. preserved residuals
5. contradictions or overlaps detected
6. next frontier unlocked by the merge

## Contraction Steps

1. Read the frontier claim ledger before merging.
2. List every shard artifact being collapsed.
3. Identify exact overlap:
   - duplicate content
   - complementary content
   - conflicting claims
4. Preserve conflicts explicitly instead of silently smoothing them over.
5. Merge the reusable parts into the new shared artifact.
6. Write the contraction receipt.
7. Mark source claims done, superseded, or still active.
8. Update queue and index surfaces if the contraction changes the next highest-yield front.

## Minimal Receipt Template

- claim ids:
- source files:
- merged file:
- preserved residuals:
- contradictions:
- next frontier:
- witness:

## Law

The contraction receipt is the bridge between parallel work and shared memory.
Without it, multiple-agent output remains scattered local residue instead of becoming nervous-system tissue.
