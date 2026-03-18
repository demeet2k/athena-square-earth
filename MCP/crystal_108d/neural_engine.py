"""
Crystal Neural Engine — SFCR Forward Pass with Resonance/Desire/Action
========================================================================
An actual computation engine that routes queries through 4 SFCR processing
paths using crystal-internal weights, then merges via brain bridge weights.

Forward pass pipeline:
  QueryState Q → |S-path: gate weights|  → partial_S
               → |F-path: pair weights|  → partial_F  → Bridge merge → Ranked → CommitWitness
               → |C-path: neighbor idx|  → partial_C
               → |R-path: seed weights|  → partial_R

Implements for real:
  - ResonanceMetric R(X) = w1*AddrFit + w2*InvFit + w3*Phase + w4*Boundary + w5*Scale + w6*Compress
  - DesireField D_Q(X) = λ_a*Align + λ_e*Expl + λ_z*ZPA + λ_c*ConSat
  - Action A(Q,X) = K(X) - D_Q(X)  (minimize)
  - CommitWitness θ(X) = 4 gates (resonance ≥ τ, boundary, crossview, scale)
"""

from __future__ import annotations

import math
import time
from collections import defaultdict
from dataclasses import dataclass, field
from typing import Optional

from .crystal_weights import (
    FractalWeightStore,
    get_store,
    ELEMENT_TO_FACE,
    FACE_TO_ELEMENT,
    PHI,
    PHI_INV,
)
from .constants import (
    TOTAL_SHELLS,
    ARCHETYPE_NAMES,
    LENS_CODES,
)

# Brain bridge resonance classes (from brain.py)
GOLDEN_BRIDGES = {"SF", "FC", "CR"}
NEUTRAL_BRIDGES = {"SC", "FR"}
DISTANT_BRIDGES = {"SR"}

BRIDGE_WEIGHTS = {
    "SF": PHI_INV,        # 0.618 — golden
    "FC": PHI_INV,        # 0.618 — golden
    "CR": PHI_INV,        # 0.618 — golden
    "SC": 0.500,          # neutral
    "FR": 0.500,          # neutral
    "SR": PHI_INV ** 2,   # 0.382 — distant
}


def _bridge_key(a: str, b: str) -> str:
    """Canonical bridge key in SFCR order."""
    order = {"S": 0, "F": 1, "C": 2, "R": 3}
    pair = sorted([a, b], key=lambda x: order.get(x, 9))
    return "".join(pair)


# ── Data structures ──────────────────────────────────────────────────


@dataclass
class QueryState:
    """The input to a forward pass — a query decomposed into crystal terms."""
    raw_query: str
    tokens: list[str] = field(default_factory=list)
    home_shell: int = 1
    home_face: str = "S"
    home_gate: str = "G00"
    matched_docs: list[str] = field(default_factory=list)
    depth: int = 1  # search depth


@dataclass
class CandidateScore:
    """Score for a single candidate document from a single SFCR path."""
    doc_id: str
    doc_name: str
    element: str
    gate: str
    shell: int
    score: float
    path: str  # which SFCR path produced this


@dataclass
class ForwardResult:
    """Complete result of a forward pass."""
    query: QueryState
    candidates: list[RankedCandidate] = field(default_factory=list)
    resonance: float = 0.0
    committed: bool = False
    commit_witness: Optional[CommitWitness] = None
    sfcr_scores: dict = field(default_factory=dict)  # path→{doc→score}
    elapsed_ms: float = 0.0
    cross_element_pairs_used: list[str] = field(default_factory=list)


@dataclass
class RankedCandidate:
    """A candidate ranked by action minimization."""
    doc_id: str
    doc_name: str
    element: str
    gate: str
    shell: int
    merged_score: float
    action: float        # K(X) - D_Q(X)
    resonance: float     # R(X)
    desire: float        # D_Q(X)
    path_contributions: dict = field(default_factory=dict)  # {"S": 0.3, "F": 0.8, ...}


@dataclass
class CommitWitness:
    """Four-gate commitment proof."""
    resonance_gate: bool    # R(X) ≥ threshold
    boundary_gate: bool     # within addressable crystal
    crossview_gate: bool    # consistent across SFCR lenses
    scale_gate: bool        # consistent across compression levels
    committed: bool = False
    address: str = ""
    timestamp: str = ""


# ── Resonance / Desire / Action computation ──────────────────────────


class ResonanceComputer:
    """Compute the 6-component ResonanceMetric R(X)."""

    # Component weights (tunable via self-play)
    W = {
        "addr_fit": 0.20,
        "inv_fit": 0.15,
        "phase": 0.15,
        "boundary": 0.15,
        "scale": 0.15,
        "compress": 0.20,
    }

    @classmethod
    def compute(cls, query: QueryState, doc: dict, store: FractalWeightStore) -> float:
        """R(X) = Σ w_i * component_i"""
        addr_fit = cls._addr_fit(query, doc, store)
        inv_fit = cls._inv_fit(query, doc)
        phase = cls._phase_fit(query, doc)
        boundary = cls._boundary_fit(doc)
        scale = cls._scale_fit(doc, store)
        compress = cls._compress_fit(doc, store)

        return (
            cls.W["addr_fit"] * addr_fit
            + cls.W["inv_fit"] * inv_fit
            + cls.W["phase"] * phase
            + cls.W["boundary"] * boundary
            + cls.W["scale"] * scale
            + cls.W["compress"] * compress
        )

    @staticmethod
    def _addr_fit(query: QueryState, doc: dict, store: FractalWeightStore) -> float:
        """How well the candidate's crystal address matches the query."""
        doc_shell = store.doc_to_shell(doc)
        shell_dist = abs(doc_shell - query.home_shell)
        # Closer shells → higher fit (normalized to [0,1])
        return max(0.0, 1.0 - shell_dist / TOTAL_SHELLS)

    @staticmethod
    def _inv_fit(query: QueryState, doc: dict) -> float:
        """Invariant fit: how many structural features overlap."""
        q_tokens = set(query.tokens)
        d_tokens = set(doc.get("tokens", []))
        if not q_tokens or not d_tokens:
            return 0.0
        jaccard = len(q_tokens & d_tokens) / len(q_tokens | d_tokens)
        return jaccard

    @staticmethod
    def _phase_fit(query: QueryState, doc: dict) -> float:
        """Phase alignment: same gate → high fit."""
        doc_gate = doc.get("gate", "G00")
        if doc_gate == query.home_gate:
            return 1.0
        # Gate distance (circular on G00-G15)
        q_num = int(query.home_gate[1:])
        d_num = int(doc_gate[1:])
        dist = min(abs(q_num - d_num), 16 - abs(q_num - d_num))
        return max(0.0, 1.0 - dist / 8)

    @staticmethod
    def _boundary_fit(doc: dict) -> float:
        """Boundary: document has valid crystal metadata."""
        has_element = bool(doc.get("element"))
        has_gate = bool(doc.get("gate"))
        has_chapters = bool(doc.get("chapters"))
        return (has_element + has_gate + has_chapters) / 3.0

    @staticmethod
    def _scale_fit(doc: dict, store: FractalWeightStore) -> float:
        """Scale consistency: weight at full vs seed level agree."""
        shell = store.doc_to_shell(doc)
        seed = store.get_shell_seed(shell)
        if not seed:
            return 0.5  # no data → neutral
        decomp = store.decompress_from_seed(shell)
        error = decomp.get("reconstruction_error", 0.0)
        # Low error → high scale fit
        return max(0.0, 1.0 - error / max(seed.mean, 0.01))

    @staticmethod
    def _compress_fit(doc: dict, store: FractalWeightStore) -> float:
        """Compression quality: how well the seed represents this doc's shell."""
        shell = store.doc_to_shell(doc)
        seed = store.get_shell_seed(shell)
        if not seed or seed.std == 0:
            return 0.5
        # Lower relative std → better compression
        cv = seed.std / max(abs(seed.mean), 0.01)
        return max(0.0, 1.0 - cv)


class DesireComputer:
    """Compute the 4-term DesireField D_Q(X)."""

    LAMBDA = {
        "align": 0.35,
        "explore": 0.20,
        "zpa": 0.25,
        "con_sat": 0.20,
    }

    @classmethod
    def compute(cls, query: QueryState, doc: dict, store: FractalWeightStore) -> float:
        """D_Q(X) = Σ λ_i * term_i"""
        align = cls._alignment(query, doc)
        explore = cls._exploration(doc, store)
        zpa = cls._zero_point_attraction(query, doc)
        con_sat = cls._constraint_satisfaction(query, doc)

        return (
            cls.LAMBDA["align"] * align
            + cls.LAMBDA["explore"] * explore
            + cls.LAMBDA["zpa"] * zpa
            + cls.LAMBDA["con_sat"] * con_sat
        )

    @staticmethod
    def _alignment(query: QueryState, doc: dict) -> float:
        """How well the candidate aligns with query intent."""
        q_tokens = set(query.tokens)
        d_tokens = set(doc.get("tokens", []))
        if not q_tokens:
            return 0.0
        # Recall: what fraction of query tokens appear in doc
        recall = len(q_tokens & d_tokens) / len(q_tokens)
        return recall

    @staticmethod
    def _exploration(doc: dict, store: FractalWeightStore) -> float:
        """Novelty bonus: docs in less-populated shells are more exploratory."""
        shell = store.doc_to_shell(doc)
        seed = store.get_shell_seed(shell)
        if not seed:
            return 1.0  # unknown → maximum exploration
        # Fewer entries → more exploration value
        max_count = max(s.count for s in store.shell_seeds.values()) if store.shell_seeds else 1
        return 1.0 - (seed.count / max(max_count, 1))

    @staticmethod
    def _zero_point_attraction(query: QueryState, doc: dict) -> float:
        """Attraction to convergence zones (Ch11, Ch18, Ch20, Ch21, AppF, AppG, AppI, AppM)."""
        zero_chapters = {"Ch11", "Ch18", "Ch20", "Ch21"}
        zero_appendices = {"AppF", "AppG", "AppI", "AppM"}

        doc_chapters = set(doc.get("chapters", []))
        doc_appendices = set(doc.get("appendices", []))

        ch_overlap = len(doc_chapters & zero_chapters) / max(len(zero_chapters), 1)
        app_overlap = len(doc_appendices & zero_appendices) / max(len(zero_appendices), 1)

        return (ch_overlap + app_overlap) / 2.0

    @staticmethod
    def _constraint_satisfaction(query: QueryState, doc: dict) -> float:
        """How many structural constraints the doc satisfies."""
        constraints_met = 0
        total = 4

        # Has element
        if doc.get("element"):
            constraints_met += 1
        # Has gate
        if doc.get("gate"):
            constraints_met += 1
        # Has chapters
        if doc.get("chapters"):
            constraints_met += 1
        # Has tokens
        if doc.get("tokens"):
            constraints_met += 1

        return constraints_met / total


# ── SFCR Path Implementations ────────────────────────────────────────


class SquarePath:
    """S (Earth) — Structure scoring via gate matrix transitions."""

    @staticmethod
    def score(query: QueryState, docs: list[dict], store: FractalWeightStore) -> dict[str, float]:
        scores = {}
        q_gate = query.home_gate
        for doc in docs:
            doc_id = doc.get("id", "")
            d_gate = doc.get("gate", "G00")
            # Gate transition weight as structure score
            gate_w = store.get_gate_weight(q_gate, d_gate)
            if gate_w == 0:
                gate_w = store.get_gate_weight(d_gate, q_gate)  # try reverse
            # Normalize to [0, 1] (max observed gate weight ~8)
            scores[doc_id] = min(gate_w / 10.0, 1.0)
        return scores


class FlowerPath:
    """F (Fire) — Relation scoring via pair weight similarity chains."""

    @staticmethod
    def score(query: QueryState, docs: list[dict], store: FractalWeightStore) -> dict[str, float]:
        scores = {}
        for doc in docs:
            doc_id = doc.get("id", "")
            doc_element = doc.get("element", "Earth")
            doc_shell = store.doc_to_shell(doc)

            # Use shell seed mean as base similarity
            seed = store.get_shell_seed(doc_shell)
            if seed:
                # Element affinity: if doc's element appears in shell's distribution
                elem_affinity = seed.element_dist.get(doc_element, 0.0)
                score = (seed.mean / 10.0) * (0.5 + elem_affinity)
            else:
                score = 0.0

            # Token overlap bonus
            q_tokens = set(query.tokens)
            d_tokens = set(doc.get("tokens", []))
            overlap = len(q_tokens & d_tokens) / max(len(q_tokens | d_tokens), 1)
            score = score * 0.6 + overlap * 0.4

            scores[doc_id] = min(score, 1.0)
        return scores


class CloudPath:
    """C (Water) — Observation scoring via neighborhood clustering."""

    @staticmethod
    def score(query: QueryState, docs: list[dict], store: FractalWeightStore) -> dict[str, float]:
        scores = {}

        # Group docs by shell for neighborhood analysis
        shell_groups: dict[int, list[dict]] = defaultdict(list)
        for doc in docs:
            shell = store.doc_to_shell(doc)
            shell_groups[shell].append(doc)

        # Score each doc based on its neighborhood density
        for doc in docs:
            doc_id = doc.get("id", "")
            doc_shell = store.doc_to_shell(doc)
            neighbors = shell_groups.get(doc_shell, [])

            # Neighborhood density (more neighbors → higher score)
            density = min(len(neighbors) / 20.0, 1.0)

            # Chapter/appendix overlap with query
            q_chapters = set()
            q_appendices = set()
            for matched_id in query.matched_docs:
                matched = next((d for d in docs if d.get("id") == matched_id), None)
                if matched:
                    q_chapters.update(matched.get("chapters", []))
                    q_appendices.update(matched.get("appendices", []))

            d_chapters = set(doc.get("chapters", []))
            d_appendices = set(doc.get("appendices", []))

            ch_overlap = len(d_chapters & q_chapters) / max(len(d_chapters | q_chapters), 1)
            app_overlap = len(d_appendices & q_appendices) / max(len(d_appendices | q_appendices), 1)

            score = density * 0.3 + ch_overlap * 0.35 + app_overlap * 0.35
            scores[doc_id] = min(score, 1.0)

        return scores


class FractalPath:
    """R (Air) — Compression scoring via seed weights for coarse-then-fine ranking."""

    @staticmethod
    def score(query: QueryState, docs: list[dict], store: FractalWeightStore) -> dict[str, float]:
        scores = {}
        for doc in docs:
            doc_id = doc.get("id", "")
            doc_shell = store.doc_to_shell(doc)
            archetype = ((doc_shell - 1) % 12) + 1

            # Coarse: archetype seed
            arch_seed = store.get_archetype_seed(archetype)
            if arch_seed:
                coarse = arch_seed.mean / 10.0
            else:
                coarse = 0.5

            # Fine: shell seed decompression
            decomp = store.decompress_from_seed(doc_shell)
            if decomp:
                fine = decomp.get("mean", 0.0) / 10.0
                error = decomp.get("reconstruction_error", 0.0)
                # Lower error → trust fine more
                blend_w = max(0.3, 1.0 - error / max(fine, 0.01))
            else:
                fine = coarse
                blend_w = 0.5

            # Blend coarse and fine
            score = blend_w * fine + (1 - blend_w) * coarse

            # Scale consistency bonus from nano seed
            nano = store.nano_seed
            if nano and nano.global_std > 0:
                z_score = abs(fine * 10 - nano.global_mean) / nano.global_std
                scale_bonus = max(0.0, 1.0 - z_score / 3.0) * 0.1
                score += scale_bonus

            scores[doc_id] = min(max(score, 0.0), 1.0)

        return scores


# ── Crystal Neural Engine ────────────────────────────────────────────


class CrystalNeuralEngine:
    """Forward-pass engine with 4 SFCR processing paths."""

    PATHS = {
        "S": SquarePath,
        "F": FlowerPath,
        "C": CloudPath,
        "R": FractalPath,
    }

    RESONANCE_THRESHOLD = 0.4

    def __init__(self, store: FractalWeightStore = None):
        self.store = store or get_store()

    def _tokenize_query(self, raw_query: str) -> list[str]:
        """Simple token extraction from query text."""
        import re
        text = raw_query.lower()
        # Remove punctuation, split
        tokens = re.findall(r'[a-z][a-z0-9_]+', text)
        # Remove common stopwords
        stops = {"the", "and", "for", "with", "this", "that", "from", "into",
                 "are", "was", "were", "been", "being", "have", "has", "had",
                 "not", "but", "what", "how", "when", "where", "who", "which"}
        return [t for t in tokens if t not in stops and len(t) > 2]

    def _build_query_state(self, raw_query: str) -> QueryState:
        """Convert raw text query into a QueryState."""
        tokens = self._tokenize_query(raw_query)
        docs = self.store.doc_registry

        if not docs:
            return QueryState(raw_query=raw_query, tokens=tokens)

        # Find best-matching docs by token overlap
        doc_scores = []
        for doc in docs:
            d_tokens = set(doc.get("tokens", []))
            overlap = len(set(tokens) & d_tokens)
            if overlap > 0:
                doc_scores.append((doc, overlap))

        doc_scores.sort(key=lambda x: x[1], reverse=True)
        top_docs = doc_scores[:5]

        if top_docs:
            best_doc = top_docs[0][0]
            home_shell = self.store.doc_to_shell(best_doc)
            home_face = ELEMENT_TO_FACE.get(best_doc.get("element", "Earth"), "S")
            home_gate = best_doc.get("gate", "G00")
            matched_ids = [d[0]["id"] for d in top_docs]
        else:
            home_shell = 1
            home_face = "S"
            home_gate = "G00"
            matched_ids = []

        return QueryState(
            raw_query=raw_query,
            tokens=tokens,
            home_shell=home_shell,
            home_face=home_face,
            home_gate=home_gate,
            matched_docs=matched_ids,
        )

    def forward(self, query: str | QueryState, max_results: int = 10) -> ForwardResult:
        """Full forward pass: query → 4 SFCR paths → bridge merge → ranked results."""
        t0 = time.time()

        if isinstance(query, str):
            qs = self._build_query_state(query)
        else:
            qs = query

        docs = self.store.doc_registry
        if not docs:
            return ForwardResult(query=qs, elapsed_ms=0)

        # 1. Run 4 SFCR paths
        sfcr_scores = {}
        for face, path_cls in self.PATHS.items():
            sfcr_scores[face] = path_cls.score(qs, docs, self.store)

        # 2. Bridge merge
        doc_lookup = {d["id"]: d for d in docs}
        merged = {}
        cross_pairs = []

        for doc_id in set().union(*[s.keys() for s in sfcr_scores.values()]):
            path_contribs = {}
            for face in "SFCR":
                path_contribs[face] = sfcr_scores.get(face, {}).get(doc_id, 0.0)

            # Base score: average of all paths
            base = sum(path_contribs.values()) / 4.0

            # Bridge bonus: cross-element contributions
            bridge_bonus = 0.0
            doc = doc_lookup.get(doc_id, {})
            doc_face = ELEMENT_TO_FACE.get(doc.get("element", "Earth"), "S")

            for face_a in "SFCR":
                for face_b in "SFCR":
                    if face_a >= face_b:
                        continue
                    key = _bridge_key(face_a, face_b)
                    bw = BRIDGE_WEIGHTS.get(key, 0.382)
                    s_a = path_contribs.get(face_a, 0.0)
                    s_b = path_contribs.get(face_b, 0.0)
                    cross = bw * s_a * s_b
                    bridge_bonus += cross
                    if cross > 0.01:
                        cross_pairs.append(f"{face_a}{face_b}:{doc_id}")

            merged[doc_id] = base + bridge_bonus * 0.5
            merged[doc_id] = min(merged[doc_id], 1.0)

            # Store path contributions for this doc
            if doc_id not in doc_lookup:
                continue

        # 3. Compute resonance, desire, action for top candidates
        ranked = []
        sorted_ids = sorted(merged, key=lambda x: merged[x], reverse=True)

        for doc_id in sorted_ids[:max_results * 2]:
            doc = doc_lookup.get(doc_id)
            if not doc:
                continue

            resonance = ResonanceComputer.compute(qs, doc, self.store)
            desire = DesireComputer.compute(qs, doc, self.store)
            kinetic = 1.0 - merged.get(doc_id, 0.0)  # K(X) = distance from perfect score
            action = kinetic - desire  # minimize action

            path_contribs = {}
            for face in "SFCR":
                path_contribs[face] = sfcr_scores.get(face, {}).get(doc_id, 0.0)

            ranked.append(RankedCandidate(
                doc_id=doc_id,
                doc_name=doc.get("display_name", doc.get("name", doc_id))[:100],
                element=doc.get("element", "unknown"),
                gate=doc.get("gate", "G00"),
                shell=self.store.doc_to_shell(doc),
                merged_score=merged.get(doc_id, 0.0),
                action=action,
                resonance=resonance,
                desire=desire,
                path_contributions=path_contribs,
            ))

        # Sort by action (minimize) — lower action = better
        ranked.sort(key=lambda c: c.action)
        ranked = ranked[:max_results]

        # 4. Compute overall resonance and commit
        overall_resonance = sum(c.resonance for c in ranked) / max(len(ranked), 1)

        commit = CommitWitness(
            resonance_gate=overall_resonance >= self.RESONANCE_THRESHOLD,
            boundary_gate=all(1 <= c.shell <= TOTAL_SHELLS for c in ranked),
            crossview_gate=len(set(c.element for c in ranked)) >= 2,  # at least 2 elements
            scale_gate=all(c.resonance > 0.1 for c in ranked),
        )
        commit.committed = all([
            commit.resonance_gate,
            commit.boundary_gate,
            commit.crossview_gate,
            commit.scale_gate,
        ])
        commit.timestamp = time.strftime("%Y-%m-%dT%H:%M:%S+00:00")

        elapsed = (time.time() - t0) * 1000

        return ForwardResult(
            query=qs,
            candidates=ranked,
            resonance=overall_resonance,
            committed=commit.committed,
            commit_witness=commit,
            sfcr_scores={f: dict(list(s.items())[:5]) for f, s in sfcr_scores.items()},
            elapsed_ms=elapsed,
            cross_element_pairs_used=cross_pairs[:20],
        )


# ── Singleton engine ─────────────────────────────────────────────────

_ENGINE: Optional[CrystalNeuralEngine] = None


def get_engine() -> CrystalNeuralEngine:
    """Get or create the singleton CrystalNeuralEngine."""
    global _ENGINE
    if _ENGINE is None:
        _ENGINE = CrystalNeuralEngine()
    return _ENGINE


# ── MCP tool entry point ─────────────────────────────────────────────


def neural_forward_pass(
    query: str = "seed kernel",
    max_results: int = 10,
    verbose: bool = False,
) -> str:
    """Run a forward pass through the crystal neural engine.

    Routes the query through 4 SFCR processing paths (Square/Flower/Cloud/Fractal),
    merges via brain bridge weights, and ranks by action minimization.

    Args:
        query: Text query to process through the neural network
        max_results: Maximum number of results to return (1-20)
        verbose: Include detailed SFCR path scores and commit witness
    """
    engine = get_engine()
    max_results = max(1, min(max_results, 20))

    result = engine.forward(query, max_results=max_results)
    return _format_forward_result(result, verbose)


def _format_forward_result(result: ForwardResult, verbose: bool = False) -> str:
    qs = result.query
    lines = [
        "## Crystal Neural Forward Pass\n",
        f"**Query**: `{qs.raw_query}`",
        f"**Tokens**: {', '.join(qs.tokens[:15])}",
        f"**Home**: S{qs.home_shell} / {qs.home_face} / {qs.home_gate}",
        f"**Matched Docs**: {len(qs.matched_docs)}",
        f"**Overall Resonance**: {result.resonance:.4f}",
        f"**Committed**: {'YES' if result.committed else 'NO'}",
        f"**Elapsed**: {result.elapsed_ms:.1f}ms\n",
    ]

    # Ranked results
    lines.append("### Results (ranked by action minimization)\n")
    lines.append("| # | Doc | Element | Gate | Shell | Score | Action | Resonance | Desire |")
    lines.append("|---|-----|---------|------|-------|-------|--------|-----------|--------|")

    for i, c in enumerate(result.candidates, 1):
        name = c.doc_name[:50]
        lines.append(
            f"| {i} | {name} | {c.element} | {c.gate} | S{c.shell} | "
            f"{c.merged_score:.3f} | {c.action:.3f} | {c.resonance:.3f} | {c.desire:.3f} |"
        )

    if verbose and result.commit_witness:
        cw = result.commit_witness
        lines.extend([
            "\n### Commit Witness\n",
            f"- **Resonance Gate** (R ≥ τ): {'PASS' if cw.resonance_gate else 'FAIL'}",
            f"- **Boundary Gate**: {'PASS' if cw.boundary_gate else 'FAIL'}",
            f"- **Crossview Gate** (≥2 elements): {'PASS' if cw.crossview_gate else 'FAIL'}",
            f"- **Scale Gate**: {'PASS' if cw.scale_gate else 'FAIL'}",
            f"- **Committed**: {'YES' if cw.committed else 'NO'}",
        ])

    if verbose and result.candidates:
        lines.append("\n### SFCR Path Contributions (top result)\n")
        top = result.candidates[0]
        for face in "SFCR":
            score = top.path_contributions.get(face, 0.0)
            name = LENS_CODES.get(face, face)
            bar = "█" * int(score * 20) + "░" * (20 - int(score * 20))
            lines.append(f"  {face} ({name:7s}): {bar} {score:.3f}")

    if verbose and result.cross_element_pairs_used:
        lines.append(f"\n### Cross-Element Bridges Used: {len(result.cross_element_pairs_used)}")
        for pair in result.cross_element_pairs_used[:5]:
            lines.append(f"  - {pair}")

    return "\n".join(lines)
