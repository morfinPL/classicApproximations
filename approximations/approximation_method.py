from enum import Enum


class ApproximationMethod(Enum):
    CHEBYSHEV = "Chebyshev"
    HAAR = "Haar"
    LEGENDRE = "Legendre"
    TRIGONOMETRIC = "Trigonometric"
