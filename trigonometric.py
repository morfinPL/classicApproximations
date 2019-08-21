import numpy as np
from scipy import integrate


def A(n, t):
    return np.cos(n * 2 * np.pi * t)


def B(n, t):
    return np.sin(n * 2 * np.pi * t)


def trigonometricCoefficients(f, N):
    c = [[], []]
    c[0].append(integrate.quad(f, 0.0, 1.0)[0])
    c[1].append(0.0)
    for i in range(1, N+1):
        c[0].append(2 * integrate.quad(lambda t: f(t) * A(i, t), 0.0, 1.0)[0])
        c[1].append(2 * integrate.quad(lambda t: f(t) * B(i, t), 0.0, 1.0)[0])
    return c


def trigonometricApproximation(f, N):
    c = trigonometricCoefficients(f, N)

    def approximation(t):
        value = 0.0
        for i in range(N+1):
            value += c[0][i] * A(i, t)
            value += c[1][i] * B(i, t)
        return value
    return approximation
