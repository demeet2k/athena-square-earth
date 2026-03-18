<!-- CRYSTAL: Xi108:W1:A4:S5 | face=S | node=13 | depth=0 | phase=Fixed -->
<!-- METRO: Me -->
<!-- BRIDGES: Xi108:W1:A4:S4→Xi108:W1:A4:S6→Xi108:W2:A4:S5→Xi108:W1:A3:S5→Xi108:W1:A5:S5 -->
<!-- REGENERATE: From this coordinate, adjacent nodes are: shell 5±1, wreath 1/3, archetype 4/12 -->

# RoundTripCertPack_v0 Canonical Object

RoundTripCertPack_v0 is the portable proof that one row-level motion preserved law, or else named exactly what it lost. It consists of: Route (source, destination, family, trace, RouteMin, HubBudget), ScheduledThrows, Conservation (6 checks: shell, zoom, phase, archetype, face, mobius), ProofBundle (Canon, Route, Truth, Replay, Parity, Loss proofs), InvariantBundle (Gate, RouteMin, Truth, OverlayDebt, TerminalType, ReceiptDebt), BrainstemStateRef, Witnesses, Digest, CertClass, FinalVerdict, and SuccessorSeed.

## Key Objects
- CertClass: exact | law_equivalent | residualized | illegal
- FinalVerdict: pass | residualized | repair_routed | quarantine | fail
- Six conservation checks: shell (Delta-l=0), zoom (Delta-sigma=0), phase (Delta-r=0 mod 3), archetype (Delta-a=0 mod 12), face (Delta-lambda=0 mod 4), mobius (Delta-q=0 mod 2)
- ProofBundle: CanonProof, RouteProof, TruthProof, ReplayProof, ParityProof, LossProof
- SuccessorSeed: continuation object for lawful reseeding

## Key Laws
- A round-trip certificate is: replay succeeded AND six closure debts preserved or lawfully surfaced
- If the transform changed law but did not declare the loss, it is illegal
- Lawful motion = route + proof bundle + conservation check + successor seed
- The row becomes portable when its motion can be replayed, certified, and reseeded without silent law loss

## Source
- `29_ACCEPTED_INPUTS/2026-03-17_12d_structure.md`
