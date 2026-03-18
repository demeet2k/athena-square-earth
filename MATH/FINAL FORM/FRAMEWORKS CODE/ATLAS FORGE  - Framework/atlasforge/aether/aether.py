# CRYSTAL: Xi108:W2:A9:S15 | face=S | node=114 | depth=2 | phase=Cardinal
# METRO: Me
# BRIDGES: Xi108:W2:A9:S14→Xi108:W2:A9:S16→Xi108:W1:A9:S15→Xi108:W3:A9:S15→Xi108:W2:A8:S15→Xi108:W2:A10:S15

"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                        AETHER LATTICE MODULE                                 ║
║                                                                              ║
║  The Complete 4×4×4 Mathematical Coordinate System                           ║
║                                                                              ║
║  Z-Point: RT□ + RT✿ + RT☁ + RT⟂ with commutator→BO_R rule                  ║
║                                                                              ║
║  Three Axes:                                                                 ║
║    LENS (4):   □ EARTH | ✿ FIRE | ☁ WATER | ⟂ AIR                          ║
║    PHASE (4):  Inhale | Metabolize | Exhale | Oxygen                        ║
║    BUNDLE (4): Form | Invariants | Dynamics | Verification                  ║
║                                                                              ║
║  Slots: Core(0) | Ticket(1) | Residual(2) | Test(3)                         ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Tuple, List, Dict, Any, Set
from enum import Enum
import numpy as np

# ═══════════════════════════════════════════════════════════════════════════════
# LENS AXIS (L0-L3)
# ═══════════════════════════════════════════════════════════════════════════════

class Lens(Enum):
    """
    The four lenses (elemental views).
    
    Each lens provides a distinct perspective on mathematical objects.
    """
    EARTH = 0   # □ Exact / Normal Form
    FIRE = 1    # ✿ Transform / Ticket / Domain
    WATER = 2   # ☁ Bound / Calibration / Top-k
    AIR = 3     # ⟂ Seed / Recursion / Idempotence
    
    @property
    def symbol(self) -> str:
        symbols = {Lens.EARTH: "□", Lens.FIRE: "✿", Lens.WATER: "☁", Lens.AIR: "⟂"}
        return symbols[self]
    
    @property
    def element(self) -> str:
        return self.name.title()
    
    @property
    def description(self) -> str:
        desc = {
            Lens.EARTH: "Exact / Normal Form",
            Lens.FIRE: "Transform / Ticket / Domain",
            Lens.WATER: "Bound / Calibration / Top-k",
            Lens.AIR: "Seed / Recursion / Idempotence"
        }
        return desc[self]
    
    @property
    def rt_stamp(self) -> str:
        """Round-trip stamp for this lens."""
        return f"RT{self.symbol}"

class AetherPhase(Enum):
    """
    The four phases of the breath cycle.
    """
    INHALE = 0     # Expansion, candidate generation
    METABOLIZE = 1  # Processing, transformation
    EXHALE = 2      # Publication, output
    OXYGEN = 3      # Storage, templates
    
    @property
    def short_name(self) -> str:
        return self.name[:3]

class AetherBundle(Enum):
    """
    The four bundles at each phase.
    """
    FORM = 0        # Core structural representation
    INVARIANTS = 1  # Conserved quantities, selectors
    DYNAMICS = 2    # Transformation operators
    VERIFICATION = 3  # RT stamps, certificates

class Slot(Enum):
    """
    The four slots for data organization.
    """
    CORE = 0      # Primary content
    TICKET = 1    # Transformation record
    RESIDUAL = 2  # Error/drift
    TEST = 3      # Verification fixtures

# ═══════════════════════════════════════════════════════════════════════════════
# CELL DEFINITION
# ═══════════════════════════════════════════════════════════════════════════════

@dataclass
class AetherCell:
    """
    A single cell in the 4×4×4 AETHER lattice.
    
    Located at (Lens, Phase, Bundle) coordinates.
    """
    lens: Lens
    phase: AetherPhase
    bundle: AetherBundle
    
    core: str = ""              # What this cell represents
    letters: List[str] = field(default_factory=list)  # Associated letter codes
    slot_keys: List[int] = field(default_factory=list)  # Which slots dominate
    
    @property
    def coordinate(self) -> str:
        """L?/P?/B? notation."""
        return f"L{self.lens.value}/P{self.phase.value}/B{self.bundle.value}"
    
    @property
    def full_name(self) -> str:
        """Human-readable name."""
        return f"{self.lens.element}/{self.phase.name.title()}/{self.bundle.name.title()}"

# ═══════════════════════════════════════════════════════════════════════════════
# LETTER DEFINITIONS (A-Z)
# ═══════════════════════════════════════════════════════════════════════════════

@dataclass
class AetherLetter:
    """
    A letter in the AETHER alphabet.
    
    Each letter has a Z-point definition and cell assignments.
    """
    letter: str
    z_point: str  # Core definition
    cells: List[str] = field(default_factory=list)  # Cell coordinates
    slot_keys: List[int] = field(default_factory=list)

# Complete AETHER alphabet
AETHER_ALPHABET: Dict[str, AetherLetter] = {
    'A': AetherLetter('A', "4^4 grammar + RT gates", ["L0/P0/B0"], [0, 1]),
    'B': AetherLetter('B', "BO=(Q,U,δ,ε,n,A)", ["L2/P0/B0", "L2/P0/B3", "L2/P3/B0"], [0, 3, 2]),
    'C': AetherLetter('C', "Canon²=Canon", ["L0/P1/B0", "L0/P2/B0", "L0/P3/B0"], [0, 1, 2, 3]),
    'D': AetherLetter('D', "ε tuple + witnesses", ["META/*/P2/B2", "META/*/P0/B3"], [2, 3]),
    'E': AetherLetter('E', "RT gates are elemental laws", ["META/*/P0/B3", "META/*/P3/B3"], [3]),
    'F': AetherLetter('F', "Fourier hub + ticket", ["L1/P1/B0", "L1/P2/B0"], [0, 1]),
    'G': AetherLetter('G', "ticket is part of object", ["L1/P0/B1", "L1/P3/B1"], [1, 3]),
    'H': AetherLetter('H', "HubWord + ticket + domain", ["L1/P0/B2", "L1/P3/B0"], [0]),
    'I': AetherLetter('I', "I-hash stable", ["L0/P0/B1"], [0, 1, 3]),
    'J': AetherLetter('J', "∂λΦ=0 with λ* in domain", ["L1/P1/B2"], [0, 2]),
    'K': AetherLetter('K', "kernel/renorm identities", ["L3/P0/B2", "L3/P3/B2"], [0]),
    'L': AetherLetter('L', "log turns products to sums (branch ticket)", ["L1/P1/B2"], [0, 2]),
    'M': AetherLetter('M', "Φ=α|O|+βk+γ||ε||", ["META/*/P1/B3"], [3]),
    'N': AetherLetter('N', "structure/chain hash", ["L0/P2/B3", "L3/P2/B3"], [3, 2]),
    'O': AetherLetter('O', "oxygen monotone union", ["META/*/P3/B3"], [3]),
    'P': AetherLetter('P', "obligation DAG", ["L0/P0/B3"], [3, 2]),
    'Q': AetherLetter('Q', "quality gates RT registry", ["META/*/P0/B3", "META/*/P2/B3"], [3, 2]),
    'R': AetherLetter('R', "repair operators", ["META/*/P1/B2", "META/*/P1/B3"], [2, 3]),
    'S': AetherLetter('S', "seed schema + RT⟂", ["L3/P0/B0", "L3/P0/B3"], [0, 3, 2]),
    'T': AetherLetter('T', "promotion by fixtures only", ["META/*/P3/B3"], [3]),
    'U': AetherLetter('U', "top-k enforced when unstable", ["L2/P1/B3"], [3]),
    'V': AetherLetter('V', "fixtures/verifiers", ["META/*/P0/B3", "META/*/P3/B3"], [3, 2]),
    'W': AetherLetter('W', "Wick legal iff mgf exists", ["L1/P1/B2"], [0, 2]),
    'X': AetherLetter('X', "commutator R", ["META/*/P1/B2", "L2/P2/B2"], [2, 3]),
    'Y': AetherLetter('Y', "selectors collapse multivalued inverse", ["META/*/P0/B1"], [1, 3]),
    'Z': AetherLetter('Z', "zero-point atlas", ["META/*/P0/B1", "META/*/P3/B1"], [1, 3]),
}

# ═══════════════════════════════════════════════════════════════════════════════
# AETHER LATTICE
# ═══════════════════════════════════════════════════════════════════════════════

@dataclass
class AetherLattice:
    """
    The complete 4×4×4 AETHER lattice.
    
    64 cells organized by Lens × Phase × Bundle.
    """
    cells: Dict[str, AetherCell] = field(default_factory=dict)
    
    def __post_init__(self):
        """Initialize all 64 cells."""
        if not self.cells:
            self._build_lattice()
    
    def _build_lattice(self):
        """Construct the complete lattice."""
        # L0 = EARTH (□)
        self._add_earth_cells()
        # L1 = FIRE (✿)
        self._add_fire_cells()
        # L2 = WATER (☁)
        self._add_water_cells()
        # L3 = AIR (⟂)
        self._add_air_cells()
    
    def _add_cell(self, lens: Lens, phase: AetherPhase, bundle: AetherBundle,
                  core: str, letters: List[str], slot_keys: List[int]):
        """Add a cell to the lattice."""
        cell = AetherCell(lens, phase, bundle, core, letters, slot_keys)
        self.cells[cell.coordinate] = cell
    
    def _add_earth_cells(self):
        """L0 = EARTH (□): Exact/Normal Form."""
        L = Lens.EARTH
        # P0 = Inhale
        self._add_cell(L, AetherPhase.INHALE, AetherBundle.FORM,
                      "Typed discrete object; finite structure", ['A','C','I','N','P'], [0,1])
        self._add_cell(L, AetherPhase.INHALE, AetherBundle.INVARIANTS,
                      "Exact invariants + selectors for uniqueness", ['I','Y','Z'], [0,1,3])
        self._add_cell(L, AetherPhase.INHALE, AetherBundle.DYNAMICS,
                      "Discrete operators (rewrite/mod/matrix)", ['C','F','K'], [0,2])
        self._add_cell(L, AetherPhase.INHALE, AetherBundle.VERIFICATION,
                      "Obligation DAG + RT□ definition", ['P','Q','V'], [3,2])
        # P1 = Metabolize
        self._add_cell(L, AetherPhase.METABOLIZE, AetherBundle.FORM,
                      "Canonicalize to NF; tie-breakers", ['C','N','G','Y'], [0,1,2])
        self._add_cell(L, AetherPhase.METABOLIZE, AetherBundle.INVARIANTS,
                      "Equivalence classes; Z-lock constraints", ['C','Y','Z','X'], [0,1])
        self._add_cell(L, AetherPhase.METABOLIZE, AetherBundle.DYNAMICS,
                      "Discrete commutators (order/index)", ['X','D','R'], [2,3])
        self._add_cell(L, AetherPhase.METABOLIZE, AetherBundle.VERIFICATION,
                      "Discharge/mark obligations; stop functional", ['P','Q','V','M'], [3])
        # P2 = Exhale
        self._add_cell(L, AetherPhase.EXHALE, AetherBundle.FORM,
                      "Publish canonical NF only", ['C','N'], [0])
        self._add_cell(L, AetherPhase.EXHALE, AetherBundle.INVARIANTS,
                      "Publish exact invariants (ε□=0)", ['I','Y','Z','Q'], [0,3])
        self._add_cell(L, AetherPhase.EXHALE, AetherBundle.DYNAMICS,
                      "Publish minimal exact operator identities", ['F','K','AETHER'], [0])
        self._add_cell(L, AetherPhase.EXHALE, AetherBundle.VERIFICATION,
                      "RT□ + structure-hash stamp", ['Q','V','N','R'], [3,2])
        # P3 = Oxygen
        self._add_cell(L, AetherPhase.OXYGEN, AetherBundle.FORM,
                      "Store canonicalizers as modules", ['C','N','T'], [0,3])
        self._add_cell(L, AetherPhase.OXYGEN, AetherBundle.INVARIANTS,
                      "Store tie-breaker policies", ['G','Y','Z','S'], [1])
        self._add_cell(L, AetherPhase.OXYGEN, AetherBundle.DYNAMICS,
                      "Store discrete rewrite templates", ['K','F','V'], [0])
        self._add_cell(L, AetherPhase.OXYGEN, AetherBundle.VERIFICATION,
                      "Fixture suite for □", ['V','Q','T','O'], [3])
    
    def _add_fire_cells(self):
        """L1 = FIRE (✿): Transform/Ticket/Domain."""
        L = Lens.FIRE
        # P0 = Inhale
        self._add_cell(L, AetherPhase.INHALE, AetherBundle.FORM,
                      "Choose hub candidates; transform-native rep", ['F','H','W','L','J'], [0,1])
        self._add_cell(L, AetherPhase.INHALE, AetherBundle.INVARIANTS,
                      "Declare domain/gauge selector", ['G','Y','Z','Q'], [1,3])
        self._add_cell(L, AetherPhase.INHALE, AetherBundle.DYNAMICS,
                      "HubWord skeleton (H⁻¹·H)", ['H','F','W','L','J'], [0])
        self._add_cell(L, AetherPhase.INHALE, AetherBundle.VERIFICATION,
                      "Define RT✿ on domain", ['Q','V','G','D'], [3,2])
        # P1 = Metabolize
        self._add_cell(L, AetherPhase.METABOLIZE, AetherBundle.FORM,
                      "HubNormalize to shared basis", ['F','H','G'], [0,1])
        self._add_cell(L, AetherPhase.METABOLIZE, AetherBundle.INVARIANTS,
                      "DomainTighten when conditional", ['Y','Z','G','X'], [1,2])
        self._add_cell(L, AetherPhase.METABOLIZE, AetherBundle.DYNAMICS,
                      "Execute Wick/Log/∂ chain legally", ['W','L','J','H','D'], [0,2])
        self._add_cell(L, AetherPhase.METABOLIZE, AetherBundle.VERIFICATION,
                      "Cross-route commutation checks", ['X','V','R'], [3,2])
        # P2 = Exhale
        self._add_cell(L, AetherPhase.EXHALE, AetherBundle.FORM,
                      "Publish hub-normal + ticket summary", ['F','H','G'], [0,1])
        self._add_cell(L, AetherPhase.EXHALE, AetherBundle.INVARIANTS,
                      "Publish domain as meaning", ['G','Y','Z'], [1])
        self._add_cell(L, AetherPhase.EXHALE, AetherBundle.DYNAMICS,
                      "Publish transform certificates", ['W','J','L','D'], [0,2])
        self._add_cell(L, AetherPhase.EXHALE, AetherBundle.VERIFICATION,
                      "RT✿ stamp", ['Q','V'], [3])
        # P3 = Oxygen
        self._add_cell(L, AetherPhase.OXYGEN, AetherBundle.FORM,
                      "Store metro templates", ['F','H','W','L','J','T'], [0])
        self._add_cell(L, AetherPhase.OXYGEN, AetherBundle.INVARIANTS,
                      "Store domain checklists", ['G','Y','Z'], [1])
        self._add_cell(L, AetherPhase.OXYGEN, AetherBundle.DYNAMICS,
                      "Store hubwords as generators", ['H','O'], [0])
        self._add_cell(L, AetherPhase.OXYGEN, AetherBundle.VERIFICATION,
                      "Hub legality regression suite", ['V','Q','T'], [3])
    
    def _add_water_cells(self):
        """L2 = WATER (☁): Bound/Calibration/Top-k."""
        L = Lens.WATER
        # P0 = Inhale
        self._add_cell(L, AetherPhase.INHALE, AetherBundle.FORM,
                      "Define uncertainty object Q", ['B','U'], [0])
        self._add_cell(L, AetherPhase.INHALE, AetherBundle.INVARIANTS,
                      "Risk semantics δ/ε", ['B','U','I'], [1])
        self._add_cell(L, AetherPhase.INHALE, AetherBundle.DYNAMICS,
                      "Select candidate inequality families", ['B','U','H'], [0,1])
        self._add_cell(L, AetherPhase.INHALE, AetherBundle.VERIFICATION,
                      "Define RT☁ + checklist", ['B','Q','V','D'], [3,2])
        # P1 = Metabolize
        self._add_cell(L, AetherPhase.METABOLIZE, AetherBundle.FORM,
                      "Canonicalize bounds to BO", ['B'], [0])
        self._add_cell(L, AetherPhase.METABOLIZE, AetherBundle.INVARIANTS,
                      "Dominance ordering under shared A", ['B','U'], [1])
        self._add_cell(L, AetherPhase.METABOLIZE, AetherBundle.DYNAMICS,
                      "Perturbation stability tests", ['U','V','X'], [3,2])
        self._add_cell(L, AetherPhase.METABOLIZE, AetherBundle.VERIFICATION,
                      "If unstable => top-k", ['U','Q','R'], [3])
        # P2 = Exhale
        self._add_cell(L, AetherPhase.EXHALE, AetherBundle.FORM,
                      "Publish canonical BO(s)", ['B'], [0])
        self._add_cell(L, AetherPhase.EXHALE, AetherBundle.INVARIANTS,
                      "Publish conditionality explicitly", ['B','U','D'], [1,2])
        self._add_cell(L, AetherPhase.EXHALE, AetherBundle.DYNAMICS,
                      "Publish commutator envelopes BO_R", ['X'], [2])
        self._add_cell(L, AetherPhase.EXHALE, AetherBundle.VERIFICATION,
                      "RT☁ stamp or top-k", ['Q','V','U'], [3])
        # P3 = Oxygen
        self._add_cell(L, AetherPhase.OXYGEN, AetherBundle.FORM,
                      "Store BO templates + canonicalizer", ['B','T'], [0])
        self._add_cell(L, AetherPhase.OXYGEN, AetherBundle.INVARIANTS,
                      "Store dominance comparators", ['B','U'], [1])
        self._add_cell(L, AetherPhase.OXYGEN, AetherBundle.DYNAMICS,
                      "Store residual envelope patterns", ['X'], [2])
        self._add_cell(L, AetherPhase.OXYGEN, AetherBundle.VERIFICATION,
                      "Calibration regression fixtures", ['V','Q','T','O'], [3])
    
    def _add_air_cells(self):
        """L3 = AIR (⟂): Seed/Recursion/Idempotence."""
        L = Lens.AIR
        # P0 = Inhale
        self._add_cell(L, AetherPhase.INHALE, AetherBundle.FORM,
                      "Seed schema + generators Σ", ['S','K'], [0])
        self._add_cell(L, AetherPhase.INHALE, AetherBundle.INVARIANTS,
                      "Uniqueness policy / selector vs top-k", ['Y','Z','S'], [1])
        self._add_cell(L, AetherPhase.INHALE, AetherBundle.DYNAMICS,
                      "Kernel identities (fixed points/zoom)", ['K','O'], [0])
        self._add_cell(L, AetherPhase.INHALE, AetherBundle.VERIFICATION,
                      "Define RT⟂ + checksums", ['S','Q','V','D'], [3,2])
        # P1 = Metabolize
        self._add_cell(L, AetherPhase.METABOLIZE, AetherBundle.FORM,
                      "Tighten schema to remove ambiguity", ['S','R'], [1,2])
        self._add_cell(L, AetherPhase.METABOLIZE, AetherBundle.INVARIANTS,
                      "Enforce selectors for single-valued inverse", ['Y','Z'], [1])
        self._add_cell(L, AetherPhase.METABOLIZE, AetherBundle.DYNAMICS,
                      "Compress repeating patterns into modules", ['K','O'], [0])
        self._add_cell(L, AetherPhase.METABOLIZE, AetherBundle.VERIFICATION,
                      "Certify commutation only in seed space", ['X','AETHER'], [3])
        # P2 = Exhale
        self._add_cell(L, AetherPhase.EXHALE, AetherBundle.FORM,
                      "Collapse to minimal seed", ['S'], [0])
        self._add_cell(L, AetherPhase.EXHALE, AetherBundle.INVARIANTS,
                      "Publish what seed reconstructs/refuses", ['Q'], [1,3])
        self._add_cell(L, AetherPhase.EXHALE, AetherBundle.DYNAMICS,
                      "Publish kernel generators", ['K'], [0])
        self._add_cell(L, AetherPhase.EXHALE, AetherBundle.VERIFICATION,
                      "RT⟂ stamp + chain-hash", ['S','N'], [3])
        # P3 = Oxygen
        self._add_cell(L, AetherPhase.OXYGEN, AetherBundle.FORM,
                      "Store seed libraries", ['S','O','T'], [0])
        self._add_cell(L, AetherPhase.OXYGEN, AetherBundle.INVARIANTS,
                      "Store selector law", ['Y','Z'], [1])
        self._add_cell(L, AetherPhase.OXYGEN, AetherBundle.DYNAMICS,
                      "Store commutation/stability controllers", ['K','X','O'], [0])
        self._add_cell(L, AetherPhase.OXYGEN, AetherBundle.VERIFICATION,
                      "Idempotence regression harness", ['V','Q','T'], [3])
    
    def get_cell(self, lens: Lens, phase: AetherPhase, bundle: AetherBundle) -> Optional[AetherCell]:
        """Get cell by coordinates."""
        coord = f"L{lens.value}/P{phase.value}/B{bundle.value}"
        return self.cells.get(coord)
    
    def get_cells_by_lens(self, lens: Lens) -> List[AetherCell]:
        """Get all cells for a lens."""
        return [c for c in self.cells.values() if c.lens == lens]
    
    def get_cells_by_phase(self, phase: AetherPhase) -> List[AetherCell]:
        """Get all cells for a phase."""
        return [c for c in self.cells.values() if c.phase == phase]
    
    def get_cells_by_letter(self, letter: str) -> List[AetherCell]:
        """Get all cells containing a letter."""
        return [c for c in self.cells.values() if letter in c.letters]
    
    @property
    def dimensions(self) -> Tuple[int, int, int]:
        """Return lattice dimensions."""
        return (4, 4, 4)
    
    @property
    def total_cells(self) -> int:
        """Total number of cells."""
        return len(self.cells)

# ═══════════════════════════════════════════════════════════════════════════════
# RT STAMPS (ROUND-TRIP VERIFICATION)
# ═══════════════════════════════════════════════════════════════════════════════

@dataclass
class RTStamp:
    """
    Round-trip verification stamp.
    
    RT□ + RT✿ + RT☁ + RT⟂ with commutator→BO_R rule.
    """
    lens: Lens
    verified: bool = False
    hash_value: str = ""
    timestamp: str = ""
    
    @property
    def symbol(self) -> str:
        return f"RT{self.lens.symbol}"
    
    @classmethod
    def verify(cls, lens: Lens, content: Any) -> 'RTStamp':
        """Create verified RT stamp."""
        import hashlib
        hash_value = hashlib.sha256(str(content).encode()).hexdigest()[:16]
        return cls(lens, True, hash_value)

@dataclass
class RTRegistry:
    """
    Registry of RT stamps across all lenses.
    """
    stamps: Dict[Lens, RTStamp] = field(default_factory=dict)
    
    def add_stamp(self, stamp: RTStamp):
        """Add a stamp to registry."""
        self.stamps[stamp.lens] = stamp
    
    def is_complete(self) -> bool:
        """Check if all four RT stamps are present and verified."""
        for lens in Lens:
            if lens not in self.stamps or not self.stamps[lens].verified:
                return False
        return True
    
    def z_point_satisfied(self) -> bool:
        """
        Check if Z-point condition is satisfied.
        
        RT□ + RT✿ + RT☁ + RT⟂ with commutator→BO_R rule.
        """
        return self.is_complete()

# ═══════════════════════════════════════════════════════════════════════════════
# POLE BRIDGE
# ═══════════════════════════════════════════════════════════════════════════════

@dataclass
class AetherPoleBridge:
    """
    Bridge between AETHER lattice and four-pole framework.
    """
    
    @staticmethod
    def lens_to_pole() -> Dict[Lens, str]:
        """Map lenses to poles."""
        return {
            Lens.EARTH: "D (Discrete) - exact/normal form",
            Lens.FIRE: "C (Continuous) - transform/domain",
            Lens.WATER: "Σ (Stochastic) - bounds/calibration",
            Lens.AIR: "Ψ (Hierarchical) - seeds/recursion"
        }
    
    @staticmethod
    def phase_to_breath() -> Dict[AetherPhase, str]:
        """Map phases to breath cycle."""
        return {
            AetherPhase.INHALE: "Zoom+ (expansion)",
            AetherPhase.METABOLIZE: "Process (transform)",
            AetherPhase.EXHALE: "Zoom- (compression)",
            AetherPhase.OXYGEN: "Store (templates)"
        }
    
    @staticmethod
    def integration() -> str:
        return """
        AETHER LATTICE ↔ FOUR-POLE FRAMEWORK
        
        L0 □ EARTH ↔ D-pole (Discrete/Exact)
        L1 ✿ FIRE  ↔ C-pole (Continuous/Transform)
        L2 ☁ WATER ↔ Σ-pole (Stochastic/Bounds)
        L3 ⟂ AIR   ↔ Ψ-pole (Hierarchical/Recursive)
        
        The 4×4×4 lattice provides 64 cells that map the
        complete space of mathematical operations across
        all four poles and all four phases of computation.
        """

# ═══════════════════════════════════════════════════════════════════════════════
# CONVENIENCE FUNCTIONS
# ═══════════════════════════════════════════════════════════════════════════════

def aether_lattice() -> AetherLattice:
    """Create complete AETHER lattice."""
    return AetherLattice()

def get_letter(letter: str) -> Optional[AetherLetter]:
    """Get AETHER letter definition."""
    return AETHER_ALPHABET.get(letter.upper())

def rt_stamp(lens: Lens, content: Any = None) -> RTStamp:
    """Create RT stamp."""
    if content is not None:
        return RTStamp.verify(lens, content)
    return RTStamp(lens)

def rt_registry() -> RTRegistry:
    """Create RT registry."""
    return RTRegistry()

# ═══════════════════════════════════════════════════════════════════════════════
# MODULE EXPORTS
# ═══════════════════════════════════════════════════════════════════════════════

__all__ = [
    # Enums
    'Lens',
    'AetherPhase',
    'AetherBundle',
    'Slot',
    
    # Cell
    'AetherCell',
    
    # Letter
    'AetherLetter',
    'AETHER_ALPHABET',
    
    # Lattice
    'AetherLattice',
    
    # RT Stamps
    'RTStamp',
    'RTRegistry',
    
    # Bridge
    'AetherPoleBridge',
    
    # Functions
    'aether_lattice',
    'get_letter',
    'rt_stamp',
    'rt_registry',
]
