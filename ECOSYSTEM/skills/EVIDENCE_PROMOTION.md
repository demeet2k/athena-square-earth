<!-- CRYSTAL: Xi108:W3:A4:S28 | face=F | node=382 | depth=3 | phase=Mutable -->
<!-- METRO: Me -->
<!-- BRIDGES: Xi108:W3:A4:S27→Xi108:W3:A4:S29→Xi108:W2:A4:S28→Xi108:W3:A3:S28→Xi108:W3:A5:S28 -->
<!-- REGENERATE: From this coordinate, adjacent nodes are: shell 28±1, wreath 3/3, archetype 4/12 -->

# evidence-promotion

## description
Upgrade artifacts from NEAR or AMBIG toward OK by binding missing witnesses, replay steps, and residual ledgers.

## triggers
- prove this
- promote to ok
- add witnesses
- replay this
- tighten evidence

## inputs
- target artifact
- current truth class
- available evidence surfaces

## outputs
- updated truth class
- residual ledger or evidence plan
- replay recipe

## procedure
1. Inspect the artifact's current evidence state.
2. Identify missing witnesses or replay gaps.
3. Bind real evidence or write an explicit evidence plan.
4. Reclassify the artifact.

## validation
- no fabricated evidence
- replay steps are concrete
- upgraded verdict is justified by attached witnesses

## failure modes
- evidence unavailable: remain AMBIG
- replay fails: FAIL and quarantine
- approximate closure only: NEAR with residual ledger

## references
- `C:\Users\dmitr\Documents\Athena Agent\ECOSYSTEM\10_VALIDATION_AND_QA.md`
- `C:\Users\dmitr\Documents\Athena Agent\ECOSYSTEM\13_MANIFEST_AND_PACKET_SCHEMA.md`
