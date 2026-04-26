# 📝 AI Complete Answer Guide — Part 2 (TIER 2 & 3 Topics)

---

## 10. 📌 A* SEARCH ALGORITHM [10 Marks] — 🟠 VERY HIGH (4/6)

### Answer:

**A\*** is an **informed (heuristic) search algorithm** that finds the shortest path by combining:
- **g(n)**: Actual cost from start to node n
- **h(n)**: Estimated (heuristic) cost from n to goal
- **f(n) = g(n) + h(n)**: Total estimated cost

### Properties:
- **Complete**: Yes (finds solution if one exists)
- **Optimal**: Yes, if h(n) is **admissible** (never overestimates)
- **Informed search** — uses heuristic to guide search
- Uses **priority queue** (open list) ordered by f(n)

### Algorithm:
```
1. Initialize OPEN list with start node (f = h(start))
2. Initialize CLOSED list as empty
3. While OPEN is not empty:
   a. Remove node n with smallest f(n) from OPEN
   b. If n is goal → return path (SUCCESS)
   c. Add n to CLOSED
   d. For each neighbor m of n:
      - Calculate g(m) = g(n) + cost(n,m)
      - Calculate f(m) = g(m) + h(m)
      - If m in CLOSED with lower f → skip
      - If m in OPEN with lower f → skip
      - Else add m to OPEN
4. Return FAILURE (no path exists)
```

### Worked Example:

```
Graph:
    S ──5── A ──3── G
    |       |
    2       4
    |       |
    B ──6── C
    
h(S)=7, h(A)=4, h(B)=6, h(C)=2, h(G)=0
```

| Step | OPEN (node, f=g+h) | Pick | CLOSED |
|------|-------------------|------|--------|
| 1 | {S(0+7=7)} | S | {} |
| 2 | {A(5+4=9), B(2+6=8)} | B | {S} |
| 3 | {A(5+4=9), C(2+6+2=10)} | A | {S,B} |
| 4 | {G(5+3+0=8), C(10)} | G | {S,B,A} |
| 5 | **G is goal → SUCCESS!** | | |

**Path: S → A → G, Cost = 8** ✅

### A* vs Other Algorithms:

| Feature | A* | BFS | DFS | Greedy |
|---------|-----|-----|-----|--------|
| Uses heuristic | ✅ | ❌ | ❌ | ✅ |
| Optimal | ✅ | ✅ (uniform cost) | ❌ | ❌ |
| Complete | ✅ | ✅ | ❌ | ❌ |
| f(n) | g(n)+h(n) | depth | — | h(n) only |

---

## 11. 📌 HILL CLIMBING ALGORITHM [5-10 Marks] — 🟠 VERY HIGH (4/6)

### Answer:

**Hill Climbing** is a **local search algorithm** that continuously moves in the direction of increasing value (for maximization) or decreasing value (for minimization).

### Algorithm:
```
1. Start with initial state (current)
2. Loop:
   a. Generate all neighbors of current
   b. If no neighbor has better value → return current (STUCK)
   c. Else: current = best neighbor
3. Return current as solution
```

### Diagram:
```
    Value
    ▲
    │         ╱╲ Global
    │        ╱  ╲ Maximum
    │  ╱╲   ╱    ╲
    │ ╱  ╲ ╱      ╲
    │╱  Local       ╲ 
    │   Maximum      ╲
    │                  ╲
    └────────────────────► State
```

### Problems in Hill Climbing:

#### 1. Local Maxima
- A peak higher than neighbors but NOT the global maximum
- Algorithm gets stuck, thinking it found the best
```
    ▲  ↑ Stuck here (local max)
    │  ╱╲        ╱╲ ← Global max
    │ ╱  ╲      ╱  ╲
    │╱    ╲    ╱    ╲
    └──────╲──╱──────►
```

#### 2. Plateau (Flat Region)
- Region where all neighbors have the same value
- Algorithm cannot determine direction to move
```
    ▲
    │      ┌──────────┐
    │      │ Plateau  │
    │ ╱────┘          └───╲
    │╱                     ╲
    └───────────────────────►
```

#### 3. Ridge
- A narrow elevated region; uphill in some dimensions
- Algorithm oscillates without progress
```
    ▲
    │     ╱ ╲ ╱ ╲ ╱ ╲
    │    ╱               (zigzag path)
    │   ╱
    └────────────────────►
```

### Solutions to Problems:
1. **Random Restart Hill Climbing**: Run from multiple random start points
2. **Stochastic Hill Climbing**: Choose randomly among uphill neighbors
3. **Simulated Annealing**: Allow occasional downhill moves
4. **First-Choice Hill Climbing**: Pick first better neighbor found

### Variants:
| Variant | Description |
|---------|-------------|
| **Steepest Ascent** | Pick BEST neighbor (standard) |
| **First-Choice** | Pick FIRST better neighbor |
| **Random Restart** | Restart from random state multiple times |
| **Stochastic** | Random selection among uphill neighbors |

---

## 12. 📌 NLP / LANGUAGE MODELS [10 Marks] — 🟠 VERY HIGH (4/6)

### Answer:

**Natural Language Processing (NLP)** is a branch of AI that enables computers to understand, interpret, and generate human language.

### Language Models:

A **language model** assigns probabilities to sequences of words. It predicts the likelihood of a word given previous words.

### Types of Language Models:

#### 1. N-gram Models
- Predicts next word based on previous **N-1** words
- **Unigram (N=1)**: P(w) = count(w) / total words
- **Bigram (N=2)**: P(wₙ|wₙ₋₁) = count(wₙ₋₁, wₙ) / count(wₙ₋₁)
- **Trigram (N=3)**: P(wₙ|wₙ₋₂,wₙ₋₁)

**Example (Bigram):**
Corpus: "the cat sat on the mat"
P("mat"|"the") = count("the mat") / count("the") = 1/2

#### 2. Hidden Markov Model (HMM)
- Uses hidden states and observed emissions
- Used for POS tagging, speech recognition
- Components: States, Observations, Transition probabilities, Emission probabilities

#### 3. Neural Language Models
- Use neural networks to learn word representations
- **Word2Vec**: Maps words to dense vectors
- **RNN/LSTM**: Sequential processing of text
- **Transformer**: Self-attention mechanism (GPT, BERT)

### NLP Processing Levels:

```
┌──────────────────────────┐
│ 1. Phonological Analysis │ → Sound patterns
├──────────────────────────┤
│ 2. Morphological Analysis│ → Word structure (prefix, suffix)
├──────────────────────────┤
│ 3. Lexical Analysis      │ → Word meaning
├──────────────────────────┤
│ 4. Syntactic Analysis    │ → Grammar / Parse tree
├──────────────────────────┤
│ 5. Semantic Analysis     │ → Meaning of sentences
├──────────────────────────┤
│ 6. Discourse Analysis    │ → Meaning in context
├──────────────────────────┤
│ 7. Pragmatic Analysis    │ → Intended meaning / purpose
└──────────────────────────┘
```

### Parse Tree Example: "The cat ate the fish"

```
            S
          /   \
        NP     VP
       / \    / \
     Det  N  V   NP
      |   |  |  / \
     The cat ate Det N
                 |   |
                The fish
```

---

## 13. 📌 AGENT TYPES [5 Marks] — 🟠 VERY HIGH (4/6)

### Answer:

### Types of AI Agents:

#### 1. Simple Reflex Agent
- Acts based on **current percept only**
- Uses **condition-action rules** (if-then)
- No memory of past
```
┌──────────┐    Percept     ┌──────────────┐
│Environment│──────────────►│ Condition-   │
│           │◄──────────────│ Action Rules │
└──────────┘    Action      └──────────────┘
```

#### 2. Model-Based Reflex Agent
- Maintains **internal state** (model of world)
- Can handle partially observable environments
```
┌──────────┐    Percept    ┌──────────────┐
│Environment│─────────────►│ Internal     │
│           │◄─────────────│ State +      │
└──────────┘    Action     │ Rules        │
                           └──────────────┘
```

#### 3. Goal-Based Agent
- Has **goals** to achieve
- Considers future actions and their outcomes
- Uses search and planning

#### 4. Utility-Based Agent
- Uses a **utility function** to evaluate states
- Chooses action that maximizes expected utility
- Handles trade-offs between conflicting goals
```
┌──────────┐  Percept  ┌─────────┐
│Environment│─────────►│ State   │
└─────┬─────┘         │         │
      │               │ How     │──► Utility
      │  Action       │ happy?  │    Function
      │◄──────────────│         │
      │               │ What to │
                      │ do?     │
                      └─────────┘
```

#### 5. Learning Agent
- Can **improve** its performance through experience
- Components:
```
┌────────────────────────────────────────────┐
│              LEARNING AGENT                │
│                                            │
│  ┌──────────┐        ┌──────────────┐      │
│  │ Learning │◄──────►│ Performance  │      │
│  │ Element  │        │ Element      │──►Actions
│  └────┬─────┘        └──────┬───────┘      │
│       │                     │              │
│  ┌────▼─────┐        ┌─────▼────────┐     │
│  │ Critic   │◄───────│ Problem      │     │
│  │(feedback)│        │ Generator    │     │
│  └──────────┘        └──────────────┘     │
└────────────────────────────────────────────┘
```

---

## 14. 📌 TASK ENVIRONMENT PROPERTIES [10 Marks] — 🟠 VERY HIGH (4/6)

### Answer:

| Property | Options | Description |
|----------|---------|-------------|
| **Observable** | Fully / Partially | Can agent see complete state? |
| **Deterministic** | Deterministic / Stochastic | Is next state fully determined by action? |
| **Episodic** | Episodic / Sequential | Does current action affect future? |
| **Static** | Static / Dynamic | Does environment change while agent thinks? |
| **Discrete** | Discrete / Continuous | Finite or infinite states? |
| **Agents** | Single / Multi-agent | One or more agents? |
| **Known** | Known / Unknown | Are rules of environment known? |

### Examples:

| Environment | Observable | Deterministic | Episodic | Static | Discrete | Agents |
|-------------|-----------|---------------|----------|--------|----------|--------|
| Chess | Fully | Deterministic | Sequential | Semi | Discrete | Multi |
| Taxi driving | Partially | Stochastic | Sequential | Dynamic | Continuous | Multi |
| Crossword | Fully | Deterministic | Sequential | Static | Discrete | Single |
| Poker | Partially | Stochastic | Sequential | Static | Discrete | Multi |
| Medical diagnosis | Partially | Stochastic | Sequential | Dynamic | Continuous | Single |

---

## 15. 📌 REINFORCEMENT LEARNING [5-10 Marks] — 🟠 VERY HIGH (4/6)

### Answer:

**Reinforcement Learning (RL)** is a type of machine learning where an agent learns to make decisions by **interacting with an environment** and receiving **rewards or penalties**.

### Key Components:
```
         ┌─────────────────────┐
         │    ENVIRONMENT      │
         │                     │
    ┌────┤  State Sₜ           │
    │    │  Reward Rₜ          │
    │    └─────────┬───────────┘
    │              │
    │              ▼ Action Aₜ
    │    ┌─────────────────────┐
    │    │      AGENT          │
    │    │                     │
    └───►│  Policy π           │
         │  Value Function V   │
         └─────────────────────┘
```

### Key Concepts:
- **State (S)**: Current situation of the agent
- **Action (A)**: Choice made by the agent
- **Reward (R)**: Feedback signal (+ve or -ve)
- **Policy (π)**: Strategy mapping states to actions
- **Value Function V(s)**: Expected cumulative reward from state s
- **Q-Function Q(s,a)**: Expected reward for taking action a in state s

### Types:
1. **Model-Based**: Agent has/builds a model of environment
2. **Model-Free**: Agent learns directly from experience
   - **Q-Learning**: Learns Q-values without model
   - **SARSA**: On-policy TD learning

### Q-Learning Update Rule:
```
Q(s,a) ← Q(s,a) + α[R + γ·max Q(s',a') - Q(s,a)]

α = learning rate
γ = discount factor (0 to 1)
R = immediate reward
```

### Example: Robot Navigation
- **States**: Grid positions
- **Actions**: Up, Down, Left, Right
- **Rewards**: +100 for reaching goal, -100 for obstacles, -1 per step
- Agent explores, updates Q-values, eventually learns optimal path

---

## 16. 📌 INFORMED vs UNINFORMED SEARCH [5-10 Marks] — 🟠 (4/6)

| Feature | Uninformed (Blind) | Informed (Heuristic) |
|---------|-------------------|---------------------|
| **Definition** | No additional info about states beyond problem definition | Uses heuristic function to guide search |
| **Knowledge** | Only knows goal test | Knows how "close" a state is to goal |
| **Efficiency** | Explores many unnecessary nodes | More directed, efficient |
| **Examples** | BFS, DFS, UCS, DLS, IDDFS | A*, Greedy Best-First, Hill Climbing |
| **Heuristic** | Not used | h(n) estimates cost to goal |
| **Optimality** | BFS/UCS optimal | A* optimal (with admissible h) |
| **Completeness** | BFS complete; DFS not always | A* complete |
| **Time** | Generally slower | Generally faster |

---

## 17. 📌 DEPTH LIMITED & ITERATIVE DEEPENING [10 Marks] — 🟡 MODERATE

### Depth Limited Search (DLS):
- DFS with a **maximum depth limit L**
- Avoids infinite paths of DFS
- If solution is deeper than L → fails

### Iterative Deepening DFS (IDDFS):
- Runs DLS with **increasing depth limits**: 0, 1, 2, 3, ...
- Combines benefits of BFS (completeness) and DFS (space efficiency)

```
IDDFS Algorithm:
for depth = 0 to ∞:
    result = DLS(root, depth)
    if result ≠ cutoff:
        return result
```

| Property | DLS | IDDFS |
|----------|-----|-------|
| Complete | No (if L < d) | Yes |
| Optimal | No | Yes (if step cost = 1) |
| Time | O(b^L) | O(b^d) |
| Space | O(bL) | O(bd) |

---

## 18. 📌 MINIMAX ALGORITHM [10 Marks] — 🟡 MODERATE

### Answer:

**Minimax** is a decision-making algorithm for **two-player zero-sum games**.

- **MAX player**: Tries to maximize score
- **MIN player**: Tries to minimize score

### Algorithm:
```
function MINIMAX(node, depth, isMaxPlayer):
  if terminal or depth == 0:
    return utility value

  if isMaxPlayer:
    bestVal = -∞
    for each child:
      val = MINIMAX(child, depth-1, FALSE)
      bestVal = max(bestVal, val)
    return bestVal

  else:
    bestVal = +∞
    for each child:
      val = MINIMAX(child, depth-1, TRUE)
      bestVal = min(bestVal, val)
    return bestVal
```

### Properties:
- **Complete**: Yes (finite tree)
- **Optimal**: Yes (against optimal opponent)
- **Time**: O(b^d)
- **Space**: O(bd)
- Alpha-Beta pruning optimizes Minimax to O(b^(d/2))

---

## 19. 📌 GENETIC ALGORITHMS [10 Marks] — 🟡 MODERATE

### Answer:

**Genetic Algorithm (GA)** is a search/optimization technique inspired by **natural selection and evolution**.

### Key Concepts:
- **Chromosome**: Candidate solution (string/array)
- **Gene**: Single element of chromosome
- **Population**: Set of candidate solutions
- **Fitness Function**: Evaluates quality of solution

### Steps:
```
1. Initialize random population
2. Evaluate fitness of each individual
3. REPEAT until convergence:
   a. SELECTION: Choose parents (fittest survive)
   b. CROSSOVER: Combine parents to create offspring
   c. MUTATION: Randomly alter some genes
   d. REPLACEMENT: New generation replaces old
   e. Evaluate fitness
4. Return best individual
```

### Diagram:
```
┌─────────────┐
│ Initial      │
│ Population   │
└──────┬──────┘
       ▼
┌─────────────┐
│ Fitness      │◄──────────────────┐
│ Evaluation   │                   │
└──────┬──────┘                   │
       ▼                          │
┌─────────────┐                   │
│ Selection    │                   │
│ (Roulette/   │                   │
│  Tournament) │                   │
└──────┬──────┘                   │
       ▼                          │
┌─────────────┐                   │
│ Crossover    │  (e.g., single-  │
│              │   point crossover)│
└──────┬──────┘                   │
       ▼                          │
┌─────────────┐                   │
│ Mutation     │                   │
│ (bit flip)   │                   │
└──────┬──────┘                   │
       ▼                          │
┌─────────────┐                   │
│ New          │───────────────────┘
│ Generation   │
└──────┬──────┘
       ▼
  Best Solution
```

### Crossover Example:
```
Parent 1: 1 0 1 1 | 0 0 1        (crossover point after bit 4)
Parent 2: 0 1 0 0 | 1 1 0

Child 1:  1 0 1 1 | 1 1 0
Child 2:  0 1 0 0 | 0 0 1
```

### Mutation Example:
```
Before: 1 0 1 1 0 0 1
After:  1 0 1 0 0 0 1    (bit 4 flipped)
```

---

## 20. 📌 WATER JUG PROBLEM [10 Marks] — 🔵 LOW

### Answer:

**Problem:** You have a 4-gallon jug and a 3-gallon jug. Neither has measuring marks. You need to get exactly **2 gallons** of water in the 4-gallon jug.

**State Space:** (x, y) where x = water in 4-gal jug, y = water in 3-gal jug

**Initial State:** (0, 0)
**Goal State:** (2, y) for any y

### Production Rules:

| Rule | Condition | Action | Result |
|------|-----------|--------|--------|
| 1 | x < 4 | Fill 4-gal jug | (4, y) |
| 2 | y < 3 | Fill 3-gal jug | (x, 3) |
| 3 | x > 0 | Empty 4-gal jug | (0, y) |
| 4 | y > 0 | Empty 3-gal jug | (x, 0) |
| 5 | x+y ≥ 4, y > 0 | Pour 3→4 until 4 full | (4, y-(4-x)) |
| 6 | x+y ≥ 3, x > 0 | Pour 4→3 until 3 full | (x-(3-y), 3) |
| 7 | x+y ≤ 4, y > 0 | Pour all 3→4 | (x+y, 0) |
| 8 | x+y ≤ 3, x > 0 | Pour all 4→3 | (0, x+y) |

### Solution Path:

| Step | 4-gal | 3-gal | Rule Applied |
|------|-------|-------|-------------|
| 0 | 0 | 0 | Initial |
| 1 | 0 | 3 | Fill 3-gal (Rule 2) |
| 2 | 3 | 0 | Pour 3→4 (Rule 7) |
| 3 | 3 | 3 | Fill 3-gal (Rule 2) |
| 4 | 4 | 2 | Pour 3→4 until full (Rule 5) |
| 5 | 0 | 2 | Empty 4-gal (Rule 3) |
| 6 | **2** | 0 | Pour 3→4 (Rule 7) |

**Goal (2, 0) reached!** ✅

---

## 21. 📌 PAC LEARNING [10 Marks] — 🟡 MODERATE

### Answer:

**PAC** = **Probably Approximately Correct** Learning

A framework for analyzing whether a learning algorithm can learn a concept from examples **efficiently**.

### Key Idea:
A concept class C is PAC-learnable if there exists an algorithm that:
- With probability ≥ (1 - δ): produces hypothesis h
- Where h has error ≤ ε
- In time polynomial in 1/ε, 1/δ, and size of concept

### Parameters:
- **ε (epsilon)**: Error parameter — how close to correct
- **δ (delta)**: Confidence parameter — probability of failure
- **Sample complexity**: Number of examples needed = (1/ε) × ln(1/δ)

### Significance:
- Provides **theoretical guarantee** of learning quality
- Bridges ML theory and practice
- Determines how many training examples are sufficient
