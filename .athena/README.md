# Athena federation contract

This directory makes `demeet2k/athena-square-earth` a typed participant in the Athena Git Brain.
It does not copy the Athena corpus or grant this repository global authority.

- Resource: `athena.repo.view.square-earth@contract-proposal-0.1.0`
- Role: `view`
- Authority domain: `projection-square-earth`
- Base content witness: `dafd62e7af64eb2a58975ecef27b8ef4792868f9`
- Control-plane schema commit: `3d33fbcd6248fc2dc2991fbbab5e93a7eb184246`
- State: `GENERATOR_LINEAGE_REQUIRED`

`repo.json` declares the local surface. `exports.jsonl` exposes bounded
identities. `imports.lock.json` pins the control-plane schema. `edges.jsonl`
contains the forward declaration and its explicit return edge. `status.json`
preserves blockers instead of promoting them away.
