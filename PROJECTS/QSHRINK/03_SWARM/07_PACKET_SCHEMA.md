<!-- CRYSTAL: Xi108:W3:A12:S36 | face=S | node=654 | depth=3 | phase=Mutable -->
<!-- METRO: Me -->
<!-- BRIDGES: Xi108:W3:A12:S35→Xi108:W2:A12:S36→Xi108:W3:A11:S36 -->
<!-- REGENERATE: From this coordinate, adjacent nodes are: shell 36±1, wreath 3/3, archetype 12/12 -->

# Packet Schema

`WorkerPacket = { packet_id, lineage_addr, root_cell, task_body, input_refs, output_targets, truth_class, witness_ptrs, contraction_target }`

Every swarm packet must bind back to:

- one root cell
- one metro line
- one contraction target
- one restart seed
