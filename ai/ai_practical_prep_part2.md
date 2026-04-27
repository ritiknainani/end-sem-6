# 🎯 AI Practical Exam Prep — Part 2: Optimization + Prolog (Exp 7–11)

> [!IMPORTANT]
> **Key Exam Instructions:**
> - Exp 7 GA: Use F(x) = (a+2b+3c+4d) - 30, take **6 chromosomes**, print initial + final population + best
> - Exp 8 Hill Climbing: Use y = sin(x) OR -x² OR -5x²+3x+6
> - Exp 9 & 10: Perform **ONE iteration** only, 6 chromosomes, binary conversion
> - Exp 9 Crossover rate = 25%, Exp 10 Mutation rate = 10%

---

## Exp 7: Genetic Algorithm — F(x)= (a+2b+3c+4d)-30

### Code (Exam-Ready — MATCHES EXACT requirement)
```python
import random

def fitness(chromo):
    a, b, c, d = chromo
    return abs((a + 2*b + 3*c + 4*d) - 30)

def create_population(size):
    return [[random.randint(0,9) for _ in range(4)] for _ in range(size)]

def selection(pop):
    pop.sort(key=fitness)  # lower fitness = closer to 30 = better
    return pop[:2]

def crossover(p1, p2):
    pt = random.randint(1,3)
    return p1[:pt]+p2[pt:], p2[:pt]+p1[pt:]

def mutate(chromo):
    i = random.randint(0,3)
    chromo[i] = random.randint(0,9)
    return chromo

def genetic_algorithm():
    pop = create_population(6)
    print("Initial Population:")
    for i,c in enumerate(pop):
        print(f"  C{i+1}: {c}  fitness={fitness(c)}")

    for gen in range(10):
        parents = selection(pop)
        new_pop = [p[:] for p in parents]
        while len(new_pop) < 6:
            c1, c2 = crossover(parents[0][:], parents[1][:])
            new_pop.append(mutate(c1))
            if len(new_pop) < 6:
                new_pop.append(mutate(c2))
        pop = new_pop

    print("\nFinal Population:")
    for i,c in enumerate(pop):
        print(f"  C{i+1}: {c}  fitness={fitness(c)}")
    best = min(pop, key=fitness)
    print(f"\nBest Chromosome: {best}")
    print(f"Value: a+2b+3c+4d = {best[0]+2*best[1]+3*best[2]+4*best[3]}")
    print(f"Fitness (distance from 30): {fitness(best)}")

genetic_algorithm()
```

### Sample I/O
```
Initial Population:
  C1: [3, 5, 2, 1]  fitness=11
  C2: [7, 1, 4, 3]  fitness=3
  C3: [2, 4, 1, 6]  fitness=7
  C4: [1, 3, 5, 2]  fitness=0    ← optimal!
  C5: [8, 0, 3, 4]  fitness=3
  C6: [4, 2, 6, 0]  fitness=4

Final Population:
  C1: [1, 3, 5, 2]  fitness=0
  ...
Best Chromosome: [1, 3, 5, 2]
Value: a+2b+3c+4d = 30
Fitness: 0
```

### Viva Points
- **Goal:** Minimize |F(x) - 30| → fitness = 0 means optimal
- **Steps:** Initialize → Selection → Crossover → Mutation → Repeat
- GA is a **metaheuristic** inspired by natural selection
- **Selection:** Choose fittest (lowest distance from 30)
- **Crossover:** Single-point crossover, combine parent genes
- **Mutation:** Random gene change to maintain diversity

---

## Exp 8: Hill Climbing

### Code — y = sin(x)
```python
import math

def hill_climbing_sinx():
    current = float(input("Enter initial x: "))
    step = float(input("Enter step size: "))
    iters = int(input("Enter iterations: "))

    print(f"\nInitial: x={current:.4f}, y=sin(x)={math.sin(current):.4f}")

    for i in range(iters):
        left = current - step
        right = current + step
        neighbors = [left, right]
        best = max(neighbors, key=lambda x: math.sin(x))
        if math.sin(best) > math.sin(current):
            current = best
            print(f"Step {i+1}: x={current:.4f}, y={math.sin(current):.4f}")
        else:
            print(f"Converged at step {i+1}")
            break

    print(f"\nBest: x={current:.4f}, y=sin(x)={math.sin(current):.4f}")

hill_climbing_sinx()
```

### Code — y = -x²
```python
def hill_climbing_neg_x2():
    current = float(input("Enter initial x: "))
    step = float(input("Enter step size: "))
    iters = int(input("Enter iterations: "))

    f = lambda x: -(x**2)
    print(f"\nInitial: x={current:.4f}, y={f(current):.4f}")

    for i in range(iters):
        neighbors = [current - step, current + step]
        best = max(neighbors, key=f)
        if f(best) > f(current):
            current = best
            print(f"Step {i+1}: x={current:.4f}, y={f(current):.4f}")
        else:
            print(f"Converged at step {i+1}")
            break

    print(f"\nBest: x={current:.4f}, y={f(current):.4f}")
```

### Code — y = -5x²+3x+6
```python
def hill_climbing_quadratic():
    current = float(input("Enter initial x: "))
    step = float(input("Enter step size: "))
    iters = int(input("Enter iterations: "))

    f = lambda x: -5*x**2 + 3*x + 6
    print(f"\nInitial: x={current:.4f}, y={f(current):.4f}")

    for i in range(iters):
        neighbors = [current - step, current + step]
        best = max(neighbors, key=f)
        if f(best) > f(current):
            current = best
            print(f"Step {i+1}: x={current:.4f}, y={f(current):.4f}")
        else:
            print(f"Converged at step {i+1}")
            break

    print(f"\nBest: x={current:.4f}, y={f(current):.4f}")
```

### Sample I/O (y = -x²)
```
Enter initial x: 5
Enter step size: 0.5
Enter iterations: 20

Initial: x=5.0000, y=-25.0000
Step 1: x=4.5000, y=-20.2500
Step 2: x=4.0000, y=-16.0000
...
Step 10: x=0.0000, y=0.0000
Converged at step 11

Best: x=0.0000, y=0.0000
```

### Viva Points
- **Local search** — only looks at neighbors
- **Greedy** — always moves to best neighbor
- **Problems:** Gets stuck at local maxima, plateaus, ridges
- **Variants:** Steepest ascent, Stochastic, Random restart
- **No backtracking** — unlike DFS
- For -x²: maximum at x=0 (y=0)
- For sin(x): maximum at x=π/2 (y=1)
- For -5x²+3x+6: maximum at x=0.3 (y=6.45)

---

## Exp 9: Crossover in Genetic Algorithm (ONE ITERATION, 25% rate)

### Code (Exact as per requirement)
```python
import random

POP_SIZE = 6
CHROM_LEN = 5  # 5-bit binary
CROSSOVER_RATE = 0.25

def generate_population():
    pop = []
    for _ in range(POP_SIZE):
        num = random.randint(0, 31)
        binary = format(num, f'0{CHROM_LEN}b')
        pop.append(binary)
    return pop

def crossover(population):
    print("\n--- Crossover (Rate=25%) ---")
    new_pop = population.copy()
    for i in range(0, POP_SIZE, 2):
        if i+1 >= POP_SIZE:
            break
        p1, p2 = population[i], population[i+1]
        r = random.random()
        print(f"\nPair: {p1} x {p2} | Random={r:.2f}")
        if r < CROSSOVER_RATE:
            pt = random.randint(1, CHROM_LEN-1)
            c1 = p1[:pt] + p2[pt:]
            c2 = p2[:pt] + p1[pt:]
            print(f"  Crossover at point {pt} → {c1}, {c2}")
            new_pop[i], new_pop[i+1] = c1, c2
        else:
            print(f"  No crossover (r >= 0.25)")
    return new_pop

# Main
pop = generate_population()
print("Initial Population (6 chromosomes):")
for i,c in enumerate(pop):
    print(f"  C{i+1}: {c} (decimal={int(c,2)})")

pop = crossover(pop)

print("\nFinal Population After Crossover:")
for i,c in enumerate(pop):
    print(f"  C{i+1}: {c} (decimal={int(c,2)})")
```

### Sample I/O
```
Initial Population (6 chromosomes):
  C1: 10110 (decimal=22)
  C2: 01101 (decimal=13)
  C3: 11001 (decimal=25)
  C4: 00111 (decimal=7)
  C5: 10010 (decimal=18)
  C6: 01010 (decimal=10)

--- Crossover (Rate=25%) ---
Pair: 10110 x 01101 | Random=0.18
  Crossover at point 3 → 10101, 01110
Pair: 11001 x 00111 | Random=0.67
  No crossover (r >= 0.25)
Pair: 10010 x 01010 | Random=0.89
  No crossover (r >= 0.25)

Final Population After Crossover:
  C1: 10101 (decimal=21)
  C2: 01110 (decimal=14)
  C3: 11001 (decimal=25)
  C4: 00111 (decimal=7)
  C5: 10010 (decimal=18)
  C6: 01010 (decimal=10)
```

### Viva Points
- **Single-point crossover:** Pick random point, swap tails
- Crossover rate 25% → only 25% chance a pair actually crosses
- Pairs: (C1,C2), (C3,C4), (C5,C6)
- If random < 0.25 → crossover happens; else parents pass unchanged
- **Purpose:** Combine good traits from two parents

---

## Exp 10: Mutation in Genetic Algorithm (ONE ITERATION, 10% rate)

### Code
```python
import random

POP_SIZE = 6
CHROM_LEN = 5
MUTATION_RATE = 0.10

def generate_population():
    pop = []
    for _ in range(POP_SIZE):
        num = random.randint(0, 31)
        pop.append(format(num, f'0{CHROM_LEN}b'))
    return pop

def mutation(population):
    print("\n--- Mutation (Rate=10%) ---")
    new_pop = []
    for chrom in population:
        bits = list(chrom)
        print(f"\nOriginal: {chrom}")
        for i in range(CHROM_LEN):
            r = random.random()
            if r < MUTATION_RATE:
                bits[i] = '1' if bits[i] == '0' else '0'
                print(f"  Bit {i} flipped! (r={r:.2f})")
        result = ''.join(bits)
        print(f"After: {result}")
        new_pop.append(result)
    return new_pop

pop = generate_population()
print("Initial Population:")
for i,c in enumerate(pop):
    print(f"  C{i+1}: {c} (decimal={int(c,2)})")

pop = mutation(pop)

print("\nFinal Population After Mutation:")
for i,c in enumerate(pop):
    print(f"  C{i+1}: {c} (decimal={int(c,2)})")
```

### Sample I/O
```
Initial Population:
  C1: 11010 (decimal=26)
  C2: 01001 (decimal=9)
  C3: 10110 (decimal=22)
  C4: 00011 (decimal=3)
  C5: 11100 (decimal=28)
  C6: 01111 (decimal=15)

--- Mutation (Rate=10%) ---
Original: 11010
  Bit 2 flipped! (r=0.04)
After: 11110

Original: 01001
After: 01001  (no mutation)
...

Final Population After Mutation:
  C1: 11110 (decimal=30)
  C2: 01001 (decimal=9)
  ...
```

### Viva Points
- **Bit-flip mutation:** Each bit has 10% chance of flipping
- **Purpose:** Maintain genetic diversity, prevent premature convergence
- Total bits = 6 chromosomes × 5 bits = 30 bits checked
- Expected mutations per iteration = 30 × 0.10 = ~3 bits
- Without mutation → population converges too quickly (loses diversity)

---

## Exp 11: Family Tree in Prolog

### Code (Directly from your file — perfect as-is)
```prolog
% FACTS
male(john).
male(paul).
male(mike).
male(david).

female(linda).
female(susan).
female(anna).
female(emma).

parent(john, paul).
parent(john, anna).
parent(linda, paul).
parent(linda, anna).
parent(paul, mike).
parent(paul, emma).
parent(susan, mike).
parent(susan, emma).
parent(anna, david).

% RULES
father(X,Y):- parent(X,Y), male(X).
mother(X,Y):- parent(X,Y), female(X).
sibling(X,Y):- parent(Z,X), parent(Z,Y), X\=Y.
brother(X,Y):- sibling(X,Y), male(X).
sister(X,Y):- sibling(X,Y), female(X).
grandparent(X,Y):- parent(X,Z), parent(Z,Y).
grandfather(X,Y):- grandparent(X,Y), male(X).
grandmother(X,Y):- grandparent(X,Y), female(X).
uncle(X,Y):- brother(X,Z), parent(Z,Y).
aunt(X,Y):- sister(X,Z), parent(Z,Y).
```

### Family Tree Diagram (DRAW THIS)
```
    John ─── Linda
    ┌────┴────┐
   Paul     Anna
    │          │
  Susan      David
  ┌─┴─┐
Mike  Emma
```

### Sample Queries & Output
```prolog
?- father(john, paul).     → true
?- mother(linda, anna).    → true
?- sibling(paul, anna).    → true
?- grandfather(john, mike).→ true
?- grandmother(linda, emma).→ true
?- uncle(paul, david).     → false (paul is not brother of anna's parent... wait)
?- brother(paul, anna).    → true
?- aunt(anna, mike).       → true
?- father(X, mike).        → X = paul
?- mother(X, emma).        → X = susan
?- grandparent(john, X).   → X = mike ; X = emma ; X = david
```

### Viva Points
- **Prolog = Logic Programming** — declarative, not imperative
- **Facts:** Ground truth (male, female, parent)
- **Rules:** Derived relations using `:-` (if)
- **Queries:** `?-` asks Prolog to prove/find solutions
- **Unification:** Pattern matching to bind variables
- **Backtracking:** Prolog automatically tries alternatives
- `,` means AND | `;` means OR | `\=` means not equal
- **Closed World Assumption:** Anything not stated/derivable = false

---

## 🔑 Genetic Algorithm Master Summary (VIVA)

| Term | Meaning |
|------|---------|
| Chromosome | Solution representation (binary string or array) |
| Gene | Single element of chromosome |
| Population | Set of candidate solutions |
| Fitness | How good a solution is |
| Selection | Choose best parents |
| Crossover | Combine two parents to create children |
| Mutation | Random change to maintain diversity |
| Generation | One cycle of selection+crossover+mutation |
| Elitism | Best solutions pass unchanged to next gen |

### GA Flow
```
Initialize Population → Evaluate Fitness → Selection → Crossover → Mutation → New Population → Repeat
```
