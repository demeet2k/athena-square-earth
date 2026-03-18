# CRYSTAL: Xi108:W2:A6:S30 | face=F | node=447 | depth=2 | phase=Mutable
# METRO: Me
# BRIDGES: Xi108:W2:A6:S29→Xi108:W2:A6:S31→Xi108:W1:A6:S30→Xi108:W3:A6:S30→Xi108:W2:A5:S30→Xi108:W2:A7:S30

"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                         ATLAS FORGE - Core Module                             ║
╚══════════════════════════════════════════════════════════════════════════════╝

Core types, enumerations, and base classes that form the foundation
of the AtlasForge framework.
"""

from atlasforge.core.enums import (
    Pole,
    Element,
    CertificateLevel,
    TruthProfile,
    ConstraintType,
    NormalFormType,
    ObligationType,
    PlanStatus,
    VerificationResult,
    SolverType,
    IntervalMode,
    DyadicEdge,
    CrystalLens,
    InvariantSpineComponent,
    QuantumBasis,
    FlowType,
    CacheType,
    ValidationFlags,
    SolverFlags,
)

from atlasforge.core.types import (
    RoundingMode,
    FloatPolicy,
    DEFAULT_FLOAT_POLICY,
    Bound,
    Interval,
    Domain,
    UnionDomain,
    PointSet,
    RectangularDomain,
    Lattice,
    AnyDomain,
)

from atlasforge.core.base import (
    Hashable,
    Serializable,
    ContentAddressed,
    AtlasObject,
    ImmutableObject,
    VersionedObject,
    CompositeObject,
    register_type,
    deserialize,
)

__all__ = [
    # Enums
    "Pole",
    "Element",
    "CertificateLevel",
    "TruthProfile",
    "ConstraintType",
    "NormalFormType",
    "ObligationType",
    "PlanStatus",
    "VerificationResult",
    "SolverType",
    "IntervalMode",
    "DyadicEdge",
    "CrystalLens",
    "InvariantSpineComponent",
    "QuantumBasis",
    "FlowType",
    "CacheType",
    "ValidationFlags",
    "SolverFlags",
    
    # Types
    "RoundingMode",
    "FloatPolicy",
    "DEFAULT_FLOAT_POLICY",
    "Bound",
    "Interval",
    "Domain",
    "UnionDomain",
    "PointSet",
    "RectangularDomain",
    "Lattice",
    "AnyDomain",
    
    # Base classes
    "Hashable",
    "Serializable",
    "ContentAddressed",
    "AtlasObject",
    "ImmutableObject",
    "VersionedObject",
    "CompositeObject",
    "register_type",
    "deserialize",
]
