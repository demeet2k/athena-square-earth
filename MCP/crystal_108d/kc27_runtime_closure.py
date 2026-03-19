# CRYSTAL: Xi108:W2:A7:S31 | face=C | node=410 | depth=2 | phase=Mutable
# METRO: Sa
# BRIDGES: Xi108:W2:A7:S30→Xi108:W2:A7:S32→Xi108:W1:A7:S31→Xi108:W3:A7:S31→Xi108:W2:A6:S31→Xi108:W2:A8:S31

"""
KC27 Runtime Closure — Quantum Crystal Runtime Closure
=======================================================
Provides the KC27 runtime closure system:
  - Problem field (27 problems, desire field, target class, resolution planes)
  - C2 holographic attractor (super-object, five membranes, current state)
  - Proof cell (replay-bearing proof, six-stage compiler, reseeding chain)
  - Runtime closure (ternary ring, 9 books, closure conditions, invariants)
  - Knowledge crystal (4D geometry, extraction types, operator algebra, civilization substrate)
"""

from ._cache import JsonCache

_CACHE = JsonCache("kc27_runtime_closure.json")


def query_kc27_runtime_closure(component: str = "all") -> str:
    """
    Query KC27 runtime closure — quantum crystal runtime closure system.

    Components:
      - all              : Full KC27 runtime closure overview
      - problem_field    : 27-problem desire field, target class, resolution planes
      - c2_attractor     : C2 holographic attractor super-object and current state
      - proof_cell       : First replay-bearing proof cell definition
      - runtime_closure  : Runtime closure conditions, ternary ring, and invariants
      - knowledge_crystal: 4D Knowledge Crystal architecture and civilization substrate
    """
    data = _CACHE.load()
    comp = component.strip().lower()

    if comp == "all":
        return _format_all(data)
    elif comp == "problem_field":
        return _format_problem_field(data)
    elif comp == "c2_attractor":
        return _format_c2_attractor(data)
    elif comp == "proof_cell":
        return _format_proof_cell(data)
    elif comp == "runtime_closure":
        return _format_runtime_closure(data)
    elif comp == "knowledge_crystal":
        return _format_knowledge_crystal(data)
    else:
        return (
            f"Unknown component '{component}'. Use: all, problem_field, c2_attractor, "
            "proof_cell, runtime_closure, knowledge_crystal"
        )


def _format_all(data: dict) -> str:
    meta = data.get("meta", {})
    lines = [
        "## KC27 — Quantum Crystal Runtime Closure\n",
        f"**Title**: {meta.get('title', '')}",
        f"**Doc ID**: {meta.get('doc_id', '')}",
        f"**Size**: {meta.get('size_chars', '')} chars",
        f"**Modified**: {meta.get('modified', '')}",
        f"**Description**: {meta.get('description', '')}",
    ]

    # Problem field summary
    pf = data.get("problem_field", {})
    lines.append(f"\n### Problem Field")
    lines.append(f"- **Raw Desire**: {pf.get('raw_desire', '')}")
    lines.append(f"- **Desire Seed**: {pf.get('desire_seed', '')}")
    planes = pf.get("resolution_planes", [])
    for p in planes:
        lines.append(f"- **{p.get('plane', '')}** ({p.get('symbol', '')}): {p.get('question', '')}")

    # C2 attractor summary
    c2 = data.get("c2_attractor", {})
    lines.append(f"\n### C2 Holographic Attractor")
    lines.append(f"- **Truth Class**: {c2.get('truth_class', '')}")
    so = c2.get("super_object", {})
    lines.append(f"- **Super-Object**: {so.get('definition', '')}")

    # Proof cell summary
    pc = data.get("proof_cell", {})
    lines.append(f"\n### Proof Cell")
    lines.append(f"- **Replay Protocol**: {pc.get('replay_protocol', '')}")
    for ob in pc.get("proof_obligations", []):
        lines.append(f"- {ob}")

    # Runtime closure summary
    rc = data.get("runtime_closure", {})
    tr = rc.get("ternary_ring", {})
    lines.append(f"\n### Runtime Closure")
    lines.append(f"- **Chapters**: {tr.get('total_chapters', '')}")
    lines.append(f"- **Mirror Law**: {tr.get('mirror_law', '')}")
    lines.append(f"- **Center**: {tr.get('center', '')}")
    for cond in rc.get("closure_conditions", []):
        lines.append(f"- {cond}")

    # Knowledge crystal summary
    kc = data.get("knowledge_crystal", {})
    geom = kc.get("geometry", {})
    lines.append(f"\n### 4D Knowledge Crystal")
    lines.append(f"- **Dimensions**: {geom.get('dimensions', '')}")
    lines.append(f"- **Structure**: {geom.get('structure', '')}")
    lines.append(f"- **Coordinates**: {geom.get('coordinates', '')}")

    return "\n".join(lines)


def _format_problem_field(data: dict) -> str:
    pf = data.get("problem_field", {})
    lines = [
        "## Problem Field — Book I\n",
        f"**Description**: {pf.get('description', '')}",
        f"\n**Raw Desire**: {pf.get('raw_desire', '')}",
        f"**Desire Seed**: {pf.get('desire_seed', '')}",
    ]

    # Target class
    tc = pf.get("target_class", {})
    lines.append(f"\n### Target Class")
    lines.append(f"**Definition**: {tc.get('definition', '')}")
    lines.append(f"**Nonempty Condition**: {tc.get('nonempty_condition', '')}")

    # C2 minimality
    cm = pf.get("c2_minimality", {})
    lines.append(f"\n### C2 Minimality")
    lines.append(cm.get("proposition", ""))

    # Resolution planes
    lines.append(f"\n### Resolution Planes")
    for p in pf.get("resolution_planes", []):
        lines.append(f"- **{p.get('plane', '')}** ({p.get('symbol', '')}): "
                      f"{p.get('question', '')} — {p.get('satisfied_by', '')}")

    lines.append(f"\n### Plane Inseparability")
    lines.append(pf.get("plane_inseparability", ""))

    # Desire compilation
    dc = pf.get("desire_compilation", {})
    lines.append(f"\n### Desire Compilation Schema")
    lines.append(f"**Schema**: `{dc.get('schema', '')}`")
    comps = dc.get("components", {})
    for k, v in comps.items():
        lines.append(f"- **{k}**: {v}")

    # Desire dynamics
    lines.append(f"\n### Desire Dynamics")
    for d in pf.get("desire_dynamics", []):
        lines.append(f"- {d}")

    # Failure surfaces
    lines.append(f"\n### Failure Surfaces")
    for f_ in pf.get("failure_surfaces", []):
        lines.append(f"- {f_}")

    # Chapters and books
    lines.append(f"\n### Chapters")
    for ch, desc in pf.get("chapters", {}).items():
        lines.append(f"- **{ch}**: {desc}")

    lines.append(f"\n### Books")
    for bk, desc in pf.get("books", {}).items():
        lines.append(f"- **{bk}**: {desc}")

    return "\n".join(lines)


def _format_c2_attractor(data: dict) -> str:
    c2 = data.get("c2_attractor", {})
    lines = [
        "## C2 Holographic Attractor\n",
        f"**Description**: {c2.get('description', '')}",
        f"**Truth Class**: {c2.get('truth_class', '')}",
    ]

    # Super-object
    so = c2.get("super_object", {})
    lines.append(f"\n### Super-Object Definition")
    lines.append(f"**Definition**: `{so.get('definition', '')}`")
    for key in ("M_cell", "M_store", "M_transition", "M_lineage", "M_roundtrip"):
        lines.append(f"- **{key}**: {so.get(key, '')}")

    lines.append(f"\n### Holographic Attractor Theorem")
    lines.append(c2.get("holographic_attractor_theorem", ""))

    # Current state
    lines.append(f"\n### Current State")
    state = c2.get("current_state", {})
    for comp, status in state.items():
        lines.append(f"- **{comp}**: {status}")

    # Five membranes
    lines.append(f"\n### Five Membranes")
    for mem in c2.get("five_membranes", []):
        lines.append(f"- {mem}")

    return "\n".join(lines)


def _format_proof_cell(data: dict) -> str:
    pc = data.get("proof_cell", {})
    lines = [
        "## First Replay-Bearing Proof Cell\n",
        f"**Description**: {pc.get('description', '')}",
        f"**Replay Protocol**: {pc.get('replay_protocol', '')}",
    ]

    # Proof obligations
    lines.append(f"\n### Proof Obligations")
    for ob in pc.get("proof_obligations", []):
        lines.append(f"- {ob}")

    # Branch outcomes
    lines.append(f"\n### Branch Outcomes")
    outcomes = pc.get("branch_outcomes", [])
    lines.append(f"Possible: {', '.join(outcomes)}")
    lines.append(f"**Successor Seed**: {pc.get('successor_seed', '')}")

    lines.append(f"\n### Commit Ready Gate")
    lines.append(pc.get("commit_ready_gate", ""))

    # Six-stage compiler
    lines.append(f"\n### Six-Stage Desire Compiler")
    for stage in pc.get("six_stage_compiler", []):
        lines.append(f"- {stage}")

    # Replayability
    lines.append(f"\n### Replayability")
    lines.append(pc.get("replayability", ""))

    # Reseeding chain
    lines.append(f"\n### Reseeding Chain")
    for seed in pc.get("reseeding_chain", []):
        lines.append(f"- {seed}")

    return "\n".join(lines)


def _format_runtime_closure(data: dict) -> str:
    rc = data.get("runtime_closure", {})
    lines = [
        "## Runtime Closure\n",
        f"**Description**: {rc.get('description', '')}",
    ]

    # Ternary ring
    tr = rc.get("ternary_ring", {})
    lines.append(f"\n### Ternary Ring Structure")
    lines.append(f"- **Total Chapters**: {tr.get('total_chapters', '')}")
    lines.append(f"- **Encoding**: {tr.get('encoding', '')}")
    lines.append(f"- **Mirror Law**: {tr.get('mirror_law', '')}")
    lines.append(f"- **Center**: {tr.get('center', '')}")
    lines.append(f"- **Ring Count**: {tr.get('ring_count', '')}")
    lines.append(f"- **Outermost Ring**: {tr.get('outermost_ring', '')}")
    lines.append(f"- **Innermost Ring**: {tr.get('innermost_ring', '')}")

    # Book structure
    lines.append(f"\n### Book Structure")
    for book in rc.get("book_structure", []):
        lines.append(f"- **Book {book.get('book', '')}** — {book.get('title', '')} "
                      f"({book.get('chapters', '')}): {book.get('function', '')}")

    # Chapter face structure
    cfs = rc.get("chapter_face_structure", {})
    lines.append(f"\n### Chapter Face Structure (SFCR)")
    for face in cfs.get("faces", []):
        lines.append(f"- **{face.get('face', '')}**: {face.get('function', '')}")

    # Closure conditions
    lines.append(f"\n### Closure Conditions")
    for cond in rc.get("closure_conditions", []):
        lines.append(f"- {cond}")

    # Truth classification
    lines.append(f"\n### Truth Classification")
    tc = rc.get("truth_classification", {})
    for cls, desc in tc.items():
        lines.append(f"- **{cls}**: {desc}")

    # Key invariants
    lines.append(f"\n### Key Invariants")
    for inv in rc.get("key_invariants", []):
        lines.append(f"- {inv}")

    # Anti-overfit guards
    lines.append(f"\n### Anti-Overfit Guards")
    for guard in rc.get("anti_overfit_guards", []):
        lines.append(f"- {guard}")

    return "\n".join(lines)


def _format_knowledge_crystal(data: dict) -> str:
    kc = data.get("knowledge_crystal", {})
    lines = [
        "## 4D Knowledge Crystal\n",
        f"**Description**: {kc.get('description', '')}",
    ]

    # Geometry
    geom = kc.get("geometry", {})
    lines.append(f"\n### Geometry")
    lines.append(f"- **Dimensions**: {geom.get('dimensions', '')}")
    lines.append(f"- **Structure**: {geom.get('structure', '')}")
    lines.append(f"- **Center**: {geom.get('center', '')}")
    lines.append(f"- **Rings**: {geom.get('rings', '')}")
    lines.append(f"- **Coordinates**: `{geom.get('coordinates', '')}`")

    # Extraction types
    lines.append(f"\n### Extraction Types")
    for et in kc.get("extraction_types", []):
        lines.append(f"- **{et.get('type', '')}**: {et.get('description', '')}")

    # Score vector
    sv = kc.get("score_vector", {})
    lines.append(f"\n### Score Vector ({sv.get('axes', '')} axes)")
    for axis in sv.get("list", []):
        lines.append(f"- {axis}")

    # Operator algebra
    oa = kc.get("operator_algebra", {})
    lines.append(f"\n### Operator Algebra")
    lines.append(f"**Completeness**: {oa.get('completeness', '')}")
    lines.append(f"**Shell Transport**: {oa.get('shell_transport', '')}")
    lines.append("**K1 Primitives**:")
    for prim in oa.get("K1_primitives", []):
        lines.append(f"- {prim}")

    # Civilization substrate
    cs = kc.get("civilization_substrate", {})
    lines.append(f"\n### Civilization Substrate")
    lines.append(f"**Description**: {cs.get('description', '')}")
    lines.append("**Phases**:")
    for phase in cs.get("phases", []):
        lines.append(f"- {phase}")
    lines.append("**Key Invariants**:")
    for inv in cs.get("key_invariants", []):
        lines.append(f"- {inv}")

    return "\n".join(lines)
