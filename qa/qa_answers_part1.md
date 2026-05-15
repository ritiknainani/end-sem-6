# 📝 QA Complete Answer Guide — Part 1 (TIER 1 & 2)

---

## 1. 📌 SIMPLE LINEAR REGRESSION [10 Marks] — 🔴 GUARANTEED (4/4)

### Theory:

**Regression** = technique to find the **best-fit line** describing the relationship between a dependent variable (Y) and independent variable (X).

**Regression equation:** ŷ = a + bx

Where:
- **b** (slope/regression coefficient) = n∑xy - (∑x)(∑y) / n∑x² - (∑x)²
- **a** (intercept) = ȳ - bx̄

### Alternative Formulas for Regression Coefficients:

**b_yx** (regression of Y on X) = r × (σy/σx) = [n∑xy - ∑x∑y] / [n∑x² - (∑x)²]

**b_xy** (regression of X on Y) = r × (σx/σy) = [n∑xy - ∑x∑y] / [n∑y² - (∑y)²]

### Key Properties:
- **r² = b_yx × b_xy** (product of regression coefficients = r²)
- Both regression coefficients have the **same sign**
- If b_yx > 1, then b_xy < 1 (and vice versa)
- Regression line of Y on X passes through (x̄, ȳ)

### Worked Example:

Given data:

| X | 2 | 4 | 6 | 8 |
|---|---|---|---|---|
| Y | 10 | 20 | 25 | 30 |

**Step 1: Calculate sums**

| X | Y | XY | X² | Y² |
|---|---|----|----|-----|
| 2 | 10 | 20 | 4 | 100 |
| 4 | 20 | 80 | 16 | 400 |
| 6 | 25 | 150 | 36 | 625 |
| 8 | 30 | 240 | 64 | 900 |
| **∑X=20** | **∑Y=85** | **∑XY=490** | **∑X²=120** | **∑Y²=2025** |

n = 4, x̄ = 20/4 = 5, ȳ = 85/4 = 21.25

**Step 2: Calculate b (slope)**
b = [n∑XY - ∑X∑Y] / [n∑X² - (∑X)²]
b = [4(490) - (20)(85)] / [4(120) - (20)²]
b = [1960 - 1700] / [480 - 400]
b = 260/80 = **3.25**

**Step 3: Calculate a (intercept)**
a = ȳ - bx̄ = 21.25 - 3.25(5) = 21.25 - 16.25 = **5**

**Regression equation: ŷ = 5 + 3.25x**

**Prediction:** If X = 5, ŷ = 5 + 3.25(5) = **21.25**

---

## 2. 📌 CORRELATION COEFFICIENT [10 Marks] — 🔴 GUARANTEED (4/4)

### Karl Pearson's Correlation Coefficient:

```
        n∑xy - (∑x)(∑y)
r = ─────────────────────────────────
    √[n∑x² - (∑x)²] × √[n∑y² - (∑y)²]
```

### Properties:
- **-1 ≤ r ≤ +1**
- r = +1: Perfect positive correlation
- r = -1: Perfect negative correlation
- r = 0: No linear correlation
- **r² = b_yx × b_xy** (from regression coefficients)

### From Regression Lines:

If two regression lines are given, e.g.:
- Line 1: ax + by + c = 0 → Y on X: y = (-a/b)x + (-c/b) → b_yx = -a/b
- Line 2: dx + ey + f = 0 → X on Y: x = (-e/d)y + (-f/d) → b_xy = -e/d

Then: **r = ±√(b_yx × b_xy)** (sign = sign of regression coefficients)

### Worked Example — Finding r from Regression Lines:

Given: 2X - 3Y - 6 = 0 and 2Y - 5X + 10 = 0

**Line 1 (Y on X):** 2X - 3Y - 6 = 0 → Y = (2/3)X - 2 → **b_yx = 2/3**

**Line 2 (X on Y):** 2Y - 5X + 10 = 0 → X = (2/5)Y + 2 → **b_xy = 2/5**

**r = ±√(b_yx × b_xy)** = ±√(2/3 × 2/5) = ±√(4/15) = ±**0.516**

Since both b_yx and b_xy are positive → **r = +0.516**

**Finding means (x̄, ȳ):** Both lines pass through (x̄, ȳ). Solve simultaneously:
- 2x̄ - 3ȳ = 6 ...(1)
- 5x̄ - 2ȳ = 10 ...(2)

Solving: x̄ = **18/11**, ȳ = **-10/11**

### Interpreting Correlation:
| Value of r | Interpretation |
|-----------|----------------|
| 0.00 – 0.25 | Very weak |
| 0.25 – 0.50 | Weak |
| 0.50 – 0.75 | Moderate |
| 0.75 – 0.90 | Strong |
| 0.90 – 1.00 | Very strong |

---

## 3. 📌 MULTIPLE LINEAR REGRESSION (MLR) [10 Marks] — 🟠 VERY HIGH (3/4)

### Theory:

**MLR** models the relationship between ONE dependent variable (Y) and TWO or more independent variables (X₁, X₂, ...).

**Equation:** ŷ = a + b₁x₁ + b₂x₂

### Normal Equations (for 2 predictors):

```
∑Y = na + b₁∑X₁ + b₂∑X₂              ...(1)
∑X₁Y = a∑X₁ + b₁∑X₁² + b₂∑X₁X₂      ...(2)
∑X₂Y = a∑X₂ + b₁∑X₁X₂ + b₂∑X₂²      ...(3)
```

Solve these 3 equations simultaneously for a, b₁, b₂.

### Coefficient of Multiple Determination (R²):

```
R² = (b₁∑X₁Y + b₂∑X₂Y + na² + 2ab₁∑X₁ + 2ab₂∑X₂ + 2b₁b₂∑X₁X₂ - nȳ²) / (∑Y² - nȳ²)
```

**Simplified (using deviations):**
```
        SSR (Regression Sum of Squares)
R² = ──────────────────────────────────
        SST (Total Sum of Squares)

Where: SST = ∑Y² - nȳ²
       SSR = b₁∑x₁y + b₂∑x₂y  (using deviations from mean)
       SSE = SST - SSR
```

- R² ranges from **0 to 1**
- R² = 0.85 means 85% of variation in Y is explained by X₁ and X₂

### F-test for Significance of Regression:

```
        R²/k
F = ──────────────
    (1-R²)/(n-k-1)

k = number of predictors
n = number of observations
```

**Decision:** If F_calculated > F_table → Regression is **significant** (reject H₀)

### Assumptions of MLR:
1. Linear relationship between Y and X's
2. **No multicollinearity** (predictors not highly correlated)
3. Errors are **normally distributed**
4. **Homoscedasticity** (constant variance of errors)
5. Errors are **independent** (no autocorrelation)
6. Sample size should be sufficiently large

---

## 4. 📌 POINT ESTIMATION PROPERTIES [5-10 Marks] — 🟠 VERY HIGH (3/4)

### What is Point Estimation?
Using a **single value** (statistic) computed from sample data to estimate an **unknown population parameter**.

Example: Sample mean x̄ is a point estimator of population mean μ.

### Desirable Properties:

#### 1. Unbiasedness
An estimator T is **unbiased** if:
```
E(T) = θ   (expected value equals true parameter)
```
- **Bias = E(T) - θ**
- If Bias = 0 → Unbiased
- **Example:** Sample mean x̄ is unbiased for μ: E(x̄) = μ ✅
- **Example:** S² = ∑(xᵢ-x̄)²/(n-1) is unbiased for σ² ✅
- Note: ∑(xᵢ-x̄)²/n is BIASED (divide by n-1 to correct)

#### 2. Consistency
An estimator T_n is **consistent** if it converges to the true parameter as sample size increases:
```
As n → ∞: P(|Tₙ - θ| < ε) → 1
```
- Larger samples give better estimates
- **Example:** x̄ is consistent for μ (Var(x̄) = σ²/n → 0 as n→∞)

#### 3. Efficiency
Among all unbiased estimators, the one with **minimum variance** is most efficient.
```
Efficiency = Var(T₁)/Var(T₂)
```
- **Cramér-Rao Lower Bound:** Var(T) ≥ 1/I(θ) where I(θ) is Fisher information
- An estimator achieving this bound is **efficient**

#### 4. Sufficiency
An estimator T is **sufficient** for θ if it captures **all information** in the sample about θ.
```
By Fisher-Neyman Factorization Theorem:
f(x₁,...,xₙ|θ) = g(T,θ) × h(x₁,...,xₙ)
```
If the likelihood can be factored as above → T is sufficient.

---

## 5. 📌 PARTIAL CORRELATION COEFFICIENT [5-10 Marks] — 🟠 VERY HIGH (3/4)

### Definition:
Measures the correlation between two variables **after removing the effect** of one or more other variables.

### Formula (for 3 variables):

```
              r₁₂ - r₁₃ × r₂₃
r₁₂.₃ = ─────────────────────────────
          √(1 - r₁₃²) × √(1 - r₂₃²)

Similarly:
              r₁₃ - r₁₂ × r₂₃
r₁₃.₂ = ─────────────────────────────
          √(1 - r₁₂²) × √(1 - r₂₃²)

              r₂₃ - r₁₂ × r₁₃
r₂₃.₁ = ─────────────────────────────
          √(1 - r₁₂²) × √(1 - r₁₃²)
```

### Multiple Correlation Coefficient:

```
R₁.₂₃ = √(1 - (1-r₁₂²)(1-r₁₃.₂²))

Or: R₁.₂₃ = √[(r₁₂² + r₁₃² - 2r₁₂·r₁₃·r₂₃) / (1 - r₂₃²)]
```

### Worked Example:

Given: r₁₂ = 0.7, r₁₃ = 0.61, r₂₃ = 0.4

**r₁₂.₃:**
= (0.7 - 0.61 × 0.4) / √(1 - 0.61²) × √(1 - 0.4²)
= (0.7 - 0.244) / √(1 - 0.3721) × √(1 - 0.16)
= 0.456 / (√0.6279 × √0.84)
= 0.456 / (0.7924 × 0.9165)
= 0.456 / 0.7263
= **0.628**

**r₁₃.₂:**
= (0.61 - 0.7 × 0.4) / √(1 - 0.7²) × √(1 - 0.4²)
= (0.61 - 0.28) / (√0.51 × √0.84)
= 0.33 / (0.7141 × 0.9165)
= 0.33 / 0.6544
= **0.504**

---

## 6. 📌 DEFINE STATISTICS + USES + LIMITATIONS [5-10 Marks] — 🟠 (3/4)

### Definition:
**Statistics** is the science of **collecting, organizing, presenting, analyzing, and interpreting** numerical data to make decisions under uncertainty.

> "Statistics is the science of estimates and probabilities." — Boddington

### Uses of Statistics:
1. **Business & Trade**: Demand forecasting, quality control, market research
2. **Economics**: National income, inflation analysis, GDP estimation
3. **Medicine**: Drug testing, clinical trials, epidemiology
4. **Government**: Census, policy planning, budget allocation
5. **Research**: Hypothesis testing, experimental design, data analysis
6. **Banking**: Risk assessment, credit scoring, fraud detection
7. **Education**: Performance analysis, grading systems

### Functions:
1. **Simplifies complex data** → tables, graphs, averages
2. **Facilitates comparison** → between groups, time periods
3. **Tests hypotheses** → validates claims scientifically
4. **Predicts trends** → regression, time series
5. **Measures uncertainty** → probability, confidence intervals

### Limitations:
1. **Deals with aggregates only** — cannot study individual cases
2. **Deals with quantitative data only** — qualitative data needs coding
3. **Results are averages** — may not apply to specific cases
4. **Can be misused** — "There are lies, damned lies, and statistics"
5. **Requires homogeneous data** — comparison of unlike groups is invalid
6. **Statistical laws are not exact** — they are approximations
7. **Doesn't reveal causes** — only shows associations/correlations
