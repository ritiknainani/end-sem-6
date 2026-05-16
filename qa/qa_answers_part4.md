# 📝 QA Answer Guide — Part 4 (Dec 2024 Paper Additions)

---

## ✅ SOLVED: Dec 2024 Q2a — Finding Mean & r from Regression Equation

**Q:** For 100 students, regression equation of Statistics (X) and Economics (Y) is 3Y − 5X + 180 = 0. Mean marks in Economics = 50, Var(X) = (4/9)Var(Y). Find mean marks in Statistics and correlation coefficient.

**Step 1: Find mean of X (Statistics)**

Both regression lines pass through (x̄, ȳ). Given ȳ = 50:
```
3(50) − 5x̄ + 180 = 0
150 − 5x̄ + 180 = 0
330 = 5x̄
x̄ = 66
```
**Mean marks in Statistics = 66**

**Step 2: Identify the regression line**

Equation: 3Y − 5X + 180 = 0

As Y on X: Y = (5/3)X − 60 → b_yx = 5/3
As X on Y: X = (3/5)Y + 36 → b_xy = 3/5

Given: σ_x² = (4/9)σ_y² → σ_x/σ_y = 2/3

**Try Y on X:** b_yx = r(σ_y/σ_x) → 5/3 = r(3/2) → r = 10/9 > 1 → ❌ IMPOSSIBLE

**Try X on Y:** b_xy = r(σ_x/σ_y) → 3/5 = r(2/3) → r = (3/5)(3/2) = **9/10 = 0.9** ✅

**Answer: x̄ = 66, r = 0.9**

---

## ✅ SOLVED: Dec 2024 Q4a — MLR (Sales Territory Data)

**Q:** Fit ŷ = a + b₁X₁ + b₂X₂. Find R². Test significance (F = 13.274, α = 0.01).

| Territory | Y (Sales, Lakh ₹) | X₁ (Advt, ₹000) | X₂ (Agents) |
|---|---|---|---|
| 1 | 190 | 80 | 40 |
| 2 | 80 | 35 | 13 |
| 3 | 75 | 35 | 7 |
| 4 | 100 | 50 | 20 |
| 5 | 125 | 60 | 19 |
| 6 | 90 | 40 | 13 |
| 7 | 70 | 20 | 20 |
| 8 | 130 | 60 | 28 |

**n = 8, k = 2**

**Step 1: Compute sums**
```
∑Y = 860       ∑X₁ = 380      ∑X₂ = 160
∑X₁Y = 45925   ∑X₂Y = 19750   ∑X₁² = 20550
∑X₂² = 3932    ∑X₁X₂ = 8640   ∑Y² = 103650
```

**Verification table:**

| Y | X₁ | X₂ | X₁Y | X₂Y | X₁² | X₂² | X₁X₂ | Y² |
|---|----|----|-----|-----|-----|-----|------|----|
| 190 | 80 | 40 | 15200 | 7600 | 6400 | 1600 | 3200 | 36100 |
| 80 | 35 | 13 | 2800 | 1040 | 1225 | 169 | 455 | 6400 |
| 75 | 35 | 7 | 2625 | 525 | 1225 | 49 | 245 | 5625 |
| 100 | 50 | 20 | 5000 | 2000 | 2500 | 400 | 1000 | 10000 |
| 125 | 60 | 19 | 7500 | 2375 | 3600 | 361 | 1140 | 15625 |
| 90 | 40 | 13 | 3600 | 1170 | 1600 | 169 | 520 | 8100 |
| 70 | 20 | 20 | 1400 | 1400 | 400 | 400 | 400 | 4900 |
| 130 | 60 | 28 | 7800 | 3640 | 3600 | 784 | 1680 | 16900 |
| **860** | **380** | **160** | **45925** | **19750** | **20550** | **3932** | **8640** | **103650** |

**Means:** ȳ = 107.5, x̄₁ = 47.5, x̄₂ = 20

**Step 2: Normal equations**
```
(I)   860   = 8a    + 380b₁  + 160b₂
(II)  45925 = 380a  + 20550b₁ + 8640b₂
(III) 19750 = 160a  + 8640b₁  + 3932b₂
```

From (I): **a = 107.5 − 47.5b₁ − 20b₂**

Sub in (II):
```
45925 = 380(107.5 − 47.5b₁ − 20b₂) + 20550b₁ + 8640b₂
45925 = 40850 − 18050b₁ − 7600b₂ + 20550b₁ + 8640b₂
5075 = 2500b₁ + 1040b₂          ...(IV)
```

Sub in (III):
```
19750 = 160(107.5 − 47.5b₁ − 20b₂) + 8640b₁ + 3932b₂
19750 = 17200 − 7600b₁ − 3200b₂ + 8640b₁ + 3932b₂
2550 = 1040b₁ + 732b₂           ...(V)
```

From (V): b₁ = (2550 − 732b₂) / 1040

Sub in (IV):
```
5075 = 2500 × [(2550 − 732b₂)/1040] + 1040b₂
5075 = (2500 × 2550)/1040 − (2500 × 732/1040)b₂ + 1040b₂
5075 = 6129.81 − 1759.62b₂ + 1040b₂
5075 − 6129.81 = −719.62b₂
−1054.81 = −719.62b₂
b₂ = 1.466
```

```
b₁ = (2550 − 732 × 1.466) / 1040
   = (2550 − 1077.11) / 1040
   = 1472.89 / 1040
   = 1.416
```

```
a = 107.5 − 47.5(1.416) − 20(1.466)
  = 107.5 − 67.26 − 29.32
  = 10.92
```

### **ŷ = 10.92 + 1.416X₁ + 1.466X₂**

**Step 3: R²**
```
SST = ∑Y² − nȳ² = 103650 − 8(107.5)² = 103650 − 92450 = 11200

∑X₁Y − nx̄₁ȳ = 45925 − 8(47.5)(107.5) = 45925 − 40850 = 5075
∑X₂Y − nx̄₂ȳ = 19750 − 8(20)(107.5) = 19750 − 17200 = 2550

SSR = 1.416(5075) + 1.466(2550) = 7186.2 + 3738.3 = 10924.5

R² = 10924.5 / 11200 = 0.9754
```

### **R² = 0.975 (97.5% of variation explained)**

**Step 4: F-test**
```
F = [R²/k] / [(1−R²)/(n−k−1)]
  = [0.975/2] / [(0.025)/5]
  = 0.4875 / 0.005
  = 97.5

F_table = 13.274 (α = 0.01, df₁ = 2, df₂ = 5)

Since F_calc (97.5) >> F_table (13.274) → REJECT H₀
```

### **Regression is HIGHLY SIGNIFICANT at 1% level ✅**

---

## 📌 NEW THEORY TOPICS FROM DEC 2024

### b_yx and b_xy Sign Property (Q1c)

**Statement:** b_yx and b_xy must **always have the same sign** (both positive or both negative).

**Proof:**
```
r² = b_yx × b_xy

Since r² ≥ 0 always, the product b_yx × b_xy ≥ 0
This is only possible when both have the SAME sign.

Also: r = ±√(b_yx × b_xy)
- If both positive → r is positive
- If both negative → r is negative
- They CANNOT have opposite signs
```

---

### Grouped Data Terminology (Q2b)

| Term | Definition |
|------|-----------|
| **Grouped Data** | Data organized into classes/groups with frequencies |
| **Class Interval** | Range of each group (e.g., 10-20, 20-30) |
| **Class Limits** | Lower and upper values of a class (10 and 20 in "10-20") |
| **Class Boundaries** | True limits: Lower − 0.5, Upper + 0.5 (9.5 and 20.5) |
| **Class Mark** | Midpoint = (Lower + Upper) / 2 = (10+20)/2 = 15 |
| **Inclusive Series** | Both limits included (10-19, 20-29) |
| **Exclusive Series** | Upper limit excluded (10-20, 20-30) — used for continuous data |
| **Frequency** | Number of observations in each class |
| **Tally Marks** | Counting marks in groups of 5: ⧸⧸⧸⧸ ⧸ = 5 |

---

### Simple Random Sampling (Q1d)

Method where **every member** of the population has an **equal probability** of being selected.

**Methods:**
1. **Lottery method**: Assign numbers, draw randomly
2. **Random number table**: Use published tables of random digits
3. **Computer-generated**: Use PRNG to select samples

**Advantages:** No bias, easy to implement, statistical inference is straightforward
**Disadvantages:** Needs complete list (sampling frame), may not represent subgroups well

---

### Census Method (Q1b)

Complete enumeration of **every unit** in the population.

| Merits | Demerits |
|--------|---------|
| No sampling error | Very expensive |
| Comprehensive data | Extremely time-consuming |
| Suitable for small populations | Impractical for large populations |
| Data available for all units | Higher non-sampling errors (fatigue) |

---

### MP and UMP Tests (Q6d)

**MP (Most Powerful) Test:**
- For a given significance level α, the test with the **highest power** (1−β)
- Derived using **Neyman-Pearson Lemma**
- Based on likelihood ratio criterion
- Applicable to **simple vs simple** hypotheses (H₀: θ=θ₀ vs H₁: θ=θ₁)

**UMP (Uniformly Most Powerful) Test:**
- A test that is **most powerful for ALL values** of θ in the alternative hypothesis
- More general than MP — works for **composite** H₁ (e.g., H₁: θ > θ₀)
- Exists mainly for **one-sided** alternatives in exponential family distributions
- If UMP exists → it's the best test to use

---

### Overall Fit of Regression Model (Q6c)

Measured using **R²** and **F-test**:

- **R² (Coefficient of Determination):** Proportion of total variation in Y explained by the model (0 to 1)
- **Adjusted R²:** R²_adj = 1 − [(1−R²)(n−1)/(n−k−1)] — penalizes adding unnecessary predictors
- **F-test:** Tests if the overall regression is significant (at least one predictor matters)
- If F_calc > F_table → model is significant → good overall fit
