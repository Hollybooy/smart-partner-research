"""
Verify the statistics quoted on the Smart Partner research page and in the
3-minute speech, so every number is internally consistent.

Sample: n = 218 valid responses, XJTLU Year 1 students.

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

# --------------------------------------------------------------- sample split
# EAP level x used?   (observed counts)
#                      used   not   total
LEVELS = {
    "A (foundation)":     {"used": 22, "not": 4},    #  26  11.9%
    "B (core)":           {"used": 52, "not": 22},   #  74  33.9%
    "C (core)":           {"used": 55, "not": 26},   #  81  37.2%
    "High Level (adv.)":  {"used": 18, "not": 19},   #  37  17.0%
}

rows = []
tot_used = tot_not = tot_all = 0
for name, c in LEVELS.items():
    n = c["used"] + c["not"]
    rows.append((name, c["used"], c["not"], n))
    tot_used += c["used"]
    tot_not += c["not"]
    tot_all += n

print("=== Contingency table: EAP level x 'have used Smart Partner' ===")
print(f"{'level':<20}{'used':>6}{'not':>6}{'total':>7}{'% of n':>9}{'adoption':>11}")
for name, u, nn, n in rows:
    print(f"{name:<20}{u:>6}{nn:>6}{n:>7}{100*n/tot_all:>8.1f}%{100*u/n:>10.1f}%")
print(f"{'ALL':<20}{tot_used:>6}{tot_not:>6}{tot_all:>7}")
print(f"\noverall adoption = {tot_used}/{tot_all} = {100*tot_used/tot_all:.1f}%")
core = LEVELS["B (core)"]["used"] + LEVELS["B (core)"]["not"] \
     + LEVELS["C (core)"]["used"] + LEVELS["C (core)"]["not"]
print(f"core (B + C) share = {core}/{tot_all} = {100*core/tot_all:.1f}%")
print(f"response rate      = 218/260 = {100*218/260:.1f}%")
print(f"Year 1 share       = 206/218 = {100*206/218:.1f}%")

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
# Weekly usage frequency (times/week) among the 147 users
ANOVA = {
    "A":          {"n": 22, "mean": 4.2, "sd": 1.4},
    "B":          {"n": 52, "mean": 3.5, "sd": 1.3},
    "C":          {"n": 55, "mean": 3.2, "sd": 1.4},
    "High Level": {"n": 18, "mean": 2.1, "sd": 1.1},
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
r, n_corr = 0.42, 147
t_r = r * math.sqrt(n_corr - 2) / math.sqrt(1 - r ** 2)
print("\n=== Pearson correlation: weekly use x self-rated confidence ===")
print(f"  r = {r}   r^2 = {r**2:.3f}  ({100*r**2:.1f}% shared variance)")
print(f"  t({n_corr - 2}) = {t_r:.3f}")

# ------------------------------------------------------------ descriptives
print("\n=== Descriptives quoted on the page ===")
print(f"  weekly uses (users): M = {grand:.2f}, SD = {math.sqrt(ms_w):.2f}")
print(f"  avg session length : 24 min")
print(f"  more before exams  : 116/147 = {100*116/147:.1f}%")
