# Development Guide

## Prerequisites

- **Python** 3.8.10 (or 3.9 -- see note below)
- **PyTorch** >= 1.10.0
- **Poetry** (Python package manager)
- **R** with packages: `lme4`, `emmeans` (for statistical analysis)
- **LaTeX** with `pgfplots` package (for generating publication plots)
- **GPU** recommended for model training (fairseq)

> **Note:** There is a version conflict between `pyproject.toml` (Python 3.8.10) and `README.org` (Python 3.9). Verify which version works with your fairseq installation.

## Installation

### 1. Install Poetry

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

### 2. Install Python Dependencies

```bash
cd modeling_spanish_naacl25
poetry install
```

### 3. Install R Dependencies (for statistical analysis)

```r
install.packages(c("lme4", "emmeans"))
```

### 4. Install LaTeX (for plot generation)

Install a TeX distribution (e.g., TeX Live) with the `pgfplots` package.

## Running the Pipeline

### Step 1: Preprocess Data

```bash
cd scripts/model
bash preprocess.sh <model_id>
# Example: bash preprocess.sh 90L_10NL_1_1
```

### Step 2: Train Model

```bash
bash train.sh <model_id>
# Example: bash train.sh 90L_10NL_1_1
```

**Note:** `train.sh` hardcodes `SEED=111`. For multi-seed runs, edit the SEED variable before each run.

### Step 3: Generate Predictions

```bash
bash generate.sh <model_id>
# Example: bash generate.sh 90L_10NL_1_1
```

### Step 4: Evaluate

```bash
python evaluate.py \
  --prediction-filepath=predictions/<model_id>.pred \
  --gold-filepath=<gold_file_path> \
  --config=<model_id>
```

> **Warning:** `evaluate.py` has known bugs (undefined `halsize` variable, incorrect `format()` call). Fix before use.

## Running Analysis Scripts

Each analysis section has its own directory under `scripts/`. Run scripts from the project root or from within each directory (scripts use relative paths like `../data/`).

### Overall Accuracy (Section 4)

```bash
cd scripts/overall_accuracy
python get_accuracy.py
python combine_accuracy.py
bash concatenate.sh
python plot.py
```

### L vs NL Accuracy (Section 4)

```bash
cd scripts/l_nl_accuracies
python get_accuracy.py
python combine_accuracy.py
bash concatenate.sh
python plot_l_nl_accuracy.py
```

### Cell Combinations (Section 4.1)

```bash
cd scripts/cell_combinations
python cell_combinations.py
python combine_accuracy.py
bash concatenate.sh
python plot.py
```

### Memorization & Generalization (Section 4.2)

```bash
cd scripts/memorization_generalization
bash run_df.sh          # Prepare dataframes
bash run_calc.sh        # Run calculations
bash run_combine.sh     # Combine results
python plot_l_shape.py
python plot_nl_shape.py
```

For statistical analysis:

```bash
cd scripts/memorization_generalization/R
Rscript emmeans_analysis_l_shape.R
Rscript emmeans_analysis_nl_shape.R
```

### Consonant Pair Analysis (Section 4.3)

```bash
cd scripts/consonant_pair
# Run scripts in sequence (see individual files for usage)
```

### Suffix Errors (Section 4.3)

```bash
cd scripts/suffix_errors
python suffix_errors.py
python compute_suffix_per_type.py
python compute_overall_suffix_accuracy.py
```

## Running Tests

```bash
pytest tests/
```

> **Note:** Tests have known issues -- see `_bmad-output/project-context.md` for details.

## Model Identifiers

All 36 model identifiers follow the pattern `{condition}_{run}_{seed}`:

| Condition | Models |
|---|---|
| `10L_90NL` | `10L_90NL_1_1` through `10L_90NL_3_4` |
| `50L_50NL` | `50L_50NL_1_1` through `50L_50NL_3_4` |
| `90L_10NL` | `90L_10NL_1_1` through `90L_10NL_3_4` |

These are defined in `scripts/config.py`.

## Key Data Files

| File | Description |
|---|---|
| `data/ipa_clean_lshaped_dict.json` | L-shaped verb forms (ground truth) |
| `data/ipa_clean_non_lshaped_dict.json` | NL-shaped verb forms (ground truth) |
| `scripts/config.py` | Suffix dictionaries (AR/ER/IR) and model ID lists |

## Known Issues

1. **`evaluate.py`**: References undefined variable `halsize`; `format()` call has wrong argument count
2. **Test suite**: Duplicate function names, typo in function call, string vs int type mismatch
3. **Path inconsistency**: `train.sh` uses `fixed_data_bin`/`fixed_checkpoints` while `preprocess.sh`/`generate.sh` use `data-bin`/`checkpoints`
4. **No `poetry.lock`**: Dependency versions may not be exactly reproducible
5. **Python version conflict**: `pyproject.toml` says 3.8.10, `README.org` says 3.9
