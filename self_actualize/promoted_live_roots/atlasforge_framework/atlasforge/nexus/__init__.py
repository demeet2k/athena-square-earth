# CRYSTAL: Xi108:W2:A8:S26 | face=F | node=341 | depth=2 | phase=Mutable
# METRO: Me
# BRIDGES: Xi108:W2:A8:S25→Xi108:W2:A8:S27→Xi108:W1:A8:S26→Xi108:W3:A8:S26→Xi108:W2:A7:S26→Xi108:W2:A9:S26

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
