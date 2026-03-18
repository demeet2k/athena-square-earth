# CRYSTAL: Xi108:W2:A10:S28 | face=F | node=400 | depth=2 | phase=Mutable
# METRO: Sa,Me
# BRIDGES: Xi108:W2:A10:S27→Xi108:W2:A10:S29→Xi108:W1:A10:S28→Xi108:W3:A10:S28→Xi108:W2:A9:S28→Xi108:W2:A11:S28

"""Spectral-Geometric Duality Module - Platonic shells, nodal surfaces."""

from atlasforge.spectral_geometry.spectral_geometry import (
    PlatonicSolid,
    PlatonicShell,
    SphericalHarmonic,
    SphericalHarmonicExpansion,
    NodalDomain,
    NodalAnalysis,
    SpectralGeometry,
    SpectralGeometricTranslator,
    platonic_spectrum,
    spherical_harmonic,
    spectral_embedding,
    heat_kernel_trace,
)

__all__ = [
    'PlatonicSolid',
    'PlatonicShell',
    'SphericalHarmonic',
    'SphericalHarmonicExpansion',
    'NodalDomain',
    'NodalAnalysis',
    'SpectralGeometry',
    'SpectralGeometricTranslator',
    'platonic_spectrum',
    'spherical_harmonic',
    'spectral_embedding',
    'heat_kernel_trace',
]
