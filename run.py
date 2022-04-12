"""The module runs the whole approximation process."""

from argparse import ArgumentParser
from pathlib import Path
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


def parse_args() -> Tuple[int, int, Path, ApproximationMethod]:
    """Function, which parses command line arguments.

    Returns:
        Tuple[Path, str, int, ApproximationMethod, int]: Output directory path, output file name without extension, number of probes used \
for plots on [a, b] interval, approximation method, order of approximation.
    """
    parser = ArgumentParser()
    parser.add_argument("-o", "--output-dir", type=Path, required=True, help="Output directory path.")
    parser.add_argument("-f", "--output-file-name", type=str, default="approximation", help="Output file name without extension.")
    parser.add_argument("-p", "--probes", type=int, default=1000, help="Number of probes for plot.")
    parser.add_argument(
        "-m",
        "--method",
        type=str,
        required=True,
        choices=[
            method.value for method in ApproximationMethod],
        help="Approximation method.")
    parser.add_argument("-n", "--order", type=int, default=4, help="Order of approximation.")
    args = parser.parse_args()
    args.output_dir.mkdir(exist_ok=True, parents=True)
    return args.output_dir, args.output_file_name, args.probes, ApproximationMethod(args.method), args.order


def function(time: float) -> float:
    """Simple real domain real value function.

    Args:
        time (float): Input float value.

    Returns:
        float: Function value on time argument.
    """
    return 2 + np.exp(time) * (1 + time) * (1 - time) * time * (time - 1.0 / 3.0) * (time - 4.0 / 5.0)


approximation_methods = {
    ApproximationMethod.CHEBYSHEV: chebyshevApproximation,
    ApproximationMethod.HAAR: haarApproximation,
    ApproximationMethod.LEGENDRE: legendreApproximation,
    ApproximationMethod.TRIGONOMETRIC: trigonometricApproximation,
}


if __name__ == "__main__":
    output_dir, output_file_name, probes, method, order = parse_args()
    approximationMethod = approximation_methods[method]
    approximation = approximationMethod(function, order)
    plot(output_dir, output_file_name, probes, order, method.value, function, approximation, 0.0, 1.0)
