# CRYSTAL: Xi108:W2:A6:S18 | face=S | node=159 | depth=2 | phase=Cardinal
# METRO: Me
# BRIDGES: Xi108:W2:A6:S17→Xi108:W2:A6:S19→Xi108:W1:A6:S18→Xi108:W3:A6:S18→Xi108:W2:A5:S18→Xi108:W2:A7:S18

"""Categorical Translation Module - SKF functor, boundary realization."""

from atlasforge.categorical.categorical import (
    CategoryError,
    CategoricalObject,
    Morphism,
    BoundaryObject,
    BoundaryMorphism,
    HybridObject,
    HybridMorphism,
    SKFFunctor,
    NaturalTransformation,
    KernelPreservingCategory,
    TranslationPipeline,
    create_boundary_object,
    create_skf_functor,
    translate_to_hybrid,
    verify_kernel_preservation,
)

__all__ = [
    'CategoryError',
    'CategoricalObject',
    'Morphism',
    'BoundaryObject',
    'BoundaryMorphism',
    'HybridObject',
    'HybridMorphism',
    'SKFFunctor',
    'NaturalTransformation',
    'KernelPreservingCategory',
    'TranslationPipeline',
    'create_boundary_object',
    'create_skf_functor',
    'translate_to_hybrid',
    'verify_kernel_preservation',
]
