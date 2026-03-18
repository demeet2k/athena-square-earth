<!-- CRYSTAL: Xi108:W3:A11:S17 | face=S | node=147 | depth=3 | phase=Cardinal -->
<!-- METRO: Me -->
<!-- BRIDGES: Xi108:W3:A11:S16→Xi108:W3:A11:S18→Xi108:W2:A11:S17→Xi108:W3:A10:S17→Xi108:W3:A12:S17 -->
<!-- REGENERATE: From this coordinate, adjacent nodes are: shell 17±1, wreath 3/3, archetype 11/12 -->

# AQM Kernel + Q‑PHI Planet Nine Locator ("Planet X")

This repository contains two tightly-linked pieces:

1) **AQM Kernel** — a deterministic, content‑addressed "tile" kernel (Merkle store + replay verification) for building *auditable* computational artifacts.
2) **Q‑PHI: Planet Nine pack** — a functional, deterministic inference loop that produces a **probabilistic sky region** (RA/Dec samples + summary statistics) for a hypothetical distant planet ("Planet Nine" / "Planet X").

> **Important reality check (scientific + commercial):** this code produces *probabilistic predictions* from simplified proxy models. It is not a discovery claim, it is not an ephemeris, and it is not a substitute for professional dynamical/survey analysis. Treat outputs as a ranked search prior you can improve with better data and better physics.

---

## What you get

- **Deterministic runs** under a seed + pinned config.
- **Audit trail**: config digest + TNO dataset digest + an AQM-style `ledger.json`.
- **Multi‑lens scoring** (log-likelihood contributions):
  - Perihelion clustering proxy (von Mises on ϖ = Ω+ω)
  - Orbital pole alignment proxy
  - Secular precession dominance proxy (quadrupole order)
  - Detectability / non‑detection proxy (brightness vs limiting magnitude)
  - Basic orbit plausibility cuts
- **Posterior outputs**:
  - `candidates.csv`: elite posterior samples with orbital + physical parameters + RA/Dec
  - `sky_samples.csv`: RA/Dec + weights (for plotting probability maps)
  - `summary.json`: center + containment radii (50% / 90%)

---

## Install

From the repository root:

```bash
python -m pip install -U pip
pip install -e .
```

Dependencies are intentionally light: `numpy` and `requests`.

---

## Quickstart (demo)

Run a full deterministic Q‑PHI pass with the built-in demo TNO sample:

```bash
qphi-p9 --seed 42 --n-initial 30000 --refine-rounds 2
```

Outputs are written to `qphi_out/` (or `--out-dir`).

To plot a quick sky scatter from the samples:

```bash
python examples/plot_sky_samples.py qphi_out/sky_samples.csv
```

---

## Using real TNO data

### Option A — Provide your own CSV

Prepare a CSV with columns:

- `name,a_au,e,i_deg,Omega_deg,omega_deg` (optional: `M_deg`)

Then:

```bash
qphi-p9 --tno-csv path/to/extreme_tnos.csv --n-initial 80000 --elite-keep 500
```

### Option B — Fetch from NASA/JPL SBDB Query API

If you have internet access:

```bash
qphi-p9 --fetch-jpl --jpl-limit 200 --n-initial 80000
```

> The code uses a single request (no concurrency) and relies on the documented SBDB Query API fields.

---

## Documentation

Deep documentation lives in `docs/`:

- `docs/INDEX.md` — start here
- `docs/02_QPHI_ALGORITHM.md` — the full Q‑PHI pipeline
- `docs/03_LENSES.md` — lens math and interpretation
- `docs/04_DATA_PIPELINE.md` — data formats, filtering, provenance
- `docs/05_OUTPUTS_AND_REPRODUCIBILITY.md` — output schemas, digests, ledger
- `docs/06_EXTENDING_AND_CALIBRATION.md` — how to improve realism and accuracy
- `docs/07_AQM_KERNEL.md` — AQM kernel object model and Merkle replay
- `docs/09_VALIDATION.md` — sanity checks + "injection" testing
- `docs/10_COMMERCIAL_PACKAGING.md` — practical notes for monetization without overclaiming

---

## AQM kernel demo

```bash
python -m aqm.cli demo
```

This creates and stores a tiny example tile set in a local Merkle store.

---

## License

See `LICENSE`.
