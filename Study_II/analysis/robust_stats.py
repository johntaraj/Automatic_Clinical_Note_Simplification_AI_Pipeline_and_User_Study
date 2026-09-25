"""Participant-clustered analyses: bootstrap intervals and GEE odds ratios.

Usage:
    python analysis/robust_stats.py [--strict | --all] [--figures]
"""

import json, glob, os, sys, math, warnings, statistics as st
from collections import defaultdict

import numpy as np
import pandas as pd
from scipy import stats
import statsmodels.api as sm
from statsmodels.genmod.generalized_estimating_equations import GEE
from statsmodels.genmod.families import Binomial
from statsmodels.genmod.cov_struct import Exchangeable

warnings.filterwarnings("ignore")
rng = np.random.default_rng(20260824)

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DATA = os.path.join(ROOT, "data")
ERR, CLEAN = [2, 4, 6, 8], [1, 3, 5, 7]
SUB1, SUB2 = [2, 6], [4, 8]
CLIN = {"Clinically incorrect", "Misleading", "Important information is missing"}
NAMES = {2: "anticoagulation", 4: "dysphagia", 6: "analgesia", 8: "hyperkalemia"}


def load(which):
    paths = sorted(glob.glob(os.path.join(DATA, "*.txt")))
    if which in ("primary", "all"):
        paths += sorted(glob.glob(os.path.join(DATA, "borderline", "*.txt")))
    if which == "all":
        paths += sorted(glob.glob(os.path.join(DATA, "excluded", "*.txt")))
    out = []
    for p in paths:
        d = json.load(open(p, encoding="utf-8"))
        d["_f"] = os.path.basename(p)[:-4]
        out.append(d)
    return out


q = lambda d, i, k: d["items"][str(i)]["q"][k]
strict_det = lambda d, i: q(d, i, "q2") == "No" and q(d, i, "q3") in CLIN
loose_det = lambda d, i: q(d, i, "q2") == "No"


def dwell(d, i, key, thr):
    r = d["items"][str(i)].get("hovers", {}).get(key, {})
    return sum(x for x in r.get("dwellsMs", []) if x >= thr)


def long_frame(D, thr=500):
    rows = []
    for d in D:
        for i in ERR:
            rows.append(dict(
                pid=d["_f"], item=i, subtype=1 if i in SUB1 else 2,
                strict=int(strict_det(d, i)), loose=int(loose_det(d, i)),
                approved=int(q(d, i, "q2") == "Yes"),
                conf=int(q(d, i, "q4")),
                open_b=int(dwell(d, i, "0_B", thr) > 0),
                open_c=int(dwell(d, i, "0_C", thr) > 0),
                open_any=int(dwell(d, i, "0_B", thr) > 0 or dwell(d, i, "0_C", thr) > 0),
                c_dwell=dwell(d, i, "0_C", thr) / 1000,
            ))
    return pd.DataFrame(rows)


def boot_prop(D, fn, n_boot=5000):
    people = list(D)
    point = fn(people)
    draws = []
    for _ in range(n_boot):
        samp = [people[k] for k in rng.integers(0, len(people), len(people))]
        try:
            draws.append(fn(samp))
        except ZeroDivisionError:
            pass
    lo, hi = np.percentile(draws, [2.5, 97.5])
    return point, lo, hi


def gee_fit(df, formula, group="pid"):
    m = GEE.from_formula(formula, groups=group, data=df,
                         family=Binomial(), cov_struct=Exchangeable())
    return m.fit()


def show_gee(res, term, label):
    b = res.params[term]
    se = res.bse[term]
    lo, hi = b - 1.96 * se, b + 1.96 * se
    p = res.pvalues[term]
    print(f"    {label:<34} OR={math.exp(b):6.2f}  95% CI [{math.exp(lo):.2f}, {math.exp(hi):.2f}]  p={p:.4f}")


def main():
    which = "primary"
    if "--strict" in sys.argv: which = "strict"
    if "--all" in sys.argv: which = "all"
    D = load(which)
    df = long_frame(D)
    n = len(D)
    print(f"\n{'='*74}\nROBUST ANALYSIS: {which.upper()}   {n} participants, {len(df)} error decisions\n{'='*74}")

    print("\n1. HEADLINE PROPORTIONS with participant-clustered bootstrap CIs")
    print("   (resampling participants, not decisions, so nesting is respected)")
    defs = [
        ("strict detection", lambda P: sum(strict_det(d, i) for d in P for i in ERR) / (4 * len(P))),
        ("loose detection (Q2=No)", lambda P: sum(loose_det(d, i) for d in P for i in ERR) / (4 * len(P))),
        ("approved a wrong item", lambda P: sum(q(d, i, "q2") == "Yes" for d in P for i in ERR) / (4 * len(P))),
        ("false alarm on clean items", lambda P: sum(q(d, i, "q2") == "No" for d in P for i in CLEAN) / (4 * len(P))),
        ("high-confidence unsafe approval", lambda P: sum(
            q(d, i, "q2") == "Yes" and int(q(d, i, "q4")) >= 4 for d in P for i in ERR) / (4 * len(P))),
    ]
    for lab, fn in defs:
        pt, lo, hi = boot_prop(D, fn)
        print(f"    {lab:<34} {100*pt:5.1f}%   95% CI [{100*lo:.1f}, {100*hi:.1f}]")

    print("\n2. ERROR-RELEVANT SUPPORT ASSOCIATION, participant-clustered GEE with item fixed effects")
    a = df[(df.open_any == 1) & (df.strict == 1)].shape[0]
    b = df[(df.open_any == 1) & (df.strict == 0)].shape[0]
    c = df[(df.open_any == 0) & (df.strict == 1)].shape[0]
    e = df[(df.open_any == 0) & (df.strict == 0)].shape[0]
    orr, pf = stats.fisher_exact([[a, b], [c, e]])
    print(f"    descriptive: opened {a}/{a+b} = {100*a/(a+b):.0f}%   not opened {c}/{c+e} = {100*c/(c+e):.0f}%")
    print(f"    unadjusted Fisher (NOT the primary test): OR={orr:.1f} p={pf:.2e}")
    res = gee_fit(df, "strict ~ open_any + C(item)")
    show_gee(res, "open_any", "adjusted OR, opened error-relevant support")

    print("\n3. WHICH SUPPORT? B source vs C explanation, separately")
    for state, sub in [("neither", df[(df.open_b == 0) & (df.open_c == 0)]),
                       ("B source only", df[(df.open_b == 1) & (df.open_c == 0)]),
                       ("C explanation only", df[(df.open_b == 0) & (df.open_c == 1)]),
                       ("both", df[(df.open_b == 1) & (df.open_c == 1)])]:
        if len(sub):
            print(f"    {state:<20} n={len(sub):<4} detected {100*sub.strict.mean():5.1f}%")
    res2 = gee_fit(df, "strict ~ open_b + open_c + C(item)")
    show_gee(res2, "open_b", "adjusted OR, opened B source")
    show_gee(res2, "open_c", "adjusted OR, opened C explanation")

    print("\n4. SUBTYPE CONTRAST, clustered")
    s1 = df[df.subtype == 1].strict.mean()
    s2 = df[df.subtype == 2].strict.mean()
    print(f"    subtype 1 (contradiction visible) {100*s1:.1f}%   subtype 2 (falsified passage) {100*s2:.1f}%")
    res3 = gee_fit(df, "strict ~ subtype")
    b3 = res3.params["subtype"]; se3 = res3.bse["subtype"]
    print(f"    adjusted OR per step toward subtype 2 = {math.exp(b3):.2f} "
          f"95% CI [{math.exp(b3-1.96*se3):.2f}, {math.exp(b3+1.96*se3):.2f}] p={res3.pvalues['subtype']:.4f}")
    print("    NOTE: only two items instantiate each subtype, so this is conditional on these four stimuli.")

    print("\n5. CONFIDENCE: does it discriminate correct from incorrect?")
    for lvl in range(1, 6):
        sub = df[df.conf == lvl]
        if len(sub):
            print(f"    confidence {lvl}: n={len(sub):<4} correct {100*sub.strict.mean():5.1f}%")
    res4 = gee_fit(df, "strict ~ conf + C(item)")
    show_gee(res4, "conf", "adjusted OR per +1 confidence point")

    print("\n6. SIGNAL DETECTION with a consistent response rule")
    print("    Hits and false alarms both use Q2 rejection.")
    for lab, hit_fn in [("consistent (Q2 rejection for both)", loose_det),
                        ("strict hits (inconsistent, for reference only)", strict_det)]:
        dp, criterion = [], []
        for d in D:
            h = sum(hit_fn(d, i) for i in ERR) / 4
            f = sum(q(d, i, "q2") == "No" for i in CLEAN) / 4
            h = min(max(h, 0.5 / 4), (4 - 0.5) / 4)
            f = min(max(f, 0.5 / 4), (4 - 0.5) / 4)
            zh, zf = stats.norm.ppf(h), stats.norm.ppf(f)
            dp.append(zh - zf)
            criterion.append(-0.5 * (zh + zf))
        t, p = stats.ttest_1samp(dp, 0)
        print(f"    {lab:<46} d'={st.mean(dp):+.2f}  c={st.mean(criterion):+.2f}  "
              f"t={t:.2f} p={p:.4f}")

    print("\n7. LEAVE-ONE-ITEM-OUT stability of strict detection")
    for drop in ERR:
        sub = df[df.item != drop]
        print(f"    without item {drop} ({NAMES[drop]:<15}) detection = {100*sub.strict.mean():5.1f}%")
    print(f"    all four items                       detection = {100*df.strict.mean():5.1f}%")

    print("\n8. HOVER THRESHOLD SENSITIVITY")
    for thr in (300, 500, 1000, 2000):
        d2 = long_frame(D, thr)
        o = d2[d2.open_any == 1]; nn = d2[d2.open_any == 0]
        r = gee_fit(d2, "strict ~ open_any + C(item)")
        bb = r.params["open_any"]; ss = r.bse["open_any"]
        print(f"    {thr:>5} ms: opened {100*o.strict.mean():5.1f}% (n={len(o)})  "
              f"not opened {100*nn.strict.mean():5.1f}% (n={len(nn)})  "
              f"adjOR={math.exp(bb):5.2f} [{math.exp(bb-1.96*ss):.2f}, {math.exp(bb+1.96*ss):.2f}]")

    print("\n9. STRICT vs LOOSE detection definition")
    print(f"    strict (rejection + clinical reason) {100*df.strict.mean():5.1f}%")
    print(f"    loose  (rejection, any reason)       {100*df.loose.mean():5.1f}%")
    print(f"    rejections given a non-clinical reason: {df.loose.sum()-df.strict.sum()} of {df.loose.sum()}")

    print("\n10. ENGAGEMENT AND DETECTION, participant level, clustered")
    med_t = [st.median([d["timing"]["perScreenMs"].get(f"item{i}", 0) / 1000 for i in range(1, 9)]) for d in D]
    det_n = [sum(strict_det(d, i) for i in ERR) for d in D]
    r, p = stats.spearmanr(med_t, det_n)
    print(f"    median seconds per item vs errors caught: rho={r:+.3f} p={p:.4f}  (participant level, n={n})")
    tmap = {d["_f"]: math.log10(max(t, 1)) for d, t in zip(D, med_t)}
    df["logt"] = df.pid.map(tmap)
    res5 = gee_fit(df, "strict ~ logt + C(item)")
    show_gee(res5, "logt", "adjusted OR per 10x time per item")
    print("    Engagement was self-selected, so this is an association and not a causal estimate.")

    print("\n11. PLANNED H3: VERSION C DWELL AND TYPE 2 DETECTION")
    type2 = df[df.subtype == 2].copy()
    opened_c = type2[type2.open_c == 1]
    closed_c = type2[type2.open_c == 0]
    print(f"    C opened     {opened_c.strict.sum():.0f}/{len(opened_c)} = {100*opened_c.strict.mean():.1f}%")
    print(f"    C not opened {closed_c.strict.sum():.0f}/{len(closed_c)} = {100*closed_c.strict.mean():.1f}%")
    per_person = type2.groupby("pid").agg(c_dwell=("c_dwell", "sum"), strict=("strict", "sum"))
    r, p = stats.spearmanr(per_person.c_dwell, per_person.strict)
    print(f"    participant-level total C dwell vs Type 2 detections: rho={r:+.3f} p={p:.4f}")
    type2["log_c_dwell"] = np.log10(1 + type2.c_dwell)
    res6 = gee_fit(type2, "strict ~ log_c_dwell + C(item)")
    show_gee(res6, "log_c_dwell", "adjusted OR per 10x (1 + C seconds)")
    print("    Dwell was self-selected, so the association does not establish an explanation effect.")

    if "--figures" in sys.argv:
        make_figures()


def make_figures():
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    figs = os.path.join(ROOT, "figures")
    os.makedirs(figs, exist_ok=True)
    plt.rcParams.update({"figure.dpi": 150, "font.size": 9,
                         "axes.spines.top": False, "axes.spines.right": False})
    sets = {"unfiltered": "all", "primary": "primary", "strict": "strict"}
    colors = {"unfiltered": "#b0b7c3", "primary": "#2b6cb0", "strict": "#7cc4a4"}

    fig, ax = plt.subplots(figsize=(7, 3.5))
    states = [("neither", 0, 0), ("B source\nonly", 1, 0), ("C explanation\nonly", 0, 1), ("both", 1, 1)]
    xs = np.arange(len(states))
    for j, (lab, key) in enumerate(sets.items()):
        d2 = long_frame(load(key))
        vals, ns = [], []
        for _, ob, oc in states:
            sub = d2[(d2.open_b == ob) & (d2.open_c == oc)]
            vals.append(100 * sub.strict.mean() if len(sub) else 0)
            ns.append(len(sub))
        bars = ax.bar(xs + (j - 1) * 0.26, vals, 0.26, color=colors[lab], label=lab)
        ax.bar_label(bars, labels=[f"{v:.0f}%\nn={n}" for v, n in zip(vals, ns)], fontsize=6.5, padding=1)
    ax.set_xticks(xs); ax.set_xticklabels([s[0] for s in states])
    ax.set_ylabel("% of error decisions detected"); ax.set_ylim(0, 82)
    ax.legend(frameon=False, fontsize=8)
    ax.set_title("Detection by which supporting information was opened")
    fig.tight_layout(); fig.savefig(os.path.join(figs, "F11_support_states.png"), bbox_inches="tight")
    plt.close(fig); print("  wrote F11_support_states.png")

    fig, ax = plt.subplots(figsize=(7, 2.9))
    rows = []
    for lab, key in sets.items():
        D = load(key); d2 = long_frame(D)
        a = d2[(d2.open_any == 1) & (d2.strict == 1)].shape[0]
        b = d2[(d2.open_any == 1) & (d2.strict == 0)].shape[0]
        c = d2[(d2.open_any == 0) & (d2.strict == 1)].shape[0]
        e = d2[(d2.open_any == 0) & (d2.strict == 0)].shape[0]
        unadj = stats.fisher_exact([[a, b], [c, e]])[0]
        r = gee_fit(d2, "strict ~ open_any + C(item)")
        bb, ss = r.params["open_any"], r.bse["open_any"]
        rows.append((lab, unadj, math.exp(bb), math.exp(bb - 1.96 * ss), math.exp(bb + 1.96 * ss)))
    y = np.arange(len(rows))
    ax.scatter([r[1] for r in rows], y + .15, marker="o", s=45, color="#c53030", label="unadjusted Fisher (overstated)")
    ax.scatter([r[2] for r in rows], y - .15, marker="s", s=45, color="#2b6cb0", label="participant-clustered GEE")
    for i, r in enumerate(rows):
        ax.plot([r[3], r[4]], [i - .15, i - .15], color="#2b6cb0", lw=2)
    ax.axvline(1, color="k", lw=.8, ls=":")
    ax.set_xscale("log"); ax.set_yticks(y); ax.set_yticklabels([r[0] for r in rows])
    ax.set_xlabel("odds ratio for detection after opening error-relevant support (log scale)")
    ax.legend(frameon=False, fontsize=8, loc="lower right")
    ax.set_title("Correcting for nesting shrinks the effect by roughly fourfold")
    fig.tight_layout(); fig.savefig(os.path.join(figs, "F12_or_comparison.png"), bbox_inches="tight")
    plt.close(fig); print("  wrote F12_or_comparison.png")


if __name__ == "__main__":
    main()
