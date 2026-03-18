# CRYSTAL: Xi108:W2:A10:S16 | face=S | node=134 | depth=2 | phase=Cardinal
# METRO: Me,Bw
# BRIDGES: Xi108:W2:A10:S15→Xi108:W2:A10:S17→Xi108:W1:A10:S16→Xi108:W3:A10:S16→Xi108:W2:A9:S16→Xi108:W2:A11:S16

"""Unified Integration Module - Cross-module connectors, pole synthesis."""

from atlasforge.integration.integration import (
    Pole,
    PoleWeights,
    UnifiedState,
    CrossPoleConnector,
    HybridPathStep,
    HybridPath,
    ShortcutDetector,
    UnifiedSolver,
    create_unified_state,
    pole_weights,
    diagnose_state,
    find_shortcut,
    hybrid_evolution,
)

__all__ = [
    'Pole',
    'PoleWeights',
    'UnifiedState',
    'CrossPoleConnector',
    'HybridPathStep',
    'HybridPath',
    'ShortcutDetector',
    'UnifiedSolver',
    'create_unified_state',
    'pole_weights',
    'diagnose_state',
    'find_shortcut',
    'hybrid_evolution',
]
