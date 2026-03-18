# CRYSTAL: Xi108:W2:A12:S18 | face=S | node=171 | depth=2 | phase=Cardinal
# METRO: Me
# BRIDGES: Xi108:W2:A12:S17→Xi108:W2:A12:S19→Xi108:W1:A12:S18→Xi108:W3:A12:S18→Xi108:W2:A11:S18

"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                      ∞-CATEGORIES MODULE                                     ║
║                                                                              ║
║  Model Categories, Quasicategories, and Higher Categorical Structures        ║
║                                                                              ║
║  Core Principle:                                                             ║
║    Higher categories generalize categories:                                  ║
║    - 1-categories: objects, morphisms                                        ║
║    - 2-categories: objects, morphisms, 2-morphisms                          ║
║    - ∞-categories: objects, morphisms, n-morphisms for all n                ║
║                                                                              ║
║  Connection to Framework:                                                    ║
║    - Ψ-pole ↔ Higher morphism hierarchy                                     ║
║    - C-pole ↔ Simplicial structure (topological)                            ║
║    - D-pole ↔ Model structure (weak equivalences)                           ║
║    - Gateway ↔ Quillen equivalences (category correspondences)              ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Tuple, List, Dict, Any, Callable
from enum import Enum
import numpy as np
from numpy.typing import NDArray

# ═══════════════════════════════════════════════════════════════════════════════
# MODEL CATEGORIES
# ═══════════════════════════════════════════════════════════════════════════════

@dataclass
class ModelStructure:
    """
    Model structure on a category C.
    
    Three distinguished classes of morphisms:
    - W: weak equivalences
    - F: fibrations  
    - C: cofibrations
    
    Satisfying axioms MC1-MC5.
    """
    category_name: str
    weak_equivalences: str = "W"
    fibrations: str = "Fib"
    cofibrations: str = "Cof"
    
    def mc1_2of3(self) -> str:
        """MC1: 2-of-3 for weak equivalences."""
        return "f, g ∈ W, one of f,g,gf ⟹ third ∈ W"
    
    def mc2_retract(self) -> str:
        """MC2: W, F, C closed under retracts."""
        return "Retracts of W, Fib, Cof remain in respective class"
    
    def mc3_lifting(self) -> str:
        """MC3: Lifting properties."""
        return "Cof ∩ W ⊥ Fib and Cof ⊥ Fib ∩ W"
    
    def mc4_factorization(self) -> str:
        """MC4: Factorization axioms."""
        return "f = (Cof ∩ W) ∘ Fib = Cof ∘ (Fib ∩ W)"
    
    def mc5_initial_terminal(self) -> str:
        """MC5: Initial and terminal objects exist."""
        return "∅ and * exist in C"
    
    def homotopy_category(self) -> str:
        """Ho(C) = C[W^{-1}]."""
        return f"Ho({self.category_name}) = {self.category_name}[{self.weak_equivalences}^{{-1}}]"

@dataclass
class ModelCategory:
    """
    Model category (C, W, F, C).
    """
    name: str
    model_structure: ModelStructure
    
    def cofibrant_objects(self) -> str:
        """Cofibrant: ∅ → X is cofibration."""
        return f"Cof objects = {{X : ∅ → X ∈ Cof}}"
    
    def fibrant_objects(self) -> str:
        """Fibrant: X → * is fibration."""
        return f"Fib objects = {{X : X → * ∈ Fib}}"
    
    def derived_functor(self, F: str) -> str:
        """Derived functor LF or RF."""
        return f"𝕃{F} = {F} ∘ Q or ℝ{F} = {F} ∘ R"
    
    @classmethod
    def topological_spaces(cls) -> 'ModelCategory':
        """Standard model structure on Top."""
        return cls("Top", ModelStructure("Top", "homotopy eq", "Serre fib", "retracts of CW"))
    
    @classmethod
    def simplicial_sets(cls) -> 'ModelCategory':
        """Kan model structure on sSet."""
        return cls("sSet", ModelStructure("sSet", "weak htpy eq", "Kan fib", "mono"))
    
    @classmethod
    def chain_complexes(cls) -> 'ModelCategory':
        """Projective model structure on Ch(R)."""
        return cls("Ch(R)", ModelStructure("Ch(R)", "quasi-iso", "surjective", "degreewise mono"))

# ═══════════════════════════════════════════════════════════════════════════════
# QUILLEN ADJUNCTIONS AND EQUIVALENCES
# ═══════════════════════════════════════════════════════════════════════════════

@dataclass
class QuillenAdjunction:
    """
    Quillen adjunction (F ⊣ G): C ⇌ D.
    
    F: C → D left adjoint (preserves cofibrations, acyclic cofibrations)
    G: D → C right adjoint (preserves fibrations, acyclic fibrations)
    """
    left_functor: str
    right_functor: str
    source: ModelCategory
    target: ModelCategory
    
    def adjunction(self) -> str:
        """F ⊣ G."""
        return f"{self.left_functor} ⊣ {self.right_functor}: {self.source.name} ⇌ {self.target.name}"
    
    def derived_adjunction(self) -> str:
        """𝕃F ⊣ ℝG on homotopy categories."""
        return f"𝕃{self.left_functor} ⊣ ℝ{self.right_functor}: Ho({self.source.name}) ⇌ Ho({self.target.name})"

@dataclass
class QuillenEquivalence:
    """
    Quillen equivalence: derived functors are equivalences.
    
    Ho(C) ≃ Ho(D)
    """
    adjunction: QuillenAdjunction
    
    def equivalence(self) -> str:
        """Derived equivalence."""
        C = self.adjunction.source.name
        D = self.adjunction.target.name
        return f"Ho({C}) ≃ Ho({D})"
    
    def criterion(self) -> str:
        """Criterion for Quillen equivalence."""
        return "F reflects weak eq between cofibrant, G reflects weak eq between fibrant"

# ═══════════════════════════════════════════════════════════════════════════════
# SIMPLICIAL AND TOPOLOGICAL HOMOTOPY THEORY
# ═══════════════════════════════════════════════════════════════════════════════

@dataclass
class SimplicialSet:
    """
    Simplicial set X: Δ^{op} → Set.
    
    X_n = n-simplices with face maps d_i and degeneracy maps s_i.
    """
    name: str
    
    def n_simplices(self, n: int) -> str:
        """X_n."""
        return f"{self.name}_{n}"
    
    def face_maps(self, n: int) -> str:
        """d_i: X_n → X_{n-1}."""
        return f"d_i: {self.name}_{n} → {self.name}_{{{n-1}}}, i=0,...,{n}"
    
    def degeneracy_maps(self, n: int) -> str:
        """s_i: X_n → X_{n+1}."""
        return f"s_i: {self.name}_{n} → {self.name}_{{{n+1}}}, i=0,...,{n}"
    
    def geometric_realization(self) -> str:
        """|X| - geometric realization."""
        return f"|{self.name}| = ∐_n ({self.name}_n × Δ^n) / ~"
    
    @classmethod
    def standard_simplex(cls, n: int) -> 'SimplicialSet':
        """Δ^n = Hom_Δ(-, [n])."""
        return cls(f"Δ^{n}")
    
    @classmethod
    def nerve(cls, C: str) -> 'SimplicialSet':
        """Nerve of category C."""
        return cls(f"N({C})")

@dataclass
class KanComplex:
    """
    Kan complex: simplicial set satisfying Kan extension condition.
    
    Every horn Λ^n_k → X extends to Δ^n → X.
    """
    simplicial_set: SimplicialSet
    
    def horn_extension(self, n: int, k: int) -> str:
        """Horn extension property."""
        return f"Λ^{n}_{k} → {self.simplicial_set.name} extends to Δ^{n}"
    
    def homotopy_groups(self, basepoint: str) -> str:
        """π_n(X, x)."""
        return f"π_n({self.simplicial_set.name}, {basepoint})"
    
    @classmethod
    def singular_complex(cls, X: str) -> 'KanComplex':
        """Sing(X) - singular simplicial set."""
        return cls(SimplicialSet(f"Sing({X})"))

# ═══════════════════════════════════════════════════════════════════════════════
# QUASICATEGORIES (∞-CATEGORIES)
# ═══════════════════════════════════════════════════════════════════════════════

@dataclass
class Quasicategory:
    """
    Quasicategory (weak Kan complex / ∞-category).
    
    Simplicial set where inner horns extend:
    Λ^n_k → X extends for 0 < k < n.
    """
    name: str
    
    def inner_horn_condition(self, n: int, k: int) -> str:
        """Inner horn extension (0 < k < n)."""
        if 0 < k < n:
            return f"Λ^{n}_{k} → {self.name} extends to Δ^{n}"
        return "Not an inner horn"
    
    def objects(self) -> str:
        """0-simplices."""
        return f"Ob({self.name}) = {self.name}_0"
    
    def morphisms(self, x: str, y: str) -> str:
        """Mapping space Hom(x, y)."""
        return f"Hom_{{{self.name}}}({x}, {y})"
    
    def homotopy_category(self) -> str:
        """h(C) - ordinary category from quasicategory."""
        return f"h({self.name})"
    
    @classmethod
    def nerve_of_category(cls, C: str) -> 'Quasicategory':
        """N(C) is a quasicategory (actually strict)."""
        return cls(f"N({C})")

@dataclass
class InfinityCategory:
    """
    ∞-category in Lurie's sense.
    
    Can be modeled as:
    - Quasicategory
    - Complete Segal space
    - Segal category
    - Model category
    """
    name: str
    model: str = "quasicategory"
    
    def mapping_space(self, x: str, y: str) -> str:
        """Map_C(x, y) - mapping ∞-groupoid."""
        return f"Map_{{{self.name}}}({x}, {y})"
    
    def limits_colimits(self) -> str:
        """∞-categorical limits."""
        return f"lim, colim exist in {self.name}"
    
    def adjunctions(self) -> str:
        """∞-categorical adjunction."""
        return f"F ⊣ G: {self.name} ⇌ D"
    
    @classmethod
    def spaces(cls) -> 'InfinityCategory':
        """𝒮 - ∞-category of spaces (∞-groupoids)."""
        return cls("𝒮", "Kan complexes")
    
    @classmethod
    def spectra(cls) -> 'InfinityCategory':
        """Sp - ∞-category of spectra."""
        return cls("Sp", "stable")

# ═══════════════════════════════════════════════════════════════════════════════
# STABLE ∞-CATEGORIES
# ═══════════════════════════════════════════════════════════════════════════════

@dataclass
class StableInfinityCategory:
    """
    Stable ∞-category.
    
    - Has zero object
    - Has fiber and cofiber sequences
    - Fiber ≃ cofiber (loop-suspension equivalence)
    """
    name: str
    
    def zero_object(self) -> str:
        """0 is both initial and terminal."""
        return f"0 ∈ {self.name}: initial and terminal"
    
    def fiber_cofiber(self) -> str:
        """Fiber sequences = cofiber sequences."""
        return "X → Y → Z → X[1] (exact triangle)"
    
    def suspension(self) -> str:
        """Suspension functor Σ = [1]."""
        return "Σ: C → C, Σ ≃ cofib(0 → -)"
    
    def loop(self) -> str:
        """Loop functor Ω = [-1]."""
        return "Ω: C → C, Ω ≃ fib(- → 0)"
    
    def triangulated_homotopy(self) -> str:
        """h(C) is triangulated."""
        return f"h({self.name}) is triangulated category"
    
    @classmethod
    def derived_category(cls, A: str) -> 'StableInfinityCategory':
        """D(A) as stable ∞-category."""
        return cls(f"D({A})")

# ═══════════════════════════════════════════════════════════════════════════════
# (∞,n)-CATEGORIES
# ═══════════════════════════════════════════════════════════════════════════════

@dataclass
class InfinityNCategory:
    """
    (∞,n)-category: ∞-category where k-morphisms are invertible for k > n.
    
    - (∞,0)-category = ∞-groupoid = space
    - (∞,1)-category = ∞-category (usual)
    - (∞,2)-category = ∞-bicategory
    """
    n: int
    name: str
    
    def description(self) -> str:
        """Description of (∞,n)-category."""
        if self.n == 0:
            return f"{self.name}: (∞,0)-category = space/∞-groupoid"
        elif self.n == 1:
            return f"{self.name}: (∞,1)-category = ∞-category"
        else:
            return f"{self.name}: (∞,{self.n})-category"
    
    def morphism_category(self) -> str:
        """Hom is (∞,n-1)-category."""
        return f"Hom_{{{self.name}}} is (∞,{self.n-1})-category"

# ═══════════════════════════════════════════════════════════════════════════════
# LOCALIZATION AND PRESENTABILITY
# ═══════════════════════════════════════════════════════════════════════════════

@dataclass
class BousfieldLocalization:
    """
    Bousfield localization L_W C.
    
    Formally invert class W of morphisms.
    """
    category: str
    localizing_class: str
    
    def localization(self) -> str:
        """L_W C."""
        return f"L_{{{self.localizing_class}}} {self.category}"
    
    def local_objects(self) -> str:
        """W-local objects."""
        return f"{{X : f^* → X bijection for f ∈ {self.localizing_class}}}"

@dataclass
class PresentableCategory:
    """
    Presentable ∞-category.
    
    - Has all small colimits
    - Accessible: has κ-compact generators for some κ
    """
    name: str
    
    def colimit_completeness(self) -> str:
        """All small colimits exist."""
        return f"{self.name} has all small colimits"
    
    def compact_generation(self) -> str:
        """κ-compact generation."""
        return f"{self.name} = Ind_κ({self.name}^κ)"
    
    def adjoint_functor_theorem(self) -> str:
        """Presentable AFT."""
        return "F: C → D has right adjoint ⟺ F preserves colimits"

# ═══════════════════════════════════════════════════════════════════════════════
# POLE BRIDGE
# ═══════════════════════════════════════════════════════════════════════════════

@dataclass
class InfinityCategoryPoleBridge:
    """
    Bridge between ∞-category theory and pole structure.
    """
    
    @staticmethod
    def psi_pole_as_higher_morphisms() -> str:
        """
        Ψ-pole corresponds to higher morphism hierarchy.
        n-morphisms for all n.
        """
        return "Ψ ↔ Higher: n-morphisms form hierarchy"
    
    @staticmethod
    def c_pole_as_simplicial() -> str:
        """
        C-pole corresponds to simplicial structure.
        Topological/continuous nature.
        """
        return "C ↔ Simplicial: Δ^n → X continuous"
    
    @staticmethod
    def d_pole_as_model() -> str:
        """
        D-pole corresponds to model structure.
        Weak equivalences as discrete class.
        """
        return "D ↔ Model: W, Fib, Cof discrete classes"
    
    @staticmethod
    def gateway_as_quillen() -> str:
        """
        Gateway corresponds to Quillen equivalences.
        Category correspondences.
        """
        return "Gateway ↔ Quillen: Ho(C) ≃ Ho(D)"
    
    @staticmethod
    def sigma_pole_as_homotopy() -> str:
        """
        Σ-pole corresponds to homotopy.
        Equivalence up to homotopy.
        """
        return "Σ ↔ Homotopy: f ~ g homotopic"

# ═══════════════════════════════════════════════════════════════════════════════
# CONVENIENCE FUNCTIONS
# ═══════════════════════════════════════════════════════════════════════════════

def model_category(name: str) -> ModelCategory:
    """Create model category."""
    return ModelCategory(name, ModelStructure(name))

def quillen_adjunction(L: str, R: str, 
                       C: ModelCategory, D: ModelCategory) -> QuillenAdjunction:
    """Create Quillen adjunction."""
    return QuillenAdjunction(L, R, C, D)

def quasicategory(name: str) -> Quasicategory:
    """Create quasicategory."""
    return Quasicategory(name)

def infinity_category(name: str) -> InfinityCategory:
    """Create ∞-category."""
    return InfinityCategory(name)

def stable_infinity(name: str) -> StableInfinityCategory:
    """Create stable ∞-category."""
    return StableInfinityCategory(name)

def simplicial_set(name: str) -> SimplicialSet:
    """Create simplicial set."""
    return SimplicialSet(name)

def kan_complex(X: SimplicialSet) -> KanComplex:
    """Create Kan complex."""
    return KanComplex(X)

# ═══════════════════════════════════════════════════════════════════════════════
# MODULE EXPORTS
# ═══════════════════════════════════════════════════════════════════════════════

__all__ = [
    # Model categories
    'ModelStructure',
    'ModelCategory',
    'QuillenAdjunction',
    'QuillenEquivalence',
    
    # Simplicial
    'SimplicialSet',
    'KanComplex',
    
    # ∞-categories
    'Quasicategory',
    'InfinityCategory',
    'StableInfinityCategory',
    'InfinityNCategory',
    
    # Localization
    'BousfieldLocalization',
    'PresentableCategory',
    
    # Bridge
    'InfinityCategoryPoleBridge',
    
    # Functions
    'model_category',
    'quillen_adjunction',
    'quasicategory',
    'infinity_category',
    'stable_infinity',
    'simplicial_set',
    'kan_complex',
]
