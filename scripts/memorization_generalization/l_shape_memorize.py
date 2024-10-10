"""
we are checking if the test triples are attested and the model's prediction for that test item is correct or wrong
"""
from typing import List
import json
import pandas as pd
from config import all_models


def get_lshaped_forms() -> List[str]:
    with open("../../data/ipa_clean_lshaped_dict.json") as f:
        lshaped_dict = json.load(f)

    forms = [
        form.replace(" ", "").replace("ˈ", "")
        for k, v in lshaped_dict.items()
        for _, form in v.items()
    ]
    return forms


def get_shape(form: str, lshaped_forms: List[str]) -> str:
    if form in lshaped_forms:
        return "L"

    if form not in lshaped_forms:
        return "NL"


if __name__ == "__main__":
    for model in all_models:
        print(model)

        train_src_sf = pd.read_csv(
            "../../data/fixed_run/analysis/src_sf/train/" + model + ".csv"
        )
        train_src1_sfs = train_src_sf["src1_sf"].tolist()
        train_src2_sfs = train_src_sf["src2_sf"].tolist()
        train_tgt_sf = pd.read_csv(
            "../../data/fixed_run/analysis/tgt_sf/train/" + model + ".csv"
        )
        train_tgt_sfs = train_tgt_sf["tgt_sf"]

        test_src_sf = pd.read_csv(
            "../../data/fixed_run/analysis/src_sf/test/" + model + ".csv"
        )
        test_src1_sfs = test_src_sf["src1_sf"].tolist()
        test_src2_sfs = test_src_sf["src2_sf"].tolist()
        test_tgt_sf = pd.read_csv(
            "../../data/fixed_run/analysis/tgt_sf/test/" + model + ".csv"
        )
        test_tgt_sfs = test_tgt_sf["tgt_sf"].tolist()
        test_from_tgt_sfs = test_tgt_sf["tgt"].tolist()
        pred_sf = pd.read_csv("../../data/fixed_run/analysis/pred_sf/" + model + ".csv")

        predictions = pred_sf["pred"].tolist()
        pred_tests = pred_sf["test"].tolist()

        stem_sfs = pd.read_csv("../../data/fixed_run/analysis/stems/" + model + ".csv")

        test_from_stem_sfs = stem_sfs["test_form"].tolist()
        shapes = stem_sfs["shapes"].tolist()
        train_triples = list(zip(train_src1_sfs, train_src2_sfs, train_tgt_sfs))

        test_triples = list(zip(test_src1_sfs, test_src2_sfs, test_tgt_sfs))

        lshaped_forms = get_lshaped_forms()

        seen_triples_correct_predictions = []
        unseen_triples_correct_predictions = []
        total_attested_l = []
        total_attested_nl = []
        total_correct_predictions = []
        total_incorrect_predictions = []
        seen_triples_wrong_predictions = []
        unseen_triples_wrong_predictions = []
        total_unattested_l = []
        for (
            test_triple,
            test_from_stem_sf,
            test_from_tgt_sf,
            shape,
            pred,
            pred_test,
        ) in zip(
            test_triples,
            test_from_stem_sfs,
            test_from_tgt_sfs,
            shapes,
            predictions,
            pred_tests,
        ):
            test_from_stem_sf = test_from_stem_sf.replace("ˈ", "").replace(" ", "")
            test_from_tgt_sf = test_from_tgt_sf.replace("ˈ", "").replace(" ", "")
            pred_test = pred_test.replace("ˈ", "").replace(" ", "")
            pred = pred.replace("ˈ", "").replace(" ", "")

            shape = get_shape(test_from_tgt_sf, lshaped_forms)
            if shape == "L":
                if pred == test_from_tgt_sf:
                    total_correct_predictions.append(pred)
                if pred != test_from_tgt_sf:
                    total_incorrect_predictions.append(pred)

                if test_triple in train_triples:
                    total_attested_l.append(test_triple)
                    if pred == test_from_tgt_sf:
                        seen_triples_correct_predictions.append(test_triple)
                    else:
                        seen_triples_wrong_predictions.append(test_triple)

                if test_triple not in train_triples:
                    total_unattested_l.append(test_triple)
                    if pred == test_from_tgt_sf:
                        unseen_triples_correct_predictions.append(test_triple)
                    else:
                        unseen_triples_wrong_predictions.append(test_triple)

        total_predictions = len(total_correct_predictions) + len(
            total_incorrect_predictions
        )
        df = pd.DataFrame()
        df["num_correct_predictions"] = [len(total_correct_predictions)]
        df["num_incorrect_predictions"] = [len(total_incorrect_predictions)]
        df["per_correct_predictions"] = [
            round(len(total_correct_predictions) / total_predictions, 2)
        ]
        df["num_attested_triples"] = [len(total_attested_l)]
        df["num_unattested_triples"] = [len(total_unattested_l)]
        df["seen_triples_correct_predictions"] = [len(seen_triples_correct_predictions)]
        df["seen_triples_wrong_predictions"] = [len(seen_triples_wrong_predictions)]
        df["unseen_triples_correct_predictions"] = [
            len(unseen_triples_correct_predictions)
        ]
        df["unseen_triples_wrong_predictions"] = [len(unseen_triples_wrong_predictions)]
        df["per_seen_triples_correct"] = [
            round(
                len(seen_triples_correct_predictions) / len(total_attested_l) * 100, 2
            )
        ]
        if len(total_unattested_l) == 0:
            df["per_unseen_triples_correct"] = "NA"
        else:
            df["per_unseen_triples_correct"] = [
                round(
                    len(unseen_triples_correct_predictions)
                    / len(total_unattested_l)
                    * 100,
                    2,
                )
            ]
        df.to_csv(
            "../../data/fixed_run/analysis/memorization_generalization/l_shape/"
            + model
            + ".csv",
            index=False,
        )
