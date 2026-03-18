<!-- CRYSTAL: Xi108:W1:A4:S4 | face=S | node=8 | depth=0 | phase=Fixed -->
<!-- METRO: Me -->
<!-- BRIDGES: Xi108:W1:A4:S3→Xi108:W1:A4:S5→Xi108:W2:A4:S4→Xi108:W1:A3:S4→Xi108:W1:A5:S4 -->
<!-- REGENERATE: From this coordinate, adjacent nodes are: shell 4±1, wreath 1/3, archetype 4/12 -->

# 12D Liminal Coordinate Schema

Command packets carry a 12-dimensional coordinate tuple. Each slot is persisted as a normalized scalar in `[0,1]` plus a named stamp.

1. `utc_time_fraction`
2. `local_earth_rotation_phase`
3. `earth_orbital_phase`
4. `local_node_anchor`
5. `solar_phase`
6. `lunar_phase`
7. `sidereal_phase`
8. `sky_anchor_slot`
9. `runtime_node_anchor`
10. `queue_pressure`
11. `goal_salience_vector`
12. `novelty_routing_concentration`

The first eight dimensions provide Earth and astro anchoring. The last four encode runtime and liminal state.

- Prompt-level liminal GPS: `supported now`
- Keystroke-level liminal GPS: `future instrumentation only`
