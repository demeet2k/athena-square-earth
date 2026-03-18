# CRYSTAL: Xi108:W2:A7:S13 | face=S | node=82 | depth=2 | phase=Cardinal
# METRO: Me
# BRIDGES: Xi108:W2:A7:S12→Xi108:W2:A7:S14→Xi108:W1:A7:S13→Xi108:W3:A7:S13→Xi108:W2:A6:S13→Xi108:W2:A8:S13

"""Hybrid Coupling Module - Phase coupling, spectral invariants, eigenvalue detectors."""

from atlasforge.coupling.coupling import (
    PhaseVector,
    HybridOperator,
    TraceMoments,
    DeterminantInvariants,
    HeatKernelTrace,
    EigenvalueSpikeDetector,
    PhaseCoherence,
    HybridInvariantBundle,
    create_hybrid_coupling,
    analyze_hybrid,
    check_coherence,
    trace_fingerprint,
)

__all__ = [
    'PhaseVector',
    'HybridOperator',
    'TraceMoments',
    'DeterminantInvariants',
    'HeatKernelTrace',
    'EigenvalueSpikeDetector',
    'PhaseCoherence',
    'HybridInvariantBundle',
    'create_hybrid_coupling',
    'analyze_hybrid',
    'check_coherence',
    'trace_fingerprint',
]
