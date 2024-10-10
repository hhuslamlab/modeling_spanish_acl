import matplotlib.pyplot as plt
import statistics
from math import sqrt
import tikzplotlib
import pandas as pd
from config import all_models


def plot_confidence_interval(
    x, values, z=1.96, color="#2187bb", horizontal_line_width=0.25
):
    mean = statistics.mean(values)
    stdev = statistics.stdev(values)
    confidence_interval = z * stdev / sqrt(len(values))

    left = x - horizontal_line_width / 2
    top = mean - confidence_interval
    right = x + horizontal_line_width / 2
    bottom = mean + confidence_interval
    plt.plot([x, x], [top, bottom], color=color)
    plt.plot([left, right], [top, top], color=color)
    plt.plot([left, right], [bottom, bottom], color=color)
    plt.plot(x, mean, "o", color="#f44336")

    return mean, confidence_interval


if __name__ == "__main__":
    df = pd.read_csv("../../data/fixed_run/analysis/accuracies/combine.csv")
    models = df["filename"].tolist()
    accs = df["accuracy"].tolist()
    acc_10L, acc_50L, acc_90L = [], [], []

    for model, acc in zip(models, accs):
        if model.startswith("10L"):
            acc_10L.append(acc)

        if model.startswith("50L"):
            acc_50L.append(acc)

        if model.startswith("90L"):
            acc_90L.append(acc)

    plt.xticks([1, 2, 3], ["10%L-90%NL", "50%L-50%NL", "90%L-10%NL"], color="white")
    plt.ylabel("Accuracy (in %)")
    plot_confidence_interval(1, acc_10L)
    plot_confidence_interval(2, acc_50L)
    plot_confidence_interval(3, acc_90L)
    barWidth = 1

    plt.xticks(
        [r + barWidth for r in range(3)], ["10%L-90%NL", "50%L-50%NL", "90%L-10%NL"]
    )
    plt.ylabel("Accuracy (in %)")
    # plt.xlabel('Condition (L%-NL%)')
    plt.ylim(bottom=0)
    # plt.legend(('L-shape', 'NL-shape'))
    plt.title("")
    tikzplotlib.save("../../data/fixed_run/analysis/plots/overall_accuracy_white.tex")
