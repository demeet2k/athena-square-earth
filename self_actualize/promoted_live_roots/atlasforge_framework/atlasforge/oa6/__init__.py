# CRYSTAL: Xi108:W2:A1:S25 | face=F | node=308 | depth=2 | phase=Mutable
# METRO: Me,w
# BRIDGES: Xi108:W2:A1:S24→Xi108:W2:A1:S26→Xi108:W1:A1:S25→Xi108:W3:A1:S25→Xi108:W2:A2:S25

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
