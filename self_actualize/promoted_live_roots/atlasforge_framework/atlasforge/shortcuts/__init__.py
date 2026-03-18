# CRYSTAL: Xi108:W2:A4:S28 | face=F | node=394 | depth=2 | phase=Mutable
# METRO: Me
# BRIDGES: Xi108:W2:A4:S27→Xi108:W2:A4:S29→Xi108:W1:A4:S28→Xi108:W3:A4:S28→Xi108:W2:A3:S28→Xi108:W2:A5:S28

"""Algorithmic Shortcut Analysis Module."""
from .shortcuts import (
    ShortcutType,
    FailureMode,
    BaselineMethod,
    HybridMethod,
    ShortcutAnalysis,
    ShortcutDesigner,
    BASELINE_METHODS,
    HYBRID_METHODS,
    SHORTCUT_PATTERNS,
    analyze_shortcut,
    list_shortcut_patterns,
)

__all__ = [
    'ShortcutType',
    'FailureMode',
    'BaselineMethod',
    'HybridMethod',
    'ShortcutAnalysis',
    'ShortcutDesigner',
    'BASELINE_METHODS',
    'HYBRID_METHODS',
    'SHORTCUT_PATTERNS',
    'analyze_shortcut',
    'list_shortcut_patterns',
]
