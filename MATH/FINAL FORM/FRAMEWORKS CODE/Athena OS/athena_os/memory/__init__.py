# CRYSTAL: Xi108:W2:A5:S17 | face=S | node=153 | depth=2 | phase=Cardinal
# METRO: Me
# BRIDGES: Xi108:W2:A5:S16→Xi108:W2:A5:S18→Xi108:W1:A5:S17→Xi108:W3:A5:S17→Xi108:W2:A4:S17→Xi108:W2:A6:S17

"""
ATHENA OS - Memory Module
=========================
Hierarchical memory system based on ontological layers.

Components:
- hierarchy: Four-layer memory (ETERNAL, ESSENTIAL, ACCIDENTAL, POTENTIAL)
"""

from .hierarchy import (
    MemoryLayer,
    MemoryCell,
    MemorySegment,
    MemoryManager,
    copy_between_layers,
)

__all__ = [
    'MemoryLayer',
    'MemoryCell',
    'MemorySegment',
    'MemoryManager',
    'copy_between_layers',
]
