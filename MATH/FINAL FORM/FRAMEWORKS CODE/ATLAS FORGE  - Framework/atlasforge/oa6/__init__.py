# CRYSTAL: Xi108:W2:A1:S14 | face=S | node=103 | depth=2 | phase=Cardinal
# METRO: Me,w
# BRIDGES: Xi108:W2:A1:S13→Xi108:W2:A1:S15→Xi108:W1:A1:S14→Xi108:W3:A1:S14→Xi108:W2:A2:S14

"""OA6 Operator Word Algebra Module - Six generators, normal forms, kernel transport."""

from atlasforge.oa6.oa6 import (
    OA6GeneratorType,
    FoldIndex,
    OA6Generator,
    ComplementGenerator,
    RotationGenerator,
    GatewayGenerator,
    KernelProjector,
    DilationGenerator,
    TemperleyLiebGenerator,
    IdentityGenerator,
    OA6Word,
    ModularNormalForm,
    KernelEffectTable,
    OA6Algebra,
    create_oa6_algebra,
    modular_normal_form,
    kernel_effect_summary,
)

__all__ = [
    'OA6GeneratorType',
    'FoldIndex',
    'OA6Generator',
    'ComplementGenerator',
    'RotationGenerator',
    'GatewayGenerator',
    'KernelProjector',
    'DilationGenerator',
    'TemperleyLiebGenerator',
    'IdentityGenerator',
    'OA6Word',
    'ModularNormalForm',
    'KernelEffectTable',
    'OA6Algebra',
    'create_oa6_algebra',
    'modular_normal_form',
    'kernel_effect_summary',
]
