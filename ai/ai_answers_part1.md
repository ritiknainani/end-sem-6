# 📝 AI Complete Answer Guide — Part 1 (TIER 1: GUARANTEED Topics)

---

## 1. 📌 ALPHA-BETA PRUNING [10 Marks] — 🔴 GUARANTEED (6/6)

### Answer:

**Alpha-Beta Pruning** is an optimization technique for the **Minimax algorithm** that reduces the number of nodes evaluated in the game tree by pruning branches that cannot affect the final decision.

### Key Concepts:
- **α (Alpha)**: Best value that the **MAX** player can guarantee (initially -∞)
- **β (Beta)**: Best value that the **MIN** player can guarantee (initially +∞)
- **Pruning condition**: If α ≥ β at any node, prune remaining children

### Algorithm:

```
function ALPHA-BETA(node, depth, α, β, maximizingPlayer):
  if depth == 0 or node is terminal:
    return heuristic value of node

  if maximizingPlayer:
    value = -∞
    for each child of node:
      value = max(value, ALPHA-BETA(child, depth-1, α, β, FALSE))
      α = max(α, value)
      if α ≥ β:
        break    ← β cutoff (prune remaining)
    return value

  else: (minimizingPlayer)
    value = +∞
    for each child of node:
      value = min(value, ALPHA-BETA(child, depth-1, α, β, TRUE))
      β = min(β, value)
      if α ≥ β:
        break    ← α cutoff (prune remaining)
    return value
```

### Worked Example:

```
                        MAX
                    ┌────A────┐
                   MIN       MIN
                ┌──B──┐   ┌──C──┐
               MAX   MAX MAX   MAX
              ┌D─┐  ┌E─┐ ┌F─┐ ┌G─┐
              3   5  6  9  1  2  0  -1
```

**Step-by-step traversal:**

1. Start at A (MAX), α=-∞, β=+∞
2. Go to B (MIN), α=-∞, β=+∞
3. Go to D (MAX), α=-∞, β=+∞
   - D's children: 3, 5 → MAX picks **5** → D=5
4. Back at B (MIN): β = min(+∞, 5) = **5**
5. Go to E (MAX), α=-∞, β=5
   - E's left child: 6 → α = max(-∞, 6) = 6
   - **α(6) ≥ β(5) → PRUNE** right child (9) ← β cutoff!
   - E returns 6 (but B won't use it since 6 > β)
6. B (MIN) = min(5, 6) = **5** → B=5
7. Back at A (MAX): α = max(-∞, 5) = **5**
8. Go to C (MIN), α=5, β=+∞
9. Go to F (MAX), α=5, β=+∞
   - F's children: 1, 2 → MAX picks **2** → F=2
10. Back at C (MIN): β = min(+∞, 2) = **2**
    - **α(5) ≥ β(2) → PRUNE** node G entirely ← α cutoff!
11. C returns **2**
12. A (MAX) = max(5, 2) = **5**

**Final value of root = 5**

### Properties:
- **Time Complexity**: O(b^(d/2)) in best case vs O(b^d) for minimax
- **Effectively doubles the searchable depth**
- Does NOT affect the final result — same as minimax
- Move ordering improves pruning efficiency

---

## 2. 📌 FOL + CNF + RESOLUTION PROOFS [10 Marks] — 🔴 GUARANTEED (6/6)

### Key Concepts:

**First Order Logic (FOL):** Uses predicates, quantifiers (∀, ∃), variables, and constants.

**Steps for Resolution Proof:**
1. Convert English statements to FOL
2. Convert each FOL statement to CNF (Conjunctive Normal Form)
3. Negate the conclusion
4. Apply Resolution until empty clause (□) is derived

### CNF Conversion Steps:
1. Eliminate implications: A → B becomes ¬A ∨ B
2. Move negations inward (De Morgan's)
3. Standardize variables
4. Skolemize (remove ∃ by introducing constants)
5. Drop universal quantifiers
6. Distribute ∨ over ∧

### Worked Example 1: "Is someone smiling?"
**Given:**
- All people who are earning are happy
- All happy people smile
- Someone is earning

**Step 1: Convert to FOL:**
1. ∀x [Earning(x) → Happy(x)]
2. ∀x [Happy(x) → Smile(x)]
3. ∃x [Earning(x)]

**Step 2: Convert to CNF:**
1. ¬Earning(x) ∨ Happy(x)
2. ¬Happy(x) ∨ Smile(x)
3. Earning(A) — Skolem constant A

**Step 3: Negate conclusion:**
- To prove: ∃x [Smile(x)]
- Negation: ∀x [¬Smile(x)] → ¬Smile(x)

**Step 4: Resolution:**
```
Clauses:
C1: ¬Earning(x) ∨ Happy(x)
C2: ¬Happy(x) ∨ Smile(x)
C3: Earning(A)
C4: ¬Smile(x)        ← negated conclusion

Resolution Tree:
   C2: ¬Happy(x) ∨ Smile(x)     C4: ¬Smile(x)
              \                    /
               ¬Happy(x)  ← C5 (resolve on Smile)
                    |
   C1: ¬Earning(x) ∨ Happy(x)     C5: ¬Happy(x)
              \                    /
               ¬Earning(x) ← C6 (resolve on Happy)
                    |
   C3: Earning(A)          C6: ¬Earning(x), x=A
              \            /
               □ (empty clause) ← CONTRADICTION!
```
∴ **Someone is smiling — PROVED** ✅

### Worked Example 2: Colonel West is a Criminal
**Given:**
- It is a crime for an American to sell weapons to hostile nations
- Nono is an enemy of America (hostile)
- Nono has some missiles
- All missiles were sold to Nono by Colonel West
- Colonel West is American

**FOL:**
1. ∀x,y,z [American(x) ∧ Weapon(y) ∧ Sells(x,y,z) ∧ Hostile(z) → Criminal(x)]
2. Enemy(Nono, America) → Hostile(Nono)
3. ∃x [Owns(Nono, x) ∧ Missile(x)] → Owns(Nono, M1) ∧ Missile(M1)
4. ∀x [Missile(x) ∧ Owns(Nono,x) → Sells(West, x, Nono)]
5. American(West)
6. ∀x [Missile(x) → Weapon(x)]
7. Hostile(Nono) (from 2)

**CNF Clauses:**
1. ¬American(x) ∨ ¬Weapon(y) ∨ ¬Sells(x,y,z) ∨ ¬Hostile(z) ∨ Criminal(x)
2. Hostile(Nono)
3. Owns(Nono, M1)
4. Missile(M1)
5. ¬Missile(x) ∨ ¬Owns(Nono,x) ∨ Sells(West, x, Nono)
6. American(West)
7. ¬Missile(x) ∨ Weapon(x)

**Negate goal:** ¬Criminal(West)

**Resolution chain:**
- From 4+7: Weapon(M1)
- From 4+3+5: Sells(West, M1, Nono)
- From 6+Weapon(M1)+Sells(West,M1,Nono)+2+1: Criminal(West)
- Criminal(West) + ¬Criminal(West) = □

∴ **Colonel West is a criminal — PROVED** ✅

---

## 3. 📌 PLANNING IN AI [10-20 Marks] — 🔴 GUARANTEED (6/6)

### 3.1 What is Planning?

**Planning** is the process of computing sequences of actions to achieve a goal. It involves:
- **Initial State**: Starting configuration
- **Goal State**: Desired configuration
- **Actions**: Operations that change state
- **Plan**: Sequence of actions from initial to goal state

### 3.2 STRIPS Representation

**STRIPS** (Stanford Research Institute Problem Solver) represents actions as:
- **Preconditions**: Conditions that must be true before action
- **Add List (Effects+)**: Facts that become true after action
- **Delete List (Effects-)**: Facts that become false after action

### STRIPS Example: Air Cargo Transport

**Initial State:** At(C1,SFO), At(C2,JFK), At(P1,SFO), At(P2,JFK)
**Goal:** At(C1,JFK), At(C2,SFO)

**Actions:**

| Action | Precondition | Add List | Delete List |
|--------|-------------|----------|-------------|
| Load(c,p,a) | At(c,a) ∧ At(p,a) | In(c,p) | At(c,a) |
| Unload(c,p,a) | In(c,p) ∧ At(p,a) | At(c,a) | In(c,p) |
| Fly(p,from,to) | At(p,from) | At(p,to) | At(p,from) |

**Plan:**
1. Load(C1, P1, SFO)
2. Fly(P1, SFO, JFK)
3. Unload(C1, P1, JFK) → Goal: At(C1,JFK) ✅
4. Load(C2, P2, JFK)
5. Fly(P2, JFK, SFO)
6. Unload(C2, P2, SFO) → Goal: At(C2,SFO) ✅

### 3.3 Partial Order Planning (POP)

Unlike total-order planning (fixed sequence), POP:
- Only orders actions when there's a **causal dependency**
- Allows **parallel execution** of independent actions
- Uses **causal links** to protect preconditions

**Components of POP:**
1. **Actions**: Set of partially ordered actions
2. **Ordering Constraints**: A < B means A must come before B
3. **Causal Links**: A →(p)→ B means A achieves precondition p for B
4. **Open Preconditions**: Not yet achieved by any action

**POP Algorithm:**
```
1. Start with initial plan: Start action and Finish action
2. While open preconditions exist:
   a. Pick an open precondition p of action B
   b. Find action A that achieves p
   c. Add causal link A →(p)→ B
   d. Add ordering constraint A < B
   e. Resolve threats: If action C might delete p,
      add C < A (demotion) or B < C (promotion)
3. Return plan
```

### 3.4 Hierarchical Planning

- Decomposes complex tasks into **subtasks**
- Uses **Hierarchical Task Networks (HTN)**
- High-level actions are refined into lower-level primitive actions

```
        Travel(Home, Office)
              |
    ┌─────────┼─────────┐
    ▼         ▼         ▼
 Walk to    Drive      Walk to
  Car      Car→Office   Office
```

---

## 4. 📌 PEAS DESCRIPTORS [5-10 Marks] — 🔴 GUARANTEED (6/6)

### Answer:

**PEAS** stands for: **P**erformance measure, **E**nvironment, **A**ctuators, **S**ensors

Used to specify the **task environment** of an intelligent agent.

| Component | What it defines |
|-----------|----------------|
| **Performance** | How success is measured |
| **Environment** | The external world the agent operates in |
| **Actuators** | How the agent acts on the environment |
| **Sensors** | How the agent perceives the environment |

### PEAS Examples (Memorize 4-5):

| Agent | Performance | Environment | Actuators | Sensors |
|-------|------------|-------------|-----------|---------|
| **Vacuum Cleaner** | Cleanliness, efficiency, battery | Room, floor, dirt | Wheels, vacuum, brushes | Dirt sensor, bump sensor, camera |
| **Self-driving Taxi** | Safe, fast, legal, comfortable, profit | Roads, traffic, pedestrians, weather | Steering, accelerator, brake, signals | Camera, LIDAR, GPS, speedometer |
| **Medical Diagnosis** | Correct diagnosis, minimize cost | Patient, hospital, staff | Display, prescription output | Keyboard input, test results, symptoms |
| **Part-picking Robot** | % parts correctly picked, speed | Conveyor belt, parts bin | Jointed arm, gripper | Camera, joint angle sensors |
| **Online Tutor** | Student score improvement, engagement | Student, website, exercises | Display text/exercises, hints | Keyboard input, student responses |
| **Automobile Driver** | Safety, time, comfort, legality | Roads, vehicles, pedestrians | Steering, brake, accelerator | Camera, radar, GPS, accelerometer |

---

## 5. 📌 FORWARD & BACKWARD CHAINING [10 Marks] — 🔴 GUARANTEED (5/6)

### Answer:

Both are **inference methods** used in rule-based/knowledge-based systems.

### Forward Chaining (Data-Driven)

- Starts from **known facts**
- Applies rules whose conditions are satisfied
- Derives new facts until **goal is reached**
- "Bottom-up" reasoning

```
Algorithm:
1. Start with known facts in working memory
2. Check all rules — find those whose LHS (conditions) match facts
3. Fire the matched rule → add conclusion to working memory
4. Repeat until goal is found or no more rules fire
```

### Backward Chaining (Goal-Driven)

- Starts from **goal**
- Works backward to find supporting facts
- Checks if preconditions are known or can be proved
- "Top-down" reasoning

```
Algorithm:
1. Start with the goal to prove
2. Find rules whose RHS (conclusion) matches goal
3. Check if LHS conditions are known facts
4. If not known, set each condition as a new sub-goal
5. Recurse until all sub-goals are satisfied by known facts
```

### Worked Example:

**Rules:**
```
R1: If A and B → C
R2: If C and D → E
R3: If E → F
R4: If A → D
```
**Known Facts:** A, B
**Goal:** Prove F

**Forward Chaining:**
```
Step 1: Facts = {A, B}
  R1 fires (A ∧ B) → add C    Facts = {A, B, C}
  R4 fires (A) → add D        Facts = {A, B, C, D}
Step 2:
  R2 fires (C ∧ D) → add E    Facts = {A, B, C, D, E}
Step 3:
  R3 fires (E) → add F        Facts = {A, B, C, D, E, F}
  Goal F reached! ✅
```

**Backward Chaining:**
```
Goal: F
  R3: E → F, so prove E
    R2: C ∧ D → E, so prove C and D
      Prove C:
        R1: A ∧ B → C, A=known ✅, B=known ✅ → C proved ✅
      Prove D:
        R4: A → D, A=known ✅ → D proved ✅
    C ✅ ∧ D ✅ → E proved ✅
  E ✅ → F proved ✅
```

### Comparison:

| Feature | Forward Chaining | Backward Chaining |
|---------|-----------------|-------------------|
| Direction | Facts → Goal | Goal → Facts |
| Strategy | Data-driven | Goal-driven |
| Starts from | Known facts | Goal/hypothesis |
| Use case | Monitoring, diagnosis | Query answering, proving |
| Efficiency | May derive irrelevant facts | Focused on goal |
| Also called | Bottom-up | Top-down |

---

## 6. 📌 WUMPUS WORLD [10 Marks] — 🔴 GUARANTEED (5/6)

### Answer:

**Wumpus World** is a classic AI environment used to illustrate knowledge-based agents and logical reasoning.

### Description:
A cave consisting of a **4×4 grid of rooms** connected by passageways.

```
┌─────┬─────┬─────┬─────┐
│     │     │     │  P  │  4
├─────┼─────┼─────┼─────┤
│     │     │     │     │  3
├─────┼─────┼─────┼─────┤
│     │  W  │  P  │     │  2
├─────┼─────┼─────┼─────┤
│START│     │     │  P  │  1
│  A  │     │     │     │
└─────┴─────┴─────┴─────┘
  1      2      3      4
W = Wumpus, P = Pit, A = Agent (Start)
Gold is in some room
```

### PEAS Description:

| Component | Description |
|-----------|-------------|
| **Performance** | +1000 for gold, -1000 for death (pit/wumpus), -1 per step, -10 for arrow |
| **Environment** | 4×4 grid, 1 Wumpus, multiple pits, 1 gold |
| **Actuators** | Move forward, Turn left/right, Grab, Shoot, Climb (exit) |
| **Sensors** | Stench, Breeze, Glitter, Bump, Scream |

### Percepts:

| Percept | Indicates |
|---------|-----------|
| **Stench** | Wumpus is in adjacent room (not diagonal) |
| **Breeze** | Pit is in adjacent room |
| **Glitter** | Gold is in current room |
| **Bump** | Walked into a wall |
| **Scream** | Wumpus has been killed (by arrow) |

### Environment Properties:
- **Partially Observable** — agent sees only current room percepts
- **Deterministic** — outcomes are fixed
- **Sequential** — current action affects future states
- **Static** — Wumpus and pits don't move
- **Discrete** — finite states
- **Single Agent** — only one explorer

### Agent's Strategy (using logic):
1. Start at (1,1), facing right
2. If Glitter → Grab gold → Climb out
3. If Breeze in (1,1) → no safe move possible
4. Use logical inference to mark rooms as Safe/Unsafe/Unknown
5. Use Stench/Breeze to infer Wumpus/Pit locations
6. Only move to rooms proved safe

---

## 7. 📌 CATEGORIES/TYPES OF AI [5 Marks] — 🔴 GUARANTEED (5/6)

### Answer:

AI can be categorized in **two ways**:

### A. Based on Capability:

```
┌─────────────────────────────────────────────────┐
│  1. Narrow AI (Weak AI)                         │
│     - Designed for ONE specific task             │
│     - Examples: Siri, Chess AI, Spam filter      │
│     - Current AI systems are all Narrow AI       │
├─────────────────────────────────────────────────┤
│  2. General AI (Strong AI)                      │
│     - Can perform ANY intellectual task          │
│     - Human-level intelligence                   │
│     - Does NOT exist yet (theoretical)           │
├─────────────────────────────────────────────────┤
│  3. Super AI (Superintelligence)                │
│     - Surpasses human intelligence               │
│     - Self-aware, consciousness                  │
│     - Hypothetical / future concept              │
└─────────────────────────────────────────────────┘
```

### B. Based on Functionality:

| Type | Description | Example |
|------|-------------|---------|
| **Reactive Machines** | No memory, responds to current input only | IBM Deep Blue |
| **Limited Memory** | Uses past data for short-term decisions | Self-driving cars |
| **Theory of Mind** | Understands emotions, beliefs of others | Future AI (research) |
| **Self-Aware** | Has consciousness, self-awareness | Hypothetical |

---

## 8. 📌 PROBLEM FORMULATION [5-15 Marks] — 🔴 GUARANTEED (6/6)

### Answer:

**Problem Formulation** involves defining a problem formally with these components:

| Component | Description |
|-----------|-------------|
| **Initial State** | Starting configuration |
| **Actions/Successor Function** | What actions are available |
| **State Space** | Set of all reachable states |
| **Goal Test** | Checks if goal is reached |
| **Path Cost** | Cost of reaching a state |

### Example 1: 8-Puzzle Problem

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

- **States**: All permutations of tiles on 3×3 grid
- **Actions**: Move blank Up, Down, Left, Right
- **Goal Test**: State matches goal configuration
- **Path Cost**: 1 per move

### Example 2: Autonomous Taxi Driver

- **Initial State**: Taxi at some location with passenger
- **Actions**: Turn left/right, accelerate, brake, signal, pick-up, drop-off
- **State Space**: All combinations of location, speed, traffic, passenger
- **Goal Test**: Passenger delivered to destination safely
- **Path Cost**: Time + fuel + tolls + penalties for violations

### Example 3: Monkey-Banana Problem

- **Initial State**: Monkey on floor, Bananas hanging from ceiling, Crate in corner
- **Goal**: Monkey has bananas
- **Actions**: Walk(x,y), Push(crate,x,y), ClimbUp(crate), Grasp(bananas)
- **Plan**: Walk to crate → Push crate under bananas → Climb crate → Grasp bananas

---

## 9. 📌 APPLICATIONS OF AI [5-10 Marks] — 🟠 (5/6)

### Answer:

| Domain | Applications |
|--------|-------------|
| **Healthcare** | Disease diagnosis, Drug discovery, Medical imaging, Robot surgery, Personalized medicine |
| **Finance/Banking** | Fraud detection, Algorithmic trading, Credit scoring, Chatbots for customer service |
| **Retail** | Recommendation systems, Demand forecasting, Inventory management, Price optimization |
| **Transportation** | Self-driving cars, Traffic prediction, Route optimization, Autonomous drones |
| **Robotics** | Industrial automation, Warehouse robots, Surgical robots, Space exploration |
| **NLP** | Machine translation, Voice assistants (Siri, Alexa), Sentiment analysis, Chatbots |
| **Gaming** | Game AI opponents, Procedural content generation, Player behavior modeling |
| **Education** | Intelligent tutoring, Automated grading, Personalized learning paths |
| **Security** | Surveillance, Facial recognition, Cyber threat detection |
| **Agriculture** | Crop monitoring, Yield prediction, Pest detection, Automated harvesting |
