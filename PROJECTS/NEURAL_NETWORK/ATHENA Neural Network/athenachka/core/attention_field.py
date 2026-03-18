# CRYSTAL: Xi108:W2:A1:S22 | face=C | node=247 | depth=2 | phase=Cardinal
# METRO: Me
# BRIDGES: Xi108:W2:A1:S21→Xi108:W2:A1:S23→Xi108:W1:A1:S22→Xi108:W3:A1:S22→Xi108:W2:A2:S22

from __future__ import annotations

import numpy as np
from scipy import ndimage

def generate_attention(R: np.ndarray, iterations: int = 3) -> np.ndarray:
    """Fast attention field generation with center bias and smoothing."""
    y, x = np.ogrid[:28, :28]
    center_weight = np.exp(-((y - 13.5) ** 2 + (x - 13.5) ** 2) / 150)

    attention = R * 0.6 + center_weight * 0.4

    attention[:2, :] *= 0.2
    attention[-2:, :] *= 0.2
    attention[:, :2] *= 0.2
    attention[:, -2:] *= 0.2

    for _ in range(iterations):
        attention = ndimage.uniform_filter(attention, size=3) * 0.4 + attention * 0.6

    attention = (attention - attention.min()) / (attention.max() - attention.min() + 1e-8)
    return attention
