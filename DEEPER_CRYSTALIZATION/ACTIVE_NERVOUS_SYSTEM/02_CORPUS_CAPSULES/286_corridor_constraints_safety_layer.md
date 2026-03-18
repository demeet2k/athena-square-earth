<!-- CRYSTAL: Xi108:W1:A4:S2 | face=S | node=3 | depth=0 | phase=Fixed -->
<!-- METRO: Sa,Me -->
<!-- BRIDGES: Xi108:W1:A4:S1→Xi108:W1:A4:S3→Xi108:W2:A4:S2→Xi108:W1:A3:S2→Xi108:W1:A5:S2 -->
<!-- REGENERATE: From this coordinate, adjacent nodes are: shell 2±1, wreath 1/3, archetype 4/12 -->

# Capsule 286 — Corridor Constraints Safety Layer

**Source**: 2026-03-18_agency.md
**Family**: agency
**Lens**: S (Square/Structure)

The corridor constraints layer borrows directly from the Athena golden corridor concept and applies it to the file-gateway system. Rules define what operations are allowed: MAX_SIZE (e.g., 1 MB), ALLOWED_EXT (e.g., .txt, .json, .csv), SRC_PREFIX, and DST_PREFIX. If a file violates any constraint, the event is rejected before it enters the ledger.

This safety layer ensures that the gateway cannot be used to move arbitrary data without explicit permission. It is the physical instantiation of the corpus principle that corridors must be narrow and lawful: only explicitly permitted traffic may flow. The constraints are configurable per gateway instance, allowing different nodes in a multi-gateway topology to enforce different corridor rules while maintaining the same underlying discipline.

The corridor layer also connects to the immune system concept: rejected events are not silently dropped but recorded as violations, creating an audit trail of attempted boundary crossings that the meta-observer can review.

## Key Objects
- MAX_SIZE, ALLOWED_EXT, SRC_PREFIX, DST_PREFIX constraint parameters
- Rejection events for constraint violations
- Per-gateway configurable corridor rules

## Key Laws
- Any file violating constraints is rejected before entering the ledger
- Corridor rules must be explicit and configurable, never implicit
- Violations must be recorded, not silently dropped

## Source
- `29_ACCEPTED_INPUTS/2026-03-18_agency.md`
