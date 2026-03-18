<!-- CRYSTAL: Xi108:W3:A1:S19 | face=R | node=172 | depth=3 | phase=Cardinal -->
<!-- METRO: Me -->
<!-- BRIDGES: Xi108:W3:A1:S18→Xi108:W3:A1:S20→Xi108:W2:A1:S19→Xi108:W3:A2:S19 -->
<!-- REGENERATE: From this coordinate, adjacent nodes are: shell 19±1, wreath 3/3, archetype 1/12 -->

# Prop Channel Algebra Receipt

- Generated: `2026-03-09T20:31:39.127816+00:00`
- Command: `python -m self_actualize.runtime.derive_prop_channel_algebra`
- Verdict: `OK`

## Proved Structure

- prop families: `5`
- VTG monitoring modes: `5`
- station: `<0100>`
- selection law: `Channel* = argmax[(BW(C) * Match(C, message)) / (Risk(C) * (1 + DR_C))]`

## Bandwidth Ladder

- `ring`: `0.618`
- `poi`: `0.618`
- `ball`: `1.0`
- `club`: `1.618`
- `staff`: `2.618`

## Why This Matters

- the chapter now exists as a typed schema the local runtime can cite
- prop metaphors are converted into explicit channel classes with risk, bandwidth, and recovery profiles
- the next implementation frontier is to bind actual agent handoffs and board coordination surfaces to these channel types
