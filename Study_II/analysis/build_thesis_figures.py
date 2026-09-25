"""Builds the Study II figures of the thesis into figures/thesis."""

import glob
import json
import math
import os
import statistics as st
import warnings
from collections import Counter

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats
from statsmodels.genmod.families import Binomial
from statsmodels.genmod.generalized_estimating_equations import GEE
from statsmodels.genmod.cov_struct import Exchangeable
import statsmodels.formula.api as smf

warnings.filterwarnings("ignore")

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DATA = os.path.join(ROOT, "data")
OUT = os.path.join(ROOT, "figures", "thesis")

ERR, CORRECT = [2, 4, 6, 8], [1, 3, 5, 7]
TYPE1, TYPE2 = [2, 6], [4, 8]
CLIN = {"Clinically incorrect", "Misleading", "Important information is missing"}
NAMES = {2: "anticoagulation", 4: "dysphagia", 6: "analgesia", 8: "hyperkalemia"}
DWELL_MS = 500
WORDS_PER_ITEM_SCREEN = 199

GREEN, AMBER, RED = "#2f855a", "#d69e2e", "#c53030"
BLUE, GREY, TEAL = "#2b6cb0", "#a0aec0", "#4fa3a5"
YEARS = ["<1", "1-3", "4-7", "8-15", ">15"]
AGES = ["18-24", "25-34", "35-44", "45-54", "55-64", "65+"]
rng = np.random.default_rng(20260824)

plt.rcParams.update({
    "figure.dpi": 200, "savefig.dpi": 200, "font.size": 9,
    "axes.spines.top": False, "axes.spines.right": False,
    "axes.titlesize": 10, "axes.titleweight": "bold", "legend.frameon": False,
})


def load(which="primary"):
    paths = sorted(glob.glob(os.path.join(DATA, "*.txt")))
    if which in ("primary", "unfiltered"):
        paths += sorted(glob.glob(os.path.join(DATA, "borderline", "*.txt")))
    if which == "unfiltered":
        paths += sorted(glob.glob(os.path.join(DATA, "excluded", "*.txt")))
    out = []
    for p in paths:
        d = json.load(open(p, encoding="utf-8"))
        d["_f"] = os.path.basename(p)[:-4]
        out.append(d)
    return out


q = lambda d, i, k: d["items"][str(i)]["q"][k]
detected = lambda d, i: q(d, i, "q2") == "No" and q(d, i, "q3") in CLIN
rejected = lambda d, i: q(d, i, "q2") == "No"
approved = lambda d, i: q(d, i, "q2") == "Yes"
det_count = lambda d: sum(detected(d, i) for i in ERR)
med_secs = lambda d: st.median([d["timing"]["perScreenMs"].get(f"item{i}", 0) / 1000 for i in range(1, 9)])


def dwell(d, i, key, thr=DWELL_MS):
    r = d["items"][str(i)].get("hovers", {}).get(key, {})
    return sum(x for x in r.get("dwellsMs", []) if x >= thr)


def opened_dec(d, i, thr=DWELL_MS):
    return dwell(d, i, "0_B", thr) > 0 or dwell(d, i, "0_C", thr) > 0


def hover_secs(d):
    return sum(x for it in d["items"].values() for r in it.get("hovers", {}).values()
               for x in r.get("dwellsMs", []) if x >= DWELL_MS) / 1000


def frame(D, thr=DWELL_MS):
    return pd.DataFrame([dict(
        pid=d["_f"], item=i, subtype=1 if i in TYPE1 else 2,
        strict=int(detected(d, i)), approved=int(approved(d, i)), conf=int(q(d, i, "q4")),
        open_b=int(dwell(d, i, "0_B", thr) > 0), open_c=int(dwell(d, i, "0_C", thr) > 0),
        open_any=int(opened_dec(d, i, thr)),
    ) for d in D for i in ERR])


def boot(D, fn, n=5000):
    draws = [fn([D[k] for k in rng.integers(0, len(D), len(D))]) for _ in range(n)]
    lo, hi = np.percentile(draws, [2.5, 97.5])
    return fn(D), lo, hi


def gee_or(df, formula, term):
    r = GEE.from_formula(formula, groups="pid", data=df,
                         family=Binomial(), cov_struct=Exchangeable()).fit()
    b, se = r.params[term], r.bse[term]
    return math.exp(b), math.exp(b - 1.96 * se), math.exp(b + 1.96 * se), r.pvalues[term]


def save(fig, name):
    os.makedirs(OUT, exist_ok=True)
    fig.tight_layout()
    for ext in ("png", "pdf"):
        fig.savefig(os.path.join(OUT, f"{name}.{ext}"), bbox_inches="tight")
    plt.close(fig)
    print("  wrote", name)


def pct_labels(ax, bars, fmt="%.0f%%", size=8):
    ax.bar_label(bars, fmt=fmt, fontsize=size, padding=2)


P = load("primary")
NP = len(P)
DF = frame(P)


def fig_outcome_composition():
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(7.4, 3.2), gridspec_kw={"width_ratios": [1, 2.1]})

    dec = [(d, i) for d in P for i in ERR]
    n = len(dec)
    parts = [100 * sum(approved(d, i) for d, i in dec) / n,
             100 * sum(detected(d, i) for d, i in dec) / n,
             100 * sum(rejected(d, i) and not detected(d, i) for d, i in dec) / n]
    left = 0
    for v, c in zip(parts, [RED, GREEN, AMBER]):
        a1.barh(0, v, left=left, color=c, height=.55)
        if v > 15:
            a1.text(left + v / 2, 0, f"{v:.1f}%", ha="center", va="center",
                    color="w", fontsize=9, fontweight="bold")
        else:
            a1.annotate(f"{v:.1f}%", (left + v / 2, .30), ha="center", va="bottom",
                        color=c, fontsize=9, fontweight="bold")
        left += v
    a1.set_yticks([]); a1.set_xlim(0, 100); a1.set_ylim(-.45, .62)
    a1.set_xlabel("% of the 136 error decisions")
    a1.set_title(f"All error decisions (N = {NP})")

    xs = np.arange(4)
    stack = np.zeros(4)
    for key, c, lab in [(lambda d, i: approved(d, i), RED, "approved for patient use"),
                        (lambda d, i: detected(d, i), GREEN, "detected (rejected, clinical reason)"),
                        (lambda d, i: rejected(d, i) and not detected(d, i), AMBER,
                         "rejected, non-clinical reason")]:
        vals = np.array([100 * sum(key(d, i) for d in P) / NP for i in ERR])
        a2.bar(xs, vals, .6, bottom=stack, color=c, label=lab)
        for x, v, b in zip(xs, vals, stack):
            if v > 4:
                a2.text(x, b + v / 2, f"{v:.0f}", ha="center", va="center", color="w", fontsize=8)
        stack += vals
    a2.set_xticks(xs)
    a2.set_xticklabels([f"item {i}\n{NAMES[i]}" for i in ERR], fontsize=8)
    a2.set_ylim(0, 100); a2.set_ylabel("% of participants")
    a2.set_title("By planted error")
    a2.legend(fontsize=7.5, loc="upper center", bbox_to_anchor=(.5, -.22), ncol=1)
    save(fig, "fig_4_1_outcome_composition")


def fig_headline_rates():
    dec_rate = lambda f: (lambda S: 100 * sum(f(d, i) for d in S for i in ERR) / (4 * len(S)))
    specs = [
        ("Errors\ndetected", dec_rate(detected), GREEN),
        ("Errors approved\nfor patient use", dec_rate(approved), RED),
        ("Approved with\nhigh confidence", dec_rate(lambda d, i: approved(d, i) and int(q(d, i, "q4")) >= 4), RED),
        ("Correct items\nrejected", lambda S: 100 * sum(rejected(d, i) for d in S for i in CORRECT) / (4 * len(S)), GREY),
    ]
    fig, ax = plt.subplots(figsize=(6.6, 3.4))
    for j, (lab, fn, c) in enumerate(specs):
        pt, lo, hi = boot(P, fn)
        ax.bar(j, pt, .6, color=c)
        ax.errorbar(j, pt, yerr=[[pt - lo], [hi - pt]], fmt="none", ecolor="#2d3748", capsize=4, lw=1.2)
        ax.text(j, hi + 2, f"{pt:.1f}", ha="center", fontsize=8.5, fontweight="bold")
    ax.set_xticks(range(len(specs))); ax.set_xticklabels([s[0] for s in specs], fontsize=8)
    ax.set_ylabel("%"); ax.set_ylim(0, 78)
    ax.set_title(f"Primary safety outcomes with 95% bootstrap intervals (N = {NP})")
    save(fig, "fig_4_1_headline_rates")


def fig_participant_distribution():
    c = Counter(det_count(d) for d in P)
    fig, ax = plt.subplots(figsize=(5.4, 3.0))
    vals = [c.get(k, 0) for k in range(5)]
    cols = [RED, RED, AMBER, GREEN, GREEN]
    bars = ax.bar(range(5), vals, .62, color=cols)
    ax.bar_label(bars, labels=[f"{v}\n({100*v/NP:.0f}%)" for v in vals], fontsize=8, padding=2)
    ax.set_xlabel("number of the four planted errors detected")
    ax.set_ylabel("participants"); ax.set_ylim(0, max(vals) + 5)
    ax.set_title(f"Detection is spread unevenly across reviewers (N = {NP})")
    save(fig, "fig_4_1_participants_by_errors_detected")


def fig_confidence_calibration():
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(7.4, 3.2))
    dec = [(d, i) for d in P for i in ERR]
    lv = {}
    for d, i in dec:
        lv.setdefault(int(q(d, i, "q4")), []).append(detected(d, i))
    ks = sorted(k for k in lv if len(lv[k]) >= 5)
    ys = [100 * sum(lv[k]) / len(lv[k]) for k in ks]
    a1.plot(ks, ys, "o-", color=BLUE, lw=2, ms=7)
    for k, y in zip(ks, ys):
        a1.annotate(f"{y:.0f}%\nn={len(lv[k])}", (k, y), textcoords="offset points",
                    xytext=(0, 9), ha="center", fontsize=7.5)
    a1.set_xticks([1, 2, 3, 4, 5]); a1.set_ylim(-8, 100)
    a1.set_xlabel("stated confidence (Q4)"); a1.set_ylabel("strict detection rate (%)")
    a1.set_title("Strict detection by confidence rating")

    hi_app = sum(approved(d, i) and int(q(d, i, "q4")) >= 4 for d, i in dec)
    lo_app = sum(approved(d, i) and int(q(d, i, "q4")) < 4 for d, i in dec)
    det = sum(detected(d, i) for d, i in dec)
    rest = len(dec) - hi_app - lo_app - det
    vals = [100 * v / len(dec) for v in (hi_app, lo_app, det, rest)]
    labs = ["approved\nconf. 4-5", "approved\nconf. 1-3",
            "detected", "rejected,\nnon-clinical"]
    bars = a2.bar(range(4), vals, .6, color=[RED, "#e8a0a0", GREEN, AMBER])
    a2.bar_label(bars, fmt="%.1f%%", fontsize=8, padding=2)
    a2.set_xticks(range(4)); a2.set_xticklabels(labs, fontsize=7.5)
    a2.set_ylabel("% of error decisions"); a2.set_ylim(0, 55)
    a2.set_title("Error decisions by outcome and confidence")
    save(fig, "fig_4_2_confidence_calibration")


def fig_support_opened():
    fig, ax = plt.subplots(figsize=(5.8, 3.2))
    opened = DF[DF.open_any == 1]["strict"].mean() * 100
    shut = DF[DF.open_any == 0]["strict"].mean() * 100
    n_op, n_sh = int((DF.open_any == 1).sum()), int((DF.open_any == 0).sum())
    app_open = DF[(DF.approved == 1) & (DF.open_any == 1)].shape[0] / max(1, DF.approved.sum()) * 100
    bars = ax.bar([0, 1], [opened, shut], .5, color=[GREEN, RED])
    ax.bar_label(bars, labels=[f"{opened:.1f}%\nn={n_op}", f"{shut:.1f}%\nn={n_sh}"], fontsize=8, padding=2)
    ax.set_xticks([0, 1]); ax.set_xticklabels(["opened error-relevant\nsupport", "did not open\nerror-relevant support"], fontsize=8)
    ax.set_ylabel("strict detection rate"); ax.set_ylim(0, 82)
    ax.set_title("Strict detection by error-relevant support opening")
    ax.text(.5, 72, f"{app_open:.1f}% of unsafe approvals occurred\nafter the support was opened",
            ha="center", fontsize=7.5,
            bbox=dict(boxstyle="round,pad=.35", fc="#fff5f5", ec=RED, lw=.8))
    save(fig, "fig_4_3_support_opened")


def fig_clustering_adjustment():
    naive = smf.logit("strict ~ open_any", data=DF).fit(disp=0)
    b, se = naive.params["open_any"], naive.bse["open_any"]
    n_or, n_lo, n_hi = math.exp(b), math.exp(b - 1.96 * se), math.exp(b + 1.96 * se)
    c_or, c_lo, c_hi, _ = gee_or(DF, "strict ~ open_any + C(item)", "open_any")

    fig, ax = plt.subplots(figsize=(6.4, 2.5))
    rows = [("Naive: decisions treated\nas independent", n_or, n_lo, n_hi, GREY),
            ("Reported: participant-clustered\n+ item adjusted", c_or, c_lo, c_hi, BLUE)]
    for j, (lab, o, lo, hi, c) in enumerate(rows):
        ax.plot([lo, hi], [j, j], color=c, lw=2.4)
        ax.plot(o, j, "o", color=c, ms=9)
        ax.text(hi * 1.12, j, f"OR {o:.2f}  [{lo:.2f}, {hi:.2f}]", va="center", fontsize=8.5, color=c)
    ax.axvline(1, color="k", ls="--", lw=.9)
    ax.set_yticks([0, 1]); ax.set_yticklabels([r[0] for r in rows], fontsize=8)
    ax.set_xscale("log"); ax.set_xlim(.8, 600)
    ax.set_xticks([1, 2, 5, 10, 20, 50]); ax.set_xticklabels(["1", "2", "5", "10", "20", "50"])
    ax.set_xlabel("odds ratio for detecting the error (log scale)")
    ax.set_ylim(-.6, 1.6); ax.invert_yaxis()
    ax.set_title("Why the clustered, item-adjusted estimate is reported")
    save(fig, "fig_4_3_clustering_adjustment")


def fig_time_dose_response():
    bins = {"< 20 s": [], "20-40 s": [], "40-80 s": [], ">= 80 s": []}
    for d in P:
        s = med_secs(d)
        k = "< 20 s" if s < 20 else "20-40 s" if s < 40 else "40-80 s" if s < 80 else ">= 80 s"
        bins[k].append(det_count(d))
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(7.4, 3.2))
    ks = list(bins)
    ys = [100 * st.mean(v) / 4 if v else 0 for v in bins.values()]
    a1.plot(range(4), ys, "o-", color=BLUE, lw=2, ms=8)
    for j, (k, y) in enumerate(zip(ks, ys)):
        a1.annotate(f"{y:.0f}%\nn={len(bins[k])}", (j, y), textcoords="offset points",
                    xytext=(0, 10), ha="center", fontsize=7.5)
    a1.set_xticks(range(4)); a1.set_xticklabels(ks, fontsize=8)
    a1.set_xlabel("median time per item"); a1.set_ylabel("% of the four errors detected")
    a1.set_ylim(-8, 92); a1.set_title("Detection by review-time group")

    x = [med_secs(d) for d in P]
    y = [det_count(d) for d in P]
    jitter = rng.normal(0, .06, len(y))
    a2.scatter(x, np.array(y) + jitter, s=26, color=BLUE, alpha=.75, edgecolor="w", lw=.6)
    rho, p = stats.spearmanr(x, y)
    a2.set_xscale("log")
    a2.set_xticks([10, 20, 50, 100, 200]); a2.set_xticklabels(["10", "20", "50", "100", "200"])
    a2.set_xlabel("median seconds per item (log scale)")
    a2.set_ylabel("errors detected"); a2.set_yticks(range(5))
    a2.set_title(f"Participant-level association\n(\u03c1 = {rho:+.2f}, p = {p:.4f})")
    save(fig, "fig_4_4_time_dose_response")


def fig_predictor_correlations():
    y = [det_count(d) for d in P]
    preds = [
        ("Median seconds per item", [med_secs(d) for d in P], True),
        ("Seconds of evidence viewing", [hover_secs(d) for d in P], True),
        ("Writes patient information (B7)", [int(d["background"]["B7"]) for d in P], False),
        ("Years in healthcare (B3)", [YEARS.index(d["background"]["B3"]) for d in P], False),
        ("AI familiarity (B6)", [int(d["background"]["B6"]) for d in P], False),
        ("Reading comfort (B5)", [int(d["background"]["B5"]) for d in P], False),
        ("Age band (B10)", [AGES.index(d["background"]["B10"]) for d in P], False),
    ]
    fig, ax = plt.subplots(figsize=(6.6, 3.3))
    ys = np.arange(len(preds))
    for j, (lab, v, beh) in enumerate(preds):
        rho, p = stats.spearmanr(v, y)
        ax.barh(j, rho, .58, color=BLUE if beh else GREY)
        off = .02 if rho >= 0 else -.02
        ax.text(rho + off, j, f"{rho:+.3f}" + ("  *" if p < .05 else "  ns"),
                va="center", ha="left" if rho >= 0 else "right", fontsize=8,
                fontweight="bold" if p < .05 else "normal")
    ax.axvline(0, color="k", lw=.9)
    ax.set_yticks(ys); ax.set_yticklabels([p[0] for p in preds], fontsize=8)
    ax.invert_yaxis(); ax.set_xlim(-.3, .82)
    ax.set_xlabel("Spearman \u03c1 with number of errors detected")
    ax.legend(handles=[plt.Rectangle((0, 0), 1, 1, color=BLUE), plt.Rectangle((0, 0), 1, 1, color=GREY)],
              labels=["what the reviewer did", "who the reviewer is"], fontsize=8, loc="lower right")
    ax.set_title("Behavioural measures show the clearest associations with detection")
    save(fig, "fig_4_4_predictor_correlations")


def fig_detection_by_item():
    o, lo, hi, p = gee_or(DF, "strict ~ subtype", "subtype")
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(7.4, 3.2), gridspec_kw={"width_ratios": [1.5, 1]})
    xs = np.arange(4)
    vals = [100 * sum(detected(d, i) for d in P) / NP for i in ERR]
    cols = [BLUE if i in TYPE1 else TEAL for i in ERR]
    bars = a1.bar(xs, vals, .6, color=cols)
    a1.bar_label(bars, fmt="%.0f%%", fontsize=8, padding=2)
    a1.set_xticks(xs)
    a1.set_xticklabels([f"item {i}\n{NAMES[i]}" for i in ERR], fontsize=8)
    a1.set_ylabel("% detected"); a1.set_ylim(0, 60)
    a1.legend(handles=[plt.Rectangle((0, 0), 1, 1, color=BLUE), plt.Rectangle((0, 0), 1, 1, color=TEAL)],
              labels=["Type 1: source contradicts the rewrite", "Type 2: source is false too"], fontsize=7.5)
    a1.set_title("Detection by planted error")

    t1 = 100 * DF[DF.subtype == 1]["strict"].mean()
    t2 = 100 * DF[DF.subtype == 2]["strict"].mean()
    bars = a2.bar([0, 1], [t1, t2], .5, color=[BLUE, TEAL])
    a2.bar_label(bars, fmt="%.1f%%", fontsize=9, padding=2)
    a2.set_xticks([0, 1]); a2.set_xticklabels(["Type 1\n(n = 68)", "Type 2\n(n = 68)"], fontsize=8)
    a2.set_ylabel("% detected"); a2.set_ylim(0, 60)
    a2.set_title(f"OR {o:.2f} [{lo:.2f}, {hi:.2f}], p = {p:.3f}")
    save(fig, "fig_4_5_detection_by_error_type")


def fig_preferences():
    fig, (a1, a2, a3) = plt.subplots(1, 3, figsize=(7.6, 2.9))
    means = [st.mean([int(d["rationale"][k]) for d in P]) for k in ("S", "M", "L")]
    bars = a1.bar(range(3), np.array(means) - 1, .58, bottom=1, color=[GREEN, GREY, TEAL])
    a1.bar_label(bars, fmt="%.2f", fontsize=8, padding=2)
    a1.set_xticks(range(3)); a1.set_xticklabels(["Short", "Medium", "Detailed"], fontsize=8)
    a1.set_ylim(1, 5); a1.set_yticks([1, 2, 3, 4, 5]); a1.set_ylabel("mean usefulness (1-5)")
    a1.set_title("Rated usefulness")

    c = Counter(d["rationale"]["R2"] for d in P)
    keys = ["Short", "Medium", "Detailed", "No explanation by default"]
    vals = [c.get(k, 0) for k in keys]
    bars = a2.bar(range(4), vals, .6, color=[GREEN, GREY, TEAL, "#cbd5e0"])
    a2.bar_label(bars, fontsize=8, padding=2)
    a2.set_xticks(range(4)); a2.set_xticklabels(["Short", "Med.", "Det.", "None"], fontsize=8)
    a2.set_ylabel("participants"); a2.set_ylim(0, max(vals) + 4)
    a2.set_title("Preferred default")

    c = Counter(d["overall"]["O1"] for d in P)
    keys = ["Plain (A)", "With source passages (B)", "With source passages and explanations (C)"]
    vals = [c.get(k, 0) for k in keys]
    bars = a3.bar(range(3), vals, .6, color=[GREY, TEAL, BLUE])
    a3.bar_label(bars, fontsize=8, padding=2)
    a3.set_xticks(range(3)); a3.set_xticklabels(["A", "B", "C"], fontsize=9)
    a3.set_ylabel("participants"); a3.set_ylim(0, max(vals) + 4)
    a3.set_title("Preferred version")
    save(fig, "fig_4_6_explanation_and_version_preference")


def fig_subgroups():
    fig, axes = plt.subplots(1, 3, figsize=(7.6, 3.0))
    groups = [
        ("Language", lambda d: "English +\nGerman" if d["meta"]["language"] in ("en", "de") else "Albanian",
         ["English +\nGerman", "Albanian"], "p = .072"),
        ("Professional role", lambda d: "Physician" if d["background"]["B1"] == "Physician" else "Other roles",
         ["Physician", "Other roles"], "p = .14"),
        ("Gender", lambda d: d["background"]["B9"], ["Woman", "Man"], "not tested"),
    ]
    for ax, (title, key, order, note) in zip(axes, groups):
        buckets = {}
        for d in P:
            buckets.setdefault(key(d), []).append(det_count(d))
        vals = [100 * st.mean(buckets[k]) / 4 if buckets.get(k) else 0 for k in order]
        ns = [len(buckets.get(k, [])) for k in order]
        bars = ax.bar(range(len(order)), vals, .55, color=[BLUE, GREY])
        ax.bar_label(bars, labels=[f"{v:.0f}%\nn={n}" for v, n in zip(vals, ns)], fontsize=8, padding=2)
        ax.set_xticks(range(len(order))); ax.set_xticklabels(order, fontsize=8)
        ax.set_ylim(0, 78); ax.set_title(f"{title}  ({note})", fontsize=9)
        if ax is axes[0]:
            ax.set_ylabel("% of the four errors detected")
    fig.suptitle("Subgroup differences are confounded and none reached significance",
                 fontsize=10, fontweight="bold", y=1.04)
    save(fig, "fig_4_7_subgroup_detection")


def fig_a_sensitivity():
    sets = [("unfiltered\nN=42", load("unfiltered")), ("primary\nN=34", P),
            ("strict\nN=27", load("strict"))]
    specs = [("Detected", lambda S: 100 * sum(detected(d, i) for d in S for i in ERR) / (4 * len(S))),
             ("Approved\nwrong", lambda S: 100 * sum(approved(d, i) for d in S for i in ERR) / (4 * len(S))),
             ("Confidently\nwrong", lambda S: 100 * sum(
                 approved(d, i) and int(q(d, i, "q4")) >= 4 for d in S for i in ERR) / (4 * len(S))),
             ("Detected\nnothing", lambda S: 100 * sum(det_count(d) == 0 for d in S) / len(S)),
             ("Approved\nall 8", lambda S: 100 * sum(
                 all(approved(d, i) for i in range(1, 9)) for d in S) / len(S))]
    fig, ax = plt.subplots(figsize=(7.4, 3.4))
    w, xs = .26, np.arange(len(specs))
    for j, (lab, S) in enumerate(sets):
        vals = [fn(S) for _, fn in specs]
        bars = ax.bar(xs + (j - 1) * w, vals, w, label=lab, color=[GREY, BLUE, TEAL][j])
        ax.bar_label(bars, fmt="%.0f", fontsize=7, padding=1)
    ax.set_xticks(xs); ax.set_xticklabels([s[0] for s in specs], fontsize=8)
    ax.set_ylabel("%"); ax.set_ylim(0, 70); ax.legend(fontsize=8, ncol=3)
    ax.set_title("Headline measures across three dataset definitions")
    save(fig, "fig_A_1_sensitivity_across_datasets")


def fig_a_exclusion():
    groups = [("retained clean", "", GREEN, "o"), ("borderline", "borderline", AMBER, "^"),
              ("excluded", "excluded", RED, "X")]
    data = []
    for lab, folder, c, mk in groups:
        pat = os.path.join(DATA, folder, "*.txt") if folder else os.path.join(DATA, "*.txt")
        D = []
        for p in sorted(glob.glob(pat)):
            d = json.load(open(p, encoding="utf-8")); d["_f"] = os.path.basename(p)[:-4]; D.append(d)
        data.append((lab, D, c, mk))

    fig, (a1, a2) = plt.subplots(1, 2, figsize=(7.6, 3.4), gridspec_kw={"width_ratios": [1, 1.25]})
    for j, (lab, D, c, mk) in enumerate(data):
        xs = rng.normal(j, .07, len(D))
        ys = [med_secs(d) for d in D]
        a1.scatter(xs, ys, s=38, marker=mk, color=c, alpha=.85, edgecolor="w", lw=.5)
        a1.plot([j - .28, j + .28], [st.median(ys)] * 2, color="#2d3748", lw=2)
        a1.text(j + .32, st.median(ys), f"median {st.median(ys):.0f} s",
                fontsize=7.5, va="center", ha="left", color="#2d3748")
    a1.axhline(20, color=RED, ls="--", lw=1)
    a1.text(-.45, 21, "20 s speed flag", color=RED, fontsize=7, ha="left")
    a1.set_yscale("log"); a1.set_yticks([10, 20, 50, 100, 200])
    a1.set_yticklabels(["10", "20", "50", "100", "200"])
    a1.set_xlim(-.5, 2.9)
    a1.set_xticks(range(3)); a1.set_xticklabels([f"{l}\nn={len(D)}" for l, D, _, _ in data], fontsize=8)
    a1.set_ylabel("median seconds per item (log scale)")
    a1.set_title("Review time by stored group")

    for lab, D, c, mk in data:
        x = [WORDS_PER_ITEM_SCREEN / (med_secs(d) / 60) for d in D]
        y = [det_count(d) + rng.normal(0, .07) for d in D]
        a2.scatter(x, y, s=40, marker=mk, color=c, label=f"{lab} (n={len(D)})",
                   alpha=.85, edgecolor="w", lw=.5)
    a2.axvspan(200, 250, color="#68d391", alpha=.18)
    a2.text(225, 4.45, "normal adult\nreading speed", ha="center", fontsize=7, color="#22543d")
    a2.set_xlabel("implied reading speed (words per minute)")
    a2.set_ylabel("errors detected"); a2.set_yticks(range(5)); a2.set_ylim(-.5, 5.0)
    a2.legend(fontsize=7.5, loc="upper right")
    a2.set_title("Review time and error detection")
    fig.suptitle("Recorded review times by stored screening group",
                 fontsize=9, fontweight="bold", y=1.05)
    save(fig, "fig_A_2_screening_and_reading_speed")


def fig_a_leave_one_out():
    fig, ax = plt.subplots(figsize=(6.0, 2.8))
    full = 100 * sum(detected(d, i) for d in P for i in ERR) / (4 * NP)
    labs, vals = ["all four items"], [full]
    for drop in ERR:
        keep = [i for i in ERR if i != drop]
        vals.append(100 * sum(detected(d, i) for d in P for i in keep) / (len(keep) * NP))
        labs.append(f"without item {drop}\n{NAMES[drop]}")
    bars = ax.bar(range(5), vals, .58, color=[BLUE] + [GREY] * 4)
    ax.bar_label(bars, fmt="%.1f%%", fontsize=8, padding=2)
    ax.axhline(full, color=BLUE, ls="--", lw=.9)
    ax.set_xticks(range(5)); ax.set_xticklabels(labs, fontsize=7.5)
    ax.set_ylabel("% detected"); ax.set_ylim(0, 55)
    ax.set_title("No single planted error drives the detection rate")
    save(fig, "fig_A_3_leave_one_out")


def fig_a_hover_threshold():
    fig, ax = plt.subplots(figsize=(5.8, 2.8))
    thrs = [300, 500, 1000]
    for j, t in enumerate(thrs):
        df = frame(P, t)
        o, lo, hi, _ = gee_or(df, "strict ~ open_any + C(item)", "open_any")
        ax.plot([lo, hi], [j, j], color=BLUE, lw=2.2)
        ax.plot(o, j, "o", color=BLUE, ms=8)
        ax.text(hi + .25, j, f"OR {o:.2f} [{lo:.2f}, {hi:.2f}]", va="center", fontsize=8)
    ax.axvline(1, color="k", ls="--", lw=.9)
    ax.set_yticks(range(3)); ax.set_yticklabels([f"{t} ms" for t in thrs])
    ax.set_ylabel("minimum dwell counted as\na real popover opening")
    ax.set_xlabel("adjusted odds ratio for detection"); ax.set_xlim(0, 14)
    ax.invert_yaxis(); ax.set_title("The 500 ms threshold is not doing the work")
    save(fig, "fig_A_4_hover_threshold_sensitivity")


def fig_a_dwell_distribution():
    d = [x for dd in load("unfiltered") for it in dd["items"].values()
         for r in it.get("hovers", {}).values() for x in r.get("dwellsMs", []) if x <= 6000]
    fig, ax = plt.subplots(figsize=(6.4, 3.0))
    ax.hist(d, bins=60, color=BLUE)
    ax.axvline(DWELL_MS, color=RED, ls="--", lw=1.4)
    ax.text(DWELL_MS + 110, ax.get_ylim()[1] * .82, f"{DWELL_MS} ms threshold", color=RED, fontsize=8)
    ax.set_xlabel("duration of a single popover opening (ms, capped at 6000)")
    ax.set_ylabel("count")
    ax.set_title("Distribution of recorded popover dwell durations")
    save(fig, "fig_A_5_hover_dwell_distribution")


def fig_a_sample():
    fig, axes = plt.subplots(1, 4, figsize=(7.8, 2.9))
    panels = [
        ("Language", lambda d: {"en": "English", "de": "German", "sq": "Albanian"}[d["meta"]["language"]], None),
        ("Role", lambda d: d["background"]["B1"] if d["background"]["B1"] in ("Physician", "Nurse") else "Other", None),
        ("Years in healthcare", lambda d: d["background"]["B3"], YEARS),
        ("Age band", lambda d: d["background"]["B10"], AGES),
    ]
    for ax, (title, key, order) in zip(axes, panels):
        c = Counter(key(d) for d in P)
        keys = order or [k for k, _ in c.most_common()]
        keys = [k for k in keys if c.get(k, 0) > 0]
        vals = [c[k] for k in keys]
        bars = ax.bar(range(len(keys)), vals, .62, color=BLUE)
        ax.bar_label(bars, fontsize=7.5, padding=1)
        ax.set_xticks(range(len(keys)))
        ax.set_xticklabels(keys, fontsize=7, rotation=35, ha="right")
        ax.set_ylim(0, max(vals) + 4)
        ax.set_title(title, fontsize=9)
        if ax is axes[0]:
            ax.set_ylabel("participants")
    fig.suptitle(f"Sample composition (N = {NP})", fontsize=10, fontweight="bold", y=1.05)
    save(fig, "fig_A_6_sample_composition")


if __name__ == "__main__":
    print(f"primary dataset: N = {NP}, {4 * NP} error decisions")
    print("results figures:")
    fig_outcome_composition()
    fig_headline_rates()
    fig_participant_distribution()
    fig_confidence_calibration()
    fig_support_opened()
    fig_clustering_adjustment()
    fig_time_dose_response()
    fig_predictor_correlations()
    fig_detection_by_item()
    fig_preferences()
    fig_subgroups()
    print("appendix figures:")
    fig_a_sensitivity()
    fig_a_exclusion()
    fig_a_leave_one_out()
    fig_a_hover_threshold()
    fig_a_dwell_distribution()
    fig_a_sample()
    print(f"\nall figures written to {OUT} (png + pdf)")
