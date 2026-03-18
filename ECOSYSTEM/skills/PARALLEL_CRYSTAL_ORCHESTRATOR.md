<!-- CRYSTAL: Xi108:W3:A4:S26 | face=F | node=337 | depth=3 | phase=Mutable -->
<!-- METRO: Me -->
<!-- BRIDGES: Xi108:W3:A4:S25→Xi108:W3:A4:S27→Xi108:W2:A4:S26→Xi108:W3:A3:S26→Xi108:W3:A5:S26 -->
<!-- REGENERATE: From this coordinate, adjacent nodes are: shell 26±1, wreath 3/3, archetype 4/12 -->

# parallel-crystal-orchestrator

## description
Expand a task into a lawful 4^4 crystal, schedule the work in waves, and contract the outputs back into one replay-safe artifact.

## triggers
- run in parallel
- split into agents
- 4^4 crystal
- expand into earth water fire air
- do not stop

## inputs
- objective statement
- source corpus paths
- optional frontier limit
- optional depth cap

## outputs
- run manifest
- packet set
- contraction artifact
- next frontier recommendation

## procedure
1. Normalize the objective into a single sentence.
2. Expand the task using the elemental split and assign addresses.
3. Emit work packets for the active wave.
4. Validate packet outputs with corridor truth.
5. Contract the completed wave into a synthesis artifact.
6. Emit the next wave or a lawful stop condition.

## validation
- every packet has a unique ID
- every packet has an address
- every packet has witness or explicit AMBIG status
- contraction preserves address continuity

## failure modes
- missing witnesses: classify AMBIG
- contradictory outputs: emit CONFLICT and quarantine
- overlapping writes: freeze one packet and reroute

## references
- `C:\Users\dmitr\Documents\Athena Agent\ECOSYSTEM\06_AGENT_CRYSTAL_ECOSYSTEM.md`
- `C:\Users\dmitr\Documents\Athena Agent\ECOSYSTEM\12_PARALLEL_ORCHESTRATION_PROTOCOL.md`
- `C:\Users\dmitr\Documents\Athena Agent\ECOSYSTEM\13_MANIFEST_AND_PACKET_SCHEMA.md`
