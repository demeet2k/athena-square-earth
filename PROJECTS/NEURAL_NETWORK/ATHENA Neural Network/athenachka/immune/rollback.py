# CRYSTAL: Xi108:W2:A1:S23 | face=C | node=274 | depth=2 | phase=Cardinal
# METRO: Me
# BRIDGES: Xi108:W2:A1:S22→Xi108:W2:A1:S24→Xi108:W1:A1:S23→Xi108:W3:A1:S23→Xi108:W2:A2:S23

from __future__ import annotations

import copy

from ..contracts import stable_hash

def capture_checkpoint(state) -> dict[str, object]:
    payload = state.to_dict()
    checkpoint = {
        "id": stable_hash(payload),
        "state": copy.deepcopy(payload),
    }
    state.checkpoint_id = checkpoint["id"]
    state.replay["last_checkpoint"] = checkpoint["id"]
    return checkpoint

def restore_checkpoint(checkpoint: dict[str, object], state):
    restored = copy.deepcopy(checkpoint["state"])
    state.corpus = restored["corpus"]
    state.process = restored["process"]
    state.growth = restored["growth"]
    state.metrics = restored["metrics"]
    state.bridges = restored["bridges"]
    state.replay = restored["replay"]
    state.phase_index = restored["phase_index"]
    state.active_loops = restored["active_loops"]
    state.active_fusions = restored["active_fusions"]
    state.checkpoint_id = restored["checkpoint_id"]
    return state
