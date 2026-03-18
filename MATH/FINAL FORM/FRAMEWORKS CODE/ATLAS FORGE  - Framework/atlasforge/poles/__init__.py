# CRYSTAL: Xi108:W2:A3:S15 | face=S | node=111 | depth=2 | phase=Cardinal
# METRO: Me
# BRIDGES: Xi108:W2:A3:S14→Xi108:W2:A3:S16→Xi108:W1:A3:S15→Xi108:W3:A3:S15→Xi108:W2:A2:S15→Xi108:W2:A4:S15

"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                         ATLAS FORGE - Poles Module                            ║
╚══════════════════════════════════════════════════════════════════════════════╝

The four-pole architecture and operator simplex.
"""

from atlasforge.poles.archetype import (
    Archetype,
    Fire,
    Air,
    Water,
    Earth,
    RotationEngine,
    ARCHETYPE_MAP,
    POLE_TO_ARCHETYPE,
    get_archetype,
    get_archetype_for_pole,
)

from atlasforge.poles.generator import (
    Generator,
    ScaledGenerator,
    DissipativeGenerator,
    OscillatoryGenerator,
    StochasticGenerator,
    RecursiveGenerator,
    HybridGenerator,
)

from atlasforge.poles.simplex import (
    PoleCoefficients,
    DyadicInterface,
    SimplexFace,
    OperatorSimplex,
)

__all__ = [
    # Archetypes
    "Archetype",
    "Fire",
    "Air",
    "Water",
    "Earth",
    "RotationEngine",
    "ARCHETYPE_MAP",
    "POLE_TO_ARCHETYPE",
    "get_archetype",
    "get_archetype_for_pole",
    
    # Generators
    "Generator",
    "ScaledGenerator",
    "DissipativeGenerator",
    "OscillatoryGenerator",
    "StochasticGenerator",
    "RecursiveGenerator",
    "HybridGenerator",
    
    # Simplex
    "PoleCoefficients",
    "DyadicInterface",
    "SimplexFace",
    "OperatorSimplex",
]
