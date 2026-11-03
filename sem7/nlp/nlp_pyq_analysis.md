# Mumbai University (MU) Semester 7 — Natural Language Processing (NLP)
## Comprehensive 6-Paper PYQ Trend Analysis & Priority Roadmap
*(Exam Cycles Analyzed: December 2022, May 2023, December 2023, May 2024, December 2024, May 2025)*
**Course Code:** 42175 (DLOC - III) | **Scheme:** Rev 2019 / C-Scheme | **Total Marks:** 80 per paper

---

## 1. Executive Summary & Syllabus Module Architecture

Natural Language Processing (NLP) in Mumbai University Semester 7 follows a structured 6-module curriculum. Analysis of the last six consecutive examination cycles reveals exceptional predictability in question patterns, recurring numerical problems, and mandatory algorithmic derivations.

```
+---------------------------------------------------------------------------------------------------+
|                                 MU SEM 7 NLP MODULE ARCHITECTURE                                  |
+---------------------------------------------------------------------------------------------------+
|  M1: Introduction & Morphology (15-20 Marks)                                                      |
|      - Stages of NLP & Ambiguities at each level                                                  |
|      - Inflectional vs Derivational Morphology | Morphological Analysis Output                    |
|      - FSTs for Regular/Irregular Nouns, Verbs & English Numbers 1-99                            |
|      - Porter's Stemming Algorithm (Rules, Traces, Consonant/Vowel Measure m)                     |
+---------------------------------------------------------------------------------------------------+
|  M2: Language Modeling & Part-of-Speech (POS) Tagging (25-35 Marks) -- [CRITICAL NUMERICAL HUB]    |
|      - N-gram Language Models, MLE Bigram Probabilities & Sentence Likelihoods                    |
|      - Smoothing Techniques: Laplace (Add-1), Good-Turing Discounting, Perplexity                 |
|      - POS Tagging: Rule-based, Stochastic, Transformation-based, Hybrid                          |
|      - Hidden Markov Models (HMM) for POS Tagging: Transition & Emission Matrices                 |
|      - Viterbi Decoding Algorithm (Step-by-step trellis numericals - GUARANTEED 10 MARKS)         |
|      - Maximum Entropy (MaxEnt) & Conditional Random Fields (CRF) for Sequence Labeling           |
+---------------------------------------------------------------------------------------------------+
|  M3: Syntax & Parsing (15-20 Marks) -- [CRITICAL ALGORITHM HUB]                                   |
|      - Context-Free Grammars (CFG) & Probabilistic CFG (PCFG)                                     |
|      - Top-Down vs Bottom-Up Parsing Strategies                                                   |
|      - Cocke-Younger-Kasami (CYK / CKY) Dynamic Programming Parsing Algorithm (CNF Table)        |
|      - Shift-Reduce Parsing (Stack, Buffer, Shift, Reduce, Accept, Error)                         |
+---------------------------------------------------------------------------------------------------+
|  M4: Semantic Analysis & Word Sense Disambiguation (WSD) (15-20 Marks)                            |
|      - Lexical Semantics: Homonymy, Polysemy, Synonymy, Antonymy, Hyponymy, Hypernymy, Meronymy   |
|      - Dictionary-Based WSD: Original Lesk & Simplified Lesk (Overlap Matching)                   |
|      - Supervised WSD: Naive Bayes Classifier                                                     |
|      - Semi-Supervised WSD: Yarowsky Bootstrapping Algorithm                                      |
+---------------------------------------------------------------------------------------------------+
|  M5: Discourse Analysis & Reference Resolution (15-20 Marks)                                      |
|      - Reference Phenomena: Anaphora, Cataphora, Co-reference Chains                              |
|      - 5 Types of Referring Expressions | Syntactic & Semantic Constraints                       |
|      - Hobbs Algorithm for Pronoun Resolution (9-Step Tree Search Walk)                           |
|      - Centering Theory: Cf, Cb, Cp, and Transition States (Continue, Retain, Smooth/Rough Shift) |
+---------------------------------------------------------------------------------------------------+
|  M6: Natural Language Engineering & Applications (15-20 Marks)                                    |
|      - Machine Translation (MT): Direct, Transfer-based, Interlingua (Vauquois Triangle), SMT     |
|      - Information Retrieval (IR) vs Information Extraction (IE) Architecture                     |
|      - Text Summarization: Extractive vs Abstractive Paradigms                                    |
|      - Question Answering Systems (QAS): Pipeline Architecture & Algorithmic Components           |
+---------------------------------------------------------------------------------------------------+
```

---

## 2. Topic-by-Topic 6-Paper Frequency Matrix

The following matrix records every appearance of a topic across the 6 analyzed papers (Dec 2022 to May 2025).

| # | Topic / Concept Description | Dec 22 | May 23 | Dec 23 | May 24 | Dec 24 | May 25 | Total Count | Frequency Tier |
|---|-----------------------------|:------:|:------:|:------:|:------:|:------:|:------:|:-----------:|:--------------:|
| **1** | **Stages of NLP & Level Ambiguities** (Phonology, Morphology, Syntax, Semantics, Pragmatics) | Q2b (10M), Q1a (5M) | Q1e (5M), Q3a (10M) | Q2b (10M) | Q1d (5M) | Q1e (5M), Q2b (10M) | Q2b (10M) | **8 times** | **Tier 1 (Guaranteed)** |
| **2** | **Porter Stemming Algorithm** (Rules, Measure $m$, Suffix Stripping Trace) | Q6b (10M) | Q5b (10M) | Q5a (10M) | Q1b (5M), Q2b (10M) | Q5a (10M) | — | **6 times** | **Tier 1 (Guaranteed)** |
| **3** | **FSA / FST for Morphology & English Numbers (1-99)** | Q2a (10M) | Q2b (10M) | Q2a (10M) | — | Q2a (10M) | Q1b (5M) | **5 times** | **Tier 1 (Guaranteed)** |
| **4** | **HMM POS Tagging & Viterbi Decoding Numerical** | — | Q4a (10M) | Q3a (10M) | Q3a (10M) | Q3a (10M) | Q4a (10M) | **5 times** | **Tier 1 (Guaranteed 10M)** |
| **5** | **N-gram Language Modeling & Probability Numerical** | Q3a (5M), Q1f (5M) | Q1b (5M) | Q1b (5M) | — | Q4b (10M) | Q2a (10M) | **5 times** | **Tier 1 (Guaranteed 10M)** |
| **6** | **Word Sense Disambiguation (Lesk, Naive Bayes, Yarowsky)** | Q5a (10M), Q3b (5M) | Q2a (10M) | Q4a (10M) | Q4a (10M) | Q1a (5M), Q4a (10M) | Q3a (10M), Q6a (10M) | **8 times** | **Tier 1 (Guaranteed)** |
| **7** | **Pronoun / Discourse Reference Resolution (Hobbs & Centering)** | Q5b (10M) | Q1c (5M), Q3b (10M), Q4b (10M) | Q1e (5M), Q3b (10M) | Q5a (10M), Q5b (10M) | Q1b (5M), Q3b (10M) | Q1e (5M), Q4b (10M) | **10 times** | **Tier 1 (Guaranteed 10M)** |
| **8** | **CYK (Cocke-Younger-Kasami) Parsing Algorithm** | — | Q5a (10M) | — | — | — | Q5a (10M) | **2 times** | **Tier 1 (Core Numerical)** |
| **9** | **Machine Translation (Vauquois Triangle, Direct, Transfer, SMT)** | Q1d (5M) | Q1d (5M) | Q1c (5M) | Q6a (10M) | Q1c (5M) | — | **5 times** | **Tier 2 (High Yield)** |
| **10** | **Information Retrieval (IR) vs Information Extraction (IE)** | Q4b (5M) | Q6a (10M) | — | Q6b (10M) | — | — | **3 times** | **Tier 2 (High Yield)** |
| **11** | **Text Summarization (Extractive vs Abstractive)** | Q6a (10M) | — | — | — | Q6a (10M) | — | **2 times** | **Tier 2 (High Yield)** |
| **12** | **Question Answering Systems (QAS Pipeline)** | — | — | Q6a (10M) | — | — | Q6b (10M) | **2 times** | **Tier 2 (High Yield)** |
| **13** | **MaxEnt & CRF (Conditional Random Fields) for Tagging** | — | Q6b (10M) | Q6b (10M) | Q3b (10M) | Q6b (10M) | Q1c (5M) | **5 times** | **Tier 2 (High Yield)** |
| **14** | **Lexical Semantic Relations (Hyponymy, Meronymy, Polysemy, etc.)** | Q1e (5M) | — | Q1d (5M) | Q4b (10M) | — | — | **3 times** | **Tier 3 (Standard 5M)** |
| **15** | **Shift-Reduce Parsing** | — | — | — | — | — | Q3b (10M) | **1 time** | **Tier 3 (Emerging)** |

---

## 3. High-Priority Preparation Tiers (Exam Survival Strategy)

To score 70+ out of 80 marks in MU Semester 7 NLP, students must prepare in the following strict hierarchy:

### Tier 1: Non-Negotiable Core (Guarantees 55-60 Marks)
1. **HMM POS Tagging & Viterbi Decoding Numerical (10 Marks):**
   - Must master transition probability $A_{ij} = \frac{C(t_{i-1}, t_i)}{C(t_{i-1})}$ and emission probability $B_{jk} = \frac{C(t_j, w_k)}{C(t_j)}$.
   - Full trellis forward pass $\nu_t(j) = \max_i [\nu_{t-1}(i) \cdot a_{ij}] \cdot b_j(w_t)$ and backpointer traceback $\mathrm{bp}_t(j)$.
   - All 3 MU paper variants solved in Part 1 Masterclass.
2. **N-gram Language Modeling & Probability Numerical (5-10 Marks):**
   - Calculation of bigram counts, conditional probabilities $P(w_n | w_{n-1}) = \frac{C(w_{n-1}, w_n)}{C(w_{n-1})}$, sentence probabilities, and next-word prediction.
   - Laplace smoothing ($+1$) and Good-Turing discounting formula ($c^* = (c+1)\frac{N_{c+1}}{N_c}$).
3. **Porter Stemming Algorithm (10 Marks):**
   - Consonant/Vowel definition, measure $m$, condition syntax $[m > 0]$, $[*v*]$, $[*d]$, $[*o]$.
   - Step 1a, Step 1b, Step 1c, Step 2, Step 3, Step 4, Step 5 detailed rule transformations with trace words (`sses` $\to$ `ss`, `troubles` $\to$ `trouble`, `relational` $\to$ `relate`).
4. **Discourse Reference Resolution: Hobbs vs Centering Algorithm (10 Marks):**
   - Hobbs 9-step parse-tree traversal algorithm (Left-to-Right, Breadth-First, Dominance rules).
   - Centering Theory: Utterance $U_n$, Forward-looking centers $C_f(U_n)$, Backward-looking center $C_b(U_n)$, Preferred center $C_p(U_n)$, Transition table (Continue, Retain, Smooth-Shift, Rough-Shift).
5. **CYK (Cocke-Younger-Kasami) Parsing Algorithm (10 Marks):**
   - Chomsky Normal Form (CNF) grammar requirements ($A \to BC$ or $A \to a$).
   - Triangular dynamic programming table filling formula $P[i, j, A] = \bigvee_{k=1}^{j-1} (B \in P[i, k] \land C \in P[i+k, j-k] \land (A \to BC))$.

### Tier 2: High-Yield Theory & Architecture (20-25 Marks)
1. **Stages of NLP & Ambiguities:**
   - 6 levels: Phonology, Morphology, Syntax, Semantics, Pragmatics, Discourse.
   - Lexical ambiguity (Homonymy/Polysemy/Category) vs Syntactic ambiguity (Attachment/Coordination).
2. **Word Sense Disambiguation (WSD):**
   - Simplified & Original Lesk (Dictionary overlap).
   - Supervised Naive Bayes formulation.
   - Yarowsky Bootstrapping (One sense per discourse, One sense per collocation).
3. **Finite State Transducers (FST) for Morphology:**
   - Lexical tape vs Surface tape, two-level morphology, intermediate tape, E-insertion rule.
   - FST for English Numbers 1-99 (Tens and Units concatenation with 0-exception).
4. **Machine Translation Architectures:**
   - Vauquois Triangle, Direct Translation, Rule-Based Transfer (Syntactic/Semantic), Interlingua, Statistical MT (Noisy Channel Model: $P(E|F) \propto P(F|E) \cdot P(E)$).
5. **Information Retrieval vs Information Extraction & QAS:**
   - Vector Space Model (TF-IDF), Inverted Index, Precision/Recall.
   - IE Named Entity Recognition (NER) & Relation Extraction.
   - Question Answering System 3-tier architecture: Question Processing $\to$ Document Retrieval $\to$ Answer Extraction.

---

## 4. Masterclass Content Division

To ensure maximum completeness without file truncation, the masterclass is divided into two parts:

- **`nlp_masterclass_part1.md`**:
  - **Module 1:** Introduction, Preprocessing Pipeline, NLP Stages, Ambiguities at all levels, Morphology (Inflectional vs Derivational, Open vs Closed class), FST for Nouns/Verbs & Numbers 1-99, Porter Stemming Algorithm complete specification and traces.
  - **Module 2:** N-gram Language Modeling (MLE formulas, Bigram Solved Numericals from Dec'22 & May'25), Smoothing (Laplace, Good-Turing, Perplexity), POS Tagging (Rule-based, Stochastic, Hybrid, Challenges), **HMM POS Tagging & Viterbi Algorithm (Full Numerical Solutions for May'23/May'25, Dec'23, and Dec'24)**, Maximum Entropy & Conditional Random Fields (CRF) for sequence labeling.

- **`nlp_masterclass_part2.md`**:
  - **Module 3:** Context-Free Grammars (CFG) & PCFG, Top-down vs Bottom-up Parsing, Shift-Reduce Parser trace, **Full CYK Parsing Numerical ("The man read this book" CNF Dynamic Programming Table)**.
  - **Module 4:** Lexical Semantics & WordNet relations, Word Sense Disambiguation (Need, Lesk Dictionary-based, Naive Bayes Supervised, Yarowsky Bootstrapping Semi-supervised).
  - **Module 5:** Discourse Reference Phenomena (Anaphora, Cataphora, Co-reference), 5 Types of Referring Expressions, Syntactic & Semantic Constraints, **Hobbs Parse Tree Search Algorithm**, **Centering Theory (Detailed Transitions & Mathematical Formulation)**.
  - **Module 6:** Machine Translation (Vauquois Triangle, Direct, Transfer, Interlingua, SMT Noisy Channel), Information Retrieval (IR) vs Information Extraction (IE), Text Summarization (Extractive vs Abstractive), Question Answering Systems (Architecture & Components).
