# CRYSTAL: Xi108:W2:A2:S14 | face=S | node=97 | depth=2 | phase=Cardinal
# METRO: Me
# BRIDGES: Xi108:W2:A2:S13→Xi108:W2:A2:S15→Xi108:W1:A2:S14→Xi108:W3:A2:S14→Xi108:W2:A1:S14→Xi108:W2:A3:S14

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
