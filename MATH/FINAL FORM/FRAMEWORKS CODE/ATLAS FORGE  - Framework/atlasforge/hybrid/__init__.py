# CRYSTAL: Xi108:W2:A1:S13 | face=S | node=79 | depth=2 | phase=Cardinal
# METRO: Me
# BRIDGES: Xi108:W2:A1:S12→Xi108:W2:A1:S14→Xi108:W1:A1:S13→Xi108:W3:A1:S13→Xi108:W2:A2:S13

"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                        ATLAS FORGE - Hybrid Module                            ║
╚══════════════════════════════════════════════════════════════════════════════╝

Hybrid dynamical systems: continuous flows + discrete jumps.
"""

from atlasforge.hybrid.hybrid import (
    HybridState,
    Flow,
    LinearFlow,
    GradientFlow,
    GeneratorFlow,
    Guard,
    Reset,
    Transition,
    HybridSystem,
    RelaxProjectPattern,
    FlowPrunePattern,
    PredictCorrectPattern,
    HybridEquation,
)

__all__ = [
    "HybridState",
    "Flow",
    "LinearFlow",
    "GradientFlow",
    "GeneratorFlow",
    "Guard",
    "Reset",
    "Transition",
    "HybridSystem",
    "RelaxProjectPattern",
    "FlowPrunePattern",
    "PredictCorrectPattern",
    "HybridEquation",
]
