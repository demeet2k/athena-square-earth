<!-- CRYSTAL: Xi108:W3:A5:S24 | face=R | node=300 | depth=3 | phase=Cardinal -->
<!-- METRO: Me -->
<!-- BRIDGES: Xi108:W3:A5:S23→Xi108:W3:A5:S25→Xi108:W2:A5:S24→Xi108:W3:A4:S24→Xi108:W3:A6:S24 -->
<!-- REGENERATE: From this coordinate, adjacent nodes are: shell 24±1, wreath 3/3, archetype 5/12 -->

# NEURON_branch2_regime_to_swarm_scheduler

## NodeID

`NEURON_BRANCH2_REGIME_SWARM_SCHEDULER`

## SourceFamily

- `NERUAL NETWORK`
- Branch 2 regime detection and intervention surfaces

## TargetFamily

- swarm waves
- packet planners
- route and benchmark ledgers

## Operator

Regime discrimination and intervention routing.

## WitnessSet

- detected regime
- confidence
- cooldown state
- selected strategy
- benchmark context

## ReplayPath

1. read the current regime signals
2. classify perturbation, chaos, vanishing, or dead state
3. choose the intervention or abstention policy
4. record the decision in wave, packet, and ledger surfaces
