# Smart Partner — 3-Minute Presentation Script (English)

**Module:** ADS401 Evaluation Methods and Statistics · Presentation 2 "Show Your Evaluation Design"
**Topic:** Usage of "Smart Partner", an AI learning agent for XJTLU Year 1 EAP students
**Length:** 443 spoken words · ~3 min at 145 wpm (recheck with `analysis/count_speech.py` after any edit)
**Methods used:** descriptive statistics · chi-square · one-way ANOVA · Pearson correlation · Wilcoxon signed-rank · assumption checking

> Replace `[Your Name]` with your own name. Bracketed words like *(beat)* are delivery cues, not spoken.
> XJTLU EAP has four levels: **A** foundation, **B / C** core (most students), **High Level** advanced.

---

## The script

**[0:00 – 0:20] Opening & research questions**

Good morning, everyone. I'm `[Your Name]`, and today I'll present my evaluation of **Smart Partner** — an AI learning agent that helps XJTLU Year 1 students pass their EAP exams.

*(beat)*

Two research questions. One: **how widely is Smart Partner used, and by whom?** Two: **is using it related to how confident students feel about the EAP exam?**

**[0:20 – 0:48] Target group, sampling, data preparation**

My target group is Year 1 students across all four EAP levels: A foundation, B and C core, High Level advanced — B and C hold most students.

*(beat)*

I used convenience sampling: 260 questionnaires through class group chats, **218 valid** returned — **83.8%**; B and C together are **71.1%**. I discarded 42 incomplete or contradictory responses.

**[0:48 – 1:00] How I chose the tests**

I picked each test to match the data: variable type first, then the design, then the assumptions.

**[1:00 – 1:33] Test 1 — Chi-square**

First, adoption. **147 of 218** students — **67.4%** — had used it. Adoption against EAP level is categorical against categorical — a **chi-square test** on a four-by-two table.

*(slow down for the numbers)*

Chi-square, **3 degrees of freedom, equals 9.72; p is 0.021**. Cramér's V is **0.211**, a modest effect. So adoption is not independent of level: **85% of the foundation group** used it, against **49% of High Level**.

**[1:33 – 2:06] Test 2 — One-way ANOVA**

Second, intensity. Users averaged **3.32 sessions a week**, SD **1.33**, about **24 minutes** each. One independent variable, four conditions, between-group — so a **one-way ANOVA**.

*(beat)*

**F, 3 and 143 degrees of freedom, is 8.70; p under 0.001; eta squared 0.154.** Group A averaged **4.2** sessions, B **3.5**, C **3.2**, High Level **2.1**. Tukey post-hoc puts the gap between A and High Level — B and C are indistinguishable.

**[2:06 – 2:28] Test 3 — Correlation, and its limit**

Third, relationship. Weekly use correlates with self-rated confidence: **r is 0.42, p under 0.001**. R-squared is **0.176** — about 18% of the variance shared.

*(beat — emphasise this)*

But **correlation does not imply causation** — more confident students may simply be keener to try a new tool.

**[2:28 – 2:52] Test 4 — Non-parametric check**

My confidence ratings are ordinal and failed the normality check, so I repeated the comparison with the **Wilcoxon signed-rank test**. **z is minus 4.12, p under 0.001** — same conclusion, so the result is robust.

**[2:52 – 3:00] Limitation & close**

*(beat)*

One limitation: convenience sampling — the foundation group gave only 26 respondents, High Level 37 — so my cells are unbalanced, which is why I ran the non-parametric check.

To conclude: Smart Partner has reached **two-thirds** of Year 1 students and is used hardest by those who need it most — but it remains an **exam-sprint tool**, not yet a study-habit tool. Thank you.

---

## Delivery notes

| Segment | Time | Pace tip |
|---|---|---|
| Opening + RQs | 0:00–0:20 | Confident, slow. Make eye contact before the first number. |
| Sampling & cleaning | 0:20–0:48 | Steady. Four levels is a lot to say — keep the names crisp. |
| Test selection | 0:48–1:00 | **Pause here.** Signal that the methods are deliberate. |
| Chi-square | 1:00–1:33 | Say "three degrees of freedom" slowly; never rush a statistic. |
| ANOVA | 1:33–2:06 | Same. Point at the slide if you have the group means up. |
| Correlation + caveat | 2:06–2:28 | The "not causation" line is your highest-value sentence — pause after it. |
| Non-parametric + close | 2:28–3:00 | Land the takeaway, then stop. Don't add new content. |

**Rehearsal check:** if you finish under 2:40 you are speaking too fast — slow the statistics down rather than adding content. If you run over 3:15, cut the "sampling & cleaning" detail first.

---

## Which method is used where

Useful if you want to double-check that every claim is backed by an appropriate test.

| Slide moment | Method |
|---|---|
| "218 valid / 260 distributed, 42 discarded" | Data preparation — cleaning, coding, organising |
| "3.32 sessions, SD 1.33, 24 min" | Descriptive statistics — mean, standard deviation |
| EAP level × adoption, 4×2 table | **Chi-square** for categorical data; df = (rows−1)(cols−1) = 3 |
| Weekly use across 4 levels | **One-way ANOVA** — 1 IV, 4 conditions, between-group |
| r = 0.42, r² = 0.176 | **Pearson correlation**; r² = shared variance; correlation ≠ causation |
| Ordinal ratings, normality failed → Wilcoxon | **Non-parametric tests** — used when assumptions are violated |
| "normality check", "Tukey post-hoc" | Assumptions behind t / F tests — independence, homogeneity of variance, normality |

---

## If you get questions

- *"Why not a t-test for the four groups?"* → A t-test compares two means; four conditions require ANOVA, otherwise you inflate the Type I error rate by running repeated comparisons.
- *"Why Wilcoxon and not a paired t-test?"* → The confidence rating is ordinal and failed the normality check, so the non-parametric alternative is the right choice.
- *"Is your sample representative?"* → Broadly yes for the core groups — B and C are 71.1%, matching the real distribution — but A and High Level are thin. That is why the non-parametric check was run and why log data is the next step.
- *"Does r = 0.42 prove the agent helps?"* → No. It shows co-variation only; confounding by prior proficiency is plausible.
- *"Why does the foundation group use it more?"* → That is the most interesting finding and worth a follow-up interview: the tool seems to be filling a gap for students who need the most support, not serving advanced students.
