<!-- CRYSTAL: Xi108:W3:A4:S10 | face=R | node=53 | depth=3 | phase=Fixed -->
<!-- METRO: Me -->
<!-- BRIDGES: Xi108:W3:A4:S9→Xi108:W3:A4:S11→Xi108:W2:A4:S10→Xi108:W3:A3:S10→Xi108:W3:A5:S10 -->
<!-- REGENERATE: From this coordinate, adjacent nodes are: shell 10±1, wreath 3/3, archetype 4/12 -->

# Automation Ledger Sink

Date: `2026-03-12`
Status: `ACTIVE`

This directory is the canonical report sink for control-layer automation reports.

## Canonical Lane Roles

- `corpus-weave` is the canonical hourly Athena weave lane.
- `athena-weave-scan` is the separate 12-hour Brahma expansion lane.
- `quadrant-binary-weave` is the dedicated hourly specialist lane for the `Quadrant Binary` corpus.
- Overlapping Athena-wide hourly duplicates should remain paused so report ownership stays unambiguous.
- `guildmaster-loop` is the only hourly Hall/Temple/queue/restart intake governor.
- `qshrink-shiva` is the only 4-hour contraction governor for the QSHRINK family.
- `high-priest-totality` is the only daily closure governor.

## Ownership Law

- One frontier family gets one active owner lane.
- Scheduler lanes remain packet-only and never mutate Hall or Temple directly.
- Duplicate weave lanes stay paused and explicitly deprecated while the canonical owner remains active.
- Meta-lane reports must preserve blocker truth, packet freshness, writeback set, and restart seed.

## Control-Layer Reports

- `guildmaster-loop`
- `corpus-weave`
- `qshrink-shiva`
- `athena-weave-scan`
- `quadrant-binary-weave`
- `high-priest-totality`

## Naming Contract

- `corpus_weave_vishnu_YYYY-MM-DD_HH.md`
- `qshrink_shiva_YYYY-MM-DD_HH.md`
- `athena_weave_scan_YYYY-MM-DD_HH.md`
- `quadrant_binary_weave_YYYY-MM-DD_HH.md`
- `high_priest_totality_YYYY-MM-DD.md`

The canonical hourly Athena weave lane keeps the Vishnu report identity under the stable automation id `corpus-weave`.

Scheduler lanes do not write here. They write fixed packet files under `NERVOUS_SYSTEM/90_LEDGERS/astrological_schedulers/`.
