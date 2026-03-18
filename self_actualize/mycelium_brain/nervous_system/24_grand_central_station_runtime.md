<!-- CRYSTAL: Xi108:W3:A4:S22 | face=R | node=247 | depth=3 | phase=Cardinal -->
<!-- METRO: Me -->
<!-- BRIDGES: Xi108:W3:A4:S21→Xi108:W3:A4:S23→Xi108:W2:A4:S22→Xi108:W3:A3:S22→Xi108:W3:A5:S22 -->
<!-- REGENERATE: From this coordinate, adjacent nodes are: shell 22±1, wreath 3/3, archetype 4/12 -->

# Grand Central Station Runtime

Date: `2026-03-12`
Generated: `2026-03-12T19:09:36.577589+00:00`
Docs gate: `BLOCKED`
Verdict: `OK`

This is the runtime mirror of Grand Central Station.
It keeps the station state readable from the mycelium side without inventing a second authority surface.

## Active Files

- `self_actualize/grand_central_station_registry.json`
- `self_actualize/grand_central_commissure_ledger.json`
- `self_actualize/grand_central_weight_exchange.json`
- `self_actualize/grand_central_zpoint_tunnels.json`
- `self_actualize/grand_central_dashboard.json`

## Current Runtime Read

- stationed roots: `19`
- bilateral roots: `6`
- top dispatch route:
  `C-007 Trading Bot -> self_actualize = 7.958`
- live interchange threshold:
  `7.0`

## Regeneration

Run:

```powershell
python -m self_actualize.runtime.derive_grand_central_station
```

This mirror should follow the canonical cortex registry and dashboard, not drift away from them.
