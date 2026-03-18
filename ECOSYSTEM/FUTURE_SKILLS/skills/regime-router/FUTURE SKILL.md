<!-- CRYSTAL: Xi108:W3:A6:S30 | face=F | node=441 | depth=3 | phase=Mutable -->
<!-- METRO: Me -->
<!-- BRIDGES: Xi108:W3:A6:S29→Xi108:W3:A6:S31→Xi108:W2:A6:S30→Xi108:W3:A5:S30→Xi108:W3:A7:S30 -->
<!-- REGENERATE: From this coordinate, adjacent nodes are: shell 30±1, wreath 3/3, archetype 6/12 -->

# regime-router

## address
2121

## priority
P0

## lane
runtime

## description
Infer the active regime for a task and rebalance route strategy, evidence weighting, and lens mix accordingly.

## triggers
- regime router
- route this
- map the dependencies
- where does this belong

## inputs
- runtime contracts
- route packets
- ledger or profile data

## outputs
- evaluation artifact
- measured results
- follow-up recommendations

## procedure
1. Parse the active objective and source surfaces.
2. Compute the most lawful route or dependency ordering.
3. Preserve any unresolved ambiguity instead of forcing collapse.
4. Emit the route artifact and the next recommended move.

## validation
- results are measured against a named surface
- failures remain inspectable after the run

## failure modes
- If multiple routes compete, keep the shortlist instead of forcing one path.
- If the route depends on missing evidence, surface the dependency as a blocker.

## references
- `C:\Users\dmitr\Documents\Athena Agent\self_actualize\regime_profiles.json`
- `C:\Users\dmitr\Documents\Athena Agent\MATH\FINAL FORM\Hybrid Equations\HYBRIDIZATION_COMPLETE_GUIDE.md`

## rationale
The corpus explicitly rejects one globally best strategy.
