"""
cell combination analysis
"""

import pandas as pd
from config import condition_10L_90NL, condition_50L_50NL, condition_90L_10NL


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
    condition_10L_90NL = [
        "10L_90NL_1_1",
        "10L_90NL_1_2",
        "10L_90NL_1_3",
        "10L_90NL_1_4",
        "10L_90NL_2_1",
        "10L_90NL_2_2",
        "10L_90NL_2_3",
        "10L_90NL_2_4",
        "10L_90NL_3_1",
        "10L_90NL_3_2",
        "10L_90NL_3_3",
        "10L_90NL_3_4",
    ]

    condition_50L_50NL = [
        "50L_50NL_1_1",
        "50L_50NL_1_2",
        "50L_50NL_1_3",
        "50L_50NL_1_4",
        "50L_50NL_2_1",
        "50L_50NL_2_2",
        "50L_50NL_2_3",
        "50L_50NL_2_4",
        "50L_50NL_3_1",
        "50L_50NL_3_2",
        "50L_50NL_3_3",
        "50L_50NL_3_4",
    ]

    condition_90L_10NL = [
        "90L_10NL_1_1",
        "90L_10NL_1_2",
        "90L_10NL_1_3",
        "90L_10NL_1_4",
        "90L_10NL_2_1",
        "90L_10NL_2_2",
        "90L_10NL_2_3",
        "90L_10NL_2_4",
        "90L_10NL_3_1",
        "90L_10NL_3_2",
        "90L_10NL_3_3",
        "90L_10NL_3_4",
    ]

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
