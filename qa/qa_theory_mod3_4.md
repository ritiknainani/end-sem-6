# 📘 QA ULTIMATE FULL-MARKS THEORY GUIDE — Modules 3 & 4

---

# MODULE 3: INTRODUCTION TO REGRESSION

---

## Q11. Explain Regression and its Types. Discuss its Applications. [10 Marks] — 3/5

### a) Core Concept
**Regression analysis** is a statistical technique used to establish a **mathematical relationship** between a dependent variable (Y) and one or more independent variables (X₁, X₂, ...) for the purpose of **prediction and estimation**.

### b) Types of Regression

| Type | Equation | When Used |
|------|----------|-----------|
| **Simple Linear** | ŷ = a + bX | One predictor, linear relationship |
| **Multiple Linear** | ŷ = a + b₁X₁ + b₂X₂ + ... | Multiple predictors, linear |
| **Polynomial** | ŷ = a + b₁X + b₂X² + ... | Curvilinear relationship |
| **Logistic** | P = 1/(1+e^−(a+bX)) | Binary dependent variable (0/1) |

### Two Regression Lines:
```
Y on X:  Y = a + b_yx · X     (used to predict Y given X)
X on Y:  X = a' + b_xy · Y    (used to predict X given Y)

Both lines pass through the point (x̄, ȳ)
```

### c) Diagram — Regression Line
```
Y ▲
  │         *    /
  │       *   / ← Best fit line (ŷ = a + bx)
  │     *  /  *
  │   * /  *
  │  / *
  │/ *       Residual eᵢ = yᵢ − ŷᵢ
  │           (vertical distance to line)
  └──────────────────────► X
     a = Y-intercept
     b = slope (rise/run)
```

### d) Key Formulas
```
b_yx = [n∑XY − ∑X∑Y] / [n∑X² − (∑X)²]     (slope of Y on X)
b_xy = [n∑XY − ∑X∑Y] / [n∑Y² − (∑Y)²]     (slope of X on Y)
a = ȳ − b_yx · x̄                            (intercept)
r² = b_yx × b_xy                             (coefficient of determination)
r = ±√(b_yx × b_xy)                          (correlation coefficient)
```

### e) Applications
1. **Sales Forecasting:** Predicting future sales based on advertising spend, pricing, and economic indicators
2. **Real Estate:** Estimating house prices from area, location, number of rooms
3. **Medical Research:** Relating drug dosage to patient recovery time
4. **Quality Control:** Predicting defect rate from process parameters (temperature, pressure)
5. **Economics:** Estimating GDP growth from investment, consumption, and government spending

---

## Q12. Differentiate between Regression and Correlation. [5-10 Marks]

### f) Comparison Table

| Parameter | Regression | Correlation |
|-----------|-----------|-------------|
| **Purpose** | **Prediction** — estimate Y from X | **Measurement** — strength/direction of relationship |
| **Output** | An **equation** (ŷ = a + bx) | A **coefficient** (r) between −1 and +1 |
| **Causation** | Implies cause-effect (X influences Y) | Only measures association, not causation |
| **Symmetry** | **Asymmetric** — regression of Y on X ≠ regression of X on Y | **Symmetric** — r(X,Y) = r(Y,X) |
| **Number of lines** | Two lines (Y on X and X on Y) | Single coefficient |
| **Variables** | Dependent (Y) and Independent (X) | Both variables treated equally |
| **Scope** | Can predict specific values | Cannot predict; only shows strength |

---

## Q13. Explain the Least Squares Method of Regression. [10 Marks]

### a) Core Concept
The **method of least squares** finds the regression line that minimizes the **sum of squared residuals** (vertical distances between observed and predicted values).

### d) Derivation

Minimize: S = ∑(yᵢ − a − bxᵢ)²

Take partial derivatives and set to zero:
```
∂S/∂a = −2∑(yᵢ − a − bxᵢ) = 0
→ ∑yᵢ = na + b∑xᵢ                    (Normal Equation 1)

∂S/∂b = −2∑xᵢ(yᵢ − a − bxᵢ) = 0
→ ∑xᵢyᵢ = a∑xᵢ + b∑xᵢ²             (Normal Equation 2)

Solving simultaneously:
b = [n∑xy − ∑x∑y] / [n∑x² − (∑x)²]
a = ȳ − bx̄
```

**Why squared (not absolute)?**
- Mathematically differentiable → closed-form solution exists
- Penalizes large deviations more heavily
- Has desirable statistical properties (BLUE — Best Linear Unbiased Estimator under Gauss-Markov conditions)

---

## Q14. Explain the meaning of Intercept, Slope, and Error Term. [5-10 Marks]

### b) Detailed Explanation

**Model:** Y = β₀ + β₁X + ε

| Component | Symbol | Meaning |
|-----------|--------|---------|
| **Intercept (β₀)** | a | Value of Y when X = 0. Represents the **baseline** level of Y |
| **Slope (β₁)** | b | Change in Y for a **one-unit increase** in X. Measures the **rate of change** |
| **Error Term (ε)** | eᵢ = yᵢ − ŷᵢ | Captures the variation in Y **not explained** by the model — includes measurement error, omitted variables, and random variation |

**Properties of Error Term:**
- E(ε) = 0 — Errors average to zero
- Var(ε) = σ² — Constant variance (homoscedasticity)
- Errors are independent of each other (no autocorrelation)
- Errors are normally distributed (for inference purposes)

---

## Q15. Explain R² and measures of model fit: MAE, MAPE. [5-10 Marks] — 2/5

### a) Core Concept
**Measures of model fit** quantify how well the regression model explains the variation in the dependent variable and how accurate its predictions are.

### d) Formulas

**R² (Coefficient of Determination):**
```
R² = SSR / SST = 1 − (SSE / SST)

Where:
SST = ∑(yᵢ − ȳ)²         (Total variation)
SSR = ∑(ŷᵢ − ȳ)²         (Explained variation)
SSE = ∑(yᵢ − ŷᵢ)²        (Unexplained/residual variation)
SST = SSR + SSE

Range: 0 ≤ R² ≤ 1
R² = 0.85 means 85% of variation in Y is explained by X
```

```
┌──────────────────────────────────────────────┐
│ Total Variation (SST) = SSR + SSE            │
│ ┌─────────────────────┬────────────────────┐ │
│ │ Explained by Model  │  Unexplained       │ │
│ │    (SSR)            │   (SSE/Residual)   │ │
│ │    R² = SSR/SST     │   1−R² = SSE/SST   │ │
│ └─────────────────────┴────────────────────┘ │
└──────────────────────────────────────────────┘
```

**MAE (Mean Absolute Error):**
```
MAE = (1/n) × ∑|yᵢ − ŷᵢ|
- Average of absolute prediction errors
- In the same units as Y
- Lower is better
```

**MAPE (Mean Absolute Percentage Error):**
```
MAPE = (1/n) × ∑(|yᵢ − ŷᵢ| / |yᵢ|) × 100%
- Expressed as percentage — easy to interpret across scales
- MAPE < 10% → Excellent model
- MAPE 10-20% → Good model
- MAPE > 50% → Poor model
```

---

## Q16. Justify or contradict: "b_yx and b_xy must be either positive or negative." [5 Marks] — Dec 2024

### a) Core Concept
The statement is **TRUE** — both regression coefficients must always carry the **same algebraic sign**.

### d) Mathematical Proof
```
r² = b_yx × b_xy

Since r² ≥ 0 (square of a real number is always non-negative):
→ b_yx × b_xy ≥ 0

This product is non-negative ONLY when:
  • Both b_yx > 0 and b_xy > 0   (both positive)
  • Both b_yx < 0 and b_xy < 0   (both negative)
  • One or both are zero          (no linear relationship)

They CANNOT have opposite signs because that would make r² < 0,
which is mathematically impossible.

Also: r = ±√(b_yx × b_xy)
The sign of r equals the common sign of b_yx and b_xy.
```

---

# MODULE 4: INTRODUCTION TO MULTIPLE LINEAR REGRESSION

---

## Q17. Explain the Multiple Linear Regression Model. What are its assumptions? [10 Marks] — 4/5

### a) Core Concept
**Multiple Linear Regression (MLR)** models the relationship between one dependent variable (Y) and **two or more** independent variables (X₁, X₂, ..., Xₖ) simultaneously.

### d) Model and Normal Equations

**Model:** ŷ = a + b₁X₁ + b₂X₂ (for k=2)

**Normal Equations (k=2):**
```
∑Y   = na    + b₁∑X₁   + b₂∑X₂           ...(I)
∑X₁Y = a∑X₁ + b₁∑X₁²  + b₂∑X₁X₂         ...(II)
∑X₂Y = a∑X₂ + b₁∑X₁X₂ + b₂∑X₂²          ...(III)

Solve 3 equations for 3 unknowns: a, b₁, b₂
```

### Assumptions (CLRM — Classical Linear Regression Model):
1. **Linearity:** Y is a linear function of X₁, X₂, ..., Xₖ
2. **No multicollinearity:** Independent variables are not highly correlated with each other (|r| between any two X's should be < 0.8)
3. **Homoscedasticity:** Variance of error terms is constant: Var(εᵢ) = σ² for all i
4. **No autocorrelation:** Error terms are independent: Cov(εᵢ, εⱼ) = 0 for i ≠ j
5. **Normality of errors:** εᵢ ~ N(0, σ²) — errors are normally distributed
6. **No specification error:** The model includes all relevant variables and the correct functional form
7. **n > k:** Number of observations exceeds number of parameters

---

## Q18. Explain F-test for Overall Significance of Regression Model. [5-10 Marks] — 4/5

### a) Core Concept
The **F-test** determines whether the regression model as a whole is statistically significant — i.e., whether at least one predictor variable has a non-zero coefficient.

### b) Hypotheses and Procedure
```
H₀: β₁ = β₂ = ... = βₖ = 0  (No predictor is significant)
H₁: At least one βᵢ ≠ 0      (At least one predictor matters)
```

### d) Formula
```
         MSR        SSR / k          R² / k
F = ────────── = ──────────── = ─────────────────
         MSE        SSE/(n-k-1)    (1-R²)/(n-k-1)

Where:
k = number of predictors
n = number of observations
MSR = Mean Square Regression
MSE = Mean Square Error

Decision Rule:
If F_calc > F_table(α, df₁=k, df₂=n-k-1) → REJECT H₀
→ Model is statistically significant
```

### c) Decision Diagram
```
                    F Distribution
                      ╱╲
                     ╱  ╲
                    ╱    ╲
                   ╱      ╲___________
                  ╱                    ╲
─────────────────┼────────────────────┼─────
              Accept H₀           F_critical
              (Model not            │
               significant)     Reject H₀
                              (Model IS significant)

If F_calc falls in the rejection region → Model is significant
```

---

## Q19. Explain Partial Correlation Coefficient in detail. [10 Marks] — 4/5

### a) Core Concept
**Partial correlation** measures the strength and direction of linear relationship between two variables **after removing (controlling for) the effect of one or more other variables**.

### d) Formulas
```
              r₁₂ − r₁₃ · r₂₃
r₁₂.₃ = ─────────────────────────────
         √(1 − r₁₃²) · √(1 − r₂₃²)

Interpretation: Correlation between X₁ and X₂
                after removing the effect of X₃

Similarly:
              r₁₃ − r₁₂ · r₂₃
r₁₃.₂ = ─────────────────────────────
         √(1 − r₁₂²) · √(1 − r₂₃²)

Multiple Correlation Coefficient:
R₁.₂₃ = √[1 − (1 − r₁₂²)(1 − r₁₃.₂²)]
```

### e) Application
In medical research: Studying the relationship between exercise (X₁) and weight loss (X₂) while controlling for diet quality (X₃). Simple correlation might show exercise-weight loss relationship, but part of it might be because people who exercise also tend to eat better. Partial correlation isolates the pure exercise effect.

### Properties:
- −1 ≤ r₁₂.₃ ≤ +1
- If r₁₂.₃ ≈ 0 but r₁₂ is high → the apparent relationship between X₁ and X₂ was actually due to X₃ (spurious correlation)
- If r₁₂.₃ ≈ r₁₂ → X₃ has no confounding effect
