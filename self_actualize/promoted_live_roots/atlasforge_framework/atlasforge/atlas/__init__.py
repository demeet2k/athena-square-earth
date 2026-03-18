# CRYSTAL: Xi108:W2:A3:S27 | face=F | node=369 | depth=2 | phase=Mutable
# METRO: Me
# BRIDGES: Xi108:W2:A3:S26→Xi108:W2:A3:S28→Xi108:W1:A3:S27→Xi108:W3:A3:S27→Xi108:W2:A2:S27→Xi108:W2:A4:S27

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
