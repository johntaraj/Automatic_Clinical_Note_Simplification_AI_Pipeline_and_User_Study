"""Metric registry: meaning, preferred direction, target, stage and reporting tier."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass(frozen=True)
class MetricSpec:
    key: str
    label: str
    stage: str
    tier: str
    direction: int
    fmt: str = "{:.3f}"
    target: str = ""
    what: str = ""
    caveat: str = ""
    reference_row: bool = False


def _m(**kw) -> MetricSpec:
    return MetricSpec(**kw)


REGISTRY: List[MetricSpec] = [
    _m(key="n_hard_terms", label="hard terms found", stage="2 extraction",
       tier="appendix", direction=0, fmt="{:.1f}",
       what="terms the extractor flagged per note",
       target="6-10 for a dense clinical sentence"),
    _m(key="extraction_precision", label="extraction precision", stage="2 extraction",
       tier="appendix", direction=+1, target="> 0.80",
       what="of the terms we flagged, how many a human would flag",
       caveat="needs hand-labelled gold; LLM-generated gold is circular"),
    _m(key="extraction_recall", label="extraction recall", stage="2 extraction",
       tier="appendix", direction=+1, target="> 0.85",
       what="of the terms a human would flag, how many we found",
       caveat="needs hand-labelled gold"),
    _m(key="extraction_f1", label="extraction F1", stage="2 extraction",
       tier="appendix", direction=+1, target="> 0.80",
       what="harmonic mean of the two above",
       caveat="needs hand-labelled gold"),
    _m(key="extraction_stability", label="extraction stability", stage="2 extraction",
       tier="paper", direction=+1, target="> 0.90",
       what="mean Jaccard overlap between the hard-term sets returned by two "
            "independent extractions of the SAME note at the shipped "
            "temperature - a reliability measurement that needs no gold labels",
       caveat="the only stage-2 number that does not require hand annotation. "
              "It matters because everything downstream is conditioned on the "
              "term list: if this is below ~0.9, two runs of the identical "
              "config are not comparable and an A/B measures extraction noise "
              "rather than the change under test"),

    _m(key="whole_term_coverage", label="whole-term coverage", stage="3 retrieval",
       tier="appendix", direction=+1, target="> 0.80 overall; the RARE strata matter",
       what="fraction of the EXTRACTOR's own hard terms that received >=1 "
            "WHOLE-TERM glossary definition",
       caveat="a strict lower bound, and demoted to the appendix because of it. "
              "A compound with no whole-phrase entry may still be handled by "
              "splitting, and those pieces DO reach the prompt: on the 93-note "
              "run 71 of 86 apparent misses were phrases like `chronic UTIs`, "
              "whose parts were both defined and both shown. Quote "
              "`evidence_coverage` as the headline. Counts extracted "
              "terms only; salvaged fragments are definable by construction and "
              "are reported separately as `coverage_incl_salvage`"),
    _m(key="evidence_coverage", label="terms with evidence shown",
       stage="3 retrieval", tier="paper", direction=+1,
       target="> 0.90 overall; the very_rare stratum is the binding one",
       what="fraction of extracted hard terms for which the model received a "
            "usable definition BY ANY ROUTE - a whole-term entry, or entries "
            "for the pieces of a split compound",
       caveat="answers the question retrieval actually exists to answer: did "
              "the generator have evidence for this term. Still says nothing "
              "about whether the evidence was USED (that is attribution's job) "
              "or whether it was any good - `C-diff: Clostridioides difficile` "
              "counted as covered and caused the run's worst hallucination"),
    _m(key="n_expansion_definitions", label="expansion definitions",
       stage="3 retrieval", tier="appendix", direction=0, fmt="{:.0f}",
       what="lay definitions retrieved by re-querying the glossaries with an "
            "abbreviation's expansion instead of the abbreviation",
       caveat="fires rarely by design (3 terms / 93 notes) - it triggers only "
              "when a definition NAMES the term instead of explaining it and "
              "the expansion contains a rare token to query with. Append-only, "
              "so it can add evidence but never removes the expansion itself"),
    _m(key="mean_defs_per_term", label="definitions per term", stage="3 retrieval",
       tier="appendix", direction=0, fmt="{:.2f}", target="2-3",
       what="average glossary entries retrieved per covered term"),
    _m(key="definition_redundancy", label="definition redundancy",
       stage="3 retrieval", tier="appendix", direction=0, fmt="{:.3f}",
       target="report alongside per-source attribution",
       what="mean pairwise word overlap between the definitions shown for the "
            "SAME term",
       caveat="this is the interpretation key for per-source attribution, not "
              "a quality score - there is no good value. ContextCite is weakly "
              "identified when several sources say the same thing (App. C.4), "
              "so a HIGHER number mechanically lowers top1_drop, "
              "relevant_source_rate and oracle_agreement. Improving a "
              "corpus RAISES it: it doubled 0.058 -> 0.126 between FINAL93 and "
              "CLEAN93 while coverage, orphans and reading level all got "
              "better. Quote it next to top1_drop_median_helped or those "
              "numbers look like a regression (METHODOLOGY 12.14)."),
    _m(key="definition_fkgl", label="definition reading grade", stage="3 retrieval",
       tier="appendix", direction=-1, fmt="{:.2f}", target="6-8 (US grade)",
       what="FKGL of the glossary entries that actually reached a prompt",
       caveat="the missing half of the lexical-borrowing finding. Grounded "
              "outputs demonstrably reuse the definition's vocabulary, so how "
              "the definitions are WRITTEN decides whether that helps. A high "
              "grade here predicts that borrowing hurts, and it is what "
              "separates 'making more pee' from 'Clostridioides difficile'"),
       _m(key="orphan_term_rate", label="stored-record orphan rate",
        stage="3 retrieval", tier="appendix", direction=-1,
        what="fraction of stored hard-item records with no matching entry in "
           "the prompt, counting both a split parent and its appended pieces",
        caveat="retained for transparency because it is the orphan rate stored "
             "by the reportable run. Its overlapping denominator can hide a "
             "missing fragment when another piece supplies evidence for the "
             "parent; use `split_adjusted_orphan_rate` for interpretation"),
       _m(key="split_adjusted_orphan_rate", label="split-adjusted orphan rate",
        stage="3 retrieval", tier="paper", direction=-1, target="< 0.10",
        what="fraction of non-overlapping retrieval units with no matching "
           "entry in the prompt; each split parent is replaced by its chosen "
           "pieces and any unresolved remainder",
        caveat="unlike `evidence_coverage`, this counts the units after phrase "
             "splitting. A partial split keeps its uncovered remainder in "
             "the denominator, so missing evidence cannot disappear"),
    _m(key="on_term_sources", label="entries about the edited term",
       stage="3 retrieval", tier="appendix", direction=+1, fmt="{:.2f}",
       target=">= 1.0",
       what="how many of the shown entries are about the term being edited"),
    _m(key="on_term_source_share", label="share of sources on-term", stage="3 retrieval",
       tier="appendix", direction=+1, fmt="{:.3f}", target="descriptive",
       what="related entries / all shown entries, averaged over terms - the "
            "share of the LASSO's candidates that could plausibly explain a "
            "given edit",
       caveat="low values are inherent to masking the whole glossary; report "
              "it as a limitation, do not tune against it"),
    _m(key="attrib_p_at_1", label="retrieval P@1", stage="3 retrieval",
       tier="appendix", direction=+1, target="> 0.60",
       what="gold best source ranked first",
       caveat="needs hand-labelled best-source gold"),
    _m(key="attrib_mrr", label="retrieval MRR", stage="3 retrieval",
       tier="appendix", direction=+1, target="> 0.70",
       what="mean reciprocal rank of the gold best source",
       caveat="needs hand-labelled best-source gold"),

    _m(key="fkgl", label="FKGL (absolute)", stage="4 readability",
       tier="appendix", direction=-1, fmt="{:.2f}", target="6-8 (US grade)",
       what="Flesch-Kincaid grade level of the output",
       reference_row=True,
       caveat="absolute grade is dominated by sentence length; the DROP is the "
              "honest number"),
    _m(key="fkgl_drop", label="FKGL drop vs input", stage="4 readability",
       tier="paper", direction=+1, fmt="{:.2f}", target="> +4 grades",
       what="how many US grade levels easier than the original clinical text",
       caveat="gameable by chopping sentences - read with length ratio"),
    _m(key="coleman_liau", label="Coleman-Liau (absolute)", stage="4 readability",
       tier="appendix", direction=-1, fmt="{:.2f}", target="6-8",
       what="character-based grade level", reference_row=True),
    _m(key="coleman_liau_drop", label="Coleman-Liau drop", stage="4 readability",
       tier="paper", direction=+1, fmt="{:.2f}", target="> +4",
       what="same as FKGL drop but CHARACTER-based, so it is immune to "
            "syllable-counter error on medical morphology",
       caveat="none - this is the robustness check on FKGL"),
    _m(key="fre", label="Flesch Reading Ease", stage="4 readability",
       tier="appendix", direction=+1, fmt="{:.1f}", target="60-80 (plain English)",
       what="0-100 ease score", reference_row=True,
       caveat="uses the SAME two inputs as FKGL; not independent evidence"),
    _m(key="fre_gain", label="FRE gain", stage="4 readability",
       tier="appendix", direction=+1, fmt="{:.1f}", target="> +20",
       what="ease improvement vs the original",
       caveat="redundant with fkgl_drop"),
    _m(key="smog", label="SMOG", stage="4 readability",
       tier="appendix", direction=-1, fmt="{:.2f}", target="6-8",
       what="health-literacy grade standard", reference_row=True,
       caveat="calibrated for 30+ sentence passages; very jumpy on one sentence"),
    _m(key="smog_drop", label="SMOG drop", stage="4 readability",
       tier="appendix", direction=+1, fmt="{:.2f}", target="> +3",
       what="SMOG improvement vs the original",
       caveat="same single-sentence calibration problem"),
    _m(key="n_words", label="words out", stage="4 readability",
       tier="appendix", direction=0, fmt="{:.1f}", target="close to the reference",
       what="output length", reference_row=True),
    _m(key="length_ratio", label="length ratio vs reference", stage="4 readability",
       tier="paper", direction=0, fmt="{:.2f}", target="0.9-1.3",
       what="output words / reference words - catches padding and truncation",
       caveat="descriptive, not a quality score; >1.4 means the model is "
              "glossing everything"),

    _m(key="sari", label="SARI", stage="4 quality",
       tier="appendix", direction=+1, fmt="{:.2f}", target="40-60 typical",
       what="KEEP/ADD/DELETE n-gram agreement with the human reference",
       caveat="the references are MINIMAL-EDIT, so SARI rewards not editing. "
              "Measured: a perfect rewrite scored 25.97 vs 22.64 for doing "
              "nothing. Report, do not lead with it"),
    _m(key="bertscore_f1", label="BERTScore F1", stage="4 quality",
       tier="appendix", direction=+1, fmt="{:.3f}", target="0.4-0.7 rescaled",
       what="contextual-embedding similarity to the reference, rescaled "
            "against the empirical baseline",
       caveat="read the RESCALED value. Until bug 42 the baseline lookup was "
              "silently failing for a local model directory, so raw scores "
              "were reported and everything landed in 0.90-0.96 - which is why "
              "this metric was demoted for having no dynamic range. Rescaled, "
              "the same 5 notes span 0.556-0.620, a gap six times wider. The "
              "demotion should be re-examined on the full run"),

    _m(key="nli_faithfulness", label="NLI faithfulness", stage="4 faithfulness",
       tier="paper", direction=+1, target="> 0.70",
       what="input entails output - catches HALLUCINATION (added content)",
       caveat="general-domain MNLI head; absolute values are compressed"),
    _m(key="nli_completeness", label="NLI completeness", stage="4 faithfulness",
       tier="paper", direction=+1, target="> 0.60",
       what="output entails input - catches OMISSION (dropped content)",
       caveat="omission is the dominant clinical failure mode, which is why "
              "this direction is reported separately"),
    _m(key="critical_error", label="critical-error rate", stage="4 safety",
       tier="paper", direction=-1, target="0.00 - any value > 0 needs review",
       what="fraction of outputs that lost a high-risk slot: negation, "
            "uncertainty, laterality, a number/unit, or a drug name"),
    _m(key="drug_preservation", label="drug-name preservation", stage="4 safety",
       tier="appendix", direction=+1, target="1.00 - nothing less is acceptable",
       what="named drugs surviving verbatim (WHO INN stems + curated list)",
       caveat="APPENDIX because of the DENOMINATOR, not the metric: only 2 of "
              "the 93 laymaker notes contain a detected drug name, so the mean "
              "is two observations wearing a percentage. Report the cases, not "
              "the rate. Also read it against tag_policy - under `replace` the "
              "pipeline is INSTRUCTED to drop drug names"),
    _m(key="diagnostic_identity_preservation", label="diagnostic-identity preservation",
       stage="4 safety", tier="appendix", direction=+1,
       target="1.00 - nothing less is acceptable",
       what="high-risk named diagnoses kept verbatim or rendered as a sanctioned "
            "lay equivalent - catches 'hepatic encephalopathy' -> 'brain fog'",
       caveat="scored only over a closed curated table of conditions, and only "
              "4 of 93 notes contain one, so the mean is four observations. "
              "An unlisted diagnosis is not scored rather than guessed at, so "
              "this under-reports rather than over-reports. Report the cases"),
    _m(key="severity_downgrade", label="severity downgrade rate", stage="4 safety",
       tier="appendix", direction=-1, target="0.00",
       what="fraction of outputs that state a weaker severity tier than the "
            "input - 'severe' rendered as 'mild' or dropped entirely",
       caveat="3-tier ordinal lexicon; lay renderings ('very bad') sit at the "
              "same tier as their clinical equivalent so correct paraphrase is "
              "not penalised. Appendix on denominator: 10 of 93 notes state a "
              "severity at all"),
    _m(key="number_unit_preservation", label="number/unit preservation",
       stage="4 safety", tier="appendix", direction=+1, target="1.00",
       what="all doses and units survive (spelled-out numbers and expanded "
            "unit abbreviations count)"),
    _m(key="negation_preservation", label="negation preservation",
       stage="4 safety", tier="appendix", direction=+1, target="1.00",
       what="a negation cue is still present when the input had one",
       caveat="type-level, so it cannot see WHICH negation was lost"),
    _m(key="laterality_preservation", label="laterality preservation",
       stage="4 safety", tier="appendix", direction=+1, target="1.00",
       what="left/right/bilateral/basal survive (instance-level)"),
    _m(key="uncertainty_preservation", label="uncertainty preservation",
       stage="4 safety", tier="appendix", direction=+1, target="1.00",
       what="hedging survives - 'cannot be excluded' must not become 'is present'"),

    _m(key="generation_success_rate", label="generation success rate",
       stage="4 edits", tier="paper", direction=+1, target="1.00",
       what="fraction of notes where this arm produced any output at all",
       caveat="a blank output contributes NO metrics, so it silently leaves "
              "the averages rather than scoring zero - a model that fails on "
              "hard notes would otherwise look better than one that tries. "
              "Read every other mean against this number"),
    _m(key="output_valid_rate", label="usable-output rate",
       stage="4 edits", tier="paper", direction=+1, target="1.00",
       what="of the outputs that exist, the fraction that are a rewrite "
            "rather than protocol text the model emitted about the task",
       caveat="the companion to generation_success_rate, which only checks "
              "that an output is NON-EMPTY. An echo of the system prompt or a "
              "bare '### Response:' is non-empty, scores 1.000 there, and "
              "then poisons every readability, NLI and length number computed "
              "from it. Measured after up to max_generation_attempts tries, "
              "so a value below 1.00 means the model could not be coaxed into "
              "a rewrite even on retry. Detection is a fixed marker list "
              "(core/validity.py), so it is a LOWER bound on the true rate"),
    _m(key="generation_first_attempt_rate", label="first-attempt success rate",
       stage="4 edits", tier="appendix", direction=+1, target="> 0.95",
       what="fraction of outputs that were usable on the very first call",
       caveat="the honest measure of how stable a model is on this task. "
              "Reported separately from output_valid_rate because retrying "
              "HIDES instability: a model that needs three attempts on a "
              "third of the corpus can still finish at output_valid_rate "
              "1.000. Quote both, and remember the retries cost real money"),
    _m(key="generation_attempts_mean", label="mean generation attempts",
       stage="4 edits", tier="appendix", direction=-1, target="1.00",
       what="average number of calls needed per output, 1 to "
            "max_generation_attempts",
       caveat="descriptive. Reads as a cost multiplier for the arm: 1.30 "
              "means 30% more generation calls than the ideal"),
    _m(key="human_edit_recall", label="human edit recall", stage="4 edits",
       tier="paper", direction=+1, target="> 0.85",
       what="of the jargon the human replaced, how much did we replace"),
    _m(key="copy_jargon_rate", label="copy-jargon rate", stage="4 edits",
       tier="appendix", direction=-1, target="< 0.10",
       what="jargon the human removed but we left untouched - the most "
            "interpretable way to PHRASE the recall result",
       caveat="exactly 1 - human_edit_recall, by construction: every gold term "
              "is either recalled or copied. Report it as a restatement, not "
              "as separate evidence, and keep it out of the significance "
              "family or one result consumes two FDR slots"),
    _m(key="replacement_precision", label="reference-vocabulary hit (NOT a precision)",
       stage="4 edits",
       tier="appendix", direction=+1, target="descriptive only - see caveat",
       what="whether the output used ANY content word the human reference "
            "introduced. Despite the name it is NOT per-term",
       caveat="BROKEN AS NAMED, measured 2026-08-15. The support test is "
              "`ref_added & sys_content_words`, and `ref_added` is derived "
              "from (reference, original) only - it does not depend on the "
              "term being scored. So the same verdict is applied to every "
              "changed term in a note and the per-note value can only be 0 or "
              "1. Verified on CLEAN93/qwen3p7-plus: 265 of 265 note-arm values "
              "are exactly 0.0 or 1.0, and no note has two terms that disagree. "
              "One incidental shared word credits every replacement in the "
              "sentence. Superseded by `replacement_quality`, which does the "
              "span alignment properly. Do not quote it as "
              "evidence that replacements were correct"),
    _m(key="replacement_quality", label="replacement quality, all terms",
       stage="4 edits",
       tier="appendix", direction=+1, target="descriptive for now - see caveat",
       what="for each hard term, content-word F1 between the span the SYSTEM "
            "put in that term's slot and the span the HUMAN REFERENCE put "
            "there. Answers 'did we put the right thing there', which "
            "human_edit_recall (did we change it at all) cannot",
       caveat="REWARDS NOT EDITING - quote `replacement_quality_edited` "
              "instead. A term both sides left alone scores a free 1.0, so an "
              "arm that edits less scores higher. On run100 the naive arm beats "
              "grounded on this variant in 4 of 6 models and trails it in ALL 6 "
              "once the free points are removed. Same not-editing bias that "
              "sinks SARI here. Kept only as the denominator-complete version"),
    _m(key="replacement_quality_edited",
       label="replacement quality, terms the human replaced",
       stage="4 edits",
       tier="appendix", direction=+1, target="descriptive for now - see caveat",
       what="replacement_quality restricted to terms the HUMAN actually "
            "replaced - the honest 'was our replacement any good' number",
       caveat="the replacement for `replacement_precision`. Both spans are "
              "aligned back to the term's own slot via difflib opcodes over "
              "the original, so every term gets its own verdict instead of one "
              "note-level 0/1, and the system span is re-derived by us rather "
              "than read from the model's <replace> tags, so it is not "
              "self-graded. STRICT: it is content-word overlap, so a correct "
              "paraphrase with different words scores 0 ('anhedonic' -> "
              "'unable to feel pleasure' vs 'lost interest in things'). Read "
              "it as a LOWER BOUND on replacement quality. Still DESCRIPTIVE "
              "and deliberately OUT of the Benjamini-Hochberg family: adding "
              "it would move the adjusted p-value of every other test in an "
              "already-published run"),
    _m(key="replacement_hit_rate", label="replacement any-overlap rate",
       stage="4 edits",
       tier="appendix", direction=+1, target="descriptive",
       what="fraction of aligned terms where the system's replacement shares "
            "at least one content word with the human's replacement - the "
            "binary, more forgiving version of replacement_quality",
       caveat="computed over ALL aligned terms, so it carries the same "
              "not-editing bias as `replacement_quality`"),
       _m(key="n_replacement_aligned", label="terms with an aligned replacement",
        stage="4 edits",
        tier="appendix", direction=0, target="descriptive",
        what="denominator for replacement_quality: hard terms whose slot could "
           "be aligned in BOTH the reference and the system output",
        caveat="always read the quality score against this. A term is dropped "
             "when it cannot be located in the original, or when either side "
             "replaced it with stopwords only"),
       _m(key="n_replacement_edited",
        label="terms the human replaced (scored)",
        stage="4 edits",
        tier="appendix", direction=0, target="descriptive",
        what="denominator for replacement_quality_edited - aligned terms where "
           "the reference did not keep the term verbatim"),
       _m(key="n_replacement_ambiguous",
        label="terms refused as unattributable",
        stage="4 edits",
        tier="appendix", direction=-1, target="descriptive",
        what="hard terms whose edit block also covered ANOTHER hard term, so "
           "the alignment cannot say which output words replaced which term",
        caveat="the honest cost of not faking attribution: run100 refuses 50-76 "
             "terms per arm (a quarter to a third) because two DIFFERENT hard "
             "terms sat side by side and collapsed into one difflib replace "
             "block. Crediting a merged span to every term in it would "
             "reintroduce the exact shared-verdict defect that "
             "`replacement_precision` suffers from. NOTE: a phrase and the "
             "fragments it was split into are NOT counted as rivals - only the "
             "longest span survives - or every split phrase would be refused "
             "against its own pieces. Report this next to the quality score"),
    _m(key="definition_borrow_rate", label="definition borrowing", stage="4 edits",
       tier="appendix", direction=0, target="descriptive - the arm gap IS the finding",
       what="of the terms an arm changed, how many reused a content word from "
            "that term's retrieved glossary definition",
       caveat="the mechanism behind the grounded-vs-termonly result, measured "
              "per note instead of only in analysis/conditional_grounding.py. "
              "Deliberately DESCRIPTIVE: grounded is shown the definitions and "
              "the other arms are not, so a difference here is expected by "
              "construction and testing it would burn an FDR slot to confirm "
              "something guaranteed. Read it as 'how much of the glossary's "
              "wording ended up in the output', then read what that cost in "
              "human_edit_recall and NLI"),
    _m(key="replacement_f1", label="replacement F1 (inherits a broken precision)",
       stage="4 edits",
       tier="appendix", direction=+1, target="descriptive only - see caveat",
       what="harmonic mean of human_edit_recall and replacement_precision",
       caveat="DEMOTED from paper tier 2026-08-15. Half of it is "
              "replacement_precision, which is not per-term (see its caveat), "
              "so this cannot support a claim that the system replaced jargon "
              "CORRECTLY. Quote human_edit_recall instead - that half is "
              "genuinely per-term and is unaffected"),
    _m(key="rewrite_aggressiveness", label="rewrite aggressiveness", stage="4 edits",
       tier="appendix", direction=0, target="descriptive",
       what="content words we removed that the reference kept",
       caveat="NOT an error rate - legitimate restructuring scores here"),

    _m(key="attributable_rate", label="attributable rate", stage="5 attribution",
       tier="paper", direction=+1, target="> 0.50",
       what="of the edits retrieval demonstrably caused, the fraction with a "
            "trustworthy explanation (held-out LDS >= 0.4, clear winner)"),
    _m(key="lds_median", label="held-out LDS (median)", stage="5 attribution",
       tier="paper", direction=+1, target="> 0.60 (paper reports 0.6-0.85)",
       what="Spearman between the surrogate's predictions and the true "
            "log-probs on masks it never saw - how trustworthy the "
            "attributions are"),
    _m(key="lds_optimism_gap", label="LDS optimism gap", stage="5 attribution",
       tier="appendix", direction=-1, target="< 0.15",
       what="in-sample LDS minus held-out LDS - how much an in-sample number "
            "would have overstated faithfulness",
       caveat="a methodological result in its own right, not a quality score"),
    _m(key="helped_rate", label="helped rate", stage="5 attribution",
       tier="paper", direction=0, target="descriptive - the split is the finding",
          what="fraction of edits retrieval made at least twice as likely "
          "(full-vs-empty effect >= ln(2) = 0.693 nats in the executed "
          "configuration)"),
    _m(key="hurt_rate", label="hurt rate", stage="5 attribution",
       tier="paper", direction=-1, target="< 0.10",
       what="fraction of edits retrieval made LESS likely - glossary actively "
            "harming the rewrite"),
    _m(key="top1_drop_median", label="top-1 log-prob drop (all edits)",
       stage="5 attribution",
       tier="appendix", direction=+1, fmt="{:.2f}", target="descriptive",
       what="cost of removing the single highest-weighted source (paper Eq. 1), "
            "averaged over EVERY attributed edit",
       caveat="NOT comparable to the paper's Figure 4a. Most edits have no "
              "source effect at all, so there is nothing to remove and the "
              "drop is ~0 by construction; the median over all edits therefore "
              "reads as a failure when the method is working. Quote "
              "`top1_drop_median_helped` instead"),
    _m(key="top1_drop_median_helped", label="top-1 log-prob drop (helped edits)",
       stage="5 attribution",
       tier="paper", direction=+1, fmt="{:.2f}", target="> 0.5 nats",
       what="paper Definition 2.2, restricted to the edits where retrieval "
            "demonstrably mattered - the subset the paper's own figures "
            "correspond to",
       caveat="the paper reports roughly 0.43-0.75 for top-1 across three "
              "benchmarks, so this is the number to compare against"),
    _m(key="right_term_rate", label="winning source is the right term",
       stage="5 attribution", tier="paper", direction=+1, target="> 0.80",
       what="of the edits retrieval caused, the fraction whose top-weighted "
            "source was the entry retrieved FOR THAT TERM",
       caveat="the complement is cross-term contamination - the definition of a "
              "DIFFERENT word in the same sentence winning the attribution and "
              "changing the meaning. Needs no gold labels, which is what makes "
              "it the closest thing this family has to a precision score"),
    _m(key="oracle_agreement", label="surrogate agrees with the oracle",
       stage="5 attribution", tier="appendix", direction=+1, target="> 0.70",
       what="how often the LASSO's top source is also the top source under "
            "true leave-one-out ablation",
       caveat="only produced with --leave-one-out. Leave-one-out is the "
              "BASELINE the paper beats (Sec. 4), not its method, so this is a "
              "validation check rather than a target to optimise: it says the "
              "cheap surrogate reaches the same answer as the expensive "
              "exhaustive one on our data"),
    _m(key="relevant_source_rate", label="edits with a relevant source",
       stage="5 attribution", tier="appendix", direction=+1, target="descriptive",
       what="of the edits retrieval caused, the fraction with at least one "
            "INDIVIDUALLY relevant entry by the paper's delta = 2 criterion "
            "(App. A.4)",
       caveat="only produced with --leave-one-out. This is the per-source "
              "version of helped_rate: `source_effect` compares the whole "
              "glossary against nothing, which a reviewer can dismiss as a "
              "prompt-length effect, whereas this removes one entry and leaves "
              "the rest in place"),
    _m(key="n_relevant_sources_median", label="relevant sources per edit",
       stage="5 attribution", tier="appendix", direction=0, fmt="{:.1f}",
       target="descriptive",
       what="median number of individually relevant glossary entries per "
            "caused edit - the analogue of the paper's Figure 3a",
       caveat="only produced with --leave-one-out. The paper's point is that "
              "this stays small even when the context is large, which is why a "
              "sparse surrogate works"),
    _m(key="ablation_success_rate", label="ablation success rate",
       stage="5 attribution", tier="appendix", direction=+1, target="1.00",
       what="scoring calls that returned usable log-probs - a transport "
            "health check, not a quality metric"),
    _m(key="citation_precision", label="citation precision", stage="5 attribution",
       tier="appendix", direction=+1, target="> 0.60",
       what="ALCE-style: does the top-1 cited passage entail the edit",
       caveat="DESCRIPTIVE ONLY - an ungrounded arm scores 0 because it emits "
              "no citations, which is structural, not a measurement. Never "
              "significance-test this against another arm"),
    _m(key="citation_f1", label="citation F1", stage="5 attribution",
       tier="appendix", direction=+1, target="> 0.60",
       what="harmonic mean of citation precision and recall",
       caveat="same structural-zero caveat"),

    _m(key="rationale_fact_recall", label="rationale fact recall",
       stage="6 rationale", tier="appendix", direction=+1, target="> 0.85",
       what="fraction of the numeric facts we gave the model that it repeated "
            "correctly (Zipf, age-of-acquisition, source name, quoted passage)"),
    _m(key="rationale_fabrication_rate", label="rationale fabrications",
       stage="7 audit", tier="paper", direction=-1, target="< 0.05",
       what="rationales that named the WRONG source, quoted a passage that "
            "does not exist, or stated a wrong numeric value - i.e. genuine "
            "fabrication"),
    _m(key="rationale_omission_rate", label="rationale slot omissions",
       stage="7 audit", tier="appendix", direction=-1, target="< 0.40",
       what="rationales that simply did not mention a required statistic",
       caveat="v7 merged this with fabrication and reported a scary 42.3%; "
              "they are completely different severities and must be split"),
    _m(key="rationale_source_correct", label="rationale source correct",
       stage="7 audit", tier="appendix", direction=+1, target="> 0.95",
       what="rationale named the same glossary source it was given"),
    _m(key="rationale_quote_verified", label="rationale quote verified",
       stage="7 audit", tier="appendix", direction=+1, target="1.00",
       what="every multi-word quote really appears in the cited passage"),
    _m(key="rationale_template_rate", label="templated rationales",
       stage="7 audit", tier="appendix", direction=-1, target="< 0.30",
       what="pairs of rationales with >=85% word overlap - a style/diversity "
            "check, not a correctness one"),

    _m(key="judge_faithfulness", label="judge: faithfulness", stage="8 judge",
       tier="paper", direction=+1, fmt="{:.2f}", target="> 4.0 of 5",
       what="panel rating of clinical meaning preservation",
       caveat="LLM judges have known self-preference and verbosity biases; "
              "report Krippendorff alpha alongside"),
    _m(key="judge_simplicity", label="judge: simplicity", stage="8 judge",
       tier="paper", direction=+1, fmt="{:.2f}", target="> 4.0 of 5",
       what="panel rating of readability for a 6th-8th grader"),
    _m(key="judge_fluency", label="judge: fluency", stage="8 judge",
       tier="appendix", direction=+1, fmt="{:.2f}", target="> 4.0 of 5",
       what="panel rating of grammaticality"),
    _m(key="judge_win_rate", label="judge: win rate", stage="8 judge",
       tier="paper", direction=+1, target="> 0.50 to claim an advantage",
       what="share of blind pairwise comparisons this arm won"),
    _m(key="krippendorff_alpha", label="Krippendorff alpha", stage="8 judge",
       tier="appendix", direction=+1, target="> 0.67 for tentative conclusions",
       what="inter-judge agreement; below 0.67 the panel verdict is "
            "judge-dependent and should not be leaned on"),

]

BY_KEY: Dict[str, MetricSpec] = {m.key: m for m in REGISTRY}
PAPER_KEYS = [m.key for m in REGISTRY if m.tier == "paper"]
APPENDIX_KEYS = [m.key for m in REGISTRY if m.tier == "appendix"]
STAGES = sorted({m.stage for m in REGISTRY})

LEGACY_KEYS: Dict[str, str] = {
    "retrieval_coverage_addressed": "evidence_coverage",
    "retrieval_coverage": "whole_term_coverage",
    "rationale_grounding_error_rate": "rationale_fabrication_rate",
    "rationale_slot_coverage": "rationale_fact_recall",
    "rationale_source_ok_rate": "rationale_source_correct",
    "rationale_passage_ok_rate": "rationale_quote_verified",
    "n_second_hop_definitions": "n_expansion_definitions",
    "lasso_loo_top1_agreement": "oracle_agreement",
    "definition_uptake_rate": "definition_borrow_rate",
    "mean_related_sources": "on_term_sources",
    "self_term_hit_rate": "right_term_rate",
    "gold_edit_recall": "human_edit_recall",
    "signal_ratio": "on_term_source_share",
    "nli_coverage": "nli_completeness",
    "nli_faith": "nli_faithfulness",
}


def migrate_legacy_keys(obj):
    if isinstance(obj, dict):
        return {LEGACY_KEYS.get(k, k): migrate_legacy_keys(v)
                for k, v in obj.items()}
    if isinstance(obj, list):
        return [migrate_legacy_keys(v) for v in obj]
    return obj


def spec(key: str) -> Optional[MetricSpec]:
    return BY_KEY.get(key)


def arrow(key: str) -> str:
    s = BY_KEY.get(key)
    if not s:
        return ""
    return {1: "higher is better", -1: "LOWER is better",
            0: "descriptive"}[s.direction]


def fmt(key: str, value) -> str:
    s = BY_KEY.get(key)
    if value is None:
        return "--"
    try:
        return (s.fmt if s else "{:.3f}").format(float(value))
    except (TypeError, ValueError):
        return str(value)
