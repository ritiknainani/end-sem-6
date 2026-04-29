# SPCC Practical Viva Q&A — Part 4 (Full Syllabus)
## Assemblers | Loaders & Linkers | System Programming Fundamentals

> Covers all syllabus topics NOT in Parts 1–3. Based on MU PYQ analysis + Question Bank.

---

## Module 1: System Programming Fundamentals

### Q1. What is system programming?
**A:** System programming is the development of software that provides services to computer hardware and acts as a platform for running application software. Examples: compilers, assemblers, linkers, loaders, OS, device drivers.

### Q2. What are the components of a system?
**A:** A system consists of: (1) Hardware – CPU, memory, I/O devices (2) System Software – OS, compilers, assemblers (3) Application Software – end-user programs (4) Users – people interacting with the system.

### Q3. What is the difference between system software and application software?
**A:**
| Feature | System Software | Application Software |
|---------|----------------|---------------------|
| Purpose | Manages hardware, provides platform | Solves user tasks |
| Examples | OS, Compiler, Assembler, Loader | Word, Chrome, Games |
| User Interaction | Background | Direct |
| Hardware Dependency | Machine-dependent | Machine-independent |
| Necessity | Essential | Optional |
| Speed | Optimized for efficiency | User convenience |
| Development | Low-level languages | High-level languages |

### Q4. What are the different types of system software?
**A:** Operating System, Assembler, Compiler, Interpreter, Linker, Loader, Macro Processor, Text Editor, Debugger, Device Driver.

### Q5. Explain the sequence of system programs from source code to execution.
**A:**
1. **Editor** → write source code (.c, .asm)
2. **Preprocessor** → handle #include, #define, macros
3. **Compiler/Assembler** → translate to object code (.obj)
4. **Linker** → combine object modules, resolve references → executable
5. **Loader** → load into memory, relocate, start execution
6. **CPU** → fetches and executes instructions

### Q6. What is the difference between a compiler and an assembler?
**A:**
| Compiler | Assembler |
|----------|-----------|
| Translates HLL to machine code | Translates assembly to machine code |
| One-to-many mapping | Nearly 1-to-1 mapping |
| Complex (6 phases) | Simpler (2 passes) |
| Input: C, Java, etc. | Input: MOV, ADD, etc. |
| Output: object code | Output: machine code |

### Q7. What is the difference between a compiler and an interpreter?
**A:** A compiler translates the entire program at once before execution producing an executable. An interpreter translates and executes one statement at a time. Compiler is faster at runtime; interpreter gives better debugging and immediate feedback.

### Q8. What is a preprocessor?
**A:** A preprocessor processes source code before compilation. It handles: `#include` (file inclusion), `#define` (macro substitution), `#ifdef/#endif` (conditional compilation). Output is expanded source code fed to the compiler.

---

## Module 2: Assemblers (Two-Pass Assembler)

### Q1. What is an assembler?
**A:** An assembler is a system program that translates assembly language (mnemonics like MOV, ADD) into equivalent machine language (binary opcodes). It produces object code.

### Q2. Why do we need a two-pass assembler?
**A:** To resolve the **forward reference problem** — when a label/symbol is used before it is defined. Pass 1 collects all symbol definitions and addresses. Pass 2 uses them to generate machine code.

### Q3. What is the forward reference problem?
**A:** When a symbol is referenced before it is defined in the source. Example: `JUMP LOOP` appears before `LOOP: ADD A,B`. At the time of processing JUMP, the address of LOOP is unknown. Two-pass assembler solves this.

### Q4. What are the data structures (databases) used in a two-pass assembler?
**A:**
- **MOT** (Machine Opcode Table): Mnemonic → opcode, instruction length, type
- **POT** (Pseudo Opcode Table): Pseudo-ops like START, END, DS, DC
- **ST** (Symbol Table): Symbol name → address, length
- **LT** (Literal Table): Literal value → address
- **POOLTAB** (Pool Table): Starting index of each literal pool in LT
- **LC** (Location Counter): Tracks current address during assembly

### Q5. Explain Pass 1 of two-pass assembler.
**A:** Pass 1 processes source line by line:
1. Initialize LC from START directive
2. If label present → enter in Symbol Table with current LC
3. If imperative (machine instruction) → generate intermediate code, LC += instruction length
4. If DS → allocate storage, update LC
5. If DC → allocate and initialize, update LC
6. If LTORG → assign addresses to pending literals
7. At END → process remaining literals, output Symbol Table, Literal Table, and Intermediate Code

### Q6. Explain Pass 2 of two-pass assembler.
**A:** Pass 2 reads intermediate code from Pass 1:
1. For each imperative statement → look up opcode in MOT, look up operand address from Symbol Table/Literal Table → assemble machine code
2. For DC → generate constant value
3. For DS → leave space
4. At END → output final machine code

### Q7. What are the types of assembly language statements?
**A:** Three types:
1. **Imperative** (machine instructions): MOVER, ADD, SUB, COMP, BC, READ, PRINT, STOP
2. **Declarative** (data definition): DS (Declare Storage), DC (Declare Constant)
3. **Assembler Directives** (pseudo-ops): START, END, ORIGIN, EQU, LTORG

### Q8. What is the difference between DS and DC?
**A:** DS (Declare Storage) only reserves memory without initialization. DC (Declare Constant) reserves memory AND initializes it with a value. Example: `A DS 1` reserves 1 word; `B DC '5'` reserves 1 word with value 5.

### Q9. What is a literal? How is it different from a constant?
**A:** A literal is a constant value used directly in an instruction prefixed with `=`. Example: `ADD AREG, ='5'`. Unlike constants declared with DC, literals are unnamed and the assembler automatically allocates storage for them (at LTORG or END).

### Q10. What is the purpose of LTORG?
**A:** LTORG creates a **literal pool** — it tells the assembler to assign addresses to all literals accumulated since the last LTORG (or start). This ensures literals are placed near the code that uses them, within addressable range.

### Q11. What is EQU directive?
**A:** EQU assigns a symbolic name to a value or expression. Example: `MAX EQU 100` makes MAX equivalent to 100. Unlike DC, EQU doesn't allocate memory — it's just a symbolic assignment.

### Q12. What is ORIGIN directive?
**A:** ORIGIN resets the Location Counter to a specified value. Example: `ORIGIN 200` sets LC = 200. The next statement will be assembled at address 200.

### Q13. What is the Location Counter (LC)?
**A:** LC is a variable that keeps track of the current memory address during assembly. It's initialized by START, incremented by instruction length for each imperative statement, and can be changed by ORIGIN.

### Q14. What is the difference between one-pass and two-pass assembler?
**A:**
| One-Pass | Two-Pass |
|----------|----------|
| Single scan of source | Two scans of source |
| Uses backpatching for forward references | Resolves forward references in Pass 2 |
| Faster but limited | Slower but complete |
| Cannot handle all forward references easily | Handles all forward references |

### Q15. What is backpatching?
**A:** In a single-pass assembler, when a forward reference is encountered, the assembler leaves the address field blank and records it in a **Table of Incomplete Instructions (TII)**. When the symbol is later defined, the assembler goes back and fills in (patches) the missing address. This is backpatching.

---

## Module 3: Macro Processor

### Q1. What is the difference between a macro and a subroutine?
**A:**
| Macro | Subroutine |
|-------|-----------|
| Expanded inline (code copied) | Control transfer (CALL/RET) |
| Expansion at assembly/compile time | Executed at runtime |
| Faster (no call overhead) | Slower (call overhead) |
| More memory (code duplicated) | Less memory (single copy) |
| Parameters substituted textually | Parameters passed via stack/registers |

### Q2. What are positional vs keyword parameters?
**A:**
- **Positional:** Matched by position. 1st actual → 1st formal, 2nd → 2nd, etc.
- **Keyword:** Matched by name. `&X=5, &Y=10`. Order doesn't matter. Can have default values.

### Q3. What data structures does a two-pass macro processor use?
**A:**
- **MNT** (Macro Name Table): Macro name, #PP, #KP, #EV, MDTP, KPDTP, SSTP
- **MDT** (Macro Definition Table): Body statements with parameter indices
- **KPDTAB** (Keyword Parameter Default Table): Default values
- **PNTAB** (Parameter Name Table): Parameter names → indices
- **EVTAB** (Expansion-time Variable Table): SET variable values
- **SSNTAB** (Sequencing Symbol Name Table): Labels for AIF/AGO
- **ALA** (Argument List Array): Formal → actual parameter mapping

### Q4. What is AIF and AGO?
**A:** AIF (Arithmetic IF) is a conditional branch: `AIF (condition) .label` — jumps to .label if condition is true. AGO is an unconditional branch: `AGO .label` — always jumps. Used for conditional macro expansion.

### Q5. What is an expansion-time variable (EV)?
**A:** A variable used during macro expansion (not at program runtime). Set using `SET` directive: `&CTR SET 0`. Used with AIF/AGO for loops and conditional logic during expansion.

### Q6. What is a nested macro definition?
**A:** A macro defined inside another macro body. The inner macro is only entered into MNT when the outer macro is expanded. This is different from macro calls within macros.

### Q7. What is concatenation in macros?
**A:** Joining a parameter value with other text using `.` as delimiter. Example: `&X.LOOP` — if &X = "A", result is "ALOOP". The `.` separates the parameter from surrounding text.

### Q8. Difference between single-pass and two-pass macro processor?
**A:**
| Single-Pass | Two-Pass |
|------------|----------|
| Macro must be defined before use | Macros can be defined anywhere |
| No forward references to macros | Handles forward references |
| Simpler | More flexible |
| Cannot handle nested definitions well | Handles nested definitions |

---

## Module 4: Loaders and Linkers

### Q1. What is a loader? What are its 4 functions?
**A:** A loader places an executable program into main memory and prepares it for execution. Four functions:
1. **Allocation**: Reserve memory space
2. **Linking**: Resolve inter-module references
3. **Relocation**: Adjust addresses to actual load location
4. **Loading**: Place machine code into allocated memory

### Q2. What are the types of loaders?
**A:**
1. **Compile-and-Go (Assemble-and-Go)**: Assembler directly places code in memory. No separate loader.
2. **Absolute Loader**: Loads at fixed addresses specified in object code.
3. **Relocating (BSS) Loader**: Can load at any address, uses relocation bits.
4. **Direct Linking Loader (DLL)**: Handles multiple modules, performs linking + relocation.
5. **Dynamic Linking Loader**: Links modules at runtime on demand.

### Q3. What is an absolute loader?
**A:** Simplest loader that loads object code at the exact address specified in the object file. No relocation or linking. Advantages: simple, fast. Disadvantages: no flexibility, can't relocate, can't link modules.

### Q4. What is relocation? Why is it needed?
**A:** Relocation adjusts address-dependent locations in a program when it's loaded at a different address than assumed during assembly. Needed because in multiprogramming, the exact load address isn't known at assembly time.

### Q5. What is a relocation factor?
**A:** Relocation Factor = Actual Load Address − Assumed Starting Address. All relocatable addresses are adjusted by adding this factor.

### Q6. What is a Direct Linking Loader (DLL)?
**A:** A general-purpose relocating loader that handles multiple independently assembled programs. It performs both linking (resolving external references between modules) and relocation (adjusting addresses) using two passes.

### Q7. What are the records in an object module for DLL?
**A:**
- **H** (Header): Program name, start address, length
- **D** (Define): Exported external symbols and their addresses
- **R** (Refer): Imported external references
- **T** (Text): Actual machine code with addresses
- **M** (Modification): Addresses that need relocation/linking adjustment
- **E** (End): Execution start address

### Q8. What is ESTAB in DLL?
**A:** External Symbol Table — stores all external symbols from all control sections with their absolute load addresses. Built during Pass 1 of DLL. Used in Pass 2 for resolving modification records.

### Q9. What is dynamic linking? How is it different from static linking?
**A:**
- **Static Linking**: All modules combined into one executable at link time. Complete but larger.
- **Dynamic Linking**: Modules linked at runtime when first called. Uses stubs that invoke the loader. Advantages: memory efficient, shared libraries, easy updates.

### Q10. What is a linker?
**A:** A linker combines multiple object modules into a single executable by resolving external references (symbols defined in one module and used in another). It handles: symbol resolution, address relocation, and library inclusion.

### Q11. What is the difference between a linker and a loader?
**A:**
| Linker | Loader |
|--------|--------|
| Combines object modules | Places executable in memory |
| Resolves external references | Adjusts addresses (relocation) |
| Produces executable | Initiates execution |
| Runs before loading | Runs before execution |

### Q12. What are relocation bits?
**A:** In a BSS (Bootstrap) loader, each word of object code has an associated bit. Bit = 1 means the address is relocatable (add relocation factor). Bit = 0 means the address is absolute (no change needed).

### Q13. What is a Modification record?
**A:** In Direct Linking Loader, an M record specifies: (1) the address to be modified, (2) the length of modification, (3) which external symbol's address to add/subtract. Used for both relocation and linking.

---

## Module 5: Compiler Design — Parsing Theory

### Q1. What is a grammar? What is a Context-Free Grammar (CFG)?
**A:** A grammar is a formal set of rules for generating strings of a language. A CFG is G = (V, T, P, S) where V = non-terminals, T = terminals, P = productions (each with single non-terminal on LHS), S = start symbol. CFGs describe syntax of programming languages.

### Q2. What is a parse tree?
**A:** A graphical representation of a derivation. Root = start symbol. Internal nodes = non-terminals. Leaves = terminals (input string when read left to right). Shows how input is derived from the grammar.

### Q3. What is an Abstract Syntax Tree (AST)?
**A:** A compressed parse tree that removes redundant nodes. Only shows essential structure — operators as internal nodes, operands as leaves. Parentheses and chain productions are eliminated. Used as intermediate representation.

### Q4. What is an ambiguous grammar? Give an example.
**A:** A grammar where a string has more than one parse tree (or more than one leftmost derivation). Example: `E → E + E | E * E | id`. For `id + id * id`, two parse trees exist (one applying + first, other applying * first).

### Q5. How do you remove ambiguity?
**A:** By enforcing operator precedence and associativity through grammar restructuring. Example:
```
E → E + T | T       (+ is lower precedence, left-associative)
T → T * F | F       (* is higher precedence, left-associative)
F → (E) | id
```

### Q6. What is the difference between leftmost and rightmost derivation?
**A:**
- **Leftmost**: Always expand the leftmost non-terminal first. Used by top-down parsers.
- **Rightmost**: Always expand the rightmost non-terminal first. Used by bottom-up parsers (in reverse).

### Q7. What is a recursive descent parser?
**A:** A top-down parser that uses a set of recursive procedures, one for each non-terminal. Each procedure matches the corresponding grammar rule. May require backtracking. If no backtracking needed → predictive parser.

### Q8. What is shift-reduce parsing?
**A:** A bottom-up parsing technique using two operations:
- **Shift**: Push next input symbol onto stack
- **Reduce**: Replace a handle (RHS of production) on top of stack with the LHS non-terminal
Also: Accept (successful parse) and Error.

### Q9. What is a handle in bottom-up parsing?
**A:** A handle is a substring of the sentential form that matches the right side of a production, and whose reduction to the LHS represents one step in the reverse of a rightmost derivation. It's the portion to be reduced next.

### Q10. What are the types of LR parsers?
**A:**
1. **LR(0)**: Uses LR(0) items, no lookahead
2. **SLR(1)**: Uses LR(0) items + FOLLOW sets for reduce decisions
3. **CLR(1)**: Uses LR(1) items with lookahead — most powerful
4. **LALR(1)**: Merges CLR states with same core — used by YACC/Bison
Power: LR(0) < SLR(1) < LALR(1) < CLR(1)

### Q11. What is an LR(0) item?
**A:** A production with a dot (•) indicating how much of the RHS has been seen. Example: For `A → XYZ`: `A → •XYZ` (nothing seen), `A → X•YZ` (X seen), `A → XYZ•` (complete — ready to reduce).

### Q12. What is the Closure operation?
**A:** Given a set of items I, closure(I) adds all items `B → •γ` for every item `A → α•Bβ` in I (where B is a non-terminal). Repeatedly until no more items can be added. Used to compute LR item sets.

### Q13. What is the GOTO operation?
**A:** GOTO(I, X) = closure of all items `A → αX•β` where `A → α•Xβ` is in set I. It computes the next state after seeing symbol X. Used to build the DFA for LR parsing.

### Q14. What is a shift-reduce conflict?
**A:** When the parser can't decide whether to shift (push next input) or reduce (apply a production). Occurs in SLR when a state has both a shift item and a reduce item for the same terminal. Indicates grammar may not be SLR.

### Q15. What is a reduce-reduce conflict?
**A:** When the parser can't decide which of two productions to reduce by. Occurs when a state has two complete items whose FOLLOW sets overlap. Usually means the grammar is ambiguous or not suitable for that parser type.

### Q16. What is an Operator Precedence Parser?
**A:** A bottom-up parser for operator grammars (no ε-productions, no two adjacent non-terminals). Uses three precedence relations (⋖ yields to, ≐ equal, ⋗ takes over) between terminals to find handles. Build table using LEADING and TRAILING sets.

### Q17. What are LEADING and TRAILING sets?
**A:**
- **LEADING(A)**: Set of terminals that can appear as the first terminal in any string derived from A.
- **TRAILING(A)**: Set of terminals that can appear as the last terminal in any string derived from A.
Used to build the operator precedence table.

### Q18. What is YACC?
**A:** Yet Another Compiler Compiler — a parser generator tool that takes a grammar specification and produces an LALR(1) parser in C. Companion to LEX. YACC handles syntax; LEX handles tokens. Together they build a compiler front-end.

### Q19. How do LEX and YACC work together?
**A:** LEX generates a lexer (scanner) that tokenizes input. YACC generates a parser. The lexer function `yylex()` is called by the parser to get the next token. LEX produces `lex.yy.c`, YACC produces `y.tab.c`. They're compiled and linked together.

---

## Module 6: Semantic Analysis & Intermediate Code

### Q1. What is semantic analysis?
**A:** The third phase of compilation that checks for semantic (meaning) errors that syntax analysis can't detect. It performs: type checking, scope resolution, type coercion, undeclared variable detection, and function parameter matching.

### Q2. What is type checking?
**A:** Verifying that operands and operators are type-compatible. Example: can't add int and string. If `a` is int and `b` is float, the compiler may insert an `inttoreal` conversion.

### Q3. What is type coercion?
**A:** Automatic (implicit) conversion of one type to another by the compiler. Example: in `float x = 5 + 3.14`, the integer 5 is automatically converted to float 5.0 before addition.

### Q4. What is Syntax-Directed Translation (SDT)?
**A:** A method of attaching semantic rules (actions) to grammar productions. As the parser builds the parse tree, semantic actions are executed to compute attributes (values, types, code).

### Q5. What are synthesized vs inherited attributes?
**A:**
- **Synthesized**: Computed bottom-up from children's attributes. E.g., E.val = E1.val + T.val
- **Inherited**: Computed top-down from parent/sibling attributes. E.g., passing type info down.
S-attributed grammars use only synthesized attributes.

### Q6. What is a DAG (Directed Acyclic Graph)?
**A:** Like an AST but with shared nodes for common subexpressions. If `a+b` appears twice, only one node exists, shared by both uses. DAGs automatically identify common subexpressions for optimization.

### Q7. What is the difference between a syntax tree and a DAG?
**A:** A syntax tree has separate subtrees for duplicate expressions. A DAG merges them into shared nodes. DAG → fewer nodes → identifies common subexpressions → enables optimization.

### Q8. What is postfix notation?
**A:** Also called Reverse Polish Notation (RPN). Operators appear after operands. No parentheses needed. Example: `a + b * c` → `a b c * +`. Easy to evaluate using a stack.

---

## Module 7: Code Generation & Optimization

### Q1. What are the issues in code generation?
**A:** (1) Input form (IR type) (2) Target program form (absolute/relocatable/assembly) (3) Memory management (4) Instruction selection (5) Register allocation & assignment (6) Evaluation order. Register allocation is NP-complete.

### Q2. What is a register descriptor?
**A:** Tracks which variable values are currently stored in each register. Example: R0 contains value of variable `x`. Updated after every instruction.

### Q3. What is an address descriptor?
**A:** Tracks where each variable's current value is stored — in a register, in memory, or both. Example: variable `x` is in R0 and in memory location 100.

### Q4. What is the getReg() function?
**A:** Determines the best register for an operation:
1. If operand already in a register → use it
2. If empty register available → use it
3. If all registers full → spill (save to memory) the one whose value is also in memory, or the one used furthest in the future

### Q5. What is a basic block?
**A:** A maximal sequence of consecutive instructions where control enters only at the first instruction and leaves only at the last. No jumps into the middle, no jumps out from the middle (except at end).

### Q6. How do you identify leaders (to partition into basic blocks)?
**A:** A leader is:
1. The first instruction of the program
2. Any instruction that is the target of a jump
3. Any instruction that immediately follows a jump

### Q7. What is a flow graph?
**A:** A directed graph where nodes are basic blocks and edges represent possible control flow. Edge B1→B2 exists if B1's last instruction jumps to B2, or B2 immediately follows B1 and B1 doesn't end with unconditional jump.

### Q8. What is loop-invariant code motion?
**A:** Moving computations that produce the same result in every iteration to outside the loop. Example: `x = a * b` inside a loop where `a` and `b` don't change → move before the loop.

### Q9. What is induction variable elimination?
**A:** A variable that changes by a constant amount in each loop iteration is an induction variable. If two induction variables are related (e.g., `j = 4*i`), one can be eliminated and expressed in terms of the other.

### Q10. What is the difference between peephole optimization and global optimization?
**A:**
- **Peephole**: Examines small window of target instructions, replaces with better sequences. Local, simple.
- **Global**: Analyzes entire program or function, optimizes across basic blocks. More powerful but complex.

---

## Device Drivers, Debuggers & OS (Short Notes)

### Q1. What is a device driver?
**A:** System software that acts as a translator between the OS and hardware devices. It provides a standard interface so the OS doesn't need to know device-specific details. Types: character, block, network drivers.

### Q2. What is a debugger?
**A:** A tool to test and debug programs. Features: set breakpoints, step through code, inspect variables, view call stack, watch expressions. Types: source-level (GDB), machine-level, remote debugger.

### Q3. What is the difference between machine-dependent and machine-independent optimization?
**A:**
- **Machine-independent**: Applied on intermediate code. Examples: CSE elimination, constant folding, dead code removal, code motion.
- **Machine-dependent**: Applied on target code. Examples: register allocation, instruction selection, peephole optimization. Requires knowledge of target architecture.

---

## Rapid-Fire Viva Questions (Most Common Quick-Ask)

### Q: Name the 6 phases of a compiler.
**A:** Lexical Analysis, Syntax Analysis, Semantic Analysis, Intermediate Code Generation, Code Optimization, Code Generation.

### Q: What is the output of each compiler phase?
**A:** Tokens → Parse Tree → Annotated Parse Tree → Intermediate Code (3AC) → Optimized IC → Target Machine Code.

### Q: What is ε (epsilon)?
**A:** The empty string — a string of length zero. Used in grammar to indicate that a non-terminal can derive nothing (disappear).

### Q: What is a sentential form?
**A:** Any string derivable from the start symbol using production rules. If all symbols are terminals → it's a sentence of the language.

### Q: What is a viable prefix?
**A:** A prefix of a right sentential form that can appear on the stack of a shift-reduce parser. It never extends past the right end of the handle.

### Q: What is augmented grammar?
**A:** Adding a new start symbol S' with production S' → S to the original grammar. Done in LR parsing to indicate when to accept. S' → S• means accept.

### Q: What is a production rule?
**A:** A rule in a grammar of the form A → α, where A is a non-terminal and α is a string of terminals and/or non-terminals. It defines how A can be replaced.

### Q: What is a derivation?
**A:** The process of applying production rules starting from the start symbol to generate a string. Each step replaces a non-terminal with the RHS of one of its productions.

### Q: What is the difference between a token and a lexeme?
**A:** Token is the category (e.g., IDENTIFIER), lexeme is the actual string (e.g., "count"). Multiple lexemes can belong to the same token type.

### Q: What is the handle in "id + id * id" parsing?
**A:** In bottom-up parsing with standard precedence, the first handle is the leftmost `id` (reduced to F), then to T, etc. The parser reduces handles in reverse rightmost derivation order.

### Q: Why can't LL(1) handle left recursion?
**A:** Because the parser would keep expanding the same non-terminal without consuming any input, causing an infinite loop. The grammar must be transformed to right recursion first.

### Q: What is the role of $ in parsing?
**A:** `$` is the end-of-input marker (end marker). It marks the bottom of the parser stack and the end of the input string. Parsing succeeds when stack has only `$` and input has only `$`.

### Q: What is a canonical collection?
**A:** The complete set of LR item sets (states) for a grammar, computed using closure and GOTO operations. It forms the DFA used for LR parsing table construction.

### Q: What is the difference between SLR and CLR?
**A:** SLR uses FOLLOW sets for reduce decisions (may cause conflicts). CLR uses specific lookahead in each item (more precise, fewer conflicts, but more states). CLR is more powerful.

### Q: What is LALR?
**A:** Look-Ahead LR — merges CLR states with the same core items but different lookaheads. Fewer states than CLR (same as SLR), but more powerful than SLR. Used by YACC/Bison.

### Q: What is the difference between quadruples and triples?
**A:** Quadruples have 4 fields (op, arg1, arg2, result) — explicit temporaries, easy to reorder. Triples have 3 fields (op, arg1, arg2) — result is position number, no temporary names but hard to reorder.

### Q: What is an indirect triple?
**A:** Uses a pointer array that references entries in a triples table. Allows reordering of instructions without changing the triples themselves — best of both quadruples and triples.
