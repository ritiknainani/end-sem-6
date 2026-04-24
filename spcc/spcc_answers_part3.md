# 📝 SPCC Complete Answer Guide — Part 3 (TIER 4 & 5 Topics)

---

## 20. 📌 TYPES OF ASSEMBLY LANGUAGE STATEMENTS [10 Marks] — 🟢 MODERATE

> **Asked:** ~May'23, Nov'23

### Answer:

Assembly language statements are classified into **three types**:

```
Assembly Language Statements
├── 1. Imperative Statements       (Machine Instructions)
├── 2. Declarative Statements      (Data Definition)
└── 3. Assembler Directives        (Pseudo-opcodes / Assembly Control)
```

### 1. Imperative Statements (Machine/Executable Instructions)

These are **translated into machine code** by the assembler. They specify operations to be performed by the CPU.

**Format:** `[Label] Opcode Operand1 [, Operand2]`

**Examples:**

| Statement | Description |
|-----------|-------------|
| `MOVER AREG, X` | Move value of X into register A |
| `ADD BREG, Y` | Add value of Y to register B |
| `MOVEM CREG, Z` | Move register C value to memory location Z |
| `COMP AREG, X` | Compare register A with X |
| `BC GT, LOOP` | Branch to LOOP if Greater Than |
| `READ X` | Read input into X |
| `PRINT Y` | Print value of Y |
| `STOP` | Halt execution |

**Categories:**
- **Data Transfer:** MOVER, MOVEM
- **Arithmetic:** ADD, SUB, MULT, DIV
- **Comparison:** COMP
- **Branch:** BC (Branch on Condition)
- **I/O:** READ, PRINT
- **Control:** STOP

### 2. Declarative Statements (Data Definition)

These **reserve memory** and optionally initialize data. They do NOT generate executable instructions.

| Statement | Syntax | Purpose | Example |
|-----------|--------|---------|---------|
| **DS** (Declare Storage) | `[Label] DS <size>` | Reserve memory without initialization | `A DS 1` → reserves 1 word for A |
| **DC** (Declare Constant) | `[Label] DC '<value>'` | Reserve memory and initialize | `B DC '5'` → reserves 1 word, stores 5 |

**Example:**
```
X    DS   3       ← Reserves 3 consecutive words for array X
Y    DC   '10'    ← Reserves 1 word, initializes to 10
MSG  DC   'HELLO' ← Stores string constant
```

### 3. Assembler Directives (Pseudo-opcodes)

These **instruct the assembler** on how to perform the assembly process. They do NOT generate machine code directly.

| Directive | Purpose | Example |
|-----------|---------|---------|
| **START** | Specify starting address of program | `START 100` |
| **END** | Mark end of source program | `END` |
| **ORIGIN** | Set Location Counter to specified value | `ORIGIN 200` |
| **EQU** | Define symbolic constant (assign value to symbol) | `MAX EQU 100` |
| **LTORG** | Assign addresses to accumulated literals (create literal pool) | `LTORG` |
| **USING** | Specify base register | `USING 15` |

**LTORG Example:**
```
START 100
MOVER AREG, ='5'      ← Literal ='5'
ADD AREG, ='10'        ← Literal ='10'
LTORG                   ← Allocates literals here
                        ← ='5' gets address, ='10' gets next address
MOVER BREG, ='20'     ← New literal ='20'
STOP
END                    ← ='20' allocated at end
```

---

## 21. 📌 DYNAMIC LINKING LOADER [10 Marks] — 🔵 LOW

> **Asked:** Nov'23

### Answer:

A **Dynamic Linking Loader** postpones the linking of external modules until **execution time** (runtime). Modules are loaded and linked **only when they are actually called**.

### Key Concept:
- External references are **NOT resolved** at load time
- When a subroutine is called for the first time:
  - The loader is invoked to **find, load, and link** that module
  - Subsequent calls use the already-loaded version

### Advantages:
1. **Memory Efficiency**: Only loads modules that are actually used
2. **Shared Libraries**: Multiple programs can share the same module in memory (DLLs/.so files)
3. **Easy Updates**: Update a library without recompiling all programs
4. **Faster Loading**: Initial program load is faster (less to load)
5. **Reduced Disk Space**: Common routines stored only once

### Disadvantages:
1. **Runtime Overhead**: First call to a module incurs loading delay
2. **Complexity**: More complex implementation
3. **Dependency Issues**: Missing/incompatible libraries at runtime
4. **Version Conflicts**: "DLL Hell" — wrong version loaded

### Working Mechanism:

```
┌──────────────────────────────────────────────────────────┐
│                    MAIN PROGRAM                          │
│                                                          │
│    ... code ...                                          │
│    CALL SUB_A  ──────┐                                   │
│    ... code ...       │                                   │
│    CALL SUB_B  ───┐   │                                   │
│    ... code ...   │   │                                   │
└───────────────────┼───┼──────────────────────────────────┘
                    │   │
                    │   │  First call triggers:
                    │   │  1. Interrupt/trap to loader
                    │   │  2. Loader finds SUB_A on disk
                    │   │  3. Loads SUB_A into memory
                    │   │  4. Links (resolves references)
                    │   │  5. Transfers control to SUB_A
                    │   │  6. Updates call to direct jump
                    │   │     (future calls skip loader)
                    │   │
                    │   ▼
                    │  ┌──────────┐
                    │  │  SUB_A   │ (loaded on demand)
                    │  └──────────┘
                    │
                    ▼
                   ┌──────────┐
                   │  SUB_B   │ (loaded on demand)
                   └──────────┘
```

### Implementation Using Load-on-Call (Dynamic Loading):

1. External references contain a **stub** (small piece of code)
2. When the stub is executed for the first time:
   - It calls the **Dynamic Loader**
   - Loader loads the required module into available memory
   - Loader links the module (resolves addresses)
   - Loader replaces the stub with a direct call/jump to the loaded module
3. Subsequent calls go directly to the loaded module (no loader overhead)

### Comparison with Direct Linking Loader:

| Feature | Direct Linking Loader | Dynamic Linking Loader |
|---------|----------------------|----------------------|
| When linking occurs | Load time | Run time |
| All modules loaded? | Yes, all at once | Only when needed |
| Memory usage | Higher | Lower |
| Initial load time | Slower | Faster |
| First-call overhead | None | Yes |
| Library sharing | Separate copies | Shared in memory |
| Complexity | Moderate | High |

---

## 22. 📌 ABSOLUTE LOADER [5 Marks] — 🔵 LOW

> **Asked:** ~May'23

### Answer:

An **Absolute Loader** loads the object program at the **exact memory address** specified in the object code. It is the simplest type of loader.

### Working:
1. Read Header record → verify program name and length
2. Read Text records → load object code at specified absolute addresses
3. Read End record → transfer control to the execution start address

### Algorithm:
```
1. Read Header record
2. Verify program name and length
3. While not End record:
   a. Read next Text record
   b. Move object code to memory address specified in record
4. Read End record
5. Jump to address specified in End record
```

```
┌────────────────────┐
│ Read Header Record │
└────────┬───────────┘
         │
         ▼
┌────────────────────┐     ┌──────────────────────┐
│ Read Next Record   │────►│ Is it END record?    │
└────────────────────┘     └──────────┬───────────┘
         ▲                      YES   │   NO
         │                      │     │
         │              ┌───────▼──┐  │
         │              │  Jump to │  │
         │              │  exec    │  │
         │              │  address │  │
         │              └──────────┘  │
         │                            ▼
         │              ┌──────────────────────┐
         │              │ Load object code at  │
         └──────────────│ specified address    │
                        └──────────────────────┘
```

### Advantages:
1. Simple to implement
2. Fast loading (no relocation needed)
3. No linking overhead

### Disadvantages:
1. **No relocation** — program must always load at fixed address
2. **No linking** — cannot combine separately assembled modules
3. **Memory conflicts** — if specified address is occupied, cannot load
4. Programmer must manage memory addresses manually
5. Not suitable for multiprogramming

---

## 23. 📌 RELOCATION IN LOADERS [10 Marks] — 🔵 LOW-MODERATE (NEW TREND ⬆️)

> **Asked:** Jan'25

### Answer:

**Relocation** is the process of adjusting address-dependent locations in an object program to correspond to the actual load address in memory.

### Why Relocation is Needed:
- Programs are assembled assuming a **starting address** (e.g., 0 or 100)
- At load time, the program may be placed at a **different address**
- All address references must be adjusted by the **relocation factor**
  - **Relocation Factor** = Actual Load Address − Assumed Start Address

### Example:
```
Assembled at address 0:
    JUMP 1024        ← absolute address reference

Loaded at address 5000:
    Relocation factor = 5000 - 0 = 5000
    JUMP 1024 → adjusted to JUMP 6024
```

### Methods of Handling Relocation:

#### Method 1: Relocation Bit Mask (BSS Loader)

- Each word of object code has an associated **relocation bit**
- Bit = 1 → address is relocatable (add relocation factor)
- Bit = 0 → address is absolute (no change)

```
Object Code:
Address | Code    | Reloc Bit
   0    | LOAD 50 |    1      ← relocatable → LOAD (50 + RF)
   1    | ADD  #5 |    0      ← absolute (immediate) → no change
   2    | JUMP 10 |    1      ← relocatable → JUMP (10 + RF)
```

**Advantages:** Simple, efficient for simple programs
**Disadvantages:** Only handles single control section, limited

#### Method 2: Modification Records (Direct Linking Loader)

- Object file contains **Modification (M) records** that list which addresses need relocation
- Each M record specifies: start address, length to modify, and the symbol to add/subtract

```
M Record Format: M | Address | Length | ±Symbol

Example:
M | 000004 | 05 | +PROGA    ← At address 4, add the start address of PROGA
M | 000010 | 05 | +EXTREF   ← At address 10, add address of external symbol
```

**How it works:**
1. During Pass 2 of the loader:
   - Read each M record
   - Look up the symbol in ESTAB (External Symbol Table)
   - Add or subtract the symbol's address to/from the specified location

```
Before relocation (assembled at 0):
   Addr 4: [0x00000000]     ← needs PROGA's load address added

After relocation (PROGA loaded at 0x4000):
   Addr 4: [0x00004000]     ← adjusted!
```

**Advantages:** Handles multiple control sections, supports linking
**Disadvantages:** More complex, larger object files

#### Method 3: Base Register Approach (Hardware-Assisted)

- Use a **base register** that holds the load address
- All addresses are computed as: **Base Register + Displacement**
- No relocation needed at load time — hardware handles it!

```
Base Register (BR) = Load Address = 5000

Instruction: LOAD [BR + 50]    ← effective address = 5050
             JUMP [BR + 10]    ← effective address = 5010
```

**Advantages:** No modification at load time, very fast
**Disadvantages:** Limited range (displacement field size), needs hardware support

#### Method 4: Relocation Table

- Assembler generates a **relocation table** listing all relocatable addresses
- Loader reads the table and adjusts each listed address

```
Relocation Table:
┌──────────────┬─────────────┐
│ Address      │ Type        │
├──────────────┼─────────────┤
│ 0004         │ Relocatable │
│ 0012         │ Relocatable │
│ 0020         │ Relocatable │
└──────────────┴─────────────┘
```

### Summary of Methods:

| Method | When Used | Complexity | Flexibility |
|--------|----------|------------|-------------|
| Relocation Bit | Simple relocating loaders | Low | Low |
| Modification Records | Direct Linking Loader | Medium | High |
| Base Register | Hardware-assisted | Low (at load) | Medium |
| Relocation Table | General purpose | Medium | Medium |

---

## 24. 📌 TOKENS, LEXEMES, AND PATTERNS [5 Marks] — 🔵 LOW-MODERATE

> **Asked:** Jan'25

### Answer:

These are fundamental concepts of **Lexical Analysis** (Phase 1 of compilation).

### Definitions:

| Concept | Definition | Example |
|---------|-----------|---------|
| **Token** | A classification/category of lexical unit. It is a ⟨token-name, attribute-value⟩ pair | `identifier`, `keyword`, `number`, `operator` |
| **Lexeme** | The actual character sequence in the source code that matches a token pattern | `count`, `int`, `42`, `+` |
| **Pattern** | A rule (often a regex) that describes the set of strings forming a token | `[a-zA-Z_][a-zA-Z0-9_]*` for identifiers |

### Relationship:

```
Source Code:  int count = 42 + x;

Token         Lexeme      Pattern
─────         ──────      ───────
keyword       "int"       int (exact match)
identifier    "count"     letter(letter|digit)*
operator      "="         = (exact match)
number        "42"        digit digit*
operator      "+"         + (exact match)
identifier    "x"         letter(letter|digit)*
separator     ";"         ; (exact match)
```

### Detailed Explanation:

**1. Token:**
- Abstract symbol representing a class of strings
- The parser works with tokens (not actual characters)
- Token types include:
  - **Keywords**: `if`, `else`, `while`, `int`, `return`
  - **Identifiers**: variable names, function names
  - **Constants/Literals**: integers, floats, strings, characters
  - **Operators**: `+`, `-`, `*`, `/`, `=`, `==`, `!=`
  - **Separators/Punctuation**: `;`, `(`, `)`, `{`, `}`, `,`
  - **Special symbols**: `#`, `@`

**2. Lexeme:**
- The actual substring of source code
- One token type can have many lexemes:
  - Token `identifier` → lexemes: `count`, `sum`, `total`, `i`, `temp`
  - Token `keyword` → lexemes: `int`, `float`, `if`, `while`
  - Token `number` → lexemes: `42`, `100`, `3`, `999`

**3. Pattern:**
- Formal description (usually regular expression) for recognizing lexemes
- Examples:

| Token | Pattern (Regex) |
|-------|----------------|
| identifier | `[a-zA-Z_][a-zA-Z0-9_]*` |
| integer | `[0-9]+` |
| float | `[0-9]+\.[0-9]+` |
| relop | `< | > | <= | >= | == | !=` |
| keyword_if | `if` (literal) |

---

## 25. 📌 COMPILER vs INTERPRETER [5 Marks] — 🔵 LOW

> **Asked:** ~May'23

### Answer:

| Feature | Compiler | Interpreter |
|---------|----------|-------------|
| **Definition** | Translates entire program into machine code at once before execution | Translates and executes program line by line |
| **Translation** | Full program translated first | One statement at a time |
| **Output** | Object code / executable file | No separate output file |
| **Execution Speed** | Faster (pre-compiled) | Slower (translate each time) |
| **Error Detection** | All errors shown after compilation | Stops at first error |
| **Memory** | Needs more memory (stores object code) | Less memory |
| **Debugging** | Harder (need recompilation) | Easier (line by line) |
| **Development Cycle** | Slower (compile → run → debug) | Faster (run immediately) |
| **Re-execution** | No re-translation needed | Re-translates every time |
| **Examples** | C, C++, Java (javac) | Python, Ruby, JavaScript |
| **Intermediate Code** | Generated and stored | May not be stored |
| **Portability** | Less (machine-specific output) | More (source interpreted) |

```
COMPILER:                          INTERPRETER:
┌────────────┐                     ┌────────────┐
│Source Code  │                     │Source Code  │
└─────┬──────┘                     └─────┬──────┘
      │                                  │
      ▼                                  ▼
┌────────────┐                     ┌─────────────────┐
│  COMPILER  │                     │  INTERPRETER    │
│ (One time) │                     │  (Line by Line) │
└─────┬──────┘                     └─────┬───────────┘
      │                                  │
      ▼                                  ▼
┌────────────┐                     ┌────────────┐
│Object Code │                     │  Output    │
│(Executable)│                     │ (Direct)   │
└─────┬──────┘                     └────────────┘
      │
      ▼ (Run anytime)
┌────────────┐
│  Output    │
└────────────┘
```

---

## 26. 📌 TOP-DOWN vs BOTTOM-UP PARSER [5 Marks] — 🔵 LOW

> **Asked:** Dec'22

### Answer:

| Feature | Top-Down Parser | Bottom-Up Parser |
|---------|----------------|-----------------|
| **Approach** | Starts from **Start Symbol**, derives input string | Starts from **input string**, reduces to Start Symbol |
| **Direction** | Root to leaves (of parse tree) | Leaves to root |
| **Derivation** | **Leftmost** derivation | **Rightmost** derivation (in reverse) |
| **Also Called** | Predictive parser | Shift-Reduce parser |
| **Technique** | Expansion of non-terminals | Reduction of strings |
| **Data Structure** | Stack (with recursive descent or table) | Stack + Input buffer |
| **Grammar** | Cannot handle left recursion | Can handle left recursion |
| **Types** | Recursive Descent, LL(1), Predictive | LR(0), SLR(1), CLR(1), LALR(1), Operator Precedence |
| **Power** | Less powerful | More powerful |
| **Error Detection** | Detects early | May detect late |
| **Backtracking** | May need backtracking | No backtracking (in LR) |
| **Implementation** | Simpler | Complex |
| **Tools** | Hand-coded often | YACC, Bison (auto-generated) |

```
TOP-DOWN:                          BOTTOM-UP:
    S (Start)                          S (Goal)
   / \                                / \
  A   B          BUILD               A   B          BUILD
 / \   \        DOWNWARD            / \   \        UPWARD
a   b   c     ───────────►        a   b   c     ◄───────────
(Input String)                    (Input String)
```

---

## 27. 📌 SYNTAX-DIRECTED TRANSLATION (SDT) [10 Marks] — 🔵 LOW

> **Asked:** ~May'23 (short note)

### Answer:

**Syntax-Directed Translation (SDT)** is a method of attaching **semantic rules** (actions) to grammar productions to perform translation during parsing.

### Key Concepts:

**1. Attributes:**
- Values associated with grammar symbols (terminals & non-terminals)
- Contain semantic information (type, value, code, etc.)

**2. Types of Attributes:**

| Type | Direction | Computation | Example |
|------|-----------|-------------|---------|
| **Synthesized Attribute** | Bottom-up (child → parent) | Computed from children's attributes | Value of expression |
| **Inherited Attribute** | Top-down (parent/sibling → child) | Computed from parent or sibling attributes | Type info passed down |

**3. Syntax-Directed Definition (SDD):**
- Grammar + semantic rules attached to productions
- Each rule defines how to compute attributes

### Example: Desk Calculator

**Grammar with Semantic Rules:**

| Production | Semantic Rule |
|-----------|---------------|
| E → E₁ + T | E.val = E₁.val + T.val |
| E → T | E.val = T.val |
| T → T₁ * F | T.val = T₁.val * F.val |
| T → F | T.val = F.val |
| F → (E) | F.val = E.val |
| F → digit | F.val = digit.lexval |

**For input `3 * 5 + 2`:**

```
              E.val = 17
             / \    \
       E.val=15  +   T.val=2
           |             |
       T.val=15      F.val=2
        / \  \           |
  T.val=3  *  F.val=5   2
      |           |
  F.val=3         5
      |
      3
```

### Annotated Parse Tree:
- Parse tree with attribute values computed at each node
- Synthesized attributes flow UP
- Inherited attributes flow DOWN

### S-Attributed vs L-Attributed:

| S-Attributed Definition | L-Attributed Definition |
|------------------------|------------------------|
| Uses **only synthesized** attributes | Uses synthesized + restricted inherited attributes |
| Evaluated in **bottom-up** order | Evaluated in **left-to-right, depth-first** order |
| Can be evaluated during LR parsing | Can be evaluated during LL parsing |
| Simpler | More flexible |

---

## 28. 📌 PREDICTIVE PARSER [10 Marks] — 🔵 LOW-MODERATE

> **Asked:** Jan'25

### Answer:

A **Predictive Parser** is a **recursive descent parser** that does NOT require backtracking. It uses a **parsing table** (LL(1) table) to decide which production to apply based on the current input symbol.

### Types:
1. **Recursive Predictive Parser**: Uses recursive function calls
2. **Non-Recursive (Table-Driven) Predictive Parser**: Uses an explicit stack + parsing table

### Non-Recursive Predictive Parser Structure:

```
┌────────────┐     ┌─────────────────┐     ┌───────────────┐
│   Input    │────►│  Predictive     │◄───►│  Parsing      │
│   Buffer   │     │  Parsing        │     │  Table M      │
│ a + b $ ...│     │  Program        │     │  [A,a] → prod │
└────────────┘     └────────┬────────┘     └───────────────┘
                            │
                    ┌───────▼────────┐
                    │     Stack      │
                    │  ┌───┐         │
                    │  │ $ │ bottom  │
                    │  │ S │ start   │
                    │  └───┘         │
                    └────────────────┘
                            │
                            ▼
                       Output
```

### Algorithm:

```
1. Push $ and Start Symbol S onto stack
2. Set input pointer (ip) to first symbol of input
3. Repeat:
   Let X = top of stack, a = current input symbol
   
   IF X == a (terminal match):
     Pop X from stack
     Advance ip to next input symbol
   
   ELSE IF X == $ and a == $:
     ACCEPT (parsing successful!)
   
   ELSE IF X is a non-terminal:
     Look up M[X, a] in parsing table
     IF M[X, a] = X → Y₁Y₂...Yₖ:
       Pop X from stack
       Push Yₖ, Yₖ₋₁, ..., Y₁ (right to left, so Y₁ is on top)
     ELSE:
       ERROR
   
   ELSE:
     ERROR
```

### Worked Example:

**Grammar (after left-factoring & removing left recursion):**
```
E  → T Q
T  → F R
Q  → + T Q | - T Q | ε
R  → * F R | / F R | ε
F  → ( E ) | id
```

**Step 1: Compute FIRST sets:**
- FIRST(F) = {(, id}
- FIRST(R) = {*, /, ε}
- FIRST(T) = FIRST(F) = {(, id}
- FIRST(Q) = {+, -, ε}
- FIRST(E) = FIRST(T) = {(, id}

**Step 2: Compute FOLLOW sets:**
- FOLLOW(E) = {$, )}
- FOLLOW(Q) = FOLLOW(E) = {$, )}
- FOLLOW(T) = FIRST(Q)−{ε} ∪ FOLLOW(E) ∪ FOLLOW(Q) = {+, -, $, )}
- FOLLOW(R) = FOLLOW(T) = {+, -, $, )}
- FOLLOW(F) = FIRST(R)−{ε} ∪ FOLLOW(T) ∪ FOLLOW(R) = {*, /, +, -, $, )}

**Step 3: Build Parsing Table:**

| | id | + | - | * | / | ( | ) | $ |
|---|---|---|---|---|---|---|---|---|
| **E** | E→TQ | | | | | E→TQ | | |
| **Q** | | Q→+TQ | Q→-TQ | | | | Q→ε | Q→ε |
| **T** | T→FR | | | | | T→FR | | |
| **R** | | R→ε | R→ε | R→*FR | R→/FR | | R→ε | R→ε |
| **F** | F→id | | | | | F→(E) | | |

**Step 4: Parse `id + id * id`:**

| Stack | Input | Action |
|-------|-------|--------|
| $ E | id + id * id $ | E → TQ |
| $ Q T | id + id * id $ | T → FR |
| $ Q R F | id + id * id $ | F → id |
| $ Q R **id** | **id** + id * id $ | Match id |
| $ Q R | + id * id $ | R → ε |
| $ Q | + id * id $ | Q → +TQ |
| $ Q T **+** | **+** id * id $ | Match + |
| $ Q T | id * id $ | T → FR |
| $ Q R F | id * id $ | F → id |
| $ Q R **id** | **id** * id $ | Match id |
| $ Q R | * id $ | R → *FR |
| $ Q R F **\*** | **\*** id $ | Match * |
| $ Q R F | id $ | F → id |
| $ Q R **id** | **id** $ | Match id |
| $ Q R | $ | R → ε |
| $ Q | $ | Q → ε |
| $ | $ | **ACCEPT** ✅ |

---

## 29. 📌 LOADING AND LINKING PROCESS [5 Marks] — 🔵 LOW

> **Asked:** Jan'25

### Answer:

**Loading** and **Linking** are processes that prepare a program for execution after compilation/assembly.

### Process Flow:

```
┌──────────────┐
│  Source Code  │
│  (.asm/.c)   │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│  Assembler/  │
│  Compiler    │
└──────┬───────┘
       │ Object Module (.obj)
       ▼
┌──────────────┐     ┌──────────────┐
│    LINKER    │◄────│  Library     │
│              │     │  Routines    │
└──────┬───────┘     └──────────────┘
       │ Executable / Load Module
       ▼
┌──────────────┐
│    LOADER    │
│  ┌────────┐  │
│  │Allocate│  │→ Reserve memory
│  │Relocate│  │→ Adjust addresses
│  │ Load   │  │→ Place code in memory
│  │Execute │  │→ Start execution
│  └────────┘  │
└──────────────┘
       │
       ▼
┌──────────────┐
│  EXECUTION   │
│  in Memory   │
└──────────────┘
```

### Linking:
- Combines **multiple object modules** into a single executable
- Resolves **external references** between modules
- Performed by the **Linker**
- Types:
  - **Static Linking**: All modules combined before loading
  - **Dynamic Linking**: Modules linked at runtime

### Loading:
- Places the executable program into **main memory**
- Performs the 4 functions: **Allocation, Linking, Relocation, Loading**
- Types: Absolute Loader, Relocating Loader, Direct Linking Loader

---

## 30. 📌 SEQUENCE OF SYSTEM PROGRAMS (Source → Execution) [5 Marks] — 🔵 LOW

> **Asked:** Jan'25

### Answer:

The following system programs are involved in the process from writing source code to executing it:

```
┌──────────────────────────────────────────────────────────────┐
│  1. EDITOR / IDE                                             │
│     - Used to write/modify source code                       │
│     - Output: Source Program (.c, .asm, etc.)                │
└───────────────────────────┬──────────────────────────────────┘
                            │
                            ▼
┌──────────────────────────────────────────────────────────────┐
│  2. PREPROCESSOR                                             │
│     - Handles #include, #define, macros                      │
│     - Output: Expanded Source Code                           │
└───────────────────────────┬──────────────────────────────────┘
                            │
                            ▼
┌──────────────────────────────────────────────────────────────┐
│  3. COMPILER / ASSEMBLER                                     │
│     - Compiler: HLL → Assembly / Object code                 │
│     - Assembler: Assembly → Object code (machine code)       │
│     - Output: Object Module (.obj / .o)                      │
└───────────────────────────┬──────────────────────────────────┘
                            │
                            ▼
┌──────────────────────────────────────────────────────────────┐
│  4. LINKER                                                   │
│     - Combines multiple object modules                       │
│     - Resolves external references                           │
│     - Links library routines                                 │
│     - Output: Executable / Load Module (.exe)                │
└───────────────────────────┬──────────────────────────────────┘
                            │
                            ▼
┌──────────────────────────────────────────────────────────────┐
│  5. LOADER                                                   │
│     - Allocates memory                                       │
│     - Relocates addresses                                    │
│     - Loads program into main memory                         │
│     - Transfers control to start address                     │
└───────────────────────────┬──────────────────────────────────┘
                            │
                            ▼
┌──────────────────────────────────────────────────────────────┐
│  6. EXECUTION                                                │
│     - CPU fetches and executes instructions                  │
│     - OS manages resources, I/O, interrupts                  │
│     - Output: Program results                                │
└──────────────────────────────────────────────────────────────┘
```

### Summary Table:

| # | System Program | Input | Output |
|---|----------------|-------|--------|
| 1 | Editor | User keystrokes | Source code |
| 2 | Preprocessor | Source code | Expanded source |
| 3 | Compiler | HLL source | Assembly code |
| 4 | Assembler | Assembly code | Object module |
| 5 | Linker | Object module(s) + libraries | Executable |
| 6 | Loader | Executable | Program in memory |

---

## 31. 📌 DATABASES IN DIRECT LINKING LOADER [10 Marks] — 🟡 Supporting

> **Asked:** Nov'23 (specifically asked about databases)

### Answer:

| # | Database | Full Form | Description |
|---|----------|-----------|-------------|
| 1 | **ESTAB** | External Symbol Table | Stores all external symbols (control section names + symbols defined in D records) with their assigned load addresses. Used during both passes. |
| 2 | **CSADDR** | Control Section Address | Holds the starting address of the current control section being processed. Updated after processing each section. |
| 3 | **CSLTH** | Control Section Length | Length of the current control section (from H record). Used to calculate next CSADDR. |
| 4 | **PROGADDR** | Program Load Address | The address in memory where the entire linked program starts. Assigned by OS. |
| 5 | **EXECADDR** | Execution Start Address | The address where execution should begin (from E record). Defaults to beginning of first control section. |
| 6 | **LOCCTR** | Location Counter | Tracks current position during loading. |

### ESTAB Structure:

| Control Section | Symbol Name | Address | Length |
|----------------|-------------|---------|--------|
| PROGA | PROGA | 4000 | 0070 |
| PROGA | LISTA | 4040 | — |
| PROGA | ENDA | 4054 | — |
| PROGB | PROGB | 4070 | 0088 |
| PROGB | LISTB | 40C4 | — |
| PROGB | ENDB | 40D8 | — |
| PROGC | PROGC | 40F8 | 0057 |
| PROGC | LISTC | 4112 | — |
| PROGC | ENDC | 4124 | — |

### How ESTAB is Built (Pass 1):
```
For each control section:
  1. Read H record → CS name, start addr, length
  2. ESTAB[CS_name] = CSADDR
  3. Read D records → For each symbol:
     ESTAB[symbol_name] = CSADDR + symbol's relative address
  4. CSADDR = CSADDR + CSLTH
```

### How ESTAB is Used (Pass 2):
```
For each M (Modification) record:
  1. Search symbol in ESTAB
  2. Get its absolute address
  3. Add/subtract to/from the specified location in memory
```
