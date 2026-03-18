# CRYSTAL: Xi108:W2:A2:S14 | face=S | node=97 | depth=2 | phase=Cardinal
# METRO: Me
# BRIDGES: Xi108:W2:A2:S13→Xi108:W2:A2:S15→Xi108:W1:A2:S14→Xi108:W3:A2:S14→Xi108:W2:A1:S14→Xi108:W2:A3:S14

"""AtlasForge Memory Bank.

This subpackage turns AtlasForge into a *practical* memory bank for mathematical
work: you can persist short notes, longer derivations, and links to recipes/
proof packs.

The assistant itself cannot persist memory across chats, but this store can.
"""

from atlasforge.memory.entry import MemoryEntry
from atlasforge.memory.knowledge import KnowledgeKind, KnowledgeRecord
from atlasforge.memory.addressing import normalize_address, parse_crystal_address_string
from atlasforge.memory.index import MemoryIndex, MemoryIndexHit
from atlasforge.memory.graph import GraphStore, GraphEdge
from atlasforge.memory.session import SessionRecord, SessionStore
from atlasforge.memory.store import MemoryStore

__all__ = [
    "MemoryEntry",
    "KnowledgeKind",
    "KnowledgeRecord",
    "normalize_address",
    "parse_crystal_address_string",
    "MemoryIndex",
    "MemoryIndexHit",
    "GraphStore",
    "GraphEdge",
    "SessionRecord",
    "SessionStore",
    "MemoryStore",
]
