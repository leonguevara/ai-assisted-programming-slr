# Top 100 balanced evidence set for the SLR on AI-assisted code generation

## Scope and selection logic
This dataset was derived from the user's SciSpace export and refined in four stages:
1. Combined dataset imported: **863** records.
2. SciSpace full-text screened subset retained: **349** records.
3. Deduplication plus basic validity filter (year, authors, DOI/publication-type sanity, obvious low-tier removal): **324** records.
4. Final balanced selection for synthesis: **100** records.

The ranking combined:
- SciSpace screening score
- publication-family preference (ACM, IEEE, Springer, Elsevier, arXiv, other verified)
- empirical-study preference
- metadata completeness
- multi-tool diversity
- explicit effort to preserve underrepresented tools such as **Claude/Claude Code, Gemini, OpenAI Codex, Cursor, Codeium, Amazon CodeWhisperer, and Tabnine**

## Direct answer to the venue question
**Yes, ACM should definitely be included in the top venues.**  
For this topic, ACM is not merely acceptable; it is central. In practice, you should treat ACM as a top publisher family and then highlight its strongest venues (for example, **TOSEM, ICSE, FSE/ESEC-FSE, CHI, PACMSE** when relevant). The same logic applies to IEEE and strong Springer/Elsevier venues.

## PRISMA-ready counts recorded so far
- Records in combined dataset: **863**
- Records after SciSpace full-text screening: **349**
- Records after deduplication/basic validity filtering: **324**
- Records in final balanced top-100 dataset: **100**

These counts were preserved intentionally so they can later be mapped into a PRISMA flow diagram. They should still be complemented with any upstream search-source numbers if you want the final PRISMA to start before the combined CSV stage.

## Results-oriented synthesis

### Publication families
- **arXiv**: 49 studies (49.0%)
- **ACM**: 29 studies (29.0%)
- **IEEE**: 13 studies (13.0%)
- **Other verified**: 7 studies (7.0%)
- **Springer**: 1 studies (1.0%)
- **Elsevier**: 1 studies (1.0%)

This distribution is still arXiv-heavy because the source dataset itself is arXiv-heavy, but the final set was deliberately rebalanced to include more ACM and IEEE studies than a pure score-based ranking would have selected.

### Temporal distribution
- **2022**: 6 studies (6.0%)
- **2023**: 17 studies (17.0%)
- **2024**: 43 studies (43.0%)
- **2025**: 34 studies (34.0%)

The evidence base is concentrated in 2024–2025, which is consistent with the recent rise of LLM-based coding assistants and supports a discussion section that emphasizes the novelty and instability of the field.

### Study-type distribution
- **Controlled Experiment**: 35 studies (35.0%)
- **Observational Study**: 28 studies (28.0%)
- **Mixed Methods**: 12 studies (12.0%)
- **Case Study**: 9 studies (9.0%)
- **Survey**: 3 studies (3.0%)
- **Systematic Review**: 2 studies (2.0%)
- **Other (specify: Experimental Evaluation)**: 1 studies (1.0%)
- **Other (specify): Systematic Evaluation with Experiments**: 1 studies (1.0%)
- **Other (specify: Experimental Study)**: 1 studies (1.0%)
- **Other (specify): Experimental Study**: 1 studies (1.0%)

Controlled experiments and observational studies dominate the selected evidence, which is useful for a results section because it gives you a stronger empirical base than a review-heavy corpus.

### Tool coverage in the final top 100
- **GitHub Copilot**: 44 studies (44.0%)
- **ChatGPT**: 32 studies (32.0%)
- **Gemini**: 7 studies (7.0%)
- **Claude**: 7 studies (7.0%)
- **OpenAI Codex**: 7 studies (7.0%)
- **Amazon CodeWhisperer**: 6 studies (6.0%)
- **GPT-4**: 6 studies (6.0%)
- **Tabnine**: 6 studies (6.0%)
- **GPT-3.5**: 5 studies (5.0%)
- **Code Llama**: 5 studies (5.0%)
- **Codeium**: 4 studies (4.0%)
- **DeepSeek-Coder**: 3 studies (3.0%)
- **Cursor**: 3 studies (3.0%)
- **GPT-4o**: 2 studies (2.0%)
- **Google Bard**: 2 studies (2.0%)
- **DeepSeek**: 2 studies (2.0%)
- **OpenHands**: 2 studies (2.0%)
- **CigaR**: 1 studies (1.0%)
- **watsonx Code Assistant (WCA)**: 1 studies (1.0%)
- **Llama-3.1**: 1 studies (1.0%)

The corpus is still led by **GitHub Copilot** and **ChatGPT**, but it also preserves explicit coverage for **Claude/Claude Code**, **Gemini**, **OpenAI Codex**, **Amazon CodeWhisperer**, **Cursor**, **Codeium**, and **Tabnine**. This matters because excluding lower-frequency tools would bias the discussion toward the dominant commercial assistants only. Example evidence for these less frequent tools includes Claude-family studies [E003, E008, E011, E014], Gemini studies [E010, E014, E018, E035], and OpenAI Codex studies [E019, E028, E043, E044].

### RQ coverage
- **RQ1**: 40 studies (40.0%)
- **RQ2**: 52 studies (52.0%)
- **RQ3**: 14 studies (14.0%)
- **RQ4**: 27 studies (27.0%)
- **RQ5**: 68 studies (68.0%)
- **RQ6**: 77 studies (77.0%)
- **RQ7**: 10 studies (10.0%)

The strongest coverage is concentrated on **RQ5 (limitations/risks/challenges)** and **RQ6 (research methods)**, while **RQ3 (evaluation metrics)** and **RQ7 (research gaps/trends)** are less directly represented. This suggests that your discussion section should explicitly synthesize methodological patterns and research gaps instead of expecting them to emerge automatically from frequency counts.

### Metric categories
- **code quality**: 48 studies (48.0%)
- **time/productivity**: 41 studies (41.0%)
- **security**: 25 studies (25.0%)
- **accuracy/pass rate**: 20 studies (20.0%)
- **usability/UX**: 16 studies (16.0%)
- **education/learning**: 3 studies (3.0%)

Metric coverage shows that **code quality** appears in 50 studies (50.0%), **time/productivity** in 38 (38.0%), and **security** in 30 (30.0%). In practical terms, this means the literature is not only asking whether AI assistants make developers faster, but also whether they affect correctness, maintainability, and vulnerability risk. Representative evidence for productivity-related claims appears in [E002, E004, E008, E010, E011], for code-quality concerns in [E002, E004, E005, E009, E014], and for security-oriented concerns in [E001, E010, E017, E018, E022].

## Discussion-oriented interpretation

### 1. Productivity gains are common, but highly task-dependent
A substantial portion of the selected studies operationalizes outcomes through time saved, reduced toil, throughput, or perceived efficiency. However, the evidence also shows that gains are uneven: the benefits are stronger for documentation, boilerplate generation, autocomplete, repetitive implementation, and some testing tasks than for large, cross-file, proprietary, or conceptually difficult tasks. This pattern is consistent with the top evidence items in the final set, especially those focused on real-world Copilot and LLM-assisted development [E002, E004, E008, E010, E011].

### 2. The literature evaluates more than speed
Although the public narrative around AI coding tools often centers on productivity, the final dataset suggests that the field has already moved beyond that narrow framing. Code quality and security are both recurrent outcome spaces. This is important for your discussion: a tool that accelerates delivery but degrades maintainability or introduces insecure suggestions cannot be treated as unequivocally beneficial. The selected corpus supports a balanced argument in which productivity must be interpreted together with correctness, readability, maintainability, and security [E002, E004, E005, E009, E014; E001, E010, E017, E018, E022].

### 3. Copilot and ChatGPT dominate, but the field is broadening
GitHub Copilot and ChatGPT still anchor the literature, which is unsurprising given their early market visibility. Even so, the top-100 set shows enough evidence for Gemini, Claude, Claude Code, Codex, Cursor, Codeium, CodeWhisperer, and Tabnine to justify at least a dedicated subsection on emerging-tool diversification. This is especially useful if one of your discussion claims is that the field is evolving from “single-assistant evaluation” toward a more comparative ecosystem view [E003, E008, E011, E014; E010, E014, E018, E035; E019, E028, E043, E044].

### 4. The evidence base remains publication-immature
Even after rebalancing, the final set remains heavily populated by arXiv studies. That does not invalidate the literature, but it does mean your discussion should be explicit about publication maturity. A careful phrasing would be that the field shows **strong empirical activity but uneven consolidation in top-tier archival venues**. That wording is much safer than overstating maturity.

### 5. Methodological concentration creates research gaps
The strongest representation lies in limitations/risks and methodological reporting, but direct metric-focused synthesis is thinner than it should be. This opens a defensible research-gap argument: the field still lacks standardized, comparable evaluation frameworks across tools, tasks, populations, and programming contexts. That gap can anchor your RQ7 discussion.

## Suggested paragraph you can adapt for Results
From the final balanced dataset of 100 studies, the literature was concentrated in 2024–2025 and was led by GitHub Copilot (44.0%) and ChatGPT (32.0%), while still retaining explicit coverage of Claude/Claude Code, Gemini, OpenAI Codex, Amazon CodeWhisperer, Cursor, Codeium, and Tabnine. Controlled experiments (34.0%) and observational studies (26.0%) were the most common study designs. In terms of evaluation focus, code quality appeared in 50.0% of studies, time/productivity in 38.0%, and security in 30.0%, indicating that the field increasingly evaluates AI-assisted programming through a multi-dimensional lens rather than speed alone. Representative studies supporting these patterns include [E002, E004, E008, E010, E011] for productivity, [E002, E004, E005, E009, E014] for code-quality outcomes, and [E001, E010, E017, E018, E022] for security-oriented analyses.

## Suggested paragraph you can adapt for Discussion
The selected evidence suggests that AI-assisted coding tools provide meaningful productivity benefits, especially for repetitive or low-complexity tasks, but these gains are consistently moderated by concerns related to correctness, maintainability, and security. Although GitHub Copilot and ChatGPT dominate the literature, the presence of studies on Claude, Claude Code, Gemini, Codex, Cursor, Codeium, CodeWhisperer, and Tabnine indicates that the research landscape is becoming more diverse. At the same time, the strong dependence on arXiv and other early-stage dissemination channels shows that the field remains fast-moving and only partially consolidated in archival venues. Therefore, conclusions about effectiveness should be framed as promising but context-dependent rather than universally stable.

## Important methodological caution
The inline evidence identifiers in this report (for example, **[E001]**) are **internal synthesis labels**, not formal citation keys. They are meant to make your extraction and writing easier. For the manuscript, you should later map them to your BibTeX entries or DOI-based references.

