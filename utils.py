import matplotlib.pyplot as plt


def plot(outputPath, probes, order, name, function, approximation, a, b):
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
