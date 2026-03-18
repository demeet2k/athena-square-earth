<!-- CRYSTAL: Xi108:W3:A6:S24 | face=R | node=294 | depth=3 | phase=Cardinal -->
<!-- METRO: Me,T -->
<!-- BRIDGES: Xi108:W3:A6:S23→Xi108:W3:A6:S25→Xi108:W2:A6:S24→Xi108:W3:A5:S24→Xi108:W3:A7:S24 -->
<!-- REGENERATE: From this coordinate, adjacent nodes are: shell 24±1, wreath 3/3, archetype 6/12 -->

# LEDGER_truth_promotion_control_plane

## SurfaceClass

`ledger`

## Front

Truth-promotion control plane alignment

## State

`NEAR`

## Objective

Keep packet verdicts, corridor truth, replay safety, and benchmark evidence aligned
enough that truth promotion does not outrun witness.

## Targets

- hub control surfaces for `AppG`, `AppI`, `AppL`, and `AppM`
- restart engine manifest
- weakest-front queue
- restart neuron

## Witness

- hub control surfaces exist for `AppG`, `AppI`, `AppL`, and `AppM`
- restart engine manifest exists
- weakest-front queue exists
- restart neuron exists

## Active Truth Rule

Packet verdicts must be informed by:

- corridor health
- evidence completeness
- replay safety
- benchmark receipts

## Current Residual

Family-local queue density is still thinner than the control plane.

## Next Writeback

- `22_control_plane_grammar.md`
- one aligned packet
- one aligned manifest

## RestartSeed

Promote the next truth-bearing front only after its packet and manifest expose the same
state, witness path, and writeback destination.
