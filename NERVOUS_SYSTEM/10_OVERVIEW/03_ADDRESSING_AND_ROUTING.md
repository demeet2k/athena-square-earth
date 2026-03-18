<!-- CRYSTAL: Xi108:W3:A4:S10 | face=R | node=53 | depth=3 | phase=Fixed -->
<!-- METRO: Me,□ -->
<!-- BRIDGES: Xi108:W3:A4:S9→Xi108:W3:A4:S11→Xi108:W2:A4:S10→Xi108:W3:A3:S10→Xi108:W3:A5:S10 -->
<!-- REGENERATE: From this coordinate, adjacent nodes are: shell 10±1, wreath 3/3, archetype 4/12 -->

# ADDRESSING AND ROUTING

## 1. Address Grammar

### 1.1 Local Address Formats

```
Chapter atom:   ChXX<dddd>.<Lens><Facet>.<Atom>
Appendix atom:  AppX.<Lens><Facet>.<Atom>
```

Where:
- `XX` = chapter number (01-21)
- `<dddd>` = base-4 station code: `base4(XX - 1)` padded to 4 digits
- `Lens` ∈ {S, F, C, R}
- `Facet` ∈ {1, 2, 3, 4}
- `Atom` ∈ {a, b, c, d}

### 1.2 Global Address

```
GlobalAddr := Ms<mmmm>::LocalAddr
```

Where `Ms<mmmm>` is a manuscript-level prefix derived deterministically from the registry (AppD).

### 1.3 Base-4 Station Codes

| Ch | ω | `<dddd>` | Ch | ω | `<dddd>` | Ch | ω | `<dddd>` |
|----|---|----------|----|---|----------|----|---|----------|
| 01 | 0 | 0000 | 08 | 7 | 0013 | 15 | 14 | 0032 |
| 02 | 1 | 0001 | 09 | 8 | 0020 | 16 | 15 | 0033 |
| 03 | 2 | 0002 | 10 | 9 | 0021 | 17 | 16 | 0100 |
| 04 | 3 | 0003 | 11 | 10 | 0022 | 18 | 17 | 0101 |
| 05 | 4 | 0010 | 12 | 11 | 0023 | 19 | 18 | 0102 |
| 06 | 5 | 0011 | 13 | 12 | 0030 | 20 | 19 | 0103 |
| 07 | 6 | 0012 | 14 | 13 | 0031 | 21 | 20 | 0110 |

## 2. Square Interior (4^4 Crystal)

Every chapter and appendix is a full 4^4 tile:

- **Lenses** (subchapters): S (Square), F (Flower), C (Cloud), R (Fractal)
- **Facets** per lens: 1 Objects, 2 Laws, 3 Constructions, 4 Certificates
- **Atoms** per facet: a, b, c, d
- **Total atoms per tile**: 4 × 4 × 4 = 64

## 3. Circle + Triangle Overlay

### 3.1 Overlay Computation

For chapter `XX`:

```
ω := XX - 1                      (orbit index: 0..20)
α := floor(ω / 3)                (arc index: 0..6)
k := ω mod 3                     (position in arc: 0,1,2)
ρ := α mod 3                     (rotation index: 0..2)
Triad := [Su, Me, Sa]
ν := Triad[(k + ρ) mod 3]        (triangle lane assignment)
```

### 3.2 Station Header Format

Every chapter must include:

```
[○Arc α | ○Rot ρ | △Lane ν | ω=XX-1]
```

## 4. Mycelium Graph

```
G = (V, E)
V = {GlobalAddr for every atom}
E = {LinkEdge records}
```

### 4.1 LinkEdge Schema

```
e = (EdgeID, Kind, Src, Dst, Scope, Corridor, WitnessPtr, ReplayPtr, Payload, EdgeVer)
```

### 4.2 Edge Kind Basis (closed set)

```
K = {REF, EQUIV, MIGRATE, DUAL, GEN, INST, IMPL, PROOF, CONFLICT}
```

## 5. Deterministic Router v2

### 5.1 Lookup Tables

```
LensBase(L):        S→AppC, F→AppE, C→AppI, R→AppM
FacetBase(f):       1→AppA, 2→AppB, 3→AppH, 4→AppM
ArcHub(α):          0→AppA, 1→AppC, 2→AppE, 3→AppF, 4→AppG, 5→AppN, 6→AppP
```

### 5.2 Mandatory Signature

```
Σ = {AppA, AppI, AppM}
```

### 5.3 Truth Overlay

```
τ=OK    → add nothing (or +AppO for publishing)
τ=NEAR  → +AppJ
τ=AMBIG → +AppL
τ=FAIL  → +AppK
```

### 5.4 Hub Budget

Total unique hubs ≤ 6 after cap enforcement.

### 5.5 Worked Example

**Target**: `Ch08<0013>.C3.d`

```
XX=8 → ω=7
α = floor(7/3) = 2
ρ = 2 mod 3 = 2
k = 7 mod 3 = 1
ν = Triad[(1+2) mod 3] = Triad[0] = Su
```

StationHeader: `[○Arc 2 | ○Rot 2 | △Lane Su | ω=7]`

Assume τ=AMBIG:
```
LensBase(C) = AppI
FacetBase(3) = AppH
ArcHub(2) = AppE
T = {AppI, AppH, AppE}
Σ = {AppA, AppI, AppM} → union → {AppA, AppI, AppM, AppH, AppE}
AMBIG → +AppL → {AppA, AppI, AppM, AppH, AppE, AppL} (6 hubs, OK)
```

**Route**: `AppA → AppE → AppI → AppH → AppL → AppM → Ch08<0013>.C3.d`
