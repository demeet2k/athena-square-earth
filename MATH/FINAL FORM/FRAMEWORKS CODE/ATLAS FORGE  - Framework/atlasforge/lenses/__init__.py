# CRYSTAL: Xi108:W2:A11:S17 | face=S | node=137 | depth=2 | phase=Cardinal
# METRO: Me
# BRIDGES: Xi108:W2:A11:S16→Xi108:W2:A11:S18→Xi108:W1:A11:S17→Xi108:W3:A11:S17→Xi108:W2:A10:S17→Xi108:W2:A12:S17

"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                         ATLAS FORGE - Lenses Module                           ║
╚══════════════════════════════════════════════════════════════════════════════╝

The Lens/Chart transformation system for coordinate transport.
"""

from atlasforge.lenses.chart import (
    Chart,
    Lens,
    ComposedChart,
    CorridorCondition,
    CorridorViolation,
    ChartError,
    ChartCertificate,
    ChartFactory,
)

from atlasforge.lenses.transport import (
    Transport,
    FieldTransport,
    OperatorTransport,
    ConstraintTransport,
    FlowTransport,
    TransportChain,
)

from atlasforge.lenses.canonical import (
    IdentityLens,
    LogLens,
    ExpLens,
    TrigLens,
    PhiLens,
    FourierLens,
    LogitLens,
    BoxCoxLens,
    LensCatalog,
)

__all__ = [
    # Charts
    "Chart",
    "Lens",
    "ComposedChart",
    "CorridorCondition",
    "CorridorViolation",
    "ChartError",
    "ChartCertificate",
    "ChartFactory",
    
    # Transport
    "Transport",
    "FieldTransport",
    "OperatorTransport",
    "ConstraintTransport",
    "FlowTransport",
    "TransportChain",
    
    # Canonical Lenses
    "IdentityLens",
    "LogLens",
    "ExpLens",
    "TrigLens",
    "PhiLens",
    "FourierLens",
    "LogitLens",
    "BoxCoxLens",
    "LensCatalog",
]
