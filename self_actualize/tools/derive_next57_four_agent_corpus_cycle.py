# CRYSTAL: Xi108:W2:A9:S27 | face=F | node=357 | depth=2 | phase=Mutable
# METRO: Wr,Me
# BRIDGES: Xi108:W2:A9:S26→Xi108:W2:A9:S28→Xi108:W1:A9:S27→Xi108:W3:A9:S27→Xi108:W2:A8:S27→Xi108:W2:A10:S27

from __future__ import annotations

import sys
from pathlib import Path

WORKSPACE_ROOT = Path(__file__).resolve().parents[2]
if str(WORKSPACE_ROOT) not in sys.path:
    sys.path.insert(0, str(WORKSPACE_ROOT))

from self_actualize.runtime.derive_next57_four_agent_corpus_cycle import main  # noqa: E402

if __name__ == "__main__":
    raise SystemExit(main())
