""" get L and NL accuracy """ import pandas as pd from config import all_models if __name__ == "__main__": for model in all_models:
        condition = model.split("_")[0] + "_" + model.split("_")[1]
        run = model.split("_")[2]
        with open(
            "../data/fixed_run/"
            + condition
            + "/test/run"
            + run
            + "/test."
            + model
            + ".tgt"
        ) as f:
            test_data = f.readlines()
            test_data = [
                item.strip().replace(" ", "").replace("ˈ", "") for item in test_data
            ]
        with open("../data/fixed_run/analysis/shape_info/" + model) as f:
            shapes = f.readlines()
            shapes = [item.strip() for item in shapes]

        with open("../data/fixed_run/predictions/" + model + ".txt") as f:
            predictions = f.readlines()
            predictions = [
                item.split(",")[1].replace("ˈ", "").strip() for item in predictions
            ]
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
            "../data/fixed_run/analysis/l_nl_accuracies/" + model + ".csv", index=False
        )
