# 📝 AI Complete Answer Guide — Part 3 (Remaining Topics)

---

## 22. 📌 DEFINE AI + COMPONENTS OF AI PROGRAM [5 Marks]

### Answer:

**Artificial Intelligence** is the science and engineering of making intelligent machines that can **think, learn, reason, perceive**, and **act** like humans.

> "AI is the study of how to make computers do things at which, at the moment, people are better." — Elaine Rich

### Components of an AI Program:
1. **Knowledge Base**: Stores facts, rules, and domain knowledge
2. **Inference Engine**: Applies logical rules to derive conclusions
3. **Learning Module**: Improves performance from experience
4. **Natural Language Interface**: Communicates with humans
5. **Perception Module**: Interprets sensory input (vision, speech)
6. **Planning Module**: Generates action sequences to achieve goals
7. **Reasoning Module**: Draws conclusions from available information

---

## 23. 📌 TURING TEST / TOTAL TURING TEST [5 Marks]

### Answer:

**Turing Test** (1950, Alan Turing):
- A human **interrogator** asks questions via text to both a human and a machine
- If the interrogator **cannot distinguish** machine from human → machine passes the test
- Tests: **Natural Language Processing**, **Knowledge Representation**, **Automated Reasoning**, **Machine Learning**

**Total Turing Test** extends this by also requiring:
- **Computer Vision**: To perceive objects
- **Robotics**: To manipulate objects and move

| Turing Test | Total Turing Test |
|------------|------------------|
| Text-only interaction | Text + physical interaction |
| Tests NLP, reasoning, knowledge, learning | Also tests vision + robotics |
| No physical component | Includes physical manipulation |

---

## 24. 📌 PROPOSITIONAL LOGIC vs FIRST ORDER LOGIC [5 Marks]

| Feature | Propositional Logic (PL) | First Order Logic (FOL) |
|---------|------------------------|------------------------|
| **Basic unit** | Proposition (P, Q, R) | Predicates with arguments — Likes(John, Ice) |
| **Variables** | ❌ No | ✅ Yes |
| **Quantifiers** | ❌ No | ✅ ∀ (for all), ∃ (there exists) |
| **Expressiveness** | Limited | Highly expressive |
| **Can express** | Simple true/false facts | Relations, objects, properties |
| **Example** | P: "It is raining" | Raining(Mumbai) |
| **Connectives** | ∧, ∨, ¬, →, ↔ | Same + ∀, ∃, predicates, functions |
| **Functions** | ❌ No | ✅ Yes — father(x) |
| **Decidability** | Decidable | Semi-decidable |

---

## 25. 📌 QUANTIFIERS WITH EXAMPLES [5 Marks]

### Answer:

**Quantifiers** specify the scope of variables in FOL.

### 1. Universal Quantifier (∀) — "For All"
- ∀x P(x) means P is true for **every** x in the domain

**Examples:**
- "All dogs are animals" → ∀x [Dog(x) → Animal(x)]
- "Everyone likes ice cream" → ∀x [Person(x) → Likes(x, IceCream)]

### 2. Existential Quantifier (∃) — "There Exists"
- ∃x P(x) means there is **at least one** x for which P is true

**Examples:**
- "Some students are intelligent" → ∃x [Student(x) ∧ Intelligent(x)]
- "There exists a prime number" → ∃x [Prime(x)]

### Predicate Form Conversion Examples:

| English | Predicate Form (FOL) |
|---------|---------------------|
| All vehicles have wheels | ∀x [Vehicle(x) → HasWheels(x)] |
| Some one speaks some language | ∃x ∃y [Person(x) ∧ Language(y) ∧ Speaks(x,y)] |
| Everybody loves somebody sometimes | ∀x ∃y ∃t [Person(x) → Loves(x,y,t)] |
| All software engineers develop software | ∀x [SWEngineer(x) → DevelopsSW(x)] |
| Virat is a software engineer | SWEngineer(Virat) |

---

## 26. 📌 STATE SPACE REPRESENTATION [5 Marks]

### Answer:

**State Space** is the set of all possible states reachable from the initial state through any sequence of actions.

### Components:
1. **State**: Description of the world at a given point
2. **Initial State**: Starting configuration
3. **Operators/Actions**: Transitions between states
4. **Goal State**: Desired end configuration
5. **Path**: Sequence of states from initial to goal
6. **Path Cost**: Sum of action costs along the path

### Representation as a Graph:
```
States = Nodes
Actions = Edges
Path = Sequence of edges from start to goal
```

### Example: 8-Puzzle State Space
- State: Configuration of tiles on 3×3 grid
- Operators: Slide blank UP, DOWN, LEFT, RIGHT
- Total states: 9! = 362,880

---

## 27. 📌 8-PUZZLE PROBLEM (Detailed) [5-10 Marks]

```
Initial State:          Goal State:
┌───┬───┬───┐          ┌───┬───┬───┐
│ 2 │ 8 │ 3 │          │ 1 │ 2 │ 3 │
├───┼───┼───┤          ├───┼───┼───┤
│ 1 │ 6 │ 4 │          │ 8 │   │ 4 │
├───┼───┼───┤          ├───┼───┼───┤
│ 7 │   │ 5 │          │ 7 │ 6 │ 5 │
└───┴───┴───┘          └───┴───┴───┘
```

| Component | Description |
|-----------|-------------|
| **States** | All arrangements of tiles on 3×3 grid |
| **Initial State** | Given tile configuration |
| **Actions** | Move blank: UP, DOWN, LEFT, RIGHT |
| **Goal Test** | Tiles match goal configuration |
| **Path Cost** | 1 per move |
| **State Space Size** | 9!/2 = 181,440 reachable states |

### Heuristics for A*:
- **h₁**: Number of misplaced tiles
- **h₂**: Sum of Manhattan distances of each tile from goal position
- h₂ is more informed and gives better performance

---

## 28. 📌 MONKEY-BANANA PROBLEM (Detailed) [10 Marks]

### Problem:
A monkey is in a room. Bananas hang from the ceiling. A box is in the corner. The monkey must get the bananas.

### STRIPS Formulation:

**Initial State:**
```
At(Monkey, A), At(Box, B), At(Bananas, C),
Height(Monkey, Low), Height(Bananas, High),
NOT OnBox(Monkey), NOT Has(Monkey, Bananas)
```

**Goal State:** `Has(Monkey, Bananas)`

**Actions:**

| Action | Precondition | Add | Delete |
|--------|-------------|-----|--------|
| Walk(x, y) | At(Monkey, x) | At(Monkey, y) | At(Monkey, x) |
| Push(x, y) | At(Monkey, x), At(Box, x) | At(Monkey, y), At(Box, y) | At(Monkey, x), At(Box, x) |
| ClimbUp | At(Monkey, x), At(Box, x), Height(Monkey, Low) | OnBox(Monkey), Height(Monkey, High) | Height(Monkey, Low) |
| Grasp | At(Monkey, x), At(Bananas, x), Height(Monkey, High), OnBox(Monkey) | Has(Monkey, Bananas) | — |

**Plan:**
1. Walk(A, B) — Monkey walks to box
2. Push(B, C) — Monkey pushes box under bananas
3. ClimbUp — Monkey climbs on box
4. Grasp — Monkey grabs bananas ✅

---

## 29. 📌 FLAT TIRE PROBLEM (ADL) [10 Marks]

### Problem:
Car has a flat tire on axle. Good spare tire is in the trunk. Goal: mount good tire.

### ADL (Action Description Language) Description:

**Initial State:**
```
On(FlatTire, Axle), In(SpareTire, Trunk),
NOT On(SpareTire, Axle), NOT In(FlatTire, Trunk)
```

**Goal:** `On(SpareTire, Axle)`

**Actions:**

| Action | Precondition | Effect |
|--------|-------------|--------|
| Remove(FlatTire, Axle) | On(FlatTire, Axle) | ¬On(FlatTire, Axle), At(FlatTire, Ground) |
| Remove(SpareTire, Trunk) | In(SpareTire, Trunk) | ¬In(SpareTire, Trunk), At(SpareTire, Ground) |
| PutOn(SpareTire, Axle) | At(SpareTire, Ground), ¬On(FlatTire, Axle) | On(SpareTire, Axle), ¬At(SpareTire, Ground) |

**Plan:**
1. Remove(FlatTire, Axle)
2. Remove(SpareTire, Trunk)
3. PutOn(SpareTire, Axle) ✅

---

## 30. 📌 GREEDY BEST-FIRST SEARCH [10 Marks]

### Answer:

Uses **f(n) = h(n)** only — expands the node that appears **closest to the goal** based on heuristic.

### Properties:
- **Not optimal** — can find suboptimal paths
- **Not complete** — can get stuck in loops
- **Fast** — explores fewer nodes than BFS
- Time & Space: O(b^m)

### Comparison with A*:

| Feature | Greedy Best-First | A* |
|---------|------------------|-----|
| f(n) | h(n) only | g(n) + h(n) |
| Considers path cost? | ❌ No | ✅ Yes |
| Optimal? | ❌ | ✅ (admissible h) |
| Complete? | ❌ | ✅ |
| Speed | Faster | Slower but better paths |

### Example:
With h(S)=10, h(A)=10, h(B)=6, h(C)=4, h(D)=8, h(E)=6.5, h(F)=3, h(G)=0:

Greedy expands: S → picks lowest h among neighbors → keeps choosing lowest h(n) → reaches G
(Path may not be shortest cost, but reaches goal quickly)

---

## 31. 📌 KNOWLEDGE REPRESENTATION METHODS [10 Marks]

### Answer:

Methods to encode knowledge for AI reasoning:

### 1. Logical Representation
- **Propositional Logic**: Simple facts (P, Q, P ∧ Q)
- **First Order Logic**: Predicates + quantifiers
- Precise, formal, supports inference
- Can be complex for large domains

### 2. Semantic Networks
- **Graph-based**: Nodes = concepts, Edges = relationships
- Uses IS-A (inheritance), HAS-A (composition) links
```
      Animal
        |  IS-A
       Dog ──HAS-A──► Tail
        |  IS-A
      Labrador
```

### 3. Frames
- Data structures with **slots** (attributes) and **fillers** (values)
- Supports inheritance and default values
```
Frame: Car
  Slot: Wheels → 4
  Slot: Engine → Internal Combustion
  Slot: Color → Default: White
```

### 4. Production Rules (Rule-Based)
- **IF condition THEN action** rules
- Used in expert systems
- Example: IF fever AND cough THEN flu

### 5. Ontologies
- Formal representation of concepts and relationships in a domain
- Shared vocabulary for knowledge exchange

---

## 32. 📌 BELIEF NETWORK / BAYESIAN NETWORK [10 Marks]

### Answer:

A **Bayesian Network** (Belief Network) is a **Directed Acyclic Graph (DAG)** representing **probabilistic relationships** among variables.

### Components:
1. **Nodes**: Random variables
2. **Edges**: Direct probabilistic dependencies
3. **CPT (Conditional Probability Table)**: P(node | parents) for each node

### Properties:
- Each node is conditionally independent of non-descendants given its parents
- Compact representation of joint probability distribution

### Example: Medical Diagnosis

```
  Smoking     Pollution
     \         /
      ▼       ▼
      Cancer
        |
        ▼
     X-Ray
```

**CPTs:**

P(Smoking): P(S=T)=0.3

P(Cancer | Smoking, Pollution):
| S | P | P(C=T) |
|---|---|--------|
| T | H | 0.05 |
| T | L | 0.02 |
| F | H | 0.03 |
| F | L | 0.001 |

P(X-Ray | Cancer):
| C | P(X=positive) |
|---|---------------|
| T | 0.9 |
| F | 0.2 |

### Steps to Construct:
1. Identify random variables
2. Determine causal relationships → draw edges
3. Ensure DAG (no cycles)
4. Specify CPT for each node
5. Use for inference (compute P of query given evidence)

---

## 33. 📌 SIMULATED ANNEALING [10 Marks]

### Answer:

**Simulated Annealing** is a probabilistic local search inspired by the **annealing process in metallurgy** (heating and slow cooling of material).

### Key Idea:
- Like Hill Climbing, but **allows "bad" (downhill) moves** with a probability that **decreases over time**
- **Temperature (T)** parameter controls randomness — starts high, decreases gradually

### Algorithm:
```
1. current = initial state
2. T = initial_temperature
3. While T > 0:
   a. next = random neighbor of current
   b. ΔE = value(next) - value(current)
   c. If ΔE > 0:           (better state)
        current = next
   d. Else:                 (worse state)
        Accept with probability e^(ΔE/T)
   e. T = T × cooling_rate  (e.g., T = 0.95 × T)
4. Return current
```

### Why it works:
- High T → accepts bad moves freely → **explores** widely
- Low T → rarely accepts bad moves → **exploits** good regions
- Avoids getting stuck at **local maxima**

### Comparison with Hill Climbing:

| Feature | Hill Climbing | Simulated Annealing |
|---------|-------------|-------------------|
| Bad moves | Never accepted | Accepted with probability |
| Local maxima | Gets stuck | Can escape |
| Temperature | No concept | Controls randomness |
| Completeness | Not complete | Approaches optimal with slow cooling |
| Deterministic | Yes | Stochastic |

---

## 34. 📌 CONDITIONAL PLANNING [5 Marks]

### Answer:

**Conditional Planning** handles **uncertainty** in the environment by including **conditional branches** (if-then-else) in the plan.

- Used when outcomes of actions are **not fully predictable**
- Plan contains **observation actions** to determine the current state
- Based on observation, different action sequences are followed

### Structure:
```
Plan:
  1. Check condition C
  2. IF C is true → Execute Plan-A
  3. ELSE → Execute Plan-B
```

### Example:
Vacuum cleaner robot — if room is dirty, clean it; if already clean, move to next room.

### Difference from Classical Planning:
| Classical | Conditional |
|-----------|------------|
| Deterministic outcomes | Uncertain outcomes |
| Linear action sequence | Branching plan (tree) |
| Fully observable | Partially observable |

---

## 35. 📌 GAME TREE — TIC-TAC-TOE [10 Marks]

### Answer:

**Game Playing** in AI uses **game trees** where:
- **MAX** player (X) tries to maximize score
- **MIN** player (O) tries to minimize score

### Tic-Tac-Toe Game Tree (Partial):
```
                    (Empty Board)
                     MAX (X)
            /          |          \
    X|_|_       _|X|_        _|_|_
    _|_|_       _|_|_        _|_|X
    _|_|_       _|_|_        _|_|_
   MIN(O)      MIN(O)       MIN(O)
   / | \       / | \         / | \
 ...  ... ... ...  ...     ...  ...
```

### Properties of Tic-Tac-Toe:
- **State space**: 9! ≈ 362,880 (upper bound)
- **Actual game states**: ~5,478 (considering symmetry)
- **Branching factor**: Starts at 9, decreases by 1 each turn
- **Depth**: Maximum 9 moves
- **Utility values**: +1 (X wins), -1 (O wins), 0 (draw)
- With **Minimax + Alpha-Beta Pruning**, optimal play always results in a **draw**

---

## 36. 📌 CNF CONVERSION (Propositional Logic) [10 Marks]

### Detailed Steps with Example:

**Convert:** (P → Q) ∧ (Q → R) → (P → R)

**To prove using resolution**, negate the statement and show contradiction:

**Negate:** ¬[(P → Q) ∧ (Q → R) → (P → R)]

**Step 1: Eliminate implications (→)**
- A → B becomes ¬A ∨ B
- ¬[¬(¬P ∨ Q) ∧ (¬Q ∨ R)) ∨ (¬P ∨ R)]
- = (¬P ∨ Q) ∧ (¬Q ∨ R) ∧ ¬(¬P ∨ R)

**Step 2: Move ¬ inward (De Morgan's)**
- ¬(¬P ∨ R) = P ∧ ¬R

**Step 3: Result in CNF:**
```
C1: ¬P ∨ Q
C2: ¬Q ∨ R
C3: P
C4: ¬R
```

**Step 4: Resolution:**
```
C1: ¬P ∨ Q    +    C3: P
        → C5: Q

C2: ¬Q ∨ R    +    C5: Q
        → C6: R

C4: ¬R        +    C6: R
        → □ (empty clause — CONTRADICTION!)
```

**∴ The original statement is a tautology — PROVED** ✅
