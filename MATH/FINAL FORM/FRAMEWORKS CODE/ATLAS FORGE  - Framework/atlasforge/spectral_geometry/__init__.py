# CRYSTAL: Xi108:W2:A9:S15 | face=S | node=111 | depth=2 | phase=Cardinal
# METRO: Sa,Me
# BRIDGES: Xi108:W2:A9:S14→Xi108:W2:A9:S16→Xi108:W1:A9:S15→Xi108:W3:A9:S15→Xi108:W2:A8:S15→Xi108:W2:A10:S15

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
