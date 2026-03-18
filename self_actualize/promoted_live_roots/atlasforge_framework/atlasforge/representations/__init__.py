# CRYSTAL: Xi108:W2:A4:S27 | face=F | node=363 | depth=2 | phase=Mutable
# METRO: Me,✶
# BRIDGES: Xi108:W2:A4:S26→Xi108:W2:A4:S28→Xi108:W1:A4:S27→Xi108:W3:A4:S27→Xi108:W2:A3:S27→Xi108:W2:A5:S27

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
