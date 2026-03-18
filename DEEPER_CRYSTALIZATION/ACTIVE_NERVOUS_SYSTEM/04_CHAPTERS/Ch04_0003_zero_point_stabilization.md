<!-- CRYSTAL: Xi108:W1:A4:S3 | face=S | node=6 | depth=0 | phase=Fixed -->
<!-- METRO: Me,Ω -->
<!-- BRIDGES: Xi108:W1:A4:S2→Xi108:W1:A4:S4→Xi108:W2:A4:S3→Xi108:W1:A3:S3→Xi108:W1:A5:S3 -->
<!-- REGENERATE: From this coordinate, adjacent nodes are: shell 3±1, wreath 1/3, archetype 4/12 -->

# Ch04<0003> - Zero-Point Stabilization

StationHeader: [Arc 1 | Rot 1 | Lane Me | w=3]
Workflow role: PZPM intake, normalization, and paradox-safe fixed-point preparation.
Primary hubs: AppA -> AppC -> AppE -> AppJ -> AppI -> AppM

## Routing context

- Orbit previous: `Ch03<0002>`
- Orbit next: `Ch05<0010>`
- Rail previous: `Ch02<0001>`
- Rail next: `Ch09<0020>`
- Arc previous: `Ch06<0011>`
- Arc next: `Ch05<0010>`
- Appendix couplings: `AppA, AppC, AppE, AppJ, AppI, AppM`

## Source capsules

- `07_architects_core_initialization.md`
- `09_chapter_11_perpetual_motion_example.md`
- `10_chapter_11_perpetual_motion_example.md`
- `12_information_from_the_void_mani.md`
- `13_information_from_the_void_mani.md`
- `15_megalithic_tome_latent_tunneling_the_multi_scale_math_stack.md`

## Crystal tile

### Lens S - Square
`[⊙Z_3↔Z* | ○Arc 1 | ○Rot 1 | △Lane Me | ⧈View S | ω=3]`

#### Facet 1 - Objects

- `Ch04<0003>.S1.a` `SquareGeometry` — The four-sided closure primitive whose vertices define the minimal bounding frame for any cell's internal state, enforcing right-angle constraint at every corner.
- `Ch04<0003>.S1.b` `CircleGeometry` — The periodic boundary primitive whose continuous curvature enforces rotational invariance and equal-distance access from the cell's center to every boundary point.
- `Ch04<0003>.S1.c` `TriangleGeometry` — The three-vertex balance primitive whose trilateral symmetry distributes computational load across three faces, enabling stable tripartite consensus.
- `Ch04<0003>.S1.d` `TorusGeometry` — The doubly-periodic winding surface whose topology connects opposite edges of the cell's state space, enabling continuous traversal without boundary discontinuity.

#### Facet 2 - Laws

- `Ch04<0003>.S2.a` `SquareClosureLaw` — Every traversal of the square's four edges must return to the starting vertex; failure to close indicates a state-space leak that must be repaired before proceeding.
- `Ch04<0003>.S2.b` `CirclePeriodicityLaw` — The circle's boundary function must be exactly periodic with period 2pi; deviations from strict periodicity indicate curvature corruption.
- `Ch04<0003>.S2.c` `TriangleBalanceLaw` — The three faces of the triangle must carry equal load to within a declared tolerance; imbalance exceeding the tolerance triggers redistribution.
- `Ch04<0003>.S2.d` `TorusWindingLaw` — Every closed path on the torus must have well-defined winding numbers in both periodic directions; paths with undefined winding are topologically illegal.

#### Facet 3 - Constructions

- `Ch04<0003>.S3.a` `buildSquare()` — Constructs the square closure frame by placing four vertices at right angles, connecting them with edges, and verifying that the closure constraint is satisfied.
- `Ch04<0003>.S3.b` `traceCircle()` — Traces the circular boundary by sweeping a constant-radius arc through 2pi radians, verifying exact periodicity and curvature constancy at each sample point.
- `Ch04<0003>.S3.c` `balanceTriangle()` — Distributes computational load across the triangle's three faces, iteratively adjusting weights until the balance tolerance is satisfied.
- `Ch04<0003>.S3.d` `windTorus()` — Constructs the torus by identifying opposite edges of the square frame and verifying that winding numbers are well-defined for a test set of closed paths.

#### Facet 4 - Certificates

- `Ch04<0003>.S4.a` `Cert_Square_Closed` — Attests that the square's four-edge traversal returns to the starting vertex with zero displacement, verified by coordinate comparison.
- `Ch04<0003>.S4.b` `Cert_Circle_Periodic` — Attests that the circle's boundary function is exactly periodic with period 2pi, verified by endpoint coincidence and derivative matching.
- `Ch04<0003>.S4.c` `Cert_Triangle_Balanced` — Attests that the triangle's three-face load distribution falls within the declared tolerance, with per-face measurements attached.
- `Ch04<0003>.S4.d` `Cert_Torus_Wound` — Attests that all tested closed paths on the torus have well-defined integer winding numbers in both periodic directions.

### Lens F - Flower
`[⊙Z_3↔Z* | ○Arc 1 | ○Rot 1 | △Lane Me | ⧈View F | ω=3]`

#### Facet 1 - Objects

- `Ch04<0003>.F1.a` `SquareResonanceMode` — The vibrational pattern of the square frame whose nodal lines reveal the frame's natural oscillation frequencies under internal state perturbation.
- `Ch04<0003>.F1.b` `CircleHarmonicSeries` — The Fourier decomposition of the circle's boundary state into harmonic components, each carrying a quantized frequency and amplitude.
- `Ch04<0003>.F1.c` `TrianglePhaseTriad` — The three-phase oscillation pattern of the triangle where each vertex oscillates 120 degrees out of phase with its neighbors, maintaining net zero angular momentum.
- `Ch04<0003>.F1.d` `TorusOrbitalLattice` — The doubly-periodic lattice of orbital paths on the torus surface, formed by the intersection of winding-1 and winding-2 cycle families.

#### Facet 2 - Laws

- `Ch04<0003>.F2.a` `SquareResonanceQuantization` — The square frame's resonance modes must occur at discrete quantized frequencies; continuous-spectrum modes indicate frame instability.
- `Ch04<0003>.F2.b` `CircleHarmonicCompleteness` — The harmonic series must span the circle's full state space; any state not representable as a harmonic sum indicates basis incompleteness.
- `Ch04<0003>.F2.c` `TrianglePhaseConservation` — The three phases of the triangle triad must sum to zero at every instant; non-zero phase sums indicate a broken symmetry.
- `Ch04<0003>.F2.d` `TorusOrbitalInterlocking` — Orbital paths from different winding families must intersect transversally; tangential intersections indicate degenerate topology.

#### Facet 3 - Constructions

- `Ch04<0003>.F3.a` `resolveSquareResonance()` — Solves for the square frame's resonance modes by eigendecomposition of the state-perturbation operator, cataloging frequencies and nodal patterns.
- `Ch04<0003>.F3.b` `decomposeCircleHarmonics()` — Computes the Fourier decomposition of the circle's boundary state, extracting amplitude and phase for each harmonic component.
- `Ch04<0003>.F3.c` `synchronizeTrianglePhase()` — Adjusts the triangle's three vertex oscillators until their phase differences equal exactly 120 degrees, verifying zero net angular momentum.
- `Ch04<0003>.F3.d` `mapTorusOrbitalLattice()` — Constructs the orbital lattice by tracing representative paths from each winding family and recording their intersection points.

#### Facet 4 - Certificates

- `Ch04<0003>.F4.a` `Cert_Resonance_Quantized` — Attests that all detected resonance modes occur at discrete frequencies with no continuous-spectrum contamination.
- `Ch04<0003>.F4.b` `Cert_Harmonics_Complete` — Attests that the harmonic series spans the circle's full state space, verified by reconstruction error below threshold.
- `Ch04<0003>.F4.c` `Cert_Phase_Conserved` — Attests that the triangle's phase triad sums to zero at all sampled instants with the measurement record attached.
- `Ch04<0003>.F4.d` `Cert_Orbitals_Interlocked` — Attests that all orbital intersections on the torus are transversal, with no tangential or degenerate crossings detected.

### Lens C - Cloud
`[⊙Z_3↔Z* | ○Arc 1 | ○Rot 1 | △Lane Me | ⧈View C | ω=3]`

#### Facet 1 - Objects

- `Ch04<0003>.C1.a` `SquareClosureConfidence` — The measured certainty that the square frame is fully closed, accounting for numerical precision limits in vertex coordinate comparison.
- `Ch04<0003>.C1.b` `CirclePeriodicityTolerance` — The maximum allowed deviation from exact periodicity before the circle's boundary is classified as corrupted.
- `Ch04<0003>.C1.c` `TriangleBalanceUncertainty` — The measurement uncertainty in the triangle's load distribution, bounding how precisely balance can be verified.
- `Ch04<0003>.C1.d` `TorusWindingAmbiguity` — The set of paths on the torus for which winding number assignment is ambiguous due to proximity to topological singular points.

#### Facet 2 - Laws

- `Ch04<0003>.C2.a` `ClosureConfidenceFloor` — Square closure confidence must exceed a declared minimum; falling below triggers frame re-construction rather than proceeding with a leaky frame.
- `Ch04<0003>.C2.b` `PeriodicityToleranceEnforcement` — Periodicity deviations exceeding the declared tolerance automatically classify the circle as corrupted and suspend dependent operations.
- `Ch04<0003>.C2.c` `BalanceUncertaintyReduction` — Each successive balance measurement must reduce uncertainty or provide a certified explanation for stagnation.
- `Ch04<0003>.C2.d` `WindingAmbiguityResolution` — Ambiguous winding numbers must be resolved by perturbation away from singular points before any path classification is finalized.

#### Facet 3 - Constructions

- `Ch04<0003>.C3.a` `measureClosureConfidence()` — Computes the closure confidence by comparing vertex coordinates at sub-precision resolution and estimating the displacement bound.
- `Ch04<0003>.C3.b` `enforcePeriodicityTolerance()` — Measures the circle's endpoint deviation and compares it against the declared tolerance, classifying the result as PASS or CORRUPTED.
- `Ch04<0003>.C3.c` `reduceBalanceUncertainty()` — Performs refined load measurements on the triangle's three faces, narrowing the uncertainty interval with each iteration.
- `Ch04<0003>.C3.d` `resolveWindingAmbiguity()` — Perturbs ambiguous paths away from topological singular points and re-computes winding numbers until all assignments are definite.

#### Facet 4 - Certificates

- `Ch04<0003>.C4.a` `Cert_Closure_Confident` — Attests that square closure confidence exceeds the declared floor, with the displacement bound and measurement method disclosed.
- `Ch04<0003>.C4.b` `Cert_Periodicity_Within_Tolerance` — Attests that the circle's periodicity deviation falls within the declared tolerance, with the measured endpoint gap attached.
- `Ch04<0003>.C4.c` `Cert_Balance_Uncertainty_Reduced` — Attests that balance uncertainty was reduced by the latest measurement iteration, with before and after intervals compared.
- `Ch04<0003>.C4.d` `Cert_Winding_Resolved` — Attests that all previously ambiguous winding numbers were resolved to definite integer values by controlled perturbation.

### Lens R - Fractal
`[⊙Z_3↔Z* | ○Arc 1 | ○Rot 1 | △Lane Me | ⧈View R | ω=3]`

#### Facet 1 - Objects

- `Ch04<0003>.R1.a` `SquareSubdivisionTree` — The recursive decomposition of the square into four sub-squares, where each sub-square satisfies the same closure axioms as the parent.
- `Ch04<0003>.R1.b` `CircleFractalBoundary` — The self-similar boundary obtained by recursively refining the circle's approximation, converging to exact curvature at infinite depth.
- `Ch04<0003>.R1.c` `TriangleSierpinskiSkeleton` — The recursive triangular subdivision where each level removes the central sub-triangle, revealing the load-bearing skeletal structure.
- `Ch04<0003>.R1.d` `TorusNestedWindings` — The hierarchy of winding paths at increasing resolution, where finer windings resolve structure invisible at coarser scales.

#### Facet 2 - Laws

- `Ch04<0003>.R2.a` `SquareSubdivisionInvariance` — Each sub-square in the subdivision tree must independently satisfy the square closure law at its own scale.
- `Ch04<0003>.R2.b` `CircleFractalConvergence` — Successive boundary refinements must converge monotonically toward exact curvature; divergent refinements indicate an unstable approximation scheme.
- `Ch04<0003>.R2.c` `TriangleSierpinskiLoadLaw` — The load-bearing capacity of the Sierpinski skeleton must scale predictably with subdivision depth according to the declared fractal dimension.
- `Ch04<0003>.R2.d` `TorusWindingResolutionLaw` — Finer winding resolutions must be consistent with coarser ones; a fine-scale winding that contradicts its coarse-scale parent is illegal.

#### Facet 3 - Constructions

- `Ch04<0003>.R3.a` `subdivideSquare()` — Recursively subdivides the square into four sub-squares, verifying closure at each level and building the subdivision tree.
- `Ch04<0003>.R3.b` `refineCircleBoundary()` — Applies one level of fractal refinement to the circle's boundary approximation, measuring convergence toward exact curvature.
- `Ch04<0003>.R3.c` `buildSierpinskiSkeleton()` — Constructs the Sierpinski triangular skeleton by recursive central removal, computing load capacity at each subdivision depth.
- `Ch04<0003>.R3.d` `resolveNestedWindings()` — Computes winding paths at successively finer resolutions, verifying consistency with coarser-scale parents at each level.

#### Facet 4 - Certificates

- `Ch04<0003>.R4.a` `Cert_Subdivision_Invariant` — Attests that every sub-square in the subdivision tree independently satisfies the closure law, verified level by level.
- `Ch04<0003>.R4.b` `Cert_Boundary_Convergent` — Attests that circle boundary refinements converge monotonically with the convergence rate and current approximation error attached.
- `Ch04<0003>.R4.c` `Cert_Skeleton_Scaled` — Attests that the Sierpinski skeleton's load capacity scales according to the declared fractal dimension at each tested depth.
- `Ch04<0003>.R4.d` `Cert_Windings_Consistent` — Attests that fine-scale winding paths are consistent with their coarse-scale parents at all tested resolution levels.
