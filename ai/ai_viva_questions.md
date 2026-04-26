# 🎤 AI Viva Questions — 100+ with Keyword Answers

> **Subject:** Artificial Intelligence (89284) | MU Sem 6 Comp Engg
> **Tip:** Bold words are **keywords** — mention them for marks!

---

## MODULE 1: Introduction to AI & Agents

**1. What is Artificial Intelligence?**
AI is the branch of computer science that creates **intelligent machines** capable of performing tasks that typically require **human intelligence** — such as reasoning, learning, perception, and decision-making.

**2. Who is the father of AI?**
**John McCarthy** coined the term "Artificial Intelligence" in **1956** at the **Dartmouth Conference**.

**3. What are the four categories of AI?**
Based on capability: **Narrow AI** (task-specific), **General AI** (human-level), **Super AI** (beyond human). Based on functionality: **Reactive Machines**, **Limited Memory**, **Theory of Mind**, **Self-Aware**.

**4. What is an intelligent agent?**
An entity that **perceives** its environment through **sensors** and **acts** upon it through **actuators** to achieve goals.

**5. What is PEAS?**
**Performance measure, Environment, Actuators, Sensors** — a framework to describe the **task environment** of an agent.

**6. Give PEAS for a self-driving car.**
**P:** Safety, speed, legality. **E:** Roads, traffic, pedestrians. **A:** Steering, brake, accelerator. **S:** Camera, LIDAR, GPS, speedometer.

**7. What is a reflex agent?**
An agent that acts based on **current percept only** using **condition-action rules** (if-then), with **no memory** of past states.

**8. What is a utility-based agent?**
An agent that uses a **utility function** to evaluate how "happy" a state makes it, choosing actions that **maximize expected utility**.

**9. What is a goal-based agent?**
An agent that uses **goal information** combined with knowledge of the environment to choose actions that **achieve the goal**.

**10. What is a learning agent?**
An agent with four components: **Learning Element** (improves), **Performance Element** (selects actions), **Critic** (feedback), **Problem Generator** (explores).

**11. What are the properties of a task environment?**
**Observable** (fully/partially), **Deterministic/Stochastic**, **Episodic/Sequential**, **Static/Dynamic**, **Discrete/Continuous**, **Single/Multi-agent**.

**12. Differentiate fully vs partially observable.**
**Fully observable:** Agent sees complete state (chess). **Partially observable:** Agent has incomplete information (poker, driving).

**13. What is a deterministic environment?**
Next state is **completely determined** by the current state and action. No randomness. Example: Chess.

**14. What is the Turing Test?**
A test where a human interrogator cannot distinguish between a **machine** and a **human** based on responses. Proposed by **Alan Turing** in 1950.

**15. What is the Total Turing Test?**
Extends the Turing Test to include **computer vision** (seeing) and **robotics** (physical manipulation), not just text communication.

---

## MODULE 2: Search Algorithms

**16. What is a search problem?**
Defined by: **Initial state**, **Actions/Successor function**, **State space**, **Goal test**, **Path cost**.

**17. What is state space?**
The set of **all possible states** reachable from the initial state by any sequence of actions.

**18. Differentiate informed vs uninformed search.**
**Uninformed:** No extra knowledge, explores blindly (BFS, DFS). **Informed:** Uses **heuristic function h(n)** to guide search (A*, Greedy).

**19. What is BFS?**
**Breadth-First Search** — explores all nodes at current depth before going deeper. Uses a **queue**. **Complete** and **optimal** for uniform cost.

**20. What is DFS?**
**Depth-First Search** — explores as deep as possible before backtracking. Uses a **stack**. **Not complete** (can loop), **not optimal**.

**21. What is Uniform Cost Search (UCS)?**
Expands node with **lowest path cost g(n)**. Uses **priority queue**. **Optimal** and **complete**.

**22. What is Depth Limited Search?**
DFS with a **predetermined depth limit L**. Solves infinite path problem of DFS. **Not complete** if L < solution depth.

**23. What is Iterative Deepening DFS?**
Runs DLS with **increasing limits** (0, 1, 2...). Combines **BFS completeness** with **DFS space efficiency**. **Optimal** and **complete**.

**24. What is a heuristic function?**
A function **h(n)** that estimates the cost from node n to the goal. Must be **admissible** (never overestimates) for optimal A*.

**25. What is A* search?**
Informed search using **f(n) = g(n) + h(n)**. g(n)=actual cost, h(n)=heuristic estimate. **Optimal** and **complete** with admissible heuristic.

**26. What makes A* optimal?**
The heuristic must be **admissible** (h(n) ≤ actual cost) and **consistent** (h(n) ≤ cost(n,n') + h(n')).

**27. What is Greedy Best-First Search?**
Uses only **f(n) = h(n)** — expands node closest to goal. **Not optimal**, **not complete**. Fast but can be misled.

**28. What is Hill Climbing?**
A **local search** that moves to the **best neighbor** continuously. Gets stuck at **local maxima**, **plateaus**, and **ridges**.

**29. What are problems of Hill Climbing?**
**Local maxima** (stuck at non-global peak), **Plateau** (flat region, no direction), **Ridge** (narrow elevated path, oscillation).

**30. How to solve Hill Climbing problems?**
**Random restart** (multiple start points), **Simulated Annealing** (allow downhill), **Stochastic hill climbing** (random uphill neighbor).

**31. What is Simulated Annealing?**
Like hill climbing but allows **bad moves** with decreasing probability. Uses **temperature** parameter that cools over time. Inspired by **metallurgy annealing**.

**32. What is a local search?**
Search that operates on a **single current state** and moves to neighbors. Uses **very little memory**. Examples: Hill Climbing, Simulated Annealing, Genetic Algorithm.

**33. What is Beam Search?**
Keeps **k best** states at each level instead of just one (hill climbing) or all (BFS). Trade-off between memory and completeness.

---

## MODULE 3: Game Playing

**34. What is a game tree?**
A tree representation of all possible moves in a game, with **MAX** and **MIN** players alternating turns.

**35. What is the Minimax algorithm?**
A recursive algorithm for two-player **zero-sum games**. **MAX** maximizes utility, **MIN** minimizes it. Explores full tree.

**36. What is Alpha-Beta Pruning?**
An **optimization of Minimax** that prunes branches that **cannot affect the final decision**. α = best for MAX, β = best for MIN. Prune when **α ≥ β**.

**37. When does α cutoff occur?**
At a **MIN node**, when the value found is ≤ α (MAX's guaranteed value). The remaining children are pruned.

**38. When does β cutoff occur?**
At a **MAX node**, when the value found is ≥ β (MIN's guaranteed value). The remaining children are pruned.

**39. What is the benefit of Alpha-Beta Pruning?**
Reduces time from **O(b^d) to O(b^(d/2))** in best case — effectively **doubles the searchable depth**.

**40. Does Alpha-Beta change the result?**
**No** — it gives the same result as Minimax, just faster by pruning irrelevant branches.

---

## MODULE 4: Knowledge Representation & Logic

**41. What is knowledge representation?**
Methods to **encode knowledge** about the world in a form that AI systems can use for **reasoning and inference**.

**42. What are the types of knowledge representation?**
**Logical** (PL, FOL), **Semantic Networks**, **Frames**, **Production Rules**, **Ontologies**.

**43. What is Propositional Logic (PL)?**
Logic using **propositions** (true/false statements) and **connectives** (∧, ∨, ¬, →, ↔). Cannot express relations or quantifiers.

**44. What is First Order Logic (FOL)?**
Extends PL with **predicates**, **variables**, **quantifiers** (∀, ∃), **functions**, and **constants**. More expressive than PL.

**45. Difference between PL and FOL?**
PL: No variables, no quantifiers, limited expressiveness. FOL: Has **predicates, variables, ∀ (for all), ∃ (there exists)** — can express complex relationships.

**46. What is Universal Quantifier (∀)?**
"**For all**" — ∀x P(x) means P is true for every x in the domain.

**47. What is Existential Quantifier (∃)?**
"**There exists**" — ∃x P(x) means there is at least one x for which P is true.

**48. What is CNF?**
**Conjunctive Normal Form** — a conjunction (∧) of **clauses**, where each clause is a disjunction (∨) of **literals**. Required for **resolution**.

**49. How to convert to CNF?**
1. Eliminate → and ↔. 2. Move ¬ inward (De Morgan). 3. Standardize variables. 4. **Skolemize** (remove ∃). 5. Drop ∀. 6. Distribute ∨ over ∧.

**50. What is Resolution?**
An inference rule: from (A ∨ B) and (¬B ∨ C), derive (A ∨ C). Used to prove statements by **refutation** — negate conclusion and derive **empty clause (□)**.

**51. What is Forward Chaining?**
**Data-driven** inference — starts from **known facts**, applies rules to derive new facts until **goal is reached**. Bottom-up.

**52. What is Backward Chaining?**
**Goal-driven** inference — starts from **goal**, finds rules that conclude it, recursively proves preconditions. Top-down.

**53. When to use Forward vs Backward Chaining?**
Forward: when many goals, few facts (**monitoring, diagnosis**). Backward: when specific goal to prove (**query answering, expert systems**).

**54. What is Skolemization?**
Removing **existential quantifiers** by replacing ∃x with a **Skolem constant** (if no ∀ before it) or **Skolem function** (if under ∀).

**55. What is unification?**
Process of making two logical expressions **identical** by finding appropriate **substitutions** for variables.

---

## MODULE 5: Planning

**56. What is planning in AI?**
Computing a **sequence of actions** to achieve a goal from an initial state. Uses **state-space representation** with actions having preconditions and effects.

**57. What is STRIPS?**
**Stanford Research Institute Problem Solver** — represents actions with **Preconditions**, **Add List** (effects+), and **Delete List** (effects-).

**58. What is Total Order Planning?**
Plans where actions are in a **completely fixed linear sequence**. Simple but inflexible.

**59. What is Partial Order Planning (POP)?**
Plans where actions are ordered only when **necessary** (causal dependency). Allows **parallel execution** of independent actions.

**60. What are causal links?**
In POP, a link A →(p)→ B means action A **achieves precondition p** needed by action B. Must be **protected** from threats.

**61. What is a threat in POP?**
An action C that might **delete** a condition protected by a causal link. Resolved by **promotion** (B before C) or **demotion** (C before A).

**62. What is Hierarchical Planning?**
Breaking complex tasks into **subtasks** using **HTN (Hierarchical Task Networks)**. High-level actions decomposed into primitive actions.

**63. What is Conditional Planning?**
Planning that handles **uncertainty** by including **conditional branches** (if-then-else) in the plan based on observations.

**64. What is the Sussman Anomaly?**
A problem in **linear planning** where achieving subgoals independently leads to **conflicts**. Shows need for interleaving subgoal steps.

**65. What is the Frame Problem?**
The difficulty of representing what **does NOT change** when an action is performed. Addressed by STRIPS's closed-world assumption.

---

## MODULE 6: Machine Learning Concepts

**66. What is Machine Learning?**
A subset of AI where systems **learn from data** and improve performance without being explicitly programmed. Coined by **Arthur Samuel** (1959).

**67. What are the types of ML?**
**Supervised** (labeled data), **Unsupervised** (unlabeled data), **Reinforcement** (reward-based), **Semi-supervised**.

**68. What is Reinforcement Learning?**
Agent learns by **trial and error** through **rewards** (positive) and **penalties** (negative). Uses **policy**, **value function**, and **Q-function**.

**69. What is the exploration-exploitation trade-off?**
**Explore**: Try new actions to discover better rewards. **Exploit**: Use known best actions. Balance is key in RL.

**70. What is Q-Learning?**
A **model-free RL** algorithm that learns **Q(s,a)** values — expected reward for action a in state s. Update: Q(s,a) ← Q(s,a) + α[R + γ·maxQ(s',a') - Q(s,a)].

**71. What is the discount factor (γ)?**
A value between 0 and 1 that determines the importance of **future rewards**. γ close to 0 = short-sighted, γ close to 1 = far-sighted.

**72. What is PAC Learning?**
**Probably Approximately Correct** — a framework guaranteeing a learning algorithm produces a hypothesis with error ≤ **ε** with probability ≥ **1-δ** in polynomial time.

**73. What is a Genetic Algorithm?**
Optimization inspired by **natural selection**: **Selection**, **Crossover**, **Mutation**. Uses population of candidate solutions called **chromosomes**.

**74. What is crossover in GA?**
Combining two parent chromosomes to produce **offspring** by swapping segments at a **crossover point**.

**75. What is mutation in GA?**
**Randomly altering** a gene in a chromosome with small probability. Maintains **genetic diversity**, prevents premature convergence.

**76. What is fitness function?**
A function that evaluates how **good** a candidate solution is. Higher fitness = better solution.

**77. What is a Belief/Bayesian Network?**
A **directed acyclic graph (DAG)** representing **probabilistic relationships** between variables. Nodes = variables, edges = dependencies.

---

## MODULE 7: NLP & Miscellaneous

**78. What is NLP?**
**Natural Language Processing** — enabling computers to **understand, interpret, and generate** human language.

**79. What are the levels of NLP?**
**Phonological** → **Morphological** → **Lexical** → **Syntactic** → **Semantic** → **Discourse** → **Pragmatic** analysis.

**80. What is a language model?**
A model that assigns **probabilities to sequences of words**. Predicts next word given context. Types: **N-gram, HMM, Neural (RNN, Transformer)**.

**81. What is an N-gram model?**
Predicts word based on previous **N-1 words**. Bigram: P(wₙ|wₙ₋₁). Simple but suffers from **data sparsity**.

**82. What is a parse tree?**
A tree showing the **syntactic structure** of a sentence according to grammar rules. Root = S (sentence), leaves = words.

**83. What is tokenization?**
Splitting text into individual **tokens** (words, subwords, characters). First step in most NLP pipelines.

**84. What is POS tagging?**
Assigning **Part-of-Speech** tags (noun, verb, adjective, etc.) to each word in a sentence.

**85. What is Named Entity Recognition (NER)?**
Identifying and classifying **named entities** (persons, organizations, locations, dates) in text.

**86. What is sentiment analysis?**
Determining the **emotional tone** (positive, negative, neutral) of a piece of text.

---

## MODULE 8: Classic Problems & Environments

**87. Describe the Wumpus World.**
4×4 grid cave with 1 **Wumpus**, **pits**, and **gold**. Agent perceives **Stench** (Wumpus nearby), **Breeze** (Pit nearby), **Glitter** (Gold here). Goal: grab gold, exit alive.

**88. What percepts exist in Wumpus World?**
**Stench** (adjacent Wumpus), **Breeze** (adjacent pit), **Glitter** (gold in room), **Bump** (hit wall), **Scream** (Wumpus killed).

**89. Is Wumpus World fully or partially observable?**
**Partially observable** — agent only perceives current room's sensors, not the entire grid.

**90. What is the 8-puzzle problem?**
3×3 grid with tiles 1-8 and one blank. Slide tiles to reach **goal configuration**. States: tile arrangements. Actions: move blank up/down/left/right.

**91. What is the Monkey-Banana Problem?**
A monkey in a room must reach bananas hanging from ceiling using a crate. Actions: **Walk, Push crate, Climb, Grasp**. Classic planning problem.

**92. What is the Missionary-Cannibal Problem?**
3 missionaries and 3 cannibals must cross a river with a 2-person boat. Cannibals must **never outnumber** missionaries on either side.

**93. What is the Water Jug Problem?**
Given jugs of known capacity (e.g., 4L and 3L), measure a target amount (e.g., 2L). Solved using **state space search** with production rules.

---

## MODULE 9: Quick Conceptual Questions

**94. What is an admissible heuristic?**
h(n) that **never overestimates** the actual cost to reach the goal. Required for A* optimality. h(n) ≤ h*(n).

**95. What is a consistent (monotonic) heuristic?**
h(n) ≤ cost(n,n') + h(n') for every successor n'. Consistent implies admissible. Ensures A* doesn't need to re-expand nodes.

**96. What is the difference between A* and Greedy Best-First?**
A*: f = g + h (**optimal**). Greedy: f = h only (**not optimal**, faster but can be misled).

**97. What is means-ends analysis?**
Problem-solving by identifying the **difference** between current and goal state, then finding an action to **reduce** that difference.

**98. What is a production system?**
A system with **working memory** (facts), **production rules** (if-then), and a **conflict resolution strategy**. Used in expert systems.

**99. What is an expert system?**
An AI system that emulates decision-making of a **human expert** using a **knowledge base** and **inference engine**.

**100. What is the closed-world assumption?**
Anything **not known to be true is assumed false**. Used in STRIPS and databases.

**101. What is the frame problem?**
The challenge of representing what **stays the same** after an action. STRIPS handles it by only listing what changes (add/delete lists).

**102. What is the difference between AI and ML?**
**AI**: Broad field of making intelligent machines. **ML**: Subset of AI — systems learn from data without explicit programming.

**103. What is Deep Learning?**
A subset of ML using **multi-layered neural networks** to learn hierarchical representations. Used in image recognition, NLP, etc.

**104. What is the Chinese Room Argument?**
**John Searle**'s thought experiment arguing that a machine following rules can simulate understanding without **actually understanding** — challenges Strong AI.

**105. Name AI programming languages.**
**Python**, **Prolog** (logic programming), **LISP** (symbolic), **R** (statistical), Java, C++.
