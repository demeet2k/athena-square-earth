<!-- CRYSTAL: Xi108:W3:A12:S12 | face=R | node=78 | depth=3 | phase=Fixed -->
<!-- METRO: Me -->
<!-- BRIDGES: Xi108:W3:A12:S11→Xi108:W3:A12:S13→Xi108:W2:A12:S12→Xi108:W3:A11:S12 -->
<!-- REGENERATE: From this coordinate, adjacent nodes are: shell 12±1, wreath 3/3, archetype 12/12 -->

﻿# Section Final Draft Protocol v4.3

Status: Canonical section-local drafting protocol.
Scope: one section only.

## Purpose

This protocol governs final-draft generation for exactly one chapter section, appendix section, or tightly bounded subsection.

## Selection Rule

Use this protocol for one section only. Do not use it for whole-corpus synthesis or title/abstract generation.

## Prime Directive

Produce the final manuscript-grade draft of the requested section only.

## Live Corpus Rule

1. Attempt live Google Docs search first.
2. If the Docs gate is blocked, preserve `BLOCKED` honestly and fall back to the best local corpus witness.
3. Do not claim a live-docs pass when `Trading Bot/credentials.json` or `Trading Bot/token.json` is missing.

## Tesseract Development Pass

Rotate every section through `S -> F -> C -> R`:
- Square: definitions, structure, exact objects
- Flower: transformations and relations
- Cloud: admissibility, uncertainty, edge cases
- Fractal: recursion, compression, regeneration

## Output Contract

- stay inside the requested section boundary
- avoid previewing future sections unless explicitly requested
- improve rigor and sequencing beyond the seed
- end with the section chapter or appendix name as the organizational footer
