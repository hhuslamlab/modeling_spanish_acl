import pandas as pd
import statistics

if __name__ == "__main__":
    df = pd.read_csv("../data/fixed_run/analysis/accuracies/combine.csv")

    models = df["model"].tolist()
    accs = df["accuracy"].tolist()

    acc_10L = []
    acc_50L = []
    acc_90L = []
    for model, acc in zip(models, accs):
        if model.startswith("10L"):
            acc_10L.append(acc)

        if model.startswith("50L"):
            acc_50L.append(acc)

        if model.startswith("90L"):
            acc_90L.append(acc)

    mean_10L = statistics.mean(acc_10L)
    mean_50L = statistics.mean(acc_50L)
    mean_90L = statistics.mean(acc_90L)

    print(f"mean 10L: {mean_10L}")
    print(f"mean 50L: {mean_50L}")
    print(f"mean 90L: {mean_90L}")
