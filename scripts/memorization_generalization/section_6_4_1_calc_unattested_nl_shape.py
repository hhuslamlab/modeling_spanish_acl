"""
take the dataframe with incorrect predictions and the seen triples. report numbers. NL-forms

Usage:
    section_6_4_2_unattested_nl_shape.py --condition=<c> --train_triples_set=<tt>

Options:
    --condition=<c>`    Specify the condition (e.g: 10L_90NL or 50L_50NL or 90L_10NL
    --train_triples_set=<tt>    Specify "all" if you want to check against all training triples or just "L" if you want to check it against L-shaped training triples.
"""
from docopt import docopt
import pandas as pd
from config import condition_90L_10NL, condition_50L_50NL, condition_10L_90NL


if __name__ == "__main__":
    args = docopt(__doc__)
    input_condition = args["--condition"]
    train_triples_set = args["--train_triples_set"]

    cond_dict = {
        "10L_90NL": condition_10L_90NL,
        "50L_50NL": condition_50L_50NL,
        "90L_10NL": condition_90L_10NL,
    }

    input_condition = cond_dict[input_condition]

    for model in input_condition:
        condition = model.split("_")[0] + "_" + model.split("_")[1]
        run = model.split("_")[2]
        print(model)
        df = pd.read_csv(
            "../../data/fixed_run/analysis/memorization_generalization/nl_shape/unattested_dataframes/"
            + condition
            + "/"
            + model
            + ".csv"
        )

        predictions = df["prediction"].tolist()
        tests = df["test"].tolist()
        triples = df["triples"].tolist()

        triples_in_incorrect_predictions = []
        incorrect_predictions = []
        test_items_incorrect_predictions = []

        for pred, test, triple in zip(predictions, tests, triples):
            if pred != test:
                triples_in_incorrect_predictions.append(triple)
                incorrect_predictions.append(pred)
                test_items_incorrect_predictions.append(test)

        unattested_triples_df = pd.read_csv(
            "../../data/fixed_run/analysis/memorization_generalization/nl_shape/section_6_4_2/unattested/triples_"
            + train_triples_set
            + "/"
            + condition
            + "/"
            + model
            + ".csv"
        )

        unattested_triples = unattested_triples_df["triples_seen_in_training"].tolist()

        new_df = pd.DataFrame()
        new_df["condition"] = [condition]
        new_df["run"] = [run]
        new_df["model"] = [model]
        new_df["num_incorrect_predictions"] = [len(incorrect_predictions)]
        new_df["num_of_triples_seen_in_training"] = [len(unattested_triples)]
        new_df["num_of_triples_unseen_in_training"] = [
            len(incorrect_predictions) - len(unattested_triples)
        ]
        new_df.to_csv(
            "../../data/fixed_run/analysis/memorization_generalization/nl_shape/section_6_4_2/unattested/counts_"
            + train_triples_set
            + "/"
            + condition
            + "/"
            + model
            + ".csv",
            index=False,
        )
