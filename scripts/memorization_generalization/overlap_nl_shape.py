"""
we are checking if the test triples are attested in the training test. if the triples are seen in the training, we term it as 'old' and if not, then its 'new' for NL verbs.
"""
from typing import List
import json
import pandas as pd
from config import all_models


def get_nlshaped_forms():
    with open("../../data/ipa_clean_non_lshaped_dict.json") as f:
        nlshaped_dict = json.load(f)

    forms = [
        form.replace(" ", "").replace("ˈ", "")
        for k, v in nlshaped_dict.items()
        for _, form in v.items()
    ]
    return forms


def get_shape(form: str, nlshaped_forms: List[str]) -> str:
    if form in nlshaped_forms:
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

        stem_sfs = pd.read_csv("../../data/fixed_run/analysis/stems/" + model + ".csv")

        test_from_stem_sfs = stem_sfs["test_form"].tolist()
        shapes = stem_sfs["shapes"].tolist()
        train_triples = list(zip(train_src1_sfs, train_src2_sfs, train_tgt_sfs))

        test_triples = list(zip(test_src1_sfs, test_src2_sfs, test_tgt_sfs))

        lshaped_forms = get_nlshaped_forms()

        seen_triples = []
        unseen_triples = []
        total_l = []
        total_nl = []
        for test_triple, test_from_stem_sf, test_from_tgt_sf, shape in zip(
            test_triples, test_from_stem_sfs, test_from_tgt_sfs, shapes
        ):
            test_from_stem_sf = test_from_stem_sf.replace("ˈ", "").replace(" ", "")
            test_from_tgt_sf = test_from_tgt_sf.replace("ˈ", "").replace(" ", "")

            shape = get_shape(test_from_tgt_sf, lshaped_forms)
            if shape == "NL":
                if test_triple in train_triples:
                    seen_triples.append(test_triple)
                else:
                    unseen_triples.append(test_triple)
            if shape == "L":
                total_l.append(test_triple)
        total_nl = len(test_triples) - len(total_l)
        print(
            "seen: ",
            len(seen_triples) / total_nl * 100,
            "unseen: ",
            len(unseen_triples) / total_nl * 100,
            "total L-shaped: ",
            len(total_l),
            "total NL-shaped: ",
            total_nl,
        )
