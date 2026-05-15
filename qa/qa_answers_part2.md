# 📝 QA Complete Answer Guide — Part 2 (TIER 3 & Remaining)

---

## 7. 📌 HYPOTHESIS TESTING + Z-TEST [10 Marks] — 🟡 (2/4)

### What is Hypothesis Testing?
A statistical procedure to make decisions about **population parameters** based on **sample data**.

### Steps:
1. **State H₀** (Null Hypothesis) and **H₁** (Alternative Hypothesis)
2. Choose **significance level** (α = 0.05 or 0.01)
3. Calculate **test statistic** (Z, t, F, χ²)
4. Find **critical value** from table
5. **Decision**: If |Z_calc| > Z_critical → **Reject H₀**

### Z-Test for Single Mean:

**Used when:** Testing if sample mean differs from a known population mean (n ≥ 30 or σ known).

```
        x̄ - μ₀
Z = ──────────
      σ / √n

x̄ = sample mean
μ₀ = hypothesized population mean
σ = population standard deviation
n = sample size
```

**Example:** A company claims average weight = 500g. Sample of n=36, x̄=510g, σ=30g. Test at α=0.05.

H₀: μ = 500, H₁: μ ≠ 500 (two-tailed)
Z = (510-500)/(30/√36) = 10/5 = **2.0**
Z_critical (α=0.05, two-tailed) = ±1.96
Since |2.0| > 1.96 → **Reject H₀**. Mean is significantly different.

### Z-Test for Difference of Means:

**Used when:** Comparing means of two populations.

```
          (x̄₁ - x̄₂) - (μ₁ - μ₂)
Z = ─────────────────────────────────
     √(σ₁²/n₁ + σ₂²/n₂)
```

Under H₀: μ₁ = μ₂, so (μ₁ - μ₂) = 0:
```
        x̄₁ - x̄₂
Z = ──────────────────
    √(σ₁²/n₁ + σ₂²/n₂)
```

---

## 8. 📌 MAXIMUM LIKELIHOOD ESTIMATION (MLE) [10 Marks] — 🟡 (2/4)

### Definition:
MLE finds the parameter value that **maximizes the probability** (likelihood) of observing the given sample data.

### Steps:
1. Write the **likelihood function** L(θ) = ∏f(xᵢ|θ)
2. Take **log-likelihood**: ln L(θ)
3. Differentiate: d(ln L)/dθ = 0
4. Solve for θ̂ (MLE estimate)
5. Verify: d²(ln L)/dθ² < 0 (maximum)

### Example — MLE for Normal Distribution Mean:

Given: X₁, X₂, ..., Xₙ ~ N(μ, σ²), find MLE for μ.

L(μ) = ∏(1/σ√2π) exp[-(xᵢ-μ)²/2σ²]

ln L = -n/2 ln(2π) - n/2 ln(σ²) - ∑(xᵢ-μ)²/2σ²

d(ln L)/dμ = ∑(xᵢ-μ)/σ² = 0

→ ∑xᵢ = nμ → **μ̂ = x̄** (sample mean)

### Advantages:
- Asymptotically efficient, consistent, and sufficient
- Invariance property: If θ̂ is MLE of θ, then g(θ̂) is MLE of g(θ)

### Disadvantages:
- May be biased for small samples
- Can be computationally difficult
- Requires knowledge of the distribution form

---

## 9. 📌 NEYMAN PEARSON LEMMA [10 Marks] — 🟡 (2/4)

### Statement:
For testing H₀: θ = θ₀ vs H₁: θ = θ₁ (simple vs simple), the **most powerful test** of size α has the critical region:

```
              L(θ₁)
C = {x : ────────── ≥ k}
              L(θ₀)

Where:
L(θ₀) = Likelihood under H₀
L(θ₁) = Likelihood under H₁
k = constant determined by significance level α
P(X ∈ C | H₀) = α
```

### Key Points:
- Provides the **most powerful (MP) test** for simple hypotheses
- The **likelihood ratio** is the optimal test statistic
- If the MP test exists for all values of θ₁ > θ₀, it's called **Uniformly Most Powerful (UMP)**
- Foundation of **likelihood ratio tests**

### Related: MP and UMP Tests
- **MP Test**: Most powerful test at a given α for specific H₁
- **UMP Test**: Most powerful for ALL values of θ in H₁ simultaneously
- UMP tests exist mainly for **one-sided** alternatives in exponential family distributions

---

## 10. 📌 NULL vs ALTERNATIVE HYPOTHESIS [5-10 Marks] — 🟡 (2/4)

| Feature | Null Hypothesis (H₀) | Alternative Hypothesis (H₁) |
|---------|---------------------|---------------------------|
| **Definition** | Statement of "no effect" or "no difference" | Statement of "effect exists" or "difference exists" |
| **Default** | Assumed true until evidence against it | Accepted only when H₀ is rejected |
| **Symbol** | H₀: μ = μ₀ | H₁: μ ≠ μ₀ or μ > μ₀ or μ < μ₀ |
| **Contains** | Always contains **equality** (=, ≤, ≥) | Contains **inequality** (≠, >, <) |
| **Burden of proof** | On the researcher to disprove | Accepted when evidence is strong |
| **Error** | Type I error if wrongly rejected | Type II error if wrongly not accepted |

---

## 11. 📌 TYPE I AND TYPE II ERROR [5-10 Marks] — QB

| | H₀ is TRUE | H₀ is FALSE |
|---|------------|-------------|
| **Reject H₀** | **Type I Error** (α) — False Positive | ✅ Correct Decision (Power = 1-β) |
| **Fail to reject H₀** | ✅ Correct Decision | **Type II Error** (β) — False Negative |

- **α** (Level of significance) = P(Type I Error) = P(Reject H₀ | H₀ is true)
- **β** = P(Type II Error) = P(Fail to reject H₀ | H₀ is false)
- **Power** = 1 - β = P(Reject H₀ | H₀ is false)
- As α ↓, β ↑ (trade-off)
- Increasing **sample size** reduces both errors

---

## 12. 📌 CRITICAL REGION vs REGION OF ACCEPTANCE [5-10 Marks]

| Feature | Critical Region (Rejection Region) | Region of Acceptance |
|---------|-----------------------------------|---------------------|
| **Definition** | Set of values of test statistic that lead to **rejecting H₀** | Set of values where H₀ is **not rejected** |
| **Location** | Tails of the distribution | Center of the distribution |
| **Determined by** | Significance level α | 1 - α |
| **One-tailed** | One tail only | Rest of distribution |
| **Two-tailed** | Both tails (α/2 each) | Center area |

```
Two-tailed test (α = 0.05):

     Reject H₀    Accept H₀     Reject H₀
     (α/2=0.025)  (1-α=0.95)    (α/2=0.025)
     ┌──┐     ┌──────────────┐     ┌──┐
─────┘  └─────┘              └─────┘  └─────
    -1.96                        +1.96
```

---

## 13. 📌 DATA COLLECTION METHODS [10 Marks]

### Primary Data:
Data collected **first-hand** by the researcher for a specific purpose.

**Methods:**
1. **Direct Personal Interview**: Researcher meets respondent
2. **Indirect Oral Investigation**: Info from third parties
3. **Mailed Questionnaire**: Sent by post/email
4. **Schedule**: Filled by enumerator, not respondent
5. **Observation**: Watching and recording events
6. **Experiment**: Controlled conditions

### Secondary Data:
Data **already collected** by someone else for a different purpose.

**Sources:** Government reports, journals, census data, company records, websites

### Primary vs Secondary Data:

| Feature | Primary | Secondary |
|---------|---------|-----------|
| **Collected by** | Researcher | Others |
| **Purpose** | Current research | Originally different |
| **Cost** | Expensive | Cheaper |
| **Time** | Time-consuming | Quick |
| **Accuracy** | More reliable | Less reliable (may be outdated) |
| **Control** | Full control | No control |

### Precautions for Secondary Data:
1. Check the **source reliability**
2. Check **when** data was collected (timeliness)
3. Check **methodology** used
4. Check for **bias** in collection
5. Verify **units and definitions** used

---

## 14. 📌 QUESTIONNAIRE vs SCHEDULE [10 Marks]

| Feature | Questionnaire | Schedule |
|---------|--------------|----------|
| **Filled by** | Respondent | Enumerator/Investigator |
| **Cost** | Low | High (need trained enumerators) |
| **Response rate** | Low (many don't return) | High (personal contact) |
| **Literacy** | Requires literate respondents | Can include illiterate respondents |
| **Coverage** | Wide (can be mailed) | Limited (need physical presence) |
| **Bias** | Less interviewer bias | May have interviewer bias |
| **Depth** | Limited | Can probe deeper |

### Essential Points for Drafting a Questionnaire:
1. Keep questions **simple and clear**
2. Avoid **leading/biased** questions
3. Use **logical sequence**
4. Include **both open and closed** questions
5. Keep it **short** (avoid respondent fatigue)
6. **Pre-test** (pilot study) before actual use
7. Ensure **anonymity** if sensitive topics

---

## 15. 📌 SAMPLING [5-10 Marks]

### Definition:
**Sampling** = selecting a subset (sample) from a population to draw conclusions about the entire population.

### Purpose:
1. Reduces **cost and time** vs census
2. Greater **accuracy** (focus on quality)
3. When population is **infinite** or destructive testing

### Types:

**Probability Sampling:**
| Method | Description |
|--------|-------------|
| **Simple Random** | Each element has equal probability of selection |
| **Stratified** | Population divided into strata; random sample from each |
| **Systematic** | Every kth element selected (k = N/n) |
| **Cluster** | Population divided into clusters; randomly select entire clusters |

**Non-probability Sampling:**
| Method | Description |
|--------|-------------|
| **Convenience** | Most accessible elements |
| **Judgmental** | Researcher's judgment |
| **Quota** | Predetermined quotas for subgroups |
| **Snowball** | Existing subjects recruit future subjects |

### Stratified Sampling:
- Population divided into **homogeneous groups (strata)**
- Random sample drawn from **each stratum**
- **Merits**: More representative, lower sampling error, allows stratum-level analysis
- **Limitations**: Requires knowledge of strata, complex design, strata must be identifiable

---

## 16. 📌 DATA PRESENTATION [10 Marks]

### Histogram:
- Bar chart for **continuous frequency distribution**
- X-axis: class intervals, Y-axis: frequency
- Bars touch each other (no gaps)
- Area of bar ∝ frequency

### Frequency Polygon:
- Line graph connecting **midpoints** of histogram bars
- Close the polygon by extending to x-axis at both ends

### Ogive (Cumulative Frequency Curve):
- **Less-than ogive**: Cumulative frequency vs upper class boundary (S-curve rising)
- **More-than ogive**: Cumulative frequency vs lower class boundary (S-curve falling)
- **Intersection** of two ogives gives the **median**

### Pie Chart:
- Circle divided into **sectors** proportional to values
- Angle for each = (value/total) × 360°
- **Advantages**: Easy to understand, shows proportions clearly
- **Disadvantages**: Difficult with many categories, exact values hard to read

### Bar Diagram:
- **Simple**: One variable, bars of equal width
- **Multiple/Grouped**: Compare categories across groups
- **Sub-divided/Stacked**: Shows composition within each bar
- **Percentage sub-divided**: Each bar = 100%, shows proportions

### Diagrammatic Representation — Advantages:
1. **Attractive** and easy to understand
2. Facilitates **quick comparison**
3. Saves **time and effort**
4. Has **lasting impression** on mind
5. Useful for **general public** (no statistical knowledge needed)

---

## 17. 📌 SKEWNESS [10 Marks]

### Definition:
**Skewness** = measure of **asymmetry** in a frequency distribution.

### Types:
```
Positive Skew:        Symmetric:         Negative Skew:
    ╱╲                  ╱╲                    ╱╲
   ╱  ╲____         __╱  ╲__            ____╱  ╲
  ╱        ╲       ╱        ╲          ╱        ╲
Mode<Median<Mean  Mode=Median=Mean   Mean<Median<Mode
```

### Tests/Measures of Skewness:

**1. Karl Pearson's Coefficient:**
```
Sk = (Mean - Mode) / σ    or    Sk = 3(Mean - Median) / σ
```
- Sk = 0: Symmetric
- Sk > 0: Positive skew
- Sk < 0: Negative skew

**2. Bowley's Coefficient (Quartile):**
```
Sk = (Q₃ + Q₁ - 2Q₂) / (Q₃ - Q₁)
```

**3. Moment-based:**
```
γ₁ = μ₃ / (μ₂)^(3/2)
```
Where μ₂, μ₃ are 2nd and 3rd central moments.

---

## 18. 📌 RANDOM VARIABLE & MATHEMATICAL EXPECTATION [10 Marks]

### Random Variable:
A **function** that assigns a numerical value to each outcome of a random experiment.
- **Discrete**: Countable values (e.g., number of heads)
- **Continuous**: Any value in an interval (e.g., height, weight)

### Mathematical Expectation:

**For discrete:** E(X) = ∑ xᵢ P(xᵢ)

**For continuous:** E(X) = ∫ x f(x) dx

### Properties:
1. E(c) = c (constant)
2. E(cX) = cE(X)
3. E(X + Y) = E(X) + E(Y)
4. Var(X) = E(X²) - [E(X)]²

---

## 19. 📌 MAE & MAPE [5 Marks]

### MAE (Mean Absolute Error):
```
MAE = (1/n) ∑|yᵢ - ŷᵢ|
```
- Average of absolute differences between actual and predicted values
- In same units as Y

### MAPE (Mean Absolute Percentage Error):
```
MAPE = (1/n) ∑(|yᵢ - ŷᵢ| / |yᵢ|) × 100%
```
- Expressed as percentage → easier to interpret
- MAPE < 10% → excellent model

### Other Metrics:
- **MSE** = (1/n) ∑(yᵢ - ŷᵢ)²
- **RMSE** = √MSE
- **R²** = 1 - (SSE/SST)

---

## 20. 📌 METHOD OF MOMENTS [5 Marks]

Equates **sample moments** to **population moments** to estimate parameters.

**Steps:**
1. Calculate sample moments: m₁ = x̄, m₂ = ∑xᵢ²/n
2. Set equal to population moments: μ₁' = E(X), μ₂' = E(X²)
3. Solve the system of equations for parameters

**Example (Normal):** m₁ = μ → μ̂ = x̄; m₂ = σ² + μ² → σ̂² = m₂ - m₁²

---

## 21. 📌 CENSUS METHOD [5 Marks]

Complete enumeration of **every unit** in the population.

**Merits:** Accurate (no sampling error), detailed data for all units, suitable for small populations
**Demerits:** Expensive, time-consuming, impractical for large/infinite populations, may have non-sampling errors

---

## 📋 QUESTION BANK → CROSS-REFERENCE MAP

| QB # | Question | Answer Location |
|------|----------|----------------|
| Q.1 | Type I and Type II error | **Part 2, Topic 11** |
| Q.2 | Primary and secondary data | **Part 2, Topic 13** |
| Q.3 | Neyman Pearson Lemma | **Part 2, Topic 9** |
| Q.4 | Define Statistics + Uses + Limitations | **Part 1, Topic 6** |
| Q.5 | Random variable + Mathematical expectation | **Part 2, Topic 18** |
| Q.6 | Hypothesis testing + Z-tests | **Part 2, Topic 7** |
| Q.7 | Maximum likelihood estimation | **Part 2, Topic 8** |
| Q.8 | Point estimation + characteristics | **Part 1, Topic 4** |
| Q.9 | Sampling and purpose | **Part 2, Topic 15** |
| Q.10 | Point estimation properties | **Part 1, Topic 4** |
| Q.11 | Multiple Regression + MLR assumptions | **Part 1, Topic 3** |
| Q.12 | Skewness + tests | **Part 2, Topic 17** |
| Q.13 | Methods of collecting data | **Part 2, Topic 13** |
| Q.14 | Partial correlation coefficient | **Part 1, Topic 5** |
| Q.15 | Regression types + applications | **Part 1, Topic 1** |
| Q.16 | Census method + merits/demerits | **Part 2, Topic 21** |
| Q.17 | Data collection + types of data | **Part 2, Topic 13** |
| Q.18 | Stratified sampling | **Part 2, Topic 15** |
| Q.19 | Questionnaire + essential points | **Part 2, Topic 14** |
| Q.20 | Null and Alternative hypothesis | **Part 2, Topic 10** |
| Q.21 | Methods of data collection | **Part 2, Topic 13** |
| Q.20 Diff | Prob/non-prob sampling, Critical/Acceptance region, H₀/H₁, Questionnaire/Schedule | **Part 2, Topics 15, 12, 10, 14** |
| Q.21 SN | MAE/MAPE, Regression analysis, Pie chart, LSR, Diagrammatic repr, MP/UMP test | **Part 2, Topics 19, 16, 9; Part 1, Topic 1** |
| **Numericals** | **Refer PYQs — V.V.V.V.V.I.M.P** | **Part 1, Topics 1-5** (formulas + examples) |
