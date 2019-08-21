import os.path
from argparse import ArgumentParser
from json import dump

from haar import haarApproximation
from utils import plot


def parseArguments():
    parser = ArgumentParser()
    parser.add_argument("-p", "--probes", dest="probes", default=1000, help="Number of probes for plot.")
    parser.add_argument("-n", "--order", dest="order", help="Order of approximation.", default=4)
    parser.add_argument("-o", "--outputPath", dest="outputPath", required=True, help="Output directory for experiment.")
    args = parser.parse_args()
    if not os.path.exists(args.outputPath):
        os.makedirs(args.outputPath)
    with open(args.outputPath + "\\config.json", "w") as configFile:
        dump(vars(args), configFile, indent=4)
    return int(args.probes), int(args.order), args.outputPath


def function(t):
    return 2 + (1 + t) * (1 - t) * t * (t - 1.0 / 3.0) * (t - 4.0 / 5.0)


probes, order, outputPath = parseArguments()
approximation = haarApproximation(function, order)
plot(outputPath, probes, order, "Haar", function, approximation)
