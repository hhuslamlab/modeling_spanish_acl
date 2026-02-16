### Test script to check the coverage of the % of combinations in the dataset
import pytest
import json
import os


def load_data_and_calculate_ratio(
    filename, lshaped_file, non_lshaped_file, condition, run, split
):
    current_dir = os.path.dirname(os.path.abspath(__file__))

    file_path = os.path.join(current_dir, "..", "data", condition, split, run, filename)
    lshaped_path = os.path.join(current_dir, "..", "data", lshaped_file)
    non_lshaped_path = os.path.join(current_dir, "..", "data", non_lshaped_file)

    with open(file_path) as f:
        lines = f.readlines()
        lines = [line.replace(" ", "").strip() for line in lines]

    with open(lshaped_path) as f:
        lshaped_dict = json.load(f)

    with open(non_lshaped_path) as f:
        non_lshaped_dict = json.load(f)

    lshaped_form_to_shape = {
        form.replace(" ", ""): "L" for v in lshaped_dict.values() for form in v.values()
    }
    non_lshaped_form_to_shape = {
        form.replace(" ", ""): "NL"
        for v in non_lshaped_dict.values()
        for form in v.values()
    }

    form_to_shape = {**lshaped_form_to_shape, **non_lshaped_form_to_shape}

    shapes = [form_to_shape[line] for line in lines if line in form_to_shape]

    l_count = shapes.count("L")
    ratio = l_count / len(shapes) * 100

    return len(shapes), len(lines), ratio


LSHAPED_FILE = "ipa_clean_lshaped_dict.json"
NON_LSHAPED_FILE = "ipa_clean_non_lshaped_dict.json"


def _make_cases(condition, runs_seeds, expected_ratio):
    """Generate parametrize tuples for a condition across runs and seeds."""
    cases = []
    for run_num, seed in runs_seeds:
        filename = f"train.{condition}_{run_num}_{seed}.tgt"
        run = f"run{run_num}"
        cases.append(
            pytest.param(
                filename, LSHAPED_FILE, NON_LSHAPED_FILE,
                condition, run, "train", expected_ratio,
                id=f"{condition}_{run_num}_{seed}",
            )
        )
    return cases


_90L_10NL_CASES = _make_cases(
    "90L_10NL",
    [(r, s) for r in range(1, 4) for s in range(1, 5)],
    88,
)

_50L_50NL_CASES = _make_cases(
    "50L_50NL",
    [(r, s) for r in range(1, 4) for s in range(1, 5)],
    48,
)

_10L_90NL_CASES = _make_cases(
    "10L_90NL",
    [(r, s) for r in range(1, 4) for s in range(1, 5)],
    8,
)


@pytest.mark.parametrize(
    "filename, lshaped_file, non_lshaped_file, condition, run, split, expected_ratio",
    _90L_10NL_CASES + _50L_50NL_CASES + _10L_90NL_CASES,
)
def test_l_shaped_ratio(
    filename, lshaped_file, non_lshaped_file, condition, run, split, expected_ratio
):
    shapes_count, lines_count, ratio = load_data_and_calculate_ratio(
        filename, lshaped_file, non_lshaped_file, condition, run, split
    )

    assert (
        ratio > expected_ratio
    ), f"The L-shaped ratio ({ratio:.2f}%) is not above the expected {expected_ratio}%"


if __name__ == "__main__":
    pytest.main([__file__])
