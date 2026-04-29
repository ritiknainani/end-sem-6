# SPCC Practical Viva Q&A — Part 1
## Lexical Analyzer | Macroprocessor | Left Recursion | Left Factoring

---

## 1. Lexical Analyzer

### Q1. What is a Lexical Analyzer?
**A:** A lexical analyzer (scanner) is the first phase of a compiler. It reads the source code character by character and groups them into meaningful sequences called **tokens** (like keywords, identifiers, operators, literals, etc.).

### Q2. What is a token, lexeme, and pattern?
**A:**
- **Token:** A category/class of lexical unit (e.g., `KEYWORD`, `IDENTIFIER`, `NUMBER`)
- **Lexeme:** The actual character sequence matched (e.g., `int`, `count`, `42`)
- **Pattern:** The rule describing a set of lexemes for a token (e.g., `[a-zA-Z_][a-zA-Z0-9_]*` for identifiers)

### Q3. What are the different types of tokens?
**A:** Keywords (`if`, `while`, `int`), Identifiers (variable/function names), Constants/Literals (numbers, strings), Operators (`+`, `-`, `=`), Punctuation/Delimiters (`;`, `{`, `}`), and Comments.

### Q4. What is the role of a lexical analyzer in a compiler?
**A:**
1. Reads source code and produces a stream of tokens
2. Removes whitespace and comments
3. Correlates error messages with line numbers
4. Interacts with the symbol table
5. Feeds tokens to the syntax analyzer (parser)

### Q5. Why is lexical analysis separated from syntax analysis?
**A:**
- **Simplicity of design** — each phase has a clear responsibility
- **Efficiency** — specialized buffering techniques for reading characters
- **Portability** — only the scanner needs to change for different character sets

### Q6. What data structures are used in your lexical analyzer program?
**A:** Typically: a character buffer (input buffer), a symbol table (hash map/dictionary), and a token list (array/list of token objects with type and value).

### Q7. How do you identify keywords vs identifiers?
**A:** We maintain a list/set of all keywords. After extracting an alphanumeric token, we check if it exists in the keyword list. If yes → keyword token; if no → identifier token.

### Q8. What is input buffering? Why is it needed?
**A:** Input buffering uses two buffers to read the source code in blocks rather than one character at a time, improving I/O efficiency. A **sentinel character** (e.g., `EOF`) marks the end of each buffer to avoid checking for buffer boundaries at every step.

### Q9. What are the error-handling strategies in lexical analysis?
**A:**
- **Panic mode recovery** — delete successive characters until a valid token is found
- **Insert a missing character**
- **Replace an incorrect character**
- **Transpose adjacent characters**

### Q10. What is the difference between a lexer and a parser?
**A:** The lexer deals with **regular languages** (tokens) using finite automata. The parser deals with **context-free languages** (syntax structure) using pushdown automata. The lexer produces tokens; the parser produces a parse tree.

---

## 2. Multi-Pass Macroprocessor (Pass 1)

### Q1. What is a macro?
**A:** A macro is a single-line abbreviation for a group of instructions. It allows code reuse by defining a template that is expanded wherever the macro name is invoked.

### Q2. What is a Macroprocessor?
**A:** A macroprocessor is a system program that replaces each macro invocation (call) with the corresponding sequence of instructions (macro body/definition). It works as a preprocessor before assembly.

### Q3. What is the difference between a macro and a subroutine/function?
**A:**
| Feature | Macro | Subroutine |
|---------|-------|------------|
| Expansion | Inline expansion (code copied) | Control transfer (CALL/RET) |
| Speed | Faster (no call overhead) | Slower (call overhead) |
| Memory | More (duplicated code) | Less (single copy) |
| Time of processing | Assembly time | Execution time |

### Q4. What tables are generated in Pass 1 of the macroprocessor?
**A:**
- **MNT (Macro Name Table):** Stores macro name and a pointer to MDT
- **MDT (Macro Definition Table):** Stores the body of each macro (line by line)
- **MNT Counter (MNTC):** Tracks the current index in MNT
- **MDT Counter (MDTC):** Tracks the current index in MDT
- **ALA (Argument List Array):** Maps formal parameters to positional indicators (#1, #2, etc.)

### Q5. What happens in Pass 1 vs Pass 2?
**A:**
- **Pass 1:** Identifies macro definitions, builds MNT, MDT, and ALA. Separates macro definitions from the rest of the code.
- **Pass 2:** Processes macro calls, expands them using MNT and MDT, and substitutes actual arguments for formal parameters.

### Q6. What are MACRO and MEND directives?
**A:** `MACRO` marks the beginning of a macro definition. `MEND` marks the end. Everything between them is the macro body.

### Q7. What are formal and actual parameters?
**A:**
- **Formal parameters:** Placeholders in the macro definition (e.g., `&ARG1`, `&ARG2`)
- **Actual parameters:** Real values passed during macro invocation that replace formal parameters

### Q8. What is a nested macro?
**A:** A macro definition appearing inside another macro definition. The inner macro is defined only when the outer macro is expanded.

### Q9. What is conditional macro expansion?
**A:** Using directives like `AIF` (Arithmetic IF) and `AGO` (unconditional branch) within macro bodies to conditionally include or exclude lines during expansion.

### Q10. How is a positional parameter different from a keyword parameter?
**A:**
- **Positional:** Matched by position (1st actual → 1st formal)
- **Keyword:** Matched by name (e.g., `&X=5`), order doesn't matter, can have default values

---

## 3. Left Recursion Removal

### Q1. What is left recursion?
**A:** A grammar is left-recursive if a non-terminal `A` can derive a string starting with `A` itself. Directly: `A → Aα | β`. Indirectly: `A → Bα`, `B → Aβ`.

### Q2. Why do we need to remove left recursion?
**A:** Top-down parsers (like recursive descent and LL(1)) **cannot handle left recursion** because it leads to infinite loops — the parser keeps expanding the same non-terminal without consuming any input.

### Q3. How do you remove direct left recursion?
**A:** For `A → Aα₁ | Aα₂ | β₁ | β₂`, replace with:
```
A  → β₁A' | β₂A'
A' → α₁A' | α₂A' | ε
```
We introduce a new non-terminal `A'` and move the recursive part to it with ε (epsilon) as a base case.

### Q4. Give an example of left recursion removal.
**A:**
```
Original:  E → E + T | T
Converted: E  → T E'
           E' → + T E' | ε
```

### Q5. What is indirect left recursion? How do you remove it?
**A:** Indirect: `A → Bα`, `B → Aβ`. To remove:
1. Order non-terminals (A₁, A₂, ... Aₙ)
2. For each Aᵢ, substitute productions of Aⱼ (j < i) into Aᵢ's productions
3. Remove any direct left recursion that results

### Q6. What is the difference between left recursion and right recursion?
**A:**
- **Left recursion:** `A → Aα` (recursive non-terminal is leftmost) — problematic for top-down parsers
- **Right recursion:** `A → αA` (recursive non-terminal is rightmost) — acceptable for top-down parsers

### Q7. Does removing left recursion change the language generated?
**A:** No, the language remains the same. Only the parse tree structure changes (right-recursive trees instead of left-recursive).

### Q8. Can bottom-up parsers handle left recursion?
**A:** Yes! Bottom-up parsers (like LR parsers) can handle left-recursive grammars without any transformation. Left recursion removal is only needed for top-down parsing.

### Q9. What is the time complexity of your program?
**A:** O(n²) in the worst case where n is the number of productions, due to possible substitutions needed for indirect left recursion removal.

### Q10. What happens if β (non-recursive alternative) is missing?
**A:** If all alternatives are left-recursive (e.g., `A → Aα` only), the grammar generates no strings from A and is essentially useless/empty.

---

## 4. Left Factoring

### Q1. What is left factoring?
**A:** Left factoring is a grammar transformation technique used when two or more alternatives of a production share a **common prefix**. We factor out the common prefix to defer the decision until enough input has been seen.

### Q2. Why is left factoring needed?
**A:** Predictive parsers (LL(1)) need to decide which production to use by looking at just one token. If two alternatives start with the same symbol(s), the parser can't decide. Left factoring resolves this ambiguity.

### Q3. How do you perform left factoring?
**A:** For `A → αβ₁ | αβ₂`:
```
A  → αA'
A' → β₁ | β₂
```
Extract the common prefix `α`, introduce a new non-terminal `A'` for the differing suffixes.

### Q4. Give an example.
**A:**
```
Original:  S → iEtS | iEtSeS | a
Left Factored:
           S  → iEtSS' | a
           S' → eS | ε
```
(Here the dangling-else grammar is left factored)

### Q5. What is the difference between left factoring and left recursion removal?
**A:**
| Left Factoring | Left Recursion Removal |
|---|---|
| Removes common prefixes | Removes self-referential derivations |
| Needed when FIRST sets overlap | Needed to prevent infinite loops |
| Defers choice | Eliminates loops |

### Q6. Can left factoring be applied multiple times?
**A:** Yes. After one pass of left factoring, new common prefixes may appear among the newly created productions, requiring further left factoring until no common prefixes remain.

### Q7. Does left factoring guarantee an LL(1) grammar?
**A:** No. Left factoring is a **necessary but not sufficient** condition. The grammar may still not be LL(1) due to other conflicts (e.g., left recursion or ambiguity).

### Q8. What data structure did you use in your program?
**A:** Typically a dictionary/map where keys are non-terminals and values are lists of production alternatives (each alternative is a list of symbols). String comparison is used to find common prefixes.

### Q9. How do you find the longest common prefix among alternatives?
**A:** Compare the alternatives character by character (or symbol by symbol) from left to right. The longest common prefix is the longest initial substring shared by at least two alternatives.

### Q10. Is left factoring mandatory for bottom-up parsers?
**A:** No. Bottom-up parsers (LR parsers) can handle grammars with common prefixes directly. Left factoring is only required for top-down parsers.
