import matplotlib.pyplot as plt

from pathlib import Path

from typing import Callable


def plot(outputPath: Path, probes: int, order: int, name:str, function: Callable[[float], float], approximation: Callable[[float], float], a:float, b:float) -> None:
    """Function to plot orginal function and it's approximation.

    Args:
        outputPath (Path): Directory where function saves approximation.png.
        probes (int): Number of probes used in [a, b] interval.
        order (int): Order of approximation method, used only for title.
        name (str): Name of approximation method, used only for title.
        function (Callable[[float], float]): Original function.
        approximation (Callable[[float], float]): Approximation function.
        a (float): Left end of approximation interval.
        b (float): Right end of approximation interval.
    """
    plt.clf()
    plt.title(name + " approximation of " + repr(order) + " order")
    xArray = [a + (b - a) * i / probes for i in range(1, probes)]
    yArray = [function(x) for x in xArray]
    plt.plot(xArray, yArray, ls="-", lw=0.5, color="g", ms=5)
    yArray = [approximation(x) for x in xArray]
    plt.plot(xArray, yArray, ls="-", lw=0.5, color="r", ms=5)
    plt.legend(["Original function", name + " approximation"], bbox_to_anchor=(0.5, -0.1), loc="lower center", ncol=3)
    plt.tight_layout(rect=[0, 0, 1, 1])
    plt.gcf().set_size_inches(12, 9)
    plt.savefig(outputPath + "\\approximation.png", dpi=100)
