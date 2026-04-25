# SLR Workflow Chat Export

## Context
This document captures the structured workflow and decisions made during the construction of a Systematic Literature Review (SLR) on AI-assisted programming.

---

## Key Decisions

### Dataset Curation
- Only **primary empirical studies (A1, A2, some B)** are included in Results.
- Secondary studies (Surveys, SLRs) are moved to **Background / Related Work**.
- Weak studies are removed.

### Replacement Strategy
- Low-quality or secondary papers replaced with stronger empirical studies.
- Maintained dataset size (~100 papers) for consistency.

---

## Final High-Value Papers Added

### Paper_105
- Liu et al., 2024
- Large-scale empirical study (TSE)
- Focus: code correctness, generalization, multi-round fixing
- Classification: **A1**

### Paper_106
- Khojah et al., 2024
- Observational study (FSE)
- Focus: real-world developer usage
- Classification: **A1**

### Paper_107
- Aguiar et al., 2024
- DevGPT dataset analysis
- Focus: multi-language development behavior
- Classification: **A2**

### Paper_108
- Tang et al., 2024
- Controlled experiment with developers
- Focus: debugging behavior + cognition
- Classification: **A2**

### Paper_109
- Zheng et al., 2025
- HumanEvo benchmark
- Focus: realistic evaluation of LLM performance
- Classification: **A1**

---

## Key Insights Across Papers

### 1. Overestimation of LLM Performance
- Benchmarks may inflate results by **10%–61%**.

### 2. Limited Generalization
- Strong drop in performance on unseen problems.

### 3. Human Role Remains Critical
- Developers use LLMs primarily for:
  - guidance
  - learning
  - debugging

### 4. Multi-language Development
- LLMs encourage cross-language usage (>75% foreign snippets).

### 5. Error Patterns are Structural
- Errors are mostly logical, not syntactic.

### 6. Debugging Behavior Changes
- Increased cognitive load
- Strategy shifts depending on code origin

---

## Methodological Principles Applied

- PRISMA-aligned filtering
- Kitchenham guidelines
- Separation of:
  - Primary vs Secondary evidence
- Emphasis on:
  - reproducibility
  - empirical rigor

---

## Current State

- Dataset: Clean, consistent, high-quality
- Ready for:
  - Results construction
  - Discussion synthesis
  - Theoretical contributions

---

## Next Steps

1. Reconstruct SLR mental map using final Excel
2. Build Results section
3. Develop Discussion (cross-paper insights)
4. Formalize contributions

---

## Notes

- Taulli (2024) used as contextual reference only
- Surveys excluded from quantitative synthesis

---

## End of Document

