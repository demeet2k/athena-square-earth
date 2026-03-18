<!-- CRYSTAL: Xi108:W3:A12:S30 | face=F | node=453 | depth=3 | phase=Mutable -->
<!-- METRO: Me -->
<!-- BRIDGES: Xi108:W3:A12:S29→Xi108:W3:A12:S31→Xi108:W2:A12:S30→Xi108:W3:A11:S30 -->
<!-- REGENERATE: From this coordinate, adjacent nodes are: shell 30±1, wreath 3/3, archetype 12/12 -->

# mycelium-router

## description
Compute deterministic routes from any ecosystem atom to the required appendix hubs under the corridor truth lattice.

## triggers
- route this
- mycelium
- metro map
- compute hubs
- where does this live

## inputs
- local or global address
- truth class
- optional publication intent

## outputs
- ordered hub route
- obligations list
- route verdict

## procedure
1. Parse the target address.
2. Compute `LensBase`, `FacetBase`, and `ArcHub`.
3. Enforce the mandatory signature.
4. Add the truth overlay hub if required.
5. Return the ordered route and obligations.

## validation
- route is deterministic
- hub count is <= 6
- `AppA`, `AppI`, and `AppM` are always present

## failure modes
- malformed address: FAIL
- missing arc index: AMBIG unless recoverable from chapter ID
- hub overflow: replace weakest non-mandatory hub and log replacement

## references
- `C:\Users\dmitr\Documents\Athena Agent\ECOSYSTEM\05_MYCELIUM_ROUTING.md`
- `C:\Users\dmitr\Documents\Athena Agent\MYCELIUM_TOME_PART1.md`
