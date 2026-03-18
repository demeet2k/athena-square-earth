# CRYSTAL: Xi108:W2:A4:S15 | face=S | node=120 | depth=2 | phase=Cardinal
# METRO: Me,✶
# BRIDGES: Xi108:W2:A4:S14→Xi108:W2:A4:S16→Xi108:W1:A4:S15→Xi108:W3:A4:S15→Xi108:W2:A3:S15→Xi108:W2:A5:S15

"""Representation Routing Module (Square/Flower/Cloud/Fractal)."""
from .representations import (
    Representation,
    SquareState,
    FlowerState,
    CloudState,
    FractalState,
    RepresentationTransform,
    SquareToFlower,
    FlowerToCloud,
    CloudToFractal,
    FractalToSquare,
    RepresentationRouter,
    route_through_flower,
    route_through_cloud,
    optimal_representation_for_task,
)

__all__ = [
    'Representation',
    'SquareState',
    'FlowerState',
    'CloudState',
    'FractalState',
    'RepresentationTransform',
    'SquareToFlower',
    'FlowerToCloud',
    'CloudToFractal',
    'FractalToSquare',
    'RepresentationRouter',
    'route_through_flower',
    'route_through_cloud',
    'optimal_representation_for_task',
]
