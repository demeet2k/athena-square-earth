# CRYSTAL: Xi108:W2:A2:S26 | face=F | node=331 | depth=2 | phase=Mutable
# METRO: Me
# BRIDGES: Xi108:W2:A2:S25→Xi108:W2:A2:S27→Xi108:W1:A2:S26→Xi108:W3:A2:S26→Xi108:W2:A1:S26→Xi108:W2:A3:S26

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
