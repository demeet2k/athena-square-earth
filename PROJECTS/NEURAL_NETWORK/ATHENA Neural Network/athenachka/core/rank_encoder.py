# CRYSTAL: Xi108:W2:A1:S19 | face=C | node=183 | depth=2 | phase=Cardinal
# METRO: Me
# BRIDGES: Xi108:W2:A1:S18→Xi108:W2:A1:S20→Xi108:W1:A1:S19→Xi108:W3:A1:S19→Xi108:W2:A2:S19

from __future__ import annotations

import numpy as np
from scipy import ndimage

def rank_transform(img: np.ndarray) -> np.ndarray:
    """Convert intensity to ordinal rank values."""
    flat = img.flatten()
    ranks = np.zeros_like(flat)
    sorted_idx = np.argsort(flat)
    ranks[sorted_idx] = np.linspace(0, 1, len(flat))
    return ranks.reshape(img.shape)

def compute_gradients(img: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Sobel gradients used throughout the kernel."""
    gy = ndimage.sobel(img, axis=0)
    gx = ndimage.sobel(img, axis=1)
    mag = np.sqrt(gx**2 + gy**2)
    angle = np.arctan2(gy, gx)
    return mag, angle
