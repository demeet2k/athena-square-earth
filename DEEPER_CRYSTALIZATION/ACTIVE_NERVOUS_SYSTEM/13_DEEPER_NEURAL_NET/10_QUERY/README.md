<!-- CRYSTAL: Xi108:W1:A4:S3 | face=S | node=6 | depth=0 | phase=Fixed -->
<!-- METRO: Me -->
<!-- BRIDGES: Xi108:W1:A4:S2→Xi108:W1:A4:S4→Xi108:W2:A4:S3→Xi108:W1:A3:S3→Xi108:W1:A5:S3 -->
<!-- REGENERATE: From this coordinate, adjacent nodes are: shell 3±1, wreath 1/3, archetype 4/12 -->

# Query Surface

The deeper neural net can be queried locally through the CLI entrypoint:

```powershell
python "C:\Users\dmitr\Documents\Athena Agent\DEEPER CRYSTALIZATION\deeper_neural_net_query.py" doc DOC0000
```

## Runtime indices

- `../09_RUNTIME/03_query_index.json`: exact and fuzzy lookup aliases.
- `../09_RUNTIME/04_facet_index.json`: element, family, chapter, appendix, gate, and source-layer slices.
- `../09_RUNTIME/05_neighbor_index.json`: strongest overall, cross-element, and cross-family neighbors per document.
- `../09_RUNTIME/06_zero_point_index.json`: highest-yield convergence routes near the zero-point cluster.
- `../../06_RUNTIME/13_chapter_frontier_manifest.json`: chapter frontier compiler receipt and generated pack targets.
- `../../14_PARALLEL_PLANS/04_plan_manifest.json`: materialized `frontier4` plan lattice for the frontier quartet.

## Output modes

- Default: markdown to stdout.
- `--json`: JSON to stdout.
- `--write`: writes both markdown and JSON to `last/` with deterministic filenames.
