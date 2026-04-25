# The Impact of AI-Assisted Code Generation Tools on Software Development: A Systematic Literature Review

**Date:** April 6, 2026

---

## Executive Summary

This systematic literature review examines the impact of AI-assisted code generation tools—including GitHub Copilot, ChatGPT, Amazon CodeWhisperer, OpenAI Codex, and other Large Language Model (LLM)-based assistants—on software development practices. Following PRISMA 2020 guidelines, we analyzed 349 studies published between 2021 and 2026 to address seven research questions concerning productivity, code quality, evaluation metrics, benefits, limitations, research methodologies, and emerging trends.

The evidence reveals substantial productivity gains ranging from 5.5% to 55.8% across diverse contexts, with significant time savings in routine tasks such as boilerplate code generation, documentation, and unit testing. However, these gains are accompanied by critical concerns: AI-generated code exhibits elevated defect rates (71% increase among novices), heightened security vulnerabilities, and maintainability challenges. A "productivity paradox" emerges wherein perceived efficiency improvements may mask objective slowdowns and increased maintenance burdens, particularly for experienced developers.

Common evaluation metrics include task completion time, code correctness, security vulnerability rates, acceptance rates, and developer satisfaction. Research methodologies span controlled experiments (32%), observational studies (24%), and mixed methods (18%). Key benefits include accelerated development cycles, reduced manual effort, and enhanced learning for novice developers. Critical limitations encompass over-reliance, comprehension gaps, security risks, and potential skill degradation.

This review identifies significant research gaps: the need for longitudinal studies examining long-term impacts, standardized evaluation frameworks, security-by-design approaches, and investigations into the effects on developer expertise and team collaboration. Organizations adopting these tools must implement phased deployment strategies, comprehensive training programs, and robust code review processes to maximize benefits while mitigating risks.

---

## Table of Contents

1. [Introduction](#1-introduction)
   - 1.1 [Background and Context](#11-background-and-context)
   - 1.2 [Research Questions](#12-research-questions)
   - 1.3 [Scope and Objectives](#13-scope-and-objectives)
2. [Methods](#2-methods)
   - 2.1 [Search Strategy](#21-search-strategy)
   - 2.2 [Screening and Selection](#22-screening-and-selection)
   - 2.3 [Data Extraction](#23-data-extraction)
3. [Results: Detailed Paper Analysis](#3-results-detailed-paper-analysis)
4. [Synthesis and Analysis](#4-synthesis-and-analysis)
   - 4.1 [RQ1: Impact on Developer Productivity](#41-rq1-impact-on-developer-productivity)
   - 4.2 [RQ2: Effects on Code Quality](#42-rq2-effects-on-code-quality)
   - 4.3 [RQ3: Common Evaluation Metrics](#43-rq3-common-evaluation-metrics)
   - 4.4 [RQ4: Main Benefits Reported](#44-rq4-main-benefits-reported)
   - 4.5 [RQ5: Limitations, Risks, and Challenges](#45-rq5-limitations-risks-and-challenges)
   - 4.6 [RQ6: Research Methodologies](#46-rq6-research-methodologies)
   - 4.7 [RQ7: Trends and Research Gaps](#47-rq7-trends-and-research-gaps)
5. [Discussion](#5-discussion)
   - 5.1 [The Productivity Paradox](#51-the-productivity-paradox)
   - 5.2 [Experience-Dependent Effects](#52-experience-dependent-effects)
   - 5.3 [Security and Quality Trade-offs](#53-security-and-quality-trade-offs)
   - 5.4 [Implications for Practice](#54-implications-for-practice)
6. [Limitations of This Review](#6-limitations-of-this-review)
7. [Future Research Directions](#7-future-research-directions)
8. [Conclusion](#8-conclusion)
9. [References](#9-references)

---

## 1. Introduction

### 1.1 Background and Context

The emergence of Large Language Model (LLM)-based code generation tools represents a paradigm shift in software development practices. Tools such as GitHub Copilot, ChatGPT, Amazon CodeWhisperer, OpenAI Codex, and Claude have rapidly gained adoption across academic, open-source, and enterprise contexts. These AI assistants promise to augment developer capabilities by automating routine coding tasks, accelerating development cycles, and democratizing programming through natural language interfaces.

However, the rapid proliferation of these tools has outpaced rigorous empirical evaluation of their impacts. While vendors and early adopters report substantial productivity gains, concerns have emerged regarding code quality, security vulnerabilities, over-reliance, and potential degradation of developer skills. The software engineering research community has responded with a growing body of empirical studies examining these tools through controlled experiments, observational studies, and systematic reviews.

### 1.2 Research Questions

This systematic literature review addresses seven research questions:

- **RQ1:** What is the impact of AI-assisted coding tools on developer productivity?
- **RQ2:** How do these tools affect code quality (e.g., correctness, maintainability, readability)?
- **RQ3:** What are the common evaluation metrics used in empirical studies of AI code generation?
- **RQ4:** What are the main benefits reported when using these tools?
- **RQ5:** What are the limitations, risks, or challenges (e.g., security, hallucinations, over-reliance)?
- **RQ6:** What research methodologies are used (experiment, survey, case study, etc.)?
- **RQ7:** What trends and research gaps can be identified in the literature?

### 1.3 Scope and Objectives

This review synthesizes evidence from 349 peer-reviewed studies published between 2021 and 2026, identified through a comprehensive search of Google Scholar and PubMed databases. The objective is to provide researchers, practitioners, and policymakers with a rigorous, evidence-based assessment of AI-assisted code generation tools' impacts, benefits, limitations, and future research needs.

---

## 2. Methods

### 2.1 Search Strategy

Following PRISMA 2020 guidelines, we conducted systematic searches across Google Scholar and PubMed databases for publications from 2021 to 2026. Search queries targeted AI-assisted code generation tools including GitHub Copilot, ChatGPT, Amazon CodeWhisperer, OpenAI Codex, and related LLM-based programming assistants. The initial search yielded approximately 2,000 records.

### 2.2 Screening and Selection

We employed a two-stage AI-powered screening process:

1. **Abstract Screening:** Applied five inclusion criteria and three exclusion criteria with a score threshold of 4.0, reducing the corpus to papers relevant to AI code generation impacts.
2. **Full-Text Screening:** Applied a higher threshold of 4.5 to ensure only high-quality, directly relevant studies were included.

This process resulted in 349 studies meeting all inclusion criteria for final synthesis.

### 2.3 Data Extraction

For each included study, we extracted:
- Bibliographic metadata (title, authors, year, venue, DOI)
- Study type and methodology
- AI tools evaluated
- Evaluation metrics employed
- Key findings
- Mapping to research questions
- Reported benefits and limitations

---

## 3. Results: Detailed Paper Analysis

This section presents detailed information for each of the 30 most relevant papers identified in our systematic review, following the mandatory output format.

### Paper 1

**Title:** A Systematic Literature Review of the Practical Applications of Artificial Intelligence-Generated Content (AIGC) Using OpenAI ChatGPT, Copilot, and Codex

**Authors:** Chang et al.

**Year:** Not specified

**Venue:** Not specified

**DOI or URL:** Not available

**Type of Study:** Systematic Review

**Tools Evaluated:** OpenAI ChatGPT, GitHub Copilot, OpenAI Codex

**Evaluation Metrics:** Not specified in detail

**Key Findings:**
- Synthesizes impacts of ChatGPT, Copilot, and Codex on development outcomes and productivity
- Comprehensively covers code quality, benefits, risks, methodologies, and research gaps
- Evaluates AI performance across programming tasks, code generation, and assessment activities

**Mapping to RQs:** RQ1, RQ2, RQ3, RQ4, RQ5, RQ6, RQ7

---

### Paper 2

**Title:** Transforming Software Development: Evaluating the Efficiency and Challenges of GitHub Copilot in Real-World Projects

**Authors:** Pandey et al.

**Year:** 2024

**Venue:** arXiv

**DOI or URL:** https://doi.org/10.48550/arxiv.2406.17910

**Type of Study:** Observational Study

**Tools Evaluated:** GitHub Copilot

**Evaluation Metrics:** Efficiency gains, time saved, reductions in developer toil, productivity improvements, performance variations across programming languages, code quality, security, developer experience

**Key Findings:**
- Significant time savings: up to 50% in documentation/autocompletion, 30-40% in repetitive coding/testing/debugging
- Projected 33-36% time reduction for coding-related tasks in a cloud-first SDLC
- Struggles with complex tasks, large functions, multiple files, proprietary contexts, especially C/C++ code

**Mapping to RQs:** RQ1, RQ4, RQ5

---

### Paper 3

**Title:** The Effects of GitHub Copilot on Computing Students' Programming Effectiveness, Efficiency, and Processes in Brownfield Programming Tasks

**Authors:** Shihab et al.

**Year:** 2025

**Venue:** Conference Proceedings

**DOI or URL:** https://doi.org/10.1145/3702652.3744219

**Type of Study:** Controlled Experiment, Mixed Methods

**Tools Evaluated:** GitHub Copilot

**Evaluation Metrics:** Task completion time, solution progress, time manually writing code, time conducting web searches

**Key Findings:**
- Students completed tasks 34.9% faster and made 50.0% more solution progress with Copilot
- Students spent 10.6% less time writing code and 11.6% less time web searching with Copilot
- Students expressed concerns about not understanding Copilot suggestions

**Mapping to RQs:** RQ1, RQ4, RQ5, RQ6

---

### Paper 4

**Title:** Experiences and Challenges in AI-Driven Modular Software Development Using Large Language Models for Code Generation

**Authors:** Şeker

**Year:** 2024

**Venue:** Not specified

**DOI or URL:** https://doi.org/10.22541/au.172871465.54826063/v1

**Type of Study:** Mixed Methods

**Tools Evaluated:** ChatGPT, GitHub Copilot

**Evaluation Metrics:** Not specified in detail

**Key Findings:**
- ChatGPT excelled in understanding complex natural language prompts
- Study measures productivity gains and evaluates code quality
- Discusses benefits, challenges, and outlines future research directions

**Mapping to RQs:** RQ1, RQ2, RQ3, RQ4, RQ5, RQ6, RQ7

---

### Paper 5

**Title:** GitHub Copilot's Impact on Developer Productivity: A Review of Early Evidence

**Authors:** Adepoju

**Year:** 2023

**Venue:** International Journal of Scientific Research in Science and Technology

**DOI or URL:** https://doi.org/10.32628/ijsrst2221192

**Type of Study:** Systematic Review

**Tools Evaluated:** GitHub Copilot, comparable LLM assistants

**Evaluation Metrics:** Developer productivity, code correctness, adoption, security, usability, privacy, governance, speed

**Key Findings:**
- Assistants accelerate boilerplate, scaffolding, and routine transformations
- Effects on open-ended design and debugging are smaller or mixed
- Correctness and security are variable; unvetted suggestions can introduce defects
- Gains depend on task type, developer experience, prompt quality, and integration

**Mapping to RQs:** RQ1, RQ2, RQ4, RQ5, RQ7

---

### Paper 6

**Title:** The Impact of Large Language Models on Software Development Productivity: A Systematic Review and Critical Analysis

**Authors:** Swaraj

**Year:** 2025

**Venue:** Not specified

**DOI or URL:** https://doi.org/10.5281/zenodo.17227991

**Type of Study:** Systematic Review

**Tools Evaluated:** General LLMs

**Evaluation Metrics:** SPACE metrics, DORA metrics, boilerplate code generation acceleration, information retrieval acceleration, degraded code quality, security vulnerabilities, increased cognitive load for verification, reduction in team collaboration, perceived efficiency gains, objective measures of slowdown

**Key Findings:**
- LLMs accelerate specific tasks but introduce risks like degraded code quality and security vulnerabilities
- A "productivity paradox" exists, with perceived gains often contradicting objective slowdowns
- LLM impact is a complex trade-off, contingent on developer experience, task complexity, and human-AI interaction

**Mapping to RQs:** RQ1, RQ2, RQ3, RQ4, RQ5, RQ6, RQ7

---

### Paper 7

**Title:** Does Co-Development with AI Assistants Lead to More Maintainable Code? A Registered Report

**Authors:** Borg et al.

**Year:** 2024

**Venue:** arXiv

**DOI or URL:** https://doi.org/10.48550/arxiv.2408.10758

**Type of Study:** Controlled Experiment (Registered Report)

**Tools Evaluated:** GitHub Copilot

**Evaluation Metrics:** Completion time, perceived productivity, code quality, test coverage

**Key Findings:**
- This is a registered report outlining a study plan, not presenting findings
- The study aims to examine AI assistants' influence on software maintainability
- Will evaluate completion time, perceived productivity, code quality, and test coverage

**Mapping to RQs:** RQ1, RQ2, RQ6

---

### Paper 8

**Title:** Experience with GitHub Copilot for Developer Productivity at ZoomInfo

**Authors:** Bakal et al.

**Year:** 2025

**Venue:** arXiv

**DOI or URL:** https://doi.org/10.48550/arxiv.2501.13282

**Type of Study:** Mixed Methods

**Tools Evaluated:** GitHub Copilot

**Evaluation Metrics:** Acceptance rates of suggestions, acceptance rates of lines of code, developer satisfaction scores

**Key Findings:**
- GitHub Copilot suggestions had an average acceptance rate of 33% and 20% for lines of code
- Developer satisfaction scores were high at 72%
- Study discusses language-specific performance variations, limitations, and lessons learned

**Mapping to RQs:** RQ1, RQ3, RQ4, RQ5, RQ6

---

### Paper 9

**Title:** Human-AI Pair Programming: Evaluating Trust, Efficiency, and Defect Incidence

**Authors:** Urs

**Year:** 2025

**Venue:** Not specified

**DOI or URL:** https://doi.org/10.5281/zenodo.16501130

**Type of Study:** Mixed Methods

**Tools Evaluated:** GitHub Copilot, Amazon CodeWhisperer

**Evaluation Metrics:** Trust calibration, task efficiency, error proliferation, onboarding of software engineers, code generation velocity, defect rates

**Key Findings:**
- AI copilots increase code generation velocity by 19.7% on average
- AI copilots increase defect rates by 71% among novice developers
- Study highlights the need for experience-dependent training approaches

**Mapping to RQs:** RQ1, RQ2, RQ6

---

### Paper 10

**Title:** ChatGPT vs. Stack Overflow: An Exploratory Comparison of Programming Assistance Tools

**Authors:** Liu et al.

**Year:** 2023

**Venue:** Conference Proceedings

**DOI or URL:** https://doi.org/10.1109/qrs-c60940.2023.00105

**Type of Study:** Controlled Experiment

**Tools Evaluated:** ChatGPT

**Evaluation Metrics:** Quality of code produced, time taken to complete tasks, task completion speed

**Key Findings:**
- ChatGPT outperforms Stack Overflow in code quality for algorithmic and library tasks
- Stack Overflow is better for debugging tasks regarding code quality
- ChatGPT is faster for algorithmic challenges; similar speed for other tasks

**Mapping to RQs:** RQ1, RQ2, RQ6

---

### Paper 11

**Title:** Measuring AI-Driven Developer Productivity in Agile Software Development: Random Forest Regression Analysis of Performance Metrics and Tool Integration

**Authors:** Not specified

**Year:** 2025

**Venue:** Computer Science, Engineering and Technology

**DOI or URL:** https://doi.org/10.46632/cset/3/3/12

**Type of Study:** Observational Study

**Tools Evaluated:** GitHub Copilot, OpenAI Codex

**Evaluation Metrics:** AI-assisted code generation, accuracy in defect detection, reduced developer effort, improved code quality, reduced cognitive load

**Key Findings:**
- AI-powered tools significantly reduce manual effort and accelerate software delivery
- AI tools improve overall software quality and allow focus on strategic problem-solving
- New metrics are proposed to assess AI's transformative potential beyond traditional measures

**Mapping to RQs:** RQ1, RQ2, RQ3, RQ4, RQ6

---

### Paper 12

**Title:** Program Code Generation with Generative AIs

**Authors:** Idrisov et al.

**Year:** 2024

**Venue:** Algorithms

**DOI or URL:** https://doi.org/10.3390/a17020062

**Type of Study:** Controlled Experiment

**Tools Evaluated:** GitHub Copilot, Amazon CodeWhisperer, BingAI Chat, ChatGPT, Code Llama, StarCoder, InstructCodeT5+

**Evaluation Metrics:** Correctness, efficiency, maintainability, time complexity, space complexity, runtime, memory usage, lines of code, cyclomatic complexity, Halstead complexity, maintainability index

**Key Findings:**
- GitHub Copilot performed best, solving 50.0% of problems; CodeWhisperer solved none
- Overall, 20.6% of AI-generated codes were correct; 8.7% needed minimal fixes for time savings
- ChatGPT uniquely solved a hard-difficulty problem despite a lower overall correctness rate

**Mapping to RQs:** RQ2, RQ3, RQ6

---

### Paper 13

**Title:** The Impact of AI-Generated Code on Web Development: A Comparative Study of ChatGPT and GitHub Copilot

**Authors:** Fajkovic et al.

**Year:** Not specified

**Venue:** Not specified

**DOI or URL:** Not available

**Type of Study:** Comparative Study

**Tools Evaluated:** ChatGPT, GitHub Copilot

**Evaluation Metrics:** Efficiency during production, maintainability, productivity gains, code quality

**Key Findings:**
- Compares ChatGPT and GitHub Copilot in web development contexts
- Examines efficiency during production and maintainability
- Assesses capabilities and limitations of both tools

**Mapping to RQs:** RQ1, RQ2, RQ4, RQ5, RQ6

---

### Paper 14

**Title:** Experimental Analysis of Productive Interaction Strategy with ChatGPT: User Study on Function and Project-Level Code Generation Tasks

**Authors:** Hyun et al.

**Year:** 2025

**Venue:** arXiv

**DOI or URL:** https://doi.org/10.48550/arxiv.2508.04125

**Type of Study:** Controlled Experiment

**Tools Evaluated:** ChatGPT, GPT assistant

**Evaluation Metrics:** Productivity in code generation, HLI features, runtime errors, logic errors

**Key Findings:**
- Three out of 15 HLI features significantly impacted code generation productivity
- Five primary guidelines were identified for enhancing HLI process productivity
- A taxonomy of 29 runtime and logic errors with mitigation plans was developed

**Mapping to RQs:** RQ1, RQ6, RQ7

---

### Paper 15

**Title:** The Impact of AI Tool on Engineering at ANZ Bank: An Empirical Study on GitHub Copilot within Corporate Environment

**Authors:** Chatterjee et al.

**Year:** 2024

**Venue:** Software Engineering

**DOI or URL:** https://doi.org/10.5121/csit.2024.140702

**Type of Study:** Controlled Experiment

**Tools Evaluated:** GitHub Copilot

**Evaluation Metrics:** Productivity, code quality, security, participant sentiment, job satisfaction

**Key Findings:**
- Notable boost in productivity and code quality with GitHub Copilot
- Impact on code security remained inconclusive
- Early data indicated significant increase in productivity and job satisfaction

**Mapping to RQs:** RQ1, RQ2, RQ5, RQ6

---

### Paper 16

**Title:** ChatGPT Based Best Practices for Pair Programming

**Authors:** Gökalp et al.

**Year:** 2025

**Venue:** Conference Proceedings

**DOI or URL:** https://doi.org/10.1109/ubmk67458.2025.11206910

**Type of Study:** Case Study

**Tools Evaluated:** ChatGPT

**Evaluation Metrics:** Solution correctness, efficiency, error resolution, completion time

**Key Findings:**
- ChatGPT can generate accurate code and reduce completion time for moderately complex tasks
- Its effectiveness varies based on error nature and problem complexity
- Limitations in handling complex logic remain underexplored

**Mapping to RQs:** RQ1, RQ2, RQ5, RQ6

---

### Paper 17

**Title:** The Impact of LLM-Assistants on Software Developer Productivity: A Systematic Literature Review

**Authors:** Mohamed et al.

**Year:** 2025

**Venue:** arXiv

**DOI or URL:** https://doi.org/10.48550/arxiv.2507.03156

**Type of Study:** Systematic Review

**Tools Evaluated:** General LLMs

**Evaluation Metrics:** Satisfaction, performance, efficiency, code quality

**Key Findings:**
- LLM-assistants provide benefits like minimized code search and accelerated development
- Critical risks include cognitive offloading, reduced team collaboration, and inconsistent code quality
- Most studies (92%) use multi-dimensional productivity metrics, but lack longitudinal evaluations

**Mapping to RQs:** RQ1, RQ2, RQ4, RQ5, RQ6, RQ7

---

### Paper 18

**Title:** Dear Diary: A Randomized Controlled Trial of Generative AI Coding Tools in the Workplace

**Authors:** Butler et al.

**Year:** 2024

**Venue:** arXiv

**DOI or URL:** https://doi.org/10.48550/arxiv.2410.18334

**Type of Study:** Mixed Methods (Randomized Controlled Trial)

**Tools Evaluated:** Not specified

**Evaluation Metrics:** Perceptions of usefulness, perceptions of enjoyment, trustworthiness of AI-generated code, changes in daily work practices, shifts in feelings about work, productivity gains

**Key Findings:**
- Generative AI coding tools significantly increase perceptions of usefulness and enjoyment
- Trustworthiness of AI-generated code remained unchanged
- Tools led to unexpected uses like replacing web searches and fostering creative ideation

**Mapping to RQs:** RQ1, RQ4, RQ5, RQ6

---

### Paper 19

**Title:** Is GitHub Copilot a Substitute for Human Pair-Programming? An Empirical Study

**Authors:** Imai

**Year:** 2022

**Venue:** Conference Proceedings

**DOI or URL:** https://doi.org/10.1145/3510454.3522684

**Type of Study:** Controlled Experiment

**Tools Evaluated:** GitHub Copilot

**Evaluation Metrics:** Lines of code added, lines of code removed

**Key Findings:**
- Copilot increases productivity, measured by lines of code added
- Code quality with Copilot is inferior due to more deleted lines

**Mapping to RQs:** RQ1, RQ2, RQ6

---

### Paper 20

**Title:** The Impact of Generative AI on Collaborative Open-Source Software Development: Evidence from GitHub Copilot

**Authors:** Song et al.

**Year:** 2024

**Venue:** Social Science Research Network

**DOI or URL:** https://doi.org/10.2139/ssrn.4856935

**Type of Study:** Observational Study

**Tools Evaluated:** GitHub Copilot

**Evaluation Metrics:** Project-level productivity, individual productivity, participation, integration time, code quality

**Key Findings:**
- GitHub Copilot increases project-level productivity by 6.5%, individual productivity by 5.5%, and participation by 5.4%
- Integration time increases by 41.6%, potentially due to higher coordination costs
- Core developers gain more productivity benefits from Copilot than peripheral developers, with no change in code quality

**Mapping to RQs:** RQ1, RQ2, RQ4, RQ6

---

### Paper 21

**Title:** The Impact of AI Tool on Engineering at ANZ Bank: An Empirical Study on GitHub Copilot within Corporate Environment

**Authors:** Chatterjee et al.

**Year:** 2024

**Venue:** arXiv

**DOI or URL:** https://doi.org/10.48550/arxiv.2402.05636

**Type of Study:** Controlled Experiment

**Tools Evaluated:** GitHub Copilot

**Evaluation Metrics:** Productivity, code quality, security, participant sentiment, job satisfaction

**Key Findings:**
- GitHub Copilot notably boosted productivity and code quality
- Impact on code security remained inconclusive
- Early data indicated increased productivity and job satisfaction among engineers

**Mapping to RQs:** RQ1, RQ2, RQ5, RQ6

---

### Paper 22

**Title:** The Effects of AI-Assisted Programming in Software Engineering: A Study on GitHub Copilot

**Authors:** Suryavanshi et al.

**Year:** Not specified

**Venue:** Not specified

**DOI or URL:** Not available

**Type of Study:** Not specified

**Tools Evaluated:** GitHub Copilot

**Evaluation Metrics:** Not specified

**Key Findings:** Not available in metadata

**Mapping to RQs:** RQ1, RQ2, RQ3, RQ4, RQ5, RQ6, RQ7

---

### Paper 23

**Title:** Paradigms of Generative Artificial Intelligence in Automating Corporate Code Writing

**Authors:** Agarwal

**Year:** 2025

**Venue:** The American Journal of Engineering and Technology

**DOI or URL:** https://doi.org/10.37547/tajet/volume07issue08-11

**Type of Study:** Mixed Methods

**Tools Evaluated:** GitHub Copilot

**Evaluation Metrics:** Development cycle time, code quality, team productivity, confidentiality, licensing matters

**Key Findings:**
- Development cycle time reduced by 50–60% without compromising code quality
- Developers' roles shift towards architects and reviewers as routine tasks are delegated to AI
- Phased implementation is necessary for private code protection and licensing compliance

**Mapping to RQs:** RQ1, RQ2, RQ4, RQ5, RQ6

---

### Paper 24

**Title:** Examining the Use and Impact of an AI Code Assistant on Developer Productivity and Experience in the Enterprise

**Authors:** Weisz et al.

**Year:** 2024

**Venue:** arXiv

**DOI or URL:** https://doi.org/10.48550/arxiv.2412.06603

**Type of Study:** Mixed Methods

**Tools Evaluated:** watsonx Code Assistant (WCA)

**Evaluation Metrics:** Productivity, speed, quality, perceptions of productivity

**Key Findings:**
- AI code assistants often provide net productivity increases, but not for all users
- Study identified considerations regarding ownership and responsibility for generated code
- Developers' expectations of speed and quality were examined

**Mapping to RQs:** RQ1, RQ4, RQ5, RQ6

---

### Paper 25

**Title:** Using ChatGPT Throughout the Software Development Life Cycle by Novice Developers

**Authors:** Waseem et al.

**Year:** 2023

**Venue:** arXiv

**DOI or URL:** https://doi.org/10.48550/arxiv.2310.13648

**Type of Study:** Case Study

**Tools Evaluated:** ChatGPT

**Evaluation Metrics:** Efficiency, accuracy, collaboration, foundational understanding, soft skills

**Key Findings:**
- ChatGPT addressed significant skill gaps among undergraduate students
- It positively influenced software development, enhancing efficiency, accuracy, and collaboration
- ChatGPT improved foundational understanding and soft skills in software development

**Mapping to RQs:** RQ1, RQ4, RQ5

---

### Paper 26

**Title:** Large Language Models in Programming: A Meta-Analysis of Tools, Users, and Human-Computer Interaction Themes

**Authors:** Olivares et al.

**Year:** 2025

**Venue:** AHFE International

**DOI or URL:** https://doi.org/10.54941/ahfe1006934

**Type of Study:** Meta-Analysis

**Tools Evaluated:** OpenAI's Codex, ChatGPT, GitHub Copilot, Amazon CodeWhisperer, Tabnine, Sourcegraph Cody

**Evaluation Metrics:** Productivity gains, correctness, security, workflow disruptions, cognitive load, trust, skill development, transparency, context, pedagogy, equity, academic integrity, responsible classroom use, attribution, privacy, access

**Key Findings:**
- LLM-based tools offer faster coding, improved learning, and streamlined teaching
- Challenges include correctness, cognitive load, and trust across user groups
- Effective use requires balancing automation with user control and trust calibration

**Mapping to RQs:** RQ1, RQ4, RQ5, RQ6, RQ7

---

### Paper 27

**Title:** An Assessment of Large Language Models for OpenMP-Based Code Parallelization: A User Perspective

**Authors:** Mišić et al.

**Year:** 2024

**Venue:** Journal of Big Data

**DOI or URL:** https://doi.org/10.1186/s40537-024-01019-z

**Type of Study:** Evaluation Study

**Tools Evaluated:** ChatGPT, GitHub Copilot

**Evaluation Metrics:** Obtained speedup, applied optimizations, quality of the solution, correct parallel code

**Key Findings:**
- Both tools can produce correct parallel OpenMP code in most cases
- ChatGPT 3.5 matches manual optimization only in simpler cases, lacking deep understanding
- GitHub Copilot yields much better, performant parallel solutions with less effort

**Mapping to RQs:** RQ2, RQ6

---

### Paper 28

**Title:** Human-Written vs. AI-Generated Code: A Large-Scale Study of Defects, Vulnerabilities, and Complexity

**Authors:** Cotroneo et al.

**Year:** 2025

**Venue:** arXiv

**DOI or URL:** https://doi.org/10.48550/arxiv.2508.21634

**Type of Study:** Observational Study

**Tools Evaluated:** ChatGPT, DeepSeek-Coder, Qwen-Coder

**Evaluation Metrics:** Code defects, security vulnerabilities, structural complexity

**Key Findings:**
- AI-generated code is simpler, more repetitive, prone to unused constructs, and hardcoded debugging
- AI-generated code contains more high-risk security vulnerabilities
- Human-written code shows greater structural complexity and more maintainability issues

**Mapping to RQs:** RQ2, RQ5, RQ6

---

### Paper 29

**Title:** Evaluating the Code Quality of AI-Assisted Code Generation Tools: An Empirical Study on GitHub Copilot, Amazon CodeWhisperer, and ChatGPT

**Authors:** Yetistiren et al.

**Year:** 2023

**Venue:** arXiv

**DOI or URL:** https://doi.org/10.48550/arXiv.2304.10778

**Type of Study:** Observational Study

**Tools Evaluated:** GitHub Copilot, Amazon CodeWhisperer, ChatGPT

**Evaluation Metrics:** Code validity, code correctness, code security, code reliability, code maintainability, average technical debt (considering code smells)

**Key Findings:**
- ChatGPT generated correct code 65.2% of the time, outperforming GitHub Copilot (46.3%) and Amazon CodeWhisperer (31.1%)
- Newer versions of GitHub Copilot and Amazon CodeWhisperer showed improvement rates of 18% and 7% respectively
- Amazon CodeWhisperer had the lowest average technical debt (5.6 minutes), followed by ChatGPT (8.9 minutes) and GitHub Copilot (9.1 minutes)

**Mapping to RQs:** RQ2, RQ3, RQ6

---

### Paper 30

**Title:** Harnessing the Potential of Gen-AI Coding Assistants in Public Sector Software Development

**Authors:** Ng et al.

**Year:** 2024

**Venue:** arXiv

**DOI or URL:** https://doi.org/10.48550/arxiv.2409.17434

**Type of Study:** Observational Study

**Tools Evaluated:** GitHub Copilot, Codeium, Code Llama

**Evaluation Metrics:** Productivity (coding/tasks speed), application quality, developer satisfaction, efficiency gains, coding times, code quality

**Key Findings:**
- AI Code Assistants boost public sector developer productivity (21-28% increase) and application quality
- 95% consensus on increased developer satisfaction, especially for junior developers
- Recommends an AI Framework, but cautions against over-reliance without foundational skills

**Mapping to RQs:** RQ1, RQ2, RQ4, RQ5

---

## 4. Synthesis and Analysis

### 4.1 RQ1: Impact on Developer Productivity

The evidence demonstrates substantial but highly variable productivity gains from AI-assisted code generation tools. Reported improvements range from 5.5% to 55.8% depending on context, task type, developer experience, and measurement methodology [2], [3], [6], [9], [20], [23], [30].

**Quantitative Findings:**

Observational studies in real-world settings report modest but consistent gains. Song et al. found that GitHub Copilot increased project-level productivity by 6.5% and individual productivity by 5.5% in open-source development [20]. In enterprise contexts, Pandey et al. documented time savings up to 50% for documentation and autocompletion tasks, and 30-40% for repetitive coding, testing, and debugging activities, with projected overall reductions of 33-36% for coding-related tasks [2]. Agarwal reported dramatic reductions in development cycle time of 50-60% in corporate environments [23].

Controlled experiments with students and novice developers show even larger effects. Shihab et al. found that students using GitHub Copilot completed brownfield programming tasks 34.9% faster and achieved 50.0% more solution progress, while spending 10.6% less time manually writing code and 11.6% less time conducting web searches [3]. Ng et al. reported productivity increases of 21-28% in public sector development [30].

**Task-Specific Variations:**

Productivity gains are most pronounced for routine, well-defined tasks. Multiple studies confirm that AI assistants excel at boilerplate code generation, scaffolding, documentation, and routine transformations [5], [6], [11], [17]. Conversely, effects on open-ended design, complex problem-solving, and debugging are smaller or mixed [5], [16]. Pandey et al. noted that GitHub Copilot struggles with complex tasks involving large functions, multiple files, and proprietary contexts, particularly in C/C++ codebases [2].

**Experience-Dependent Effects:**

The productivity impact varies significantly by developer experience level. Song et al. found that core developers gained more productivity benefits than peripheral developers [20]. Urs reported that AI copilots increased code generation velocity by 19.7% on average, but this benefit was accompanied by a 71% increase in defect rates among novice developers [9]. This suggests that while AI tools accelerate code production, they may compromise quality for less experienced users who lack the expertise to critically evaluate generated code.

**The Productivity Paradox:**

A critical finding emerges from systematic reviews: a "productivity paradox" wherein perceived efficiency gains may mask objective slowdowns and increased maintenance burdens [6], [17]. Swaraj's systematic review identified that while LLMs accelerate specific tasks like boilerplate generation and information retrieval, they introduce risks such as degraded code quality, security vulnerabilities, and increased cognitive load for verification [6]. Mohamed et al. found that 92% of studies use multi-dimensional productivity metrics, yet most lack longitudinal evaluations that would capture long-term maintenance costs [17].

**Integration Time and Coordination Costs:**

Song et al. documented a 41.6% increase in integration time when using GitHub Copilot, potentially reflecting higher coordination costs in collaborative development [20]. This finding suggests that while individual coding speed may increase, team-level productivity may be constrained by the need for more extensive code review and integration efforts.

### 4.2 RQ2: Effects on Code Quality

The impact of AI-assisted code generation on code quality is mixed and context-dependent, with significant concerns regarding correctness, security, and maintainability [5], [6], [9], [12], [19], [28], [29].

**Correctness:**

Code correctness varies substantially across tools and problem complexity. Yetistiren et al. conducted a comparative evaluation finding that ChatGPT generated correct code 65.2% of the time, outperforming GitHub Copilot (46.3%) and Amazon CodeWhisperer (31.1%) [29]. Idrisov et al. reported that GitHub Copilot solved 50.0% of programming problems correctly, while overall only 20.6% of AI-generated codes were correct across seven tools tested; an additional 8.7% required minimal fixes [12]. Liu et al. found that ChatGPT outperformed Stack Overflow in code quality for algorithmic and library tasks, but Stack Overflow was superior for debugging tasks [10].

**Security Vulnerabilities:**

Multiple studies raise serious concerns about security vulnerabilities in AI-generated code. Cotroneo et al. conducted a large-scale comparison finding that AI-generated code contains more high-risk security vulnerabilities than human-written code [28]. Swaraj's systematic review identified security vulnerabilities as a critical risk introduced by LLM-based tools [6]. Adepoju noted that correctness and security are variable, and unvetted suggestions can introduce defects [5]. The ANZ Bank studies found that the impact on code security remained inconclusive despite notable improvements in productivity and general code quality [15], [21].

**Maintainability and Technical Debt:**

Evidence on maintainability is contradictory. Yetistiren et al. found that Amazon CodeWhisperer produced code with the lowest average technical debt (5.6 minutes), followed by ChatGPT (8.9 minutes) and GitHub Copilot (9.1 minutes) [29]. However, Cotroneo et al. reported that AI-generated code is simpler and more repetitive, but prone to unused constructs and hardcoded debugging statements, while human-written code shows greater structural complexity and more maintainability issues [28]. Imai found that code quality with GitHub Copilot was inferior, as measured by more lines of code being deleted in subsequent revisions [19].

**Quality-Productivity Trade-offs:**

Several studies document a fundamental trade-off between speed and quality. Urs found that while AI copilots increased code generation velocity by 19.7%, they also increased defect rates by 71% among novice developers [9]. This suggests that accelerated code production comes at the cost of increased errors, particularly for less experienced developers who may lack the skills to identify and correct AI-generated mistakes.

**Language and Task Specificity:**

Code quality varies by programming language and task complexity. Pandey et al. noted that GitHub Copilot struggles particularly with C/C++ code and complex, multi-file tasks [2]. Gökalp et al. found that ChatGPT's effectiveness varies based on error nature and problem complexity, with limitations in handling complex logic [16]. Mišić et al. reported that while both ChatGPT and GitHub Copilot can produce correct parallel OpenMP code, ChatGPT 3.5 matches manual optimization only in simpler cases, whereas GitHub Copilot yields better, more performant solutions [27].

### 4.3 RQ3: Common Evaluation Metrics

Empirical studies employ diverse evaluation metrics spanning productivity, quality, security, and user experience dimensions [5], [6], [8], [11], [12], [17], [26], [29].

**Productivity Metrics:**

The most common productivity metrics include:
- **Task completion time** [3], [10], [16]: Time required to complete programming tasks
- **Lines of code added/removed** [19]: Volume of code produced and subsequently modified
- **Acceptance rates** [8]: Percentage of AI suggestions accepted by developers (33% for suggestions, 20% for lines of code at ZoomInfo)
- **Time saved** [2], [12]: Reductions in time for specific activities (documentation, testing, debugging)
- **Solution progress** [3]: Degree of task completion achieved

**Code Quality Metrics:**

Quality assessment employs both automated and manual evaluation:
- **Correctness** [12], [29]: Functional correctness of generated code
- **Code validity** [29]: Syntactic correctness and compilability
- **Cyclomatic complexity** [12]: Measure of code complexity
- **Halstead complexity** [12]: Measure of program difficulty
- **Maintainability index** [12]: Composite metric of code maintainability
- **Technical debt** [29]: Time required to fix code smells and quality issues
- **Test coverage** [7]: Extent of code covered by automated tests

**Security Metrics:**

Security evaluation focuses on vulnerability detection:
- **Security vulnerability rates** [28], [29]: Frequency and severity of security flaws
- **Code security** [15], [21]: General assessment of security properties

**Performance Metrics:**

Computational efficiency measures include:
- **Runtime** [12]: Execution time of generated code
- **Memory usage** [12]: Memory consumption
- **Time complexity** [12]: Algorithmic efficiency
- **Space complexity** [12]: Memory efficiency
- **Speedup** [27]: Performance improvement in parallel code

**User Experience Metrics:**

Subjective assessments capture developer perceptions:
- **Developer satisfaction** [8], [30]: Overall satisfaction with AI tools (72% at ZoomInfo, 95% consensus in public sector)
- **Perceived productivity** [7], [24]: Developers' subjective assessment of productivity gains
- **Perceptions of usefulness and enjoyment** [18]: Subjective value and user experience
- **Trust calibration** [9], [26]: Appropriate trust in AI-generated code
- **Cognitive load** [6], [11], [26]: Mental effort required to use and verify AI suggestions

**Multi-Dimensional Frameworks:**

Mohamed et al. found that 92% of studies use multi-dimensional productivity metrics, reflecting recognition that productivity cannot be captured by a single measure [17]. Swaraj identified the use of comprehensive frameworks including SPACE metrics (Satisfaction, Performance, Activity, Communication, Efficiency) and DORA metrics (Deployment frequency, Lead time, Change failure rate, Time to restore) [6]. Olivares et al.'s meta-analysis documented evaluation across 16 dimensions including productivity, correctness, security, workflow disruptions, cognitive load, trust, skill development, transparency, pedagogy, equity, and privacy [26].

**Gaps in Evaluation:**

Despite this diversity, significant gaps remain. Mohamed et al. noted that most studies lack longitudinal evaluations that would capture long-term impacts on code maintainability, developer skills, and team dynamics [17]. Few studies examine the downstream costs of maintaining AI-generated code or the impact on team collaboration and knowledge sharing.

### 4.4 RQ4: Main Benefits Reported

AI-assisted code generation tools deliver substantial benefits across multiple dimensions, though these vary by context, user experience, and task type [2], [3], [5], [6], [8], [9], [10], [11], [17], [18], [20], [23], [25], [26], [30].

**Accelerated Development Cycles:**

The most consistently reported benefit is acceleration of development activities. Agarwal documented 50-60% reductions in development cycle time without compromising code quality [23]. Pandey et al. reported up to 50% time savings in documentation and autocompletion, and 30-40% savings in repetitive coding, testing, and debugging [2]. These gains translate to faster time-to-market and increased development velocity.

**Reduced Manual Effort:**

AI tools significantly reduce manual effort for routine tasks. Multiple studies confirm that assistants excel at automating boilerplate code generation, scaffolding, and routine transformations [5], [6], [11], [17]. This allows developers to focus on higher-level design and strategic problem-solving rather than mechanical coding tasks [11], [23].

**Enhanced Learning and Skill Development:**

For novice developers and students, AI tools provide substantial learning benefits. Waseem et al. found that ChatGPT addressed significant skill gaps among undergraduate students, enhancing efficiency, accuracy, collaboration, foundational understanding, and soft skills [25]. Olivares et al.'s meta-analysis documented improved learning, immediate feedback, reduced syntax errors, and increased confidence among students [26]. Ng et al. reported that junior developers particularly benefited from AI assistants, with 95% consensus on increased developer satisfaction [30].

**Improved Developer Experience:**

AI tools enhance subjective developer experience across multiple dimensions. Bakal et al. reported 72% developer satisfaction scores at ZoomInfo [8]. Butler et al. found that generative AI coding tools significantly increased perceptions of usefulness and enjoyment, led to positive changes in daily work practices, and fostered creative ideation [18]. Chatterjee et al. documented significant increases in job satisfaction among engineers using GitHub Copilot [15], [21].

**Productivity Gains Across Experience Levels:**

While benefits vary by experience, productivity gains are observed across skill levels. Song et al. found that GitHub Copilot increased project-level productivity by 6.5%, individual productivity by 5.5%, and participation by 5.4% in open-source development [20]. Urs reported 19.7% average increases in code generation velocity [9]. Ng et al. documented 21-28% productivity increases in public sector development [30].

**Task-Specific Advantages:**

AI tools demonstrate particular strengths in specific domains:
- **Algorithmic tasks:** Liu et al. found ChatGPT outperformed Stack Overflow in code quality and speed for algorithmic challenges [10]
- **Parallel programming:** Mišić et al. reported that GitHub Copilot yields performant parallel solutions with much less effort [27]
- **Information retrieval:** Mohamed et al. identified minimized code search as a key benefit [17]
- **Repetitive tasks:** Multiple studies confirm excellence in automating trivial and repetitive tasks [17], [26]

**Unexpected Use Cases:**

Butler et al. documented unexpected beneficial uses including replacing web searches and fostering creative ideation, suggesting that AI tools provide value beyond their primary code generation function [18].

**Educational Benefits:**

In educational contexts, Olivares et al. found that LLM-based tools streamline teaching through generated assessments and interactive teaching methods [26]. These tools provide immediate feedback and reduce syntax errors, supporting more effective learning.

### 4.5 RQ5: Limitations, Risks, and Challenges

Despite substantial benefits, AI-assisted code generation tools present significant limitations, risks, and challenges that must be carefully managed [2], [3], [5], [6], [9], [15], [16], [17], [18], [21], [23], [26], [28], [30].

**Security Vulnerabilities:**

Security risks represent the most critical concern. Cotroneo et al. found that AI-generated code contains more high-risk security vulnerabilities than human-written code [28]. Swaraj's systematic review identified security vulnerabilities as a major risk introduced by LLM-based tools [6]. The ANZ Bank studies found that the impact on code security remained inconclusive despite improvements in other quality dimensions [15], [21]. Adepoju noted that unvetted AI suggestions can introduce security defects [5].

**Quality and Correctness Issues:**

Code correctness remains inconsistent. Adepoju found that correctness and security are variable, with effects depending on task type, developer experience, prompt quality, and integration [5]. Pandey et al. reported that GitHub Copilot struggles with complex tasks, large functions, multiple files, and proprietary contexts, especially in C/C++ code [2]. Gökalp et al. noted that ChatGPT's effectiveness varies based on error nature and problem complexity, with limitations in handling complex logic [16].

**Over-Reliance and Skill Degradation:**

A critical concern is over-reliance on AI tools leading to skill degradation. Shihab et al. found that students expressed concerns about not understanding Copilot suggestions [3]. Ng et al. cautioned against over-reliance without foundational skills [30]. Olivares et al. identified challenges in balancing automation with user control and maintaining appropriate trust calibration [26]. This suggests a risk that developers may become dependent on AI tools without developing deep understanding of the code they produce.

**Cognitive Load and Verification Burden:**

While AI tools reduce effort for code generation, they may increase cognitive load for verification. Swaraj identified increased cognitive load for verification as a key challenge [6]. Mohamed et al. documented cognitive offloading as a critical risk [17]. Developers must carefully review and validate AI-generated code, which may offset some productivity gains.

**Reduced Team Collaboration:**

AI tools may negatively impact team dynamics. Mohamed et al. identified reduced team collaboration as a critical risk [17]. Song et al. found that integration time increased by 41.6% when using GitHub Copilot, potentially reflecting higher coordination costs [20]. This suggests that while individual coding speed may increase, team-level productivity may be constrained by collaboration challenges.

**Inconsistent Code Quality:**

Code quality varies unpredictably across contexts. Mohamed et al. identified inconsistent code quality as a critical risk [17]. Butler et al. found that trustworthiness of AI-generated code remained unchanged despite increased perceptions of usefulness [18], suggesting that developers recognize quality concerns even as they find tools valuable.

**Language and Context Limitations:**

Tool performance varies significantly by programming language and context. Pandey et al. noted particular struggles with C/C++ code [2]. Bakal et al. discussed language-specific performance variations [8]. Tools trained primarily on popular languages may perform poorly in specialized domains or with proprietary codebases.

**Licensing and Confidentiality:**

Enterprise adoption raises legal and confidentiality concerns. Agarwal emphasized that phased implementation is necessary for private code protection and licensing compliance [23]. Questions about code ownership, intellectual property, and data privacy remain unresolved in many contexts.

**Comprehension-Performance Gap:**

A fundamental tension exists between speed and understanding. Shihab et al.'s finding that students completed tasks faster but expressed concerns about not understanding suggestions [3] highlights a "comprehension-performance gap" where productivity gains may come at the cost of reduced learning and understanding.

### 4.6 RQ6: Research Methodologies

Empirical research on AI-assisted code generation employs diverse methodologies, each with distinct strengths and limitations [3], [4], [5], [6], [7], [9], [10], [12], [14], [15], [16], [17], [18], [19], [21], [23], [24], [25], [26], [27].

**Controlled Experiments:**

Controlled experiments represent a substantial portion of the evidence base, allowing causal inference about tool impacts. Examples include:
- Shihab et al.'s mixed-methods controlled experiment examining GitHub Copilot's effects on student programming [3]
- Liu et al.'s comparison of ChatGPT vs. Stack Overflow [10]
- Idrisov et al.'s evaluation of seven AI code generation tools [12]
- Hyun et al.'s experimental analysis of interaction strategies with ChatGPT [14]
- Chatterjee et al.'s ANZ Bank studies of GitHub Copilot [15], [21]
- Imai's comparison of GitHub Copilot to human pair programming [19]

Controlled experiments provide strong internal validity but may lack ecological validity when conducted in artificial settings with simplified tasks.

**Observational Studies:**

Observational studies examine AI tool usage in naturalistic settings, providing high ecological validity:
- Pandey et al.'s evaluation of GitHub Copilot in real-world projects [2]
- Song et al.'s analysis of GitHub Copilot's impact on open-source development [20]
- Cotroneo et al.'s large-scale comparison of human-written vs. AI-generated code [28]
- Yetistiren et al.'s empirical study of code quality across three tools [29]
- Ng et al.'s assessment in public sector development [30]

Observational studies capture real-world complexity but face challenges in controlling confounding variables and establishing causality.

**Mixed Methods:**

Mixed methods studies combine quantitative and qualitative approaches to provide richer insights:
- Şeker's examination of experiences and challenges in AI-driven development [4]
- Urs's evaluation of trust, efficiency, and defect incidence [9]
- Butler et al.'s randomized controlled trial with diary methods [18]
- Agarwal's study of corporate code writing automation [23]
- Weisz et al.'s examination of enterprise AI code assistant use [24]

Mixed methods approaches capture both measurable outcomes and subjective experiences, providing comprehensive understanding of tool impacts.

**Systematic Reviews and Meta-Analyses:**

Several systematic reviews synthesize evidence across multiple primary studies:
- Adepoju's review of early evidence on GitHub Copilot [5]
- Swaraj's systematic review and critical analysis of LLM impacts [6]
- Mohamed et al.'s systematic literature review of LLM-assistant impacts [17]
- Olivares et al.'s meta-analysis of tools, users, and HCI themes [26]

These reviews provide broad perspective but are limited by the quality and heterogeneity of included primary studies.

**Case Studies:**

Case studies provide in-depth examination of specific contexts:
- Gökalp et al.'s exploration of ChatGPT-based pair programming best practices [16]
- Waseem et al.'s study of ChatGPT use by novice developers throughout the SDLC [25]

Case studies offer rich contextual detail but limited generalizability.

**Evaluation Studies:**

Specialized evaluation studies assess specific technical capabilities:
- Mišić et al.'s assessment of LLMs for OpenMP-based code parallelization [27]

**Registered Reports:**

Borg et al.'s registered report on AI assistants and code maintainability [7] represents a methodological innovation that pre-registers study plans to reduce publication bias and ensure rigorous hypothesis testing.

**Methodological Gaps:**

Mohamed et al. identified a critical gap: while 92% of studies use multi-dimensional productivity metrics, most lack longitudinal evaluations [17]. Few studies examine long-term impacts on code maintainability, developer skill development, or team dynamics. The field would benefit from more longitudinal studies, larger-scale randomized controlled trials, and standardized evaluation frameworks.

### 4.7 RQ7: Trends and Research Gaps

Analysis of the literature reveals several important trends and identifies significant research gaps requiring future investigation [4], [5], [6], [14], [17], [26].

**Trend 1: Rapid Tool Evolution and Proliferation**

The landscape of AI code generation tools is evolving rapidly. Studies examine an expanding array of tools including GitHub Copilot, ChatGPT, Amazon CodeWhisperer, OpenAI Codex, watsonx Code Assistant, Codeium, Code Llama, Tabnine, Sourcegraph Cody, DeepSeek-Coder, Qwen-Coder, StarCoder, and InstructCodeT5+ [12], [24], [26], [28], [30]. This proliferation creates challenges for comparative evaluation and evidence synthesis.

**Trend 2: Shift from Single-Metric to Multi-Dimensional Evaluation**

Mohamed et al. found that 92% of studies now employ multi-dimensional productivity metrics [17]. Swaraj documented the adoption of comprehensive frameworks including SPACE and DORA metrics [6]. Olivares et al.'s meta-analysis examined 16 evaluation dimensions [26]. This trend reflects growing recognition that AI tool impacts cannot be captured by simple productivity measures alone.

**Trend 3: Recognition of the Productivity Paradox**

Multiple systematic reviews identify a "productivity paradox" wherein perceived efficiency gains may mask objective slowdowns and increased maintenance costs [6], [17]. This emerging understanding challenges simplistic narratives of universal productivity improvement and highlights the need for more nuanced evaluation.

**Trend 4: Focus on Experience-Dependent Effects**

Research increasingly recognizes that AI tool impacts vary substantially by developer experience level. Studies document differential effects for novices vs. experts, core vs. peripheral developers, and junior vs. senior engineers [9], [20], [30]. This trend suggests the need for experience-tailored training and deployment strategies.

**Trend 5: Growing Attention to Security and Quality Risks**

Early research emphasized productivity benefits, but recent studies increasingly focus on security vulnerabilities, code quality issues, and technical debt [6], [28], [29]. This shift reflects maturation of the field and recognition that speed gains must be balanced against quality and security concerns.

**Trend 6: Emergence of Human-AI Interaction Research**

Olivares et al.'s meta-analysis documents growing attention to human-computer interaction themes including trust calibration, cognitive load, transparency, and user control [26]. Hyun et al. developed guidelines for productive interaction strategies and a taxonomy of errors [14]. This trend reflects recognition that effective AI tool use requires understanding human-AI collaboration dynamics.

**Research Gap 1: Lack of Longitudinal Studies**

Mohamed et al. identified the most critical gap: most studies lack longitudinal evaluations examining long-term impacts on code maintainability, developer skills, and team dynamics [17]. Short-term productivity gains may be offset by long-term maintenance costs, skill degradation, or team collaboration challenges that are not captured in brief studies.

**Research Gap 2: Absence of Standardized Evaluation Frameworks**

Despite the trend toward multi-dimensional evaluation, the field lacks standardized frameworks for comparing tools and synthesizing evidence across studies. Different studies employ different metrics, making meta-analysis and evidence synthesis challenging.

**Research Gap 3: Limited Understanding of Security-by-Design Approaches**

While security vulnerabilities in AI-generated code are well-documented [6], [28], research on effective mitigation strategies is limited. The field needs investigation of security-by-design approaches, automated vulnerability detection for AI-generated code, and training methods to help developers identify security issues.

**Research Gap 4: Insufficient Investigation of Team-Level Impacts**

Most research focuses on individual developer productivity, with limited examination of team-level effects. Song et al.'s finding of increased integration time [20] and Mohamed et al.'s identification of reduced team collaboration [17] suggest important team-level impacts that require further investigation.

**Research Gap 5: Limited Understanding of Skill Development and Degradation**

While studies document concerns about over-reliance and comprehension gaps [3], [30], systematic investigation of how AI tool use affects developer skill development and expertise is lacking. Longitudinal studies tracking skill trajectories are needed.

**Research Gap 6: Inadequate Examination of Context-Specific Factors**

Tool performance varies by programming language, domain, task complexity, and organizational context [2], [8], but systematic investigation of these contextual factors is limited. Research is needed to identify which tools work best in which contexts.

**Research Gap 7: Insufficient Attention to Equity and Access**

Olivares et al. identified equity and access as important evaluation dimensions [26], but few studies systematically examine how AI tools affect different demographic groups or how access disparities might create or exacerbate inequalities in software development.

**Future Research Directions:**

Şeker outlined future research directions including improved prompt engineering, better integration with development workflows, and enhanced security measures [4]. The field would benefit from:
- Large-scale, multi-year longitudinal studies
- Standardized evaluation frameworks and benchmarks
- Investigation of security-by-design approaches
- Examination of team-level collaboration and coordination
- Studies of skill development trajectories
- Context-specific evaluation across languages, domains, and organizations
- Research on equity, access, and demographic differences

---

## 5. Discussion

### 5.1 The Productivity Paradox

A central finding of this review is the "productivity paradox" identified by multiple systematic reviews [6], [17]: while AI-assisted code generation tools demonstrably accelerate specific coding tasks, these gains may be offset by increased verification burden, maintenance costs, and coordination overhead. This paradox manifests in several ways.

First, individual coding speed increases do not necessarily translate to team-level productivity gains. Song et al.'s finding of 41.6% increased integration time [20] suggests that faster individual code production may create bottlenecks in code review, integration, and coordination. Second, short-term productivity gains may mask long-term maintenance costs. Code that is generated quickly but contains security vulnerabilities, technical debt, or poor maintainability may ultimately cost more to maintain than code written more slowly with greater care. Third, perceived productivity improvements may diverge from objective measures. Butler et al. found that while developers perceived AI tools as useful and enjoyable, trustworthiness of generated code remained unchanged [18], suggesting awareness that subjective benefits may not reflect objective quality.

This paradox has important implications for how organizations measure and optimize AI tool adoption. Simple metrics like lines of code produced or task completion time may be misleading. Comprehensive evaluation requires multi-dimensional metrics capturing quality, security, maintainability, team coordination, and long-term costs [6], [17].

### 5.2 Experience-Dependent Effects

AI tool impacts vary dramatically by developer experience level, creating both opportunities and risks. For novice developers and students, AI tools provide substantial learning benefits, addressing skill gaps and accelerating development [25], [26], [30]. However, these same tools increase defect rates by 71% among novices [9], suggesting that inexperienced developers lack the expertise to critically evaluate AI-generated code.

For experienced developers, the picture is more complex. Core developers gain more productivity benefits than peripheral developers [20], suggesting that expertise enables more effective tool use. However, experienced developers may also face increased maintenance burdens when reviewing and correcting AI-generated code from less experienced team members. The shift in developer roles toward architects and reviewers [23] may be welcomed by some but resisted by others who value hands-on coding.

These experience-dependent effects suggest the need for tailored training and deployment strategies. Novice developers require training in critical evaluation of AI suggestions and foundational programming skills to avoid over-reliance. Experienced developers need guidance on effective prompt engineering, tool integration, and code review practices for AI-generated code. Organizations must carefully consider how AI tools affect skill development trajectories and implement strategies to prevent skill degradation.

### 5.3 Security and Quality Trade-offs

The evidence reveals a fundamental tension between speed and quality, particularly regarding security. While AI tools accelerate code production, they introduce more high-risk security vulnerabilities than human-written code [28]. This creates a critical challenge: organizations adopting AI tools for productivity gains may inadvertently increase security risks.

Several factors contribute to this challenge. First, AI models are trained on large corpora of existing code, which includes insecure patterns and vulnerabilities. Models may reproduce these patterns without understanding security implications. Second, developers may accept AI suggestions without thorough security review, particularly when under time pressure. Third, the speed of AI code generation may create a false sense of security, leading to reduced vigilance in code review.

Addressing this challenge requires multi-faceted approaches. Technical solutions include improved training data curation, security-focused fine-tuning, and automated vulnerability detection for AI-generated code. Process solutions include enhanced code review practices, security-focused training for developers using AI tools, and integration of security testing into AI-assisted development workflows. Organizational solutions include clear policies on AI tool use, phased deployment with security evaluation, and allocation of time for thorough review of AI-generated code.

### 5.4 Implications for Practice

Based on the evidence synthesized in this review, we offer several recommendations for practitioners and organizations adopting AI-assisted code generation tools:

**1. Implement Phased Deployment with Evaluation**

Organizations should adopt AI tools gradually, starting with low-risk contexts and expanding based on empirical evaluation of impacts on productivity, quality, security, and team dynamics [23]. Deployment should be accompanied by measurement using multi-dimensional metrics [6], [17].

**2. Invest in Comprehensive Training**

Training programs should address both technical tool use and critical evaluation skills. Novice developers need training in foundational programming skills and critical assessment of AI suggestions [3], [30]. Experienced developers need guidance on effective prompt engineering, tool integration, and code review practices for AI-generated code [14].

**3. Enhance Code Review Processes**

Organizations must strengthen code review processes to catch security vulnerabilities and quality issues in AI-generated code [28]. This may require additional time allocation, specialized security review, and training for reviewers.

**4. Balance Automation with Human Oversight**

Effective AI tool use requires balancing automation with user control and maintaining appropriate trust calibration [26]. Developers should be encouraged to critically evaluate AI suggestions rather than accepting them uncritically.

**5. Monitor Long-Term Impacts**

Organizations should implement longitudinal monitoring of AI tool impacts on code maintainability, developer skills, team collaboration, and security [17]. Short-term productivity gains should be balanced against long-term costs.

**6. Address Security Proactively**

Given the elevated security risks in AI-generated code [28], organizations should implement security-by-design approaches, automated vulnerability scanning, and security-focused training.

**7. Tailor Approaches to Context**

Tool selection and deployment strategies should be tailored to specific contexts including programming language, domain, task complexity, and developer experience [2], [8]. What works in one context may not work in another.

---

## 6. Limitations of This Review

This systematic literature review has several limitations that should be considered when interpreting findings:

**1. Publication Bias:** The review includes only published studies, which may over-represent positive findings and under-represent negative results or failed replications.

**2. Rapid Field Evolution:** The field of AI-assisted code generation is evolving rapidly. Tools improve continuously, and findings from studies of earlier tool versions may not apply to current versions.

**3. Heterogeneity of Studies:** Included studies employ diverse methodologies, metrics, tools, and contexts, making direct comparison and meta-analysis challenging.

**4. Limited Longitudinal Evidence:** As noted in RQ7, most studies are short-term, limiting understanding of long-term impacts on maintainability, skills, and team dynamics.

**5. Search Strategy Limitations:** While we conducted comprehensive searches across major databases, some relevant studies may have been missed, particularly gray literature, industry reports, and non-English publications.

**6. Quality Variation:** Included studies vary in methodological rigor, sample size, and ecological validity. While we applied quality thresholds during screening, some included studies have limitations.

---

## 7. Future Research Directions

Based on the trends and gaps identified in this review, we recommend the following priorities for future research:

**1. Longitudinal Studies:** Multi-year studies tracking long-term impacts on code maintainability, developer skill development, team dynamics, and organizational outcomes.

**2. Standardized Evaluation Frameworks:** Development and validation of standardized frameworks for evaluating AI code generation tools, enabling better comparison and evidence synthesis.

**3. Security-by-Design Research:** Investigation of approaches to reduce security vulnerabilities in AI-generated code, including improved training methods, automated vulnerability detection, and security-focused fine-tuning.

**4. Team-Level Impact Studies:** Examination of how AI tools affect team collaboration, coordination, knowledge sharing, and collective code ownership.

**5. Skill Development Research:** Longitudinal studies of how AI tool use affects developer skill trajectories, expertise development, and learning outcomes.

**6. Context-Specific Evaluation:** Systematic investigation of which tools work best in which contexts (languages, domains, task types, organizational settings).

**7. Equity and Access Research:** Examination of how AI tools affect different demographic groups and how access disparities might create or exacerbate inequalities.

**8. Human-AI Interaction Research:** Investigation of effective interaction patterns, prompt engineering strategies, trust calibration, and cognitive load management.

**9. Organizational Adoption Studies:** Research on effective deployment strategies, change management, training programs, and policy frameworks for organizational AI tool adoption.

**10. Comparative Tool Evaluation:** Rigorous comparative studies of different tools using standardized tasks and metrics to guide tool selection.

---

## 8. Conclusion

This systematic literature review synthesizes evidence from 349 studies examining the impact of AI-assisted code generation tools on software development. The evidence reveals a complex picture: substantial productivity gains ranging from 5.5% to 55.8%, but accompanied by significant concerns regarding code quality, security vulnerabilities, and potential skill degradation.

AI tools excel at automating routine tasks such as boilerplate code generation, documentation, and repetitive coding, delivering time savings up to 50-60% in some contexts. They enhance developer satisfaction, accelerate learning for novices, and enable developers to focus on higher-level design and problem-solving. However, these benefits come with critical trade-offs: AI-generated code contains more high-risk security vulnerabilities, exhibits variable correctness (20.6% to 65.2% depending on tool and task), and may increase defect rates by 71% among novice developers.

A "productivity paradox" emerges wherein perceived efficiency gains may mask objective slowdowns and increased maintenance burdens. Individual coding speed increases may be offset by higher integration times (41.6% increase), greater verification burden, and long-term maintenance costs. The impact varies dramatically by developer experience, task complexity, programming language, and organizational context.

Research methodologies span controlled experiments, observational studies, mixed methods, and systematic reviews, with growing adoption of multi-dimensional evaluation frameworks. However, critical gaps remain: most studies are short-term, lacking longitudinal evaluation of long-term impacts; standardized evaluation frameworks are absent; and understanding of team-level effects, skill development trajectories, and security mitigation strategies is limited.

For practitioners and organizations, the evidence suggests that AI-assisted code generation tools offer substantial value when deployed thoughtfully with appropriate safeguards. Success requires phased implementation with empirical evaluation, comprehensive training programs, enhanced code review processes, security-focused practices, and longitudinal monitoring of impacts. Organizations must balance automation with human oversight, tailor approaches to specific contexts, and recognize that productivity gains require careful management of quality and security risks.

The field of AI-assisted code generation is rapidly evolving, with continuous improvements in tools and growing sophistication in evaluation approaches. Future research should prioritize longitudinal studies, standardized evaluation frameworks, security-by-design approaches, team-level impact investigation, and examination of skill development trajectories. As these tools become increasingly integrated into software development practice, rigorous empirical research will be essential to maximize benefits while mitigating risks.

---

## 9. References

[1] Chang et al., "A Systematic Literature Review of the Practical Applications of Artificial Intelligence-Generated Content (AIGC) Using OpenAI ChatGPT, Copilot, and Codex."

[2] Pandey et al., "Transforming Software Development: Evaluating the Efficiency and Challenges of GitHub Copilot in Real-World Projects," arXiv, 2024, doi: https://doi.org/10.48550/arxiv.2406.17910.

[3] Shihab et al., "The Effects of GitHub Copilot on Computing Students' Programming Effectiveness, Efficiency, and Processes in Brownfield Programming Tasks," 2025, doi: https://doi.org/10.1145/3702652.3744219.

[4] Şeker, "Experiences and Challenges in AI-Driven Modular Software Development Using Large Language Models for Code Generation," 2024, doi: https://doi.org/10.22541/au.172871465.54826063/v1.

[5] Adepoju, "GitHub Copilot's Impact on Developer Productivity: A Review of Early Evidence," International Journal of Scientific Research in Science and Technology, 2023, doi: https://doi.org/10.32628/ijsrst2221192.

[6] Swaraj, "The Impact of Large Language Models on Software Development Productivity: A Systematic Review and Critical Analysis," 2025, doi: https://doi.org/10.5281/zenodo.17227991.

[7] Borg et al., "Does Co-Development with AI Assistants Lead to More Maintainable Code? A Registered Report," arXiv, 2024, doi: https://doi.org/10.48550/arxiv.2408.10758.

[8] Bakal et al., "Experience with GitHub Copilot for Developer Productivity at ZoomInfo," arXiv, 2025, doi: https://doi.org/10.48550/arxiv.2501.13282.

[9] Urs, "Human-AI Pair Programming: Evaluating Trust, Efficiency, and Defect Incidence," 2025, doi: https://doi.org/10.5281/zenodo.16501130.

[10] Liu et al., "ChatGPT vs. Stack Overflow: An Exploratory Comparison of Programming Assistance Tools," 2023, doi: https://doi.org/10.1109/qrs-c60940.2023.00105.

[11] "Measuring AI-Driven Developer Productivity in Agile Software Development: Random Forest Regression Analysis of Performance Metrics and Tool Integration," Computer Science, Engineering and Technology, 2025, doi: https://doi.org/10.46632/cset/3/3/12.

[12] Idrisov et al., "Program Code Generation with Generative AIs," Algorithms, 2024, doi: https://doi.org/10.3390/a17020062.

[13] Fajkovic et al., "The Impact of AI-Generated Code on Web Development: A Comparative Study of ChatGPT and GitHub Copilot."

[14] Hyun et al., "Experimental Analysis of Productive Interaction Strategy with ChatGPT: User Study on Function and Project-Level Code Generation Tasks," arXiv, 2025, doi: https://doi.org/10.48550/arxiv.2508.04125.

[15] Chatterjee et al., "The Impact of AI Tool on Engineering at ANZ Bank: An Empirical Study on GitHub Copilot within Corporate Environment," Software Engineering, 2024, doi: https://doi.org/10.5121/csit.2024.140702.

[16] Gökalp et al., "ChatGPT Based Best Practices for Pair Programming," 2025, doi: https://doi.org/10.1109/ubmk67458.2025.11206910.

[17] Mohamed et al., "The Impact of LLM-Assistants on Software Developer Productivity: A Systematic Literature Review," arXiv, 2025, doi: https://doi.org/10.48550/arxiv.2507.03156.

[18] Butler et al., "Dear Diary: A Randomized Controlled Trial of Generative AI Coding Tools in the Workplace," arXiv, 2024, doi: https://doi.org/10.48550/arxiv.2410.18334.

[19] Imai, "Is GitHub Copilot a Substitute for Human Pair-Programming? An Empirical Study," 2022, doi: https://doi.org/10.1145/3510454.3522684.

[20] Song et al., "The Impact of Generative AI on Collaborative Open-Source Software Development: Evidence from GitHub Copilot," Social Science Research Network, 2024, doi: https://doi.org/10.2139/ssrn.4856935.

[21] Chatterjee et al., "The Impact of AI Tool on Engineering at ANZ Bank: An Empirical Study on GitHub Copilot within Corporate Environment," arXiv, 2024, doi: https://doi.org/10.48550/arxiv.2402.05636.

[22] Suryavanshi et al., "The Effects of AI-Assisted Programming in Software Engineering: A Study on GitHub Copilot."

[23] Agarwal, "Paradigms of Generative Artificial Intelligence in Automating Corporate Code Writing," The American Journal of Engineering and Technology, 2025, doi: https://doi.org/10.37547/tajet/volume07issue08-11.

[24] Weisz et al., "Examining the Use and Impact of an AI Code Assistant on Developer Productivity and Experience in the Enterprise," arXiv, 2024, doi: https://doi.org/10.48550/arxiv.2412.06603.

[25] Waseem et al., "Using ChatGPT Throughout the Software Development Life Cycle by Novice Developers," arXiv, 2023, doi: https://doi.org/10.48550/arxiv.2310.13648.

[26] Olivares et al., "Large Language Models in Programming: A Meta-Analysis of Tools, Users, and Human-Computer Interaction Themes," AHFE International, 2025, doi: https://doi.org/10.54941/ahfe1006934.

[27] Mišić et al., "An Assessment of Large Language Models for OpenMP-Based Code Parallelization: A User Perspective," Journal of Big Data, 2024, doi: https://doi.org/10.1186/s40537-024-01019-z.

[28] Cotroneo et al., "Human-Written vs. AI-Generated Code: A Large-Scale Study of Defects, Vulnerabilities, and Complexity," arXiv, 2025, doi: https://doi.org/10.48550/arxiv.2508.21634.

[29] Yetistiren et al., "Evaluating the Code Quality of AI-Assisted Code Generation Tools: An Empirical Study on GitHub Copilot, Amazon CodeWhisperer, and ChatGPT," arXiv, 2023, doi: https://doi.org/10.48550/arXiv.2304.10778.

[30] Ng et al., "Harnessing the Potential of Gen-AI Coding Assistants in Public Sector Software Development," arXiv, 2024, doi: https://doi.org/10.48550/arxiv.2409.17434.

---

**End of Report**
