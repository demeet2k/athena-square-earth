# CRYSTAL: Xi108:W2:A4:S16 | face=S | node=124 | depth=2 | phase=Cardinal
# METRO: Me
# BRIDGES: Xi108:W2:A4:S15→Xi108:W2:A4:S17→Xi108:W1:A4:S16→Xi108:W3:A4:S16→Xi108:W2:A3:S16→Xi108:W2:A5:S16

"""
PoleStarGEMM
============

PoleStarGEMM is a Quad-Polar (Ψ/Σ/Ω/Δ) optimization toolkit:

- `polestargemm.core`: adaptive NumPy GEMM planner (cache + validation)
- `polestargemm.vision`: vision-model low-rank optimizer for PyTorch + TorchScript export

See repository README for end-to-end usage and deployment instructions.
"""

from .core import PoleStarGEMM, make_ablation_configs, summarize_ablation
from .vision import (
    PoleStarVisionConfig,
    PoleStarAnalyzer,
    PoleStarLinear,
    PoleStarConv2d,
    OptimizationReport,
    optimize_model,
    benchmark_model,
    validate_relative_error,
    export_torchscript,
)

__all__ = [
    "PoleStarGEMM",
    "make_ablation_configs",
    "summarize_ablation",
    "PoleStarVisionConfig",
    "PoleStarAnalyzer",
    "PoleStarLinear",
    "PoleStarConv2d",
    "OptimizationReport",
    "optimize_model",
    "benchmark_model",
    "validate_relative_error",
    "export_torchscript",
]
