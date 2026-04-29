# SPCC Practical Viva Q&A — Part 2
## FIRST Set | FOLLOW Set | LL(1) Parser | TAC | Code Optimization | Symbol Table

---

## 5. FIRST Set

### Q1. What is a FIRST set?
**A:** FIRST(α) is the set of terminals that can appear as the **first symbol** of any string derived from α. If α can derive ε (empty string), then ε is also in FIRST(α).

### Q2. What are the rules to compute FIRST?
**A:**
1. If X is a terminal → FIRST(X) = {X}
2. If X → ε is a production → add ε to FIRST(X)
3. If X → Y₁Y₂...Yₖ → add FIRST(Y₁) - {ε} to FIRST(X). If ε ∈ FIRST(Y₁), also add FIRST(Y₂) - {ε}, and so on. If ε is in ALL FIRST(Yᵢ), add ε to FIRST(X).

### Q3. Why do we compute FIRST sets?
**A:** FIRST sets are used to construct **predictive parsing tables** (LL(1)). They help determine which production to use when a non-terminal is on top of the stack and we see a particular input symbol.

### Q4. Compute FIRST for: E → TE', E' → +TE' | ε, T → FT', T' → *FT' | ε, F → (E) | id
**A:**
- FIRST(F) = { `(`, `id` }
- FIRST(T') = { `*`, ε }
- FIRST(T) = FIRST(F) = { `(`, `id` }
- FIRST(E') = { `+`, ε }
- FIRST(E) = FIRST(T) = { `(`, `id` }

### Q5. What happens if FIRST sets of two alternatives overlap?
**A:** If for a production `A → α | β`, FIRST(α) ∩ FIRST(β) ≠ ∅, then the grammar is **not LL(1)**. The parser can't decide which alternative to choose. Left factoring may help resolve this.

### Q6. When is ε added to FIRST set?
**A:** ε is added to FIRST(X) if:
- X → ε is a production, OR
- X → Y₁Y₂...Yₖ and ε ∈ FIRST(Yᵢ) for ALL i from 1 to k

### Q7. What data structure did you use to store FIRST sets?
**A:** A dictionary/map where keys are non-terminals (strings) and values are sets of terminals (including ε). Sets are used to automatically handle duplicates.

### Q8. How do you handle cycles in FIRST computation?
**A:** Use an iterative fixed-point algorithm — keep computing FIRST sets until no changes occur in any set. This naturally handles cycles and mutual dependencies.

### Q9. What is the difference between FIRST of a terminal and non-terminal?
**A:** FIRST of a terminal is just the terminal itself: FIRST(a) = {a}. FIRST of a non-terminal requires analyzing all its productions and possibly the FIRST sets of other non-terminals.

### Q10. Can FIRST set contain more than one element?
**A:** Yes. If a non-terminal has multiple alternatives starting with different terminals, all those terminals appear in its FIRST set. E.g., `F → (E) | id` → FIRST(F) = {(, id}.

---

## 6. FOLLOW Set

### Q1. What is a FOLLOW set?
**A:** FOLLOW(A) is the set of terminals that can appear **immediately to the right** of non-terminal A in some sentential form. `$` (end-of-input marker) is always in FOLLOW of the start symbol.

### Q2. What are the rules to compute FOLLOW?
**A:**
1. Add `$` to FOLLOW(S) where S is the start symbol
2. If A → αBβ, add FIRST(β) - {ε} to FOLLOW(B)
3. If A → αB, or A → αBβ where ε ∈ FIRST(β), add FOLLOW(A) to FOLLOW(B)

### Q3. Why do we need FOLLOW sets?
**A:** FOLLOW sets are used when a non-terminal can derive ε. In that case, we need to know what can follow that non-terminal to make parsing decisions. They are essential for building LL(1) parsing tables.

### Q4. Compute FOLLOW for: E → TE', E' → +TE' | ε, T → FT', T' → *FT' | ε, F → (E) | id
**A:**
- FOLLOW(E) = { `)`, `$` }
- FOLLOW(E') = FOLLOW(E) = { `)`, `$` }
- FOLLOW(T) = { `+`, `)`, `$` } (from FIRST(E') ∪ FOLLOW(E'))
- FOLLOW(T') = FOLLOW(T) = { `+`, `)`, `$` }
- FOLLOW(F) = { `*`, `+`, `)`, `$` } (from FIRST(T') ∪ FOLLOW(T'))

### Q5. Is ε ever in a FOLLOW set?
**A:** **No.** ε is never in any FOLLOW set. FOLLOW sets contain only terminals and `$`. This is a key difference from FIRST sets.

### Q6. Why is $ added to FOLLOW of start symbol?
**A:** `$` represents the end-of-input marker. Since the start symbol represents the entire program, the end-of-input naturally follows it. This ensures the parser knows when to accept.

### Q7. What is the relationship between FIRST and FOLLOW?
**A:** FOLLOW uses FIRST during computation (Rule 2: FIRST(β) is added to FOLLOW(B)). Together they determine entries in the LL(1) parsing table. FIRST tells what a non-terminal can start with; FOLLOW tells what can come after it.

### Q8. Does FOLLOW set computation depend on order of processing?
**A:** The iterative algorithm processes all productions repeatedly until no changes occur (fixed-point). The final result is independent of processing order.

### Q9. Can two non-terminals have the same FOLLOW set?
**A:** Yes. For example, if A → Bα and α can derive ε, FOLLOW(A) ⊆ FOLLOW(B). In some grammars, E' and E may share the same FOLLOW set.

### Q10. What if a non-terminal appears multiple times on the RHS?
**A:** Apply the FOLLOW rules at each occurrence independently. Each occurrence contributes terminals to the FOLLOW set of that non-terminal.

---

## 7. LL(1) Parser

### Q1. What does LL(1) stand for?
**A:**
- **L** — Left-to-right scanning of input
- **L** — Leftmost derivation
- **(1)** — One lookahead symbol

### Q2. What is an LL(1) parsing table?
**A:** A 2D table where rows are non-terminals, columns are terminals (+ $). Entry M[A, a] contains the production to use when non-terminal A is on the stack and terminal a is the current input. Empty entries indicate syntax errors.

### Q3. How do you construct an LL(1) parsing table?
**A:** For each production A → α:
1. For each terminal `a` in FIRST(α), add A → α to M[A, a]
2. If ε ∈ FIRST(α), for each terminal `b` in FOLLOW(A), add A → α to M[A, b]
3. If ε ∈ FIRST(α) and $ ∈ FOLLOW(A), add A → α to M[A, $]

### Q4. When is a grammar LL(1)?
**A:** A grammar is LL(1) if and only if for every pair of productions A → α | β:
1. FIRST(α) ∩ FIRST(β) = ∅
2. At most one of α, β can derive ε
3. If α ⇒* ε, then FIRST(β) ∩ FOLLOW(A) = ∅

### Q5. What is the parsing algorithm for LL(1)?
**A:**
1. Initialize stack with `$` and start symbol
2. Repeat: Let X = top of stack, a = current input
   - If X = a = $, **accept**
   - If X = a ≠ $, pop X and advance input
   - If X is a non-terminal, look up M[X, a]:
     - If entry exists (X → Y₁Y₂...Yₖ), pop X, push Yₖ...Y₂Y₁ (reverse order)
     - If entry is empty, **error**

### Q6. What are the limitations of LL(1) parsing?
**A:**
- Cannot handle left-recursive grammars
- Cannot handle ambiguous grammars
- Limited to one lookahead symbol
- Not all context-free grammars can be converted to LL(1)

### Q7. What is a conflict in the parsing table?
**A:** A conflict occurs when a cell M[A, a] has more than one production. This means the grammar is **not LL(1)**. Types: FIRST-FIRST conflict (overlapping FIRST sets) and FIRST-FOLLOW conflict.

### Q8. What is the difference between LL(1) and LR(1)?
**A:**
| LL(1) | LR(1) |
|-------|-------|
| Top-down parsing | Bottom-up parsing |
| Leftmost derivation | Rightmost derivation (reverse) |
| Uses predictive table | Uses shift-reduce table |
| Less powerful | More powerful |
| Can't handle left recursion | Can handle left recursion |

### Q9. What is the role of the stack in LL(1) parsing?
**A:** The stack holds the expected symbols (terminals and non-terminals) that the parser predicts will match the remaining input. It essentially tracks the current state of the leftmost derivation.

### Q10. What is a predictive parser?
**A:** A predictive parser is a special case of recursive descent parser with no backtracking. It uses a lookahead symbol to predict which production to apply. LL(1) parsers are predictive parsers.

---

## 8. Three Address Code (TAC)

### Q1. What is Three Address Code?
**A:** TAC is an intermediate code representation where each instruction has **at most three addresses** (two operands and one result). General form: `x = y op z`. It bridges the gap between source code and machine code.

### Q2. What are the types of TAC statements?
**A:**
- **Assignment:** `x = y op z`, `x = op y`, `x = y`
- **Copy:** `x = y`
- **Conditional jump:** `if x relop y goto L`
- **Unconditional jump:** `goto L`
- **Indexed assignment:** `x = y[i]`, `x[i] = y`
- **Procedure call:** `param x`, `call p, n`, `return y`

### Q3. What are the different representations of TAC?
**A:**
1. **Quadruples:** (operator, arg1, arg2, result) — four fields per instruction
2. **Triples:** (operator, arg1, arg2) — result is referenced by position number
3. **Indirect Triples:** A list of pointers to triples — allows easy reordering

### Q4. What is the difference between quadruples and triples?
**A:**
| Quadruples | Triples |
|---|---|
| Explicit result field | Result = position number |
| Easy to rearrange code | Rearranging is difficult |
| More space (4 fields) | Less space (3 fields) |
| Temporary variables are explicit | Temporaries are implicit |

### Q5. Convert `a = b * c + d - e` to TAC.
**A:**
```
t1 = b * c
t2 = t1 + d
t3 = t2 - e
a = t3
```

### Q6. What are temporary variables in TAC?
**A:** Compiler-generated variables (t1, t2, t3...) used to hold intermediate results of sub-expressions. They are created by the compiler during TAC generation and don't exist in the original source code.

### Q7. Why is TAC used as intermediate representation?
**A:**
- Close to machine code but machine-independent
- Easy to optimize (constant folding, dead code elimination)
- Easy to translate to target machine code
- Simplifies the compiler into front-end and back-end

### Q8. How do you generate TAC for expressions with parentheses?
**A:** Parentheses affect the order of evaluation. Subexpressions inside parentheses are evaluated first and stored in temporaries. E.g., `a = (b + c) * d` → `t1 = b + c`, `t2 = t1 * d`, `a = t2`.

### Q9. How do you handle function calls in TAC?
**A:** Using `param` to push arguments, `call` to invoke the function, and `return` for the result:
```
param a
param b
call func, 2
t1 = return_value
```

### Q10. What is a basic block?
**A:** A sequence of consecutive TAC statements where control enters at the beginning and leaves at the end with no jumps or jump targets in the middle (except at the end). It's the unit of optimization.

---

## 9. Code Optimization

### Q1. What is code optimization?
**A:** Code optimization is the process of transforming code to make it run **faster** or use **less memory** without changing its output/behavior. It is applied to intermediate code or target code.

### Q2. What are the types of optimization?
**A:**
- **Machine-independent optimization:** Applied on intermediate code (TAC). E.g., constant folding, dead code elimination.
- **Machine-dependent optimization:** Applied on target/machine code. E.g., register allocation, instruction scheduling.

### Q3. What is constant folding?
**A:** Evaluating constant expressions at compile time instead of runtime. E.g., `x = 2 + 3` → `x = 5`. This eliminates unnecessary runtime computation.

### Q4. What is constant propagation?
**A:** Replacing variables with their constant values when possible. E.g., if `x = 5` and later `y = x + 3`, replace with `y = 5 + 3` → `y = 8`.

### Q5. What is dead code elimination?
**A:** Removing code that computes results that are **never used** or code that is **unreachable**. E.g., after `return`, any code is dead. If variable `x` is assigned but never read, the assignment is dead.

### Q6. What is common sub-expression elimination?
**A:** If an expression is computed more than once and its operands haven't changed, compute it only once and reuse the result. E.g.:
```
t1 = a + b        t1 = a + b
t2 = a + b    →   t2 = t1
```

### Q7. What is loop optimization?
**A:** Techniques to speed up loops:
- **Code motion:** Move loop-invariant computations outside the loop
- **Strength reduction:** Replace expensive operations with cheaper ones (e.g., `x * 2` → `x + x` or `x << 1`)
- **Loop unrolling:** Duplicate loop body to reduce loop control overhead

### Q8. What is strength reduction? Give an example.
**A:** Replacing expensive operations with equivalent cheaper ones.
- `x * 2` → `x << 1` (shift instead of multiply)
- `x * 4` → `x << 2`
- `x ^ 2` → `x * x`

### Q9. What is the difference between local and global optimization?
**A:**
- **Local (peephole):** Applied within a single basic block. E.g., redundant instruction elimination.
- **Global:** Applied across multiple basic blocks. E.g., global common sub-expression elimination, loop optimization.

### Q10. What is peephole optimization?
**A:** A technique that examines a small window (peephole) of instructions and replaces them with a better sequence. Examples: removing redundant loads/stores, simplifying algebraic operations, eliminating unreachable code.

### Q11. What is copy propagation?
**A:** After a copy statement `x = y`, replace subsequent uses of `x` with `y` (assuming x is not reassigned). This can enable further dead code elimination of the copy statement itself.

### Q12. Does optimization always improve performance?
**A:** Usually yes, but not always. Some optimizations may increase code size (loop unrolling), and excessive optimization can increase compile time. The goal is a balance between compile time and runtime performance.

---

## 10. Symbol Table

### Q1. What is a symbol table?
**A:** A data structure used by the compiler to store information about identifiers (variables, functions, classes) in the source program. It stores the **name, type, size, scope**, and other attributes.

### Q2. What information does a symbol table store?
**A:**
- Variable name
- Data type (int, float, char, etc.)
- Size (bytes occupied)
- Scope/block level
- Memory address/offset
- Line number of declaration
- For functions: parameter list, return type

### Q3. What data structures can be used for a symbol table?
**A:**
- **Linear list (array):** Simple but O(n) search — slow
- **Hash table:** O(1) average search — most commonly used
- **Binary search tree:** O(log n) search
- **Linked list:** Easy insertion, O(n) search

### Q4. When is the symbol table used during compilation?
**A:** It is used in **every phase**:
- Lexical analysis: enters identifiers
- Syntax analysis: uses type info for checking
- Semantic analysis: type checking, scope resolution
- Code generation: uses addresses and sizes
- Optimization: uses liveness and alias information

### Q5. What is scope and how does the symbol table handle it?
**A:** Scope defines the region of a program where an identifier is valid. The symbol table handles scope using:
- **Separate tables per scope** with pointers between them
- **A single table with scope level field** for each entry
- **Stack-based approach:** push entries on block entry, pop on exit

### Q6. What operations are performed on a symbol table?
**A:**
- **Insert:** Add a new identifier
- **Lookup:** Search for an identifier
- **Delete:** Remove identifiers (when scope ends)
- **Modify:** Update attributes (e.g., after type inference)

### Q7. How did you implement the symbol table in your program?
**A:** Used a dictionary/hash map where the key is the variable name, and the value is an object/tuple containing type and size. We parse the source code line by line, identify declarations, and populate the table.

### Q8. How do you determine the size of a variable?
**A:** Based on its data type:
| Type | Size (typical in C) |
|------|-----------|
| int | 4 bytes |
| float | 4 bytes |
| double | 8 bytes |
| char | 1 byte |
| pointer | 4 or 8 bytes |

### Q9. What is the difference between a symbol table and a literal table?
**A:**
- **Symbol table:** Stores identifiers (variables, functions)
- **Literal table:** Stores constant values (literals) like string constants and numeric constants used in the program

### Q10. How do you handle duplicate variable declarations?
**A:** Before inserting, perform a lookup. If the variable already exists in the **current scope**, report a "duplicate declaration" error. If it exists in an outer scope, the new declaration **shadows** the outer one.
