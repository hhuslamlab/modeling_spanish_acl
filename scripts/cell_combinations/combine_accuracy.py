"""
combine accuracies

Usage:
    combine_accuracy.py --condition=<c>

Options:
    --condition=<c>`    Specify the condition (e.g: 10L_90NL or 50L_50NL or 90L_10NL)
"""
from docopt import docopt
import pandas as pd
import statistics
from config import condition_10L_90NL, condition_50L_50NL, condition_90L_10NL


if __name__ == "__main__":
    args = docopt(__doc__)
    input_condition = args["--condition"]

    df = pd.read_csv("../../data/fixed_run/analysis/cell_combinations/combine.csv")

    cond_df = df.loc[df.filename.str.contains(input_condition)]

    mean_df = pd.DataFrame()

    mean_in_in_in_L = round(cond_df["acc_in_in_in_L"].mean(), 2)
    mean_in_in_in_NL = round(cond_df["acc_in_in_in_NL"].mean(), 2)
    mean_in_in_in_ratio = round(cond_df["acc_in_in_in_ratio"].mean(), 2)

    mean_in_out_out_L = round(cond_df["acc_in_out_out_L"].mean(), 2)
    mean_in_out_out_NL = round(cond_df["acc_in_out_out_NL"].mean(), 2)
    mean_in_out_out_ratio = round(cond_df["acc_in_out_out_ratio"].mean(), 2)

    mean_in_in_out_L = round(cond_df["acc_in_in_out_L"].mean(), 2)
    mean_in_in_out_NL = round(cond_df["acc_in_in_out_NL"].mean(), 2)
    mean_in_in_out_ratio = round(cond_df["acc_in_in_out_ratio"].mean(), 2)

    mean_in_out_in_L = round(cond_df["acc_in_out_in_L"].mean(), 2)
    mean_in_out_in_NL = round(cond_df["acc_in_out_in_NL"].mean(), 2)
    mean_in_out_in_ratio = round(cond_df["acc_in_out_in_ratio"].mean(), 2)

    mean_out_in_in_L = round(cond_df["acc_out_in_in_L"].mean(), 2)
    mean_out_in_in_NL = round(cond_df["acc_out_in_in_NL"].mean(), 2)
    mean_out_in_in_ratio = round(cond_df["acc_out_in_in_ratio"].mean(), 2)

    mean_out_in_out_L = round(cond_df["acc_out_in_out_L"].mean(), 2)
    mean_out_in_out_NL = round(cond_df["acc_out_in_out_NL"].mean(), 2)
    mean_out_in_out_ratio = round(cond_df["acc_out_in_out_ratio"].mean(), 2)

    mean_out_out_in_L = round(cond_df["acc_out_out_in_L"].mean(), 2)
    mean_out_out_in_NL = round(cond_df["acc_out_out_in_NL"].mean(), 2)
    mean_out_out_in_ratio = round(cond_df["acc_out_out_in_ratio"].mean(), 2)

    mean_out_out_out_L = round(cond_df["acc_out_out_out_L"].mean(), 2)
    mean_out_out_out_NL = round(cond_df["acc_out_out_out_NL"].mean(), 2)
    mean_out_out_out_ratio = round(cond_df["acc_out_out_out_ratio"].mean(), 2)

    mean_df["mean_in_in_in_L"] = [mean_in_in_in_L]
    mean_df["mean_in_in_in_NL"] = [mean_in_in_in_NL]
    mean_df["mean_in_in_in_ratio"] = [mean_in_in_in_ratio]

    mean_df["mean_in_out_out_L"] = [mean_in_out_out_L]
    mean_df["mean_in_out_out_NL"] = [mean_in_out_out_NL]
    mean_df["mean_in_out_out_ratio"] = [mean_in_out_out_ratio]

    mean_df["mean_in_in_out_L"] = [mean_in_in_out_L]
    mean_df["mean_in_in_out_NL"] = [mean_in_in_out_NL]
    mean_df["mean_in_in_out_ratio"] = [mean_in_in_out_ratio]

    mean_df["mean_in_out_in_L"] = [mean_in_out_in_L]
    mean_df["mean_in_out_in_NL"] = [mean_in_out_in_NL]
    mean_df["mean_in_out_in_ratio"] = [mean_in_out_in_ratio]

    mean_df["mean_out_in_in_L"] = [mean_out_in_in_L]
    mean_df["mean_out_in_in_NL"] = [mean_out_in_in_NL]
    mean_df["mean_out_in_in_ratio"] = [mean_out_in_in_ratio]

    mean_df["mean_out_in_out_L"] = [mean_out_in_out_L]
    mean_df["mean_out_in_out_NL"] = [mean_out_in_out_NL]
    mean_df["mean_out_in_out_ratio"] = [mean_out_in_out_ratio]

    mean_df["mean_out_out_in_L"] = [mean_out_out_in_L]
    mean_df["mean_out_out_in_NL"] = [mean_out_out_in_NL]
    mean_df["mean_out_out_in_ratio"] = [mean_out_out_in_ratio]

    mean_df["mean_out_out_out_L"] = [mean_out_out_out_L]
    mean_df["mean_out_out_out_NL"] = [mean_out_out_out_NL]
    mean_df["mean_out_out_out_ratio"] = [mean_out_out_out_ratio]

    mean_df.to_csv(
        "../../data/fixed_run/analysis/cell_combinations/mean_accuracies/"
        + input_condition
        + ".csv",
        index=False,
    )
