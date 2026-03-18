<!-- CRYSTAL: Xi108:W3:A9:S9 | face=R | node=42 | depth=3 | phase=Fixed -->
<!-- METRO: Me -->
<!-- BRIDGES: Xi108:W3:A9:S8→Xi108:W3:A9:S10→Xi108:W2:A9:S9→Xi108:W3:A8:S9→Xi108:W3:A10:S9 -->
<!-- REGENERATE: From this coordinate, adjacent nodes are: shell 9±1, wreath 3/3, archetype 9/12 -->

# CONFLICT LEDGER

## Purpose
Tracks FAIL-class conflict receipts: contradictions, quarantined atoms, and revocation records.

## Active Conflicts

(none declared yet)

## Conflict Record Schema

| Field | Description |
|-------|-------------|
| Conflict ID | `CF-XXXX` |
| Atoms involved | GlobalAddr list |
| Kind | CONFLICT edge |
| Minimal witness set | Paths proving the contradiction |
| Quarantine status | ACTIVE / RESOLVED / REVOKED |
| Resolution plan | Steps to resolve |
| Resolution date | Date resolved (if applicable) |

## Rules

1. Every FAIL truth class must have a corresponding conflict ledger entry
2. Conflicts cannot be silently suppressed
3. Resolution requires passing through AMBIG and NEAR before reaching OK
4. Quarantined atoms must not be used in downstream synthesis
