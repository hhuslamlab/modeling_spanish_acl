"""
prepare dataset for logistic regression for NL shape verbs for unattested
"""
from typing import List
from collections import Counter
import pandas as pd
from l_shape_memorize import get_lshaped_forms, get_shape
from config import condition_90L_10NL, condition_50L_50NL, condition_10L_90NL
from config import exception_forms


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


def get_train_tgts(model) -> List[str]:
    train_tgt = pd.read_csv(
        "../../data/fixed_run/analysis/tgt_sf/train/" + model + ".csv"
    )
    train_tgts = train_tgt["tgt"]
    return train_tgts


def get_test_triples() -> List[str]:
    test_src_sf = pd.read_csv(
        "../../data/fixed_run/analysis/src_sf/test/" + model + ".csv"
    )
    test_src1_sfs = test_src_sf["src1_sf"].tolist()
    test_src2_sfs = test_src_sf["src2_sf"].tolist()
    test_tgt_sf = pd.read_csv(
        "../../data/fixed_run/analysis/tgt_sf/test/" + model + ".csv"
    )
    test_tgt_sfs = test_tgt_sf["tgt_sf"].tolist()

    return list(zip(test_src1_sfs, test_src2_sfs, test_tgt_sfs))


def get_test_tgts(model) -> List[str]:
    test_tgt_sf = pd.read_csv(
        "../../data/fixed_run/analysis/tgt_sf/test/" + model + ".csv"
    )
    test_tgts = test_tgt_sf["tgt"].tolist()

    return test_tgts


def get_train_triples_nl(
    train_tgts: List[str], train_triples: List[List[str]], lshaped_forms
) -> List[str]:
    train_triples_nl = []
    for tgt, train_triple in zip(train_tgts, train_triples):
        tgt = tgt.replace("ˈ", "").replace(" ", "")
        shape = get_shape(tgt, lshaped_forms)

        if shape == "NL":
            train_triples_nl.append(train_triple)

    return train_triples_nl


if __name__ == "__main__":
    input_condition = condition_10L_90NL
    for model in input_condition:
        print(model)
        ## get train and test triples
        train_triples = get_train_triples()
        test_triples = get_test_triples()

        ## get target forms in both training and testing phase
        train_tgts = get_train_tgts(model)
        test_tgts = get_test_tgts()

        ## get stem-final consonant from the predictions
        pred_sf = pd.read_csv("../../data/fixed_run/analysis/pred_sf/" + model + ".csv")

        predictions = pred_sf["pred"].tolist()
        pred_tests = pred_sf["test"].tolist()

        stem_sfs = pd.read_csv("../../data/fixed_run/analysis/stems/" + model + ".csv")

        test_from_stem_sfs = stem_sfs["test_form"].tolist()
        shapes = stem_sfs["shapes"].tolist()

        lshaped_forms = get_lshaped_forms()

        seen_triples_correct_predictions = []
        unseen_triples_correct_predictions = []
        total_attested_l = []
        total_attested_nl = []
        total_correct_predictions = []
        total_incorrect_predictions = []
        seen_triples_wrong_predictions = []
        unseen_triples_wrong_predictions = []
        total_unattested_nl = []
        total_prediction_status = []
        total_predictions_nl = []
        total_predictions_unattested_nl = []
        total_prediction_status_unattested_nl = []
        total_test_unattested_nl = []
        total_prediction_status_attested_nl = []
        total_test_nl = []
        condition = []
        run = []
        models = []
        train_triples_nl = []
        print("num of train_triples: ", len(train_triples))

        train_triples_nl = get_train_triples_nl(
            train_tgts, train_triples, lshaped_forms
        )
        print("num. of NL-shaped train triples: ", len(train_triples_nl))
        print("test_from_stem_sfs: ", len(test_from_stem_sfs))
        print("test_triples: ", len(test_triples))
        print("test_tgts: ", len(test_tgts))
        print("shapes: ", len(shapes))
        print("predictions: ", len(predictions))
        print("pred_tests: ", len(pred_tests))

        for (
            test_triple,
            test_from_stem_sf,
            test_from_tgt_sf,
            shape,
            pred,
            pred_test,
        ) in zip(
            test_triples, test_from_stem_sfs, test_tgts, shapes, predictions, pred_tests
        ):
            test_from_stem_sf = test_from_stem_sf.replace("ˈ", "").replace(" ", "")
            test_from_tgt_sf = test_from_tgt_sf.replace("ˈ", "").replace(" ", "")
            pred_test = pred_test.replace("ˈ", "").replace(" ", "")
            pred = pred.replace("ˈ", "").replace(" ", "")

            shape = get_shape(test_from_tgt_sf, lshaped_forms)
            if shape == "NL" and test_from_tgt_sf not in exception_forms:
                total_predictions_nl.append(pred)
                total_test_nl.append(test_from_tgt_sf)
                if pred == test_from_tgt_sf:
                    total_correct_predictions.append(pred)
                    total_prediction_status.append("1")
                if pred != test_from_tgt_sf:
                    total_incorrect_predictions.append(pred)
                    total_prediction_status.append("0")
                if test_triple not in train_triples_nl:
                    condition.append(model.split("_")[0] + "_" + model.split("_")[1])
                    run.append(model.split("_")[2])
                    models.append(model)
                    total_unattested_nl.append(test_triple)
                    total_predictions_unattested_nl.append(pred)
                    total_test_unattested_nl.append(test_from_tgt_sf)
                    if pred == test_from_tgt_sf:
                        total_prediction_status_unattested_nl.append(1)
                        seen_triples_correct_predictions.append(test_triple)
                    if pred != test_from_tgt_sf:
                        seen_triples_wrong_predictions.append(test_triple)
                        total_prediction_status_unattested_nl.append(0)

        total_predictions = len(total_correct_predictions) + len(
            total_incorrect_predictions
        )

        df = pd.DataFrame()

        freq_info = []

        freq_train_triples = dict(Counter(total_unattested_nl))

        for item in total_unattested_nl:
            freq_info.append(int(freq_train_triples[item]))

        print(
            "total predictions l: ",
            len(total_predictions_nl),
            "len of prediction status: ",
            len(total_prediction_status_unattested_nl),
            "len of frequency info: ",
            len(freq_info),
            "len of triples: ",
            len(total_attested_nl),
            "len of prediction: ",
            len(total_predictions_unattested_nl),
            "len of test: ",
            len(total_test_unattested_nl),
        )
        if (
            not total_prediction_status_unattested_nl
            and not total_unattested_nl
            and not total_predictions_unattested_nl
            and not total_test_unattested_nl
        ):
            total_prediction_status_unattested_nl.append(0)
            total_attested_nl.append(0)
            freq_info.append(0)
            total_unattested_nl.append(0)
            total_test_unattested_nl.append(0)
            total_predictions_unattested_nl.append(0)
            condition.append(model.split("_")[0] + "_" + model.split("_")[1])
            run.append(model.split("_")[2])
            models.append(model)

        df["condition"] = condition
        df["run"] = run
        df["model"] = models
        df["prediction_status"] = total_prediction_status_unattested_nl
        df["frequency"] = freq_info
        df["triples"] = total_unattested_nl
        df["prediction"] = total_predictions_unattested_nl
        df["test"] = total_test_unattested_nl

        df.to_csv(
            "../../data/fixed_run/analysis/memorization_generalization/nl_shape/unattested_dataframes/"
            + condition[0]
            + "/"
            + model
            + ".csv",
            index=False,
        )
