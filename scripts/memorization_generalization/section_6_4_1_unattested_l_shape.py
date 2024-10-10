"""
Unattested triples > incorrect predictions > check if this incorrect prediction's triple is seen in training for L-shape forms

Usage:
    section_6_4_1_unattested_l_shape.py --condition=<c> --train_triples_set=<tt>

Options:
    --condition=<c>`    Specify the condition (e.g: 10L_90NL or 50L_50NL or 90L_10NL
    --train_triples_set=<tt>    Specify "all" if you want to check against all training triples or just "L" if you want to check it against L-shaped training triples.
"""
from docopt import docopt
from typing import List
import pandas as pd
import numpy as np
from config import condition_90L_10NL, condition_50L_50NL, condition_10L_90NL
from section_6_4_1_attested_l_shape import get_train_triples_l, get_train_tgts
from l_shape_memorize import get_shape, get_lshaped_forms


def get_train_triples() -> List[List[str]]:
    train_src_sf = pd.read_csv(
        "../../data/fixed_run/analysis/src_sf/train/" + model + ".csv"
    )
    train_src1_sfs = train_src_sf["src1_sf"].tolist()
    train_src2_sfs = train_src_sf["src2_sf"].tolist()
    train_tgt_sf = pd.read_csv(
        "../../data/fixed_run/analysis/tgt_sf/train/" + model + ".csv"
    )
    train_tgt_sfs = train_tgt_sf["tgt_sf"].tolist()

    return list(zip(train_src1_sfs, train_src2_sfs, train_tgt_sfs))


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
        print(model)
        condition = model.split("_")[0] + "_" + model.split("_")[1]
        run = model.split("_")[2]
        df = pd.read_csv(
            "../../data/fixed_run/analysis/memorization_generalization/l_shape/unattested_dataframes/"
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
        if train_triples_set == "all":
            train_triples = get_train_triples()
            all_triples = [str(tr) for tr in train_triples]
        if train_triples_set == "l":
            train_triples = get_train_triples()

            lshaped_forms = get_lshaped_forms()
            train_tgts = get_train_tgts(model)
            train_triples_l = get_train_triples_l(
                train_tgts, train_triples, lshaped_forms
            )
            all_triples = [str(tr) for tr in train_triples_l]

        seen_triples = []
        conditions = []
        runs = []
        models = []
        for item in triples_in_incorrect_predictions:
            if item in all_triples:
                seen_triples.append(item)
                conditions.append(condition)
                runs.append(run)
                models.append(model)

        new_df = pd.DataFrame()
        new_df["condition"] = conditions
        new_df["run"] = runs
        new_df["model"] = models
        new_df["triples_seen_in_training"] = seen_triples
        new_df.to_csv(
            "../../data/fixed_run/analysis/memorization_generalization/l_shape/section_6_4_1/unattested/triples_"
            + train_triples_set
            + "/"
            + condition
            + "/"
            + model
            + ".csv",
            index=False,
        )
