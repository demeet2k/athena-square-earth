# CRYSTAL: Xi108:W1:A5:S34 | face=C | node=251 | depth=1 | phase=Mutable
# METRO: Sa
# BRIDGES: Xi108:W1:A5:S33→Xi108:W1:A5:S35→Xi108:W2:A5:S34→Xi108:W1:A4:S34→Xi108:W1:A6:S34

"""Test configuration for the Athena MCP server."""

import os
import sys
from pathlib import Path

# Set ATHENA_ROOT to the repo root so tests can find data files
REPO_ROOT = Path(__file__).resolve().parent.parent
os.environ.setdefault("ATHENA_ROOT", str(REPO_ROOT))

# Add MCP directory to path so crystal_108d can be imported
sys.path.insert(0, str(REPO_ROOT / "MCP"))
