# CRYSTAL: Xi108:W2:A5:S17 | face=S | node=147 | depth=2 | phase=Cardinal
# METRO: Me
# BRIDGES: Xi108:W2:A5:S16→Xi108:W2:A5:S18→Xi108:W1:A5:S17→Xi108:W3:A5:S17→Xi108:W2:A4:S17→Xi108:W2:A6:S17

"""Example: run Q‑PHI programmatically.

This is useful if you want to embed Q‑PHI inside a service or notebook.

Run:
    python examples/run_qphi_demo.py
"""

from pathlib import Path

from aqm.apps.planet9.qphi import QPHIConfig, load_tnos_for_run, run_qphi

def main() -> None:
    cfg = QPHIConfig(
        seed=42,
        # smaller numbers so this runs quickly on most machines
        n_initial=8000,
        elite_keep=200,
        refine_rounds=1,
        offspring_per_elite=15,
        out_dir="qphi_out_demo",
        store_dir=None,
    )

    tnos = load_tnos_for_run(tno_csv=None, cfg=cfg, fetch_jpl=False)
    summary = run_qphi(tnos, cfg)

    print("\nSummary")
    for k in [
        "seed",
        "n_tnos",
        "best_log_score",
        "sky_center_ra_deg",
        "sky_center_dec_deg",
        "containment_radius_50_deg",
        "containment_radius_90_deg",
        "cfg_digest",
        "tno_digest",
    ]:
        print(f"- {k}: {summary.get(k)}")

    out = Path(cfg.out_dir)
    print(f"\nWrote outputs to: {out.resolve()}")

if __name__ == "__main__":
    main()
