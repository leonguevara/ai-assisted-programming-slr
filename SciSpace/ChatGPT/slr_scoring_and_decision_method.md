# SLR scoring and decision method

## What can be reconstructed faithfully
The available files allow reconstruction of:
- exported SciSpace **title/abstract screening scores** when they appear explicitly in the text fields
- exported SciSpace **full-text screening scores** when they appear explicitly
- our own downstream ranking logic used to reduce the dataset to a balanced final top 100

## What cannot be reconstructed exactly
SciSpace's internal scoring mechanism is **not transparent in the export**. Therefore:
- the numeric scores shown in the files were preserved
- but the exact proprietary formula used by SciSpace to generate those scores cannot be reverse engineered honestly from the available artifacts

## Dataset states recorded
- Combined dataset imported: **863**
- Records present in `fulltext_screened_filtered.csv`: **349**
- Records after deduplication + basic validity filtering: **324**
- Final balanced top-100 evidence set: **100**

## Our downstream score
For records in the full-text screened set, the downstream ranking score was:

`overall_score2 = SciSpace score * 10 + venue_score + study_score + meta_score + diversity_score + rq_score + pub_bonus`

Where:
- **SciSpace score** = full-text score if available; otherwise title/abstract score
- **venue_score** = heuristic preference for top software engineering venues / trustworthy publisher signals, with penalties for suspicious or low-tier signals
- **study_score** = heuristic preference for stronger empirical designs (experiments > observational/surveys/case studies > reviews > other)
- **meta_score** = metadata completeness and recency (DOI presence, abstract presence, publication year)
- **diversity_score** = modest reward for explicit tool diversity, especially underrepresented tools such as Claude/Claude Code, Gemini, OpenAI Codex, Cursor, Codeium, Tabnine, Amazon CodeWhisperer
- **rq_score** = reward for explicit research-question coverage in the SciSpace export
- **pub_bonus** = balancing preference for publication families (ACM, IEEE, Springer, Elsevier, arXiv, other verified)

## Why papers were marked as included or rejected
Each paper in the audit table has one of four statuses:
1. **Included in final Top100**
2. **Included after validity filtering, excluded from final Top100**
3. **Rejected after validity filtering**
4. **Rejected before/at SciSpace full-text stage**

### Included in final Top100
A paper reached the final set if it:
- survived full-text screening
- passed deduplication/basic validity checks
- ranked highly under the combined downstream score
- fit the balancing constraints used to avoid over-dominance of a few tools and publication families

### Included after validity filtering, excluded from final Top100
A paper reached the high-quality candidate pool but was not selected into the final 100 because:
- it ranked below the final cutoff after balancing
- or its inclusion would have worsened publication-family or tool-coverage balance

### Rejected after validity filtering
A paper was removed at this stage because of at least one of the following:
- missing/invalid publication year or outside the 2021+ window
- missing trustworthy DOI/publication-type evidence
- suspicious/low-tier venue or publisher signal

### Rejected before/at SciSpace full-text stage
These papers appeared in the combined export but not in the `fulltext_screened_filtered.csv` export. That means they were likely screened out by SciSpace during title/abstract or full-text screening. The exact exclusion trigger is **not always inferable** from the available files.

## Important caution for the manuscript
The audit table is rigorous as a **traceability artifact**, but when writing the paper you should avoid claiming that SciSpace used our downstream score. It did not.  
Instead, describe the process as:
- SciSpace produced screening scores and initial screening decisions
- we then performed an additional researcher-controlled filtering, validation, and balancing stage to construct the final evidence set
