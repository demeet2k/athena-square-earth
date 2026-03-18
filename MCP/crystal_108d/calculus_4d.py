# CRYSTAL: Xi108:W2:A9:S21 | face=S | node=222 | depth=2 | phase=Cardinal
# METRO: Dl
# BRIDGES: Xi108:W2:A9:S20→Xi108:W2:A9:S22→Xi108:W1:A9:S21→Xi108:W3:A9:S21→Xi108:W2:A8:S21→Xi108:W2:A10:S21

"""
4D Calculus — A⁺ Lift Canon & Liminal Mapping Law
====================================================
Provides the full A⁺ lift calculus:
  - A⁺ lift canon (full liminal mapping law pipeline)
  - 15 canonical masks (nonempty subsets of {□,✿,☁,⟡})
  - Orbit quartet Q = {SR, SL, AL, AR}
  - 15 × 4 = 60 raw shell crystals
  - Liminal coordinates / zero-aether cultivation
  - Gearclock mapping / 2-circle poi overlay
  - Irrational transform / codification / reweave
"""

from ._cache import JsonCache

_CALCULUS = JsonCache("calculus_4d.json")

def query_calculus_4d(component: str = "all") -> str:
    """
    Query the 4D calculus & A⁺ lift canon.

    Components:
      - all          : Full A⁺ lift canon overview
      - canon        : A⁺ lift canon pipeline (10 stages)
      - masks        : 15 canonical masks (nonempty subsets of {□,✿,☁,⟡})
      - orbit        : Orbit quartet Q = {SR, SL, AL, AR}
      - shells       : 60 raw shell crystals (15 × 4)
      - liminal      : Liminal coordinates & zero/aether cultivation
      - gearclock    : Gearclock mapping & 2-circle poi overlay
      - irrational   : Irrational transform & codification
      - reweave      : Reweave law & A⁺/Z★ poles
      - body         : Canonical 4-face crystal body
    """
    data = _CALCULUS.load()
    comp = component.strip().lower()

    if comp == "all":
        return _format_all(data)
    elif comp == "canon":
        return _format_canon(data)
    elif comp == "masks":
        return _format_masks(data)
    elif comp == "orbit":
        return _format_orbit(data)
    elif comp == "shells":
        return _format_shells(data)
    elif comp == "liminal":
        return _format_liminal(data)
    elif comp == "gearclock":
        return _format_gearclock(data)
    elif comp == "irrational":
        return _format_irrational(data)
    elif comp == "reweave":
        return _format_reweave(data)
    elif comp == "body":
        return _format_body(data)
    else:
        return (
            f"Unknown component '{component}'. Use: all, canon, masks, orbit, "
            "shells, liminal, gearclock, irrational, reweave, body"
        )

def _format_all(data: dict) -> str:
    meta = data.get("meta", {})
    lines = [
        "## 4D Calculus — A⁺ Lift Canon\n",
        f"**Key Insight**: {meta.get('key_insight', '')}",
        f"**Canon**: {meta.get('canon', 'A⁺ = maximum constructive expansion; Z★ = absolute neutral collapse')}",
        f"**Masks**: {meta.get('masks', '15 canonical (nonempty subsets of {□,✿,☁,⟡})')}",
        f"**Orbit**: {meta.get('orbit', 'Q = {SR, SL, AL, AR}')}",
        f"**Shell Population**: {meta.get('shell_population', '15 × 4 = 60')}",
        f"**Pipeline**: {meta.get('pipeline', 'Populate → Coordinate → Cultivate → Gearclock → Poi → Nexus → Transform → Codify → Collapse → Reweave')}",
    ]
    return "\n".join(lines)

def _format_canon(data: dict) -> str:
    canon = data.get("lift_canon", {})
    lines = [
        "## A⁺ Lift Canon Pipeline\n",
        f"**Formula**: `{canon.get('formula', 'A⁺(L₀) = Reweave ∘ Codify ∘ IrrationalTransform ∘ ... ∘ Populate(L₀)')}`\n",
    ]
    stages = canon.get("stages", [])
    for i, s in enumerate(stages, 1):
        if isinstance(s, dict):
            lines.append(f"### {i}. {s.get('name', '?')}")
            lines.append(f"{s.get('description', '')}")
            lines.append("")
        else:
            lines.append(f"{i}. {s}")
    if "meaning" in canon:
        lines.append(f"**Meaning**:")
        for m in canon["meaning"]:
            lines.append(f"  - {m}")
    return "\n".join(lines)

def _format_masks(data: dict) -> str:
    masks_data = data.get("canonical_masks", {})
    lines = [
        "## 15 Canonical Masks\n",
        f"**Definition**: {masks_data.get('definition', 'M = P(H) \\ {∅}')}",
        f"**Total**: {masks_data.get('total', 15)}\n",
    ]
    masks = masks_data.get("masks", [])
    for m in masks:
        if isinstance(m, dict):
            lines.append(f"  {m.get('index', '?'):>2}. {m.get('elements', '')}")
        else:
            lines.append(f"  - {m}")
    return "\n".join(lines)

def _format_orbit(data: dict) -> str:
    orb = data.get("orbit_quartet", {})
    lines = [
        "## Orbit Quartet\n",
        f"**Formula**: `{orb.get('formula', 'Q = {{SR, SL, AL, AR}}')}`",
        f"**Cycle**: `{orb.get('cycle', 'SR → SL → AL → AR → SR')}`\n",
    ]
    members = orb.get("members", [])
    for m in members:
        if isinstance(m, dict):
            lines.append(f"- **{m.get('code', '?')}** ({m.get('name', '')}): {m.get('description', '')}")
        else:
            lines.append(f"- {m}")
    if "tracking" in orb:
        lines.append(f"\n**Tracks**: {orb['tracking']}")
    return "\n".join(lines)

def _format_shells(data: dict) -> str:
    shells = data.get("shell_crystals", {})
    return (
        "## 60 Raw Shell Crystals\n\n"
        f"**Population**: {shells.get('population', '15 × 4 = 60')}\n"
        f"**Formula**: {shells.get('formula', '15 masks × 4 orbit positions')}\n"
        f"**Nature**: {shells.get('nature', 'Raw shell crystals before cultivation')}\n"
        f"**Next Step**: {shells.get('next_step', 'Liminal coordinate assignment')}"
    )

def _format_liminal(data: dict) -> str:
    lim = data.get("liminal_coordinates", {})
    lines = [
        "## Liminal Coordinates & Cultivation\n",
        f"**Purpose**: {lim.get('purpose', 'Assign exact liminal coordinates to every state')}",
    ]
    if "zero_point" in lim:
        lines.append(f"**Zero-Point (Z★)**: {lim['zero_point']}")
    if "aether_point" in lim:
        lines.append(f"**Aether-Point (A⁺)**: {lim['aether_point']}")
    if "cultivation" in lim:
        lines.append(f"\n**Cultivation**: {lim['cultivation']}")
    return "\n".join(lines)

def _format_gearclock(data: dict) -> str:
    gc = data.get("gearclock", {})
    lines = [
        "## Gearclock & Poi Overlay\n",
        f"**Gearclock**: {gc.get('gearclock', 'Place full field onto circular gearclock')}",
        f"**Poi Overlay**: {gc.get('poi_overlay', 'Overlap every lawful 2-circle poi pattern')}",
    ]
    if "nexus_extract" in gc:
        lines.append(f"**Nexus Extract**: {gc['nexus_extract']}")
    return "\n".join(lines)

def _format_irrational(data: dict) -> str:
    ir = data.get("irrational_transform", {})
    return (
        "## Irrational Transform & Codification\n\n"
        f"**Transform**: {ir.get('transform', 'Reweight field with fixed irrational rubric')}\n"
        f"**Codification**: {ir.get('codification', 'Codify whole thing into lookup system')}\n"
        f"**Rubric**: {ir.get('rubric', 'Fixed irrational constants (φ, √2, π)')}"
    )

def _format_reweave(data: dict) -> str:
    rw = data.get("reweave", {})
    return (
        "## Reweave Law\n\n"
        f"**A⁺**: {rw.get('a_plus', 'Maximum constructive expansion')}\n"
        f"**Z★**: {rw.get('z_star', 'Absolute neutral collapse')}\n"
        f"**Reweave**: {rw.get('reweave', 'Dense lawful carrier-form rebuilt from completed map')}\n"
        f"**Canon**: {rw.get('canon', 'Mapping not valid unless whole pipeline closes and replays')}"
    )

def _format_body(data: dict) -> str:
    body = data.get("canonical_body", {})
    lines = [
        "## Canonical 4-Face Crystal Body\n",
        f"**Formula**: `{body.get('formula', 'H = {{□, ✿, ☁, ⟡}}')}`\n",
    ]
    faces = body.get("faces", [])
    for f in faces:
        if isinstance(f, dict):
            lines.append(f"- **{f.get('symbol', '?')} {f.get('name', '')}**: {f.get('meaning', '')}")
        else:
            lines.append(f"- {f}")
    if "mask_family" in body:
        lines.append(f"\n**Mask Family**: {body['mask_family']}")
    return "\n".join(lines)
