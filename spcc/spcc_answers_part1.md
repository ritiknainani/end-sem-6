# 📝 SPCC Complete Answer Guide — Part 1 (TIER 1 & 2 Topics)

> **Strategy:** Every answer below is structured for maximum marks.
> Include diagrams wherever possible. Use headings, bullet points, and tables.

---

## 1. 📌 PHASES OF COMPILER [10 Marks] — 🔴 GUARANTEED

> **Asked:** Dec'22, May'23, Nov'23, Dec'24, Jan'25 — ALL 5 Papers

### Answer:

A compiler translates source code written in a high-level language into target machine code. The compilation process involves **6 phases** grouped into **2 stages**: Analysis (Front-end) and Synthesis (Back-end), along with two auxiliary modules.

### Block Diagram:

```
┌─────────────────────────────────────────────────────────┐
│                    Source Program                        │
└──────────────────────────┬──────────────────────────────┘
                           │
                           ▼
              ┌─────────────────────────┐
              │   1. Lexical Analyzer   │──────────┐
              │      (Scanner)          │          │
              └────────────┬────────────┘          │
                           │ Tokens                │
                           ▼                       │
              ┌─────────────────────────┐          │
              │   2. Syntax Analyzer    │          │
              │      (Parser)           │     ┌────┴────┐
              └────────────┬────────────┘     │ Symbol  │
                           │ Parse Tree       │  Table  │
                           ▼                  │ Manager │
              ┌─────────────────────────┐     └────┬────┘
              │  3. Semantic Analyzer   │          │
              └────────────┬────────────┘          │
                           │ Annotated Parse Tree  │
                           ▼                       │
              ┌─────────────────────────┐          │
              │ 4. Intermediate Code    │          │
              │    Generator            │     ┌────┴────┐
              └────────────┬────────────┘     │  Error  │
                           │ IC (e.g., 3AC)   │ Handler │
                           ▼                  └────┬────┘
              ┌─────────────────────────┐          │
              │   5. Code Optimizer     │          │
              └────────────┬────────────┘          │
                           │ Optimized IC          │
                           ▼                       │
              ┌─────────────────────────┐          │
              │   6. Code Generator     │──────────┘
              └────────────┬────────────┘
                           │
                           ▼
              ┌─────────────────────────┐
              │    Target Machine Code  │
              └─────────────────────────┘
```

### Example: Processing `a = b * c + 10`

**Phase 1: Lexical Analysis (Scanner)**
- Input: `a = b * c + 10`
- Breaks source code into **tokens** (smallest meaningful units)
- Output tokens:

| Token | Token Type |
|-------|-----------|
| a | Identifier (id1) |
| = | Assignment operator |
| b | Identifier (id2) |
| * | Multiplication operator |
| c | Identifier (id3) |
| + | Addition operator |
| 10 | Integer constant |

- Also creates entries in **Symbol Table**
- Removes whitespace and comments

**Phase 2: Syntax Analysis (Parser)**
- Checks grammatical structure using **CFG (Context Free Grammar)**
- Produces **Parse Tree / Syntax Tree**

```
         (=)
        /   \
      id1    (+)
            /   \
          (*)   10
         /   \
       id2   id3
```

**Phase 3: Semantic Analysis**
- **Type checking**: Ensures operations are type-compatible
- If `a, b, c` are `real` and `10` is `int`, it performs **type conversion**:
  - `inttoreal(10)` → converts 10 to 10.0
- Output: **Annotated Parse Tree**

```
         (=)
        /   \
      id1    (+)
            /   \
          (*)   inttoreal(10)
         /   \
       id2   id3
```

**Phase 4: Intermediate Code Generation**
- Generates **Three-Address Code** (platform independent):
```
t1 = id2 * id3
t2 = inttoreal(10)
t3 = t1 + t2
id1 = t3
```

**Phase 5: Code Optimization**
- Removes redundancies, improves efficiency:
```
t1 = id2 * id3
id1 = t1 + 10.0
```
- Eliminated temporary `t2`, `t3`; folded constant

**Phase 6: Code Generation**
- Generates **target machine code** (assembly):
```
MOV R1, id2
MUL R1, id3
ADD R1, #10.0
MOV id1, R1
```

### Two Auxiliary Modules:
1. **Symbol Table Manager**: Stores info about identifiers (name, type, scope, memory location). Used by all phases.
2. **Error Handler**: Detects and reports errors at each phase. Lexical errors, syntax errors, semantic errors, etc.

---

## 2. 📌 TWO PASS ASSEMBLER [10 Marks] — 🔴 GUARANTEED

> **Asked:** ALL 5 papers

### Answer:

An **assembler** translates assembly language programs into machine code. A **two-pass assembler** processes the source program **twice**.

### Why Two Passes?
- To resolve the **Forward Reference Problem** — when a symbol is used before it is defined, Pass-1 collects all symbol definitions, and Pass-2 uses them.

### Databases Used:

| Database | Purpose |
|----------|---------|
| **MOT** (Machine Opcode Table) | Stores mnemonic, opcode, instruction length, type |
| **POT** (Pseudo Opcode Table) | Stores pseudo-ops (START, END, DS, DC, EQU, LTORG) |
| **ST** (Symbol Table) | Stores symbol name, address, length |
| **LT** (Literal Table) | Stores literals and their addresses |
| **POOLTAB** (Pool Table) | Stores starting index of literals in each pool |
| **LC** (Location Counter) | Tracks memory address during assembly |
| **IC** (Intermediate Code) | Output of Pass-1, input to Pass-2 |

### PASS-1: Define Symbols & Assign Addresses

```
┌──────────────────────────────────┐
│          START                   │
│   Initialize LC to starting     │
│   address                       │
└───────────────┬──────────────────┘
                │
                ▼
┌──────────────────────────────────┐
│   Read next assembly statement   │◄──────────────── ─┐
└───────────────┬──────────────────┘                   │
                │                                      │
                ▼                                      │
        ┌───────────────┐                              │
        │  Is it END?   │── YES ──► Process literals   │
        └───────┬───────┘           in LITTAB, write   │
                │ NO                IC, ST, LT to file │
                ▼                   ► STOP             │
        ┌───────────────┐                              │
        │ Has a label?  │── YES ──► Enter label in     │
        └───────┬───────┘           Symbol Table       │
                │ NO                with LC value       │
                ▼                                      │
        ┌───────────────────────┐                      │
        │  Is it Imperative     │                      │
        │  (Machine Instruction)│                      │
        │  ?                    │                      │
        └───────┬───────────────┘                      │
                │ YES → Generate IC,                   │
                │        LC = LC + instruction length  │
                │ NO ↓                                 │
        ┌───────────────────────┐                      │
        │  Is it Declarative?   │                      │
        │  (DS / DC)            │                      │
        └───────┬───────────────┘                      │
                │ YES → Allocate memory,               │
                │        Update LC                     │
                │ NO ↓                                 │
        ┌───────────────────────┐                      │
        │  Is it Assembler      │                      │
        │  Directive?           │                      │
        │  (START/END/LTORG/    │                      │
        │   EQU/ORIGIN)         │                      │
        └───────┬───────────────┘                      │
                │ Process directive                    │
                │ (LTORG: assign addresses to          │
                │  pending literals)                   │
                └──────────────────────────────────────┘
```

### PASS-2: Generate Machine Code

```
┌──────────────────────────────────┐
│   Read Intermediate Code (IC)    │◄─────────────────┐
│   from Pass-1                    │                  │
└───────────────┬──────────────────┘                  │
                │                                     │
                ▼                                     │
        ┌───────────────┐                             │
        │  Is it END?   │── YES ──► Write machine     │
        └───────┬───────┘           code to output     │
                │ NO                file ► STOP        │
                ▼                                     │
        ┌────────────────────────┐                    │
        │ Is it Imperative?      │                    │
        └───────┬────────────────┘                    │
                │ YES:                                │
                │ - Look up opcode in MOT             │
                │ - Look up operand addresses         │
                │   from Symbol Table / Literal Table │
                │ - Assemble binary machine code      │
                │ NO ↓                                │
        ┌────────────────────────┐                    │
        │ Is it DC?              │                    │
        │ → Generate constant    │                    │
        │ Is it DS?              │                    │
        │ → Skip (leave space)   │                    │
        └───────┬────────────────┘                    │
                └─────────────────────────────────────┘
```

### Example:
```
START 100
READ A          → (100) (04)(1)(S,01)      ; IC: opcode=04, operand=symbol #1
MOVER BREG, A   → (101) (04)(2)(S,01)
ADD BREG, B     → (102) (01)(2)(S,02)
MOVEM BREG, C   → (103) (05)(2)(S,03)
STOP            → (104) (00)(0)(0)
A DS 1          → (105) Symbol A = 105
B DC '5'        → (106) Symbol B = 106, value=5
C DS 1          → (107) Symbol C = 107
END
```

**Symbol Table (after Pass-1):**

| Index | Symbol | Address |
|-------|--------|---------|
| 1 | A | 105 |
| 2 | B | 106 |
| 3 | C | 107 |

---

## 3. 📌 MACROS — FEATURES, TYPES & EXPANSION [5-10 Marks] — 🔴 GUARANTEED

> **Asked:** Every single paper in various forms

### 3.1 What is a Macro?

A **macro** is a single-line abbreviation for a group of instructions. It allows programmers to define a sequence of instructions once and use them multiple times by invoking the macro name.

### 3.2 Macro Definition & Call Structure

```
MACRO                    ← Macro Header
macro_name &arg1, &arg2  ← Macro Prototype (name + parameters)
  MOVER AREG, &arg1     ← Macro Body
  ADD AREG, &arg2       │
  MOVEM AREG, &arg1     │
MEND                     ← End of Macro
```

**Macro Call:** `macro_name A, B`

**Macro Expansion:** The macro call is replaced by the body with actual arguments substituted:
```
+  MOVER AREG, A
+  ADD AREG, B
+  MOVEM AREG, A
```
(The `+` indicates expanded code)

### 3.3 Features of Macros:

1. **Macro Definition**: MACRO ... MEND block defines a macro
2. **Macro Call/Invocation**: Using the macro name as a statement
3. **Macro Expansion**: Replacing call with the body
4. **Positional Parameters**: `&arg1, &arg2` — matched by position
5. **Keyword Parameters**: `&X=, &Y=` — matched by name
6. **Default Parameter Values**: `&X=5` — default if not specified
7. **Conditional Expansion (AIF/AGO)**: Selective assembly based on conditions
8. **Expansion Time Variables (EV)**: SET statements for counters
9. **Nested Macro Calls**: Macro call within another macro body
10. **Macro Calls within Macros**: One macro's expansion contains another macro call

### 3.4 Conditional Macro Example:
```
MACRO
INCR &ARG, &REG=AREG
  AIF (&REG EQ AREG) .NEXT
  MOVER AREG, &ARG
  ADD AREG, ='1'
  MOVEM AREG, &ARG
  AGO .END
.NEXT  
  ADD &REG, ='1'
  MOVEM &REG, &ARG
.END  
MEND
```

### 3.5 Advanced Macro Facilities:
1. **Nested Macro Definitions**: Macro defined inside another macro body
2. **Macro Calls within Macros**: A macro body containing call to another macro
3. **Recursive Macros**: A macro that calls itself
4. **Concatenation**: Using `.` to concatenate parameter with text (e.g., `&X.LOOP`)
5. **Multiple Macro Definitions**: Using SET, AIF, AGO for loops in expansion

---

## 4. 📌 SINGLE-PASS MACRO PROCESSOR [10 Marks]

> **Asked:** Dec'22, Dec'24

### Answer:

A **single-pass macro processor** handles macro definition, macro calls, and expansion in a **single scan** of the source program.

### Data Structures:
1. **MDT (Macro Definition Table)**: Stores macro body statements
2. **MNT (Macro Name Table)**: Stores macro name and pointer to MDT
3. **MDTC (MDT Counter)**: Points to next free entry in MDT
4. **MNTC (MNT Counter)**: Points to next free entry in MNT
5. **ALA (Argument List Array)**: Stores formal-actual parameter mapping

### Flowchart:

```
┌───────────────────────┐
│  Read next statement   │ ◄───────────────────────────┐
└──────────┬────────────┘                              │
           │                                           │
           ▼                                           │
   ┌───────────────┐                                   │
   │  Is it MACRO  │── YES ──► Enter macro name in MNT │
   │  directive?   │           Store body in MDT        │
   └───────┬───────┘           (until MEND)            │
           │ NO                └────────────────┐      │
           ▼                                    │      │
   ┌───────────────┐                            │      │
   │ Is it a Macro │── YES ──► Look up in MNT   │      │
   │ Call? (found   │          Set up ALA         │      │
   │ in MNT)       │          (map formals to     │      │
   └───────┬───────┘           actuals)           │      │
           │ NO                Read MDT, expand   │      │
           ▼                   body with actual   │      │
   ┌───────────────┐           args, write to     │      │
   │  Is it END?   │          output              │      │
   │               │── YES ──► STOP               │      │
   └───────┬───────┘                              │      │
           │ NO                                   │      │
           ▼                                      │      │
   Write statement to                             │      │
   output as-is                                   │      │
           │                                      │      │
           └──────────────────────────────────────┘──────┘
```

### Key Points:
- Macro must be **defined before its call** (limitation of single-pass)
- Cannot handle forward references to macros
- Simple and efficient for straightforward macro usage

---

## 5. 📌 TWO-PASS MACRO PROCESSOR [10 Marks]

> **Asked:** Nov'23, ~May'23, Jan'25

### Answer:

### Pass 1: Process Macro Definitions
- Scans entire source for MACRO...MEND blocks
- Builds **MNT** and **MDT**
- Removes macro definitions from source
- Handles nested definitions

### Pass 2: Expand Macro Calls
- Scans for macro calls
- Looks up MNT → gets MDT pointer
- Sets up ALA (formal → actual parameter mapping)
- Reads MDT entries; substitutes parameters → writes expanded code

### Data Structures Used:

| Data Structure | Description |
|----------------|-------------|
| **MNT** (Macro Name Table) | Macro name, #PP, #KP, #EV, MDTP, KPDTP, SSTP |
| **MDT** (Macro Definition Table) | Stores macro body with parameter indices |
| **KPDTAB** (Keyword Parameter Default Table) | Keyword parameter name and default value |
| **PNTAB** (Parameter Name Table) | Maps parameter names to indices |
| **EVTAB** (Expansion-time Variable Table) | Stores values of expansion variables (SET) |
| **SSNTAB** (Sequencing Symbol Name Table) | Stores labels for AIF/AGO |
| **ALA** (Argument List Array) | Maps formal parameters to actual values during expansion |
| **APTAB** (Actual Parameter Table) | Stores actual parameters during call |

### Example:

Source:
```
MACRO
COMPUTE &x, &a, &y          ← Definition
  MOVER AREG, &a
  MULT AREG, &x
  MOVEM AREG, &y
MEND
...
COMPUTE A, B, C               ← Call
```

**MNT:**
| Index | Name | #PP | #KP | #EV | MDTP |
|-------|------|-----|-----|-----|------|
| 1 | COMPUTE | 3 | 0 | 0 | 1 |

**MDT:**
| Index | Statement |
|-------|-----------|
| 1 | MOVER AREG, (P,2) |
| 2 | MULT AREG, (P,1) |
| 3 | MOVEM AREG, (P,3) |
| 4 | MEND |

**ALA during expansion of `COMPUTE A, B, C`:**
| Index | Formal | Actual |
|-------|--------|--------|
| 1 | &x | A |
| 2 | &a | B |
| 3 | &y | C |

**Expanded Code:**
```
+ MOVER AREG, B
+ MULT AREG, A
+ MOVEM AREG, C
```

---

## 6. 📌 DIRECT LINKING LOADER (DLL) [10 Marks] — 🟠 VERY HIGH

> **Asked:** Dec'22, ~May'23, Nov'23, Dec'24

### Answer:

A **Direct Linking Loader** is a general relocating loader that allows **multiple independently assembled/compiled programs** to be loaded and linked together.

### Features:
1. Allows **separate assembly** of subroutines
2. Performs **relocation** (adjusts addresses based on load address)
3. Performs **linking** (resolves external references between modules)
4. Uses **two passes** for loading

### Data Structures (Databases):

| Database | Description |
|----------|-------------|
| **ESTAB** (External Symbol Table) | Stores all external symbols with their load addresses |
| **LOCCTR** (Location Counter) | Tracks current loading address |
| **PROGADDR** (Program Load Address) | Starting address where program is loaded |
| **CSADDR** (Control Section Address) | Start address of current control section |
| **CSLTH** (Control Section Length) | Length of current control section |
| **EXECADDR** (Execution Start Address) | Address where execution begins |

### Loader Records:

| Record | Format | Purpose |
|--------|--------|---------|
| **Header (H)** | H \| Prog_name \| Start_addr \| Length | Identifies program module |
| **Define (D)** | D \| Symbol \| Address \| ... | Defines external symbols (exported) |
| **Refer (R)** | R \| Symbol \| ... | Lists external references (imported) |
| **Text (T)** | T \| Start_addr \| Length \| Object_code | Contains actual machine code |
| **Modification (M)** | M \| Address \| Length \| ±Symbol | Relocation/linking info |
| **End (E)** | E \| Exec_start_addr | Marks end of object module |

### Algorithm:

**Pass 1: Assign Addresses**
```
1. Set CSADDR = PROGADDR (starting load address)
2. For each control section:
   a. Read Header record → Extract name and length
   b. Enter control section name in ESTAB with CSADDR
   c. Read Define records → Enter each external symbol in ESTAB
      (address = CSADDR + relative address from D record)
   d. Set CSADDR = CSADDR + CSLTH (for next section)
3. Total program length = CSADDR - PROGADDR
```

**Pass 2: Load and Relocate**
```
1. Set CSADDR = PROGADDR
2. For each control section:
   a. Read Text records → Load object code into memory at
      (CSADDR + offset specified in T record)
   b. Read Modification records:
      - Look up symbol in ESTAB
      - Add/subtract symbol value to/from specified address
   c. At End record: set execution start address if specified
3. Transfer control to EXECADDR
```

```
     ┌──────────────────────────────────────────┐
     │         PASS 1 of Direct Linking Loader   │
     │                                           │
     │  ┌─ Read H record → get CSNAME, CSLTH    │
     │  ├─ Enter CSNAME in ESTAB (addr=CSADDR)  │
     │  ├─ Read D records → enter in ESTAB       │
     │  ├─   (symbol addr = CSADDR + D.addr)     │
     │  └─ CSADDR = CSADDR + CSLTH              │
     │                                           │
     │  Repeat for all control sections          │
     └──────────────────────────────────────────┘
                        │
                        ▼
     ┌──────────────────────────────────────────┐
     │         PASS 2 of Direct Linking Loader   │
     │                                           │
     │  ┌─ Read T records → load code at         │
     │  │    CSADDR + T.start_addr               │
     │  ├─ Read M records → look up symbol       │
     │  │    in ESTAB → modify address           │
     │  └─ At E record → jump to EXECADDR        │
     └──────────────────────────────────────────┘
```

---

## 7. 📌 CODE OPTIMIZATION TECHNIQUES [10 Marks] — 🟠 VERY HIGH

> **Asked:** ~May'23, Nov'23, Dec'24, Jan'25

### Answer:

**Code Optimization** is the process of transforming code to make it **faster**, use **less memory**, or consume **fewer resources** without changing the program's output.

### Classification:

```
Code Optimization
├── Machine Independent
│   ├── Local Optimization (within basic block)
│   └── Global Optimization (across basic blocks)
└── Machine Dependent
    ├── Register Allocation
    └── Instruction Selection
```

### Major Techniques:

#### 1. Common Sub-expression Elimination (CSE)
Eliminate redundant computation of the same expression.
```
BEFORE:                    AFTER:
t1 = a + b                t1 = a + b
t2 = a + b + c            t2 = t1 + c       ← reuse t1
```

#### 2. Constant Folding
Evaluate constant expressions at compile time.
```
BEFORE:                    AFTER:
x = 2 * 3 + 5             x = 11
```

#### 3. Constant Propagation
Replace variables with their known constant values.
```
BEFORE:                    AFTER:
x = 5                     x = 5
y = x + 3                 y = 8             ← x is known to be 5
```

#### 4. Dead Code Elimination
Remove code that never executes or whose result is never used.
```
BEFORE:                    AFTER:
x = a + b                 y = a * b
y = a * b                 (x = a + b removed —
z = x                      x never used again)
```

#### 5. Code Motion (Loop Invariant Code Motion)
Move computations that don't change inside a loop to **outside** the loop.
```
BEFORE:                    AFTER:
while(i < 100) {           t = a * b         ← moved out
  x = a * b + i;           while(i < 100) {
  i++;                       x = t + i;
}                             i++;
                            }
```

#### 6. Strength Reduction
Replace expensive operations with cheaper ones.
```
BEFORE:                    AFTER:
x = i * 4                 x = i << 2        ← shift is cheaper
y = x ^ 2                 y = x * x         ← multiply cheaper than power
```

#### 7. Copy Propagation
After `x = y`, replace subsequent uses of x with y.
```
BEFORE:                    AFTER:
x = y                     z = y + 1         ← x replaced by y
z = x + 1                 (x = y can be removed if x unused)
```

#### 8. Loop Unrolling
Reduce loop overhead by expanding loop body.
```
BEFORE:                    AFTER:
for(i=0; i<4; i++)        a[0] = 0;
  a[i] = 0;               a[1] = 0;
                           a[2] = 0;
                           a[3] = 0;
```

#### 9. Induction Variable Elimination
Replace loop index computations with simpler increments.
```
BEFORE:                    AFTER:
for(i=0; i<n; i++)        t = &a[0]
  sum += a[i];             for(i=0; i<n; i++)
                             sum += *t;
                             t += sizeof(int);
```

---

## 8. 📌 THREE ADDRESS CODE (3AC) [5-10 Marks] — 🟠 VERY HIGH

> **Asked:** Dec'22, ~May'23, Nov'23, Dec'24

### Answer:

**Three-Address Code** is an intermediate representation where each instruction has **at most three addresses** (two operands and one result).

### General Form: `x = y op z`

### Types of 3AC Statements:
1. **Assignment**: `x = y op z` or `x = op y`
2. **Copy**: `x = y`
3. **Unconditional Jump**: `goto L`
4. **Conditional Jump**: `if x relop y goto L`
5. **Procedure Call**: `param x`, `call p, n`, `return y`
6. **Indexed Assignment**: `x = y[i]` or `x[i] = y`
7. **Address/Pointer**: `x = &y`, `x = *y`, `*x = y`

### Implementation Methods:

| Method | Description |
|--------|-------------|
| **Quadruples** | (operator, arg1, arg2, result) — 4 fields per entry |
| **Triples** | (operator, arg1, arg2) — result is the triple index itself |
| **Indirect Triples** | Uses a pointer array to reference triples (allows reordering) |

### Example 1: `a = b * c + d`

**Three-Address Code:**
```
t1 = b * c
t2 = t1 + d
a = t2
```

**Quadruples:**
| # | Op | Arg1 | Arg2 | Result |
|---|-----|------|------|--------|
| 0 | * | b | c | t1 |
| 1 | + | t1 | d | t2 |
| 2 | = | t2 | — | a |

**Triples:**
| # | Op | Arg1 | Arg2 |
|---|----|------|------|
| 0 | * | b | c |
| 1 | + | (0) | d |
| 2 | = | a | (1) |

### Example 2: For loop
```c
for(i=0; i<10; i++) {
  if(i < 5)
    a = b + c * 3;
  else
    x = y * z;
}
```

**Three-Address Code:**
```
(1)  i = 0
(2)  if i >= 10 goto (11)
(3)  if i >= 5 goto (7)
(4)  t1 = c * 3
(5)  a = b + t1
(6)  goto (8)
(7)  x = y * z
(8)  t2 = i + 1
(9)  i = t2
(10) goto (2)
(11) ...
```

### Example 3: While + if-else
```c
while (a > b) do
  if (c < d) then
    x = y + z
  else
    x = y - z
```

**Three-Address Code:**
```
(1)  if a <= b goto (7)
(2)  if c >= d goto (5)
(3)  x = y + z
(4)  goto (6)
(5)  x = y - z
(6)  goto (1)
(7)  ...
```

---

## 9. 📌 SYSTEM SOFTWARE vs APPLICATION SOFTWARE [5 Marks] — 🟠 VERY HIGH

> **Asked:** Dec'22, Nov'23, Dec'24, Jan'25

### Answer:

| Feature | System Software | Application Software |
|---------|----------------|---------------------|
| **Definition** | Software that manages and controls hardware resources | Software designed for end-user tasks |
| **Purpose** | Provides platform for applications to run | Solves specific user problems |
| **Examples** | OS, Compiler, Assembler, Loader, Linker | MS Word, Chrome, Games, Calculator |
| **User Interaction** | Usually runs in background | Directly interacts with user |
| **Hardware Dependency** | Machine-dependent, low-level | Machine-independent, high-level |
| **Development Language** | Assembly, C (low-level) | Java, Python, C# (high-level) |
| **Execution** | Runs when system starts | Runs when user launches |
| **Necessity** | Essential for system operation | Not essential for system |
| **Speed** | Designed for efficiency | User convenience prioritized |
| **Complexity** | Complex, interacts with hardware | Relatively simpler |
| **Replaceability** | Difficult to replace | Easy to install/uninstall |

---

## 10. 📌 FORWARD REFERENCE PROBLEM [5 Marks] — 🟡 HIGH

> **Asked:** Nov'23, ~May'23, Dec'24

### Answer:

**Forward Reference** occurs when a symbol (label/variable) is **used before it is defined** in the source program.

### Example:
```
        MOVER AREG, X     ← Uses X (but X not yet defined!)
        ...
        ...
X       DC '5'            ← X defined here
```

At line 1, the assembler encounters `X` but doesn't know its address yet.

### Problem:
In a **single-pass assembler**, the assembler cannot generate the complete machine code for the instruction because the address of `X` is unknown at the time of first encounter.

### Solution Approaches:

**1. Two-Pass Assembly (Most Common)**
- **Pass 1**: Scan entire program, define all symbols and their addresses in the Symbol Table
- **Pass 2**: Generate machine code using the now-complete Symbol Table
- Forward references are automatically resolved

**2. Back-Patching (in Single-Pass Assembler)**
- When a forward reference is encountered:
  - Leave the address field blank (or put 0)
  - Add entry to a **Table of Incomplete Instructions (TII)**
  - TII stores: instruction address, symbol name
- When the symbol is eventually defined:
  - Go back and fill in (patch) all incomplete instructions
- At the end, if any symbol in TII is still undefined → **Error**

### TII Example:

```
100  MOVER AREG, X     → TII entry: (100, X)
101  ADD AREG, Y       → TII entry: (101, Y)
...
105  X DC '5'          → X = 105, patch address at 100
106  Y DC '3'          → Y = 106, patch address at 101
```

```
Table of Incomplete Instructions (TII):
┌────────────────┬──────────┐
│ Instr Address  │ Symbol   │
├────────────────┼──────────┤
│     100        │    X     │
│     101        │    Y     │
└────────────────┴──────────┘
```

---

## 11. 📌 LOADER — FUNCTIONS & SCHEMES [5 Marks] — 🟡 HIGH

> **Asked:** Dec'22, Dec'24, Jan'25

### Answer:

A **Loader** is a system program that places object code into main memory and prepares it for execution.

### Four Basic Functions of a Loader:
1. **Allocation**: Allocates space in memory for the program
2. **Linking**: Resolves symbolic references between independently compiled modules
3. **Relocation**: Adjusts address-sensitive locations based on where program is actually loaded
4. **Loading**: Physically places machine code and data into memory

### Loader Schemes:

```
┌─────────────────────────────────────────────────┐
│                  LOADER SCHEMES                  │
├───────────────────────┬─────────────────────────┤
│  1. Compile-and-Go    │ No separate loader;     │
│     Loader            │ assembler directly       │
│                       │ puts code in memory      │
├───────────────────────┼─────────────────────────┤
│  2. Absolute Loader   │ Loads at fixed address   │
│     (Simple)          │ No relocation/linking    │
├───────────────────────┼─────────────────────────┤
│  3. Relocating Loader │ Adjusts addresses for    │
│     (BSS Loader)      │ any load location.       │
│                       │ Bootstrap, Subroutine,   │
│                       │ Segment                  │
├───────────────────────┼─────────────────────────┤
│  4. Direct Linking     │ Full relocation +       │
│     Loader (DLL)      │ linking. Most general.   │
├───────────────────────┼─────────────────────────┤
│  5. Dynamic Linking   │ Links at run-time.       │
│     Loader            │ Loads modules on demand. │
└───────────────────────┴─────────────────────────┘
```
