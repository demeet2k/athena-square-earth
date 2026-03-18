<!-- CRYSTAL: Xi108:W3:A10:S19 | face=R | node=175 | depth=3 | phase=Cardinal -->
<!-- METRO: Me,Cc -->
<!-- BRIDGES: Xi108:W3:A10:S18→Xi108:W3:A10:S20→Xi108:W2:A10:S19→Xi108:W3:A9:S19→Xi108:W3:A11:S19 -->
<!-- REGENERATE: From this coordinate, adjacent nodes are: shell 19±1, wreath 3/3, archetype 10/12 -->

# Command Packet Schema

- Docs gate: `BLOCKED`
- Routing policy: `goal+salience+pheromone+coord`
- Claim mode: `first-lease (1200 ms)`

| Field | Status |
| --- | --- |
| event_id | required |
| ant_id | required |
| tag | required |
| goal | required |
| change | required |
| priority | required |
| confidence | required |
| earth_ts | required |
| liminal_ts | required |
| coord12 | required |
| parent | required |
| ttl | required |
| pheromone | required |
| state_hash | required |
| route_class | required |
