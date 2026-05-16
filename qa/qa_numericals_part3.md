# 🔢 QA ULTIMATE NUMERICAL MASTERCLASS — Part 3 (Modules 1, 5, 6)

---

## TYPE 6: MEAN DEVIATION FROM MEDIAN [10 Marks]

### Core Formulas:
```
Median (grouped) = L + [(N/2 − CF) / f] × h

Mean Deviation = (1/N) × ∑fᵢ|xᵢ − Median|
```

### ✅ Solved Example 11 — PYQ Dec 2022 Q3a Style

**Q:** Calculate Mean Deviation from Median:

| Class | 0-10 | 10-20 | 20-30 | 30-40 | 40-50 |
|-------|------|-------|-------|-------|-------|
| f | 5 | 8 | 12 | 6 | 4 |

**N = 35, N/2 = 17.5**

**Step 1: Cumulative Frequency**

| Class | f | CF | Midpoint (xᵢ) |
|-------|---|-----|--------------|
| 0-10 | 5 | 5 | 5 |
| 10-20 | 8 | 13 | 15 |
| **20-30** | **12** | **25** | **25** |
| 30-40 | 6 | 31 | 35 |
| 40-50 | 4 | 35 | 45 |

Median class = 20-30 (CF just exceeds 17.5)

**Step 2: Calculate Median**
```
L = 20, f = 12, CF = 13, h = 10
Median = 20 + [(17.5 − 13)/12] × 10
       = 20 + [4.5/12] × 10
       = 20 + 3.75
       = 23.75
```

**Step 3: Mean Deviation**

| Class | f | xᵢ | |xᵢ − 23.75| | f × |xᵢ − 23.75| |
|-------|---|-----|-------------|---------------------|
| 0-10 | 5 | 5 | 18.75 | 93.75 |
| 10-20 | 8 | 15 | 8.75 | 70.00 |
| 20-30 | 12 | 25 | 1.25 | 15.00 |
| 30-40 | 6 | 35 | 11.25 | 67.50 |
| 40-50 | 4 | 45 | 21.25 | 85.00 |
| | **35** | | | **∑ = 331.25** |

```
Mean Deviation = 331.25 / 35 = 9.464
```

---

## TYPE 7: HISTOGRAM & FREQUENCY POLYGON [10 Marks]

### ✅ Solved Example 12 — PYQ Paper 3 Q3a

**Q:** Draw Histogram and Frequency Polygon for weekly wages of 100 workers:

| Wages (₹00) | 20-24 | 25-29 | 30-34 | 35-39 | 40-44 | 45-49 | 50-54 | 55-59 | 60-64 |
|-------------|-------|-------|-------|-------|-------|-------|-------|-------|-------|
| Workers | 4 | 5 | 12 | 23 | 31 | 10 | 8 | 5 | 2 |

**Step 1: Make classes continuous** (boundaries)

| Class Boundary | f | Midpoint |
|---------------|---|----------|
| 19.5 – 24.5 | 4 | 22 |
| 24.5 – 29.5 | 5 | 27 |
| 29.5 – 34.5 | 12 | 32 |
| 34.5 – 39.5 | 23 | 37 |
| 39.5 – 44.5 | 31 | 42 |
| 44.5 – 49.5 | 10 | 47 |
| 49.5 – 54.5 | 8 | 52 |
| 54.5 – 59.5 | 5 | 57 |
| 59.5 – 64.5 | 2 | 62 |

**Step 2: Histogram** — Draw bars with:
- X-axis: Class boundaries (19.5, 24.5, ..., 64.5)
- Y-axis: Frequency (0 to 35)
- Bars touch each other (no gaps)
- Tallest bar: 39.5–44.5 (f = 31)

**Step 3: Frequency Polygon** — Plot midpoints (22, 27, 32, ..., 62) vs frequencies, connect with straight lines. Close by extending to (17, 0) and (67, 0).

```
Frequency
35|                    ___
30|                   |   |
25|               ___|   |
20|              |       |
15|          ___|        |___
10|         |                |___
 5|     ___|                     |___
 0|___|_____________________________|___
   19.5  24.5  29.5  34.5  39.5  44.5  49.5  54.5  59.5  64.5
```

---

## TYPE 8: OGIVE (CUMULATIVE FREQUENCY CURVE) [10 Marks]

### ✅ Solved Example 13 — PYQ Paper 4 Q2b Style

**Q:** Draw Less-than and More-than Ogive. Find Median from the graph.

| Scores | 400-450 | 450-500 | 500-550 | 550-600 | 600-650 | 650-700 | 700-750 | 750-800 |
|--------|---------|---------|---------|---------|---------|---------|---------|---------|
| f | 25 | 30 | 45 | 37 | 30 | 23 | 15 | 35 |

**N = 240**

**Less-than Ogive:**

| Upper Boundary | CF (Less-than) |
|---------------|----------------|
| 450 | 25 |
| 500 | 55 |
| 550 | 100 |
| 600 | 137 |
| 650 | 167 |
| 700 | 190 |
| 750 | 205 |
| 800 | 240 |

**More-than Ogive:**

| Lower Boundary | CF (More-than) |
|---------------|----------------|
| 400 | 240 |
| 450 | 215 |
| 500 | 185 |
| 550 | 140 |
| 600 | 103 |
| 650 | 73 |
| 700 | 50 |
| 750 | 35 |

**Plot both curves on same graph. The intersection point gives Median ≈ 598.**

Verification: N/2 = 120, Median class = 550-600
```
Median = 550 + [(120 − 100)/37] × 50
       = 550 + [20/37] × 50
       = 550 + 27.03
       = 577.03
```

---

## TYPE 9: PERCENTAGE SUB-DIVIDED BAR DIAGRAM [10 Marks]

### ✅ Solved Example 14 — PYQ Paper 3 Q2a

**Q:** Represent by percentage sub-divided bar diagram:

| Item | Family A (₹500) | Family B (₹300) |
|------|-----------------|-----------------|
| Food | 150 | 150 |
| Clothing | 125 | 60 |
| Education | 25 | 50 |
| Miscellaneous | 190 | 70 |
| Savings/Deficit | 10 | −30 |

**Step 1: Convert to percentages**

| Item | Family A (%) | Family B (%) |
|------|-------------|-------------|
| Food | 150/500 × 100 = **30%** | 150/300 × 100 = **50%** |
| Clothing | 125/500 × 100 = **25%** | 60/300 × 100 = **20%** |
| Education | 25/500 × 100 = **5%** | 50/300 × 100 = **16.67%** |
| Misc | 190/500 × 100 = **38%** | 70/300 × 100 = **23.33%** |
| Savings | 10/500 × 100 = **2%** | −30/300 × 100 = **−10%** |

**Step 2: Draw** — Two bars (both height = 100%), each divided into sections with different shadings. Label percentages.

---

## TYPE 10: EXPECTED VALUE / PROFIT PROBLEMS [10 Marks]

### ✅ Solved Example 15 — PYQ Dec 2022 Q1d

**Q:** In 25 years: 10 mild, 8 cold, 7 very cold winters. Company sells 1000 coats (mild), 1300 (cold), 2000 (very cold). Cost ₹1750, sold for ₹2500. Find expected yearly profit.

**Step 1: Probabilities**
```
P(mild) = 10/25 = 0.4
P(cold) = 8/25 = 0.32
P(very cold) = 7/25 = 0.28
```

**Step 2: Profit per coat** = 2500 − 1750 = ₹750

**Step 3: Profit for each scenario**
```
Mild:      1000 × 750 = ₹7,50,000
Cold:      1300 × 750 = ₹9,75,000
Very Cold: 2000 × 750 = ₹15,00,000
```

**Step 4: Expected profit**
```
E(Profit) = 0.4(7,50,000) + 0.32(9,75,000) + 0.28(15,00,000)
          = 3,00,000 + 3,12,000 + 4,20,000
          = ₹10,32,000
```

**Expected yearly profit = ₹10,32,000**

---

## TYPE 11: Z-TEST FOR SINGLE MEAN [10 Marks]

### ✅ Solved Example 16

**Q:** A manufacturer claims mean weight = 500g. Sample: n = 64, x̄ = 507g, σ = 40g. Test at α = 0.05.

```
H₀: μ = 500
H₁: μ ≠ 500 (two-tailed)

Z = (x̄ − μ₀) / (σ/√n)
  = (507 − 500) / (40/√64)
  = 7 / (40/8)
  = 7 / 5
  = 1.4

Z_critical (α = 0.05, two-tailed) = ±1.96

|1.4| < 1.96 → FAIL TO REJECT H₀
```

**Conclusion:** At 5% significance, the claim is valid. Mean weight is not significantly different from 500g.

---

### ✅ Solved Example 17 — Confidence Interval (PYQ Paper 3 Q1b)

**Q:** Sample of n = 100, σ = 5. What can you say about max error with 95% confidence?

```
Maximum Error (E) = Z × (σ/√n)
                  = 1.96 × (5/√100)
                  = 1.96 × 0.5
                  = 0.98
```

**The maximum error at 95% confidence is 0.98.** The true population mean lies within ±0.98 of the sample mean.

---

## TYPE 12: Z-TEST FOR DIFFERENCE OF MEANS [10 Marks]

### ✅ Solved Example 18

**Q:** Two groups: Group A (n₁ = 50, x̄₁ = 75, σ₁ = 8) and Group B (n₂ = 60, x̄₂ = 72, σ₂ = 6). Test if means differ at α = 0.05.

```
H₀: μ₁ = μ₂ (no difference)
H₁: μ₁ ≠ μ₂ (two-tailed)

Z = (x̄₁ − x̄₂) / √(σ₁²/n₁ + σ₂²/n₂)
  = (75 − 72) / √(64/50 + 36/60)
  = 3 / √(1.28 + 0.6)
  = 3 / √1.88
  = 3 / 1.3711
  = 2.188

Z_critical = ±1.96

|2.188| > 1.96 → REJECT H₀
```

**Conclusion:** At 5% significance, the means are significantly different.

---

## TYPE 13: PROVING S² IS UNBIASED ESTIMATOR [5 Marks]

### ✅ Solved Example 19 — PYQ Paper 4 Q1d

**Q:** Show that S² = ∑(Xᵢ − X̄)² / (n−1) is unbiased for σ².

**Proof:**
```
We need to show: E(S²) = σ²

∑(Xᵢ − X̄)² = ∑Xᵢ² − nX̄²

E[∑(Xᵢ − X̄)²] = E[∑Xᵢ²] − nE[X̄²]

Now:
E[Xᵢ²] = Var(Xᵢ) + [E(Xᵢ)]² = σ² + μ²
So E[∑Xᵢ²] = n(σ² + μ²)

E[X̄²] = Var(X̄) + [E(X̄)]² = σ²/n + μ²
So nE[X̄²] = n(σ²/n + μ²) = σ² + nμ²

Therefore:
E[∑(Xᵢ − X̄)²] = n(σ² + μ²) − (σ² + nμ²)
                = nσ² + nμ² − σ² − nμ²
                = (n−1)σ²

Hence:
E[S²] = E[∑(Xᵢ − X̄)²/(n−1)] = (n−1)σ²/(n−1) = σ²  ✅
```

**∴ S² is an unbiased estimator of σ².**

Note: Dividing by **n** instead of **(n−1)** gives a biased estimator since E[∑(Xᵢ−X̄)²/n] = (n−1)σ²/n ≠ σ².

---

## 📋 COMPLETE TYPE REFERENCE

| Type | Module | Topic | Priority |
|------|--------|-------|----------|
| 1 | 3 | Simple Linear Regression + Prediction | 🔴 4/4 |
| 2 | 3 | Correlation from raw data | 🔴 4/4 |
| 3 | 3 | From Regression Lines → r, means | 🔴 4/4 |
| 4 | 4 | MLR + R² + F-test | 🟠 3/4 |
| 5 | 4 | Partial Correlation Coefficient | 🟠 3/4 |
| 6 | 1 | Mean Deviation from Median | 🟡 1/4 |
| 7 | 1 | Histogram + Frequency Polygon | 🟡 2/4 |
| 8 | 1 | Ogive (Less/More than) | 🟡 1/4 |
| 9 | 1 | % Sub-divided Bar Diagram | 🟡 1/4 |
| 10 | — | Expected Value / Profit | 🟡 1/4 |
| 11 | 6 | Z-test Single Mean | 🟡 2/4 |
| 12 | 6 | Z-test Difference of Means | 🟡 2/4 |
| 13 | 5 | S² unbiased proof | 🟡 1/4 |
