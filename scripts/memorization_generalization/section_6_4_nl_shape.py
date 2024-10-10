"""
Now section 6.4 investigates the third possible factor which possibly influences learning, namely, whether the models care for inherent characteristics of single consonant combinations (across in and out cell combinations).


In other words: Is there something special about the stem codas s-sk or b-p or s-g or... pattern in L-shaped verbs? Is there something special about specific stem coda consonants in NL verbs?

section 6.4 only looks at errors. So only the subset of wrong predictions in memorization subset

The question is: We look at all wrongly predicted forms and the coda stem consonant - is there a difference between known triplets from training and new triplets? possible answers: 1) no diff 2) yes, more errors in new triplets (= expected), 3)  yes, more errors in training triplets
"""
import pandas as pd
from config import condition_90L_10NL, condition_50L_50NL, condition_10L_90NL
from prepare_dataframes_nl_shape import get_train_triples


if __name__ == "__main__":
    input_condition = condition_90L_10NL
    for model in input_condition:
        len_attested_data = []
        len_unattested_data = []
        attested_wrong_predictions = []
        unattested_wrong_predictions = []
        per_attested_wrong_predictions = []
        per_unattested_wrong_predictions = []
        condition = []
        run = []
        models = []

        condition.append(model.split("_")[0] + "_" + model.split("_")[1])
        run.append(model.split("_")[2])
        models.append(model)

        train_triples = get_train_triples(model)
        print(len(train_triples))
        attested_data = pd.read_csv(
            "../../data/fixed_run/analysis/memorization_generalization/nl_shape/dataframes/"
            + condition[0]
            + "/"
            + model
            + ".csv"
        )

        unattested_data = pd.read_csv(
            "../../data/fixed_run/analysis/memorization_generalization/nl_shape/unattested_dataframes/"
            + condition[0]
            + "/"
            + model
            + ".csv"
        )

        attested_wrong_predictions = attested_data[
            attested_data["prediction_status"] == 0
        ]

        seen_wrong_predictions_attested = []

        triples_attested_wrong_predictions = attested_wrong_predictions[
            "triples"
        ].tolist()

        for triple in triples_attested_wrong_predictions:
            triple = str(triple)
            if triple in train_triples:
                seen_wrong_predictions_attested.append(triple)
        print(
            "train_triples: ",
            train_triples[:4],
            "triple: ",
            triples_attested_wrong_predictions[:3],
        )
        print(
            "seen wrong predictions attested: ",
            len(seen_wrong_predictions_attested),
            "number of wrong predictions: ",
            len(triples_attested_wrong_predictions),
        )

        unattested_wrong_predictions = unattested_data[
            unattested_data["prediction_status"] == 0
        ]

        df = pd.DataFrame()
        print([len(attested_data)], models, condition, run)
        df["condition"] = condition
        df["run"] = run
        df["model"] = models
        df["len_attested_data"] = [len(attested_data)]
        df["len_attested_wrong_predictions"] = [len(attested_wrong_predictions)]
        df["per_attested_wrong_among_attested"] = [
            round(len(attested_wrong_predictions) / len(attested_data), 2) * 100
        ]
        df["per_attested_wrong_among_all"] = [
            round(
                len(attested_wrong_predictions)
                / (len(attested_data) + len(unattested_data)),
                2,
            )
            * 100
        ]
        df["len_unattested_data"] = [len(unattested_data)]
        df["len_unattested_wrong_predictions"] = [len(unattested_wrong_predictions)]
        df["per_unattested_wrong_among_unattested"] = [
            round(len(unattested_wrong_predictions) / len(unattested_data), 2) * 100
        ]
        df["per_unattested_wrong_among_all"] = [
            round(
                len(unattested_wrong_predictions)
                / (len(attested_data) + len(unattested_data)),
                2,
            )
            * 100
        ]
        # df.to_csv(
        #     "../../data/fixed_run/analysis/memorization_generalization/nl_shape/section_6_4_1/" + condition[0] + "/" + model + ".csv",
        #     index=False)
