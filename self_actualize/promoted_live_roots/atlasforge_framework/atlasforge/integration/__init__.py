# CRYSTAL: Xi108:W2:A2:S26 | face=F | node=339 | depth=2 | phase=Mutable
# METRO: Me,Bw
# BRIDGES: Xi108:W2:A2:S25→Xi108:W2:A2:S27→Xi108:W1:A2:S26→Xi108:W3:A2:S26→Xi108:W2:A1:S26→Xi108:W2:A3:S26

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
