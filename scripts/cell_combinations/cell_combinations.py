"""
Get cell combination accuracies (section 6.1)

Usage:
    cell_combination.py --condition=<c>

Options:
    --condition=<c>`    Specify the condition (e.g: 10L_90NL or 50L_50NL or 90L_10NL
"""
from docopt import docopt
from typing import Any
import pandas as pd
import re
from config import condition_10L_90NL, condition_50L_50NL, condition_90L_10NL


def get_lines(filename):
    with open(filename) as f:
        lines = f.readlines()
        lines = [item.strip().replace(" ", "") for item in lines]

    return lines


def get_prediction_status(tgts, preds, shapes):
    total = []
    total_l = []
    total_nl = []

    for truth, pred, shape in zip(tgts, preds, shapes):
        if shape == "NL":
            if truth == pred:
                total.append(True)
                total_nl.append(True)
            if truth != pred:
                total.append(False)
                total_nl.append(False)

        if shape == "L":
            if pred == truth:
                total_l.append(True)
                total.append(True)
            if pred != truth:
                total.append(False)
                total_l.append(False)

    return total, total_l, total_nl


def write_prediction_status(model, status, split):
    with open(
        "../data/fixed_run/analysis/prediction_status/" + split + "/" + model, "w+"
    ) as f:
        for item in status:
            f.write(str(item) + "\n")


def get_cell_combo_acc(
    cell_combo, cell_shape, cell_info, shapes, correct_wrong_samples
):
    cell_combo_shape_cells = 0
    cell_combo_correct_shape = 0
    for idx, cell_info in enumerate(cell_infos):
        if cell_info == cell_combo:
            sample = correct_wrong_samples[idx]
            shape = shapes[idx]
            if shape == cell_shape:
                cell_combo_shape_cells += 1
                if sample == "1":
                    cell_combo_correct_shape += 1

    ### if there are no cells of a given shape, return 0
    if cell_combo_shape_cells == 0:
        return -1.00
    return round(cell_combo_correct_shape / cell_combo_shape_cells * 100, 2)


def get_cell_tags(filename):
    data = get_src(filename)
    all_cell_tags = []
    for item in data:
        tags = re.findall("\<.*?\>", item)
        cell_tags = []
        for tag in tags:
            if tag in in_cell_tags:
                cell = "in_cell"
            if tag in out_cell_tags:
                cell = "out_cell"
            cell_tags.append(cell)
        all_cell_tags.append(cell_tags)

    return all_cell_tags


if __name__ == "__main__":
    args = docopt(__doc__)
    input_condition = args["--condition"]
    cond_mapping = {
        "10L_90NL": condition_10L_90NL,
        "50L_90NL": condition_50L_50NL,
        "90L_10NL": condition_90L_10NL,
    }

    cond = cond_mapping[input_condition]
    for model in cond:
        condition = model.split("_")[0] + "_" + model.split("_")[1]
        run = model.split("_")[2]

        ## get true targets
        tgts = get_lines(
            "../data/fixed_run/"
            + condition
            + "/test/run"
            + run
            + "/test."
            + model
            + ".tgt"
        )

        ## get predictions
        preds = get_lines("../data/fixed_run/predictions/" + model + ".txt")
        preds = [item.split(",")[1] for item in preds]
        ## get shape2
        shapes = get_lines("../data/fixed_run/analysis/shape_info/" + model)

        # print("truth: ", tgts[0], "pred: ", preds[0], "shape: ", shapes[0])
        total, total_l, total_nl = get_prediction_status(tgts, preds, shapes)
        all_preds = write_prediction_status(model, total, "all")

        l_shape_preds = write_prediction_status(model, total, "l_shape")

        nl_shape_preds = write_prediction_status(model, total, "nl_shape")

        in_cell_tags = [
            "<V;IND;PRS;1;SG>",
            "<V;SBJV;PRS;1;SG>",
            "<V;SBJV;PRS;2;SG>",
            "<V;SBJV;PRS;3;SG>",
            "<V;SBJV;PRS;1;PL>",
            "<V;SBJV;PRS;2;PL>",
            "<V;SBJV;PRS;3;PL>",
        ]

        out_cell_tags = [
            "<V;IND;PRS;2;SG>",
            "<V;IND;PRS;3;SG>",
            "<V;IND;PRS;1;PL>",
            "<V;IND;PRS;2;PL>",
            "<V;IND;PRS;3;PL>",
        ]

        #     ### correct sample
        #     acc_in_in_in_L = get_cell_combo_acc(["in_cell", "in_cell", "in_cell"], 'L', cell_infos, shapes, correct_wrong_samples)
        #     acc_in_in_in_NL = get_cell_combo_acc(["in_cell", "in_cell", "in_cell"], 'NL', cell_infos, shapes, correct_wrong_samples)

        #     acc_in_out_out_L = get_cell_combo_acc(["in_cell", "out_cell", "out_cell"], 'L', cell_infos, shapes, correct_wrong_samples)
        #     acc_in_out_out_NL = get_cell_combo_acc(["in_cell", "out_cell", "out_cell"], 'NL', cell_infos, shapes, correct_wrong_samples)

        #     acc_in_in_out_L = get_cell_combo_acc(["in_cell", "in_cell", "out_cell"], 'L', cell_infos, shapes, correct_wrong_samples)
        #     acc_in_in_out_NL = get_cell_combo_acc(["in_cell", "in_cell", "out_cell"], 'NL', cell_infos, shapes, correct_wrong_samples)

        #     acc_in_out_in_L = get_cell_combo_acc(["in_cell", "out_cell", "in_cell"], 'L', cell_infos, shapes, correct_wrong_samples)
        #     acc_in_out_in_NL = get_cell_combo_acc(["in_cell", "out_cell", "in_cell"], 'NL', cell_infos, shapes, correct_wrong_samples)

        #     acc_out_in_in_L = get_cell_combo_acc(["out_cell", "in_cell", "in_cell"], 'L', cell_infos, shapes, correct_wrong_samples)
        #     acc_out_in_in_NL = get_cell_combo_acc(["out_cell", "in_cell", "in_cell"], 'NL', cell_infos, shapes, correct_wrong_samples)

        #     acc_out_in_out_L = get_cell_combo_acc(["out_cell", "in_cell", "out_cell"], 'L', cell_infos, shapes, correct_wrong_samples)
        #     acc_out_in_out_NL = get_cell_combo_acc(["out_cell", "in_cell", "out_cell"], 'NL', cell_infos, shapes, correct_wrong_samples)

        #     acc_out_out_in_L = get_cell_combo_acc(["out_cell", "out_cell", "in_cell"], 'L', cell_infos, shapes, correct_wrong_samples)
        #     acc_out_out_in_NL = get_cell_combo_acc(["out_cell", "out_cell", "in_cell"], 'NL', cell_infos, shapes, correct_wrong_samples)

        #     acc_out_out_out_L = get_cell_combo_acc(["out_cell", "out_cell", "out_cell"], 'L', cell_infos, shapes, correct_wrong_samples)
        #     acc_out_out_out_NL = get_cell_combo_acc(["out_cell", "out_cell", "out_cell"], 'NL', cell_infos, shapes, correct_wrong_samples)

        #     df = pd.DataFrame()
        #     ### FIXME: refactor!

        #     df['filename'] = [filename]
        #     df['acc_in_in_in_L'] = [acc_in_in_in_L]
        #     df['acc_in_in_in_NL'] = [acc_in_in_in_NL]
        #     df['acc_in_out_out_L'] = [acc_in_out_out_L]
        #     df['acc_in_out_out_NL'] = [acc_in_out_out_NL]
        #     df['acc_in_in_out_L'] = [acc_in_in_out_L]
        #     df['acc_in_in_out_NL'] = [acc_in_in_out_NL]
        #     df['acc_in_out_in_L'] = [acc_in_out_in_L]
        #     df['acc_in_out_in_NL'] = [acc_in_out_in_NL]
        #     df['acc_out_in_in_L'] = [acc_out_in_in_L]
        #     df['acc_out_in_in_NL'] = [acc_out_in_in_NL]
        #     df['acc_out_in_out_L'] = [acc_out_in_out_L]
        #     df['acc_out_in_out_NL'] = [acc_out_in_out_NL]
        #     df['acc_out_out_in_L'] = [acc_out_out_in_L]
        #     df['acc_out_out_in_NL'] = [acc_out_out_in_NL]
        #     df['acc_out_out_out_L'] = [acc_out_out_out_L]
        #     df['acc_out_out_out_NL'] = [acc_out_out_out_NL]

        #     df.to_csv('../../data/fixed_analysis/cell_combination_accuracies/' + filename + ".csv", index=False)
