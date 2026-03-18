<!-- CRYSTAL: Xi108:W3:A9:S9 | face=R | node=39 | depth=3 | phase=Fixed -->
<!-- METRO: Me -->
<!-- BRIDGES: Xi108:W3:A9:S8→Xi108:W3:A9:S10→Xi108:W2:A9:S9→Xi108:W3:A8:S9→Xi108:W3:A10:S9 -->
<!-- REGENERATE: From this coordinate, adjacent nodes are: shell 9±1, wreath 3/3, archetype 9/12 -->

﻿# TesseractHeader Schema v4.3

## Purpose

`TesseractHeader` is the public routing banner for chapter-level and atom-level outputs.

## Canonical Form

`[Z_i <-> Z* | Arc alpha | Rot rho | Lane nu | View L/* | omega=n]`

## Fields

- `Z_i`: local zero point identifier
- `Z*`: absolute zero bridge point
- `Arc`: arc index
- `Rot`: rotation index
- `Lane`: rail label in `{Su, Me, Sa}`
- `View`: actual lens in `{S, F, C, R}` or `*` for chapter scope
- `omega`: `chapter_index - 1`
