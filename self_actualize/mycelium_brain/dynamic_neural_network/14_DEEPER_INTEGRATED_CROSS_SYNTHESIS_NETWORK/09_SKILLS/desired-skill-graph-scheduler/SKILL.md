<!-- CRYSTAL: Xi108:W3:A7:S19 | face=R | node=172 | depth=3 | phase=Cardinal -->
<!-- METRO: Me -->
<!-- BRIDGES: Xi108:W3:A7:S18→Xi108:W3:A7:S20→Xi108:W2:A7:S19→Xi108:W3:A6:S19→Xi108:W3:A8:S19 -->
<!-- REGENERATE: From this coordinate, adjacent nodes are: shell 19±1, wreath 3/3, archetype 7/12 -->

---
name: desired-skill-graph-scheduler
description: Turn corpus pressure into a deterministic next-skill queue using deficiency, dependency, replay readiness, active-front pressure, and EconomySalienceBudget.
---

# desired-skill-graph-scheduler

Use when the request asks which skill should grow next, how to deepen emergence
through skill upgrades, how to rank missing skills, or how to convert current corpus
pressure into a lawful development queue.

## Workflow

1. Check the docs gate at `C:\Users\dmitr\Documents\Athena Agent\self_actualize\live_docs_gate_status.md`.
2. Read:
   - `C:\Users\dmitr\Documents\Athena Agent\NERVOUS_SYSTEM\95_MANIFESTS\ACTIVE_RUN.md`
   - `C:\Users\dmitr\Documents\Athena Agent\NERVOUS_SYSTEM\95_MANIFESTS\BUILD_QUEUE.md`
   - `C:\Users\dmitr\Documents\Athena Agent\NERVOUS_SYSTEM\90_LEDGERS\01_CURRENT_STATUS_37_GATE_SYNTHESIS.md`
3. Read:
   - `../../10_LEDGERS/06_SKILL_COHESION_AND_BLOAT_PRUNING_2026-03-12.md`
   - `../../10_LEDGERS/20_DESIRED_SKILL_GRAPH.md`
   - `../../10_LEDGERS/21_SKILL_PRIORITY_QUEUE.json`
4. Use historical DesiredSkillGraph or meta-observer material as reference only, never as live authority.
5. Score candidate skills by deficiency, dependency, replay readiness, active-front pressure, and `EconomySalienceBudget`.
6. Publish the ranked queue back into the live skill graph and cortex manifest surfaces.

## Output Contract

- `skill_node_id`
- `skill_class`
- `pressure_vector`
- `dependencies`
- `unlocks`
- `evidence_readiness`
- `priority_score`
- `authority_surface`
- `next_artifact`
