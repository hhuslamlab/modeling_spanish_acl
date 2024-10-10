### adds memorization/generalization to combine.csv of all conditions (seperately)
import pandas as pd


if __name__ == "__main__":
    conditions = ["10L_90NL", "50L_50NL", "90L_10NL"]

    for cond in conditions:
        data = pd.read_csv(
            "/home/akhilesh/personal/hmall_acl/data/fixed_run/analysis/memorization_generalization/nl_shape/unattested_dataframes/"
            + cond
            + "/combine.csv"
        )
        data["memgen"] = "gen"

        data.to_csv(
            "/home/akhilesh/personal/hmall_acl/data/fixed_run/analysis/memorization_generalization/nl_shape/unattested_dataframes/"
            + cond
            + "/combine.csv",
            index=False,
        )
