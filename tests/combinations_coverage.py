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


@pytest.mark.parametrize(
    "filename, lshaped_file, non_lshaped_file, condition, run, split, expected_ratio",
    [
        (
            "train.90L_10NL_1_1.tgt",
            "ipa_clean_lshaped_dict.json",
            "ipa_clean_non_lshaped_dict.json",
            "90L_10NL",
            "run1",
            "train",
            88,
        )
    ],
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


@pytest.mark.parametrize(
    "filename, lshaped_file, non_lshaped_file, condition, run, split, expected_ratio",
    [
        (
            "train.90L_10NL_1_2.tgt",
            "ipa_clean_lshaped_dict.json",
            "ipa_clean_non_lshaped_dict.json",
            "90L_10NL",
            "run1",
            "train",
            88,
        )
    ],
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


@pytest.mark.parametrize(
    "filename, lshaped_file, non_lshaped_file, condition, run, split, expected_ratio",
    [
        (
            "train.90L_10NL_1_3.tgt",
            "ipa_clean_lshaped_dict.json",
            "ipa_clean_non_lshaped_dict.json",
            "90L_10NL",
            "run1",
            "train",
            88,
        )
    ],
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


@pytest.mark.parametrize(
    "filename, lshaped_file, non_lshaped_file, condition, run, split, expected_ratio",
    [
        (
            "train.90L_10NL_1_4.tgt",
            "ipa_clean_lshaped_dict.json",
            "ipa_clean_non_lshaped_dict.json",
            "90L_10NL",
            "run1",
            "train",
            88,
        )
    ],
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


@pytest.mark.parametrize(
    "filename, lshaped_file, non_lshaped_file, condition, run, split, expected_ratio",
    [
        (
            "train.90L_10NL_2_1.tgt",
            "ipa_clean_lshaped_dict.json",
            "ipa_clean_non_lshaped_dict.json",
            "90L_10NL",
            "run2",
            "train",
            88,
        )
    ],
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


@pytest.mark.parametrize(
    "filename, lshaped_file, non_lshaped_file, condition, run, split, expected_ratio",
    [
        (
            "train.90L_10NL_2_2.tgt",
            "ipa_clean_lshaped_dict.json",
            "ipa_clean_non_lshaped_dict.json",
            "90L_10NL",
            "run2",
            "train",
            88,
        )
    ],
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


@pytest.mark.parametrize(
    "filename, lshaped_file, non_lshaped_file, condition, run, split, expected_ratio",
    [
        (
            "train.90L_10NL_2_2.tgt",
            "ipa_clean_lshaped_dict.json",
            "ipa_clean_non_lshaped_dict.json",
            "90L_10NL",
            "run2",
            "train",
            88,
        )
    ],
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


@pytest.mark.parametrize(
    "filename, lshaped_file, non_lshaped_file, condition, run, split, expected_ratio",
    [
        (
            "train.90L_10NL_2_3.tgt",
            "ipa_clean_lshaped_dict.json",
            "ipa_clean_non_lshaped_dict.json",
            "90L_10NL",
            "run2",
            "train",
            88,
        )
    ],
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


@pytest.mark.parametrize(
    "filename, lshaped_file, non_lshaped_file, condition, run, split, expected_ratio",
    [
        (
            "train.90L_10NL_2_4.tgt",
            "ipa_clean_lshaped_dict.json",
            "ipa_clean_non_lshaped_dict.json",
            "90L_10NL",
            "run2",
            "train",
            88,
        )
    ],
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


@pytest.mark.parametrize(
    "filename, lshaped_file, non_lshaped_file, condition, run, split, expected_ratio",
    [
        (
            "train.90L_10NL_3_1.tgt",
            "ipa_clean_lshaped_dict.json",
            "ipa_clean_non_lshaped_dict.json",
            "90L_10NL",
            "run3",
            "train",
            88,
        )
    ],
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


@pytest.mark.parametrize(
    "filename, lshaped_file, non_lshaped_file, condition, run, split, expected_ratio",
    [
        (
            "train.90L_10NL_3_2.tgt",
            "ipa_clean_lshaped_dict.json",
            "ipa_clean_non_lshaped_dict.json",
            "90L_10NL",
            "run3",
            "train",
            88,
        )
    ],
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


@pytest.mark.parametrize(
    "filename, lshaped_file, non_lshaped_file, condition, run, split, expected_ratio",
    [
        (
            "train.90L_10NL_3_3.tgt",
            "ipa_clean_lshaped_dict.json",
            "ipa_clean_non_lshaped_dict.json",
            "90L_10NL",
            "run3",
            "train",
            88,
        )
    ],
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


@pytest.mark.parametrize(
    "filename, lshaped_file, non_lshaped_file, condition, run, split, expected_ratio",
    [
        (
            "train.90L_10NL_3_4.tgt",
            "ipa_clean_lshaped_dict.json",
            "ipa_clean_non_lshaped_dict.json",
            "90L_10NL",
            "run3",
            "train",
            88,
        )
    ],
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


@pytest.mark.parametrize(
    "filename, lshaped_file, non_lshaped_file, condition, run, split, expected_ratio",
    [
        (
            "train.50L_50NL_1_1.tgt",
            "ipa_clean_lshaped_dict.json",
            "ipa_clean_non_lshaped_dict.json",
            "50L_50NL",
            "run1",
            "train",
            48,
        )
    ],
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


@pytest.mark.parametrize(
    "filename, lshaped_file, non_lshaped_file, condition, run, split, expected_ratio",
    [
        (
            "train.50L_50NL_1_2.tgt",
            "ipa_clean_lshaped_dict.json",
            "ipa_clean_non_lshaped_dict.json",
            "50L_50NL",
            "run1",
            "train",
            48,
        )
    ],
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


@pytest.mark.parametrize(
    "filename, lshaped_file, non_lshaped_file, condition, run, split, expected_ratio",
    [
        (
            "train.50L_50NL_1_3.tgt",
            "ipa_clean_lshaped_dict.json",
            "ipa_clean_non_lshaped_dict.json",
            "50L_50NL",
            "run1",
            "train",
            48,
        )
    ],
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


@pytest.mark.parametrize(
    "filename, lshaped_file, non_lshaped_file, condition, run, split, expected_ratio",
    [
        (
            "train.50L_50NL_1_4.tgt",
            "ipa_clean_lshaped_dict.json",
            "ipa_clean_non_lshaped_dict.json",
            "50L_50NL",
            "run1",
            "train",
            48,
        )
    ],
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


@pytest.mark.parametrize(
    "filename, lshaped_file, non_lshaped_file, condition, run, split, expected_ratio",
    [
        (
            "train.50L_50NL_2_1.tgt",
            "ipa_clean_lshaped_dict.json",
            "ipa_clean_non_lshaped_dict.json",
            "50L_50NL",
            "run2",
            "train",
            48,
        )
    ],
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


@pytest.mark.parametrize(
    "filename, lshaped_file, non_lshaped_file, condition, run, split, expected_ratio",
    [
        (
            "train.50L_50NL_2_2.tgt",
            "ipa_clean_lshaped_dict.json",
            "ipa_clean_non_lshaped_dict.json",
            "50L_50NL",
            "run2",
            "train",
            48,
        )
    ],
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


@pytest.mark.parametrize(
    "filename, lshaped_file, non_lshaped_file, condition, run, split, expected_ratio",
    [
        (
            "train.50L_50NL_2_3.tgt",
            "ipa_clean_lshaped_dict.json",
            "ipa_clean_non_lshaped_dict.json",
            "50L_50NL",
            "run2",
            "train",
            48,
        )
    ],
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


@pytest.mark.parametrize(
    "filename, lshaped_file, non_lshaped_file, condition, run, split, expected_ratio",
    [
        (
            "train.50L_50NL_2_4.tgt",
            "ipa_clean_lshaped_dict.json",
            "ipa_clean_non_lshaped_dict.json",
            "50L_50NL",
            "run2",
            "train",
            48,
        )
    ],
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


@pytest.mark.parametrize(
    "filename, lshaped_file, non_lshaped_file, condition, run, split, expected_ratio",
    [
        (
            "train.50L_50NL_3_1.tgt",
            "ipa_clean_lshaped_dict.json",
            "ipa_clean_non_lshaped_dict.json",
            "50L_50NL",
            "run3",
            "train",
            48,
        )
    ],
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


@pytest.mark.parametrize(
    "filename, lshaped_file, non_lshaped_file, condition, run, split, expected_ratio",
    [
        (
            "train.50L_50NL_3_2.tgt",
            "ipa_clean_lshaped_dict.json",
            "ipa_clean_non_lshaped_dict.json",
            "50L_50NL",
            "run3",
            "train",
            48,
        )
    ],
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


@pytest.mark.parametrize(
    "filename, lshaped_file, non_lshaped_file, condition, run, split, expected_ratio",
    [
        (
            "train.50L_50NL_3_3.tgt",
            "ipa_clean_lshaped_dict.json",
            "ipa_clean_non_lshaped_dict.json",
            "50L_50NL",
            "run3",
            "train",
            48,
        )
    ],
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


@pytest.mark.parametrize(
    "filename, lshaped_file, non_lshaped_file, condition, run, split, expected_ratio",
    [
        (
            "train.50L_50NL_3_4.tgt",
            "ipa_clean_lshaped_dict.json",
            "ipa_clean_non_lshaped_dict.json",
            "50L_50NL",
            "run3",
            "train",
            48,
        )
    ],
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


@pytest.mark.parametrize(
    "filename, lshaped_file, non_lshaped_file, condition, run, split, expected_ratio",
    [
        (
            "train.10L_90NL_1_1.tgt",
            "ipa_clean_lshaped_dict.json",
            "ipa_clean_non_lshaped_dict.json",
            "10L_90NL",
            "run1",
            "train",
            8,
        )
    ],
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


@pytest.mark.parametrize(
    "filename, lshaped_file, non_lshaped_file, condition, run, split, expected_ratio",
    [
        (
            "train.10L_90NL_1_2.tgt",
            "ipa_clean_lshaped_dict.json",
            "ipa_clean_non_lshaped_dict.json",
            "10L_90NL",
            "run1",
            "train",
            8,
        )
    ],
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


@pytest.mark.parametrize(
    "filename, lshaped_file, non_lshaped_file, condition, run, split, expected_ratio",
    [
        (
            "train.10L_90NL_1_3.tgt",
            "ipa_clean_lshaped_dict.json",
            "ipa_clean_non_lshaped_dict.json",
            "10L_90NL",
            "run1",
            "train",
            8,
        )
    ],
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


@pytest.mark.parametrize(
    "filename, lshaped_file, non_lshaped_file, condition, run, split, expected_ratio",
    [
        (
            "train.10L_90NL_1_4.tgt",
            "ipa_clean_lshaped_dict.json",
            "ipa_clean_non_lshaped_dict.json",
            "10L_90NL",
            "run1",
            "train",
            8,
        )
    ],
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


@pytest.mark.parametrize(
    "filename, lshaped_file, non_lshaped_file, condition, run, split, expected_ratio",
    [
        (
            "train.10L_90NL_2_1.tgt",
            "ipa_clean_lshaped_dict.json",
            "ipa_clean_non_lshaped_dict.json",
            "10L_90NL",
            "run2",
            "train",
            8,
        )
    ],
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


@pytest.mark.parametrize(
    "filename, lshaped_file, non_lshaped_file, condition, run, split, expected_ratio",
    [
        (
            "train.10L_90NL_2_2.tgt",
            "ipa_clean_lshaped_dict.json",
            "ipa_clean_non_lshaped_dict.json",
            "10L_90NL",
            "run2",
            "train",
            8,
        )
    ],
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


@pytest.mark.parametrize(
    "filename, lshaped_file, non_lshaped_file, condition, run, split, expected_ratio",
    [
        (
            "train.10L_90NL_2_3.tgt",
            "ipa_clean_lshaped_dict.json",
            "ipa_clean_non_lshaped_dict.json",
            "10L_90NL",
            "run2",
            "train",
            8,
        )
    ],
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


@pytest.mark.parametrize(
    "filename, lshaped_file, non_lshaped_file, condition, run, split, expected_ratio",
    [
        (
            "train.10L_90NL_2_4.tgt",
            "ipa_clean_lshaped_dict.json",
            "ipa_clean_non_lshaped_dict.json",
            "10L_90NL",
            "run2",
            "train",
            8,
        )
    ],
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


@pytest.mark.parametrize(
    "filename, lshaped_file, non_lshaped_file, condition, run, split, expected_ratio",
    [
        (
            "train.10L_90NL_3_1.tgt",
            "ipa_clean_lshaped_dict.json",
            "ipa_clean_non_lshaped_dict.json",
            "10L_90NL",
            "run3",
            "train",
            8,
        )
    ],
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


@pytest.mark.parametrize(
    "filename, lshaped_file, non_lshaped_file, condition, run, split, expected_ratio",
    [
        (
            "train.10L_90NL_3_2.tgt",
            "ipa_clean_lshaped_dict.json",
            "ipa_clean_non_lshaped_dict.json",
            "10L_90NL",
            "run3",
            "train",
            8,
        )
    ],
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


@pytest.mark.parametrize(
    "filename, lshaped_file, non_lshaped_file, condition, run, split, expected_ratio",
    [
        (
            "train.10L_90NL_3_2.tgt",
            "ipa_clean_lshaped_dict.json",
            "ipa_clean_non_lshaped_dict.json",
            "10L_90NL",
            "run3",
            "train",
            8,
        )
    ],
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


@pytest.mark.parametrize(
    "filename, lshaped_file, non_lshaped_file, condition, run, split, expected_ratio",
    [
        (
            "train.10L_90NL_3_3.tgt",
            "ipa_clean_lshaped_dict.json",
            "ipa_clean_non_lshaped_dict.json",
            "10L_90NL",
            "run3",
            "train",
            8,
        )
    ],
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


@pytest.mark.parametrize(
    "filename, lshaped_file, non_lshaped_file, condition, run, split, expected_ratio",
    [
        (
            "train.10L_90NL_3_4.tgt",
            "ipa_clean_lshaped_dict.json",
            "ipa_clean_non_lshaped_dict.json",
            "10L_90NL",
            "run3",
            "train",
            8,
        )
    ],
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
