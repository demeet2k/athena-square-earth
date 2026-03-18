# CRYSTAL: Xi108:W2:A10:S16 | face=S | node=134 | depth=2 | phase=Cardinal
# METRO: Me
# BRIDGES: Xi108:W2:A10:S15→Xi108:W2:A10:S17→Xi108:W1:A10:S16→Xi108:W3:A10:S16→Xi108:W2:A9:S16→Xi108:W2:A11:S16

"""High-level orchestration: Atlas = solve + remember + retrieve.

The lower-level AtlasForge subsystems are powerful, but the user-facing
workflow you described is:

> "this is the full understanding of all the math we've been doing"

That is exactly what the :class:`~atlasforge.atlas.atlas.Atlas` object is for.

`Atlas` binds together:
- the Recipe executor (compute → certify → verify)
- the Memory bank (remember → search → link)
- optional sessions and graph linking
"""

from atlasforge.atlas.atlas import Atlas, AtlasConfig
from atlasforge.atlas.book import AtlasBookBuilder, AtlasBookConfig
from atlasforge.atlas.navigator import CrystalNavigator, CrystalCell

__all__ = [
    "Atlas",
    "AtlasConfig",
    "AtlasBookBuilder",
    "AtlasBookConfig",
    "CrystalNavigator",
    "CrystalCell",
]
