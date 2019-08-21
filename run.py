import os.path
from argparse import ArgumentParser
from json import dump

import numpy as np

from haar import haarApproximation
from legendre import legendreApproximation
from trigonometric import trigonometricApproximation
from utils import plot


def parseArguments():
    parser = ArgumentParser()
    parser.add_argument("-p", "--probes", dest="probes", default=1000, help="Number of probes for plot.")
    parser.add_argument("-n", "--order", dest="order", help="Order of approximation.", default=4)
    parser.add_argument("-o", "--outputPath", dest="outputPath", required=True, help="Output directory for experiment.")
    parser.add_argument("-m", "--method", dest="method",
                        help="Approximation method [Haar - default | Trigonometric | Legendre].", default="Haar")
    args = parser.parse_args()
    if (args.method != "Trigonometric" and args.method != "Legendre"):
        args.method = "Haar"
    if not os.path.exists(args.outputPath):
        os.makedirs(args.outputPath)
    with open(args.outputPath + "\\config.json", "w") as configFile:
        dump(vars(args), configFile, indent=4)
    return int(args.probes), int(args.order), args.outputPath, args.method


def function(t):
    return 2 + np.exp(t) * (1 + t) * (1 - t) * t * (t - 1.0 / 3.0) * (t - 4.0 / 5.0)


probes, order, outputPath, method = parseArguments()
approximationMethod = legendreApproximation if method == "Legendre" else (
    trigonometricApproximation if method == "Trigonometric" else haarApproximation)
approximation = approximationMethod(function, order)
plot(outputPath, probes, order, method, function, approximation, 0.0, 1.0)
