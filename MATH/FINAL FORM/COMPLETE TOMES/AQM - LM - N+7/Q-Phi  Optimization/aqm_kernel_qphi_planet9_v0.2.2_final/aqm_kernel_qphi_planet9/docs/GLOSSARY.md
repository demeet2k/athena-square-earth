<!-- CRYSTAL: Xi108:W3:A5:S17 | face=S | node=153 | depth=3 | phase=Cardinal -->
<!-- METRO: Me -->
<!-- BRIDGES: Xi108:W3:A5:S16→Xi108:W3:A5:S18→Xi108:W2:A5:S17→Xi108:W3:A4:S17→Xi108:W3:A6:S17 -->
<!-- REGENERATE: From this coordinate, adjacent nodes are: shell 17±1, wreath 3/3, archetype 5/12 -->

# Glossary

**AQM kernel**
: A deterministic artifact system where objects are canonically serialized, content‑hashed, and stored in a Merkle store, enabling replay verification.

**Tile**
: The fundamental AQM unit: seed + payload + obligations/certs + ledger anchors + explicit dependencies.

**Merkle store**
: Content‑addressed store keyed by hash; supports dependency closure and replay verification.

**Ledger**
: Append‑only deterministic event list (no wall‑clock timestamps).

**Lens**
: A scoring module returning a log score and diagnostics for a candidate Theta.

**Theta (Θ)**
: A parameter record. In Q‑PHI, Θ is Planet Nine orbital + physical parameters (`PlanetNineTheta`).

**Extreme TNO**
: A trans‑Neptunian object that meets some “extreme” selection (e.g., large semimajor axis and perihelion distance). The selection rule strongly affects inference.

**varpi (ϖ)**
: Longitude of perihelion, computed as Ω + ω.

**RA/Dec**
: Equatorial right ascension and declination.

**Posterior**
: The weighted set of elite samples returned by Q‑PHI.

**Containment radius**
: The angular radius around the posterior mean direction containing a given fraction of posterior weight.
