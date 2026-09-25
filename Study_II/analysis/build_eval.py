"""Headline measures for the three inclusion sets (unfiltered, primary, strict).

Usage:
    python analysis/build_eval.py [--figures]
"""

import json, glob, os, math, sys, statistics as st
from collections import Counter, defaultdict

import numpy as np
from scipy import stats

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DATA = os.path.join(ROOT, "data")
FIGS = os.path.join(ROOT, "figures")

ERR = [2, 4, 6, 8]
CLEAN = [1, 3, 5, 7]
SUB1, SUB2 = [2, 6], [4, 8]
CLIN = {"Clinically incorrect", "Misleading", "Important information is missing"}
NAMES = {2: "anticoagulation", 4: "dysphagia", 6: "analgesia", 8: "hyperkalemia"}
SWAPS = {1: 3, 2: 2, 3: 2, 4: 2, 5: 2, 6: 2, 7: 2, 8: 3}
DWELL_MIN_MS = 500


def _read(folder=""):
    pat = os.path.join(DATA, folder, "*.txt") if folder else os.path.join(DATA, "*.txt")
    out = []
    for p in sorted(glob.glob(pat)):
        d = json.load(open(p, encoding="utf-8"))
        d["_f"] = os.path.basename(p)[:-4]
        out.append(d)
    return out


CLEAN_SET = _read()
BORDER = _read("borderline")
EXCLUDED = _read("excluded")
SETS = {
    "unfiltered": CLEAN_SET + BORDER + EXCLUDED,
    "primary": CLEAN_SET + BORDER,
    "strict": CLEAN_SET,
}

q = lambda d, i, k: d["items"][str(i)]["q"][k]
detected = lambda d, i: q(d, i, "q2") == "No" and q(d, i, "q3") in CLIN
det_count = lambda d: sum(detected(d, i) for i in ERR)
n_swaps = lambda d, i: 2 if (d["meta"]["language"] == "sq" and i == 8) else SWAPS[i]
real_dwell = lambda r: sum(x for x in r.get("dwellsMs", []) if x >= DWELL_MIN_MS)
opened = lambda d, i, k: real_dwell(d["items"][str(i)].get("hovers", {}).get(k, {})) > 0
opened_dec = lambda d, i: opened(d, i, "0_B") or opened(d, i, "0_C")
med_item = lambda d: st.median([d["timing"]["perScreenMs"].get(f"item{i}", 0) / 1000 for i in range(1, 9)])
lang2 = lambda d: "en+de" if d["meta"]["language"] in ("en", "de") else "sq"


def dwell_ver(d, suf):
    return sum(real_dwell(r) for it in d["items"].values()
               for k, r in it.get("hovers", {}).items() if k.endswith(suf)) / 1000


def wilson(k, n):
    if n == 0:
        return (0.0, 0.0)
    z, p = 1.96, k / n
    den = 1 + z * z / n
    c = (p + z * z / (2 * n)) / den
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / den
    return (max(0, c - h) * 100, min(1, c + h) * 100)


def cliffs(a, b):
    a, b = list(a), list(b)
    return sum((x > y) - (x < y) for x in a for y in b) / (len(a) * len(b)) if a and b else 0.0


def rbc(x, y):
    dd = [a - b for a, b in zip(x, y) if a != b]
    if not dd:
        return 0.0
    r = stats.rankdata([abs(v) for v in dd])
    return (sum(r[i] for i, v in enumerate(dd) if v > 0)
            - sum(r[i] for i, v in enumerate(dd) if v < 0)) / sum(r)


def holm(p_values):
    order = sorted(range(len(p_values)), key=lambda i: p_values[i])
    adjusted, running = [0.0] * len(p_values), 0.0
    for rank, index in enumerate(order):
        running = max(running, min(1.0, (len(p_values) - rank) * p_values[index]))
        adjusted[index] = running
    return adjusted


def metrics(D):
    n = len(D)
    dec = [(d, i) for d in D for i in ERR]
    m = {}
    m["n"] = n
    m["decisions"] = len(dec)
    m["detected"] = sum(detected(d, i) for d, i in dec)
    m["approved"] = sum(q(d, i, "q2") == "Yes" for d, i in dec)
    m["fa"] = sum(q(d, i, "q2") == "No" for d in D for i in CLEAN)
    m["conf_wrong"] = sum(1 for d, i in dec if q(d, i, "q2") == "Yes" and int(q(d, i, "q4")) >= 4)
    m["all_yes"] = sum(1 for d in D if all(q(d, i, "q2") == "Yes" for i in range(1, 9)))
    m["zero"] = sum(1 for d in D if det_count(d) == 0)
    m["perfect"] = sum(1 for d in D if det_count(d) == 4)
    m["looked_missed"] = sum(1 for d, i in dec if q(d, i, "q2") == "Yes" and opened_dec(d, i))

    a = b = c = e = 0
    for d, i in dec:
        if opened_dec(d, i):
            a, b = (a + 1, b) if detected(d, i) else (a, b + 1)
        else:
            c, e = (c + 1, e) if detected(d, i) else (c, e + 1)
    m["ev"] = (a, b, c, e)
    m["ev_open_rate"] = 100 * a / max(a + b, 1)
    m["ev_shut_rate"] = 100 * c / max(c + e, 1)
    orr, pv = stats.fisher_exact([[a, b], [c, e]])
    m["ev_or"], m["ev_p"] = orr, pv

    m["sub1"] = sum(detected(d, i) for d in D for i in SUB1)
    m["sub2"] = sum(detected(d, i) for d in D for i in SUB2)
    x = [sum(detected(d, i) for i in SUB1) for d in D]
    y = [sum(detected(d, i) for i in SUB2) for d in D]
    m["sub_p"] = stats.wilcoxon(x, y, zero_method="wilcox")[1]

    m["per_item"] = {i: (100 * sum(detected(d, i) for d in D) / n,
                         100 * sum(q(d, i, "q2") == "Yes" for d in D) / n,
                         100 * sum(opened_dec(d, i) for d in D) / n) for i in ERR}

    cr, wr = [], []
    for d in D:
        rc = [int(q(d, i, "q4")) for i in ERR if detected(d, i)]
        rw = [int(q(d, i, "q4")) for i in ERR if not detected(d, i)]
        if rc and rw:
            cr.append(st.mean(rc)); wr.append(st.mean(rw))
    m["conf_pairs"] = len(cr)
    m["conf_right"] = st.mean(cr) if cr else float("nan")
    m["conf_wrongm"] = st.mean(wr) if wr else float("nan")
    m["conf_p"] = stats.wilcoxon(cr, wr, zero_method="wilcox")[1] if len(cr) >= 6 else float("nan")

    m["calib"] = {}
    for lvl in range(1, 6):
        tot = sum(1 for d, i in dec if int(q(d, i, "q4")) == lvl)
        ok = sum(1 for d, i in dec if int(q(d, i, "q4")) == lvl and detected(d, i))
        m["calib"][lvl] = (ok, tot)

    bins = defaultdict(list)
    for d in D:
        t = med_item(d)
        bins["<20" if t < 20 else "20-40" if t < 40 else "40-80" if t < 80 else ">=80"].append(det_count(d))
    m["dose"] = {k: (len(v), st.mean(v)) for k, v in bins.items()}

    det = [det_count(d) for d in D]
    m["corr"] = {}
    for lab, vals in [
        ("time", [med_item(d) for d in D]),
        ("hover", [dwell_ver(d, "_B") + dwell_ver(d, "_C") for d in D]),
        ("B7 comms", [int(d["background"]["B7"]) for d in D]),
        ("B3 years", [["<1", "1-3", "4-7", "8-15", ">15"].index(d["background"]["B3"]) for d in D]),
        ("B6 AI", [int(d["background"]["B6"]) for d in D]),
        ("B5 reading", [int(d["background"]["B5"]) for d in D]),
        ("B10 age", [["18-24", "25-34", "35-44", "45-54", "55-64", "65+"].index(d["background"]["B10"])
                     if d["background"].get("B10") else np.nan for d in D]),
    ]:
        pr = [(v, dd) for v, dd in zip(vals, det) if not (isinstance(v, float) and math.isnan(v))]
        m["corr"][lab] = stats.spearmanr([p[0] for p in pr], [p[1] for p in pr])

    g = defaultdict(list)
    for d in D:
        g[lang2(d)].append(det_count(d))
    m["lang"] = {k: (len(v), st.mean(v)) for k, v in g.items()}
    m["lang_p"] = stats.mannwhitneyu(g["en+de"], g["sq"])[1]
    m["lang_d"] = cliffs(g["en+de"], g["sq"])
    t = defaultdict(list)
    for d in D:
        t[lang2(d)].append(med_item(d))
    m["lang_time"] = {k: st.median(v) for k, v in t.items()}

    x = np.array([1.0 if lang2(d) == "en+de" else 0.0 for d in D])
    y = np.array([float(det_count(d)) for d in D])
    z = np.array([med_item(d) for d in D])
    A = np.vstack([z, np.ones_like(z)]).T
    res = lambda v: v - A @ np.linalg.lstsq(A, v, rcond=None)[0]
    m["lang_raw"] = stats.spearmanr(x, y)
    m["lang_part"] = stats.pearsonr(res(x), res(y))

    r = defaultdict(list)
    for d in D:
        r[d["background"]["B1"]].append(det_count(d))
    m["role"] = {k: (len(v), st.mean(v)) for k, v in r.items()}
    ph = [det_count(d) for d in D if d["background"]["B1"] == "Physician"]
    ot = [det_count(d) for d in D if d["background"]["B1"] != "Physician"]
    m["role_p"] = stats.mannwhitneyu(ph, ot)[1]
    m["role_d"] = cliffs(ph, ot)
    m["role_means"] = (st.mean(ph), st.mean(ot))

    gg = defaultdict(list)
    for d in D:
        if d["background"].get("B9"):
            gg[d["background"]["B9"]].append(det_count(d))
    m["gender"] = {k: (len(v), st.mean(v)) for k, v in gg.items()}
    ag = defaultdict(list)
    for d in D:
        if d["background"].get("B10"):
            ag[d["background"]["B10"]].append(det_count(d))
    m["age"] = {k: (len(v), st.mean(v)) for k, v in sorted(ag.items())}

    S = [int(d["rationale"]["S"]) for d in D]
    M = [int(d["rationale"]["M"]) for d in D]
    L = [int(d["rationale"]["L"]) for d in D]
    m["expl"] = (st.mean(S), st.mean(M), st.mean(L))
    m["expl_p"] = stats.friedmanchisquare(S, M, L)[1]
    pairwise = [stats.wilcoxon(a, b, zero_method="wilcox")[1]
                for a, b in [(S, M), (S, L), (M, L)]]
    m["expl_pair_raw"] = pairwise
    m["expl_pair_holm"] = holm(pairwise)
    m["expl_sm"] = m["expl_pair_holm"][0]
    m["R2"] = dict(Counter(d["rationale"]["R2"] for d in D))
    m["O1"] = dict(Counter(d["overall"]["O1"] for d in D))
    m["O"] = {k: st.mean([int(d["overall"][k]) for d in D]) for k in ["O2", "O3", "O4", "O5"]}
    m["Q5"] = st.mean([int(q(d, i, "q5")) for d in D for i in range(1, 9)])
    m["Q6"] = st.mean([int(q(d, i, "q6")) for d in D for i in range(1, 9)])

    q1c = [st.mean([int(q(d, i, "q1")) for i in CLEAN]) for d in D]
    q1e = [st.mean([int(q(d, i, "q1")) for i in ERR]) for d in D]
    m["q1"] = (st.mean(q1c), st.mean(q1e))
    m["q1_p"] = stats.wilcoxon(q1c, q1e, zero_method="wilcox")[1]
    m["q1_r"] = rbc(q1c, q1e)

    dp, criterion = [], []
    for d in D:
        h = min(max(sum(q(d, i, "q2") == "No" for i in ERR) / 4, 1 / 8), 1 - 1 / 8)
        f = min(max(sum(q(d, i, "q2") == "No" for i in CLEAN) / 4, 1 / 8), 1 - 1 / 8)
        zh, zf = stats.norm.ppf(h), stats.norm.ppf(f)
        dp.append(zh - zf)
        criterion.append(-0.5 * (zh + zf))
    m["dprime"] = st.mean(dp)
    m["criterion"] = st.mean(criterion)
    m["dprime_p"] = stats.ttest_1samp(dp, 0)[1]

    m["reasons_err"] = dict(Counter(q(d, i, "q3") for d in D for i in ERR if q(d, i, "q2") == "No"))
    m["reasons_clean"] = dict(Counter(q(d, i, "q3") for d in D for i in CLEAN if q(d, i, "q2") == "No"))
    m["dwells"] = [x for d in D for it in d["items"].values()
                   for r in it.get("hovers", {}).values() for x in r.get("dwellsMs", [])]
    return m


R = {k: metrics(v) for k, v in SETS.items()}
ORDER = ["unfiltered", "primary", "strict"]


def pc(m, num, den):
    lo, hi = wilson(m[num], m[den])
    return f"{100*m[num]/m[den]:.1f}% [{lo:.0f}, {hi:.0f}]"


def report():
    for k in ORDER:
        m = R[k]
        print(f"\n{'='*70}\n{k.upper()}  N={m['n']}  decisions={m['decisions']}\n{'='*70}")
        print(f"  detected            {pc(m,'detected','decisions')}")
        print(f"  approved wrong      {pc(m,'approved','decisions')}")
        print(f"  confidently wrong   {pc(m,'conf_wrong','decisions')}")
        print(f"  false alarm         {100*m['fa']/(4*m['n']):.1f}%")
        print(f"  approved all 8      {m['all_yes']}/{m['n']} = {100*m['all_yes']/m['n']:.1f}%")
        print(f"  caught zero         {m['zero']}/{m['n']} = {100*m['zero']/m['n']:.1f}%")
        print(f"  caught all four     {m['perfect']}/{m['n']} = {100*m['perfect']/m['n']:.1f}%")
        print(f"  looked&missed       {m['looked_missed']}/{m['approved']} = {100*m['looked_missed']/m['approved']:.1f}% of approvals")
        a, b, c, e = m["ev"]
        print(f"  evidence  opened {a}/{a+b} = {m['ev_open_rate']:.0f}% | not opened {c}/{c+e} = {m['ev_shut_rate']:.0f}% | OR={m['ev_or']:.1f} p={m['ev_p']:.2e}")
        print(f"  subtype1 {100*m['sub1']/(2*m['n']):.0f}% vs subtype2 {100*m['sub2']/(2*m['n']):.0f}%  p={m['sub_p']:.4f}")
        print(f"  per item: " + " | ".join(f"{i} {NAMES[i][:6]} det{v[0]:.0f}% app{v[1]:.0f}% open{v[2]:.0f}%" for i, v in m["per_item"].items()))
        print(f"  dose: " + " | ".join(f"{k2}s n={v[0]} {100*v[1]/4:.0f}%" for k2, v in m["dose"].items()))
        print(f"  conf right {m['conf_right']:.2f} wrong {m['conf_wrongm']:.2f} (n={m['conf_pairs']}) p={m['conf_p']:.4f}")
        print(f"  calib: " + " | ".join(f"{l}:{v[0]}/{v[1]}" for l, v in m["calib"].items()))
        print(f"  corr: " + " | ".join(f"{lab} rho={v.statistic:+.3f} p={v.pvalue:.4f}" for lab, v in m["corr"].items()))
        print(f"  lang {m['lang']}  p={m['lang_p']:.4f} d={m['lang_d']:+.2f} time={m['lang_time']}")
        print(f"       raw r={m['lang_raw'].statistic:+.3f} p={m['lang_raw'].pvalue:.4f} | partial r={m['lang_part'].statistic:+.3f} p={m['lang_part'].pvalue:.4f}")
        print(f"  role phys {m['role_means'][0]:.2f} vs other {m['role_means'][1]:.2f} p={m['role_p']:.4f} d={m['role_d']:+.2f}")
        print(f"  gender {m['gender']}")
        print(f"  age {m['age']}")
        print(f"  R2 {m['R2']}")
        print(f"  O1 {m['O1']}")
        print(f"  O {[(k2, round(v,2)) for k2,v in m['O'].items()]}  Q5={m['Q5']:.2f} Q6={m['Q6']:.2f}")
        print(f"  q1 clean {m['q1'][0]:.2f} err {m['q1'][1]:.2f} p={m['q1_p']:.4f} r={m['q1_r']:+.2f}")
        print(f"  d'={m['dprime']:.2f} criterion={m['criterion']:+.2f} p={m['dprime_p']:.4f}")
        print(f"  reasons err {m['reasons_err']}")
        print(f"  reasons clean {m['reasons_clean']}")


def figures():
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    os.makedirs(FIGS, exist_ok=True)
    C = {"unfiltered": "#b0b7c3", "primary": "#2b6cb0", "strict": "#7cc4a4"}
    plt.rcParams.update({"figure.dpi": 150, "font.size": 9, "axes.spines.top": False, "axes.spines.right": False})

    def save(fig, name):
        fig.tight_layout()
        fig.savefig(os.path.join(FIGS, name), bbox_inches="tight")
        plt.close(fig)
        print("  wrote", name)

    keys = [("detected", "decisions", "Detected"), ("approved", "decisions", "Approved\nwrong"),
            ("conf_wrong", "decisions", "Confidently\nwrong"), ("all_yes", "n", "Approved\nall 8"),
            ("zero", "n", "Caught\nzero")]
    fig, ax = plt.subplots(figsize=(7.5, 3.6))
    w, xs = 0.26, np.arange(len(keys))
    for j, s in enumerate(ORDER):
        vals = [100 * R[s][a] / R[s][b] for a, b, _ in keys]
        bars = ax.bar(xs + (j - 1) * w, vals, w, label=f"{s} (N={R[s]['n']})", color=C[s])
        ax.bar_label(bars, fmt="%.0f", fontsize=7, padding=1)
    ax.set_xticks(xs); ax.set_xticklabels([l for _, _, l in keys])
    ax.set_ylabel("% "); ax.set_ylim(0, 70); ax.legend(frameon=False, fontsize=8)
    ax.set_title("Headline measures across the three datasets")
    save(fig, "F1_headline.png")

    fig, ax = plt.subplots(figsize=(6, 3.4))
    for j, s in enumerate(ORDER):
        m = R[s]
        bars = ax.bar([j - 0.17, j + 0.17], [m["ev_open_rate"], m["ev_shut_rate"]],
                      0.32, color=["#2b6cb0", "#d98880"])
        ax.bar_label(bars, fmt="%.0f%%", fontsize=8)
    ax.set_xticks(range(3)); ax.set_xticklabels([f"{s}\nN={R[s]['n']}" for s in ORDER])
    ax.set_ylabel("% of error decisions detected"); ax.set_ylim(0, 75)
    ax.legend(handles=[plt.Rectangle((0, 0), 1, 1, color="#2b6cb0"),
                       plt.Rectangle((0, 0), 1, 1, color="#d98880")],
              labels=["opened the error-relevant popover", "did not open it"], frameon=False, fontsize=8)
    ax.set_title("Detection depends on whether the evidence was opened")
    save(fig, "F2_evidence.png")

    fig, ax = plt.subplots(figsize=(6, 3.4))
    order = ["<20", "20-40", "40-80", ">=80"]
    for s in ORDER:
        xs2 = [i for i, k in enumerate(order) if k in R[s]["dose"]]
        ys = [100 * R[s]["dose"][order[i]][1] / 4 for i in xs2]
        ax.plot(xs2, ys, "o-", color=C[s], label=f"{s} (N={R[s]['n']})")
    ax.set_xticks(range(4)); ax.set_xticklabels(["<20 s", "20-40 s", "40-80 s", ">=80 s"])
    ax.set_xlabel("median time per item"); ax.set_ylabel("% of errors caught")
    ax.legend(frameon=False, fontsize=8); ax.set_ylim(-5, 85)
    ax.set_title("More time on task, more errors caught")
    save(fig, "F3_dose.png")

    fig, ax = plt.subplots(figsize=(7.5, 3.4))
    xs = np.arange(4)
    for j, s in enumerate(ORDER):
        vals = [R[s]["per_item"][i][0] for i in ERR]
        bars = ax.bar(xs + (j - 1) * 0.26, vals, 0.26, color=C[s], label=f"{s} (N={R[s]['n']})")
        ax.bar_label(bars, fmt="%.0f", fontsize=7)
    ax.set_xticks(xs)
    ax.set_xticklabels([f"item {i}\n{NAMES[i]}\n{'subtype 1' if i in SUB1 else 'subtype 2'}" for i in ERR])
    ax.set_ylabel("% detected"); ax.legend(frameon=False, fontsize=8); ax.set_ylim(0, 60)
    ax.set_title("Detection by planted error")
    save(fig, "F4_items.png")

    fig, ax = plt.subplots(figsize=(6.5, 3.4))
    labs = ["time", "hover", "B7 comms", "B3 years", "B6 AI", "B5 reading", "B10 age"]
    y = np.arange(len(labs))
    for j, s in enumerate(ORDER):
        vals = [R[s]["corr"][l].statistic for l in labs]
        ax.barh(y + (j - 1) * 0.26, vals, 0.26, color=C[s], label=f"{s} (N={R[s]['n']})")
    ax.axvline(0, color="k", lw=.8)
    ax.set_yticks(y); ax.set_yticklabels(["time per item", "hover seconds", "patient comms B7",
                                          "years B3", "AI familiarity B6", "reading comfort B5", "age B10"])
    ax.set_xlabel("Spearman rho with errors caught"); ax.legend(frameon=False, fontsize=8)
    ax.invert_yaxis(); ax.set_title("Only behaviour predicts detection, not background")
    save(fig, "F5_predictors.png")

    fig, ax = plt.subplots(figsize=(6, 3.4))
    for s in ORDER:
        xs2, ys = [], []
        for l, (ok, tot) in R[s]["calib"].items():
            if tot >= 5:
                xs2.append(l); ys.append(100 * ok / tot)
        ax.plot(xs2, ys, "o-", color=C[s], label=f"{s} (N={R[s]['n']})")
    ax.set_xlabel("stated confidence (Q4)"); ax.set_ylabel("% of those decisions that were correct")
    ax.set_xticks([1, 2, 3, 4, 5]); ax.set_ylim(0, 100)
    ax.legend(frameon=False, fontsize=8); ax.set_title("Confidence barely tracks correctness")
    save(fig, "F6_calibration.png")

    fig, ax = plt.subplots(figsize=(6, 3.4))
    xs = np.arange(3)
    for j, s in enumerate(ORDER):
        bars = ax.bar(xs + (j - 1) * 0.26, list(R[s]["expl"]), 0.26, color=C[s], label=f"{s} (N={R[s]['n']})")
        ax.bar_label(bars, fmt="%.2f", fontsize=7)
    ax.set_xticks(xs); ax.set_xticklabels(["Short", "Medium", "Detailed"])
    ax.set_ylabel("mean usefulness (1-5)"); ax.set_ylim(3, 4.4)
    ax.legend(frameon=False, fontsize=8); ax.set_title("Short explanations rated most useful")
    save(fig, "F7_explanation.png")

    fig, ax = plt.subplots(figsize=(6.5, 3.4))
    xs = np.arange(2)
    for j, s in enumerate(ORDER):
        vals = [100 * R[s]["lang"][g][1] / 4 for g in ["en+de", "sq"]]
        bars = ax.bar(xs + (j - 1) * 0.26, vals, 0.26, color=C[s],
                      label=f"{s} (n={R[s]['lang']['en+de'][0]}/{R[s]['lang']['sq'][0]})")
        ax.bar_label(bars, fmt="%.0f", fontsize=7)
    ax.set_xticks(xs); ax.set_xticklabels(["English + German", "Albanian"])
    ax.set_ylabel("% of errors caught"); ax.legend(frameon=False, fontsize=8); ax.set_ylim(0, 70)
    ax.set_title("Language groups (differences are not significant)")
    save(fig, "F8_language.png")

    fig, ax = plt.subplots(figsize=(6.5, 3.4))
    d = [x for x in R["unfiltered"]["dwells"] if x <= 6000]
    ax.hist(d, bins=60, color="#2b6cb0")
    ax.axvline(DWELL_MIN_MS, color="crimson", ls="--", lw=1.4)
    ax.text(DWELL_MIN_MS + 90, ax.get_ylim()[1] * .8, f"{DWELL_MIN_MS} ms threshold", color="crimson", fontsize=8)
    ax.set_xlabel("single hover duration (ms, capped at 6000)"); ax.set_ylabel("count")
    ax.set_title("Hover durations: accidental pass-throughs versus real reading")
    save(fig, "F9_dwell.png")

    fig, ax = plt.subplots(figsize=(7, 3.0))
    for j, s in enumerate(ORDER):
        m = R[s]
        det = 100 * m["detected"] / m["decisions"]
        lm = 100 * m["looked_missed"] / m["decisions"]
        rest = 100 - det - lm
        ax.barh(j, det, color="#2f855a")
        ax.barh(j, lm, left=det, color="#dd6b20")
        ax.barh(j, rest, left=det + lm, color="#c53030")
        ax.text(det / 2, j, f"{det:.0f}%", ha="center", va="center", color="w", fontsize=8)
        ax.text(det + lm / 2, j, f"{lm:.0f}%", ha="center", va="center", color="w", fontsize=8)
        ax.text(det + lm + rest / 2, j, f"{rest:.0f}%", ha="center", va="center", color="w", fontsize=8)
    ax.set_yticks(range(3)); ax.set_yticklabels([f"{s}\nN={R[s]['n']}" for s in ORDER])
    ax.set_xlabel("% of all error decisions"); ax.set_xlim(0, 100)
    ax.legend(handles=[plt.Rectangle((0, 0), 1, 1, color=c) for c in ["#2f855a", "#dd6b20", "#c53030"]],
              labels=["detected", "approved after opening the evidence", "approved without opening it"],
              frameon=False, fontsize=8, loc="upper left", bbox_to_anchor=(1.01, 1.0))
    ax.set_title("What happened on the 4 error items")
    save(fig, "F10_outcomes.png")


if __name__ == "__main__":
    report()
    if "--figures" in sys.argv:
        print("\nfigures:")
        figures()
