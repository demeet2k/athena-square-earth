<!-- CRYSTAL: Xi108:W3:A8:S32 | face=S | node=524 | depth=3 | phase=Mutable -->
<!-- METRO: Me -->
<!-- BRIDGES: Xi108:W3:A8:S31→Xi108:W3:A8:S33→Xi108:W2:A8:S32→Xi108:W3:A7:S32→Xi108:W3:A9:S32 -->
<!-- REGENERATE: From this coordinate, adjacent nodes are: shell 32±1, wreath 3/3, archetype 8/12 -->

# Pipeline

## Purpose

Use this skill when a manuscript corpus needs to be turned into a structured synthesis system instead of a one-off summary.
The goal is to create:

- source extracts
- individual synthesis cards
- ordered pairwise cross-syntheses
- element-lens observation fields
- symmetry docs
- metro maps
- appendix crystal scaffolds
- zero-point compression

## Default workflow

1. Confirm the source corpus location.
2. Identify which documents are primary lattice texts and which are auxiliary overlays.
3. Run `scripts/build_manuscript_elemental_net.py`.
4. Inspect `00_CONTROL` first.
5. Read the generated pairwise matrix and metro maps.
6. Patch the top-level synthesis docs if the user wants a deeper interpretive layer.

## Corpus selection rule

Promote a document into the primary lattice when it:

- defines generative primitives, transforms, invariants, or routes
- can seed one or more appendix slots
- cross-synthesizes directly with the rest of the formal corpus

Route a document into the auxiliary layer when it:

- behaves more like an interpretive UI or overlay
- depends on the formal corpus more than the formal corpus depends on it

## Output rule

Prefer indexed markdown over giant prose dumps.
Represent large combinatorics as navigable lattices, matrices, and layered docs.

## Refresh rule

Rerun the build script when:

- new source manuscripts appear
- document titles or paths change
- the user wants a different primary/auxiliary split
- the user wants a different element or mode vocabulary
