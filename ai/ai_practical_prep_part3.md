# 🎯 AI Practical Exam Prep — Part 3: Viva Preparation

> [!CAUTION]
> **From experiment list Note 1:** "Viva can be asked on **entire syllabus** OR technical paper taken during practicals"
> **Note 2:** Prepare **Block World, Wumpus World, and FOL** — you can be given any sentence to convert to FOL

---

## 📌 Block World Problem

### What is it?
- World of blocks on a table; goal is to rearrange using a robot arm
- Only one block moved at a time; only topmost block can be moved
- Block can be placed on table or on another block

### Key States
```
Initial:        Goal:
  C                A
  B  A             B
-------           C
 Table          -------
                 Table
```

### Operators
| Operator | Precondition | Effect |
|----------|-------------|--------|
| PICK(x) | Clear(x), On(x,y), ArmEmpty | Holding(x), Clear(y), ¬On(x,y), ¬ArmEmpty |
| PLACE(x,y) | Holding(x), Clear(y) | On(x,y), ArmEmpty, ¬Holding(x), ¬Clear(y) |
| PUTDOWN(x) | Holding(x) | OnTable(x), ArmEmpty, ¬Holding(x) |
| PICKUP(x) | OnTable(x), Clear(x), ArmEmpty | Holding(x), ¬OnTable(x), ¬ArmEmpty |

### Predicates
- `On(x,y)` — x is on y
- `OnTable(x)` — x on table
- `Clear(x)` — nothing on x
- `Holding(x)` — arm holds x
- `ArmEmpty` — arm is free

### Solution Steps (for above example)
```
1. PICK(C)       → Holding(C), Clear(B)
2. PUTDOWN(C)    → OnTable(C), ArmEmpty
3. PICK(B)       → Holding(B)
4. PLACE(B,C)    → On(B,C), ArmEmpty
5. PICKUP(A)     → Holding(A)
6. PLACE(A,B)    → On(A,B) ✅ Goal achieved
```

---

## 📌 Wumpus World Problem

### Environment (4×4 Grid)
```
  1   2   3   4
4 [ ] [ ] [ ] [P]
3 [W] [G] [P] [ ]
2 [ ] [ ] [ ] [ ]
1 [A] [ ] [ ] [ ]
```
- **A** = Agent starts at (1,1) facing Right
- **W** = Wumpus at (1,3)
- **G** = Gold at (2,3)
- **P** = Pits at (4,4) and (3,3)

### Percepts (sensors)
| Percept | Meaning |
|---------|---------|
| **Stench** | Adjacent to Wumpus |
| **Breeze** | Adjacent to Pit |
| **Glitter** | Same cell as Gold |
| **Bump** | Hit a wall |
| **Scream** | Wumpus killed |

### Agent Actions
`TurnLeft, TurnRight, Forward, Grab, Shoot, Climb`

### Performance Measure
- +1000 for gold and climb out
- -1000 for death (Wumpus or Pit)
- -1 per action, -10 for arrow

### PEAS Description
| Element | Description |
|---------|-------------|
| **P**erformance | Gold +1000, Death -1000, -1/action |
| **E**nvironment | 4x4 grid, Wumpus, Pits, Gold |
| **A**ctuators | Move, Turn, Grab, Shoot, Climb |
| **S**ensors | Stench, Breeze, Glitter, Bump, Scream |

### Properties
- **Partially Observable** (only perceives adjacent cells)
- **Deterministic** (outcome of actions is predictable)
- **Sequential** (current decision affects future)
- **Static** (Wumpus doesn't move)
- **Discrete** (finite states)
- **Single Agent**

---

## 📌 First Order Logic (FOL)

### Key Symbols
| Symbol | Meaning | Example |
|--------|---------|---------|
| ∀ | For all | ∀x P(x) |
| ∃ | There exists | ∃x P(x) |
| ∧ | AND | P(x) ∧ Q(x) |
| ∨ | OR | P(x) ∨ Q(x) |
| ¬ | NOT | ¬P(x) |
| → | Implies | P(x) → Q(x) |
| ↔ | If and only if | P(x) ↔ Q(x) |

### Common FOL Conversions

**1. "All students are intelligent"**
```
∀x (Student(x) → Intelligent(x))
```

**2. "Some students like cricket"**
```
∃x (Student(x) ∧ Likes(x, Cricket))
```

**3. "No student likes homework"**
```
¬∃x (Student(x) ∧ Likes(x, Homework))
OR: ∀x (Student(x) → ¬Likes(x, Homework))
```

**4. "Every dog is an animal"**
```
∀x (Dog(x) → Animal(x))
```

**5. "There is a student who likes every subject"**
```
∃x (Student(x) ∧ ∀y (Subject(y) → Likes(x, y)))
```

**6. "Not all birds can fly"**
```
¬∀x (Bird(x) → CanFly(x))
OR: ∃x (Bird(x) ∧ ¬CanFly(x))
```

**7. "John loves Mary"**
```
Loves(John, Mary)
```

**8. "Everyone who loves someone is loved by someone"**
```
∀x (∃y Loves(x,y)) → (∃z Loves(z,x))
```

**9. "All that glitters is not gold"**
```
¬∀x (Glitters(x) → Gold(x))
OR: ∃x (Glitters(x) ∧ ¬Gold(x))
```

**10. "Marcus was a man, a Pompeian, and was born in 40AD"**
```
Man(Marcus) ∧ Pompeian(Marcus) ∧ Born(Marcus, 40AD)
```

### FOL Conversion Rules
> [!TIP]
> - "All/Every/Each" → use **∀** with **→** (implication)
> - "Some/There exists/A" → use **∃** with **∧** (conjunction)
> - "No/None" → use **¬∃** with ∧ OR **∀** with → ¬
> - "Not all" → **¬∀** OR **∃ ... ¬**

---

## 📌 Top Viva Questions & Answers

### Search Algorithms

**Q1: Difference between informed and uninformed search?**
- **Uninformed:** No domain knowledge, blind (DFS, BFS, DLS, DFID)
- **Informed:** Uses heuristic function to guide search (Greedy, A*)

**Q2: What is a heuristic function?**
- An estimate of cost from current node to goal
- Must be admissible (never overestimate) for A* optimality

**Q3: Why is A* optimal?**
- Uses f(n) = g(n) + h(n); with admissible heuristic, it expands minimum-cost nodes first and guarantees shortest path

**Q4: What is admissibility?**
- h(n) ≤ actual cost to goal for all n. Ensures A* never misses the optimal path.

**Q5: Difference between BFS and DFS?**
- BFS: Queue, level-by-level, complete, optimal, O(b^d) space
- DFS: Stack, goes deep first, not complete, not optimal, O(bd) space

### Genetic Algorithm

**Q6: What is fitness function?**
- Evaluates how good a chromosome (solution) is. Higher fitness = better solution.

**Q7: Why is crossover needed?**
- Combines traits from two parents to create potentially better offspring. Exploitation of good solutions.

**Q8: Why is mutation needed?**
- Introduces randomness to prevent premature convergence. Exploration of search space.

**Q9: What is elitism?**
- Best chromosomes pass directly to next generation without modification.

**Q10: Difference between crossover and mutation?**
- Crossover: Combines two parents (exploitation)
- Mutation: Random change in single chromosome (exploration)

### Hill Climbing

**Q11: What are problems with Hill Climbing?**
1. **Local maxima** — peak that's not global best
2. **Plateau** — flat area, no gradient to follow
3. **Ridge** — narrow peak, hard to navigate

**Q12: How to fix local maxima?**
- Random restart hill climbing, Simulated annealing, Genetic algorithms

### Prolog

**Q13: What is unification in Prolog?**
- Process of making two terms identical by finding variable substitutions. E.g., f(X,b) unifies with f(a,b) when X=a.

**Q14: What is backtracking in Prolog?**
- When a goal fails, Prolog automatically goes back to try the next alternative clause.

**Q15: Difference between facts and rules?**
- Fact: Unconditional truth — `male(john).`
- Rule: Conditional — `father(X,Y) :- parent(X,Y), male(X).`

### General AI

**Q16: Types of agents?**
1. Simple Reflex
2. Model-based Reflex
3. Goal-based
4. Utility-based
5. Learning

**Q17: What is the Turing Test?**
- If a human can't distinguish machine responses from human responses, the machine is intelligent.

**Q18: Difference between AI, ML, and DL?**
- AI ⊃ ML ⊃ DL
- AI: Machines mimicking intelligence
- ML: Learning from data
- DL: Neural networks with multiple layers

**Q19: What are production rules?**
- IF condition THEN action format. Used in expert systems.

**Q20: What is means-end analysis?**
- Problem solving by reducing difference between current and goal state using operators.

---

## 📌 Quick Reference: What to Write on Answer Sheet

### For Search Algorithms (Exp 1-6)
1. ✅ Draw the **tree/graph** diagram
2. ✅ Write **Open List** and **Close List** table
3. ✅ Show the **traversal order**
4. ✅ State if goal found and at what cost (for A*)

### For Genetic Algorithm (Exp 7)
1. ✅ Print **initial population** (6 chromosomes with fitness)
2. ✅ Show selection, crossover, mutation steps
3. ✅ Print **final population** (6 chromosomes)
4. ✅ Identify **best chromosome** and verify against equation

### For Hill Climbing (Exp 8)
1. ✅ State the function and initial point
2. ✅ Show each step with x value and f(x) value
3. ✅ Show convergence point

### For Crossover/Mutation (Exp 9, 10)
1. ✅ Print **initial 6 chromosomes** in binary
2. ✅ Show **ONE iteration** with random values
3. ✅ Print **final 6 chromosomes**
4. ✅ Show which pairs were crossed / which bits mutated

### For Prolog (Exp 11)
1. ✅ Draw the **family tree diagram**
2. ✅ Write facts and rules
3. ✅ Show sample queries and outputs

---

> [!TIP]
> **Last-minute priority order for revision:**
> 1. A* and Greedy (most commonly asked, need heuristic understanding)
> 2. Genetic Algorithm with F(x)=(a+2b+3c+4d)-30
> 3. Crossover & Mutation (one iteration each)
> 4. FOL conversions (can be asked any random sentence)
> 5. Block World & Wumpus World
> 6. DFS/BFS/DLS/DFID (these are simpler, revise the comparison table)
> 7. Hill Climbing (straightforward)
> 8. Prolog Family Tree
