import sys, os
import pandas as pd

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from config import all_models


if __name__ == "__main__":
    df = pd.DataFrame()

    for model in all_models:
        model_df = pd.read_csv("../../data/fixed_run/analysis/stems/" + model + ".csv")
        predictions = model_df["preds_stems"].tolist()
        test_data = model_df["test_stems"].tolist()
        shapes = model_df["shapes"].tolist()

        lshape_count = 0
        nlshape_count = 0

        all_lshape_count = len([item for item in shapes if item == "L"])
        all_nlshape_count = len([item for item in shapes if item == "NL"])

        for pred, test, shape in zip(predictions, test_data, shapes):
            if pred == test:
                if shape == "L":
                    lshape_count += 1
                if shape == "NL":
                    nlshape_count += 1
        l_acc = lshape_count / all_lshape_count * 100
        nl_acc = nlshape_count / all_nlshape_count * 100

        df = pd.DataFrame()
        df["filename"] = [model]
        df["l_acc"] = [l_acc]
        df["nl_acc"] = [nl_acc]

        df.to_csv(
            "../../data/fixed_run/analysis/stem_accuracies/" + model + ".csv",
            index=False,
        )
