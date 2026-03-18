# CRYSTAL: Xi108:W2:A8:S14 | face=S | node=105 | depth=2 | phase=Cardinal
# METRO: Me
# BRIDGES: Xi108:W2:A8:S13→Xi108:W2:A8:S15→Xi108:W1:A8:S14→Xi108:W3:A8:S14→Xi108:W2:A7:S14→Xi108:W2:A9:S14

"""Biology and Physics Module - Morphogen gradients, Turing patterns, neural signaling."""

from atlasforge.biology.biology import (
    TetradicState,
    TetradicController,
    FIRE, AIR, EARTH, WATER,
    ReactionDiffusionSystem,
    GiererMeinhardtSystem,
    GrayScottSystem,
    TuringPatternType,
    MorphogenGradient,
    NeuralPulse,
    IntegrateAndFireNeuron,
    DefectHyperplane,
    DefectNetwork,
    MultiScaleHomeostasis,
    analyze_pattern,
    create_turing_system,
    morphogen_gradient_1d,
    simulate_neuron,
)

__all__ = [
    'TetradicState',
    'TetradicController',
    'FIRE', 'AIR', 'EARTH', 'WATER',
    'ReactionDiffusionSystem',
    'GiererMeinhardtSystem',
    'GrayScottSystem',
    'TuringPatternType',
    'MorphogenGradient',
    'NeuralPulse',
    'IntegrateAndFireNeuron',
    'DefectHyperplane',
    'DefectNetwork',
    'MultiScaleHomeostasis',
    'analyze_pattern',
    'create_turing_system',
    'morphogen_gradient_1d',
    'simulate_neuron',
]
