from scipy import integrate


def x(t):
    value = 0.0
    if (t >= 0.0 and t < 0.5):
        value = 1.0
    if (t >= 0.5 and t < 1.0):
        value = -1.0
    return value


def y(t):
    return 1.0 if (t >= 0 and t < 1.0) else 0.0


def W(n, k, t):
    if (n == 0 and k == 0):
        return y(t)
    return 2**(0.5 * n) * x(2**n * t - k + 1) * y(2**n * t - k + 1)


def haarCoefficients(f, N):
    c = [[]]
    c[0].append(integrate.quad(lambda t: f(t), 0.0, 1.0)[0])
    c[0].append(integrate.quad(lambda t: f(t) * W(0, 1, t), 0.0, 1.0)[0])
    for n in range(1, N + 1):
        c.append([0.0])
        for k in range(1, 2**n + 1):
            c[n].append(integrate.quad(lambda t: f(t) * W(n, k, t), (k-1) / 2**n, k / 2**n)[0])
    return c


def haarApproximation(f, N):
    c = haarCoefficients(f, N)

    def approximation(t):
        value = 0.0
        value += c[0][0] * W(0, 0, t)
        value += c[0][1] * W(0, 1, t)
        for n in range(1, N + 1):
            for k in range(1, 2**n + 1):
                value += c[n][k] * W(n, k, t)
        return value
    return approximation
