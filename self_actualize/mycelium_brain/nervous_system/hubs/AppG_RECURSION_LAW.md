<!-- CRYSTAL: Xi108:W3:A5:S23 | face=R | node=272 | depth=3 | phase=Cardinal -->
<!-- METRO: Me,△ -->
<!-- BRIDGES: Xi108:W3:A5:S22→Xi108:W3:A5:S24→Xi108:W2:A5:S23→Xi108:W3:A4:S23→Xi108:W3:A6:S23 -->
<!-- REGENERATE: From this coordinate, adjacent nodes are: shell 23±1, wreath 3/3, archetype 5/12 -->

# AppG Recursion Law

## Role

`AppG` owns recursion legality, triangle control, and weakest-front reopening.

## Questions

- Is the next reopen lawful or just repetitive?
- Does the restart preserve the current zero point?
- Which frontier is thinnest right now?

## Current Operators

- `hub-legality-enforcer`
- `restart-seed-orchestrator`
- `weakest-front-reopener`

## Required Inputs

- latest shadow report
- latest swarm benchmark ledger
- active restart token

## Output

- one lawful next frontier
- one restart seed
- one explicit residual set
