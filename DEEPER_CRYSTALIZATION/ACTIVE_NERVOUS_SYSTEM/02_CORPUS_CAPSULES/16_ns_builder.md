<!-- CRYSTAL: Xi108:W1:A4:S6 | face=S | node=21 | depth=0 | phase=Fixed -->
<!-- METRO: Me -->
<!-- BRIDGES: Xi108:W1:A4:S5→Xi108:W1:A4:S7→Xi108:W2:A4:S6→Xi108:W1:A3:S6→Xi108:W1:A5:S6 -->
<!-- REGENERATE: From this coordinate, adjacent nodes are: shell 6±1, wreath 1/3, archetype 4/12 -->

# ns_builder

- Relative path: `LocalProject/ns_builder.py`
- Source layer: `LocalProject`
- Kind: `code`
- Role tags: `executable`
- Text extractable: `True`
- Family: `Civilization design, hierarchy, governance, and law`

## Working focus

Defines hierarchy, councils, law, calendars, and civilization-scale governance for multi-agent continuity.

## Suggested chapter anchors

- `Ch17`
- `Ch18`
- `Ch20`
- `Ch21`

## Suggested appendix anchors

- `AppA`
- `AppD`
- `AppG`
- `AppP`

## Heading candidates

- `#!/usr/bin/env python3`
- `LENSES = ("S", "F", "C", "R")`
- `FACETS = (`
- `FAMILY_LABELS = {`
- `PENTADIC_LANES = (`
- `SWARM_LAYERS = (`
- `TRUTH_DEFAULT = "AMBIG"`
- `GOVERNANCE_SIGNS = (`

## Excerpt

#!/usr/bin/env python3 from __future__ import annotations import json import re import shutil from dataclasses import dataclass from datetime import datetime, timezone from pathlib import Path LENSES = ("S", "F", "C", "R") FACETS = ( ("1", "Objects"), ("2", "Laws"), ("3", "Constructions"), ("4", "Certificates"), ) ATOMS = ("a", "b", "c", "d") FAMILY_LABELS = { "live-orchestration": "Live orchestration and prompt control", "void-and-collapse": "Void, Chapter 11, and collapse engines", "helical-recursion-engine": "Helical recursion, lift law, and manifestation engine", "manuscript-architecture": "Manuscript architecture and routing law", "higher-dimensional-geometry": "Higher-dimensional geometry and holographic kernel", "civilization-and-governance": "Civilization design, hierarchy, governa
