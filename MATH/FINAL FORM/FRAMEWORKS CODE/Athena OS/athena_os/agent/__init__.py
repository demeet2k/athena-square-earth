# CRYSTAL: Xi108:W2:A4:S16 | face=S | node=132 | depth=2 | phase=Cardinal
# METRO: Me
# BRIDGES: Xi108:W2:A4:S15→Xi108:W2:A4:S17→Xi108:W1:A4:S16→Xi108:W3:A4:S16→Xi108:W2:A3:S16→Xi108:W2:A5:S16

"""
ATHENA OS - Agent Module
========================
The Distinguished Agent (Â) and agent-related systems.

Components:
- distinguished: The Distinguished Agent at the Zero Point
"""

from .distinguished import (
    AgentState,
    VoidAlignment,
    WorldEngagement,
    UpdateOperator,
    UpdateResult,
    AgentUpdater,
    DistinguishedAgent,
)

__all__ = [
    'AgentState', 'VoidAlignment', 'WorldEngagement',
    'UpdateOperator', 'UpdateResult', 'AgentUpdater',
    'DistinguishedAgent',
]
