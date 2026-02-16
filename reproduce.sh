#!/bin/bash
# Master reproduction script for:
# "Frequency matters: Modeling irregular morphological patterns in Spanish with Transformers"
# ACL 2025 (Findings)
#
# Usage:
#   bash reproduce.sh           # Run analysis only (uses pre-computed predictions)
#   bash reproduce.sh --train   # Full pipeline: train all 36 models + analysis
#
# Prerequisites:
#   - Python 3.9 with dependencies installed (poetry install)
#   - R with lme4 and emmeans packages (for statistical analysis)
#   - GPU recommended for training

set -e

ROOT="$(cd "$(dirname "$0")" && pwd)"
CONDITIONS=("10L_90NL" "50L_50NL" "90L_10NL")
RUNS=(1 2 3)
SEEDS=(111 312 112 64)

# =============================================================================
# Training pipeline (optional, skip with pre-computed predictions)
# =============================================================================

if [ "$1" = "--train" ]; then
    echo "=== Training all 36 models ==="

    for cond in "${CONDITIONS[@]}"; do
        for run in "${RUNS[@]}"; do
            for seed_idx in "${!SEEDS[@]}"; do
                seed=${SEEDS[$seed_idx]}
                model_id="${cond}_${run}_$((seed_idx + 1))"
                echo "--- Training ${model_id} (seed=${seed}) ---"

                # Update seed in train.sh
                sed -i "s/^SEED=.*/SEED=${seed}/" "${ROOT}/scripts/model/train.sh"

                # Preprocess
                cd "${ROOT}/scripts/model"
                bash preprocess.sh "${model_id}"

                # Train
                bash train.sh "${model_id}"

                # Generate predictions
                bash generate.sh "${model_id}"

                cd "${ROOT}"
            done
        done
    done

    echo "=== Training complete ==="
fi

# =============================================================================
# Analysis pipeline (Section 4)
# =============================================================================

echo "=== Running analysis pipeline ==="

# --- Overall accuracy ---
echo "--- Section 4: Overall accuracy ---"
cd "${ROOT}/scripts/overall_accuracy"
python get_accuracy.py
python combine_accuracy.py
bash concatenate.sh
python plot.py

# --- Stem accuracies ---
echo "--- Section 4: Stem accuracies ---"
cd "${ROOT}/scripts/stem_accuracies"
python get_accuracy.py
python combine_accuracy.py
bash concatenate.sh

# --- L vs NL accuracies ---
echo "--- Section 4: L vs NL accuracies ---"
cd "${ROOT}/scripts/l_nl_accuracies"
python get_accuracy.py
python combine_accuracy.py
bash concatenate.sh
python plot_l_nl_accuracy.py

# --- Cell combinations (Section 4.1) ---
echo "--- Section 4.1: Cell combinations ---"
cd "${ROOT}/scripts/cell_combinations"
python cell_combinations.py
python combine_accuracy.py
bash concatenate.sh
python plot.py

# --- Memorization & Generalization (Section 4.2) ---
echo "--- Section 4.2: Memorization & Generalization ---"
cd "${ROOT}/scripts/memorization_generalization"
bash run_df.sh
bash run_calc.sh
bash run_combine.sh
python plot_l_shape.py
python plot_nl_shape.py

# --- Statistical analysis (Section 4.2, requires R) ---
echo "--- Section 4.2: Statistical analysis (R) ---"
cd "${ROOT}/scripts/memorization_generalization/R"
Rscript emmeans_analysis_l_shape.R
Rscript emmeans_analysis_nl_shape.R

# --- Consonant pair analysis (Section 4.3) ---
echo "--- Section 4.3: Consonant pair analysis ---"
cd "${ROOT}/scripts/consonant_pair"
python get_shape.py
python get_stems.py
python src_sf.py
python tgt_sf.py
python pred_sf.py
python train_test_sf.py
python lemma_sf.py
python consonant_pairs.py
python freq_train_test_sf.py
python get_lemma_test_pred_sf.py
python compute_overlap_train_test_sf.py
python overlap_sf_all_tokens.py
python overlap_sf_l_shape_tokens.py
python filter_sf_lshape_entries.py
python l_shaped_lemma_sf.py
python l_shaped_lemma_pred_sf.py
python compute_overlap_sfs.py
python compute_overlap_wrong_predictions_sf.py
python compute_overlap_wrong_predictions_l_shape_sf.py
python compute_per_misclassified_lemmas.py
python compute_metrics.py
python compute_avg_confusion_matrix.py
bash replace_nan.sh

# --- Suffix analysis (Section 4.3) ---
echo "--- Section 4.3: Suffix analysis ---"
cd "${ROOT}/scripts/suffix_errors"
python suffix_errors.py
python suffix_error_verb_type.py
python compute_suffix_per_type.py
python compute_overall_suffix_accuracy.py

cd "${ROOT}"
echo "=== Analysis complete ==="
echo "Results are in data/analysis/"
echo "Plots are in data/analysis/plots/"
