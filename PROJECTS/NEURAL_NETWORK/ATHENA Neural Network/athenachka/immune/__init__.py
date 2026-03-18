# CRYSTAL: Xi108:W2:A1:S23 | face=C | node=255 | depth=2 | phase=Cardinal
# METRO: Me
# BRIDGES: Xi108:W2:A1:S22→Xi108:W2:A1:S24→Xi108:W1:A1:S23→Xi108:W3:A1:S23→Xi108:W2:A2:S23

from .boundary_isolation import verify_boundary
from .contradiction_quarantine import detect_contradictions
from .corridor import resolve_corridor, trim_candidate_set
from .merge_boundary import (
    MergeBoundaryError,
    MergeGuardError,
    MergeTransitionError,
    advance_merge_state,
    allowed_transitions,
    bootstrap_merge_attempt,
    build_merge_ledger_entry,
    destination_for_terminal_state,
    emit_required_artifacts,
)
from .rollback import capture_checkpoint, restore_checkpoint
from .self_contract_gate import evaluate_self_contract
from .truth_lattice import classify_truth
from .witness_kernel import build_witness_bundle

__all__ = [
    "advance_merge_state",
    "allowed_transitions",
    "bootstrap_merge_attempt",
    "build_witness_bundle",
    "build_merge_ledger_entry",
    "capture_checkpoint",
    "classify_truth",
    "detect_contradictions",
    "destination_for_terminal_state",
    "emit_required_artifacts",
    "evaluate_self_contract",
    "MergeBoundaryError",
    "MergeGuardError",
    "MergeTransitionError",
    "resolve_corridor",
    "restore_checkpoint",
    "trim_candidate_set",
    "verify_boundary",
]
