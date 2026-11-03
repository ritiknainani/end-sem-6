# Mumbai University (MU) Semester 7 — Natural Language Processing (NLP)
## Masterclass Part 2: Modules 3, 4, 5 & 6 (Syntax, Semantics, Discourse & Applications)
**Course Code:** 42175 (DLOC - III) | **Scheme:** Rev 2019 / C-Scheme | **Applicable Cycles:** Dec 2022 – May 2025

---

# MODULE 3: SYNTAX & PARSING

---

## 3.1 Formal Grammars: Context-Free Grammars (CFG) vs Probabilistic CFG (PCFG)
*(Appeared in: Dec 2023 Q5b [10M], Dec 2024 Q5b [10M])*

### Context-Free Grammar (CFG)
A Context-Free Grammar is formally defined as a 4-tuple:
$$G = (V_N, V_T, P, S)$$
where:
- $V_N$: A finite set of **non-terminal** characters (syntactic categories like $S, NP, VP, PP$).
- $V_T$: A finite set of **terminal** symbols disjoint from $V_N$ (lexical words like `the`, `man`, `read`).
- $P$: A finite set of **production rules** of the form $A \to \alpha$, where $A \in V_N$ and $\alpha \in (V_N \cup V_T)^*$.
- $S$: The designated **start symbol** ($S \in V_N$).

### Probabilistic Context-Free Grammar (PCFG)
Standard CFGs suffer from two major flaws:
1. They cannot rank or disambiguate alternative parse trees for structurally ambiguous sentences.
2. They cannot model lexical selectional preferences.

A **PCFG** augments each production rule $A \to \alpha$ with a conditional probability $P(A \to \alpha)$:
$$\sum_{\alpha} P(A \to \alpha) = 1 \quad \forall A \in V_N$$

#### Probability of a Parse Tree:
The probability of an entire derivation tree $T$ is the product of the probabilities of all rules $r \in T$ used in its construction:
$$P(T, S) = \prod_{A \to \alpha \in T} P(A \to \alpha)$$
The optimal parse tree for an ambiguous sentence is chosen via:
$$\hat{T} = \arg\max_T P(T \mid S)$$

#### Parameter Estimation (from Treebank):
$$P(A \to \alpha) = \frac{\text{Count}(A \to \alpha)}{\sum_\beta \text{Count}(A \to \beta)} = \frac{\text{Count}(A \to \alpha)}{\text{Count}(A)}$$

---

## 3.2 Parsing Paradigms: Top-Down vs Bottom-Up Parsing
*(Appeared in: Dec 2022 Q4c [10M])*

```
+---------------------------------------------------------------------------------------------------+
|                                 TOP-DOWN VS BOTTOM-UP PARSING                                     |
+---------------------------------------------------------------------------------------------------+
| TOP-DOWN PARSING (Goal-Driven / Expectation-Driven):                                              |
|   - Starts at Root Start Symbol 'S' and works downward to match input words.                      |
|   - Algorithm: Recursive Descent, Early Parser (Predict step).                                    |
|   - Pro: Never wastes time exploring trees that cannot connect to root S.                         |
|   - Con: Wastes heavy computation generating subtrees that don't match input words;                |
|          suffers infinite loops on left-recursive rules (A --> A B).                              |
+---------------------------------------------------------------------------------------------------+
|                                                  |                                                |
|                   S                              |                 S                              |
|                 /   \                            |               /   \                            |
|               NP     VP                          |             NP     VP                          |
|              /  \     |                          |            /  \     |                          |
|            Det   N    V                          |          Det   N    V                          |
|             |    |    |                          |           |    |    |                          |
|            The  man read                         |          The  man read                         |
|        [Top-Down: Expands S downward]            |     [Bottom-Up: Reduces words upward]          |
|                                                  |                                                |
+---------------------------------------------------------------------------------------------------+
| BOTTOM-UP PARSING (Data-Driven / Input-Driven):                                                   |
|   - Starts with input tokens and replaces RHS phrases with non-terminals until 'S' is reached.    |
|   - Algorithm: Shift-Reduce, CYK (Cocke-Younger-Kasami).                                          |
|   - Pro: Never explores categories that do not match actual input tokens; handles left-recursion. |
|   - Con: Builds countless local valid phrases that cannot legally integrate into root 'S'.         |
+---------------------------------------------------------------------------------------------------+
```

### Comprehensive Comparison:

| Parameter | Top-Down Parsing | Bottom-Up Parsing |
|:---|:---|:---|
| **Starting Point** | Start symbol $S$ (Root of tree). | Raw input words (Leaves of tree). |
| **Strategy** | Goal-driven (Predicts words from rules). | Data-driven (Reduces words to syntactic heads). |
| **Search Direction** | Root to Leaves. | Leaves to Root. |
| **Left Recursion** | Traps into infinite loops ($A \to A \alpha$). | Naturally immune to left recursion. |
| **Inefficiency Risk**| Generates trees incompatible with tokens. | Builds isolated phrases that cannot combine to $S$. |
| **Representative** | Recursive Descent, Earley Predictor. | Shift-Reduce, CYK Algorithm. |

---

## 3.3 Shift-Reduce Parser Trace
*(Appeared in: May 2025 Q3b [10M])*

A Shift-Reduce parser uses a **Stack** and an **Input Buffer** with 4 operations:
1. **Shift:** Push the current lookahead word from buffer onto stack.
2. **Reduce:** Match top items on stack against RHS of a grammar rule and replace with LHS non-terminal.
3. **Accept:** Stack contains only start symbol $S$ and input buffer is empty.
4. **Error:** No legal shift or reduce operation exists.

### Trace for Sentence: `"The tall girl sings"`
Using CFG rules (from Dec 2024 Q5b):
$S \to NP \; VP, \quad NP \to Det \; Adj \; N \mid Det \; N, \quad VP \to V, \quad Det \to the, \quad Adj \to tall, \quad N \to girl, \quad V \to sings$.

| Step | Stack | Input Buffer | Action Taken | Rule Applied |
|:---:|:---|:---|:---|:---|
| 0 | `$` | `The tall girl sings $` | **Shift** | — |
| 1 | `$ The` | `tall girl sings $` | **Reduce** | $Det \to \text{"The"}$ |
| 2 | `$ Det` | `tall girl sings $` | **Shift** | — |
| 3 | `$ Det tall` | `girl sings $` | **Reduce** | $Adj \to \text{"tall"}$ |
| 4 | `$ Det Adj` | `girl sings $` | **Shift** | — |
| 5 | `$ Det Adj girl` | `sings $` | **Reduce** | $N \to \text{"girl"}$ |
| 6 | `$ Det Adj N` | `sings $` | **Reduce** | $NP \to Det \; Adj \; N$ |
| 7 | `$ NP` | `sings $` | **Shift** | — |
| 8 | `$ NP sings` | `$` | **Reduce** | $V \to \text{"sings"}$ |
| 9 | `$ NP V` | `$` | **Reduce** | $VP \to V$ |
| 10 | `$ NP VP` | `$` | **Reduce** | $S \to NP \; VP$ |
| 11 | `$ S` | `$` | **Accept** | Parse successful! |

---

## 3.4 SOLVED NUMERICAL: CYK (Cocke-Younger-Kasami) Parsing Algorithm
*(Appeared in: May 2023 Paper Q5a & May 2025 Paper Q5a [10 Marks])*

### Problem Statement:
For the given grammar using the CYK algorithm, parse the statement:
$$\mathbf{"The \; man \; read \; this \; book"}$$

**Given Grammar Rules:**
- $S \to NP \; VP$
- $S \to Aux \; NP \; VP$
- $S \to VP$
- $NP \to Det \; NOM$
- $NOM \to Noun$
- $NOM \to Noun \; NOM$
- $VP \to Verb$
- $VP \to Verb \; NP$
- $Det \to that \mid this \mid a \mid the$
- $Noun \to book \mid flight \mid meal \mid man$
- $Verb \to book \mid include \mid read$
- $Aux \to does$

---

### Step 1: CNF Compliance & Grammar Closure
CYK operates strictly on grammars in **Chomsky Normal Form (CNF)**, where all productions are of the form:
$$A \to B \; C \quad \text{or} \quad A \to a$$
The provided grammar contains unary/unit rules:
- $NOM \to Noun$
- $VP \to Verb$
- $S \to VP$

In standard CYK implementations with unit production closures, whenever a terminal yields $X$, any unary chain $Y \to X$ is immediately added to that cell:
- `man`: $Noun \implies NOM \implies (NP \text{ if bare})$
- `read`: $Verb \implies VP \implies S$
- `book`: $Noun \implies NOM$ **AND** $Verb \implies VP \implies S$
- `this`: $Det$
- `The`: $Det$

Binary rules in CNF form:
1. $S \to NP \; VP$
2. $NP \to Det \; NOM$
3. $NOM \to Noun \; NOM$
4. $VP \to Verb \; NP$

---

### Step 2: The CYK Dynamic Programming Table Definition
We construct a 2D triangular table $T[i, j]$, where:
- $i$ is the starting position of the substring ($1 \le i \le 5$).
- $j$ is the length of the substring ($1 \le j \le 5$).
- Sentence words:
  - $w_1 = \text{"The"}$
  - $w_2 = \text{"man"}$
  - $w_3 = \text{"read"}$
  - $w_4 = \text{"this"}$
  - $w_5 = \text{"book"}$

#### CYK Recurrence Relation:
For length $j = 1$ (base case):
$$T[i, 1] = \{ A \mid A \to w_i \in P \}$$

For length $j \ge 2$ (span combinations):
$$T[i, j] = \bigcup_{k=1}^{j-1} \{ A \mid A \to B \; C \in P, \; B \in T[i, k], \; C \in T[i+k, j-k] \}$$

---

### Step 3: Step-by-Step Table Population

#### 1. Substring Length $j = 1$ (Single Words):
- **Cell $T[1, 1]$ ("The"):**
  - Terminal match: $Det \to the$.
  - $T[1, 1] = \{ Det \}$
- **Cell $T[2, 1]$ ("man"):**
  - Terminal match: $Noun \to man$.
  - Unit production: $NOM \to Noun$.
  - $T[2, 1] = \{ Noun, NOM \}$
- **Cell $T[3, 1]$ ("read"):**
  - Terminal match: $Verb \to read$.
  - Unit production: $VP \to Verb, \; S \to VP$.
  - $T[3, 1] = \{ Verb, VP, S \}$
- **Cell $T[4, 1]$ ("this"):**
  - Terminal match: $Det \to this$.
  - $T[4, 1] = \{ Det \}$
- **Cell $T[5, 1]$ ("book"):**
  - Terminal matches: $Noun \to book$ AND $Verb \to book$.
  - Unit productions: $Noun \implies NOM$; $Verb \implies VP, S$.
  - $T[5, 1] = \{ Noun, NOM, Verb, VP, S \}$

---

#### 2. Substring Length $j = 2$ (Two-Word Phrases):
- **Cell $T[1, 2]$ ("The man", span $i=1, j=2$):**
  - Split $k=1$: $B \in T[1, 1] = \{Det\}$, $C \in T[2, 1] = \{Noun, NOM\}$.
  - Rule match: $NP \to Det \; NOM$.
  - $T[1, 2] = \{ NP \}$
- **Cell $T[2, 2]$ ("man read", span $i=2, j=2$):**
  - Split $k=1$: $B \in T[2, 1] = \{Noun, NOM\}$, $C \in T[3, 1] = \{Verb, VP, S\}$.
  - Candidate pairs: $(Noun, Verb), (NOM, Verb), (NOM, VP)$, etc.
  - No binary rule $A \to B \; C$ matches these combinations.
  - $T[2, 2] = \emptyset$
- **Cell $T[3, 2]$ ("read this", span $i=3, j=2$):**
  - Split $k=1$: $B \in T[3, 1] = \{Verb, VP, S\}$, $C \in T[4, 1] = \{Det\}$.
  - No binary rule matches.
  - $T[3, 2] = \emptyset$
- **Cell $T[4, 2]$ ("this book", span $i=4, j=2$):**
  - Split $k=1$: $B \in T[4, 1] = \{Det\}$, $C \in T[5, 1] = \{Noun, NOM, Verb, VP, S\}$.
  - Rule match: $NP \to Det \; NOM$ (since $NOM \in T[5, 1]$).
  - $T[4, 2] = \{ NP \}$

---

#### 3. Substring Length $j = 3$ (Three-Word Phrases):
- **Cell $T[1, 3]$ ("The man read", span $i=1, j=3$):**
  - $k=1$: $T[1, 1] \times T[2, 2] = \{Det\} \times \emptyset = \emptyset$.
  - $k=2$: $T[1, 2] \times T[3, 1] = \{NP\} \times \{Verb, VP, S\}$.
  - Binary rule check: $S \to NP \; VP$ (since $VP \in T[3, 1]$).
  - $T[1, 3] = \{ S \}$
- **Cell $T[2, 3]$ ("man read this", span $i=2, j=3$):**
  - $k=1$: $T[2, 1] \times T[3, 2] = \{Noun, NOM\} \times \emptyset = \emptyset$.
  - $k=2$: $T[2, 2] \times T[4, 1] = \emptyset \times \{Det\} = \emptyset$.
  - $T[2, 3] = \emptyset$
- **Cell $T[3, 3]$ ("read this book", span $i=3, j=3$):**
  - $k=1$: $T[3, 1] \times T[4, 2] = \{Verb, VP, S\} \times \{NP\}$.
    - Match: $VP \to Verb \; NP$ (since $Verb \in T[3, 1]$ and $NP \in T[4, 2]$).
    - Unit rule closure: $S \to VP$.
    - Yields: $\{VP, S\}$.
  - $k=2$: $T[3, 2] \times T[5, 1] = \emptyset \times T[5, 1] = \emptyset$.
  - $T[3, 3] = \{ VP, S \}$

---

#### 4. Substring Length $j = 4$ (Four-Word Phrases):
- **Cell $T[1, 4]$ ("The man read this", span $i=1, j=4$):**
  - $k=1$: $T[1, 1] \times T[2, 3] = \{Det\} \times \emptyset = \emptyset$.
  - $k=2$: $T[1, 2] \times T[3, 2] = \{NP\} \times \emptyset = \emptyset$.
  - $k=3$: $T[1, 3] \times T[4, 1] = \{S\} \times \{Det\} = \emptyset$.
  - $T[1, 4] = \emptyset$
- **Cell $T[2, 4]$ ("man read this book", span $i=2, j=4$):**
  - $k=1$: $T[2, 1] \times T[3, 3] = \{Noun, NOM\} \times \{VP, S\} = \emptyset$.
  - $k=2$: $T[2, 2] \times T[4, 2] = \emptyset \times \{NP\} = \emptyset$.
  - $k=3$: $T[2, 3] \times T[5, 1] = \emptyset \times T[5, 1] = \emptyset$.
  - $T[2, 4] = \emptyset$

---

#### 5. Substring Length $j = 5$ (Full Sentence: "The man read this book"):
- Span $i=1, j=5$:
  - $k=1$: $T[1, 1] \times T[2, 4] = \{Det\} \times \emptyset = \emptyset$.
  - $k=2$: $T[1, 2] \times T[3, 3] = \{NP\} \times \{VP, S\}$.
    - Rule match: **$S \to NP \; VP$** (since $NP \in T[1, 2]$ and $VP \in T[3, 3]$).
    - Yields: $\{ S \}$.
  - $k=3$: $T[1, 3] \times T[4, 2] = \{S\} \times \{NP\} = \emptyset$.
  - $k=4$: $T[1, 4] \times T[5, 1] = \emptyset \times T[5, 1] = \emptyset$.
  - **$T[1, 5] = \{ S \}$**

---

### Step 4: The Final Completed CYK Triangular Parse Table

```
+---------------------------------------------------------------------------------------------------+
|                            CYK DYNAMIC PROGRAMMING PARSE TABLE                                    |
|                              "The man read this book"                                             |
+---------------------------------------------------------------------------------------------------+
| Length j \ i |    1 (The)     |    2 (man)    |    3 (read)   |    4 (this)   |    5 (book)   |
+--------------+----------------+---------------+---------------+---------------+---------------+
|  j = 5       |    { S }       |               |               |               |               |
|  j = 4       |     ---        |      ---      |               |               |               |
|  j = 3       |    { S }       |      ---      |   { VP, S }   |               |               |
|  j = 2       |    { NP }      |      ---      |      ---      |    { NP }     |               |
|  j = 1       |    { Det }     | { Noun, NOM } | {Verb, VP, S} |    { Det }    |{Noun, NOM,    |
|              |                |               |               |               | Verb, VP, S}  |
+---------------------------------------------------------------------------------------------------+
```

### Step 5: Derivation Tree Construction
Since the root cell $T[1, 5]$ contains the designated start symbol $\mathbf{S}$, the sentence is grammatically accepted.

```
                              [ S ]
                            /       \
                          /           \
                     [ NP ]           [ VP ]
                     /    \           /    \
                 [ Det ]  [ NOM ]  [ Verb ] [ NP ]
                    |        |        |     /    \
                   The    [ Noun ]   read [Det] [ NOM ]
                             |              |      |
                            man            this [ Noun ]
                                                   |
                                                  book
```

> **Conclusion:** The CYK algorithm successfully parsed `"The man read this book"` into valid category **$S$** via derivation $S \to NP \; VP \to (Det \; NOM) \; (Verb \; NP) \to (Det \; Noun) \; (Verb \; (Det \; Noun))$.

---

## MU Keyword Checklist: Module 3
- [ ] *CFG 4-tuple $G = (V_N, V_T, P, S)$, Production rules $A \to \alpha$*
- [ ] *PCFG Rule Probabilities $\sum P(A \to \alpha) = 1$, Tree Probability Product*
- [ ] *Top-Down (Goal-driven, Left-recursion vulnerability) vs Bottom-Up (Data-driven, Wasteful local chunks)*
- [ ] *Shift-Reduce Parser: Stack, Input Buffer, Shift, Reduce, Accept, Error*
- [ ] *Chomsky Normal Form (CNF): $A \to BC$ or $A \to a$, Unit Production Elimination*
- [ ] *CYK Triangular Dynamic Programming Table $T[i, j]$, Span splitting $k$ from $1$ to $j-1$*
- [ ] *Root cell $T[1, N]$ contains Start symbol $S$*

---
---

# MODULE 4: SEMANTIC ANALYSIS & WORD SENSE DISAMBIGUATION (WSD)

---

## 4.1 Lexical Semantic Relationships (WordNet Ontological Hierarchy)
*(Appeared in: Dec 2022 Q1e [5M], Dec 2023 Q1d [5M], May 2024 Q4b [10M])*

Word meanings do not exist in isolation; they are interconnected via systematic lexical semantic relations.

```
+---------------------------------------------------------------------------------------------------+
|                                LEXICAL SEMANTIC RELATIONSHIPS                                     |
+---------------------------------------------------------------------------------------------------+
| 1. HOMONYMY:                                                                                      |
|    - Words that share identical spelling AND pronunciation, but have entirely unrelated meanings.  |
|    - Examples:                                                                                    |
|      - "bank" (financial repository) vs "bank" (river embankment).                                |
|      - "bat" (flying mammal) vs "bat" (wooden sports equipment).                                  |
+---------------------------------------------------------------------------------------------------+
| 2. POLYSEMY:                                                                                      |
|    - A single word having multiple related meanings derived from a common etymological root.      |
|    - Examples:                                                                                    |
|      - "mouth" (mouth of a human vs mouth of a river vs mouth of a cave).                         |
|      - "wood" (material from a tree vs a small forest).                                           |
+---------------------------------------------------------------------------------------------------+
| 3. SYNONYMY:                                                                                      |
|    - Distinct words that express identical or nearly identical propositions in context.          |
|    - Examples: `couch` / `sofa`, `large` / `big`, `automobile` / `car`.                            |
+---------------------------------------------------------------------------------------------------+
| 4. ANTONYMY:                                                                                      |
|    - Words having opposite meanings along a semantic dimension.                                   |
|    - Complementary: `alive` / `dead` (binary: not alive = dead).                                  |
|    - Gradable: `hot` / `cold`, `long` / `short` (scale: warm, tepid, cool).                       |
|    - Reversal / Relational: `buy` / `sell`, `borrow` / `lend`.                                    |
+---------------------------------------------------------------------------------------------------+
| 5. HYPONYMY & HYPERNYMY (Taxonomic IS-A Hierarchy):                                              |
|    - Hyponym: Specific subordinate instance (X is a hyponym of Y if X is a type of Y).            |
|    - Hypernym: Generic superordinate class (Y is a hypernym of X).                                |
|    - Example: `robin` is a hyponym of `bird`; `animal` is a hypernym of `dog`.                    |
+---------------------------------------------------------------------------------------------------+
| 6. MERONYMY & HOLONYMY (Part-Whole Partonomic Hierarchy):                                         |
|    - Meronym: Denotes a component/part of a whole (X is a meronym of Y if X is a part of Y).      |
|    - Holonym: Denotes the complete whole containing the part (Y is a holonym of X).               |
|    - Examples: `wheel` is a meronym of `car`; `forest` is a holonym of `tree`.                    |
+---------------------------------------------------------------------------------------------------+
```

---

## 4.2 Word Sense Disambiguation (WSD): Need & Problem Definition
*(Appeared in: Dec 2022 Q5a [10M], May 2023 Q2a [10M], Dec 2023 Q4a [10M], May 2024 Q4a [10M], Dec 2024 Q1a [5M], May 2025 Q3a [10M])*

### Why WSD is Critical in NLP:
- **Machine Translation (MT):** The English word `"bass"` must translate to German as `"Barsch"` (fish) or `"Bass"` (musical instrument). Translating without WSD results in absurd outputs.
- **Information Retrieval (IR):** A query for `"jaguar car maintenance"` must filter out documents about big wild cats in the Amazon.
- **Question Answering (QAS):** Understanding `"What is the interest rate of the bank?"` requires disambiguating financial institution from river shore.

---

## 4.3 Dictionary-Based Approach: The Lesk Algorithm
*(Appeared in: Dec 2022 Q5a [10M], May 2023 Q2a [10M], Dec 2023 Q4a [10M], May 2024 Q4a [10M])*

Michael Lesk's algorithm (1986) disambiguates a polysemous word by calculating the lexical overlap between the dictionary glosses (definitions and examples) of candidate senses and the words in the context window.

### Simplified Lesk Algorithm Workflow:

```
+---------------------------------------------------------------------------------------------------+
|                               SIMPLIFIED LESK ALGORITHM FLOWCHART                                 |
+---------------------------------------------------------------------------------------------------+
|  Input: Ambiguous Target Word 'w', Context Sentence 'C'                                           |
+---------------------------------------------------------------------------------------------------+
                                                  |
                                                  v
|  Step 1: Extract Context Bag-of-Words:                                                            |
|          B_context = Words(C) - {w} - Stopwords                                                   |
+---------------------------------------------------------------------------------------------------+
                                                  |
                                                  v
|  Step 2: For each Candidate Sense 's_i' in Dictionary/WordNet:                                    |
|          Signature(s_i) = Words(Gloss(s_i)) + Words(Examples(s_i)) - Stopwords                   |
+---------------------------------------------------------------------------------------------------+
                                                  |
                                                  v
|  Step 3: Compute Overlap Score:                                                                   |
|          Score(s_i) = | Signature(s_i) INTERSECTION B_context |                                   |
+---------------------------------------------------------------------------------------------------+
                                                  |
                                                  v
|  Step 4: Predict Sense with Maximum Overlap:                                                      |
|          s* = argmax_i Score(s_i)                                                                 |
+---------------------------------------------------------------------------------------------------+
```

### Concrete Worked Example: Disambiguating `"cone"` in `"pine cone"`

- **Context $C$:** `"The pine cone fell from the tree."`
  - $B_{\text{context}} = \{ \text{pine, fell, tree} \}$ (stopwords removed).
- **Candidate Senses for target word `"cone"` from WordNet:**
  - **Sense 1 ($s_1$, botany):** *"A visual fruit of a pine tree or conifer containing seeds."*
    - $\text{Signature}(s_1) = \{ \text{visual, fruit, \textbf{pine}, \textbf{tree}, conifer, containing, seeds} \}$
  - **Sense 2 ($s_2$, geometry):** *"A solid geometric body with a circular base tapering to a point."*
    - $\text{Signature}(s_2) = \{ \text{solid, geometric, body, circular, base, tapering, point} \}$
  - **Sense 3 ($s_3$, confectionery):** *"A wafer cup used for holding ice cream scoops."*
    - $\text{Signature}(s_3) = \{ \text{wafer, cup, holding, ice, cream, scoops} \}$
- **Calculate Overlap:**
  - $\text{Score}(s_1) = |\{ \text{pine, fell, tree} \} \cap \{ \text{visual, fruit, \textbf{pine}, \textbf{tree}, conifer, seeds} \}| = |\{\text{pine}, \text{tree}\}| = \mathbf{2}$.
  - $\text{Score}(s_2) = |\{ \text{pine, fell, tree} \} \cap \{ \text{solid, geometric, ...} \}| = \mathbf{0}$.
  - $\text{Score}(s_3) = |\{ \text{pine, fell, tree} \} \cap \{ \text{wafer, cup, ...} \}| = \mathbf{0}$.
- **Decision:** $\mathbf{s^* = s_1}$ (Botany sense selected correctly with highest score = 2).

---

## 4.4 Supervised Learning Approach: Naive Bayes Classifier for WSD
*(Appeared in: Dec 2024 Q4a [10M], May 2025 Q3a [10M])*

When a sense-annotated corpus (e.g., SemCor) is available, WSD is formulated as a supervised multi-class text classification problem.

### Mathematical Formulation:
Given a context window $C = \{w_{-k}, \ldots, w_{-1}, w_{+1}, \ldots, w_{+k}\}$ around ambiguous word $w$, find sense $\hat{s} \in S$:
$$\hat{s} = \arg\max_{s \in S} P(s \mid C) = \arg\max_{s \in S} \frac{P(C \mid s) P(s)}{P(C)} = \arg\max_{s \in S} P(s) P(C \mid s)$$

Assuming conditional independence of context features given sense $s$ (Naive Bayes Assumption):
$$\hat{s} = \arg\max_{s \in S} \left[ P(s) \prod_{j=-k, j \ne 0}^{+k} P(w_j \mid s) \right]$$

In log-space to prevent underflow:
$$\hat{s} = \arg\max_{s \in S} \left[ \log P(s) + \sum_{j=-k, j \ne 0}^{+k} \log P(w_j \mid s) \right]$$

- **Prior Probability $P(s)$:**
  $$P(s) = \frac{\text{Count}(s, w)}{\text{Count}(w)}$$
- **Feature Likelihood with Laplace Smoothing:**
  $$P(w_j \mid s) = \frac{\text{Count}(w_j, s) + 1}{\sum_{w' \in V} \text{Count}(w', s) + |V|}$$

---

## 4.5 Semi-Supervised Bootstrapping: Yarowsky's Algorithm
*(Appeared in: Dec 2022 Q3b [5M], May 2025 Q6a [10M])*

David Yarowsky (1995) showed that high-accuracy WSD ($>96\%$) can be achieved with almost no labeled data by leveraging two fundamental linguistic regularities:

### The Two Guiding Heuristics:
1. **One Sense Per Collocation:** Words strongly associate with specific senses when appearing next to particular words (e.g., `plant` preceded by `flowering` almost always means *flora*; followed by `manufacturing` means *factory*).
2. **One Sense Per Discourse:** Across a single document or discourse unit, an ambiguous word almost always retains the exact same sense throughout.

```
+---------------------------------------------------------------------------------------------------+
|                               YAROWSKY BOOTSTRAPPING PIPELINE                                     |
+---------------------------------------------------------------------------------------------------+
|  1. Collect massive untagged corpus containing ambiguous word 'w' (e.g., "plant").                |
+---------------------------------------------------------------------------------------------------+
                                                  |
                                                  v
|  2. Identify tiny hand-crafted SEED WORDS:                                                        |
|     - Sense A (Living plant): Seed = "life", "flora"                                              |
|     - Sense B (Factory plant): Seed = "manufacturing", "industrial"                               |
+---------------------------------------------------------------------------------------------------+
                                                  |
                                                  v
|  3. Train Initial Decision List Classifier on the labeled seed examples:                         |
|     Collocation Rule: "manufacturing plant" --> Sense B (Log-likelihood ratio: 8.5)               |
+---------------------------------------------------------------------------------------------------+
                                                  |
                                                  v
|  4. Classify Residual Untagged Corpus:                                                            |
|     Apply decision list to untagged instances; extract all classifications                        |
|     exceeding probability threshold theta.                                                        |
+---------------------------------------------------------------------------------------------------+
                                                  |
                                                  v
|  5. Apply "One Sense Per Discourse":                                                              |
|     If 90% of instances of "plant" in Document D were classified as Sense B,                      |
|     re-label residual ambiguous instances in Document D as Sense B.                               |
+---------------------------------------------------------------------------------------------------+
                                                  |
                                                  v
|  6. Iterate Steps 3-5:                                                                            |
|     Add new confident instances into training set. Re-train decision list.                        |
|     Repeat until no new examples are labeled (Convergence).                                       |
+---------------------------------------------------------------------------------------------------+
```

---

## MU Keyword Checklist: Module 4
- [ ] *Homonymy (Unrelated origins, identical form), Polysemy (Related senses)*
- [ ] *Synonymy, Antonymy (Complementary, Gradable, Relational)*
- [ ] *Hyponymy (Subordinate IS-A), Hypernymy (Superordinate)*
- [ ] *Meronymy (Part-of), Holonymy (Whole)*
- [ ] *Lesk Algorithm, Dictionary Gloss, Signature Overlap, Stopword Filtering*
- [ ] *Supervised Naive Bayes, Context Window, Bag-of-words Likelihood, Log-sum*
- [ ] *Yarowsky Bootstrapping, Seed Collocations, Decision List Classifier*
- [ ] *One Sense Per Collocation, One Sense Per Discourse*

---
---

# MODULE 5: DISCOURSE ANALYSIS & REFERENCE RESOLUTION

---

## 5.1 Reference Phenomena: Anaphora, Cataphora & Referring Expressions
*(Appeared in: Dec 2022 Q5b [10M], May 2023 Q1c/Q3b/Q4b [10M], Dec 2023 Q1e/Q3b [10M], May 2024 Q5a/b [10M], Dec 2024 Q1b/Q3b [10M], May 2025 Q1e/Q4b [10M])*

### Definitions
- **Referring Expression:** A linguistic phrase that points to an entity in the real or discourse world (the **referent**).
- **Coreference:** When two or more expressions refer to the exact same discourse entity.
- **Anaphora:** The linguistic phenomenon where an expression (the *anaphor*) derives its reference from a previously mentioned entity (the *antecedent*).
  - *Example:* *"**Elon Musk** launched the rocket. **He** smiled."* (`He` is an anaphor pointing back to `Elon Musk`).
- **Cataphora:** When the pronoun appears *before* the antecedent entity is introduced.
  - *Example:* *"When **she** entered the office, **Dr. Sarah** greeted her colleagues."*

### 5 Types of Referring Expressions
*(Appeared in: Dec 2023 Q3b [10M])*

1. **Indefinite Noun Phrases:** Introduces completely new, previously unmentioned entities into the discourse.
   - Form: Marked by indefinite articles (`a`, `an`) or bare plurals (`some`, quantifiers).
   - *Example:* *"I saw **a red Tesla** on the street."*
2. **Definite Noun Phrases:** Refers to entities that are identifiable, uniquely accessible, or already grounded in discourse.
   - Form: Marked by the definite article `the`.
   - *Example:* *"**The vehicle** was traveling at high speed."*
3. **Pronouns:** High-salience short grammatical tokens referring to active discourse entities.
   - Form: Personal (`he, she, it, they`), possessive (`his, her, their`), objective (`him, her, them`).
   - *Example:* *"**It** stopped abruptly at the light."*
4. **Demonstratives:** Referring expressions indicating relative cognitive or physical proximity (near vs far).
   - Form: `this, these` (proximal) vs `that, those` (distal).
   - *Example:* *"**This** is unacceptable; **that** was fine."*
5. **One-Anaphora:** Blends an indefinite referent with anaphoric category tracking.
   - Form: Pronoun `one` replacing a nominal head.
   - *Example:* *"I didn't like the green apple, so I picked the red **one**."*

### Syntactic and Semantic Constraints on Coreference
*(Appeared in: May 2025 Q1e [5M])*
1. **Number Agreement:** Singular pronouns require singular antecedents (*"The student finished **his** exam"* vs *"The students finished **their** exams"*).
2. **Person and Case Agreement:** 1st, 2nd, 3rd person and Nominative/Accusative/Genitive alignment (*"She gave **him** **his** book"*).
3. **Gender Agreement:** Pronoun gender must match referent (*"Mary loves **her** brother"*).
4. **Syntactic Binding Constraints (Chomsky's Binding Principles):**
   - *Principle A:* A reflexive pronoun (`himself`, `herself`) must be bound in its local syntactic domain (*"John$_i$ shaved himself$_i$"*).
   - *Principle B:* A non-reflexive pronoun (`him`, `her`) must be free in its local syntactic domain (*"John$_i$ shaved him$_j$"* $\implies i \ne j$).
5. **Selectional Restrictions:** Verbs impose semantic constraints on their arguments (*"The compiler crashed because **it** encountered a syntax error"* $\implies$ compiler is non-animate, hence `it`).

---

## 5.2 Hobbs' Parse-Tree Search Algorithm for Pronoun Resolution
*(Appeared in: Dec 2022 Q5b [10M], May 2024 Q5b [10M], Dec 2024 Q3b [10M], May 2025 Q4b [10M])*

Jerry Hobbs (1978) formulated a deterministic syntactic parse-tree traversal algorithm that searches for candidate antecedents using left-to-right, breadth-first dominance rules.

```
+---------------------------------------------------------------------------------------------------+
|                                 THE 9 STEPS OF HOBBS' ALGORITHM                                   |
+---------------------------------------------------------------------------------------------------+
| Step 1: Begin at the NP node immediately dominating the pronoun to be resolved.                  |
+---------------------------------------------------------------------------------------------------+
                                                  |
                                                  v
| Step 2: Go up the tree to the first NP or S node encountered. Call this node X, and call the      |
|         path to reach it p.                                                                       |
+---------------------------------------------------------------------------------------------------+
                                                  |
                                                  v
| Step 3: Traverse all branches below X to the LEFT of path p, in a left-to-right, breadth-first    |
|         manner. Propose any NP node encountered as a candidate antecedent (if it matches          |
|         gender/number constraints).                                                               |
+---------------------------------------------------------------------------------------------------+
                                                  |
                                                  v
| Step 4: If node X is the highest S node in the current sentence, go to Step 9 (Search Previous    |
|         Sentences). Otherwise, proceed to Step 5.                                                 |
+---------------------------------------------------------------------------------------------------+
                                                  |
                                                  v
| Step 5: From node X, go up the tree to the next NP or S node encountered. Call this new node X,   |
|         and call the path to reach it p.                                                          |
+---------------------------------------------------------------------------------------------------+
                                                  |
                                                  v
| Step 6: If node X is an NP node and path p did not pass through the Nominal that X dominates,     |
|         propose X as a candidate antecedent.                                                     |
+---------------------------------------------------------------------------------------------------+
                                                  |
                                                  v
| Step 7: Traverse all branches below X to the LEFT of path p, left-to-right, breadth-first.        |
|         Propose any NP node encountered as a candidate antecedent.                                |
+---------------------------------------------------------------------------------------------------+
                                                  |
                                                  v
| Step 8: If X is an S node, traverse branches below X to the RIGHT of path p (excluding any        |
|         subtrees dominated by an S or NP node), proposing matching NPs.                           |
|         Loop back to Step 4.                                                                      |
+---------------------------------------------------------------------------------------------------+
                                                  |
                                                  v
| Step 9: [Inter-sentential Search] Take the parse tree of the immediately preceding sentence.     |
|         Traverse the entire tree in a left-to-right, breadth-first manner. Propose the first      |
|         NP node encountered that matches gender/number/person constraints.                        |
+---------------------------------------------------------------------------------------------------+
```

---

## 5.3 Centering Theory: Complete Mathematical Formulation & Transitions
*(Appeared in: May 2023 Q4b [10M], May 2024 Q5b [10M], Dec 2024 Q3b [10M], May 2025 Q4b [10M])*

Developed by Barbara Grosz, Aravind Joshi, and Scott Weinstein (1995), Centering Theory models the local coherence of discourse by tracking the shifting focus of attention across adjacent utterances.

### Core Constructs:
For every utterance $U_n$ in a discourse:
1. **Forward-Looking Centers List $C_f(U_n)$:**
   An ordered set of all discourse entities mentioned in utterance $U_n$.
   Ranked strictly by grammatical salience:
   $$\mathbf{Subject > Object > Indirect \; Object > Other \; Obliques}$$
2. **Preferred Center $C_p(U_n)$:**
   The highest-ranked element in $C_f(U_n)$. It represents the speaker's predicted topic for the next utterance:
   $$C_p(U_n) = \text{First}(C_f(U_n))$$
3. **Backward-Looking Center $C_b(U_n)$:**
   The single entity that links utterance $U_n$ back to the preceding utterance $U_{n-1}$.
   It is the highest-ranked entity of $C_f(U_{n-1})$ that appears anywhere in $C_f(U_n)$:
   $$C_b(U_n) = \arg\max_{c \in C_f(U_n) \cap C_f(U_{n-1})} \text{Rank}_{C_f(U_{n-1})}(c)$$

### The 4 Discourse Transition States
The relationship between $U_{n-1}$ and $U_n$ is categorized along two orthogonal binary dimensions:
- Does the backward-looking center stay the same? ($C_b(U_n) = C_b(U_{n-1})$?)
- Is the backward-looking center the preferred center? ($C_b(U_n) = C_p(U_n)$?)

```
+---------------------------------------------------------------------------------------------------+
|                                  CENTERING THEORY TRANSITION MATRIX                               |
+---------------------------------------------------------------------------------------------------+
|                                      |   C_b(U_n) = C_b(U_{n-1})     |   C_b(U_n) != C_b(U_{n-1}) |
|                                      |      (Coherence Maintained)   |      (Center Has Shifted)  |
+--------------------------------------+-------------------------------+----------------------------+
| C_b(U_n) = C_p(U_n)                  |          CONTINUE             |        SMOOTH-SHIFT        |
| (Entity is predicted to continue)    |       (Most Coherent)         |       (Topic Changes)      |
+--------------------------------------+-------------------------------+----------------------------+
| C_b(U_n) != C_p(U_n)                 |           RETAIN              |        ROUGH-SHIFT         |
| (Entity is NOT predicted to continue)|   (Preparing to change topic) |      (Least Coherent)      |
+--------------------------------------+-------------------------------+----------------------------+
```

### Centering Theory Preference Rule:
Discourse coherence follows this strict descending order of transitions:
$$\mathbf{CONTINUE \succ RETAIN \succ SMOOTH\text{-}SHIFT \succ ROUGH\text{-}SHIFT}$$

### Comparison: Hobbs' Algorithm vs Centering Theory
*(Appeared in: Dec 2024 Q3b [10M])*

| Parameter | Hobbs' Algorithm | Centering Theory |
|:---|:---|:---|
| **Underlying Approach** | Purely syntactic tree-search traversal. | Discourse-pragmatic focus tracking model. |
| **Input Representation** | Precise syntactic parse trees ($S, NP, VP$). | Ordered lists of entities ranked by salience ($C_f, C_b, C_p$). |
| **Search Direction** | Left-to-right, breadth-first parse walk. | Evaluates candidate pronoun assignments against transition preferences. |
| **Inter-Sentential Model** | Linearly walks preceding sentence trees. | Computes $C_b(U_n)$ as highest-ranked intersection with $C_f(U_{n-1})$. |
| **Computational Nature** | Procedural, algorithmic, rule-based. | Declarative, cognitive constraint optimization. |

---

## MU Keyword Checklist: Module 5
- [ ] *Referring Expression, Referent, Antecedent, Anaphora, Cataphora*
- [ ] *5 Expressions: Indefinite NP, Definite NP, Pronouns, Demonstratives, One-Anaphora*
- [ ] *Number/Gender/Person Agreement, Chomsky Binding Principles A & B, Selectional Restrictions*
- [ ] *Hobbs Algorithm, 9-Step Parse-Tree Walk, Left-to-Right, Breadth-First, Dominance*
- [ ] *Centering Theory: Forward-Looking $C_f$, Backward-Looking $C_b$, Preferred Center $C_p$*
- [ ] *Grammatical Salience Ranking: Subject > Object > Indirect Object > Obliques*
- [ ] *Transition Matrix: Continue, Retain, Smooth-Shift, Rough-Shift*

---
---

# MODULE 6: NATURAL LANGUAGE ENGINEERING & APPLICATIONS

---

## 6.1 Machine Translation (MT) Architectures & The Vauquois Triangle
*(Appeared in: Dec 2022 Q1d [5M], May 2023 Q1d [5M], Dec 2023 Q1c [5M], May 2024 Q6a [10M], Dec 2024 Q1c [5M])*

Machine Translation systems automatically translate source natural language text $S$ into target natural language text $T$.

```
+---------------------------------------------------------------------------------------------------+
|                                    THE VAUQUOIS TRIANGLE                                          |
+---------------------------------------------------------------------------------------------------+
|                                      INTERLINGUA                                                  |
|                             (Deepest Semantic Abstraction)                                        |
|                                       /      \                                                    |
|                                      /        \                                                   |
|                                     /          \                                                  |
|                        Semantic Transfer    Semantic Transfer                                     |
|                                   /              \                                                |
|                                  /                \                                               |
|                    Syntactic Transfer          Syntactic Transfer                                 |
|                                /                    \                                             |
|                               /                      \                                            |
|                 Syntactic Analysis               Syntactic Generation                             |
|                             /                          \                                          |
|                            /                            \                                         |
|              Morphological Analysis               Morphological Generation                        |
|                          /                                \                                       |
|                         /                                  \                                      |
|    SOURCE TEXT --------+-------- DIRECT TRANSLATION --------+---------> TARGET TEXT               |
|                           (Word-for-Word Dictionary Mapping)                                      |
+---------------------------------------------------------------------------------------------------+
```

### The 4 Major MT Paradigms:

1. **Direct Machine Translation (Dictionary-Based):**
   - Primitive word-by-word substitution using massive bilingual dictionaries followed by simple morphological adjustments and local reordering rules.
   - *Limitation:* Incapable of handling long-range structural divergences or idioms.

2. **Transfer-Based Machine Translation:**
   - Follows a 3-stage pipeline: **Analysis $\to$ Transfer $\to$ Generation**.
   - *Syntactic Transfer:* Parses source sentence into source parse tree, transforms it to target language parse tree via transfer grammar rules, and generates target text.
   - *Semantic Transfer:* Maps source semantic predicate-argument structures to target semantic structures.

3. **Interlingua-Based MT:**
   - Translates source text into a completely language-independent semantic representation (**Interlingua**), from which target text is generated.
   - *Pro:* For $N$ languages, requires only $2N$ translation modules (instead of $N(N-1)$ pairs).
   - *Con:* Designing a universal semantic representation capable of capturing all human concepts is near impossible.

4. **Statistical Machine Translation (SMT) & The Noisy Channel Model:**
   - Formulates translation as decoding a corrupted signal through a noisy channel:
     $$\hat{E} = \arg\max_E P(E \mid F) = \arg\max_E \frac{P(F \mid E) P(E)}{P(F)} = \arg\max_E \underbrace{P(F \mid E)}_{\text{Translation Model}} \times \underbrace{P(E)}_{\text{Language Model}}$$
   - **Translation Model $P(F \mid E)$:** Ensures faithfulness/fidelity (word alignment via IBM Models 1-5, phrase-based tables).
   - **Language Model $P(E)$:** Ensures fluency and grammatical correctness in the target language (N-gram LM).

---

## 6.2 Information Retrieval (IR) vs Information Extraction (IE)
*(Appeared in: Dec 2022 Q4b [5M], May 2023 Q6a [10M], May 2024 Q6b [10M])*

```
+---------------------------------------------------------------------------------------------------+
|                                       IR VS IE COMPARATIVE MATRIX                                 |
+---------------------------------------------------------------------------------------------------+
| Parameter          | Information Retrieval (IR)            | Information Extraction (IE)          |
+--------------------+---------------------------------------+--------------------------------------+
| Primary Objective  | Selects relevant UNSTRUCTURED         | Extracts structured tabular semantic |
|                    | documents from a massive repository.  | facts/relations from text.           |
+--------------------+---------------------------------------+--------------------------------------+
| Input Format       | Short natural language query/keywords.| Unstructured raw document/corpus.    |
+--------------------+---------------------------------------+--------------------------------------+
| Output Format      | Ranked list of complete documents.    | Relational tuples / Filled templates.|
+--------------------+---------------------------------------+--------------------------------------+
| Underlying NLP     | Shallow (Stemming, Stopwords,         | Deep (NER, POS, Parsing, Semantic    |
| Depth              | Tokenization, Inverted Index).        | Role Labeling, Coreference).         |
+--------------------+---------------------------------------+--------------------------------------+
| Core Mathematics   | Vector Space Model, TF-IDF, BM25,     | Sequence Labeling (CRF, BiLSTM,      |
|                    | Cosine Similarity.                    | Transformer BERT NER).               |
+--------------------+---------------------------------------+--------------------------------------+
| Example Systems    | Google Search, Elasticsearch, Lucene. | Financial event extractors, PubMed   |
|                    |                                       | gene-disease interaction extractors. |
+--------------------+---------------------------------------+--------------------------------------+
```

### The Information Retrieval Mathematical Foundation:
1. **Term Frequency (TF):**
   $$\text{TF}(t, d) = \frac{f_{t, d}}{\sum_{t' \in d} f_{t', d}}$$
2. **Inverse Document Frequency (IDF):**
   $$\text{IDF}(t, D) = \log \left( \frac{|D|}{|\{d \in D : t \in d\}|} \right)$$
3. **TF-IDF Weight:**
   $$w_{t, d} = \text{TF}(t, d) \times \text{IDF}(t, D)$$
4. **Cosine Similarity Scoring:**
   $$\text{Sim}(Q, D_i) = \frac{\vec{V}(Q) \cdot \vec{V}(D_i)}{\|\vec{V}(Q)\| \|\vec{V}(D_i)\|} = \frac{\sum_{t} w_{t, Q} \cdot w_{t, D_i}}{\sqrt{\sum_t w_{t, Q}^2} \sqrt{\sum_t w_{t, D_i}^2}}$$

---

## 6.3 Text Summarization: Extractive vs Abstractive Paradigms
*(Appeared in: Dec 2022 Q6a [10M], Dec 2024 Q6a [10M])*

Text summarization condenses an extensive text into a compact summary preserving salient information.

```
+---------------------------------------------------------------------------------------------------+
|                                 TEXT SUMMARIZATION ARCHITECTURES                                  |
+---------------------------------------------------------------------------------------------------+
| EXTRACTIVE SUMMARIZATION:                                                                         |
|   - Identifies, scores, and extracts verbatim sentences from the source document.                 |
|   - Methods:                                                                                      |
|     1. Feature-Based: Sentence position, TF-IDF weight, presence of title words, cue phrases.     |
|     2. Graph-Based (TextRank / LexRank): Builds graph where nodes = sentences, edges = cosine     |
|        similarity. Computes PageRank centrality to select top sentences.                          |
|     3. Maximal Marginal Relevance (MMR): Balances relevance to query with diversity to eliminate |
|        redundancy: MMR = argmax [ lambda * Sim(s, Q) - (1 - lambda) * max_s' Sim(s, s') ]        |
|   - Pro: Grammatically intact, zero hallucination.                                                |
|   - Con: Cohesion lapses, dangling pronouns, verbose summaries.                                  |
+---------------------------------------------------------------------------------------------------+
| ABSTRACTIVE SUMMARIZATION:                                                                        |
|   - Synthesizes and paraphrases original content using novel words and compressed sentences.      |
|   - Architecture: Sequence-to-sequence Encoder-Decoder with Attention (BART, T5, PEGASUS).       |
|   - Pro: Human-like fluent synthesis, compact information density.                                |
|   - Con: Risk of hallucination (generating factually false statements).                          |
+---------------------------------------------------------------------------------------------------+
```

---

## 6.4 Question Answering Systems (QAS): Pipeline Architecture & Algorithms
*(Appeared in: Dec 2023 Q6a [10M], May 2025 Q6b [10M])*

A Question Answering System automatically retrieves concise, factual answers to natural language questions from unstructured document collections.

```
+---------------------------------------------------------------------------------------------------+
|                                    QAS 3-TIER PIPELINE ARCHITECTURE                               |
+---------------------------------------------------------------------------------------------------+
|  Input: "Who invented the telephone in 1876?"                                                     |
+---------------------------------------------------------------------------------------------------+
                                                  |
                                                  v
| TIER 1: QUESTION PROCESSING & ANALYSIS                                                            |
|   - Question Classification: Determines Expected Answer Type (EAT).                               |
|     (e.g., Li & Roth taxonomy: "Who" --> HUMAN:INDIVIDUAL).                                       |
|   - Focus & Topic Identification: Focus = "invented", Topic = "telephone".                       |
|   - Query Formulation: Strips interrogatives; expands synonyms via WordNet:                      |
|     Query = ('telephone' AND 'invented' AND '1876').                                               |
+---------------------------------------------------------------------------------------------------+
                                                  |
                                                  v
| TIER 2: DOCUMENT & PASSAGE RETRIEVAL                                                              |
|   - Document Retrieval: Uses BM25 or TF-IDF to retrieve top-k candidate documents.                |
|   - Passage Segmentation: Divides documents into short paragraphs/passages (3-5 sentences).       |
|   - Passage Ranking: Ranks passages based on term density, exact phrase matching, and EAT.        |
+---------------------------------------------------------------------------------------------------+
                                                  |
                                                  v
| TIER 3: ANSWER EXTRACTION & SELECTION                                                             |
|   - Named Entity Recognition (NER): Tags entities in top passages matching EAT (PERSON).           |
|   - Candidate Scoring: Evaluates syntactic dependency relations with question terms.              |
|   - Answer Selection: Extracts exact span "Alexander Graham Bell" with maximum confidence score.  |
+---------------------------------------------------------------------------------------------------+
                                                  |
                                                  v
|  Final Answer: "Alexander Graham Bell"                                                            |
+---------------------------------------------------------------------------------------------------+
```

---

## MU Keyword Checklist: Module 6
- [ ] *Vauquois Triangle: Direct Translation, Syntactic Transfer, Semantic Transfer, Interlingua*
- [ ] *SMT Noisy Channel Model: $P(E \mid F) \propto P(F \mid E) \cdot P(E)$, Translation Model, Language Model*
- [ ] *Information Retrieval vs Information Extraction (Unstructured docs vs Structured facts)*
- [ ] *TF-IDF Formula, Inverted Index, Cosine Similarity*
- [ ] *Extractive (Verbatim sentences, TextRank PageRank, MMR) vs Abstractive (Seq2Seq, Paraphrasing)*
- [ ] *Question Answering System 3-Tiers: Question Processing (EAT), Passage Retrieval, Answer Extraction*
