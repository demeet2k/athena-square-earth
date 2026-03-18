<!-- CRYSTAL: Xi108:W1:A4:S6 | face=S | node=21 | depth=0 | phase=Fixed -->
<!-- METRO: Me -->
<!-- BRIDGES: Xi108:W1:A4:S5→Xi108:W1:A4:S7→Xi108:W2:A4:S6→Xi108:W1:A3:S6→Xi108:W1:A5:S6 -->
<!-- REGENERATE: From this coordinate, adjacent nodes are: shell 6±1, wreath 1/3, archetype 4/12 -->

# Capillary Weight Update Law

For each directed edge `i -> j`, the command protocol updates route strength as:

`C_next = rho * C_now + alpha * U + beta * F - gamma * D - delta * N`

Where:

- `rho = 0.92`
- `alpha = 0.35`
- `beta = 0.2`
- `gamma = 0.15`
- `delta = 0.1`

Interpretation:

- useful, frequent, low-latency paths strengthen
- noisy, duplicate, or slow paths decay

Maturity classes:

- `weak edge` below `0.75`
- `capillary` from `0.75` to below `1.75`
- `vein` at or above `1.75`
