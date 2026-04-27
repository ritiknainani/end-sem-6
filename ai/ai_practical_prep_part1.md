# 🎯 AI Practical Exam Prep — Part 1: Search Algorithms (Exp 1–6)

> **Course:** CSL604 — AI Lab | **Semester:** TE/VI | **Session:** Jan–Apr 2026

> [!IMPORTANT]
> **Exam Instructions from experiment list:**
> - For search algorithms: **Draw tree/graph on answer book** and write output with **OPEN list and CLOSE list**
> - Viva can be on entire syllabus OR your technical/research paper
> - Prepare Block World, Wumpus World, FOL conversions

---

## 📌 Graph Used In All Search Experiments

```
        A
       / \
      B   C
     / \   \
    D   E   F
        |
        G
```

```python
# Unweighted (for DFS, DLS, DFID, BFS)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}

# Weighted (for Greedy, A*)
graph = {
    'A': [('B',1),('C',3)],
    'B': [('D',3),('E',1)],
    'C': [('F',5)],
    'D': [],
    'E': [('G',2)],
    'F': [],
    'G': []
}
heuristic = {'A':6,'B':4,'C':5,'D':3,'E':2,'F':4,'G':0}
```

---

## Exp 1: DFS (Depth First Search)

### Code (use this — clean & simple)
```python
def dfs(graph, start, goal, visited=None):
    if visited is None:
        visited = set()
    print(start, end=" ")
    if start == goal:
        return True
    visited.add(start)
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            if dfs(graph, neighbor, goal, visited):
                return True
    return False
```

### Sample I/O
```
Start: A, Goal: G
DFS: A B D E G
Goal Found!
```

### Open/Close List Trace (WRITE THIS ON ANSWER SHEET)
| Step | OPEN (Stack) | CLOSE (Visited) | Current |
|------|-------------|-----------------|---------|
| 1 | [A] | {} | A |
| 2 | [B, C] | {A} | B |
| 3 | [D, E, C] | {A,B} | D |
| 4 | [E, C] | {A,B,D} | E |
| 5 | [G, C] | {A,B,D,E} | G ✅ |

### Viva Points
- **Type:** Uninformed, Blind search
- **Data Structure:** Stack (recursion = implicit stack)
- **Time:** O(b^m), **Space:** O(bm) where b=branching, m=max depth
- **Complete?** No (can loop in cyclic graphs without visited set)
- **Optimal?** No (doesn't guarantee shortest path)

---

## Exp 2: DLS (Depth Limited Search)

### Code
```python
def dls(graph, start, goal, limit):
    print(start, end=" ")
    if start == goal:
        return True
    if limit <= 0:
        return False
    for neighbor in graph.get(start, []):
        if dls(graph, neighbor, goal, limit - 1):
            return True
    return False
```

### Sample I/O
```
Start: A, Goal: G, Limit: 3
DLS: A B D E G
Goal Found!

Start: A, Goal: G, Limit: 2
DLS: A B D E C F
Goal Not Found.
```

### Open/Close List (Limit=3)
| Step | Current | Depth | Action |
|------|---------|-------|--------|
| 1 | A | 0 | Expand |
| 2 | B | 1 | Expand |
| 3 | D | 2 | Expand (leaf) |
| 4 | E | 2 | Expand |
| 5 | G | 3 | ✅ Goal Found |

### Viva Points
- DFS + depth limit → prevents infinite loops
- **Complete?** No (goal may be beyond limit)
- **Optimal?** No
- If limit < depth of goal → fails; if limit too high → wastes time

---

## Exp 3: DFID (Depth First Iterative Deepening)

### Code
```python
def dls(graph, start, goal, limit):
    print(start, end=" ")
    if start == goal:
        return True
    if limit <= 0:
        return False
    for neighbor in graph.get(start, []):
        if dls(graph, neighbor, goal, limit - 1):
            return True
    return False

def dfid(graph, start, goal, max_depth):
    for depth in range(max_depth + 1):
        print(f"\nDepth = {depth}: ", end="")
        if dls(graph, start, goal, depth):
            print("\nGoal Found!")
            return True
    print("\nGoal Not Found")
    return False
```

### Sample I/O
```
Start: A, Goal: G, Max Depth: 4

Depth = 0: A
Depth = 1: A B C
Depth = 2: A B D E C F
Depth = 3: A B D E G
Goal Found!
```

### Viva Points
- **Combines** BFS completeness + DFS space efficiency
- Runs DLS with limit = 0, 1, 2, ... until goal found
- **Complete?** Yes | **Optimal?** Yes (uniform cost)
- **Time:** O(b^d) | **Space:** O(bd) — best of both worlds
- Repeated work is minimal (~11% overhead for b=2)

---

## Exp 4: BFS (Breadth First Search)

### Code
```python
from collections import deque

def bfs(graph, start, goal):
    visited = set()
    queue = deque([start])
    print("BFS:", end=" ")
    while queue:
        node = queue.popleft()
        print(node, end=" ")
        if node == goal:
            print("\nGoal Found!")
            return
        visited.add(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited and neighbor not in queue:
                queue.append(neighbor)
    print("\nGoal Not Found")
```

### Sample I/O
```
Start: A, Goal: G
BFS: A B C D E F G
Goal Found!
```

### Open/Close List Trace (WRITE THIS)
| Step | OPEN (Queue) | CLOSE | Current |
|------|-------------|-------|---------|
| 1 | [A] | {} | A |
| 2 | [B, C] | {A} | B |
| 3 | [C, D, E] | {A,B} | C |
| 4 | [D, E, F] | {A,B,C} | D |
| 5 | [E, F] | {A,B,C,D} | E |
| 6 | [F, G] | {A,B,C,D,E} | F |
| 7 | [G] | {A,B,C,D,E,F} | G ✅ |

### Viva Points
- **Data Structure:** Queue (FIFO)
- **Complete?** Yes | **Optimal?** Yes (uniform cost edges)
- **Time:** O(b^d) | **Space:** O(b^d) — space is the problem!
- Explores level by level

---

## Exp 5: Greedy Best First Search

### Code
```python
import heapq

def greedy(graph, h, start, goal):
    visited = set()
    pq = [(h[start], start)]
    print("Greedy:")
    while pq:
        _, node = heapq.heappop(pq)
        if node in visited:
            continue
        print(f"{node}(h={h[node]})", end=" ")
        if node == goal:
            print("\nGoal Found!")
            return
        visited.add(node)
        for nbr, cost in graph.get(node, []):
            if nbr not in visited:
                heapq.heappush(pq, (h[nbr], nbr))
    print("\nGoal Not Found")
```

### Sample I/O
```
Start: A, Goal: G
Greedy: A(h=6) B(h=4) E(h=2) G(h=0)
Goal Found!
```

### Open/Close List Trace
| Step | OPEN (Priority Queue) | CLOSE | Current | h |
|------|----------------------|-------|---------|---|
| 1 | [(6,A)] | {} | A | 6 |
| 2 | [(4,B),(5,C)] | {A} | B | 4 |
| 3 | [(2,E),(5,C),(3,D)] | {A,B} | E | 2 |
| 4 | [(0,G),(5,C),(3,D)] | {A,B,E} | G | 0 ✅ |

### Viva Points
- **Informed search** — uses heuristic h(n) only
- **f(n) = h(n)** — selects node closest to goal (estimated)
- **Data Structure:** Priority Queue / Min-Heap
- **Complete?** No (can get stuck in loops) | **Optimal?** No
- Faster than BFS but not guaranteed shortest path

---

## Exp 6: A* Search

### Code
```python
import heapq

def astar(graph, h, start, goal):
    visited = set()
    pq = [(h[start], 0, start)]  # (f, g, node)
    print("A*:")
    while pq:
        f, g, node = heapq.heappop(pq)
        if node in visited:
            continue
        print(f"{node}(g={g},h={h[node]},f={f})", end=" ")
        if node == goal:
            print(f"\nGoal Found, Cost={g}")
            return
        visited.add(node)
        for nbr, cost in graph.get(node, []):
            if nbr not in visited:
                new_g = g + cost
                new_f = new_g + h[nbr]
                heapq.heappush(pq, (new_f, new_g, nbr))
    print("\nGoal Not Found")
```

### Sample I/O
```
Start: A, Goal: G
A*: A(g=0,h=6,f=6) B(g=1,h=4,f=5) E(g=2,h=2,f=4) G(g=4,h=0,f=4)
Goal Found, Cost=4
```

### Open/Close List Trace
| Step | OPEN (f, g, node) | CLOSE | Current | g | h | f=g+h |
|------|-------------------|-------|---------|---|---|-------|
| 1 | [(6,0,A)] | {} | A | 0 | 6 | 6 |
| 2 | [(5,1,B),(8,3,C)] | {A} | B | 1 | 4 | 5 |
| 3 | [(4,2,E),(6,4,D),(8,3,C)] | {A,B} | E | 2 | 2 | 4 |
| 4 | [(4,4,G),(6,4,D),(8,3,C)] | {A,B,E} | G | 4 | 0 | 4 ✅ |

### Viva Points
- **f(n) = g(n) + h(n)** — actual cost + estimated cost
- **Complete?** Yes | **Optimal?** Yes (if h is admissible)
- **Admissible heuristic:** h(n) never overestimates actual cost
- **Consistent heuristic:** h(n) ≤ cost(n,n') + h(n') → no reopening
- A* = Greedy + UCS combined
- If h=0 → becomes UCS; if g=0 → becomes Greedy

---

## 🔑 Quick Comparison Table (VIVA FAVORITE!)

| Algorithm | Complete | Optimal | Time | Space | DS | Informed? |
|-----------|----------|---------|------|-------|----|-----------|
| DFS | No | No | O(b^m) | O(bm) | Stack | No |
| DLS | No | No | O(b^l) | O(bl) | Stack | No |
| DFID | Yes | Yes* | O(b^d) | O(bd) | Stack | No |
| BFS | Yes | Yes* | O(b^d) | O(b^d) | Queue | No |
| Greedy | No | No | O(b^m) | O(b^m) | PQ | Yes |
| A* | Yes | Yes | O(b^d) | O(b^d) | PQ | Yes |

*Yes for uniform cost edges
