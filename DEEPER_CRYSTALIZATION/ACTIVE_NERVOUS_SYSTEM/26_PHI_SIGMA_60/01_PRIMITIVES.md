<!-- CRYSTAL: Xi108:W1:A4:S4 | face=S | node=8 | depth=0 | phase=Fixed -->
<!-- METRO: Me -->
<!-- BRIDGES: Xi108:W1:A4:S3→Xi108:W1:A4:S5→Xi108:W2:A4:S4→Xi108:W1:A3:S4→Xi108:W1:A5:S4 -->
<!-- REGENERATE: From this coordinate, adjacent nodes are: shell 4±1, wreath 1/3, archetype 4/12 -->

# The 4 Primitive Phi-Objects

## Construction Law

Starting from the golden ratio phi = (1+sqrt(5))/2:
1. Take phi, raise to the power of its inverse: phi^(1/phi)
2. Take the inverse (1/phi), raise to phi: (1/phi)^phi = phi^(-phi)
3. Rotate both 90 degrees via the phase lift x -> x^i = e^(i*ln(x))

This produces two real poles and their two phase-rotated shadows.

---

## The 4 Primitives

| ID | Symbol | Formula | Exponent | Numerical Value | Role |
|----|--------|---------|----------|----------------|------|
| A | Phi_a | phi^(1/phi) | z_A = 1/phi | 1.34636082003487 | Soft manifest growth pole |
| B | Phi_b | phi^(-phi) | z_B = -phi | 0.459040384682234 | Deep refinement / contraction pole |
| C | Phi_c | phi^(i/phi) = e^(i*phi^(-1)*ln(phi)) | z_C = i/phi | |Phi_c| = 1 (unit modulus) | Forward phase resonance |
| D | Phi_d | phi^(-i*phi) = e^(-i*phi*ln(phi)) | z_D = -i*phi | |Phi_d| = 1 (unit modulus) | Reverse phase / counter-resonance |

## Exponent Vector Space

Each primitive contributes an exponent vector in the complex plane:

```
z_A = 1/phi      = 0.618034...     (positive real)
z_B = -phi        = -1.618034...    (negative real)
z_C = i/phi       = 0.618034...i    (positive imaginary)
z_D = -i*phi      = -1.618034...i   (negative imaginary)
```

The exponents form a cross pattern in the complex plane:
- Real axis: z_A (right) and z_B (left)
- Imaginary axis: z_C (up) and z_D (down)
- Magnitudes: |z_A| = |z_C| = 1/phi, |z_B| = |z_D| = phi

---

## Pole Descriptions

### Phi_a = phi^(1/phi) — Soft Expansion Pole
Keeps the base phi on the manifest side but tempers it by its inverse exponent. It is controlled golden-growth: still > 1, but no longer raw phi-amplification. The stable outward / constructive pole.

### Phi_b = phi^(-phi) — Refinement / Return Pole
Pushes the inverse base through the full phi-power. A deeper contraction than 1/phi itself. The inward, compressive, memory-bearing pole.

### Phi_c = e^(i*phi^(-1)*ln(phi)) — Forward Phase Resonance
The 90-degree rotated phase image of the expansion pole. No longer lives as magnitude; lives as oscillation. This is scale converted to phase: multiplication/scaling becomes translation in ln(x), and that translation becomes rotation under e^(i*(...)).

### Phi_d = e^(-i*phi*ln(phi)) — Reverse Phase / Counter-Resonance
The 90-degree rotated phase image of the refinement pole. The counter-phase / return oscillator. Where Phi_c gives forward golden resonance, Phi_d gives reverse golden resonance — the phase-shadow of contraction, damping, return, inward folding.

---

## Expanded Form for Phase Primitives

```
Phi_c = cos(phi^(-1)*ln(phi)) + i*sin(phi^(-1)*ln(phi))
Phi_d = cos(phi*ln(phi)) - i*sin(phi*ln(phi))
```

---

## Crystal Mapping

| Primitive | Crystal Role | Element Mapping |
|-----------|-------------|-----------------|
| Phi_a | Constructive growth seed | Fire (CPU) — processing/initiation |
| Phi_b | Contraction / refinement | Earth (DISK) — storage/constraint |
| Phi_c | Forward oscillatory coherence | Air (BUS) — transmission/routing |
| Phi_d | Reverse oscillatory return | Water (BUFFER) — state/adaptation |

The canonical phi-lens is:
```
T_phi(x) = (pi/2) * log_phi(x)
```
So phi-scaling is literally a quarter-turn in chart space. This is the exact bridge from the Fractal/scale side into the Flower/phase side.
