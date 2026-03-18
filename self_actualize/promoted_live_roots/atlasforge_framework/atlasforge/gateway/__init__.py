# CRYSTAL: Xi108:W2:A9:S27 | face=F | node=372 | depth=2 | phase=Mutable
# METRO: Me
# BRIDGES: Xi108:W2:A9:S26→Xi108:W2:A9:S28→Xi108:W1:A9:S27→Xi108:W3:A9:S27→Xi108:W2:A8:S27→Xi108:W2:A10:S27

"""Gateway Algebra Module - Pell equations, Möbius boosts, hyperbolic navigation."""

from atlasforge.gateway.gateway import (
    GatewayScalar,
    BoostMatrix,
    PellSolution,
    PellGateway,
    FoldLadder,
    GatewayAlgebra,
    SpecialGateways,
    solve_pell_fundamental,
    gateway_from_angle,
    gateway_angle,
    hyperbolic_distance,
    create_gateway_algebra,
    pell_orbit,
    velocity_addition,
    rapidity_from_velocity,
    velocity_from_rapidity,
    transmission_coefficient,
)

__all__ = [
    'GatewayScalar',
    'BoostMatrix',
    'PellSolution',
    'PellGateway',
    'FoldLadder',
    'GatewayAlgebra',
    'SpecialGateways',
    'solve_pell_fundamental',
    'gateway_from_angle',
    'gateway_angle',
    'hyperbolic_distance',
    'create_gateway_algebra',
    'pell_orbit',
    'velocity_addition',
    'rapidity_from_velocity',
    'velocity_from_rapidity',
    'transmission_coefficient',
]
