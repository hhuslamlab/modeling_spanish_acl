# Source Tree Analysis

## Project Root

```
modeling_spanish_naacl25/
├── README.org                    # Project README (Org-mode format)
├── pyproject.toml                # Poetry dependency manifest
├── ACL25.zip                     # Paper LaTeX source
├── .gitignore                    # Git ignore rules (minimal)
│
├── scripts/                      # All analysis and model code
│   ├── config.py                 # ★ Central configuration: model IDs, suffix dictionaries
│   ├── __init__.py
│   │
│   ├── model/                    # [Section 3] Training pipeline
│   │   ├── preprocess.sh         #   fairseq-preprocess (character-level tokenization)
│   │   ├── train.sh              #   fairseq-train (Transformer 4L/4H/256E/1024H)
│   │   ├── generate.sh           #   fairseq-generate (beam=5, checkpoint_best.pt)
│   │   └── evaluate.py           #   Prediction evaluation (has known bugs)
│   │
│   ├── overall_accuracy/         # [Section 4] Overall accuracy computation
│   │   ├── get_accuracy.py       #   Compute per-model accuracy
│   │   ├── combine_accuracy.py   #   Aggregate across models
│   │   ├── plot.py               #   Generate accuracy plots
│   │   └── concatenate.sh        #   Combine CSV outputs
│   │
│   ├── stem_accuracies/          # [Section 4] Stem-level accuracy
│   │   ├── get_stem_accuracy.py
│   │   ├── combine_accuracy.py
│   │   ├── plot_stem_accuracy.py
│   │   └── concatenate.sh
│   │
│   ├── l_nl_accuracies/          # [Section 4] L-shaped vs NL-shaped accuracy
│   │   ├── get_accuracy.py
│   │   ├── combine_accuracy.py
│   │   ├── plot_l_nl_accuracy.py
│   │   └── concatenate.sh
│   │
│   ├── cell_combinations/        # [Section 4.1] Paradigm cell combination analysis
│   │   ├── cell_combo.py
│   │   ├── cell_combinations.py
│   │   ├── combine_accuracy.py
│   │   ├── config_new.py
│   │   ├── plot.py
│   │   ├── x.py
│   │   └── concatenate.sh
│   │
│   ├── memorization_generalization/  # [Section 4.2] Memorization & generalization
│   │   ├── add_memgen.py
│   │   ├── combine_dataframe.py
│   │   ├── prepare_dataframes_l_shape.py
│   │   ├── prepare_dataframes_nl_shape.py
│   │   ├── prepare_atttested_dataframes_l_shape.py
│   │   ├── prepare_unattested_dataframes_l_shape.py
│   │   ├── prepare_unattested_dataframes_nl_shape.py
│   │   ├── section_6_4_l_shape.py
│   │   ├── section_6_4_nl_shape.py
│   │   ├── section_6_4_1_*.py      # Multiple sub-analysis scripts
│   │   ├── overlap_l_shape.py
│   │   ├── overlap_nl_shape.py
│   │   ├── l_shape_memorize.py
│   │   ├── lshape_memorize.py
│   │   ├── nl_shape_memorize.py
│   │   ├── plot_l_shape.py
│   │   ├── plot_nl_shape.py
│   │   ├── run_df.sh
│   │   ├── run_calc.sh
│   │   ├── run_combine.sh
│   │   └── R/                       # R statistical analysis
│   │       ├── section_6_4_1.R
│   │       ├── regression.R
│   │       ├── emmeans_analysis_l_shape.R
│   │       ├── emmeans_analysis_nl_shape.R
│   │       └── logisticregression_16Dec2023.Rmd
│   │
│   ├── consonant_pair/           # [Section 4.3] Consonant alternation analysis
│   │   ├── consonant_pairs.py
│   │   ├── get_shape.py
│   │   ├── get_stems.py
│   │   ├── src_sf.py / tgt_sf.py / pred_sf.py
│   │   ├── lemma_sf.py / l_shaped_lemma_sf.py
│   │   ├── train_test_sf.py / freq_train_test_sf.py
│   │   ├── compute_metrics.py
│   │   ├── compute_avg_confusion_matrix.py
│   │   ├── compute_overlap_*.py     # Multiple overlap computation scripts
│   │   ├── filter_sf_lshape_entries.py
│   │   ├── compute_per_misclassified_lemmas.py
│   │   └── replace_nan.sh
│   │
│   ├── suffix_errors/            # [Section 4.3] Suffix error analysis
│   │   ├── suffix_errors.py
│   │   ├── suffix_error_verb_type.py
│   │   ├── compute_suffix_per_type.py
│   │   └── compute_overall_suffix_accuracy.py
│   │
│   ├── effect_batch_size/        # Supplementary: batch size effect
│   │   ├── plot_lshaped_batch_size.py
│   │   └── plot_nlshaped_batch_size.py
│   │
│   ├── non_neural/               # Baseline: non-neural model
│   │   └── non_neural.py         #   SIGMORPHON 2020 string transduction baseline
│   │
│   ├── misc/                     # Miscellaneous utilities
│   │   └── concatenate.sh
│   │
│   └── viz_attention.py          # Attention weight visualization
│
├── data/                         # All data, predictions, and analysis outputs
│   ├── 10L_90NL/                 # Condition: 10% L-shaped, 90% NL-shaped
│   │   ├── train/run{1,2,3}/     #   Training splits (3 runs)
│   │   ├── dev/run{1,2,3}/       #   Development splits
│   │   └── test/run{1,2,3}/      #   Test splits
│   ├── 50L_50NL/                 # Condition: 50% L-shaped, 50% NL-shaped
│   │   └── (same structure)
│   ├── 90L_10NL/                 # Condition: 90% L-shaped, 10% NL-shaped
│   │   └── (same structure)
│   │
│   ├── predictions/              # Model predictions (main)
│   ├── naacl25_predictions/      # Alternative prediction runs
│   ├── naacl25_1_predictions/    # Alternative prediction runs
│   ├── batch_size_*_predictions/ # Batch size experiment predictions
│   ├── processed_predictions_orig/ # Post-processed predictions
│   ├── checkpoints/              # Model checkpoint files (large binaries)
│   │
│   ├── ipa_clean_lshaped_dict.json      # ★ Ground truth: L-shaped verb forms
│   ├── ipa_clean_non_lshaped_dict.json  # ★ Ground truth: NL-shaped verb forms
│   │
│   └── analysis/                 # All computed analysis outputs
│       ├── accuracies/           #   Overall accuracy CSVs
│       ├── l_nl_accuracies/      #   L vs NL accuracy CSVs
│       ├── stem_accuracies/      #   Stem accuracy CSVs
│       ├── cell_combinations/    #   Cell combination analysis
│       ├── memorization_generalization/  # Mem/gen dataframes and R models
│       ├── suffix_accuracies/    #   Suffix accuracy by verb class
│       ├── suffix_errors/        #   Suffix error analysis
│       ├── misclassification/    #   Misclassified forms
│       ├── plots/                #   Generated LaTeX/pgfplots figures
│       └── (many more subdirs)   #   Overlap, lemma, shape analyses
│
├── tests/                        # Test suite
│   ├── __init__.py
│   └── test_combi_coverage.py    # Dataset composition validation tests
│
└── docs/                         # Project documentation (this directory)
```

## Critical Files

| File | Role |
|---|---|
| `scripts/config.py` | Central model ID registry and suffix dictionaries |
| `data/ipa_clean_lshaped_dict.json` | L-shaped verb classification ground truth |
| `data/ipa_clean_non_lshaped_dict.json` | NL-shaped verb classification ground truth |
| `scripts/model/train.sh` | Model training configuration (hyperparameters) |
| `pyproject.toml` | Python dependency manifest |

## Entry Points

| Task | Entry Point |
|---|---|
| Preprocess data | `scripts/model/preprocess.sh <model_id>` |
| Train model | `scripts/model/train.sh <model_id>` |
| Generate predictions | `scripts/model/generate.sh <model_id>` |
| Evaluate predictions | `scripts/model/evaluate.py --prediction-filepath=... --gold-filepath=... --config=...` |
| Run analysis | Individual scripts in `scripts/<analysis_type>/` |
| Run tests | `pytest tests/` |
