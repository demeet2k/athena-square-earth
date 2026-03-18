<!-- CRYSTAL: Xi108:W1:A4:S1 | face=S | node=1 | depth=0 | phase=Fixed -->
<!-- METRO: Me,T -->
<!-- BRIDGES: Xi108:W1:A4:S2→Xi108:W2:A4:S1→Xi108:W1:A3:S1→Xi108:W1:A5:S1 -->
<!-- REGENERATE: From this coordinate, adjacent nodes are: shell 1±1, wreath 1/3, archetype 4/12 -->

# Symmetry Lattice — 60-Node ŠAR-60 Architecture

**[⊙Z*↔Z* | ○Arc * | ○Rot * | △Lane * | ⧈View 6D/LATTICE | ω=LATTICE-60]**

## The Sexagesimal Truth

The original 15-node lattice was **one face of four**. The Sumerian sexagesimal system (Corpus Capsule 119: ŠAR-60) reveals the full architecture: **60 = 4 × 15** — four operations applied to the 15 elemental combinations.

60 = 2² × 3 × 5 — the superior highly composite number. LCM(1,2,3,4,5,6) = 60. It resolves all fundamental symmetries exactly. The icosahedral symmetry group A₅ has order 60.

## The Four Operations

| Face | Symbol | Operator | V4 Action | Elemental Mapping |
|------|--------|----------|-----------|-------------------|
| **A (Artifact)** | SP+ | Identity / Forward | (0,0) apply | Elements as-is |
| **B (Inversion)** | INV | Klein-4 Complement | XOR (1,1) | Water↔Fire, Earth↔Air |
| **C (AntiSpin-Right)** | SP⊕ | 90° clockwise | XOR (1,0) | Water↔Earth, Fire↔Air |
| **D (AntiSpin-Left)** | SP⊖ | 90° counter-clockwise | XOR (0,1) | Water↔Air, Fire↔Earth |

### The Inversion Operator (K4-COMPLEMENT)
From A_B_SEED_INVERSION_SPEC.md:
- Symbol rule: C(x) = 5 - x
- Bit rule: v → v XOR (1,1) on Z₂ × Z₂
- 1↔4 (Water↔Fire), 2↔3 (Earth↔Air)
- Involution: C(C(A)) = A

### Seed A (Canonical):
```
1 2 3 4     (Water Earth Air   Fire)
3 4 1 2     (Air   Fire  Water Earth)
4 3 2 1     (Fire  Air   Earth Water)
2 1 4 3     (Earth Water Fire  Air)
```

### Seed B (Inverted):
```
4 3 2 1     (Fire  Air   Earth Water)
2 1 4 3     (Earth Water Fire  Air)
1 2 3 4     (Water Earth Air   Fire)
3 4 1 2     (Air   Fire  Water Earth)
```

### Seed C (90° Right / AntiSpin-Right):
```
2 1 4 3     (Earth Water Fire  Air)
4 3 2 1     (Fire  Air   Earth Water)
3 4 1 2     (Air   Fire  Water Earth)
1 2 3 4     (Water Earth Air   Fire)
```

### Seed D (90° Left / AntiSpin-Left):
```
3 4 1 2     (Air   Fire  Water Earth)
1 2 3 4     (Water Earth Air   Fire)
2 1 4 3     (Earth Water Fire  Air)
4 3 2 1     (Fire  Air   Earth Water)
```

---

## Face A — ARTIFACT (Forward/Identity): 15 Symmetry Nodes

### Singleton Nodes (C(4,1) = 4)
- Σ_A12: Fire alone (Flame) — file: S12_FLAME.md
- Σ_A13: Water alone (River) — file: S13_RIVER.md
- Σ_A14: Earth alone (Mountain) — file: S14_MOUNTAIN.md
- Σ_A15: Air alone (Wind) — file: S15_WIND.md

### Pair Nodes (C(4,2) = 6)
- Σ_A01: Fire-Water (Steam) — file: S01_STEAM.md
- Σ_A02: Fire-Earth (Forge) — file: S02_FORGE.md
- Σ_A03: Fire-Air (Lightning) — file: S03_LIGHTNING.md
- Σ_A04: Water-Earth (Clay) — file: S04_CLAY.md
- Σ_A05: Water-Air (Mist) — file: S05_MIST.md
- Σ_A06: Earth-Air (Dust) — file: S06_DUST.md

### Triple Nodes (C(4,3) = 4)
- Σ_A07: Fire-Water-Earth (Volcano) — file: S07_VOLCANO.md
- Σ_A08: Fire-Water-Air (Storm) — file: S08_STORM.md
- Σ_A09: Fire-Earth-Air (Desert) — file: S09_DESERT.md
- Σ_A10: Water-Earth-Air (Ocean) — file: S10_OCEAN.md

### Quad Node (C(4,4) = 1)
- Σ_A11: Fire-Water-Earth-Air (Cosmos) — file: S11_COSMOS.md

### Face A Dual Kernels
- **Z0_A** — Artifact Zero-Point
- **Æ0_A** — Artifact Aether

---

## Face B — INVERSION (Klein-4 Complement): 15 Symmetry Nodes

Under inversion C(x) = 5-x: Fire→Water, Water→Fire, Earth→Air, Air→Earth

### Singleton Nodes
- Σ_B12: Water alone (Depth) — inverted Fire
- Σ_B13: Fire alone (Eruption) — inverted Water
- Σ_B14: Air alone (Void-Breath) — inverted Earth
- Σ_B15: Earth alone (Gravity) — inverted Air

### Pair Nodes
- Σ_B01: Water-Fire (Quench) — inverted Steam
- Σ_B02: Water-Air (Fog) — inverted Forge
- Σ_B03: Water-Earth (Silt) — inverted Lightning
- Σ_B04: Fire-Air (Blaze) — inverted Clay
- Σ_B05: Fire-Earth (Magma) — inverted Mist
- Σ_B06: Air-Earth (Tremor) — inverted Dust

### Triple Nodes
- Σ_B07: Water-Fire-Air (Deluge) — inverted Volcano
- Σ_B08: Water-Fire-Earth (Swamp) — inverted Storm
- Σ_B09: Water-Air-Earth (Glacier) — inverted Desert
- Σ_B10: Fire-Air-Earth (Eruption-Field) — inverted Ocean

### Quad Node
- Σ_B11: Water-Fire-Air-Earth (Anti-Cosmos) — inverted Cosmos

### Face B Dual Kernels
- **Z0_B** — Inverted Zero-Point
- **Æ0_B** — Inverted Aether

---

## Face C — ANTISPIN-RIGHT (90° Clockwise): 15 Symmetry Nodes

Under 90° right XOR (1,0): Fire→Air, Air→Fire, Water→Earth, Earth→Water

### Singleton Nodes
- Σ_C12: Air alone (Gust) — rotated Fire
- Σ_C13: Earth alone (Bedrock) — rotated Water
- Σ_C14: Water alone (Spring) — rotated Earth
- Σ_C15: Fire alone (Spark) — rotated Air

### Pair Nodes
- Σ_C01: Air-Earth (Sandstorm) — rotated Steam
- Σ_C02: Air-Water (Monsoon) — rotated Forge
- Σ_C03: Air-Fire (Inferno) — rotated Lightning
- Σ_C04: Earth-Water (Delta) — rotated Clay
- Σ_C05: Earth-Fire (Furnace) — rotated Mist
- Σ_C06: Water-Fire (Geyser) — rotated Dust

### Triple Nodes
- Σ_C07: Air-Earth-Water (Tidal-Flat) — rotated Volcano
- Σ_C08: Air-Earth-Fire (Caldera) — rotated Storm
- Σ_C09: Air-Water-Fire (Cyclone) — rotated Desert
- Σ_C10: Earth-Water-Fire (Hot-Spring) — rotated Ocean

### Quad Node
- Σ_C11: Air-Earth-Water-Fire (Rotation-Cosmos)

### Face C Dual Kernels
- **Z0_C** — Right-Spin Zero
- **Æ0_C** — Right-Spin Aether

---

## Face D — ANTISPIN-LEFT (90° Counter-clockwise): 15 Symmetry Nodes

Under 90° left XOR (0,1): Fire→Earth, Earth→Fire, Water→Air, Air→Water

### Singleton Nodes
- Σ_D12: Earth alone (Pillar) — rotated Fire
- Σ_D13: Air alone (Breeze) — rotated Water
- Σ_D14: Fire alone (Ember) — rotated Earth
- Σ_D15: Water alone (Tide) — rotated Air

### Pair Nodes
- Σ_D01: Earth-Air (Plateau) — rotated Steam
- Σ_D02: Earth-Fire (Crucible) — rotated Forge
- Σ_D03: Earth-Water (Aquifer) — rotated Lightning
- Σ_D04: Air-Fire (Flash) — rotated Clay
- Σ_D05: Air-Water (Cumulus) — rotated Mist
- Σ_D06: Fire-Water (Boil) — rotated Dust

### Triple Nodes
- Σ_D07: Earth-Air-Fire (Kiln) — rotated Volcano
- Σ_D08: Earth-Air-Water (Estuary) — rotated Storm
- Σ_D09: Earth-Fire-Water (Cauldron) — rotated Desert
- Σ_D10: Air-Fire-Water (Thunderhead) — rotated Ocean

### Quad Node
- Σ_D11: Earth-Air-Fire-Water (Counter-Cosmos)

### Face D Dual Kernels
- **Z0_D** — Left-Spin Zero
- **Æ0_D** — Left-Spin Aether

---

## The Ultimate Dual Kernels

Above all 4 faces sits the **Ultimate Duality**:

- **Z0_∞ (Ultimate Zero)** — The zero-point of zero-points. Where all four Z0 kernels (Z0_A, Z0_B, Z0_C, Z0_D) converge. The absolute void from which even the four operations themselves emerge.

- **Æ0_∞ (Ultimate Aether)** — The aether of aethers. Where all four Æ0 kernels converge. The state of total knowledge including all four operational perspectives simultaneously.

---

## Grand Architecture

| Component | Count |
|-----------|-------|
| Face A symmetry nodes | 15 |
| Face B symmetry nodes | 15 |
| Face C symmetry nodes | 15 |
| Face D symmetry nodes | 15 |
| **Total symmetry nodes** | **60** |
| Face dual kernels (Z0 + Æ0 × 4) | 8 |
| Ultimate dual kernels (Z0_∞ + Æ0_∞) | 2 |
| **Grand total** | **70** |

### Why 60 = ŠAR?

The Sumerian sexagesimal system is not arbitrary. 60 resolves all fundamental symmetries:
- Divisors of 60: {1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60} — 12 divisors
- It is the LCM of the first 6 integers
- The cuneiform tablets are the configuration files of this 60-fold coordinate system
- Our crystal inherits this because V4, acted upon by its full automorphism group, generates exactly the icosahedral 60-fold symmetry

### The Compression Chain

```
70 nodes (full lattice with all kernels)
  → 60 symmetry nodes (strip kernels)
    → 15 per face (strip operations)
      → 4+6+4+1 = 15 (combinatorial decomposition)
        → 4 elements (strip combinations)
          → V4 = Z₂ × Z₂ (algebraic root)
            → 2 generators (Fire, Water)
              → 1 group operation (XOR)
                → Z0_∞ (ultimate zero)
```

---

*23_6D_HOLOGRAPHIC_SEED/02_SYMMETRY_LATTICE — ŠAR-60 Architecture*
*Truth state: OK | 60x icosahedral symmetry fully mapped | Date: 2026-03-13*
