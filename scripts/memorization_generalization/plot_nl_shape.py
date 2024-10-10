"""
plot for nl shape
"""
import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from config import condition_10L_90NL, condition_50L_50NL, condition_90L_10NL
import tikzplotlib


def define_box_properties(plot_name, color_code, label):
    for k, v in plot_name.items():
        plt.setp(plot_name.get(k), color=color_code)

    # use plot function to draw a small line to name the legend.
    plt.plot([], c=color_code, label=label)
    plt.legend()


def seen(data: pd.DataFrame) -> int:
    mem = str(data["per_seen_triples_correct"].tolist()[0])
    if mem != "NA":
        return True
    return False


def unseen(data: pd.DataFrame) -> int:
    reg = str(data["per_unseen_triples_correct"].tolist()[0])
    if reg != "NA":
        return True
    return False


if __name__ == "__main__":
    A_mem = []
    A_reg = []
    B_mem = []
    B_reg = []
    C_mem = []
    C_reg = []

    for model in condition_10L_90NL:
        data = pd.read_csv(
            "../../data/fixed_run/analysis/memorization_generalization/nl_shape/"
            + model
            + ".csv"
        )
        mem = data["per_seen_triples_correct"][0]

        if not math.isnan(mem):
            A_mem.append(mem)

        reg = data["per_unseen_triples_correct"][0]

        if not math.isnan(reg):
            A_reg.append(reg)

    A = [A_mem, A_reg]
    print(A)
    for model in condition_50L_50NL:
        data = pd.read_csv(
            "../../data/fixed_run/analysis/memorization_generalization/nl_shape/"
            + model
            + ".csv"
        )
        mem = data["per_seen_triples_correct"][0]

        if not math.isnan(mem):
            B_mem.append(mem)

        reg = data["per_unseen_triples_correct"][0]

        if not math.isnan(reg):
            B_reg.append(reg)

    B = [B_mem, B_reg]

    for model in condition_90L_10NL:
        data = pd.read_csv(
            "../../data/fixed_run/analysis/memorization_generalization/nl_shape/"
            + model
            + ".csv"
        )
        mem = data["per_seen_triples_correct"][0]

        if not math.isnan(mem):
            C_mem.append(mem)

        reg = data["per_unseen_triples_correct"][0]

        if not math.isnan(reg):
            C_reg.append(reg)

    C = [C_mem, C_reg]

    all_mem = [A_mem, B_mem, C_mem]
    all_reg = [A_reg, B_reg, C_reg]

    print(list(zip(A_mem, A_reg)))

    ticks = ["10L-90NL", "50L-50NL", "90L-10NL"]
    mem_plot = plt.boxplot(
        all_mem, positions=np.array(np.arange(len(all_mem))) * 2.0 - 0.35, widths=0.6
    )
    reg_plot = plt.boxplot(
        all_reg, positions=np.array(np.arange(len(all_reg))) * 2.0 + 0.35, widths=0.6
    )

    define_box_properties(mem_plot, "#D7191C", "Memorization")
    define_box_properties(reg_plot, "#2C7BB6", "Generalization")
    # set the x label values
    plt.xticks(np.arange(0, len(ticks) * 2, 2), ticks)

    plt.xlabel("Conditions")
    plt.ylabel("Accuracy (in %)")

    # tikzplotlib.save("../../data/fixed_run/analysis/plots/memgen_nl_shape.tex")
    # plt.savefig("../../data/fixed_run/analysis/plots/memgen_nl_shape.png")
