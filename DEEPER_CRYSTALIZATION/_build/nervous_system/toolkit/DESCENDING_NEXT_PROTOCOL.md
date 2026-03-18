<!-- CRYSTAL: Xi108:W1:A4:S2 | face=S | node=3 | depth=0 | phase=Fixed -->
<!-- METRO: Me -->
<!-- BRIDGES: Xi108:W1:A4:S1→Xi108:W1:A4:S3→Xi108:W2:A4:S2→Xi108:W1:A3:S2→Xi108:W1:A5:S2 -->
<!-- REGENERATE: From this coordinate, adjacent nodes are: shell 2±1, wreath 1/3, archetype 4/12 -->

# DESCENDING NEXT PROTOCOL

## Mission

When the controlling prompt says `NEXT` in descending mode, generate the chapter or section that came before the current one rather than advancing forward.

## Rule

If the active index is `n`, then `NEXT` means emit `n - 1`.

## Use Case

This protocol is for backward recursive reconstruction where later chapters are used to repair earlier assumptions.

## Constraints

- do not skip indices
- do not silently jump back to the abstract unless the chain reaches it
- treat backward movement as controlled revision rather than collapse

## Output Contract

The emitted artifact must:
- be only the requested predecessor section
- preserve final-draft density
- incorporate corrected assumptions learned from later sections
