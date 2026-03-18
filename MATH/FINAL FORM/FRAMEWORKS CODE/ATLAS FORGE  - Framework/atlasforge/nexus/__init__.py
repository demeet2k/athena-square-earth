# CRYSTAL: Xi108:W2:A8:S14 | face=S | node=103 | depth=2 | phase=Cardinal
# METRO: Me
# BRIDGES: Xi108:W2:A8:S13→Xi108:W2:A8:S15→Xi108:W1:A8:S14→Xi108:W3:A8:S14→Xi108:W2:A7:S14→Xi108:W2:A9:S14

"""Nexus Navigation Module - Pell nexus points, figurate sequences."""

from atlasforge.nexus.nexus import (
    FigurateType,
    FigurateNumber,
    NexusPoint,
    TriangularSquareNexus,
    PellNexus,
    NexusNavigator,
    FigurateLattice,
    NexusScaling,
    triangular,
    is_triangular,
    is_square,
    is_triangular_square,
    triangular_square_sequence,
    solve_pell,
    figurate_intersections,
)

__all__ = [
    'FigurateType',
    'FigurateNumber',
    'NexusPoint',
    'TriangularSquareNexus',
    'PellNexus',
    'NexusNavigator',
    'FigurateLattice',
    'NexusScaling',
    'triangular',
    'is_triangular',
    'is_square',
    'is_triangular_square',
    'triangular_square_sequence',
    'solve_pell',
    'figurate_intersections',
]
