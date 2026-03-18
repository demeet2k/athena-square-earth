# CRYSTAL: Xi108:W2:A4:S28 | face=F | node=390 | depth=2 | phase=Mutable
# METRO: Me
# BRIDGES: Xi108:W2:A4:S27→Xi108:W2:A4:S29→Xi108:W1:A4:S28→Xi108:W3:A4:S28→Xi108:W2:A3:S28→Xi108:W2:A5:S28

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
