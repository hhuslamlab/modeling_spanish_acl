# Project Overview: Modeling Spanish Morphological Patterns

**Paper:** *"Frequency matters: Modeling irregular morphological patterns in Spanish with Transformers"*
**Venue:** ACL 2025 (Findings), pages 4474-4489
**Authors:** Akhilesh Kakolu Ramarao, Kevin Tang, Dinah Baer-Henney
**Affiliation:** Heinrich Heine University Düsseldorf; University of Florida

---

## Summary

This project investigates how type frequency affects the learnability of L-shaped morphomic patterns in Spanish verbal paradigms using transformer-based morphological reinflection. The study uses encoder-decoder transformers (via fairseq) to model the Paradigm Cell Filling Problem (PCFP) -- how speakers generate inflected forms from incomplete paradigms.

The L-shaped pattern is an irregular morphological pattern in Spanish where the first-person singular present indicative stem matches the stem used throughout the present subjunctive mood (e.g., *decir* -> *digo/diga/digas/...*).

## Key Findings

1. Models perform better on L-shaped verbs compared to regular verbs, especially in uneven frequency conditions
2. Robust primacy effects are observed, but no consistent recency effects
3. Memorization becomes more prominent as the proportion of L-shaped verbs increases
4. Tendency to regularize L-shaped verbs when their consonant alternation pairs are rare or absent in training data

## Technology Stack

| Category | Technology | Version |
|---|---|---|
| Language | Python | 3.8.10 |
| Deep Learning | PyTorch | >= 1.10.0 |
| Seq2Seq Framework | fairseq | 0.10.2 |
| Package Manager | Poetry | - |
| Data Analysis | pandas | ^1.3.5 |
| Visualization | matplotlib / seaborn | 3.5.0 / ^0.11.2 |
| Statistical Analysis | R (lme4, emmeans) | - |
| Publication Plots | LaTeX / pgfplots | - |
| Testing | pytest | ^5.2 |
| Code Formatting | black | ^21.12b0 |

## Architecture

**Type:** Monolith | **Pattern:** Sequential Research Pipeline

```
Data Preparation → fairseq Preprocess → Train → Generate → Evaluate → Analyze → Plot
```

## Repository Structure

- **Single repository** with all code, data, and analysis outputs
- **3 experimental conditions** x 3 runs x 4 seeds = 36 models
- **Published at:** `https://github.com/hhuslamlab/modeling_spanish_acl`

## Links to Detailed Documentation

- [Source Tree Analysis](./source-tree-analysis.md)
- [Architecture](./architecture.md)
- [Development Guide](./development-guide.md)
