import os.path
from argparse import ArgumentParser
from json import dump
from typing import Callable

import numpy as np

from approximations import (
    chebyshevApproximation,
    haarApproximation,
    legendreApproximation,
    trigonometricApproximation,
)
from utils import plot


def parseArguments():
    parser = ArgumentParser()
    parser.add_argument("-p", "--probes", type=int, default=1000, help="Number of probes for plot.")
    parser.add_argument("-n", "--order", type=int, default=4, help="Order of approximation.")
    parser.add_argument("-o", "--output_path", required=True, help="Output directory for experiment.")
    parser.add_argument("-m", "--method", type=str, default="Haar", choices=["Haar", "Trigonometric", "Legendre", "Chebyshev"],
                        help="Approximation method.")
    args = parser.parse_args()
    if not os.path.exists(args.output_path):
        os.makedirs(args.output_path)
    with open(args.output_path + "\\config.json", "w") as configFile:
        dump(vars(args), configFile, indent=4)
    return args.probes, args.order, args.output_path, args.method


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
    probes, order, output_path, method = parseArguments()
    approximationMethod = parseMethod(method)
    approximation = approximationMethod(function, order)
    plot(output_path, probes, order, method, function, approximation, 0.0, 1.0)
