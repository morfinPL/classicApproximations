import numpy as np
from scipy import integrate
from typing import Callable, List

def A(n: int, t: float) -> float:
    return np.cos(n * 2 * np.pi * t)


def B(n: int, t: float) -> float:
    return np.sin(n * 2 * np.pi * t)


def trigonometricCoefficients(f:Callable[[float], float], N: int) ->List[List[float]]:
    c = [[], []]
    c[0].append(integrate.quad(f, 0.0, 1.0)[0])
    c[1].append(0.0)
    for i in range(1, N+1):
        c[0].append(2 * integrate.quad(lambda t: f(t) * A(i, t), 0.0, 1.0)[0])
        c[1].append(2 * integrate.quad(lambda t: f(t) * B(i, t), 0.0, 1.0)[0])
    return c


def trigonometricApproximation(f: Callable[[float], float], N: int) -> Callable[[float], float]:
    c = trigonometricCoefficients(f, N)

    def approximation(t:float) -> float:
        value = 0.0
        for i in range(N+1):
            value += c[0][i] * A(i, t)
            value += c[1][i] * B(i, t)
        return value
    return approximation
