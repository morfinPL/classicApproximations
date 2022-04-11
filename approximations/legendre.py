from typing import Callable, List

import scipy as sp


def W(n:int, t:float):
    value = 0.0
    for k in range(n+1):
        value += sp.special.binom(n, k) * sp.special.binom((n+k-1)*0.5, n) * (2 * t - 1)**k
    return value * 2**n


def legendreCoefficients(f:Callable[[float], float], N: int) -> List[float]:
    c = []
    for i in range(N+1):
        c.append(sp.integrate.quad(lambda t: f(t) * W(i, t), 0.0, 1.0)[0] /
                 sp.integrate.quad(lambda t: W(i, t) * W(i, t), 0.0, 1.0)[0])
    return c


def legendreApproximation(f: Callable[[float], float], N: int) -> Callable[[float], float]:
    c = legendreCoefficients(f, N)

    def approximation(t:float) -> float:
        value = 0.0
        for i in range(N+1):
            value += c[i] * W(i, t)
        return value
    return approximation
