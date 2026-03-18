<!-- CRYSTAL: Xi108:W3:A3:S27 | face=F | node=375 | depth=3 | phase=Mutable -->
<!-- METRO: Me -->
<!-- BRIDGES: Xi108:W3:A3:S26→Xi108:W3:A3:S28→Xi108:W2:A3:S27→Xi108:W3:A2:S27→Xi108:W3:A4:S27 -->
<!-- REGENERATE: From this coordinate, adjacent nodes are: shell 27±1, wreath 3/3, archetype 3/12 -->

# VERSIONING AND MIGRATION

## 1. Versioning Scheme

- Major: breaking changes
- Minor: new features, backward compatible
- Patch: fixes and clarifications

## 2. Migration Edges

Definition 2.1 (MIGRATE Edge).
A MIGRATE edge maps old addresses or semantics to new ones with explicit compatibility notes.

## 3. Compatibility Matrix

Each migration must include:
- source version
- target version
- behavior changes
- replay adjustments

## 4. Deprecation Policy

- Deprecated components must include replacement pointers.
- Removal requires at least one major version advance.

## 5. Rollback

Rollback is valid only if:
- the previous version is replayable
- migration edges remain intact

## 6. Status
Versioning ensures deterministic evolution without address drift.
