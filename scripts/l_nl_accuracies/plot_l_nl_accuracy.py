"""
plot L and NL accuracies
"""
import tikzplotlib
import pandas as pd
import matplotlib.pyplot as plt
import statistics
from math import sqrt
from config import condition_10L_90NL, condition_50L_50NL, condition_90L_10NL


def plot_confidence_interval(
    x, values, point_color, label, z=1.96, color="#2187bb", horizontal_line_width=0.25
):
    mean = statistics.mean(values)
    stdev = statistics.stdev(values)
    confidence_interval = z * stdev / sqrt(len(values))
    print(confidence_interval)
    left = x - horizontal_line_width / 2
    top = mean - confidence_interval
    right = x + horizontal_line_width / 2
    bottom = mean + confidence_interval
    plt.plot([x, x], [top, bottom], color=color)
    plt.plot([left, right], [top, top], color=color)
    plt.plot([left, right], [bottom, bottom], color=color)
    plt.plot(x, mean, "o", color=point_color, label=label)

    return mean, confidence_interval


def final(filename):
    data = pd.read_csv(
        "../../data/fixed_run/analysis/l_nl_accuracies/" + filename + ".csv"
    )
    return {
        "l_acc": round(data["l_acc"].tolist()[0]),
        "nl_acc": round(data["nl_acc"].tolist()[0]),
    }


if __name__ == "__main__":
    res_10L_90NL = [final(item) for item in condition_10L_90NL]

    res_50L_50NL = [final(item) for item in condition_50L_50NL]

    res_90L_10NL = [final(item) for item in condition_90L_10NL]

    l_acc_10L_90NL = [item["l_acc"] for item in res_10L_90NL]
    l_acc_50L_50NL = [item["l_acc"] for item in res_50L_50NL]
    l_acc_90L_10NL = [item["l_acc"] for item in res_90L_10NL]

    nl_acc_10L_90NL = [item["nl_acc"] for item in res_10L_90NL]

    print(statistics.mean(nl_acc_10L_90NL))
    nl_acc_50L_50NL = [item["nl_acc"] for item in res_50L_50NL]
    print(statistics.mean(nl_acc_50L_50NL))
    nl_acc_90L_10NL = [item["nl_acc"] for item in res_90L_10NL]

    print(statistics.mean(nl_acc_90L_10NL))

    plt.title("")
    plot_confidence_interval(1, l_acc_10L_90NL, "#FFA500", "L-shape")
    plot_confidence_interval(1, nl_acc_10L_90NL, "#808080", "NL-shape")
    plot_confidence_interval(2, l_acc_50L_50NL, "#FFA500", "")
    plot_confidence_interval(2, nl_acc_50L_50NL, "#808080", "")
    plot_confidence_interval(3, l_acc_90L_10NL, "#FFA500", "")
    plot_confidence_interval(3, nl_acc_90L_10NL, "#808080", "")
    barWidth = 1

    plt.xticks(
        [r + barWidth for r in range(3)], ["10%L-90%NL", "50%L-50%NL", "90%L-10%NL"]
    )
    plt.ylabel("Accuracy (in %)")
    # plt.xlabel('Condition (L%-NL%)')
    plt.ylim(bottom=0)
    # plt.legend(('L-shape', 'NL-shape'))
    plt.title("")
    tikzplotlib.save(
        "../../data/fixed_run/analysis/plots/l_vs_nl_accuracy_without_stress.tex"
    )
