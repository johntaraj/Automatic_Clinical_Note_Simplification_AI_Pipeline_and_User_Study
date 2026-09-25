"""Descriptive results, subgroup summaries and hypothesis tests.

Usage:
    python analysis/analyse.py              # primary sample (N = 34)
    python analysis/analyse.py --strict     # clean responses only (N = 27)
    python analysis/analyse.py --all        # all responses (N = 42)
    python analysis/analyse.py --compare    # headline numbers for all three samples
"""

import json, glob, os, math, sys, statistics as st
from collections import Counter, defaultdict

import numpy as np
from scipy import stats

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DATA = os.path.join(ROOT, "data")

ERR = [2, 4, 6, 8]
CLEAN = [1, 3, 5, 7]
SUB1 = [2, 6]
SUB2 = [4, 8]
CLIN = {"Clinically incorrect", "Misleading", "Important information is missing"}
NAMES = {2: "anticoagulation", 4: "dysphagia", 6: "analgesia", 8: "hyperkalemia"}
SWAPS = {1: 3, 2: 2, 3: 2, 4: 2, 5: 2, 6: 2, 7: 2, 8: 3}
DWELL_MIN_MS = 500


def load(include_borderline=True, include_excluded=False):
    paths = sorted(glob.glob(os.path.join(DATA, "*.txt")))
    if include_borderline:
        paths += sorted(glob.glob(os.path.join(DATA, "borderline", "*.txt")))
    if include_excluded:
        paths += sorted(glob.glob(os.path.join(DATA, "excluded", "*.txt")))
    out = []
    for p in paths:
        d = json.load(open(p, encoding="utf-8"))
        d["_f"] = os.path.basename(p)[:-4]
        d["_link"] = "link " + str(d["meta"].get("copyId") or "?")
        out.append(d)
    return out


def q(d, i, k):
    return d["items"][str(i)]["q"][k]

def detected(d, i):
    return q(d, i, "q2") == "No" and q(d, i, "q3") in CLIN

def n_swaps(d, i):
    return 2 if (d["meta"]["language"] == "sq" and i == 8) else SWAPS[i]

def total_swaps(d):
    return sum(n_swaps(d, i) for i in range(1, 9))

def real_dwell_ms(rec):
    return sum(x for x in rec.get("dwellsMs", []) if x >= DWELL_MIN_MS)

def opened(d, i, key):
    return real_dwell_ms(d["items"][str(i)].get("hovers", {}).get(key, {})) > 0

def opened_decisive(d, i):
    return opened(d, i, "0_B") or opened(d, i, "0_C")

def dwell_by_version(d, suffix):
    return sum(real_dwell_ms(r)
               for it in d["items"].values()
               for k, r in it.get("hovers", {}).items() if k.endswith(suffix)) / 1000

def med_item_secs(d):
    return st.median([d["timing"]["perScreenMs"].get(f"item{i}", 0) / 1000 for i in range(1, 9)])

def det_count(d):
    return sum(detected(d, i) for i in ERR)

def lang_group(d):
    return "en+de" if d["meta"]["language"] in ("en", "de") else "sq"


def wilson(k, n):
    if n == 0:
        return (0.0, 0.0)
    z, p = 1.96, k / n
    den = 1 + z * z / n
    c = (p + z * z / (2 * n)) / den
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / den
    return (max(0, c - h), min(1, c + h))

def holm(ps):
    order = sorted(range(len(ps)), key=lambda i: ps[i])
    out, running = [0] * len(ps), 0.0
    for rank, i in enumerate(order):
        v = min(1.0, (len(ps) - rank) * ps[i])
        running = max(running, v)
        out[i] = running
    return out

def rank_biserial(x, y):
    diffs = [a - b for a, b in zip(x, y) if a != b]
    if not diffs:
        return 0.0
    r = stats.rankdata([abs(v) for v in diffs])
    pos = sum(r[i] for i, v in enumerate(diffs) if v > 0)
    neg = sum(r[i] for i, v in enumerate(diffs) if v < 0)
    return (pos - neg) / sum(r)

def cliffs_delta(a, b):
    a, b = list(a), list(b)
    if not a or not b:
        return 0.0
    return sum((x > y) - (x < y) for x in a for y in b) / (len(a) * len(b))

def sig(p):
    return "***" if p < .001 else "**" if p < .01 else "*" if p < .05 else "ns"

def pct(k, n):
    lo, hi = wilson(k, n)
    return f"{100*k/n:5.1f}%  [{100*lo:.0f}, {100*hi:.0f}]"


def headline(D, label):
    n = len(D)
    dec_err = [(d, i) for d in D for i in ERR]
    det = sum(detected(d, i) for d, i in dec_err)
    appr = sum(q(d, i, "q2") == "Yes" for d, i in dec_err)
    fa = sum(q(d, i, "q2") == "No" for d in D for i in CLEAN)
    conf_wrong = sum(1 for d, i in dec_err if q(d, i, "q2") == "Yes" and int(q(d, i, "q4")) >= 4)
    allyes = sum(1 for d in D if all(q(d, i, "q2") == "Yes" for i in range(1, 9)))
    zero = sum(1 for d in D if det_count(d) == 0)
    looked_missed = sum(1 for d, i in dec_err if q(d, i, "q2") == "Yes" and opened_decisive(d, i))
    print(f"\n{'='*74}\n{label}   N={n} participants, {len(dec_err)} error decisions\n{'='*74}")
    print(f"  detected (strict)          {pct(det, len(dec_err))}")
    print(f"  approved a wrong item      {pct(appr, len(dec_err))}")
    print(f"  false alarm on clean items {pct(fa, 4*n)}")
    print(f"  CONFIDENTLY wrong (conf>=4){pct(conf_wrong, len(dec_err))}")
    print(f"  approved all 8 items       {pct(allyes, n)}")
    print(f"  caught zero of 4 errors    {pct(zero, n)}")
    print(f"  approved after opening the wrong swap  {pct(looked_missed, appr)} of approvals")


def per_item(D):
    print("\nPER ERROR ITEM")
    print(f"  {'item':<20}{'subtype':<14}{'detected':>10}{'approved':>10}{'opened wrong swap':>20}")
    for i in ERR:
        sub = "1 detectable" if i in SUB1 else "2 falsified"
        det = sum(detected(d, i) for d in D)
        app = sum(q(d, i, "q2") == "Yes" for d in D)
        op = sum(opened_decisive(d, i) for d in D)
        print(f"  {str(i)+' '+NAMES[i]:<20}{sub:<14}{100*det/len(D):>9.0f}%{100*app/len(D):>9.0f}%{100*op/len(D):>19.0f}%")


def evidence_test(D):
    print("\nDOES LOOKING AT THE EVIDENCE HELP?  (item-level, all error decisions)")
    a = b = c = e = 0
    for d in D:
        for i in ERR:
            if opened_decisive(d, i):
                if detected(d, i): a += 1
                else: b += 1
            else:
                if detected(d, i): c += 1
                else: e += 1
    table = [[a, b], [c, e]]
    odds, p = stats.fisher_exact(table)
    print(f"                        detected   missed")
    print(f"    opened the swap  {a:>10} {b:>8}   -> {100*a/max(a+b,1):.0f}% detected")
    print(f"    did not open it  {c:>10} {e:>8}   -> {100*c/max(c+e,1):.0f}% detected")
    print(f"    Fisher exact odds ratio={odds:.2f}  p={p:.4f} {sig(p)}")


def dose_response(D):
    print("\nDOSE RESPONSE: time spent vs errors caught")
    binned = defaultdict(list)
    for d in D:
        t = med_item_secs(d)
        b = "<20s" if t < 20 else "20-40s" if t < 40 else "40-80s" if t < 80 else ">=80s"
        binned[b].append(det_count(d))
    for b in ["<20s", "20-40s", "40-80s", ">=80s"]:
        if binned[b]:
            v = binned[b]
            print(f"    {b:<8} n={len(v):<3} mean {st.mean(v):.2f}/4  ({100*st.mean(v)/4:.0f}%)")


def subgroup(D, fn, label, min_n=1):
    g = defaultdict(list)
    for d in D:
        g[fn(d)].append(det_count(d))
    print(f"\n  {label}")
    for k, v in sorted(g.items(), key=lambda x: -len(x[1])):
        if len(v) >= min_n:
            flag = "" if len(v) >= 8 else "   (too small to test)"
            print(f"    {str(k):<24} n={len(v):<3} {st.mean(v):.2f}/4  {100*st.mean(v)/4:>3.0f}%{flag}")
    return g


def language_analysis(D):
    print(f"\n{'='*74}\nLANGUAGE: en+de versus sq\n{'='*74}")
    g = defaultdict(list)
    for d in D:
        g[lang_group(d)].append(det_count(d))
    for k in ["en+de", "sq"]:
        print(f"  {k:<8} n={len(g[k]):<3} mean {st.mean(g[k]):.2f}/4  ({100*st.mean(g[k])/4:.0f}%)")
    u, p = stats.mannwhitneyu(g["en+de"], g["sq"])
    print(f"  Mann-Whitney U={u:.1f} p={p:.4f} {sig(p)}  Cliff delta={cliffs_delta(g['en+de'], g['sq']):+.2f}")

    print("\n  Review time by language group")
    t = defaultdict(list)
    for d in D:
        t[lang_group(d)].append(med_item_secs(d))
    for k in ["en+de", "sq"]:
        print(f"    {k:<8} median seconds per item: {st.median(t[k]):.0f}s")
    u2, p2 = stats.mannwhitneyu(t["en+de"], t["sq"])
    print(f"    Mann-Whitney on TIME: U={u2:.1f} p={p2:.4f} {sig(p2)}")

    x = np.array([1 if lang_group(d) == "en+de" else 0 for d in D], float)
    y = np.array([det_count(d) for d in D], float)
    z = np.array([med_item_secs(d) for d in D], float)
    def resid(v, ctrl):
        A = np.vstack([ctrl, np.ones_like(ctrl)]).T
        beta, *_ = np.linalg.lstsq(A, v, rcond=None)
        return v - A @ beta
    r_raw, p_raw = stats.spearmanr(x, y)
    r_par, p_par = stats.pearsonr(resid(x, z), resid(y, z))
    print(f"\n    language vs detection, raw            : r={r_raw:+.3f} p={p_raw:.4f} {sig(p_raw)}")
    print(f"    language vs detection, time controlled: r={r_par:+.3f} p={p_par:.4f} {sig(p_par)}")


def run_tests(D):
    print(f"\n{'='*74}\nHYPOTHESIS TESTS   N={len(D)}\n{'='*74}")

    a = [sum(detected(d, i) for i in SUB1) for d in D]
    b = [sum(detected(d, i) for i in SUB2) for d in D]
    s, p = stats.wilcoxon(a, b, zero_method="wilcox")
    print(f"\n  H2 subtype 1 vs subtype 2 detection")
    print(f"     {100*sum(a)/(2*len(D)):.0f}% vs {100*sum(b)/(2*len(D)):.0f}%   "
          f"W={s:.1f} p={p:.4f} {sig(p)}  r={rank_biserial(a,b):+.2f}")

    a = [st.mean([int(q(d, i, "q1")) for i in CLEAN]) for d in D]
    b = [st.mean([int(q(d, i, "q1")) for i in ERR]) for d in D]
    s, p = stats.wilcoxon(a, b, zero_method="wilcox")
    print(f"\n  Q1 meaning score clean vs error")
    print(f"     {st.mean(a):.2f} vs {st.mean(b):.2f}   W={s:.1f} p={p:.4f} {sig(p)}  r={rank_biserial(a,b):+.2f}")

    pa, pb = [], []
    for d in D:
        cr = [int(q(d, i, "q4")) for i in ERR if detected(d, i)]
        wr = [int(q(d, i, "q4")) for i in ERR if not detected(d, i)]
        if cr and wr:
            pa.append(st.mean(cr)); pb.append(st.mean(wr))
    if len(pa) >= 6:
        s, p = stats.wilcoxon(pa, pb, zero_method="wilcox")
        print(f"\n  H4 confidence when right vs wrong  (n={len(pa)} usable)")
        print(f"     {st.mean(pa):.2f} vs {st.mean(pb):.2f}  gap {st.mean(pa)-st.mean(pb):+.2f}   "
              f"W={s:.1f} p={p:.4f} {sig(p)}")

    S = [int(d["rationale"]["S"]) for d in D]
    M = [int(d["rationale"]["M"]) for d in D]
    L = [int(d["rationale"]["L"]) for d in D]
    chi, p = stats.friedmanchisquare(S, M, L)
    print(f"\n  H6 explanation length S/M/L")
    print(f"     means {st.mean(S):.2f} / {st.mean(M):.2f} / {st.mean(L):.2f}   "
          f"Friedman chi2={chi:.2f} p={p:.4f} {sig(p)}  W={chi/(len(D)*2):.3f}")
    ps = [stats.wilcoxon(x, y, zero_method="wilcox")[1] for x, y in [(S, M), (S, L), (M, L)]]
    for lab, raw, adj in zip(["S vs M", "S vs L", "M vs L"], ps, holm(ps)):
        print(f"       {lab}: p={raw:.4f} Holm={adj:.4f} {sig(adj)}")
    print(f"     R2 preferred default: {dict(Counter(d['rationale']['R2'] for d in D))}")

    print(f"\n  Spearman correlations with number of errors caught")
    det = [det_count(d) for d in D]
    feats = [
        ("years in healthcare", [["<1","1-3","4-7","8-15",">15"].index(d["background"]["B3"]) for d in D]),
        ("AI familiarity B6", [int(d["background"]["B6"]) for d in D]),
        ("patient comms B7", [int(d["background"]["B7"]) for d in D]),
        ("reading comfort B5", [int(d["background"]["B5"]) for d in D]),
        ("age band B10", [["18-24","25-34","35-44","45-54","55-64","65+"].index(d["background"]["B10"])
                          if d["background"].get("B10") else np.nan for d in D]),
        ("median secs per item", [med_item_secs(d) for d in D]),
        ("real hover seconds", [dwell_by_version(d, "_B") + dwell_by_version(d, "_C") for d in D]),
    ]
    for lab, vals in feats:
        pairs = [(v, dd) for v, dd in zip(vals, det) if not (isinstance(v, float) and math.isnan(v))]
        r, p = stats.spearmanr([x for x, _ in pairs], [y for _, y in pairs])
        print(f"     {lab:<24} rho={r:+.3f} p={p:.4f} {sig(p)}  (n={len(pairs)})")

    dp, cr = [], []
    for d in D:
        h = min(max(sum(q(d, i, "q2") == "No" for i in ERR) / 4, 1/8), 1 - 1/8)
        f = min(max(sum(q(d, i, "q2") == "No" for i in CLEAN) / 4, 1/8), 1 - 1/8)
        zh, zf = stats.norm.ppf(h), stats.norm.ppf(f)
        dp.append(zh - zf); cr.append(-0.5 * (zh + zf))
    t, p = stats.ttest_1samp(dp, 0)
    print(f"\n  Signal detection: d'={st.mean(dp):.2f} (sd {st.stdev(dp):.2f})  "
          f"vs zero t={t:.2f} p={p:.4f} {sig(p)};  criterion c={st.mean(cr):+.2f}")


def descriptives(D):
    print(f"\n{'='*74}\nSAMPLE\n{'='*74}")
    print(f"  language   {dict(Counter(d['meta']['language'] for d in D))}")
    print(f"  link       {dict(Counter(d['_link'] for d in D))}")
    for k, lab in [("B1","role"),("B3","years"),("B9","gender"),("B10","age")]:
        print(f"  {lab:<10} {dict(Counter(d['background'].get(k) for d in D))}")
    print(f"\n  perceived value (1-5)")
    for k, lab in [("O2","worth the effort"),("O3","sources help"),("O4","explanations add value"),("O5","would use it")]:
        v = [int(d["overall"][k]) for d in D]
        print(f"    {k} {lab:<24} mean {st.mean(v):.2f}  median {st.median(v):.0f}")
    print(f"  O1 preferred version: {dict(Counter(d['overall']['O1'] for d in D))}")
    print(f"\n  rejection reasons on ERROR items:  {dict(Counter(q(d,i,'q3') for d in D for i in ERR if q(d,i,'q2')=='No'))}")
    print(f"  rejection reasons on CLEAN items:  {dict(Counter(q(d,i,'q3') for d in D for i in CLEAN if q(d,i,'q2')=='No'))}")


def main():
    args = sys.argv[1:]
    if "--compare" in args:
        for lab, kw in [("ALL (unfiltered)", dict(include_borderline=True, include_excluded=True)),
                        ("PRIMARY: clean + borderline", dict(include_borderline=True)),
                        ("STRICT: clean only", dict(include_borderline=False))]:
            headline(load(**kw), lab)
        return

    if "--all" in args:
        D, label = load(True, True), "ALL RESPONSES (unfiltered)"
    elif "--strict" in args:
        D, label = load(False, False), "STRICT (clean only)"
    else:
        D, label = load(True, False), "PRIMARY (clean + borderline)"

    headline(D, label)
    per_item(D)
    evidence_test(D)
    dose_response(D)
    print(f"\n{'='*74}\nSUBGROUPS\n{'='*74}")
    subgroup(D, lambda d: d["background"]["B1"], "by role")
    subgroup(D, lambda d: d["background"].get("B9"), "by gender")
    subgroup(D, lambda d: d["background"].get("B10"), "by age band")
    subgroup(D, lambda d: d["meta"]["language"], "by language")
    subgroup(D, lambda d: d["_link"], "by distribution link")
    language_analysis(D)
    run_tests(D)
    descriptives(D)


if __name__ == "__main__":
    main()
