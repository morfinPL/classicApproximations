import os.path
from argparse import ArgumentParser
from json import dump

import numpy as np

from chebyshev import chebyshevApproximation
from haar import haarApproximation
from legendre import legendreApproximation
from trigonometric import trigonometricApproximation
from utils import plot
from typing import Callable

def parseArguments():
    parser = ArgumentParser()
    parser.add_argument("-p", "--probes", dest="probes", default=1000, help="Number of probes for plot.")
    parser.add_argument("-n", "--order", dest="order", help="Order of approximation.", default=4)
    parser.add_argument("-o", "--outputPath", dest="outputPath", required=True, help="Output directory for experiment.")
    parser.add_argument("-m", "--method", dest="method", choices=["Haar", "Trigonometric", "Legendre", "Chebyshev"],
                        help="Approximation method.", default="Haar")
    args = parser.parse_args()
    if (args.method != "Trigonometric" and args.method != "Legendre" and args.method != "Chebyshev"):
        args.method = "Haar"
    if not os.path.exists(args.outputPath):
        os.makedirs(args.outputPath)
    with open(args.outputPath + "\\config.json", "w") as configFile:
        dump(vars(args), configFile, indent=4)
    return int(args.probes), int(args.order), args.outputPath, args.method


def parseMethod(method: str) -> Callable[[Callable[[float], float], int], Callable[[float], float]]:
    """Parse approximation method name to approximation object.

    Args:
        method (str): Approximation method name.

    Raises:
        ValueError: When you pass wrong method name.

    Returns:
        Callable[[Callable[[float], float], int], Callable[[float], float]]: Approximation callable object, which returns approximation after call with original function object and order.
    """
    if(method == "Haar"):
        return haarApproximation
    if(method == "Trigonometric"):
        return trigonometricApproximation
    if(method == "Legendre"):
        return legendreApproximation
    if(method == "Chebyshev"):
        return chebyshevApproximation
    raise ValueError(f"Wrong approximation method name: {method}!")


def function(t):
    return 2 + np.exp(t) * (1 + t) * (1 - t) * t * (t - 1.0 / 3.0) * (t - 4.0 / 5.0)

if __name__ == "__main__":
    probes, order, outputPath, method = parseArguments()
    approximationMethod = parseMethod(method)
    approximation = approximationMethod(function, order)
    plot(outputPath, probes, order, method, function, approximation, 0.0, 1.0)
