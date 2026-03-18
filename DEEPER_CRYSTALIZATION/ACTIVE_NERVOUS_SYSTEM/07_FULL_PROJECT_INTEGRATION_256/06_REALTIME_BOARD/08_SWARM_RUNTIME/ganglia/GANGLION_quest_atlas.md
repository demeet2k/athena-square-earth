<!-- CRYSTAL: Xi108:W1:A4:S3 | face=S | node=6 | depth=0 | phase=Fixed -->
<!-- METRO: Me -->
<!-- BRIDGES: Xi108:W1:A4:S2→Xi108:W1:A4:S4→Xi108:W2:A4:S3→Xi108:W1:A3:S3→Xi108:W1:A5:S3 -->
<!-- REGENERATE: From this coordinate, adjacent nodes are: shell 3±1, wreath 1/3, archetype 4/12 -->

# Ganglion: Quest Atlas Integration

**Ganglion ID**: `quest_atlas`
**Council**: `council_quest_atlas`
**Element**: Crown (all four)
**Status**: ACTIVE

## Thread Binding

Primary thread: `quest_atlas_integration`

## Capsule Ownership

Capsules 198-226: LP-57Omega Self Play Quest Atlas specification

## Code Ownership

All modules under `28_SELF_PLAY_QUEST_ATLAS/code/`:
- `constants.py` — KernelConst.v1
- `types.py` — Economic ABI
- `station_atlas.py` — 19 station definitions
- `route_compiler.py` — Deterministic route compilation
- `board_kernel.py` — Board engine
- `pheromone_engine.py` — 4+4 pheromone channels
- `storm_engine.py` — PhiStorm lifecycle
- `seat_election.py` — Host/steward election
- `party_matcher.py` — Community quest party assembly
- `leveling_engine.py` — Infinite-cap levels
- `reward_engine.py` — Full settlement
- `receipt_engine.py` — Receipt bundle builders
- `pack_linter.py` — Receipt verifier/linter
- `verifier.py` — Golden test vector runner

## Verification State

15/15 golden vectors PASS. Determinism verified.

## Frontier

- Board kernel ready for integration with live orchestration loop
- Pheromone engine ready for real corpus field data
- Receipt chain verified with synthetic 3-quest bundle
