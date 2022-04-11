import os.path
from argparse import ArgumentParser
from json import dump
from typing import Tuple

import numpy as np

from approximations import (
    ApproximationMethod,
    chebyshevApproximation,
    haarApproximation,
    legendreApproximation,
    trigonometricApproximation,
)
from utils import plot


def parseArguments() -> Tuple[int, int, str, ApproximationMethod]:
    parser = ArgumentParser()
    parser.add_argument("-p", "--probes", type=int, default=1000, help="Number of probes for plot.")
    parser.add_argument("-n", "--order", type=int, default=4, help="Order of approximation.")
    parser.add_argument("-o", "--output_path", required=True, help="Output directory for experiment.")
    parser.add_argument(
        "-m",
        "--method",
        type=str,
        required=True,
        choices=[
            method.value for method in ApproximationMethod],
        help="Approximation method.")
    args = parser.parse_args()
    if not os.path.exists(args.output_path):
        os.makedirs(args.output_path)
    with open(args.output_path + "\\config.json", "w") as config_file:
        dump(vars(args), config_file, indent=4)
    return args.probes, args.order, args.output_path, ApproximationMethod(args.method)


def function(t: float) -> float:
    return 2 + np.exp(t) * (1 + t) * (1 - t) * t * (t - 1.0 / 3.0) * (t - 4.0 / 5.0)


approximation_methods = {
    ApproximationMethod.CHEBYSHEV: chebyshevApproximation,
    ApproximationMethod.HAAR: haarApproximation,
    ApproximationMethod.LEGENDRE: legendreApproximation,
    ApproximationMethod.TRIGONOMETRIC: trigonometricApproximation,
}
if __name__ == "__main__":
    probes, order, output_path, method = parseArguments()
    approximationMethod = approximation_methods[method]
    approximation = approximationMethod(function, order)
    plot(output_path, probes, order, method, function, approximation, 0.0, 1.0)
