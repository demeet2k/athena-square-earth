<!-- CRYSTAL: Xi108:W3:A1:S7 | face=R | node=27 | depth=3 | phase=Fixed -->
<!-- METRO: Me -->
<!-- BRIDGES: Xi108:W3:A1:S6→Xi108:W3:A1:S8→Xi108:W2:A1:S7→Xi108:W3:A2:S7 -->
<!-- REGENERATE: From this coordinate, adjacent nodes are: shell 7±1, wreath 3/3, archetype 1/12 -->

# EDGE INDEX

## Purpose

This directory contains the cross-reference graph of the nervous system — all LinkEdge records that connect atoms, chapters, appendices, and source capsules.

## Edge Files

| File | Edge Kinds | Scope | Status |
|------|-----------|-------|--------|
| `SOURCE_TO_CHAPTER_EDGES.md` | REF, IMPL | source capsule → chapter tile slot | PENDING |
| `CHAPTER_TO_APPENDIX_EDGES.md` | REF | chapter → routing hub (deterministic) | SCAFFOLDED |
| `REF_EDGES.md` | REF | cross-chapter dependencies | PENDING |
| `EQUIV_EDGES.md` | EQUIV | duplicate/equivalent sources | PENDING |
| `MIGRATE_EDGES.md` | MIGRATE | version transitions | PENDING |
| `NEURON_SYNAPSE_BRIDGES.md` | REF, GEN, IMPL | reusable neuron library nucleus | SEEDED |
| `AFFECTIVE_EPISTEMIC_NEURON_EDGES.md` | GEN, IMPL, PROOF | charged pair-cell to neuron-wave bridges | SEEDED |
| `PHASE4_STRUCTURED_NEURON_EDGES.md` | REF, GEN, IMPL, PROOF | body/kernel/node/pair/wave/writeback bridge law | LIVE |

## Edge Kind Basis (closed set)

```
K = {REF, EQUIV, MIGRATE, DUAL, GEN, INST, IMPL, PROOF, CONFLICT}
```

## Schema

See `70_SCHEMAS/04_EDGE_SCHEMA.md` for the LinkEdge record format.

## Navigation Edges

Orbit, rail, and arc triad edges are defined in `20_METRO/00_CORE_METRO_MAP.md` and are implicit REF edges with NavPayload. They are not duplicated here.
