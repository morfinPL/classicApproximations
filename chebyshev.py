import numpy as np
from scipy import integrate


def W(n, t):
    t = 2 * t - 1
    return np.cos(n * np.arccos(t))


def chebyshevCoefficients(f, N):
    c = []
    for j in range(N):
        c.append(0.0)
        for k in range(1, N+1):
            xk = 0.5 * np.cos(np.pi * (k - 0.5) / N) + 0.5
            c[j] += f(xk) * W(j, xk)
        c[j] *= 2 / N
    c[0] /= 2
    return c


def chebyshevApproximation(f, N):
    c = chebyshevCoefficients(f, N)

    def approximation(t):
        value = 0.0
        for i in range(N):
            value += c[i] * W(i, t)
        return value
    return approximation
