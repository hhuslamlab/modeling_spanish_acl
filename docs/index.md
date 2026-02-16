# Project Documentation Index

## Project Overview

- **Name:** Modeling Spanish Morphological Patterns with Transformers
- **Type:** Monolith (research data analysis pipeline)
- **Primary Language:** Python 3.9
- **Architecture:** Sequential research pipeline (fairseq Transformer)
- **Paper:** ACL 2025 (Findings), pages 4474-4489

## Quick Reference

- **Framework:** fairseq 0.10.2 (Transformer encoder-decoder)
- **Entry Point:** `scripts/model/train.sh <model_id>`
- **Architecture Pattern:** Sequential pipeline: preprocess -> train -> generate -> evaluate -> analyze -> plot
- **Experimental Design:** 3 conditions x 3 runs x 4 seeds = 36 models
- **Conditions:** `10L_90NL`, `50L_50NL`, `90L_10NL`

## Generated Documentation

- [Project Overview](./project-overview.md) - Summary, tech stack, key findings
- [Architecture](./architecture.md) - Pipeline, model architecture, experimental design, data format
- [Source Tree Analysis](./source-tree-analysis.md) - Complete annotated directory structure
- [Development Guide](./development-guide.md) - Installation, running pipeline, analysis scripts, known issues

## Existing Documentation

- [README](../README.md) - Project README

## Getting Started

### Quick Start (Analysis Only)

1. Install dependencies: `poetry install`
2. Analysis scripts are in `scripts/<section_name>/`
3. Pre-computed outputs are in `data/analysis/`
4. Plots are in `data/analysis/plots/` (LaTeX/pgfplots format)

### Full Pipeline (Training + Analysis)

1. Install Python dependencies: `poetry install`
2. Ensure PyTorch >= 1.10.0 and fairseq 0.10.2 are available
3. Preprocess: `bash scripts/model/preprocess.sh <model_id>`
4. Train: `bash scripts/model/train.sh <model_id>`
5. Generate: `bash scripts/model/generate.sh <model_id>`
6. Evaluate and analyze using scripts in `scripts/`

### Statistical Analysis

1. Install R with `lme4` and `emmeans` packages
2. Run R scripts in `scripts/memorization_generalization/R/`

---

*Generated: 2026-02-16 | Scan Level: quick | Mode: initial_scan*
