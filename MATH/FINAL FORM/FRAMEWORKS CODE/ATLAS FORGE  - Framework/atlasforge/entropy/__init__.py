# CRYSTAL: Xi108:W2:A4:S16 | face=S | node=128 | depth=2 | phase=Cardinal
# METRO: Me
# BRIDGES: Xi108:W2:A4:S15→Xi108:W2:A4:S17→Xi108:W1:A4:S16→Xi108:W3:A4:S16→Xi108:W2:A3:S16→Xi108:W2:A5:S16

"""Entropy and Information Geometry Module - Σ-pole realization."""

from atlasforge.entropy.entropy import (
    EntropyFunctional,
    FisherInformation,
    ProbabilitySimplex,
    FisherRaoMetric,
    SigmaPoleConnector,
    shannon_entropy,
    kl_divergence,
    js_divergence,
    fisher_rao_distance,
    hellinger_distance,
    mutual_information,
    maximum_entropy,
)

__all__ = [
    'EntropyFunctional',
    'FisherInformation',
    'ProbabilitySimplex',
    'FisherRaoMetric',
    'SigmaPoleConnector',
    'shannon_entropy',
    'kl_divergence',
    'js_divergence',
    'fisher_rao_distance',
    'hellinger_distance',
    'mutual_information',
    'maximum_entropy',
]
