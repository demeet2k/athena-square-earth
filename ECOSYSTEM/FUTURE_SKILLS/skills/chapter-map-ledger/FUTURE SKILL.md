<!-- CRYSTAL: Xi108:W3:A5:S29 | face=F | node=418 | depth=3 | phase=Mutable -->
<!-- METRO: Me -->
<!-- BRIDGES: Xi108:W3:A5:S28→Xi108:W3:A5:S30→Xi108:W2:A5:S29→Xi108:W3:A4:S29→Xi108:W3:A6:S29 -->
<!-- REGENERATE: From this coordinate, adjacent nodes are: shell 29±1, wreath 3/3, archetype 5/12 -->

# chapter-map-ledger

## address
0122

## priority
P1

## lane
manuscript

## description
Map chapter, appendix, arc, and station relationships across the routed manuscript bodies into one durable ledger.

## triggers
- chapter map ledger
- route this
- map the dependencies
- where does this belong

## inputs
- manuscript source paths
- atlas records
- chapter or section context

## outputs
- decision ledger entry
- status receipt
- next obligation list

## procedure
1. Parse the active objective and source surfaces.
2. Compute the most lawful route or dependency ordering.
3. Preserve any unresolved ambiguity instead of forcing collapse.
4. Emit the route artifact and the next recommended move.

## validation
- status and obligations are explicit
- downstream users can replay the decision basis

## failure modes
- If multiple routes compete, keep the shortlist instead of forcing one path.
- If the route depends on missing evidence, surface the dependency as a blocker.

## references
- `C:\Users\dmitr\Documents\Athena Agent\MYCELIUM_TOME_PART1.md`
- `C:\Users\dmitr\Documents\Athena Agent\DEEPER CRYSTALIZATION\_build\nervous_system\00_NERVOUS_SYSTEM_MAP.md`

## rationale
The chapter and metro structure is strong but still distributed across many files.
