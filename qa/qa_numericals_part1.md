# 🔢 QA ULTIMATE NUMERICAL MASTERCLASS — Part 1 (Module 3)

> ⚠️ All calculations verified step-by-step. Cross-check encouraged.

---

## TYPE 1: SIMPLE LINEAR REGRESSION — Fit ŷ = a + bx, Predict

### Core Formulas:

```
b (slope) = [n∑XY − ∑X·∑Y] / [n∑X² − (∑X)²]

a (intercept) = ȳ − b·x̄

Regression of Y on X:  ŷ = a + bx
Regression of X on Y:  x̂ = a' + b'y

b_yx = r·(σy/σx)       b_xy = r·(σx/σy)
```

---

### ✅ Solved Example 1 — PYQ Paper 4 Q3a

**Q:** Age of cars (X) and maintenance cost in ₹000 (Y). Find regression equation. Predict cost for age = 5.

| Age (X) | 2 | 4 | 6 | 8 |
|---------|---|---|---|---|
| Cost (Y) | 10 | 20 | 25 | 30 |

**Step 1: Compute sums (n = 4)**

| X | Y | XY | X² |
|---|---|----|----|
| 2 | 10 | 20 | 4 |
| 4 | 20 | 80 | 16 |
| 6 | 25 | 150 | 36 |
| 8 | 30 | 240 | 64 |
| **∑X = 20** | **∑Y = 85** | **∑XY = 490** | **∑X² = 120** |

x̄ = 20/4 = **5**, ȳ = 85/4 = **21.25**

**Step 2: Calculate b (slope)**
```
b = [n∑XY − ∑X·∑Y] / [n∑X² − (∑X)²]
  = [4(490) − 20(85)] / [4(120) − (20)²]
  = [1960 − 1700] / [480 − 400]
  = 260 / 80
  = 3.25
```

**Step 3: Calculate a (intercept)**
```
a = ȳ − b·x̄ = 21.25 − 3.25(5) = 21.25 − 16.25 = 5.0
```

**Regression Equation: ŷ = 5 + 3.25X**

**Step 4: Prediction for X = 5**
```
ŷ = 5 + 3.25(5) = 5 + 16.25 = 21.25 (i.e., ₹21,250)
```

---

### ✅ Solved Example 2 — PYQ Dec 2022 Q4a (Correlation + Regression + Prediction)

**Q:** Test scores and sales data for 9 salesmen. Find (a) correlation coefficient, (b) Does it justify termination? (c) Min test score for ₹30,000 sales, (d) Predicted sales for score = 28.

| Test Score (X) | 14 | 19 | 24 | 21 | 26 | 22 | 15 | 20 | 18 |
|---|---|---|---|---|---|---|---|---|---|
| Sales Y (₹000) | 31 | 36 | 48 | 37 | 50 | 45 | 33 | 41 | 39 |

**Step 1: Compute all sums (n = 9)**

| X | Y | XY | X² | Y² |
|---|---|----|----|-----|
| 14 | 31 | 434 | 196 | 961 |
| 19 | 36 | 684 | 361 | 1296 |
| 24 | 48 | 1152 | 576 | 2304 |
| 21 | 37 | 777 | 441 | 1369 |
| 26 | 50 | 1300 | 676 | 2500 |
| 22 | 45 | 990 | 484 | 2025 |
| 15 | 33 | 495 | 225 | 1089 |
| 20 | 41 | 820 | 400 | 1681 |
| 18 | 39 | 702 | 324 | 1521 |
| **∑X=179** | **∑Y=360** | **∑XY=7354** | **∑X²=3683** | **∑Y²=14746** |

x̄ = 179/9 = **19.889**, ȳ = 360/9 = **40**

**Step 2: Correlation Coefficient (r)**
```
Numerator = n∑XY − ∑X·∑Y = 9(7354) − 179(360) = 66186 − 64440 = 1746

Denom₁ = n∑X² − (∑X)² = 9(3683) − (179)² = 33147 − 32041 = 1106
Denom₂ = n∑Y² − (∑Y)² = 9(14746) − (360)² = 132714 − 129600 = 3114

r = 1746 / √(1106 × 3114)
  = 1746 / √(3,444,084)
  = 1746 / 1855.83
  = 0.941
```

**r ≈ 0.941** → Strong positive correlation. **Yes, termination is justified** — low test scores strongly correlate with low sales.

**Step 3: Regression of Y on X**
```
b_yx = 1746 / 1106 = 1.5786
a = ȳ − b·x̄ = 40 − 1.5786(19.889) = 40 − 31.39 = 8.61

ŷ = 8.61 + 1.579X
```

**Step 4: Min test score for ₹30,000 sales (Y = 30)**
```
30 = 8.61 + 1.579X
X = (30 − 8.61) / 1.579 = 21.39 / 1.579 = 13.55 ≈ 14
```
**Minimum test score ≈ 14**

**Step 5: Predicted sales for X = 28**
```
ŷ = 8.61 + 1.579(28) = 8.61 + 44.21 = 52.82
```
**Predicted sales ≈ ₹52,820**

---

## TYPE 2: CORRELATION COEFFICIENT FROM RAW DATA

### Core Formula (Karl Pearson):
```
        n∑XY − ∑X·∑Y
r = ─────────────────────────────────
    √[n∑X² − (∑X)²] × √[n∑Y² − (∑Y)²]
```

> Already solved in Example 2 above (r = 0.941).

---

### ✅ Solved Example 3 — PYQ Paper 3 Q4a Style

**Q:** Find two regression coefficients, two regression equations, correlation coefficient, and predict Y when X = 30.

| Economics (X) | 25 | 28 | 35 | 32 | 31 | 36 | 29 | 38 | 34 | 32 |
|---|---|---|---|---|---|---|---|---|---|---|
| Statistics (Y) | 43 | 46 | 49 | 41 | 36 | 32 | 31 | 30 | 33 | 39 |

**Step 1: Compute sums (n = 10)**

| X | Y | XY | X² | Y² |
|---|---|----|----|-----|
| 25 | 43 | 1075 | 625 | 1849 |
| 28 | 46 | 1288 | 784 | 2116 |
| 35 | 49 | 1715 | 1225 | 2401 |
| 32 | 41 | 1312 | 1024 | 1681 |
| 31 | 36 | 1116 | 961 | 1296 |
| 36 | 32 | 1152 | 1296 | 1024 |
| 29 | 31 | 899 | 841 | 961 |
| 38 | 30 | 1140 | 1444 | 900 |
| 34 | 33 | 1122 | 1156 | 1089 |
| 32 | 39 | 1248 | 1024 | 1521 |
| **∑=320** | **∑=380** | **∑=12067** | **∑=10380** | **∑=14838** |

x̄ = 320/10 = **32**, ȳ = 380/10 = **38**

**Step 2: Intermediate values**
```
n∑XY − ∑X·∑Y = 10(12067) − 320(380) = 120670 − 121600 = −930
n∑X² − (∑X)² = 10(10380) − (320)² = 103800 − 102400 = 1400
n∑Y² − (∑Y)² = 10(14838) − (380)² = 148380 − 144400 = 3980
```

**Step 3: Regression coefficients**
```
b_yx = −930 / 1400 = −0.6643
b_xy = −930 / 3980 = −0.2337
```

**Step 4: Correlation coefficient**
```
r = ±√(b_yx × b_xy) = ±√(−0.6643 × −0.2337) = ±√(0.1552) = ±0.394
Both b values are negative → r = −0.394
```

**Step 5: Regression equations**
```
Y on X:  Y − ȳ = b_yx(X − x̄)
         Y − 38 = −0.6643(X − 32)
         Y = 38 − 0.6643X + 21.26
         Y = 59.26 − 0.6643X

X on Y:  X − x̄ = b_xy(Y − ȳ)
         X − 32 = −0.2337(Y − 38)
         X = 32 − 0.2337Y + 8.88
         X = 40.88 − 0.2337Y
```

**Step 6: Predict Y when X = 30**
```
Y = 59.26 − 0.6643(30) = 59.26 − 19.93 = 39.33
```

---

## TYPE 3: FROM TWO REGRESSION LINES → FIND r, MEANS

### Core Method:
1. Both regression lines pass through **(x̄, ȳ)** — solve simultaneously for means
2. Identify which line is Y-on-X and which is X-on-Y by trying both and checking **|r| ≤ 1**
3. **r² = b_yx × b_xy** (sign of r = sign of regression coefficients)

---

### ✅ Solved Example 4 — PYQ Paper 3 Q3b

**Q:** Regression lines are: 2X − 8 = 3Y and 2Y − 5 = X. Find r.

Rewrite:
- Line 1: 2X − 3Y = 8
- Line 2: X − 2Y = −5

**Step 1: Find means (x̄, ȳ)**
```
2x̄ − 3ȳ = 8     ...(1)
x̄ − 2ȳ = −5      ...(2)

From (2): x̄ = 2ȳ − 5
Sub in (1): 2(2ȳ − 5) − 3ȳ = 8
            4ȳ − 10 − 3ȳ = 8
            ȳ = 18
            x̄ = 2(18) − 5 = 31
```
**x̄ = 31, ȳ = 18**

**Step 2: Identify lines (try both assignments)**

**Try A:** Line 1 = Y on X, Line 2 = X on Y
```
Line 1: 3Y = 2X − 8 → Y = (2/3)X − 8/3     → b_yx = 2/3
Line 2: X = 2Y − 5                            → b_xy = 2
r² = (2/3)(2) = 4/3 > 1 → ❌ IMPOSSIBLE
```

**Try B:** Line 1 = X on Y, Line 2 = Y on X
```
Line 1: 2X = 3Y + 8 → X = (3/2)Y + 4         → b_xy = 3/2
Line 2: 2Y = X + 5 → Y = (1/2)X + 5/2        → b_yx = 1/2
r² = (3/2)(1/2) = 3/4 = 0.75 → ✅ VALID
```

**Step 3: Calculate r**
```
r = +√(3/4) = +0.866
(Positive because both b values are positive)
```

**Answer: r = +0.866, x̄ = 31, ȳ = 18**

---

### ✅ Solved Example 5 — PYQ Paper 4 Q2a

**Q:** Regression lines are 2x − y + 1 = 0 and 3x − 2y + 7 = 0. Find means, regression coefficients, and r.

**Step 1: Find means**
```
2x̄ − ȳ + 1 = 0  →  2x̄ − ȳ = −1    ...(1)
3x̄ − 2ȳ + 7 = 0  →  3x̄ − 2ȳ = −7   ...(2)

Multiply (1) by 2: 4x̄ − 2ȳ = −2     ...(3)
(3) − (2): 4x̄ − 2ȳ − 3x̄ + 2ȳ = −2 + 7
            x̄ = 5
From (1): 2(5) − ȳ = −1 → ȳ = 11
```
**x̄ = 5, ȳ = 11**

**Step 2: Identify lines**

**Try A:** Line 1 = Y on X, Line 2 = X on Y
```
Line 1: y = 2x + 1         → b_yx = 2
Line 2: x = (2/3)y − 7/3   → b_xy = 2/3
r² = 2 × 2/3 = 4/3 > 1 → ❌ IMPOSSIBLE
```

**Try B:** Line 1 = X on Y, Line 2 = Y on X
```
Line 1: x = (1/2)y − 1/2   → b_xy = 1/2
Line 2: y = (3/2)x + 7/2   → b_yx = 3/2
r² = (1/2)(3/2) = 3/4 → ✅ VALID
```

**Step 3: Calculate r**
```
r = +√(3/4) = +0.866
(Both b values positive → r is positive)
```

**Answer: x̄ = 5, ȳ = 11, b_yx = 3/2, b_xy = 1/2, r = +0.866**

---

### ✅ Solved Example 6 — Additional Practice

**Q:** Regression lines: 4x − 5y + 33 = 0 and 20x − 9y − 107 = 0. Find r, means, and σy/σx if σx = 3.

**Step 1: Means**
```
4x̄ − 5ȳ = −33    ...(1)
20x̄ − 9ȳ = 107   ...(2)

Multiply (1) by 5: 20x̄ − 25ȳ = −165  ...(3)
(2) − (3): −9ȳ + 25ȳ = 107 + 165
            16ȳ = 272 → ȳ = 17
From (1): 4x̄ = −33 + 85 = 52 → x̄ = 13
```

**Step 2: Identify lines**

**Try A:** Line 1 = Y on X, Line 2 = X on Y
```
Line 1: 5y = 4x + 33 → y = (4/5)x + 33/5  → b_yx = 4/5 = 0.8
Line 2: 20x = 9y + 107 → x = (9/20)y + 107/20 → b_xy = 9/20 = 0.45
r² = 0.8 × 0.45 = 0.36 → ✅ VALID
```

**Try B:** Line 1 = X on Y, Line 2 = Y on X
```
Line 1: x = (5/4)y − 33/4 → b_xy = 5/4 = 1.25
Line 2: y = (20/9)x − 107/9 → b_yx = 20/9 = 2.222
r² = 1.25 × 2.222 = 2.778 > 1 → ❌ IMPOSSIBLE
```

**So Try A is correct.**
```
r = +√0.36 = +0.6

b_yx = r × σy/σx → 0.8 = 0.6 × σy/3 → σy = 0.8 × 3/0.6 = 4
```

**Answer: x̄ = 13, ȳ = 17, r = 0.6, σy = 4**
