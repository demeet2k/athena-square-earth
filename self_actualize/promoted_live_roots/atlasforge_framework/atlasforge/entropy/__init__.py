# CRYSTAL: Xi108:W2:A1:S25 | face=F | node=307 | depth=2 | phase=Mutable
# METRO: Me
# BRIDGES: Xi108:W2:A1:S24→Xi108:W2:A1:S26→Xi108:W1:A1:S25→Xi108:W3:A1:S25→Xi108:W2:A2:S25

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
