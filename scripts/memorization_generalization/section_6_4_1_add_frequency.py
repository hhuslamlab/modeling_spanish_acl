"""
Add frequency information for each dataframe in section 6.4.1
"""
from collections import Counter
import pandas as pd
from config import condition_10L_90NL, condition_50L_50NL, condition_90L_10NL
from section_6_4_1_attested_l_shape import (
    get_train_triples_l,
    get_train_triples,
    get_train_tgts,
)
from l_shape_memorize import get_shape, get_lshaped_forms


if __name__ == "__main__":
    input_condition = condition_10L_90NL
    for model in input_condition:
        condition = model.split("_")[0] + "_" + model.split("_")[1]

        print(condition, model)
        data = pd.read_csv(
            "../../data/fixed_run/analysis/memorization_generalization/nl_shape/section_6_4_1/attested/triples_nl/"
            + condition
            + "/"
            + model
            + ".csv"
        )

        triples = data["triples_seen_in_training"].tolist()
        counts = Counter(triples)

        triples_count = []
        for triple in triples:
            for k, v in counts.items():
                if triple == k:
                    triples_count.append(v)

        data["test_frequency"] = triples_count
        train_triples = get_train_triples(model)

        lshaped_forms = get_lshaped_forms()
        train_tgts = get_train_tgts(model)
        train_triples_l = get_train_triples_l(train_tgts, train_triples, lshaped_forms)
        train_triples_l = [str(item) for item in train_triples_l]
        data["training_frequency"] = [
            train_triples_l.count(triple) for triple in triples
        ]

        data.to_csv(
            "../../data/fixed_run/analysis/memorization_generalization/nl_shape/section_6_4_1/attested/triples_nl/"
            + condition
            + "/"
            + model
            + ".csv",
            index=False,
        )
