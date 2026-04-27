# 📝 SPCC Complete Answer Guide — Part 4 (Question Bank — New Topics)

> **Source:** SPCC Question Bank
> Only NEW topics not already in Parts 1-3 are covered here.
> A cross-reference map is at the end.

---

## 32. 📌 DEVICE DRIVERS, OPERATING SYSTEM, DEBUGGERS [10 Marks]

> **QB Q.21** — Not covered in any previous part

### 1. Device Drivers

A **device driver** is a specialized system program that acts as a **translator between hardware devices and the operating system**.

**Functions:**
- Provides **standard interface** between OS and hardware
- Handles device-specific commands and protocols
- Manages **I/O operations** (read/write to device)
- Handles **interrupts** from devices

**Types:**
| Type | Description | Example |
|------|-------------|---------|
| Character device driver | Handles data byte by byte | Keyboard, mouse, serial port |
| Block device driver | Handles data in fixed-size blocks | Hard disk, USB drive |
| Network device driver | Handles network communication | Ethernet card, Wi-Fi adapter |

**Architecture:**
```
┌───────────────────────┐
│   Application Program │
├───────────────────────┤
│   Operating System    │
│   (Kernel)            │
├───────────────────────┤
│   Device Driver       │ ← Translates OS calls to
│   (Software layer)    │   device-specific commands
├───────────────────────┤
│   Hardware Device     │
│   (Printer, Disk, etc)│
└───────────────────────┘
```

### 2. Operating System

An **Operating System (OS)** is the most fundamental **system software** that manages computer hardware and provides services to application programs.

**Key Functions:**
1. **Process Management**: Creation, scheduling, termination of processes
2. **Memory Management**: Allocation, deallocation, virtual memory
3. **File System Management**: Create, delete, read, write files
4. **I/O Management**: Manages input/output devices via drivers
5. **Security & Protection**: User authentication, access control
6. **Resource Allocation**: CPU, memory, devices shared among processes

**Types:** Batch OS, Multiprogramming, Multitasking, Real-Time OS, Distributed OS

**Examples:** Windows, Linux, macOS, Android, iOS

### 3. Debuggers

A **debugger** is a system program used to **test and debug** other programs.

**Functions:**
1. **Set breakpoints**: Pause execution at specified lines
2. **Step execution**: Execute one instruction at a time (step-in, step-over, step-out)
3. **Inspect variables**: View/modify variable values at runtime
4. **Stack trace**: View function call sequence
5. **Watch expressions**: Monitor specific variables for changes
6. **Memory inspection**: Examine raw memory contents

**Types:**
| Type | Description |
|------|-------------|
| **Source-level debugger** | Works with high-level source code (GDB, Visual Studio Debugger) |
| **Machine-level debugger** | Works with assembly/machine code |
| **Remote debugger** | Debugs programs on a different machine |
| **Post-mortem debugger** | Analyzes core dumps after a crash |

**How a debugger works:**
```
┌──────────────┐    ┌────────────┐    ┌──────────────┐
│  Source Code  │───►│  Compiler  │───►│ Object Code  │
│  (with debug  │    │ (with -g   │    │ (with debug  │
│   info)       │    │  flag)     │    │  symbols)    │
└──────────────┘    └────────────┘    └──────┬───────┘
                                             │
                                     ┌───────▼───────┐
                                     │   DEBUGGER    │
                                     │  - Breakpoints│
                                     │  - Step exec  │
                                     │  - Inspect    │
                                     │  - Stack trace│
                                     └───────────────┘
```

---

## 33. 📌 MACHINE DEPENDENT vs MACHINE INDEPENDENT [5-10 Marks]

> **QB Q.22(ii)** — Not covered in previous parts

### In Context of Code Optimization:

| Feature | Machine Independent | Machine Dependent |
|---------|-------------------|------------------|
| **Level** | Applied on **intermediate code** | Applied on **target machine code** |
| **Knowledge** | No knowledge of target architecture needed | Requires knowledge of CPU, registers, instruction set |
| **When applied** | During/after IC generation | During/after code generation |
| **Examples** | CSE elimination, Constant folding, Dead code elimination, Loop optimization | Register allocation, Instruction selection, Instruction scheduling, Peephole optimization |
| **Portability** | Techniques are portable across machines | Specific to target architecture |
| **Phase** | Code Optimization phase | Code Generation phase |

### In Context of System Software:

| Feature | Machine Dependent | Machine Independent |
|---------|------------------|-------------------|
| **Definition** | Depends on specific hardware architecture | Works across different architectures |
| **Examples** | Device drivers, Boot loader, Machine code | Compilers (front-end), Macro processors, Text editors |
| **Portability** | Not portable | Portable |
| **In Assembler** | Instruction formats, addressing modes, opcode table | Symbol table management, literal handling, pseudo-op processing |

### Peephole Optimization (Machine Dependent):

Examines a **small window (peephole)** of target instructions and replaces with more efficient equivalents.

**Examples:**

1. **Redundant loads/stores elimination:**
```
BEFORE:                    AFTER:
MOV R0, a                 MOV R0, a
MOV a, R0   ← redundant   (removed)
```

2. **Unreachable code elimination:**
```
BEFORE:                    AFTER:
GOTO L2                    GOTO L2
ADD R0, R1  ← unreachable  (removed)
L2: ...                    L2: ...
```

3. **Algebraic simplification:**
```
BEFORE:                    AFTER:
MUL R0, #1                (removed — x*1 = x)
ADD R0, #0                (removed — x+0 = x)
```

4. **Strength reduction:**
```
BEFORE:                    AFTER:
MUL R0, #2                SHL R0, #1  (shift left = ×2)
MUL R0, #4                SHL R0, #2  (shift left = ×4)
```

---

## 34. 📌 CLR(1) / CANONICAL LR(1) PARSER [10 Marks]

> **QB Q.25(ii)** — Not covered in previous parts (only LR(0)/SLR was covered)

### Answer:

**CLR(1)** is the most powerful LR parser. It uses **LR(1) items** which include a **lookahead symbol** to make more precise reduce decisions.

### LR(1) Item Format:
```
[A → α • β, a]

Where:
- A → αβ is a production
- • indicates parsing position
- a is the lookahead terminal (1 symbol)
```

### Difference from SLR:

| Feature | SLR(1) | CLR(1) | LALR(1) |
|---------|--------|--------|---------|
| Items | LR(0) items | LR(1) items (with lookahead) | LR(1) items, merged states |
| Reduce decision | Uses FOLLOW set | Uses **specific lookahead** | Uses merged lookaheads |
| Power | Least | Most | Middle |
| States | Fewest | Most | Same as SLR |
| Conflicts | May have S/R conflicts | Resolves most conflicts | Between SLR and CLR |

### Closure for LR(1):

If [A → α • Bβ, a] is in the set, and B → γ is a production:
- Add [B → •γ, b] for each b ∈ FIRST(βa)

### GOTO for LR(1):
Same as LR(0), but carry the lookahead along.

### CLR(1) Parsing Table Rules:

| Condition | Action |
|-----------|--------|
| [A → α•aβ, b] in Iᵢ, GOTO(Iᵢ, a) = Iⱼ | ACTION[i, a] = **shift j** |
| [A → α•, a] in Iᵢ (A ≠ S') | ACTION[i, a] = **reduce A → α** |
| [S' → S•, $] in Iᵢ | ACTION[i, $] = **accept** |

**Key difference from SLR:** Reduce action is placed ONLY in the column of the **specific lookahead** `a`, not for all symbols in FOLLOW(A).

### Example:

**Grammar:** S → CC, C → cC | d

**Augmented:** S' → S

**LR(1) Item Sets:**

**I₀:** Closure({[S'→•S, $]})
```
[S' → •S, $]
[S → •CC, $]
[C → •cC, c/d]    ← lookahead = FIRST(C$) = {c,d}
[C → •d, c/d]
```

**I₁:** GOTO(I₀, S) = {[S'→S•, $]}

**I₂:** GOTO(I₀, C)
```
[S → C•C, $]
[C → •cC, $]      ← lookahead = FIRST($) = {$}
[C → •d, $]
```

**I₃:** GOTO(I₀, c)
```
[C → c•C, c/d]
[C → •cC, c/d]
[C → •d, c/d]
```

**I₄:** GOTO(I₀, d) = {[C→d•, c/d]}

**I₅:** GOTO(I₂, C) = {[S→CC•, $]}

**I₆:** GOTO(I₂, c)
```
[C → c•C, $]
[C → •cC, $]
[C → •d, $]
```

**I₇:** GOTO(I₂, d) = {[C→d•, $]}

**I₈:** GOTO(I₃, C) = {[C→cC•, c/d]}

**I₉:** GOTO(I₆, C) = {[C→cC•, $]}

Note: I₃ and I₆ have same core but **different lookaheads** → CLR keeps them separate, LALR merges them.

### LALR(1) Parser:

- **Merges CLR(1) states** that have the same core items but different lookaheads
- Fewer states than CLR(1), same number as SLR
- More powerful than SLR but less than CLR
- Used by **YACC/Bison**
- In above example: Merge I₃+I₆ and I₄+I₇ and I₈+I₉

---

## 35. 📌 CONDITIONAL MACROS (Detailed) [5-10 Marks]

> **QB Q.23(iii)** — Needs more detail than Part 1

### Answer:

**Conditional macros** allow selective expansion of macro body using **AIF** (conditional branch) and **AGO** (unconditional branch) directives.

### Directives:
| Directive | Purpose |
|-----------|---------|
| **AIF** | Conditional branch: `AIF (condition) .label` — jump if true |
| **AGO** | Unconditional branch: `AGO .label` — always jump |
| **SET** | Assign value to expansion-time variable (EV) |
| **.label** | Sequencing symbol (target for AIF/AGO) |

### Example 1: Conditional Register Selection

```
MACRO
INCR &ARG, &REG=AREG
  AIF (&REG EQ AREG) .USE_A
  MOVER &REG, &ARG
  ADD &REG, ='1'
  MOVEM &REG, &ARG
  AGO .DONE
.USE_A
  MOVER AREG, &ARG
  ADD AREG, ='1'
  MOVEM AREG, &ARG
.DONE
MEND
```

**Call 1:** `INCR X, REG=BREG`
- &REG = BREG, condition (BREG EQ AREG) is FALSE
- Expansion:
```
+  MOVER BREG, X
+  ADD BREG, ='1'
+  MOVEM BREG, X
```

**Call 2:** `INCR Y` (uses default REG=AREG)
- &REG = AREG, condition (AREG EQ AREG) is TRUE → jump to .USE_A
- Expansion:
```
+  MOVER AREG, Y
+  ADD AREG, ='1'
+  MOVEM AREG, Y
```

### Example 2: Loop in Macro (using SET)

```
MACRO
CLEAR &FIRST, &COUNT
  &CTR SET 0
.LOOP
  AIF (&CTR GE &COUNT) .END
  MOVER AREG, ='0'
  MOVEM AREG, &FIRST+&CTR
  &CTR SET &CTR+1
  AGO .LOOP
.END
MEND
```

**Call:** `CLEAR X, 3` — generates 3 clear operations:
```
+  MOVER AREG, ='0'
+  MOVEM AREG, X+0
+  MOVER AREG, ='0'
+  MOVEM AREG, X+1
+  MOVER AREG, ='0'
+  MOVEM AREG, X+2
```

---

## 36. 📌 MACRO CALLS WITHIN MACROS (Detailed) [10 Marks]

> **QB Q.12** — Needs fuller treatment than Part 1

### Answer:

When one macro's body contains a **call to another macro**, the inner macro is expanded during the expansion of the outer macro.

### Example:

**Define two macros:**
```
MACRO
INCR &X                    ← Macro 1
  MOVER AREG, &X
  ADD AREG, ='1'
  MOVEM AREG, &X
MEND

MACRO
CALC &A, &B, &RESULT       ← Macro 2 (calls Macro 1)
  MOVER AREG, &A
  ADD AREG, &B
  MOVEM AREG, &RESULT
  INCR &RESULT              ← Call to Macro 1 inside Macro 2
MEND
```

**Source:** `CALC X, Y, Z`

**Pass 1 of Macro Processor:** Stores both definitions in MNT/MDT.

**Pass 2 — Expansion of `CALC X, Y, Z`:**
```
+ MOVER AREG, X             ← from CALC body
+ ADD AREG, Y               ← from CALC body
+ MOVEM AREG, Z             ← from CALC body
```
Now encounters `INCR Z` → expands it:
```
+ MOVER AREG, Z             ← from INCR expansion
+ ADD AREG, ='1'            ← from INCR expansion
+ MOVEM AREG, Z             ← from INCR expansion
```

**Final expanded code:**
```
+ MOVER AREG, X
+ ADD AREG, Y
+ MOVEM AREG, Z
+ MOVER AREG, Z
+ ADD AREG, ='1'
+ MOVEM AREG, Z
```

### Processing Rules:
1. Outer macro is expanded first
2. When inner macro call is encountered during expansion → it is expanded in place
3. The **two-pass macro processor** handles this naturally: Pass 1 collects all definitions, Pass 2 expands recursively
4. In **single-pass processor**: inner macro must be defined BEFORE outer macro

### Nested Macro Definitions (different from calls within macros):
A macro **defined inside** another macro body. The inner macro definition only becomes available after the outer macro is expanded.

---

## 37. 📌 RELOCATION AND LINKING (Combined) [10 Marks]

> **QB Q.18** — Combined explanation with diagram

### Answer:

### Relocation:
The process of **adjusting address-sensitive locations** when a program is loaded at a different address than originally assumed during assembly.

### Linking:
The process of **combining multiple independently compiled/assembled modules** by resolving **inter-module references** (external symbols).

### Combined Process:

```
┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│  Module A    │  │  Module B    │  │  Module C    │
│  (obj code)  │  │  (obj code)  │  │  (obj code)  │
│              │  │              │  │              │
│ CALL B_FUNC  │  │ B_FUNC:     │  │ CALL A_FUNC  │
│ (external    │  │ (exported)   │  │ (external    │
│  reference)  │  │              │  │  reference)  │
└──────┬───────┘  └──────┬───────┘  └──────┬───────┘
       │                 │                 │
       └─────────┬───────┴─────────┬───────┘
                 │                 │
                 ▼                 ▼
        ┌─────────────────────────────────┐
        │           LINKER                │
        │  1. Combine all modules         │
        │  2. Resolve external references │
        │     (B_FUNC, A_FUNC → addresses)│
        │  3. Generate load module        │
        └────────────┬────────────────────┘
                     │
                     ▼
        ┌─────────────────────────────────┐
        │           LOADER                │
        │  1. Allocate memory             │
        │  2. Relocate addresses          │
        │     (adjust by load address)    │
        │  3. Place code in memory        │
        │  4. Transfer control            │
        └────────────┬────────────────────┘
                     │
                     ▼
        ┌─────────────────────────────────┐
        │   PROGRAM IN MEMORY (executing) │
        │                                 │
        │  Module A [0000-00FF]           │
        │  Module B [0100-01FF]           │
        │  Module C [0200-02FF]           │
        └─────────────────────────────────┘
```

### Relocation Example:
```
Module assembled at address 0:
  0000: LOAD 0050      ← address 0050 is relative
  0004: JUMP 0020      ← address 0020 is relative

Module loaded at address 5000 (relocation factor = 5000):
  5000: LOAD 5050      ← 0050 + 5000
  5004: JUMP 5020      ← 0020 + 5000
```

### Linking Example:
```
Module A (at 0000):              Module B (at 0100):
  0010: CALL ???  ←ext ref        0100: B_FUNC:
        (B_FUNC)                        ... code ...

After Linking:
  0010: CALL 0100  ← resolved to B_FUNC's address
```

### Types of Linking:
1. **Static Linking**: All references resolved before execution
2. **Dynamic Linking**: References resolved at runtime (DLLs, .so files)

---

## 📋 QUESTION BANK → ANSWER CROSS-REFERENCE MAP

| QB # | Question | Answer Location |
|------|----------|----------------|
| Q.1 | Intermediate code representation | **Part 2, Topic 12** |
| Q.2 | Single pass macro processor (flowchart) | **Part 1, Topic 4** |
| Q.3 | Issues in code generation | **Part 2, Topic 14** |
| Q.4 | Code optimization techniques | **Part 1, Topic 7** |
| Q.5 | Phases of compiler | **Part 1, Topic 1** |
| Q.6 | Direct linking loader | **Part 1, Topic 6** |
| Q.7 | Databases in DLL | **Part 3, Topic 31** |
| Q.8 | Dynamic linking loader | **Part 3, Topic 21** |
| Q.9 | First pass of two-pass macro processor | **Part 1, Topic 5** |
| Q.10 | Two pass assembler flowchart | **Part 1, Topic 2** |
| Q.11 | Advanced macro facilities | **Part 1, Topic 3.5** |
| Q.12 | Macro calls within macros | **Part 4, Topic 36** ⬅️ |
| Q.13 | Operator precedence parser | **Part 2, Topic 18** |
| Q.14 | Forward reference problem | **Part 1, Topic 10** |
| Q.15 | Assembly language statement types | **Part 3, Topic 20** |
| Q.16 | Flowchart Pass-I of two pass assembler | **Part 1, Topic 2** |
| Q.17 | Macro features and facilities | **Part 1, Topic 3** |
| Q.18 | Relocation and linking | **Part 4, Topic 37** ⬅️ |
| Q.19 | Loader functions and schemes | **Part 1, Topic 11** |
| Q.20 | Data structures in two-pass macro processor | **Part 1, Topic 5** |
| Q.21 | Device drivers, OS, Debuggers | **Part 4, Topic 32** ⬅️ |
| Q.22(i) | System vs Application software | **Part 1, Topic 9** |
| Q.22(ii) | Machine Dependent vs Independent | **Part 4, Topic 33** ⬅️ |
| Q.22(iii) | Compiler vs Interpreter | **Part 3, Topic 25** |
| Q.22(iv) | Bottom-up vs Top-down parser | **Part 3, Topic 26** |
| Q.23(i) | DAG | **Part 2, Topic 16** |
| Q.23(ii) | Syntax directed translation | **Part 3, Topic 27** |
| Q.23(iii) | Conditional macro | **Part 4, Topic 35** ⬅️ |
| Q.24 | 3AC + Basic blocks + Flow graph | **Part 1 Topic 8 + Part 2 Topic 15** |
| Q.25(i) | LR(0) | **Part 2, Topic 17** |
| Q.25(ii) | LR(1) / CLR | **Part 4, Topic 34** ⬅️ |
| Q.25(iii) | SLR | **Part 2, Topic 17** |
| Q.25(iv) | FIRST and FOLLOW | **Part 2, Topic 19** |
| Q.25(v) | Three address code | **Part 1, Topic 8** |
