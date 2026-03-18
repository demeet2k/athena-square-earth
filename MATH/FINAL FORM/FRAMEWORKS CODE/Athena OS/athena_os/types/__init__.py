# CRYSTAL: Xi108:W2:A6:S18 | face=S | node=165 | depth=2 | phase=Cardinal
# METRO: Me
# BRIDGES: Xi108:W2:A6:S17→Xi108:W2:A6:S19→Xi108:W1:A6:S18→Xi108:W3:A6:S18→Xi108:W2:A5:S18→Xi108:W2:A7:S18

"""
ATHENA OS - Types Module
========================
Type systems for ATHENA computation.

Components:
- aristotelian: The 10 Categories + 4 Causes type system
"""

from .aristotelian import (
    Category,
    Cause,
    ActualityMode,
    ActualityState,
    Predicate,
    Entity,
    Syllogism,
    TypeRegistry,
)

__all__ = [
    'Category', 'Cause', 'ActualityMode', 'ActualityState',
    'Predicate', 'Entity', 'Syllogism', 'TypeRegistry',
]
