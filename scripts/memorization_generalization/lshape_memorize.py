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
        return "NL"

    else:
        return "L"


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

        seen_triples = []
        unseen_triples = []
        total_attested_l = []
        total_attested_nl = []
        count = 0
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

            shape = get_shape(test_from_tgt_sf, lshaped_forms)
            if shape == "L":
                if test_triple in train_triples:
                    total_attested_l.append(test_triple)
                    if pred == test_from_tgt_sf:
                        seen_triples.append(test_triple)
                    else:
                        unseen_triples.append(test_triple)

        df = pd.DataFrame()
        df["correct_predictions_percentage"] = [
            round(len(seen_triples) / len(total_attested_l) * 100)
        ]
        df["incorrect_predictions_percentage"] = [
            round(len(unseen_triples) / len(total_attested_l) * 100)
        ]
        df.to_csv(
            "../../data/fixed_run/analysis/memorization_generalization/l_shape/old/"
            + model
            + ".csv",
            index=False,
        )
        print(
            "seen: ",
            len(seen_triples) / len(total_attested_l) * 100,
            "unseen: ",
            len(unseen_triples) / len(total_attested_l) * 100,
            "total attested L-shaped: ",
            len(total_attested_l),
        )
