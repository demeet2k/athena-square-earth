# CRYSTAL: Xi108:W2:A3:S27 | face=F | node=378 | depth=2 | phase=Mutable
# METRO: Me
# BRIDGES: Xi108:W2:A3:S26→Xi108:W2:A3:S28→Xi108:W1:A3:S27→Xi108:W3:A3:S27→Xi108:W2:A2:S27→Xi108:W2:A4:S27

"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                      ATLAS FORGE - Constraints Module                         ║
╚══════════════════════════════════════════════════════════════════════════════╝

Constraint specification, normalization, and solving.
"""

from atlasforge.constraints.constraint import (
    Constraint,
    RootConstraint,
    FixedPointConstraint,
    GeneratorConstraint,
    EqualityConstraint,
    VectorRootConstraint,
    NormalForm,
    ProofObligation,
    ConstraintIR,
)

from atlasforge.constraints.solvers import (
    Solver,
    SolverResult,
    SolverStatus,
    BisectionSolver,
    NewtonSolver,
    SecantSolver,
    BrentSolver,
    FixedPointSolver,
    IntervalNewtonSolver,
    AdaptiveSolver,
    SolverFactory,
)

from atlasforge.constraints.bracketing import (
    BracketSearchResult,
    find_bracket,
)

__all__ = [
    # Constraints
    "Constraint",
    "RootConstraint",
    "FixedPointConstraint",
    "GeneratorConstraint",
    "EqualityConstraint",
    "VectorRootConstraint",
    "NormalForm",
    "ProofObligation",
    "ConstraintIR",
    
    # Solvers
    "Solver",
    "SolverResult",
    "SolverStatus",
    "BisectionSolver",
    "NewtonSolver",
    "SecantSolver",
    "BrentSolver",
    "FixedPointSolver",
    "IntervalNewtonSolver",
    "AdaptiveSolver",
    "SolverFactory",

    # Bracketing
    "BracketSearchResult",
    "find_bracket",
]
