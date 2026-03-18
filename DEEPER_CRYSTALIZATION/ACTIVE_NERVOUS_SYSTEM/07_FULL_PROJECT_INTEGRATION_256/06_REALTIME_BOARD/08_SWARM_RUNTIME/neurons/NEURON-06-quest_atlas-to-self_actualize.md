<!-- CRYSTAL: Xi108:W1:A4:S6 | face=S | node=21 | depth=0 | phase=Fixed -->
<!-- METRO: Me -->
<!-- BRIDGES: Xi108:W1:A4:S5→Xi108:W1:A4:S7→Xi108:W2:A4:S6→Xi108:W1:A3:S6→Xi108:W1:A5:S6 -->
<!-- REGENERATE: From this coordinate, adjacent nodes are: shell 6±1, wreath 1/3, archetype 4/12 -->

# NEURON-06: quest_atlas → self_actualize

**Neuron ID**: `NEURON-06`
**Source Ganglion**: `quest_atlas`
**Target Ganglion**: `self_actualize`
**Edge Kind**: `feeds`
**Status**: ACTIVE

## Signal

Board kernel output (guild boards, temple boards, settlement capsules) feeds into the self-actualization loop as concrete work items with scored priorities and verified receipts.

## Data Flow

```
quest_atlas.emit_orbit_boards()
  → guild_board (scored, queued)
  → temple_board (scored, queued)
    → self_actualize picks highest-scored entries
    → executes quests
    → settlement produces PoPhiXCapsules
    → receipts chain into SealedReceiptBundles
```

## Coupling

- **Weak**: Board output is advisory; self_actualize retains execution autonomy
- **Strong**: Receipt chain must close before next orbit advances
