# Mumbai University (MU) Semester 7 — Natural Language Processing (NLP)
## Masterclass Part 1: Modules 1 & 2 (Foundations, Morphology, Language Modeling & POS Tagging)
**Course Code:** 42175 (DLOC - III) | **Scheme:** Rev 2019 / C-Scheme | **Applicable Cycles:** Dec 2022 – May 2025

---

# MODULE 1: INTRODUCTION & MORPHOLOGICAL ANALYSIS

---

## 1.1 Stages of Natural Language Processing (The NLP Pipeline)
*(Appeared in: Dec 2022 Q2b [10M], May 2023 Q1e [5M], Dec 2023 Q2b [10M], May 2024 Q1a/d [5M], Dec 2024 Q2b [10M], May 2025 Q2b [10M])*

### Architectural Pipeline of NLP
Human language processing requires a structured cascade of analyses starting from raw acoustic signals or character bytes up to situational discourse context.

```
+---------------------------------------------------------------------------------------------------+
|                                     THE 6-STAGE NLP PIPELINE                                      |
+---------------------------------------------------------------------------------------------------+
|  [Raw Input Text] --> "The bank had to freeze accounts because the river bank flooded."          |
+---------------------------------------------------------------------------------------------------+
                                                  |
                                                  v
| 1. PHONETICS & PHONOLOGY                                                                          |
|    - Studies physical sound waves (phonetics) and systematic sound patterns (phonology).          |
|    - Focuses on phonemes, stress, intonation, and speech-to-text acoustic modeling.               |
+---------------------------------------------------------------------------------------------------+
                                                  |
                                                  v
| 2. MORPHOLOGICAL ANALYSIS                                                                         |
|    - Breaks words down into morphemes (stems, roots, prefixes, suffixes).                         |
|    - Tokenization, Stemming (Porter), Lemmatization, Inflectional/Derivational parsing.           |
|    - Example: "unhappiness" --> [un- (prefix)] + [happy (root)] + [-ness (suffix)]                |
+---------------------------------------------------------------------------------------------------+
                                                  |
                                                  v
| 3. SYNTACTIC ANALYSIS (PARSING)                                                                   |
|    - Enforces grammatical structures and linear ordering of tokens using Formal Grammars (CFG).   |
|    - Constructs Parse Trees / Dependency Trees checking Subject-Verb-Object agreement.            |
|    - Example: [S [NP [Det The] [N bank]] [VP [V froze] [NP [N accounts]]]]                        |
+---------------------------------------------------------------------------------------------------+
                                                  |
                                                  v
| 4. SEMANTIC ANALYSIS                                                                              |
|    - Determines the literal, context-independent compositional meaning of phrases and sentences.  |
|    - Resolves lexical word senses (Word Sense Disambiguation - WSD) and thematic roles.           |
|    - Example: Disambiguates "financial institution" vs "sloping land beside a river".            |
+---------------------------------------------------------------------------------------------------+
                                                  |
                                                  v
| 5. DISCOURSE INTEGRATION                                                                          |
|    - Interprets multi-sentence textual units; connects references across sentence boundaries.     |
|    - Coreference resolution, Anaphora resolution (Hobbs algorithm, Centering Theory).             |
|    - Example: In "John bought a car. It is blue.", resolves "It" --> "car".                      |
+---------------------------------------------------------------------------------------------------+
                                                  |
                                                  v
| 6. PRAGMATIC ANALYSIS                                                                             |
|    - Incorporates real-world knowledge, speaker intentions, social conventions, and illocution.   |
|    - Speech act theory, sarcasm detection, conversational implicatures.                           |
|    - Example: "Can you pass the salt?" interpreted as a REQUEST, not an inquiry into ability.     |
+---------------------------------------------------------------------------------------------------+
```

### Detailed Breakdown of Each Stage

1. **Phonology / Phonetics:**
   - **Definition:** The level dealing with sound structure. In speech processing, it transforms continuous acoustic waveforms into discrete phonetic units (phones/phonemes) using acoustic models (e.g., MFCCs, Hidden Markov Models, DNNs).
   - **Key Concepts:** Allophones, syllable boundaries, prosody, intonation.

2. **Morphology:**
   - **Definition:** The study of word formation and structure from minimal meaning-bearing units called **morphemes**.
   - **Types of Morphemes:**
     - *Free Morphemes:* Can stand alone as independent words (e.g., `cat`, `walk`, `table`).
     - *Bound Morphemes:* Must attach to other morphemes; cannot stand alone (e.g., `-ed`, `-s`, `un-`, `pre-`).

3. **Syntax:**
   - **Definition:** The study of structural rules governing how words combine into phrases, clauses, and complete grammatical sentences.
   - **Formalism:** Context-Free Grammars (CFG), Treebanks (Penn Treebank), dependency representations. Checks if a sentence is grammatically well-formed according to rules such as $S \to NP \; VP$.

4. **Semantics:**
   - **Definition:** Focuses on the literal meaning of words, phrases, and compositional propositions, mapping linguistic forms into semantic representations (e.g., First-Order Predicate Calculus, Lambda calculus).
   - **Key Tasks:** Word Sense Disambiguation (WSD), Semantic Role Labeling (SRL), Named Entity Recognition (NER).

5. **Discourse Integration:**
   - **Definition:** Language processing that extends beyond individual sentence boundaries. A sentence's meaning depends directly on preceding sentences.
   - **Key Tasks:** Anaphora resolution (pronouns pointing backward), Cataphora resolution (pronouns pointing forward), discourse coherence relations, rhetorical structure theory.

6. **Pragmatics:**
   - **Definition:** The study of how context influences the interpretation of meaning, bridging the gap between literal sentence meaning and speaker meaning.
   - **Key Tasks:** Gricean maxims of conversation, speech act classification (assertives, directives, commissives, expressives, declarations).

---

## 1.2 Ambiguities at Each Stage of NLP
*(Appeared in: Dec 2022 Q1a [5M], May 2023 Q3a [10M], Dec 2023 Q2b [10M], Dec 2024 Q1e [5M])*

Ambiguity is the core scientific challenge of NLP: natural human language is inherently polysemic, non-deterministic, and context-dependent.

```
+---------------------------------------------------------------------------------------------------+
|                                  NLP AMBIGUITY TAXONOMY & EXAMPLES                                |
+---------------------------------------------------------------------------------------------------+
| 1. Phonological Ambiguity:                                                                        |
|    - Acoustic confusion between identical sound sequences.                                       |
|    - Example: "I scream" vs "Ice cream"; "recognize speech" vs "wreck a nice beach".              |
+---------------------------------------------------------------------------------------------------+
| 2. Lexical / Morphological Ambiguity:                                                             |
|    - A single word token possesses multiple dictionary definitions or parts of speech.           |
|    - Category Ambiguity: "bear" (Noun: animal) vs "bear" (Verb: to carry/tolerate).               |
|    - Polysemy: "bank" (financial institution) vs "bank" (sloping river edge).                    |
+---------------------------------------------------------------------------------------------------+
| 3. Syntactic / Structural Ambiguity:                                                              |
|    - A sentence admits multiple distinct valid parse trees.                                       |
|    - Prepositional Phrase (PP) Attachment: "I saw the man with a telescope."                     |
|      Tree 1: [VP saw [NP the man] [PP with a telescope]] (Instrument of seeing)                   |
|      Tree 2: [VP saw [NP the man [PP with a telescope]]] (Man holds telescope)                    |
|    - Coordination Ambiguity: "Old men and women" --> [Old [men and women]] vs [[Old men] and women]|
+---------------------------------------------------------------------------------------------------+
| 4. Semantic Scope Ambiguity:                                                                      |
|    - Multiple quantifiers or logical operators allow different interpretations.                  |
|    - Example: "Every student loves a teacher."                                                    |
|      Meaning 1 ($\forall s \exists t$): Each student has some teacher they love.                  |
|      Meaning 2 ($\exists t \forall s$): There is one single teacher whom all students love.       |
+---------------------------------------------------------------------------------------------------+
| 5. Referential / Discourse Ambiguity:                                                             |
|    - Ambiguous antecedent for pronouns across clauses.                                            |
|    - Example: "The boy told his father the secret because he was worried."                        |
|      Does "he" refer to the boy or the father?                                                    |
+---------------------------------------------------------------------------------------------------+
| 6. Pragmatic Ambiguity:                                                                           |
|    - Unclear speaker intent, sarcasm, or non-literal meaning.                                     |
|    - Example: "Can you close the door?"                                                           |
|      Literal: Questioning physical capability. Pragmatic: A polite directive to close the door.  |
+---------------------------------------------------------------------------------------------------+
```

### Comprehensive Comparison: Lexical vs Syntactic Ambiguity

| Parameter | Lexical Ambiguity | Syntactic (Structural) Ambiguity |
|:---|:---|:---|
| **Locus of Ambiguity** | Isolated word level (single token). | Sentence or phrase level (grammatical relationship). |
| **Root Cause** | Homonymy (different etymology, same spelling), Polysemy (related meanings), Category overlap. | Multiple valid Context-Free Grammar derivation trees for the exact same linear sequence of tokens. |
| **Classic Example** | *"He deposited money at the **bank**."* / *"We need to **table** this motion."* | *"Flying planes can be dangerous."* (Act of flying vs airplanes that fly) |
| **Resolution Method** | Word Sense Disambiguation (Lesk algorithm, WordNet embedding, Naive Bayes, BERT). | Probabilistic Context-Free Grammars (PCFG), Shift-Reduce parsers, CYK dynamic programming. |
| **Parsing Impact** | Generates multiple initial POS tags for a single leaf node. | Causes multiple branchings in non-terminal nodes ($NP, VP, PP$). |

---

## 1.3 Morphology: Inflectional vs Derivational, Open vs Closed Class Words
*(Appeared in: Dec 2022 Q1b/c [5M], May 2023 Q2b [10M], May 2024 Q2a [10M], May 2025 Q1a/b [5M])*

### Definitions: Stems, Roots, and Affixes
- **Stem:** The base form to which morphological affixes attach. (e.g., in `connecting`, `connect` is the stem).
- **Root:** The fundamental lexical unit of a word that cannot be reduced into smaller morphemes (e.g., in `irreplaceability`, `place` is the root).
- **Affixes:** Bound morphemes that attach to roots/stems.
  - **Prefix:** Attached before the root (e.g., `un-`, `re-`, `dis-`).
  - **Suffix:** Attached after the root (e.g., `-able`, `-ing`, `-tion`).
  - **Infix:** Inserted directly inside a root (common in Tagalog and Arabic; rare in English except colloquial expletive infixation: `abso-freaking-lutely`).
  - **Circumfix:** Attached both before and after a root simultaneously (common in German: `ge-` + `seh` + `-en` = `gesehen`).

### Inflectional vs Derivational Morphology

```
+---------------------------------------------------------------------------------------------------+
|                              INFLECTIONAL VS DERIVATIONAL MORPHOLOGY                              |
+---------------------------------------------------------------------------------------------------+
| INFLECTIONAL MORPHOLOGY:                                                                          |
|   - Modifies word's grammatical form without changing its syntactic category or core meaning.     |
|   - Predictable, highly productive, closes the word to further affixation.                        |
|   - English has only 8 inflectional affixes:                                                      |
|     1. Noun plural (-s): cat --> cats                                                             |
|     2. Noun possessive (-'s): Mary --> Mary's                                                     |
|     3. Verb 3rd person singular present (-s): he wait --> he waits                                |
|     4. Verb past tense (-ed): wait --> waited                                                     |
|     5. Verb past participle (-en/-ed): eat --> eaten                                              |
|     6. Verb present participle (-ing): sing --> singing                                           |
|     7. Adjective comparative (-er): fast --> faster                                               |
|     8. Adjective superlative (-est): fast --> fastest                                             |
+---------------------------------------------------------------------------------------------------+
| DERIVATIONAL MORPHOLOGY:                                                                          |
|   - Creates completely new words, often changing grammatical part of speech and core meaning.     |
|   - Less productive, unpredictable semantic shifts.                                               |
|   - Examples:                                                                                     |
|     - Verb to Noun: write (V) + -er --> writer (N)                                                |
|     - Adjective to Adverb: quick (Adj) + -ly --> quickly (Adv)                                    |
|     - Noun to Adjective: friend (N) + -ly --> friendly (Adj)                                      |
|     - Meaning inversion: legal + il- --> illegal                                                  |
+---------------------------------------------------------------------------------------------------+
```

### Morphological Analysis Output Representation
*(Explicit MU Question: "Represent output of morphological analysis for Regular verb, Irregular verb, singular noun, plural noun" — May 2023 Q2b, May 2025 Q1b)*

| Word Class | Input Surface Word | Morphological Analysis Output Representation | Explanation |
|:---|:---|:---|:---|
| **Regular Verb** | `walked` | `walk + V + PAST` | Root `walk`, Part of Speech Verb (`V`), Past tense inflection (`PAST`). |
| **Regular Verb** | `walking` | `walk + V + PRES_PART` | Root `walk`, Verb (`V`), Present participle (`PRES_PART`). |
| **Irregular Verb** | `went` | `go + V + PAST` | Root `go` (suppletive form), Verb (`V`), Past tense (`PAST`). |
| **Irregular Verb** | `caught` | `catch + V + PAST` | Root `catch`, Verb (`V`), Past tense (`PAST`). |
| **Singular Noun** | `dog` | `dog + N + SG` | Root `dog`, Part of Speech Noun (`N`), Number Singular (`SG`). |
| **Plural Noun** | `dogs` | `dog + N + PL` | Root `dog`, Noun (`N`), Number Plural (`PL`). |
| **Irregular Plural Noun** | `geese` | `goose + N + PL` | Root `goose`, Noun (`N`), Number Plural (`PL`). |

---

### 🌟 Word Level Analysis: Tokenization, Stemming, and Lemmatization [5 Marks] — Nov'25 (Q1b)
**Question:** *"What is word level analysis? Explain the following terms with examples: Tokenization, Stemming, Lemmatization."*

#### 1. Concept of Word Level Analysis
**Word Level Analysis** (Morphological Analysis) is the primary structural tier in the NLP processing pipeline. It examines words in isolation as discrete lexical units, segmenting character sequences, analyzing sub-word morphemes (stems, roots, prefixes, suffixes), and stripping inflectional variations to standardize words into base grammatical canonical forms for downstream parsing and semantic processing.

#### 2. Core Word Level Techniques & Examples:

```
┌──────────────────────────────────────────────────────────────────────────────────┐
│                           WORD LEVEL ANALYSIS PIPELINE                           │
│                                                                                  │
│  Raw Input:      "The patient's legs were aching badly."                         │
│                           │                                                      │
│                           ▼ [TOKENIZATION]                                       │
│  Tokens:         ["The", "patient", "'s", "legs", "were", "aching", "badly", "."]│
│                           │                                                      │
│         ┌─────────────────┴─────────────────┐                                    │
│         ▼ [STEMMING]                        ▼ [LEMMATIZATION]                    │
│  Crude heuristic stripping:          Dictionary & POS-aware normalization:       │
│  "aching" --> "ach" (non-word!)      "aching" (Verb) --> "ache" (valid lemma)    │
│  "were"   --> "were"                 "were"   (Verb) --> "be"   (base root)      │
│  "legs"   --> "leg"                  "legs"   (Noun) --> "leg"                   │
│  "badly"  --> "badli"                "badly"  (Adv)  --> "badly"                 │
└──────────────────────────────────────────────────────────────────────────────────┘
```

1. **Tokenization:**
   - **Definition:** The fundamental process of breaking an unstructured character sequence (sentences, paragraphs) into discrete, semantically meaningful units called **tokens** (words, punctuation, numbers).
   - **Challenges:** Clitic separation (`don't` $\to$ `do` + `n't` or `patient's` $\to$ `patient` + `'s`), hyphenated compounds (`state-of-the-art`), and domain-specific tokens (URLs, emails, emoticons).
   - **Example:** Sentence `"Dr. Smith arrived at 5:30 p.m."` $\to$ `["Dr.", "Smith", "arrived", "at", "5:30", "p.m."]` (correctly handling abbreviations without erroneously splitting at periods).
2. **Stemming:**
   - **Definition:** A fast, crude heuristic process that chops off the affixes (suffixes and prefixes) of words based on predefined string-transformation rules, hoping to map related word forms to a common base stem.
   - **Characteristics:** Fast and computationally lightweight; does **not** require a dictionary; often produces non-real grammatical words (crude stems).
   - **Errors:**
     - *Over-stemming:* Conflating unrelated words (e.g., `universe`, `university` $\to$ `univers`).
     - *Under-stemming:* Failing to conflate related words (e.g., `alumna`, `alumni` $\to$ distinct stems).
   - **Example (Porter Stemmer):**
     - `"studies"` $\to$ `"studi"`
     - `"studying"` $\to$ `"studi"`
     - `"troublesome"` $\to$ `"troubl"`
3. **Lemmatization:**
   - **Definition:** A sophisticated algorithmic process that determines the canonical base dictionary form of a word—known as its **lemma**—by performing complete morphological analysis utilizing vocabulary dictionaries (like WordNet) and taking into account the word's Part-of-Speech (POS) in context.
   - **Characteristics:** Computationally slower; strictly guarantees that the output lemma is a valid, existing grammatical dictionary headword.
   - **Example (Context-Aware):**
     - `"meeting"` as a Noun: `"The committee held three meetings."` $\to$ Lemma: `"meeting"`.
     - `"meeting"` as a Verb: `"We were meeting in the hall."` $\to$ Lemma: `"meet"`.
     - `"better"` (Adjective) $\to$ Lemma: `"good"`.
     - `"was" / "were"` (Verb) $\to$ Lemma: `"be"`.

---

### Open Class vs Closed Class Words
*(Appeared in: Dec 2022 Q1c [5M])*

- **Open Class Words (Content Words):**
  - New words are constantly invented and incorporated into this category as technology, culture, and society evolve.
  - Carry heavy, standalone semantic weight.
  - Four primary classes:
    1. **Nouns:** `blockchain`, `prompt`, `cryptocurrency`, `selfie`.
    2. **Verbs:** `google` (as a verb), `download`, `tweet`, `jailbreak`.
    3. **Adjectives:** `algorithmic`, `viral`, `cloud-native`.
    4. **Adverbs:** `dynamically`, `computationally`.
- **Closed Class Words (Function Words):**
  - Grammatical structural words with fixed, finite membership. Languages rarely or never accept new members into these classes.
  - Primarily manage syntactic relationships between content words.
  - Classes:
    1. **Prepositions:** `in`, `on`, `at`, `under`, `between`, `of`.
    2. **Determiners / Articles:** `the`, `a`, `an`, `this`, `that`.
    3. **Pronouns:** `he`, `she`, `it`, `they`, `whom`.
    4. **Conjunctions:** `and`, `but`, `or`, `yet`, `because`.
    5. **Auxiliaries & Modals:** `is`, `was`, `can`, `could`, `will`, `should`.

---

## 1.4 Finite State Automata (FSA) & Transducers (FST) in Morphology
*(Appeared in: Dec 2022 Q2a [10M], May 2023 Q2b [10M], Dec 2023 Q2a [10M], Dec 2024 Q2a [10M])*

### Two-Level Morphology Architecture
A **Finite State Automata (FSA)** acts as a recognizer (accepting valid morphological strings). A **Finite State Transducer (FST)** maps an input tape to an output tape, enabling two-way translation between the abstract lexical representation and the actual surface spelling.

```
+---------------------------------------------------------------------------------------------------+
|                                TWO-LEVEL MORPHOLOGICAL ARCHITECTURE                               |
+---------------------------------------------------------------------------------------------------+
|  LEXICAL LEVEL (Tape 1):       c   a   t   +N   +PL       |   f   o   x   +N   +PL                |
+---------------------------------------------------------------------------------------------------+
                                   |                           |
                                   v                           v
                           [ FST 1: Lexicon Transducer ]
                                   |                           |
                                   v                           v
| INTERMEDIATE LEVEL (Tape 2):    c   a   t   ^   s         |   f   o   x   ^   s                   |
+---------------------------------------------------------------------------------------------------+
                                   |                           |
                                   v                           v
                           [ FST 2: Orthographic / Spelling Rules (e-insertion) ]
                                   |                           |
                                   v                           v
| SURFACE LEVEL (Tape 3):         c   a   t   s             |   f   o   x   e   s                   |
+---------------------------------------------------------------------------------------------------+
```

### Design of FSA for English Numbers 1–99
*(Appeared in: Dec 2023 Q2a [10M])*

English numbers from 1 to 99 are composed of:
1. **Single Digits (1-9):** `one`, `two`, `three`, `four`, `five`, `six`, `seven`, `eight`, `nine`.
2. **Teens (10-19):** `ten`, `eleven`, `twelve`, `thirteen`, `fourteen`, `fifteen`, `sixteen`, `seventeen`, `eighteen`, `nineteen`.
3. **Decades (20, 30, 40, ..., 90):** `twenty`, `thirty`, `forty`, `fifty`, `sixty`, `seventy`, `eighty`, `ninety`.
4. **Compound Numbers (21-99 excluding multiples of 10):** Decade + hyphen/space + Single Digit (e.g., `twenty-one`, `ninety-nine`).

#### State Transition Table & Diagram for Numbers 1–99

```
                 +----------------- Digit (1-9) ------------------> ((q_final))
                 |                                                      ^
                 |                                                      |
                 |                                                      |
              [q0] (Start) -------- Teens (10-19) ----------------------+
                 |                                                      |
                 |                                                      |
                 +----------------- Decades (20-90) ---------> [q1] ----+
                                                                |   (epsilon)
                                                                |
                                                                +-- Hyphen/Space + Digit (1-9) --> ((q_final))
```

- **States:**
  - $q_0$: Initial state (Start).
  - $q_1$: Decade parsed state (e.g., after reading `twenty`, `thirty`, ..., `ninety`).
  - $q_f$: Final accepting state.
- **Transitions:**
  - $\delta(q_0, \text{Digit}) = q_f$, where $\text{Digit} \in \{\text{one, two, three, four, five, six, seven, eight, nine}\}$.
  - $\delta(q_0, \text{Teens}) = q_f$, where $\text{Teens} \in \{\text{ten, eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen}\}$.
  - $\delta(q_0, \text{Decades}) = q_1$, where $\text{Decades} \in \{\text{twenty, thirty, forty, fifty, sixty, seventy, eighty, ninety}\}$.
  - $\delta(q_1, \epsilon) = q_f$ (Handles pure decades like `twenty`, `fifty`).
  - $\delta(q_1, \text{Hyphen/Space} + \text{Digit}) = q_f$ (Handles compound numbers like `twenty-one`, `forty-five`).

### FST for Regular and Plural Nouns
*(Appeared in: Dec 2024 Q2a [10M])*

The transducer operates on two tapes:
- **Upper / Lexical Tape:** Word root followed by grammatical tags: `f o x +N +PL`
- **Lower / Surface Tape:** Resulting orthographic string: `f o x e s`

```
  Input (Lexical):   f : f    o : o    x : x    +N : epsilon    +PL : ^s
                       |        |        |           |             |
                       v        v        v           v             v
  Intermediate:      f        o        x             ^             s
                       |        |        |           |             |
                       v        v        v           v             v
  Rule Transducer:   f : f    o : o    x : x       ^ : e         s : s   --> "foxes"
```
- **Rule Transducer (E-insertion Rule):**
  $\epsilon \to e \Big/ \{s, x, z, ch, sh\}^{\wedge} \_\_ s$
  *Logic:* Insert letter `e` between an intermediate morpheme boundary symbol `^` and suffix `s` if the preceding stem ends in a sibilant consonant (`s, x, z, ch, sh`).

---

## 1.5 Porter's Stemming Algorithm: Complete Rules & Step-by-Step Traces
*(Appeared in: Dec 2022 Q6b [10M], May 2023 Q5b [10M], Dec 2023 Q5a [10M], May 2024 Q2b [10M], Dec 2024 Q5a [10M])*

Martin Porter's algorithm (1980) is an iterative, rule-based conflation stemmer for English based on suffix stripping without relying on a full dictionary.

### Formal Notation & The Measure $m$
A consonant is represented by $c$, a vowel by $v$. Sequences of consonants are denoted $C$, sequences of vowels $V$.
Any English word can be represented by the master pattern:

$$[C](VC)^m[V]$$

where:
- $[C]$ denotes optional initial consonants.
- $[V]$ denotes optional trailing vowels.
- $m$ is the **measure** of the word (the count of alternating $VC$ sequences).

#### Calculating the Measure $m$:
- $m = 0$: `TR` ($C$), `EE` ($V$), `TREE` ($CV$), `Y` ($V$).
- $m = 1$: `TROUBLE` ($C(VC)^1$), `OATS` ($(VC)^1$), `TREES` ($C(VC)^1$).
- $m = 2$: `TROUBLES` ($C(VC)^2$), `PRIVATE` ($C(VC)^2$), `ORBITAL` ($(VC)^2$).

#### Additional Conditions on Stem $S$:
- `*v*`: Stem contains at least one vowel.
- `*d`: Stem ends with a double consonant (e.g., `-TT`, `-SS`, `-ZZ`).
- `*o`: Stem ends in $c v c$ where the final consonant is not $w, x,$ or $y$ (e.g., `-WIL`, `-HOP`).

### The 5 Cascading Steps of Porter's Algorithm

```
+---------------------------------------------------------------------------------------------------+
|                              PORTER STEMMER STEP-BY-STEP CASCADE                                  |
+---------------------------------------------------------------------------------------------------+
| STEP 1a: Plurals and Third Person Singular Suffixes                                               |
|   SSES --> SS          (caresses --> caress)                                                      |
|   IES  --> I           (ponies --> poni, ties --> ti)                                             |
|   SS   --> SS          (caress --> caress)                                                        |
|   S    --> null        (cats --> cat)                                                             |
+---------------------------------------------------------------------------------------------------+
| STEP 1b: Past Tense and Participles                                                               |
|   (m > 0) EED --> EE   (feed --> feed [m=0, no], agreed --> agree [m=1, yes])                     |
|   (*v*) ED   --> null  (plastered --> plaster, bled --> bled [*v* fails])                         |
|   (*v*) ING  --> null  (motoring --> motor, sing --> sing [*v* fails])                            |
|   If rule 2 or 3 succeeded and stem ends in:                                                      |
|     AT --> ATE         (conflat(ed) --> conflate)                                                 |
|     BL --> BLE         (troubl(ed) --> trouble)                                                   |
|     IZ --> IZE         (siz(ed) --> size)                                                         |
|     (*d and not (*L or *S or *Z)) --> single consonant (hopp(ed) --> hop, tann(ed) --> tan)       |
|     (m=1 and *o) --> E (fail(ed) --> fail)                                                        |
+---------------------------------------------------------------------------------------------------+
| STEP 1c: Y-Replacement                                                                            |
|   (*v*) Y --> I        (happy --> happi, sky --> sky [*v* fails])                                 |
+---------------------------------------------------------------------------------------------------+
| STEP 2: Derivational Suffix Stripping for m > 0                                                   |
|   (m > 0) ATIONAL --> ATE     (relational --> relate)                                             |
|   (m > 0) TIONAL  --> TION    (conditional --> condition)                                         |
|   (m > 0) ENCI    --> ENCE    (valenci --> valence)                                               |
|   (m > 0) ANCI    --> ANCE    (hesitanci --> hesitance)                                           |
|   (m > 0) IZER    --> IZE     (digitizer --> digitize)                                            |
|   (m > 0) ABLI    --> ABLE    (conformabli --> conformable)                                       |
|   (m > 0) ALLI    --> AL      (radicalli --> radical)                                             |
|   (m > 0) ENTLI   --> ENT     (differentli --> different)                                         |
|   (m > 0) ELI     --> E       (vileli --> vile)                                                   |
|   (m > 0) OUSLI   --> OUS     (analogousli --> analogous)                                         |
|   (m > 0) IZATION --> IZE     (modernization --> modernize)                                       |
|   (m > 0) ATION   --> ATE     (predication --> predicate)                                         |
|   (m > 0) ATOR    --> ATE     (operator --> operate)                                              |
|   (m > 0) ALISM   --> AL      (feudalism --> feudal)                                              |
|   (m > 0) IVENESS --> IVE     (decisiveness --> decisive)                                         |
|   (m > 0) FULNESS --> FUL     (hopefulness --> hopeful)                                           |
|   (m > 0) OUSNESS --> OUS     (callousness --> callous)                                           |
+---------------------------------------------------------------------------------------------------+
| STEP 3: Further Derivational Reductions for m > 0                                                 |
|   (m > 0) ICATE   --> IC      (triplicate --> triplic)                                            |
|   (m > 0) ATIVE   --> null    (formative --> form)                                                |
|   (m > 0) ALIZE   --> AL      (formalize --> formal)                                              |
|   (m > 0) ICITI   --> IC      (electriciti --> electric)                                          |
|   (m > 0) ICAL    --> IC      (electrical --> electric)                                           |
|   (m > 0) FUL     --> null    (hopeful --> hope)                                                  |
|   (m > 0) NESS    --> null    (goodness --> good)                                                 |
+---------------------------------------------------------------------------------------------------+
| STEP 4: Suffix Removal for m > 1                                                                  |
|   (m > 1) AL      --> null    (revival --> reviv)                                                 |
|   (m > 1) ANCE    --> null    (allowance --> allow)                                               |
|   (m > 1) ENCE    --> null    (inference --> infer)                                               |
|   (m > 1) ER      --> null    (airliner --> airlin)                                               |
|   (m > 1) IC      --> null    (gyroscopic --> gyroscop)                                           |
|   (m > 1) ABLE    --> null    (adjustable --> adjust)                                             |
|   (m > 1) IBLE    --> null    (defensible --> defens)                                             |
|   (m > 1) ANT     --> null    (irritant --> irrit)                                                |
|   (m > 1) MENT    --> null    (adjustment --> adjust)                                             |
|   (m > 1) ENT     --> null    (dependent --> depend)                                              |
|   (m > 1 and (*S or *T)) ION --> null (adoption --> adopt)                                        |
|   (m > 1) OU      --> null    (homologou --> homolog)                                             |
|   (m > 1) ISM     --> null    (communism --> commun)                                              |
|   (m > 1) ATE     --> null    (activate --> activ)                                                |
|   (m > 1) ITI     --> null    (angulariti --> angular)                                            |
|   (m > 1) OUS     --> null    (homologous --> homolog)                                            |
|   (m > 1) IVE     --> null    (effective --> effect)                                              |
|   (m > 1) IZE     --> null    (bowdlerize --> bowdler)                                            |
+---------------------------------------------------------------------------------------------------+
| STEP 5: Tidying Up Output                                                                         |
|   Step 5a: (m > 1) E --> null  (probate --> probat, rate --> rate [m=1, preserved])               |
|            (m = 1 and not *o) E --> null (cease --> ceas)                                         |
|   Step 5b: (m > 1 and *d and *L) --> single consonant (controll --> control, roll --> roll)       |
+---------------------------------------------------------------------------------------------------+
```

### Complete Word Execution Traces (Exam Favorites)

1. **Input Word: `RELATIONAL`**
   - Step 1a, 1b, 1c: No match.
   - Step 2: Suffix `-ATIONAL`. Rule: `(m > 0) ATIONAL --> ATE`.
     Stem remaining: `REL` $\to$ Consonant-Vowel: $R(c) \, E(v) \, L(c) \implies m = 1 > 0$.
     Transformation: `RELATIONAL` $\to$ `RELATE`.
   - Step 3: Suffix `-ATE` (not matching Step 3 rules).
   - Step 4: Rule: `(m > 1) ATE --> null`. Stem: `REL` has $m = 1 \ngtr 1$. Suffix is preserved.
   - Step 5: `(m = 1 and not *o) E --> null`. Stem `RELAT` has $m = 2$.
   - **Final Output:** `relate`.

2. **Input Word: `TROUBLES`**
   - Step 1a: Rule `S --> null`. Stem: `TROUBLE`. Output: `trouble`.
   - Step 1b, 1c: No match.
   - Step 2, 3, 4: No match.
   - Step 5a: Suffix `-E`. Stem `TROUBL` $\to$ $T(c) \, R(c) \, OU(v) \, B(c) \, L(c) \implies m = 1$. Condition `(m=1 and not *o)`: ends in $BL$ which is not $c v c \implies E$ dropped.
   - **Final Output:** `troubl`.

---

## 1.6 Preprocessing Operations in NLP
*(Appeared in: Dec 2024 Q2b [10M], May 2025 Q1d [5M])*

Text preprocessing converts noisy, unstructured human text into standardized discrete symbols ready for numerical vectorization.

```
+---------------------------------------------------------------------------------------------------+
|                                 TEXT PREPROCESSING ARCHITECTURE                                   |
+---------------------------------------------------------------------------------------------------+
|  Raw Text: "Mr. O'Neill spent $4.5M on AI-driven servers in New York! Don't wait..."              |
+---------------------------------------------------------------------------------------------------+
                                                  |
                                                  v
| 1. SENTENCE SEGMENTATION (PUNKT ALGORITHM / REGEX)                                                |
|    - Splits continuous string into distinct sentences.                                            |
|    - Resolves period (.) ambiguity: Abbreviations ("Mr.", "Dr.") vs End of sentence.              |
|    - Output: ["Mr. O'Neill spent $4.5M on AI-driven servers in New York!", "Don't wait..."]       |
+---------------------------------------------------------------------------------------------------+
                                                  |
                                                  v
| 2. TOKENIZATION (WORD BOUNDARY IDENTIFICATION)                                                    |
|    - Splits sentence into lexical tokens; handles clitics ("Don't" --> "Do" + "n't"),              |
|      hyphenated words ("AI-driven"), currency/numbers ("$4.5M").                                  |
|    - Output: ['Mr.', "O'Neill", 'spent', '$', '4.5M', 'on', 'AI-driven', 'servers', ...]          |
+---------------------------------------------------------------------------------------------------+
                                                  |
                                                  v
| 3. TEXT NORMALIZATION                                                                             |
|    - Case Folding: Lowercasing text ("New" --> "new", careful with "US" [country] vs "us" [pronoun])|
|    - Unicode Normalization: Handling NFC/NFD diacritics (e.g., "café" vs "cafe\u0301").           |
|    - Noise Removal: Stripping HTML tags (`<p>`, `&amp;`), punctuation stripping.                  |
+---------------------------------------------------------------------------------------------------+
                                                  |
                                                  v
| 4. STOPWORD REMOVAL                                                                               |
|    - Eliminates high-frequency grammatical words with negligible discriminative domain meaning    |
|      (e.g., 'the', 'is', 'at', 'which', 'on').                                                    |
|    - Caution: Suppressed in sentiment analysis ("not happy" must not drop "not").                 |
+---------------------------------------------------------------------------------------------------+
                                                  |
                                                  v
| 5. STEMMING VS LEMMATIZATION                                                                      |
|    - Stemming: Crude heuristic suffix stripping (e.g., "running" --> "run", "studies" --> "studi").|
|    - Lemmatization: Context-aware morphological reduction to true dictionary lemma using WordNet  |
|      (e.g., "better" + ADJ --> "good", "was" + VERB --> "be").                                    |
+---------------------------------------------------------------------------------------------------+
```

---

## MU Keyword Checklist: Module 1
Ensure your exam script contains these specific terms:
- [ ] *Phonetics/Phonology, Morphology, Syntax, Semantics, Pragmatics, Discourse*
- [ ] *Lexical Ambiguity (Homonymy, Polysemy), Syntactic Ambiguity (PP-attachment, Coordination)*
- [ ] *Free vs Bound Morpheme, Prefix, Suffix, Infix, Circumfix*
- [ ] *Inflectional vs Derivational Morphology (Grammatical role vs Part-of-speech transformation)*
- [ ] *Open Class (Content) vs Closed Class (Function)*
- [ ] *Two-Level Morphology, Lexical Tape, Surface Tape, E-insertion Orthographic Rule*
- [ ] *FSA for Numbers 1-99 (Decades + Hyphen + Digit)*
- [ ] *Porter Stemmer, Consonant/Vowel Measure $m$, Step 1a to Step 5b, Suffix Stripping*
- [ ] *Sentence Boundary Disambiguation, Clitic Splitting, Lemmatization vs Stemming*

---
---

# MODULE 2: LANGUAGE MODELING & PART-OF-SPEECH (POS) TAGGING

---

## 2.1 N-Gram Language Models: Mathematical Formulation
*(Appeared in: Dec 2022 Q3a [5M], May 2023 Q1b [5M], Dec 2024 Q4b [10M], May 2025 Q2a [10M])*

### Definition & Chain Rule
A Language Model computes the probability distribution over word sequences $P(W) = P(w_1, w_2, \ldots, w_n)$ or predicts the conditional probability of the next token $P(w_n | w_1, \ldots, w_{n-1})$.

By the exact **Chain Rule of Probability**:

$$P(w_1, w_2, \ldots, w_n) = \prod_{k=1}^n P(w_k \mid w_1, w_2, \ldots, w_{k-1})$$

### The Markov Assumption
Computing full historical contexts is computationally intractable due to explosive combinatorial state spaces and data sparsity. The **Markov Assumption** conditions the probability of a word solely on the preceding $N-1$ words:
- **Unigram Model ($N=1$):** Complete independence.

$$P(w_1, w_2, \ldots, w_n) \approx \prod_{k=1}^n P(w_k)$$

- **Bigram Model ($N=2$):** Conditions solely on the immediate previous token.

$$P(w_1, w_2, \ldots, w_n) \approx \prod_{k=1}^n P(w_k \mid w_{k-1})$$

- **Trigram Model ($N=3$):** Conditions on the preceding two tokens.

$$P(w_1, w_2, \ldots, w_n) \approx \prod_{k=1}^n P(w_k \mid w_{k-2}, w_{k-1})$$

### Maximum Likelihood Estimation (MLE)
Parameters are estimated by relative frequency counting in a training corpus:

$$P_{MLE}(w_i \mid w_{i-1}) = \frac{C(w_{i-1}, w_i)}{C(w_{i-1})}$$

where $C(w_{i-1}, w_i)$ is the bigram co-occurrence frequency, and $C(w_{i-1}) = \sum_w C(w_{i-1}, w)$ is the unigram frequency of the preceding word.

---

## 2.2 SOLVED NUMERICAL 1: Bigram Probability & Next-Word Prediction
*(Appeared in: May 2025 Paper, Question 2(a) [10 Marks])*

### Problem Statement:
Given the training corpus:
- Sentence 1: `<s> I am Sam </s>`
- Sentence 2: `<s> Sam I am </s>`
- Sentence 3: `<s> Sam I like </s>`
- Sentence 4: `<s> Sam I do like </s>`
- Sentence 5: `<s> do I like Sam </s>`

**Questions to Solve:**
1. What is the most probable next word predicted by the model for the following word sequences?
   - (a) `<s> Sam ...`
   - (b) `<s> Sam I do ...`
   - (c) `<s> Sam I am Sam ...`
   - (d) `<s> do I like ...`
2. Which of the following sentences is better (i.e., gets a higher probability with this model)?
   - (e) `<s> Sam I do I like </s>`
   - (f) `<s> Sam I am </s>`
   - (g) `<s> I do like Sam I am </s>`

---

### Step 1: Unigram Counts $C(w)$
Count every token across all 5 sentences (including boundary markers `<s>` and `</s>`):

| Token $w$ | Sentence Occurrences | Total Count $C(w)$ |
|:---|:---|:---:|
| `<s>` | S1 (1), S2 (1), S3 (1), S4 (1), S5 (1) | **5** |
| `I` | S1 (1), S2 (1), S3 (1), S4 (1), S5 (1) | **5** |
| `am` | S1 (1), S2 (1) | **2** |
| `Sam` | S1 (1), S2 (1), S3 (1), S4 (1), S5 (1) | **5** |
| `like` | S3 (1), S4 (1), S5 (1) | **3** |
| `do` | S4 (1), S5 (1) | **2** |
| `</s>` | S1 (1), S2 (1), S3 (1), S4 (1), S5 (1) | **5** |

---

### Step 2: Complete Bigram Counts $C(w_{i-1}, w_i)$

List every consecutive bigram occurring in the 5 sentences:
- **From Sentence 1 (`<s> I am Sam </s>`):**
  - `(<s>, I)`: 1
  - `(I, am)`: 1
  - `(am, Sam)`: 1
  - `(Sam, </s>)`: 1
- **From Sentence 2 (`<s> Sam I am </s>`):**
  - `(<s>, Sam)`: 1
  - `(Sam, I)`: 1
  - `(I, am)`: 1
  - `(am, </s>)`: 1
- **From Sentence 3 (`<s> Sam I like </s>`):**
  - `(<s>, Sam)`: 1
  - `(Sam, I)`: 1
  - `(I, like)`: 1
  - `(like, </s>)`: 1
- **From Sentence 4 (`<s> Sam I do like </s>`):**
  - `(<s>, Sam)`: 1
  - `(Sam, I)`: 1
  - `(I, do)`: 1
  - `(do, like)`: 1
  - `(like, </s>)`: 1
- **From Sentence 5 (`<s> do I like Sam </s>`):**
  - `(<s>, do)`: 1
  - `(do, I)`: 1
  - `(I, like)`: 1
  - `(like, Sam)`: 1
  - `(Sam, </s>)`: 1

#### Aggregated Bigram Frequency Matrix $C(w_{i-1}, w_i)$:

| $w_{i-1} \downarrow \backslash w_i \to$ | `<s>` | `I` | `am` | `Sam` | `like` | `do` | `</s>` | **Total $C(w_{i-1})$** |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `<s>` | 0 | 1 | 0 | 3 | 0 | 1 | 0 | **5** |
| `I` | 0 | 0 | 2 | 0 | 2 | 1 | 0 | **5** |
| `am` | 0 | 0 | 0 | 1 | 0 | 0 | 1 | **2** |
| `Sam` | 0 | 3 | 0 | 0 | 0 | 0 | 2 | **5** |
| `like` | 0 | 0 | 0 | 1 | 0 | 0 | 2 | **3** |
| `do` | 0 | 1 | 0 | 0 | 1 | 0 | 0 | **2** |

---

### Step 3: Conditional Transition Probabilities $P(w_i \mid w_{i-1}) = \frac{C(w_{i-1}, w_i)}{C(w_{i-1})}$

- **Conditioned on `<s>` ($C=5$):**
  - $P(\text{Sam} \mid \text{<s>}) = \frac{3}{5} = \mathbf{0.60}$
  - $P(\text{I} \mid \text{<s>}) = \frac{1}{5} = \mathbf{0.20}$
  - $P(\text{do} \mid \text{<s>}) = \frac{1}{5} = \mathbf{0.20}$
- **Conditioned on `Sam` ($C=5$):**
  - $P(\text{I} \mid \text{Sam}) = \frac{3}{5} = \mathbf{0.60}$
  - $P(\text{</s>} \mid \text{Sam}) = \frac{2}{5} = \mathbf{0.40}$
  - All other tokens: $0$
- **Conditioned on `I` ($C=5$):**
  - $P(\text{am} \mid \text{I}) = \frac{2}{5} = \mathbf{0.40}$
  - $P(\text{like} \mid \text{I}) = \frac{2}{5} = \mathbf{0.40}$
  - $P(\text{do} \mid \text{I}) = \frac{1}{5} = \mathbf{0.20}$
- **Conditioned on `do` ($C=2$):**
  - $P(\text{like} \mid \text{do}) = \frac{1}{2} = \mathbf{0.50}$
  - $P(\text{I} \mid \text{do}) = \frac{1}{2} = \mathbf{0.50}$
- **Conditioned on `am` ($C=2$):**
  - $P(\text{Sam} \mid \text{am}) = \frac{1}{2} = \mathbf{0.50}$
  - $P(\text{</s>} \mid \text{am}) = \frac{1}{2} = \mathbf{0.50}$
- **Conditioned on `like` ($C=3$):**
  - $P(\text{</s>} \mid \text{like}) = \frac{2}{3} \approx \mathbf{0.667}$
  - $P(\text{Sam} \mid \text{like}) = \frac{1}{3} \approx \mathbf{0.333}$

---

### Step 4: Answering Part 1 (Next-Word Predictions)

In a bigram model, the next word depends **only** on the immediately preceding word:

#### (a) Given sequence: `<s> Sam ...`
- The preceding word is `Sam`.
- Candidate probabilities:

$$P(\text{I} \mid \text{Sam}) = \frac{3}{5} = 0.60, \quad P(\text{</s>} \mid \text{Sam}) = \frac{2}{5} = 0.40$$

- **Most probable next word:** **`I`** (Probability = $0.60$).

#### (b) Given sequence: `<s> Sam I do ...`
- The preceding word is `do`.
- Candidate probabilities:

$$P(\text{like} \mid \text{do}) = \frac{1}{2} = 0.50, \quad P(\text{I} \mid \text{do}) = \frac{1}{2} = 0.50$$

- **Most probable next word:** Tie between **`like`** and **`I`** (Probability = $0.50$ each).

#### (c) Given sequence: `<s> Sam I am Sam ...`
- The preceding word is `Sam`.
- Candidate probabilities:

$$P(\text{I} \mid \text{Sam}) = \frac{3}{5} = 0.60, \quad P(\text{</s>} \mid \text{Sam}) = \frac{2}{5} = 0.40$$

- **Most probable next word:** **`I`** (Probability = $0.60$).

#### (d) Given sequence: `<s> do I like ...`
- The preceding word is `like`.
- Candidate probabilities:

$$P(\text{</s>} \mid \text{like}) = \frac{2}{3} \approx 0.667, \quad P(\text{Sam} \mid \text{like}) = \frac{1}{3} \approx 0.333$$

- **Most probable next word:** **`</s>`** (Sentence End, Probability = $0.667$). If restricted to non-boundary words, it is **`Sam`** (Probability = $0.333$).

---

### Step 5: Answering Part 2 (Sentence Comparison)

Evaluate the joint probability of each sentence using the bigram formula:

$$P(W) = \prod_{k=1}^n P(w_k \mid w_{k-1})$$

#### Evaluation of (e): `<s> Sam I do I like </s>`
$$P(W_e) = P(\text{Sam}\mid\text{<s>}) \times P(\text{I}\mid\text{Sam}) \times P(\text{do}\mid\text{I}) \times P(\text{I}\mid\text{do}) \times P(\text{like}\mid\text{I}) \times P(\text{</s>}\mid\text{like})$$

Substitute exact values:

$$P(W_e) = \left(\frac{3}{5}\right) \times \left(\frac{3}{5}\right) \times \left(\frac{1}{5}\right) \times \left(\frac{1}{2}\right) \times \left(\frac{2}{5}\right) \times \left(\frac{2}{3}\right)$$

$$P(W_e) = \frac{3 \times 3 \times 1 \times 1 \times 2 \times 2}{5 \times 5 \times 5 \times 2 \times 5 \times 3} = \frac{36}{3750} = \mathbf{0.0096}$$

#### Evaluation of (f): `<s> Sam I am </s>`
$$P(W_f) = P(\text{Sam}\mid\text{<s>}) \times P(\text{I}\mid\text{Sam}) \times P(\text{am}\mid\text{I}) \times P(\text{</s>}\mid\text{am})$$

Substitute exact values:

$$P(W_f) = \left(\frac{3}{5}\right) \times \left(\frac{3}{5}\right) \times \left(\frac{2}{5}\right) \times \left(\frac{1}{2}\right)$$

$$P(W_f) = \frac{3 \times 3 \times 2 \times 1}{5 \times 5 \times 5 \times 2} = \frac{18}{250} = \mathbf{0.0720}$$

#### Evaluation of (g): `<s> I do like Sam I am </s>`
$$P(W_g) = P(\text{I}\mid\text{<s>}) \times P(\text{do}\mid\text{I}) \times P(\text{like}\mid\text{do}) \times P(\text{Sam}\mid\text{like}) \times P(\text{I}\mid\text{Sam}) \times P(\text{am}\mid\text{I}) \times P(\text{</s>}\mid\text{am})$$

Substitute exact values:

$$P(W_g) = \left(\frac{1}{5}\right) \times \left(\frac{1}{5}\right) \times \left(\frac{1}{2}\right) \times \left(\frac{1}{3}\right) \times \left(\frac{3}{5}\right) \times \left(\frac{2}{5}\right) \times \left(\frac{1}{2}\right)$$

$$P(W_g) = \frac{1 \times 1 \times 1 \times 1 \times 3 \times 2 \times 1}{5 \times 5 \times 2 \times 3 \times 5 \times 5 \times 2} = \frac{6}{15000} = \mathbf{0.0004}$$

#### Comparison & Conclusion:
- $P(W_f) = 0.0720$
- $P(W_e) = 0.0096$
- $P(W_g) = 0.0004$

$$\mathbf{P(W_f) > P(W_e) > P(W_g)}$$

> **Final Conclusion:** Sentence **(f) `<s> Sam I am </s>`** is the best sentence as it receives the highest probability ($0.0720$).

---

## 2.3 SOLVED NUMERICAL 2: Bigram Probabilities & Next Word for "to"
*(Appeared in: Dec 2022 Paper, Question 3(a) [5 Marks])*

### Problem Statement:
Consider the following corpus:
- `<s> I tell you to sleep and rest </s>`
- `<s> I would like to sleep for an hour </s>`
- `<s> Sleep helps one to relax </s>`

*Tasks:*
1. List all possible bigrams.
2. Compute conditional probabilities.
3. Predict the next word for the word **"to"**.

---

### Step 1: Bigram Extraction
Note: Token `Sleep` in sentence 3 is lowercased to `sleep` under standard text normalization, or kept distinct if case-sensitive. In standard MU evaluation, lowercased treatment is followed.

Occurrences of bigrams starting with `to`:
- Sentence 1: `(to, sleep)` $\to 1$
- Sentence 2: `(to, sleep)` $\to 1$
- Sentence 3: `(to, relax)` $\to 1$

Total count of unigram `to`:

$$C(\text{"to"}) = 1 + 1 + 1 = 3$$

### Step 2: Conditional Probabilities for Word Following "to"
$$P(w \mid \text{"to"}) = \frac{C(\text{"to"}, w)}{C(\text{"to"})}$$

- For $w = \text{"sleep"}$:

$$P(\text{"sleep"} \mid \text{"to"}) = \frac{C(\text{"to", "sleep"})}{C(\text{"to"})} = \frac{2}{3} \approx \mathbf{0.667}$$

- For $w = \text{"relax"}$:

$$P(\text{"relax"} \mid \text{"to"}) = \frac{C(\text{"to", "relax"})}{C(\text{"to"})} = \frac{1}{3} \approx \mathbf{0.333}$$

- For all other vocabulary words:

$$P(w \mid \text{"to"}) = \frac{0}{3} = \mathbf{0}$$

### Step 3: Next Word Prediction
$$\arg\max_w P(w \mid \text{"to"}) = \text{"sleep"} \quad \left(P = \frac{2}{3}\right)$$

> **Final Answer:** The predicted next word following **"to"** is **`sleep`** with probability **$0.667$** ($66.7\%$).

---

## 2.4 Smoothing Techniques: Laplace, Good-Turing Discounting & Perplexity
*(Appeared in: Dec 2022 Q1f [5M], Dec 2023 Q1b [5M])*

### The Zero-Frequency Problem
Maximum Likelihood Estimation assigns probability $P_{MLE} = 0$ to any valid word pair unseen during training. If a single bigram has probability $0$, the joint sentence probability collapses to zero:

$$P(W) = \prod_{k=1}^n P(w_k \mid w_{k-1}) = 0$$

Smoothing re-allocates a fraction of probability mass from frequent events to unseen events.

### 1. Laplace (Add-1) Smoothing
Adds 1 to every possible n-gram count:

$$P_{\text{Laplace}}(w_i \mid w_{i-1}) = \frac{C(w_{i-1}, w_i) + 1}{C(w_{i-1}) + V}$$

where $V$ is the total vocabulary size.
- **Adjusted Count $c^*$:**

$$c^* = (C(w_{i-1}, w_i) + 1) \frac{C(w_{i-1})}{C(w_{i-1}) + V}$$

- *Limitation:* Shifts far too much probability mass to unseen events when $V$ is large (thousands of words).

### 2. Good-Turing Discounting
Re-estimates the probability of an n-gram occurring $r$ times based on the frequency of n-grams that occur $r+1$ times.
Let $N_r$ denote the number of distinct n-grams that occur exactly $r$ times in the corpus:
- $N_0$: Count of unseen n-grams.
- $N_1$: Count of singleton n-grams (seen exactly once).
- $N_2$: Count of doubleton n-grams (seen exactly twice).

#### The Discounted Count Formula:
$$r^* = (r + 1) \frac{N_{r+1}}{N_r}$$

#### Probability of Unseen Events ($r=0$):
The total probability mass reserved for all unseen events is:

$$P_0 = \frac{N_1}{N}$$

where $N = \sum_{r=1}^\infty r N_r$ is the total token count.
For each individual unseen event:

$$P(w_{\text{unseen}}) = \frac{P_0}{N_0} = \frac{N_1}{N \cdot N_0}$$

### 3. Perplexity of a Language Model
*(Appeared in: Dec 2022 Q1f [5M])*

**Perplexity ($PP$)** is the standard evaluation metric for language models. It represents the reciprocal of the geometric mean probability of the test set:

$$PP(W) = P(w_1, w_2, \ldots, w_N)^{-\frac{1}{N}} = \sqrt[N]{\frac{1}{\prod_{i=1}^N P(w_i \mid w_{i-1})}}$$

Converting to logarithmic form (cross-entropy $H(W)$):

$$H(W) = -\frac{1}{N} \sum_{i=1}^N \log_2 P(w_i \mid w_{i-1})$$

$$PP(W) = 2^{H(W)}$$

- **Interpretation:** Perplexity measures the *effective branching factor* of the language model (the weighted average number of choices the model faces at each step).
- **Golden Rule:** **Lower perplexity indicates a superior, more confident language model.**

---

## 2.5 Part-of-Speech (POS) Tagging Paradigms & Challenges
*(Appeared in: Dec 2022 Q3c [10M], Dec 2023 Q1a [5M], Dec 2023 Q4b [10M], May 2024 Q1c [5M], Dec 2024 Q1d [5M])*

POS tagging assigns a syntactic lexical category (Noun, Verb, Adjective, Preposition, etc.) to each token in a sentence.

```
+---------------------------------------------------------------------------------------------------+
|                                   POS TAGGING TAXONOMY                                            |
+---------------------------------------------------------------------------------------------------+
| 1. RULE-BASED TAGGERS                                                                             |
|    - Two-stage architecture:                                                                      |
|      Stage 1: Dictionary lookup assigns all permissible tags to each word.                        |
|      Stage 2: Handcrafted disambiguation rules (e.g., "If word ends in -ing preceded by Aux,       |
|               tag as Verb; if preceded by Determiner, tag as Noun").                              |
|    - System: ENGCG (Constraint Grammar). High precision, brittle on out-of-vocabulary terms.      |
+---------------------------------------------------------------------------------------------------+
| 2. STOCHASTIC (PROBABILISTIC) TAGGERS                                                             |
|    - Uses probability models trained on hand-annotated corpora (Penn Treebank).                   |
|    - Generative Models: Hidden Markov Models (HMM) maximizing $P(\text{Words} \mid \text{Tags})   |
|      \times P(\text{Tags})$.                                                                      |
|    - Discriminative Models: Maximum Entropy Markov Models (MEMM), Conditional Random Fields (CRF).|
+---------------------------------------------------------------------------------------------------+
| 3. TRANSFORMATION-BASED LEARNING (TBL / BRILL TAGGER)                                             |
|    - Combines rule-based interpretability with stochastic data-driven induction.                  |
|    - Begins by assigning the most frequent tag to each word, then iteratively learns              |
|      error-correcting transformation rules ranked by error reduction score.                       |
+---------------------------------------------------------------------------------------------------+
| 4. HYBRID POS TAGGERS                                                                             |
|    - Fuses statistical models (HMM/CRF) with deterministic expert morphological rule engines.      |
|    - Handcrafted rules filter improbable transitions; statistical weights rank ambiguous cases.   |
+---------------------------------------------------------------------------------------------------+
```

### Major Challenges in POS Tagging
1. **Pervasive Lexical Ambiguity:**
   - Over $11\%$ of English word types are ambiguous, but they account for over $40\%$ of word tokens in running text. (e.g., `back` can be Noun, Verb, Adjective, or Adverb).
2. **Syntactic Context Sensitivity:**
   - Words like `that` can function as a Demonstrative Pronoun (*"That is fine"*), Demonstrative Determiner (*"That dog"*), Relative Pronoun (*"The dog that barked"*), or Subordinating Conjunction (*"He said that..."*).
3. **Out-of-Vocabulary (OOV) / Unknown Words:**
   - Proper nouns, domain jargon, and typos not present in training lexicons require morphological sub-word feature inspection (e.g., capital letters, suffixes like `-able`, `-tion`, `-ly`).

---

### 🌟 SOLVED APPLIED POS TAGGING: Penn Treebank Tagset & NER Pre-processing [10 Marks] — Nov'25 (Q4b)
> **MU Official Exam Question (Paper Code 42175, Q4b):**
> *"Define POS Tagging. Explain why it is a necessary pre-processing step for higher-level NLP tasks like Named Entity Recognition (NER). Using the common Penn Treebank tagset, assign the appropriate POS tag to each word in the following sentence: 'The fast train from Dadar will arrive at platform seven shortly.' Briefly explain the reasoning for the tag assigned to the highlighted words."*

#### 1. Definition of POS Tagging:
**Part-of-Speech (POS) Tagging** (Grammatical Tagging or Word-Category Disambiguation) is the automated sequence labeling process of assigning a syntactic category marker (such as Noun, Verb, Adjective, Adverb, Pronoun, Preposition) to each word token in an input sentence, based on both its intrinsic definition and its surrounding syntactic context.

#### 2. Why POS Tagging is a Mandatory Pre-processing Step for NER:
**Named Entity Recognition (NER)** seeks to locate and classify unstructured mentions into predefined categories such as Person (`PER`), Organization (`ORG`), Location (`LOC`), or Temporal expressions (`TIME`). POS tagging is indispensable for NER because:
1. **Candidate Boundary Filtering:** Named entities are almost exclusively **Proper Nouns (`NNP`, `NNPS`)** or complex **Noun Phrases (`NP`)**. Words tagged as Prepositions (`IN`), Conjunctions (`CC`), or Modal verbs (`MD`) are instantly excluded from named entity consideration, pruning 80%+ of search space.
2. **Contextual Capitalization Disambiguation:** Capitalization alone is an unreliable indicator because sentence-initial words are capitalized regardless of whether they are entities (e.g., *"The"* or *"Fast"* at the start of a sentence). A POS tagger distinguishes between a capitalized common noun/adjective at the start of a sentence vs a genuine proper noun.
3. **Trigger Words & Relational Anchors:** Prepositions like `"from"`, `"to"`, `"in"`, `"at"` (tagged `IN`) followed by a proper noun (`NNP`) form characteristic syntactic patterns indicating **Geographic Locations** (e.g., `[IN from] [NNP Dadar]` $\implies \text{Location}$).
4. **Disambiguating Polysemous Entity Names:** Words that can be both verbs and names (e.g., *"Mark"*, *"Cook"*, *"Bill"*, *"Amazon"*, *"Apple"*) are resolved by POS context:
   - *"He paid the **bill**"* $\to$ `bill/NN` (Common noun $\implies$ Not an entity).
   - *"**Bill** signed the treaty"* $\to$ `Bill/NNP` (Proper noun $\implies \text{Person}$ entity).

#### 3. Step-by-Step Penn Treebank Tag Assignment Table:

| # | Word Token | Penn Treebank Tag | Full Description | Syntactic Reasoning & Disambiguation |
|:---:|:---|:---:|:---|:---|
| 1 | **The** | `DT` | Determiner | Definite article introducing the noun phrase `[NP The fast train]`. |
| 2 | **fast** | `JJ` | Adjective | **Highlighted:** Functions attributively to modify the head noun `"train"`. (Not an adverb `RB`, as it describes the train's property, not the verb). |
| 3 | **train** | `NN` | Noun, singular or mass | **Highlighted:** The head noun of the subject noun phrase. (Not a verb `VB`, because it is preceded by determiner `The` and adjective `fast`). |
| 4 | **from** | `IN` | Preposition | Introduces the prepositional phrase specifying origin `[PP from Dadar]`. |
| 5 | **Dadar** | `NNP` | Proper Noun, singular | **Highlighted:** Specific capitalized geographic entity (railway terminus in Mumbai). Acts as prime anchor for NER `LOCATION`. |
| 6 | **will** | `MD` | Modal | **Highlighted:** Modal auxiliary verb expressing future tense and intent; governs the main lexical verb `"arrive"`. |
| 7 | **arrive** | `VB` | Verb, base form | Main uninflected lexical action verb following modal auxiliary `"will"`. |
| 8 | **at** | `IN` | Preposition | Spatial preposition introducing the locative phrase `[PP at platform seven]`. |
| 9 | **platform** | `NN` | Noun, singular | Common noun specifying the transit terminal structure. |
| 10 | **seven** | `CD` | Cardinal Number | Number functioning as a post-nominal identifier/specifier for platform. |
| 11 | **shortly** | `RB` | Adverb | Temporal adverb modifying the verb phrase `"will arrive"`. |
| 12 | **.** | `.` | Sentence-final Punctuation | Punctuation boundary marker. |

#### Complete Tagged Sequence Output:
$$\mathbf{The/DT \quad fast/JJ \quad train/NN \quad from/IN \quad Dadar/NNP \quad will/MD \quad arrive/VB \quad at/IN \quad platform/NN \quad seven/CD \quad shortly/RB \quad ./.}$$

---

## 2.6 Hidden Markov Model (HMM) for POS Tagging: Theory & Limitations
*(Appeared in: Dec 2022 Q4a [5M], May 2024 Q3a [10M], Dec 2024 Q3a [10M], May 2025 Q1c [5M])*

### Generative Formulation
An HMM is a generative probabilistic graphical model where the true syntactic tags $T = \{t_1, t_2, \ldots, t_n\}$ are **hidden states**, and the observed words $W = \{w_1, w_2, \ldots, w_n\}$ are **emissions**.

$$\hat{T} = \arg\max_T P(T \mid W) = \arg\max_T \frac{P(W \mid T) P(T)}{P(W)} = \arg\max_T P(W \mid T) P(T)$$

Under the two fundamental HMM assumptions:
1. **Bigram Tag Independence Assumption:** The probability of a tag depends solely on the immediate predecessor:

$$P(T) \approx \prod_{i=1}^n P(t_i \mid t_{i-1})$$

2. **Output Emission Independence Assumption:** The emission of word $w_i$ depends solely on current state $t_i$:

$$P(W \mid T) \approx \prod_{i=1}^n P(w_i \mid t_i)$$

The optimal sequence decoding problem becomes:

$$\hat{T} = \arg\max_T \prod_{i=1}^n \underbrace{P(t_i \mid t_{i-1})}_{\text{Transition } a_{ij}} \cdot \underbrace{P(w_i \mid t_i)}_{\text{Emission } b_j(w_i)}$$

### Limitations of HMM
*(Appeared in: Dec 2022 Q4a [5M], May 2025 Q1c [5M], Nov 2025 Q1a [5M])*
1. **Extremely Short History (First-Order Horizon):** Considers only $t_{i-1}$, ignoring long-range agreement (e.g., subject-verb agreement across embedded clauses).
2. **Feature Poverty:** Generative modeling requires computing joint distribution $P(W, T)$, making it mathematically impossible to inject overlapping, non-independent features (e.g., capitalization, suffixes, prefixes, sentence-level context) without exploding the parameter space.
3. **Output Independence Unreality:** Assumes word $w_i$ is completely independent of neighboring words $w_{i-1}$ and $w_{i+1}$ given tag $t_i$.

### 🌟 Deep-Dive: Limitations of HMM vs MaxEnt Model for POS Tagging [5 Marks] — Nov'25 (Q1a)
**Question:** *"What are the limitations of Hidden Markov Model (HMM) and MaxEnt Model for POS Tagging."*

```
┌──────────────────────────────────────────────────────────────────────────────────┐
│                   HMM VS MAXENT LIMITATIONS AT A GLANCE                          │
│                                                                                  │
│  [HMM LIMITATIONS] (Generative Paradigm):                                        │
│  • Cannot incorporate overlapping, correlated features (capitalization, affixes) │
│  • Forces generative joint probability P(W, T) = P(W|T) * P(T)                   │
│  • Strict conditional independence: P(w_i | t_i) ignores surrounding words       │
│                                                                                  │
│  [MAXENT / MEMM LIMITATIONS] (Discriminative Paradigm):                          │
│  • Suffers from the severe LABEL BIAS PROBLEM due to local per-step normalization│
│  • State with low transition entropy traps probability mass regardless of input  │
│  • Cannot perform global sequence optimization (necessitating CRF)               │
└──────────────────────────────────────────────────────────────────────────────────┘
```

1. **Detailed Limitations of Hidden Markov Models (HMM):**
   - **Inability to Handle Overlapping Features:** An HMM is strictly generative ($P(W, T) = \prod P(t_i \mid t_{i-1}) P(w_i \mid t_i)$). To add sub-word features (like prefix, suffix, capitalization, digit presence, and preceding/succeeding words), HMM would have to compute joint distributions across all combinations, causing catastrophic parameter explosion and severe data sparsity.
   - **Local Observation Independence Assumption:** HMM assumes the emission of word $w_i$ depends *only* on the current hidden state $t_i$. In human language, words depend heavily on neighboring words (collocations, idioms).
   - **Directionality Rigidity:** Forward-only Markov conditioning cannot condition current tag $t_i$ on future tags $t_{i+1}$ without complex higher-order extensions.
2. **Detailed Limitations of Maximum Entropy (MaxEnt / MEMM) Models:**
   - **The Label Bias Problem:** MaxEnt models compute transition probabilities locally at each step:

$$P(y_t \mid y_{t-1}, x_t) = \frac{\exp(\sum \lambda_k f_k)}{\sum_{y'} \exp(\sum \lambda_k f_k)}$$

     Because each state's outgoing probabilities must sum to 1 locally, **states with few outgoing transitions have very low entropy**. Even if the observed word $x_t$ strongly disagrees with that transition, the model is mathematically forced to assign it high local probability, ignoring the true observational evidence!
   - **Failure to Find Global Optimum:** Because normalizations are performed per state transition rather than over the entire sentence string, MEMM cannot guarantee that the decoded sequence is globally optimal. (This fundamental flaw directly led to the invention of **Linear-Chain CRFs**, which use global normalization $Z(X)$).

---

## 2.7 The Viterbi Algorithm: Dynamic Programming Trellis
The Viterbi algorithm finds the optimal state sequence in $O(N^2 \cdot T)$ time using dynamic programming.

### Formal Recurrence Equations:
1. **Initialization ($t = 1$):**

$$\nu_1(j) = \pi_j \cdot b_j(w_1) = P(t_j \mid \text{<s>}) \cdot P(w_1 \mid t_j), \quad 1 \le j \le N$$

$$\mathrm{bp}_1(j) = 0$$

2. **Induction / Recursion ($2 \le t \le T$):**

$$\nu_t(j) = \max_{1 \le i \le N} \left[ \nu_{t-1}(i) \cdot a_{ij} \right] \cdot b_j(w_t), \quad 1 \le j \le N$$

$$\mathrm{bp}_t(j) = \arg\max_{1 \le i \le N} \left[ \nu_{t-1}(i) \cdot a_{ij} \right]$$

3. **Termination:**

$$P^* = \max_{1 \le i \le N} \nu_T(i)$$

$$q_T^* = \arg\max_{1 \le i \le N} \nu_T(i)$$

4. **Backtracking ($t = T-1$ down to $1$):**

$$q_t^* = \mathrm{bp}_{t+1}(q_{t+1}^*)$$

---

## 2.8 SOLVED NUMERICAL 3: HMM POS Tagging & Viterbi Decoding ("Justin will spot Will")
*(Appeared in: May 2023 Paper Q4a & May 2025 Paper Q4a [10 Marks])*

### Problem Statement:
Given Corpus:
- Sentence 1: `<S> Martin Justin can watch Will <E>`
- Sentence 2: `<S> Spot will watch Martin <E>`
- Sentence 3: `<S> Will Justin spot Martin <E>`
- Sentence 4: `<S> Martin will pat Spot <E>`

*Syntactic Classes:*
- **N (Noun):** `Martin`, `Justin`, `Will`, `Spot`, `Pat`
- **M (Modal Verb):** `can`, `will`
- **V (Verb):** `watch`, `spot`, `pat`
- Note: `<S>` = Start of sentence, `<E>` = End of sentence.

*Tasks:*
1. Compute the **Transition Probability Matrix** $A$.
2. Compute the **Emission Probability Matrix** $B$.
3. Decode the sentence **"Justin will spot Will"** using the **Viterbi Algorithm**.

---

### Step 1: Tagging the Training Sentences
Assign tags $N, M, V$ based on the given word classes:

- **S1:** `<S>` $\to$ `Martin` ($N$) $\to$ `Justin` ($N$) $\to$ `can` ($M$) $\to$ `watch` ($V$) $\to$ `Will` ($N$) $\to$ `<E>`
- **S2:** `<S>` $\to$ `Spot` ($N$) $\to$ `will` ($M$) $\to$ `watch` ($V$) $\to$ `Martin` ($N$) $\to$ `<E>`
- **S3:** `<S>` $\to$ `Will` ($N$) $\to$ `Justin` ($N$) $\to$ `spot` ($V$) $\to$ `Martin` ($N$) $\to$ `<E>`
- **S4:** `<S>` $\to$ `Martin` ($N$) $\to$ `will` ($M$) $\to$ `pat` ($V$) $\to$ `Spot` ($N$) $\to$ `<E>`

---

### Step 2: Transition Counts & Probabilities

#### Count of occurrences of each state:
- Count of `<S>` = $4$
- Count of tag $N$:
  - S1: `Martin`, `Justin`, `Will` (3)
  - S2: `Spot`, `Martin` (2)
  - S3: `Will`, `Justin`, `Martin` (3)
  - S4: `Martin`, `Spot` (2)
  - Total $C(N) = 3 + 2 + 3 + 2 = \mathbf{10}$
- Count of tag $M$:
  - S1: `can` (1)
  - S2: `will` (1)
  - S3: none (0)
  - S4: `will` (1)
  - Total $C(M) = 1 + 1 + 0 + 1 = \mathbf{3}$
- Count of tag $V$:
  - S1: `watch` (1)
  - S2: `watch` (1)
  - S3: `spot` (1)
  - S4: `pat` (1)
  - Total $C(V) = 1 + 1 + 1 + 1 = \mathbf{4}$

#### Bigram Tag Transitions Count $C(t_{i-1}, t_i)$:
- **From `<S>`:**
  - `<S> -> Martin (N)`: 1
  - `<S> -> Spot (N)`: 1
  - `<S> -> Will (N)`: 1
  - `<S> -> Martin (N)`: 1
  - Total: `<S> -> N` = 4. All other transitions from `<S>` = 0.
- **From $N$ ($C(N) = 10$):**
  - S1: `Martin -> Justin` ($N \to N$), `Justin -> can` ($N \to M$), `Will -> <E>` ($N \to <E>$)
  - S2: `Spot -> will` ($N \to M$), `Martin -> <E>` ($N \to <E>$)
  - S3: `Will -> Justin` ($N \to N$), `Justin -> spot` ($N \to V$), `Martin -> <E>` ($N \to <E>$)
  - S4: `Martin -> will` ($N \to M$), `Spot -> <E>` ($N \to <E>$)
  - Summary from $N$:
    - $N \to N$: 2 (`Martin->Justin`, `Will->Justin`)
    - $N \to M$: 3 (`Justin->can`, `Spot->will`, `Martin->will`)
    - $N \to V$: 1 (`Justin->spot`)
    - $N \to <E>$: 4 (`Will-><E>`, `Martin-><E>`, `Martin-><E>`, `Spot-><E>`)
    - Sum = $2 + 3 + 1 + 4 = 10$.
- **From $M$ ($C(M) = 3$):**
  - S1: `can -> watch` ($M \to V$)
  - S2: `will -> watch` ($M \to V$)
  - S4: `will -> pat` ($M \to V$)
  - Summary from $M$:
    - $M \to V$: 3
    - $M \to N$: 0, $M \to M$: 0, $M \to <E>$: 0
    - Sum = 3.
- **From $V$ ($C(V) = 4$):**
  - S1: `watch -> Will` ($V \to N$)
  - S2: `watch -> Martin` ($V \to N$)
  - S3: `spot -> Martin` ($V \to N$)
  - S4: `pat -> Spot` ($V \to N$)
  - Summary from $V$:
    - $V \to N$: 4
    - $V \to M$: 0, $V \to V$: 0, $V \to <E>$: 0
    - Sum = 4.

#### Transition Probability Matrix $A = P(t_j \mid t_i)$:

| From / To | $N$ | $M$ | $V$ | $<E>$ |
|:---|:---:|:---:|:---:|:---:|
| **`<S>`** | $\frac{4}{4} = \mathbf{1.0}$ | $\frac{0}{4} = \mathbf{0.0}$ | $\frac{0}{4} = \mathbf{0.0}$ | $0.0$ |
| **$N$** | $\frac{2}{10} = \mathbf{0.2}$ | $\frac{3}{10} = \mathbf{0.3}$ | $\frac{1}{10} = \mathbf{0.1}$ | $\frac{4}{10} = \mathbf{0.4}$ |
| **$M$** | $\frac{0}{3} = \mathbf{0.0}$ | $\frac{0}{3} = \mathbf{0.0}$ | $\frac{3}{3} = \mathbf{1.0}$ | $0.0$ |
| **$V$** | $\frac{4}{4} = \mathbf{1.0}$ | $\frac{0}{4} = \mathbf{0.0}$ | $\frac{0}{4} = \mathbf{0.0}$ | $0.0$ |

---

### Step 3: Emission Counts & Probabilities $B = P(w_k \mid t_j)$

#### Emission counts:
- **For tag $N$ ($C(N) = 10$):**
  - `Martin`: 4 (S1, S2, S3, S4)
  - `Justin`: 2 (S1, S3)
  - `Will`: 2 (S1, S3)
  - `Spot`: 2 (S2, S4)
  - Total = $4 + 2 + 2 + 2 = 10$.
  - All other words (`can`, `will`, `watch`, `spot`, `pat`) = 0 for tag $N$.
- **For tag $M$ ($C(M) = 3$):**
  - `will`: 2 (S2, S4)
  - `can`: 1 (S1)
  - Total = $2 + 1 = 3$.
  - All other words = 0 for tag $M$.
- **For tag $V$ ($C(V) = 4$):**
  - `watch`: 2 (S1, S2)
  - `spot`: 1 (S3)
  - `pat`: 1 (S4)
  - Total = $2 + 1 + 1 = 4$.
  - All other words = 0 for tag $V$.

#### Emission Probability Matrix $B$:

| State $t_j$ | `Justin` | `will` | `spot` | `Will` | `Martin` | `Spot` | `can` | `watch` | `pat` |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **$N$** | $\frac{2}{10} = \mathbf{0.2}$ | $0$ | $0$ | $\frac{2}{10} = \mathbf{0.2}$ | $\frac{4}{10} = 0.4$ | $\frac{2}{10} = 0.2$ | $0$ | $0$ | $0$ |
| **$M$** | $0$ | $\frac{2}{3} \approx \mathbf{0.667}$ | $0$ | $0$ | $0$ | $0$ | $\frac{1}{3} \approx 0.333$ | $0$ | $0$ |
| **$V$** | $0$ | $0$ | $\frac{1}{4} = \mathbf{0.25}$ | $0$ | $0$ | $0$ | $0$ | $\frac{2}{4} = 0.5$ | $\frac{1}{4} = 0.25$ |

*(Note: In the corpus, `Will` is tagged as $N$ and `will` as $M$. Even if treated case-insensitively, $P(\text{will} \mid M) = 2/3$, $P(\text{will} \mid N) = 2/10$. We evaluate precisely as defined).*

---

### Step 4: Viterbi Trellis Execution for "Justin will spot Will"

Sentence length $T = 4$:
- $w_1 = \text{"Justin"}$
- $w_2 = \text{"will"}$
- $w_3 = \text{"spot"}$
- $w_4 = \text{"Will"}$

#### Time Step $t = 1$ ($w_1 = \text{"Justin"}$):
$$\nu_1(j) = P(t_j \mid \text{<s>}) \times P(\text{"Justin"} \mid t_j)$$

- For $j = N$:

$$\nu_1(N) = P(N \mid \text{<s>}) \times P(\text{"Justin"} \mid N) = 1.0 \times 0.2 = \mathbf{0.20}$$

$$\mathrm{bp}_1(N) = 0$$

- For $j = M$:

$$\nu_1(M) = P(M \mid \text{<s>}) \times P(\text{"Justin"} \mid M) = 0.0 \times 0.0 = \mathbf{0.0}$$

$$\mathrm{bp}_1(M) = 0$$

- For $j = V$:

$$\nu_1(V) = P(V \mid \text{<s>}) \times P(\text{"Justin"} \mid V) = 0.0 \times 0.0 = \mathbf{0.0}$$

$$\mathrm{bp}_1(V) = 0$$

---

#### Time Step $t = 2$ ($w_2 = \text{"will"}$):
$$\nu_2(j) = \max_{i \in \{N, M, V\}} \left[ \nu_1(i) \times P(t_j \mid t_i) \right] \times P(\text{"will"} \mid t_j)$$

- **For $j = N$:**
  $P(\text{"will"} \mid N) = 0 \implies \nu_2(N) = \mathbf{0.0}$
- **For $j = M$:**

$$P(\text{"will"} \mid M) = \frac{2}{3} \approx 0.667$$

  Evaluate candidate transitions from $t=1$:
  - From $N$: $\nu_1(N) \times P(M \mid N) = 0.20 \times 0.3 = 0.060$
  - From $M$: $\nu_1(M) \times P(M \mid M) = 0.0 \times 0.0 = 0.0$
  - From $V$: $\nu_1(V) \times P(M \mid V) = 0.0 \times 0.0 = 0.0$

$$\max = 0.060 \quad (\text{from } i = N)$$

$$\nu_2(M) = 0.060 \times \frac{2}{3} = \mathbf{0.040}$$

$$\mathrm{bp}_2(M) = N$$

- **For $j = V$:**
  $P(\text{"will"} \mid V) = 0 \implies \nu_2(V) = \mathbf{0.0}$

---

#### Time Step $t = 3$ ($w_3 = \text{"spot"}$):
$$\nu_3(j) = \max_{i \in \{N, M, V\}} \left[ \nu_2(i) \times P(t_j \mid t_i) \right] \times P(\text{"spot"} \mid t_j)$$

- **For $j = N$:**
  $P(\text{"spot"} \mid N) = 0 \implies \nu_3(N) = \mathbf{0.0}$
- **For $j = M$:**
  $P(\text{"spot"} \mid M) = 0 \implies \nu_3(M) = \mathbf{0.0}$
- **For $j = V$:**

$$P(\text{"spot"} \mid V) = \frac{1}{4} = 0.25$$

  Evaluate candidate transitions from $t=2$:
  - From $N$: $\nu_2(N) \times P(V \mid N) = 0.0 \times 0.1 = 0.0$
  - From $M$: $\nu_2(M) \times P(V \mid M) = 0.040 \times 1.0 = 0.040$
  - From $V$: $\nu_2(V) \times P(V \mid V) = 0.0 \times 0.0 = 0.0$

$$\max = 0.040 \quad (\text{from } i = M)$$

$$\nu_3(V) = 0.040 \times 0.25 = \mathbf{0.010}$$

$$\mathrm{bp}_3(V) = M$$

---

#### Time Step $t = 4$ ($w_4 = \text{"Will"}$):
$$\nu_4(j) = \max_{i \in \{N, M, V\}} \left[ \nu_3(i) \times P(t_j \mid t_i) \right] \times P(\text{"Will"} \mid t_j)$$

- **For $j = N$:**

$$P(\text{"Will"} \mid N) = \frac{2}{10} = 0.20$$

  Evaluate candidate transitions from $t=3$:
  - From $N$: $\nu_3(N) \times P(N \mid N) = 0.0 \times 0.2 = 0.0$
  - From $M$: $\nu_3(M) \times P(N \mid M) = 0.0 \times 0.0 = 0.0$
  - From $V$: $\nu_3(V) \times P(N \mid V) = 0.010 \times 1.0 = 0.010$

$$\max = 0.010 \quad (\text{from } i = V)$$

$$\nu_4(N) = 0.010 \times 0.20 = \mathbf{0.0020}$$

$$\mathrm{bp}_4(N) = V$$

- **For $j = M$:**
  $P(\text{"Will"} \mid M) = 0 \implies \nu_4(M) = \mathbf{0.0}$
- **For $j = V$:**
  $P(\text{"Will"} \mid V) = 0 \implies \nu_4(V) = \mathbf{0.0}$

---

### Step 5: Termination & Backtracking
At $t = 4$:
- $\nu_4(N) = 0.0020$
- $\nu_4(M) = 0.0$
- $\nu_4(V) = 0.0$

The maximum final probability is:

$$P^* = 0.0020 \implies q_4^* = N$$

Trace backpointers:
- $q_4^* = N$
- $q_3^* = \mathrm{bp}_4(q_4^*) = \mathrm{bp}_4(N) = \mathbf{V}$
- $q_2^* = \mathrm{bp}_3(q_3^*) = \mathrm{bp}_3(V) = \mathbf{M}$
- $q_1^* = \mathrm{bp}_2(q_2^*) = \mathrm{bp}_2(M) = \mathbf{N}$

```
+---------------------------------------------------------------------------------------------------+
|                            VITERBI TRELLIS TRACE: "Justin will spot Will"                         |
+---------------------------------------------------------------------------------------------------+
|   Tag \ Word   |    Justin (t=1)    |     will (t=2)     |     spot (t=3)     |     Will (t=4)      |
+----------------+--------------------+--------------------+--------------------+-------------------+
|   N (Noun)     |    0.20 [bp=0]     |        0.0         |        0.0         |   0.0020 [bp=V]   |
|   M (Modal)    |        0.0         |   0.040 [bp=N]     |        0.0         |        0.0        |
|   V (Verb)     |        0.0         |        0.0         |   0.010 [bp=M]     |        0.0        |
+---------------------------------------------------------------------------------------------------+
|   Optimal Path |       [ N ] ------->     [ M ] -------->     [ V ] -------->     [ N ]           |
+---------------------------------------------------------------------------------------------------+
```

> **Final Output POS Tag Sequence:**
> $$\mathbf{Justin/N \quad will/M \quad spot/V \quad Will/N}$$
> **Optimal Sequence Probability:** $P^* = \mathbf{0.0020}$ ($2.0 \times 10^{-3}$).

---

## 2.9 SOLVED NUMERICAL 4: Bigram HMM & Viterbi ("The cat chases the dog")
*(Appeared in: Dec 2024 Paper, Question 3(a) [10 Marks])*

### Problem Statement:
Given corpus:
- `<s> a/DT dog/NN chases/V a/DT cat/NN </s>`
- `<s> the/DT dog/NN barks/V loudly/RB </s>`
- `<s> a/DT cat/NN runs/V fast/RB </s>`

*Tasks:*
1. Compute emission and transition probabilities for a bigram HMM.
2. Decode the sentence: **"The cat chases the dog"** using the Viterbi algorithm.
*(Assume case-insensitive match for `The` and `the`)*.

---

### Step 1: Count States and Transitions

#### State Counts $C(t_i)$:
- `<S>`: 3
- `DT`: 4 (`a`, `a`, `the`, `a`)
- `NN`: 4 (`dog`, `cat`, `dog`, `cat`)
- `V`: 3 (`chases`, `barks`, `runs`)
- `RB`: 2 (`loudly`, `fast`)
- `</s>`: 3

#### Bigram Transitions $C(t_{i-1}, t_i)$:
- **From `<S>` ($C=3$):**
  - S1: `<S> -> DT` (`a`)
  - S2: `<S> -> DT` (`the`)
  - S3: `<S> -> DT` (`a`)
  - Total: `<S> -> DT` = 3. All others = 0.
- **From `DT` ($C=4$):**
  - S1: `DT -> NN` (`dog`), `DT -> NN` (`cat`)
  - S2: `DT -> NN` (`dog`)
  - S3: `DT -> NN` (`cat`)
  - Total: `DT -> NN` = 4. All others = 0.
- **From `NN` ($C=4$):**
  - S1: `NN -> V` (`chases`), `NN -> </s>` (`cat -> </s>`)
  - S2: `NN -> V` (`barks`)
  - S3: `NN -> V` (`runs`)
  - Summary: `NN -> V` = 3, `NN -> </s>` = 1.
- **From `V` ($C=3$):**
  - S1: `V -> DT` (`chases -> a`)
  - S2: `V -> RB` (`barks -> loudly`)
  - S3: `V -> RB` (`runs -> fast`)
  - Summary: `V -> DT` = 1, `V -> RB` = 2.
- **From `RB` ($C=2$):**
  - S2: `RB -> </s>`
  - S3: `RB -> </s>`
  - Summary: `RB -> </s>` = 2.

#### Transition Probabilities $A = P(t_j \mid t_i)$:
- $P(\text{DT} \mid \text{<s>}) = \frac{3}{3} = \mathbf{1.0}$
- $P(\text{NN} \mid \text{DT}) = \frac{4}{4} = \mathbf{1.0}$
- $P(\text{V} \mid \text{NN}) = \frac{3}{4} = \mathbf{0.75}, \quad P(\text{</s>} \mid \text{NN}) = \frac{1}{4} = \mathbf{0.25}$
- $P(\text{DT} \mid \text{V}) = \frac{1}{3} \approx \mathbf{0.333}, \quad P(\text{RB} \mid \text{V}) = \frac{2}{3} \approx \mathbf{0.667}$
- $P(\text{</s>} \mid \text{RB}) = \frac{2}{2} = \mathbf{1.0}$

---

### Step 2: Emission Probabilities $B = P(w_k \mid t_j)$
- **For `DT` ($C=4$):**
  - `a`: 3 $\implies P(\text{a} \mid \text{DT}) = \frac{3}{4} = \mathbf{0.75}$
  - `the`: 1 $\implies P(\text{the} \mid \text{DT}) = \frac{1}{4} = \mathbf{0.25}$
- **For `NN` ($C=4$):**
  - `dog`: 2 $\implies P(\text{dog} \mid \text{NN}) = \frac{2}{4} = \mathbf{0.50}$
  - `cat`: 2 $\implies P(\text{cat} \mid \text{NN}) = \frac{2}{4} = \mathbf{0.50}$
- **For `V` ($C=3$):**
  - `chases`: 1 $\implies P(\text{chases} \mid \text{V}) = \frac{1}{3} \approx \mathbf{0.333}$
  - `barks`: 1 $\implies P(\text{barks} \mid \text{V}) = \frac{1}{3} \approx \mathbf{0.333}$
  - `runs`: 1 $\implies P(\text{runs} \mid \text{V}) = \frac{1}{3} \approx \mathbf{0.333}$
- **For `RB` ($C=2$):**
  - `loudly`: 1 $\implies P(\text{loudly} \mid \text{RB}) = \frac{1}{2} = \mathbf{0.50}$
  - `fast`: 1 $\implies P(\text{fast} \mid \text{RB}) = \frac{1}{2} = \mathbf{0.50}$

---

### Step 3: Viterbi Trellis Execution for "The cat chases the dog"

Sentence: $w_1 = \text{"the"}, \; w_2 = \text{"cat"}, \; w_3 = \text{"chases"}, \; w_4 = \text{"the"}, \; w_5 = \text{"dog"}$.

- **$t = 1$ ($w_1 = \text{"the"}$):**

$$\nu_1(\text{DT}) = P(\text{DT} \mid \text{<s>}) \times P(\text{"the"} \mid \text{DT}) = 1.0 \times 0.25 = \mathbf{0.25}, \quad \mathrm{bp}_1(\text{DT}) = 0$$

  All other tags have probability 0.

- **$t = 2$ ($w_2 = \text{"cat"}$):**

$$\nu_2(\text{NN}) = \nu_1(\text{DT}) \times P(\text{NN} \mid \text{DT}) \times P(\text{"cat"} \mid \text{NN}) = 0.25 \times 1.0 \times 0.50 = \mathbf{0.125}, \quad \mathrm{bp}_2(\text{NN}) = \text{DT}$$

  All other tags have probability 0.

- **$t = 3$ ($w_3 = \text{"chases"}$):**

$$\nu_3(\text{V}) = \nu_2(\text{NN}) \times P(\text{V} \mid \text{NN}) \times P(\text{"chases"} \mid \text{V}) = 0.125 \times 0.75 \times \frac{1}{3} = \mathbf{0.03125}, \quad \mathrm{bp}_3(\text{V}) = \text{NN}$$

  All other tags have probability 0.

- **$t = 4$ ($w_4 = \text{"the"}$):**

$$\nu_4(\text{DT}) = \nu_3(\text{V}) \times P(\text{DT} \mid \text{V}) \times P(\text{"the"} \mid \text{DT}) = 0.03125 \times \frac{1}{3} \times 0.25 = \frac{0.03125}{12} \approx \mathbf{0.002604}, \quad \mathrm{bp}_4(\text{DT}) = \text{V}$$

  All other tags have probability 0.

- **$t = 5$ ($w_5 = \text{"dog"}$):**

$$\nu_5(\text{NN}) = \nu_4(\text{DT}) \times P(\text{NN} \mid \text{DT}) \times P(\text{"dog"} \mid \text{NN}) = 0.002604 \times 1.0 \times 0.50 \approx \mathbf{0.001302}, \quad \mathrm{bp}_5(\text{NN}) = \text{DT}$$

  All other tags have probability 0.

#### Backtracking:
$$q_5^* = \text{NN} \to q_4^* = \text{DT} \to q_3^* = \text{V} \to q_2^* = \text{NN} \to q_1^* = \text{DT}$$

> **Final Output Sequence:**
> $$\mathbf{The/DT \quad cat/NN \quad chases/V \quad the/DT \quad dog/NN}$$
> **Probability:** $P^* = \frac{1}{768} \approx \mathbf{0.001302}$.

---

## 2.10 Maximum Entropy (MaxEnt) & Conditional Random Fields (CRF) for Sequence Labeling
*(Appeared in: May 2023 Q6b [10M], Dec 2023 Q6b [10M], May 2024 Q3b [10M], Dec 2024 Q6b [10M], May 2025 Q1c [5M])*

### 1. Maximum Entropy (MaxEnt) / Multinomial Logistic Regression
MaxEnt is a **discriminative** framework modeling the posterior conditional probability directly:

$$P(y \mid x) = \frac{1}{Z(x)} \exp\left( \sum_{i=1}^K \lambda_i f_i(x, y) \right)$$

where:
- $x$ is the context (current word, neighboring words, affixes, previous tags).
- $y$ is the candidate POS tag.
- $f_i(x, y)$ are arbitrary binary **indicator feature functions**:

$$f_1(x, y) = \begin{cases} 1 & \text{if word ends in "-tion" and } y = \text{NN} \\ 0 & \text{otherwise} \end{cases}$$

$$f_2(x, y) = \begin{cases} 1 & \text{if previous word is "the" and } y \in \{\text{NN, JJ}\} \\ 0 & \text{otherwise} \end{cases}$$

- $\lambda_i$ are learned feature weights (via L-BFGS or GIS).
- $Z(x) = \sum_{y'} \exp\left( \sum_i \lambda_i f_i(x, y') \right)$ is the per-token **local normalization factor**.

### 2. Maximum Entropy Markov Models (MEMM) & The Label Bias Problem

```
       LOCAL NORMALIZATION (MEMM):                      GLOBAL NORMALIZATION (CRF):
          Z(x_1)          Z(x_2)                                    Z(X)
            |               |                                         |
            v               v                                         v
       [ y_1 ] --------> [ y_2 ]                            [ y_1 ] ----- [ y_2 ]
          ^               ^                                    |             |
          |               |                                    +------+------+
        (x_1)           (x_2)                                         |
                                                                     (X)
   *Suffers from Label Bias:                           *Immune to Label Bias:
    States with low entropy transitions                 Scores all possible label paths
    dominate irrespective of observation.*              globally before normalizing.*
```

- **The Label Bias Problem:** In MEMMs, each state normalizes locally ($Z(x_t)$). A state with very few outgoing branches transmits almost its entire probability mass forward regardless of what input token is observed. The model prefers paths with low-entropy transitions over globally optimal paths.

### 3. Conditional Random Fields (CRF)
A linear-chain CRF solves label bias by removing local normalization. It defines a single **global clique potential** over the entire sentence sequence:

$$P(Y \mid X) = \frac{1}{Z(X)} \exp\left( \sum_{t=1}^T \sum_{k} \lambda_k f_k(y_{t-1}, y_t, X, t) \right)$$

where $Z(X)$ is the global partition function computed across **all possible full sequences** $\mathcal{Y}$:

$$Z(X) = \sum_{Y' \in \mathcal{Y}} \exp\left( \sum_{t=1}^T \sum_k \lambda_k f_k(y'_{t-1}, y'_t, X, t) \right)$$

- **Training:** Maximum conditional likelihood with $L_2$ regularization.
- **Decoding:** Global Viterbi algorithm operating over additive log-potentials:

$$\hat{Y} = \arg\max_Y \sum_{t=1}^T \sum_k \lambda_k f_k(y_{t-1}, y_t, X, t)$$

### Architectural Comparison: HMM vs MaxEnt/MEMM vs CRF

| Parameter | Hidden Markov Model (HMM) | MaxEnt / MEMM | Conditional Random Field (CRF) |
|:---|:---|:---|:---|
| **Model Type** | Generative ($P(X, Y)$). | Discriminative ($P(Y \mid X)$). | Discriminative ($P(Y \mid X)$). |
| **Objective** | Joint likelihood $\prod P(x_i \mid y_i) P(y_i \mid y_{i-1})$. | Conditional likelihood with local per-step normalization. | Conditional likelihood with global sequence normalization. |
| **Feature Richness** | Very low (strictly word token and tag bigram). | High (arbitrary overlapping contextual and sub-word features). | High (arbitrary overlapping contextual and sub-word features). |
| **Label Bias Problem**| Not applicable (generative). | **Severe (caused by local normalization).** | **Completely Eliminated (global partition $Z(X)$).** |
| **Training Complexity**| Closed-form MLE counting ($O(N)$). | Convex optimization (L-BFGS) — fast. | Convex optimization with forward-backward passes ($O(N^2 \cdot T)$). |

---

## MU Keyword Checklist: Module 2
Ensure your exam script contains these specific terms:
- [ ] *Markov Assumption, Bigram MLE Formula $C(w_{i-1}, w_i)/C(w_{i-1})$*
- [ ] *Sentence Probability Chain Rule Product*
- [ ] *Laplace Add-1 Smoothing, Vocabulary $V$, Zero-frequency problem*
- [ ] *Good-Turing Discounting, $r^* = (r+1) N_{r+1} / N_r$, Probability of unseen $P_0 = N_1 / N$*
- [ ] *Perplexity $PP(W) = P(W)^{-1/N}$, Inverse geometric mean, Effective branching factor*
- [ ] *Rule-based, Stochastic, Transformation-Based Learning (Brill), Hybrid POS Tagging*
- [ ] *HMM Bigram Independence, Emission Independence, Limitations of HMM*
- [ ] *Viterbi Trellis, $\nu_t(j)$, Backpointer $\mathrm{bp}_t(j)$, Forward pass, Backtracking*
- [ ] *MaxEnt Indicator Features $f_i(x, y)$, Feature weights $\lambda_i$*
- [ ] *MEMM Local Normalization vs Label Bias Problem*
- [ ] *Linear-Chain CRF Global Normalization, Global Partition Function $Z(X)$*
