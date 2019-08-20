import matplotlib.pyplot as plt
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
            c[n].append(integrate.quad(lambda t: f(t) * W(n, k, t), (k-1) / 2**n, k / 2**n)[0])  # /
            # integrate.quad(lambda t: W(n, k, t) * W(n, k, t), (k-1) / 2**n, k / 2**n)[0]
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


def function(t):
    return 2 + (1 + t) * (1 - t) * t * (t - 1.0 / 3.0) * (t - 4.0 / 5.0)


p = 10000
N = 4
xArray = [i / p for i in range(1, p)]
yArray = [function(x) for x in xArray]
plt.plot(xArray, yArray, ls="-", lw=0.5, color="g", ms=5)
approximation = haarApproximation(function, N)
yArray = [approximation(x) for x in xArray]
plt.plot(xArray, yArray, ls="-", lw=0.5, color="r", ms=5)
plt.legend(["Orginal function", "Haar approximation"], bbox_to_anchor=(0.5, -0.15), loc="lower center", ncol=3)
plt.show()
