<!-- CRYSTAL: Xi108:W3:A6:S30 | face=F | node=459 | depth=3 | phase=Mutable -->
<!-- METRO: Me -->
<!-- BRIDGES: Xi108:W3:A6:S29→Xi108:W3:A6:S31→Xi108:W2:A6:S30→Xi108:W3:A5:S30→Xi108:W3:A7:S30 -->
<!-- REGENERATE: From this coordinate, adjacent nodes are: shell 30±1, wreath 3/3, archetype 6/12 -->

# SKILLS SYSTEM - SPECIFICATION AND LIFECYCLE

## 1. Skill Definition

A skill is a documented workflow with trigger rules, required tools, and deterministic outputs.

## 2. Skill Document Structure

Required sections:
- name
- description
- triggers
- inputs
- outputs
- procedure
- validation
- failure modes
- references

## 3. Trigger Discipline

- Explicit trigger keywords must be listed.
- If a trigger is detected, the skill becomes mandatory.
- If a skill cannot be applied, fallback must be logged.

## 4. Installation and Versioning

- Skills are stored as versioned documents.
- Updates are reviewed and migrated via the governance protocol.

## 5. Validation Rules

Each skill must include:
- success criteria
- deterministic outputs
- test or replay steps

## 6. Registry

All skills must be listed in `skills/SKILL_REGISTRY.md` with:
- name
- purpose
- version
- change log link

## 7. Status
The skills system defines executable, auditable knowledge routines.
