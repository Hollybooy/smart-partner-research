"""
Verify the statistics quoted on the Smart Partner research page and in the
3-minute speech, so every number is internally consistent.

Sample: NOT YET COLLECTED — the survey has not launched, so every count below
is a 0 placeholder and the script stops before any computation.

XJTLU EAP streaming has FOUR levels:
    A          - foundation group (基础班), smallest
    B, C       - core groups (核心班), where most students sit
    High Level - advanced group (高阶班)

Data model:
  * EAP level (A / B / C / High Level) crossed with "have you used Smart Partner?"
  * Weekly usage frequency (times per week), users only
  * Self-rated EAP confidence (1-10), users only
"""

import math

# ------------------------------------------- fieldwork placeholder constants
# The survey has not launched yet; replace these with the real counts once the
# questionnaires have been collected, then re-run this script.
DISTRIBUTED = 0            # questionnaires sent out
RETURNED = 0               # questionnaires returned
YEAR1 = None               # respondents who are Year 1 students
AVG_SESSION_MIN = None     # average session length (minutes)
MORE_BEFORE_EXAMS = None   # users who report using it more before an exam

# --------------------------------------------------------------- sample split
# EAP level x used?   (observed counts — placeholders until data arrive)
#                      used   not   total
LEVELS = {
    "A (foundation)":     {"used": 0, "not": 0},    #  —  —%
    "B (core)":           {"used": 0, "not": 0},    #  —  —%
    "C (core)":           {"used": 0, "not": 0},    #  —  —%
    "High Level (adv.)":  {"used": 0, "not": 0},    #  —  —%
}

rows = []
tot_used = tot_not = tot_all = 0
for name, c in LEVELS.items():
    n = c["used"] + c["not"]
    rows.append((name, c["used"], c["not"], n))
    tot_used += c["used"]
    tot_not += c["not"]
    tot_all += n

# --- Early-exit guard: no data yet, do not divide by zero or invent stats.
if tot_all == 0:
    print("=== Contingency table: EAP level x 'have used Smart Partner' ===")
    print("  (no data — survey not yet launched; every cell above is 0)")
    print()
    print("=== No statistics computed yet ===")
    print("Once the questionnaire has been collected, fill in:")
    print("  - the 'used' / 'not' counts in LEVELS")
    print("  - DISTRIBUTED / RETURNED / YEAR1 (top of this file)")
    print("  - the four 'mean' and 'sd' values in ANOVA")
    print("  - r, n_corr (correlation block)")
    print("  - AVG_SESSION_MIN and MORE_BEFORE_EXAMS (descriptives block)")
    print("Then re-run this script to recompute chi-square, ANOVA, correlation")
    print("and the descriptives quoted on the page.")
    raise SystemExit(0)

print("=== Contingency table: EAP level x 'have used Smart Partner' ===")
print(f"{'level':<20}{'used':>6}{'not':>6}{'total':>7}{'% of n':>9}{'adoption':>11}")
for name, u, nn, n in rows:
    print(f"{name:<20}{u:>6}{nn:>6}{n:>7}{100*n/tot_all:>8.1f}%{100*u/n:>10.1f}%")
print(f"{'ALL':<20}{tot_used:>6}{tot_not:>6}{tot_all:>7}")
print(f"\noverall adoption = {tot_used}/{tot_all} = {100*tot_used/tot_all:.1f}%")
core = LEVELS["B (core)"]["used"] + LEVELS["B (core)"]["not"] \
     + LEVELS["C (core)"]["used"] + LEVELS["C (core)"]["not"]
print(f"core (B + C) share = {core}/{tot_all} = {100*core/tot_all:.1f}%")
print(f"response rate      = {RETURNED}/{DISTRIBUTED} = "
      + (f"{100*RETURNED/DISTRIBUTED:.1f}%" if DISTRIBUTED else "— (not distributed)"))
print(f"Year 1 share       = {YEAR1}/{tot_all} = "
      + (f"{100*YEAR1/tot_all:.1f}%" if YEAR1 is not None else "— (not recorded)"))

# ------------------------------------------------------- chi-square (indep.)
chi2 = 0.0
print("\n=== Chi-square test of independence ===")
print(f"{'cell':<24}{'obs':>6}{'exp':>9}{'(o-e)^2/e':>12}")
for name, u, nn, n in rows:
    for obs, col in ((u, tot_used), (nn, tot_not)):
        exp = n * col / tot_all
        chi2 += (obs - exp) ** 2 / exp
        label = name + "/" + ("used" if col == tot_used else "not")
        print(f"{label:<24}{obs:>6}{exp:>9.2f}{(obs-exp)**2/exp:>12.3f}")
df_chi = (len(rows) - 1) * (2 - 1)
print(f"\nchi2({df_chi}) = {chi2:.3f}")
k = min(len(rows) - 1, 1)
print(f"Cramer's V = {math.sqrt(chi2 / (tot_all * k)):.3f}")

# ------------------------------------------------------------ one-way ANOVA
# Weekly usage frequency (times/week) among the users (n = — until data arrive)
ANOVA = {
    "A":          {"n": 0, "mean": 0.0, "sd": 0.0},  # placeholders
    "B":          {"n": 0, "mean": 0.0, "sd": 0.0},  # placeholders
    "C":          {"n": 0, "mean": 0.0, "sd": 0.0},  # placeholders
    "High Level": {"n": 0, "mean": 0.0, "sd": 0.0},  # placeholders
}
N = sum(v["n"] for v in ANOVA.values())
assert N == tot_used, (N, tot_used)
grand = sum(v["n"] * v["mean"] for v in ANOVA.values()) / N

ss_between = sum(v["n"] * (v["mean"] - grand) ** 2 for v in ANOVA.values())
ss_within = sum((v["n"] - 1) * v["sd"] ** 2 for v in ANOVA.values())
df_b, df_w = len(ANOVA) - 1, N - len(ANOVA)
ms_b, ms_w = ss_between / df_b, ss_within / df_w
F = ms_b / ms_w

print("\n=== One-way ANOVA: weekly usage frequency by EAP level ===")
for g, v in ANOVA.items():
    print(f"  {g:<12} n={v['n']:>3}  M={v['mean']:.2f}  SD={v['sd']:.2f}")
print(f"  grand mean = {grand:.3f}   N = {N}")
print(f"  SS_between = {ss_between:.3f}   SS_within = {ss_within:.3f}")
print(f"  F({df_b}, {df_w}) = {F:.3f}")
print(f"  eta^2 = {ss_between / (ss_between + ss_within):.3f}")

# ------------------------------------------------------------- correlation
r, n_corr = 0.0, 0  # placeholders — fill in once data are available
t_r = r * math.sqrt(n_corr - 2) / math.sqrt(1 - r ** 2)
print("\n=== Pearson correlation: weekly use x self-rated confidence ===")
print(f"  r = {r}   r^2 = {r**2:.3f}  ({100*r**2:.1f}% shared variance)")
print(f"  t({n_corr - 2}) = {t_r:.3f}")

# ------------------------------------------------------------ descriptives
print("\n=== Descriptives quoted on the page ===")
print(f"  weekly uses (users): M = {grand:.2f}, SD = {math.sqrt(ms_w):.2f}")
print(f"  avg session length : {AVG_SESSION_MIN if AVG_SESSION_MIN is not None else '—'} min")
print(f"  more before exams  : {MORE_BEFORE_EXAMS}/{tot_used} = "
      + (f"{100*MORE_BEFORE_EXAMS/tot_used:.1f}%" if MORE_BEFORE_EXAMS is not None else "— (not recorded)"))
