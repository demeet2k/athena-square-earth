# CRYSTAL: Xi108:W2:A10:S16 | face=S | node=134 | depth=2 | phase=Cardinal
# METRO: Me
# BRIDGES: Xi108:W2:A10:S15→Xi108:W2:A10:S17→Xi108:W1:A10:S16→Xi108:W3:A10:S16→Xi108:W2:A9:S16→Xi108:W2:A11:S16

"""
ATHENA OS - Philosophical Module
================================
Philosophical foundations for consciousness-compatible computation.

Components:
- elements: Four Elements archetype system with 90° rotation
- stoic: Stoic control system and liberation protocols
- alchemy: Alchemical transformation calculus
"""

from .elements import (
    Element,
    ElementalState,
    RotationEngine,
    ShadowPoles,
    WaveParticleLens,
    ElementalProcessor,
)

from .stoic import (
    ControlDomain,
    ControlItem,
    JudgmentType,
    Judgment,
    Hegemonikon,
    StressTensor,
    OptimizationProtocol,
    KarmaYoga,
    BhaktiYoga,
    JnanaYoga,
    ControlLevel,
    ControlLevelState,
    LiberationEngine,
)

from .alchemy import (
    AlchemicalStage,
    AlchemicalOperator,
    AlchemicalState,
    AlchemicalTransformer,
    AlchemicalVector,
    find_fixed_point,
)

__all__ = [
    # Elements
    'Element', 'ElementalState', 'RotationEngine', 'ShadowPoles',
    'WaveParticleLens', 'ElementalProcessor',
    # Stoic
    'ControlDomain', 'ControlItem', 'JudgmentType', 'Judgment',
    'Hegemonikon', 'StressTensor', 'OptimizationProtocol',
    'KarmaYoga', 'BhaktiYoga', 'JnanaYoga',
    'ControlLevel', 'ControlLevelState', 'LiberationEngine',
    # Alchemy
    'AlchemicalStage', 'AlchemicalOperator', 'AlchemicalState',
    'AlchemicalTransformer', 'AlchemicalVector', 'find_fixed_point',
]
