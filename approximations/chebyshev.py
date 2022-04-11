import numpy as np
from typing import Callable, List


def W(n: int, t: float) -> float:
    t = 2 * t - 1
    return np.cos(n * np.arccos(t))


def chebyshevCoefficients(f: Callable[[float], float], N: int) -> List[float]:
    c = []
    for j in range(N):
        c.append(0.0)
        for k in range(1, N+1):
            xk = 0.5 * np.cos(np.pi * (k - 0.5) / N) + 0.5
            c[j] += f(xk) * W(j, xk)
        c[j] *= 2 / N
    c[0] /= 2
    return c


def chebyshevApproximation(f: Callable[[float], float], N: int) -> Callable[[float], float]:
    c = chebyshevCoefficients(f, N)

    def approximation(t: float) -> float:
        value = 0.0
        for i in range(N):
            value += c[i] * W(i, t)
        return value
    return approximation
