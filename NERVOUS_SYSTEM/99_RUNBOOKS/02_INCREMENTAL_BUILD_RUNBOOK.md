<!-- CRYSTAL: Xi108:W3:A11:S11 | face=R | node=62 | depth=3 | phase=Fixed -->
<!-- METRO: Me,T -->
<!-- BRIDGES: Xi108:W3:A11:S10→Xi108:W3:A11:S12→Xi108:W2:A11:S11→Xi108:W3:A10:S11→Xi108:W3:A12:S11 -->
<!-- REGENERATE: From this coordinate, adjacent nodes are: shell 11±1, wreath 3/3, archetype 11/12 -->

# INCREMENTAL BUILD RUNBOOK

## Purpose
Guide for incrementally extending the nervous system one domain or chapter at a time.

## Adding a New Domain

1. Create subdirectory in `50_CORPUS_CAPSULES/[domain_name]/`
2. For each major source surface in the domain:
   a. Read the source document
   b. Create a capsule file following `70_SCHEMAS/03_CAPSULE_SCHEMA.md`
   c. Assign capsule_id (CC-XXXX, incrementing)
   d. Map to chapter tile slots using the deterministic router
   e. Record in domain INDEX.md
3. Update `50_CORPUS_CAPSULES/INDEX.md`
4. Update `95_MANIFESTS/SOURCE_SURFACE_ATLAS.md`
5. Record promotion in `90_LEDGERS/PROMOTION_LEDGER.md`

## Populating a Chapter Tile

1. Read the chapter file from `30_CHAPTERS/`
2. Read all capsules listed in the chapter's `## Source capsules` section
3. For each capsule, extract content matching the chapter's theme
4. Assign extracted content to specific `<Lens><Facet>.<Atom>` slots
5. Update the chapter file with slot content
6. Record the promotion in `90_LEDGERS/PROMOTION_LEDGER.md`
7. Update obligations in `90_LEDGERS/OBLIGATIONS_LEDGER.md`

## Adding an Edge

1. Identify the source and destination atoms
2. Determine the edge kind from K
3. Record in the appropriate `85_EDGES/` file
4. Assign truth class (default: AMBIG)
5. If witness exists, record WitnessPtr
