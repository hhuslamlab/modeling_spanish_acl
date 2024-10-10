"""
plotting

Usage:
    plot.py --condition=<c>

Options:
    --condition=<c>`    Specify the condition (e.g: 10L_90NL or 50L_50NL or 90L_10NL)
"""
from docopt import docopt
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import numpy as np
import tikzplotlib


def select_columns(df, col_names):
    new_df = df.loc[:, col_names]
    return new_df


if __name__ == "__main__":
    args = docopt(__doc__)
    input_condition = args["--condition"]

    df = pd.read_csv(
        "../../data/fixed_run/analysis/cell_combinations/mean_accuracies/"
        + input_condition
        + ".csv"
    )

    l_cols = []
    nl_cols = []

    for col in df.columns:
        if "_L" in col:
            l_cols.append(col)
        if "_NL" in col:
            nl_cols.append(col)

    ldf = select_columns(df, l_cols)
    ldf = ldf.replace(-1.0, 0.0)
    nldf = select_columns(df, nl_cols)

    nldf = nldf.replace(-1.0, 0.0)
    ldf_values = ldf.values[0]
    nldf_values = nldf.values[0]

    figure(figsize=(8, 6), dpi=80)

    x = np.arange(len(ldf_values))
    y1 = ldf_values
    y2 = nldf_values
    width = 0.25

    plt.bar(x - 0.25, ldf_values, width, color="#FFA500")
    plt.bar(x, nldf_values, width, color="#808080")
    # plt.bar(x+0.2, y3, width, color='green')
    plt.xticks(
        x,
        [
            "In-In-In",
            "In-Out-Out",
            "In-In-Out",
            "In-Out-In",
            "Out-In-In",
            "Out-In-Out",
            "Out-Out-In",
            "Out-Out-Out",
        ],
    )
    plt.xticks(fontsize=9)
    plt.xlabel("Cell combinations")
    plt.ylabel("Accuracy (in %)")
    plt.legend(["L-shape", "NL-shape"])
    tikzplotlib.save(
        "../../data/fixed_run/analysis/plots/cell_combination_"
        + input_condition
        + ".tex"
    )
