# Frequency matters: Modeling irregular morphological patterns in Spanish with Transformers

Code and data for the paper:

> Akhilesh Kakolu Ramarao, Kevin Tang, Dinah Baer-Henney. *Frequency matters: Modeling irregular morphological patterns in Spanish with Transformers*. Findings of the Association for Computational Linguistics: ACL 2025, pages 4474-4489.

## Installation

### Prerequisites

- Python 3.9
- PyTorch >= 1.10.0
- [Poetry](https://python-poetry.org/) (Python package manager)

### Poetry

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

### Python packages

```bash
poetry install
```

### R (for statistical analysis)

Install R with the following packages:

```r
install.packages(c("lme4", "emmeans"))
```

## Experimental Design

We train 36 models: 3 conditions x 3 runs x 4 seeds.

### Model identifiers

Each model is identified as `{condition}_{run}_{seed_index}` (e.g., `90L_10NL_3_4`).

| Condition | L-shaped % | NL-shaped % |
|---|---|---|
| `10L_90NL` | ~10% | ~90% |
| `50L_50NL` | ~50% | ~50% |
| `90L_10NL` | ~90% | ~10% |

### Seed mapping

| Seed index | Seed value |
|---|---|
| `_1` | 111 |
| `_2` | 312 |
| `_3` | 112 |
| `_4` | 64 |

For multi-seed runs, edit the `SEED` variable in `scripts/model/train.sh` before each run.

## Quick Reproduction

```bash
# Analysis only (uses pre-computed predictions)
bash reproduce.sh

# Full pipeline: train all 36 models + analysis (requires GPU)
bash reproduce.sh --train
```

## Usage

To replicate the analysis of each section, run the standalone scripts in the corresponding directories.

### Training and evaluation

All training and evaluation scripts are under `scripts/model/`:

```bash
# Preprocess
bash scripts/model/preprocess.sh <model_id>

# Train (edit SEED in train.sh for each seed index)
bash scripts/model/train.sh <model_id>

# Generate predictions
bash scripts/model/generate.sh <model_id>

# Evaluate
python scripts/model/evaluate.py \
  --prediction-filepath=predictions/<model_id>.pred \
  --gold-filepath=<gold_file_path> \
  --config=<model_id>
```

### Dataset (Section 3: Methodology)

The data for all three conditions (`10L_90NL`, `50L_50NL`, `90L_10NL`) is organized in the `data/` directory as follows:

```
data/
├── 10L_90NL/
│   ├── dev/run{1,2,3}/
│   ├── test/run{1,2,3}/
│   └── train/run{1,2,3}/
├── 50L_50NL/
│   ├── dev/run{1,2,3}/
│   ├── test/run{1,2,3}/
│   └── train/run{1,2,3}/
└── 90L_10NL/
    ├── dev/run{1,2,3}/
    ├── test/run{1,2,3}/
    └── train/run{1,2,3}/
```

### Predictions

Pre-computed predictions for all 36 models are in `data/predictions/` as `.txt` files in `index,form` format (e.g., `0,supeɾbenɡˈajs`). These are the processed outputs used by the analysis scripts.

If retraining, `generate.sh` produces raw fairseq output (`.pred` files). Run `evaluate.py` to convert these to the processed format used by the analysis pipeline.

### Analysis (Section 4)

To get the overall accuracies and stem accuracies, run the scripts in the following directories under `scripts/`:

```
scripts/
├── overall_accuracy/
├── stem_accuracies/
└── l_nl_accuracies/
```

Output is under `data/analysis/`:

```
data/analysis/
├── accuracies/
├── l_nl_accuracies/
└── stem_accuracies/
```

### Analysis: Cell combinations (Section 4.1)

Run the scripts in `scripts/cell_combinations/`.

Output:

```
data/analysis/
└── cell_combinations/
    ├── cell_infos/
    └── mean_accuracies/
```

### Analysis: Memorization and Generalization (Section 4.2)

Run the scripts in `scripts/memorization_generalization/`.

For statistical analysis (mixed-effects logistic regression):

```bash
cd scripts/memorization_generalization/R
Rscript emmeans_analysis_l_shape.R
Rscript emmeans_analysis_nl_shape.R
```

Output:

```
data/analysis/
└── memorization_generalization/
    ├── l_shape/
    │   ├── dataframes/{10L_90NL,50L_50NL,90L_10NL,combine}/
    │   ├── r_models/{10L_90NL,50L_50NL,90L_10NL}/
    │   ├── section_6_4_1/{attested,unattested}/
    │   └── unattested_dataframes/{10L_90NL,50L_50NL,90L_10NL,combine}/
    └── nl_shape/
        └── (same structure)
```

### Analysis: Consonant pair analysis (Section 4.3)

Run the scripts in `scripts/consonant_pair/`.

Output:

```
data/analysis/
├── compute_overlap_train_test_sf/
├── lemmas_sf/
├── overlap_lemma_train_test_sf/
├── lemma_test_pred_sf/
├── lemma_train_test_sf/
└── l_shaped/
    └── lemma_sf/{pred,test,train}/
```

### Analysis: Suffix analysis (Section 4.3)

Run the scripts in `scripts/suffix_errors/`.

Output:

```
data/analysis/
├── suffix_accuracies/{10L_90NL,50L_50NL,90L_10NL}/
└── suffix_errors/{10L_90NL,50L_50NL,90L_10NL}/
```

### Plots

All plots are in `data/analysis/plots/` (LaTeX/pgfplots format).

### Misclassifications

The misclassified L-shaped and NL-shaped words are under:

```
data/analysis/
└── misclassification/
    ├── 10L_90NL/{src,tgt}/{test,train}/
    ├── 50L_50NL/{src,tgt}/{test,train}/
    └── 90L_10NL/{src,tgt}/{test,train}/
```
