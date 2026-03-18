# CRYSTAL: Xi108:W2:A9:S27 | face=F | node=369 | depth=2 | phase=Mutable
# METRO: Me
# BRIDGES: Xi108:W2:A9:S26→Xi108:W2:A9:S28→Xi108:W1:A9:S27→Xi108:W3:A9:S27→Xi108:W2:A8:S27→Xi108:W2:A10:S27

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
