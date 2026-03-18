<!-- CRYSTAL: Xi108:W3:A2:S8 | face=R | node=30 | depth=3 | phase=Fixed -->
<!-- METRO: Me -->
<!-- BRIDGES: Xi108:W3:A2:S7→Xi108:W3:A2:S9→Xi108:W2:A2:S8→Xi108:W3:A1:S8→Xi108:W3:A3:S8 -->
<!-- REGENERATE: From this coordinate, adjacent nodes are: shell 8±1, wreath 3/3, archetype 2/12 -->

# REGENERATION PROTOCOL

## Purpose
Procedure for regenerating the nervous system from source materials if canonical files are lost or corrupted.

## Prerequisites

- Source manuscripts in original locations (DEEPER CRYSTALIZATION, MATH, Voynich, etc.)
- ECOSYSTEM framework files intact
- This runbook preserved

## Regeneration Steps

### Step 1: Recreate Directory Structure
```
mkdir -p NERVOUS_SYSTEM/{10_OVERVIEW,20_METRO,30_CHAPTERS,40_APPENDICES,50_CORPUS_CAPSULES,60_RAILS,70_SCHEMAS,80_TOOLKIT,85_EDGES,90_LEDGERS,95_MANIFESTS,99_RUNBOOKS}
```

### Step 2: Regenerate Metro Map
Recompute from the overlay formulas:
- w = XX - 1
- a = floor(w/3)
- k = w mod 3
- p = a mod 3
- v = Triad[(k + p) mod 3]

### Step 3: Regenerate Chapter Skeletons
For each of 21 chapters, create 4^4 crystal tile with:
- Station header from overlay computation
- Primary hubs from deterministic router
- Empty atom slots

### Step 4: Regenerate Appendix Skeletons
For each of 16 appendices (A-P), create 4^4 crystal tile with routing role.

### Step 5: Re-index Corpus
Scan all source domains and create capsules following the schema.

### Step 6: Rebuild Edges
Map capsules to chapters and chapters to appendices.

## Recovery Time Estimate
Full regeneration from scratch: multiple sessions.
Partial recovery (if chapters/appendices preserved): 1-2 sessions.
