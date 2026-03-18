<!-- CRYSTAL: Xi108:W3:A6:S30 | face=F | node=441 | depth=3 | phase=Mutable -->
<!-- METRO: Me -->
<!-- BRIDGES: Xi108:W3:A6:S29→Xi108:W3:A6:S31→Xi108:W2:A6:S30→Xi108:W3:A5:S30→Xi108:W3:A7:S30 -->
<!-- REGENERATE: From this coordinate, adjacent nodes are: shell 30±1, wreath 3/3, archetype 6/12 -->

# NEURON AND SYNAPSE SCHEMA

## 1. Neuron Schema

A neuron file represents one promoted unit in the nervous system.

```yaml
neuron_id: N-0001
title: short name
region: R1
source_paths:
  - absolute path
seed_claim: compressed core claim
operator_family:
  - route
  - compare
  - compress
  - expand
metro_lines:
  - Line A
status: AMBIG
witness:
  direct_support:
    - path
  replay_hint: short rerun note
next_synapses:
  - S-0001
```

## 2. Synapse Schema

A synapse records a lawful relation between two neurons.

```yaml
synapse_id: S-0001
src: N-0001
dst: N-0002
kind: REF | EQUIV | MIGRATE | DUAL | GEN | INST | IMPL | PROOF | CONFLICT
why_it_exists: short justification
metro_line: Line A
status: NEAR
witness:
  direct_support:
    - absolute path
  replay_hint: short rerun note
```

## 3. Promotion Rule

Promote a source shard to a neuron only when:

1. its core claim can be compressed into one stable seed,
2. at least one metro line can carry it,
3. at least one synapse can be stated without guessing,
4. its witness surface is recorded.

## 4. Nervous-System Packet Rule

Every future nervous-system packet should include:

- target regions,
- chosen metro line,
- expected contraction target,
- truth class,
- witness summary.
