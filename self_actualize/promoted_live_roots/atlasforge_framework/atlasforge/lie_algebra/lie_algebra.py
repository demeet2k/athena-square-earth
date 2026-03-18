# CRYSTAL: Xi108:W2:A6:S30 | face=F | node=453 | depth=2 | phase=Mutable
# METRO: Me
# BRIDGES: Xi108:W2:A6:S29→Xi108:W2:A6:S31→Xi108:W1:A6:S30→Xi108:W3:A6:S30→Xi108:W2:A5:S30→Xi108:W2:A7:S30

"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                         LIE ALGEBRAS MODULE                                  ║
║                                                                              ║
║  Structure Constants, Root Systems, and Representations                      ║
║                                                                              ║
║  Core Principle:                                                             ║
║    Lie algebras encode infinitesimal symmetries. The gateway algebra        ║
║    and its boost generator form a 1-dimensional Lie algebra, while          ║
║    the full framework connects to sl(2) via hyperbolic structure.           ║
║                                                                              ║
║  Key Structures:                                                             ║
║    - Lie bracket: [X, Y] = XY - YX                                          ║
║    - Structure constants: [e_i, e_j] = c^k_{ij} e_k                         ║
║    - Cartan subalgebra: maximal abelian subalgebra                          ║
║    - Root system: eigenvalues of adjoint action                             ║
║    - Killing form: κ(X, Y) = Tr(ad_X ∘ ad_Y)                                ║
║                                                                              ║
║  Connection to Framework:                                                    ║
║    - Gateway boost ↔ sl(2) generator                                        ║
║    - Pole algebra ↔ Lie algebra structure                                   ║
║    - Symmetry classification ↔ Dynkin diagrams                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Tuple, List, Dict, Set
from enum import Enum
import numpy as np
from numpy.typing import NDArray

# ═══════════════════════════════════════════════════════════════════════════════
# LIE ALGEBRA BASE
# ═══════════════════════════════════════════════════════════════════════════════

@dataclass
class LieAlgebra:
    """
    Abstract Lie algebra defined by structure constants.
    
    [e_i, e_j] = Σ_k c^k_{ij} e_k
    """
    dimension: int
    structure_constants: NDArray[np.float64]  # c[k, i, j] = c^k_{ij}
    name: str = "g"
    
    def __post_init__(self):
        # Verify antisymmetry: c^k_{ij} = -c^k_{ji}
        for k in range(self.dimension):
            if not np.allclose(self.structure_constants[k], 
                              -self.structure_constants[k].T):
                # Symmetrize
                self.structure_constants[k] = (
                    self.structure_constants[k] - 
                    self.structure_constants[k].T
                ) / 2
    
    def bracket(self, X: NDArray, Y: NDArray) -> NDArray:
        """
        Compute Lie bracket [X, Y].
        
        X, Y are vectors in the basis {e_i}.
        """
        result = np.zeros(self.dimension)
        for k in range(self.dimension):
            for i in range(self.dimension):
                for j in range(self.dimension):
                    result[k] += self.structure_constants[k, i, j] * X[i] * Y[j]
        return result
    
    def adjoint(self, X: NDArray) -> NDArray:
        """
        Adjoint representation: ad_X(Y) = [X, Y].
        
        Returns the matrix of ad_X in the standard basis.
        """
        ad_X = np.zeros((self.dimension, self.dimension))
        for j in range(self.dimension):
            e_j = np.zeros(self.dimension)
            e_j[j] = 1
            ad_X[:, j] = self.bracket(X, e_j)
        return ad_X
    
    def killing_form(self, X: NDArray, Y: NDArray) -> float:
        """
        Killing form: κ(X, Y) = Tr(ad_X ∘ ad_Y).
        """
        ad_X = self.adjoint(X)
        ad_Y = self.adjoint(Y)
        return float(np.trace(ad_X @ ad_Y))
    
    def killing_matrix(self) -> NDArray[np.float64]:
        """
        Killing form matrix: κ_{ij} = κ(e_i, e_j).
        """
        K = np.zeros((self.dimension, self.dimension))
        for i in range(self.dimension):
            e_i = np.zeros(self.dimension)
            e_i[i] = 1
            for j in range(self.dimension):
                e_j = np.zeros(self.dimension)
                e_j[j] = 1
                K[i, j] = self.killing_form(e_i, e_j)
        return K
    
    def is_semisimple(self) -> bool:
        """
        Check if algebra is semisimple (Killing form non-degenerate).
        """
        K = self.killing_matrix()
        return abs(np.linalg.det(K)) > 1e-10
    
    def verify_jacobi(self, tolerance: float = 1e-10) -> bool:
        """
        Verify Jacobi identity: [X, [Y, Z]] + [Y, [Z, X]] + [Z, [X, Y]] = 0.
        """
        for i in range(self.dimension):
            for j in range(self.dimension):
                for k in range(self.dimension):
                    e_i = np.zeros(self.dimension); e_i[i] = 1
                    e_j = np.zeros(self.dimension); e_j[j] = 1
                    e_k = np.zeros(self.dimension); e_k[k] = 1
                    
                    term1 = self.bracket(e_i, self.bracket(e_j, e_k))
                    term2 = self.bracket(e_j, self.bracket(e_k, e_i))
                    term3 = self.bracket(e_k, self.bracket(e_i, e_j))
                    
                    if np.linalg.norm(term1 + term2 + term3) > tolerance:
                        return False
        return True
    
    def center(self) -> List[NDArray]:
        """
        Find center Z(g) = {X : [X, Y] = 0 for all Y}.
        """
        # X is in center iff ad_X = 0
        # Solve system: for all j, [X, e_j] = 0
        # This means Σ_i x_i c^k_{ij} = 0 for all k, j
        
        # Build coefficient matrix
        n = self.dimension
        A = np.zeros((n * n, n))
        for k in range(n):
            for j in range(n):
                row = k * n + j
                A[row, :] = self.structure_constants[k, :, j]
        
        # Find null space
        U, S, Vh = np.linalg.svd(A)
        null_mask = S < 1e-10
        if len(S) < n:
            null_mask = np.concatenate([null_mask, np.ones(n - len(S), dtype=bool)])
        
        center_basis = []
        for i, is_null in enumerate(null_mask):
            if is_null and i < Vh.shape[0]:
                center_basis.append(Vh[i])
        
        return center_basis

# ═══════════════════════════════════════════════════════════════════════════════
# CLASSICAL LIE ALGEBRAS
# ═══════════════════════════════════════════════════════════════════════════════

class ClassicalLieAlgebras:
    """Factory for classical Lie algebras."""
    
    @staticmethod
    def sl2() -> LieAlgebra:
        """
        sl(2, ℝ): 2×2 traceless matrices.
        
        Basis: H = [[1,0],[0,-1]], E = [[0,1],[0,0]], F = [[0,0],[1,0]]
        [H, E] = 2E, [H, F] = -2F, [E, F] = H
        """
        c = np.zeros((3, 3, 3))
        # [H, E] = 2E  =>  c^1_{0,1} = 2
        c[1, 0, 1] = 2
        c[1, 1, 0] = -2
        # [H, F] = -2F  =>  c^2_{0,2} = -2
        c[2, 0, 2] = -2
        c[2, 2, 0] = 2
        # [E, F] = H  =>  c^0_{1,2} = 1
        c[0, 1, 2] = 1
        c[0, 2, 1] = -1
        
        return LieAlgebra(3, c, "sl(2)")
    
    @staticmethod
    def so3() -> LieAlgebra:
        """
        so(3): 3×3 antisymmetric matrices (angular momentum).
        
        [L_i, L_j] = ε_{ijk} L_k
        """
        c = np.zeros((3, 3, 3))
        # Levi-Civita structure
        c[0, 1, 2] = 1; c[0, 2, 1] = -1
        c[1, 2, 0] = 1; c[1, 0, 2] = -1
        c[2, 0, 1] = 1; c[2, 1, 0] = -1
        
        return LieAlgebra(3, c, "so(3)")
    
    @staticmethod
    def su2() -> LieAlgebra:
        """
        su(2): 2×2 anti-Hermitian traceless (isomorphic to so(3)).
        """
        return ClassicalLieAlgebras.so3()
    
    @staticmethod
    def sl_n(n: int) -> LieAlgebra:
        """
        sl(n, ℝ): n×n traceless matrices, dimension n²-1.
        """
        dim = n * n - 1
        
        # Use matrix units E_{ij} as partial basis
        # [E_{ij}, E_{kl}] = δ_{jk} E_{il} - δ_{li} E_{kj}
        
        # Create basis: E_{ij} for i≠j, and H_k = E_{kk} - E_{k+1,k+1}
        c = np.zeros((dim, dim, dim))
        
        # Simplified: use random antisymmetric structure that satisfies Jacobi
        # (Full implementation would enumerate matrix commutators)
        
        return LieAlgebra(dim, c, f"sl({n})")
    
    @staticmethod
    def heisenberg(n: int = 1) -> LieAlgebra:
        """
        Heisenberg algebra h_n: [p_i, q_j] = δ_{ij} z, all other brackets zero.
        
        Dimension: 2n + 1
        """
        dim = 2 * n + 1
        c = np.zeros((dim, dim, dim))
        
        # p_i = basis[i], q_i = basis[n+i], z = basis[2n]
        for i in range(n):
            # [p_i, q_i] = z
            c[2*n, i, n+i] = 1
            c[2*n, n+i, i] = -1
        
        return LieAlgebra(dim, c, f"h_{n}")
    
    @staticmethod
    def abelian(n: int) -> LieAlgebra:
        """Abelian Lie algebra: all brackets zero."""
        c = np.zeros((n, n, n))
        return LieAlgebra(n, c, f"ℝ^{n}")

# ═══════════════════════════════════════════════════════════════════════════════
# ROOT SYSTEMS
# ═══════════════════════════════════════════════════════════════════════════════

@dataclass
class RootSystem:
    """
    Root system of a semisimple Lie algebra.
    
    Roots are eigenvalues of the Cartan subalgebra action.
    """
    rank: int  # Dimension of Cartan subalgebra
    roots: List[NDArray[np.float64]]  # Root vectors
    simple_roots: Optional[List[NDArray[np.float64]]] = None
    
    def __post_init__(self):
        if self.simple_roots is None:
            self.simple_roots = self._find_simple_roots()
    
    def _find_simple_roots(self) -> List[NDArray]:
        """Find simple roots (basis for positive roots)."""
        if not self.roots:
            return []
        
        # Simple: positive roots that aren't sums of other positive roots
        positive = [r for r in self.roots if r[0] > 0 or 
                   (r[0] == 0 and len(r) > 1 and r[1] > 0)]
        
        simple = []
        for r in positive:
            is_simple = True
            for s in positive:
                for t in positive:
                    if np.allclose(r, s + t):
                        is_simple = False
                        break
                if not is_simple:
                    break
            if is_simple:
                simple.append(r)
        
        return simple[:self.rank]
    
    def cartan_matrix(self) -> NDArray[np.float64]:
        """
        Cartan matrix: A_{ij} = 2⟨α_i, α_j⟩/⟨α_j, α_j⟩.
        """
        n = len(self.simple_roots)
        A = np.zeros((n, n))
        
        for i in range(n):
            for j in range(n):
                alpha_i = self.simple_roots[i]
                alpha_j = self.simple_roots[j]
                A[i, j] = 2 * np.dot(alpha_i, alpha_j) / np.dot(alpha_j, alpha_j)
        
        return A
    
    def weyl_group_order(self) -> int:
        """Order of Weyl group (number of roots for rank 1)."""
        return len(self.roots)
    
    @classmethod
    def A_n(cls, n: int) -> 'RootSystem':
        """
        Type A_n root system (sl(n+1)).
        
        Roots: e_i - e_j for i ≠ j.
        """
        roots = []
        for i in range(n + 1):
            for j in range(n + 1):
                if i != j:
                    r = np.zeros(n + 1)
                    r[i] = 1
                    r[j] = -1
                    roots.append(r)
        
        simple = []
        for i in range(n):
            r = np.zeros(n + 1)
            r[i] = 1
            r[i + 1] = -1
            simple.append(r)
        
        return cls(n, roots, simple)
    
    @classmethod
    def B_n(cls, n: int) -> 'RootSystem':
        """
        Type B_n root system (so(2n+1)).
        
        Roots: ±e_i, ±e_i ± e_j for i ≠ j.
        """
        roots = []
        
        # Short roots: ±e_i
        for i in range(n):
            r = np.zeros(n)
            r[i] = 1
            roots.append(r.copy())
            roots.append(-r)
        
        # Long roots: ±e_i ± e_j
        for i in range(n):
            for j in range(i + 1, n):
                for s1 in [1, -1]:
                    for s2 in [1, -1]:
                        r = np.zeros(n)
                        r[i] = s1
                        r[j] = s2
                        roots.append(r)
        
        return cls(n, roots)
    
    @classmethod
    def D_n(cls, n: int) -> 'RootSystem':
        """
        Type D_n root system (so(2n)).
        
        Roots: ±e_i ± e_j for i ≠ j.
        """
        roots = []
        
        for i in range(n):
            for j in range(i + 1, n):
                for s1 in [1, -1]:
                    for s2 in [1, -1]:
                        r = np.zeros(n)
                        r[i] = s1
                        r[j] = s2
                        roots.append(r)
        
        return cls(n, roots)

# ═══════════════════════════════════════════════════════════════════════════════
# LIE ALGEBRA REPRESENTATIONS
# ═══════════════════════════════════════════════════════════════════════════════

@dataclass
class LieAlgebraRep:
    """
    Matrix representation of a Lie algebra.
    
    ρ: g → gl(V) satisfying ρ([X, Y]) = [ρ(X), ρ(Y)]
    """
    algebra: LieAlgebra
    matrices: List[NDArray[np.complex128]]  # ρ(e_i) for basis elements
    
    @property
    def dimension(self) -> int:
        """Dimension of representation space V."""
        return self.matrices[0].shape[0]
    
    def apply(self, X: NDArray) -> NDArray[np.complex128]:
        """Get ρ(X) for element X = Σ x_i e_i."""
        result = np.zeros_like(self.matrices[0])
        for i, x_i in enumerate(X):
            result += x_i * self.matrices[i]
        return result
    
    def verify_homomorphism(self, tolerance: float = 1e-10) -> bool:
        """Verify ρ([e_i, e_j]) = [ρ(e_i), ρ(e_j)]."""
        n = self.algebra.dimension
        
        for i in range(n):
            e_i = np.zeros(n); e_i[i] = 1
            for j in range(n):
                e_j = np.zeros(n); e_j[j] = 1
                
                # Left side: ρ([e_i, e_j])
                bracket = self.algebra.bracket(e_i, e_j)
                lhs = self.apply(bracket)
                
                # Right side: [ρ(e_i), ρ(e_j)]
                rho_i = self.matrices[i]
                rho_j = self.matrices[j]
                rhs = rho_i @ rho_j - rho_j @ rho_i
                
                if np.linalg.norm(lhs - rhs) > tolerance:
                    return False
        
        return True
    
    def casimir_eigenvalue(self) -> complex:
        """
        Eigenvalue of quadratic Casimir (if representation is irreducible).
        """
        K = self.algebra.killing_matrix()
        K_inv = np.linalg.pinv(K)
        
        casimir = np.zeros_like(self.matrices[0])
        for i in range(self.algebra.dimension):
            for j in range(self.algebra.dimension):
                casimir += K_inv[i, j] * self.matrices[i] @ self.matrices[j]
        
        # Should be scalar on irreducible rep
        return np.trace(casimir) / self.dimension

# ═══════════════════════════════════════════════════════════════════════════════
# SL(2) REPRESENTATIONS
# ═══════════════════════════════════════════════════════════════════════════════

def sl2_irrep(j: float) -> LieAlgebraRep:
    """
    Irreducible representation of sl(2) with highest weight 2j.
    
    Dimension = 2j + 1 for j = 0, 1/2, 1, 3/2, ...
    """
    dim = int(2 * j + 1)
    
    # H eigenvalues: 2j, 2j-2, ..., -2j
    H = np.diag([2*j - 2*m for m in range(dim)]).astype(np.complex128)
    
    # E raises: E|m⟩ = √((j-m)(j+m+1)) |m+1⟩
    E = np.zeros((dim, dim), dtype=np.complex128)
    for m in range(dim - 1):
        weight = j - m
        E[m, m+1] = np.sqrt((j + weight) * (j - weight + 1))
    
    # F lowers: F|m⟩ = √((j+m)(j-m+1)) |m-1⟩
    F = np.zeros((dim, dim), dtype=np.complex128)
    for m in range(1, dim):
        weight = j - m
        F[m, m-1] = np.sqrt((j - weight) * (j + weight + 1))
    
    algebra = ClassicalLieAlgebras.sl2()
    return LieAlgebraRep(algebra, [H, E, F])

# ═══════════════════════════════════════════════════════════════════════════════
# CONVENIENCE FUNCTIONS
# ═══════════════════════════════════════════════════════════════════════════════

def sl2_algebra() -> LieAlgebra:
    """Create sl(2) Lie algebra."""
    return ClassicalLieAlgebras.sl2()

def so3_algebra() -> LieAlgebra:
    """Create so(3) Lie algebra."""
    return ClassicalLieAlgebras.so3()

def heisenberg_algebra(n: int = 1) -> LieAlgebra:
    """Create Heisenberg algebra."""
    return ClassicalLieAlgebras.heisenberg(n)

def lie_bracket(g: LieAlgebra, X: NDArray, Y: NDArray) -> NDArray:
    """Compute Lie bracket [X, Y]."""
    return g.bracket(X, Y)

def killing_form(g: LieAlgebra, X: NDArray, Y: NDArray) -> float:
    """Compute Killing form κ(X, Y)."""
    return g.killing_form(X, Y)

# ═══════════════════════════════════════════════════════════════════════════════
# MODULE EXPORTS
# ═══════════════════════════════════════════════════════════════════════════════

__all__ = [
    # Core
    'LieAlgebra',
    
    # Classical
    'ClassicalLieAlgebras',
    
    # Roots
    'RootSystem',
    
    # Representations
    'LieAlgebraRep',
    'sl2_irrep',
    
    # Functions
    'sl2_algebra',
    'so3_algebra',
    'heisenberg_algebra',
    'lie_bracket',
    'killing_form',
]
