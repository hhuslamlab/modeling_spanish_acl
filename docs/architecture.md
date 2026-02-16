# Architecture: Research Pipeline

## Executive Summary

This project implements a morphological reinflection pipeline for studying L-shaped morphomic patterns in Spanish. It uses fairseq Transformer models to perform character-level sequence-to-sequence transduction, with post-hoc analysis scripts mapping to paper sections.

## Pipeline Architecture

```
┌─────────────┐    ┌──────────────┐    ┌─────────────┐    ┌──────────────┐
│  Data Prep  │───▶│  Preprocess  │───▶│    Train     │───▶│   Generate   │
│ (manual)    │    │ fairseq-     │    │ fairseq-     │    │ fairseq-     │
│             │    │ preprocess   │    │ train        │    │ generate     │
└─────────────┘    └──────────────┘    └─────────────┘    └──────────────┘
                                                                 │
                                                                 ▼
┌─────────────┐    ┌──────────────┐    ┌─────────────┐    ┌──────────────┐
│   Plots     │◀───│  Statistical │◀───│  Analysis    │◀───│  Evaluate    │
│ LaTeX/      │    │  Analysis    │    │  Python      │    │  evaluate.py │
│ pgfplots    │    │  R scripts   │    │  scripts     │    │              │
└─────────────┘    └──────────────┘    └─────────────┘    └──────────────┘
```

## Model Architecture

**Framework:** fairseq 0.10.2 (Transformer architecture)

| Parameter | Value |
|---|---|
| Architecture | Transformer (encoder-decoder) |
| Encoder/Decoder layers | 4 |
| Attention heads | 4 |
| Embedding dimension | 256 |
| FFN hidden dimension | 1024 |
| Dropout | 0.3 (attention, activation, regular) |
| Optimizer | Adam (betas: 0.9, 0.98) |
| Learning rate | 0.001 (inverse sqrt scheduler) |
| Warmup updates | 4000 |
| Max updates | 10,000 |
| Batch size | 400 |
| Label smoothing | 0.1 |
| Clip norm | 1.0 |
| Beam width | 5 (at inference) |
| Checkpoint selection | Best (checkpoint_best.pt) |

## Experimental Design

### Conditions

Three experimental conditions vary the ratio of L-shaped to NL-shaped verbs in training data:

| Condition | L-shaped % | NL-shaped % | Description |
|---|---|---|---|
| `10L_90NL` | ~10% | ~90% | Minority L-shaped |
| `50L_50NL` | ~50% | ~50% | Balanced |
| `90L_10NL` | ~90% | ~10% | Majority L-shaped |

### Replication Structure

- **3 runs** per condition (independent data splits)
- **4 seeds** per run (random initialization)
- **36 total models** (3 conditions x 3 runs x 4 seeds)
- Model naming: `{condition}_{run}_{seed}` (e.g., `90L_10NL_3_4`)

### Task Formulation

**Multi-source morphological reinflection:**
```
Input:  (source_form_1, source_tag_1, source_form_2, source_tag_2, target_tag)
Output: target_inflected_form
```

Character-level tokenization (space-separated characters), processed by fairseq as a translation task.

## Data Architecture

### Input Data Format

- Source: space-separated characters with morphological feature tags
- Target: space-separated characters of the inflected form
- File extensions: `.src` / `.tgt` (training), `.input` / `.output` (preprocessing)

### Ground Truth Dictionaries

| File | Purpose |
|---|---|
| `data/ipa_clean_lshaped_dict.json` | Maps lemmas to L-shaped inflected forms (IPA) |
| `data/ipa_clean_non_lshaped_dict.json` | Maps lemmas to NL-shaped inflected forms (IPA) |

### Analysis Output Structure

Analysis outputs mirror the paper sections under `data/analysis/`:

| Directory | Paper Section | Content |
|---|---|---|
| `accuracies/` | Section 4 | Overall accuracy CSVs |
| `l_nl_accuracies/` | Section 4 | L vs NL accuracy comparison |
| `stem_accuracies/` | Section 4 | Per-stem accuracy |
| `cell_combinations/` | Section 4.1 | Paradigm cell combination analysis |
| `memorization_generalization/` | Section 4.2 | Memorization/generalization with R models |
| `suffix_accuracies/` | Section 4.3 | Suffix accuracy by verb class |
| `suffix_errors/` | Section 4.3 | Suffix error patterns |
| `plots/` | All | LaTeX/pgfplots figures |

## Non-Neural Baseline

Located in `scripts/non_neural/non_neural.py`, adapted from SIGMORPHON 2020 Shared Task (Hulden/Pimentel/Kodner/Goldman). Uses Levenshtein-based string transduction rules. Expects tab-separated `.trn`/`.dev` files.

## Testing Strategy

- **Framework:** pytest with parametrized tests
- **Current coverage:** Dataset composition validation only (`tests/test_combi_coverage.py`)
- **Approach:** Data-driven tests that verify L-shaped verb ratios meet expected thresholds per condition
