# Step-by-step detail - together-qwen3.5-9b (`run100_20260815_222318`)

Everything the pipeline did, per note and per stage. Not summarised.

==============================================================================

## Note 1 - `8`

**ORIGINAL**  He became anhedonic and disinterested in social activities, and had difficulty sleeping for frequent waking and restlessness.

**REFERENCE** He became unable to feel pleasure and disinterested in social activities, and had difficulty sleeping for frequent waking and restlessness.

| | FKGL | FRE | SMOG | Coleman-Liau | words |
|---|---:|---:|---:|---:|---:|
| ORIGINAL | 16.03 | 10.43 | 15.90 | 18.96 | 17 |
| REFERENCE | 15.22 | 21.57 | 15.90 | 16.94 | 20 |

### Stage 2 - extraction + classification

| term | kind | category | action | Zipf | AoA | syll |
|---|---|---|---|---:|---:|---:|
| `disinterested` | word | general_hard_word | replace | 2.91 | 12.4 | 4 |
| `anhedonic` | word | medical_descriptor | replace | 1.11 | None | 4 |

### Stage 3 - retrieval

coverage **0.5** (1/2), glossary budget 2/16

| term | Zipf stratum | defs | sources | matched via | origin |
|---|---|---:|---|---|---|
| `disinterested` | rare | 2 | wiktionary.json | exact | extracted |
| `anhedonic` | very_rare | 0 | - | - | extracted |

Glossary shown to the model:

1. `[wiktionary]` disinterested: If someone is disinterested, they are not affected by a situation, so they can make fair decisions about it.
2. `[wiktionary]` disinterested: If someone is disinterested, they are not interested in something; they find it boring.

### Stage 4 - arm `naive`

**output:** He felt no pleasure and lost interest in social activities, and he had trouble sleeping because he woke up often and felt restless.

| metric | value |
|---|---:|
| bertscore_f1 | 0.631 |
| coleman_liau | 9.90 |
| coleman_liau_drop | 9.07 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 10.82 |
| fkgl_drop | 5.20 |
| fre | 58.4 |
| fre_gain | 48.0 |
| human_edit_recall | 1.000 |
| length_ratio | 1.15 |
| n_words | 23.0 |
| nli_completeness | 0.993 |
| nli_faithfulness | 0.994 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.714 |
| sari | 20.69 |
| smog | 8.84 |
| smog_drop | 7.06 |

### Stage 4 - arm `termonly`

**output:** He felt no joy and lost interest in social activities, and had trouble sleeping due to frequent waking and restlessness.

| metric | value |
|---|---:|
| bertscore_f1 | 0.754 |
| coleman_liau | 11.43 |
| coleman_liau_drop | 7.53 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 10.50 |
| fkgl_drop | 5.53 |
| fre | 55.4 |
| fre_gain | 45.0 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 20.0 |
| nli_completeness | 0.992 |
| nli_faithfulness | 0.994 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 30.85 |
| smog | 11.21 |
| smog_drop | 4.70 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `disinterested` -> `lost interest` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** He felt no pleasure and lost interest in social activities, and had trouble sleeping due to frequent waking and restlessness.

| metric | value |
|---|---:|
| bertscore_f1 | 0.766 |
| coleman_liau | 12.88 |
| coleman_liau_drop | 6.08 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 11.09 |
| fkgl_drop | 4.94 |
| fre | 51.2 |
| fre_gain | 40.8 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 20.0 |
| nli_completeness | 0.991 |
| nli_faithfulness | 0.994 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 33.22 |
| smog | 11.21 |
| smog_drop | 4.70 |

annotation backend `novita`, 0 edits kept


==============================================================================

## Note 2 - `18`

**ORIGINAL**  Myocardial infarction can not be excluded.

**REFERENCE** Heart attack can not be excluded.

| | FKGL | FRE | SMOG | Coleman-Liau | words |
|---|---:|---:|---:|---:|---:|
| ORIGINAL | 14.28 | 3.34 | 13.02 | 14.07 | 6 |
| REFERENCE | 4.45 | 73.85 | 8.84 | 5.37 | 6 |

### Stage 2 - extraction + classification

| term | kind | category | action | Zipf | AoA | syll |
|---|---|---|---|---:|---:|---:|
| `Myocardial infarction` | phrase | medical_essential | elaborate | 2.58 | 16.64 | 8 |
| `can not be excluded` | phrase | general_hard_word | replace | 3.89 | 5.11 | 6 |
| `can` | word | medical_descriptor | replace | - | - | - |
| `not` | word | medical_descriptor | replace | - | - | - |
| `be` | word | medical_descriptor | replace | - | - | - |
| `excluded` | word | medical_descriptor | replace | - | - | - |

### Stage 3 - retrieval

coverage **0.5** (1/2), glossary budget 12/16

| term | Zipf stratum | defs | sources | matched via | origin |
|---|---|---:|---|---|---|
| `Myocardial infarction` | rare | 5 | iowa.json, justplainclear.json, michigan_plmd.json, readme_lay_vocab.jsonl | exact | extracted |
| `can not be excluded` | uncommon | 0 | - | - | extracted |
| `can` | common | 2 | wiktionary.json | exact | split_from_uncovered |
| `not` | common | 2 | wiktionary.json | exact | split_from_uncovered |
| `be` | common | 2 | wiktionary.json | exact | split_from_uncovered |
| `excluded` | uncommon | 1 | wiktionary.json | exact | split_from_uncovered |

Glossary shown to the model:

1. `[wiktionary]` excluded: If you exclude someone or something, you keep them out.
2. `[wiktionary]` not: "Not" makes a phrase have the opposite meaning.
3. `[wiktionary]` can: If someone can do something, they are able to do it.
4. `[wiktionary]` be: This verb tells us that a thing is present, or in a place.
5. `[readme]` inferior wall myocardial infarction: Heart damage at the bottom of the left ventricle due to a blocked artery.
6. `[wiktionary]` not: The item before "not" is more correct or better than the item after "not".
7. `[wiktionary]` can: If someone can do something, they are allowed to do it.
8. `[wiktionary]` be: Go somewhere; visit someone (only in the perfect tense).
9. `[readme]` inferior myocardial infarction: A heart attack caused by a blockage in a blood vessel that affects the lower part of the heart muscle.
10. `[iowa]` MYOCARDIAL INFARCTION: heart attack
11. `[michigan]` myocardial infarction: Occurs when the flow of blood to the heart is stopped by a blood clot or a spasm of an artery. Also called a heart attack or MI.
12. `[justplainclear]` myocardial infarction: A heart attack

### Stage 4 - arm `naive`

**output:** It is not possible to rule out a heart attack.

| metric | value |
|---|---:|
| bertscore_f1 | 0.581 |
| coleman_liau | 2.12 |
| coleman_liau_drop | 11.95 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.400 |
| diagnostic_identity_preservation | 1.000 |
| fkgl | 3.65 |
| fkgl_drop | 10.63 |
| fre | 86.7 |
| fre_gain | 83.4 |
| human_edit_recall | 1.000 |
| length_ratio | 1.67 |
| n_words | 10.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.902 |
| nli_faithfulness | 0.984 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 24.27 |
| smog | 8.84 |
| smog_drop | 4.18 |
| uncertainty_preservation | 1.000 |

### Stage 4 - arm `termonly`

**output:** A heart attack cannot be ruled out.

| metric | value |
|---|---:|
| bertscore_f1 | 0.703 |
| coleman_liau | 3.17 |
| coleman_liau_drop | 10.90 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.400 |
| diagnostic_identity_preservation | 1.000 |
| fkgl | 2.31 |
| fkgl_drop | 11.97 |
| fre | 91.0 |
| fre_gain | 87.6 |
| human_edit_recall | 1.000 |
| length_ratio | 1.17 |
| n_words | 7.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.823 |
| nli_faithfulness | 0.972 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 25.97 |
| smog | 3.13 |
| smog_drop | 9.89 |
| uncertainty_preservation | 1.000 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `Myocardial infarction` -> `heart attack` | replace | - | - | - | - | - | - | - |
| `can not be excluded` -> `ruled out` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** A heart attack might not be ruled out.

| metric | value |
|---|---:|
| bertscore_f1 | 0.679 |
| coleman_liau | 2.25 |
| coleman_liau_drop | 11.82 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| diagnostic_identity_preservation | 1.000 |
| fkgl | 0.80 |
| fkgl_drop | 13.48 |
| fre | 103.5 |
| fre_gain | 100.2 |
| human_edit_recall | 1.000 |
| length_ratio | 1.33 |
| n_words | 8.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.783 |
| nli_faithfulness | 0.709 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 34.03 |
| smog | 3.13 |
| smog_drop | 9.89 |
| uncertainty_preservation | 1.000 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `Myocardial infarction` -> `heart attack` | replace | attributed | 0.029 | 1.187 | 0.680 | 0.770 | 0.130 | - |
| `can not be excluded` -> `ruled out` | replace | attributed | -0.200 | -1.279 | 0.566 | 0.728 | 0.187 | - |

**edit `Myocardial infarction` -> `heart attack`**

- status: `attributed`
- log p full -0.0132, empty -0.0426
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.460` [justplainclear] myocardial infarction: A heart attack
    - `+0.330` [iowa] MYOCARDIAL INFARCTION: heart attack
    - `+0.110` [wiktionary] excluded: If you exclude someone or something, you keep them out.
    - `+0.095` [wiktionary] can: If someone can do something, they are able to do it.
    - `+0.089` [wiktionary] be: This verb tells us that a thing is present, or in a place.

- rationale: The original term refers to a sudden blockage of blood flow to the heart muscle, so "heart attack" conveys this life-threatening event in plain language. Phrase frequency rises from Zipf 2.58 to 4.89, while age of acquisition drops from 16.64 to 6.58. Patients can now grasp the severity of the condition without needing to know the specific medical terminology.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `can not be excluded` -> `ruled out`**

- status: `attributed`
- log p full -0.2888, empty -0.0891
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.501` [michigan] myocardial infarction: Occurs when the flow of blood to the heart is stopped by a blood clot or a spasm of an 
    - `+0.314` [readme] inferior myocardial infarction: A heart attack caused by a blockage in a blood vessel that affects the lower p
    - `+0.273` [wiktionary] can: If someone can do something, they are allowed to do it.
    - `+0.159` [wiktionary] excluded: If you exclude someone or something, you keep them out.
    - `+0.028` [wiktionary] be: Go somewhere; visit someone (only in the perfect tense).

- rationale: The original phrase means that a diagnosis remains possible, so "ruled out" conveys the same idea by stating it is no longer a possibility. Phrase frequency increases from Zipf 3.89 to 4.30, while age of acquisition decreases from 5.11 to 3.28. Patients can now immediately grasp that the condition is not a concern without needing to parse the negative construction.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

==============================================================================

## Note 3 - `21`

**ORIGINAL**  There was marked hematoma and swelling within the subdeltoid bursa.

**REFERENCE** There was obvious collection of blood and swelling within the side of the shoulder.

| | FKGL | FRE | SMOG | Coleman-Liau | words |
|---|---:|---:|---:|---:|---:|
| ORIGINAL | 6.01 | 69.79 | 8.84 | 14.30 | 10 |
| REFERENCE | 7.57 | 65.73 | 11.21 | 10.67 | 14 |

### Stage 2 - extraction + classification

| term | kind | category | action | Zipf | AoA | syll |
|---|---|---|---|---:|---:|---:|
| `subdeltoid bursa` | phrase | medical_essential | elaborate | 0.0 | 15.78 | 5 |
| `bursa` | word | medical_descriptor | replace | - | - | - |
| `hematoma` | word | medical_essential | elaborate | 2.61 | 14.78 | 1 |
| `marked` | word | general_hard_word | replace | 4.5 | None | 1 |

### Stage 3 - retrieval

coverage **0.6667** (2/3), glossary budget 8/16

| term | Zipf stratum | defs | sources | matched via | origin |
|---|---|---:|---|---|---|
| `subdeltoid bursa` | very_rare | 0 | - | - | extracted |
| `bursa` | rare | 2 | justplainclear.json, readme_lay_vocab.jsonl | exact | partial_split_from_uncovered |
| `hematoma` | rare | 4 | iowa.json, justplainclear.json, michigan_plmd.json, nih.json | exact | extracted |
| `marked` | common | 2 | wiktionary.json | exact | extracted |

Glossary shown to the model:

1. `[wiktionary]` marked: Something that is marked is significant or notable.
2. `[readme]` bursa: A small sac of fluid that cushions joints as they move.
3. `[nih]` hematoma: A pool of clotted or partially clotted blood in an organ, tissue, or body space, usually caused by a broken blood vessel.
4. `[wiktionary]` marked: A mark is a single line left by a pen or pencil, or any small bit of color that got onto something.
5. `[justplainclear]` bursa: A small sac (pouch) found in your body which is filled with fluid. Bursa help your tendons or muscles move around your joints. Parts of the shoulder showing a bursa
6. `[iowa]` HEMATOMA: a bruise, a black and blue mark
7. `[michigan]` hematoma: A bruise or when your skin is black and blue after an injury.
8. `[justplainclear]` hematoma: A collection of blood under the skin or in the body that is typically caused by a broken blood vessel

### Stage 4 - arm `naive`

**output:** There was a large collection of blood and swelling inside the sac under the shoulder muscle.

| metric | value |
|---|---:|
| bertscore_f1 | 0.734 |
| coleman_liau | 9.90 |
| coleman_liau_drop | 4.40 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 7.61 |
| fkgl_drop | -1.60 |
| fre | 69.0 |
| fre_gain | -0.8 |
| human_edit_recall | 1.000 |
| length_ratio | 1.14 |
| n_words | 16.0 |
| nli_completeness | 0.799 |
| nli_faithfulness | 0.711 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.200 |
| sari | 49.87 |
| severity_downgrade | 0.000 |
| severity_preservation | 1.000 |
| severity_tier_input | 2.000 |
| severity_tier_output | 2.000 |
| smog | 8.84 |
| smog_drop | 0.00 |

### Stage 4 - arm `termonly`

**output:** There was a big bruise and swelling inside the sac under the shoulder blade.

| metric | value |
|---|---:|
| bertscore_f1 | 0.588 |
| coleman_liau | 7.77 |
| coleman_liau_drop | 6.53 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 5.04 |
| fkgl_drop | 0.97 |
| fre | 83.9 |
| fre_gain | 14.1 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 14.0 |
| nli_completeness | 0.926 |
| nli_faithfulness | 0.708 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.200 |
| sari | 41.17 |
| severity_downgrade | 0.000 |
| severity_preservation | 0.000 |
| severity_tier_input | 2.000 |
| severity_tier_output | 2.000 |
| smog | 3.13 |
| smog_drop | 5.71 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `marked` -> `big` | replace | - | - | - | - | - | - | - |
| `hematoma` -> `bruise` | replace | - | - | - | - | - | - | - |
| `subdeltoid bursa` -> `sac under the shoulder blade` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** There was a big bruise and swelling in the fluid sac near the shoulder.

| metric | value |
|---|---:|
| bertscore_f1 | 0.575 |
| coleman_liau | 5.70 |
| coleman_liau_drop | 8.60 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 4.20 |
| fkgl_drop | 1.81 |
| fre | 89.9 |
| fre_gain | 20.1 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 14.0 |
| nli_completeness | 0.862 |
| nli_faithfulness | 0.719 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.200 |
| sari | 41.17 |
| severity_downgrade | 0.000 |
| severity_preservation | 0.000 |
| severity_tier_input | 2.000 |
| severity_tier_output | 2.000 |
| smog | 3.13 |
| smog_drop | 5.71 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `marked` -> `big` | replace | attributed | -0.076 | -0.205 | 0.719 | 0.842 | 0.053 | - |
| `hematoma` -> `bruise` | replace | attributed | -0.084 | -0.124 | 0.842 | 0.889 | 0.953 | - |
| `subdeltoid bursa` -> `fluid sac near the shoulder` | replace | attributed | 2.276 | 2.390 | 0.756 | 0.828 | 0.586 | - |

**edit `marked` -> `big`**

- status: `attributed`
- log p full -0.5006, empty -0.4249
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+0.172` [wiktionary] marked: A mark is a single line left by a pen or pencil, or any small bit of color that got onto something.
    - `+0.119` [michigan] hematoma: A bruise or when your skin is black and blue after an injury.
    - `+0.052` [nih] hematoma: A pool of clotted or partially clotted blood in an organ, tissue, or body space, usually caused by a
    - `+0.037` [justplainclear] hematoma: A collection of blood under the skin or in the body that is typically caused by a broken blood vesse

- rationale: The original term "marked" indicates a significant or noticeable degree, so "big" conveys that same sense of size or intensity in plain words. Phrase frequency increases from Zipf 4.50 to 5.67, while syllable count remains at 1. Patients can now grasp the scale of the condition without needing to know the specific adjective.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `hematoma` -> `bruise`**

- status: `attributed`
- log p full -1.1713, empty -1.0874
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+1.612` [iowa] HEMATOMA: a bruise, a black and blue mark
    - `+0.659` [michigan] hematoma: A bruise or when your skin is black and blue after an injury.
    - `-0.005` [readme] bursa: A small sac of fluid that cushions joints as they move.
    - `-0.331` [wiktionary] marked: A mark is a single line left by a pen or pencil, or any small bit of color that got onto something.
    - `-0.678` [nih] hematoma: A pool of clotted or partially clotted blood in an organ, tissue, or body space, usually caused by a

- rationale: The original term refers to a localized collection of blood outside of blood vessels, so "bruise" conveys that visible mark in plain language. Phrase frequency increases from 2.61 to 3.18, while age of acquisition drops from 14.78 to 5.45. Patients can now recognize the injury as a common skin mark rather than a complex medical condition.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `subdeltoid bursa` -> `fluid sac near the shoulder`**

- status: `attributed`
- log p full -2.1280, empty -4.4036
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+1.125` [readme] bursa: A small sac of fluid that cushions joints as they move.
    - `+0.538` [justplainclear] bursa: A small sac (pouch) found in your body which is filled with fluid. Bursa help your tendons or muscles m

- rationale: The glossary defines the subdeltoid bursa as a small sac of fluid that cushions joints as they move, so "fluid sac near the shoulder" keeps that protective function in plain language. Phrase frequency increases from 0.00 to 3.51, while age of acquisition falls from 15.78 to 9.00. Patients can now visualize the anatomical structure without needing to know the specific medical name.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

==============================================================================

## Note 4 - `26`

**ORIGINAL**  Smoking history, hypertension, and hyperlipidemia.

**REFERENCE** Smoking history, high blood pressure, and high fat in the blood.

| | FKGL | FRE | SMOG | Coleman-Liau | words |
|---|---:|---:|---:|---:|---:|
| ORIGINAL | 19.40 | -35.12 | 13.02 | 28.16 | 5 |
| REFERENCE | 4.79 | 80.31 | 8.84 | 8.40 | 11 |

### Stage 2 - extraction + classification

| term | kind | category | action | Zipf | AoA | syll |
|---|---|---|---|---:|---:|---:|
| `hyperlipidemia` | word | medical_essential | elaborate | 1.95 | None | 4 |
| `hypertension` | word | medical_essential | elaborate | 3.41 | 16.28 | 4 |

### Stage 3 - retrieval

coverage **1.0** (2/2), glossary budget 11/16

| term | Zipf stratum | defs | sources | matched via | origin |
|---|---|---:|---|---|---|
| `hyperlipidemia` | very_rare | 4 | justplainclear.json, michigan_plmd.json, readme_lay_vocab.jsonl | exact | extracted |
| `hypertension` | rare | 7 | iowa.json, justplainclear.json, michigan_plmd.json, nih.json, readme_lay_vocab.jsonl, wiktionary.json | exact | extracted |

Glossary shown to the model:

1. `[readme]` Hyperlipidemia: Hyperlipidemia is when you have too much fat, like cholesterol, in your blood.
2. `[readme]` HYPERTENSION: High blood pressure: when the force of blood in your arteries is too high.
3. `[readme]` hyperlipidemia: Having a lot of fats like cholesterol in your blood.
4. `[readme]` hypertension: High blood pressure is when the force of blood in the arteries is too high.
5. `[michigan]` hyperlipidemia: High levels of fat or fat-like substances (cholesterol). Hyperlipidemia is also called high cholesterol.
6. `[nih]` hypertension: A blood pressure of 140/90 or higher. Hypertension usually has no symptoms. It can harm the arteries and cause an increase in the risk of stroke, heart attack, kidney failure, and blindness. Also called high blood pressure.
7. `[justplainclear]` hyperlipidemia: High cholesterol
8. `[iowa]` HYPERTENSION: high blood pressure
9. `[michigan]` hypertension: When your low pressure (diastolic) is 90 or higher or the high pressure (systolic) is 140 or higher. Also called high blood pressure.
10. `[justplainclear]` hypertension: Also known as: high blood pressure, HBP A condition of having high blood pressure for a long period of time
11. `[wiktionary]` hypertension: Hypertension is the disease of having high blood pressure.

### Stage 4 - arm `naive`

**output:** The patient has a history of smoking, high blood pressure, and high cholesterol.

| metric | value |
|---|---:|
| bertscore_f1 | 0.572 |
| coleman_liau | 10.92 |
| coleman_liau_drop | 17.24 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 8.54 |
| fkgl_drop | 10.86 |
| fre | 57.0 |
| fre_gain | 92.1 |
| human_edit_recall | 1.000 |
| length_ratio | 1.18 |
| n_words | 13.0 |
| nli_completeness | 0.958 |
| nli_faithfulness | 0.966 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 51.55 |
| smog | 11.21 |
| smog_drop | 1.82 |

### Stage 4 - arm `termonly`

**output:** Smoking history, high blood pressure, and high cholesterol.

| metric | value |
|---|---:|
| bertscore_f1 | 0.820 |
| coleman_liau | 16.02 |
| coleman_liau_drop | 12.14 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 9.66 |
| fkgl_drop | 9.75 |
| fre | 40.1 |
| fre_gain | 75.2 |
| human_edit_recall | 1.000 |
| length_ratio | 0.73 |
| n_words | 8.0 |
| nli_completeness | 0.851 |
| nli_faithfulness | 0.981 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 71.24 |
| smog | 11.21 |
| smog_drop | 1.82 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `hypertension` -> `high blood pressure` | replace | - | - | - | - | - | - | - |
| `hyperlipidemia` -> `high cholesterol` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Smoking history, high blood pressure, and high cholesterol.

| metric | value |
|---|---:|
| bertscore_f1 | 0.820 |
| coleman_liau | 16.02 |
| coleman_liau_drop | 12.14 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 9.66 |
| fkgl_drop | 9.75 |
| fre | 40.1 |
| fre_gain | 75.2 |
| human_edit_recall | 1.000 |
| length_ratio | 0.73 |
| n_words | 8.0 |
| nli_completeness | 0.851 |
| nli_faithfulness | 0.981 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 71.24 |
| smog | 11.21 |
| smog_drop | 1.82 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `hypertension` -> `high blood pressure` | replace | attributed | -0.102 | -1.124 | 0.325 | 0.894 | 0.116 | - |
| `hyperlipidemia` -> `high cholesterol` | replace | attributed | -0.148 | -0.282 | 0.874 | 0.914 | 1.605 | - |

**edit `hypertension` -> `high blood pressure`**

- status: `attributed`
- log p full -0.1557, empty -0.0533
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.454` [iowa] HYPERTENSION: high blood pressure
    - `+0.337` [michigan] hyperlipidemia: High levels of fat or fat-like substances (cholesterol). Hyperlipidemia is also called high ch

- rationale: The original term refers to a condition where blood pressure remains persistently elevated, so "high blood pressure" conveys this same physiological state in everyday language. Phrase frequency rises from 3.41 to 4.71, indicating the replacement is more common, while age of acquisition drops from 16.28 to 8.95, showing it is learned much earlier in life. Patients can now recognize the condition immediately without needing specialized medical knowledge.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `hyperlipidemia` -> `high cholesterol`**

- status: `attributed`
- log p full -0.8197, empty -0.6718
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+2.059` [justplainclear] hyperlipidemia: High cholesterol
    - `+0.454` [michigan] hyperlipidemia: High levels of fat or fat-like substances (cholesterol). Hyperlipidemia is also called high ch
    - `+0.338` [justplainclear] hypertension: Also known as: high blood pressure, HBP A condition of having high blood pressure for a long per
    - `+0.028` [readme] HYPERTENSION: High blood pressure: when the force of blood in your arteries is too high.

- rationale: The original term refers to an excess of fats in the blood, so "high cholesterol" conveys that same condition using everyday language. Phrase frequency rises from Zipf 1.95 to 3.72, while syllable count increases from 4 to 5. Readers can now recognize the specific lipid issue without needing specialized medical vocabulary.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

==============================================================================

## Note 5 - `31`

**ORIGINAL**  She did complain of bladder spasms when she urinated and she did say that she has a history of chronic UTIs.

**REFERENCE** She did complain of bladder spasms when she urinated and she did say that she has a history of chronic urinary tract infections

| | FKGL | FRE | SMOG | Coleman-Liau | words |
|---|---:|---:|---:|---:|---:|
| ORIGINAL | 8.90 | 68.69 | 11.21 | 6.82 | 21 |
| REFERENCE | 11.85 | 51.07 | 14.55 | 9.39 | 23 |

### Stage 2 - extraction + classification

| term | kind | category | action | Zipf | AoA | syll |
|---|---|---|---|---:|---:|---:|
| `bladder spasms` | phrase | medical_descriptor | replace | 2.89 | 10.78 | 4 |
| `bladder` | word | medical_descriptor | replace | - | - | - |
| `spasms` | word | medical_descriptor | replace | - | - | - |
| `chronic UTIs` | phrase | abbreviation_essential | abbr_expand_elaborate | 2.05 | 11.25 | 3 |
| `chronic` | word | medical_descriptor | replace | - | - | - |
| `UTIs` | abbreviation | abbreviation_essential | abbr_expand_elaborate | - | - | - |
| `urinated` | word | general_hard_word | replace | 2.31 | None | 3 |

### Stage 3 - retrieval

coverage **0.3333** (1/3), glossary budget 16/16

| term | Zipf stratum | defs | sources | matched via | origin |
|---|---|---:|---|---|---|
| `bladder spasms` | rare | 0 | - | - | extracted |
| `bladder` | uncommon | 7 | justplainclear.json, michigan_plmd.json, nih.json, readme_lay_vocab.jsonl, wiktionary.json | exact | split_from_uncovered |
| `spasms` | rare | 2 | readme_lay_vocab.jsonl, wiktionary.json | exact | split_from_uncovered |
| `chronic UTIs` | very_rare | 0 | - | - | extracted |
| `chronic` | uncommon | 9 | iowa.json, justplainclear.json, michigan_plmd.json, readme_lay_vocab.jsonl, thesarus.json, wiktionary.json | exact | split_from_uncovered |
| `UTIs` | very_rare | 2 | dorland_medical_abbreviations.csv, readme_lay_vocab.jsonl | exact | split_from_uncovered |
| `urinated` | very_rare | 1 | wiktionary.json | exact | extracted |

Glossary shown to the model:

1. `[wiktionary]` urinated: When a person or animal urinates, it passes urine to empty the bladder.
2. `[readme]` UTIs: UTIs are infections in the urinary system.
3. `[readme]` spasms: When your muscles suddenly tighten up and hurt.
4. `[readme]` bladder: A bladder is a sac in your body that holds pee.
5. `[readme]` Chronic: A long-lasting or recurring health issue.
6. `[dorland]` UTIs: urinary tract infections
7. `[wiktionary]` spasms: A spasm is a sudden and jerky movement.
8. `[readme]` BLADDER: Bladder: Holds pee in your body.
9. `[readme]` chronic: An ongoing or frequently recurring health issue.
10. `[nih]` bladder: The organ that stores urine.
11. `[iowa]` CHRONIC: continuing for a long time, ongoing
12. `[michigan]` bladder: A hollow organ that stores pee (urine).
13. `[michigan]` chronic: Something, like a disease or symptom, that lasts for a long time.
14. `[justplainclear]` bladder: An organ where urine collects so the body can get rid of it
15. `[justplainclear]` chronic: Long term, long lasting, lifelong, constant, never ending, never goes away, happens again and again
16. `[wiktionary]` bladder: The bladder is the internal organ where urine collects.

### Stage 4 - arm `naive`

**output:** She complained of bladder spasms when she urinated and said she has a history of chronic UTIs.

| metric | value |
|---|---:|
| bertscore_f1 | 0.785 |
| coleman_liau | 8.73 |
| coleman_liau_drop | -1.91 |
| copy_jargon_rate | 1.000 |
| critical_error | 0.000 |
| fkgl | 8.39 |
| fkgl_drop | 0.50 |
| fre | 65.2 |
| fre_gain | -3.5 |
| human_edit_recall | 0.000 |
| length_ratio | 0.74 |
| n_words | 17.0 |
| nli_completeness | 0.995 |
| nli_faithfulness | 0.995 |
| replacement_f1 | 0.000 |
| rewrite_aggressiveness | 1.000 |
| sari | 22.80 |
| smog | 11.21 |
| smog_drop | 0.00 |
| temporality_preservation | 1.000 |

### Stage 4 - arm `termonly`

**output:** She said her bladder muscles twitched when she peed and she said she has had many long-term bladder infections.

| metric | value |
|---|---:|
| bertscore_f1 | 0.552 |
| coleman_liau | 10.42 |
| coleman_liau_drop | -3.60 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 7.97 |
| fkgl_drop | 0.93 |
| fre | 71.8 |
| fre_gain | 3.1 |
| human_edit_recall | 1.000 |
| length_ratio | 0.87 |
| n_words | 20.0 |
| nli_completeness | 0.980 |
| nli_faithfulness | 0.994 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 10.35 |
| smog | 8.84 |
| smog_drop | 2.37 |
| temporality_preservation | 0.000 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `bladder spasms` -> `bladder muscles twitched` | replace | - | - | - | - | - | - | - |
| `urinated` -> `peed` | replace | - | - | - | - | - | - | - |
| `chronic UTIs` -> `long-term bladder infections` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** She complained of her pee bladder squeezing tight when she peed and said she has had long-lasting urinary tract infections.

| metric | value |
|---|---:|
| bertscore_f1 | 0.579 |
| coleman_liau | 12.30 |
| coleman_liau_drop | -5.48 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 9.91 |
| fkgl_drop | -1.01 |
| fre | 59.6 |
| fre_gain | -9.1 |
| human_edit_recall | 1.000 |
| length_ratio | 0.91 |
| n_words | 21.0 |
| nli_completeness | 0.992 |
| nli_faithfulness | 0.993 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 14.31 |
| smog | 13.02 |
| smog_drop | -1.82 |
| temporality_preservation | 0.000 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `bladder spasms` -> `bladder squeezing tight` | replace | attributed | 1.790 | 1.814 | 0.313 | 0.866 | 0.217 | - |
| `urinated` -> `peed` | replace | attributed | 0.017 | 0.057 | 0.876 | 0.936 | 0.131 | - |
| `chronic UTIs` -> `long-lasting urinary tract infections` | replace | attributed | 1.909 | 1.936 | 0.815 | 0.938 | 0.068 | - |

**edit `bladder spasms` -> `bladder squeezing tight`**

- status: `attributed`
- log p full -3.5637, empty -5.3536
- masks scored: 66/66 (+5 top-k)
- ranked sources:
    - `+0.761` [readme] Chronic: A long-lasting or recurring health issue.
    - `+0.544` [readme] BLADDER: Bladder: Holds pee in your body.
    - `+0.447` [readme] spasms: When your muscles suddenly tighten up and hurt.
    - `+0.393` [michigan] chronic: Something, like a disease or symptom, that lasts for a long time.
    - `+0.237` [michigan] bladder: A hollow organ that stores pee (urine).

- rationale: The original term describes involuntary, painful contractions of the bladder muscle, so "bladder squeezing tight" conveys that same physical sensation in plain language. Phrase frequency increases from Zipf 2.89 to 3.16, while age of acquisition remains unchanged at 10.78. Patients can now visualize the uncomfortable muscle action without needing to know the specific medical name for the spasms.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `urinated` -> `peed`**

- status: `attributed`
- log p full -0.3370, empty -0.3536
- masks scored: 66/66 (+5 top-k)
- ranked sources:
    - `+0.251` [readme] spasms: When your muscles suddenly tighten up and hurt.
    - `+0.120` [justplainclear] chronic: Long term, long lasting, lifelong, constant, never ending, never goes away, happens again and again
    - `+0.060` [nih] bladder: The organ that stores urine.
    - `+0.039` [readme] UTIs: UTIs are infections in the urinary system.

- rationale: The original term means to release urine, so "peed" conveys that same bodily function in a much simpler word. Frequency (Zipf) increases from 2.31 to 3.10, while syllables drop from 3 to 1. Patients can now recognize the action immediately without needing to recall a formal medical verb.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `chronic UTIs` -> `long-lasting urinary tract infections`**

- status: `attributed`
- log p full -3.4545, empty -5.3633
- masks scored: 66/66 (+5 top-k)
- ranked sources:
    - `+0.776` [readme] Chronic: A long-lasting or recurring health issue.
    - `+0.707` [michigan] chronic: Something, like a disease or symptom, that lasts for a long time.
    - `+0.589` [dorland] UTIs: urinary tract infections
    - `+0.081` [nih] bladder: The organ that stores urine.

- rationale: The original phrase refers to urinary tract infections that persist over time, so "long-lasting urinary tract infections" keeps that central idea in plain language. Phrase frequency increases from 2.05 to 3.06, while age of acquisition rises from 11.25 to 13.67. Patients can now clearly identify the condition as a recurring issue without needing to know the specific medical abbreviation.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

==============================================================================

## Note 6 - `32`

**ORIGINAL**  There was no instability of the knee and no effusion.

**REFERENCE** There was no instability of the knee and no fluid collection.

| | FKGL | FRE | SMOG | Coleman-Liau | words |
|---|---:|---:|---:|---:|---:|
| ORIGINAL | 7.19 | 61.33 | 11.21 | 6.18 | 10 |
| REFERENCE | 8.01 | 57.23 | 11.21 | 7.87 | 11 |

### Stage 2 - extraction + classification

| term | kind | category | action | Zipf | AoA | syll |
|---|---|---|---|---:|---:|---:|
| `instability` | word | general_hard_word | replace | 3.71 | 12.55 | 5 |
| `effusion` | word | medical_descriptor | replace | 2.41 | 14.29 | 3 |

### Stage 3 - retrieval

coverage **1.0** (2/2), glossary budget 2/16

| term | Zipf stratum | defs | sources | matched via | origin |
|---|---|---:|---|---|---|
| `instability` | uncommon | 1 | wiktionary.json | exact | extracted |
| `effusion` | very_rare | 1 | nih.json | exact | extracted |

Glossary shown to the model:

1. `[wiktionary]` instability: Instability is the condition of not being stable, which can make things uncertain or unsafe.
2. `[nih]` effusion: An abnormal collection of fluid in hollow spaces or between tissues of the body. For example, a pleural effusion is a collection of fluid between the two layers of membrane covering the lungs.

### Stage 4 - arm `naive`

**output:** The knee was stable and there was no swelling.

| metric | value |
|---|---:|
| bertscore_f1 | 0.635 |
| coleman_liau | 4.76 |
| coleman_liau_drop | 1.42 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 2.34 |
| fkgl_drop | 4.85 |
| fre | 94.3 |
| fre_gain | 33.0 |
| human_edit_recall | 1.000 |
| length_ratio | 0.82 |
| n_words | 9.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.994 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 20.32 |
| smog | 3.13 |
| smog_drop | 8.08 |

### Stage 4 - arm `termonly`

**output:** There was no loose movement in the knee and no fluid buildup.

| metric | value |
|---|---:|
| bertscore_f1 | 0.815 |
| coleman_liau | 5.42 |
| coleman_liau_drop | 0.76 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 3.84 |
| fkgl_drop | 3.35 |
| fre | 88.9 |
| fre_gain | 27.6 |
| human_edit_recall | 1.000 |
| length_ratio | 1.09 |
| n_words | 12.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.994 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 36.98 |
| smog | 3.13 |
| smog_drop | 8.08 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `instability` -> `loose movement` | replace | - | - | - | - | - | - | - |
| `effusion` -> `fluid buildup` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** The knee was stable and had no fluid buildup.

| metric | value |
|---|---:|
| bertscore_f1 | 0.698 |
| coleman_liau | 4.11 |
| coleman_liau_drop | 2.07 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 3.65 |
| fkgl_drop | 3.54 |
| fre | 84.9 |
| fre_gain | 23.6 |
| human_edit_recall | 1.000 |
| length_ratio | 0.82 |
| n_words | 9.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.994 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 18.25 |
| smog | 3.13 |
| smog_drop | 8.08 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `instability` -> `stable` | replace | attributed | -0.161 | -0.640 | - | 1.000 | 1.012 | - |
| `effusion` -> `fluid buildup` | replace | attributed | 0.636 | 0.856 | - | 0.800 | 0.118 | - |

**edit `instability` -> `stable`**

- status: `attributed`
- log p full -0.3780, empty -0.2169
- masks scored: 6/6 (+2 top-k)
- ranked sources:
    - `+0.297` [nih] effusion: An abnormal collection of fluid in hollow spaces or between tissues of the body. For example, a pleu
    - `-0.715` [wiktionary] instability: Instability is the condition of not being stable, which can make things uncertain or unsafe.

- rationale: The original term "instability" refers to a state of being unsteady or prone to change, whereas the replacement "stable" directly conveys the opposite condition of being steady and secure. Phrase frequency increases from Zipf 3.71 to 4.48, while age of acquisition decreases from 12.55 to 8.90. Patients can now grasp the concept of a steady condition without needing to process the abstract idea of unsteadiness.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `effusion` -> `fluid buildup`**

- status: `attributed`
- log p full -1.0684, empty -1.7044
- masks scored: 6/6 (+2 top-k)
- ranked sources:
    - `+0.287` [wiktionary] instability: Instability is the condition of not being stable, which can make things uncertain or unsafe.
    - `+0.168` [nih] effusion: An abnormal collection of fluid in hollow spaces or between tissues of the body. For example, a pleu

- rationale: The original term refers to an abnormal collection of fluid within a body cavity, so "fluid buildup" conveys this accumulation in plain language. Phrase frequency increases from 2.41 to 3.31, while age of acquisition drops from 14.29 to 9.63. Patients can now visualize the physical presence of excess liquid without needing specialized medical vocabulary.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

==============================================================================

## Note 7 - `64`

**ORIGINAL**  Two days later, the pain resolved and she has not had a recurrence.

**REFERENCE** Two days later, the pain got better and she has not had a recurrence.

| | FKGL | FRE | SMOG | Coleman-Liau | words |
|---|---:|---:|---:|---:|---:|
| ORIGINAL | 4.91 | 83.01 | 8.84 | 5.57 | 13 |
| REFERENCE | 5.04 | 83.85 | 8.84 | 4.46 | 14 |

### Stage 2 - extraction + classification

| term | kind | category | action | Zipf | AoA | syll |
|---|---|---|---|---:|---:|---:|
| `recurrence` | word | general_hard_word | replace | 3.2 | 11.79 | 3 |
| `resolved` | word | general_hard_word | replace | 4.1 | None | 2 |

### Stage 3 - retrieval

coverage **1.0** (2/2), glossary budget 5/16

| term | Zipf stratum | defs | sources | matched via | origin |
|---|---|---:|---|---|---|
| `recurrence` | rare | 3 | nih.json, readme_lay_vocab.jsonl, wiktionary.json | exact | extracted |
| `resolved` | uncommon | 2 | wiktionary.json | exact | extracted |

Glossary shown to the model:

1. `[wiktionary]` resolved: To resolve means to create a solution for a problem.
2. `[readme]` recurrence: When a disease comes back after being treated.
3. `[wiktionary]` resolved: When a problem is resolved, it has been brought to a successful solution.
4. `[nih]` recurrence: Cancer that has recurred (come back), usually after a period of time during which the cancer could not be detected. The cancer may come back to the same place as the original (primary) tumor or to another place in the body. Also called recurrent cancer.
5. `[wiktionary]` recurrence: A recurrence is something that happens again.

### Stage 4 - arm `naive`

**output:** Two days later, the pain went away and she has not had it come back.

| metric | value |
|---|---:|
| bertscore_f1 | 0.827 |
| coleman_liau | 2.33 |
| coleman_liau_drop | 3.24 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 3.63 |
| fkgl_drop | 1.28 |
| fre | 95.7 |
| fre_gain | 12.7 |
| human_edit_recall | 1.000 |
| length_ratio | 1.07 |
| n_words | 15.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.995 |
| nli_faithfulness | 0.994 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 46.29 |
| smog | 3.13 |
| smog_drop | 5.71 |
| temporality_preservation | 1.000 |

### Stage 4 - arm `termonly`

**output:** Two days later, the pain stopped and she has not had a flare-up.

| metric | value |
|---|---:|
| bertscore_f1 | 0.864 |
| coleman_liau | 3.78 |
| coleman_liau_drop | 1.78 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 3.10 |
| fkgl_drop | 1.82 |
| fre | 96.0 |
| fre_gain | 13.0 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 14.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.995 |
| nli_faithfulness | 0.994 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 53.86 |
| smog | 3.13 |
| smog_drop | 5.71 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `resolved` -> `stopped` | replace | - | - | - | - | - | - | - |
| `recurrence` -> `flare-up` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Two days later, the pain stopped and she has not had it come back.

| metric | value |
|---|---:|
| bertscore_f1 | 0.831 |
| coleman_liau | 3.21 |
| coleman_liau_drop | 2.35 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 2.51 |
| fkgl_drop | 2.40 |
| fre | 102.0 |
| fre_gain | 19.0 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 14.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.995 |
| nli_faithfulness | 0.994 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 46.29 |
| smog | 3.13 |
| smog_drop | 5.71 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `resolved` -> `stopped` | replace | attributed | -0.107 | -0.235 | - | 0.833 | 0.011 | - |
| `recurrence` -> `it come back` | replace | attributed | 2.062 | 2.546 | - | 0.875 | 0.299 | - |

**edit `resolved` -> `stopped`**

- status: `attributed`
- log p full -0.6624, empty -0.5554
- masks scored: 34/34 (+4 top-k)
- ranked sources:
    - `+0.100` [wiktionary] recurrence: A recurrence is something that happens again.
    - `+0.088` [wiktionary] resolved: When a problem is resolved, it has been brought to a successful solution.
    - `-0.002` [readme] recurrence: When a disease comes back after being treated.
    - `-0.040` [nih] recurrence: Cancer that has recurred (come back), usually after a period of time during which the cancer could
    - `-0.288` [wiktionary] resolved: To resolve means to create a solution for a problem.

- rationale: The original term "resolved" means that a problem or condition has come to an end, so "stopped" conveys that the issue is no longer active in simple language. Phrase frequency increases from Zipf 4.10 to 4.84, while syllable count drops from 2 to 1. Patients can now clearly see that the medical issue has ceased without needing to process a more complex verb.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `recurrence` -> `it come back`**

- status: `attributed`
- log p full -0.8759, empty -2.9379
- masks scored: 34/34 (+4 top-k)
- ranked sources:
    - `+0.836` [nih] recurrence: Cancer that has recurred (come back), usually after a period of time during which the cancer could
    - `+0.537` [wiktionary] resolved: To resolve means to create a solution for a problem.
    - `+0.513` [readme] recurrence: When a disease comes back after being treated.
    - `+0.179` [wiktionary] resolved: When a problem is resolved, it has been brought to a successful solution.

- rationale: The original term means that a condition returns after a period of absence, so "it come back" conveys that same idea of reappearance in simple language. Phrase frequency rises from 3.20 to 5.57, while age of acquisition drops from 11.79 to 5.31. Patients can now grasp that the illness is returning without needing to know the specific medical vocabulary.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

==============================================================================

## Note 8 - `81`

**ORIGINAL**  Description : Fever, otitis media, and possible sepsis.

**REFERENCE** Description : Fever, ear infection, and possible general infection.

| | FKGL | FRE | SMOG | Coleman-Liau | words |
|---|---:|---:|---:|---:|---:|
| ORIGINAL | 14.11 | 6.36 | 13.02 | 16.43 | 7 |
| REFERENCE | 15.56 | -2.21 | 15.90 | 20.37 | 8 |

### Stage 2 - extraction + classification

| term | kind | category | action | Zipf | AoA | syll |
|---|---|---|---|---:|---:|---:|
| `otitis media` | phrase | medical_essential | elaborate | 2.16 | None | 5 |
| `sepsis` | word | medical_essential | elaborate | 3.01 | 16.33 | 2 |

### Stage 3 - retrieval

coverage **1.0** (2/2), glossary budget 7/16

| term | Zipf stratum | defs | sources | matched via | origin |
|---|---|---:|---|---|---|
| `otitis media` | very_rare | 3 | michigan_plmd.json, readme_lay_vocab.jsonl, thesarus.json | exact | extracted |
| `sepsis` | rare | 4 | michigan_plmd.json, nih.json, readme_lay_vocab.jsonl | exact | extracted |

Glossary shown to the model:

1. `[readme]` otitis media: An ear infection causing inflammation in the middle ear.
2. `[readme]` sepsis: A severe condition where the body reacts to bacteria in the bloodstream by harming tissues and organs, potentially leading to death.
3. `[michigan]` otitis media: Ear infection, often in the middle ear.
4. `[readme]` Sepsis: When bacteria get into the blood, the body's reaction can lead to tissue and organ damage, potentially becoming life-threatening.
5. `[thesaurus]` otitis media: middle ear infection
6. `[nih]` sepsis: The presence of bacteria or their toxins in the blood or tissues.
7. `[michigan]` sepsis: A very serious infection in your blood caused by a germ (a bacteria). Also called septicemia.

### Stage 4 - arm `naive`

**output:** The patient has a fever, an ear infection, and might have sepsis.

| metric | value |
|---|---:|
| bertscore_f1 | 0.459 |
| coleman_liau | 6.38 |
| coleman_liau_drop | 10.05 |
| copy_jargon_rate | 0.500 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| diagnostic_identity_preservation | 1.000 |
| fkgl | 5.81 |
| fkgl_drop | 8.30 |
| fre | 74.8 |
| fre_gain | 68.5 |
| human_edit_recall | 0.500 |
| length_ratio | 1.50 |
| n_words | 12.0 |
| nli_completeness | 0.933 |
| nli_faithfulness | 0.821 |
| replacement_f1 | 0.667 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 37.05 |
| smog | 8.84 |
| smog_drop | 4.18 |
| uncertainty_preservation | 1.000 |

### Stage 4 - arm `termonly`

**output:** Fever, ear infection, and possible blood infection.

| metric | value |
|---|---:|
| bertscore_f1 | 0.653 |
| coleman_liau | 14.77 |
| coleman_liau_drop | 1.66 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| diagnostic_identity_preservation | 1.000 |
| fkgl | 10.74 |
| fkgl_drop | 3.37 |
| fre | 30.5 |
| fre_gain | 24.2 |
| human_edit_recall | 1.000 |
| length_ratio | 0.88 |
| n_words | 7.0 |
| nli_completeness | 0.737 |
| nli_faithfulness | 0.701 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.250 |
| sari | 61.09 |
| smog | 13.02 |
| smog_drop | 0.00 |
| uncertainty_preservation | 1.000 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `otitis media` -> `ear infection` | replace | - | - | - | - | - | - | - |
| `sepsis` -> `blood infection` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Fever, ear infection, and possible severe bloodstream infection.

| metric | value |
|---|---:|
| bertscore_f1 | 0.643 |
| coleman_liau | 19.65 |
| coleman_liau_drop | -3.22 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 1.000 |
| diagnostic_identity_preservation | 0.000 |
| fkgl | 12.61 |
| fkgl_drop | 1.51 |
| fre | 18.9 |
| fre_gain | 12.6 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 8.0 |
| nli_completeness | 0.834 |
| nli_faithfulness | 0.883 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.250 |
| sari | 59.09 |
| smog | 13.02 |
| smog_drop | 0.00 |
| uncertainty_preservation | 1.000 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `otitis media` -> `ear infection` | replace | attributed | -0.834 | -1.744 | 0.913 | 0.925 | 0.644 | - |
| `sepsis` -> `severe bloodstream infection` | replace | attributed | 1.700 | 1.822 | 0.893 | 0.957 | 1.479 | - |

**edit `otitis media` -> `ear infection`**

- status: `attributed`
- log p full -1.1575, empty -0.3232
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.759` [michigan] otitis media: Ear infection, often in the middle ear.
    - `+0.115` [nih] sepsis: The presence of bacteria or their toxins in the blood or tissues.
    - `+0.057` [readme] Sepsis: When bacteria get into the blood, the body's reaction can lead to tissue and organ damage, potentially
    - `+0.006` [michigan] sepsis: A very serious infection in your blood caused by a germ (a bacteria). Also called septicemia.
    - `-0.253` [readme] sepsis: A severe condition where the body reacts to bacteria in the bloodstream by harming tissues and organs,

- rationale: The original term refers to an inflammation of the middle ear, so "ear infection" conveys that same condition in plain language. Phrase frequency increases from Zipf 2.16 to 4.08, while syllable count drops from 5 to 4. Patients can now recognize the common ailment without needing to know the specific medical classification.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `sepsis` -> `severe bloodstream infection`**

- status: `attributed`
- log p full -1.9913, empty -3.6916
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+2.255` [readme] sepsis: A severe condition where the body reacts to bacteria in the bloodstream by harming tissues and organs,
    - `+0.776` [michigan] sepsis: A very serious infection in your blood caused by a germ (a bacteria). Also called septicemia.
    - `+0.228` [readme] otitis media: An ear infection causing inflammation in the middle ear.
    - `-0.010` [thesaurus] otitis media: middle ear infection

- rationale: The glossary defines sepsis as a severe condition where the body reacts to bacteria in the bloodstream by harming tissues and organs, so "severe bloodstream infection" captures that life-threatening reaction in plain language. Phrase frequency increases from Zipf 3.01 to 3.12, while age of acquisition drops from 16.33 to 9.05. You can now grasp the gravity of the infection without needing to know the specific medical diagnosis.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

==============================================================================

## Note 9 - `101`

**ORIGINAL**  Currently, primary complaint is one of fatigue that she feels throughout the day.

**REFERENCE** Currently, primary complaint is one of feeling tired that she feels throughout the day.

| | FKGL | FRE | SMOG | Coleman-Liau | words |
|---|---:|---:|---:|---:|---:|
| ORIGINAL | 7.63 | 63.49 | 11.21 | 11.82 | 13 |
| REFERENCE | 8.41 | 59.68 | 11.21 | 11.91 | 14 |

### Stage 2 - extraction + classification

| term | kind | category | action | Zipf | AoA | syll |
|---|---|---|---|---:|---:|---:|
| `primary complaint` | phrase | general_hard_word | replace | 4.21 | 8.89 | 5 |
| `primary` | word | medical_descriptor | replace | - | - | - |
| `complaint` | word | medical_descriptor | replace | - | - | - |
| `fatigue` | word | medical_descriptor | replace | 3.86 | 11.83 | 2 |

### Stage 3 - retrieval

coverage **0.5** (1/2), glossary budget 13/16

| term | Zipf stratum | defs | sources | matched via | origin |
|---|---|---:|---|---|---|
| `primary complaint` | uncommon | 0 | - | - | extracted |
| `primary` | common | 2 | wiktionary.json | exact | split_from_uncovered |
| `complaint` | uncommon | 5 | michigan_plmd.json, readme_lay_vocab.jsonl, wiktionary.json | exact | split_from_uncovered |
| `fatigue` | uncommon | 6 | justplainclear.json, michigan_plmd.json, nih.json, readme_lay_vocab.jsonl, wiktionary.json | exact | extracted |

Glossary shown to the model:

1. `[wiktionary]` primary: most basic, simplest.
2. `[readme]` complaint: A complaint is when a patient talks about their illness or problem.
3. `[readme]` fatigue: Feeling exhausted and lacking energy.
4. `[wiktionary]` primary: A primary is a kind of election held by a political party to choose the people it prefers for public office.
5. `[readme]` COMPLAINT: A complaint is when someone tells the doctor about an illness or issue they are experiencing.
6. `[nih]` fatigue: A condition marked by extreme tiredness and inability to function due to lack of energy. Fatigue may be acute or chronic.
7. `[michigan]` complaint: Your illness or symptom that is most important; the main reason you go to the doctor. Also known as "chief complaint".
8. `[michigan]` fatigue: tired, weak feeling of the whole body, feeling tired all over
9. `[wiktionary]` complaint: A complaint is an expression of dissatisfaction
10. `[justplainclear]` fatigue: Tired, weak feeling of the whole body, feeling tired
11. `[wiktionary]` complaint: A complaint is a small medical problem.
12. `[wiktionary]` fatigue: Fatigue is the extreme tiredness which is the result of having mental or physical exertion or illness.
13. `[wiktionary]` fatigue: Fatigue is the material failure, such as cracking or separation, caused by stress on the material.

### Stage 4 - arm `naive`

**output:** She is tired all day long.

| metric | value |
|---|---:|
| bertscore_f1 | 0.447 |
| coleman_liau | -1.40 |
| coleman_liau_drop | 13.22 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.250 |
| fkgl | 0.52 |
| fkgl_drop | 7.12 |
| fre | 102.0 |
| fre_gain | 38.6 |
| human_edit_recall | 1.000 |
| length_ratio | 0.43 |
| n_words | 6.0 |
| nli_completeness | 0.867 |
| nli_faithfulness | 0.970 |
| number_unit_preservation | 0.500 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.571 |
| sari | 14.49 |
| smog | 3.13 |
| smog_drop | 8.08 |
| temporality_preservation | 0.000 |

### Stage 4 - arm `termonly`

**output:** Currently, her main issue is tiredness that she feels all day.

| metric | value |
|---|---:|
| bertscore_f1 | 0.736 |
| coleman_liau | 7.87 |
| coleman_liau_drop | 3.94 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 5.86 |
| fkgl_drop | 1.77 |
| fre | 72.6 |
| fre_gain | 9.1 |
| human_edit_recall | 1.000 |
| length_ratio | 0.79 |
| n_words | 11.0 |
| nli_completeness | 0.993 |
| nli_faithfulness | 0.994 |
| number_unit_preservation | 0.500 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.400 |
| sari | 18.88 |
| smog | 11.21 |
| smog_drop | 0.00 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `primary complaint` -> `main issue` | replace | - | - | - | - | - | - | - |
| `fatigue` -> `tiredness` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Currently, her main reason for seeing the doctor is feeling very tired all day.

| metric | value |
|---|---:|
| bertscore_f1 | 0.553 |
| coleman_liau | 8.60 |
| coleman_liau_drop | 3.22 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 8.41 |
| fkgl_drop | -0.78 |
| fre | 59.7 |
| fre_gain | -3.8 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 14.0 |
| nli_completeness | 0.993 |
| nli_faithfulness | 0.064 |
| number_unit_preservation | 0.500 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 14.87 |
| smog | 8.84 |
| smog_drop | 2.37 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `primary complaint` -> `main reason for seeing the doctor` | replace | attributed | 2.198 | 2.379 | 0.918 | 0.963 | 1.977 | - |
| `fatigue` -> `very tired` | replace | attributed | -0.051 | -0.179 | 0.735 | 0.903 | 0.436 | - |

**edit `primary complaint` -> `main reason for seeing the doctor`**

- status: `attributed`
- log p full -1.7026, empty -3.9007
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+2.745` [michigan] complaint: Your illness or symptom that is most important; the main reason you go to the doctor. Also known as
    - `+0.768` [readme] COMPLAINT: A complaint is when someone tells the doctor about an illness or issue they are experiencing.
    - `+0.573` [wiktionary] primary: A primary is a kind of election held by a political party to choose the people it prefers for public 
    - `+0.379` [nih] fatigue: A condition marked by extreme tiredness and inability to function due to lack of energy. Fatigue may 
    - `+0.068` [readme] fatigue: Feeling exhausted and lacking energy.

- rationale: The glossary defines the primary complaint as the illness or symptom that is most important, so "main reason for seeing the doctor" keeps that central focus in plain language. Phrase frequency increases from Zipf 4.21 to 4.49, while age of acquisition falls from 8.89 to 7.84. Patients can now understand why they are there without needing to know the specific medical label.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `fatigue` -> `very tired`**

- status: `attributed`
- log p full -0.3573, empty -0.3067
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.698` [nih] fatigue: A condition marked by extreme tiredness and inability to function due to lack of energy. Fatigue may 
    - `+0.262` [wiktionary] fatigue: Fatigue is the material failure, such as cracking or separation, caused by stress on the material.
    - `+0.161` [readme] fatigue: Feeling exhausted and lacking energy.
    - `+0.148` [readme] COMPLAINT: A complaint is when someone tells the doctor about an illness or issue they are experiencing.
    - `+0.124` [wiktionary] primary: A primary is a kind of election held by a political party to choose the people it prefers for public 

- rationale: The original term "fatigue" refers to a state of extreme exhaustion, which the replacement "very tired" expresses in simple, everyday language. Phrase frequency rises from 3.86 to 4.69, indicating the new phrase is more common, while age of acquisition drops from 11.83 to 4.90, showing it is learned much earlier in life. Patients can now immediately recognize the symptom without needing to recall a specific medical label.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

==============================================================================

## Note 10 - `108`

**ORIGINAL**  He has noted some stool irregularity with occasional loose stools and new onset of pain predominantly in left neck.

**REFERENCE** He has noted some poop irregularity with occasional loose poop and new onset of pain predominantly in left neck.

| | FKGL | FRE | SMOG | Coleman-Liau | words |
|---|---:|---:|---:|---:|---:|
| ORIGINAL | 12.31 | 40.61 | 13.02 | 11.95 | 19 |
| REFERENCE | 12.31 | 40.61 | 13.02 | 11.03 | 19 |

### Stage 2 - extraction + classification

| term | kind | category | action | Zipf | AoA | syll |
|---|---|---|---|---:|---:|---:|
| `stool irregularity` | phrase | medical_descriptor | replace | 2.52 | 12.63 | 7 |
| `stool` | word | medical_descriptor | replace | - | - | - |
| `irregularity` | word | medical_descriptor | replace | - | - | - |
| `predominantly` | word | general_hard_word | replace | 3.8 | None | 5 |
| `loose stools` | phrase | medical_descriptor | replace | 3.03 | 7.71 | 2 |
| `new onset` | phrase | general_hard_word | replace | 3.72 | 10.72 | 3 |
| `new` | word | medical_descriptor | replace | - | - | - |
| `onset` | word | medical_descriptor | replace | - | - | - |

### Stage 3 - retrieval

coverage **0.5** (2/4), glossary budget 13/16

| term | Zipf stratum | defs | sources | matched via | origin |
|---|---|---:|---|---|---|
| `stool irregularity` | rare | 0 | - | - | extracted |
| `stool` | uncommon | 6 | justplainclear.json, nih.json, readme_lay_vocab.jsonl, wiktionary.json | exact | split_from_uncovered |
| `irregularity` | rare | 1 | dictonary.csv | exact | split_from_uncovered |
| `predominantly` | uncommon | 1 | dictonary.csv | exact | extracted |
| `loose stools` | rare | 1 | readme_lay_vocab.jsonl | exact | extracted |
| `new onset` | uncommon | 0 | - | - | extracted |
| `new` | common | 2 | wiktionary.json | exact | split_from_uncovered |
| `onset` | uncommon | 2 | michigan_plmd.json, wiktionary.json | exact | split_from_uncovered |

Glossary shown to the model:

1. `[readme]` loose stools: Watery poop.
2. `[dictionary]` Predominantly (adv.): In a predominant manner.
3. `[dictionary]` Irregularity (n.): The state or quality of being irregular; that which is irregular.
4. `[michigan]` onset: The start.
5. `[wiktionary]` new: If something is new, it is not old.
6. `[readme]` stool: The stuff that comes out when you go to the bathroom.
7. `[wiktionary]` onset: The onset of something is the time when it begins (usually something bad).
8. `[wiktionary]` new: If somebody is new, they are not experienced.
9. `[readme]` Stool: Stool is the waste material that comes out during a bowel movement.
10. `[nih]` stool: The material in a bowel movement. Stool is made up of undigested food, bacteria, mucus, and cells from the lining of the intestines. Also called feces.
11. `[justplainclear]` stool: Also known as: bowel movement, BM, feces, poop The solid or semi-solid waste that passes out of your rectum after food has been digested
12. `[wiktionary]` stool: A stool is a seat for one person that does not have a back or an armrest.
13. `[wiktionary]` stool: A stool is a piece of feces.

### Stage 4 - arm `naive`

**output:** He has noticed some changes in his bowel movements, including occasional loose stools, and he has started feeling pain mostly in his left neck.

| metric | value |
|---|---:|
| bertscore_f1 | 0.601 |
| coleman_liau | 11.24 |
| coleman_liau_drop | 0.71 |
| copy_jargon_rate | 0.333 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.143 |
| fkgl | 11.47 |
| fkgl_drop | 0.84 |
| fre | 55.6 |
| fre_gain | 15.0 |
| human_edit_recall | 0.667 |
| laterality_preservation | 1.000 |
| length_ratio | 1.26 |
| n_words | 24.0 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.994 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.167 |
| sari | 17.02 |
| smog | 11.21 |
| smog_drop | 1.82 |
| temporality_preservation | 0.000 |

### Stage 4 - arm `termonly`

**output:** He has noticed some bowel problems with occasional loose stools and new pain mostly in the left neck.

| metric | value |
|---|---:|
| bertscore_f1 | 0.768 |
| coleman_liau | 9.30 |
| coleman_liau_drop | 2.65 |
| copy_jargon_rate | 0.333 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.167 |
| fkgl | 7.82 |
| fkgl_drop | 4.50 |
| fre | 71.1 |
| fre_gain | 30.4 |
| human_edit_recall | 0.667 |
| laterality_preservation | 1.000 |
| length_ratio | 0.95 |
| n_words | 18.0 |
| nli_completeness | 0.993 |
| nli_faithfulness | 0.995 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.200 |
| sari | 19.78 |
| smog | 8.84 |
| smog_drop | 4.18 |
| temporality_preservation | 0.000 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `stool irregularity` -> `bowel problems` | replace | - | - | - | - | - | - | - |
| `new onset` -> `new` | replace | - | - | - | - | - | - | - |
| `predominantly` -> `mostly` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** He has noticed some poop irregularity with occasional watery poop and new pain mostly in the left neck.

| metric | value |
|---|---:|
| bertscore_f1 | 0.856 |
| coleman_liau | 9.94 |
| coleman_liau_drop | 2.00 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.333 |
| fkgl | 11.10 |
| fkgl_drop | 1.22 |
| fre | 47.6 |
| fre_gain | 7.0 |
| human_edit_recall | 1.000 |
| laterality_preservation | 1.000 |
| length_ratio | 0.95 |
| n_words | 18.0 |
| nli_completeness | 0.993 |
| nli_faithfulness | 0.931 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.167 |
| sari | 34.64 |
| smog | 13.02 |
| smog_drop | 0.00 |
| temporality_preservation | 0.000 |

annotation backend `novita`, 4 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `stool irregularity` -> `poop irregularity` | replace | attributed | 2.130 | 2.204 | 0.783 | 0.912 | 0.958 | - |
| `loose stools` -> `watery poop` | replace | attributed | 3.248 | 5.036 | 0.859 | 0.910 | 4.523 | - |
| `new onset` -> `new` | replace | attributed | -0.108 | -0.382 | 0.791 | 0.931 | 0.039 | - |
| `predominantly` -> `mostly` | replace | attributed | -0.304 | -0.795 | 0.836 | 0.924 | 0.020 | - |

**edit `stool irregularity` -> `poop irregularity`**

- status: `attributed`
- log p full -2.5254, empty -4.6557
- masks scored: 66/66 (+7 top-k)
- ranked sources:
    - `+1.310` [readme] loose stools: Watery poop.
    - `+0.352` [michigan] onset: The start.
    - `+0.322` [dictionary] Irregularity (n.): The state or quality of being irregular; that which is irregular.
    - `+0.224` [wiktionary] onset: The onset of something is the time when it begins (usually something bad).
    - `+0.195` [wiktionary] stool: A stool is a piece of feces.

- rationale: The original term refers to inconsistent bowel movements, so "poop irregularity" conveys the same idea using a more direct word for waste. Phrase frequency increases from Zipf 2.52 to 2.54, while age of acquisition remains at 12.63. Patients can now recognize the symptom without needing to know the formal medical classification.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `loose stools` -> `watery poop`**

- status: `attributed`
- log p full -0.1765, empty -3.4247
- masks scored: 66/66 (+7 top-k)
- ranked sources:
    - `+4.730` [readme] loose stools: Watery poop.
    - `+0.207` [readme] Stool: Stool is the waste material that comes out during a bowel movement.
    - `+0.135` [wiktionary] stool: A stool is a seat for one person that does not have a back or an armrest.
    - `+0.044` [justplainclear] stool: Also known as: bowel movement, BM, feces, poop The solid or semi-solid waste that passes out of your re

- rationale: The glossary defines the original term as "loose stools," so "watery poop" keeps that description of liquid waste in plain language. Phrase frequency increases from 3.03 to 3.06, while age of acquisition falls from 7.71 to 6.65. Patients can now understand the symptom immediately without needing to recall the clinical phrase.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `new onset` -> `new`**

- status: `attributed`
- log p full -0.3894, empty -0.2813
- masks scored: 66/66 (+7 top-k)
- ranked sources:
    - `+0.191` [dictionary] Irregularity (n.): The state or quality of being irregular; that which is irregular.
    - `+0.153` [readme] loose stools: Watery poop.
    - `+0.108` [readme] stool: The stuff that comes out when you go to the bathroom.
    - `+0.049` [readme] Stool: Stool is the waste material that comes out during a bowel movement.

- rationale: The original phrase "new onset" signals the beginning of a condition, so replacing it with "new" keeps that idea of a fresh start in simple language. Phrase frequency rises from Zipf 3.72 to 6.25, and age of acquisition drops from 10.72 to 4.72. Patients can now grasp that the illness is recent without needing to know the specific medical jargon.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `predominantly` -> `mostly`**

- status: `attributed`
- log p full -0.6496, empty -0.3457
- masks scored: 66/66 (+7 top-k)
- ranked sources:
    - `+0.052` [readme] stool: The stuff that comes out when you go to the bathroom.
    - `+0.032` [dictionary] Predominantly (adv.): In a predominant manner.

- rationale: The original term indicates that something occurs for the greater part of the time, so "mostly" conveys that same sense of majority in simpler language. Phrase frequency rises from Zipf 3.80 to 4.83, while syllable count drops from 5 to 2. Readers can now grasp the general proportion without needing to process a longer, more technical word.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

==============================================================================

## Note 11 - `143`

**ORIGINAL**  Description : The patient presents for a followup for history of erythema nodosum.

**REFERENCE** Description : The patient presents for a followup for history of red, painful tender lumps around fatty areas.

| | FKGL | FRE | SMOG | Coleman-Liau | words |
|---|---:|---:|---:|---:|---:|
| ORIGINAL | 11.71 | 32.50 | 14.55 | 14.60 | 12 |
| REFERENCE | 12.56 | 35.31 | 14.55 | 13.16 | 17 |

### Stage 2 - extraction + classification

| term | kind | category | action | Zipf | AoA | syll |
|---|---|---|---|---:|---:|---:|
| `erythema nodosum` | phrase | medical_essential | elaborate | 1.39 | None | 5 |
| `erythema` | word | medical_descriptor | replace | - | - | - |

### Stage 3 - retrieval

coverage **0.0** (0/1), glossary budget 3/16

| term | Zipf stratum | defs | sources | matched via | origin |
|---|---|---:|---|---|---|
| `erythema nodosum` | very_rare | 0 | - | - | extracted |
| `erythema` | very_rare | 3 | nih.json, readme_lay_vocab.jsonl | exact | partial_split_from_uncovered |

Glossary shown to the model:

1. `[readme]` erythema: Skin redness.
2. `[readme]` Erythema: Red skin.
3. `[nih]` erythema: Redness of the skin.

### Stage 4 - arm `naive`

**output:** The patient is coming back for a checkup because she has had a condition called erythema nodosum.

| metric | value |
|---|---:|
| bertscore_f1 | 0.201 |
| coleman_liau | 9.75 |
| coleman_liau_drop | 4.85 |
| copy_jargon_rate | 1.000 |
| critical_error | 0.000 |
| fkgl | 9.09 |
| fkgl_drop | 2.62 |
| fre | 60.2 |
| fre_gain | 27.7 |
| human_edit_recall | 0.000 |
| length_ratio | 1.00 |
| n_words | 17.0 |
| nli_completeness | 0.963 |
| nli_faithfulness | 0.971 |
| replacement_f1 | 0.000 |
| rewrite_aggressiveness | 1.000 |
| sari | 11.78 |
| smog | 11.21 |
| smog_drop | 3.35 |
| temporality_preservation | 0.000 |

### Stage 4 - arm `termonly`

**output:** The patient comes back for a checkup because of a history of red lumps under the skin.

| metric | value |
|---|---:|
| bertscore_f1 | 0.562 |
| coleman_liau | 6.00 |
| coleman_liau_drop | 8.60 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 7.00 |
| fkgl_drop | 4.70 |
| fre | 75.1 |
| fre_gain | 42.6 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 17.0 |
| nli_completeness | 0.541 |
| nli_faithfulness | 0.603 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.600 |
| sari | 23.58 |
| smog | 8.84 |
| smog_drop | 5.71 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `erythema nodosum` -> `red lumps under the skin` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** The patient comes back for a checkup about red skin lumps.

| metric | value |
|---|---:|
| bertscore_f1 | 0.527 |
| coleman_liau | 6.29 |
| coleman_liau_drop | 8.31 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 3.72 |
| fkgl_drop | 7.99 |
| fre | 88.0 |
| fre_gain | 55.5 |
| human_edit_recall | 1.000 |
| length_ratio | 0.65 |
| n_words | 11.0 |
| nli_completeness | 0.550 |
| nli_faithfulness | 0.523 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.667 |
| sari | 18.29 |
| smog | 3.13 |
| smog_drop | 11.43 |
| temporality_preservation | 0.000 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `erythema nodosum` -> `red skin lumps` | replace | attributed | 3.988 | 4.067 | - | 0.714 | 1.289 | - |

**edit `erythema nodosum` -> `red skin lumps`**

- status: `attributed`
- log p full -2.5660, empty -6.5541
- masks scored: 10/10 (+2 top-k)
- ranked sources:
    - `+1.832` [readme] Erythema: Red skin.
    - `+0.543` [nih] erythema: Redness of the skin.
    - `+0.514` [readme] erythema: Skin redness.

- rationale: The original term refers to a specific type of painful inflammation that causes tender, red bumps under the skin, so "red skin lumps" captures that visible and physical sensation in plain words. Phrase frequency increases from Zipf 1.39 to 3.18, while syllable count drops from 5 to 3. Patients can now recognize the physical signs of the condition without needing to memorize a complex medical diagnosis.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

==============================================================================

## Note 12 - `144`

**ORIGINAL**  She was iron deficient last year, and with her multiple surgeries and poor p. o. intake, may have become iron deficient again.

**REFERENCE** She was iron deficient last year, and with her multiple surgeries and poor food and fluid intake, may have become iron deficient again.

| | FKGL | FRE | SMOG | Coleman-Liau | words |
|---|---:|---:|---:|---:|---:|
| ORIGINAL | 7.47 | 61.08 | 11.21 | 7.87 | 22 |
| REFERENCE | 12.36 | 47.39 | 14.55 | 10.65 | 23 |

### Stage 2 - extraction + classification

| term | kind | category | action | Zipf | AoA | syll |
|---|---|---|---|---:|---:|---:|
| `iron deficient` | phrase | medical_descriptor | replace | 3.31 | 11.61 | 5 |
| `iron` | word | medical_descriptor | replace | - | - | - |
| `deficient` | word | medical_descriptor | replace | - | - | - |
| `p. o.` | phrase | general_hard_word | replace | 4.82 | None | 2 |
| `p` | word | medical_descriptor | replace | - | - | - |
| `o` | word | medical_descriptor | replace | - | - | - |

### Stage 3 - retrieval

coverage **0.0** (0/2), glossary budget 11/16

| term | Zipf stratum | defs | sources | matched via | origin |
|---|---|---:|---|---|---|
| `iron deficient` | rare | 0 | - | - | extracted |
| `iron` | common | 5 | michigan_plmd.json, nih.json, readme_lay_vocab.jsonl, wiktionary.json | exact | split_from_uncovered |
| `deficient` | rare | 3 | michigan_plmd.json, readme_lay_vocab.jsonl, thesarus.json | exact | split_from_uncovered |
| `p. o.` | unknown | 0 | - | - | extracted |
| `p` | common | 2 | wiktionary.json | exact | split_from_uncovered |
| `o` | common | 1 | wiktionary.json | exact | split_from_uncovered |

Glossary shown to the model:

1. `[wiktionary]` o: The fifteenth (15th) letter of the alphabet. It is a vowel.
2. `[wiktionary]` p: The sixteenth (16th) letter of the alphabet.
3. `[readme]` deficient: Not having as much of something as needed.
4. `[readme]` iron: A mineral that helps prevent anemia and can be taken in pill form.
5. `[wiktionary]` p: post, meaning after
6. `[michigan]` deficient: To not have enough.
7. `[nih]` iron: An important mineral the body needs to make hemoglobin, a substance in the blood that carries oxygen from the lungs to tissues throughout the body. Iron is also an important part of many other proteins and enzymes needed by the body for normal growth and development. It is found in red meat, fish, poultry, lentils, beans, and foods with iron added, such as cereal.
8. `[thesaurus]` deficient: lacking, not enough, poor
9. `[michigan]` iron: A mineral that can helps your body work in many ways. For example, it help blood carry oxygen and muscles to use oxygen.
10. `[wiktionary]` iron: An element with the symbol Fe and the atomic number 26.
11. `[wiktionary]` iron: A metal from the element.

### Stage 4 - arm `naive`

**output:** She was iron deficient last year, and because of her many surgeries and poor eating, she may have become iron deficient again.

| metric | value |
|---|---:|
| bertscore_f1 | 0.875 |
| coleman_liau | 9.75 |
| coleman_liau_drop | -1.87 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 11.76 |
| fkgl_drop | -4.29 |
| fre | 49.9 |
| fre_gain | -11.2 |
| human_edit_recall | 1.000 |
| length_ratio | 0.96 |
| n_words | 22.0 |
| nli_completeness | 0.787 |
| nli_faithfulness | 0.026 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 1.000 |
| sari | 39.88 |
| smog | 13.02 |
| smog_drop | -1.82 |
| uncertainty_preservation | 1.000 |

### Stage 4 - arm `termonly`

**output:** She was low in iron last year, and with her multiple surgeries and poor eating by mouth, may have become low in iron again.

| metric | value |
|---|---:|
| bertscore_f1 | 0.846 |
| coleman_liau | 6.41 |
| coleman_liau_drop | 1.46 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.200 |
| fkgl | 10.00 |
| fkgl_drop | -2.52 |
| fre | 66.2 |
| fre_gain | 5.1 |
| human_edit_recall | 1.000 |
| length_ratio | 1.04 |
| n_words | 24.0 |
| nli_completeness | 0.821 |
| nli_faithfulness | 0.074 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 36.35 |
| smog | 11.21 |
| smog_drop | 0.00 |
| uncertainty_preservation | 1.000 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `iron deficient` -> `low in iron` | replace | - | - | - | - | - | - | - |
| `p. o.` -> `by mouth` | replace | - | - | - | - | - | - | - |
| `iron deficient` -> `low in iron` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** She lacked iron last year, and with her many surgeries and poor eating by mouth, may have become iron lacking again.

| metric | value |
|---|---:|
| bertscore_f1 | 0.811 |
| coleman_liau | 8.48 |
| coleman_liau_drop | -0.60 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.200 |
| fkgl | 9.46 |
| fkgl_drop | -1.98 |
| fre | 64.7 |
| fre_gain | 3.6 |
| human_edit_recall | 1.000 |
| length_ratio | 0.91 |
| n_words | 21.0 |
| nli_completeness | 0.810 |
| nli_faithfulness | 0.086 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.667 |
| sari | 29.63 |
| smog | 8.84 |
| smog_drop | 2.37 |
| uncertainty_preservation | 1.000 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `iron deficient` -> `lacked iron` | replace | attributed | 0.697 | 0.843 | 0.430 | 0.801 | 0.147 | - |
| `p. o.` -> `by mouth` | replace | attributed | -0.106 | -0.436 | 0.783 | 0.912 | 0.076 | - |
| `iron deficient` -> `iron lacking` | replace | attributed | 0.838 | 1.063 | 0.906 | 0.810 | 0.100 | - |

**edit `iron deficient` -> `lacked iron`**

- status: `attributed`
- log p full -1.4364, empty -2.1337
- masks scored: 66/66 (+5 top-k)
- ranked sources:
    - `+0.183` [thesaurus] deficient: lacking, not enough, poor
    - `+0.036` [wiktionary] p: post, meaning after

- rationale: The source defines "iron deficient" as lacking or having poor amounts of iron, so "lacked iron" keeps that meaning in plain words. Phrase frequency increases from 3.31 to 3.75, while age of acquisition falls from 11.61 to 7.32. Patients can now understand the specific nutritional shortage without needing to parse the medical phrasing.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `p. o.` -> `by mouth`**

- status: `attributed`
- log p full -0.3351, empty -0.2290
- masks scored: 66/66 (+5 top-k)
- ranked sources:
    - `+0.180` [nih] iron: An important mineral the body needs to make hemoglobin, a substance in the blood that carries oxygen fro
    - `+0.104` [michigan] deficient: To not have enough.
    - `+0.043` [michigan] iron: A mineral that can helps your body work in many ways. For example, it help blood carry oxygen and muscle
    - `+0.022` [wiktionary] o: The fifteenth (15th) letter of the alphabet. It is a vowel.
    - `+0.014` [readme] iron: A mineral that helps prevent anemia and can be taken in pill form.

- rationale: The abbreviation "p. o." stands for the Latin phrase *per os*, which means "by mouth," so the replacement keeps the instruction to take medication orally in plain English. Phrase frequency remains stable at Zipf 4.82, while syllable count stays the same at 2. Patients can follow the dosing route immediately without needing to know Latin abbreviations.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `iron deficient` -> `iron lacking`**

- status: `attributed`
- log p full -1.1793, empty -2.0176
- masks scored: 66/66 (+5 top-k)
- ranked sources:
    - `+0.433` [thesaurus] deficient: lacking, not enough, poor
    - `+0.333` [readme] deficient: Not having as much of something as needed.
    - `+0.045` [michigan] deficient: To not have enough.

- rationale: The source defines "iron deficient" as having insufficient iron, so "iron lacking" keeps that meaning in plain words. Phrase frequency increases from 3.31 to 3.99, while age of acquisition falls from 11.61 to 7.32. Patients can now grasp the nutritional shortfall without needing to know the specific medical phrasing.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

==============================================================================

## Note 13 - `150`

**ORIGINAL**  We will schedule him for the Holter monitor and refer him back to his cardiologist.

**REFERENCE** We will schedule him for the continuous heart monitor and refer him back to his cardiologist.

| | FKGL | FRE | SMOG | Coleman-Liau | words |
|---|---:|---:|---:|---:|---:|
| ORIGINAL | 9.14 | 56.25 | 11.21 | 8.52 | 15 |
| REFERENCE | 10.56 | 47.83 | 13.02 | 10.26 | 16 |

### Stage 2 - extraction + classification

| term | kind | category | action | Zipf | AoA | syll |
|---|---|---|---|---:|---:|---:|
| `Holter monitor` | phrase | medical_essential | elaborate | 2.12 | 9.68 | 5 |
| `cardiologist` | word | medical_essential | elaborate | 2.9 | 13.42 | 5 |

### Stage 3 - retrieval

coverage **1.0** (2/2), glossary budget 5/16

| term | Zipf stratum | defs | sources | matched via | origin |
|---|---|---:|---|---|---|
| `Holter monitor` | very_rare | 1 | iowa.json | exact | extracted |
| `cardiologist` | rare | 4 | justplainclear.json, michigan_plmd.json, nih.json, wiktionary.json | exact | extracted |

Glossary shown to the model:

1. `[iowa]` HOLTER MONITOR: a portable machine for recording heart beats
2. `[nih]` cardiologist: A doctor who has special training to diagnose and treat diseases of the heart and blood vessels.
3. `[michigan]` cardiologist: A doctor who treats heart and blood vessel problems.
4. `[justplainclear]` cardiologist: Heart doctor
5. `[wiktionary]` cardiologist: A cardiologist is a doctor who specializes in medical problems related to the heart.

### Stage 4 - arm `naive`

**output:** We will schedule him for the Holter monitor and send him back to his cardiologist.

| metric | value |
|---|---:|
| bertscore_f1 | 0.834 |
| coleman_liau | 8.13 |
| coleman_liau_drop | 0.39 |
| copy_jargon_rate | 1.000 |
| critical_error | 0.000 |
| fkgl | 8.35 |
| fkgl_drop | 0.79 |
| fre | 61.9 |
| fre_gain | 5.6 |
| human_edit_recall | 0.000 |
| length_ratio | 0.94 |
| n_words | 15.0 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.994 |
| replacement_f1 | 0.000 |
| rewrite_aggressiveness | 1.000 |
| sari | 27.81 |
| smog | 11.21 |
| smog_drop | 0.00 |

### Stage 4 - arm `termonly`

**output:** We will schedule him for a heart rhythm check and refer him back to his heart doctor.

| metric | value |
|---|---:|
| bertscore_f1 | 0.840 |
| coleman_liau | 5.66 |
| coleman_liau_drop | 2.86 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 5.62 |
| fkgl_drop | 3.52 |
| fre | 85.1 |
| fre_gain | 28.8 |
| human_edit_recall | 1.000 |
| length_ratio | 1.06 |
| n_words | 17.0 |
| nli_completeness | 0.283 |
| nli_faithfulness | 0.938 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 44.48 |
| smog | 3.13 |
| smog_drop | 8.08 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `Holter monitor` -> `heart rhythm check` | replace | - | - | - | - | - | - | - |
| `cardiologist` -> `heart doctor` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** We will schedule him for a portable heart recorder and refer him back to his heart doctor.

| metric | value |
|---|---:|
| bertscore_f1 | 0.863 |
| coleman_liau | 7.36 |
| coleman_liau_drop | 1.16 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 7.70 |
| fkgl_drop | 1.44 |
| fre | 70.1 |
| fre_gain | 13.9 |
| human_edit_recall | 1.000 |
| length_ratio | 1.06 |
| n_words | 17.0 |
| nli_completeness | 0.633 |
| nli_faithfulness | 0.798 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 44.48 |
| smog | 11.21 |
| smog_drop | 0.00 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `Holter monitor` -> `portable heart recorder` | replace | attributed | 3.775 | 4.082 | - | 0.957 | 4.969 | - |
| `cardiologist` -> `heart doctor` | replace | attributed | 0.172 | 4.185 | - | 0.966 | 2.218 | - |

**edit `Holter monitor` -> `portable heart recorder`**

- status: `attributed`
- log p full -1.3149, empty -5.0903
- masks scored: 34/34 (+4 top-k)
- ranked sources:
    - `+4.969` [iowa] HOLTER MONITOR: a portable machine for recording heart beats
    - `-0.159` [nih] cardiologist: A doctor who has special training to diagnose and treat diseases of the heart and blood vessels.
    - `-0.219` [wiktionary] cardiologist: A cardiologist is a doctor who specializes in medical problems related to the heart.
    - `-0.311` [justplainclear] cardiologist: Heart doctor

- rationale: The original term refers to a small device worn on the body to continuously track heart activity, so "portable heart recorder" keeps that core function in plain language. Phrase frequency increases from Zipf 2.12 to 3.51, while age of acquisition falls from 9.68 to 8.37. Patients can now understand the equipment's purpose without needing to know the specific medical brand name.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `cardiologist` -> `heart doctor`**

- status: `attributed`
- log p full -0.0029, empty -0.1745
- masks scored: 34/34 (+4 top-k)
- ranked sources:
    - `+2.754` [justplainclear] cardiologist: Heart doctor
    - `+0.536` [nih] cardiologist: A doctor who has special training to diagnose and treat diseases of the heart and blood vessels.
    - `+0.472` [iowa] HOLTER MONITOR: a portable machine for recording heart beats
    - `+0.313` [michigan] cardiologist: A doctor who treats heart and blood vessel problems.
    - `-0.044` [wiktionary] cardiologist: A cardiologist is a doctor who specializes in medical problems related to the heart.

- rationale: The original term refers to a physician who specializes in treating the heart, so "heart doctor" conveys that specific medical role using everyday language. Phrase frequency rises from 2.90 to 4.76, while age of acquisition drops from 13.42 to 5.17. Patients can now identify the specialist's role immediately without needing to know the specific professional title.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

==============================================================================

## Note 14 - `161`

**ORIGINAL**  The patient wished to proceed with operative intervention.

**REFERENCE** The patient wished to proceed with an operation

| | FKGL | FRE | SMOG | Coleman-Liau | words |
|---|---:|---:|---:|---:|---:|
| ORIGINAL | 11.13 | 29.52 | 11.21 | 16.75 | 8 |
| REFERENCE | 6.71 | 61.24 | 8.84 | 9.50 | 8 |

### Stage 2 - extraction + classification

| term | kind | category | action | Zipf | AoA | syll |
|---|---|---|---|---:|---:|---:|
| `operative intervention` | phrase | medical_descriptor | replace | 3.71 | 13.11 | 8 |
| `operative` | word | medical_descriptor | replace | - | - | - |
| `intervention` | word | medical_descriptor | replace | - | - | - |
| `proceed` | word | general_hard_word | replace | 4.18 | 8.33 | 2 |

### Stage 3 - retrieval

coverage **0.5** (1/2), glossary budget 14/16

| term | Zipf stratum | defs | sources | matched via | origin |
|---|---|---:|---|---|---|
| `operative intervention` | uncommon | 0 | - | - | extracted |
| `operative` | uncommon | 4 | readme_lay_vocab.jsonl, wiktionary.json | exact | split_from_uncovered |
| `intervention` | uncommon | 6 | justplainclear.json, michigan_plmd.json, nih.json, readme_lay_vocab.jsonl, wiktionary.json | exact | split_from_uncovered |
| `proceed` | uncommon | 4 | michigan_plmd.json, thesarus.json, wiktionary.json | exact | extracted |

Glossary shown to the model:

1. `[michigan]` proceed: To go or move forward.
2. `[readme]` operative: Dealing with surgeries.
3. `[readme]` INTERVENTION: An intervention is a step taken to help treat or prevent illness or injury.
4. `[wiktionary]` proceed: When you proceed, you go forward with something.
5. `[readme]` Operative: Operative means related to surgery.
6. `[readme]` intervention: An intervention is a step taken to help treat or prevent a health problem.
7. `[wiktionary]` proceed: (formal) The proceeds of some individual project or sale are the money earned from doing it.
8. `[wiktionary]` operative: If something is operative, it is able to work.
9. `[nih]` intervention: In medicine, a treatment, procedure, or other action taken to prevent or treat disease, or improve health in other ways.
10. `[thesaurus]` proceed: go, move forward
11. `[wiktionary]` operative: An operative is an employee with some particular function or skill.
12. `[michigan]` intervention: A treatment or program.
13. `[justplainclear]` intervention: Ways to stop the spread of illness without drugs, such as hand washing, covering sneezes, closing schools, etc.
14. `[wiktionary]` intervention: An intervention is an activity designed to change or stop a situation.

### Stage 4 - arm `naive`

**output:** The patient wanted to have surgery.

| metric | value |
|---|---:|
| bertscore_f1 | 0.742 |
| coleman_liau | 7.30 |
| coleman_liau_drop | 9.45 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.250 |
| fkgl | 6.42 |
| fkgl_drop | 4.71 |
| fre | 59.7 |
| fre_gain | 30.2 |
| human_edit_recall | 1.000 |
| length_ratio | 0.75 |
| n_words | 6.0 |
| nli_completeness | 0.991 |
| nli_faithfulness | 0.993 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.250 |
| sari | 20.56 |
| smog | 8.84 |
| smog_drop | 2.37 |

### Stage 4 - arm `termonly`

**output:** The patient wanted to have surgery.

| metric | value |
|---|---:|
| bertscore_f1 | 0.742 |
| coleman_liau | 7.30 |
| coleman_liau_drop | 9.45 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.250 |
| fkgl | 6.42 |
| fkgl_drop | 4.71 |
| fre | 59.7 |
| fre_gain | 30.2 |
| human_edit_recall | 1.000 |
| length_ratio | 0.75 |
| n_words | 6.0 |
| nli_completeness | 0.991 |
| nli_faithfulness | 0.993 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.250 |
| sari | 20.56 |
| smog | 8.84 |
| smog_drop | 2.37 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `operative intervention` -> `surgery` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** The patient wanted to have surgery.

| metric | value |
|---|---:|
| bertscore_f1 | 0.742 |
| coleman_liau | 7.30 |
| coleman_liau_drop | 9.45 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.250 |
| fkgl | 6.42 |
| fkgl_drop | 4.71 |
| fre | 59.7 |
| fre_gain | 30.2 |
| human_edit_recall | 1.000 |
| length_ratio | 0.75 |
| n_words | 6.0 |
| nli_completeness | 0.991 |
| nli_faithfulness | 0.993 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.250 |
| sari | 20.56 |
| smog | 8.84 |
| smog_drop | 2.37 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `operative intervention` -> `surgery` | replace | attributed | 0.067 | 0.508 | 0.471 | 0.857 | 0.048 | - |

**edit `operative intervention` -> `surgery`**

- status: `attributed`
- log p full -0.1105, empty -0.1774
- masks scored: 66/66 (+2 top-k)
- ranked sources:
    - `+0.483` [readme] intervention: An intervention is a step taken to help treat or prevent a health problem.
    - `+0.435` [readme] Operative: Operative means related to surgery.
    - `+0.199` [readme] operative: Dealing with surgeries.
    - `+0.149` [wiktionary] operative: If something is operative, it is able to work.
    - `+0.061` [wiktionary] intervention: An intervention is an activity designed to change or stop a situation.

- rationale: The original phrase refers to a medical procedure performed to treat a condition, and "surgery" conveys this same idea using a common, everyday word. Phrase frequency rises from Zipf 3.71 to 4.63, while age of acquisition drops from 13.11 to 7.68. Patients can now recognize the planned treatment without needing specialized medical vocabulary.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

==============================================================================

## Note 15 - `178`

**ORIGINAL**  A KUB was obtained showing an abnormal bowel gas pattern.

**REFERENCE** An x-ray of the kidney, ureter and bladder was obtained showing an abnormal bowel gas pattern.

| | FKGL | FRE | SMOG | Coleman-Liau | words |
|---|---:|---:|---:|---:|---:|
| ORIGINAL | 7.19 | 61.33 | 8.84 | 8.50 | 10 |
| REFERENCE | 8.35 | 63.70 | 8.84 | 9.90 | 17 |

### Stage 2 - extraction + classification

| term | kind | category | action | Zipf | AoA | syll |
|---|---|---|---|---:|---:|---:|
| `abnormal bowel gas pattern` | phrase | medical_descriptor | replace | 3.29 | 10.05 | 8 |
| `abnormal` | word | medical_descriptor | replace | - | - | - |
| `bowel` | word | medical_descriptor | replace | - | - | - |
| `gas` | word | medical_descriptor | replace | - | - | - |
| `pattern` | word | medical_descriptor | replace | - | - | - |
| `obtained` | word | general_hard_word | replace | 4.49 | None | 2 |
| `KUB` | abbreviation | abbreviation_essential | abbr_expand_elaborate | None | None | 1 |

### Stage 3 - retrieval

coverage **0.6667** (2/3), glossary budget 15/16

| term | Zipf stratum | defs | sources | matched via | origin |
|---|---|---:|---|---|---|
| `abnormal bowel gas pattern` | uncommon | 0 | - | - | extracted |
| `abnormal` | uncommon | 5 | justplainclear.json, michigan_plmd.json, nih.json, wiktionary.json | exact | split_from_uncovered |
| `bowel` | uncommon | 4 | nih.json, readme_lay_vocab.jsonl, wiktionary.json | exact | split_from_uncovered |
| `gas` | common | 2 | wiktionary.json | exact | split_from_uncovered |
| `pattern` | common | 2 | wiktionary.json | exact | split_from_uncovered |
| `obtained` | uncommon | 1 | wiktionary.json | exact | extracted |
| `KUB` | very_rare | 1 | dorland_medical_abbreviations.csv | exact | extracted |

Glossary shown to the model:

1. `[wiktionary]` obtained: If you obtain something, you get it.
2. `[dorland]` KUB: kidneys, ureters, and bladder (x-ray)
3. `[wiktionary]` gas: A gas is a substance, such as air, that is not liquid or solid.
4. `[wiktionary]` pattern: A pattern is a design that uses the same set of elements many times in the same order.
5. `[readme]` bowel: The intestines in your belly that break down food.
6. `[nih]` abnormal: Not normal. Describes a state, condition, or behavior that is unusual or different from what is considered normal. An abnormal lesion or growth in or on the body may be benign (not cancer), precancerous or premalignant (likely to become cancer), or malignant (cancer).
7. `[wiktionary]` gas: Gas is a substance such as methane, ethane, propane, or butane that is burned for heat or to make electricity.
8. `[wiktionary]` pattern: The combined qualities and activities for an individual or a group of people describes a pattern.
9. `[readme]` Bowel: Your intestines in the belly that break down food.
10. `[michigan]` abnormal: Something that is not usual, like a growth or low or high amounts of blood cells.
11. `[nih]` bowel: The long, tube-shaped organ in the abdomen that completes the process of digestion. The bowel has two parts, the small bowel and the large bowel. Also called intestine.
12. `[justplainclear]` abnormal: Not normal, different from usual
13. `[wiktionary]` bowel: The bowel is an internal organ which helps an organism digest food.
14. `[wiktionary]` abnormal: An abnormal thing, or situation, is one that is strange, or not typical.
15. `[wiktionary]` abnormal: When something is abnormal, it often means that it is bigger than [[normal].

### Stage 4 - arm `naive`

**output:** A KUB was taken and showed that the bowel gas pattern was not normal.

| metric | value |
|---|---:|
| bertscore_f1 | 0.487 |
| coleman_liau | 4.87 |
| coleman_liau_drop | 3.63 |
| copy_jargon_rate | 1.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.333 |
| fkgl | 5.04 |
| fkgl_drop | 2.15 |
| fre | 83.9 |
| fre_gain | 22.5 |
| human_edit_recall | 0.000 |
| length_ratio | 0.82 |
| n_words | 14.0 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.994 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 15.87 |
| smog | 3.13 |
| smog_drop | 5.71 |

### Stage 4 - arm `termonly`

**output:** A test of the belly was done, showing too much gas in the intestines.

| metric | value |
|---|---:|
| bertscore_f1 | 0.476 |
| coleman_liau | 4.46 |
| coleman_liau_drop | 4.04 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.167 |
| fkgl | 5.04 |
| fkgl_drop | 2.15 |
| fre | 83.9 |
| fre_gain | 22.5 |
| human_edit_recall | 1.000 |
| length_ratio | 0.82 |
| n_words | 14.0 |
| nli_completeness | 0.810 |
| nli_faithfulness | 0.776 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 14.59 |
| smog | 8.84 |
| smog_drop | 0.00 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `KUB` -> `test of the belly` | replace | - | - | - | - | - | - | - |
| `obtained` -> `done` | replace | - | - | - | - | - | - | - |
| `abnormal bowel gas pattern` -> `too much gas in the intestines` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** A belly x-ray of the intestines showed unusual air pockets.

| metric | value |
|---|---:|
| bertscore_f1 | 0.489 |
| coleman_liau | 9.08 |
| coleman_liau_drop | -0.58 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.571 |
| fkgl | 8.37 |
| fkgl_drop | -1.18 |
| fre | 52.9 |
| fre_gain | -8.5 |
| human_edit_recall | 1.000 |
| length_ratio | 0.65 |
| n_words | 11.0 |
| nli_completeness | 0.598 |
| nli_faithfulness | 0.324 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.143 |
| sari | 16.41 |
| smog | 11.21 |
| smog_drop | -2.37 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `abnormal bowel gas pattern` -> `unusual air pockets` | replace | attributed | 2.229 | 2.251 | 0.784 | 0.945 | 0.285 | - |

**edit `abnormal bowel gas pattern` -> `unusual air pockets`**

- status: `attributed`
- log p full -3.7022, empty -5.9310
- masks scored: 66/66 (+2 top-k)
- ranked sources:
    - `+1.275` [wiktionary] gas: A gas is a substance, such as air, that is not liquid or solid.
    - `+0.990` [nih] abnormal: Not normal. Describes a state, condition, or behavior that is unusual or different from what is cons
    - `+0.443` [wiktionary] pattern: The combined qualities and activities for an individual or a group of people describes a pattern.
    - `+0.308` [wiktionary] obtained: If you obtain something, you get it.
    - `+0.286` [wiktionary] gas: Gas is a substance such as methane, ethane, propane, or butane that is burned for heat or to make electri

- rationale: The glossary defines gas as a substance that is not liquid or solid, so "unusual air pockets" keeps that physical description in plain language. Phrase frequency increases from 3.29 to 3.91, while age of acquisition falls from 10.05 to 8.56. Patients can now visualize the specific issue inside their abdomen without needing to interpret a complex medical phrase.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

==============================================================================

## Note 16 - `185`

**ORIGINAL**  She has been sedated with Ativan and came into the emergency room obtunded and unable to give any history.

**REFERENCE** She has been sedated with Ativan and came into the emergency room very drowsy and unable to give any history.

| | FKGL | FRE | SMOG | Coleman-Liau | words |
|---|---:|---:|---:|---:|---:|
| ORIGINAL | 12.31 | 40.61 | 15.90 | 9.20 | 19 |
| REFERENCE | 12.27 | 42.72 | 14.55 | 8.53 | 20 |

### Stage 2 - extraction + classification

| term | kind | category | action | Zipf | AoA | syll |
|---|---|---|---|---:|---:|---:|
| `obtunded` | word | medical_descriptor | replace | 1.01 | None | 3 |
| `sedated` | word | medical_descriptor | replace | 2.78 | None | 3 |
| `Ativan` | word | medical_essential | elaborate | 2.31 | None | 2 |

### Stage 3 - retrieval

coverage **0.6667** (2/3), glossary budget 4/16

| term | Zipf stratum | defs | sources | matched via | origin |
|---|---|---:|---|---|---|
| `obtunded` | very_rare | 1 | readme_lay_vocab.jsonl | exact | extracted |
| `sedated` | rare | 3 | readme_lay_vocab.jsonl, wiktionary.json | exact | extracted |
| `Ativan` | very_rare | 0 | - | - | extracted |

Glossary shown to the model:

1. `[readme]` obtunded: Being not fully alert.
2. `[readme]` Sedated: When you're sedated, you feel calm, relaxed, or sleepy because of specific medication.
3. `[readme]` SEDATED: Feeling calm, relaxed, or sleepy because of certain medications.
4. `[wiktionary]` sedated: A sedate person is calm and dignified.

### Stage 4 - arm `naive`

**output:** She has been given Ativan to help her relax, and when she arrived at the emergency room, she was very confused and could not tell anyone what happened.

| metric | value |
|---|---:|
| bertscore_f1 | 0.545 |
| coleman_liau | 8.21 |
| coleman_liau_drop | 0.99 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 12.19 |
| fkgl_drop | 0.13 |
| fre | 57.6 |
| fre_gain | 16.9 |
| human_edit_recall | 1.000 |
| length_ratio | 1.40 |
| n_words | 28.0 |
| nli_completeness | 0.957 |
| nli_faithfulness | 0.901 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.750 |
| sari | 18.16 |
| severity_downgrade | 0.000 |
| severity_tier_input | 3.000 |
| severity_tier_output | 3.000 |
| smog | 11.21 |
| smog_drop | 4.70 |

### Stage 4 - arm `termonly`

**output:** She was given a calming medicine by vein and came to the emergency room confused and unable to give any history.

| metric | value |
|---|---:|
| bertscore_f1 | 0.600 |
| coleman_liau | 7.92 |
| coleman_liau_drop | 1.28 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 11.70 |
| fkgl_drop | 0.61 |
| fre | 48.5 |
| fre_gain | 7.9 |
| human_edit_recall | 1.000 |
| length_ratio | 1.05 |
| n_words | 21.0 |
| nli_completeness | 0.075 |
| nli_faithfulness | 0.522 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.400 |
| sari | 27.45 |
| severity_downgrade | 0.000 |
| severity_tier_input | 3.000 |
| severity_tier_output | 3.000 |
| smog | 14.55 |
| smog_drop | 1.35 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `sedated` -> `given a calming medicine by vein` | replace | - | - | - | - | - | - | - |
| `obtunded` -> `confused` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** She was given Ativan by mouth and came to the emergency room not fully alert and unable to give any history.

| metric | value |
|---|---:|
| bertscore_f1 | 0.699 |
| coleman_liau | 6.82 |
| coleman_liau_drop | 2.38 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 11.14 |
| fkgl_drop | 1.17 |
| fre | 52.6 |
| fre_gain | 12.0 |
| human_edit_recall | 1.000 |
| length_ratio | 1.05 |
| n_words | 21.0 |
| nli_completeness | 0.986 |
| nli_faithfulness | 0.424 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 27.97 |
| severity_downgrade | 0.000 |
| severity_tier_input | 3.000 |
| severity_tier_output | 3.000 |
| smog | 13.02 |
| smog_drop | 2.88 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `sedated` -> `given` | replace | attributed | -0.393 | -0.765 | - | 0.653 | 0.018 | - |
| `obtunded` -> `not fully alert` | replace | attributed | 7.907 | 8.119 | - | 0.976 | 9.874 | - |

**edit `sedated` -> `given`**

- status: `attributed`
- log p full -0.9342, empty -0.5416
- masks scored: 18/18 (+3 top-k)
- ranked sources:
    - `+0.040` [readme] obtunded: Being not fully alert.
    - `+0.021` [wiktionary] sedated: A sedate person is calm and dignified.
    - `-0.165` [readme] Sedated: When you're sedated, you feel calm, relaxed, or sleepy because of specific medication.
    - `-0.333` [readme] SEDATED: Feeling calm, relaxed, or sleepy because of certain medications.

- rationale: The original term "sedated" describes a state of calmness or sleepiness, so "given" conveys that the patient received a calming treatment in simple words. Phrase frequency rises from Zipf 2.78 to 5.41, while syllable count drops from 3 to 2. Patients can now recognize that they received a calming treatment without needing to know the specific medical state.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `obtunded` -> `not fully alert`**

- status: `attributed`
- log p full -1.6541, empty -9.5608
- masks scored: 18/18 (+3 top-k)
- ranked sources:
    - `+9.627` [readme] obtunded: Being not fully alert.
    - `-0.247` [wiktionary] sedated: A sedate person is calm and dignified.
    - `-0.379` [readme] SEDATED: Feeling calm, relaxed, or sleepy because of certain medications.
    - `-0.405` [readme] Sedated: When you're sedated, you feel calm, relaxed, or sleepy because of specific medication.

- rationale: The original term describes a state where a patient is drowsy and difficult to wake, so "not fully alert" conveys that lack of responsiveness in plain language. Phrase frequency increases from Zipf 1.01 to 4.22, while syllable count rises from 3 to 5. Patients can now recognize the level of consciousness without needing to know the specific medical label.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

==============================================================================

## Note 17 - `202`

**ORIGINAL**  He has no edema now, but has had some mild leg swelling in the past.

**REFERENCE** He has no swelling now, but has had some mild leg swelling in the past.

| | FKGL | FRE | SMOG | Coleman-Liau | words |
|---|---:|---:|---:|---:|---:|
| ORIGINAL | 4.42 | 90.09 | 8.84 | 2.33 | 15 |
| REFERENCE | 3.63 | 95.73 | 3.13 | 3.49 | 15 |

### Stage 2 - extraction + classification

| term | kind | category | action | Zipf | AoA | syll |
|---|---|---|---|---:|---:|---:|
| `edema` | word | medical_descriptor | replace | 2.95 | 15.07 | 3 |

### Stage 3 - retrieval

coverage **1.0** (1/1), glossary budget 5/16

| term | Zipf stratum | defs | sources | matched via | origin |
|---|---|---:|---|---|---|
| `edema` | rare | 5 | iowa.json, michigan_plmd.json, nih.json, readme_lay_vocab.jsonl | exact | extracted |

Glossary shown to the model:

1. `[readme]` Edema: Swelling in the body caused by too much fluid.
2. `[readme]` edema: Swelling due to too much fluid in the body tissues.
3. `[nih]` edema: Swelling caused by excess fluid in body tissues.
4. `[iowa]` EDEMA: excess fluid collecting in tissue
5. `[michigan]` edema: Swelling caused by too much fluid in your body.

### Stage 4 - arm `naive`

**output:** He does not have swelling in his legs now, but he has had some mild swelling in his legs before.

| metric | value |
|---|---:|
| bertscore_f1 | 0.805 |
| coleman_liau | 4.47 |
| coleman_liau_drop | -2.14 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 5.78 |
| fkgl_drop | -1.36 |
| fre | 89.2 |
| fre_gain | -0.8 |
| human_edit_recall | 1.000 |
| length_ratio | 1.33 |
| n_words | 20.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.577 |
| nli_faithfulness | 0.994 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.667 |
| sari | 26.06 |
| severity_downgrade | 0.000 |
| severity_preservation | 1.000 |
| severity_tier_input | 1.000 |
| severity_tier_output | 1.000 |
| smog | 3.13 |
| smog_drop | 5.71 |
| temporality_preservation | 1.000 |

### Stage 4 - arm `termonly`

**output:** He has no swelling now, but has had some mild leg swelling in the past.

| metric | value |
|---|---:|
| bertscore_f1 | 1.000 |
| coleman_liau | 3.49 |
| coleman_liau_drop | -1.16 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 3.63 |
| fkgl_drop | 0.79 |
| fre | 95.7 |
| fre_gain | 5.6 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 15.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.156 |
| nli_faithfulness | 0.994 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 91.67 |
| severity_downgrade | 0.000 |
| severity_preservation | 1.000 |
| severity_tier_input | 1.000 |
| severity_tier_output | 1.000 |
| smog | 3.13 |
| smog_drop | 5.71 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `edema` -> `swelling` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** He has no swelling now, but had some mild leg swelling before.

| metric | value |
|---|---:|
| bertscore_f1 | 0.907 |
| coleman_liau | 5.42 |
| coleman_liau_drop | -3.08 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 3.84 |
| fkgl_drop | 0.58 |
| fre | 88.9 |
| fre_gain | -1.2 |
| human_edit_recall | 1.000 |
| length_ratio | 0.80 |
| n_words | 12.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.236 |
| nli_faithfulness | 0.994 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 47.71 |
| severity_downgrade | 0.000 |
| severity_preservation | 1.000 |
| severity_tier_input | 1.000 |
| severity_tier_output | 1.000 |
| smog | 3.13 |
| smog_drop | 5.71 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `edema` -> `swelling` | replace | attributed | 0.261 | 0.609 | - | 0.582 | 0.355 | - |

**edit `edema` -> `swelling`**

- status: `attributed`
- log p full -0.4381, empty -0.6986
- masks scored: 34/34 (+2 top-k)
- ranked sources:
    - `+0.453` [readme] Edema: Swelling in the body caused by too much fluid.
    - `+0.098` [michigan] edema: Swelling caused by too much fluid in your body.
    - `-0.045` [readme] edema: Swelling due to too much fluid in the body tissues.
    - `-0.268` [iowa] EDEMA: excess fluid collecting in tissue

- rationale: The original term refers to fluid buildup in the body tissues, so "swelling" conveys that physical expansion in plain words. Phrase frequency increases from Zipf 2.95 to 3.68, while syllable count drops from 3 to 2. Patients can now recognize the visible symptom without needing to recall a specific medical label.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

==============================================================================

## Note 18 - `231`

**ORIGINAL**  Mild secondary hyperparathyroidism.

**REFERENCE** Mild secondary hyperactive parathyroid gland

| | FKGL | FRE | SMOG | Coleman-Liau | words |
|---|---:|---:|---:|---:|---:|
| ORIGINAL | 20.98 | -50.01 | 11.21 | 36.20 | 3 |
| REFERENCE | 14.68 | -1.28 | 11.21 | 24.68 | 5 |

### Stage 2 - extraction + classification

| term | kind | category | action | Zipf | AoA | syll |
|---|---|---|---|---:|---:|---:|
| `secondary hyperparathyroidism` | phrase | medical_essential | elaborate | 1.88 | 19.11 | 8 |
| `secondary` | word | medical_descriptor | replace | - | - | - |
| `hyperparathyroidism` | word | medical_descriptor | replace | - | - | - |

### Stage 3 - retrieval

coverage **0.0** (0/1), glossary budget 4/16

| term | Zipf stratum | defs | sources | matched via | origin |
|---|---|---:|---|---|---|
| `secondary hyperparathyroidism` | very_rare | 0 | - | - | extracted |
| `secondary` | common | 2 | wiktionary.json | exact | split_from_uncovered |
| `hyperparathyroidism` | very_rare | 2 | justplainclear.json, nih.json | exact | split_from_uncovered |

Glossary shown to the model:

1. `[wiktionary]` secondary: second, next in order to the first or primary.
2. `[nih]` hyperparathyroidism: A condition in which the parathyroid gland (one of four pea-sized organs found on the thyroid) makes too much parathyroid hormone. This causes a loss of calcium from the bones and an increased level of calcium in the blood. Symptoms include bone pain and kidney problems.
3. `[wiktionary]` secondary: of less than primary importance.
4. `[justplainclear]` hyperparathyroidism: A condition where your parathyroid glands work too hard and raise the calcium level in your blood.

### Stage 4 - arm `naive`

**output:** The patient has mild secondary hyperparathyroidism.

| metric | value |
|---|---:|
| bertscore_f1 | 0.467 |
| coleman_liau | 22.77 |
| coleman_liau_drop | 13.43 |
| copy_jargon_rate | 1.000 |
| critical_error | 0.000 |
| fkgl | 12.32 |
| fkgl_drop | 8.66 |
| fre | 17.4 |
| fre_gain | 67.5 |
| human_edit_recall | 0.000 |
| length_ratio | 1.20 |
| n_words | 6.0 |
| nli_completeness | 0.991 |
| nli_faithfulness | 0.937 |
| replacement_f1 | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 12.22 |
| severity_downgrade | 0.000 |
| severity_preservation | 1.000 |
| severity_tier_input | 1.000 |
| severity_tier_output | 1.000 |
| smog | 11.21 |
| smog_drop | 0.00 |

### Stage 4 - arm `termonly`

**output:** Mild secondary hyperparathyroidism.

| metric | value |
|---|---:|
| bertscore_f1 | 0.623 |
| coleman_liau | 36.20 |
| coleman_liau_drop | 0.00 |
| copy_jargon_rate | 1.000 |
| critical_error | 0.000 |
| fkgl | 20.98 |
| fkgl_drop | 0.00 |
| fre | -50.0 |
| fre_gain | 0.0 |
| human_edit_recall | 0.000 |
| length_ratio | 0.60 |
| n_words | 3.0 |
| nli_completeness | 0.987 |
| nli_faithfulness | 0.987 |
| replacement_f1 | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 12.22 |
| severity_downgrade | 0.000 |
| severity_preservation | 1.000 |
| severity_tier_input | 1.000 |
| severity_tier_output | 1.000 |
| smog | 11.21 |
| smog_drop | 0.00 |

annotation backend `novita`, 0 edits kept


### Stage 4 - arm `grounded`

**output:** A mild flare-up of the parathyroid gland's overactivity.

| metric | value |
|---|---:|
| bertscore_f1 | 0.501 |
| coleman_liau | 13.85 |
| coleman_liau_drop | 22.35 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.333 |
| fkgl | 8.18 |
| fkgl_drop | 12.80 |
| fre | 50.7 |
| fre_gain | 100.7 |
| human_edit_recall | 1.000 |
| length_ratio | 2.00 |
| n_words | 10.0 |
| nli_completeness | 0.818 |
| nli_faithfulness | 0.935 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 26.39 |
| severity_downgrade | 0.000 |
| severity_preservation | 1.000 |
| severity_tier_input | 1.000 |
| severity_tier_output | 1.000 |
| smog | 8.84 |
| smog_drop | 2.37 |

annotation backend `novita`, 0 edits kept


==============================================================================

## Note 19 - `248`

**ORIGINAL**  Otherwise, a complete review of systems was obtained and was negative except for as mentioned above.

**REFERENCE** Otherwise, a complete review of systems was obtained and was normal except for as mentioned above.

| | FKGL | FRE | SMOG | Coleman-Liau | words |
|---|---:|---:|---:|---:|---:|
| ORIGINAL | 10.56 | 47.83 | 11.21 | 12.44 | 16 |
| REFERENCE | 9.82 | 53.12 | 8.84 | 11.71 | 16 |

### Stage 2 - extraction + classification

| term | kind | category | action | Zipf | AoA | syll |
|---|---|---|---|---:|---:|---:|
| `review of systems` | phrase | medical_essential | elaborate | 4.79 | 8.84 | 5 |
| `negative` | word | medical_descriptor | replace | 4.79 | 7.47 | 3 |
| `obtained` | word | general_hard_word | replace | 4.49 | None | 2 |

### Stage 3 - retrieval

coverage **1.0** (3/3), glossary budget 4/16

| term | Zipf stratum | defs | sources | matched via | origin |
|---|---|---:|---|---|---|
| `review of systems` | common | 1 | readme_lay_vocab.jsonl | exact | extracted |
| `negative` | common | 2 | wiktionary.json | exact | extracted |
| `obtained` | uncommon | 1 | wiktionary.json | exact | extracted |

Glossary shown to the model:

1. `[wiktionary]` obtained: If you obtain something, you get it.
2. `[readme]` Review of systems: Questions that ask patients about any symptoms they might be experiencing in different parts of their body.
3. `[wiktionary]` negative: If something is negative, it is harmful, sad, or otherwise not good.
4. `[wiktionary]` negative: If a word, sentence, answer, etc. is negative, it uses a word like no, not, never, etc.

### Stage 4 - arm `naive`

**output:** Otherwise, the doctor checked the patient's entire body for other problems, and found nothing except for the issues mentioned above.

| metric | value |
|---|---:|
| bertscore_f1 | 0.373 |
| coleman_liau | 14.33 |
| coleman_liau_drop | -1.89 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.667 |
| fkgl | 12.27 |
| fkgl_drop | -1.71 |
| fre | 42.7 |
| fre_gain | -5.1 |
| human_edit_recall | 1.000 |
| length_ratio | 1.31 |
| n_words | 21.0 |
| nli_completeness | 0.974 |
| nli_faithfulness | 0.143 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.200 |
| sari | 13.45 |
| smog | 11.21 |
| smog_drop | 0.00 |

### Stage 4 - arm `termonly`

**output:** Otherwise, the doctor asked about many body parts and found no problems except as mentioned above.

| metric | value |
|---|---:|
| bertscore_f1 | 0.471 |
| coleman_liau | 11.71 |
| coleman_liau_drop | 0.73 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.667 |
| fkgl | 9.82 |
| fkgl_drop | 0.74 |
| fre | 53.1 |
| fre_gain | 5.3 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 16.0 |
| nli_completeness | 0.876 |
| nli_faithfulness | 0.056 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.200 |
| sari | 14.98 |
| smog | 8.84 |
| smog_drop | 2.37 |

annotation backend `novita`, 0 edits kept


### Stage 4 - arm `grounded`

**output:** Otherwise, the doctor asked about all body symptoms and found no other problems.

| metric | value |
|---|---:|
| bertscore_f1 | 0.224 |
| coleman_liau | 11.37 |
| coleman_liau_drop | 1.07 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.667 |
| fkgl | 8.54 |
| fkgl_drop | 2.02 |
| fre | 57.0 |
| fre_gain | 9.2 |
| human_edit_recall | 1.000 |
| length_ratio | 0.81 |
| n_words | 13.0 |
| nli_completeness | 0.177 |
| nli_faithfulness | 0.041 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 8.02 |
| smog | 8.84 |
| smog_drop | 2.37 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `review of systems` -> `all body symptoms` | replace | attributed | 4.141 | 4.264 | - | 0.959 | 3.198 | - |
| `negative` -> `no other problems` | replace | attributed | 1.507 | 1.595 | - | 0.953 | 0.905 | - |

**edit `review of systems` -> `all body symptoms`**

- status: `attributed`
- log p full -2.1396, empty -6.2804
- masks scored: 18/18 (+4 top-k)
- ranked sources:
    - `+3.426` [readme] Review of systems: Questions that ask patients about any symptoms they might be experiencing in different part
    - `+0.228` [wiktionary] obtained: If you obtain something, you get it.
    - `+0.099` [wiktionary] negative: If a word, sentence, answer, etc. is negative, it uses a word like no, not, never, etc.
    - `-0.095` [wiktionary] negative: If something is negative, it is harmful, sad, or otherwise not good.

- rationale: The original term asks a patient to report on every body system, so "all body symptoms" captures that full physical check in plain language. Phrase frequency rises from 4.79 to 4.43, while age of acquisition drops from 8.84 to 4.28. Patients can now describe their general health without needing to recall specific medical categories.
- audit: coverage 1.0, grounding_error=True, omission=False, source_ok=True, passage_ok=True

**edit `negative` -> `no other problems`**

- status: `attributed`
- log p full -2.2487, empty -3.7554
- masks scored: 18/18 (+4 top-k)
- ranked sources:
    - `+1.210` [wiktionary] negative: If a word, sentence, answer, etc. is negative, it uses a word like no, not, never, etc.
    - `+0.305` [readme] Review of systems: Questions that ask patients about any symptoms they might be experiencing in different part
    - `+0.194` [wiktionary] negative: If something is negative, it is harmful, sad, or otherwise not good.

- rationale: The original term "negative" indicates the absence of a condition, which the replacement "no other problems" expresses in straightforward language. Phrase frequency rises from 4.79 to 5.12, and age of acquisition drops from 7.47 to 5.33. Patients can now clearly see that the test results are clear without needing to interpret a technical label.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

==============================================================================

## Note 20 - `277`

**ORIGINAL**  Symptoms are worse when sitting for any length of time, such as driving a motor vehicle.

**REFERENCE** Symptoms are worse when sitting for any length of time, such as driving a car.

| | FKGL | FRE | SMOG | Coleman-Liau | words |
|---|---:|---:|---:|---:|---:|
| ORIGINAL | 7.61 | 68.98 | 8.84 | 8.09 | 16 |
| REFERENCE | 5.21 | 84.45 | 3.13 | 6.20 | 15 |

### Stage 2 - extraction + classification

| term | kind | category | action | Zipf | AoA | syll |
|---|---|---|---|---:|---:|---:|
| `motor vehicle` | phrase | general_hard_word | replace | 4.33 | 7.42 | 5 |

### Stage 3 - retrieval

coverage **1.0** (1/1), glossary budget 1/16

| term | Zipf stratum | defs | sources | matched via | origin |
|---|---|---:|---|---|---|
| `motor vehicle` | common | 1 | wiktionary.json | exact | extracted |

Glossary shown to the model:

1. `[wiktionary]` motor vehicle: A motor vehicle a road vehicle powered by an internal combustion engine to provide power to rotate the tires.

### Stage 4 - arm `naive`

**output:** The patient feels worse after sitting for a long time, like when driving a car.

| metric | value |
|---|---:|
| bertscore_f1 | 0.602 |
| coleman_liau | 6.59 |
| coleman_liau_drop | 1.50 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 5.21 |
| fkgl_drop | 2.41 |
| fre | 84.5 |
| fre_gain | 15.5 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 15.0 |
| nli_completeness | 0.968 |
| nli_faithfulness | 0.993 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.667 |
| sari | 17.94 |
| severity_preservation | 1.000 |
| smog | 3.13 |
| smog_drop | 5.71 |

### Stage 4 - arm `termonly`

**output:** Symptoms are worse when sitting for any length of time, such as driving a car.

| metric | value |
|---|---:|
| bertscore_f1 | 1.000 |
| coleman_liau | 6.20 |
| coleman_liau_drop | 1.89 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 5.21 |
| fkgl_drop | 2.41 |
| fre | 84.5 |
| fre_gain | 15.5 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 15.0 |
| nli_completeness | 0.978 |
| nli_faithfulness | 0.994 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 100.00 |
| severity_preservation | 1.000 |
| smog | 3.13 |
| smog_drop | 5.71 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `motor vehicle` -> `car` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Symptoms are worse when sitting for any length of time, such as driving a car.

| metric | value |
|---|---:|
| bertscore_f1 | 1.000 |
| coleman_liau | 6.20 |
| coleman_liau_drop | 1.89 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 5.21 |
| fkgl_drop | 2.41 |
| fre | 84.5 |
| fre_gain | 15.5 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 15.0 |
| nli_completeness | 0.978 |
| nli_faithfulness | 0.994 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 100.00 |
| severity_preservation | 1.000 |
| smog | 3.13 |
| smog_drop | 5.71 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `motor vehicle` -> `car` | replace | attributed | 0.035 | 1.418 | - | - | - | - |

**edit `motor vehicle` -> `car`**

- status: `attributed`
- log p full -0.0115, empty -0.0468
- masks scored: 4/4 (+1 top-k)
- ranked sources:
    - `+1.398` [wiktionary] motor vehicle: A motor vehicle a road vehicle powered by an internal combustion engine to provide power to rot

- rationale: The original term refers to any road vehicle used for transport, so "car" captures that general idea in a single, familiar word. Phrase frequency rises from 4.33 to 5.45, while age of acquisition drops from 7.42 to 3.37. Patients can now immediately recognize the type of vehicle involved without needing to recall a broader category.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

==============================================================================

## Note 21 - `290`

**ORIGINAL**  Forearm, elbow and shoulder exams reveal no neurologic compromise.

**REFERENCE** Forearm, elbow and shoulder exams reveal no nerve problems

| | FKGL | FRE | SMOG | Coleman-Liau | words |
|---|---:|---:|---:|---:|---:|
| ORIGINAL | 12.83 | 19.10 | 11.21 | 17.00 | 9 |
| REFERENCE | 7.59 | 56.70 | 3.13 | 12.49 | 9 |

### Stage 2 - extraction + classification

| term | kind | category | action | Zipf | AoA | syll |
|---|---|---|---|---:|---:|---:|
| `neurologic compromise` | phrase | medical_descriptor | replace | 2.55 | 13.85 | 7 |
| `neurologic` | word | medical_descriptor | replace | - | - | - |
| `compromise` | word | medical_descriptor | replace | - | - | - |

### Stage 3 - retrieval

coverage **0.0** (0/1), glossary budget 6/16

| term | Zipf stratum | defs | sources | matched via | origin |
|---|---|---:|---|---|---|
| `neurologic compromise` | rare | 0 | - | - | extracted |
| `neurologic` | rare | 4 | justplainclear.json, nih.json, readme_lay_vocab.jsonl | exact | split_from_uncovered |
| `compromise` | uncommon | 2 | wiktionary.json | exact | split_from_uncovered |

Glossary shown to the model:

1. `[wiktionary]` compromise: A compromise is an agreement in which everyone gets only some of what they wanted.
2. `[readme]` NEUROLOGIC: Having to do with the nerves in the body, brain, or spinal cord.
3. `[wiktionary]` compromise: Compromise is the act making this type of agreement.
4. `[readme]` Neurologic: Having to do with nerves in the body, brain, or spinal cord.
5. `[nih]` neurologic: Having to do with nerves or the nervous system.
6. `[justplainclear]` neurologic: Relating to the nervous system, brain or spinal cord

### Stage 4 - arm `naive`

**output:** Exams of the forearm, elbow, and shoulder show no problems with the nerves.

| metric | value |
|---|---:|
| bertscore_f1 | 0.601 |
| coleman_liau | 8.69 |
| coleman_liau_drop | 8.31 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.333 |
| fkgl | 5.82 |
| fkgl_drop | 7.01 |
| fre | 76.5 |
| fre_gain | 57.4 |
| human_edit_recall | 1.000 |
| length_ratio | 1.44 |
| n_words | 13.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.974 |
| nli_faithfulness | 0.961 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 38.98 |
| smog | 3.13 |
| smog_drop | 8.08 |

### Stage 4 - arm `termonly`

**output:** Forearm, elbow and shoulder exams reveal no nerve damage.

| metric | value |
|---|---:|
| bertscore_f1 | 0.935 |
| coleman_liau | 11.20 |
| coleman_liau_drop | 5.80 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 7.59 |
| fkgl_drop | 5.24 |
| fre | 56.7 |
| fre_gain | 37.6 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 9.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.921 |
| nli_faithfulness | 0.903 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 83.33 |
| smog | 3.13 |
| smog_drop | 8.08 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `neurologic compromise` -> `nerve damage` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Forearm, elbow and shoulder exams reveal no nerve problems.

| metric | value |
|---|---:|
| bertscore_f1 | 0.960 |
| coleman_liau | 12.49 |
| coleman_liau_drop | 4.51 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 7.59 |
| fkgl_drop | 5.24 |
| fre | 56.7 |
| fre_gain | 37.6 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 9.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.949 |
| nli_faithfulness | 0.972 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 100.00 |
| smog | 3.13 |
| smog_drop | 8.08 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `neurologic compromise` -> `nerve problems` | replace | attributed | 0.785 | 1.120 | 0.670 | 0.841 | 0.258 | - |

**edit `neurologic compromise` -> `nerve problems`**

- status: `attributed`
- log p full -0.8601, empty -1.6447
- masks scored: 66/66 (+2 top-k)
- ranked sources:
    - `+0.680` [readme] Neurologic: Having to do with nerves in the body, brain, or spinal cord.
    - `+0.422` [nih] neurologic: Having to do with nerves or the nervous system.
    - `+0.373` [readme] NEUROLOGIC: Having to do with the nerves in the body, brain, or spinal cord.
    - `+0.241` [wiktionary] compromise: Compromise is the act making this type of agreement.
    - `+0.058` [wiktionary] compromise: A compromise is an agreement in which everyone gets only some of what they wanted.

- rationale: The glossary defines neurologic compromise as having to do with nerves in the body, brain, or spinal cord, so "nerve problems" keeps that central meaning in plain language. Phrase frequency increases from 2.55 to 4.15, while age of acquisition falls from 13.85 to 9.67. Patients can now understand the specific issue affecting their nervous system without needing to know the complex medical term.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

==============================================================================

## Note 22 - `296`

**ORIGINAL**  Thereafter, the local anesthesia was injected into the area around the tumor.

**REFERENCE** Thereafter, the numbing agent was injected into the area around the tumor.

| | FKGL | FRE | SMOG | Coleman-Liau | words |
|---|---:|---:|---:|---:|---:|
| ORIGINAL | 13.67 | 18.41 | 14.55 | 12.67 | 12 |
| REFERENCE | 11.71 | 32.50 | 13.02 | 11.22 | 12 |

### Stage 2 - extraction + classification

| term | kind | category | action | Zipf | AoA | syll |
|---|---|---|---|---:|---:|---:|
| `local anesthesia` | phrase | medical_essential | elaborate | 3.39 | 12.53 | 6 |
| `Thereafter` | word | general_hard_word | replace | 3.97 | None | 3 |
| `tumor` | word | medical_essential | elaborate | 3.97 | 10.32 | 2 |

### Stage 3 - retrieval

coverage **1.0** (3/3), glossary budget 11/16

| term | Zipf stratum | defs | sources | matched via | origin |
|---|---|---:|---|---|---|
| `local anesthesia` | rare | 4 | iowa.json, michigan_plmd.json, nih.json, readme_lay_vocab.jsonl | exact | extracted |
| `Thereafter` | uncommon | 2 | dictonary.csv | exact | extracted |
| `tumor` | uncommon | 5 | justplainclear.json, michigan_plmd.json, nih.json, thesarus.json, wiktionary.json | exact | extracted |

Glossary shown to the model:

1. `[dictionary]` Thereafter (adv.): After that; afterward.
2. `[readme]` local anesthesia: A drug that numbs a specific part of your body without affecting the rest.
3. `[nih]` tumor: An abnormal mass of tissue that results when cells divide more than they should or do not die when they should. Tumors may be benign (not cancer), or malignant (cancer). Also called neoplasm.
4. `[dictionary]` Thereafter (adv.): According to that; accordingly.
5. `[nih]` local anesthesia: A temporary loss of feeling in one small area of the body caused by special drugs called anesthetics. The patient stays awake but has no feeling in the area of the body treated with the anesthetic. Local anesthetics may be injected or put on the skin to lessen pain during medical, surgical, or dental procedures. Some are available over-the-counter (without a doctor’s order) and may help lessen local pain, irritation, and itching caused by conditions such as cold sores, sunburn, poison ivy, and minor cuts.
6. `[michigan]` tumor: A growth or lump in your body. It may be cancer, but it also may not be cancer.
7. `[iowa]` LOCAL ANESTHESIA: creation of insensitivity to pain in a small, local area of the body, usually by injection of numbing drugs
8. `[justplainclear]` tumor: Growth or lump
9. `[michigan]` local anesthesia: A drug that causes only in the area of the body where the drug is put, as when a tooth is pulled.
10. `[wiktionary]` tumor: A tumor is an abnormal growth of tissue in a human or animal.
11. `[thesaurus]` tumor: growth, lump

### Stage 4 - arm `naive`

**output:** After that, the doctor injected the local anesthesia into the area around the tumor.

| metric | value |
|---|---:|
| bertscore_f1 | 0.658 |
| coleman_liau | 10.67 |
| coleman_liau_drop | 2.00 |
| copy_jargon_rate | 1.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 12.63 |
| fkgl_drop | 1.05 |
| fre | 29.5 |
| fre_gain | 11.1 |
| human_edit_recall | 0.000 |
| length_ratio | 1.17 |
| n_words | 14.0 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.503 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 37.17 |
| smog | 13.02 |
| smog_drop | 1.53 |

### Stage 4 - arm `termonly`

**output:** After that, the numbing medicine was injected into the area around the growth.

| metric | value |
|---|---:|
| bertscore_f1 | 0.780 |
| coleman_liau | 10.48 |
| coleman_liau_drop | 2.19 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 10.36 |
| fkgl_drop | 3.32 |
| fre | 44.0 |
| fre_gain | 25.6 |
| human_edit_recall | 1.000 |
| length_ratio | 1.08 |
| n_words | 13.0 |
| nli_completeness | 0.810 |
| nli_faithfulness | 0.984 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 56.27 |
| smog | 13.02 |
| smog_drop | 1.53 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `local anesthesia` -> `numbing medicine` | replace | - | - | - | - | - | - | - |
| `tumor` -> `growth` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** After that, the numbing medicine was injected into the area around the lump.

| metric | value |
|---|---:|
| bertscore_f1 | 0.786 |
| coleman_liau | 9.58 |
| coleman_liau_drop | 3.08 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 10.36 |
| fkgl_drop | 3.32 |
| fre | 44.0 |
| fre_gain | 25.6 |
| human_edit_recall | 1.000 |
| length_ratio | 1.08 |
| n_words | 13.0 |
| nli_completeness | 0.249 |
| nli_faithfulness | 0.803 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 56.27 |
| smog | 13.02 |
| smog_drop | 1.53 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `local anesthesia` -> `numbing medicine` | replace | attributed | 0.102 | 0.284 | 0.744 | 0.790 | 0.269 | - |
| `tumor` -> `lump` | replace | attributed | 0.438 | 0.800 | 0.436 | 0.626 | 0.128 | - |

**edit `local anesthesia` -> `numbing medicine`**

- status: `attributed`
- log p full -0.3984, empty -0.5008
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.509` [readme] local anesthesia: A drug that numbs a specific part of your body without affecting the rest.
    - `+0.240` [dictionary] Thereafter (adv.): After that; afterward.
    - `+0.108` [michigan] local anesthesia: A drug that causes only in the area of the body where the drug is put, as when a tooth is pu
    - `+0.063` [nih] tumor: An abnormal mass of tissue that results when cells divide more than they should or do not die when th
    - `+0.021` [wiktionary] tumor: A tumor is an abnormal growth of tissue in a human or animal.

- rationale: The original term refers to a medication that blocks pain signals in a specific area, so "numbing medicine" conveys that same effect using everyday language. Phrase frequency rises from 2.89 to 3.39, while age of acquisition drops from 12.53 to 4.89. Patients can now recognize the treatment as a simple pain reliever without needing to know the technical medical name.
- audit: coverage 1.0, grounding_error=True, omission=False, source_ok=True, passage_ok=True

**edit `tumor` -> `lump`**

- status: `attributed`
- log p full -0.5949, empty -1.0328
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.252` [michigan] tumor: A growth or lump in your body. It may be cancer, but it also may not be cancer.
    - `+0.124` [readme] local anesthesia: A drug that numbs a specific part of your body without affecting the rest.
    - `+0.110` [thesaurus] tumor: growth, lump
    - `+0.056` [michigan] local anesthesia: A drug that causes only in the area of the body where the drug is put, as when a tooth is pu
    - `+0.037` [nih] local anesthesia: A temporary loss of feeling in one small area of the body caused by special drugs called ane

- rationale: The original term refers to an abnormal growth of tissue, so "lump" conveys that physical presence in simpler language. Phrase frequency rises from 3.97 to 3.71, while age of acquisition drops from 10.32 to 5.89. Patients can now recognize the physical sign without needing to know the medical classification.
- audit: coverage 1.0, grounding_error=True, omission=False, source_ok=True, passage_ok=True

==============================================================================

## Note 23 - `307`

**ORIGINAL**  There is no numbness or paresthesias in the hand or arm.

**REFERENCE** There is no numbness or abnormal sensation in the hand or arm.

| | FKGL | FRE | SMOG | Coleman-Liau | words |
|---|---:|---:|---:|---:|---:|
| ORIGINAL | 3.72 | 88.00 | 8.84 | 5.24 | 11 |
| REFERENCE | 5.81 | 74.81 | 11.21 | 5.90 | 12 |

### Stage 2 - extraction + classification

| term | kind | category | action | Zipf | AoA | syll |
|---|---|---|---|---:|---:|---:|
| `paresthesias` | word | medical_descriptor | replace | 1.23 | None | 3 |

### Stage 3 - retrieval

coverage **0.0** (0/1), glossary budget 0/16

| term | Zipf stratum | defs | sources | matched via | origin |
|---|---|---:|---|---|---|
| `paresthesias` | very_rare | 0 | - | - | extracted |

### Stage 4 - arm `naive`

**output:** There is no numbness or tingling in the hand or arm.

| metric | value |
|---|---:|
| bertscore_f1 | 0.839 |
| coleman_liau | 3.13 |
| coleman_liau_drop | 2.11 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 3.72 |
| fkgl_drop | 0.00 |
| fre | 88.0 |
| fre_gain | 0.0 |
| human_edit_recall | 1.000 |
| length_ratio | 0.92 |
| n_words | 11.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.921 |
| nli_faithfulness | 0.953 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 66.67 |
| smog | 8.84 |
| smog_drop | 0.00 |

### Stage 4 - arm `termonly`

**output:** There is no numbness or tingling in the hand or arm.

| metric | value |
|---|---:|
| bertscore_f1 | 0.839 |
| coleman_liau | 3.13 |
| coleman_liau_drop | 2.11 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 3.72 |
| fkgl_drop | 0.00 |
| fre | 88.0 |
| fre_gain | 0.0 |
| human_edit_recall | 1.000 |
| length_ratio | 0.92 |
| n_words | 11.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.921 |
| nli_faithfulness | 0.953 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 66.67 |
| smog | 8.84 |
| smog_drop | 0.00 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `paresthesias` -> `tingling` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** There is no numbness or tingling in the hand or arm.

| metric | value |
|---|---:|
| bertscore_f1 | 0.839 |
| coleman_liau | 3.13 |
| coleman_liau_drop | 2.11 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 3.72 |
| fkgl_drop | 0.00 |
| fre | 88.0 |
| fre_gain | 0.0 |
| human_edit_recall | 1.000 |
| length_ratio | 0.92 |
| n_words | 11.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.921 |
| nli_faithfulness | 0.953 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 66.67 |
| smog | 8.84 |
| smog_drop | 0.00 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `paresthesias` -> `tingling` | replace | - | - | - | - | - | - | - |

==============================================================================

## Note 24 - `357`

**ORIGINAL**  I do not think she has an obvious current abscessed lesion, although there is some drainage.

**REFERENCE** I do not think she has an obvious current collection of pus, although there is some drainage.

| | FKGL | FRE | SMOG | Coleman-Liau | words |
|---|---:|---:|---:|---:|---:|
| ORIGINAL | 7.61 | 68.98 | 8.84 | 9.54 | 16 |
| REFERENCE | 7.70 | 70.14 | 11.21 | 8.05 | 17 |

### Stage 2 - extraction + classification

| term | kind | category | action | Zipf | AoA | syll |
|---|---|---|---|---:|---:|---:|
| `abscessed lesion` | phrase | medical_descriptor | replace | 1.6 | 12.82 | 4 |
| `lesion` | word | medical_descriptor | replace | - | - | - |
| `drainage` | word | medical_descriptor | replace | 3.77 | 10.84 | 2 |

### Stage 3 - retrieval

coverage **0.5** (1/2), glossary budget 9/16

| term | Zipf stratum | defs | sources | matched via | origin |
|---|---|---:|---|---|---|
| `abscessed lesion` | very_rare | 0 | - | - | extracted |
| `lesion` | rare | 6 | iowa.json, justplainclear.json, michigan_plmd.json, nih.json, readme_lay_vocab.jsonl | exact | partial_split_from_uncovered |
| `drainage` | uncommon | 3 | readme_lay_vocab.jsonl, wiktionary.json | exact | extracted |

Glossary shown to the model:

1. `[readme]` drainage: When any fluid is leaking out of a body part.
2. `[readme]` lesion: It's any damage or abnormal change in tissue from disease or injury.
3. `[readme]` DRAINAGE: Fluid leaving an organ or body area.
4. `[readme]` LESION: A lesion is a type of damage or change in tissue caused by disease or injury.
5. `[wiktionary]` drainage: To use a drainage is engage in the action or process of draining something.
6. `[nih]` lesion: An area of abnormal tissue. A lesion may be benign (not cancer) or malignant (cancer).
7. `[iowa]` LESION: wound or injury; a diseased patch of skin
8. `[michigan]` lesion: A sore or any part of your sking that looks different from the rest.
9. `[justplainclear]` lesion: Wound; sore; infected patch of skin

### Stage 4 - arm `naive`

**output:** I do not think she has an obvious abscess right now, although there is some drainage.

| metric | value |
|---|---:|
| bertscore_f1 | 0.766 |
| coleman_liau | 7.00 |
| coleman_liau_drop | 2.54 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 6.14 |
| fkgl_drop | 1.48 |
| fre | 79.6 |
| fre_gain | 10.6 |
| human_edit_recall | 1.000 |
| length_ratio | 0.94 |
| n_words | 16.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.992 |
| nli_faithfulness | 0.994 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 57.08 |
| severity_preservation | 1.000 |
| smog | 8.84 |
| smog_drop | 0.00 |

### Stage 4 - arm `termonly`

**output:** I do not think she has an obvious current pus-filled sore, although there is some fluid coming out.

| metric | value |
|---|---:|
| bertscore_f1 | 0.761 |
| coleman_liau | 8.01 |
| coleman_liau_drop | 1.53 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.667 |
| fkgl | 7.82 |
| fkgl_drop | -0.21 |
| fre | 71.1 |
| fre_gain | 2.1 |
| human_edit_recall | 1.000 |
| length_ratio | 1.12 |
| n_words | 19.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.990 |
| nli_faithfulness | 0.981 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 58.94 |
| severity_preservation | 1.000 |
| smog | 8.84 |
| smog_drop | 0.00 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `abscessed lesion` -> `pus-filled sore` | replace | - | - | - | - | - | - | - |
| `drainage` -> `fluid coming out` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** I do not think she has an obvious current infected sore, although there is some fluid leaking out.

| metric | value |
|---|---:|
| bertscore_f1 | 0.777 |
| coleman_liau | 8.01 |
| coleman_liau_drop | 1.53 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.667 |
| fkgl | 8.47 |
| fkgl_drop | -0.86 |
| fre | 66.4 |
| fre_gain | -2.6 |
| human_edit_recall | 1.000 |
| length_ratio | 1.06 |
| n_words | 18.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.990 |
| nli_faithfulness | 0.993 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 57.08 |
| severity_preservation | 1.000 |
| smog | 11.21 |
| smog_drop | -2.37 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `abscessed lesion` -> `infected sore` | replace | attributed | 1.706 | 1.908 | 0.769 | 0.896 | 0.754 | - |
| `drainage` -> `fluid leaking out` | replace | attributed | 1.290 | 1.749 | 0.828 | 0.894 | 1.610 | - |

**edit `abscessed lesion` -> `infected sore`**

- status: `attributed`
- log p full -1.5376, empty -3.2438
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+1.043` [justplainclear] lesion: Wound; sore; infected patch of skin
    - `+0.289` [michigan] lesion: A sore or any part of your sking that looks different from the rest.
    - `+0.135` [readme] lesion: It's any damage or abnormal change in tissue from disease or injury.
    - `+0.055` [readme] LESION: A lesion is a type of damage or change in tissue caused by disease or injury.

- rationale: The glossary defines an abscessed lesion as a wound or infected patch of skin, so "infected sore" keeps that central idea in plain language. Phrase frequency increases from 1.60 to 3.75, while age of acquisition drops from 12.82 to 5.84. Patients can now recognize the problem as a common skin infection rather than a complex medical term.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `drainage` -> `fluid leaking out`**

- status: `attributed`
- log p full -0.8075, empty -2.0973
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+1.690` [readme] drainage: When any fluid is leaking out of a body part.
    - `+0.080` [iowa] LESION: wound or injury; a diseased patch of skin
    - `+0.035` [readme] DRAINAGE: Fluid leaving an organ or body area.

- rationale: The glossary defines drainage as fluid leaking out of a body part, so the replacement phrase keeps that specific image in plain language. Phrase frequency increases from 3.77 to 3.58, while age of acquisition falls from 10.84 to 7.94. Patients can now visualize the movement of fluid without needing to know the medical term.
- audit: coverage 1.0, grounding_error=True, omission=False, source_ok=True, passage_ok=True

==============================================================================

## Note 25 - `358`

**ORIGINAL**  At this time, we would rehydrate with intravenous fluids and reassess.

**REFERENCE** At this time, we would rehydrate with fluids through the vein and reassess.

| | FKGL | FRE | SMOG | Coleman-Liau | words |
|---|---:|---:|---:|---:|---:|
| ORIGINAL | 9.08 | 49.54 | 13.02 | 12.09 | 11 |
| REFERENCE | 5.82 | 76.50 | 11.21 | 9.14 | 13 |

### Stage 2 - extraction + classification

| term | kind | category | action | Zipf | AoA | syll |
|---|---|---|---|---:|---:|---:|
| `intravenous fluids` | phrase | medical_essential | elaborate | 3.03 | 15.29 | 6 |
| `rehydrate` | word | general_hard_word | replace | 2.2 | 13.63 | 3 |
| `reassess` | word | general_hard_word | replace | 2.8 | 12.79 | 3 |

### Stage 3 - retrieval

coverage **1.0** (3/3), glossary budget 3/16

| term | Zipf stratum | defs | sources | matched via | origin |
|---|---|---:|---|---|---|
| `intravenous fluids` | rare | 1 | readme_lay_vocab.jsonl | intravenous fluid | extracted |
| `rehydrate` | very_rare | 1 | wiktionary.json | exact | extracted |
| `reassess` | rare | 1 | wiktionary.json | exact | extracted |

Glossary shown to the model:

1. `[readme]` intravenous fluid: Fluids that go straight into a vein through a needle.
2. `[wiktionary]` rehydrate: If you rehydrate something, you supply it with water to make it moist or wet again.
3. `[wiktionary]` reassess: If you reassess a person, idea, skill, process, etc., you judge or measure them again.

### Stage 4 - arm `naive`

**output:** At this time, we would give fluids through an IV and check again.

| metric | value |
|---|---:|
| bertscore_f1 | 0.645 |
| coleman_liau | 4.68 |
| coleman_liau_drop | 7.41 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 3.10 |
| fkgl_drop | 5.99 |
| fre | 96.0 |
| fre_gain | 46.5 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 13.0 |
| nli_completeness | 0.860 |
| nli_faithfulness | 0.993 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 45.22 |
| smog | 3.13 |
| smog_drop | 9.89 |

### Stage 4 - arm `termonly`

**output:** At this time, we would give fluids by vein and check again.

| metric | value |
|---|---:|
| bertscore_f1 | 0.705 |
| coleman_liau | 3.97 |
| coleman_liau_drop | 8.12 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 2.86 |
| fkgl_drop | 6.23 |
| fre | 96.0 |
| fre_gain | 46.4 |
| human_edit_recall | 1.000 |
| length_ratio | 0.92 |
| n_words | 12.0 |
| nli_completeness | 0.696 |
| nli_faithfulness | 0.944 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 45.56 |
| smog | 3.13 |
| smog_drop | 9.89 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `rehydrate` -> `give fluids by vein` | replace | - | - | - | - | - | - | - |
| `reassess` -> `check again` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** At this time, we would give fluids by vein and check again.

| metric | value |
|---|---:|
| bertscore_f1 | 0.705 |
| coleman_liau | 3.97 |
| coleman_liau_drop | 8.12 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 2.86 |
| fkgl_drop | 6.23 |
| fre | 96.0 |
| fre_gain | 46.4 |
| human_edit_recall | 1.000 |
| length_ratio | 0.92 |
| n_words | 12.0 |
| nli_completeness | 0.696 |
| nli_faithfulness | 0.944 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 45.56 |
| smog | 3.13 |
| smog_drop | 9.89 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `rehydrate` -> `give fluids by vein` | replace | attributed | 0.100 | 0.156 | - | 0.830 | 0.257 | - |
| `reassess` -> `check again` | replace | attributed | -0.273 | -0.809 | - | 0.952 | 0.283 | - |

**edit `rehydrate` -> `give fluids by vein`**

- status: `attributed`
- log p full -0.9690, empty -1.0686
- masks scored: 10/10 (+3 top-k)
- ranked sources:
    - `+0.257` [readme] intravenous fluid: Fluids that go straight into a vein through a needle.
    - `-0.167` [wiktionary] rehydrate: If you rehydrate something, you supply it with water to make it moist or wet again.

- rationale: The original term means to restore the body's water levels, so "give fluids by vein" describes the specific medical action of delivering liquid directly into the bloodstream. Phrase frequency increases from 2.20 to 3.45, while age of acquisition drops from 13.63 to 8.53. Patients can now clearly see that the treatment involves a direct injection of liquid rather than just drinking water.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `reassess` -> `check again`**

- status: `attributed`
- log p full -0.5623, empty -0.2897
- masks scored: 10/10 (+3 top-k)
- ranked sources:
    - `+0.267` [wiktionary] rehydrate: If you rehydrate something, you supply it with water to make it moist or wet again.
    - `-0.016` [readme] intravenous fluid: Fluids that go straight into a vein through a needle.
    - `-1.192` [wiktionary] reassess: If you reassess a person, idea, skill, process, etc., you judge or measure them again.

- rationale: The original term means to evaluate a situation once more, so "check again" keeps that core idea of repeating an assessment in plain words. Phrase frequency rises from 2.80 to 5.16, while age of acquisition drops from 12.79 to 5.78. You can now grasp the need for a second look without needing to know the specific medical verb.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

==============================================================================

## Note 26 - `380`

**ORIGINAL**  Findings are compatible with acute appendicitis.

**REFERENCE** Findings are compatible with acute inflammation of the appendix

| | FKGL | FRE | SMOG | Coleman-Liau | words |
|---|---:|---:|---:|---:|---:|
| ORIGINAL | 14.28 | 3.34 | 11.21 | 19.87 | 6 |
| REFERENCE | 12.83 | 19.10 | 13.02 | 16.36 | 9 |

### Stage 2 - extraction + classification

| term | kind | category | action | Zipf | AoA | syll |
|---|---|---|---|---:|---:|---:|
| `acute appendicitis` | phrase | medical_essential | elaborate | 2.74 | 12.0 | 6 |
| `acute` | word | medical_descriptor | replace | - | - | - |
| `appendicitis` | word | medical_essential | elaborate | - | - | - |
| `compatible with` | phrase | general_hard_word | replace | 3.97 | 10.16 | 5 |
| `compatible` | word | medical_descriptor | replace | - | - | - |
| `with` | word | medical_descriptor | replace | - | - | - |
| `Findings` | word | general_hard_word | replace | 4.38 | None | 2 |

### Stage 3 - retrieval

coverage **0.3333** (1/3), glossary budget 11/16

| term | Zipf stratum | defs | sources | matched via | origin |
|---|---|---:|---|---|---|
| `acute appendicitis` | rare | 0 | - | - | extracted |
| `acute` | uncommon | 6 | iowa.json, justplainclear.json, michigan_plmd.json, nih.json, thesarus.json, wiktionary.json | exact | split_from_uncovered |
| `appendicitis` | rare | 1 | readme_lay_vocab.jsonl | exact | split_from_uncovered |
| `compatible with` | uncommon | 0 | - | - | extracted |
| `compatible` | uncommon | 1 | wiktionary.json | exact | split_from_uncovered |
| `with` | common | 2 | wiktionary.json | exact | split_from_uncovered |
| `Findings` | uncommon | 1 | wiktionary.json | exact | extracted |

Glossary shown to the model:

1. `[wiktionary]` findings: A finding is the information from a research or an investigation.
2. `[readme]` appendicitis: Appendicitis is when your appendix gets swollen and inflamed, typically causing stomach pain.
3. `[wiktionary]` compatible: Things or people are compatible when they can work and communicate with each other without problems
4. `[wiktionary]` with: With is used to show the other people or things present when something happened.
5. `[nih]` acute: Symptoms or signs that begin and worsen quickly; not chronic.
6. `[wiktionary]` with: With is used to describe something added to something else.
7. `[iowa]` ACUTE: new, recent, sudden, urgent
8. `[michigan]` acute: An illness or symptom that begins suddenly or lasts a short time. It can also be an intense flare-up of an illness.
9. `[justplainclear]` acute: Sudden start, doesn't last long
10. `[wiktionary]` acute: If an angle is acute, it is less than 90 degrees in size.
11. `[thesaurus]` acute: sudden start, short term, quick

### Stage 4 - arm `naive`

**output:** The test results match what is expected for acute appendicitis.

| metric | value |
|---|---:|
| bertscore_f1 | 0.436 |
| coleman_liau | 11.98 |
| coleman_liau_drop | 7.89 |
| copy_jargon_rate | 1.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 8.37 |
| fkgl_drop | 5.91 |
| fre | 52.9 |
| fre_gain | 49.5 |
| human_edit_recall | 0.000 |
| length_ratio | 1.11 |
| n_words | 10.0 |
| nli_completeness | 0.989 |
| nli_faithfulness | 0.968 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 8.63 |
| smog | 11.21 |
| smog_drop | 0.00 |
| temporality_preservation | 1.000 |
| uncertainty_preservation | 0.000 |

### Stage 4 - arm `termonly`

**output:** The signs show a sudden attack of appendix inflammation.

| metric | value |
|---|---:|
| bertscore_f1 | 0.445 |
| coleman_liau | 11.20 |
| coleman_liau_drop | 8.67 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.429 |
| fkgl | 8.90 |
| fkgl_drop | 5.39 |
| fre | 47.3 |
| fre_gain | 44.0 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 9.0 |
| nli_completeness | 0.846 |
| nli_faithfulness | 0.462 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 13.04 |
| smog | 11.21 |
| smog_drop | 0.00 |
| temporality_preservation | 0.000 |
| uncertainty_preservation | 0.000 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `acute appendicitis` -> `sudden attack of appendix inflammation` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** The test results show a sudden flare-up of swollen appendix.

| metric | value |
|---|---:|
| bertscore_f1 | 0.415 |
| coleman_liau | 9.66 |
| coleman_liau_drop | 10.21 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.429 |
| fkgl | 7.19 |
| fkgl_drop | 7.09 |
| fre | 61.3 |
| fre_gain | 58.0 |
| human_edit_recall | 1.000 |
| length_ratio | 1.22 |
| n_words | 11.0 |
| nli_completeness | 0.774 |
| nli_faithfulness | 0.488 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 11.25 |
| smog | 8.84 |
| smog_drop | 2.37 |
| temporality_preservation | 0.000 |
| uncertainty_preservation | 0.000 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `compatible with` -> `show` | replace | attributed | 0.051 | 0.076 | 0.738 | 0.900 | 0.026 | - |
| `acute` -> `sudden` | replace | attributed | 0.992 | 2.284 | 0.627 | 0.845 | 0.147 | - |
| `appendicitis` -> `flare-up of swollen appendix` | replace | attributed | 3.066 | 3.136 | 0.939 | 0.968 | 2.234 | - |

**edit `compatible with` -> `show`**

- status: `attributed`
- log p full -1.0635, empty -1.1142
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+0.141` [michigan] acute: An illness or symptom that begins suddenly or lasts a short time. It can also be an intense flare-up of
    - `+0.115` [nih] acute: Symptoms or signs that begin and worsen quickly; not chronic.
    - `+0.043` [wiktionary] with: With is used to show the other people or things present when something happened.
    - `+0.042` [thesaurus] acute: sudden start, short term, quick
    - `+0.020` [wiktionary] with: With is used to describe something added to something else.

- rationale: The original phrase "compatible with" implies that a test result aligns with a specific condition, so "show" conveys that the evidence points directly to that diagnosis. Phrase frequency rises from Zipf 3.97 to 5.68, while age of acquisition drops from 10.16 to 6.21. Patients can now see the clear link between the test and the condition without getting lost in abstract phrasing.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `acute` -> `sudden`**

- status: `attributed`
- log p full -0.2140, empty -1.2063
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+0.450` [justplainclear] acute: Sudden start, doesn't last long
    - `+0.303` [thesaurus] acute: sudden start, short term, quick
    - `+0.243` [michigan] acute: An illness or symptom that begins suddenly or lasts a short time. It can also be an intense flare-up of
    - `+0.238` [wiktionary] compatible: Things or people are compatible when they can work and communicate with each other without problem
    - `+0.093` [wiktionary] with: With is used to show the other people or things present when something happened.

- rationale: The glossary defines acute as a sudden start that does not last long, so "sudden" keeps that quick onset in plain words. Phrase frequency increases from 4.00 to 4.40, while age of acquisition drops from 11.60 to 6.67. You can now recognize the rapid nature of the symptom without needing to know the medical label.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `appendicitis` -> `flare-up of swollen appendix`**

- status: `attributed`
- log p full -2.6534, empty -5.7198
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+2.553` [readme] appendicitis: Appendicitis is when your appendix gets swollen and inflamed, typically causing stomach pain.
    - `+0.319` [michigan] acute: An illness or symptom that begins suddenly or lasts a short time. It can also be an intense flare-up of
    - `+0.192` [wiktionary] acute: If an angle is acute, it is less than 90 degrees in size.
    - `+0.164` [nih] acute: Symptoms or signs that begin and worsen quickly; not chronic.
    - `+0.039` [wiktionary] compatible: Things or people are compatible when they can work and communicate with each other without problem

- rationale: The glossary defines appendicitis as a condition where the appendix becomes swollen and inflamed, so "flare-up of swollen appendix" keeps that core physical change in plain language. Phrase frequency increases from 2.76 to 3.09, while age of acquisition drops from 12.00 to 10.56. Patients can now grasp the specific nature of the abdominal pain without needing to know the medical diagnosis.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

==============================================================================

## Note 27 - `391`

**ORIGINAL**  She denies weight loss, but acknowledged decreased appetite and increased generalized fatigue for the past 3-4 months.

**REFERENCE** She denies weight loss, but acknowledged reduced appetite and more generalized tiredness for the past 3-4 months.

| | FKGL | FRE | SMOG | Coleman-Liau | words |
|---|---:|---:|---:|---:|---:|
| ORIGINAL | 10.48 | 50.24 | 13.02 | 16.24 | 18 |
| REFERENCE | 10.48 | 50.24 | 14.55 | 14.53 | 18 |

### Stage 2 - extraction + classification

| term | kind | category | action | Zipf | AoA | syll |
|---|---|---|---|---:|---:|---:|
| `generalized fatigue` | phrase | medical_descriptor | replace | 3.29 | 11.83 | 6 |
| `generalized` | word | medical_descriptor | replace | - | - | - |
| `fatigue` | word | medical_descriptor | replace | - | - | - |
| `decreased appetite` | phrase | medical_descriptor | replace | 3.63 | 8.83 | 5 |
| `decreased` | word | medical_descriptor | replace | - | - | - |
| `appetite` | word | medical_descriptor | replace | - | - | - |
| `acknowledged` | word | general_hard_word | replace | 4.08 | None | 3 |
| `denies` | word | general_hard_word | replace | 3.73 | None | 2 |

### Stage 3 - retrieval

coverage **0.5** (2/4), glossary budget 15/16

| term | Zipf stratum | defs | sources | matched via | origin |
|---|---|---:|---|---|---|
| `generalized fatigue` | rare | 0 | - | - | extracted |
| `generalized` | rare | 3 | readme_lay_vocab.jsonl, wiktionary.json | exact | split_from_uncovered |
| `fatigue` | uncommon | 6 | justplainclear.json, michigan_plmd.json, nih.json, readme_lay_vocab.jsonl, wiktionary.json | exact | split_from_uncovered |
| `decreased appetite` | uncommon | 0 | - | - | extracted |
| `decreased` | uncommon | 1 | wiktionary.json | exact | split_from_uncovered |
| `appetite` | uncommon | 3 | nih.json, readme_lay_vocab.jsonl, wiktionary.json | exact | split_from_uncovered |
| `acknowledged` | uncommon | 1 | wiktionary.json | exact | extracted |
| `denies` | uncommon | 1 | wiktionary.json | exact | extracted |

Glossary shown to the model:

1. `[wiktionary]` decreased: If something decreases, it goes down in number or value.
2. `[wiktionary]` denies: If you deny something, you say it didn't happen or isn't true.
3. `[wiktionary]` acknowledged: If you acknowledge a fact or a situation, you accept or admit that it is true or that it exists.
4. `[readme]` appetite: Wanting to eat food.
5. `[readme]` Generalized: Generalized means not focusing on one specific area.
6. `[readme]` fatigue: Feeling exhausted and lacking energy.
7. `[nih]` appetite: A desire to satisfy a physical or mental need, such as for food, sex, or adventure.
8. `[readme]` generalized: Not specific, covers a broad range.
9. `[nih]` fatigue: A condition marked by extreme tiredness and inability to function due to lack of energy. Fatigue may be acute or chronic.
10. `[wiktionary]` appetite: When you have appetite, you feel hungry and would like to eat some food.
11. `[wiktionary]` generalized: When you generalize you speak in general, or in vague terms.
12. `[michigan]` fatigue: tired, weak feeling of the whole body, feeling tired all over
13. `[justplainclear]` fatigue: Tired, weak feeling of the whole body, feeling tired
14. `[wiktionary]` fatigue: Fatigue is the extreme tiredness which is the result of having mental or physical exertion or illness.
15. `[wiktionary]` fatigue: Fatigue is the material failure, such as cracking or separation, caused by stress on the material.

### Stage 4 - arm `naive`

**output:** She says she has not lost weight, but she admitted she has had less of an appetite and more tiredness all over her body for the last 3-4 months.

| metric | value |
|---|---:|
| bertscore_f1 | 0.648 |
| coleman_liau | 5.78 |
| coleman_liau_drop | 10.46 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.286 |
| fkgl | 10.78 |
| fkgl_drop | -0.30 |
| fre | 69.5 |
| fre_gain | 19.2 |
| human_edit_recall | 1.000 |
| length_ratio | 1.67 |
| n_words | 30.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.995 |
| nli_faithfulness | 0.995 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.250 |
| sari | 32.16 |
| smog | 13.02 |
| smog_drop | 0.00 |
| temporality_preservation | 0.000 |

### Stage 4 - arm `termonly`

**output:** She says she has not lost weight, but admitted feeling very tired and not wanting to eat for the past 3-4 months.

| metric | value |
|---|---:|
| bertscore_f1 | 0.640 |
| coleman_liau | 6.32 |
| coleman_liau_drop | 9.92 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.375 |
| fkgl | 8.01 |
| fkgl_drop | 2.47 |
| fre | 76.8 |
| fre_gain | 26.6 |
| human_edit_recall | 1.000 |
| length_ratio | 1.28 |
| n_words | 23.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.992 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.125 |
| sari | 42.08 |
| smog | 8.84 |
| smog_drop | 4.18 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `acknowledged` -> `admitted` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** She says she did not lose weight, but admitted feeling tired all over and wanting less food for the past 3-4 months.

| metric | value |
|---|---:|
| bertscore_f1 | 0.620 |
| coleman_liau | 7.11 |
| coleman_liau_drop | 9.13 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.375 |
| fkgl | 8.01 |
| fkgl_drop | 2.47 |
| fre | 76.8 |
| fre_gain | 26.6 |
| human_edit_recall | 1.000 |
| length_ratio | 1.28 |
| n_words | 23.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.992 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.125 |
| sari | 42.08 |
| smog | 8.84 |
| smog_drop | 4.18 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `acknowledged` -> `admitted` | replace | attributed | 0.134 | 0.778 | 0.831 | 0.972 | 0.556 | - |
| `generalized fatigue` -> `feeling tired all over` | replace | attributed | 0.665 | 0.781 | 0.898 | 0.952 | 2.338 | - |
| `decreased appetite` -> `wanting less food` | replace | attributed | 3.727 | 4.092 | 0.823 | 0.938 | 1.111 | - |

**edit `acknowledged` -> `admitted`**

- status: `attributed`
- log p full -0.1296, empty -0.2633
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+0.795` [wiktionary] acknowledged: If you acknowledge a fact or a situation, you accept or admit that it is true or that it exists.
    - `+0.239` [wiktionary] denies: If you deny something, you say it didn't happen or isn't true.
    - `+0.040` [wiktionary] generalized: When you generalize you speak in general, or in vague terms.
    - `+0.011` [nih] fatigue: A condition marked by extreme tiredness and inability to function due to lack of energy. Fatigue may 

- rationale: The original term "acknowledged" means to admit or accept something as true, and "admitted" conveys that same act of acceptance in simpler language. Phrase frequency increases from 4.08 to 4.49, while syllable count remains steady at 3. Patients can now recognize the admission of fact without needing to process the more formal verb.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `generalized fatigue` -> `feeling tired all over`**

- status: `attributed`
- log p full -1.6056, empty -2.2710
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+2.758` [michigan] fatigue: tired, weak feeling of the whole body, feeling tired all over
    - `+0.420` [justplainclear] fatigue: Tired, weak feeling of the whole body, feeling tired
    - `+0.374` [readme] Generalized: Generalized means not focusing on one specific area.
    - `+0.292` [readme] fatigue: Feeling exhausted and lacking energy.
    - `+0.172` [wiktionary] fatigue: Fatigue is the material failure, such as cracking or separation, caused by stress on the material.

- rationale: The original term describes a widespread sense of exhaustion affecting the whole body, so "feeling tired all over" conveys that same physical state in everyday language. Phrase frequency rises from Zipf 3.29 to 4.55, while age of acquisition drops from 11.83 to 5.57. Patients can now grasp the extent of their weariness without needing to recall a specific medical label.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `decreased appetite` -> `wanting less food`**

- status: `attributed`
- log p full -1.1663, empty -4.8930
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+2.109` [readme] appetite: Wanting to eat food.
    - `+0.998` [nih] appetite: A desire to satisfy a physical or mental need, such as for food, sex, or adventure.
    - `+0.351` [wiktionary] decreased: If something decreases, it goes down in number or value.
    - `+0.340` [readme] fatigue: Feeling exhausted and lacking energy.
    - `+0.332` [nih] fatigue: A condition marked by extreme tiredness and inability to function due to lack of energy. Fatigue may 

- rationale: The glossary defines the original phrase as wanting to eat food, so "wanting less food" keeps that core idea in plain language. Phrase frequency increases from 3.63 to 4.40, while age of acquisition drops from 8.83 to 3.25. Patients can now grasp the symptom of reduced hunger without needing to know the medical phrasing.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

==============================================================================

## Note 28 - `392`

**ORIGINAL**  Consideration given to completion thyroidectomy.

**REFERENCE** Consideration given to remove remaining parts of the thyroid

| | FKGL | FRE | SMOG | Coleman-Liau | words |
|---|---:|---:|---:|---:|---:|
| ORIGINAL | 21.76 | -52.04 | 13.02 | 28.16 | 5 |
| REFERENCE | 11.52 | 28.50 | 11.21 | 14.42 | 9 |

### Stage 2 - extraction + classification

| term | kind | category | action | Zipf | AoA | syll |
|---|---|---|---|---:|---:|---:|
| `completion thyroidectomy` | phrase | medical_essential | elaborate | 1.69 | 8.56 | 7 |
| `completion` | word | medical_descriptor | replace | - | - | - |
| `thyroidectomy` | word | medical_essential | elaborate | - | - | - |
| `Consideration given to` | phrase | general_hard_word | replace | 4.25 | 9.5 | 8 |
| `Consideration` | word | medical_descriptor | replace | - | - | - |
| `given` | word | medical_descriptor | replace | - | - | - |
| `to` | word | medical_descriptor | replace | - | - | - |

### Stage 3 - retrieval

coverage **0.0** (0/2), glossary budget 11/16

| term | Zipf stratum | defs | sources | matched via | origin |
|---|---|---:|---|---|---|
| `completion thyroidectomy` | very_rare | 0 | - | - | extracted |
| `completion` | uncommon | 2 | thesarus.json, wiktionary.json | exact | split_from_uncovered |
| `thyroidectomy` | very_rare | 3 | nih.json, readme_lay_vocab.jsonl | exact | split_from_uncovered |
| `Consideration given to` | uncommon | 0 | - | - | extracted |
| `Consideration` | uncommon | 2 | wiktionary.json | exact | split_from_uncovered |
| `given` | common | 2 | wiktionary.json | exact | split_from_uncovered |
| `to` | common | 2 | wiktionary.json | exact | split_from_uncovered |

Glossary shown to the model:

1. `[wiktionary]` completion: Completion is the action from the verb complete.
2. `[wiktionary]` given: If you give something to someone else, you had the thing and you let the other person have it. Maybe you use your hands to put the thing in the other person's hands. Usually after that, the thing is the other person's thing.
3. `[wiktionary]` to: To has no meaning. It is used with a bare infinitival clause.
4. `[wiktionary]` consideration: Consideration is the process of thinking carefully about something.
5. `[readme]` thyroidectomy: Surgery to remove the thyroid gland.
6. `[thesaurus]` completion: end, finish
7. `[wiktionary]` given: Given x means if x is true, happened, exists, etc.
8. `[wiktionary]` to: To shows where something goes, the goal of movement.
9. `[wiktionary]` consideration: Consideration can also be a thoughtful and caring attitude towards others.
10. `[readme]` Thyroidectomy: A thyroidectomy is surgery to take out the thyroid gland.
11. `[nih]` thyroidectomy: Surgery to remove part or all of the thyroid.

### Stage 4 - arm `naive`

**output:** The doctors are thinking about finishing the thyroid removal.

| metric | value |
|---|---:|
| bertscore_f1 | 0.330 |
| coleman_liau | 14.42 |
| coleman_liau_drop | 13.74 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.286 |
| fkgl | 10.21 |
| fkgl_drop | 11.55 |
| fre | 37.9 |
| fre_gain | 89.9 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 9.0 |
| nli_completeness | 0.985 |
| nli_faithfulness | 0.614 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 24.96 |
| smog | 11.21 |
| smog_drop | 1.82 |
| uncertainty_preservation | 0.000 |

### Stage 4 - arm `termonly`

**output:** The doctors thought about finishing the removal of the thyroid gland.

| metric | value |
|---|---:|
| bertscore_f1 | 0.359 |
| coleman_liau | 12.09 |
| coleman_liau_drop | 16.07 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.286 |
| fkgl | 8.01 |
| fkgl_drop | 13.75 |
| fre | 57.2 |
| fre_gain | 109.3 |
| human_edit_recall | 1.000 |
| length_ratio | 1.22 |
| n_words | 11.0 |
| nli_completeness | 0.990 |
| nli_faithfulness | 0.483 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 27.92 |
| smog | 11.21 |
| smog_drop | 1.82 |
| uncertainty_preservation | 0.000 |

annotation backend `novita`, 0 edits kept


### Stage 4 - arm `grounded`

**output:** The doctors thought about finishing the surgery to remove the thyroid gland.

| metric | value |
|---|---:|
| bertscore_f1 | 0.337 |
| coleman_liau | 12.67 |
| coleman_liau_drop | 15.49 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.333 |
| fkgl | 8.76 |
| fkgl_drop | 13.00 |
| fre | 53.7 |
| fre_gain | 105.7 |
| human_edit_recall | 1.000 |
| length_ratio | 1.33 |
| n_words | 12.0 |
| nli_completeness | 0.990 |
| nli_faithfulness | 0.422 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 31.68 |
| smog | 11.21 |
| smog_drop | 1.82 |
| uncertainty_preservation | 0.000 |

annotation backend `novita`, 0 edits kept


==============================================================================

## Note 29 - `394`

**ORIGINAL**  She notes that she had epistaxis a few days ago, requiring nasal packing and fortunately that had resolved now.

**REFERENCE** She notes that she had a nose bleed a few days ago, requiring nose packing and fortunately that had resolved now.

| | FKGL | FRE | SMOG | Coleman-Liau | words |
|---|---:|---:|---:|---:|---:|
| ORIGINAL | 10.45 | 53.97 | 11.21 | 10.42 | 19 |
| REFERENCE | 9.46 | 64.66 | 11.21 | 7.92 | 21 |

### Stage 2 - extraction + classification

| term | kind | category | action | Zipf | AoA | syll |
|---|---|---|---|---:|---:|---:|
| `nasal packing` | phrase | medical_essential | elaborate | 3.39 | 8.75 | 4 |
| `nasal` | word | medical_descriptor | replace | - | - | - |
| `packing` | word | medical_descriptor | replace | - | - | - |
| `epistaxis` | word | medical_descriptor | replace | 1.6 | None | 2 |
| `requiring` | word | general_hard_word | replace | 4.14 | None | 4 |
| `resolved` | word | general_hard_word | replace | 4.1 | None | 2 |

### Stage 3 - retrieval

coverage **0.75** (3/4), glossary budget 14/16

| term | Zipf stratum | defs | sources | matched via | origin |
|---|---|---:|---|---|---|
| `nasal packing` | rare | 0 | - | - | extracted |
| `nasal` | rare | 5 | justplainclear.json, michigan_plmd.json, nih.json, readme_lay_vocab.jsonl | exact | split_from_uncovered |
| `packing` | uncommon | 3 | readme_lay_vocab.jsonl, wiktionary.json | exact | split_from_uncovered |
| `epistaxis` | very_rare | 3 | readme_lay_vocab.jsonl, wiktionary.json | exact | extracted |
| `requiring` | uncommon | 1 | wiktionary.json | exact | extracted |
| `resolved` | uncommon | 2 | wiktionary.json | exact | extracted |

Glossary shown to the model:

1. `[wiktionary]` requiring: If you require something, you need it.
2. `[wiktionary]` resolved: To resolve means to create a solution for a problem.
3. `[readme]` EPISTAXIS: EPISTAXIS: It's a nosebleed.
4. `[readme]` packing: Putting something into a wound to help it heal.
5. `[readme]` nasal: It's all about your nose when we talk about "nasal."
6. `[wiktionary]` resolved: When a problem is resolved, it has been brought to a successful solution.
7. `[readme]` Epistaxis: A nosebleed.
8. `[wiktionary]` packing: When you pack something, you put it in a container to carry with you.
9. `[readme]` Nasal: Nasal means having to do with the nose.
10. `[wiktionary]` epistaxis: Epistaxis is bleeding from the nose.
11. `[wiktionary]` packing: You put packing around an object to protect it.
12. `[nih]` nasal: By or having to do with the nose.
13. `[michigan]` nasal: Things that are related to the nose.
14. `[justplainclear]` nasal: Relating to your nose

### Stage 4 - arm `naive`

**output:** She says she had a nosebleed a few days ago that needed packing in her nose, but it is now gone.

| metric | value |
|---|---:|
| bertscore_f1 | 0.653 |
| coleman_liau | 3.23 |
| coleman_liau_drop | 7.19 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.400 |
| fkgl | 6.65 |
| fkgl_drop | 3.80 |
| fre | 84.8 |
| fre_gain | 30.8 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 21.0 |
| nli_completeness | 0.833 |
| nli_faithfulness | 0.954 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 30.14 |
| smog | 3.13 |
| smog_drop | 8.08 |
| temporality_preservation | 1.000 |

### Stage 4 - arm `termonly`

**output:** She had a nosebleed a few days ago, needed a cloth to stop it, and it is now stopped.

| metric | value |
|---|---:|
| bertscore_f1 | 0.546 |
| coleman_liau | 2.18 |
| coleman_liau_drop | 8.24 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.167 |
| fkgl | 5.48 |
| fkgl_drop | 4.97 |
| fre | 89.6 |
| fre_gain | 35.6 |
| human_edit_recall | 1.000 |
| length_ratio | 0.90 |
| n_words | 19.0 |
| nli_completeness | 0.847 |
| nli_faithfulness | 0.897 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.286 |
| sari | 27.49 |
| smog | 3.13 |
| smog_drop | 8.08 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `epistaxis` -> `nosebleed` | replace | - | - | - | - | - | - | - |
| `nasal packing` -> `a cloth to stop it` | replace | - | - | - | - | - | - | - |
| `resolved` -> `stopped` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** She had a nosebleed a few days ago, needed help with her nose to stop it, and it is now stopped.

| metric | value |
|---|---:|
| bertscore_f1 | 0.552 |
| coleman_liau | 2.95 |
| coleman_liau_drop | 7.47 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 6.09 |
| fkgl_drop | 4.37 |
| fre | 88.8 |
| fre_gain | 34.9 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 21.0 |
| nli_completeness | 0.733 |
| nli_faithfulness | 0.848 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.286 |
| sari | 28.63 |
| smog | 3.13 |
| smog_drop | 8.08 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `epistaxis` -> `nosebleed` | replace | attributed | 0.255 | 2.083 | 0.614 | 0.627 | 0.057 | - |
| `nasal packing` -> `help with her nose to stop it` | replace | attributed | 3.902 | 3.906 | 0.378 | 0.853 | 0.401 | - |
| `resolved` -> `stopped` | replace | attributed | -0.311 | -0.431 | 0.737 | 0.872 | 0.060 | - |

**edit `epistaxis` -> `nosebleed`**

- status: `attributed`
- log p full -0.0421, empty -0.2969
- masks scored: 66/66 (+5 top-k)
- ranked sources:
    - `+1.951` [readme] Epistaxis: A nosebleed.
    - `+1.893` [readme] EPISTAXIS: EPISTAXIS: It's a nosebleed.
    - `+0.751` [wiktionary] resolved: When a problem is resolved, it has been brought to a successful solution.
    - `+0.365` [wiktionary] packing: When you pack something, you put it in a container to carry with you.
    - `+0.093` [wiktionary] requiring: If you require something, you need it.

- rationale: The original term refers to bleeding from the nose, so "nosebleed" conveys that same physical symptom in everyday language. Phrase frequency rises from Zipf 1.60 to 2.51, while age of acquisition drops from 14.6 to 9.2. Patients can now recognize the symptom immediately without needing to know the medical jargon.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `nasal packing` -> `help with her nose to stop it`**

- status: `attributed`
- log p full -5.6123, empty -9.5147
- masks scored: 66/66 (+5 top-k)
- ranked sources:
    - `+0.837` [readme] nasal: It's all about your nose when we talk about "nasal."
    - `+0.436` [readme] packing: Putting something into a wound to help it heal.
    - `+0.322` [readme] Nasal: Nasal means having to do with the nose.
    - `+0.138` [wiktionary] packing: You put packing around an object to protect it.
    - `+0.077` [wiktionary] epistaxis: Epistaxis is bleeding from the nose.

- rationale: The original term refers to placing material inside the nose to control bleeding, so the replacement describes the action of helping with the nose to stop it. Phrase frequency increases from 3.39 to 4.44, while age of acquisition drops from 8.75 to 5.09. Patients can now grasp the immediate physical intervention without needing to know the specific medical procedure.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `resolved` -> `stopped`**

- status: `attributed`
- log p full -1.4374, empty -1.1268
- masks scored: 66/66 (+5 top-k)
- ranked sources:
    - `+0.203` [readme] Epistaxis: A nosebleed.
    - `+0.142` [wiktionary] packing: When you pack something, you put it in a container to carry with you.
    - `+0.116` [wiktionary] requiring: If you require something, you need it.
    - `+0.051` [wiktionary] epistaxis: Epistaxis is bleeding from the nose.
    - `+0.047` [wiktionary] resolved: To resolve means to create a solution for a problem.

- rationale: The original term "resolved" means that a problem or condition has come to an end, so "stopped" conveys that the issue is no longer active in simple language. Phrase frequency increases from Zipf 4.10 to 4.84, while syllable count drops from 2 to 1. Patients can now grasp that the medical issue has ceased without needing to process a more complex verb.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

==============================================================================

## Note 30 - `396`

**ORIGINAL**  I also explained to the patient about conscious sedation.

**REFERENCE** I also explained to the patient about awake sedation.

| | FKGL | FRE | SMOG | Coleman-Liau | words |
|---|---:|---:|---:|---:|---:|
| ORIGINAL | 8.90 | 47.30 | 8.84 | 11.84 | 9 |
| REFERENCE | 8.90 | 47.30 | 8.84 | 9.27 | 9 |

### Stage 2 - extraction + classification

| term | kind | category | action | Zipf | AoA | syll |
|---|---|---|---|---:|---:|---:|
| `conscious sedation` | phrase | medical_essential | elaborate | 2.93 | 13.2 | 5 |

### Stage 3 - retrieval

coverage **1.0** (1/1), glossary budget 2/16

| term | Zipf stratum | defs | sources | matched via | origin |
|---|---|---:|---|---|---|
| `conscious sedation` | rare | 2 | nih.json, readme_lay_vocab.jsonl | exact | extracted |

Glossary shown to the model:

1. `[readme]` conscious sedation: Medication given to a patient to make them lightly sedated and forgetful during a procedure, but they are not fully unconscious.
2. `[nih]` conscious sedation: A level of sedation in which a person is asleep but wakes when spoken to or touched. Conscious sedation is caused by special drugs and is used to help relieve anxiety during certain medical or surgical procedures. Drugs that relieve pain may be given at the same time. Also called moderate sedation.

### Stage 4 - arm `naive`

**output:** I also told the patient about conscious sedation.

| metric | value |
|---|---:|
| bertscore_f1 | 0.864 |
| coleman_liau | 10.23 |
| coleman_liau_drop | 1.62 |
| copy_jargon_rate | 1.000 |
| critical_error | 0.000 |
| fkgl | 8.18 |
| fkgl_drop | 0.72 |
| fre | 50.7 |
| fre_gain | 3.4 |
| human_edit_recall | 0.000 |
| length_ratio | 0.89 |
| n_words | 8.0 |
| nli_completeness | 0.992 |
| nli_faithfulness | 0.992 |
| replacement_f1 | 0.000 |
| rewrite_aggressiveness | 1.000 |
| sari | 13.30 |
| smog | 8.84 |
| smog_drop | 0.00 |

### Stage 4 - arm `termonly`

**output:** I also explained to the patient about a light sleep.

| metric | value |
|---|---:|
| bertscore_f1 | 0.800 |
| coleman_liau | 5.60 |
| coleman_liau_drop | 6.24 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 4.83 |
| fkgl_drop | 4.07 |
| fre | 78.2 |
| fre_gain | 30.9 |
| human_edit_recall | 1.000 |
| length_ratio | 1.11 |
| n_words | 10.0 |
| nli_completeness | 0.226 |
| nli_faithfulness | 0.261 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 61.94 |
| smog | 3.13 |
| smog_drop | 5.71 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `conscious sedation` -> `a light sleep` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** I also explained to the patient about light sleep.

| metric | value |
|---|---:|
| bertscore_f1 | 0.829 |
| coleman_liau | 7.33 |
| coleman_liau_drop | 4.51 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 4.96 |
| fkgl_drop | 3.93 |
| fre | 75.5 |
| fre_gain | 28.2 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 9.0 |
| nli_completeness | 0.118 |
| nli_faithfulness | 0.043 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 61.94 |
| smog | 3.13 |
| smog_drop | 5.71 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `conscious sedation` -> `light sleep` | replace | attributed | 0.621 | 0.759 | - | 1.000 | 0.143 | - |

**edit `conscious sedation` -> `light sleep`**

- status: `attributed`
- log p full -1.4210, empty -2.0423
- masks scored: 6/6 (+1 top-k)
- ranked sources:
    - `+0.436` [readme] conscious sedation: Medication given to a patient to make them lightly sedated and forgetful during a procedur
    - `+0.292` [nih] conscious sedation: A level of sedation in which a person is asleep but wakes when spoken to or touched. Consc

- rationale: The original term describes a state where a patient is relaxed and drowsy but can still respond to commands, so "light sleep" conveys this reduced alertness in plain language. Phrase frequency increases from Zipf 2.93 to 4.87, while age of acquisition drops from 13.20 to 4.05. Patients can now grasp that they will be resting comfortably without needing to know the specific medical procedure.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

==============================================================================

## Note 31 - `762`

**ORIGINAL**  Palpation of her right knee reveals no crepitus.

**REFERENCE** Feeling of her right knee reveals no crunchy feeling.

| | FKGL | FRE | SMOG | Coleman-Liau | words |
|---|---:|---:|---:|---:|---:|
| ORIGINAL | 5.23 | 71.82 | 8.84 | 9.50 | 8 |
| REFERENCE | 4.96 | 75.50 | 3.13 | 9.27 | 9 |

### Stage 2 - extraction + classification

| term | kind | category | action | Zipf | AoA | syll |
|---|---|---|---|---:|---:|---:|
| `Palpation` | word | general_hard_word | replace | 2.05 | 15.33 | 3 |
| `crepitus` | word | medical_descriptor | replace | 1.39 | None | 2 |

### Stage 3 - retrieval

coverage **1.0** (2/2), glossary budget 5/16

| term | Zipf stratum | defs | sources | matched via | origin |
|---|---|---:|---|---|---|
| `Palpation` | very_rare | 3 | nih.json, readme_lay_vocab.jsonl | exact | extracted |
| `crepitus` | very_rare | 2 | dictonary.csv | exact | extracted |

Glossary shown to the model:

1. `[dictionary]` Crepitus (n.): The noise produced by a sudden discharge of wind from the bowels.
2. `[readme]` palpation: Feeling a part of the body with your hands.
3. `[dictionary]` Crepitus (n.): Same as Crepitation, 2.
4. `[readme]` Palpation: Feeling a part of the body.
5. `[nih]` palpation: Examination by pressing on the surface of the body to feel the organs or tissues underneath.

### Stage 4 - arm `naive`

**output:** Palpation of her right knee shows no crackling sounds.

| metric | value |
|---|---:|
| bertscore_f1 | 0.681 |
| coleman_liau | 9.91 |
| coleman_liau_drop | -0.41 |
| copy_jargon_rate | 0.500 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 3.65 |
| fkgl_drop | 1.58 |
| fre | 84.9 |
| fre_gain | 13.1 |
| human_edit_recall | 0.500 |
| laterality_preservation | 1.000 |
| length_ratio | 1.00 |
| n_words | 9.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.899 |
| nli_faithfulness | 0.794 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 33.10 |
| smog | 8.84 |
| smog_drop | 0.00 |

### Stage 4 - arm `termonly`

**output:** Touching her right knee shows no crackling sound.

| metric | value |
|---|---:|
| bertscore_f1 | 0.647 |
| coleman_liau | 10.23 |
| coleman_liau_drop | -0.73 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 2.28 |
| fkgl_drop | 2.95 |
| fre | 93.0 |
| fre_gain | 21.1 |
| human_edit_recall | 1.000 |
| laterality_preservation | 1.000 |
| length_ratio | 0.89 |
| n_words | 8.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.897 |
| nli_faithfulness | 0.922 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 28.93 |
| smog | 3.13 |
| smog_drop | 5.71 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `crepitus` -> `crackling sound` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Feeling her right knee shows no crackling sound.

| metric | value |
|---|---:|
| bertscore_f1 | 0.666 |
| coleman_liau | 9.50 |
| coleman_liau_drop | 0.00 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 2.28 |
| fkgl_drop | 2.95 |
| fre | 93.0 |
| fre_gain | 21.1 |
| human_edit_recall | 1.000 |
| laterality_preservation | 1.000 |
| length_ratio | 0.89 |
| n_words | 8.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.903 |
| nli_faithfulness | 0.927 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 31.71 |
| smog | 3.13 |
| smog_drop | 5.71 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `crepitus` -> `crackling sound` | replace | attributed | -0.179 | -0.214 | - | 0.443 | -0.000 | - |

**edit `crepitus` -> `crackling sound`**

- status: `attributed`
- log p full -1.9042, empty -1.7255
- masks scored: 34/34 (+2 top-k)
- ranked sources:
    - `-0.003` [dictionary] Crepitus (n.): Same as Crepitation, 2.
    - `-0.005` [nih] palpation: Examination by pressing on the surface of the body to feel the organs or tissues underneath.
    - `-0.019` [dictionary] Crepitus (n.): The noise produced by a sudden discharge of wind from the bowels.

- rationale: The original term refers to a crackling sound heard during physical examination, so "crackling sound" conveys that auditory sensation in plain language. Phrase frequency increases from Zipf 1.39 to 2.91, while syllable count rises from 2 to 3. Patients can now recognize the specific noise associated with the condition without needing specialized medical vocabulary.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

==============================================================================

## Note 32 - `427`

**ORIGINAL**  She stepped on ideas, concerns and expectations the evening prior and twisted her ankle.

**REFERENCE** She stepped on ice the evening prior and twisted her ankle.

| | FKGL | FRE | SMOG | Coleman-Liau | words |
|---|---:|---:|---:|---:|---:|
| ORIGINAL | 10.10 | 47.60 | 11.21 | 12.33 | 14 |
| REFERENCE | 4.79 | 80.31 | 3.13 | 6.82 | 11 |

### Stage 2 - extraction + classification

| term | kind | category | action | Zipf | AoA | syll |
|---|---|---|---|---:|---:|---:|
| `the evening prior` | phrase | general_hard_word | replace | 4.55 | 10.63 | 5 |
| `the evening` | phrase | medical_essential | elaborate | - | - | - |
| `prior` | word | medical_descriptor | replace | - | - | - |

### Stage 3 - retrieval

coverage **0.0** (0/1), glossary budget 3/16

| term | Zipf stratum | defs | sources | matched via | origin |
|---|---|---:|---|---|---|
| `the evening prior` | common | 0 | - | - | extracted |
| `the evening` | common | 2 | wiktionary.json | evening | split_from_uncovered |
| `prior` | common | 1 | wiktionary.json | exact | split_from_uncovered |

Glossary shown to the model:

1. `[wiktionary]` prior: If something happens prior to something else, it happens before it.
2. `[wiktionary]` evening: Period from dusk to midnight.
3. `[wiktionary]` evening: You use even to focus on the most surprising or unlikely case.

### Stage 4 - arm `naive`

**output:** She stepped on ideas, concerns, and expectations the evening before and twisted her ankle.

| metric | value |
|---|---:|
| bertscore_f1 | 0.616 |
| coleman_liau | 12.74 |
| coleman_liau_drop | -0.41 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 10.10 |
| fkgl_drop | 0.00 |
| fre | 47.6 |
| fre_gain | 0.0 |
| length_ratio | 1.27 |
| n_words | 14.0 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.994 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 19.14 |
| smog | 11.21 |
| smog_drop | 0.00 |
| temporality_preservation | 1.000 |

### Stage 4 - arm `termonly`

**output:** She stepped on ideas, concerns and expectations the night before and twisted her ankle.

| metric | value |
|---|---:|
| bertscore_f1 | 0.546 |
| coleman_liau | 11.91 |
| coleman_liau_drop | 0.41 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.333 |
| fkgl | 9.26 |
| fkgl_drop | 0.84 |
| fre | 53.6 |
| fre_gain | 6.0 |
| length_ratio | 1.27 |
| n_words | 14.0 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.995 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 21.81 |
| smog | 11.21 |
| smog_drop | 0.00 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `the evening prior` -> `the night before` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** She stepped on ideas, concerns and expectations the night before and twisted her ankle.

| metric | value |
|---|---:|
| bertscore_f1 | 0.546 |
| coleman_liau | 11.91 |
| coleman_liau_drop | 0.41 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.333 |
| fkgl | 9.26 |
| fkgl_drop | 0.84 |
| fre | 53.6 |
| fre_gain | 6.0 |
| length_ratio | 1.27 |
| n_words | 14.0 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.995 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 21.81 |
| smog | 11.21 |
| smog_drop | 0.00 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `the evening prior` -> `the night before` | replace | attributed | -0.235 | -0.604 | - | 0.929 | 0.035 | - |

**edit `the evening prior` -> `the night before`**

- status: `attributed`
- log p full -0.6207, empty -0.3855
- masks scored: 10/10 (+2 top-k)
- ranked sources:
    - `-0.015` [wiktionary] prior: If something happens prior to something else, it happens before it.
    - `-0.049` [wiktionary] evening: Period from dusk to midnight.
    - `-0.434` [wiktionary] evening: You use even to focus on the most surprising or unlikely case.

- rationale: The original phrase refers to the day before the current evening, and "the night before" conveys that same timing in simpler, more common language. Phrase frequency rises from 4.55 to 5.44, while age of acquisition drops from 10.63 to 5.45. Patients can now easily identify the specific timeframe without needing to parse the formal phrasing.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

==============================================================================

## Note 33 - `439`

**ORIGINAL**  Modifying Factors : Patient 's condition is aggravated by throwing.

**REFERENCE** Modifying Factors : Patient 's condition is made worse by throwing.

| | FKGL | FRE | SMOG | Coleman-Liau | words |
|---|---:|---:|---:|---:|---:|
| ORIGINAL | 14.14 | 9.70 | 13.02 | 16.36 | 9 |
| REFERENCE | 9.55 | 44.41 | 11.21 | 12.56 | 10 |

### Stage 2 - extraction + classification

| term | kind | category | action | Zipf | AoA | syll |
|---|---|---|---|---:|---:|---:|
| `Modifying Factors` | phrase | general_hard_word | replace | 3.37 | None | 6 |
| `Modifying` | word | medical_descriptor | replace | - | - | - |
| `Factors` | word | medical_descriptor | replace | - | - | - |
| `aggravated` | word | general_hard_word | replace | 3.47 | 8.61 | 4 |

### Stage 3 - retrieval

coverage **0.5** (1/2), glossary budget 4/16

| term | Zipf stratum | defs | sources | matched via | origin |
|---|---|---:|---|---|---|
| `Modifying Factors` | rare | 0 | - | - | extracted |
| `Modifying` | rare | 1 | wiktionary.json | exact | split_from_uncovered |
| `Factors` | common | 1 | wiktionary.json | exact | split_from_uncovered |
| `aggravated` | rare | 2 | readme_lay_vocab.jsonl, wiktionary.json | exact | extracted |

Glossary shown to the model:

1. `[wiktionary]` factors: A factor is one of a number of things that causes a result.
2. `[wiktionary]` modifying: If you modify something, you change it, often only in small ways, and often because you want to use it in a different situation.
3. `[readme]` aggravated: To make a problem or injury worse.
4. `[wiktionary]` aggravated: To aggravate is to make something worse.

### Stage 4 - arm `naive`

**output:** The patient's condition gets worse when they throw.

| metric | value |
|---|---:|
| bertscore_f1 | 0.439 |
| coleman_liau | 10.95 |
| coleman_liau_drop | 5.41 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.250 |
| fkgl | 3.76 |
| fkgl_drop | 10.39 |
| fre | 82.4 |
| fre_gain | 72.7 |
| human_edit_recall | 1.000 |
| length_ratio | 0.90 |
| n_words | 9.0 |
| nli_completeness | 0.851 |
| nli_faithfulness | 0.993 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.250 |
| sari | 26.63 |
| smog | 8.84 |
| smog_drop | 4.18 |

### Stage 4 - arm `termonly`

**output:** The patient's condition gets worse when they throw up.

| metric | value |
|---|---:|
| bertscore_f1 | 0.397 |
| coleman_liau | 9.27 |
| coleman_liau_drop | 7.09 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.250 |
| fkgl | 3.65 |
| fkgl_drop | 10.49 |
| fre | 84.9 |
| fre_gain | 75.2 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 10.0 |
| nli_completeness | 0.844 |
| nli_faithfulness | 0.990 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.250 |
| sari | 26.40 |
| smog | 8.84 |
| smog_drop | 4.18 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `aggravated` -> `gets worse` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Things that change the patient's condition get worse when they throw up.

| metric | value |
|---|---:|
| bertscore_f1 | 0.287 |
| coleman_liau | 10.25 |
| coleman_liau_drop | 6.11 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.750 |
| fkgl | 3.84 |
| fkgl_drop | 10.30 |
| fre | 88.9 |
| fre_gain | 79.2 |
| human_edit_recall | 1.000 |
| length_ratio | 1.30 |
| n_words | 13.0 |
| nli_completeness | 0.919 |
| nli_faithfulness | 0.966 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.250 |
| sari | 25.93 |
| smog | 8.84 |
| smog_drop | 4.18 |

annotation backend `novita`, 0 edits kept


==============================================================================

## Note 34 - `451`

**ORIGINAL**  History of osteoarthritis, osteoporosis, hypothyroidism, allergic rhinitis and kidney stones.

**REFERENCE** History of joint inflammation, bone degeneration, underactive thyroid, hay fever and kidney stones.

| | FKGL | FRE | SMOG | Coleman-Liau | words |
|---|---:|---:|---:|---:|---:|
| ORIGINAL | 21.35 | -40.19 | 15.90 | 27.64 | 10 |
| REFERENCE | 14.90 | 11.42 | 14.55 | 18.95 | 13 |

### Stage 2 - extraction + classification

| term | kind | category | action | Zipf | AoA | syll |
|---|---|---|---|---:|---:|---:|
| `allergic rhinitis` | phrase | medical_essential | elaborate | 2.37 | 18.07 | 5 |
| `osteoarthritis` | word | medical_essential | elaborate | 2.76 | None | 6 |
| `hypothyroidism` | word | medical_essential | elaborate | 2.68 | 15.43 | 3 |
| `kidney stones` | phrase | medical_essential | elaborate | 3.85 | 9.33 | 3 |
| `osteoporosis` | word | medical_essential | elaborate | 2.99 | 14.29 | 6 |

### Stage 3 - retrieval

coverage **1.0** (5/5), glossary budget 16/16

| term | Zipf stratum | defs | sources | matched via | origin |
|---|---|---:|---|---|---|
| `allergic rhinitis` | very_rare | 2 | justplainclear.json, michigan_plmd.json | exact | extracted |
| `osteoarthritis` | rare | 3 | justplainclear.json, readme_lay_vocab.jsonl | exact | extracted |
| `hypothyroidism` | rare | 2 | justplainclear.json, nih.json | exact | extracted |
| `kidney stones` | uncommon | 3 | michigan_plmd.json, readme_lay_vocab.jsonl | exact | extracted |
| `osteoporosis` | rare | 7 | iowa.json, michigan_plmd.json, nih.json, readme_lay_vocab.jsonl, thesarus.json, wiktionary.json | exact | extracted |

Glossary shown to the model:

1. `[michigan]` allergic rhinitis: Caused by your body's reaction in your nose to mold, pollen, or dust. Also called hay fever.
2. `[nih]` hypothyroidism: Too little thyroid hormone. Symptoms include weight gain, constipation, dry skin, and sensitivity to the cold. Also called underactive thyroid.
3. `[readme]` osteoarthritis: Osteoarthritis is a painful joint condition caused by the wearing down of bone tissue, leading to inflammation and cartilage loss.
4. `[readme]` kidney stones: Hard mineral deposits in the kidneys causing pain and blockage.
5. `[readme]` osteoporosis: Osteoporosis is when bones become weak and prone to breaking because they lose density.
6. `[justplainclear]` allergic rhinitis: Also known as: hay fever A condition where you have an allergic reaction that affects the nose
7. `[justplainclear]` hypothyroidism: A condition where your thyroid isn't active enough, so you have low hormone levels Hypothyroidism may cause fatigue, weight gain, a puffy face, joint pain, depression, and many other symptoms.
8. `[readme]` osteoarthritis: Arthritis that happens when the cushioning between joints wears out.
9. `[readme]` Kidney Stones: Painful mineral deposits that can form in your kidney and block urine flow.
10. `[readme]` Osteoporosis: Osteoporosis is a condition where bones become weak and more prone to fractures.
11. `[justplainclear]` osteoarthritis: A form of arthritis caused by the wear and tear of joints
12. `[michigan]` kidney stones: A solid piece of material that forms in the kidney from material in the urine. They can be tiny or large. While most kidney stones pass without help sometimes a stone will get stuck, blocking urine and causing great pain.
13. `[nih]` osteoporosis: A condition in which there is a decrease in the amount and thickness of bone tissue. This causes the bones to become weak and break more easily. Osteoporosis may be caused by older age, hormone changes, taking certain medicines, and not eating enough foods with calcium and vitamin D. It may also be caused by certain types of cancer and cancer treatment. It is most common in white and Asian women.
14. `[iowa]` OSTEOPOROSIS: softening of the bones
15. `[michigan]` osteoporosis: When your bones are weak break easily. Also called brittle done disease.
16. `[wiktionary]` osteoporosis: Osteoporosis is a disease in which the bones become very porous and brittle.

### Stage 4 - arm `naive`

**output:** The patient has a history of osteoarthritis, osteoporosis, hypothyroidism, allergic rhinitis, and kidney stones.

| metric | value |
|---|---:|
| bertscore_f1 | 0.220 |
| coleman_liau | 21.03 |
| coleman_liau_drop | 6.61 |
| copy_jargon_rate | 1.000 |
| critical_error | 0.000 |
| fkgl | 17.68 |
| fkgl_drop | 3.67 |
| fre | -6.8 |
| fre_gain | 33.4 |
| human_edit_recall | 0.000 |
| length_ratio | 1.08 |
| n_words | 14.0 |
| nli_completeness | 0.995 |
| nli_faithfulness | 0.962 |
| replacement_f1 | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 11.57 |
| smog | 15.90 |
| smog_drop | 0.00 |
| temporality_preservation | 1.000 |

### Stage 4 - arm `termonly`

**output:** She has had joint pain, weak bones, slow thyroid, runny nose allergies, and stones in her kidneys.

| metric | value |
|---|---:|
| bertscore_f1 | 0.377 |
| coleman_liau | 8.73 |
| coleman_liau_drop | 18.91 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 6.31 |
| fkgl_drop | 15.04 |
| fre | 80.1 |
| fre_gain | 120.3 |
| human_edit_recall | 1.000 |
| length_ratio | 1.31 |
| n_words | 17.0 |
| nli_completeness | 0.926 |
| nli_faithfulness | 0.972 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.143 |
| sari | 32.60 |
| smog | 8.84 |
| smog_drop | 7.06 |
| temporality_preservation | 0.000 |

annotation backend `novita`, 5 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `osteoarthritis` -> `joint pain` | replace | - | - | - | - | - | - | - |
| `osteoporosis` -> `weak bones` | replace | - | - | - | - | - | - | - |
| `hypothyroidism` -> `slow thyroid` | replace | - | - | - | - | - | - | - |
| `allergic rhinitis` -> `runny nose allergies` | replace | - | - | - | - | - | - | - |
| `kidney stones` -> `stones in her kidneys` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** She has had joint pain from worn joints, weak bones that break easily, low thyroid hormone, and hard mineral deposits in her kidneys.

| metric | value |
|---|---:|
| bertscore_f1 | 0.304 |
| coleman_liau | 9.90 |
| coleman_liau_drop | 17.74 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.800 |
| fkgl | 9.80 |
| fkgl_drop | 11.55 |
| fre | 65.8 |
| fre_gain | 106.0 |
| human_edit_recall | 1.000 |
| length_ratio | 1.77 |
| n_words | 23.0 |
| nli_completeness | 0.583 |
| nli_faithfulness | 0.698 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.125 |
| sari | 29.70 |
| smog | 13.02 |
| smog_drop | 2.88 |
| temporality_preservation | 0.000 |

annotation backend `novita`, 4 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `osteoarthritis` -> `joint pain from worn joints` | replace | attributed | 5.162 | 5.214 | 0.767 | 0.938 | 0.732 | - |
| `osteoporosis` -> `weak bones that break easily` | replace | attributed | 3.437 | 3.860 | 0.706 | 0.848 | 0.025 | - |
| `hypothyroidism` -> `low thyroid hormone` | replace | attributed | 2.803 | 3.112 | 0.821 | 0.934 | 0.117 | - |
| `kidney stones` -> `hard mineral deposits in her kidneys` | replace | attributed | 8.581 | 8.669 | 0.839 | 0.937 | 4.546 | - |

**edit `osteoarthritis` -> `joint pain from worn joints`**

- status: `attributed`
- log p full -2.9671, empty -8.1291
- masks scored: 66/66 (+8 top-k)
- ranked sources:
    - `+1.746` [readme] osteoarthritis: Osteoarthritis is a painful joint condition caused by the wearing down of bone tissue, leading
    - `+1.015` [justplainclear] osteoarthritis: A form of arthritis caused by the wear and tear of joints
    - `+0.479` [nih] hypothyroidism: Too little thyroid hormone. Symptoms include weight gain, constipation, dry skin, and sensitiv
    - `+0.434` [readme] osteoarthritis: Arthritis that happens when the cushioning between joints wears out.
    - `+0.317` [wiktionary] osteoporosis: Osteoporosis is a disease in which the bones become very porous and brittle.

- rationale: The glossary defines osteoarthritis as a painful joint condition caused by the wearing down of bone tissue, so "joint pain from worn joints" captures that specific cause and effect in plain language. Phrase frequency increases from Zipf 2.76 to 3.63, while syllable count drops from 6 to 5. Patients can now grasp the physical nature of the condition without needing to know the complex medical name.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `osteoporosis` -> `weak bones that break easily`**

- status: `attributed`
- log p full -1.0432, empty -4.4804
- masks scored: 66/66 (+8 top-k)
- ranked sources:
    - `+0.727` [readme] osteoporosis: Osteoporosis is when bones become weak and prone to breaking because they lose density.
    - `+0.702` [nih] osteoporosis: A condition in which there is a decrease in the amount and thickness of bone tissue. This causes
    - `+0.689` [michigan] osteoporosis: When your bones are weak break easily. Also called brittle done disease.
    - `+0.412` [justplainclear] osteoarthritis: A form of arthritis caused by the wear and tear of joints
    - `+0.349` [nih] hypothyroidism: Too little thyroid hormone. Symptoms include weight gain, constipation, dry skin, and sensitiv

- rationale: Osteoporosis refers to a condition where bones lose density and become fragile, so "weak bones that break easily" captures that fragility in plain language. Phrase frequency increases from Zipf 2.99 to 4.05, while age of acquisition falls from 14.29 to 5.58. Patients can now grasp the risk of bone fractures without needing to know the medical diagnosis.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `hypothyroidism` -> `low thyroid hormone`**

- status: `attributed`
- log p full -1.2788, empty -4.0817
- masks scored: 66/66 (+8 top-k)
- ranked sources:
    - `+1.684` [nih] hypothyroidism: Too little thyroid hormone. Symptoms include weight gain, constipation, dry skin, and sensitiv
    - `+1.567` [justplainclear] hypothyroidism: A condition where your thyroid isn't active enough, so you have low hormone levels Hypothyroid
    - `+0.279` [michigan] osteoporosis: When your bones are weak break easily. Also called brittle done disease.
    - `+0.145` [michigan] allergic rhinitis: Caused by your body's reaction in your nose to mold, pollen, or dust. Also called hay fever
    - `+0.092` [readme] osteoarthritis: Osteoarthritis is a painful joint condition caused by the wearing down of bone tissue, leading

- rationale: The glossary defines hypothyroidism as a condition where the thyroid gland does not produce enough hormone, so "low thyroid hormone" keeps that core idea in plain language. Phrase frequency increases from 2.68 to 3.35, while age of acquisition drops from 15.43 to 13.83. Patients can now grasp the specific hormonal deficiency without needing to know the medical diagnosis.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `kidney stones` -> `hard mineral deposits in her kidneys`**

- status: `attributed`
- log p full -2.4806, empty -11.0619
- masks scored: 66/66 (+8 top-k)
- ranked sources:
    - `+7.381` [readme] kidney stones: Hard mineral deposits in the kidneys causing pain and blockage.
    - `+2.836` [readme] Kidney Stones: Painful mineral deposits that can form in your kidney and block urine flow.
    - `+1.958` [nih] osteoporosis: A condition in which there is a decrease in the amount and thickness of bone tissue. This causes
    - `+1.149` [readme] osteoporosis: Osteoporosis is when bones become weak and prone to breaking because they lose density.
    - `+0.920` [iowa] OSTEOPOROSIS: softening of the bones

- rationale: The glossary defines kidney stones as hard mineral deposits that cause pain and blockage, so the replacement phrase keeps that core description in plain language. Phrase frequency increases from 3.85 to 3.28, while age of acquisition decreases from 9.33 to 8.67. You can now understand the physical nature of the problem without needing to know the specific medical term.
- audit: coverage 1.0, grounding_error=True, omission=False, source_ok=True, passage_ok=True

==============================================================================

## Note 35 - `465`

**ORIGINAL**  The ultrasound was negative for intracranial hemorrhage.

**REFERENCE** The ultrasound was negative for bleeding in the brain.

| | FKGL | FRE | SMOG | Coleman-Liau | words |
|---|---:|---:|---:|---:|---:|
| ORIGINAL | 15.80 | -5.73 | 14.55 | 20.57 | 7 |
| REFERENCE | 6.28 | 66.10 | 11.21 | 9.91 | 9 |

### Stage 2 - extraction + classification

| term | kind | category | action | Zipf | AoA | syll |
|---|---|---|---|---:|---:|---:|
| `intracranial hemorrhage` | phrase | medical_essential | elaborate | 2.55 | 14.94 | 8 |

### Stage 3 - retrieval

coverage **1.0** (1/1), glossary budget 2/16

| term | Zipf stratum | defs | sources | matched via | origin |
|---|---|---:|---|---|---|
| `intracranial hemorrhage` | rare | 2 | readme_lay_vocab.jsonl | exact | extracted |

Glossary shown to the model:

1. `[readme]` INTRACRANIAL HEMORRHAGE: Bleeding inside your brain.
2. `[readme]` intracranial hemorrhage: Bleeding within the brain.

### Stage 4 - arm `naive`

**output:** The ultrasound showed no bleeding inside the skull.

| metric | value |
|---|---:|
| bertscore_f1 | 0.736 |
| coleman_liau | 11.68 |
| coleman_liau_drop | 8.90 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| diagnostic_identity_preservation | 1.000 |
| fkgl | 5.23 |
| fkgl_drop | 10.57 |
| fre | 71.8 |
| fre_gain | 77.5 |
| human_edit_recall | 1.000 |
| length_ratio | 0.89 |
| n_words | 8.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.932 |
| nli_faithfulness | 0.935 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 24.35 |
| smog | 8.84 |
| smog_drop | 5.71 |

### Stage 4 - arm `termonly`

**output:** The ultrasound showed no bleeding inside the skull.

| metric | value |
|---|---:|
| bertscore_f1 | 0.736 |
| coleman_liau | 11.68 |
| coleman_liau_drop | 8.90 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| diagnostic_identity_preservation | 1.000 |
| fkgl | 5.23 |
| fkgl_drop | 10.57 |
| fre | 71.8 |
| fre_gain | 77.5 |
| human_edit_recall | 1.000 |
| length_ratio | 0.89 |
| n_words | 8.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.932 |
| nli_faithfulness | 0.935 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 24.35 |
| smog | 8.84 |
| smog_drop | 5.71 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `intracranial hemorrhage` -> `bleeding inside the skull` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** The ultrasound showed no bleeding inside the brain.

| metric | value |
|---|---:|
| bertscore_f1 | 0.821 |
| coleman_liau | 11.68 |
| coleman_liau_drop | 8.90 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| diagnostic_identity_preservation | 1.000 |
| fkgl | 5.23 |
| fkgl_drop | 10.57 |
| fre | 71.8 |
| fre_gain | 77.5 |
| human_edit_recall | 1.000 |
| length_ratio | 0.89 |
| n_words | 8.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.929 |
| nli_faithfulness | 0.962 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 28.10 |
| smog | 8.84 |
| smog_drop | 5.71 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `intracranial hemorrhage` -> `bleeding inside the brain` | replace | attributed | 1.838 | 2.794 | - | 0.800 | 2.051 | - |

**edit `intracranial hemorrhage` -> `bleeding inside the brain`**

- status: `attributed`
- log p full -0.4221, empty -2.2603
- masks scored: 6/6 (+1 top-k)
- ranked sources:
    - `+2.397` [readme] INTRACRANIAL HEMORRHAGE: Bleeding inside your brain.
    - `+0.346` [readme] intracranial hemorrhage: Bleeding within the brain.

- rationale: The original term refers to bleeding occurring within the skull, so "bleeding inside the brain" conveys that specific location and event in plain language. Phrase frequency increases from Zipf 2.55 to 4.00, while age of acquisition drops from 14.94 to 5.76. Patients can now grasp the severity of the injury without needing to know the complex medical name.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

==============================================================================

## Note 36 - `466`

**ORIGINAL**  He is status post laparoscopic appendicectomy, and he is tolerating oral diet.

**REFERENCE** He is status after keyhole surgery to remove appendix, and he is tolerating oral diet.

| | FKGL | FRE | SMOG | Coleman-Liau | words |
|---|---:|---:|---:|---:|---:|
| ORIGINAL | 14.66 | 11.36 | 13.02 | 13.15 | 12 |
| REFERENCE | 12.29 | 33.69 | 13.02 | 9.29 | 15 |

### Stage 2 - extraction + classification

| term | kind | category | action | Zipf | AoA | syll |
|---|---|---|---|---:|---:|---:|
| `laparoscopic appendicectomy` | phrase | medical_essential | elaborate | 0.0 | None | 10 |
| `laparoscopic` | word | medical_descriptor | replace | - | - | - |
| `tolerating oral diet` | phrase | general_hard_word | replace | 2.73 | 9.39 | 8 |
| `tolerating` | word | medical_descriptor | replace | - | - | - |
| `oral` | word | medical_descriptor | replace | - | - | - |
| `diet` | word | medical_descriptor | replace | - | - | - |
| `status post` | phrase | general_hard_word | replace | 4.76 | 11.63 | 3 |
| `status` | word | medical_descriptor | replace | - | - | - |
| `post` | word | medical_descriptor | replace | - | - | - |

### Stage 3 - retrieval

coverage **0.0** (0/3), glossary budget 16/16

| term | Zipf stratum | defs | sources | matched via | origin |
|---|---|---:|---|---|---|
| `laparoscopic appendicectomy` | very_rare | 0 | - | - | extracted |
| `laparoscopic` | rare | 2 | readme_lay_vocab.jsonl | exact | partial_split_from_uncovered |
| `tolerating oral diet` | rare | 0 | - | - | extracted |
| `tolerating` | rare | 1 | wiktionary.json | exact | split_from_uncovered |
| `oral` | uncommon | 7 | justplainclear.json, michigan_plmd.json, nih.json, readme_lay_vocab.jsonl, wiktionary.json | exact | split_from_uncovered |
| `diet` | common | 3 | nih.json, wiktionary.json | exact | split_from_uncovered |
| `status post` | common | 0 | - | - | extracted |
| `status` | common | 6 | justplainclear.json, michigan_plmd.json, readme_lay_vocab.jsonl, wiktionary.json | exact | split_from_uncovered |
| `post` | common | 2 | wiktionary.json | exact | split_from_uncovered |

Glossary shown to the model:

1. `[wiktionary]` tolerating: If you tolerate something, you put up with it, or allow it.
2. `[wiktionary]` post: Post is the letters and parcels that you send to other people.
3. `[readme]` laparoscopic: A surgery where a small tube with a camera is used to see inside the body.
4. `[nih]` diet: The things a person eats and drinks.
5. `[readme]` Status: Status means the condition or state of something.
6. `[readme]` Oral: Oral means something you take by mouth.
7. `[wiktionary]` post: A post is a tall rod or stick. Examples are a sign post, a lamp post, and a goal post.
8. `[readme]` Laparoscopic: A surgery that uses a small tube and camera to see inside your body.
9. `[wiktionary]` diet: A diet is the food that an animal, person, or group usually eats.
10. `[readme]` status: The current condition of something.
11. `[readme]` oral: "Oral means something you take through your mouth."
12. `[wiktionary]` diet: A diet is a controlled set of foods chosen for health purposes.
13. `[michigan]` status: The state or condition that you or something else is in.
14. `[nih]` oral: By or having to do with the mouth.
15. `[justplainclear]` status: State, condition
16. `[michigan]` oral: Your mouth.

### Stage 4 - arm `naive`

**output:** He had his appendix removed using a keyhole surgery, and he is eating food normally.

| metric | value |
|---|---:|
| bertscore_f1 | 0.583 |
| coleman_liau | 8.52 |
| coleman_liau_drop | 4.63 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.333 |
| fkgl | 9.93 |
| fkgl_drop | 4.73 |
| fre | 50.6 |
| fre_gain | 39.2 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 15.0 |
| nli_completeness | 0.929 |
| nli_faithfulness | 0.558 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 34.24 |
| smog | 13.02 |
| smog_drop | 0.00 |
| temporality_preservation | 0.000 |

### Stage 4 - arm `termonly`

**output:** He had surgery to remove his appendix through small cuts and is eating normally.

| metric | value |
|---|---:|
| bertscore_f1 | 0.478 |
| coleman_liau | 9.43 |
| coleman_liau_drop | 3.72 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.222 |
| fkgl | 8.41 |
| fkgl_drop | 6.24 |
| fre | 59.7 |
| fre_gain | 48.3 |
| human_edit_recall | 1.000 |
| length_ratio | 0.93 |
| n_words | 14.0 |
| nli_completeness | 0.922 |
| nli_faithfulness | 0.765 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 27.75 |
| smog | 13.02 |
| smog_drop | 0.00 |
| temporality_preservation | 0.000 |

annotation backend `novita`, 0 edits kept


### Stage 4 - arm `grounded`

**output:** He had surgery to remove his appendix through small holes, and he is eating normally.

| metric | value |
|---|---:|
| bertscore_f1 | 0.527 |
| coleman_liau | 8.91 |
| coleman_liau_drop | 4.24 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.222 |
| fkgl | 8.35 |
| fkgl_drop | 6.30 |
| fre | 61.9 |
| fre_gain | 50.5 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 15.0 |
| nli_completeness | 0.931 |
| nli_faithfulness | 0.767 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 36.93 |
| smog | 13.02 |
| smog_drop | 0.00 |
| temporality_preservation | 0.000 |

annotation backend `novita`, 0 edits kept


==============================================================================

## Note 37 - `478`

**ORIGINAL**  We believe that her walking is most likely not being affected by the hydrocephalus.

**REFERENCE** We believe that her walking is most likely not being affected by the excess fluid in the brain.

| | FKGL | FRE | SMOG | Coleman-Liau | words |
|---|---:|---:|---:|---:|---:|
| ORIGINAL | 8.41 | 59.68 | 11.21 | 10.67 | 14 |
| REFERENCE | 8.47 | 66.37 | 8.84 | 7.37 | 18 |

### Stage 2 - extraction + classification

| term | kind | category | action | Zipf | AoA | syll |
|---|---|---|---|---:|---:|---:|
| `hydrocephalus` | word | medical_essential | elaborate | 2.32 | 15.78 | 3 |

### Stage 3 - retrieval

coverage **1.0** (1/1), glossary budget 4/16

| term | Zipf stratum | defs | sources | matched via | origin |
|---|---|---:|---|---|---|
| `hydrocephalus` | very_rare | 4 | justplainclear.json, nih.json, readme_lay_vocab.jsonl | exact | extracted |

Glossary shown to the model:

1. `[readme]` hydrocephalus: Swelling of brain due to excess fluid.
2. `[readme]` HYDROCEPHALUS: When fluid around the brain builds up too much.
3. `[nih]` hydrocephalus: The abnormal buildup of cerebrospinal fluid in the ventricles of the brain.
4. `[justplainclear]` hydrocephalus: Also known as: water on the brain A condition where there is too much cerebrospinal fluid in your brain

### Stage 4 - arm `naive`

**output:** We think her walking is probably not affected by the hydrocephalus.

| metric | value |
|---|---:|
| bertscore_f1 | 0.714 |
| coleman_liau | 11.04 |
| coleman_liau_drop | -0.36 |
| copy_jargon_rate | 1.000 |
| critical_error | 0.000 |
| fkgl | 8.01 |
| fkgl_drop | 0.40 |
| fre | 57.2 |
| fre_gain | -2.5 |
| human_edit_recall | 0.000 |
| length_ratio | 0.61 |
| n_words | 11.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.993 |
| nli_faithfulness | 0.992 |
| replacement_f1 | 0.000 |
| rewrite_aggressiveness | 1.000 |
| sari | 12.36 |
| smog | 13.02 |
| smog_drop | -1.82 |
| uncertainty_preservation | 1.000 |

### Stage 4 - arm `termonly`

**output:** We believe her walking is likely not affected by fluid buildup in the brain.

| metric | value |
|---|---:|
| bertscore_f1 | 0.857 |
| coleman_liau | 7.77 |
| coleman_liau_drop | 2.90 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 7.57 |
| fkgl_drop | 0.84 |
| fre | 65.7 |
| fre_gain | 6.0 |
| human_edit_recall | 1.000 |
| length_ratio | 0.78 |
| n_words | 14.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.515 |
| nli_faithfulness | 0.812 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.667 |
| sari | 28.03 |
| smog | 8.84 |
| smog_drop | 2.37 |
| uncertainty_preservation | 1.000 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `hydrocephalus` -> `fluid buildup in the brain` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** We believe her walking is likely not affected by too much fluid in her brain.

| metric | value |
|---|---:|
| bertscore_f1 | 0.832 |
| coleman_liau | 6.20 |
| coleman_liau_drop | 4.47 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 6.78 |
| fkgl_drop | 1.63 |
| fre | 73.2 |
| fre_gain | 13.5 |
| human_edit_recall | 1.000 |
| length_ratio | 0.83 |
| n_words | 15.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.331 |
| nli_faithfulness | 0.512 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.667 |
| sari | 24.08 |
| smog | 8.84 |
| smog_drop | 2.37 |
| uncertainty_preservation | 1.000 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `hydrocephalus` -> `too much fluid in her brain` | replace | attributed | 2.826 | 3.001 | - | 0.941 | 0.928 | - |

**edit `hydrocephalus` -> `too much fluid in her brain`**

- status: `attributed`
- log p full -1.7770, empty -4.6030
- masks scored: 18/18 (+2 top-k)
- ranked sources:
    - `+1.606` [justplainclear] hydrocephalus: Also known as: water on the brain A condition where there is too much cerebrospinal fluid in yo
    - `+0.679` [readme] hydrocephalus: Swelling of brain due to excess fluid.
    - `+0.454` [nih] hydrocephalus: The abnormal buildup of cerebrospinal fluid in the ventricles of the brain.
    - `-0.437` [readme] HYDROCEPHALUS: When fluid around the brain builds up too much.

- rationale: Hydrocephalus describes a condition where excess fluid builds up inside the skull, so "too much fluid in her brain" conveys that same physical reality in simple terms. The phrase frequency rises from 2.32 to 4.13, indicating the new wording is much more common, while the age of acquisition drops from 15.78 to 7.94, meaning patients learn this concept much earlier in life. This change allows the patient to grasp the immediate physical problem without needing specialized medical vocabulary.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

==============================================================================

## Note 38 - `505`

**ORIGINAL**  She noted complaints of fatigue, lightheadedness, and severe dyspnea on exertion.

**REFERENCE** She noted complaints of tiredness, lightheadedness, and severe shortness of breath on doing anything physical.

| | FKGL | FRE | SMOG | Coleman-Liau | words |
|---|---:|---:|---:|---:|---:|
| ORIGINAL | 12.30 | 26.47 | 13.02 | 17.36 | 11 |
| REFERENCE | 13.07 | 28.05 | 14.55 | 18.19 | 15 |

### Stage 2 - extraction + classification

| term | kind | category | action | Zipf | AoA | syll |
|---|---|---|---|---:|---:|---:|
| `noted complaints of` | phrase | general_hard_word | replace | 4.1 | 4.55 | 5 |
| `noted` | word | medical_descriptor | replace | - | - | - |
| `complaints` | word | medical_descriptor | replace | - | - | - |
| `of` | word | medical_descriptor | replace | - | - | - |
| `dyspnea on exertion` | phrase | medical_descriptor | replace | 2.09 | 11.58 | 7 |
| `dyspnea` | word | medical_essential | elaborate | - | - | - |
| `on` | word | medical_descriptor | replace | - | - | - |
| `exertion` | word | medical_descriptor | replace | - | - | - |
| `lightheadedness` | word | medical_descriptor | replace | 1.92 | 10.11 | 4 |
| `fatigue` | word | medical_descriptor | replace | 3.86 | 11.83 | 2 |

### Stage 3 - retrieval

coverage **0.5** (2/4), glossary budget 16/16

| term | Zipf stratum | defs | sources | matched via | origin |
|---|---|---:|---|---|---|
| `noted complaints of` | uncommon | 0 | - | - | extracted |
| `noted` | common | 2 | wiktionary.json | exact | split_from_uncovered |
| `complaints` | uncommon | 2 | readme_lay_vocab.jsonl, wiktionary.json | exact | split_from_uncovered |
| `of` | common | 2 | dictonary.csv | exact | split_from_uncovered |
| `dyspnea on exertion` | very_rare | 0 | - | - | extracted |
| `dyspnea` | very_rare | 4 | michigan_plmd.json, nih.json, readme_lay_vocab.jsonl | exact | split_from_uncovered |
| `on` | common | 2 | wiktionary.json | exact | split_from_uncovered |
| `exertion` | rare | 3 | michigan_plmd.json, thesarus.json, wiktionary.json | exact | split_from_uncovered |
| `lightheadedness` | very_rare | 1 | readme_lay_vocab.jsonl | exact | extracted |
| `fatigue` | uncommon | 6 | justplainclear.json, michigan_plmd.json, nih.json, readme_lay_vocab.jsonl, wiktionary.json | exact | extracted |

Glossary shown to the model:

1. `[readme]` lightheadedness: Feeling dizzy or almost faint.
2. `[wiktionary]` on: positioned at the upper surface of, touching from above
3. `[wiktionary]` noted: If somebody is a noted person, they are well known.
4. `[readme]` Complaints: A problem or sickness that a person talks about.
5. `[dictionary]` Of (prep.): In a general sense, from, or out from; proceeding from; belonging to; relating to; concerning; -- used in a variety of applications; as:
6. `[michigan]` exertion: Effort or work.
7. `[readme]` Dyspnea: Struggling to breathe, feeling out of breath.
8. `[readme]` fatigue: Feeling exhausted and lacking energy.
9. `[wiktionary]` on: at the date of
10. `[wiktionary]` noted: A note is a single sound in music.
11. `[wiktionary]` complaints: A complaint is an expression of dissatisfaction
12. `[dictionary]` Of (prep.): Denoting that from which anything proceeds; indicating origin, source, descent, and the like; as, he is of a race of kings; he is of noble blood.
13. `[wiktionary]` exertion: An exertion is the expenditure of physical or mental effort.
14. `[readme]` dyspnea: Having a hard time breathing or feeling like you can't catch your breath.
15. `[nih]` fatigue: A condition marked by extreme tiredness and inability to function due to lack of energy. Fatigue may be acute or chronic.
16. `[thesaurus]` exertion: effort, work

### Stage 4 - arm `naive`

**output:** She said she felt tired, dizzy, and very short of breath when she exercised.

| metric | value |
|---|---:|
| bertscore_f1 | 0.619 |
| coleman_liau | 6.94 |
| coleman_liau_drop | 10.42 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.333 |
| fkgl | 5.88 |
| fkgl_drop | 6.42 |
| fre | 77.8 |
| fre_gain | 51.3 |
| human_edit_recall | 1.000 |
| length_ratio | 0.93 |
| n_words | 14.0 |
| nli_completeness | 0.992 |
| nli_faithfulness | 0.988 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.143 |
| sari | 26.55 |
| severity_downgrade | 1.000 |
| severity_preservation | 0.000 |
| severity_tier_input | 3.000 |
| smog | 8.84 |
| smog_drop | 4.18 |

### Stage 4 - arm `termonly`

**output:** She said she felt very tired, dizzy, and out of breath when active.

| metric | value |
|---|---:|
| bertscore_f1 | 0.614 |
| coleman_liau | 5.12 |
| coleman_liau_drop | 12.24 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.333 |
| fkgl | 4.91 |
| fkgl_drop | 7.39 |
| fre | 83.0 |
| fre_gain | 56.5 |
| human_edit_recall | 1.000 |
| length_ratio | 0.87 |
| n_words | 13.0 |
| nli_completeness | 0.943 |
| nli_faithfulness | 0.991 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.143 |
| sari | 26.59 |
| severity_downgrade | 1.000 |
| severity_preservation | 0.000 |
| severity_tier_input | 3.000 |
| smog | 3.13 |
| smog_drop | 9.89 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `fatigue` -> `very tired` | replace | - | - | - | - | - | - | - |
| `lightheadedness` -> `dizzy` | replace | - | - | - | - | - | - | - |
| `dyspnea on exertion` -> `out of breath when active` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** She said she felt very tired, dizzy, and out of breath when she worked hard.

| metric | value |
|---|---:|
| bertscore_f1 | 0.569 |
| coleman_liau | 5.04 |
| coleman_liau_drop | 12.32 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.333 |
| fkgl | 4.42 |
| fkgl_drop | 7.88 |
| fre | 90.1 |
| fre_gain | 63.6 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 15.0 |
| nli_completeness | 0.749 |
| nli_faithfulness | 0.973 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.143 |
| sari | 26.45 |
| severity_downgrade | 1.000 |
| severity_preservation | 0.000 |
| severity_tier_input | 3.000 |
| smog | 3.13 |
| smog_drop | 9.89 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `fatigue` -> `very tired` | replace | attributed | -0.016 | -0.029 | 0.904 | 0.927 | 1.523 | - |
| `lightheadedness` -> `dizzy` | replace | attributed | 0.071 | 0.771 | 0.763 | 0.956 | 0.050 | - |
| `dyspnea on exertion` -> `out of breath when she worked hard` | replace | attributed | 1.739 | 1.782 | 0.545 | 0.825 | 0.815 | - |

**edit `fatigue` -> `very tired`**

- status: `attributed`
- log p full -0.8123, empty -0.7965
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+1.609` [nih] fatigue: A condition marked by extreme tiredness and inability to function due to lack of energy. Fatigue may 
    - `+0.086` [readme] dyspnea: Having a hard time breathing or feeling like you can't catch your breath.
    - `+0.038` [readme] lightheadedness: Feeling dizzy or almost faint.
    - `+0.000` [wiktionary] complaints: A complaint is an expression of dissatisfaction

- rationale: The original term "fatigue" refers to a state of extreme exhaustion, which the replacement "very tired" conveys in simple, everyday language. Phrase frequency rises from 3.86 to 4.69, indicating the new phrase is more common, while age of acquisition drops from 11.83 to 4.90, showing it is learned much earlier in life. Patients can now immediately recognize the symptom without needing to recall a specific medical label.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `lightheadedness` -> `dizzy`**

- status: `attributed`
- log p full -0.0658, empty -0.1373
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+0.222` [readme] lightheadedness: Feeling dizzy or almost faint.
    - `+0.172` [wiktionary] complaints: A complaint is an expression of dissatisfaction
    - `+0.136` [readme] dyspnea: Having a hard time breathing or feeling like you can't catch your breath.
    - `+0.089` [readme] fatigue: Feeling exhausted and lacking energy.
    - `+0.037` [wiktionary] on: at the date of

- rationale: The original term describes a sensation of faintness or unsteadiness, so "dizzy" captures that feeling of lightheadedness in simpler language. Phrase frequency rises from Zipf 1.92 to 3.43, while age of acquisition drops from 10.11 to 5.50. Patients can now grasp the symptom immediately without needing to recall a more complex medical word.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `dyspnea on exertion` -> `out of breath when she worked hard`**

- status: `attributed`
- log p full -2.9917, empty -4.7310
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+1.010` [readme] Dyspnea: Struggling to breathe, feeling out of breath.
    - `+0.195` [thesaurus] exertion: effort, work
    - `+0.189` [michigan] exertion: Effort or work.
    - `+0.018` [wiktionary] complaints: A complaint is an expression of dissatisfaction

- rationale: The glossary defines the original term as struggling to breathe, so the replacement keeps that central feeling of being out of breath in plain language. Phrase frequency increases from 2.09 to 4.38, while age of acquisition falls from 11.58 to 5.81. Patients can now understand the specific breathing problem without needing to know the medical name.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

==============================================================================

## Note 39 - `516`

**ORIGINAL**  No significant amount of edema associated with these in the dorsum of the hand.

**REFERENCE** No significant amount of swelling associated with these in the back of the hand.

| | FKGL | FRE | SMOG | Coleman-Liau | words |
|---|---:|---:|---:|---:|---:|
| ORIGINAL | 10.94 | 41.55 | 13.02 | 9.01 | 14 |
| REFERENCE | 9.26 | 53.64 | 11.21 | 9.43 | 14 |

### Stage 2 - extraction + classification

| term | kind | category | action | Zipf | AoA | syll |
|---|---|---|---|---:|---:|---:|
| `significant amount` | phrase | general_hard_word | replace | 4.75 | 9.89 | 6 |
| `significant` | word | medical_descriptor | replace | - | - | - |
| `amount` | word | medical_descriptor | replace | - | - | - |
| `associated with` | phrase | general_hard_word | replace | 4.89 | 4.44 | 6 |
| `dorsum` | word | medical_descriptor | replace | 2.47 | None | 2 |
| `edema` | word | medical_descriptor | replace | 2.95 | 15.07 | 3 |

### Stage 3 - retrieval

coverage **0.75** (3/4), glossary budget 16/16

| term | Zipf stratum | defs | sources | matched via | origin |
|---|---|---:|---|---|---|
| `significant amount` | common | 0 | - | - | extracted |
| `significant` | common | 6 | justplainclear.json, michigan_plmd.json, nih.json, thesarus.json, wiktionary.json | exact | split_from_uncovered |
| `amount` | common | 3 | justplainclear.json, wiktionary.json | exact | split_from_uncovered |
| `associated with` | common | 3 | justplainclear.json, readme_lay_vocab.jsonl | exact | extracted |
| `dorsum` | very_rare | 1 | readme_lay_vocab.jsonl | exact | extracted |
| `edema` | rare | 5 | iowa.json, michigan_plmd.json, nih.json, readme_lay_vocab.jsonl | exact | extracted |

Glossary shown to the model:

1. `[readme]` dorsum: The dorsum is basically the back or upper surface.
2. `[justplainclear]` amount: How much or how many
3. `[readme]` associated with: Linked to something.
4. `[readme]` Edema: Swelling in the body caused by too much fluid.
5. `[nih]` significant: In statistics, describes a mathematical measure of difference between groups. The difference is said to be significant if it is greater than what might be expected to happen by chance alone. Also called statistically significant.
6. `[wiktionary]` amount: A total of things; a measure of how much.
7. `[readme]` Associated with: Connected with something.
8. `[readme]` edema: Swelling due to too much fluid in the body tissues.
9. `[michigan]` significant: Big or important.
10. `[wiktionary]` amount: The full effect or value.
11. `[justplainclear]` associated with: Linked to, related to, goes along with, is part of
12. `[nih]` edema: Swelling caused by excess fluid in body tissues.
13. `[justplainclear]` significant: Big, serious, important, major
14. `[iowa]` EDEMA: excess fluid collecting in tissue
15. `[wiktionary]` significant: If something is significant, it is important, or large, enough to pay attention to or to believe.
16. `[michigan]` edema: Swelling caused by too much fluid in your body.

### Stage 4 - arm `naive`

**output:** There was no significant swelling on the back of the hand related to these.

| metric | value |
|---|---:|
| bertscore_f1 | 0.636 |
| coleman_liau | 7.36 |
| coleman_liau_drop | 1.66 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.600 |
| fkgl | 6.73 |
| fkgl_drop | 4.21 |
| fre | 71.8 |
| fre_gain | 30.2 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 14.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.923 |
| nli_faithfulness | 0.897 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 39.55 |
| severity_downgrade | 0.000 |
| severity_preservation | 1.000 |
| severity_tier_input | 2.000 |
| severity_tier_output | 2.000 |
| smog | 11.21 |
| smog_drop | 1.82 |

### Stage 4 - arm `termonly`

**output:** No swelling on the back of the hand.

| metric | value |
|---|---:|
| bertscore_f1 | 0.694 |
| coleman_liau | 0.80 |
| coleman_liau_drop | 8.21 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.333 |
| fkgl | 0.80 |
| fkgl_drop | 10.14 |
| fre | 103.5 |
| fre_gain | 62.0 |
| human_edit_recall | 1.000 |
| length_ratio | 0.57 |
| n_words | 8.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.907 |
| nli_faithfulness | 0.333 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 42.30 |
| severity_downgrade | 1.000 |
| severity_preservation | 0.000 |
| severity_tier_input | 2.000 |
| smog | 3.13 |
| smog_drop | 9.89 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `significant amount` -> `swelling` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** No big swelling on the back of the hand.

| metric | value |
|---|---:|
| bertscore_f1 | 0.692 |
| coleman_liau | 0.89 |
| coleman_liau_drop | 8.13 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 1.03 |
| fkgl_drop | 9.91 |
| fre | 103.7 |
| fre_gain | 62.1 |
| human_edit_recall | 1.000 |
| length_ratio | 0.64 |
| n_words | 9.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.916 |
| nli_faithfulness | 0.660 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 40.39 |
| severity_downgrade | 0.000 |
| severity_preservation | 0.000 |
| severity_tier_input | 2.000 |
| severity_tier_output | 2.000 |
| smog | 3.13 |
| smog_drop | 9.89 |

annotation backend `novita`, 2 edits kept

- rejected: DROP filler    'associated with' -> 'on'  (body is filler)

| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `significant amount` -> `big` | replace | attributed | 3.228 | 3.650 | 0.856 | 0.911 | 0.106 | - |
| `dorsum` -> `back` | replace | attributed | 0.332 | 2.499 | 0.741 | 0.953 | 2.433 | - |

**edit `significant amount` -> `big`**

- status: `attributed`
- log p full -1.0403, empty -4.2680
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+1.622` [justplainclear] significant: Big, serious, important, major
    - `+1.516` [michigan] significant: Big or important.
    - `+0.252` [readme] edema: Swelling due to too much fluid in the body tissues.
    - `+0.208` [readme] Edema: Swelling in the body caused by too much fluid.
    - `+0.166` [wiktionary] amount: The full effect or value.

- rationale: The glossary defines "significant amount" as big, serious, important, or major, so replacing it with "big" keeps that core idea in plain language. Phrase frequency rises from 4.75 to 5.67, while age of acquisition drops from 9.89 to 2.89. You can now grasp the scale of the issue immediately without needing to know the specific medical phrasing.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `dorsum` -> `back`**

- status: `attributed`
- log p full -0.0359, empty -0.3683
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+2.492` [readme] dorsum: The dorsum is basically the back or upper surface.
    - `+0.059` [justplainclear] associated with: Linked to, related to, goes along with, is part of
    - `+0.039` [readme] Edema: Swelling in the body caused by too much fluid.
    - `+0.030` [nih] edema: Swelling caused by excess fluid in body tissues.
    - `+0.022` [michigan] edema: Swelling caused by too much fluid in your body.

- rationale: The original term refers to the upper surface of the foot, so "back" conveys that same anatomical location in simple language. Phrase frequency rises from 2.47 to 6.04, while syllable count drops from 2 to 1. Patients can now identify the specific part of the foot without needing specialized anatomical vocabulary.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

==============================================================================

## Note 40 - `523`

**ORIGINAL**  No cardio or pulmonary complaints.

**REFERENCE** No heart or lung complaints.

| | FKGL | FRE | SMOG | Coleman-Liau | words |
|---|---:|---:|---:|---:|---:|
| ORIGINAL | 12.32 | 15.64 | 11.21 | 11.92 | 5 |
| REFERENCE | 0.52 | 100.24 | 3.13 | 4.96 | 5 |

### Stage 2 - extraction + classification

| term | kind | category | action | Zipf | AoA | syll |
|---|---|---|---|---:|---:|---:|
| `pulmonary` | word | medical_descriptor | replace | 3.5 | 13.05 | 4 |
| `cardio` | word | medical_descriptor | replace | 3.44 | None | 3 |

### Stage 3 - retrieval

coverage **0.5** (1/2), glossary budget 6/16

| term | Zipf stratum | defs | sources | matched via | origin |
|---|---|---:|---|---|---|
| `pulmonary` | uncommon | 6 | iowa.json, justplainclear.json, nih.json, readme_lay_vocab.jsonl, thesarus.json | exact | extracted |
| `cardio` | rare | 0 | - | - | extracted |

Glossary shown to the model:

1. `[readme]` Pulmonary: About the lungs.
2. `[readme]` pulmonary: Related to the lungs.
3. `[nih]` pulmonary: Having to do with the lungs.
4. `[iowa]` PULMONARY: pertaining to the lungs
5. `[justplainclear]` pulmonary: About the lungs
6. `[thesaurus]` pulmonary: related to the lungs

### Stage 4 - arm `naive`

**output:** The patient has no problems with their heart or lungs.

| metric | value |
|---|---:|
| bertscore_f1 | 0.498 |
| coleman_liau | 6.76 |
| coleman_liau_drop | 5.16 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 2.47 |
| fkgl_drop | 9.85 |
| fre | 95.2 |
| fre_gain | 79.5 |
| human_edit_recall | 1.000 |
| length_ratio | 2.00 |
| n_words | 10.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.988 |
| nli_faithfulness | 0.977 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 40.17 |
| smog | 3.13 |
| smog_drop | 8.08 |

### Stage 4 - arm `termonly`

**output:** No heart or lung problems.

| metric | value |
|---|---:|
| bertscore_f1 | 0.928 |
| coleman_liau | 2.64 |
| coleman_liau_drop | 9.28 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 0.52 |
| fkgl_drop | 11.80 |
| fre | 100.2 |
| fre_gain | 84.6 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 5.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.987 |
| nli_faithfulness | 0.986 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 59.86 |
| smog | 3.13 |
| smog_drop | 8.08 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `cardio` -> `heart` | replace | - | - | - | - | - | - | - |
| `pulmonary` -> `lung` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** No heart or lung complaints.

| metric | value |
|---|---:|
| bertscore_f1 | 1.000 |
| coleman_liau | 4.96 |
| coleman_liau_drop | 6.96 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 0.52 |
| fkgl_drop | 11.80 |
| fre | 100.2 |
| fre_gain | 84.6 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 5.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.984 |
| nli_faithfulness | 0.981 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 75.00 |
| smog | 3.13 |
| smog_drop | 8.08 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `cardio` -> `heart` | replace | attributed | 0.034 | 0.125 | 0.576 | 0.791 | 0.204 | - |
| `pulmonary` -> `lung` | replace | attributed | 0.142 | 2.584 | 0.552 | 0.568 | 0.171 | - |

**edit `cardio` -> `heart`**

- status: `attributed`
- log p full -0.2987, empty -0.3324
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.302` [iowa] PULMONARY: pertaining to the lungs
    - `+0.099` [justplainclear] pulmonary: About the lungs
    - `+0.025` [nih] pulmonary: Having to do with the lungs.
    - `+0.022` [thesaurus] pulmonary: related to the lungs
    - `-0.075` [readme] pulmonary: Related to the lungs.

- rationale: The prefix "cardio" refers to the heart, so replacing it with "heart" keeps the anatomical focus in plain language. Phrase frequency increases from Zipf 3.44 to 5.31, while syllable count drops from 3 to 1. Patients can immediately recognize the body part involved without needing to decode a medical prefix.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `pulmonary` -> `lung`**

- status: `attributed`
- log p full -0.0126, empty -0.1547
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.425` [justplainclear] pulmonary: About the lungs
    - `+0.254` [thesaurus] pulmonary: related to the lungs
    - `+0.172` [readme] Pulmonary: About the lungs.
    - `+0.054` [iowa] PULMONARY: pertaining to the lungs

- rationale: The original term refers to anything related to the lungs, so "lung" keeps that specific organ connection in plain language. Phrase frequency increases from Zipf 3.50 to 4.10, while age of acquisition falls from 13.05 to 7.16. Patients can now immediately identify the body part involved without needing to know the medical root.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

==============================================================================

## Note 41 - `553`

**ORIGINAL**  At that time, the Coreg had been held secondary to hypotension.

**REFERENCE** At that time, the Coreg had been held because of low blood pressure

| | FKGL | FRE | SMOG | Coleman-Liau | words |
|---|---:|---:|---:|---:|---:|
| ORIGINAL | 6.94 | 64.92 | 11.21 | 8.40 | 11 |
| REFERENCE | 3.10 | 96.02 | 3.13 | 6.02 | 13 |

### Stage 2 - extraction + classification

| term | kind | category | action | Zipf | AoA | syll |
|---|---|---|---|---:|---:|---:|
| `secondary to` | phrase | general_hard_word | replace | 4.53 | 9.11 | 5 |
| `secondary` | word | medical_descriptor | replace | - | - | - |
| `to` | word | medical_descriptor | replace | - | - | - |
| `hypotension` | word | medical_descriptor | replace | 2.52 | 14.41 | 4 |
| `Coreg` | word | medical_essential | elaborate | 1.16 | None | 1 |

### Stage 3 - retrieval

coverage **0.6667** (2/3), glossary budget 11/16

| term | Zipf stratum | defs | sources | matched via | origin |
|---|---|---:|---|---|---|
| `secondary to` | common | 0 | - | - | extracted |
| `secondary` | common | 2 | wiktionary.json | exact | split_from_uncovered |
| `to` | common | 2 | wiktionary.json | exact | split_from_uncovered |
| `hypotension` | rare | 6 | iowa.json, michigan_plmd.json, nih.json, readme_lay_vocab.jsonl, wiktionary.json | exact | extracted |
| `Coreg` | very_rare | 1 | nih.json | exact | extracted |

Glossary shown to the model:

1. `[nih]` Coreg: A drug used to treat high blood pressure and certain heart problems. It is also being studied in the prevention and treatment of side effects caused by some anticancer drugs. Coreg blocks certain receptors on nerve cells and causes blood vessels to dilate (widen). It is a type of antihypertensive agent and a type of antianginal agent. Also called carvedilol phosphate.
2. `[wiktionary]` secondary: second, next in order to the first or primary.
3. `[wiktionary]` to: To has no meaning. It is used with a bare infinitival clause.
4. `[readme]` hypotension: Low blood pressure.
5. `[wiktionary]` secondary: of less than primary importance.
6. `[wiktionary]` to: To shows where something goes, the goal of movement.
7. `[readme]` Hypotension: Hypotension means low blood pressure.
8. `[nih]` hypotension: Abnormally low blood pressure.
9. `[iowa]` HYPOTENSION: low blood pressure
10. `[michigan]` hypotension: When your blood pressure is low. For some people, this is normal, but it may cause problems for other people.
11. `[wiktionary]` hypotension: Hypotension is the disease of having low blood pressure.

### Stage 4 - arm `naive`

**output:** At that time, the Coreg was not used because the patient had low blood pressure.

| metric | value |
|---|---:|
| bertscore_f1 | 0.635 |
| coleman_liau | 6.97 |
| coleman_liau_drop | 1.43 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 4.42 |
| fkgl_drop | 2.52 |
| fre | 90.1 |
| fre_gain | 25.2 |
| human_edit_recall | 1.000 |
| length_ratio | 1.15 |
| n_words | 15.0 |
| nli_completeness | 0.753 |
| nli_faithfulness | 0.688 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 49.48 |
| smog | 3.13 |
| smog_drop | 8.08 |

### Stage 4 - arm `termonly`

**output:** At that time, the medicine had been stopped because of low blood pressure.

| metric | value |
|---|---:|
| bertscore_f1 | 0.670 |
| coleman_liau | 8.69 |
| coleman_liau_drop | -0.29 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.400 |
| fkgl | 4.91 |
| fkgl_drop | 2.03 |
| fre | 83.0 |
| fre_gain | 18.1 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 13.0 |
| nli_completeness | 0.207 |
| nli_faithfulness | 0.558 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.250 |
| sari | 54.48 |
| smog | 8.84 |
| smog_drop | 2.37 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `Coreg` -> `medicine` | replace | - | - | - | - | - | - | - |
| `secondary to` -> `because of` | replace | - | - | - | - | - | - | - |
| `hypotension` -> `low blood pressure` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** At that time, Coreg was stopped because of low blood pressure.

| metric | value |
|---|---:|
| bertscore_f1 | 0.739 |
| coleman_liau | 7.87 |
| coleman_liau_drop | 0.53 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.250 |
| fkgl | 2.65 |
| fkgl_drop | 4.29 |
| fre | 95.7 |
| fre_gain | 30.8 |
| human_edit_recall | 1.000 |
| length_ratio | 0.85 |
| n_words | 11.0 |
| nli_completeness | 0.743 |
| nli_faithfulness | 0.875 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 43.07 |
| smog | 3.13 |
| smog_drop | 8.08 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `secondary to` -> `because of` | replace | attributed | -0.099 | -0.146 | 0.575 | 0.637 | 0.049 | - |
| `hypotension` -> `low blood pressure` | replace | attributed | -0.006 | -0.077 | 0.590 | 0.680 | 0.043 | - |

**edit `secondary to` -> `because of`**

- status: `attributed`
- log p full -1.1858, empty -1.0870
- masks scored: 66/66 (+3 top-k)
- ranked sources:
    - `+0.167` [readme] Hypotension: Hypotension means low blood pressure.
    - `+0.118` [readme] hypotension: Low blood pressure.
    - `+0.062` [wiktionary] secondary: of less than primary importance.
    - `+0.024` [iowa] HYPOTENSION: low blood pressure
    - `+0.007` [wiktionary] to: To shows where something goes, the goal of movement.

- rationale: The original phrase "secondary to" indicates that a condition exists as a result of another cause, so "because of" conveys this causal link in simple language. Phrase frequency rises from Zipf 4.53 to 6.01, while age of acquisition drops from 9.11 to 4.55. Patients can now clearly identify the reason for their symptoms without needing to parse complex medical causality.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `hypotension` -> `low blood pressure`**

- status: `attributed`
- log p full -0.0806, empty -0.0748
- masks scored: 66/66 (+3 top-k)
- ranked sources:
    - `+0.084` [readme] Hypotension: Hypotension means low blood pressure.
    - `+0.041` [wiktionary] to: To has no meaning. It is used with a bare infinitival clause.
    - `+0.040` [wiktionary] to: To shows where something goes, the goal of movement.
    - `+0.031` [readme] hypotension: Low blood pressure.

- rationale: The original term refers to a condition where blood pressure drops below normal levels, so "low blood pressure" conveys this state using everyday language. Phrase frequency rises from 2.52 to 4.65, and age of acquisition decreases from 14.41 to 8.95. Patients can now recognize the symptom immediately without needing specialized medical vocabulary.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

==============================================================================

## Note 42 - `554`

**ORIGINAL**  Her diarrhea now has settled down and she is having less urinary incontinence, less pedal edema.

**REFERENCE** Her watery poop now has settled down and she is having less uncontrolled peeing, less foot swelling.

| | FKGL | FRE | SMOG | Coleman-Liau | words |
|---|---:|---:|---:|---:|---:|
| ORIGINAL | 12.78 | 31.97 | 14.55 | 10.99 | 16 |
| REFERENCE | 8.39 | 65.17 | 11.21 | 10.44 | 17 |

### Stage 2 - extraction + classification

| term | kind | category | action | Zipf | AoA | syll |
|---|---|---|---|---:|---:|---:|
| `urinary incontinence` | phrase | medical_descriptor | replace | 2.77 | 14.41 | 8 |
| `pedal edema` | phrase | medical_descriptor | replace | 2.87 | 15.07 | 5 |
| `diarrhea` | word | medical_descriptor | replace | 3.55 | None | 4 |

### Stage 3 - retrieval

coverage **1.0** (3/3), glossary budget 10/16

| term | Zipf stratum | defs | sources | matched via | origin |
|---|---|---:|---|---|---|
| `urinary incontinence` | rare | 3 | michigan_plmd.json, nih.json, readme_lay_vocab.jsonl | exact | extracted |
| `pedal edema` | rare | 1 | readme_lay_vocab.jsonl | exact | extracted |
| `diarrhea` | uncommon | 6 | justplainclear.json, michigan_plmd.json, nih.json, readme_lay_vocab.jsonl, wiktionary.json | exact | extracted |

Glossary shown to the model:

1. `[readme]` pedal edema: Swollen feet.
2. `[readme]` urinary incontinence: When you can't control your pee.
3. `[readme]` diarrhea: Having loose, watery poop with cramps and bloating.
4. `[nih]` urinary incontinence: Inability to hold urine in the bladder.
5. `[readme]` Diarrhea: Having runny poop with stomach pains and bloating.
6. `[michigan]` urinary incontinence: When you lose control of your bladder and the fluids it holds.
7. `[nih]` diarrhea: Frequent and watery bowel movements.
8. `[michigan]` diarrhea: Loose, watery stools three or more times a day. It can be sudden (due to a virus, for example), persistent, or chronic, that is, lasting a long time.
9. `[justplainclear]` diarrhea: A bowel movement that is loose and watery If your poop is like water or very runny, or if you have many poops, you can lose a lot of liquids and become very weak.
10. `[wiktionary]` diarrhea: Diarrhea is an illness where the person's poop or feces are soft like water.

### Stage 4 - arm `naive`

**output:** Her diarrhea has stopped, and she is having less urinary incontinence and less swelling in her feet.

| metric | value |
|---|---:|
| bertscore_f1 | 0.574 |
| coleman_liau | 10.44 |
| coleman_liau_drop | 0.55 |
| copy_jargon_rate | 0.667 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 10.48 |
| fkgl_drop | 2.30 |
| fre | 50.2 |
| fre_gain | 18.3 |
| human_edit_recall | 0.333 |
| length_ratio | 1.00 |
| n_words | 17.0 |
| nli_completeness | 0.919 |
| nli_faithfulness | 0.699 |
| replacement_f1 | 0.500 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.600 |
| sari | 36.43 |
| smog | 13.02 |
| smog_drop | 1.53 |
| temporality_preservation | 0.000 |

### Stage 4 - arm `termonly`

**output:** Her stomach upset has calmed, and she is having less urine leakage and less swelling in her feet.

| metric | value |
|---|---:|
| bertscore_f1 | 0.647 |
| coleman_liau | 7.69 |
| coleman_liau_drop | 3.30 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 7.16 |
| fkgl_drop | 5.61 |
| fre | 75.8 |
| fre_gain | 43.8 |
| human_edit_recall | 1.000 |
| length_ratio | 1.06 |
| n_words | 18.0 |
| nli_completeness | 0.919 |
| nli_faithfulness | 0.884 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.375 |
| sari | 44.05 |
| smog | 3.13 |
| smog_drop | 11.43 |
| temporality_preservation | 0.000 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `diarrhea` -> `stomach upset` | replace | - | - | - | - | - | - | - |
| `urinary incontinence` -> `urine leakage` | replace | - | - | - | - | - | - | - |
| `pedal edema` -> `swelling in her feet` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Her loose stools have settled down, and she is having less trouble holding her pee and less swollen feet.

| metric | value |
|---|---:|
| bertscore_f1 | 0.663 |
| coleman_liau | 8.59 |
| coleman_liau_drop | 2.40 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 6.73 |
| fkgl_drop | 6.05 |
| fre | 80.7 |
| fre_gain | 48.7 |
| human_edit_recall | 1.000 |
| length_ratio | 1.12 |
| n_words | 19.0 |
| nli_completeness | 0.904 |
| nli_faithfulness | 0.952 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.167 |
| sari | 53.65 |
| smog | 3.13 |
| smog_drop | 11.43 |
| temporality_preservation | 0.000 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `diarrhea` -> `loose stools` | replace | attributed | 0.836 | 1.095 | 0.430 | 0.769 | 0.013 | - |
| `urinary incontinence` -> `trouble holding her pee` | replace | attributed | 2.943 | 3.073 | 0.868 | 0.933 | 2.361 | - |
| `pedal edema` -> `swollen feet` | replace | attributed | 2.829 | 3.569 | 0.867 | 0.961 | 2.891 | - |

**edit `diarrhea` -> `loose stools`**

- status: `attributed`
- log p full -1.0725, empty -1.9089
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+0.462` [justplainclear] diarrhea: A bowel movement that is loose and watery If your poop is like water or very runny, or if you have m
    - `+0.449` [michigan] diarrhea: Loose, watery stools three or more times a day. It can be sudden (due to a virus, for example), pers
    - `+0.271` [readme] urinary incontinence: When you can't control your pee.
    - `+0.192` [readme] diarrhea: Having loose, watery poop with cramps and bloating.
    - `+0.104` [wiktionary] diarrhea: Diarrhea is an illness where the person's poop or feces are soft like water.

- rationale: The original term refers to the frequent passage of watery or unformed bowel movements, so "loose stools" conveys that same physical symptom in everyday language. Phrase frequency increases from Zipf 3.55 to 3.03, while syllable count decreases from 4 to 2. Patients can now recognize the digestive issue without needing to recall a specific medical label.
- audit: coverage 1.0, grounding_error=True, omission=False, source_ok=True, passage_ok=True

**edit `urinary incontinence` -> `trouble holding her pee`**

- status: `attributed`
- log p full -2.0607, empty -5.0040
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+2.770` [readme] urinary incontinence: When you can't control your pee.
    - `+0.409` [nih] urinary incontinence: Inability to hold urine in the bladder.
    - `+0.043` [nih] diarrhea: Frequent and watery bowel movements.
    - `+0.030` [readme] diarrhea: Having loose, watery poop with cramps and bloating.
    - `-0.020` [readme] Diarrhea: Having runny poop with stomach pains and bloating.

- rationale: The glossary defines the original term as the inability to control urination, so "trouble holding her pee" conveys that loss of control in everyday language. Phrase frequency rises from 2.77 to 3.86, while age of acquisition drops from 14.41 to 5.09. This phrasing allows the patient to immediately grasp the specific physical difficulty without needing medical training.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `pedal edema` -> `swollen feet`**

- status: `attributed`
- log p full -0.6199, empty -3.4490
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+3.095` [readme] pedal edema: Swollen feet.
    - `+0.204` [readme] urinary incontinence: When you can't control your pee.
    - `+0.019` [nih] urinary incontinence: Inability to hold urine in the bladder.
    - `+0.000` [wiktionary] diarrhea: Diarrhea is an illness where the person's poop or feces are soft like water.

- rationale: The glossary defines "pedal edema" as swollen feet, so the replacement keeps that physical description in plain language. Phrase frequency increases from 2.87 to 3.55, while syllable count drops from 5 to 3. Patients can now understand the swelling issue without needing to know the medical term.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

==============================================================================

## Note 43 - `556`

**ORIGINAL**  Description : Nausea and abdominal pain after eating - Gall bladder disease - Laparoscopic cholecystectomy scheduled.

**REFERENCE** Description : Nausea and abdominal pain after eating - Gall bladder disease - keyhole surgery to remove the gall bladder scheduled.

| | FKGL | FRE | SMOG | Coleman-Liau | words |
|---|---:|---:|---:|---:|---:|
| ORIGINAL | 19.43 | -21.11 | 15.90 | 25.65 | 13 |
| REFERENCE | 14.37 | 24.06 | 14.55 | 17.03 | 18 |

### Stage 2 - extraction + classification

| term | kind | category | action | Zipf | AoA | syll |
|---|---|---|---|---:|---:|---:|
| `Laparoscopic cholecystectomy` | phrase | medical_essential | elaborate | 1.73 | None | 10 |
| `Laparoscopic` | word | medical_descriptor | replace | - | - | - |
| `cholecystectomy` | word | medical_essential | elaborate | - | - | - |
| `Gall bladder disease` | phrase | medical_essential | elaborate | 3.12 | 12.44 | 5 |
| `Gall` | word | medical_descriptor | replace | - | - | - |
| `bladder disease` | phrase | medical_essential | elaborate | - | - | - |
| `abdominal pain` | phrase | medical_descriptor | replace | 3.56 | 10.24 | 5 |
| `Nausea` | word | medical_descriptor | replace | 3.54 | 8.63 | 3 |

### Stage 3 - retrieval

coverage **0.5** (2/4), glossary budget 12/16

| term | Zipf stratum | defs | sources | matched via | origin |
|---|---|---:|---|---|---|
| `Laparoscopic cholecystectomy` | very_rare | 0 | - | - | extracted |
| `Laparoscopic` | rare | 2 | readme_lay_vocab.jsonl | exact | split_from_uncovered |
| `cholecystectomy` | very_rare | 3 | justplainclear.json, readme_lay_vocab.jsonl | exact | split_from_uncovered |
| `Gall bladder disease` | rare | 0 | - | - | extracted |
| `Gall` | rare | 2 | wiktionary.json | exact | split_from_uncovered |
| `bladder disease` | uncommon | 1 | justplainclear.json | exact | split_from_uncovered |
| `abdominal pain` | uncommon | 1 | readme_lay_vocab.jsonl | exact | extracted |
| `Nausea` | uncommon | 3 | justplainclear.json, nih.json, wiktionary.json | exact | extracted |

Glossary shown to the model:

1. `[readme]` epigastric abdominal pain: Stomach ache that's felt below the ribs.
2. `[justplainclear]` bladder disease: A disease or disorder of your bladder. Some bladder diseases may include: • urinary incontinence • infection •overactive bladder • bladder cancer
3. `[wiktionary]` gall: If you have the gall to do something, you do it even though it is very rude or unreasonable.
4. `[readme]` laparoscopic: A surgery where a small tube with a camera is used to see inside the body.
5. `[readme]` cholecystectomy: A surgery to remove the gallbladder, a digestion-assisting organ in the stomach.
6. `[nih]` nausea: A feeling of sickness or discomfort in the stomach that may come with an urge to vomit. Nausea is a side effect of some types of cancer therapy.
7. `[wiktionary]` gall: Gall is anger or hatred.
8. `[readme]` Laparoscopic: A surgery that uses a small tube and camera to see inside your body.
9. `[readme]` Cholecystectomy: A surgery to remove the gallbladder, an organ in your stomach that helps with digestion.
10. `[justplainclear]` nausea: Feeling like you want to throw up, stomach feels upset
11. `[justplainclear]` cholecystectomy: A surgery to take out your gallbladder
12. `[wiktionary]` nausea: Nausea is the feeling of discomfort in the stomach, and the person will usually have a strong urge to vomit.

### Stage 4 - arm `naive`

**output:** The patient has nausea and abdominal pain after eating, which suggests gall bladder disease. A laparoscopic cholecystectomy is scheduled.

| metric | value |
|---|---:|
| bertscore_f1 | 0.436 |
| coleman_liau | 16.49 |
| coleman_liau_drop | 9.15 |
| copy_jargon_rate | 1.000 |
| critical_error | 0.000 |
| fkgl | 12.34 |
| fkgl_drop | 7.10 |
| fre | 23.5 |
| fre_gain | 44.6 |
| human_edit_recall | 0.000 |
| length_ratio | 1.06 |
| n_words | 19.0 |
| nli_completeness | 0.328 |
| nli_faithfulness | 0.988 |
| replacement_f1 | 0.000 |
| rewrite_aggressiveness | 1.000 |
| sari | 38.81 |
| smog | 11.21 |
| smog_drop | 4.70 |
| temporality_preservation | 1.000 |

### Stage 4 - arm `termonly`

**output:** She feels sick and has tummy pain after eating. She has gall bladder disease. The doctor plans a surgery to remove her gall bladder through small cuts.

| metric | value |
|---|---:|
| bertscore_f1 | 0.484 |
| coleman_liau | 7.12 |
| coleman_liau_drop | 18.53 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.600 |
| fkgl | 4.09 |
| fkgl_drop | 15.34 |
| fre | 81.8 |
| fre_gain | 102.9 |
| human_edit_recall | 1.000 |
| length_ratio | 1.50 |
| n_words | 27.0 |
| nli_completeness | 0.354 |
| nli_faithfulness | 0.675 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 31.03 |
| smog | 6.43 |
| smog_drop | 9.48 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 2 edits kept

- rejected: DROP noop      'Gall bladder disease' -> 'gall bladder disease'  (nothing changed)

| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `abdominal pain` -> `tummy pain` | replace | - | - | - | - | - | - | - |
| `Laparoscopic cholecystectomy` -> `surgery to remove her gall bladder through small cuts` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** She feels sick and hurts her belly after eating. She has a problem with her gallbladder. The doctor plans a surgery to remove it using a small camera.

| metric | value |
|---|---:|
| bertscore_f1 | 0.379 |
| coleman_liau | 5.89 |
| coleman_liau_drop | 19.76 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.375 |
| fkgl | 5.33 |
| fkgl_drop | 14.11 |
| fre | 73.5 |
| fre_gain | 94.6 |
| human_edit_recall | 1.000 |
| length_ratio | 1.56 |
| n_words | 28.0 |
| nli_completeness | 0.203 |
| nli_faithfulness | 0.661 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.200 |
| sari | 18.01 |
| smog | 8.84 |
| smog_drop | 7.06 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 0 edits kept


==============================================================================

## Note 44 - `618`

**ORIGINAL**  She states that she has underlying history of heart disease but is not able to elaborate to any significant extent.

**REFERENCE** She states that she has underlying history of heart disease but is not able to go into detail to any significant extent.

| | FKGL | FRE | SMOG | Coleman-Liau | words |
|---|---:|---:|---:|---:|---:|
| ORIGINAL | 12.27 | 42.72 | 14.55 | 10.27 | 20 |
| REFERENCE | 12.30 | 46.07 | 13.02 | 8.69 | 22 |

### Stage 2 - extraction + classification

| term | kind | category | action | Zipf | AoA | syll |
|---|---|---|---|---:|---:|---:|
| `to any significant extent` | phrase | general_hard_word | replace | 4.34 | 10.72 | 9 |
| `to` | word | medical_descriptor | replace | - | - | - |
| `any` | word | medical_descriptor | replace | - | - | - |
| `significant` | word | medical_descriptor | replace | - | - | - |
| `extent` | word | medical_descriptor | replace | - | - | - |
| `underlying` | word | general_hard_word | replace | 4.17 | 12.1 | 4 |
| `elaborate` | word | general_hard_word | replace | 4.06 | 11.53 | 3 |
| `states` | word | general_hard_word | replace | 5.52 | None | 1 |

### Stage 3 - retrieval

coverage **0.75** (3/4), glossary budget 16/16

| term | Zipf stratum | defs | sources | matched via | origin |
|---|---|---:|---|---|---|
| `to any significant extent` | uncommon | 0 | - | - | extracted |
| `to` | common | 2 | wiktionary.json | exact | split_from_uncovered |
| `any` | common | 2 | wiktionary.json | exact | split_from_uncovered |
| `significant` | common | 6 | justplainclear.json, michigan_plmd.json, nih.json, thesarus.json, wiktionary.json | exact | split_from_uncovered |
| `extent` | uncommon | 2 | wiktionary.json | exact | split_from_uncovered |
| `underlying` | uncommon | 2 | wiktionary.json | exact | extracted |
| `elaborate` | uncommon | 1 | wiktionary.json | exact | extracted |
| `states` | common | 1 | wiktionary.json | exact | extracted |

Glossary shown to the model:

1. `[wiktionary]` states: A state is a condition or a situation.
2. `[wiktionary]` elaborate: When something is supposed to be elaborated, it is needed to be expanded or add details to.
3. `[wiktionary]` any: some or even the smallest amount or number
4. `[wiktionary]` to: To has no meaning. It is used with a bare infinitival clause.
5. `[wiktionary]` underlying: If x underlies y, x causes y; x is the reason for y.
6. `[wiktionary]` extent: You use "to an extent" to explain how true something is or how much it happens.
7. `[nih]` significant: In statistics, describes a mathematical measure of difference between groups. The difference is said to be significant if it is greater than what might be expected to happen by chance alone. Also called statistically significant.
8. `[wiktionary]` any: it does not matter which
9. `[wiktionary]` to: To shows where something goes, the goal of movement.
10. `[wiktionary]` underlying: An underlying cause, problem, or assumption, is important but hard to notice.
11. `[wiktionary]` extent: The extent of something is how far it goes, how much area it covers, or how much it does.
12. `[michigan]` significant: Big or important.
13. `[justplainclear]` significant: Big, serious, important, major
14. `[wiktionary]` significant: If something is significant, it is important, or large, enough to pay attention to or to believe.
15. `[wiktionary]` significant: A significant look, movement, etc. is one that has a particular meaning.
16. `[thesaurus]` significant: big, serious, important

### Stage 4 - arm `naive`

**output:** She says she has a history of heart disease, but she cannot explain much about it.

| metric | value |
|---|---:|
| bertscore_f1 | 0.596 |
| coleman_liau | 5.91 |
| coleman_liau_drop | 4.36 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.125 |
| fkgl | 6.88 |
| fkgl_drop | 5.39 |
| fre | 74.3 |
| fre_gain | 31.6 |
| human_edit_recall | 1.000 |
| length_ratio | 0.73 |
| n_words | 16.0 |
| negation_preservation | 0.000 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.995 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.250 |
| sari | 19.50 |
| severity_downgrade | 1.000 |
| severity_preservation | 0.000 |
| severity_tier_input | 2.000 |
| smog | 8.84 |
| smog_drop | 5.71 |
| temporality_preservation | 1.000 |

### Stage 4 - arm `termonly`

**output:** She says she has a past heart problem but cannot explain much.

| metric | value |
|---|---:|
| bertscore_f1 | 0.514 |
| coleman_liau | 5.90 |
| coleman_liau_drop | 4.37 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.250 |
| fkgl | 3.84 |
| fkgl_drop | 8.43 |
| fre | 88.9 |
| fre_gain | 46.2 |
| human_edit_recall | 1.000 |
| length_ratio | 0.55 |
| n_words | 12.0 |
| negation_preservation | 0.000 |
| nli_completeness | 0.992 |
| nli_faithfulness | 0.994 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.400 |
| sari | 9.23 |
| severity_downgrade | 1.000 |
| severity_preservation | 0.000 |
| severity_tier_input | 2.000 |
| smog | 3.13 |
| smog_drop | 11.43 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 3 edits kept

- rejected: DROP non-term  'heart disease' -> 'heart problem'  (orig is not exactly one extracted hard term)

| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `underlying` -> `past` | replace | - | - | - | - | - | - | - |
| `elaborate` -> `explain` | replace | - | - | - | - | - | - | - |
| `to any significant extent` -> `much` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** She says she has a past heart problem but cannot explain much.

| metric | value |
|---|---:|
| bertscore_f1 | 0.514 |
| coleman_liau | 5.90 |
| coleman_liau_drop | 4.37 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.250 |
| fkgl | 3.84 |
| fkgl_drop | 8.43 |
| fre | 88.9 |
| fre_gain | 46.2 |
| human_edit_recall | 1.000 |
| length_ratio | 0.55 |
| n_words | 12.0 |
| negation_preservation | 0.000 |
| nli_completeness | 0.992 |
| nli_faithfulness | 0.994 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.400 |
| sari | 9.23 |
| severity_downgrade | 1.000 |
| severity_preservation | 0.000 |
| severity_tier_input | 2.000 |
| smog | 3.13 |
| smog_drop | 11.43 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 3 edits kept

- rejected: DROP non-term  'heart disease' -> 'heart problem'  (orig is not exactly one extracted hard term)

| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `underlying` -> `past` | replace | attributed | 0.150 | 0.229 | 0.626 | 0.819 | 0.066 | - |
| `elaborate` -> `explain` | replace | attributed | -0.919 | -1.808 | 0.891 | 0.933 | 0.007 | - |
| `to any significant extent` -> `much` | replace | attributed | -0.286 | -0.546 | 0.470 | 0.732 | 0.014 | - |

**edit `underlying` -> `past`**

- status: `attributed`
- log p full -0.9905, empty -1.1402
- masks scored: 66/66 (+5 top-k)
- ranked sources:
    - `+0.237` [wiktionary] elaborate: When something is supposed to be elaborated, it is needed to be expanded or add details to.
    - `+0.171` [wiktionary] underlying: An underlying cause, problem, or assumption, is important but hard to notice.
    - `+0.028` [wiktionary] any: some or even the smallest amount or number
    - `+0.013` [wiktionary] extent: The extent of something is how far it goes, how much area it covers, or how much it does.
    - `+0.001` [nih] significant: In statistics, describes a mathematical measure of difference between groups. The difference is s

- rationale: The original term "underlying" refers to a cause or condition that exists before and supports the current situation, so "past" captures that sense of something that came earlier in plain words. Phrase frequency increases from Zipf 4.17 to 5.36, while age of acquisition drops from 12.10 to 6.78. Patients can now grasp the timeline of the issue without needing to know the specific medical nuance of the original adjective.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `elaborate` -> `explain`**

- status: `attributed`
- log p full -1.2698, empty -0.3507
- masks scored: 66/66 (+5 top-k)
- ranked sources:
    - `+0.129` [nih] significant: In statistics, describes a mathematical measure of difference between groups. The difference is s
    - `+0.122` [michigan] significant: Big or important.
    - `+0.095` [wiktionary] underlying: If x underlies y, x causes y; x is the reason for y.
    - `+0.016` [wiktionary] any: some or even the smallest amount or number

- rationale: The original term "elaborate" means to provide a detailed explanation, so "explain" keeps that core idea in simpler language. Phrase frequency increases from Zipf 4.06 to 4.89, while age of acquisition drops from 11.53 to 6.50. Patients can now grasp the instruction to clarify their condition without needing to process a complex verb.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `to any significant extent` -> `much`**

- status: `attributed`
- log p full -0.8954, empty -0.6092
- masks scored: 66/66 (+5 top-k)
- ranked sources:
    - `+0.025` [wiktionary] elaborate: When something is supposed to be elaborated, it is needed to be expanded or add details to.
    - `+0.011` [wiktionary] extent: The extent of something is how far it goes, how much area it covers, or how much it does.
    - `+0.004` [wiktionary] any: some or even the smallest amount or number

- rationale: The original phrase "to any significant extent" means a large degree or a great amount, which the single word "much" captures in a simpler way. Phrase frequency rises from Zipf 4.34 to 6.00, while age of acquisition drops from 10.72 to 4.58. This change allows the reader to grasp the intensity of the situation immediately without needing to parse a longer, more complex expression.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

==============================================================================

## Note 45 - `661`

**ORIGINAL**  There was some slight edema of the fourth digit, on which he still is wearing his wedding band.

**REFERENCE** There was some slight swelling of the fourth finger, on which he still is wearing his wedding band.

| | FKGL | FRE | SMOG | Coleman-Liau | words |
|---|---:|---:|---:|---:|---:|
| ORIGINAL | 6.51 | 80.47 | 8.84 | 7.04 | 18 |
| REFERENCE | 5.85 | 85.16 | 3.13 | 8.33 | 18 |

### Stage 2 - extraction + classification

| term | kind | category | action | Zipf | AoA | syll |
|---|---|---|---|---:|---:|---:|
| `fourth digit` | phrase | medical_descriptor | replace | 3.73 | 9.26 | 3 |
| `fourth` | word | medical_descriptor | replace | - | - | - |
| `digit` | word | medical_descriptor | replace | - | - | - |
| `edema` | word | medical_descriptor | replace | 2.95 | 15.07 | 3 |

### Stage 3 - retrieval

coverage **0.5** (1/2), glossary budget 11/16

| term | Zipf stratum | defs | sources | matched via | origin |
|---|---|---:|---|---|---|
| `fourth digit` | uncommon | 0 | - | - | extracted |
| `fourth` | common | 2 | wiktionary.json | exact | split_from_uncovered |
| `digit` | uncommon | 4 | michigan_plmd.json, readme_lay_vocab.jsonl, wiktionary.json | exact | split_from_uncovered |
| `edema` | rare | 5 | iowa.json, michigan_plmd.json, nih.json, readme_lay_vocab.jsonl | exact | extracted |

Glossary shown to the model:

1. `[wiktionary]` fourth: The fourth thing is something that is number four (4) in order.
2. `[readme]` digit: A digit is a finger or toe.
3. `[readme]` Edema: Swelling in the body caused by too much fluid.
4. `[wiktionary]` fourth: A fourth of something is one of four equal parts of that thing; a quarter.
5. `[readme]` DIGIT: A digit is a finger or a toe.
6. `[readme]` edema: Swelling due to too much fluid in the body tissues.
7. `[michigan]` digit: A finger or toe.
8. `[nih]` edema: Swelling caused by excess fluid in body tissues.
9. `[wiktionary]` digit: A digit is any of the numerals from 0 to 9, especially when forming part of a number.
10. `[iowa]` EDEMA: excess fluid collecting in tissue
11. `[michigan]` edema: Swelling caused by too much fluid in your body.

### Stage 4 - arm `naive`

**output:** There was a little swelling on his fourth finger, where he still wears his wedding ring.

| metric | value |
|---|---:|
| bertscore_f1 | 0.798 |
| coleman_liau | 8.09 |
| coleman_liau_drop | -1.04 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.667 |
| fkgl | 5.40 |
| fkgl_drop | 1.11 |
| fre | 84.8 |
| fre_gain | 4.4 |
| human_edit_recall | 1.000 |
| length_ratio | 0.89 |
| n_words | 16.0 |
| nli_completeness | 0.993 |
| nli_faithfulness | 0.993 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.714 |
| sari | 25.04 |
| severity_downgrade | 0.000 |
| severity_preservation | 0.000 |
| severity_tier_input | 1.000 |
| severity_tier_output | 1.000 |
| smog | 3.13 |
| smog_drop | 5.71 |

### Stage 4 - arm `termonly`

**output:** There was slight swelling on his fourth finger, where he still wears his wedding ring.

| metric | value |
|---|---:|
| bertscore_f1 | 0.802 |
| coleman_liau | 9.29 |
| coleman_liau_drop | -2.25 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.667 |
| fkgl | 4.42 |
| fkgl_drop | 2.09 |
| fre | 90.1 |
| fre_gain | 9.6 |
| human_edit_recall | 1.000 |
| length_ratio | 0.83 |
| n_words | 15.0 |
| nli_completeness | 0.992 |
| nli_faithfulness | 0.992 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.667 |
| sari | 27.91 |
| severity_downgrade | 0.000 |
| severity_preservation | 1.000 |
| severity_tier_input | 1.000 |
| severity_tier_output | 1.000 |
| smog | 3.13 |
| smog_drop | 5.71 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `edema` -> `swelling` | replace | - | - | - | - | - | - | - |
| `fourth digit` -> `fourth finger` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** There was slight swelling on his fourth finger, where he still wears his wedding band.

| metric | value |
|---|---:|
| bertscore_f1 | 0.835 |
| coleman_liau | 9.29 |
| coleman_liau_drop | -2.25 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.667 |
| fkgl | 4.42 |
| fkgl_drop | 2.09 |
| fre | 90.1 |
| fre_gain | 9.6 |
| human_edit_recall | 1.000 |
| length_ratio | 0.83 |
| n_words | 15.0 |
| nli_completeness | 0.993 |
| nli_faithfulness | 0.993 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.600 |
| sari | 32.21 |
| severity_downgrade | 0.000 |
| severity_preservation | 1.000 |
| severity_tier_input | 1.000 |
| severity_tier_output | 1.000 |
| smog | 3.13 |
| smog_drop | 5.71 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `edema` -> `swelling` | replace | attributed | 0.013 | 1.184 | 0.488 | 0.822 | 0.160 | - |
| `fourth digit` -> `fourth finger` | replace | attributed | 0.172 | 0.693 | 0.849 | 0.955 | 0.408 | - |

**edit `edema` -> `swelling`**

- status: `attributed`
- log p full -0.0059, empty -0.0192
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.337` [readme] DIGIT: A digit is a finger or a toe.
    - `+0.178` [nih] edema: Swelling caused by excess fluid in body tissues.
    - `+0.163` [readme] digit: A digit is a finger or toe.
    - `+0.158` [wiktionary] digit: A digit is any of the numerals from 0 to 9, especially when forming part of a number.
    - `+0.037` [readme] Edema: Swelling in the body caused by too much fluid.

- rationale: The original term refers to fluid buildup in the body tissues, so "swelling" conveys that physical expansion in plain language. Phrase frequency increases from Zipf 2.95 to 3.68, while syllable count drops from 3 to 2. Patients can now recognize the visible symptom without needing to know the medical label.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `fourth digit` -> `fourth finger`**

- status: `attributed`
- log p full -0.2081, empty -0.3804
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.440` [wiktionary] fourth: The fourth thing is something that is number four (4) in order.
    - `+0.032` [michigan] edema: Swelling caused by too much fluid in your body.

- rationale: The original term refers to the hand's index finger, so "fourth finger" keeps that specific body part in plain language. Phrase frequency increases from 3.73 to 4.32, while age of acquisition drops from 9.26 to 4.68. Patients can now identify the exact digit on their hand without needing specialized anatomical knowledge.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

==============================================================================

## Note 46 - `669`

**ORIGINAL**  Parents do state that she does appear to breathe rapidly, tires somewhat with the feeding with increased respiratory effort and diaphoresis.

**REFERENCE** Parents do state that she does appear to breathe quickly, tires somewhat with the feeding with increased breathing effort and sweating.

| | FKGL | FRE | SMOG | Coleman-Liau | words |
|---|---:|---:|---:|---:|---:|
| ORIGINAL | 12.83 | 40.49 | 13.02 | 15.38 | 21 |
| REFERENCE | 10.02 | 60.63 | 3.13 | 14.00 | 21 |

### Stage 2 - extraction + classification

| term | kind | category | action | Zipf | AoA | syll |
|---|---|---|---|---:|---:|---:|
| `respiratory effort` | phrase | medical_descriptor | replace | 3.78 | 11.0 | 7 |
| `respiratory` | word | medical_descriptor | replace | - | - | - |
| `effort` | word | medical_descriptor | replace | - | - | - |
| `diaphoresis` | word | medical_descriptor | replace | 1.28 | 15.22 | 3 |
| `rapidly` | word | general_hard_word | replace | 4.34 | None | 3 |
| `state` | word | general_hard_word | replace | 5.78 | 6.39 | 1 |

### Stage 3 - retrieval

coverage **0.75** (3/4), glossary budget 13/16

| term | Zipf stratum | defs | sources | matched via | origin |
|---|---|---:|---|---|---|
| `respiratory effort` | uncommon | 0 | - | - | extracted |
| `respiratory` | uncommon | 3 | readme_lay_vocab.jsonl, wiktionary.json | exact | split_from_uncovered |
| `effort` | common | 1 | wiktionary.json | exact | split_from_uncovered |
| `diaphoresis` | very_rare | 4 | justplainclear.json, michigan_plmd.json, readme_lay_vocab.jsonl | exact | extracted |
| `rapidly` | uncommon | 1 | wiktionary.json | exact | extracted |
| `state` | common | 4 | michigan_plmd.json, thesarus.json, wiktionary.json | exact | extracted |

Glossary shown to the model:

1. `[wiktionary]` effort: The amount of work that is done on something.
2. `[wiktionary]` rapidly: If something is done rapidly, then it is done quickly or swiftly.
3. `[readme]` RESPIRATORY: Related to breathing or the lungs and airways.
4. `[readme]` diaphoresis: Heavy sweating.
5. `[michigan]` state: To say or tell. In medicine, how you are doing.
6. `[readme]` Respiratory: Related to how you breathe and the organs involved in breathing like the lungs and airways.
7. `[readme]` Diaphoresis: Intense sweating.
8. `[wiktionary]` state: A state is a condition or a situation.
9. `[wiktionary]` respiratory: A respiratory problem refers to something that affects breathing or the lungs.
10. `[michigan]` diaphoresis: Sweating, a clear, salty liquid produced by glands in your skin. Sweating is how your body cools itself. Also called persperation.
11. `[wiktionary]` state: Any sovereign nation (nation that rules itself) is a state.
12. `[justplainclear]` diaphoresis: Sweating
13. `[thesaurus]` state: say, tell, condition

### Stage 4 - arm `naive`

**output:** Parents say that she seems to breathe quickly, gets tired a bit while eating, and shows signs of working hard to breathe and sweating.

| metric | value |
|---|---:|
| bertscore_f1 | 0.558 |
| coleman_liau | 9.07 |
| coleman_liau_drop | 6.31 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.667 |
| fkgl | 8.52 |
| fkgl_drop | 4.31 |
| fre | 76.7 |
| fre_gain | 36.2 |
| human_edit_recall | 1.000 |
| length_ratio | 1.14 |
| n_words | 24.0 |
| nli_completeness | 0.939 |
| nli_faithfulness | 0.841 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.545 |
| sari | 20.64 |
| smog | 3.13 |
| smog_drop | 9.89 |

### Stage 4 - arm `termonly`

**output:** Parents say she breathes fast, gets tired feeding, and sweats while breathing hard.

| metric | value |
|---|---:|
| bertscore_f1 | 0.484 |
| coleman_liau | 12.26 |
| coleman_liau_drop | 3.12 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.333 |
| fkgl | 4.91 |
| fkgl_drop | 7.92 |
| fre | 83.0 |
| fre_gain | 42.5 |
| human_edit_recall | 1.000 |
| length_ratio | 0.62 |
| n_words | 13.0 |
| nli_completeness | 0.851 |
| nli_faithfulness | 0.127 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.545 |
| sari | 14.75 |
| smog | 3.13 |
| smog_drop | 9.89 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `rapidly` -> `fast` | replace | - | - | - | - | - | - | - |
| `diaphoresis` -> `sweats` | replace | - | - | - | - | - | - | - |
| `respiratory effort` -> `hard` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Parents say she breathes quickly, gets tired while eating, and sweats heavily while breathing hard.

| metric | value |
|---|---:|
| bertscore_f1 | 0.440 |
| coleman_liau | 13.93 |
| coleman_liau_drop | 1.45 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 7.57 |
| fkgl_drop | 5.26 |
| fre | 67.5 |
| fre_gain | 27.0 |
| human_edit_recall | 1.000 |
| length_ratio | 0.71 |
| n_words | 15.0 |
| nli_completeness | 0.867 |
| nli_faithfulness | 0.036 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.583 |
| sari | 15.01 |
| smog | 8.84 |
| smog_drop | 4.18 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `rapidly` -> `quickly` | replace | attributed | 2.085 | 3.694 | 0.797 | 0.921 | 3.864 | - |
| `diaphoresis` -> `sweats heavily` | replace | attributed | 3.042 | 3.317 | 0.837 | 0.842 | 1.609 | - |

**edit `rapidly` -> `quickly`**

- status: `attributed`
- log p full -0.1980, empty -2.2826
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+3.965` [wiktionary] rapidly: If something is done rapidly, then it is done quickly or swiftly.
    - `+0.102` [thesaurus] state: say, tell, condition
    - `+0.046` [readme] diaphoresis: Heavy sweating.
    - `+0.021` [wiktionary] effort: The amount of work that is done on something.

- rationale: The glossary defines "rapidly" as being done quickly or swiftly, so "quickly" keeps that sense of speed in plain words. Word frequency increases from Zipf 4.34 to 5.00, while syllable count drops from 3 to 2. Patients can now grasp the urgency of the action without needing to process a more complex adverb.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `diaphoresis` -> `sweats heavily`**

- status: `attributed`
- log p full -1.3872, empty -4.4287
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+2.487` [readme] diaphoresis: Heavy sweating.
    - `+0.878` [readme] Diaphoresis: Intense sweating.
    - `+0.213` [wiktionary] state: Any sovereign nation (nation that rules itself) is a state.
    - `+0.061` [wiktionary] state: A state is a condition or a situation.
    - `+0.037` [wiktionary] respiratory: A respiratory problem refers to something that affects breathing or the lungs.

- rationale: The glossary defines diaphoresis as heavy sweating, so "sweats heavily" keeps that central physical symptom in plain language. Phrase frequency increases from 1.28 to 3.08, while syllable count rises from 3 to 4. Patients can now recognize the symptom of excessive sweating without needing to know the medical term.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

==============================================================================

## Note 47 - `673`

**ORIGINAL**  The patient has not used amphetamines for at least four to five months, according to the patient ; however, he had onset of chest pain this evening.

**REFERENCE** The patient has not used amphetamines for at least four to five months, according to the patient ; however, he had chest pain this evening.

| | FKGL | FRE | SMOG | Coleman-Liau | words |
|---|---:|---:|---:|---:|---:|
| ORIGINAL | 11.34 | 60.05 | 13.02 | 9.38 | 26 |
| REFERENCE | 10.49 | 62.63 | 13.02 | 9.79 | 24 |

### Stage 2 - extraction + classification

| term | kind | category | action | Zipf | AoA | syll |
|---|---|---|---|---:|---:|---:|
| `amphetamines` | word | medical_essential | elaborate | 2.82 | None | 4 |
| `onset` | word | general_hard_word | replace | 3.72 | 10.72 | 2 |

### Stage 3 - retrieval

coverage **1.0** (2/2), glossary budget 3/16

| term | Zipf stratum | defs | sources | matched via | origin |
|---|---|---:|---|---|---|
| `amphetamines` | rare | 1 | wiktionary.json | exact | extracted |
| `onset` | uncommon | 2 | michigan_plmd.json, wiktionary.json | exact | extracted |

Glossary shown to the model:

1. `[wiktionary]` amphetamines: Amphetamine is a synthetic drug. It is a stimulant that helps people keep the focus and stay awake.
2. `[michigan]` onset: The start.
3. `[wiktionary]` onset: The onset of something is the time when it begins (usually something bad).

### Stage 4 - arm `naive`

**output:** The patient says he has not used amphetamines for at least four to five months, but he started having chest pain this evening.

| metric | value |
|---|---:|
| bertscore_f1 | 0.821 |
| coleman_liau | 8.63 |
| coleman_liau_drop | 0.75 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 8.77 |
| fkgl_drop | 2.57 |
| fre | 73.1 |
| fre_gain | 13.1 |
| human_edit_recall | 1.000 |
| length_ratio | 0.96 |
| n_words | 23.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.995 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.667 |
| sari | 37.20 |
| smog | 8.84 |
| smog_drop | 4.18 |

### Stage 4 - arm `termonly`

**output:** The patient has not used amphetamines for at least four to five months, according to the patient ; however, he had onset of chest pain this evening.

| metric | value |
|---|---:|
| bertscore_f1 | 0.960 |
| coleman_liau | 9.38 |
| coleman_liau_drop | 0.00 |
| copy_jargon_rate | 1.000 |
| critical_error | 0.000 |
| fkgl | 11.34 |
| fkgl_drop | 0.00 |
| fre | 60.1 |
| fre_gain | 0.0 |
| human_edit_recall | 0.000 |
| length_ratio | 1.08 |
| n_words | 26.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.994 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 30.69 |
| smog | 13.02 |
| smog_drop | 0.00 |

annotation backend `novita`, 0 edits kept


### Stage 4 - arm `grounded`

**output:** The patient has not used a stimulant for at least four to five months, according to the patient; however, he had the start of chest pain this evening.

| metric | value |
|---|---:|
| bertscore_f1 | 0.818 |
| coleman_liau | 7.79 |
| coleman_liau_drop | 1.59 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 10.92 |
| fkgl_drop | 0.42 |
| fre | 66.6 |
| fre_gain | 6.6 |
| human_edit_recall | 1.000 |
| length_ratio | 1.17 |
| n_words | 28.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.269 |
| nli_faithfulness | 0.981 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 46.93 |
| smog | 13.02 |
| smog_drop | 0.00 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `amphetamines` -> `a stimulant` | replace | attributed | 1.231 | 1.371 | - | 0.833 | 1.976 | - |
| `onset` -> `the start` | replace | attributed | 1.359 | 1.971 | - | 0.929 | 1.145 | - |

**edit `amphetamines` -> `a stimulant`**

- status: `attributed`
- log p full -1.7430, empty -2.9737
- masks scored: 10/10 (+3 top-k)
- ranked sources:
    - `+1.910` [wiktionary] amphetamines: Amphetamine is a synthetic drug. It is a stimulant that helps people keep the focus and stay awa
    - `-0.066` [wiktionary] onset: The onset of something is the time when it begins (usually something bad).
    - `-0.371` [michigan] onset: The start.

- rationale: Amphetamines are a type of drug that increases alertness and energy, so "a stimulant" keeps that core function in plain language. Phrase frequency increases from Zipf 2.82 to 3.06, while syllable count remains at 4. Patients can recognize the drug's effect on the body without needing to know the specific chemical name.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `onset` -> `the start`**

- status: `attributed`
- log p full -0.6321, empty -1.9913
- masks scored: 10/10 (+3 top-k)
- ranked sources:
    - `+1.625` [michigan] onset: The start.
    - `+0.480` [wiktionary] amphetamines: Amphetamine is a synthetic drug. It is a stimulant that helps people keep the focus and stay awa
    - `-0.227` [wiktionary] onset: The onset of something is the time when it begins (usually something bad).

- rationale: The original term "onset" refers to the point in time when a condition or event begins, and "the start" conveys this exact moment in simple language. Phrase frequency rises from 3.72 to 5.56, while age of acquisition drops from 10.72 to 4.37. Patients can now immediately recognize when a symptom begins without needing to know the specific medical vocabulary.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

==============================================================================

## Note 48 - `675`

**ORIGINAL**  Orogastric suction carried out with only scant clear stomach contents.

**REFERENCE** Suction of stomach through the mouth carried out with only a small amount clear stomach contents

| | FKGL | FRE | SMOG | Coleman-Liau | words |
|---|---:|---:|---:|---:|---:|
| ORIGINAL | 8.37 | 52.87 | 8.84 | 16.04 | 10 |
| REFERENCE | 7.61 | 68.98 | 3.13 | 11.71 | 16 |

### Stage 2 - extraction + classification

| term | kind | category | action | Zipf | AoA | syll |
|---|---|---|---|---:|---:|---:|
| `clear stomach contents` | phrase | medical_descriptor | replace | 3.96 | 8.5 | 5 |
| `clear` | word | medical_descriptor | replace | - | - | - |
| `stomach` | word | medical_descriptor | replace | - | - | - |
| `contents` | word | medical_descriptor | replace | - | - | - |
| `Orogastric suction` | phrase | medical_essential | elaborate | 0.0 | 9.42 | 5 |
| `Orogastric` | word | medical_descriptor | replace | - | - | - |
| `suction` | word | medical_descriptor | replace | - | - | - |
| `carried out` | phrase | general_hard_word | replace | 4.76 | 3.28 | 3 |
| `carried` | word | medical_descriptor | replace | - | - | - |
| `out` | word | medical_descriptor | replace | - | - | - |
| `scant` | word | general_hard_word | replace | 3.1 | 12.16 | 1 |

### Stage 3 - retrieval

coverage **0.25** (1/4), glossary budget 16/16

| term | Zipf stratum | defs | sources | matched via | origin |
|---|---|---:|---|---|---|
| `clear stomach contents` | uncommon | 0 | - | - | extracted |
| `clear` | common | 2 | wiktionary.json | exact | split_from_uncovered |
| `stomach` | uncommon | 5 | justplainclear.json, michigan_plmd.json, nih.json, wiktionary.json | exact | split_from_uncovered |
| `contents` | uncommon | 1 | wiktionary.json | exact | split_from_uncovered |
| `Orogastric suction` | very_rare | 0 | - | - | extracted |
| `Orogastric` | very_rare | 1 | readme_lay_vocab.jsonl | exact | split_from_uncovered |
| `suction` | rare | 3 | readme_lay_vocab.jsonl, wiktionary.json | exact | split_from_uncovered |
| `carried out` | common | 0 | - | - | extracted |
| `carried` | common | 1 | wiktionary.json | exact | split_from_uncovered |
| `out` | common | 2 | wiktionary.json | exact | split_from_uncovered |
| `scant` | rare | 2 | wiktionary.json | exact | extracted |

Glossary shown to the model:

1. `[wiktionary]` carried: If you carry something, you lift it up and move it to another place.
2. `[readme]` orogastric: A tube inserted through the mouth to deliver food and medication directly to the stomach.
3. `[wiktionary]` contents: The contents of a container, such as a bag, a file, a book etc., are the things that are in it.
4. `[wiktionary]` scant: If something is scant, there is very little or very few of it; very little, very few.
5. `[wiktionary]` out: Something that is out is not in.
6. `[wiktionary]` clear: A clear idea is an idea that is easy to understand.
7. `[readme]` suction: Suction is when a machine pulls in gas, liquid, or mucus.
8. `[nih]` stomach: An organ that is part of the digestive system. The stomach helps digest food by mixing it with digestive juices and churning it into a thin liquid.
9. `[wiktionary]` scant: A scant is a sheet of stone.
10. `[wiktionary]` out: If something using electricity is out, it is turned off or the electricity is not flowing..
11. `[wiktionary]` clear: If it is clear that something is a certain way, there can be no mistake about it.
12. `[wiktionary]` suction: Suction is a force which pushes matter from one space into another due to the pressure difference in pressure between the two spaces
13. `[michigan]` stomach: The place in your upper belly where food is first broken down (digested). It is between the tube that takes food from your mouth to your stomach (esophagus) and your small intestine.
14. `[wiktionary]` suction: A suction is a device that removes saliva from a patient's mouth during dental operations.
15. `[justplainclear]` stomach: A part of the body where food is digested Parts of the digestive system showing the stomach
16. `[wiktionary]` stomach: The place in the body where food is digested.

### Stage 4 - arm `naive`

**output:** A tube was placed in the patient's mouth to remove stomach contents, but there was very little clear liquid inside.

| metric | value |
|---|---:|
| bertscore_f1 | 0.339 |
| coleman_liau | 9.69 |
| coleman_liau_drop | 6.35 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.375 |
| fkgl | 8.73 |
| fkgl_drop | -0.36 |
| fre | 68.1 |
| fre_gain | 15.2 |
| human_edit_recall | 1.000 |
| length_ratio | 1.31 |
| n_words | 21.0 |
| nli_completeness | 0.950 |
| nli_faithfulness | 0.788 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.167 |
| sari | 28.31 |
| smog | 3.13 |
| smog_drop | 5.71 |

### Stage 4 - arm `termonly`

**output:** A tube through the mouth removed very little clear liquid from the stomach.

| metric | value |
|---|---:|
| bertscore_f1 | 0.429 |
| coleman_liau | 9.58 |
| coleman_liau_drop | 6.46 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.333 |
| fkgl | 5.82 |
| fkgl_drop | 2.55 |
| fre | 76.5 |
| fre_gain | 23.6 |
| human_edit_recall | 1.000 |
| length_ratio | 0.81 |
| n_words | 13.0 |
| nli_completeness | 0.953 |
| nli_faithfulness | 0.924 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.143 |
| sari | 27.67 |
| smog | 3.13 |
| smog_drop | 5.71 |

annotation backend `novita`, 0 edits kept


### Stage 4 - arm `grounded`

**output:** A tube through the mouth pulled out very little clear liquid from the stomach.

| metric | value |
|---|---:|
| bertscore_f1 | 0.401 |
| coleman_liau | 8.60 |
| coleman_liau_drop | 7.44 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.375 |
| fkgl | 5.04 |
| fkgl_drop | 3.33 |
| fre | 83.9 |
| fre_gain | 31.0 |
| human_edit_recall | 1.000 |
| length_ratio | 0.88 |
| n_words | 14.0 |
| nli_completeness | 0.954 |
| nli_faithfulness | 0.929 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.167 |
| sari | 29.08 |
| smog | 3.13 |
| smog_drop | 5.71 |

annotation backend `novita`, 0 edits kept


==============================================================================

## Note 49 - `680`

**ORIGINAL**  Probably there is some restrictive element because of fibrosis.

**REFERENCE** Probably there is some restrictive element because of scarring of tissues.

| | FKGL | FRE | SMOG | Coleman-Liau | words |
|---|---:|---:|---:|---:|---:|
| ORIGINAL | 11.52 | 28.50 | 14.55 | 15.71 | 9 |
| REFERENCE | 10.15 | 41.85 | 13.02 | 14.73 | 11 |

### Stage 2 - extraction + classification

| term | kind | category | action | Zipf | AoA | syll |
|---|---|---|---|---:|---:|---:|
| `restrictive element` | phrase | medical_descriptor | replace | 3.49 | 11.0 | 6 |
| `restrictive` | word | medical_descriptor | replace | - | - | - |
| `element` | word | medical_descriptor | replace | - | - | - |
| `fibrosis` | word | medical_essential | elaborate | 3.19 | 14.94 | 3 |

### Stage 3 - retrieval

coverage **0.5** (1/2), glossary budget 6/16

| term | Zipf stratum | defs | sources | matched via | origin |
|---|---|---:|---|---|---|
| `restrictive element` | uncommon | 0 | - | - | extracted |
| `restrictive` | uncommon | 1 | wiktionary.json | exact | split_from_uncovered |
| `element` | uncommon | 3 | nih.json, wiktionary.json | exact | split_from_uncovered |
| `fibrosis` | rare | 2 | nih.json, readme_lay_vocab.jsonl | exact | extracted |

Glossary shown to the model:

1. `[wiktionary]` restrictive: If something is restrictive, it limits or controls what people can do.
2. `[readme]` FIBROSIS: Fibrosis is tissue that becomes thick and scarred due to injury.
3. `[nih]` element: A basic part of a whole. In chemistry, refers to a simple substance that cannot be broken down into smaller parts or changed into another substance. The basic part of an element is an atom, which contains protons, neutrons, and electrons. All atoms of an element have the same number of protons. Examples of elements are hydrogen, carbon, oxygen, nitrogen, and calcium.
4. `[nih]` fibrosis: The growth of fibrous tissue.
5. `[wiktionary]` element: An element is one part of something bigger, such as a plan, an engine, or a business.
6. `[wiktionary]` element: An element is one basic kind of substance, such as iron (Fe), oxygen (O), or sodium (Na).

### Stage 4 - arm `naive`

**output:** There is likely a restrictive problem because of fibrosis.

| metric | value |
|---|---:|
| bertscore_f1 | 0.464 |
| coleman_liau | 12.49 |
| coleman_liau_drop | 3.22 |
| copy_jargon_rate | 1.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 8.90 |
| fkgl_drop | 2.62 |
| fre | 47.3 |
| fre_gain | 18.8 |
| human_edit_recall | 0.000 |
| length_ratio | 0.82 |
| n_words | 9.0 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.992 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.667 |
| sari | 10.67 |
| smog | 11.21 |
| smog_drop | 3.35 |
| uncertainty_preservation | 1.000 |

### Stage 4 - arm `termonly`

**output:** Probably there is some trouble breathing because of scarring in the lungs.

| metric | value |
|---|---:|
| bertscore_f1 | 0.598 |
| coleman_liau | 11.70 |
| coleman_liau_drop | 4.01 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 6.79 |
| fkgl_drop | 4.73 |
| fre | 67.8 |
| fre_gain | 39.2 |
| human_edit_recall | 1.000 |
| length_ratio | 1.09 |
| n_words | 12.0 |
| nli_completeness | 0.975 |
| nli_faithfulness | 0.179 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 33.61 |
| smog | 8.84 |
| smog_drop | 5.71 |
| uncertainty_preservation | 1.000 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `restrictive element` -> `trouble breathing` | replace | - | - | - | - | - | - | - |
| `fibrosis` -> `scarring in the lungs` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Probably there is some thick, scarred tissue limiting how the lungs work.

| metric | value |
|---|---:|
| bertscore_f1 | 0.537 |
| coleman_liau | 10.73 |
| coleman_liau_drop | 4.98 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.250 |
| fkgl | 5.81 |
| fkgl_drop | 5.71 |
| fre | 74.8 |
| fre_gain | 46.3 |
| human_edit_recall | 1.000 |
| length_ratio | 1.09 |
| n_words | 12.0 |
| nli_completeness | 0.647 |
| nli_faithfulness | 0.074 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.250 |
| sari | 24.17 |
| smog | 11.21 |
| smog_drop | 3.35 |
| uncertainty_preservation | 1.000 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `restrictive element` -> `thick, scarred tissue limiting how the lungs work` | replace | attributed | 19.893 | 19.893 | 0.964 | 0.960 | 8.739 | - |

**edit `restrictive element` -> `thick, scarred tissue limiting how the lungs work`**

- status: `attributed`
- log p full -7.1456, empty -27.0381
- masks scored: 66/66 (+2 top-k)
- ranked sources:
    - `+12.825` [readme] FIBROSIS: Fibrosis is tissue that becomes thick and scarred due to injury.
    - `+4.086` [wiktionary] restrictive: If something is restrictive, it limits or controls what people can do.
    - `+1.152` [nih] fibrosis: The growth of fibrous tissue.

- rationale: The original term refers to a lung structure that is stiff and damaged, preventing normal expansion, so the replacement describes this thick, scarred tissue limiting how the lungs work in plain language. Phrase frequency increases from 3.49 to 3.08, while age of acquisition drops from 11.00 to 5.86. Patients can now grasp the physical barrier to breathing without needing to know the technical classification.
- audit: coverage 1.0, grounding_error=True, omission=False, source_ok=True, passage_ok=True

==============================================================================

## Note 50 - `681`

**ORIGINAL**  The uterus was placed back into the abdominal cavity.

**REFERENCE** The womb was placed back into the abdomen

| | FKGL | FRE | SMOG | Coleman-Liau | words |
|---|---:|---:|---:|---:|---:|
| ORIGINAL | 10.21 | 37.90 | 13.02 | 9.27 | 9 |
| REFERENCE | 3.76 | 82.39 | 8.84 | 5.15 | 8 |

### Stage 2 - extraction + classification

| term | kind | category | action | Zipf | AoA | syll |
|---|---|---|---|---:|---:|---:|
| `abdominal cavity` | phrase | medical_essential | elaborate | 3.29 | 10.24 | 7 |
| `uterus` | word | medical_essential | elaborate | 3.4 | 12.84 | 3 |

### Stage 3 - retrieval

coverage **1.0** (2/2), glossary budget 6/16

| term | Zipf stratum | defs | sources | matched via | origin |
|---|---|---:|---|---|---|
| `abdominal cavity` | uncommon | 1 | readme_lay_vocab.jsonl | exact | extracted |
| `uterus` | rare | 5 | justplainclear.json, michigan_plmd.json, nih.json, thesarus.json, wiktionary.json | exact | extracted |

Glossary shown to the model:

1. `[readme]` abdominal cavity: The belly area where your stomach and other organs are located.
2. `[nih]` uterus: The hollow, pear-shaped organ in a woman's pelvis. The uterus is where a fetus (unborn baby) develops and grows. Also called womb.
3. `[michigan]` uterus: Womb, or where a baby grows when a woman is pregnant.
4. `[justplainclear]` uterus: Also known as: womb An organ in a woman's body where babies may grow during pregnancy Uterus
5. `[wiktionary]` uterus: The uterus is the internal organ inside of a female mammal where an embryo grows into an infant ready to be born.
6. `[thesaurus]` uterus: womb

### Stage 4 - arm `naive`

**output:** The doctor put the uterus back inside the belly.

| metric | value |
|---|---:|
| bertscore_f1 | 0.613 |
| coleman_liau | 6.04 |
| coleman_liau_drop | 3.22 |
| copy_jargon_rate | 0.500 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 6.28 |
| fkgl_drop | 3.93 |
| fre | 66.1 |
| fre_gain | 28.2 |
| human_edit_recall | 0.500 |
| length_ratio | 1.12 |
| n_words | 9.0 |
| nli_completeness | 0.990 |
| nli_faithfulness | 0.616 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 22.22 |
| smog | 8.84 |
| smog_drop | 4.18 |

### Stage 4 - arm `termonly`

**output:** The womb was put back into the belly.

| metric | value |
|---|---:|
| bertscore_f1 | 0.850 |
| coleman_liau | 1.53 |
| coleman_liau_drop | 7.74 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 2.28 |
| fkgl_drop | 7.93 |
| fre | 93.0 |
| fre_gain | 55.1 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 8.0 |
| nli_completeness | 0.986 |
| nli_faithfulness | 0.984 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.250 |
| sari | 49.80 |
| smog | 3.13 |
| smog_drop | 9.89 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `uterus` -> `womb` | replace | - | - | - | - | - | - | - |
| `abdominal cavity` -> `belly` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** The womb was placed back into the belly area.

| metric | value |
|---|---:|
| bertscore_f1 | 0.837 |
| coleman_liau | 4.11 |
| coleman_liau_drop | 5.16 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 4.96 |
| fkgl_drop | 5.24 |
| fre | 75.5 |
| fre_gain | 37.6 |
| human_edit_recall | 1.000 |
| length_ratio | 1.12 |
| n_words | 9.0 |
| nli_completeness | 0.983 |
| nli_faithfulness | 0.981 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 84.29 |
| smog | 8.84 |
| smog_drop | 4.18 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `uterus` -> `womb` | replace | attributed | 0.695 | 1.723 | 0.726 | 0.743 | 0.500 | - |
| `abdominal cavity` -> `belly area` | replace | attributed | 1.015 | 1.592 | 0.811 | 0.867 | 1.830 | - |

**edit `uterus` -> `womb`**

- status: `attributed`
- log p full -0.2460, empty -0.9408
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.629` [thesaurus] uterus: womb
    - `+0.130` [michigan] uterus: Womb, or where a baby grows when a woman is pregnant.
    - `+0.041` [nih] uterus: The hollow, pear-shaped organ in a woman's pelvis. The uterus is where a fetus (unborn baby) develops 
    - `-0.113` [justplainclear] uterus: Also known as: womb An organ in a woman's body where babies may grow during pregnancy Uterus
    - `-0.119` [readme] abdominal cavity: The belly area where your stomach and other organs are located.

- rationale: The source defines "uterus" as the organ where a baby grows, so "womb" keeps that central meaning in plain language. Phrase frequency increases from 3.40 to 3.63, while age of acquisition falls from 12.84 to 9.48. Patients can now understand the location of pregnancy without needing to know the medical name.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `abdominal cavity` -> `belly area`**

- status: `attributed`
- log p full -0.5979, empty -1.6132
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+1.830` [readme] abdominal cavity: The belly area where your stomach and other organs are located.

- rationale: The glossary defines the belly area as the space containing your stomach and other organs, so "belly area" keeps that anatomical location in plain language. Phrase frequency increases from Zipf 3.29 to 4.08, while age of acquisition falls from 10.24 to 6.58. Patients can now visualize the internal organs' location without needing to know the formal medical term.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

==============================================================================

## Note 51 - `682`

**ORIGINAL**  This was viewed on the AP and lateral projections.

**REFERENCE** This was viewed from the front and sides.

| | FKGL | FRE | SMOG | Coleman-Liau | words |
|---|---:|---:|---:|---:|---:|
| ORIGINAL | 4.96 | 75.50 | 11.21 | 7.33 | 9 |
| REFERENCE | -0.67 | 114.12 | 3.13 | 4.43 | 8 |

### Stage 2 - extraction + classification

| term | kind | category | action | Zipf | AoA | syll |
|---|---|---|---|---:|---:|---:|
| `lateral projections` | phrase | medical_descriptor | replace | 3.43 | 12.41 | 6 |
| `lateral` | word | medical_descriptor | replace | - | - | - |
| `projections` | word | medical_descriptor | replace | - | - | - |
| `AP` | abbreviation | abbreviation_essential | abbr_expand_elaborate | None | None | 1 |

### Stage 3 - retrieval

coverage **0.5** (1/2), glossary budget 9/16

| term | Zipf stratum | defs | sources | matched via | origin |
|---|---|---:|---|---|---|
| `lateral projections` | uncommon | 0 | - | - | extracted |
| `lateral` | uncommon | 4 | michigan_plmd.json, readme_lay_vocab.jsonl, wiktionary.json | exact | split_from_uncovered |
| `projections` | uncommon | 1 | wiktionary.json | exact | split_from_uncovered |
| `AP` | uncommon | 4 | dorland_medical_abbreviations.csv, justplainclear.json, readme_lay_vocab.jsonl | exact | extracted |

Glossary shown to the model:

1. `[wiktionary]` projections: A projection is when something juts out.
2. `[dorland]` AP: alkaline phosphatase
3. `[readme]` lateral: Lateral means on or related to the side of the body or a body part.
4. `[dorland]` AP: anteroposterior
5. `[readme]` Lateral: To the side or relating to the side of the body or a body part.
6. `[justplainclear]` alkaline phosphatase test: Also known as: ALP test A test to determine how well your liver or gallbladder are working It measures the amount of the enzyme alkaline phosphatase (ALP) in your blood.
7. `[michigan]` lateral: The side or on the side.
8. `[readme]` anteroposterior: Front to back.
9. `[wiktionary]` lateral: An object's lateral refers to the side of it.

### Stage 4 - arm `naive`

**output:** The X-rays were taken from the front and side views.

| metric | value |
|---|---:|
| bertscore_f1 | 0.591 |
| coleman_liau | 5.02 |
| coleman_liau_drop | 2.31 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 1.29 |
| fkgl_drop | 3.67 |
| fre | 103.6 |
| fre_gain | 28.1 |
| human_edit_recall | 1.000 |
| laterality_preservation | 0.000 |
| length_ratio | 1.38 |
| n_words | 11.0 |
| nli_completeness | 0.479 |
| nli_faithfulness | 0.339 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 41.28 |
| smog | 3.13 |
| smog_drop | 8.08 |

### Stage 4 - arm `termonly`

**output:** This was viewed on the front and side views.

| metric | value |
|---|---:|
| bertscore_f1 | 0.841 |
| coleman_liau | 3.47 |
| coleman_liau_drop | 3.87 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.500 |
| fkgl | -0.28 |
| fkgl_drop | 5.24 |
| fre | 113.1 |
| fre_gain | 37.6 |
| human_edit_recall | 1.000 |
| laterality_preservation | 0.000 |
| length_ratio | 1.12 |
| n_words | 9.0 |
| nli_completeness | 0.879 |
| nli_faithfulness | 0.968 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 58.96 |
| smog | 3.13 |
| smog_drop | 8.08 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `AP` -> `front` | replace | - | - | - | - | - | - | - |
| `lateral projections` -> `side views` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** This was viewed on the front-to-back and side views.

| metric | value |
|---|---:|
| bertscore_f1 | 0.668 |
| coleman_liau | 7.33 |
| coleman_liau_drop | 0.00 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.250 |
| fkgl | 2.34 |
| fkgl_drop | 2.62 |
| fre | 94.3 |
| fre_gain | 18.8 |
| human_edit_recall | 1.000 |
| laterality_preservation | 0.000 |
| length_ratio | 1.38 |
| n_words | 11.0 |
| nli_completeness | 0.807 |
| nli_faithfulness | 0.908 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 54.23 |
| smog | 8.84 |
| smog_drop | 2.37 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `AP` -> `front-to-back` | replace | attributed | 3.955 | 5.567 | 0.860 | 0.906 | 2.664 | - |
| `lateral projections` -> `side views` | replace | attributed | 0.441 | 1.213 | 0.701 | 0.873 | 0.126 | - |

**edit `AP` -> `front-to-back`**

- status: `attributed`
- log p full -0.2187, empty -4.1740
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+4.707` [readme] anteroposterior: Front to back.
    - `+2.042` [dorland] AP: anteroposterior
    - `+0.416` [dorland] AP: alkaline phosphatase
    - `+0.355` [justplainclear] alkaline phosphatase test: Also known as: ALP test A test to determine how well your liver or gallbladder are 
    - `+0.307` [wiktionary] lateral: An object's lateral refers to the side of it.

- rationale: The glossary defines "AP" as "front to back," so the replacement keeps this directional meaning in plain words. Syllables increase from 1 to 3, while the phrase frequency rises from 2.6 to 3.4 and the age of acquisition drops from 14.6 to 9.2. Patients can now visualize the spatial orientation without needing to know the medical abbreviation.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `lateral projections` -> `side views`**

- status: `attributed`
- log p full -0.2672, empty -0.7084
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.190` [readme] lateral: Lateral means on or related to the side of the body or a body part.
    - `+0.064` [readme] anteroposterior: Front to back.
    - `+0.007` [dorland] AP: alkaline phosphatase

- rationale: The original term refers to structures extending outward from the side of an object, so "side views" captures this directional position in plain language. Phrase frequency increases from 3.43 to 4.75, while age of acquisition drops from 12.41 to 4.72. Patients can now visualize the anatomy from the correct angle without needing specialized vocabulary.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

==============================================================================

## Note 52 - `686`

**ORIGINAL**  The cords move normally with phonation and ventilation.

**REFERENCE** The cords move normally when speaking and breathing

| | FKGL | FRE | SMOG | Coleman-Liau | words |
|---|---:|---:|---:|---:|---:|
| ORIGINAL | 8.18 | 50.67 | 11.21 | 14.58 | 8 |
| REFERENCE | 5.23 | 71.82 | 8.84 | 12.40 | 8 |

### Stage 2 - extraction + classification

| term | kind | category | action | Zipf | AoA | syll |
|---|---|---|---|---:|---:|---:|
| `ventilation` | word | medical_descriptor | replace | 3.6 | 10.39 | 4 |
| `phonation` | word | medical_descriptor | replace | 1.8 | None | 2 |
| `cords` | word | medical_essential | elaborate | 3.35 | None | 1 |

### Stage 3 - retrieval

coverage **1.0** (3/3), glossary budget 5/16

| term | Zipf stratum | defs | sources | matched via | origin |
|---|---|---:|---|---|---|
| `ventilation` | uncommon | 3 | readme_lay_vocab.jsonl, wiktionary.json | exact | extracted |
| `phonation` | very_rare | 1 | dictonary.csv | exact | extracted |
| `cords` | rare | 1 | wiktionary.json | exact | extracted |

Glossary shown to the model:

1. `[wiktionary]` cords: A long, thin rope or wire.
2. `[dictionary]` Phonation (n.): The act or process by which articulate sounds are uttered; the utterance of articulate sounds; articulate speech.
3. `[readme]` ventilation: Ventilation is about bringing in fresh air.
4. `[wiktionary]` ventilation: Ventilation is the replacement of stale air with fresh air.
5. `[wiktionary]` ventilation: Ventilation is the bodily process of breathing; the inhalation of air to provide oxygen, and the exhalation of spent air to remove carbon dioxide.

### Stage 4 - arm `naive`

**output:** The vocal cords move normally when the patient speaks or breathes.

| metric | value |
|---|---:|
| bertscore_f1 | 0.636 |
| coleman_liau | 10.51 |
| coleman_liau_drop | 4.07 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 4.79 |
| fkgl_drop | 3.39 |
| fre | 80.3 |
| fre_gain | 29.6 |
| human_edit_recall | 1.000 |
| length_ratio | 1.38 |
| n_words | 11.0 |
| nli_completeness | 0.982 |
| nli_faithfulness | 0.922 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 51.90 |
| smog | 8.84 |
| smog_drop | 2.37 |

### Stage 4 - arm `termonly`

**output:** The vocal cords move normally when breathing and making sound.

| metric | value |
|---|---:|
| bertscore_f1 | 0.708 |
| coleman_liau | 11.40 |
| coleman_liau_drop | 3.18 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 6.01 |
| fkgl_drop | 2.17 |
| fre | 69.8 |
| fre_gain | 19.1 |
| human_edit_recall | 1.000 |
| length_ratio | 1.25 |
| n_words | 10.0 |
| nli_completeness | 0.979 |
| nli_faithfulness | 0.977 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 57.60 |
| smog | 8.84 |
| smog_drop | 2.37 |

annotation backend `novita`, 2 edits kept

- rejected: DROP noop      'cords' -> 'cords'  (nothing changed)

| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `ventilation` -> `breathing` | replace | - | - | - | - | - | - | - |
| `phonation` -> `making sound` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** The vocal cords move normally when speaking and breathing.

| metric | value |
|---|---:|
| bertscore_f1 | 0.829 |
| coleman_liau | 12.49 |
| coleman_liau_drop | 2.09 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 6.28 |
| fkgl_drop | 1.90 |
| fre | 66.1 |
| fre_gain | 15.4 |
| human_edit_recall | 1.000 |
| length_ratio | 1.12 |
| n_words | 9.0 |
| nli_completeness | 0.989 |
| nli_faithfulness | 0.987 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 76.03 |
| smog | 8.84 |
| smog_drop | 2.37 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `phonation` -> `speaking` | replace | attributed | 0.123 | 0.157 | - | 0.918 | 0.614 | - |
| `ventilation` -> `breathing` | replace | attributed | 0.060 | 0.689 | - | 0.938 | 0.236 | - |

**edit `phonation` -> `speaking`**

- status: `attributed`
- log p full -1.4500, empty -1.5725
- masks scored: 34/34 (+4 top-k)
- ranked sources:
    - `+0.815` [dictionary] Phonation (n.): The act or process by which articulate sounds are uttered; the utterance of articulate sounds;
    - `+0.202` [wiktionary] cords: A long, thin rope or wire.
    - `+0.134` [readme] ventilation: Ventilation is about bringing in fresh air.
    - `-0.470` [wiktionary] ventilation: Ventilation is the bodily process of breathing; the inhalation of air to provide oxygen, and the 

- rationale: The original term refers to the act of producing sound through the vocal cords, so "speaking" captures this vocal action in everyday language. Phrase frequency rises from Zipf 1.80 to 4.91, while syllable count remains steady at two. Patients can now recognize the basic act of vocalizing without needing specialized medical knowledge.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `ventilation` -> `breathing`**

- status: `attributed`
- log p full -0.0645, empty -0.1246
- masks scored: 34/34 (+4 top-k)
- ranked sources:
    - `+0.533` [wiktionary] ventilation: Ventilation is the bodily process of breathing; the inhalation of air to provide oxygen, and the 
    - `+0.297` [readme] ventilation: Ventilation is about bringing in fresh air.
    - `+0.088` [wiktionary] cords: A long, thin rope or wire.
    - `+0.082` [wiktionary] ventilation: Ventilation is the replacement of stale air with fresh air.
    - `-0.238` [dictionary] Phonation (n.): The act or process by which articulate sounds are uttered; the utterance of articulate sounds;

- rationale: The original term refers to the mechanical process of moving air in and out of the lungs, so "breathing" captures this essential action in everyday language. Phrase frequency rises from 3.60 to 4.28, while syllable count drops from 4 to 2. Patients can now grasp the concept of air movement without needing to recall a technical medical procedure.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

==============================================================================

## Note 53 - `688`

**ORIGINAL**  Once the abdomen was opened, there was noted to be gross purulent drainage.

**REFERENCE** Once the abdomen was opened, there was noted to be a lot of pus draining.

| | FKGL | FRE | SMOG | Coleman-Liau | words |
|---|---:|---:|---:|---:|---:|
| ORIGINAL | 7.63 | 63.49 | 11.21 | 9.14 | 13 |
| REFERENCE | 5.99 | 78.81 | 8.84 | 4.27 | 15 |

### Stage 2 - extraction + classification

| term | kind | category | action | Zipf | AoA | syll |
|---|---|---|---|---:|---:|---:|
| `gross purulent drainage` | phrase | medical_descriptor | replace | 1.92 | 15.5 | 6 |
| `gross` | word | medical_descriptor | replace | - | - | - |
| `purulent` | word | medical_descriptor | replace | - | - | - |
| `drainage` | word | medical_descriptor | replace | - | - | - |
| `abdomen` | word | medical_essential | elaborate | 3.56 | 8.61 | 3 |

### Stage 3 - retrieval

coverage **0.5** (1/2), glossary budget 10/16

| term | Zipf stratum | defs | sources | matched via | origin |
|---|---|---:|---|---|---|
| `gross purulent drainage` | very_rare | 0 | - | - | extracted |
| `gross` | uncommon | 2 | wiktionary.json | exact | split_from_uncovered |
| `purulent` | very_rare | 1 | michigan_plmd.json | exact | split_from_uncovered |
| `drainage` | uncommon | 3 | readme_lay_vocab.jsonl, wiktionary.json | exact | split_from_uncovered |
| `abdomen` | uncommon | 4 | nih.json, thesarus.json, wiktionary.json | exact | extracted |

Glossary shown to the model:

1. `[michigan]` purulent: Pus.
2. `[wiktionary]` gross: The gross amount is the total before you take away losses or expenses.
3. `[readme]` drainage: When any fluid is leaking out of a body part.
4. `[nih]` abdomen: The area of the body that contains the pancreas, stomach, intestines, liver, gallbladder, and other organs.
5. `[wiktionary]` gross: A gross violation or abuse is very bad and clearly wrong.
6. `[readme]` DRAINAGE: Fluid leaving an organ or body area.
7. `[wiktionary]` abdomen: The abdomen is the front part of the lower torso containing many internal organs.
8. `[wiktionary]` drainage: To use a drainage is engage in the action or process of draining something.
9. `[wiktionary]` abdomen: The abdomen is the last of the three parts of an insect's body.
10. `[thesaurus]` abdomen: stomach, stomach area, belly, tummy

### Stage 4 - arm `naive`

**output:** Once the abdomen was opened, there was a lot of thick, pus-like fluid coming out.

| metric | value |
|---|---:|
| bertscore_f1 | 0.742 |
| coleman_liau | 6.59 |
| coleman_liau_drop | 2.55 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.250 |
| fkgl | 6.78 |
| fkgl_drop | 0.85 |
| fre | 73.2 |
| fre_gain | 9.7 |
| human_edit_recall | 1.000 |
| length_ratio | 1.07 |
| n_words | 16.0 |
| nli_completeness | 0.972 |
| nli_faithfulness | 0.866 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.250 |
| sari | 51.00 |
| smog | 8.84 |
| smog_drop | 2.37 |

### Stage 4 - arm `termonly`

**output:** Once the belly was opened, there was a lot of thick, pus-like fluid.

| metric | value |
|---|---:|
| bertscore_f1 | 0.722 |
| coleman_liau | 5.12 |
| coleman_liau_drop | 4.02 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.400 |
| fkgl | 4.91 |
| fkgl_drop | 2.72 |
| fre | 83.0 |
| fre_gain | 19.5 |
| human_edit_recall | 1.000 |
| length_ratio | 0.93 |
| n_words | 14.0 |
| nli_completeness | 0.960 |
| nli_faithfulness | 0.879 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.200 |
| sari | 37.67 |
| smog | 3.13 |
| smog_drop | 8.08 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `abdomen` -> `belly` | replace | - | - | - | - | - | - | - |
| `gross purulent drainage` -> `a lot of thick, pus-like fluid` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Once the belly was opened, pus was leaking out.

| metric | value |
|---|---:|
| bertscore_f1 | 0.673 |
| coleman_liau | 4.76 |
| coleman_liau_drop | 4.38 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.600 |
| fkgl | 3.65 |
| fkgl_drop | 3.98 |
| fre | 84.9 |
| fre_gain | 21.4 |
| human_edit_recall | 1.000 |
| length_ratio | 0.60 |
| n_words | 9.0 |
| nli_completeness | 0.926 |
| nli_faithfulness | 0.835 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 20.84 |
| smog | 3.13 |
| smog_drop | 8.08 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `abdomen` -> `belly` | replace | attributed | 0.334 | 1.127 | 0.915 | 0.883 | 1.795 | - |
| `gross purulent drainage` -> `pus was leaking out` | replace | attributed | 4.272 | 4.347 | 0.901 | 0.918 | 1.089 | - |

**edit `abdomen` -> `belly`**

- status: `attributed`
- log p full -0.2109, empty -0.5451
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+2.251` [thesaurus] abdomen: stomach, stomach area, belly, tummy
    - `+0.456` [wiktionary] gross: A gross violation or abuse is very bad and clearly wrong.
    - `+0.205` [readme] DRAINAGE: Fluid leaving an organ or body area.
    - `+0.127` [wiktionary] gross: The gross amount is the total before you take away losses or expenses.
    - `-0.034` [nih] abdomen: The area of the body that contains the pancreas, stomach, intestines, liver, gallbladder, and other o

- rationale: The original term refers to the front part of the body between the chest and hips, so "belly" conveys that same central location in everyday language. Phrase frequency rises from 3.56 to 4.10, while age of acquisition drops from 8.61 to 4.05. Patients can now identify the body region without needing to recall a more formal anatomical label.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `gross purulent drainage` -> `pus was leaking out`**

- status: `attributed`
- log p full -2.6148, empty -6.8867
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+2.660` [readme] drainage: When any fluid is leaking out of a body part.
    - `+1.571` [michigan] purulent: Pus.
    - `+0.221` [readme] DRAINAGE: Fluid leaving an organ or body area.
    - `+0.125` [wiktionary] drainage: To use a drainage is engage in the action or process of draining something.

- rationale: The glossary defines the original phrase as fluid leaking from a body part, so "pus was leaking out" keeps that core image in plain language. Phrase frequency increases from 1.92 to 2.94, while age of acquisition drops from 15.50 to 7.78. Patients can now clearly visualize the infection without needing to know the clinical term for the discharge.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

==============================================================================

## Note 54 - `692`

**ORIGINAL**  Once all four ports were placed, the right upper quadrant was then explored.

**REFERENCE** Once all four tubes were placed, the top right corner of her abdomen was then explored.

| | FKGL | FRE | SMOG | Coleman-Liau | words |
|---|---:|---:|---:|---:|---:|
| ORIGINAL | 4.00 | 89.52 | 3.13 | 9.58 | 13 |
| REFERENCE | 5.40 | 84.84 | 8.84 | 7.72 | 16 |

### Stage 2 - extraction + classification

| term | kind | category | action | Zipf | AoA | syll |
|---|---|---|---|---:|---:|---:|
| `right upper quadrant` | phrase | medical_essential | elaborate | 3.26 | 12.76 | 5 |
| `right upper` | phrase | medical_essential | elaborate | - | - | - |
| `quadrant` | word | medical_descriptor | replace | - | - | - |
| `explored` | word | general_hard_word | replace | 3.9 | None | 2 |
| `ports` | word | medical_essential | elaborate | 4.07 | None | 1 |

### Stage 3 - retrieval

coverage **0.6667** (2/3), glossary budget 6/16

| term | Zipf stratum | defs | sources | matched via | origin |
|---|---|---:|---|---|---|
| `right upper quadrant` | rare | 0 | - | - | extracted |
| `right upper` | common | 2 | readme_lay_vocab.jsonl | exact | split_from_uncovered |
| `quadrant` | rare | 2 | dictonary.csv | exact | split_from_uncovered |
| `explored` | uncommon | 1 | wiktionary.json | exact | extracted |
| `ports` | uncommon | 1 | wiktionary.json | exact | extracted |

Glossary shown to the model:

1. `[wiktionary]` ports: A port is a place for ships to stop to trade or refuel.
2. `[wiktionary]` explored: If you explore a possibility, plan, idea, etc. you think about it carefully.
3. `[readme]` right upper lobe: A section of the right lung.
4. `[dictionary]` Quadrant (n.): The fourth part; the quarter.
5. `[readme]` Right Upper Lobe: The upper right part of the right lung.
6. `[dictionary]` Quadrant (n.): The quarter of a circle, or of the circumference of a circle, an arc of 90, or one subtending a right angle at the center.

### Stage 4 - arm `naive`

**output:** Once all four ports were placed, the doctor looked inside the right upper part of the belly.

| metric | value |
|---|---:|
| bertscore_f1 | 0.701 |
| coleman_liau | 7.71 |
| coleman_liau_drop | 1.88 |
| copy_jargon_rate | 0.500 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.333 |
| fkgl | 5.62 |
| fkgl_drop | -1.61 |
| fre | 85.1 |
| fre_gain | -4.4 |
| human_edit_recall | 0.500 |
| laterality_preservation | 1.000 |
| length_ratio | 1.06 |
| n_words | 17.0 |
| nli_completeness | 0.975 |
| nli_faithfulness | 0.245 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 37.24 |
| smog | 3.13 |
| smog_drop | 0.00 |

### Stage 4 - arm `termonly`

**output:** Once all four tubes were placed, the area on the right side of the belly was then checked.

| metric | value |
|---|---:|
| bertscore_f1 | 0.800 |
| coleman_liau | 5.43 |
| coleman_liau_drop | 4.15 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.200 |
| fkgl | 5.20 |
| fkgl_drop | -1.19 |
| fre | 89.9 |
| fre_gain | 0.3 |
| human_edit_recall | 1.000 |
| laterality_preservation | 0.500 |
| length_ratio | 1.12 |
| n_words | 18.0 |
| nli_completeness | 0.931 |
| nli_faithfulness | 0.883 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 59.05 |
| smog | 8.84 |
| smog_drop | -5.71 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `ports` -> `tubes` | replace | - | - | - | - | - | - | - |
| `right upper quadrant` -> `area on the right side of the belly` | replace | - | - | - | - | - | - | - |
| `explored` -> `checked` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Once all four ports were placed, the doctor then looked inside the upper right part of the belly.

| metric | value |
|---|---:|
| bertscore_f1 | 0.746 |
| coleman_liau | 7.69 |
| coleman_liau_drop | 1.90 |
| copy_jargon_rate | 0.250 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 5.85 |
| fkgl_drop | -1.85 |
| fre | 85.2 |
| fre_gain | -4.3 |
| human_edit_recall | 0.750 |
| laterality_preservation | 1.000 |
| length_ratio | 1.12 |
| n_words | 18.0 |
| nli_completeness | 0.982 |
| nli_faithfulness | 0.222 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 41.39 |
| smog | 3.13 |
| smog_drop | 0.00 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `right upper quadrant` -> `upper right part of the belly` | replace | attributed | -0.404 | -0.447 | 0.840 | 0.832 | 0.204 | - |

**edit `right upper quadrant` -> `upper right part of the belly`**

- status: `attributed`
- log p full -2.5553, empty -2.1509
- masks scored: 66/66 (+2 top-k)
- ranked sources:
    - `+0.204` [dictionary] Quadrant (n.): The fourth part; the quarter.
    - `-0.262` [wiktionary] explored: If you explore a possibility, plan, idea, etc. you think about it carefully.

- rationale: The original term refers to the specific area on the right side of the abdomen, so "upper right part of the belly" keeps that location clear in plain language. Phrase frequency increases from 3.26 to 3.99, while age of acquisition drops from 12.76 to 7.56. Patients can now easily identify the general area of pain without needing to know the precise anatomical name.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

==============================================================================

## Note 55 - `693`

**ORIGINAL**  Options such as watchful waiting, robotic prostatectomy, seed implantation with and without radiation were discussed.

**REFERENCE** Options such as watch and wait, removing the prostate with the help of a robot, seed implantation with and without radiation were discussed.

| | FKGL | FRE | SMOG | Coleman-Liau | words |
|---|---:|---:|---:|---:|---:|
| ORIGINAL | 15.43 | 11.13 | 14.55 | 20.89 | 15 |
| REFERENCE | 11.85 | 51.07 | 13.02 | 11.91 | 23 |

### Stage 2 - extraction + classification

| term | kind | category | action | Zipf | AoA | syll |
|---|---|---|---|---:|---:|---:|
| `robotic prostatectomy` | phrase | medical_essential | elaborate | 2.13 | 15.27 | 8 |
| `prostatectomy` | word | medical_essential | elaborate | - | - | - |
| `seed implantation` | phrase | medical_essential | elaborate | 2.99 | 11.95 | 5 |
| `seed` | word | medical_descriptor | replace | - | - | - |
| `implantation` | word | medical_descriptor | replace | - | - | - |
| `watchful waiting` | phrase | medical_essential | elaborate | 3.09 | 8.16 | 4 |
| `radiation` | word | medical_essential | elaborate | 4.27 | 11.44 | 4 |

### Stage 3 - retrieval

coverage **0.5** (2/4), glossary budget 12/16

| term | Zipf stratum | defs | sources | matched via | origin |
|---|---|---:|---|---|---|
| `robotic prostatectomy` | very_rare | 0 | - | - | extracted |
| `prostatectomy` | very_rare | 2 | nih.json, readme_lay_vocab.jsonl | exact | partial_split_from_uncovered |
| `seed implantation` | rare | 0 | - | - | extracted |
| `seed` | uncommon | 2 | wiktionary.json | exact | split_from_uncovered |
| `implantation` | rare | 2 | readme_lay_vocab.jsonl | exact | split_from_uncovered |
| `watchful waiting` | rare | 1 | nih.json | exact | extracted |
| `radiation` | uncommon | 5 | nih.json, readme_lay_vocab.jsonl, thesarus.json, wiktionary.json | exact | extracted |

Glossary shown to the model:

1. `[nih]` watchful waiting: Closely watching a patient’s condition but not giving treatment unless symptoms appear or change. Watchful waiting is sometimes used in conditions that progress slowly. It is also used when the risks of treatment are greater than the possible benefits. During watchful waiting, patients may be given certain tests and exams. Watchful waiting is sometimes used in prostate cancer. It is a type of expectant management.
2. `[wiktionary]` seed: A seed is a small round thing that can grow to be a plant, a flower or a tree.
3. `[readme]` implantation: Surgery where a device is placed inside your body.
4. `[readme]` prostatectomy: A prostatectomy is a surgery to remove part or all of the prostate and some surrounding tissue.
5. `[readme]` radiation: High energy rays used to kill cancer cells.
6. `[wiktionary]` seed: The seed of a man is his semen.
7. `[readme]` IMPLANTATION: A surgery where a device is placed inside the body.
8. `[nih]` prostatectomy: Surgery to remove part or all of the prostate and some of the tissue around it, including the seminal vesicles (a gland that helps make semen). Nearby lymph nodes may also be removed. A prostatectomy may be done through an incision (cut) made in the wall of the lower abdomen or in the perineum (the area between the scrotum and anus). It may also be done using a laparoscope (a thin, tube-like instrument with a light and lens for viewing) or a special robotic system. An attempt is made to protect the nerves that control penile erection and the bladder from damage.
9. `[readme]` Radiation: Radiation is powerful energy waves that are sometimes utilized to destroy cancer cells.
10. `[nih]` radiation: Energy released in the form of particle or electromagnetic waves. Common sources of radiation include radon gas, cosmic rays from outer space, medical x-rays, and energy given off by a radioisotope (unstable form of a chemical element that releases radiation as it breaks down and becomes more stable). Radiation can damage cells. It is used to diagnose and treat some types of cancer.
11. `[wiktionary]` radiation: Radiation is the emission or transmission of energy in the form of waves or particles through space or through a material medium.
12. `[thesaurus]` radiation: see ionizing radiation and non-ionizing radiation

### Stage 4 - arm `naive`

**output:** The doctor talked about different choices, like watching and waiting, having a robotic surgery to remove the prostate, or putting seeds in the prostate with or without radiation.

| metric | value |
|---|---:|
| bertscore_f1 | 0.492 |
| coleman_liau | 13.59 |
| coleman_liau_drop | 7.30 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 15.56 |
| fkgl_drop | -0.13 |
| fre | 33.4 |
| fre_gain | 22.3 |
| human_edit_recall | 1.000 |
| length_ratio | 1.22 |
| n_words | 28.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.995 |
| nli_faithfulness | 0.437 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.429 |
| sari | 22.50 |
| smog | 14.55 |
| smog_drop | 0.00 |

### Stage 4 - arm `termonly`

**output:** The doctor talked about waiting, surgery, and putting seeds in, with or without radiation.

| metric | value |
|---|---:|
| bertscore_f1 | 0.369 |
| coleman_liau | 12.33 |
| coleman_liau_drop | 8.56 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.333 |
| fkgl | 10.10 |
| fkgl_drop | 5.33 |
| fre | 47.6 |
| fre_gain | 36.5 |
| human_edit_recall | 1.000 |
| length_ratio | 0.61 |
| n_words | 14.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.917 |
| nli_faithfulness | 0.269 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.375 |
| sari | 21.17 |
| smog | 11.21 |
| smog_drop | 3.35 |

annotation backend `novita`, 3 edits kept

- rejected: DROP noop      'radiation' -> 'radiation'  (nothing changed)

| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `watchful waiting` -> `waiting` | replace | - | - | - | - | - | - | - |
| `robotic prostatectomy` -> `surgery` | replace | - | - | - | - | - | - | - |
| `seed implantation` -> `putting seeds in` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Options like waiting to see if symptoms change, a surgery to remove the prostate, and placing small devices inside the body with or without high-energy rays were discussed.

| metric | value |
|---|---:|
| bertscore_f1 | 0.506 |
| coleman_liau | 12.35 |
| coleman_liau_drop | 8.54 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.714 |
| fkgl | 14.29 |
| fkgl_drop | 1.14 |
| fre | 42.5 |
| fre_gain | 31.3 |
| human_edit_recall | 1.000 |
| length_ratio | 1.26 |
| n_words | 29.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.551 |
| nli_faithfulness | 0.907 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.143 |
| sari | 24.40 |
| smog | 13.02 |
| smog_drop | 1.53 |

annotation backend `novita`, 4 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `watchful waiting` -> `waiting to see if symptoms change` | replace | attributed | 1.433 | 1.446 | 0.880 | 0.933 | 2.082 | - |
| `robotic prostatectomy` -> `a surgery to remove the prostate` | replace | attributed | -0.556 | -0.608 | 0.904 | 0.923 | 0.149 | - |
| `seed implantation` -> `placing small devices inside the body` | replace | attributed | 10.420 | 10.449 | 0.772 | 0.820 | 2.180 | - |
| `radiation` -> `high-energy rays` | replace | attributed | 3.357 | 3.549 | 0.940 | 0.977 | 5.384 | - |

**edit `watchful waiting` -> `waiting to see if symptoms change`**

- status: `attributed`
- log p full -4.1178, empty -5.5511
- masks scored: 66/66 (+8 top-k)
- ranked sources:
    - `+2.255` [nih] watchful waiting: Closely watching a patient’s condition but not giving treatment unless symptoms appear or ch
    - `+0.173` [thesaurus] radiation: see ionizing radiation and non-ionizing radiation

- rationale: The source defines watchful waiting as closely monitoring a patient's condition without immediate treatment unless symptoms appear or worsen, so "waiting to see if symptoms change" captures that core idea in plain language. Phrase frequency increases from Zipf 3.09 to 4.34, while age of acquisition drops from 8.16 to 5.36. Patients can now understand the strategy of monitoring without needing to know the specific medical term.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `robotic prostatectomy` -> `a surgery to remove the prostate`**

- status: `attributed`
- log p full -2.7557, empty -2.1998
- masks scored: 66/66 (+8 top-k)
- ranked sources:
    - `+0.227` [readme] prostatectomy: A prostatectomy is a surgery to remove part or all of the prostate and some surrounding tissue.
    - `+0.078` [readme] IMPLANTATION: A surgery where a device is placed inside the body.
    - `+0.042` [nih] watchful waiting: Closely watching a patient’s condition but not giving treatment unless symptoms appear or ch

- rationale: The original term refers to a surgical procedure that uses robotic assistance to remove the prostate, while the replacement describes the same operation in plain language as a surgery to remove the prostate. Phrase frequency increases from Zipf 2.13 to 3.59, and age of acquisition decreases from 15.27 to 15.00. Patients can now grasp the core action of the procedure without needing specialized medical knowledge.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `seed implantation` -> `placing small devices inside the body`**

- status: `attributed`
- log p full -3.5462, empty -13.9658
- masks scored: 66/66 (+8 top-k)
- ranked sources:
    - `+6.318` [readme] implantation: Surgery where a device is placed inside your body.
    - `+4.138` [readme] IMPLANTATION: A surgery where a device is placed inside the body.
    - `+1.233` [wiktionary] seed: A seed is a small round thing that can grow to be a plant, a flower or a tree.
    - `+0.763` [thesaurus] radiation: see ionizing radiation and non-ionizing radiation
    - `+0.457` [wiktionary] seed: The seed of a man is his semen.

- rationale: The glossary defines the procedure as surgery where a device is placed inside your body, so "placing small devices inside the body" keeps that core action in plain language. Phrase frequency increases from 2.99 to 3.97, while age of acquisition drops from 11.95 to 4.77. You can now understand the basic surgical step without needing to know the technical term for the procedure.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `radiation` -> `high-energy rays`**

- status: `attributed`
- log p full -1.7173, empty -5.0747
- masks scored: 66/66 (+8 top-k)
- ranked sources:
    - `+6.222` [readme] radiation: High energy rays used to kill cancer cells.
    - `+0.838` [nih] radiation: Energy released in the form of particle or electromagnetic waves. Common sources of radiation inclu
    - `+0.452` [nih] prostatectomy: Surgery to remove part or all of the prostate and some of the tissue around it, including the s
    - `+0.276` [nih] watchful waiting: Closely watching a patient’s condition but not giving treatment unless symptoms appear or ch
    - `+0.252` [thesaurus] radiation: see ionizing radiation and non-ionizing radiation

- rationale: The glossary defines radiation as high-energy rays used to kill cancer cells, so "high-energy rays" keeps that specific medical function in plain language. Phrase frequency increases from 4.27 to 4.00, while syllable count rises from 4 to 5. Patients can now understand the treatment method without needing to know the technical term.
- audit: coverage 1.0, grounding_error=True, omission=False, source_ok=True, passage_ok=True

==============================================================================

## Note 56 - `695`

**ORIGINAL**  He also reportedly was on Lasix prior to hospitalization, possible

**REFERENCE** He also was reportedly on water pills (lasix) before his admission to the hospital, possible

| | FKGL | FRE | SMOG | Coleman-Liau | words |
|---|---:|---:|---:|---:|---:|
| ORIGINAL | 14.27 | 10.56 | 13.02 | 13.72 | 10 |
| REFERENCE | 11.50 | 39.33 | 14.55 | 11.23 | 15 |

### Stage 2 - extraction + classification

| term | kind | category | action | Zipf | AoA | syll |
|---|---|---|---|---:|---:|---:|
| `hospitalization` | word | general_hard_word | replace | 3.09 | 9.53 | 6 |
| `reportedly` | word | general_hard_word | replace | 4.13 | None | 4 |
| `prior to` | phrase | general_hard_word | replace | 4.85 | 10.63 | 3 |
| `Lasix` | word | medical_essential | elaborate | 1.98 | None | 1 |

### Stage 3 - retrieval

coverage **0.75** (3/4), glossary budget 6/16

| term | Zipf stratum | defs | sources | matched via | origin |
|---|---|---:|---|---|---|
| `hospitalization` | rare | 4 | readme_lay_vocab.jsonl, wiktionary.json | exact | extracted |
| `reportedly` | uncommon | 1 | wiktionary.json | exact | extracted |
| `prior to` | common | 1 | michigan_plmd.json | exact | extracted |
| `Lasix` | very_rare | 0 | - | - | extracted |

Glossary shown to the model:

1. `[michigan]` prior to: Earlier or before.
2. `[wiktionary]` reportedly: If something is reportedly true, people say it happened, but we don't have other reasons to believe it.
3. `[readme]` hospitalization: Being admitted to and staying in a hospital.
4. `[readme]` Hospitalization: Being admitted to a hospital for an extended period of time.
5. `[wiktionary]` hospitalization: Hospitalization is the period of time when a person is in hospital for medical care.
6. `[wiktionary]` hospitalization: Hospitalization is the process of putting a person in hospital for medical care.

### Stage 4 - arm `naive`

**output:** He also reportedly took Lasix before he was admitted to the hospital, possibly.

| metric | value |
|---|---:|
| bertscore_f1 | 0.584 |
| coleman_liau | 10.92 |
| coleman_liau_drop | 2.80 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 11.26 |
| fkgl_drop | 3.01 |
| fre | 37.5 |
| fre_gain | 26.9 |
| human_edit_recall | 1.000 |
| length_ratio | 0.87 |
| n_words | 13.0 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.991 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 48.61 |
| smog | 14.55 |
| smog_drop | -1.53 |
| temporality_preservation | 1.000 |
| uncertainty_preservation | 1.000 |

### Stage 4 - arm `termonly`

**output:** He also reportedly took a diuretic before being admitted to the hospital.

| metric | value |
|---|---:|
| bertscore_f1 | 0.443 |
| coleman_liau | 11.22 |
| coleman_liau_drop | 2.50 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.667 |
| fkgl | 13.67 |
| fkgl_drop | 0.60 |
| fre | 18.4 |
| fre_gain | 7.8 |
| human_edit_recall | 1.000 |
| length_ratio | 0.80 |
| n_words | 12.0 |
| nli_completeness | 0.065 |
| nli_faithfulness | 0.424 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.250 |
| sari | 44.49 |
| smog | 14.55 |
| smog_drop | -1.53 |
| temporality_preservation | 1.000 |
| uncertainty_preservation | 0.000 |

annotation backend `novita`, 2 edits kept

- rejected: DROP noop      'reportedly' -> 'reportedly'  (nothing changed)

| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `Lasix` -> `diuretic` | replace | - | - | - | - | - | - | - |
| `hospitalization` -> `admitted to the hospital` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** He also reportedly was on Lasix before being admitted to the hospital.

| metric | value |
|---|---:|
| bertscore_f1 | 0.610 |
| coleman_liau | 9.77 |
| coleman_liau_drop | 3.95 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 10.72 |
| fkgl_drop | 3.55 |
| fre | 39.6 |
| fre_gain | 29.0 |
| human_edit_recall | 1.000 |
| length_ratio | 0.80 |
| n_words | 12.0 |
| nli_completeness | 0.137 |
| nli_faithfulness | 0.986 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 48.79 |
| smog | 13.02 |
| smog_drop | 0.00 |
| temporality_preservation | 1.000 |
| uncertainty_preservation | 0.000 |

annotation backend `novita`, 2 edits kept

- rejected: DROP noop      'reportedly' -> 'reportedly'  (nothing changed)

| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `prior to` -> `before` | replace | attributed | 1.554 | 2.111 | 0.512 | 0.646 | 0.083 | - |
| `hospitalization` -> `being admitted to the hospital` | replace | attributed | 0.923 | 1.050 | 0.899 | 0.877 | 0.225 | - |

**edit `prior to` -> `before`**

- status: `attributed`
- log p full -0.7214, empty -2.2754
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.083` [wiktionary] hospitalization: Hospitalization is the process of putting a person in hospital for medical care.
    - `-0.026` [michigan] prior to: Earlier or before.
    - `-0.049` [readme] hospitalization: Being admitted to and staying in a hospital.
    - `-0.067` [wiktionary] hospitalization: Hospitalization is the period of time when a person is in hospital for medical care.

- rationale: The original term "prior to" indicates a time that comes before another event, and "before" conveys this same sequence in simpler language. Phrase frequency rises from 4.85 to 5.93, while age of acquisition drops from 10.63 to 5.45. Patients can now grasp the timing of an event without needing to process a more complex phrase.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `hospitalization` -> `being admitted to the hospital`**

- status: `attributed`
- log p full -1.6996, empty -2.6229
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+1.029` [readme] hospitalization: Being admitted to and staying in a hospital.
    - `+0.804` [readme] Hospitalization: Being admitted to a hospital for an extended period of time.
    - `+0.089` [michigan] prior to: Earlier or before.
    - `+0.061` [wiktionary] hospitalization: Hospitalization is the process of putting a person in hospital for medical care.
    - `+0.009` [wiktionary] hospitalization: Hospitalization is the period of time when a person is in hospital for medical care.

- rationale: The glossary defines hospitalization as being admitted to and staying in a hospital, so the replacement phrase keeps that core idea of entering and remaining in a medical facility. Phrase frequency increases from 3.09 to 4.38, while age of acquisition drops from 9.53 to 5.99. You can now grasp the concept of staying in a hospital without needing to know the formal medical term.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

==============================================================================

## Note 57 - `697`

**ORIGINAL**  The four cardiac chambers dimensions are within normal limits.

**REFERENCE** The sizes of the four parts of the heart are within normal limits.

| | FKGL | FRE | SMOG | Coleman-Liau | words |
|---|---:|---:|---:|---:|---:|
| ORIGINAL | 10.21 | 37.90 | 11.21 | 15.07 | 9 |
| REFERENCE | 4.91 | 83.01 | 3.13 | 5.57 | 13 |

### Stage 2 - extraction + classification

| term | kind | category | action | Zipf | AoA | syll |
|---|---|---|---|---:|---:|---:|
| `within normal limits` | phrase | medical_descriptor | replace | 4.32 | 7.65 | 6 |
| `within` | word | medical_descriptor | replace | - | - | - |
| `normal` | word | medical_descriptor | replace | - | - | - |
| `limits` | word | medical_descriptor | replace | - | - | - |
| `cardiac chambers` | phrase | medical_essential | elaborate | 3.64 | 11.74 | 5 |
| `cardiac` | word | medical_descriptor | replace | - | - | - |
| `chambers` | word | medical_descriptor | replace | - | - | - |
| `dimensions` | word | general_hard_word | replace | 4.05 | None | 3 |

### Stage 3 - retrieval

coverage **0.3333** (1/3), glossary budget 14/16

| term | Zipf stratum | defs | sources | matched via | origin |
|---|---|---:|---|---|---|
| `within normal limits` | uncommon | 0 | - | - | extracted |
| `within` | common | 2 | wiktionary.json | exact | split_from_uncovered |
| `normal` | common | 3 | justplainclear.json, wiktionary.json | exact | split_from_uncovered |
| `limits` | uncommon | 2 | justplainclear.json, wiktionary.json | exact | split_from_uncovered |
| `cardiac chambers` | uncommon | 0 | - | - | extracted |
| `cardiac` | uncommon | 5 | iowa.json, michigan_plmd.json, nih.json, readme_lay_vocab.jsonl, wiktionary.json | exact | split_from_uncovered |
| `chambers` | uncommon | 1 | wiktionary.json | exact | split_from_uncovered |
| `dimensions` | uncommon | 1 | wiktionary.json | exact | extracted |

Glossary shown to the model:

1. `[wiktionary]` chambers: A chamber is a room that is often used for sleeping.
2. `[wiktionary]` dimensions: A dimension is a part of a problem, issue, or situation.
3. `[wiktionary]` within: before the time ends
4. `[justplainclear]` limits: A certain point that you can't go past; a certain amount but no more
5. `[justplainclear]` normal: Whats expected for a person similar to you or to what's usual for you
6. `[readme]` cardiac: Related to the heart.
7. `[wiktionary]` within: not farther than
8. `[wiktionary]` limits: The limit is the edge of how far something can go. It can go up to the limit but no farther.
9. `[wiktionary]` normal: A normal thing, or situation, is one that is not special.
10. `[nih]` cardiac: Having to do with the heart.
11. `[wiktionary]` normal: When someone is back to normal, he is healthier and no longer sick.
12. `[iowa]` CARDIAC: related to the heart
13. `[michigan]` cardiac: Related to your heart.
14. `[wiktionary]` cardiac: Something that is cardiac is related to the heart.

### Stage 4 - arm `naive`

**output:** The sizes of the four heart chambers are normal.

| metric | value |
|---|---:|
| bertscore_f1 | 0.803 |
| coleman_liau | 6.04 |
| coleman_liau_drop | 9.02 |
| copy_jargon_rate | 0.250 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.167 |
| fkgl | 3.65 |
| fkgl_drop | 6.56 |
| fre | 84.9 |
| fre_gain | 47.0 |
| human_edit_recall | 0.750 |
| length_ratio | 0.69 |
| n_words | 9.0 |
| nli_completeness | 0.969 |
| nli_faithfulness | 0.972 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 0.857 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 47.28 |
| smog | 3.13 |
| smog_drop | 8.08 |

### Stage 4 - arm `termonly`

**output:** The four heart room sizes are normal.

| metric | value |
|---|---:|
| bertscore_f1 | 0.469 |
| coleman_liau | 4.83 |
| coleman_liau_drop | 10.24 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.286 |
| fkgl | 2.31 |
| fkgl_drop | 7.90 |
| fre | 91.0 |
| fre_gain | 53.1 |
| human_edit_recall | 1.000 |
| length_ratio | 0.54 |
| n_words | 7.0 |
| nli_completeness | 0.947 |
| nli_faithfulness | 0.958 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 37.42 |
| smog | 3.13 |
| smog_drop | 8.08 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `cardiac chambers` -> `heart room` | replace | - | - | - | - | - | - | - |
| `within normal limits` -> `normal` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** The four heart rooms are the right size.

| metric | value |
|---|---:|
| bertscore_f1 | 0.401 |
| coleman_liau | 3.70 |
| coleman_liau_drop | 11.37 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.125 |
| fkgl | -0.67 |
| fkgl_drop | 10.88 |
| fre | 114.1 |
| fre_gain | 76.2 |
| human_edit_recall | 1.000 |
| length_ratio | 0.62 |
| n_words | 8.0 |
| nli_completeness | 0.899 |
| nli_faithfulness | 0.948 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 32.80 |
| smog | 3.13 |
| smog_drop | 8.08 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `cardiac chambers` -> `heart rooms` | replace | attributed | 0.199 | 0.316 | 0.915 | 0.940 | 1.304 | - |
| `within normal limits` -> `the right size` | replace | attributed | 0.436 | 0.617 | 0.535 | 0.859 | 0.022 | - |

**edit `cardiac chambers` -> `heart rooms`**

- status: `attributed`
- log p full -0.8985, empty -1.0974
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+1.304` [wiktionary] chambers: A chamber is a room that is often used for sleeping.

- rationale: The original term refers to the internal spaces within the heart where blood is collected and pumped, so "heart rooms" keeps that core idea in simple language. Phrase frequency rises from 3.64 to 4.49, while age of acquisition drops from 11.74 to 5.17. Patients can now visualize the heart's internal structure without needing to know the specific anatomical name.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `within normal limits` -> `the right size`**

- status: `attributed`
- log p full -1.0208, empty -1.4564
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.119` [justplainclear] limits: A certain point that you can't go past; a certain amount but no more
    - `+0.098` [wiktionary] normal: When someone is back to normal, he is healthier and no longer sick.
    - `+0.092` [nih] cardiac: Having to do with the heart.

- rationale: The original phrase "within normal limits" means that a measurement falls in the healthy range, so "the right size" conveys that the value is appropriate without using clinical jargon. Phrase frequency rises from 4.32 to 5.07, and age of acquisition drops from 7.65 to 4.84. Patients can now see that the result is healthy without needing to know what "normal limits" specifically refers to.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

==============================================================================

## Note 58 - `698`

**ORIGINAL**  Digital rectal examination was performed, which showed no masses.

**REFERENCE** Examination of the back passage was performed, which showed no lumps.

| | FKGL | FRE | SMOG | Coleman-Liau | words |
|---|---:|---:|---:|---:|---:|
| ORIGINAL | 11.52 | 28.50 | 11.21 | 16.36 | 9 |
| REFERENCE | 6.94 | 64.92 | 8.84 | 11.56 | 11 |

### Stage 2 - extraction + classification

| term | kind | category | action | Zipf | AoA | syll |
|---|---|---|---|---:|---:|---:|
| `Digital rectal examination` | phrase | medical_essential | elaborate | 2.88 | 13.06 | 10 |
| `performed` | word | general_hard_word | replace | 4.68 | None | 2 |
| `masses` | word | medical_descriptor | replace | 3.94 | 9.42 | 2 |

### Stage 3 - retrieval

coverage **1.0** (3/3), glossary budget 4/16

| term | Zipf stratum | defs | sources | matched via | origin |
|---|---|---:|---|---|---|
| `Digital rectal examination` | rare | 1 | nih.json | exact | extracted |
| `performed` | common | 1 | wiktionary.json | exact | extracted |
| `masses` | uncommon | 2 | wiktionary.json | exact | extracted |

Glossary shown to the model:

1. `[wiktionary]` performed: When you perform something, you do it.
2. `[nih]` digital rectal examination: An examination in which a doctor inserts a lubricated, gloved finger into the rectum to feel for abnormalities. Also called DRE.
3. `[wiktionary]` masses: A measure of how much material is in something.
4. `[wiktionary]` masses: The masses are the regular people, not those in power.

### Stage 4 - arm `naive`

**output:** A doctor checked inside the patient's rectum and did not find any lumps.

| metric | value |
|---|---:|
| bertscore_f1 | 0.465 |
| coleman_liau | 7.80 |
| coleman_liau_drop | 8.56 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.667 |
| fkgl | 5.82 |
| fkgl_drop | 5.70 |
| fre | 76.5 |
| fre_gain | 48.0 |
| human_edit_recall | 1.000 |
| length_ratio | 1.27 |
| n_words | 14.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.110 |
| nli_faithfulness | 0.684 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.286 |
| sari | 19.02 |
| smog | 3.13 |
| smog_drop | 8.08 |

### Stage 4 - arm `termonly`

**output:** A doctor felt inside the rectum and found no lumps.

| metric | value |
|---|---:|
| bertscore_f1 | 0.488 |
| coleman_liau | 5.02 |
| coleman_liau_drop | 11.34 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.333 |
| fkgl | 3.65 |
| fkgl_drop | 7.87 |
| fre | 86.7 |
| fre_gain | 58.2 |
| human_edit_recall | 1.000 |
| length_ratio | 0.91 |
| n_words | 10.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.383 |
| nli_faithfulness | 0.811 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.286 |
| sari | 23.48 |
| smog | 3.13 |
| smog_drop | 8.08 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `Digital rectal examination` -> `doctor felt inside the rectum` | replace | - | - | - | - | - | - | - |
| `masses` -> `lumps` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** A doctor felt inside the rectum and found no lumps.

| metric | value |
|---|---:|
| bertscore_f1 | 0.488 |
| coleman_liau | 5.02 |
| coleman_liau_drop | 11.34 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.333 |
| fkgl | 3.65 |
| fkgl_drop | 7.87 |
| fre | 86.7 |
| fre_gain | 58.2 |
| human_edit_recall | 1.000 |
| length_ratio | 0.91 |
| n_words | 10.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.383 |
| nli_faithfulness | 0.811 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.286 |
| sari | 23.48 |
| smog | 3.13 |
| smog_drop | 8.08 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `Digital rectal examination` -> `doctor felt inside the rectum` | replace | attributed | 0.244 | 0.263 | - | 0.935 | 1.002 | - |
| `masses` -> `lumps` | replace | attributed | -0.071 | -0.482 | - | 0.732 | 0.090 | - |

**edit `Digital rectal examination` -> `doctor felt inside the rectum`**

- status: `attributed`
- log p full -2.5009, empty -2.7450
- masks scored: 18/18 (+4 top-k)
- ranked sources:
    - `+1.002` [nih] digital rectal examination: An examination in which a doctor inserts a lubricated, gloved finger into the rect
    - `-0.109` [wiktionary] masses: The masses are the regular people, not those in power.
    - `-0.111` [wiktionary] performed: When you perform something, you do it.

- rationale: The original term refers to a doctor using a finger to check the rectum, so "doctor felt inside the rectum" describes that physical action in plain words. Phrase frequency increases from 2.88 to 2.95, while age of acquisition drops from 13.06 to 9.84. Patients can now understand exactly what the doctor is doing without needing to know the formal medical procedure.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `masses` -> `lumps`**

- status: `attributed`
- log p full -0.1972, empty -0.1264
- masks scored: 18/18 (+4 top-k)
- ranked sources:
    - `+0.175` [wiktionary] performed: When you perform something, you do it.
    - `+0.084` [wiktionary] masses: A measure of how much material is in something.
    - `-0.059` [nih] digital rectal examination: An examination in which a doctor inserts a lubricated, gloved finger into the rect
    - `-0.681` [wiktionary] masses: The masses are the regular people, not those in power.

- rationale: The original term refers to abnormal growths or clumps of tissue, so "lumps" conveys that physical shape in simpler language. Phrase frequency increases from Zipf 3.94 to 3.19, while syllable count drops from 2 to 1. Patients can now visualize the physical presence of these growths without needing to know the clinical label.
- audit: coverage 1.0, grounding_error=True, omission=False, source_ok=True, passage_ok=True

==============================================================================

## Note 59 - `699`

**ORIGINAL**  He then had a problem with seizures, hemiparesis, has been to the hospital, developed C-diff, and is in the nursing home currently.

**REFERENCE** He then had a problem with fits, weakness on one side, has been to the hospital, developed an infection in the gut, and is in the nursing home currently.

| | FKGL | FRE | SMOG | Coleman-Liau | words |
|---|---:|---:|---:|---:|---:|
| ORIGINAL | 11.23 | 53.76 | 14.55 | 10.27 | 23 |
| REFERENCE | 12.00 | 60.71 | 14.55 | 7.18 | 29 |

### Stage 2 - extraction + classification

| term | kind | category | action | Zipf | AoA | syll |
|---|---|---|---|---:|---:|---:|
| `hemiparesis` | word | medical_descriptor | replace | 1.49 | None | 3 |
| `seizures` | word | medical_essential | elaborate | 3.59 | None | 2 |
| `C-diff` | abbreviation | abbreviation_essential | abbr_expand_elaborate | None | None | 2 |

### Stage 3 - retrieval

coverage **1.0** (3/3), glossary budget 7/16

| term | Zipf stratum | defs | sources | matched via | origin |
|---|---|---:|---|---|---|
| `hemiparesis` | very_rare | 1 | readme_lay_vocab.jsonl | exact | extracted |
| `seizures` | uncommon | 3 | readme_lay_vocab.jsonl, wiktionary.json | exact | extracted |
| `C-diff` | unknown | 3 | dorland_medical_abbreviations.csv, nih.json, readme_lay_vocab.jsonl | exact | extracted |

Glossary shown to the model:

1. `[readme]` hemiparesis: Weakness on one side of the body.
2. `[dorland]` C-diff: Clostridioides difficile
3. `[readme]` seizures: Seizures are when the brain has strange electrical activity that may make someone lose consciousness or have jerky movements.
4. `[readme]` Clostridium difficile colitis: A type of gut infection that causes symptoms like fever, diarrhea, and cramps.
5. `[readme]` Seizures: Seizures are when the brain has sudden abnormal activity that can lead to loss of consciousness and muscle movements.
6. `[nih]` Clostridium difficile: A type of bacterium found in human and animal waste. Clostridium difficile is a common cause of diarrhea that occurs in hospitals. It can also cause diarrhea or other intestinal disorders in patients treated with antibiotics.
7. `[wiktionary]` seizures: If someone seizes (takes) something from someone by force, or arrests someone, it is a seizure.

### Stage 4 - arm `naive`

**output:** He then had seizures, weakness on one side of his body, went to the hospital, developed C-diff, and is currently in the nursing home.

| metric | value |
|---|---:|
| bertscore_f1 | 0.668 |
| coleman_liau | 8.10 |
| coleman_liau_drop | 2.17 |
| copy_jargon_rate | 0.667 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 10.98 |
| fkgl_drop | 0.25 |
| fre | 59.1 |
| fre_gain | 5.3 |
| human_edit_recall | 0.333 |
| length_ratio | 0.86 |
| n_words | 25.0 |
| nli_completeness | 0.861 |
| nli_faithfulness | 0.978 |
| replacement_f1 | 0.500 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.667 |
| sari | 36.00 |
| smog | 13.02 |
| smog_drop | 1.53 |
| temporality_preservation | 1.000 |

### Stage 4 - arm `termonly`

**output:** He then had a problem with shaking fits, weakness on one side of his body, has been to the hospital, developed a bad gut infection, and is in the nursing home currently.

| metric | value |
|---|---:|
| bertscore_f1 | 0.856 |
| coleman_liau | 7.38 |
| coleman_liau_drop | 2.89 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.667 |
| fkgl | 13.48 |
| fkgl_drop | -2.26 |
| fre | 55.4 |
| fre_gain | 1.6 |
| human_edit_recall | 1.000 |
| length_ratio | 1.10 |
| n_words | 32.0 |
| nli_completeness | 0.351 |
| nli_faithfulness | 0.843 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 77.63 |
| smog | 14.55 |
| smog_drop | 0.00 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `seizures` -> `shaking fits` | replace | - | - | - | - | - | - | - |
| `hemiparesis` -> `weakness on one side of his body` | replace | - | - | - | - | - | - | - |
| `C-diff` -> `a bad gut infection` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** He then had a problem with jerky movements, weakness on one side of the body, has been to the hospital, developed a gut infection, and is in the nursing home currently.

| metric | value |
|---|---:|
| bertscore_f1 | 0.818 |
| coleman_liau | 8.13 |
| coleman_liau_drop | 2.14 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 13.63 |
| fkgl_drop | -2.40 |
| fre | 52.6 |
| fre_gain | -1.2 |
| human_edit_recall | 1.000 |
| length_ratio | 1.07 |
| n_words | 31.0 |
| nli_completeness | 0.274 |
| nli_faithfulness | 0.909 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 75.82 |
| smog | 14.55 |
| smog_drop | 0.00 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `seizures` -> `jerky movements` | replace | attributed | 5.706 | 6.268 | 0.776 | 0.877 | 6.078 | - |
| `hemiparesis` -> `weakness on one side of the body` | replace | attributed | 1.716 | 1.989 | 0.867 | 0.874 | 1.632 | - |
| `C-diff` -> `a gut infection` | replace | attributed | 1.791 | 2.406 | 0.918 | 0.932 | 3.602 | - |

**edit `seizures` -> `jerky movements`**

- status: `attributed`
- log p full -0.8417, empty -6.5478
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+6.324` [readme] seizures: Seizures are when the brain has strange electrical activity that may make someone lose consciousness
    - `+0.246` [readme] hemiparesis: Weakness on one side of the body.
    - `+0.081` [readme] Clostridium difficile colitis: A type of gut infection that causes symptoms like fever, diarrhea, and cramps.

- rationale: The glossary defines seizures as strange electrical activity in the brain that may cause jerky movements, so the replacement keeps that physical description in plain words. Phrase frequency increases from 3.59 to 3.08, while syllable count rises from 2 to 4. Patients can now visualize the physical shaking without needing to know about brain electrical activity.
- audit: coverage 1.0, grounding_error=True, omission=False, source_ok=True, passage_ok=True

**edit `hemiparesis` -> `weakness on one side of the body`**

- status: `attributed`
- log p full -1.2845, empty -3.0009
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+1.735` [readme] hemiparesis: Weakness on one side of the body.
    - `+0.103` [readme] seizures: Seizures are when the brain has strange electrical activity that may make someone lose consciousness
    - `+0.069` [wiktionary] seizures: If someone seizes (takes) something from someone by force, or arrests someone, it is a seizure.

- rationale: The glossary defines hemiparesis as weakness on one side of the body, so the replacement phrase keeps that specific symptom in plain language. Phrase frequency increases from 1.49 to 4.14, while syllable count rises from 3 to 9. Patients can now recognize the physical limitation without needing to know the medical term.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `C-diff` -> `a gut infection`**

- status: `attributed`
- log p full -0.6834, empty -2.4744
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+3.707` [readme] Clostridium difficile colitis: A type of gut infection that causes symptoms like fever, diarrhea, and cramps.
    - `+0.105` [readme] seizures: Seizures are when the brain has strange electrical activity that may make someone lose consciousness
    - `-0.163` [wiktionary] seizures: If someone seizes (takes) something from someone by force, or arrests someone, it is a seizure.

- rationale: The glossary defines C-diff as a specific type of gut infection that causes symptoms like fever, diarrhea, and cramps, so "a gut infection" keeps this central medical condition in plain language. Syllable count increases from 2 to 5, while the phrase frequency rises from 3.4 to 4.2. Patients can now understand the basic nature of the illness without needing to know the specific abbreviation.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

==============================================================================

## Note 60 - `700`

**ORIGINAL**  He has been on continuous positive airway pressure now for several months, and returns for followup to review his response to treatment.

**REFERENCE** He has been using a breathing mask now for several months, and returns for follow up to review how he is doing with the treatment.

| | FKGL | FRE | SMOG | Coleman-Liau | words |
|---|---:|---:|---:|---:|---:|
| ORIGINAL | 12.30 | 46.07 | 13.02 | 12.65 | 22 |
| REFERENCE | 9.74 | 69.79 | 3.13 | 7.14 | 25 |

### Stage 2 - extraction + classification

| term | kind | category | action | Zipf | AoA | syll |
|---|---|---|---|---:|---:|---:|
| `continuous positive airway pressure` | phrase | medical_essential | elaborate | 3.14 | 11.39 | 11 |
| `continuous` | word | medical_descriptor | replace | - | - | - |
| `positive` | word | medical_descriptor | replace | - | - | - |
| `airway` | word | medical_descriptor | replace | - | - | - |
| `pressure` | word | medical_descriptor | replace | - | - | - |
| `followup` | word | general_hard_word | replace | 2.87 | None | 3 |

### Stage 3 - retrieval

coverage **0.5** (1/2), glossary budget 13/16

| term | Zipf stratum | defs | sources | matched via | origin |
|---|---|---:|---|---|---|
| `continuous positive airway pressure` | rare | 0 | - | - | extracted |
| `continuous` | uncommon | 3 | readme_lay_vocab.jsonl, wiktionary.json | exact | split_from_uncovered |
| `positive` | common | 4 | readme_lay_vocab.jsonl, wiktionary.json | exact | split_from_uncovered |
| `airway` | rare | 2 | wiktionary.json | exact | split_from_uncovered |
| `pressure` | common | 2 | wiktionary.json | exact | split_from_uncovered |
| `followup` | rare | 2 | readme_lay_vocab.jsonl | exact | extracted |

Glossary shown to the model:

1. `[wiktionary]` airway: The airway in our body refers to the trachea.
2. `[wiktionary]` pressure: In science, pressure is force applied over an area.
3. `[readme]` followup: Going back to your doctor for a checkup or follow-up appointment.
4. `[readme]` continuous: Continuous means something that never stops or has interruptions.
5. `[readme]` Positive: Something is there.
6. `[wiktionary]` airway: An airway is a path an aircraft takes.
7. `[wiktionary]` pressure: If a person is under pressure, they feel stressed.
8. `[readme]` followup: Going back to the doctor or caregiver for a check-up later on.
9. `[wiktionary]` continuous: Something that is continuous happens without stopping.
10. `[readme]` POSITIVE: Something is good or beneficial.
11. `[wiktionary]` continuous: If a surface is continuous, it is long and doesn't have anything in the middle.
12. `[wiktionary]` positive: If something is positive, it is good, happy, or wanted.
13. `[wiktionary]` positive: If you are positive about something, you are sure that you are not mistaken.

### Stage 4 - arm `naive`

**output:** He has been using continuous positive airway pressure for several months and is back for a checkup to see how well the treatment is working.

| metric | value |
|---|---:|
| bertscore_f1 | 0.665 |
| coleman_liau | 9.70 |
| coleman_liau_drop | 2.95 |
| copy_jargon_rate | 0.833 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 11.62 |
| fkgl_drop | 0.68 |
| fre | 56.3 |
| fre_gain | 10.2 |
| human_edit_recall | 0.167 |
| length_ratio | 1.00 |
| n_words | 25.0 |
| nli_completeness | 0.993 |
| nli_faithfulness | 0.991 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 0.286 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.600 |
| sari | 48.42 |
| smog | 11.21 |
| smog_drop | 1.82 |
| temporality_preservation | 0.000 |

### Stage 4 - arm `termonly`

**output:** He has used a breathing machine for several months and returns for a checkup to review his response to treatment.

| metric | value |
|---|---:|
| bertscore_f1 | 0.789 |
| coleman_liau | 9.69 |
| coleman_liau_drop | 2.96 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.167 |
| fkgl | 8.73 |
| fkgl_drop | 3.57 |
| fre | 68.1 |
| fre_gain | 22.0 |
| human_edit_recall | 1.000 |
| length_ratio | 0.80 |
| n_words | 20.0 |
| nli_completeness | 0.808 |
| nli_faithfulness | 0.855 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.286 |
| sari | 53.10 |
| smog | 3.13 |
| smog_drop | 9.89 |
| temporality_preservation | 0.000 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `continuous positive airway pressure` -> `a breathing machine` | replace | - | - | - | - | - | - | - |
| `followup` -> `a checkup` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** He has used a breathing machine that pushes air into his lungs for several months, and returns for a checkup to review his response to treatment.

| metric | value |
|---|---:|
| bertscore_f1 | 0.698 |
| coleman_liau | 9.38 |
| coleman_liau_drop | 3.26 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.167 |
| fkgl | 10.89 |
| fkgl_drop | 1.41 |
| fre | 63.3 |
| fre_gain | 17.2 |
| human_edit_recall | 1.000 |
| length_ratio | 1.04 |
| n_words | 26.0 |
| nli_completeness | 0.914 |
| nli_faithfulness | 0.834 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.286 |
| sari | 52.45 |
| smog | 3.13 |
| smog_drop | 9.89 |
| temporality_preservation | 0.000 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `continuous positive airway pressure` -> `breathing machine that pushes air into his lungs` | replace | attributed | -0.570 | -0.582 | 0.503 | 0.667 | 0.142 | - |
| `followup` -> `checkup` | replace | attributed | 0.341 | 0.781 | 0.742 | 0.885 | 2.400 | - |

**edit `continuous positive airway pressure` -> `breathing machine that pushes air into his lungs`**

- status: `attributed`
- log p full -4.1354, empty -3.5658
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.602` [wiktionary] pressure: In science, pressure is force applied over an area.
    - `+0.460` [wiktionary] airway: An airway is a path an aircraft takes.
    - `+0.371` [readme] Positive: Something is there.
    - `+0.153` [wiktionary] pressure: If a person is under pressure, they feel stressed.
    - `+0.105` [wiktionary] continuous: Something that is continuous happens without stopping.

- rationale: The original term describes a medical device that maintains steady air pressure to keep airways open, so the replacement phrase "breathing machine that pushes air into his lungs" conveys this function in simple, visual language. Phrase frequency increases from Zipf 3.14 to 3.45, while age of acquisition drops from 11.39 to 6.53. Patients can now grasp the purpose of the equipment without needing to know the technical jargon.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `followup` -> `checkup`**

- status: `attributed`
- log p full -0.4200, empty -0.7609
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+3.348` [readme] followup: Going back to your doctor for a checkup or follow-up appointment.
    - `+0.948` [wiktionary] positive: If you are positive about something, you are sure that you are not mistaken.
    - `+0.924` [wiktionary] pressure: If a person is under pressure, they feel stressed.
    - `+0.515` [wiktionary] airway: An airway is a path an aircraft takes.
    - `+0.498` [readme] Positive: Something is there.

- rationale: The original term "followup" refers to a scheduled return visit to monitor health, while "checkup" conveys the same idea of a routine medical examination in simpler language. Phrase frequency increases from Zipf 2.87 to 2.88, and syllable count decreases from 3 to 2. Patients can now recognize the appointment as a standard health review without needing to parse the compound word.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

==============================================================================

## Note 61 - `709`

**ORIGINAL**  The patient to take small bite and small sips to help decrease the risk of aspiration and penetration.

**REFERENCE** The patient is to take small bite and small sips to help decrease the risk of having the food or drink going down the wrong pipe and piercing the pipe.

| | FKGL | FRE | SMOG | Coleman-Liau | words |
|---|---:|---:|---:|---:|---:|
| ORIGINAL | 8.47 | 66.37 | 11.21 | 9.62 | 18 |
| REFERENCE | 9.88 | 77.69 | 3.13 | 6.61 | 30 |

### Stage 2 - extraction + classification

| term | kind | category | action | Zipf | AoA | syll |
|---|---|---|---|---:|---:|---:|
| `penetration` | word | medical_descriptor | replace | 3.71 | 11.05 | 4 |
| `aspiration` | word | medical_descriptor | replace | 3.3 | 11.47 | 4 |

### Stage 3 - retrieval

coverage **1.0** (2/2), glossary budget 6/16

| term | Zipf stratum | defs | sources | matched via | origin |
|---|---|---:|---|---|---|
| `penetration` | uncommon | 2 | wiktionary.json | exact | extracted |
| `aspiration` | rare | 4 | iowa.json, nih.json, readme_lay_vocab.jsonl | exact | extracted |

Glossary shown to the model:

1. `[wiktionary]` penetration: Penetration is the action of penetrating into something.
2. `[readme]` aspiration: Breathing food or liquid into your lungs by mistake.
3. `[wiktionary]` penetration: Penetration is the penis being inserted into the vagina or another part of the body during sex.
4. `[readme]` aspiration: Breathing in food or liquid by mistake.
5. `[nih]` aspiration: Removal of fluid or tissue through a needle. Also, the accidental breathing in of food or fluid into the lungs.
6. `[iowa]` ASPIRATION: fluid entering the lungs, such as after vomiting

### Stage 4 - arm `naive`

**output:** The patient should take small bites and small sips to help decrease the risk of aspiration and penetration.

| metric | value |
|---|---:|
| bertscore_f1 | 0.628 |
| coleman_liau | 11.23 |
| coleman_liau_drop | -1.61 |
| copy_jargon_rate | 1.000 |
| critical_error | 0.000 |
| fkgl | 8.47 |
| fkgl_drop | 0.00 |
| fre | 66.4 |
| fre_gain | 0.0 |
| human_edit_recall | 0.000 |
| length_ratio | 0.60 |
| n_words | 18.0 |
| nli_completeness | 0.995 |
| nli_faithfulness | 0.995 |
| replacement_f1 | 0.000 |
| rewrite_aggressiveness | 1.000 |
| sari | 32.39 |
| severity_downgrade | 0.000 |
| severity_preservation | 1.000 |
| severity_tier_input | 1.000 |
| severity_tier_output | 1.000 |
| smog | 11.21 |
| smog_drop | 0.00 |

### Stage 4 - arm `termonly`

**output:** The patient should take small bites and sips to lower the risk of food going into the lungs or airway.

| metric | value |
|---|---:|
| bertscore_f1 | 0.629 |
| coleman_liau | 6.50 |
| coleman_liau_drop | 3.12 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 6.96 |
| fkgl_drop | 1.51 |
| fre | 80.8 |
| fre_gain | 14.4 |
| human_edit_recall | 1.000 |
| length_ratio | 0.67 |
| n_words | 20.0 |
| nli_completeness | 0.741 |
| nli_faithfulness | 0.619 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.600 |
| sari | 27.56 |
| severity_downgrade | 0.000 |
| severity_preservation | 1.000 |
| severity_tier_input | 1.000 |
| severity_tier_output | 1.000 |
| smog | 3.13 |
| smog_drop | 8.08 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `aspiration` -> `food going into the lungs or airway` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** The patient should take small bites and sips to lower the risk of food or liquid going into the lungs by mistake.

| metric | value |
|---|---:|
| bertscore_f1 | 0.636 |
| coleman_liau | 6.85 |
| coleman_liau_drop | 2.78 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 8.01 |
| fkgl_drop | 0.47 |
| fre | 76.8 |
| fre_gain | 10.5 |
| human_edit_recall | 1.000 |
| length_ratio | 0.73 |
| n_words | 22.0 |
| nli_completeness | 0.501 |
| nli_faithfulness | 0.560 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.600 |
| sari | 27.83 |
| severity_downgrade | 0.000 |
| severity_preservation | 1.000 |
| severity_tier_input | 1.000 |
| severity_tier_output | 1.000 |
| smog | 3.13 |
| smog_drop | 8.08 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `aspiration` -> `food or liquid going into the lungs by mistake` | replace | attributed | 5.808 | 5.819 | 0.874 | 0.921 | 0.467 | - |

**edit `aspiration` -> `food or liquid going into the lungs by mistake`**

- status: `attributed`
- log p full -4.5599, empty -10.3683
- masks scored: 66/66 (+2 top-k)
- ranked sources:
    - `+2.579` [readme] aspiration: Breathing food or liquid into your lungs by mistake.
    - `+2.112` [readme] aspiration: Breathing in food or liquid by mistake.
    - `+0.103` [nih] aspiration: Removal of fluid or tissue through a needle. Also, the accidental breathing in of food or fluid in
    - `+0.025` [iowa] ASPIRATION: fluid entering the lungs, such as after vomiting

- rationale: The glossary defines aspiration as breathing food or liquid into your lungs by mistake, so the replacement phrase keeps that specific error in plain words. Phrase frequency increases from 3.30 to 3.76, while age of acquisition drops from 11.47 to 6.52. You can now clearly see how a simple swallowing error can lead to a serious breathing problem.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

==============================================================================

## Note 62 - `714`

**ORIGINAL**  The patient was awakened and extubated and moved to the recovery room in satisfactory condition.

**REFERENCE** The patient was awakened and tube was removed from the airway and moved to the recovery room in satisfactory condition.

| | FKGL | FRE | SMOG | Coleman-Liau | words |
|---|---:|---:|---:|---:|---:|
| ORIGINAL | 12.29 | 33.69 | 15.90 | 13.55 | 15 |
| REFERENCE | 11.09 | 51.18 | 14.55 | 11.43 | 20 |

### Stage 2 - extraction + classification

| term | kind | category | action | Zipf | AoA | syll |
|---|---|---|---|---:|---:|---:|
| `satisfactory` | word | general_hard_word | replace | 3.57 | 8.84 | 4 |
| `extubated` | word | medical_essential | elaborate | 1.26 | None | 4 |
| `awakened` | word | general_hard_word | replace | 3.3 | None | 3 |

### Stage 3 - retrieval

coverage **1.0** (3/3), glossary budget 5/16

| term | Zipf stratum | defs | sources | matched via | origin |
|---|---|---:|---|---|---|
| `satisfactory` | uncommon | 2 | michigan_plmd.json, wiktionary.json | exact | extracted |
| `extubated` | very_rare | 2 | readme_lay_vocab.jsonl | exact | extracted |
| `awakened` | rare | 1 | wiktionary.json | exact | extracted |

Glossary shown to the model:

1. `[wiktionary]` awakened: If you awaken somebody, they stop sleeping because of something you do.
2. `[michigan]` satisfactory: When something is okay or good.
3. `[readme]` extubated: Not having a breathing tube anymore.
4. `[wiktionary]` satisfactory: If something is satisfactory, it is good enough.
5. `[readme]` extubated: Taking out a tube used for breathing.

### Stage 4 - arm `naive`

**output:** The patient woke up, had the breathing tube removed, and was moved to the recovery room in good condition.

| metric | value |
|---|---:|
| bertscore_f1 | 0.738 |
| coleman_liau | 8.59 |
| coleman_liau_drop | 4.96 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.667 |
| fkgl | 7.97 |
| fkgl_drop | 4.32 |
| fre | 71.8 |
| fre_gain | 38.1 |
| human_edit_recall | 1.000 |
| length_ratio | 0.95 |
| n_words | 19.0 |
| nli_completeness | 0.991 |
| nli_faithfulness | 0.988 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 36.87 |
| smog | 11.21 |
| smog_drop | 4.70 |

### Stage 4 - arm `termonly`

**output:** The patient woke up, had the breathing tube removed, and went to recovery feeling okay.

| metric | value |
|---|---:|
| bertscore_f1 | 0.584 |
| coleman_liau | 9.29 |
| coleman_liau_drop | 4.25 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.667 |
| fkgl | 7.57 |
| fkgl_drop | 4.72 |
| fre | 67.5 |
| fre_gain | 33.8 |
| human_edit_recall | 1.000 |
| length_ratio | 0.75 |
| n_words | 15.0 |
| nli_completeness | 0.983 |
| nli_faithfulness | 0.990 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 16.13 |
| smog | 8.84 |
| smog_drop | 7.06 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `awakened` -> `woke up` | replace | - | - | - | - | - | - | - |
| `extubated` -> `removed` | replace | - | - | - | - | - | - | - |
| `satisfactory` -> `okay` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** The patient woke up, had the breathing tube removed, and went to recovery feeling okay.

| metric | value |
|---|---:|
| bertscore_f1 | 0.584 |
| coleman_liau | 9.29 |
| coleman_liau_drop | 4.25 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.667 |
| fkgl | 7.57 |
| fkgl_drop | 4.72 |
| fre | 67.5 |
| fre_gain | 33.8 |
| human_edit_recall | 1.000 |
| length_ratio | 0.75 |
| n_words | 15.0 |
| nli_completeness | 0.983 |
| nli_faithfulness | 0.990 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 16.13 |
| smog | 8.84 |
| smog_drop | 7.06 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `awakened` -> `woke up` | replace | attributed | 0.038 | 0.085 | - | 0.484 | 0.000 | - |
| `extubated` -> `removed` | replace | attributed | 0.007 | 0.112 | - | 0.490 | 0.117 | - |
| `satisfactory` -> `okay` | replace | attributed | 0.939 | 2.413 | - | 0.916 | 2.245 | - |

**edit `awakened` -> `woke up`**

- status: `attributed`
- log p full -0.5816, empty -0.6198
- masks scored: 34/34 (+5 top-k)
- ranked sources:
    - `-0.045` [wiktionary] satisfactory: If something is satisfactory, it is good enough.
    - `-0.126` [readme] extubated: Taking out a tube used for breathing.

- rationale: The original term means to stop sleeping and start being conscious, so "woke up" conveys that same transition in everyday language. Phrase frequency rises from 3.30 to 4.22, while syllable count drops from 3 to 2. Patients can now grasp the moment of consciousness without needing to process a more formal verb.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `extubated` -> `removed`**

- status: `attributed`
- log p full -0.0598, empty -0.0667
- masks scored: 34/34 (+5 top-k)
- ranked sources:
    - `+0.174` [readme] extubated: Taking out a tube used for breathing.
    - `+0.056` [michigan] satisfactory: When something is okay or good.
    - `+0.022` [wiktionary] awakened: If you awaken somebody, they stop sleeping because of something you do.
    - `-0.092` [wiktionary] satisfactory: If something is satisfactory, it is good enough.

- rationale: The original term describes the act of taking a breathing tube out of a patient, so "removed" conveys that same action in simple language. Phrase frequency rises from 1.26 to 4.79, while syllable count drops from 4 to 2. Patients can now clearly understand that the tube is gone without needing to know the specific medical procedure.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `satisfactory` -> `okay`**

- status: `attributed`
- log p full -0.1665, empty -1.1060
- masks scored: 34/34 (+5 top-k)
- ranked sources:
    - `+2.501` [michigan] satisfactory: When something is okay or good.
    - `+0.256` [wiktionary] awakened: If you awaken somebody, they stop sleeping because of something you do.
    - `-0.077` [readme] extubated: Taking out a tube used for breathing.
    - `-0.327` [wiktionary] satisfactory: If something is satisfactory, it is good enough.

- rationale: The original term "satisfactory" means meeting an acceptable standard, while "okay" conveys that same sense of adequacy in simpler language. Phrase frequency rises from 3.57 to 5.06, and age of acquisition drops from 8.84 to 3.43, making the word more common and easier to learn. Patients can now grasp that the medical result is acceptable without needing to process a more formal adjective.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

==============================================================================

## Note 63 - `721`

**ORIGINAL**  PHYSICAL EXAMINATION : GENERAL : The patient was asleep, but easily aroused.

**REFERENCE** The patient was asleep, but easily woken up.

| | FKGL | FRE | SMOG | Coleman-Liau | words |
|---|---:|---:|---:|---:|---:|
| ORIGINAL | 15.45 | 2.11 | 14.55 | 16.62 | 10 |
| REFERENCE | 6.71 | 61.24 | 8.84 | 5.88 | 8 |

### Stage 2 - extraction + classification

| term | kind | category | action | Zipf | AoA | syll |
|---|---|---|---|---:|---:|---:|
| `aroused` | word | general_hard_word | replace | 3.35 | None | 2 |

### Stage 3 - retrieval

coverage **1.0** (1/1), glossary budget 1/16

| term | Zipf stratum | defs | sources | matched via | origin |
|---|---|---:|---|---|---|
| `aroused` | rare | 1 | wiktionary.json | exact | extracted |

Glossary shown to the model:

1. `[wiktionary]` aroused: If something arouses a feeling or emotion, it causes that feeling or emotion.

### Stage 4 - arm `naive`

**output:** The patient was asleep but woke up easily when someone called their name.

| metric | value |
|---|---:|
| bertscore_f1 | 0.681 |
| coleman_liau | 8.69 |
| coleman_liau_drop | 7.93 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 5.82 |
| fkgl_drop | 9.63 |
| fre | 76.5 |
| fre_gain | 74.4 |
| human_edit_recall | 1.000 |
| length_ratio | 1.62 |
| n_words | 13.0 |
| nli_completeness | 0.492 |
| nli_faithfulness | 0.079 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 59.74 |
| smog | 8.84 |
| smog_drop | 5.71 |

### Stage 4 - arm `termonly`

**output:** The patient was asleep, but easily woke up.

| metric | value |
|---|---:|
| bertscore_f1 | 0.935 |
| coleman_liau | 5.15 |
| coleman_liau_drop | 11.47 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 5.23 |
| fkgl_drop | 10.22 |
| fre | 71.8 |
| fre_gain | 69.7 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 8.0 |
| nli_completeness | 0.411 |
| nli_faithfulness | 0.988 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 70.83 |
| smog | 8.84 |
| smog_drop | 5.71 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `aroused` -> `woke up` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** The patient was asleep, but woke up easily.

| metric | value |
|---|---:|
| bertscore_f1 | 0.876 |
| coleman_liau | 5.15 |
| coleman_liau_drop | 11.47 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 5.23 |
| fkgl_drop | 10.22 |
| fre | 71.8 |
| fre_gain | 69.7 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 8.0 |
| nli_completeness | 0.458 |
| nli_faithfulness | 0.978 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 62.05 |
| smog | 8.84 |
| smog_drop | 5.71 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `aroused` -> `woke up` | replace | attributed | 0.687 | 0.812 | - | - | - | - |

**edit `aroused` -> `woke up`**

- status: `attributed`
- log p full -1.5485, empty -2.2350
- masks scored: 4/4 (+1 top-k)
- ranked sources:
    - `+0.772` [wiktionary] aroused: If something arouses a feeling or emotion, it causes that feeling or emotion.

- rationale: The original term "aroused" refers to the state of waking from sleep, which the replacement "woke up" expresses in simple, everyday language. Phrase frequency increases from 3.35 to 4.22, while syllable count remains constant at 2. Patients can now immediately recognize the action of waking without needing to interpret a more formal or ambiguous verb.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

==============================================================================

## Note 64 - `725`

**ORIGINAL**  He is to follow up in approximately 10 days for recheck as well as prescription for intended AFOs, which he will need up to 6 months.

**REFERENCE** He is to come back in approximately 10 days for recheck as well as prescription for intended foot-drop braces, which he will need up to 6 months.

| | FKGL | FRE | SMOG | Coleman-Liau | words |
|---|---:|---:|---:|---:|---:|
| ORIGINAL | 10.89 | 63.31 | 13.02 | 6.71 | 26 |
| REFERENCE | 11.55 | 60.36 | 13.02 | 8.02 | 28 |

### Stage 2 - extraction + classification

| term | kind | category | action | Zipf | AoA | syll |
|---|---|---|---|---:|---:|---:|
| `approximately` | word | general_hard_word | replace | 4.64 | None | 5 |
| `AFOs` | abbreviation | abbreviation_essential | abbr_expand_elaborate | 1.36 | None | 1 |

### Stage 3 - retrieval

coverage **1.0** (2/2), glossary budget 3/16

| term | Zipf stratum | defs | sources | matched via | origin |
|---|---|---:|---|---|---|
| `approximately` | common | 1 | wiktionary.json | exact | extracted |
| `AFOs` | very_rare | 2 | dorland_medical_abbreviations.csv, justplainclear.json | afo | extracted |

Glossary shown to the model:

1. `[wiktionary]` approximately: Approximately is close to, but not exactly.
2. `[justplainclear]` AFO: Also known as: ankle-foot orthosis, walking boot A brace that supports your ankle or foot An AFO is a brace usually made of plastic that is worn on your lower leg and foot to: • Support your ankle • Hold your ankle in the right position • Improve your ability to walk
3. `[dorland]` AFOs: ankle-foot orthosis

### Stage 4 - arm `naive`

**output:** He will come back in about 10 days for a checkup and to get a prescription for the AFOs he will need to use for up to 6 months.

| metric | value |
|---|---:|
| bertscore_f1 | 0.606 |
| coleman_liau | 2.78 |
| coleman_liau_drop | 3.93 |
| copy_jargon_rate | 1.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 9.15 |
| fkgl_drop | 1.74 |
| fre | 81.1 |
| fre_gain | 17.8 |
| human_edit_recall | 0.000 |
| length_ratio | 1.04 |
| n_words | 29.0 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.994 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 0.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.667 |
| sari | 29.34 |
| smog | 8.84 |
| smog_drop | 4.18 |

### Stage 4 - arm `termonly`

**output:** He will return in about 10 days for a checkup and new medicine orders, which he will need for up to 6 months.

| metric | value |
|---|---:|
| bertscore_f1 | 0.599 |
| coleman_liau | 4.35 |
| coleman_liau_drop | 2.36 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 8.26 |
| fkgl_drop | 2.63 |
| fre | 76.8 |
| fre_gain | 13.5 |
| human_edit_recall | 1.000 |
| length_ratio | 0.82 |
| n_words | 23.0 |
| nli_completeness | 0.040 |
| nli_faithfulness | 0.965 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.571 |
| sari | 27.87 |
| smog | 8.84 |
| smog_drop | 4.18 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `approximately` -> `about` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** He will return in about 10 days for a checkup and a prescription for a brace he will need for up to 6 months.

| metric | value |
|---|---:|
| bertscore_f1 | 0.639 |
| coleman_liau | 3.51 |
| coleman_liau_drop | 3.20 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 8.03 |
| fkgl_drop | 2.86 |
| fre | 80.3 |
| fre_gain | 16.9 |
| human_edit_recall | 1.000 |
| length_ratio | 0.86 |
| n_words | 24.0 |
| nli_completeness | 0.609 |
| nli_faithfulness | 0.947 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.571 |
| sari | 25.97 |
| smog | 8.84 |
| smog_drop | 4.18 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `approximately` -> `about` | replace | attributed | -0.016 | -0.242 | - | 0.833 | 0.371 | - |
| `AFOs` -> `a brace` | replace | attributed | 3.284 | 3.677 | - | 0.929 | 2.631 | - |

**edit `approximately` -> `about`**

- status: `attributed`
- log p full -0.0768, empty -0.0608
- masks scored: 10/10 (+3 top-k)
- ranked sources:
    - `+0.263` [wiktionary] approximately: Approximately is close to, but not exactly.
    - `-0.107` [dorland] AFOs: ankle-foot orthosis
    - `-0.179` [justplainclear] AFO: Also known as: ankle-foot orthosis, walking boot A brace that supports your ankle or foot An AFO is a bra

- rationale: The original term "approximately" signals a value that is close to but not exactly the stated number, while "about" conveys this same sense of estimation in simpler language. Phrase frequency rises from Zipf 4.64 to 6.40, and syllable count drops from 5 to 2. Readers can now grasp the estimated quantity without stumbling over a more formal mathematical qualifier.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `AFOs` -> `a brace`**

- status: `attributed`
- log p full -1.0977, empty -4.3816
- masks scored: 10/10 (+3 top-k)
- ranked sources:
    - `+3.224` [justplainclear] AFO: Also known as: ankle-foot orthosis, walking boot A brace that supports your ankle or foot An AFO is a bra
    - `+0.593` [dorland] AFOs: ankle-foot orthosis
    - `-0.163` [wiktionary] approximately: Approximately is close to, but not exactly.

- rationale: AFOs are ankle-foot orthoses, which are braces that support the foot and ankle, so "a brace" keeps that supportive function in plain words. Phrase frequency increases from Zipf 1.36 to 3.72, while syllable count rises from 1 to 2. Patients can now recognize the device as a standard support tool without needing to know the specific medical abbreviation.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

==============================================================================

## Note 65 - `726`

**ORIGINAL**  Genitourinary : The external genitalia appeared to be normal.

**REFERENCE** The penis/vagina/genitals appeared to be normal.

| | FKGL | FRE | SMOG | Coleman-Liau | words |
|---|---:|---:|---:|---:|---:|
| ORIGINAL | 14.08 | 8.37 | 13.02 | 17.47 | 8 |
| REFERENCE | 12.32 | 17.45 | 8.84 | 17.93 | 8 |

### Stage 2 - extraction + classification

| term | kind | category | action | Zipf | AoA | syll |
|---|---|---|---|---:|---:|---:|
| `external genitalia` | phrase | medical_essential | elaborate | 3.08 | 11.84 | 7 |
| `external` | word | medical_descriptor | replace | - | - | - |
| `genitalia` | word | medical_descriptor | replace | - | - | - |
| `Genitourinary` | word | general_hard_word | replace | 2.02 | None | 4 |

### Stage 3 - retrieval

coverage **0.5** (1/2), glossary budget 6/16

| term | Zipf stratum | defs | sources | matched via | origin |
|---|---|---:|---|---|---|
| `external genitalia` | rare | 0 | - | - | extracted |
| `external` | common | 3 | iowa.json, michigan_plmd.json, wiktionary.json | exact | split_from_uncovered |
| `genitalia` | rare | 1 | wiktionary.json | exact | split_from_uncovered |
| `Genitourinary` | very_rare | 2 | readme_lay_vocab.jsonl | exact | extracted |

Glossary shown to the model:

1. `[wiktionary]` genitalia: Genitalia are the body parts used for sex and reproduction, especially the parts on the outside of the body.
2. `[readme]` Genitourinary: Important body parts involved in sex and peeing.
3. `[iowa]` EXTERNAL: outside the body
4. `[readme]` genitourinary: Body parts used for peeing and sex stuff.
5. `[michigan]` external: Outside of the body.
6. `[wiktionary]` external: Something that is external is not on the inside.

### Stage 4 - arm `naive`

**output:** Genitourinary: The outside parts of the genitals looked normal.

| metric | value |
|---|---:|
| bertscore_f1 | 0.278 |
| coleman_liau | 15.07 |
| coleman_liau_drop | 2.41 |
| copy_jargon_rate | 0.250 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.667 |
| fkgl | 8.90 |
| fkgl_drop | 5.18 |
| fre | 47.3 |
| fre_gain | 38.9 |
| human_edit_recall | 0.750 |
| length_ratio | 1.12 |
| n_words | 9.0 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.994 |
| replacement_f1 | 0.857 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 25.97 |
| smog | 11.21 |
| smog_drop | 1.82 |

### Stage 4 - arm `termonly`

**output:** Genitourinary: The outside parts of the genitals looked normal.

| metric | value |
|---|---:|
| bertscore_f1 | 0.278 |
| coleman_liau | 15.07 |
| coleman_liau_drop | 2.41 |
| copy_jargon_rate | 0.250 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.667 |
| fkgl | 8.90 |
| fkgl_drop | 5.18 |
| fre | 47.3 |
| fre_gain | 38.9 |
| human_edit_recall | 0.750 |
| length_ratio | 1.12 |
| n_words | 9.0 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.994 |
| replacement_f1 | 0.857 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 25.97 |
| smog | 11.21 |
| smog_drop | 1.82 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `external genitalia` -> `outside parts of the genitals` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Genitourinary: The outside sex parts looked normal.

| metric | value |
|---|---:|
| bertscore_f1 | 0.238 |
| coleman_liau | 15.60 |
| coleman_liau_drop | 1.87 |
| copy_jargon_rate | 0.250 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.667 |
| fkgl | 7.37 |
| fkgl_drop | 6.71 |
| fre | 54.7 |
| fre_gain | 46.3 |
| human_edit_recall | 0.750 |
| length_ratio | 0.88 |
| n_words | 7.0 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.982 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 23.89 |
| smog | 8.84 |
| smog_drop | 4.18 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `external genitalia` -> `outside sex parts` | replace | attributed | 1.758 | 1.998 | 0.950 | 0.943 | 0.859 | - |

**edit `external genitalia` -> `outside sex parts`**

- status: `attributed`
- log p full -1.4011, empty -3.1595
- masks scored: 66/66 (+2 top-k)
- ranked sources:
    - `+1.261` [wiktionary] genitalia: Genitalia are the body parts used for sex and reproduction, especially the parts on the outside of 
    - `+0.402` [readme] genitourinary: Body parts used for peeing and sex stuff.
    - `+0.129` [readme] Genitourinary: Important body parts involved in sex and peeing.
    - `+0.083` [wiktionary] external: Something that is external is not on the inside.

- rationale: The glossary defines genitalia as the body parts used for sex and reproduction, especially those located on the outside of the body, so "outside sex parts" keeps this specific location and function in plain language. Phrase frequency increases from Zipf 3.08 to 4.70, while age of acquisition falls from 11.84 to 9.79. Patients can now understand the specific body parts involved in reproduction without needing to know the clinical term.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

==============================================================================

## Note 66 - `727`

**ORIGINAL**  She is postop day 21 of an exploratory laparotomy with ovarian cancer staging.

**REFERENCE** She is 21 days after an open abdominal operation which explored how widespread the ovarian cancer was.

| | FKGL | FRE | SMOG | Coleman-Liau | words |
|---|---:|---:|---:|---:|---:|
| ORIGINAL | 12.17 | 30.95 | 13.02 | 10.92 | 13 |
| REFERENCE | 12.56 | 35.31 | 13.02 | 11.46 | 17 |

### Stage 2 - extraction + classification

| term | kind | category | action | Zipf | AoA | syll |
|---|---|---|---|---:|---:|---:|
| `exploratory laparotomy` | phrase | medical_essential | elaborate | 2.01 | 12.89 | 9 |
| `ovarian cancer staging` | phrase | medical_essential | elaborate | 3.24 | 14.44 | 8 |
| `ovarian` | word | medical_descriptor | replace | - | - | - |
| `cancer staging` | phrase | medical_essential | elaborate | - | - | - |
| `postop` | abbreviation | abbreviation_essential | abbr_expand_elaborate | 1.53 | None | 1 |

### Stage 3 - retrieval

coverage **0.6667** (2/3), glossary budget 9/16

| term | Zipf stratum | defs | sources | matched via | origin |
|---|---|---:|---|---|---|
| `exploratory laparotomy` | very_rare | 2 | readme_lay_vocab.jsonl | exact | extracted |
| `ovarian cancer staging` | rare | 0 | - | - | extracted |
| `ovarian` | rare | 3 | nih.json, readme_lay_vocab.jsonl | exact | split_from_uncovered |
| `cancer staging` | uncommon | 1 | readme_lay_vocab.jsonl | exact | split_from_uncovered |
| `postop` | very_rare | 3 | dorland_medical_abbreviations.csv, readme_lay_vocab.jsonl | exact | extracted |

Glossary shown to the model:

1. `[readme]` cancer staging: Determining the extent to which cancer has spread in the body based on a numerical scale.
2. `[readme]` exploratory laparotomy: Surgery to check for problems in your belly.
3. `[readme]` postop: After surgery.
4. `[readme]` OVARIAN: Related to the female reproductive gland that produces eggs.
5. `[readme]` Exploratory laparotomy: Exploratory laparotomy: Surgery to check the organs in the belly for issues.
6. `[readme]` PostOP: PostOP means after surgery.
7. `[readme]` Ovarian: Ovarian means related to the ovaries where eggs are produced.
8. `[dorland]` postop: postoperation
9. `[nih]` ovarian: Having to do with the ovaries, the female reproductive glands in which the ova (eggs) are formed. The ovaries are located in the pelvis, one on each side of the uterus.

### Stage 4 - arm `naive`

**output:** She is on her twenty-first day after surgery to check for ovarian cancer.

| metric | value |
|---|---:|
| bertscore_f1 | 0.494 |
| coleman_liau | 8.25 |
| coleman_liau_drop | 2.68 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 9.45 |
| fkgl_drop | 2.72 |
| fre | 50.5 |
| fre_gain | 19.5 |
| human_edit_recall | 1.000 |
| length_ratio | 0.82 |
| n_words | 14.0 |
| nli_completeness | 0.357 |
| nli_faithfulness | 0.980 |
| number_unit_preservation | 0.500 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 46.48 |
| smog | 13.02 |
| smog_drop | 0.00 |

### Stage 4 - arm `termonly`

**output:** She is 21 days after her surgery to check her ovaries for cancer.

| metric | value |
|---|---:|
| bertscore_f1 | 0.618 |
| coleman_liau | 5.12 |
| coleman_liau_drop | 5.80 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.600 |
| fkgl | 6.73 |
| fkgl_drop | 5.45 |
| fre | 70.0 |
| fre_gain | 39.0 |
| human_edit_recall | 1.000 |
| length_ratio | 0.76 |
| n_words | 13.0 |
| nli_completeness | 0.284 |
| nli_faithfulness | 0.961 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 50.01 |
| smog | 11.21 |
| smog_drop | 1.82 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `postop` -> `21 days after` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** She is 21 days after surgery to check her belly for ovarian cancer.

| metric | value |
|---|---:|
| bertscore_f1 | 0.635 |
| coleman_liau | 6.02 |
| coleman_liau_drop | 4.91 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 8.54 |
| fkgl_drop | 3.63 |
| fre | 57.0 |
| fre_gain | 26.0 |
| human_edit_recall | 1.000 |
| length_ratio | 0.76 |
| n_words | 13.0 |
| nli_completeness | 0.394 |
| nli_faithfulness | 0.560 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 55.35 |
| smog | 11.21 |
| smog_drop | 1.82 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `postop` -> `21 days after` | replace | attributed | 0.043 | 0.669 | 0.756 | 0.764 | 0.014 | - |
| `ovarian cancer staging` -> `ovarian cancer` | replace | attributed | -0.670 | -1.122 | 0.287 | 0.725 | 0.179 | - |

**edit `postop` -> `21 days after`**

- status: `attributed`
- log p full -0.0469, empty -0.0896
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.140` [readme] PostOP: PostOP means after surgery.
    - `+0.126` [readme] exploratory laparotomy: Surgery to check for problems in your belly.
    - `+0.062` [readme] cancer staging: Determining the extent to which cancer has spread in the body based on a numerical scale.
    - `+0.046` [dorland] postop: postoperation

- rationale: The abbreviation "postop" refers to the period following a surgical procedure, so "21 days after" explicitly states that specific timeframe in plain words. Phrase frequency rises from Zipf 1.53 to 4.94, while syllable count increases from 1 to 4. Patients can now clearly identify the exact recovery window without needing to decode medical shorthand.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `ovarian cancer staging` -> `ovarian cancer`**

- status: `attributed`
- log p full -1.2871, empty -0.6171
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.489` [readme] postop: After surgery.
    - `+0.310` [readme] exploratory laparotomy: Surgery to check for problems in your belly.
    - `+0.106` [readme] cancer staging: Determining the extent to which cancer has spread in the body based on a numerical scale.

- rationale: The original term refers to the specific classification of how far ovarian cancer has spread, while the replacement simply names the disease itself. Phrase frequency increases from 3.24 to 3.45, and age of acquisition remains steady at 14.44. Patients can now focus on the disease identity rather than the complex diagnostic details.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

==============================================================================

## Note 67 - `732`

**ORIGINAL**  Prescription for prednisone as part of his chemotherapy has been given to him.

**REFERENCE** Prescription for steroid tablets as part of his cancer treatment has been given to him.

| | FKGL | FRE | SMOG | Coleman-Liau | words |
|---|---:|---:|---:|---:|---:|
| ORIGINAL | 8.54 | 56.98 | 11.21 | 10.92 | 13 |
| REFERENCE | 7.57 | 67.53 | 8.84 | 10.07 | 15 |

### Stage 2 - extraction + classification

| term | kind | category | action | Zipf | AoA | syll |
|---|---|---|---|---:|---:|---:|
| `chemotherapy` | word | medical_essential | elaborate | 3.56 | 12.53 | 5 |
| `prednisone` | word | medical_essential | elaborate | 2.56 | 17.17 | 2 |

### Stage 3 - retrieval

coverage **1.0** (2/2), glossary budget 10/16

| term | Zipf stratum | defs | sources | matched via | origin |
|---|---|---:|---|---|---|
| `chemotherapy` | uncommon | 7 | iowa.json, justplainclear.json, michigan_plmd.json, nih.json, readme_lay_vocab.jsonl, wiktionary.json | exact | extracted |
| `prednisone` | rare | 3 | nih.json, readme_lay_vocab.jsonl | exact | extracted |

Glossary shown to the model:

1. `[readme]` Prednisone: A medication that lowers the body's immune response and inflammation.
2. `[readme]` chemotherapy: Using drugs to treat cancer or other diseases.
3. `[readme]` prednisone: A medication that helps lower the body's immune system reactions.
4. `[readme]` CHEMOTHERAPY: Using drugs to treat diseases like cancer.
5. `[nih]` prednisone: A drug used to reduce inflammation and lower the body’s immune response.  It is used with other drugs to treat leukemia, lymphoma, and mycosis fungoides (a type of skin lymphoma).    It is also used alone or with other drugs to prevent or treat many other conditions.  These include conditions related to cancer and its treatment, such as anemia (a low level of red blood cells) and allergic reactions. Prednisone is a type of therapeutic glucocorticoid.
6. `[nih]` chemotherapy: Treatment that uses drugs to stop the growth of cancer cells, either by killing the cells or by stopping them from dividing. Chemotherapy may be given by mouth, injection, or infusion, or on the skin, depending on the type and stage of the cancer being treated. It may be given alone or with other treatments, such as surgery, radiation therapy, or biologic therapy.
7. `[iowa]` CHEMOTHERAPY: treatment of disease, usually cancer, by chemical agents
8. `[michigan]` chemotherapy: A drug that kills cancer cells.
9. `[justplainclear]` chemotherapy: A treatment where drugs are used to kill cancer cells These drugs can be given into the vein (intravenous) or by mouth (pill).
10. `[wiktionary]` chemotherapy: Chemotherapy is the chemical treatment intended to be kill the cancerous cells in a patient.

### Stage 4 - arm `naive`

**output:** A doctor has given him a prescription for prednisone to use as part of his chemotherapy.

| metric | value |
|---|---:|
| bertscore_f1 | 0.506 |
| coleman_liau | 8.45 |
| coleman_liau_drop | 2.47 |
| copy_jargon_rate | 1.000 |
| critical_error | 0.000 |
| drug_preservation | 1.000 |
| fkgl | 9.09 |
| fkgl_drop | -0.55 |
| fre | 58.4 |
| fre_gain | 1.4 |
| human_edit_recall | 0.000 |
| length_ratio | 1.07 |
| n_words | 16.0 |
| nli_completeness | 0.990 |
| nli_faithfulness | 0.595 |
| replacement_f1 | 0.000 |
| rewrite_aggressiveness | 1.000 |
| sari | 32.84 |
| smog | 11.21 |
| smog_drop | 0.00 |

### Stage 4 - arm `termonly`

**output:** A medicine called prednisone for his cancer treatment has been given to him.

| metric | value |
|---|---:|
| bertscore_f1 | 0.553 |
| coleman_liau | 10.03 |
| coleman_liau_drop | 0.89 |
| copy_jargon_rate | 0.500 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| drug_preservation | 1.000 |
| fkgl | 6.73 |
| fkgl_drop | 1.82 |
| fre | 70.0 |
| fre_gain | 13.0 |
| human_edit_recall | 0.500 |
| length_ratio | 0.87 |
| n_words | 13.0 |
| nli_completeness | 0.616 |
| nli_faithfulness | 0.981 |
| replacement_f1 | 0.667 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.667 |
| sari | 57.33 |
| smog | 8.84 |
| smog_drop | 2.37 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `chemotherapy` -> `cancer treatment` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** A medicine called prednisone, given with drugs to treat cancer, has been prescribed for him.

| metric | value |
|---|---:|
| bertscore_f1 | 0.393 |
| coleman_liau | 11.23 |
| coleman_liau_drop | -0.30 |
| copy_jargon_rate | 0.500 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| drug_preservation | 1.000 |
| fkgl | 6.78 |
| fkgl_drop | 1.76 |
| fre | 73.2 |
| fre_gain | 16.2 |
| human_edit_recall | 0.500 |
| length_ratio | 1.00 |
| n_words | 15.0 |
| nli_completeness | 0.840 |
| nli_faithfulness | 0.972 |
| replacement_f1 | 0.667 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.667 |
| sari | 23.59 |
| smog | 8.84 |
| smog_drop | 2.37 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `chemotherapy` -> `drugs to treat cancer` | replace | attributed | 3.811 | 3.922 | 0.761 | 0.767 | 0.359 | - |

**edit `chemotherapy` -> `drugs to treat cancer`**

- status: `attributed`
- log p full -2.2378, empty -6.0491
- masks scored: 66/66 (+2 top-k)
- ranked sources:
    - `+1.309` [readme] chemotherapy: Using drugs to treat cancer or other diseases.
    - `+0.950` [readme] CHEMOTHERAPY: Using drugs to treat diseases like cancer.
    - `+0.712` [nih] chemotherapy: Treatment that uses drugs to stop the growth of cancer cells, either by killing the cells or by 
    - `+0.307` [readme] Prednisone: A medication that lowers the body's immune response and inflammation.
    - `+0.122` [nih] prednisone: A drug used to reduce inflammation and lower the body’s immune response.  It is used with other dr

- rationale: The glossary defines chemotherapy as using drugs to treat cancer or other diseases, so "drugs to treat cancer" keeps that core idea in plain language. Phrase frequency increases from 3.56 to 4.33, while age of acquisition falls from 12.53 to 8.39. Patients can now understand the treatment method without needing to know the specific medical name.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

==============================================================================

## Note 68 - `738`

**ORIGINAL**  Photic stimulation was performed, but no clear-cut photic driving was seen.

**REFERENCE** Visual stimulation was performed, but no clear-cut changes in electrical activity of the brain was seen.

| | FKGL | FRE | SMOG | Coleman-Liau | words |
|---|---:|---:|---:|---:|---:|
| ORIGINAL | 9.08 | 49.54 | 8.84 | 14.20 | 12 |
| REFERENCE | 12.78 | 31.97 | 14.55 | 13.52 | 17 |

### Stage 2 - extraction + classification

| term | kind | category | action | Zipf | AoA | syll |
|---|---|---|---|---:|---:|---:|
| `Photic stimulation` | phrase | medical_essential | elaborate | 1.8 | 8.63 | 6 |
| `Photic` | word | medical_descriptor | replace | - | - | - |
| `stimulation` | word | medical_descriptor | replace | - | - | - |
| `photic driving` | phrase | medical_essential | elaborate | 1.81 | None | 4 |
| `photic` | word | medical_descriptor | replace | - | - | - |
| `driving` | word | medical_descriptor | replace | - | - | - |
| `clear-cut` | word | general_hard_word | replace | 4.94 | None | 2 |

### Stage 3 - retrieval

coverage **0.3333** (1/3), glossary budget 8/16

| term | Zipf stratum | defs | sources | matched via | origin |
|---|---|---:|---|---|---|
| `Photic stimulation` | very_rare | 0 | - | - | extracted |
| `Photic` | very_rare | 1 | dictonary.csv | exact | split_from_uncovered |
| `stimulation` | uncommon | 2 | readme_lay_vocab.jsonl, wiktionary.json | exact | split_from_uncovered |
| `photic driving` | very_rare | 0 | - | - | extracted |
| `photic` | very_rare | 1 | dictonary.csv | exact | split_from_uncovered |
| `driving` | common | 2 | wiktionary.json | exact | split_from_uncovered |
| `clear-cut` | unknown | 2 | dictonary.csv | exact | extracted |

Glossary shown to the model:

1. `[dictionary]` Photic (a.): Relating to the production of light by the lower animals.
2. `[dictionary]` Photic (a.): Relating to the production of light by the lower animals.
3. `[dictionary]` Clear-cut (a.): Having a sharp, distinct outline, like that of a cameo.
4. `[readme]` stimulation: Making something more active or alert.
5. `[wiktionary]` driving: If you drive a car or other vehicle, you control its movement and direction.
6. `[dictionary]` Clear-cut (a.): Concisely and distinctly expressed.
7. `[wiktionary]` stimulation: Stimulation is an action that encourages something to develop or become more active.
8. `[wiktionary]` driving: If something is driving, it is moving quickly and strongly.

### Stage 4 - arm `naive`

**output:** They shined a flashing light in the patient's eyes, but the patient did not show any clear reaction to the flashing.

| metric | value |
|---|---:|
| bertscore_f1 | 0.362 |
| coleman_liau | 8.48 |
| coleman_liau_drop | 5.72 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.167 |
| fkgl | 8.33 |
| fkgl_drop | 0.75 |
| fre | 72.7 |
| fre_gain | 23.2 |
| human_edit_recall | 1.000 |
| length_ratio | 1.29 |
| n_words | 22.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.924 |
| nli_faithfulness | 0.124 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 18.75 |
| smog | 8.84 |
| smog_drop | 0.00 |

### Stage 4 - arm `termonly`

**output:** Light flashes were used, but no obvious brain response was seen.

| metric | value |
|---|---:|
| bertscore_f1 | 0.613 |
| coleman_liau | 8.93 |
| coleman_liau_drop | 5.27 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.167 |
| fkgl | 4.79 |
| fkgl_drop | 4.29 |
| fre | 80.3 |
| fre_gain | 30.8 |
| human_edit_recall | 1.000 |
| length_ratio | 0.65 |
| n_words | 11.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.956 |
| nli_faithfulness | 0.813 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.200 |
| sari | 26.44 |
| smog | 8.84 |
| smog_drop | 0.00 |

annotation backend `novita`, 0 edits kept


### Stage 4 - arm `grounded`

**output:** They flashed lights at the patient, but no obvious strong reaction was seen.

| metric | value |
|---|---:|
| bertscore_f1 | 0.390 |
| coleman_liau | 9.58 |
| coleman_liau_drop | 4.62 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 5.82 |
| fkgl_drop | 3.26 |
| fre | 76.5 |
| fre_gain | 27.0 |
| human_edit_recall | 1.000 |
| length_ratio | 0.76 |
| n_words | 13.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.910 |
| nli_faithfulness | 0.168 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.200 |
| sari | 26.31 |
| smog | 11.21 |
| smog_drop | -2.37 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `Photic stimulation` -> `flashed lights at the patient` | replace | attributed | 0.217 | 0.226 | -0.001 | 0.449 | 0.040 | - |
| `clear-cut` -> `obvious` | replace | attributed | -0.396 | -0.871 | 0.782 | 0.861 | 0.108 | - |
| `photic driving` -> `strong reaction` | replace | attributed | 3.992 | 4.019 | 0.906 | 0.938 | 2.309 | - |

**edit `Photic stimulation` -> `flashed lights at the patient`**

- status: `attributed`
- log p full -3.0918, empty -3.3090
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+0.143` [dictionary] Clear-cut (a.): Concisely and distinctly expressed.
    - `+0.103` [wiktionary] driving: If you drive a car or other vehicle, you control its movement and direction.
    - `+0.040` [dictionary] Clear-cut (a.): Having a sharp, distinct outline, like that of a cameo.
    - `+0.026` [dictionary] Photic (a.): Relating to the production of light by the lower animals.

- rationale: The original term refers to shining bright lights into a patient's eyes to observe their brain's reaction, so "flashed lights at the patient" describes this action in plain words. Phrase frequency increases from Zipf 1.80 to 3.31, while age of acquisition falls from 8.63 to 7.05. Patients can now understand the specific visual test being performed without needing to know the technical procedure name.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `clear-cut` -> `obvious`**

- status: `attributed`
- log p full -0.8267, empty -0.4305
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+0.216` [dictionary] Photic (a.): Relating to the production of light by the lower animals.
    - `+0.108` [wiktionary] stimulation: Stimulation is an action that encourages something to develop or become more active.
    - `+0.041` [wiktionary] driving: If you drive a car or other vehicle, you control its movement and direction.
    - `+0.019` [dictionary] Photic (a.): Relating to the production of light by the lower animals.
    - `-0.122` [readme] stimulation: Making something more active or alert.

- rationale: The original term "clear-cut" means something that is distinct and easy to see, so "obvious" keeps that sense of clarity in plain language. Phrase frequency increases from Zipf 4.94 to 4.63, while syllable count rises from 2 to 3. Patients can now grasp the concept of something being unmistakable without needing to know the specific hyphenated adjective.
- audit: coverage 1.0, grounding_error=True, omission=False, source_ok=True, passage_ok=True

**edit `photic driving` -> `strong reaction`**

- status: `attributed`
- log p full -3.5961, empty -7.5877
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+2.782` [wiktionary] driving: If something is driving, it is moving quickly and strongly.
    - `+0.473` [readme] stimulation: Making something more active or alert.
    - `+0.401` [dictionary] Clear-cut (a.): Having a sharp, distinct outline, like that of a cameo.
    - `+0.267` [wiktionary] stimulation: Stimulation is an action that encourages something to develop or become more active.

- rationale: The glossary defines driving as moving quickly and strongly, so "strong reaction" keeps that sense of force in plain words. Phrase frequency increases from Zipf 1.81 to 4.61, while syllable count remains at 4. Patients can now grasp the intensity of the response without needing to know the specific technical term.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

==============================================================================

## Note 69 - `739`

**ORIGINAL**  FAMILY HISTORY : Both parents died with myocardial infarctions.

**REFERENCE** Family history: Both parents died with heart attacks.

| | FKGL | FRE | SMOG | Coleman-Liau | words |
|---|---:|---:|---:|---:|---:|
| ORIGINAL | 15.56 | -2.21 | 14.55 | 18.93 | 8 |
| REFERENCE | 8.18 | 50.67 | 11.21 | 12.40 | 8 |

### Stage 2 - extraction + classification

| term | kind | category | action | Zipf | AoA | syll |
|---|---|---|---|---:|---:|---:|
| `myocardial infarctions` | phrase | medical_essential | elaborate | 1.57 | 16.64 | 8 |

### Stage 3 - retrieval

coverage **1.0** (1/1), glossary budget 5/16

| term | Zipf stratum | defs | sources | matched via | origin |
|---|---|---:|---|---|---|
| `myocardial infarctions` | very_rare | 5 | iowa.json, justplainclear.json, michigan_plmd.json, readme_lay_vocab.jsonl | myocardial infarction | extracted |

Glossary shown to the model:

1. `[readme]` inferior wall myocardial infarction: Heart damage at the bottom of the left ventricle due to a blocked artery.
2. `[readme]` inferior myocardial infarction: A heart attack caused by a blockage in a blood vessel that affects the lower part of the heart muscle.
3. `[iowa]` MYOCARDIAL INFARCTION: heart attack
4. `[michigan]` myocardial infarction: Occurs when the flow of blood to the heart is stopped by a blood clot or a spasm of an artery. Also called a heart attack or MI.
5. `[justplainclear]` myocardial infarction: A heart attack

### Stage 4 - arm `naive`

**output:** Both parents died from heart attacks.

| metric | value |
|---|---:|
| bertscore_f1 | 0.641 |
| coleman_liau | 9.23 |
| coleman_liau_drop | 9.69 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 2.48 |
| fkgl_drop | 13.07 |
| fre | 87.9 |
| fre_gain | 90.2 |
| human_edit_recall | 1.000 |
| laterality_preservation | 1.000 |
| length_ratio | 0.75 |
| n_words | 6.0 |
| nli_completeness | 0.568 |
| nli_faithfulness | 0.927 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 36.98 |
| smog | 3.13 |
| smog_drop | 11.43 |

### Stage 4 - arm `termonly`

**output:** Both parents died from heart attacks.

| metric | value |
|---|---:|
| bertscore_f1 | 0.641 |
| coleman_liau | 9.23 |
| coleman_liau_drop | 9.69 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 2.48 |
| fkgl_drop | 13.07 |
| fre | 87.9 |
| fre_gain | 90.2 |
| human_edit_recall | 1.000 |
| laterality_preservation | 1.000 |
| length_ratio | 0.75 |
| n_words | 6.0 |
| nli_completeness | 0.568 |
| nli_faithfulness | 0.927 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 36.98 |
| smog | 3.13 |
| smog_drop | 11.43 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `myocardial infarctions` -> `heart attacks` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Both parents died from heart attacks.

| metric | value |
|---|---:|
| bertscore_f1 | 0.641 |
| coleman_liau | 9.23 |
| coleman_liau_drop | 9.69 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 2.48 |
| fkgl_drop | 13.07 |
| fre | 87.9 |
| fre_gain | 90.2 |
| human_edit_recall | 1.000 |
| laterality_preservation | 1.000 |
| length_ratio | 0.75 |
| n_words | 6.0 |
| nli_completeness | 0.568 |
| nli_faithfulness | 0.927 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 36.98 |
| smog | 3.13 |
| smog_drop | 11.43 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `myocardial infarctions` -> `heart attacks` | replace | attributed | 0.015 | 0.280 | - | 0.749 | 0.384 | - |

**edit `myocardial infarctions` -> `heart attacks`**

- status: `attributed`
- log p full -0.0470, empty -0.0618
- masks scored: 34/34 (+2 top-k)
- ranked sources:
    - `+0.384` [michigan] myocardial infarction: Occurs when the flow of blood to the heart is stopped by a blood clot or a spasm of an 
    - `-0.004` [readme] inferior wall myocardial infarction: Heart damage at the bottom of the left ventricle due to a blocked artery.
    - `-0.384` [justplainclear] myocardial infarction: A heart attack

- rationale: The original term refers to tissue death in the heart muscle caused by blocked blood flow, so "heart attacks" conveys this life-threatening event in plain language. Phrase frequency rises from Zipf 1.57 to 4.59, while age of acquisition drops from 16.64 to 5.17. Patients can now grasp the severity of the condition without needing specialized medical vocabulary.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

==============================================================================

## Note 70 - `740`

**ORIGINAL**  Extremities : 2+ bilateral pitting edema to the level of the knees.

**REFERENCE** Hands and feet: There is swelling in both feet up to the level of the knees (when pressed, causes an indentation in the skin for a few seconds)

| | FKGL | FRE | SMOG | Coleman-Liau | words |
|---|---:|---:|---:|---:|---:|
| ORIGINAL | 11.23 | 34.16 | 13.02 | 9.45 | 11 |
| REFERENCE | 10.08 | 72.67 | 8.84 | 6.34 | 28 |

### Stage 2 - extraction + classification

| term | kind | category | action | Zipf | AoA | syll |
|---|---|---|---|---:|---:|---:|
| `bilateral pitting edema` | phrase | medical_descriptor | replace | 2.64 | 15.07 | 9 |
| `bilateral` | word | medical_descriptor | replace | - | - | - |
| `pitting edema` | phrase | medical_essential | elaborate | - | - | - |
| `Extremities` | word | general_hard_word | replace | 2.97 | None | 4 |

### Stage 3 - retrieval

coverage **0.5** (1/2), glossary budget 11/16

| term | Zipf stratum | defs | sources | matched via | origin |
|---|---|---:|---|---|---|
| `bilateral pitting edema` | rare | 0 | - | - | extracted |
| `bilateral` | uncommon | 8 | justplainclear.json, michigan_plmd.json, nih.json, readme_lay_vocab.jsonl, thesarus.json, wiktionary.json | exact | split_from_uncovered |
| `pitting edema` | rare | 2 | readme_lay_vocab.jsonl | exact | split_from_uncovered |
| `Extremities` | rare | 1 | wiktionary.json | exact | extracted |

Glossary shown to the model:

1. `[wiktionary]` extremities: An extremity is a part of an animal's body that is used to move around and to hold objects.
2. `[readme]` pitting edema: Swelling in the body that leaves an indention (pit) when pressed.
3. `[readme]` bilateral: Having two sides or parts on the body or an organ.
4. `[readme]` Pitting edema: Swelling caused by trapped fluid in tissues where pressed skin leaves a temporary pit.
5. `[readme]` Bilateral: Having two sides or affecting both sides of the body or structure.
6. `[nih]` bilateral: Affecting both the right and left sides of the body.
7. `[michigan]` bilateral: On both sides.
8. `[justplainclear]` bilateral: On both sides, two sided, even, balanced
9. `[wiktionary]` bilateral: If something is bilateral, it has two sides.
10. `[wiktionary]` bilateral: If something is bilateral, it involves two parties.
11. `[thesaurus]` bilateral: with both sides considered, two-sided, when both sides get a say, even, balanced

### Stage 4 - arm `naive`

**output:** The patient has 2+ pitting edema in both legs that goes up to the knees.

| metric | value |
|---|---:|
| bertscore_f1 | 0.271 |
| coleman_liau | 3.88 |
| coleman_liau_drop | 5.57 |
| copy_jargon_rate | 0.250 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.333 |
| fkgl | 5.21 |
| fkgl_drop | 6.02 |
| fre | 84.5 |
| fre_gain | 50.3 |
| human_edit_recall | 0.750 |
| laterality_preservation | 1.000 |
| length_ratio | 0.54 |
| n_words | 15.0 |
| nli_completeness | 0.855 |
| nli_faithfulness | 0.885 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 0.857 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 31.40 |
| smog | 8.84 |
| smog_drop | 4.18 |

### Stage 4 - arm `termonly`

**output:** Her arms and legs had swollen, soft spots down to the knees.

| metric | value |
|---|---:|
| bertscore_f1 | 0.253 |
| coleman_liau | 4.45 |
| coleman_liau_drop | 5.00 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 1.87 |
| fkgl_drop | 9.35 |
| fre | 103.0 |
| fre_gain | 68.8 |
| human_edit_recall | 1.000 |
| laterality_preservation | 0.000 |
| length_ratio | 0.43 |
| n_words | 12.0 |
| nli_completeness | 0.158 |
| nli_faithfulness | 0.650 |
| number_unit_preservation | 0.000 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.200 |
| sari | 32.61 |
| smog | 3.13 |
| smog_drop | 9.89 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `Extremities` -> `arms and legs` | replace | - | - | - | - | - | - | - |
| `bilateral pitting edema` -> `swollen, soft spots` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Both arms and legs have 2+ swelling that leaves a dent to the knees.

| metric | value |
|---|---:|
| bertscore_f1 | 0.340 |
| coleman_liau | 4.04 |
| coleman_liau_drop | 5.41 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 2.51 |
| fkgl_drop | 8.71 |
| fre | 102.0 |
| fre_gain | 67.8 |
| human_edit_recall | 1.000 |
| laterality_preservation | 1.000 |
| length_ratio | 0.50 |
| n_words | 14.0 |
| nli_completeness | 0.905 |
| nli_faithfulness | 0.623 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.200 |
| sari | 33.22 |
| smog | 3.13 |
| smog_drop | 9.89 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `pitting edema` -> `swelling that leaves a dent` | replace | attributed | 0.044 | 0.045 | 0.837 | 0.898 | 0.045 | - |

**edit `pitting edema` -> `swelling that leaves a dent`**

- status: `attributed`
- log p full -3.3876, empty -3.4313
- masks scored: 66/66 (+2 top-k)
- ranked sources:
    - `+0.710` [readme] pitting edema: Swelling in the body that leaves an indention (pit) when pressed.
    - `+0.665` [readme] Pitting edema: Swelling caused by trapped fluid in tissues where pressed skin leaves a temporary pit.
    - `+0.316` [thesaurus] bilateral: with both sides considered, two-sided, when both sides get a say, even, balanced
    - `+0.018` [readme] Bilateral: Having two sides or affecting both sides of the body or structure.

- rationale: The original term describes fluid buildup in the tissues that creates a temporary indentation when pressed, so "swelling that leaves a dent" captures that physical sign in plain language. Phrase frequency increases from Zipf 2.67 to 3.36, while age of acquisition drops from 15.07 to 7.33. Patients can now recognize the physical symptom of fluid retention without needing to know the specific medical jargon.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

==============================================================================

## Note 71 - `741`

**ORIGINAL**  Following questions are mostly involved in a psychosocial donor evaluation.

**REFERENCE** Following questions are mostly involved in a donor evaluation of their psychological or social states.

| | FKGL | FRE | SMOG | Coleman-Liau | words |
|---|---:|---:|---:|---:|---:|
| ORIGINAL | 14.27 | 10.56 | 13.02 | 18.94 | 10 |
| REFERENCE | 13.86 | 22.41 | 13.02 | 15.87 | 15 |

### Stage 2 - extraction + classification

| term | kind | category | action | Zipf | AoA | syll |
|---|---|---|---|---:|---:|---:|
| `psychosocial` | word | medical_descriptor | replace | 2.88 | 15.44 | 3 |

### Stage 3 - retrieval

coverage **1.0** (1/1), glossary budget 2/16

| term | Zipf stratum | defs | sources | matched via | origin |
|---|---|---:|---|---|---|
| `psychosocial` | rare | 2 | michigan_plmd.json, nih.json | exact | extracted |

Glossary shown to the model:

1. `[nih]` psychosocial: In medicine, having to do with the mental, emotional, social, and spiritual effects of a disease, such as cancer. Some of the psychosocial effects of cancer are changes in how a patient thinks, their feelings, moods, beliefs, ways of coping, and relationships with family, friends, and co-workers. There are different kinds of psychosocial support that can help cancer patients, including counseling, education, group support, and spiritual support.
2. `[michigan]` psychosocial: Including both the mental and social aspects of disease.

### Stage 4 - arm `naive`

**output:** The questions below are mostly used for a psychosocial donor evaluation.

| metric | value |
|---|---:|
| bertscore_f1 | 0.532 |
| coleman_liau | 13.67 |
| coleman_liau_drop | 5.27 |
| copy_jargon_rate | 1.000 |
| critical_error | 0.000 |
| fkgl | 11.23 |
| fkgl_drop | 3.04 |
| fre | 34.2 |
| fre_gain | 23.6 |
| human_edit_recall | 0.000 |
| length_ratio | 0.73 |
| n_words | 11.0 |
| nli_completeness | 0.985 |
| nli_faithfulness | 0.985 |
| replacement_f1 | 0.000 |
| rewrite_aggressiveness | 1.000 |
| sari | 13.45 |
| smog | 11.21 |
| smog_drop | 1.82 |

### Stage 4 - arm `termonly`

**output:** The questions mostly check the donor's social and mental health.

| metric | value |
|---|---:|
| bertscore_f1 | 0.493 |
| coleman_liau | 11.98 |
| coleman_liau_drop | 6.96 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 6.01 |
| fkgl_drop | 8.26 |
| fre | 69.8 |
| fre_gain | 59.2 |
| human_edit_recall | 1.000 |
| length_ratio | 0.73 |
| n_words | 11.0 |
| nli_completeness | 0.982 |
| nli_faithfulness | 0.543 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.750 |
| sari | 15.19 |
| smog | 3.13 |
| smog_drop | 9.89 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `psychosocial` -> `social and mental health` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** The questions mostly check the donor's mental and social situation.

| metric | value |
|---|---:|
| bertscore_f1 | 0.505 |
| coleman_liau | 13.72 |
| coleman_liau_drop | 5.22 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 9.55 |
| fkgl_drop | 4.72 |
| fre | 44.4 |
| fre_gain | 33.8 |
| human_edit_recall | 1.000 |
| length_ratio | 0.73 |
| n_words | 11.0 |
| nli_completeness | 0.983 |
| nli_faithfulness | 0.760 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.750 |
| sari | 15.19 |
| smog | 8.84 |
| smog_drop | 4.18 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `psychosocial` -> `mental and social situation` | replace | attributed | 1.526 | 1.624 | - | 1.000 | 2.184 | - |

**edit `psychosocial` -> `mental and social situation`**

- status: `attributed`
- log p full -2.1535, empty -3.6793
- masks scored: 6/6 (+1 top-k)
- ranked sources:
    - `+1.839` [michigan] psychosocial: Including both the mental and social aspects of disease.
    - `-0.345` [nih] psychosocial: In medicine, having to do with the mental, emotional, social, and spiritual effects of a disease

- rationale: The original term refers to the complex interplay between a person's inner thoughts and their external community life, so "mental and social situation" breaks this abstract concept into two clear, everyday parts. Phrase frequency rises from Zipf 2.88 to 4.57, while age of acquisition drops from 15.44 to 10.43, making the phrase significantly more common and easier to learn at a younger age. Patients can now grasp the full scope of their care needs without getting lost in academic jargon.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

==============================================================================

## Note 72 - `742`

**ORIGINAL**  Mild nonmobile descending aortic atherosclerosis.

**REFERENCE** Mild non-moving hardening of the part of aorta (the largest artery of the body) that goes down the chest and abdomen.

| | FKGL | FRE | SMOG | Coleman-Liau | words |
|---|---:|---:|---:|---:|---:|
| ORIGINAL | 24.12 | -68.96 | 14.55 | 29.32 | 5 |
| REFERENCE | 11.14 | 52.58 | 15.90 | 8.48 | 22 |

### Stage 2 - extraction + classification

| term | kind | category | action | Zipf | AoA | syll |
|---|---|---|---|---:|---:|---:|
| `descending aortic atherosclerosis` | phrase | medical_essential | elaborate | 2.55 | 13.12 | 12 |
| `descending aortic` | phrase | medical_essential | elaborate | - | - | - |
| `atherosclerosis` | word | medical_essential | elaborate | - | - | - |
| `nonmobile` | word | medical_descriptor | replace | 0.0 | None | 3 |

### Stage 3 - retrieval

coverage **0.0** (0/2), glossary budget 4/16

| term | Zipf stratum | defs | sources | matched via | origin |
|---|---|---:|---|---|---|
| `descending aortic atherosclerosis` | rare | 0 | - | - | extracted |
| `descending aortic` | rare | 1 | readme_lay_vocab.jsonl | exact | split_from_uncovered |
| `atherosclerosis` | rare | 3 | justplainclear.json, michigan_plmd.json, thesarus.json | exact | split_from_uncovered |
| `nonmobile` | very_rare | 0 | - | - | extracted |

Glossary shown to the model:

1. `[readme]` descending aortic: Descending aortic: The area of the main artery as it travels through the chest.
2. `[michigan]` atherosclerosis: A disease where your arteries get stiff and clogged by things in your blood, such as fat and calcium, called "plaque".
3. `[justplainclear]` atherosclerosis: A disease where arteries get thick and prevent the flow of blood Normal artery and atherosclerosis
4. `[thesaurus]` atherosclerosis: hardening of the arteries, clogged blood vessels

### Stage 4 - arm `naive`

**output:** The patient has mild atherosclerosis in the aorta that is not moving.

| metric | value |
|---|---:|
| bertscore_f1 | 0.297 |
| coleman_liau | 9.28 |
| coleman_liau_drop | 20.04 |
| copy_jargon_rate | 0.250 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 9.74 |
| fkgl_drop | 14.38 |
| fre | 46.6 |
| fre_gain | 115.6 |
| human_edit_recall | 0.750 |
| length_ratio | 0.55 |
| n_words | 12.0 |
| nli_completeness | 0.851 |
| nli_faithfulness | 0.982 |
| replacement_f1 | 0.857 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 41.56 |
| severity_downgrade | 0.000 |
| severity_preservation | 1.000 |
| severity_tier_input | 1.000 |
| severity_tier_output | 1.000 |
| smog | 11.21 |
| smog_drop | 3.35 |

### Stage 4 - arm `termonly`

**output:** A mild, non-moving plaque buildup in the lower part of the main artery to the body.

| metric | value |
|---|---:|
| bertscore_f1 | 0.453 |
| coleman_liau | 5.91 |
| coleman_liau_drop | 23.41 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 7.61 |
| fkgl_drop | 16.51 |
| fre | 69.0 |
| fre_gain | 137.9 |
| human_edit_recall | 1.000 |
| length_ratio | 0.77 |
| n_words | 17.0 |
| nli_completeness | 0.696 |
| nli_faithfulness | 0.961 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 48.35 |
| severity_downgrade | 0.000 |
| severity_preservation | 1.000 |
| severity_tier_input | 1.000 |
| severity_tier_output | 1.000 |
| smog | 11.21 |
| smog_drop | 3.35 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `nonmobile` -> `non-moving` | replace | - | - | - | - | - | - | - |
| `descending aortic` -> `lower part of the main artery to the body` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Mild plaque buildup in the chest artery that does not move.

| metric | value |
|---|---:|
| bertscore_f1 | 0.382 |
| coleman_liau | 6.82 |
| coleman_liau_drop | 22.50 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 3.72 |
| fkgl_drop | 20.40 |
| fre | 88.0 |
| fre_gain | 157.0 |
| human_edit_recall | 1.000 |
| length_ratio | 0.50 |
| n_words | 11.0 |
| nli_completeness | 0.560 |
| nli_faithfulness | 0.930 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 44.79 |
| severity_downgrade | 0.000 |
| severity_preservation | 1.000 |
| severity_tier_input | 1.000 |
| severity_tier_output | 1.000 |
| smog | 8.84 |
| smog_drop | 5.71 |

annotation backend `novita`, 0 edits kept


==============================================================================

## Note 73 - `750`

**ORIGINAL**  The eustachian tube was obstructed with bone wax.

**REFERENCE** The passage between the nose and the ears was blocked with bone wax.

| | FKGL | FRE | SMOG | Coleman-Liau | words |
|---|---:|---:|---:|---:|---:|
| ORIGINAL | 6.71 | 61.24 | 11.21 | 10.23 | 8 |
| REFERENCE | 3.10 | 96.02 | 3.13 | 6.46 | 13 |

### Stage 2 - extraction + classification

| term | kind | category | action | Zipf | AoA | syll |
|---|---|---|---|---:|---:|---:|
| `eustachian tube` | phrase | medical_essential | elaborate | 1.9 | 5.5 | 5 |
| `obstructed` | word | medical_descriptor | replace | 2.98 | None | 3 |
| `bone wax` | phrase | medical_essential | elaborate | 3.81 | 6.0 | 2 |
| `bone` | word | medical_descriptor | replace | - | - | - |
| `wax` | word | medical_descriptor | replace | - | - | - |

### Stage 3 - retrieval

coverage **0.6667** (2/3), glossary budget 7/16

| term | Zipf stratum | defs | sources | matched via | origin |
|---|---|---:|---|---|---|
| `eustachian tube` | very_rare | 1 | justplainclear.json | exact | extracted |
| `obstructed` | rare | 1 | wiktionary.json | exact | extracted |
| `bone wax` | uncommon | 0 | - | - | extracted |
| `bone` | uncommon | 2 | wiktionary.json | exact | split_from_uncovered |
| `wax` | uncommon | 3 | readme_lay_vocab.jsonl, wiktionary.json | exact | split_from_uncovered |

Glossary shown to the model:

1. `[wiktionary]` obstructed: If something obstructs your way, it blocks your path from point A to point B.
2. `[justplainclear]` eustachian tube: The tube that connects your middle ear to the back of your throat and pharynx area. The openings in your ears and nose both connect in the back of your throat.
3. `[wiktionary]` bone: Bones are the hard, white things inside your body. They give your body its shape.
4. `[readme]` wax: Yellow sticky stuff in your ear that keeps it clean and dry.
5. `[wiktionary]` bone: When two man bone, they have sex.
6. `[wiktionary]` wax: Wax is a solid material made of animal fat.
7. `[wiktionary]` wax: If you wax something, you put wax on it, for example, a car.

### Stage 4 - arm `naive`

**output:** The eustachian tube was blocked with bone wax.

| metric | value |
|---|---:|
| bertscore_f1 | 0.509 |
| coleman_liau | 8.05 |
| coleman_liau_drop | 2.18 |
| copy_jargon_rate | 0.500 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 3.76 |
| fkgl_drop | 2.95 |
| fre | 82.4 |
| fre_gain | 21.1 |
| human_edit_recall | 0.500 |
| length_ratio | 0.62 |
| n_words | 8.0 |
| nli_completeness | 0.993 |
| nli_faithfulness | 0.993 |
| replacement_f1 | 0.667 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 59.31 |
| smog | 8.84 |
| smog_drop | 2.37 |

### Stage 4 - arm `termonly`

**output:** The tube in the ear was blocked with a paste made of bone.

| metric | value |
|---|---:|
| bertscore_f1 | 0.631 |
| coleman_liau | 2.00 |
| coleman_liau_drop | 8.22 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 1.28 |
| fkgl_drop | 5.43 |
| fre | 109.0 |
| fre_gain | 47.8 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 13.0 |
| nli_completeness | 0.614 |
| nli_faithfulness | 0.896 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 37.04 |
| smog | 3.13 |
| smog_drop | 8.08 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `eustachian tube` -> `tube in the ear` | replace | - | - | - | - | - | - | - |
| `obstructed` -> `blocked` | replace | - | - | - | - | - | - | - |
| `bone wax` -> `paste made of bone` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** The tube in the ear was blocked with a hard, sticky substance.

| metric | value |
|---|---:|
| bertscore_f1 | 0.569 |
| coleman_liau | 5.42 |
| coleman_liau_drop | 4.81 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.600 |
| fkgl | 2.86 |
| fkgl_drop | 3.85 |
| fre | 96.0 |
| fre_gain | 34.7 |
| human_edit_recall | 1.000 |
| length_ratio | 0.92 |
| n_words | 12.0 |
| nli_completeness | 0.043 |
| nli_faithfulness | 0.826 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 34.66 |
| smog | 3.13 |
| smog_drop | 8.08 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `eustachian tube` -> `tube in the ear` | replace | attributed | 0.281 | 0.317 | 0.758 | 0.780 | 0.244 | - |
| `obstructed` -> `blocked` | replace | attributed | 0.026 | 1.054 | 0.830 | 0.885 | 0.591 | - |
| `bone wax` -> `a hard, sticky substance` | replace | attributed | 6.146 | 6.168 | 0.947 | 0.930 | 1.890 | - |

**edit `eustachian tube` -> `tube in the ear`**

- status: `attributed`
- log p full -2.0523, empty -2.3334
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+0.295` [wiktionary] bone: Bones are the hard, white things inside your body. They give your body its shape.
    - `+0.051` [justplainclear] eustachian tube: The tube that connects your middle ear to the back of your throat and pharynx area. The openi

- rationale: The eustachian tube is the passage that connects the middle ear to the back of the throat, so "tube in the ear" keeps that anatomical location in plain words. Phrase frequency increases from Zipf 1.90 to 4.09, while age of acquisition remains at 5.50. Patients can now visualize the ear's internal structure without needing to know the specific medical name.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `obstructed` -> `blocked`**

- status: `attributed`
- log p full -0.0144, empty -0.0407
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+0.740` [wiktionary] obstructed: If something obstructs your way, it blocks your path from point A to point B.
    - `+0.149` [wiktionary] bone: Bones are the hard, white things inside your body. They give your body its shape.
    - `+0.084` [readme] wax: Yellow sticky stuff in your ear that keeps it clean and dry.
    - `+0.080` [wiktionary] wax: If you wax something, you put wax on it, for example, a car.
    - `+0.013` [justplainclear] eustachian tube: The tube that connects your middle ear to the back of your throat and pharynx area. The openi

- rationale: The original term means something is prevented from flowing through, so "blocked" conveys that same physical stoppage in simpler language. Phrase frequency rises from Zipf 2.98 to 4.31, while syllable count drops from 3 to 1. Patients can now grasp the physical obstruction without needing to process a more complex medical word.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `bone wax` -> `a hard, sticky substance`**

- status: `attributed`
- log p full -3.8520, empty -9.9983
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+3.188` [readme] wax: Yellow sticky stuff in your ear that keeps it clean and dry.
    - `+1.299` [wiktionary] bone: Bones are the hard, white things inside your body. They give your body its shape.
    - `+1.225` [wiktionary] wax: If you wax something, you put wax on it, for example, a car.
    - `+0.796` [wiktionary] wax: Wax is a solid material made of animal fat.
    - `+0.049` [wiktionary] obstructed: If something obstructs your way, it blocks your path from point A to point B.

- rationale: The glossary defines bone wax as a yellow, sticky substance used to keep an ear clean and dry, so the replacement describes it as a hard, sticky material that performs that same function. Phrase frequency increases from 3.81 to 3.66, while age of acquisition rises from 6.00 to 9.68. Patients can now visualize the physical texture of the material without needing to know the specific medical name.
- audit: coverage 1.0, grounding_error=True, omission=False, source_ok=True, passage_ok=True

==============================================================================

## Note 74 - `752`

**ORIGINAL**  He was placed supine on the operating room table.

**REFERENCE** He was placed facing upwards on the operating room table.

| | FKGL | FRE | SMOG | Coleman-Liau | words |
|---|---:|---:|---:|---:|---:|
| ORIGINAL | 6.28 | 66.10 | 8.84 | 6.69 | 9 |
| REFERENCE | 7.19 | 61.33 | 8.84 | 8.50 | 10 |

### Stage 2 - extraction + classification

| term | kind | category | action | Zipf | AoA | syll |
|---|---|---|---|---:|---:|---:|
| `supine` | word | medical_descriptor | replace | 2.42 | 16.43 | 2 |

### Stage 3 - retrieval

coverage **1.0** (1/1), glossary budget 4/16

| term | Zipf stratum | defs | sources | matched via | origin |
|---|---|---:|---|---|---|
| `supine` | very_rare | 4 | iowa.json, michigan_plmd.json, readme_lay_vocab.jsonl | exact | extracted |

Glossary shown to the model:

1. `[readme]` supine: Lying on your back.
2. `[readme]` Supine: Lying down on your back.
3. `[iowa]` SUPINE: lying on the back
4. `[michigan]` supine: To lie on your back.

### Stage 4 - arm `naive`

**output:** He lay flat on his back on the operating room table.

| metric | value |
|---|---:|
| bertscore_f1 | 0.539 |
| coleman_liau | 3.13 |
| coleman_liau_drop | 3.56 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 4.79 |
| fkgl_drop | 1.48 |
| fre | 80.3 |
| fre_gain | 14.2 |
| human_edit_recall | 1.000 |
| length_ratio | 1.10 |
| n_words | 11.0 |
| nli_completeness | 0.970 |
| nli_faithfulness | 0.981 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 50.81 |
| smog | 8.84 |
| smog_drop | 0.00 |

### Stage 4 - arm `termonly`

**output:** He was placed face up on the operating room table.

| metric | value |
|---|---:|
| bertscore_f1 | 0.896 |
| coleman_liau | 4.44 |
| coleman_liau_drop | 2.25 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 4.83 |
| fkgl_drop | 1.45 |
| fre | 78.2 |
| fre_gain | 12.1 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 10.0 |
| nli_completeness | 0.468 |
| nli_faithfulness | 0.220 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 66.67 |
| smog | 8.84 |
| smog_drop | 0.00 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `supine` -> `face up` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** He was placed on his back on the operating room table.

| metric | value |
|---|---:|
| bertscore_f1 | 0.687 |
| coleman_liau | 4.18 |
| coleman_liau_drop | 2.51 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 4.79 |
| fkgl_drop | 1.48 |
| fre | 80.3 |
| fre_gain | 14.2 |
| human_edit_recall | 1.000 |
| length_ratio | 1.10 |
| n_words | 11.0 |
| nli_completeness | 0.904 |
| nli_faithfulness | 0.962 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 66.67 |
| smog | 8.84 |
| smog_drop | 0.00 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `supine` -> `on his back` | replace | attributed | 0.788 | 1.081 | - | 0.852 | 0.349 | - |

**edit `supine` -> `on his back`**

- status: `attributed`
- log p full -0.9555, empty -1.7433
- masks scored: 18/18 (+2 top-k)
- ranked sources:
    - `+0.702` [readme] supine: Lying on your back.
    - `+0.353` [michigan] supine: To lie on your back.
    - `-0.511` [readme] Supine: Lying down on your back.

- rationale: The original term "supine" means lying flat on the back, so the replacement "on his back" keeps that physical position in plain words. Phrase frequency increases from 2.42 to 5.87, while age of acquisition drops from 16.43 to 5.31. Patients can now easily picture the patient's position without needing to know the medical posture name.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

==============================================================================

## Note 75 - `755`

**ORIGINAL**  A urinalysis was not performed this time.

**REFERENCE** A urine test was not performed this time.

| | FKGL | FRE | SMOG | Coleman-Liau | words |
|---|---:|---:|---:|---:|---:|
| ORIGINAL | 7.37 | 54.70 | 8.84 | 8.14 | 7 |
| REFERENCE | 2.28 | 92.97 | 3.13 | 4.43 | 8 |

### Stage 2 - extraction + classification

| term | kind | category | action | Zipf | AoA | syll |
|---|---|---|---|---:|---:|---:|
| `urinalysis` | word | medical_essential | elaborate | 2.2 | 14.68 | 5 |

### Stage 3 - retrieval

coverage **1.0** (1/1), glossary budget 5/16

| term | Zipf stratum | defs | sources | matched via | origin |
|---|---|---:|---|---|---|
| `urinalysis` | very_rare | 5 | justplainclear.json, michigan_plmd.json, nih.json, readme_lay_vocab.jsonl | exact | extracted |

Glossary shown to the model:

1. `[readme]` Urinalysis: A test that checks what's in your pee.
2. `[readme]` urinalysis: A test that checks the contents of your pee to see what's in there.
3. `[nih]` urinalysis: A test that determines the content of the urine.
4. `[michigan]` urinalysis: A test of your urine to check for diseases, such as diabetes, urinary tract infections, or kidney problems.
5. `[justplainclear]` urinalysis: Also known as: urine test, pee test A test of your urine used to find certain medical conditions

### Stage 4 - arm `naive`

**output:** A urinalysis was not done this time.

| metric | value |
|---|---:|
| bertscore_f1 | 0.824 |
| coleman_liau | 4.00 |
| coleman_liau_drop | 4.14 |
| copy_jargon_rate | 1.000 |
| critical_error | 0.000 |
| fkgl | 5.68 |
| fkgl_drop | 1.69 |
| fre | 66.8 |
| fre_gain | 12.1 |
| human_edit_recall | 0.000 |
| length_ratio | 0.88 |
| n_words | 7.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.993 |
| nli_faithfulness | 0.988 |
| replacement_f1 | 0.000 |
| rewrite_aggressiveness | 1.000 |
| sari | 13.89 |
| smog | 8.84 |
| smog_drop | 0.00 |

### Stage 4 - arm `termonly`

**output:** A urine test was not done this time.

| metric | value |
|---|---:|
| bertscore_f1 | 0.974 |
| coleman_liau | 0.80 |
| coleman_liau_drop | 7.34 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 0.80 |
| fkgl_drop | 6.56 |
| fre | 103.5 |
| fre_gain | 48.8 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 8.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.985 |
| nli_faithfulness | 0.993 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 51.60 |
| smog | 3.13 |
| smog_drop | 5.71 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `urinalysis` -> `urine test` | replace | - | - | - | - | - | - | - |
| `urinalysis` -> `done` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** A urine test was not done this time.

| metric | value |
|---|---:|
| bertscore_f1 | 0.974 |
| coleman_liau | 0.80 |
| coleman_liau_drop | 7.34 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 0.80 |
| fkgl_drop | 6.56 |
| fre | 103.5 |
| fre_gain | 48.8 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 8.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.985 |
| nli_faithfulness | 0.993 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 51.60 |
| smog | 3.13 |
| smog_drop | 5.71 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `urinalysis` -> `urine test` | replace | attributed | -0.504 | -1.077 | - | 0.923 | 1.277 | - |
| `urinalysis` -> `done` | replace | attributed | 0.535 | 1.498 | - | 0.831 | 0.093 | - |

**edit `urinalysis` -> `urine test`**

- status: `attributed`
- log p full -0.9173, empty -0.4134
- masks scored: 34/34 (+4 top-k)
- ranked sources:
    - `+1.299` [justplainclear] urinalysis: Also known as: urine test, pee test A test of your urine used to find certain medical conditions
    - `+0.023` [michigan] urinalysis: A test of your urine to check for diseases, such as diabetes, urinary tract infections, or kidney 
    - `-0.258` [nih] urinalysis: A test that determines the content of the urine.
    - `-0.801` [readme] Urinalysis: A test that checks what's in your pee.
    - `-0.982` [readme] urinalysis: A test that checks the contents of your pee to see what's in there.

- rationale: The original term refers to a laboratory examination of urine, so "urine test" conveys the same idea using everyday language. Phrase frequency rises from 2.20 to 3.82, while age of acquisition drops from 14.68 to 9.83. Patients can now recognize the procedure as a simple check of their urine without needing specialized medical vocabulary.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `urinalysis` -> `done`**

- status: `attributed`
- log p full -0.2277, empty -0.7623
- masks scored: 34/34 (+4 top-k)
- ranked sources:
    - `+0.563` [readme] Urinalysis: A test that checks what's in your pee.
    - `+0.470` [nih] urinalysis: A test that determines the content of the urine.
    - `+0.454` [readme] urinalysis: A test that checks the contents of your pee to see what's in there.
    - `-0.051` [michigan] urinalysis: A test of your urine to check for diseases, such as diabetes, urinary tract infections, or kidney 
    - `-0.062` [justplainclear] urinalysis: Also known as: urine test, pee test A test of your urine used to find certain medical conditions

- rationale: The original term refers to a test of urine, so "done" simply indicates that this check has been completed. Phrase frequency increases from Zipf 2.20 to 5.58, while syllable count drops from 5 to 1. Patients can now grasp that the test is finished without needing to know the specific medical procedure.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

==============================================================================

## Note 76 - `766`

**ORIGINAL**  Vision and hearing appeared to be adequate for testing, although she did indicate that she needed to update her eyeglass prescription.

**REFERENCE** Vision and hearing appeared to be okay for testing, although she did indicate that she needed to update her glasses prescription.

| | FKGL | FRE | SMOG | Coleman-Liau | words |
|---|---:|---:|---:|---:|---:|
| ORIGINAL | 12.27 | 44.52 | 13.02 | 13.72 | 21 |
| REFERENCE | 11.70 | 48.55 | 11.21 | 12.34 | 21 |

### Stage 2 - extraction + classification

| term | kind | category | action | Zipf | AoA | syll |
|---|---|---|---|---:|---:|---:|
| `eyeglass prescription` | phrase | general_hard_word | replace | 2.32 | 9.22 | 5 |
| `eyeglass` | word | medical_descriptor | replace | - | - | - |
| `prescription` | word | medical_descriptor | replace | - | - | - |
| `did indicate` | phrase | general_hard_word | replace | 4.34 | 9.74 | 4 |
| `did` | word | medical_descriptor | replace | - | - | - |
| `indicate` | word | medical_descriptor | replace | - | - | - |
| `adequate` | word | general_hard_word | replace | 4.05 | 10.35 | 3 |

### Stage 3 - retrieval

coverage **0.3333** (1/3), glossary budget 15/16

| term | Zipf stratum | defs | sources | matched via | origin |
|---|---|---:|---|---|---|
| `eyeglass prescription` | very_rare | 0 | - | - | extracted |
| `eyeglass` | very_rare | 1 | justplainclear.json | exact | split_from_uncovered |
| `prescription` | uncommon | 5 | michigan_plmd.json, nih.json, readme_lay_vocab.jsonl, thesarus.json, wiktionary.json | exact | split_from_uncovered |
| `did indicate` | uncommon | 0 | - | - | extracted |
| `did` | common | 1 | wiktionary.json | exact | split_from_uncovered |
| `indicate` | uncommon | 4 | michigan_plmd.json, thesarus.json, wiktionary.json | exact | split_from_uncovered |
| `adequate` | uncommon | 4 | justplainclear.json, michigan_plmd.json, thesarus.json, wiktionary.json | exact | extracted |

Glossary shown to the model:

1. `[justplainclear]` eyeglass: A single lens used to help you see more clearly.
2. `[wiktionary]` did: Do is an auxiliary verb. It is used in questions, negative statements, short answers, and for emphasis when there is no other auxiliary.
3. `[michigan]` adequate: Enough or the right amount.
4. `[michigan]` indicate: To suggest or show.
5. `[readme]` Prescription: A prescription is a doctor's recommendation for medication or treatment.
6. `[justplainclear]` adequate: Enough
7. `[wiktionary]` indicate: If someone indicates something, they point it out or they point to it; they bring your attention to something.
8. `[nih]` prescription: A doctor's order for medicine or another intervention.
9. `[wiktionary]` adequate: If something is adequate, it is good enough.
10. `[wiktionary]` indicate: If someone indicates something, they show signs of something; they show it.
11. `[michigan]` prescription: An order from your doctor, nurse, or physician assistant for drugs or other treatment.
12. `[thesaurus]` adequate: enough, the right amount
13. `[thesaurus]` indicate: suggest, point to
14. `[wiktionary]` prescription: A written order, as by a physician, to tell which medicine to take and how many doses of it is needed.
15. `[thesaurus]` prescription: doctors orders, medicine, drug order

### Stage 4 - arm `naive`

**output:** Her vision and hearing were good enough for the test, but she said she needed to update her eyeglasses prescription.

| metric | value |
|---|---:|
| bertscore_f1 | 0.655 |
| coleman_liau | 10.27 |
| coleman_liau_drop | 3.45 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.167 |
| fkgl | 9.32 |
| fkgl_drop | 2.95 |
| fre | 63.9 |
| fre_gain | 19.4 |
| human_edit_recall | 1.000 |
| length_ratio | 0.95 |
| n_words | 20.0 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.995 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.429 |
| sari | 27.09 |
| smog | 11.21 |
| smog_drop | 1.82 |

### Stage 4 - arm `termonly`

**output:** Her sight and hearing were good enough for the test, though she said she needed to update her glasses.

| metric | value |
|---|---:|
| bertscore_f1 | 0.677 |
| coleman_liau | 7.67 |
| coleman_liau_drop | 6.05 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.286 |
| fkgl | 6.73 |
| fkgl_drop | 5.54 |
| fre | 80.7 |
| fre_gain | 36.2 |
| human_edit_recall | 1.000 |
| length_ratio | 0.90 |
| n_words | 19.0 |
| nli_completeness | 0.990 |
| nli_faithfulness | 0.995 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.444 |
| sari | 28.52 |
| smog | 3.13 |
| smog_drop | 9.89 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `eyeglass prescription` -> `glasses` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Vision and hearing seemed good enough for testing, though she said she needed to update her glasses order.

| metric | value |
|---|---:|
| bertscore_f1 | 0.790 |
| coleman_liau | 10.59 |
| coleman_liau_drop | 3.13 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.286 |
| fkgl | 8.47 |
| fkgl_drop | 3.79 |
| fre | 66.4 |
| fre_gain | 21.8 |
| human_edit_recall | 1.000 |
| length_ratio | 0.86 |
| n_words | 18.0 |
| nli_completeness | 0.985 |
| nli_faithfulness | 0.983 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.286 |
| sari | 32.70 |
| smog | 3.13 |
| smog_drop | 9.89 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `adequate` -> `good enough` | replace | attributed | 1.366 | 1.908 | 0.851 | 0.939 | 2.017 | - |
| `did indicate` -> `said` | replace | attributed | -0.007 | -0.033 | 0.713 | 0.743 | 0.235 | - |
| `eyeglass prescription` -> `glasses order` | replace | attributed | 2.392 | 2.524 | 0.288 | 0.774 | 0.403 | - |

**edit `adequate` -> `good enough`**

- status: `attributed`
- log p full -0.7107, empty -2.0768
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+2.059` [wiktionary] adequate: If something is adequate, it is good enough.
    - `+0.041` [readme] Prescription: A prescription is a doctor's recommendation for medication or treatment.
    - `+0.011` [michigan] prescription: An order from your doctor, nurse, or physician assistant for drugs or other treatment.

- rationale: The glossary defines "adequate" as being good enough, so the replacement keeps that meaning in plain words. Phrase frequency increases from 4.05 to 5.44, while age of acquisition falls from 10.35 to 6.96. Patients can now understand the standard of care without needing to know the specific medical term.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `did indicate` -> `said`**

- status: `attributed`
- log p full -0.2454, empty -0.2383
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+0.489` [wiktionary] did: Do is an auxiliary verb. It is used in questions, negative statements, short answers, and for emphasis wh
    - `+0.254` [readme] Prescription: A prescription is a doctor's recommendation for medication or treatment.
    - `+0.249` [wiktionary] adequate: If something is adequate, it is good enough.
    - `+0.192` [justplainclear] eyeglass: A single lens used to help you see more clearly.
    - `+0.160` [michigan] prescription: An order from your doctor, nurse, or physician assistant for drugs or other treatment.

- rationale: The original phrase "did indicate" means to point out or show something, so "said" conveys that same act of stating in simpler language. Phrase frequency rises from Zipf 4.34 to 6.01, while syllable count drops from 4 to 1. The patient can now grasp the statement without stumbling over a formal verb structure.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `eyeglass prescription` -> `glasses order`**

- status: `attributed`
- log p full -2.0020, empty -4.3938
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+1.301` [michigan] prescription: An order from your doctor, nurse, or physician assistant for drugs or other treatment.
    - `+0.898` [wiktionary] prescription: A written order, as by a physician, to tell which medicine to take and how many doses of it is n
    - `+0.738` [nih] prescription: A doctor's order for medicine or another intervention.
    - `+0.699` [readme] Prescription: A prescription is a doctor's recommendation for medication or treatment.
    - `+0.348` [michigan] indicate: To suggest or show.

- rationale: The original term refers to the specific written instructions for correcting vision, which the replacement phrase "glasses order" conveys as a simple request for corrective lenses. Phrase frequency rises from Zipf 2.32 to 4.31, indicating the new wording is much more common, while age of acquisition drops from 9.22 to 6.26, showing it is learned at a younger age. Patients can now recognize the request for new eyewear without needing to know the technical definition of a prescription.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

==============================================================================

## Note 77 - `771`

**ORIGINAL**  I have talked to him several times about a colonoscopy, which he has refused, and so we have been doing stools for occult blood.

**REFERENCE** I have talked to him several times about a procedure to have a look inside the bowels (colonoscopy), which he has refused, and so we have been testing some stool samples in the lab to look for blood (which may be invisible to the naked eye).

| | FKGL | FRE | SMOG | Coleman-Liau | words |
|---|---:|---:|---:|---:|---:|
| ORIGINAL | 8.03 | 80.25 | 3.13 | 7.62 | 24 |
| REFERENCE | 17.48 | 51.64 | 11.21 | 7.39 | 46 |

### Stage 2 - extraction + classification

| term | kind | category | action | Zipf | AoA | syll |
|---|---|---|---|---:|---:|---:|
| `occult blood` | phrase | medical_descriptor | replace | 3.28 | 12.65 | 3 |
| `occult` | word | medical_descriptor | replace | - | - | - |
| `blood` | word | medical_descriptor | replace | - | - | - |
| `colonoscopy` | word | medical_essential | elaborate | 2.74 | 15.76 | 1 |
| `stools` | word | general_hard_word | replace | 3.05 | None | 1 |

### Stage 3 - retrieval

coverage **0.6667** (2/3), glossary budget 16/16

| term | Zipf stratum | defs | sources | matched via | origin |
|---|---|---:|---|---|---|
| `occult blood` | rare | 0 | - | - | extracted |
| `occult` | rare | 4 | readme_lay_vocab.jsonl, wiktionary.json | exact | split_from_uncovered |
| `blood` | common | 7 | justplainclear.json, michigan_plmd.json, nih.json, readme_lay_vocab.jsonl, wiktionary.json | exact | split_from_uncovered |
| `colonoscopy` | rare | 5 | justplainclear.json, michigan_plmd.json, nih.json, readme_lay_vocab.jsonl | exact | extracted |
| `stools` | rare | 3 | readme_lay_vocab.jsonl, wiktionary.json | exact | extracted |

Glossary shown to the model:

1. `[readme]` stools: Stools are the stuff that comes out when you go to the bathroom.
2. `[readme]` occult: Obscure and mysterious, not easily understood.
3. `[readme]` colonoscopy: A colonoscopy is a test that checks the inside of your large intestine for signs of cancer.
4. `[readme]` blood: Blood is a fluid that carries nutrients and oxygen to different parts of the body.
5. `[readme]` stools: Poop.
6. `[readme]` Occult: Secret knowledge or practices that are mysterious or not easily understood.
7. `[readme]` colonoscopy: A procedure to check for colon cancer by examining the inside of the large intestine.
8. `[readme]` Blood: Blood is a vital fluid that carries nutrients and oxygen to our body's tissues through the heart's pumping action.
9. `[wiktionary]` stools: A stool is a seat for one person that does not have a back or an armrest.
10. `[wiktionary]` occult: If something is occult it is hidden or secret—or it is about hidden or secret things.
11. `[nih]` colonoscopy: Examination of the inside of the colon using a colonoscope, inserted into the rectum. A colonoscope is a thin, tube-like instrument with a light and a lens for viewing. It may also have a tool to remove tissue to be checked under a microscope for signs of disease.
12. `[nih]` blood: A tissue with red blood cells, white blood cells, platelets, and other substances suspended in fluid called plasma. Blood takes oxygen and nutrients to the tissues, and carries away wastes.
13. `[wiktionary]` occult: If something is occult it is part of the universe most people do not see. An occult thing is something that is strange or weird, and might be called magic.
14. `[michigan]` colonoscopy: Looks at the inside of the large intestine using a flexible tube with a ltiny camera at the end.
15. `[michigan]` blood: A fluid in your body that carries things that are needed for your body to work well, such as vitamins, minerals, and oxygen to cells. It also takes waste products away.
16. `[justplainclear]` colonoscopy: An exam of the inside of the large intestine that uses a flexible tube with a lens at the end

### Stage 4 - arm `naive`

**output:** I have talked to him several times about getting a colonoscopy, but he has refused, so we have been testing his stools for hidden blood.

| metric | value |
|---|---:|
| bertscore_f1 | 0.628 |
| coleman_liau | 8.30 |
| coleman_liau_drop | -0.69 |
| copy_jargon_rate | 0.333 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 8.79 |
| fkgl_drop | -0.76 |
| fre | 76.6 |
| fre_gain | -3.7 |
| human_edit_recall | 0.667 |
| length_ratio | 0.54 |
| n_words | 25.0 |
| nli_completeness | 0.987 |
| nli_faithfulness | 0.991 |
| replacement_f1 | 0.800 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 44.47 |
| smog | 3.13 |
| smog_drop | 0.00 |

### Stage 4 - arm `termonly`

**output:** I have talked to him several times about a colon exam, which he has refused, and so we have been checking his poop for hidden blood.

| metric | value |
|---|---:|
| bertscore_f1 | 0.648 |
| coleman_liau | 6.26 |
| coleman_liau_drop | 1.36 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.750 |
| fkgl | 9.53 |
| fkgl_drop | -1.50 |
| fre | 73.1 |
| fre_gain | -7.2 |
| human_edit_recall | 1.000 |
| length_ratio | 0.57 |
| n_words | 26.0 |
| nli_completeness | 0.957 |
| nli_faithfulness | 0.985 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 60.35 |
| smog | 3.13 |
| smog_drop | 0.00 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `colonoscopy` -> `colon exam` | replace | - | - | - | - | - | - | - |
| `stools` -> `poop` | replace | - | - | - | - | - | - | - |
| `occult blood` -> `hidden blood` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** I have talked to him several times about a test for his large intestine, which he has refused, and so we have been checking his poop for hidden blood.

| metric | value |
|---|---:|
| bertscore_f1 | 0.612 |
| coleman_liau | 6.98 |
| coleman_liau_drop | 0.64 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.750 |
| fkgl | 10.37 |
| fkgl_drop | -2.34 |
| fre | 72.4 |
| fre_gain | -7.9 |
| human_edit_recall | 1.000 |
| length_ratio | 0.63 |
| n_words | 29.0 |
| nli_completeness | 0.836 |
| nli_faithfulness | 0.954 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 60.35 |
| smog | 8.84 |
| smog_drop | -5.71 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `colonoscopy` -> `a test for his large intestine` | replace | attributed | 5.202 | 5.220 | 0.858 | 0.955 | 1.677 | - |
| `stools` -> `poop` | replace | attributed | 0.399 | 2.325 | 0.912 | 0.972 | 2.532 | - |
| `occult blood` -> `hidden blood` | replace | attributed | -0.064 | -0.625 | 0.756 | 0.748 | 0.192 | - |

**edit `colonoscopy` -> `a test for his large intestine`**

- status: `attributed`
- log p full -4.0059, empty -9.2076
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+1.970` [readme] colonoscopy: A colonoscopy is a test that checks the inside of your large intestine for signs of cancer.
    - `+0.293` [readme] occult: Obscure and mysterious, not easily understood.
    - `+0.165` [wiktionary] stools: A stool is a seat for one person that does not have a back or an armrest.
    - `+0.125` [justplainclear] colonoscopy: An exam of the inside of the large intestine that uses a flexible tube with a lens at the end
    - `+0.077` [readme] colonoscopy: A procedure to check for colon cancer by examining the inside of the large intestine.

- rationale: The glossary defines colonoscopy as a test that checks the inside of your large intestine for signs of cancer, so the replacement phrase "a test for his large intestine" keeps that specific medical check in plain language. Phrase frequency increases from 2.74 to 3.22, while age of acquisition falls from 15.76 to 9.28. Patients can now understand the purpose of the procedure without needing to know the technical name.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `stools` -> `poop`**

- status: `attributed`
- log p full -0.0546, empty -0.4539
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+2.930` [readme] stools: Poop.
    - `+0.398` [readme] occult: Obscure and mysterious, not easily understood.
    - `+0.191` [readme] Blood: Blood is a vital fluid that carries nutrients and oxygen to our body's tissues through the heart's pump
    - `+0.162` [justplainclear] colonoscopy: An exam of the inside of the large intestine that uses a flexible tube with a lens at the end
    - `+0.053` [wiktionary] occult: If something is occult it is hidden or secret—or it is about hidden or secret things.

- rationale: The original term refers to solid waste from the digestive system, so "poop" conveys that same biological function in a more direct way. Phrase frequency increases from Zipf 3.05 to 3.66, while syllable count remains constant at one. Patients can now recognize the bodily function without needing to recall the formal medical vocabulary.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `occult blood` -> `hidden blood`**

- status: `attributed`
- log p full -0.1423, empty -0.0787
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+0.392` [wiktionary] occult: If something is occult it is hidden or secret—or it is about hidden or secret things.
    - `+0.201` [readme] occult: Obscure and mysterious, not easily understood.
    - `+0.055` [nih] colonoscopy: Examination of the inside of the colon using a colonoscope, inserted into the rectum. A colonosco
    - `+0.023` [readme] stools: Stools are the stuff that comes out when you go to the bathroom.

- rationale: The original term refers to blood that is not visible to the naked eye, so "hidden blood" keeps that core idea in plain language. Phrase frequency increases from 3.28 to 4.43, while age of acquisition drops from 12.65 to 4.89. You can now grasp the concept of unseen blood in a sample without needing specialized medical vocabulary.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

==============================================================================

## Note 78 - `783`

**ORIGINAL**  The knee was copiously irrigated and suction dried once again.

**REFERENCE** The knee was washed out thoroughly and dried with a suction (or mini-vacuum) once again

| | FKGL | FRE | SMOG | Coleman-Liau | words |
|---|---:|---:|---:|---:|---:|
| ORIGINAL | 8.37 | 52.87 | 11.21 | 11.40 | 10 |
| REFERENCE | 7.57 | 67.53 | 11.21 | 9.29 | 16 |

### Stage 2 - extraction + classification

| term | kind | category | action | Zipf | AoA | syll |
|---|---|---|---|---:|---:|---:|
| `copiously irrigated` | phrase | general_hard_word | replace | 1.98 | None | 7 |
| `copiously` | word | medical_descriptor | replace | - | - | - |
| `irrigated` | word | medical_descriptor | replace | - | - | - |
| `suction dried` | phrase | general_hard_word | replace | 3.28 | 9.42 | 3 |
| `suction` | word | medical_descriptor | replace | - | - | - |
| `dried` | word | medical_descriptor | replace | - | - | - |

### Stage 3 - retrieval

coverage **0.0** (0/2), glossary budget 6/16

| term | Zipf stratum | defs | sources | matched via | origin |
|---|---|---:|---|---|---|
| `copiously irrigated` | very_rare | 0 | - | - | extracted |
| `copiously` | very_rare | 1 | dictonary.csv | exact | split_from_uncovered |
| `irrigated` | rare | 1 | wiktionary.json | exact | split_from_uncovered |
| `suction dried` | rare | 0 | - | - | extracted |
| `suction` | rare | 3 | readme_lay_vocab.jsonl, wiktionary.json | exact | split_from_uncovered |
| `dried` | uncommon | 1 | wiktionary.json | exact | split_from_uncovered |

Glossary shown to the model:

1. `[dictionary]` Copiously (adv.): In a copious manner.
2. `[wiktionary]` irrigated: To supply farms with water to grow crops.
3. `[wiktionary]` dried: If something is dry, it has no water or liquid on it.
4. `[readme]` suction: Suction is when a machine pulls in gas, liquid, or mucus.
5. `[wiktionary]` suction: Suction is a force which pushes matter from one space into another due to the pressure difference in pressure between the two spaces
6. `[wiktionary]` suction: A suction is a device that removes saliva from a patient's mouth during dental operations.

### Stage 4 - arm `naive`

**output:** The knee was washed out thoroughly and dried with suction again.

| metric | value |
|---|---:|
| bertscore_f1 | 0.732 |
| coleman_liau | 9.45 |
| coleman_liau_drop | 1.95 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 4.79 |
| fkgl_drop | 3.58 |
| fre | 80.3 |
| fre_gain | 27.4 |
| human_edit_recall | 1.000 |
| length_ratio | 0.69 |
| n_words | 11.0 |
| nli_completeness | 0.953 |
| nli_faithfulness | 0.992 |
| number_unit_preservation | 0.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 72.22 |
| smog | 8.84 |
| smog_drop | 2.37 |

### Stage 4 - arm `termonly`

**output:** The knee was washed with lots of water and dried with a vacuum.

| metric | value |
|---|---:|
| bertscore_f1 | 0.569 |
| coleman_liau | 4.23 |
| coleman_liau_drop | 7.17 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.200 |
| fkgl | 3.10 |
| fkgl_drop | 5.27 |
| fre | 96.0 |
| fre_gain | 43.2 |
| human_edit_recall | 1.000 |
| length_ratio | 0.81 |
| n_words | 13.0 |
| nli_completeness | 0.937 |
| nli_faithfulness | 0.939 |
| number_unit_preservation | 0.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.400 |
| sari | 59.65 |
| smog | 3.13 |
| smog_drop | 8.08 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `copiously irrigated` -> `washed with lots of water` | replace | - | - | - | - | - | - | - |
| `suction dried` -> `dried with a vacuum` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** The knee was washed with lots of water and cleaned with a vacuum.

| metric | value |
|---|---:|
| bertscore_f1 | 0.537 |
| coleman_liau | 5.12 |
| coleman_liau_drop | 6.28 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.333 |
| fkgl | 3.10 |
| fkgl_drop | 5.27 |
| fre | 96.0 |
| fre_gain | 43.2 |
| human_edit_recall | 1.000 |
| length_ratio | 0.81 |
| n_words | 13.0 |
| nli_completeness | 0.785 |
| nli_faithfulness | 0.866 |
| number_unit_preservation | 0.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 54.27 |
| smog | 3.13 |
| smog_drop | 8.08 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `copiously irrigated` -> `washed with lots of water` | replace | attributed | 0.324 | 0.433 | 0.453 | 0.641 | 0.057 | - |
| `suction dried` -> `cleaned with a vacuum` | replace | attributed | -0.197 | -0.200 | 0.475 | 0.786 | 0.134 | - |

**edit `copiously irrigated` -> `washed with lots of water`**

- status: `attributed`
- log p full -1.2248, empty -1.5492
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.123` [wiktionary] irrigated: To supply farms with water to grow crops.
    - `+0.066` [wiktionary] dried: If something is dry, it has no water or liquid on it.
    - `+0.018` [wiktionary] suction: Suction is a force which pushes matter from one space into another due to the pressure difference in 
    - `+0.006` [wiktionary] suction: A suction is a device that removes saliva from a patient's mouth during dental operations.

- rationale: The original phrase describes a surgical area being thoroughly cleaned with fluid, so "washed with lots of water" conveys that same idea using simple, everyday language. Phrase frequency rises from 1.98 to 4.02, while the syllable count drops from 7 to 6. Patients can now clearly visualize the cleaning process without needing to interpret complex medical jargon.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `suction dried` -> `cleaned with a vacuum`**

- status: `attributed`
- log p full -4.0979, empty -3.9013
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.220` [wiktionary] suction: A suction is a device that removes saliva from a patient's mouth during dental operations.
    - `+0.086` [wiktionary] irrigated: To supply farms with water to grow crops.
    - `+0.030` [readme] suction: Suction is when a machine pulls in gas, liquid, or mucus.

- rationale: The original term describes removing moisture using air pressure, so "cleaned with a vacuum" conveys that same action using common household language. Phrase frequency rises from 3.28 to 3.75, while age of acquisition drops from 9.42 to 6.74. This change allows the patient to visualize the process immediately without needing specialized medical vocabulary.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

==============================================================================

## Note 79 - `784`

**ORIGINAL**  She is not having painful urination, any blood in the urine, frequency or hesitancy.

**REFERENCE** She is not having painful peeing, any blood in the pee, needing to pee very often or having difficulty peeing.

| | FKGL | FRE | SMOG | Coleman-Liau | words |
|---|---:|---:|---:|---:|---:|
| ORIGINAL | 10.94 | 41.55 | 13.02 | 10.26 | 14 |
| REFERENCE | 11.09 | 51.18 | 8.84 | 8.24 | 20 |

### Stage 2 - extraction + classification

| term | kind | category | action | Zipf | AoA | syll |
|---|---|---|---|---:|---:|---:|
| `frequency` | word | medical_descriptor | replace | 4.36 | 9.79 | 3 |
| `hesitancy` | word | medical_descriptor | replace | 2.35 | 12.12 | 4 |

### Stage 3 - retrieval

coverage **1.0** (2/2), glossary budget 5/16

| term | Zipf stratum | defs | sources | matched via | origin |
|---|---|---:|---|---|---|
| `frequency` | uncommon | 3 | readme_lay_vocab.jsonl, wiktionary.json | exact | extracted |
| `hesitancy` | very_rare | 2 | readme_lay_vocab.jsonl | exact | extracted |

Glossary shown to the model:

1. `[readme]` hesitancy: Having difficulty starting or maintaining a steady flow while peeing.
2. `[readme]` frequency: How often something happens.
3. `[readme]` hesitancy: Having difficulty starting to pee or keeping the flow steady.
4. `[readme]` FREQUENCY: Frequency is how often something happens.
5. `[wiktionary]` frequency: Something's frequency is how often it happens.

### Stage 4 - arm `naive`

**output:** She does not have painful urination, blood in her urine, or the need to go often or have trouble starting.

| metric | value |
|---|---:|
| bertscore_f1 | 0.672 |
| coleman_liau | 7.08 |
| coleman_liau_drop | 3.18 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 8.14 |
| fkgl_drop | 2.80 |
| fre | 72.3 |
| fre_gain | 30.8 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 20.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.993 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 28.69 |
| smog | 8.84 |
| smog_drop | 4.18 |

### Stage 4 - arm `termonly`

**output:** She is not having painful urination, any blood in the urine, or needing to go often or having trouble starting.

| metric | value |
|---|---:|
| bertscore_f1 | 0.762 |
| coleman_liau | 8.53 |
| coleman_liau_drop | 1.73 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 10.50 |
| fkgl_drop | 0.44 |
| fre | 55.4 |
| fre_gain | 13.8 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 20.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.990 |
| nli_faithfulness | 0.982 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 65.25 |
| smog | 8.84 |
| smog_drop | 4.18 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `frequency` -> `needing to go often` | replace | - | - | - | - | - | - | - |
| `hesitancy` -> `having trouble starting` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** She is not having painful urination, blood in the urine, or peeing too often or with trouble starting.

| metric | value |
|---|---:|
| bertscore_f1 | 0.669 |
| coleman_liau | 8.98 |
| coleman_liau_drop | 1.28 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 9.13 |
| fkgl_drop | 1.81 |
| fre | 61.7 |
| fre_gain | 20.1 |
| human_edit_recall | 1.000 |
| length_ratio | 0.90 |
| n_words | 18.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.992 |
| nli_faithfulness | 0.983 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 54.30 |
| smog | 8.84 |
| smog_drop | 4.18 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `frequency` -> `peeing too often` | replace | attributed | 2.728 | 3.070 | - | 0.919 | 0.657 | - |
| `hesitancy` -> `with trouble starting` | replace | attributed | 0.491 | 0.559 | - | 0.731 | 0.066 | - |

**edit `frequency` -> `peeing too often`**

- status: `attributed`
- log p full -1.1901, empty -3.9180
- masks scored: 34/34 (+2 top-k)
- ranked sources:
    - `+1.530` [readme] hesitancy: Having difficulty starting or maintaining a steady flow while peeing.
    - `+0.873` [readme] hesitancy: Having difficulty starting to pee or keeping the flow steady.
    - `+0.096` [readme] frequency: How often something happens.
    - `+0.086` [wiktionary] frequency: Something's frequency is how often it happens.
    - `+0.018` [readme] FREQUENCY: Frequency is how often something happens.

- rationale: The original term refers to how often a person urinates, so "peeing too often" keeps that core idea in plain language. Frequency (Zipf) increases from 4.36 to 3.24, while age of acquisition falls from 9.79 to 6.53. Patients can now recognize the symptom without needing to know the clinical vocabulary.
- audit: coverage 1.0, grounding_error=True, omission=False, source_ok=True, passage_ok=True

**edit `hesitancy` -> `with trouble starting`**

- status: `attributed`
- log p full -1.8776, empty -2.3687
- masks scored: 34/34 (+2 top-k)
- ranked sources:
    - `+0.349` [readme] hesitancy: Having difficulty starting or maintaining a steady flow while peeing.
    - `+0.284` [readme] hesitancy: Having difficulty starting to pee or keeping the flow steady.
    - `+0.009` [readme] frequency: How often something happens.
    - `-0.099` [readme] FREQUENCY: Frequency is how often something happens.

- rationale: The original term hesitancy describes a delay or difficulty in beginning an action, which the replacement phrase "with trouble starting" captures in plain language. Phrase frequency increases from Zipf 2.35 to 4.60, while age of acquisition drops from 12.12 to 4.56. Patients can now clearly see the struggle to begin without needing to know the specific medical label.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

==============================================================================

## Note 80 - `789`

**ORIGINAL**  Cardiovascular : Chest pain in the retrosternal area, Occasional anginal pain and patient describes it as a sensation of tightness.

**REFERENCE** Heart and blood vessels: Chest pain just behind the breastbone, occasional chest pain when exercising or exerting themselves, which gets better with rest and patient describes it as feeling 'tightness'.

| | FKGL | FRE | SMOG | Coleman-Liau | words |
|---|---:|---:|---:|---:|---:|
| ORIGINAL | 14.80 | 22.80 | 15.90 | 15.92 | 19 |
| REFERENCE | 14.60 | 43.85 | 13.02 | 15.50 | 30 |

### Stage 2 - extraction + classification

| term | kind | category | action | Zipf | AoA | syll |
|---|---|---|---|---:|---:|---:|
| `retrosternal area` | phrase | medical_descriptor | replace | 0.0 | 6.58 | 6 |
| `Cardiovascular` | word | medical_descriptor | replace | 3.68 | 13.32 | 6 |
| `anginal pain` | phrase | medical_descriptor | replace | 1.1 | 4.26 | 3 |
| `pain` | word | medical_descriptor | replace | - | - | - |

### Stage 3 - retrieval

coverage **0.3333** (1/3), glossary budget 9/16

| term | Zipf stratum | defs | sources | matched via | origin |
|---|---|---:|---|---|---|
| `retrosternal area` | very_rare | 0 | - | - | extracted |
| `Cardiovascular` | uncommon | 6 | justplainclear.json, michigan_plmd.json, nih.json, readme_lay_vocab.jsonl, thesarus.json | exact | extracted |
| `anginal pain` | very_rare | 0 | - | - | extracted |
| `pain` | common | 3 | michigan_plmd.json, wiktionary.json | exact | split_from_uncovered |

Glossary shown to the model:

1. `[michigan]` pain: An unplesant feeling, a sign from your nerves that something may be wrong. It ca be sharp or dull, sting, burn, or ache.
2. `[readme]` Cardiovascular: Related to the blood vessels and heart.
3. `[wiktionary]` pain: A strong feeling of hurt or discomfort
4. `[readme]` CARDIOVASCULAR: Having to do with the blood vessels and the heart.
5. `[wiktionary]` pain: to sadden or hurt
6. `[nih]` cardiovascular: Having to do with the heart and blood vessels.
7. `[michigan]` cardiovascular: Having to do with your heart and blood vessels.
8. `[justplainclear]` cardiovascular: About the heart and blood vessels
9. `[thesaurus]` cardiovascular: having to do with the heart and blood vessels

### Stage 4 - arm `naive`

**output:** Cardiovascular: The patient has chest pain in the area behind the breastbone, occasional anginal pain, and describes the sensation as tightness.

| metric | value |
|---|---:|
| bertscore_f1 | 0.483 |
| coleman_liau | 15.93 |
| coleman_liau_drop | -0.02 |
| copy_jargon_rate | 0.667 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 14.51 |
| fkgl_drop | 0.28 |
| fre | 28.4 |
| fre_gain | 5.6 |
| human_edit_recall | 0.333 |
| length_ratio | 0.70 |
| n_words | 21.0 |
| nli_completeness | 0.932 |
| nli_faithfulness | 0.968 |
| replacement_f1 | 0.500 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 37.54 |
| smog | 14.55 |
| smog_drop | 1.35 |

### Stage 4 - arm `termonly`

**output:** The patient has heart pain behind the breastbone, sometimes feeling like tightness.

| metric | value |
|---|---:|
| bertscore_f1 | 0.417 |
| coleman_liau | 15.57 |
| coleman_liau_drop | 0.35 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.333 |
| fkgl | 6.79 |
| fkgl_drop | 8.01 |
| fre | 67.8 |
| fre_gain | 45.0 |
| human_edit_recall | 1.000 |
| length_ratio | 0.40 |
| n_words | 12.0 |
| nli_completeness | 0.936 |
| nli_faithfulness | 0.969 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.375 |
| sari | 33.93 |
| smog | 3.13 |
| smog_drop | 12.77 |

annotation backend `novita`, 0 edits kept


### Stage 4 - arm `grounded`

**output:** The patient has heart and blood vessel pain behind the breastbone, with occasional tightness.

| metric | value |
|---|---:|
| bertscore_f1 | 0.446 |
| coleman_liau | 14.40 |
| coleman_liau_drop | 1.52 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.333 |
| fkgl | 8.41 |
| fkgl_drop | 6.39 |
| fre | 59.7 |
| fre_gain | 36.9 |
| human_edit_recall | 1.000 |
| length_ratio | 0.47 |
| n_words | 14.0 |
| nli_completeness | 0.968 |
| nli_faithfulness | 0.951 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.286 |
| sari | 38.20 |
| smog | 8.84 |
| smog_drop | 7.06 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `Cardiovascular` -> `heart and blood vessel` | replace | attributed | 3.510 | 3.725 | 0.239 | 0.872 | 0.005 | - |
| `retrosternal area` -> `breastbone` | replace | attributed | -0.090 | -0.459 | 0.351 | 0.398 | 0.016 | - |
| `anginal pain` -> `tightness` | replace | attributed | 0.062 | 0.094 | 0.739 | 0.664 | 0.207 | - |

**edit `Cardiovascular` -> `heart and blood vessel`**

- status: `attributed`
- log p full -1.6184, empty -5.1282
- masks scored: 66/66 (+5 top-k)
- ranked sources:
    - `+0.171` [michigan] cardiovascular: Having to do with your heart and blood vessels.
    - `+0.166` [justplainclear] cardiovascular: About the heart and blood vessels

- rationale: The original term refers to the entire system of the heart and blood vessels, so "heart and blood vessel" keeps that full anatomical scope in plain language. Phrase frequency increases from Zipf 3.68 to 4.18, while age of acquisition falls from 13.32 to 9.94. Patients can now understand the specific body systems involved without needing to know the complex medical label.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `retrosternal area` -> `breastbone`**

- status: `attributed`
- log p full -0.2657, empty -0.1759
- masks scored: 66/66 (+5 top-k)
- ranked sources:
    - `+0.016` [justplainclear] cardiovascular: About the heart and blood vessels

- rationale: The original term refers to the region directly behind the breastbone, so "breastbone" captures that central anatomical landmark in plain language. Phrase frequency increases from 0.00 to 1.93, while age of acquisition rises from 6.58 to 10.75. Patients can now identify the specific chest location without needing to visualize a complex directional description.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `anginal pain` -> `tightness`**

- status: `attributed`
- log p full -1.0365, empty -1.0980
- masks scored: 66/66 (+5 top-k)
- ranked sources:
    - `+0.271` [readme] Cardiovascular: Related to the blood vessels and heart.
    - `+0.064` [justplainclear] cardiovascular: About the heart and blood vessels
    - `+0.002` [readme] CARDIOVASCULAR: Having to do with the blood vessels and the heart.

- rationale: The original term refers to chest discomfort that feels like pressure or squeezing, so "tightness" captures that physical sensation in simpler language. Phrase frequency rises from Zipf 1.10 to 2.96, while age of acquisition increases from 4.26 to 8.11. Patients can now describe their chest feeling without needing to recall a specific medical label.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

==============================================================================

## Note 81 - `790`

**ORIGINAL**  We excised a good bit of his synovium and synovial pouch.

**REFERENCE** We cut out a bit of the soft tissue of the joint.

| | FKGL | FRE | SMOG | Coleman-Liau | words |
|---|---:|---:|---:|---:|---:|
| ORIGINAL | 4.79 | 80.31 | 8.84 | 5.76 | 11 |
| REFERENCE | 1.87 | 103.01 | 3.13 | -0.38 | 12 |

### Stage 2 - extraction + classification

| term | kind | category | action | Zipf | AoA | syll |
|---|---|---|---|---:|---:|---:|
| `synovial pouch` | phrase | medical_essential | elaborate | 2.32 | 16.0 | 3 |
| `synovial` | word | medical_descriptor | replace | - | - | - |
| `pouch` | word | medical_descriptor | replace | - | - | - |
| `synovium` | word | medical_essential | elaborate | 1.46 | None | 3 |
| `excised` | word | general_hard_word | replace | 2.58 | None | 2 |

### Stage 3 - retrieval

coverage **0.6667** (2/3), glossary budget 6/16

| term | Zipf stratum | defs | sources | matched via | origin |
|---|---|---:|---|---|---|
| `synovial pouch` | very_rare | 0 | - | - | extracted |
| `synovial` | very_rare | 2 | readme_lay_vocab.jsonl | exact | split_from_uncovered |
| `pouch` | rare | 2 | wiktionary.json | exact | split_from_uncovered |
| `synovium` | very_rare | 1 | readme_lay_vocab.jsonl | exact | extracted |
| `excised` | rare | 1 | wiktionary.json | exact | extracted |

Glossary shown to the model:

1. `[readme]` SYNOVIUM: The slimy layer that covers your joints.
2. `[wiktionary]` excised: Excise it the tax that is charged on goods produced within the country.
3. `[readme]` SYNOVIAL: Synovial means having to do with the soft tissue that lines joints.
4. `[wiktionary]` pouch: A pouch is a small bag or pocket used for carrying things.
5. `[readme]` Synovial: Relating to the soft tissue that lines joints.
6. `[wiktionary]` pouch: A pouch is a pocket-like part of an animal's body, used to carry young or store food.

### Stage 4 - arm `naive`

**output:** We removed a large part of his synovium and synovial pouch.

| metric | value |
|---|---:|
| bertscore_f1 | 0.378 |
| coleman_liau | 6.82 |
| coleman_liau_drop | -1.05 |
| copy_jargon_rate | 0.800 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 4.79 |
| fkgl_drop | 0.00 |
| fre | 80.3 |
| fre_gain | 0.0 |
| human_edit_recall | 0.200 |
| length_ratio | 0.92 |
| n_words | 11.0 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.994 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 33.06 |
| smog | 8.84 |
| smog_drop | 0.00 |

### Stage 4 - arm `termonly`

**output:** We removed a good bit of his joint lining and the bag inside the joint.

| metric | value |
|---|---:|
| bertscore_f1 | 0.549 |
| coleman_liau | 3.88 |
| coleman_liau_drop | 1.88 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.200 |
| fkgl | 4.42 |
| fkgl_drop | 0.37 |
| fre | 90.1 |
| fre_gain | 9.8 |
| human_edit_recall | 1.000 |
| length_ratio | 1.25 |
| n_words | 15.0 |
| nli_completeness | 0.794 |
| nli_faithfulness | 0.967 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 46.38 |
| smog | 3.13 |
| smog_drop | 5.71 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `synovium` -> `joint lining` | replace | - | - | - | - | - | - | - |
| `synovial pouch` -> `the bag inside the joint` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** We removed a good bit of the joint lining and the small pocket inside it.

| metric | value |
|---|---:|
| bertscore_f1 | 0.563 |
| coleman_liau | 4.65 |
| coleman_liau_drop | 1.11 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.200 |
| fkgl | 5.21 |
| fkgl_drop | -0.42 |
| fre | 84.5 |
| fre_gain | 4.1 |
| human_edit_recall | 1.000 |
| length_ratio | 1.25 |
| n_words | 15.0 |
| nli_completeness | 0.658 |
| nli_faithfulness | 0.545 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 49.80 |
| smog | 3.13 |
| smog_drop | 5.71 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `synovium` -> `the joint lining` | replace | attributed | 2.050 | 2.371 | 0.560 | 0.581 | 0.226 | - |
| `synovial pouch` -> `the small pocket inside it` | replace | attributed | 1.965 | 1.970 | 0.747 | 0.759 | 0.447 | - |

**edit `synovium` -> `the joint lining`**

- status: `attributed`
- log p full -1.1956, empty -3.2460
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.873` [readme] SYNOVIUM: The slimy layer that covers your joints.
    - `+0.647` [readme] Synovial: Relating to the soft tissue that lines joints.
    - `+0.360` [readme] SYNOVIAL: Synovial means having to do with the soft tissue that lines joints.
    - `+0.106` [wiktionary] excised: Excise it the tax that is charged on goods produced within the country.

- rationale: The glossary defines synovium as the slimy layer that covers your joints, so "the joint lining" keeps that protective covering in plain words. Phrase frequency increases from 1.46 to 3.82, while age of acquisition falls from 14.6 to 9.2. Patients can now visualize the specific tissue protecting their joints without needing to know the medical name.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `synovial pouch` -> `the small pocket inside it`**

- status: `attributed`
- log p full -5.1436, empty -7.1084
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.985` [wiktionary] pouch: A pouch is a small bag or pocket used for carrying things.
    - `+0.538` [wiktionary] pouch: A pouch is a pocket-like part of an animal's body, used to carry young or store food.
    - `+0.201` [readme] SYNOVIAL: Synovial means having to do with the soft tissue that lines joints.
    - `-0.055` [wiktionary] excised: Excise it the tax that is charged on goods produced within the country.

- rationale: The source defines a synovial pouch as a small bag or pocket used for carrying things, so "the small pocket inside it" keeps that core image in plain language. Phrase frequency increases from Zipf 2.32 to 4.37, while age of acquisition falls from 16.00 to 4.77. Patients can now visualize the joint's internal structure without needing to know the specific anatomical name.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

==============================================================================

## Note 82 - `801`

**ORIGINAL**  An inflammatory process such as infection or ischemia must be considered.

**REFERENCE** An inflammatory process such as infection or reduced blood flow must be considered.

| | FKGL | FRE | SMOG | Coleman-Liau | words |
|---|---:|---:|---:|---:|---:|
| ORIGINAL | 13.37 | 18.78 | 14.55 | 14.20 | 11 |
| REFERENCE | 10.36 | 43.96 | 13.02 | 13.15 | 13 |

### Stage 2 - extraction + classification

| term | kind | category | action | Zipf | AoA | syll |
|---|---|---|---|---:|---:|---:|
| `inflammatory process` | phrase | medical_descriptor | replace | 3.71 | 13.33 | 7 |
| `ischemia` | word | medical_essential | elaborate | 2.85 | 18.0 | 4 |

### Stage 3 - retrieval

coverage **1.0** (2/2), glossary budget 6/16

| term | Zipf stratum | defs | sources | matched via | origin |
|---|---|---:|---|---|---|
| `inflammatory process` | uncommon | 1 | readme_lay_vocab.jsonl | exact | extracted |
| `ischemia` | rare | 5 | iowa.json, michigan_plmd.json, nih.json, readme_lay_vocab.jsonl | exact | extracted |

Glossary shown to the model:

1. `[readme]` inflammatory process: When your body gets inflamed, it's like it's telling you there's something wrong by showing redness, warmth, and swelling because of an infection.
2. `[readme]` ischemia: Not enough blood flow due to blocked or narrowed blood vessels.
3. `[readme]` Ischemia: Ischemia is when there's a lack of blood flow due to blocked blood vessels.
4. `[nih]` ischemia: Lack of blood supply to a part of the body. Ischemia may cause tissue damage due to the lack of oxygen and nutrients.
5. `[iowa]` ISCHEMIA: decreased oxygen in a tissue (usually because of decreased blood flow)
6. `[michigan]` ischemia: When blood supply to an organ or a body part isn't enough, especially the heart.

### Stage 4 - arm `naive`

**output:** An inflammatory process, like an infection or a lack of blood flow, must be considered.

| metric | value |
|---|---:|
| bertscore_f1 | 0.843 |
| coleman_liau | 9.29 |
| coleman_liau_drop | 4.91 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| diagnostic_identity_preservation | 1.000 |
| fkgl | 9.14 |
| fkgl_drop | 4.23 |
| fre | 56.3 |
| fre_gain | 37.5 |
| human_edit_recall | 1.000 |
| length_ratio | 1.15 |
| n_words | 15.0 |
| nli_completeness | 0.894 |
| nli_faithfulness | 0.990 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 42.04 |
| smog | 13.02 |
| smog_drop | 1.53 |

### Stage 4 - arm `termonly`

**output:** A flare-up from infection or lack of blood flow must be considered.

| metric | value |
|---|---:|
| bertscore_f1 | 0.640 |
| coleman_liau | 7.83 |
| coleman_liau_drop | 6.37 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| diagnostic_identity_preservation | 1.000 |
| fkgl | 5.81 |
| fkgl_drop | 7.57 |
| fre | 74.8 |
| fre_gain | 56.0 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 13.0 |
| nli_completeness | 0.970 |
| nli_faithfulness | 0.972 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.250 |
| sari | 33.44 |
| smog | 11.21 |
| smog_drop | 3.35 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `inflammatory process` -> `flare-up` | replace | - | - | - | - | - | - | - |
| `ischemia` -> `lack of blood flow` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** An infection or lack of blood flow must be considered.

| metric | value |
|---|---:|
| bertscore_f1 | 0.705 |
| coleman_liau | 6.76 |
| coleman_liau_drop | 7.44 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| diagnostic_identity_preservation | 1.000 |
| fkgl | 4.83 |
| fkgl_drop | 8.54 |
| fre | 78.2 |
| fre_gain | 59.5 |
| human_edit_recall | 1.000 |
| length_ratio | 0.77 |
| n_words | 10.0 |
| nli_completeness | 0.872 |
| nli_faithfulness | 0.983 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.250 |
| sari | 37.95 |
| smog | 11.21 |
| smog_drop | 3.35 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `inflammatory process` -> `infection` | replace | attributed | 0.006 | 0.065 | 0.540 | 0.755 | 0.070 | - |
| `ischemia` -> `lack of blood flow` | replace | attributed | -0.107 | -0.155 | 0.681 | 0.851 | 0.102 | - |

**edit `inflammatory process` -> `infection`**

- status: `attributed`
- log p full -0.1021, empty -0.1086
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.125` [readme] inflammatory process: When your body gets inflamed, it's like it's telling you there's something wrong by show
    - `+0.054` [iowa] ISCHEMIA: decreased oxygen in a tissue (usually because of decreased blood flow)
    - `-0.071` [readme] Ischemia: Ischemia is when there's a lack of blood flow due to blocked blood vessels.
    - `-0.118` [michigan] ischemia: When blood supply to an organ or a body part isn't enough, especially the heart.
    - `-0.131` [readme] ischemia: Not enough blood flow due to blocked or narrowed blood vessels.

- rationale: The original term refers to a condition where the body's tissues become swollen and irritated, so "infection" captures that state of illness in simpler language. Phrase frequency rises from Zipf 3.71 to 4.33, while age of acquisition drops from 13.33 to 8.05. Patients can now recognize the cause of their symptoms without needing to understand complex medical descriptions.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `ischemia` -> `lack of blood flow`**

- status: `attributed`
- log p full -1.2196, empty -1.1131
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.515` [readme] ischemia: Not enough blood flow due to blocked or narrowed blood vessels.
    - `+0.413` [readme] Ischemia: Ischemia is when there's a lack of blood flow due to blocked blood vessels.
    - `+0.057` [nih] ischemia: Lack of blood supply to a part of the body. Ischemia may cause tissue damage due to the lack of oxyg
    - `+0.015` [readme] inflammatory process: When your body gets inflamed, it's like it's telling you there's something wrong by show
    - `-0.004` [iowa] ISCHEMIA: decreased oxygen in a tissue (usually because of decreased blood flow)

- rationale: The original term refers to a condition where tissues do not receive enough oxygenated blood, so "lack of blood flow" conveys this physiological blockage in plain language. Phrase frequency increases from Zipf 2.85 to 4.39, while age of acquisition falls from 18.00 to 8.28. Patients can now grasp the immediate cause of tissue damage without needing specialized medical vocabulary.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

==============================================================================

## Note 83 - `804`

**ORIGINAL**  I have asked her to increase her prednisone when she goes home.

**REFERENCE** I have asked her to increase her steroid when she goes home.

| | FKGL | FRE | SMOG | Coleman-Liau | words |
|---|---:|---:|---:|---:|---:|
| ORIGINAL | 2.86 | 95.95 | 3.13 | 6.38 | 12 |
| REFERENCE | 2.86 | 95.95 | 3.13 | 4.93 | 12 |

### Stage 2 - extraction + classification

| term | kind | category | action | Zipf | AoA | syll |
|---|---|---|---|---:|---:|---:|
| `prednisone` | word | medical_essential | elaborate | 2.56 | 17.17 | 2 |

### Stage 3 - retrieval

coverage **1.0** (1/1), glossary budget 3/16

| term | Zipf stratum | defs | sources | matched via | origin |
|---|---|---:|---|---|---|
| `prednisone` | rare | 3 | nih.json, readme_lay_vocab.jsonl | exact | extracted |

Glossary shown to the model:

1. `[readme]` Prednisone: A medication that lowers the body's immune response and inflammation.
2. `[readme]` prednisone: A medication that helps lower the body's immune system reactions.
3. `[nih]` prednisone: A drug used to reduce inflammation and lower the body’s immune response.  It is used with other drugs to treat leukemia, lymphoma, and mycosis fungoides (a type of skin lymphoma).    It is also used alone or with other drugs to prevent or treat many other conditions.  These include conditions related to cancer and its treatment, such as anemia (a low level of red blood cells) and allergic reactions. Prednisone is a type of therapeutic glucocorticoid.

### Stage 4 - arm `naive`

**output:** I have asked her to take more prednisone when she goes home.

| metric | value |
|---|---:|
| bertscore_f1 | 0.790 |
| coleman_liau | 4.93 |
| coleman_liau_drop | 1.45 |
| copy_jargon_rate | 1.000 |
| critical_error | 0.000 |
| drug_preservation | 1.000 |
| fkgl | 1.87 |
| fkgl_drop | 0.98 |
| fre | 103.0 |
| fre_gain | 7.0 |
| human_edit_recall | 0.000 |
| length_ratio | 1.00 |
| n_words | 12.0 |
| nli_completeness | 0.992 |
| nli_faithfulness | 0.994 |
| replacement_f1 | 0.000 |
| rewrite_aggressiveness | 1.000 |
| sari | 38.27 |
| smog | 3.13 |
| smog_drop | 0.00 |

### Stage 4 - arm `termonly`

**output:** I have asked her to increase her steroid medicine when she goes home.

| metric | value |
|---|---:|
| bertscore_f1 | 0.943 |
| coleman_liau | 6.91 |
| coleman_liau_drop | -0.52 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| drug_preservation | 0.000 |
| fkgl | 4.91 |
| fkgl_drop | -2.05 |
| fre | 83.0 |
| fre_gain | -12.9 |
| human_edit_recall | 1.000 |
| length_ratio | 1.08 |
| n_words | 13.0 |
| nli_completeness | 0.085 |
| nli_faithfulness | 0.020 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 79.79 |
| smog | 8.84 |
| smog_drop | -5.71 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `prednisone` -> `steroid medicine` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** I have asked her to increase the medicine she takes when she goes home.

| metric | value |
|---|---:|
| bertscore_f1 | 0.839 |
| coleman_liau | 5.70 |
| coleman_liau_drop | 0.68 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| drug_preservation | 0.000 |
| fkgl | 4.20 |
| fkgl_drop | -1.34 |
| fre | 89.9 |
| fre_gain | -6.1 |
| human_edit_recall | 1.000 |
| length_ratio | 1.17 |
| n_words | 14.0 |
| nli_completeness | 0.001 |
| nli_faithfulness | 0.970 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 58.08 |
| smog | 8.84 |
| smog_drop | -5.71 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `prednisone` -> `the medicine she takes` | replace | attributed | 0.321 | 0.330 | - | 0.781 | 0.076 | - |

**edit `prednisone` -> `the medicine she takes`**

- status: `attributed`
- log p full -3.5002, empty -3.8217
- masks scored: 10/10 (+2 top-k)
- ranked sources:
    - `+0.155` [readme] prednisone: A medication that helps lower the body's immune system reactions.
    - `+0.079` [nih] prednisone: A drug used to reduce inflammation and lower the body’s immune response.  It is used with other dr

- rationale: Prednisone is a specific type of steroid medication used to reduce inflammation, so "the medicine she takes" keeps that general idea in plain language. Phrase frequency increases from Zipf 2.56 to 4.59, while age of acquisition falls from 17.17 to 4.89. Patients can understand the treatment without needing to know the specific drug name.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

==============================================================================

## Note 84 - `844`

**ORIGINAL**  She may need other neuropathic pain medications as needed.

**REFERENCE** She may need other nerve pain medications as needed.

| | FKGL | FRE | SMOG | Coleman-Liau | words |
|---|---:|---:|---:|---:|---:|
| ORIGINAL | 10.21 | 37.90 | 11.21 | 12.49 | 9 |
| REFERENCE | 6.28 | 66.10 | 8.84 | 8.62 | 9 |

### Stage 2 - extraction + classification

| term | kind | category | action | Zipf | AoA | syll |
|---|---|---|---|---:|---:|---:|
| `neuropathic` | word | medical_descriptor | replace | 2.35 | 15.4 | 4 |

### Stage 3 - retrieval

coverage **1.0** (1/1), glossary budget 2/16

| term | Zipf stratum | defs | sources | matched via | origin |
|---|---|---:|---|---|---|
| `neuropathic` | very_rare | 2 | readme_lay_vocab.jsonl | exact | extracted |

Glossary shown to the model:

1. `[readme]` neuropathic: Nerve pain.
2. `[readme]` Neuropathic: Neuropathic means nerve pain.

### Stage 4 - arm `naive`

**output:** She might need other medicines for nerve pain if she feels like it.

| metric | value |
|---|---:|
| bertscore_f1 | 0.660 |
| coleman_liau | 6.02 |
| coleman_liau_drop | 6.47 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 4.00 |
| fkgl_drop | 6.21 |
| fre | 89.5 |
| fre_gain | 51.6 |
| human_edit_recall | 1.000 |
| length_ratio | 1.44 |
| n_words | 13.0 |
| nli_completeness | 0.885 |
| nli_faithfulness | 0.900 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.750 |
| sari | 24.25 |
| smog | 8.84 |
| smog_drop | 2.37 |
| uncertainty_preservation | 1.000 |

### Stage 4 - arm `termonly`

**output:** She may need other nerve pain medicines as needed.

| metric | value |
|---|---:|
| bertscore_f1 | 0.978 |
| coleman_liau | 7.33 |
| coleman_liau_drop | 5.16 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 4.96 |
| fkgl_drop | 5.24 |
| fre | 75.5 |
| fre_gain | 37.6 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 9.0 |
| nli_completeness | 0.873 |
| nli_faithfulness | 0.955 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 64.54 |
| smog | 8.84 |
| smog_drop | 2.37 |
| uncertainty_preservation | 1.000 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `neuropathic` -> `nerve pain` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** She may need other nerve pain medicines as needed.

| metric | value |
|---|---:|
| bertscore_f1 | 0.978 |
| coleman_liau | 7.33 |
| coleman_liau_drop | 5.16 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 4.96 |
| fkgl_drop | 5.24 |
| fre | 75.5 |
| fre_gain | 37.6 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 9.0 |
| nli_completeness | 0.873 |
| nli_faithfulness | 0.955 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 64.54 |
| smog | 8.84 |
| smog_drop | 2.37 |
| uncertainty_preservation | 1.000 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `neuropathic` -> `nerve pain` | replace | attributed | 1.557 | 2.495 | - | 1.000 | 0.007 | - |

**edit `neuropathic` -> `nerve pain`**

- status: `attributed`
- log p full -0.4105, empty -1.9677
- masks scored: 6/6 (+1 top-k)
- ranked sources:
    - `+1.174` [readme] neuropathic: Nerve pain.
    - `+1.167` [readme] Neuropathic: Neuropathic means nerve pain.

- rationale: The original term refers to pain caused by damage to the nerves, so "nerve pain" conveys that specific physical sensation in plain words. Phrase frequency rises from Zipf 2.35 to 4.13, while age of acquisition drops from 15.40 to 9.67. Patients can now identify the exact source of their discomfort without needing specialized medical vocabulary.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

==============================================================================

## Note 85 - `852`

**ORIGINAL**  A prophylactic dose of antibiotics was given.

**REFERENCE** A prevention dose of antibiotics was given.

| | FKGL | FRE | SMOG | Coleman-Liau | words |
|---|---:|---:|---:|---:|---:|
| ORIGINAL | 12.43 | 18.44 | 11.21 | 11.46 | 7 |
| REFERENCE | 10.74 | 30.53 | 11.21 | 9.80 | 7 |

### Stage 2 - extraction + classification

| term | kind | category | action | Zipf | AoA | syll |
|---|---|---|---|---:|---:|---:|
| `prophylactic` | word | general_hard_word | replace | 2.59 | 15.2 | 4 |
| `antibiotics` | word | medical_essential | elaborate | 3.74 | 9.55 | 5 |

### Stage 3 - retrieval

coverage **1.0** (2/2), glossary budget 8/16

| term | Zipf stratum | defs | sources | matched via | origin |
|---|---|---:|---|---|---|
| `prophylactic` | rare | 6 | justplainclear.json, nih.json, readme_lay_vocab.jsonl, wiktionary.json | exact | extracted |
| `antibiotics` | uncommon | 2 | readme_lay_vocab.jsonl, wiktionary.json | exact | extracted |

Glossary shown to the model:

1. `[readme]` Antibiotics: Medicine that kills bacteria.
2. `[readme]` prophylactic: A prophylactic is like a protective shield that helps prevent diseases.
3. `[wiktionary]` antibiotics: An antibiotic is a drug that stops the growth of or destroys bacteria and other such microorganisms.
4. `[readme]` PROPHYLACTIC: Preventive measures or treatments to avoid getting sick.
5. `[nih]` prophylactic: In medicine, something that prevents or protects.
6. `[justplainclear]` prophylactic: Drugs given to prevent sickness or pregnancy, birth control, condom
7. `[wiktionary]` prophylactic: A prophylactic is a medicine which preserves or defends against disease.
8. `[wiktionary]` prophylactic: Something that is prophylactic serves to prevent or protect against a disease or pregnancy.

### Stage 4 - arm `naive`

**output:** A small dose of antibiotics was given to prevent infection.

| metric | value |
|---|---:|
| bertscore_f1 | 0.658 |
| coleman_liau | 9.66 |
| coleman_liau_drop | 1.80 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 9.55 |
| fkgl_drop | 2.88 |
| fre | 44.4 |
| fre_gain | 26.0 |
| human_edit_recall | 1.000 |
| length_ratio | 1.43 |
| n_words | 10.0 |
| nli_completeness | 0.977 |
| nli_faithfulness | 0.952 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 66.67 |
| smog | 11.21 |
| smog_drop | 0.00 |

### Stage 4 - arm `termonly`

**output:** A small dose of medicine to prevent infection was given.

| metric | value |
|---|---:|
| bertscore_f1 | 0.568 |
| coleman_liau | 7.92 |
| coleman_liau_drop | 3.54 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 7.19 |
| fkgl_drop | 5.24 |
| fre | 61.3 |
| fre_gain | 42.9 |
| human_edit_recall | 1.000 |
| length_ratio | 1.43 |
| n_words | 10.0 |
| nli_completeness | 0.218 |
| nli_faithfulness | 0.977 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 28.96 |
| smog | 11.21 |
| smog_drop | 0.00 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `prophylactic` -> `small` | replace | - | - | - | - | - | - | - |
| `antibiotics` -> `medicine to prevent infection` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** A preventive dose of medicine to stop bacteria was given.

| metric | value |
|---|---:|
| bertscore_f1 | 0.722 |
| coleman_liau | 8.50 |
| coleman_liau_drop | 2.96 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 9.55 |
| fkgl_drop | 2.88 |
| fre | 44.4 |
| fre_gain | 26.0 |
| human_edit_recall | 1.000 |
| length_ratio | 1.43 |
| n_words | 10.0 |
| nli_completeness | 0.877 |
| nli_faithfulness | 0.973 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 28.96 |
| smog | 13.02 |
| smog_drop | -1.82 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `prophylactic` -> `preventive` | replace | attributed | 0.056 | 0.083 | 0.869 | 0.950 | 1.237 | - |
| `antibiotics` -> `medicine to stop bacteria` | replace | attributed | 3.554 | 3.657 | 0.800 | 0.834 | 1.034 | - |

**edit `prophylactic` -> `preventive`**

- status: `attributed`
- log p full -1.0926, empty -1.1487
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+1.329` [readme] PROPHYLACTIC: Preventive measures or treatments to avoid getting sick.
    - `+0.092` [wiktionary] antibiotics: An antibiotic is a drug that stops the growth of or destroys bacteria and other such microorganis

- rationale: The original term refers to measures taken to prevent a condition before it occurs, so "preventive" conveys this forward-looking protection in simpler language. Phrase frequency rises from 2.59 to 3.50, and age of acquisition drops from 15.20 to 10.50. Patients can now grasp the concept of early protection without needing to know the specific medical jargon.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `antibiotics` -> `medicine to stop bacteria`**

- status: `attributed`
- log p full -2.2986, empty -5.8530
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+2.615` [wiktionary] antibiotics: An antibiotic is a drug that stops the growth of or destroys bacteria and other such microorganis
    - `+1.581` [readme] Antibiotics: Medicine that kills bacteria.
    - `+0.468` [wiktionary] prophylactic: Something that is prophylactic serves to prevent or protect against a disease or pregnancy.
    - `+0.238` [nih] prophylactic: In medicine, something that prevents or protects.
    - `+0.039` [wiktionary] prophylactic: A prophylactic is a medicine which preserves or defends against disease.

- rationale: The glossary defines antibiotics as drugs that stop the growth of or destroy bacteria, so "medicine to stop bacteria" keeps that core function in plain words. Phrase frequency increases from 3.74 to 4.06, while age of acquisition decreases from 9.55 to 9.28. Patients can now understand the specific type of medicine needed to fight infection without needing to know the technical name.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

==============================================================================

## Note 86 - `854`

**ORIGINAL**  Chronic hypokalemia secondary to chronic diarrhea.

**REFERENCE** Long term low potassium due to long term diarrhea.

| | FKGL | FRE | SMOG | Coleman-Liau | words |
|---|---:|---:|---:|---:|---:|
| ORIGINAL | 16.25 | -10.75 | 11.21 | 21.80 | 6 |
| REFERENCE | 7.59 | 56.70 | 11.21 | 7.33 | 9 |

### Stage 2 - extraction + classification

| term | kind | category | action | Zipf | AoA | syll |
|---|---|---|---|---:|---:|---:|
| `Chronic hypokalemia` | phrase | medical_essential | elaborate | 1.76 | 11.25 | 4 |
| `Chronic` | word | medical_descriptor | replace | - | - | - |
| `hypokalemia` | word | medical_essential | elaborate | - | - | - |
| `chronic diarrhea` | phrase | medical_descriptor | replace | 3.46 | 11.25 | 6 |
| `chronic` | word | medical_descriptor | replace | - | - | - |
| `diarrhea` | word | medical_essential | elaborate | - | - | - |
| `secondary to` | phrase | general_hard_word | replace | 4.53 | 9.11 | 5 |
| `secondary` | word | medical_descriptor | replace | - | - | - |
| `to` | word | medical_descriptor | replace | - | - | - |

### Stage 3 - retrieval

coverage **0.0** (0/3), glossary budget 16/16

| term | Zipf stratum | defs | sources | matched via | origin |
|---|---|---:|---|---|---|
| `Chronic hypokalemia` | very_rare | 0 | - | - | extracted |
| `Chronic` | uncommon | 9 | iowa.json, justplainclear.json, michigan_plmd.json, readme_lay_vocab.jsonl, thesarus.json, wiktionary.json | exact | split_from_uncovered |
| `hypokalemia` | very_rare | 4 | iowa.json, justplainclear.json, readme_lay_vocab.jsonl | exact | split_from_uncovered |
| `chronic diarrhea` | uncommon | 0 | - | - | extracted |
| `chronic` | uncommon | 9 | iowa.json, justplainclear.json, michigan_plmd.json, readme_lay_vocab.jsonl, thesarus.json, wiktionary.json | exact | split_from_uncovered |
| `diarrhea` | uncommon | 6 | justplainclear.json, michigan_plmd.json, nih.json, readme_lay_vocab.jsonl, wiktionary.json | exact | split_from_uncovered |
| `secondary to` | common | 0 | - | - | extracted |
| `secondary` | common | 2 | wiktionary.json | exact | split_from_uncovered |
| `to` | common | 2 | wiktionary.json | exact | split_from_uncovered |

Glossary shown to the model:

1. `[wiktionary]` secondary: second, next in order to the first or primary.
2. `[wiktionary]` to: To has no meaning. It is used with a bare infinitival clause.
3. `[readme]` hypokalemia: Not enough potassium in your blood causing muscle cramps, weakness, heart issues, or kidney problems.
4. `[readme]` diarrhea: Having loose, watery poop with cramps and bloating.
5. `[readme]` Chronic: A long-lasting or recurring health issue.
6. `[readme]` Chronic: A long-lasting or recurring health issue.
7. `[wiktionary]` secondary: of less than primary importance.
8. `[wiktionary]` to: To shows where something goes, the goal of movement.
9. `[readme]` Hypokalemia: Low potassium level in your blood that can lead to muscle cramps, weakness, heart rhythm issues, and kidney complications.
10. `[readme]` Diarrhea: Having runny poop with stomach pains and bloating.
11. `[readme]` chronic: An ongoing or frequently recurring health issue.
12. `[readme]` chronic: An ongoing or frequently recurring health issue.
13. `[iowa]` HYPOKALEMIA: low blood potassium level
14. `[nih]` diarrhea: Frequent and watery bowel movements.
15. `[iowa]` CHRONIC: continuing for a long time, ongoing
16. `[iowa]` CHRONIC: continuing for a long time, ongoing

### Stage 4 - arm `naive`

**output:** The patient has had low potassium levels for a long time because of long-term diarrhea.

| metric | value |
|---|---:|
| bertscore_f1 | 0.605 |
| coleman_liau | 9.68 |
| coleman_liau_drop | 12.12 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.286 |
| fkgl | 9.93 |
| fkgl_drop | 6.32 |
| fre | 50.6 |
| fre_gain | 61.4 |
| human_edit_recall | 1.000 |
| length_ratio | 1.78 |
| n_words | 16.0 |
| nli_completeness | 0.916 |
| nli_faithfulness | 0.946 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 43.80 |
| smog | 11.21 |
| smog_drop | 0.00 |
| temporality_preservation | 0.000 |

### Stage 4 - arm `termonly`

**output:** The patient had a long-term low potassium level caused by long-term diarrhea.

| metric | value |
|---|---:|
| bertscore_f1 | 0.646 |
| coleman_liau | 12.18 |
| coleman_liau_drop | 9.62 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.143 |
| fkgl | 10.72 |
| fkgl_drop | 5.53 |
| fre | 39.6 |
| fre_gain | 50.3 |
| human_edit_recall | 1.000 |
| length_ratio | 1.56 |
| n_words | 14.0 |
| nli_completeness | 0.934 |
| nli_faithfulness | 0.967 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 48.51 |
| smog | 11.21 |
| smog_drop | 0.00 |
| temporality_preservation | 0.000 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `Chronic hypokalemia` -> `long-term low potassium level` | replace | - | - | - | - | - | - | - |
| `chronic diarrhea` -> `long-term diarrhea` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** The patient had low blood potassium for a long time because of ongoing loose stools.

| metric | value |
|---|---:|
| bertscore_f1 | 0.450 |
| coleman_liau | 8.91 |
| coleman_liau_drop | 12.89 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.375 |
| fkgl | 7.57 |
| fkgl_drop | 8.68 |
| fre | 67.5 |
| fre_gain | 78.3 |
| human_edit_recall | 1.000 |
| length_ratio | 1.67 |
| n_words | 15.0 |
| nli_completeness | 0.826 |
| nli_faithfulness | 0.827 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 33.06 |
| smog | 11.21 |
| smog_drop | 0.00 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `Chronic hypokalemia` -> `low blood potassium for a long time` | replace | attributed | 2.578 | 2.823 | 0.919 | 0.819 | 0.766 | - |
| `chronic diarrhea` -> `ongoing loose stools` | replace | attributed | 2.603 | 2.693 | 0.682 | 0.851 | 0.753 | - |

**edit `Chronic hypokalemia` -> `low blood potassium for a long time`**

- status: `attributed`
- log p full -1.4637, empty -4.0415
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+1.123` [iowa] HYPOKALEMIA: low blood potassium level
    - `+0.357` [readme] Hypokalemia: Low potassium level in your blood that can lead to muscle cramps, weakness, heart rhythm issues, 
    - `+0.090` [wiktionary] secondary: second, next in order to the first or primary.
    - `+0.015` [readme] Chronic: A long-lasting or recurring health issue.

- rationale: The glossary defines the condition as a low blood potassium level, so the replacement phrase "low blood potassium for a long time" keeps that core meaning while adding the necessary duration. Phrase frequency increases from 1.76 to 3.56, while age of acquisition rises slightly from 11.25 to 11.89. Patients can now grasp the specific electrolyte imbalance and its persistent nature without needing to know the medical term.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `chronic diarrhea` -> `ongoing loose stools`**

- status: `attributed`
- log p full -2.3867, empty -4.9897
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+1.413` [readme] diarrhea: Having loose, watery poop with cramps and bloating.
    - `+0.660` [iowa] CHRONIC: continuing for a long time, ongoing
    - `+0.648` [readme] chronic: An ongoing or frequently recurring health issue.
    - `+0.591` [iowa] CHRONIC: continuing for a long time, ongoing
    - `+0.549` [readme] Hypokalemia: Low potassium level in your blood that can lead to muscle cramps, weakness, heart rhythm issues, 

- rationale: The glossary defines chronic diarrhea as having loose, watery poop with cramps and bloating, so "ongoing loose stools" keeps that core symptom in plain language. Phrase frequency increases from 3.46 to 3.01, while age of acquisition falls from 11.25 to 8.39. You can now understand the digestive issue without needing to know the medical term.
- audit: coverage 1.0, grounding_error=True, omission=False, source_ok=True, passage_ok=True

==============================================================================

## Note 87 - `859`

**ORIGINAL**  No hepatosplenomegaly or tenderness.

**REFERENCE** No enlarged liver or spleen or pain when pushed.

| | FKGL | FRE | SMOG | Coleman-Liau | words |
|---|---:|---:|---:|---:|---:|
| ORIGINAL | 6.62 | 54.73 | 8.84 | 23.20 | 4 |
| REFERENCE | 2.34 | 94.30 | 3.13 | 6.04 | 9 |

### Stage 2 - extraction + classification

| term | kind | category | action | Zipf | AoA | syll |
|---|---|---|---|---:|---:|---:|
| `hepatosplenomegaly` | word | medical_descriptor | replace | 1.12 | None | 2 |
| `tenderness` | word | medical_descriptor | replace | 3.24 | 8.79 | 3 |

### Stage 3 - retrieval

coverage **0.5** (1/2), glossary budget 4/16

| term | Zipf stratum | defs | sources | matched via | origin |
|---|---|---:|---|---|---|
| `hepatosplenomegaly` | very_rare | 0 | - | - | extracted |
| `tenderness` | rare | 4 | readme_lay_vocab.jsonl, wiktionary.json | exact | extracted |

Glossary shown to the model:

1. `[readme]` tenderness: Tenderness is when an area hurts when you touch it.
2. `[readme]` Tenderness: Tenderness is when an area hurts or is sensitive to touch.
3. `[wiktionary]` tenderness: Tenderness is a tendency to show concern or kindness towards others.
4. `[wiktionary]` tenderness: Tenderness is the pain or discomfort when an affected area is touched.

### Stage 4 - arm `naive`

**output:** There was no swelling or pain in the liver or spleen.

| metric | value |
|---|---:|
| bertscore_f1 | 0.482 |
| coleman_liau | 3.65 |
| coleman_liau_drop | 19.55 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 2.65 |
| fkgl_drop | 3.97 |
| fre | 95.7 |
| fre_gain | 41.0 |
| human_edit_recall | 1.000 |
| length_ratio | 1.22 |
| n_words | 11.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.962 |
| nli_faithfulness | 0.818 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 49.06 |
| smog | 3.13 |
| smog_drop | 5.71 |

### Stage 4 - arm `termonly`

**output:** No swelling of the liver or spleen, or pain when touched.

| metric | value |
|---|---:|
| bertscore_f1 | 0.734 |
| coleman_liau | 5.24 |
| coleman_liau_drop | 17.96 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 2.65 |
| fkgl_drop | 3.97 |
| fre | 95.7 |
| fre_gain | 41.0 |
| human_edit_recall | 1.000 |
| length_ratio | 1.22 |
| n_words | 11.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.967 |
| nli_faithfulness | 0.165 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 58.80 |
| smog | 3.13 |
| smog_drop | 5.71 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `tenderness` -> `pain when touched` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** No swelling of the liver or spleen, and no pain when touched.

| metric | value |
|---|---:|
| bertscore_f1 | 0.630 |
| coleman_liau | 4.93 |
| coleman_liau_drop | 18.27 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 2.86 |
| fkgl_drop | 3.76 |
| fre | 96.0 |
| fre_gain | 41.2 |
| human_edit_recall | 1.000 |
| length_ratio | 1.33 |
| n_words | 12.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.943 |
| nli_faithfulness | 0.038 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 49.72 |
| smog | 3.13 |
| smog_drop | 5.71 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `tenderness` -> `pain when touched` | replace | attributed | 0.996 | 1.669 | - | 0.822 | 0.326 | - |

**edit `tenderness` -> `pain when touched`**

- status: `attributed`
- log p full -0.5043, empty -1.4998
- masks scored: 18/18 (+2 top-k)
- ranked sources:
    - `+0.668` [wiktionary] tenderness: Tenderness is the pain or discomfort when an affected area is touched.
    - `+0.342` [readme] tenderness: Tenderness is when an area hurts when you touch it.
    - `+0.108` [readme] Tenderness: Tenderness is when an area hurts or is sensitive to touch.

- rationale: The original term refers to a physical sensation of pain triggered by touch, so "pain when touched" conveys that specific reaction in plain language. Phrase frequency increases from 3.24 to 4.22, while age of acquisition drops from 8.79 to 4.26. Patients can now recognize the symptom immediately without needing to recall a clinical descriptor.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

==============================================================================

## Note 88 - `881`

**ORIGINAL**  He did not experience his left anterior chest pain with exercise.

**REFERENCE** He did not experience his left front chest pain with exercise.

| | FKGL | FRE | SMOG | Coleman-Liau | words |
|---|---:|---:|---:|---:|---:|
| ORIGINAL | 9.08 | 49.54 | 13.02 | 9.98 | 11 |
| REFERENCE | 5.86 | 72.62 | 11.21 | 8.40 | 11 |

### Stage 2 - extraction + classification

| term | kind | category | action | Zipf | AoA | syll |
|---|---|---|---|---:|---:|---:|
| `experience` | word | general_hard_word | replace | 5.27 | 8.95 | 4 |
| `anterior` | word | medical_descriptor | replace | 3.51 | 14.12 | 4 |

### Stage 3 - retrieval

coverage **1.0** (2/2), glossary budget 8/16

| term | Zipf stratum | defs | sources | matched via | origin |
|---|---|---:|---|---|---|
| `experience` | common | 3 | thesarus.json, wiktionary.json | exact | extracted |
| `anterior` | uncommon | 5 | michigan_plmd.json, nih.json, readme_lay_vocab.jsonl, wiktionary.json | exact | extracted |

Glossary shown to the model:

1. `[wiktionary]` experience: An experience is an event that happens to you or that you are a part of.
2. `[readme]` Anterior: The front part of the body or an organ.
3. `[wiktionary]` experience: Experience is the amount of time you have been doing something (especially, a job).
4. `[readme]` anterior: Having to do with the front part of the body or an organ.
5. `[thesaurus]` experience: feel, have, go through
6. `[nih]` anterior: In human anatomy, has to do with the front of a structure, or a structure found toward the front of the body.
7. `[michigan]` anterior: The front of the body.
8. `[wiktionary]` anterior: Anterior is a word used in biology to refer to the front of an animal.

### Stage 4 - arm `naive`

**output:** He did not feel chest pain on the left side of his chest when he exercised.

| metric | value |
|---|---:|
| bertscore_f1 | 0.753 |
| coleman_liau | 3.74 |
| coleman_liau_drop | 6.24 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 3.93 |
| fkgl_drop | 5.16 |
| fre | 95.4 |
| fre_gain | 45.9 |
| human_edit_recall | 1.000 |
| laterality_preservation | 0.500 |
| length_ratio | 1.45 |
| n_words | 16.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.939 |
| nli_faithfulness | 0.992 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 25.55 |
| smog | 8.84 |
| smog_drop | 4.18 |

### Stage 4 - arm `termonly`

**output:** He did not feel chest pain on his left front side during exercise.

| metric | value |
|---|---:|
| bertscore_f1 | 0.814 |
| coleman_liau | 5.57 |
| coleman_liau_drop | 4.41 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 4.00 |
| fkgl_drop | 5.08 |
| fre | 89.5 |
| fre_gain | 40.0 |
| human_edit_recall | 1.000 |
| laterality_preservation | 0.500 |
| length_ratio | 1.18 |
| n_words | 13.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.980 |
| nli_faithfulness | 0.988 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 33.92 |
| smog | 8.84 |
| smog_drop | 4.18 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `experience` -> `feel` | replace | - | - | - | - | - | - | - |
| `anterior` -> `front side` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** He did not feel pain in the front of his left chest during exercise.

| metric | value |
|---|---:|
| bertscore_f1 | 0.790 |
| coleman_liau | 4.46 |
| coleman_liau_drop | 5.52 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 4.20 |
| fkgl_drop | 4.88 |
| fre | 89.9 |
| fre_gain | 40.4 |
| human_edit_recall | 1.000 |
| laterality_preservation | 0.500 |
| length_ratio | 1.27 |
| n_words | 14.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.979 |
| nli_faithfulness | 0.992 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 29.17 |
| smog | 8.84 |
| smog_drop | 4.18 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `experience` -> `feel` | replace | attributed | 0.003 | 0.013 | 0.742 | 0.783 | 0.014 | - |
| `anterior` -> `front of his left` | replace | attributed | 0.439 | 0.927 | 0.532 | 0.776 | 0.045 | - |

**edit `experience` -> `feel`**

- status: `attributed`
- log p full -0.2941, empty -0.2974
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.180` [thesaurus] experience: feel, have, go through
    - `+0.165` [readme] Anterior: The front part of the body or an organ.
    - `-0.042` [wiktionary] experience: An experience is an event that happens to you or that you are a part of.

- rationale: The original term "experience" refers to the personal feeling or sensation of something, which "feel" captures directly in simpler language. Phrase frequency rises from 5.27 to 5.67, and age of acquisition drops from 8.95 to 5.11, making the word more common and easier to learn at a younger age. Patients can now grasp the immediate sensation without needing to recall a more abstract concept.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `anterior` -> `front of his left`**

- status: `attributed`
- log p full -0.4480, empty -0.8874
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.070` [wiktionary] experience: Experience is the amount of time you have been doing something (especially, a job).
    - `+0.025` [wiktionary] experience: An experience is an event that happens to you or that you are a part of.
    - `+0.021` [nih] anterior: In human anatomy, has to do with the front of a structure, or a structure found toward the front of 
    - `+0.019` [thesaurus] experience: feel, have, go through

- rationale: The word "anterior" refers to the front part of the body, so replacing it with "front of his left" keeps that directional meaning in plain language. Phrase frequency rises from Zipf 3.51 to 5.10, while age of acquisition drops from 14.12 to 5.57. This change allows the patient to immediately visualize the location without needing to know anatomical terminology.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

==============================================================================

## Note 89 - `891`

**ORIGINAL**  Also, would use it to control the atrial fibrillation.

**REFERENCE** Also, would use it to control the irregular heart beat

| | FKGL | FRE | SMOG | Coleman-Liau | words |
|---|---:|---:|---:|---:|---:|
| ORIGINAL | 7.59 | 56.70 | 8.84 | 9.27 | 9 |
| REFERENCE | 6.01 | 69.79 | 8.84 | 6.76 | 10 |

### Stage 2 - extraction + classification

| term | kind | category | action | Zipf | AoA | syll |
|---|---|---|---|---:|---:|---:|
| `atrial fibrillation` | phrase | medical_essential | elaborate | 2.58 | 14.58 | 6 |

### Stage 3 - retrieval

coverage **1.0** (1/1), glossary budget 3/16

| term | Zipf stratum | defs | sources | matched via | origin |
|---|---|---:|---|---|---|
| `atrial fibrillation` | rare | 3 | justplainclear.json, readme_lay_vocab.jsonl | exact | extracted |

Glossary shown to the model:

1. `[readme]` Atrial fibrillation: Atrial fibrillation is when your heart beats irregularly and can make you tired or more likely to have a stroke.
2. `[readme]` atrial fibrillation: Atrial fibrillation is when your heart beats in a weird way that can make you tired and increase your risk of strokes.
3. `[justplainclear]` atrial fibrillation: A problem with the speed or rhythm that your heart beats It is the most common type of arrythmia. It is caused by the heart's electrical system not working properly.

### Stage 4 - arm `naive`

**output:** Also, the doctor would use it to control the atrial fibrillation.

| metric | value |
|---|---:|
| bertscore_f1 | 0.582 |
| coleman_liau | 9.45 |
| coleman_liau_drop | -0.19 |
| copy_jargon_rate | 1.000 |
| critical_error | 0.000 |
| fkgl | 8.01 |
| fkgl_drop | -0.42 |
| fre | 57.2 |
| fre_gain | 0.5 |
| human_edit_recall | 0.000 |
| length_ratio | 1.10 |
| n_words | 11.0 |
| nli_completeness | 0.980 |
| nli_faithfulness | 0.004 |
| replacement_f1 | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 25.32 |
| smog | 8.84 |
| smog_drop | 0.00 |

### Stage 4 - arm `termonly`

**output:** Also, would use it to control the heart rhythm.

| metric | value |
|---|---:|
| bertscore_f1 | 0.842 |
| coleman_liau | 4.76 |
| coleman_liau_drop | 4.51 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 3.65 |
| fkgl_drop | 3.93 |
| fre | 84.9 |
| fre_gain | 28.2 |
| human_edit_recall | 1.000 |
| length_ratio | 0.90 |
| n_words | 9.0 |
| nli_completeness | 0.164 |
| nli_faithfulness | 0.599 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 70.00 |
| smog | 3.13 |
| smog_drop | 5.71 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `atrial fibrillation` -> `heart rhythm` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Also, would use it to control the heart's irregular rhythm.

| metric | value |
|---|---:|
| bertscore_f1 | 0.809 |
| coleman_liau | 8.50 |
| coleman_liau_drop | 0.77 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 7.19 |
| fkgl_drop | 0.40 |
| fre | 61.3 |
| fre_gain | 4.6 |
| human_edit_recall | 1.000 |
| length_ratio | 1.10 |
| n_words | 11.0 |
| nli_completeness | 0.276 |
| nli_faithfulness | 0.904 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 71.43 |
| smog | 8.84 |
| smog_drop | 0.00 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `atrial fibrillation` -> `irregular rhythm` | replace | attributed | -0.355 | -0.601 | - | 0.586 | 0.186 | - |

**edit `atrial fibrillation` -> `irregular rhythm`**

- status: `attributed`
- log p full -1.0822, empty -0.7276
- masks scored: 10/10 (+2 top-k)
- ranked sources:
    - `+0.186` [readme] Atrial fibrillation: Atrial fibrillation is when your heart beats irregularly and can make you tired or more l
    - `-0.501` [readme] atrial fibrillation: Atrial fibrillation is when your heart beats in a weird way that can make you tired and i

- rationale: The original term refers to a specific type of heart rhythm disorder, so the replacement keeps that core medical concept in plain language. Phrase frequency increases from Zipf 2.58 to 3.54, while age of acquisition falls from 14.58 to 9.16. Patients can now understand the heart rhythm problem without needing to know the specific diagnostic name.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

==============================================================================

## Note 90 - `900`

**ORIGINAL**  Overall the patient is a seemingly good historian.

**REFERENCE** Overall the patient is seemingly good at remembering their history

| | FKGL | FRE | SMOG | Coleman-Liau | words |
|---|---:|---:|---:|---:|---:|
| ORIGINAL | 11.13 | 29.52 | 13.02 | 10.95 | 8 |
| REFERENCE | 11.91 | 27.49 | 14.55 | 14.30 | 10 |

### Stage 2 - extraction + classification

| term | kind | category | action | Zipf | AoA | syll |
|---|---|---|---|---:|---:|---:|
| `good historian` | phrase | medical_descriptor | replace | 3.9 | 11.58 | 5 |
| `good` | word | medical_descriptor | replace | - | - | - |
| `historian` | word | medical_descriptor | replace | - | - | - |
| `seemingly` | word | general_hard_word | replace | 4.1 | 9.79 | 3 |

### Stage 3 - retrieval

coverage **0.5** (1/2), glossary budget 4/16

| term | Zipf stratum | defs | sources | matched via | origin |
|---|---|---:|---|---|---|
| `good historian` | uncommon | 0 | - | - | extracted |
| `good` | common | 2 | wiktionary.json | exact | split_from_uncovered |
| `historian` | uncommon | 1 | wiktionary.json | exact | split_from_uncovered |
| `seemingly` | uncommon | 1 | dictonary.csv | exact | extracted |

Glossary shown to the model:

1. `[wiktionary]` historian: A historian is a person who studies or writes about history.
2. `[dictionary]` Seemingly (adv.): In appearance; in show; in semblance; apparently; ostensibly.
3. `[wiktionary]` good: When you are good, you do the right things. That is, you do things that are kind or helpful. You do not do things that hurt people or are not honest.
4. `[wiktionary]` good: If something is good it is useful or helpful. This also means high quality.

### Stage 4 - arm `naive`

**output:** Overall, the patient seems to be a good person to talk to about their health.

| metric | value |
|---|---:|
| bertscore_f1 | 0.491 |
| coleman_liau | 5.81 |
| coleman_liau_drop | 5.14 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.333 |
| fkgl | 5.99 |
| fkgl_drop | 5.14 |
| fre | 78.8 |
| fre_gain | 49.3 |
| human_edit_recall | 1.000 |
| length_ratio | 1.50 |
| n_words | 15.0 |
| nli_completeness | 0.382 |
| nli_faithfulness | 0.018 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 39.67 |
| smog | 8.84 |
| smog_drop | 4.18 |

### Stage 4 - arm `termonly`

**output:** Overall the patient seems to tell a good story.

| metric | value |
|---|---:|
| bertscore_f1 | 0.517 |
| coleman_liau | 5.40 |
| coleman_liau_drop | 5.55 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 4.96 |
| fkgl_drop | 6.17 |
| fre | 75.5 |
| fre_gain | 46.0 |
| human_edit_recall | 1.000 |
| length_ratio | 0.90 |
| n_words | 9.0 |
| nli_completeness | 0.518 |
| nli_faithfulness | 0.986 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 38.28 |
| smog | 8.84 |
| smog_drop | 4.18 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `seemingly` -> `seems` | replace | - | - | - | - | - | - | - |
| `good historian` -> `good story` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Overall the patient seems to tell a clear story.

| metric | value |
|---|---:|
| bertscore_f1 | 0.397 |
| coleman_liau | 6.04 |
| coleman_liau_drop | 4.91 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 4.96 |
| fkgl_drop | 6.17 |
| fre | 75.5 |
| fre_gain | 46.0 |
| human_edit_recall | 1.000 |
| length_ratio | 0.90 |
| n_words | 9.0 |
| nli_completeness | 0.095 |
| nli_faithfulness | 0.810 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 36.53 |
| smog | 8.84 |
| smog_drop | 4.18 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `seemingly` -> `seems` | replace | attributed | -0.302 | -0.457 | - | 0.665 | 0.003 | - |
| `good historian` -> `clear story` | replace | attributed | -0.258 | -0.346 | - | 0.968 | 0.030 | - |

**edit `seemingly` -> `seems`**

- status: `attributed`
- log p full -1.2387, empty -0.9368
- masks scored: 18/18 (+4 top-k)
- ranked sources:
    - `-0.014` [wiktionary] good: When you are good, you do the right things. That is, you do things that are kind or helpful. You do not 
    - `-0.017` [wiktionary] historian: A historian is a person who studies or writes about history.
    - `-0.128` [wiktionary] good: If something is good it is useful or helpful. This also means high quality.
    - `-0.225` [dictionary] Seemingly (adv.): In appearance; in show; in semblance; apparently; ostensibly.

- rationale: The original term "seemingly" suggests that something appears to be true but might not be, whereas "seems" conveys that same appearance in a direct and immediate way. Phrase frequency increases from Zipf 4.10 to 5.24, and the syllable count drops from 3 to 1. Patients can now grasp the tentative nature of the observation without stumbling over a longer, more formal word.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `good historian` -> `clear story`**

- status: `attributed`
- log p full -1.5057, empty -1.2474
- masks scored: 18/18 (+4 top-k)
- ranked sources:
    - `+0.460` [dictionary] Seemingly (adv.): In appearance; in show; in semblance; apparently; ostensibly.
    - `+0.430` [wiktionary] good: If something is good it is useful or helpful. This also means high quality.
    - `+0.205` [wiktionary] historian: A historian is a person who studies or writes about history.
    - `-1.326` [wiktionary] good: When you are good, you do the right things. That is, you do things that are kind or helpful. You do not 

- rationale: The original phrase "good historian" refers to a patient who can clearly recount their medical history, while "clear story" conveys that same idea of a well-organized account in simpler terms. Phrase frequency rises from 3.90 to 5.04, and age of acquisition drops from 11.58 to 5.80, making the language significantly more common and familiar. Patients can now grasp the importance of a coherent medical narrative without needing to understand the specific role of a "historian."user
You explain, to a patient, why one phrase in a medical sentence was replaced with another.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

==============================================================================

## Note 91 - `933`

**ORIGINAL**  No active Crohn 's disease was found during the colonoscopy.

**REFERENCE** No active Crohn 's disease was found during the camera test through the gut.

| | FKGL | FRE | SMOG | Coleman-Liau | words |
|---|---:|---:|---:|---:|---:|
| ORIGINAL | 3.65 | 86.71 | 3.13 | 9.66 | 10 |
| REFERENCE | 5.88 | 77.81 | 8.84 | 7.36 | 14 |

### Stage 2 - extraction + classification

| term | kind | category | action | Zipf | AoA | syll |
|---|---|---|---|---:|---:|---:|
| `active Crohn 's disease` | phrase | medical_essential | elaborate | 1.52 | 7.55 | 6 |
| `active` | word | medical_descriptor | replace | - | - | - |
| `s disease` | phrase | medical_essential | elaborate | - | - | - |
| `colonoscopy` | word | medical_essential | elaborate | 2.74 | 15.76 | 1 |

### Stage 3 - retrieval

coverage **0.5** (1/2), glossary budget 12/16

| term | Zipf stratum | defs | sources | matched via | origin |
|---|---|---:|---|---|---|
| `active Crohn 's disease` | very_rare | 0 | - | - | extracted |
| `active` | common | 5 | justplainclear.json, readme_lay_vocab.jsonl, wiktionary.json | exact | split_from_uncovered |
| `s disease` | common | 2 | readme_lay_vocab.jsonl | exact | split_from_uncovered |
| `colonoscopy` | rare | 5 | justplainclear.json, michigan_plmd.json, nih.json, readme_lay_vocab.jsonl | exact | extracted |

Glossary shown to the model:

1. `[readme]` von Willebrand 's disease: A condition where blood can't clot properly, causing abnormal bleeding.
2. `[readme]` Active: Happening right now.
3. `[readme]` colonoscopy: A colonoscopy is a test that checks the inside of your large intestine for signs of cancer.
4. `[readme]` Hashimoto 's disease: When the immune system attacks the thyroid gland in the neck.
5. `[readme]` active: Currently happening.
6. `[readme]` colonoscopy: A procedure to check for colon cancer by examining the inside of the large intestine.
7. `[justplainclear]` active: Moving; changing; keeping busy
8. `[nih]` colonoscopy: Examination of the inside of the colon using a colonoscope, inserted into the rectum. A colonoscope is a thin, tube-like instrument with a light and a lens for viewing. It may also have a tool to remove tissue to be checked under a microscope for signs of disease.
9. `[wiktionary]` active: Something is active if it is turned on or started.
10. `[michigan]` colonoscopy: Looks at the inside of the large intestine using a flexible tube with a ltiny camera at the end.
11. `[wiktionary]` active: If someone is active, he or she does exercise often or participates often.
12. `[justplainclear]` colonoscopy: An exam of the inside of the large intestine that uses a flexible tube with a lens at the end

### Stage 4 - arm `naive`

**output:** No active Crohn's disease was found during the colonoscopy.

| metric | value |
|---|---:|
| bertscore_f1 | 0.709 |
| coleman_liau | 12.49 |
| coleman_liau_drop | -2.83 |
| copy_jargon_rate | 1.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 3.65 |
| fkgl_drop | -0.00 |
| fre | 84.9 |
| fre_gain | -1.8 |
| human_edit_recall | 0.000 |
| length_ratio | 0.71 |
| n_words | 10.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.988 |
| nli_faithfulness | 0.993 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 31.21 |
| smog | 3.13 |
| smog_drop | 0.00 |

### Stage 4 - arm `termonly`

**output:** No flare-up of Crohn's disease was found during the colonoscopy.

| metric | value |
|---|---:|
| bertscore_f1 | 0.546 |
| coleman_liau | 11.40 |
| coleman_liau_drop | -1.74 |
| copy_jargon_rate | 1.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 3.65 |
| fkgl_drop | 0.00 |
| fre | 86.7 |
| fre_gain | 0.0 |
| human_edit_recall | 0.000 |
| length_ratio | 0.86 |
| n_words | 12.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.988 |
| nli_faithfulness | 0.991 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 26.54 |
| smog | 3.13 |
| smog_drop | 0.00 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `active Crohn 's disease` -> `Crohn's disease` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** The test looking inside the large intestine found no flare-up of Crohn's disease.

| metric | value |
|---|---:|
| bertscore_f1 | 0.484 |
| coleman_liau | 11.37 |
| coleman_liau_drop | -1.71 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.333 |
| fkgl | 6.73 |
| fkgl_drop | -3.08 |
| fre | 70.0 |
| fre_gain | -16.7 |
| human_edit_recall | 1.000 |
| length_ratio | 1.07 |
| n_words | 15.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.616 |
| nli_faithfulness | 0.942 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 19.13 |
| smog | 8.84 |
| smog_drop | -5.71 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `active` -> `flare-up` | replace | attributed | 0.002 | 0.003 | 0.764 | 0.632 | 0.156 | - |

**edit `active` -> `flare-up`**

- status: `attributed`
- log p full -0.8723, empty -0.8740
- masks scored: 66/66 (+2 top-k)
- ranked sources:
    - `+0.222` [wiktionary] active: Something is active if it is turned on or started.
    - `+0.066` [wiktionary] active: If someone is active, he or she does exercise often or participates often.
    - `+0.059` [justplainclear] active: Moving; changing; keeping busy
    - `+0.041` [readme] colonoscopy: A procedure to check for colon cancer by examining the inside of the large intestine.
    - `+0.024` [readme] active: Currently happening.

- rationale: The original term "active" suggests a state of being awake or engaged, whereas "flare-up" specifically conveys a sudden, intense return of symptoms. Phrase frequency increases from Zipf 4.93 to 3.64, while syllable count remains constant at 2. Patients can now clearly identify a sudden worsening of their condition without confusion over general activity levels.
- audit: coverage 1.0, grounding_error=True, omission=False, source_ok=True, passage_ok=True

==============================================================================

## Note 92 - `935`

**ORIGINAL**  Shortly after the patient's initial assessment, the patient apparently began to complain of chest pain and appeared to the nurse to have mounting exhaustion and respiratory distress.

**REFERENCE** Shortly after the patient's initial assessment, the patient apparently began to complain of chest pain and appeared to the nurse to have worsening exhaustion and breathing distress.

| | FKGL | FRE | SMOG | Coleman-Liau | words |
|---|---:|---:|---:|---:|---:|
| ORIGINAL | 16.35 | 25.90 | 15.90 | 15.97 | 28 |
| REFERENCE | 15.48 | 32.16 | 15.90 | 15.76 | 28 |

### Stage 2 - extraction + classification

| term | kind | category | action | Zipf | AoA | syll |
|---|---|---|---|---:|---:|---:|
| `respiratory distress` | phrase | medical_descriptor | replace | 3.57 | 11.16 | 7 |
| `mounting exhaustion` | phrase | medical_descriptor | replace | 3.34 | 7.61 | 5 |
| `mounting` | word | medical_descriptor | replace | - | - | - |
| `exhaustion` | word | medical_descriptor | replace | - | - | - |

### Stage 3 - retrieval

coverage **0.5** (1/2), glossary budget 5/16

| term | Zipf stratum | defs | sources | matched via | origin |
|---|---|---:|---|---|---|
| `respiratory distress` | uncommon | 2 | readme_lay_vocab.jsonl | exact | extracted |
| `mounting exhaustion` | rare | 0 | - | - | extracted |
| `mounting` | uncommon | 1 | wiktionary.json | exact | split_from_uncovered |
| `exhaustion` | rare | 2 | wiktionary.json | exact | split_from_uncovered |

Glossary shown to the model:

1. `[wiktionary]` mounting: If you mount something you get on to it.
2. `[readme]` Respiratory Distress: Having difficulty breathing.
3. `[wiktionary]` exhaustion: Exhaustion is the point where something is completely depleted.
4. `[readme]` acute respiratory distress syndrome: A serious lung condition that causes low levels of oxygen in the blood, which can be life-threatening if not treated promptly.
5. `[wiktionary]` exhaustion: Exhaustion is the state of extreme tiredness.

### Stage 4 - arm `naive`

**output:** Shortly after the nurse first checked the patient, she started complaining of chest pain and seemed to be getting more tired and having trouble breathing.

| metric | value |
|---|---:|
| bertscore_f1 | 0.687 |
| coleman_liau | 12.71 |
| coleman_liau_drop | 3.26 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.250 |
| fkgl | 11.15 |
| fkgl_drop | 5.20 |
| fre | 59.6 |
| fre_gain | 33.7 |
| human_edit_recall | 1.000 |
| length_ratio | 0.89 |
| n_words | 25.0 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.994 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.600 |
| sari | 20.58 |
| smog | 8.84 |
| smog_drop | 7.06 |
| temporality_preservation | 1.000 |

### Stage 4 - arm `termonly`

**output:** Shortly after the patient's initial assessment, the patient apparently began to complain of chest pain and appeared to the nurse to have worsening tiredness and trouble breathing.

| metric | value |
|---|---:|
| bertscore_f1 | 0.921 |
| coleman_liau | 15.33 |
| coleman_liau_drop | 0.64 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 15.48 |
| fkgl_drop | 0.87 |
| fre | 32.2 |
| fre_gain | 6.3 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 28.0 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.994 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 71.06 |
| smog | 15.90 |
| smog_drop | 0.00 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `mounting exhaustion` -> `worsening tiredness` | replace | - | - | - | - | - | - | - |
| `respiratory distress` -> `trouble breathing` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Shortly after the patient's initial assessment, the patient apparently began to complain of chest pain and appeared to the nurse to have worsening tiredness and trouble breathing.

| metric | value |
|---|---:|
| bertscore_f1 | 0.921 |
| coleman_liau | 15.33 |
| coleman_liau_drop | 0.64 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 15.48 |
| fkgl_drop | 0.87 |
| fre | 32.2 |
| fre_gain | 6.3 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 28.0 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.994 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 71.06 |
| smog | 15.90 |
| smog_drop | 0.00 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `mounting exhaustion` -> `worsening tiredness` | replace | attributed | -0.307 | -0.380 | - | 0.581 | 0.000 | - |
| `respiratory distress` -> `trouble breathing` | replace | attributed | 0.000 | 0.001 | - | 0.470 | 0.081 | - |

**edit `mounting exhaustion` -> `worsening tiredness`**

- status: `attributed`
- log p full -1.8060, empty -1.4992
- masks scored: 34/34 (+4 top-k)
- ranked sources:
    - `-0.183` [readme] Respiratory Distress: Having difficulty breathing.
    - `-0.264` [wiktionary] exhaustion: Exhaustion is the state of extreme tiredness.

- rationale: The original phrase describes a growing sense of extreme fatigue, so "worsening tiredness" conveys that same increasing weariness in simpler terms. Phrase frequency drops from Zipf 3.34 to 2.72, while age of acquisition rises from 7.61 to 10.84. You can now grasp the patient's increasing fatigue without needing to know the specific idiomatic expression.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `respiratory distress` -> `trouble breathing`**

- status: `attributed`
- log p full -0.4378, empty -0.4383
- masks scored: 34/34 (+4 top-k)
- ranked sources:
    - `+0.081` [readme] Respiratory Distress: Having difficulty breathing.
    - `-0.095` [readme] acute respiratory distress syndrome: A serious lung condition that causes low levels of oxygen in the blood, w
    - `-0.133` [wiktionary] exhaustion: Exhaustion is the point where something is completely depleted.
    - `-0.134` [wiktionary] mounting: If you mount something you get on to it.

- rationale: The original phrase describes a state of severe difficulty in breathing, so "trouble breathing" conveys that same urgent struggle in everyday language. Phrase frequency rises from 3.57 to 4.16, while age of acquisition drops from 11.16 to 4.56. Patients can now grasp the immediate physical problem without needing to know the clinical label.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

==============================================================================

## Note 93 - `968`

**ORIGINAL**  She has been referred for a pacemaker implantation.

**REFERENCE** She has been referred for a pacemaker fitting surgery.

| | FKGL | FRE | SMOG | Coleman-Liau | words |
|---|---:|---:|---:|---:|---:|
| ORIGINAL | 8.18 | 50.67 | 11.21 | 11.68 | 8 |
| REFERENCE | 7.59 | 56.70 | 11.21 | 9.91 | 9 |

### Stage 2 - extraction + classification

| term | kind | category | action | Zipf | AoA | syll |
|---|---|---|---|---:|---:|---:|
| `pacemaker implantation` | phrase | medical_essential | elaborate | 2.69 | 12.42 | 7 |
| `pacemaker` | word | medical_descriptor | replace | - | - | - |
| `implantation` | word | medical_descriptor | replace | - | - | - |
| `referred` | word | general_hard_word | replace | 4.61 | None | 2 |

### Stage 3 - retrieval

coverage **0.5** (1/2), glossary budget 8/16

| term | Zipf stratum | defs | sources | matched via | origin |
|---|---|---:|---|---|---|
| `pacemaker implantation` | rare | 0 | - | - | extracted |
| `pacemaker` | rare | 4 | justplainclear.json, nih.json, readme_lay_vocab.jsonl | exact | split_from_uncovered |
| `implantation` | rare | 2 | readme_lay_vocab.jsonl | exact | split_from_uncovered |
| `referred` | common | 2 | readme_lay_vocab.jsonl, wiktionary.json | exact | extracted |

Glossary shown to the model:

1. `[readme]` implantation: Surgery where a device is placed inside your body.
2. `[readme]` REFERRED: Sending a patient to another person or place for medical care.
3. `[readme]` pacemaker: A small device that helps regulate the heartbeat when placed in the chest.
4. `[readme]` IMPLANTATION: A surgery where a device is placed inside the body.
5. `[wiktionary]` referred: If you refer to something, you talk or write about it, usually in passing.
6. `[readme]` pacemaker: A pacemaker is a device that uses electrical signals to regulate the heartbeat.
7. `[nih]` pacemaker: An electronic device that is implanted in the body to monitor heart rate and rhythm. It gives the heart electrical stimulation when it does not beat normally. It runs on batteries and has long, thin wires that connect it to the heart. Also called artificial pacemaker and cardiac pacemaker.
8. `[justplainclear]` pacemaker: A medical device placed inside your chest or abdomen that helps control your heartbeat

### Stage 4 - arm `naive`

**output:** She has been sent to get a pacemaker put inside her heart.

| metric | value |
|---|---:|
| bertscore_f1 | 0.572 |
| coleman_liau | 3.97 |
| coleman_liau_drop | 7.71 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.333 |
| fkgl | 3.84 |
| fkgl_drop | 4.34 |
| fre | 88.9 |
| fre_gain | 38.2 |
| human_edit_recall | 1.000 |
| length_ratio | 1.33 |
| n_words | 12.0 |
| nli_completeness | 0.993 |
| nli_faithfulness | 0.956 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 23.47 |
| smog | 8.84 |
| smog_drop | 2.37 |

### Stage 4 - arm `termonly`

**output:** She has been sent to get a small battery put in her heart.

| metric | value |
|---|---:|
| bertscore_f1 | 0.452 |
| coleman_liau | 2.00 |
| coleman_liau_drop | 9.67 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.250 |
| fkgl | 3.10 |
| fkgl_drop | 5.08 |
| fre | 96.0 |
| fre_gain | 45.4 |
| human_edit_recall | 1.000 |
| length_ratio | 1.44 |
| n_words | 13.0 |
| nli_completeness | 0.664 |
| nli_faithfulness | 0.451 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 20.09 |
| smog | 8.84 |
| smog_drop | 2.37 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `referred` -> `sent` | replace | - | - | - | - | - | - | - |
| `pacemaker implantation` -> `small battery put in her heart` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** She has been sent to get a small heart device put inside her chest.

| metric | value |
|---|---:|
| bertscore_f1 | 0.479 |
| coleman_liau | 4.04 |
| coleman_liau_drop | 7.63 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 3.36 |
| fkgl_drop | 4.82 |
| fre | 95.9 |
| fre_gain | 45.3 |
| human_edit_recall | 1.000 |
| length_ratio | 1.56 |
| n_words | 14.0 |
| nli_completeness | 0.174 |
| nli_faithfulness | 0.917 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 20.09 |
| smog | 3.13 |
| smog_drop | 8.08 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `referred` -> `sent` | replace | attributed | 0.144 | 2.196 | 0.895 | 0.912 | 1.780 | - |
| `pacemaker implantation` -> `small heart device put inside her chest` | replace | attributed | 3.086 | 3.102 | 0.799 | 0.918 | 1.957 | - |

**edit `referred` -> `sent`**

- status: `attributed`
- log p full -0.0195, empty -0.1631
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+1.961` [readme] REFERRED: Sending a patient to another person or place for medical care.
    - `+0.181` [readme] implantation: Surgery where a device is placed inside your body.
    - `+0.084` [readme] pacemaker: A pacemaker is a device that uses electrical signals to regulate the heartbeat.
    - `+0.024` [justplainclear] pacemaker: A medical device placed inside your chest or abdomen that helps control your heartbeat
    - `+0.010` [readme] pacemaker: A small device that helps regulate the heartbeat when placed in the chest.

- rationale: The original term "referred" implies that a patient was directed to another provider, while "sent" conveys that same action of being dispatched in simpler language. Phrase frequency increases from Zipf 4.61 to 5.16, and syllable count drops from 2 to 1. Patients can now immediately grasp that they were directed to a specialist without needing to process the formal medical verb.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `pacemaker implantation` -> `small heart device put inside her chest`**

- status: `attributed`
- log p full -4.0842, empty -7.1703
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+2.187` [readme] pacemaker: A small device that helps regulate the heartbeat when placed in the chest.
    - `+0.230` [nih] pacemaker: An electronic device that is implanted in the body to monitor heart rate and rhythm. It gives the h
    - `+0.226` [readme] IMPLANTATION: A surgery where a device is placed inside the body.
    - `+0.183` [readme] implantation: Surgery where a device is placed inside your body.
    - `+0.032` [justplainclear] pacemaker: A medical device placed inside your chest or abdomen that helps control your heartbeat

- rationale: The glossary defines the original term as a small device placed in the chest to regulate the heartbeat, so the replacement keeps this core function in plain language. Phrase frequency rises from 2.69 to 4.16, while age of acquisition drops from 12.42 to 8.06. Patients can now understand the procedure as a simple internal tool rather than a complex medical operation.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

==============================================================================

## Note 94 - `116`

**ORIGINAL**  There was some hematoma at the cath site.

**REFERENCE** There was some swelling due to collection of blood at the catheter site.

| | FKGL | FRE | SMOG | Coleman-Liau | words |
|---|---:|---:|---:|---:|---:|
| ORIGINAL | -0.67 | 114.12 | 3.13 | 4.43 | 8 |
| REFERENCE | 5.82 | 76.50 | 11.21 | 8.25 | 13 |

### Stage 2 - extraction + classification

| term | kind | category | action | Zipf | AoA | syll |
|---|---|---|---|---:|---:|---:|
| `cath site` | phrase | abbreviation_essential | abbr_expand_elaborate | 2.9 | 8.63 | 2 |
| `site` | word | medical_descriptor | replace | - | - | - |
| `hematoma` | word | medical_descriptor | replace | 2.61 | 14.78 | 1 |

### Stage 3 - retrieval

coverage **0.5** (1/2), glossary budget 6/16

| term | Zipf stratum | defs | sources | matched via | origin |
|---|---|---:|---|---|---|
| `cath site` | rare | 0 | - | - | extracted |
| `site` | common | 2 | wiktionary.json | exact | split_from_uncovered |
| `hematoma` | rare | 4 | iowa.json, justplainclear.json, michigan_plmd.json, nih.json | exact | extracted |

Glossary shown to the model:

1. `[wiktionary]` site: A site is a location or a place.
2. `[nih]` hematoma: A pool of clotted or partially clotted blood in an organ, tissue, or body space, usually caused by a broken blood vessel.
3. `[wiktionary]` site: A site is a website.
4. `[iowa]` HEMATOMA: a bruise, a black and blue mark
5. `[michigan]` hematoma: A bruise or when your skin is black and blue after an injury.
6. `[justplainclear]` hematoma: A collection of blood under the skin or in the body that is typically caused by a broken blood vessel

### Stage 4 - arm `naive`

**output:** There was a small collection of blood at the place where the catheter was inserted.

| metric | value |
|---|---:|
| bertscore_f1 | 0.654 |
| coleman_liau | 8.52 |
| coleman_liau_drop | -4.09 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.667 |
| fkgl | 6.78 |
| fkgl_drop | -7.45 |
| fre | 73.2 |
| fre_gain | -40.9 |
| human_edit_recall | 1.000 |
| length_ratio | 1.15 |
| n_words | 15.0 |
| nli_completeness | 0.249 |
| nli_faithfulness | 0.807 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.250 |
| sari | 50.47 |
| smog | 13.02 |
| smog_drop | -9.89 |

### Stage 4 - arm `termonly`

**output:** There was a bruise at the vein access site.

| metric | value |
|---|---:|
| bertscore_f1 | 0.556 |
| coleman_liau | 2.82 |
| coleman_liau_drop | 1.60 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 1.03 |
| fkgl_drop | -1.70 |
| fre | 103.7 |
| fre_gain | -10.4 |
| human_edit_recall | 1.000 |
| length_ratio | 0.69 |
| n_words | 9.0 |
| nli_completeness | 0.104 |
| nli_faithfulness | 0.019 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 41.74 |
| smog | 3.13 |
| smog_drop | 0.00 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `hematoma` -> `bruise` | replace | - | - | - | - | - | - | - |
| `cath site` -> `vein access site` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** There was a bruise at the needle spot.

| metric | value |
|---|---:|
| bertscore_f1 | 0.549 |
| coleman_liau | 2.25 |
| coleman_liau_drop | 2.18 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.333 |
| fkgl | 0.80 |
| fkgl_drop | -1.47 |
| fre | 103.5 |
| fre_gain | -10.6 |
| human_edit_recall | 1.000 |
| length_ratio | 0.62 |
| n_words | 8.0 |
| nli_completeness | 0.174 |
| nli_faithfulness | 0.023 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.250 |
| sari | 39.44 |
| smog | 3.13 |
| smog_drop | 0.00 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `hematoma` -> `bruise` | replace | attributed | 0.417 | 0.595 | 0.925 | 0.957 | 1.244 | - |
| `cath site` -> `needle spot` | replace | attributed | 1.396 | 1.487 | 0.712 | 0.802 | 0.155 | - |

**edit `hematoma` -> `bruise`**

- status: `attributed`
- log p full -1.0091, empty -1.4256
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+2.044` [iowa] HEMATOMA: a bruise, a black and blue mark
    - `+0.800` [michigan] hematoma: A bruise or when your skin is black and blue after an injury.
    - `+0.218` [wiktionary] site: A site is a website.
    - `-1.083` [nih] hematoma: A pool of clotted or partially clotted blood in an organ, tissue, or body space, usually caused by a

- rationale: The original term refers to a localized collection of blood outside of blood vessels, so "bruise" conveys that visible mark in plain language. Phrase frequency increases from Zipf 2.61 to 3.18, while age of acquisition drops from 14.78 to 5.45. Patients can now recognize the physical injury without needing specialized medical vocabulary.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `cath site` -> `needle spot`**

- status: `attributed`
- log p full -2.1850, empty -3.5813
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.487` [nih] hematoma: A pool of clotted or partially clotted blood in an organ, tissue, or body space, usually caused by a
    - `+0.331` [wiktionary] site: A site is a website.
    - `+0.242` [wiktionary] site: A site is a location or a place.
    - `+0.184` [michigan] hematoma: A bruise or when your skin is black and blue after an injury.
    - `+0.077` [justplainclear] hematoma: A collection of blood under the skin or in the body that is typically caused by a broken blood vesse

- rationale: The original term refers to the specific location where a needle was inserted, so "needle spot" keeps that precise anatomical focus in plain language. Phrase frequency increases from 2.90 to 3.93, while age of acquisition drops from 8.63 to 5.39. Patients can now identify the exact area of concern without needing specialized medical jargon.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

==============================================================================

## Note 95 - `592`

**ORIGINAL**  The necrotic tissue was lifted out of the abdomen.

**REFERENCE** The dead flesh was lifted out of the abdomen.

| | FKGL | FRE | SMOG | Coleman-Liau | words |
|---|---:|---:|---:|---:|---:|
| ORIGINAL | 6.28 | 66.10 | 8.84 | 7.33 | 9 |
| REFERENCE | 3.65 | 84.90 | 8.84 | 4.11 | 9 |

### Stage 2 - extraction + classification

| term | kind | category | action | Zipf | AoA | syll |
|---|---|---|---|---:|---:|---:|
| `necrotic tissue` | phrase | medical_descriptor | replace | 2.54 | 15.07 | 4 |
| `necrotic` | word | medical_descriptor | replace | - | - | - |
| `tissue` | word | medical_descriptor | replace | - | - | - |

### Stage 3 - retrieval

coverage **0.0** (0/1), glossary budget 8/16

| term | Zipf stratum | defs | sources | matched via | origin |
|---|---|---:|---|---|---|
| `necrotic tissue` | rare | 0 | - | - | extracted |
| `necrotic` | rare | 2 | readme_lay_vocab.jsonl | exact | split_from_uncovered |
| `tissue` | uncommon | 6 | justplainclear.json, nih.json, readme_lay_vocab.jsonl, wiktionary.json | exact | split_from_uncovered |

Glossary shown to the model:

1. `[readme]` necrotic: Tissue or skin death.
2. `[readme]` tissue: A group of cells that work together to form body structures and organs.
3. `[readme]` Necrotic: Necrotic means when tissue or skin dies.
4. `[readme]` TISSUE: A bunch of cells teaming up to do a job.
5. `[nih]` tissue: A group or layer of cells that work together to perform a specific function.
6. `[justplainclear]` tissue: A group of cells in the body that are alike. Organs, muscles, skin and other body parts are made up of tissue.
7. `[wiktionary]` tissue: A piece of tissue is a sheet of paper that can absorb very well.
8. `[wiktionary]` tissue: Tissue is a group of cells that work together to do a job.

### Stage 4 - arm `naive`

**output:** The dead tissue was removed from the patient's belly.

| metric | value |
|---|---:|
| bertscore_f1 | 0.699 |
| coleman_liau | 8.62 |
| coleman_liau_drop | -1.29 |
| copy_jargon_rate | 0.333 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| diagnostic_identity_preservation | 1.000 |
| fkgl | 4.96 |
| fkgl_drop | 1.31 |
| fre | 75.5 |
| fre_gain | 9.4 |
| human_edit_recall | 0.667 |
| length_ratio | 1.11 |
| n_words | 10.0 |
| nli_completeness | 0.992 |
| nli_faithfulness | 0.981 |
| replacement_f1 | 0.800 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.750 |
| sari | 19.93 |
| smog | 3.13 |
| smog_drop | 5.71 |

### Stage 4 - arm `termonly`

**output:** The dead tissue was lifted out of the abdomen.

| metric | value |
|---|---:|
| bertscore_f1 | 0.871 |
| coleman_liau | 4.76 |
| coleman_liau_drop | 2.58 |
| copy_jargon_rate | 0.333 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| diagnostic_identity_preservation | 1.000 |
| fkgl | 4.96 |
| fkgl_drop | 1.31 |
| fre | 75.5 |
| fre_gain | 9.4 |
| human_edit_recall | 0.667 |
| length_ratio | 1.00 |
| n_words | 9.0 |
| nli_completeness | 0.992 |
| nli_faithfulness | 0.994 |
| replacement_f1 | 0.800 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 72.13 |
| smog | 8.84 |
| smog_drop | 0.00 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `necrotic tissue` -> `dead tissue` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** The dead tissue was lifted out of the abdomen.

| metric | value |
|---|---:|
| bertscore_f1 | 0.871 |
| coleman_liau | 4.76 |
| coleman_liau_drop | 2.58 |
| copy_jargon_rate | 0.333 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| diagnostic_identity_preservation | 1.000 |
| fkgl | 4.96 |
| fkgl_drop | 1.31 |
| fre | 75.5 |
| fre_gain | 9.4 |
| human_edit_recall | 0.667 |
| length_ratio | 1.00 |
| n_words | 9.0 |
| nli_completeness | 0.992 |
| nli_faithfulness | 0.994 |
| replacement_f1 | 0.800 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 72.13 |
| smog | 8.84 |
| smog_drop | 0.00 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `necrotic tissue` -> `dead tissue` | replace | attributed | -0.513 | -2.513 | 0.808 | 0.840 | 0.034 | - |

**edit `necrotic tissue` -> `dead tissue`**

- status: `attributed`
- log p full -0.5734, empty -0.0608
- masks scored: 66/66 (+2 top-k)
- ranked sources:
    - `+0.088` [wiktionary] tissue: A piece of tissue is a sheet of paper that can absorb very well.
    - `+0.054` [readme] tissue: A group of cells that work together to form body structures and organs.
    - `+0.031` [readme] Necrotic: Necrotic means when tissue or skin dies.
    - `-0.387` [nih] tissue: A group or layer of cells that work together to perform a specific function.

- rationale: The original term refers to body parts that have died and lost their function, so "dead tissue" conveys this biological state in plain language. Phrase frequency increases from Zipf 2.54 to 4.26, while age of acquisition drops from 15.07 to 5.17. Patients can now grasp the severity of the injury without needing specialized medical vocabulary.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

==============================================================================

## Note 96 - `249`

**ORIGINAL**  Pressure was held and the area was hemostatic.

**REFERENCE** Pressure was held and the area stopped bleeding.

| | FKGL | FRE | SMOG | Coleman-Liau | words |
|---|---:|---:|---:|---:|---:|
| ORIGINAL | 6.71 | 61.24 | 11.21 | 8.05 | 8 |
| REFERENCE | 5.23 | 71.82 | 8.84 | 9.50 | 8 |

### Stage 2 - extraction + classification

| term | kind | category | action | Zipf | AoA | syll |
|---|---|---|---|---:|---:|---:|
| `hemostatic` | word | medical_descriptor | replace | 1.73 | None | 3 |

### Stage 3 - retrieval

coverage **1.0** (1/1), glossary budget 2/16

| term | Zipf stratum | defs | sources | matched via | origin |
|---|---|---:|---|---|---|
| `hemostatic` | very_rare | 2 | readme_lay_vocab.jsonl | exact | extracted |

Glossary shown to the model:

1. `[readme]` hemostatic: Stopping blood flow.
2. `[readme]` hemostatic: Hemostatic means stopping bleeding.

### Stage 4 - arm `naive`

**output:** The pressure was kept on, and the bleeding stopped.

| metric | value |
|---|---:|
| bertscore_f1 | 0.659 |
| coleman_liau | 7.33 |
| coleman_liau_drop | 0.72 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 2.34 |
| fkgl_drop | 4.36 |
| fre | 94.3 |
| fre_gain | 33.1 |
| human_edit_recall | 1.000 |
| length_ratio | 1.12 |
| n_words | 9.0 |
| nli_completeness | 0.414 |
| nli_faithfulness | 0.188 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.667 |
| sari | 29.21 |
| smog | 3.13 |
| smog_drop | 8.08 |

### Stage 4 - arm `termonly`

**output:** Pressure was held and the bleeding stopped.

| metric | value |
|---|---:|
| bertscore_f1 | 0.871 |
| coleman_liau | 9.80 |
| coleman_liau_drop | -1.75 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 2.31 |
| fkgl_drop | 4.39 |
| fre | 91.0 |
| fre_gain | 29.7 |
| human_edit_recall | 1.000 |
| length_ratio | 0.88 |
| n_words | 7.0 |
| nli_completeness | 0.139 |
| nli_faithfulness | 0.340 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 57.96 |
| smog | 3.13 |
| smog_drop | 8.08 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `hemostatic` -> `bleeding stopped` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Pressure was held and the bleeding stopped.

| metric | value |
|---|---:|
| bertscore_f1 | 0.871 |
| coleman_liau | 9.80 |
| coleman_liau_drop | -1.75 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 2.31 |
| fkgl_drop | 4.39 |
| fre | 91.0 |
| fre_gain | 29.7 |
| human_edit_recall | 1.000 |
| length_ratio | 0.88 |
| n_words | 7.0 |
| nli_completeness | 0.139 |
| nli_faithfulness | 0.340 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 57.96 |
| smog | 3.13 |
| smog_drop | 8.08 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `hemostatic` -> `bleeding stopped` | replace | attributed | 0.395 | 0.684 | - | 0.800 | 0.542 | - |

**edit `hemostatic` -> `bleeding stopped`**

- status: `attributed`
- log p full -0.6802, empty -1.0756
- masks scored: 6/6 (+1 top-k)
- ranked sources:
    - `+0.579` [readme] hemostatic: Stopping blood flow.
    - `+0.037` [readme] hemostatic: Hemostatic means stopping bleeding.

- rationale: The original term refers to the process of stopping blood flow, so "bleeding stopped" conveys that same physical outcome in plain language. Phrase frequency rises from Zipf 1.73 to 4.01, while syllable count remains constant at 3. Patients can now grasp the immediate result of the procedure without needing specialized medical vocabulary.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

==============================================================================

## Note 97 - `701`

**ORIGINAL**  The area was lavaged with some saline and cleared.

**REFERENCE** The area was washed out with some salt water and cleared.

| | FKGL | FRE | SMOG | Coleman-Liau | words |
|---|---:|---:|---:|---:|---:|
| ORIGINAL | 3.65 | 84.90 | 8.84 | 7.33 | 9 |
| REFERENCE | 3.72 | 88.00 | 8.84 | 5.76 | 11 |

### Stage 2 - extraction + classification

| term | kind | category | action | Zipf | AoA | syll |
|---|---|---|---|---:|---:|---:|
| `lavaged` | word | general_hard_word | replace | 0.0 | None | 1 |
| `saline` | word | medical_essential | elaborate | 3.33 | 11.71 | 2 |

### Stage 3 - retrieval

coverage **1.0** (2/2), glossary budget 5/16

| term | Zipf stratum | defs | sources | matched via | origin |
|---|---|---:|---|---|---|
| `lavaged` | very_rare | 1 | readme_lay_vocab.jsonl | exact | extracted |
| `saline` | rare | 4 | nih.json, readme_lay_vocab.jsonl, wiktionary.json | exact | extracted |

Glossary shown to the model:

1. `[readme]` lavaged: To clean out an organ or wound with fluid.
2. `[readme]` saline: A solution made of saltwater that matches the body's fluid concentration and can be used to replace lost fluids.
3. `[readme]` Saline: Salt water solution used to replace body fluids.
4. `[nih]` saline: A solution of salt and water.
5. `[wiktionary]` saline: If something is saline it is salty, especially water containing salt.

### Stage 4 - arm `naive`

**output:** The area was washed with some salt water and cleared.

| metric | value |
|---|---:|
| bertscore_f1 | 0.929 |
| coleman_liau | 6.18 |
| coleman_liau_drop | 1.15 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 3.65 |
| fkgl_drop | 0.00 |
| fre | 86.7 |
| fre_gain | 1.8 |
| human_edit_recall | 1.000 |
| length_ratio | 0.91 |
| n_words | 10.0 |
| nli_completeness | 0.985 |
| nli_faithfulness | 0.989 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 81.54 |
| smog | 8.84 |
| smog_drop | 0.00 |

### Stage 4 - arm `termonly`

**output:** The area was flushed with salt water and cleared.

| metric | value |
|---|---:|
| bertscore_f1 | 0.814 |
| coleman_liau | 6.69 |
| coleman_liau_drop | 0.64 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 3.65 |
| fkgl_drop | 0.00 |
| fre | 84.9 |
| fre_gain | 0.0 |
| human_edit_recall | 1.000 |
| length_ratio | 0.82 |
| n_words | 9.0 |
| nli_completeness | 0.978 |
| nli_faithfulness | 0.963 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 63.42 |
| smog | 8.84 |
| smog_drop | 0.00 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `lavaged` -> `flushed` | replace | - | - | - | - | - | - | - |
| `saline` -> `salt water` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** The area was cleaned with saltwater and cleared.

| metric | value |
|---|---:|
| bertscore_f1 | 0.800 |
| coleman_liau | 9.50 |
| coleman_liau_drop | -2.17 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 5.23 |
| fkgl_drop | -1.58 |
| fre | 71.8 |
| fre_gain | -13.1 |
| human_edit_recall | 1.000 |
| length_ratio | 0.73 |
| n_words | 8.0 |
| nli_completeness | 0.983 |
| nli_faithfulness | 0.987 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 52.06 |
| smog | 11.21 |
| smog_drop | -2.37 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `lavaged` -> `cleaned` | replace | attributed | 1.474 | 2.165 | - | 0.902 | 1.970 | - |
| `saline` -> `saltwater` | replace | attributed | 3.401 | 4.170 | - | 0.946 | 3.972 | - |

**edit `lavaged` -> `cleaned`**

- status: `attributed`
- log p full -0.5733, empty -2.0474
- masks scored: 34/34 (+4 top-k)
- ranked sources:
    - `+2.065` [readme] lavaged: To clean out an organ or wound with fluid.
    - `+0.096` [nih] saline: A solution of salt and water.
    - `+0.016` [readme] Saline: Salt water solution used to replace body fluids.
    - `+0.005` [readme] saline: A solution made of saltwater that matches the body's fluid concentration and can be used to replace lo
    - `-0.076` [wiktionary] saline: If something is saline it is salty, especially water containing salt.

- rationale: The original term "lavaged" refers to the process of flushing out a body cavity with fluid to remove debris, which "cleaned" conveys simply as making something free of dirt or waste. Phrase frequency rises from 0.00 to 4.02, while syllable count remains steady at 1. Patients can now grasp the intent of the procedure without needing specialized medical vocabulary.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `saline` -> `saltwater`**

- status: `attributed`
- log p full -0.6070, empty -4.0082
- masks scored: 34/34 (+4 top-k)
- ranked sources:
    - `+4.413` [readme] saline: A solution made of saltwater that matches the body's fluid concentration and can be used to replace lo
    - `+0.441` [readme] lavaged: To clean out an organ or wound with fluid.
    - `+0.239` [nih] saline: A solution of salt and water.
    - `-0.062` [wiktionary] saline: If something is saline it is salty, especially water containing salt.
    - `-1.402` [readme] Saline: Salt water solution used to replace body fluids.

- rationale: The original term refers to a clear liquid made of salt and water, so "saltwater" keeps that basic composition in plain language. Phrase frequency increases from 3.33 to 3.04, while age of acquisition falls from 11.71 to 9.39. Patients can now recognize the fluid as a simple mixture without needing to know the medical name.
- audit: coverage 1.0, grounding_error=True, omission=False, source_ok=True, passage_ok=True

==============================================================================

## Note 98 - `826`

**ORIGINAL**  Pain and inability to ambulate brought him in.

**REFERENCE** Pain and inability to move around brought him in.

| | FKGL | FRE | SMOG | Coleman-Liau | words |
|---|---:|---:|---:|---:|---:|
| ORIGINAL | 8.18 | 50.67 | 11.21 | 8.05 | 8 |
| REFERENCE | 6.28 | 66.10 | 8.84 | 6.69 | 9 |

### Stage 2 - extraction + classification

| term | kind | category | action | Zipf | AoA | syll |
|---|---|---|---|---:|---:|---:|
| `inability to ambulate` | phrase | general_hard_word | replace | 1.4 | 10.67 | 9 |
| `inability` | word | medical_descriptor | replace | - | - | - |
| `to` | word | medical_descriptor | replace | - | - | - |
| `ambulate` | word | medical_descriptor | replace | - | - | - |

### Stage 3 - retrieval

coverage **0.0** (0/1), glossary budget 8/16

| term | Zipf stratum | defs | sources | matched via | origin |
|---|---|---:|---|---|---|
| `inability to ambulate` | very_rare | 0 | - | - | extracted |
| `inability` | uncommon | 2 | michigan_plmd.json, wiktionary.json | exact | split_from_uncovered |
| `to` | common | 2 | wiktionary.json | exact | split_from_uncovered |
| `ambulate` | very_rare | 4 | justplainclear.json, michigan_plmd.json, readme_lay_vocab.jsonl, wiktionary.json | exact | split_from_uncovered |

Glossary shown to the model:

1. `[michigan]` inability: Not able to.
2. `[wiktionary]` to: To has no meaning. It is used with a bare infinitival clause.
3. `[readme]` ambulate: To ambulate means to walk or move around.
4. `[wiktionary]` inability: An inability is something that you can not do.
5. `[wiktionary]` to: To shows where something goes, the goal of movement.
6. `[michigan]` ambulate: To walk or move around.
7. `[justplainclear]` ambulate: Walk, move around
8. `[wiktionary]` ambulate: If you ambulate yourself, you relocate yourself under the power of your own legs.

### Stage 4 - arm `naive`

**output:** Pain and the inability to walk brought him in.

| metric | value |
|---|---:|
| bertscore_f1 | 0.792 |
| coleman_liau | 4.76 |
| coleman_liau_drop | 3.29 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 4.96 |
| fkgl_drop | 3.22 |
| fre | 75.5 |
| fre_gain | 24.8 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 9.0 |
| nli_completeness | 0.971 |
| nli_faithfulness | 0.990 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 45.46 |
| smog | 8.84 |
| smog_drop | 2.37 |

### Stage 4 - arm `termonly`

**output:** Pain and inability to walk brought him in.

| metric | value |
|---|---:|
| bertscore_f1 | 0.815 |
| coleman_liau | 5.15 |
| coleman_liau_drop | 2.90 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 5.23 |
| fkgl_drop | 2.95 |
| fre | 71.8 |
| fre_gain | 21.1 |
| human_edit_recall | 1.000 |
| length_ratio | 0.89 |
| n_words | 8.0 |
| nli_completeness | 0.969 |
| nli_faithfulness | 0.989 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 66.67 |
| smog | 8.84 |
| smog_drop | 2.37 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `inability to ambulate` -> `inability to walk` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Pain and not being able to walk brought him in.

| metric | value |
|---|---:|
| bertscore_f1 | 0.718 |
| coleman_liau | 2.70 |
| coleman_liau_drop | 5.35 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.667 |
| fkgl | 2.47 |
| fkgl_drop | 5.71 |
| fre | 95.2 |
| fre_gain | 44.5 |
| human_edit_recall | 1.000 |
| length_ratio | 1.11 |
| n_words | 10.0 |
| nli_completeness | 0.981 |
| nli_faithfulness | 0.992 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 38.11 |
| smog | 3.13 |
| smog_drop | 8.08 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `inability to ambulate` -> `not being able to walk` | replace | attributed | -0.114 | -0.147 | 0.716 | 0.892 | 0.314 | - |

**edit `inability to ambulate` -> `not being able to walk`**

- status: `attributed`
- log p full -1.5559, empty -1.4418
- masks scored: 66/66 (+2 top-k)
- ranked sources:
    - `+0.603` [michigan] inability: Not able to.
    - `+0.289` [wiktionary] inability: An inability is something that you can not do.

- rationale: The original phrase describes a total loss of walking ability, so "not being able to walk" conveys that same physical limitation in everyday language. Phrase frequency rises from 1.40 to 4.87, while age of acquisition drops from 10.67 to 7.79. Patients can now grasp the mobility issue immediately without needing to know the clinical jargon.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

==============================================================================

## Note 99 - `751`

**ORIGINAL**  There is a hernia on the left side.

**REFERENCE** The gut sticks out through the abdomen wall on the left side.

| | FKGL | FRE | SMOG | Coleman-Liau | words |
|---|---:|---:|---:|---:|---:|
| ORIGINAL | 2.28 | 92.97 | 8.84 | 0.07 | 8 |
| REFERENCE | 2.86 | 95.95 | 8.84 | 5.42 | 12 |

### Stage 2 - extraction + classification

| term | kind | category | action | Zipf | AoA | syll |
|---|---|---|---|---:|---:|---:|
| `hernia` | word | medical_essential | elaborate | 3.0 | 12.29 | 3 |

### Stage 3 - retrieval

coverage **1.0** (1/1), glossary budget 3/16

| term | Zipf stratum | defs | sources | matched via | origin |
|---|---|---:|---|---|---|
| `hernia` | rare | 3 | justplainclear.json, nih.json, readme_lay_vocab.jsonl | exact | extracted |

Glossary shown to the model:

1. `[readme]` hernia: A hernia is when an organ pokes through a hole in a muscle.
2. `[nih]` hernia: The bulging of an internal organ through a weak area or tear in the muscle or other tissue that holds it in place. Most hernias occur in the abdomen.
3. `[justplainclear]` hernia: When part of an organ or tissue inside of you bulges through a weak area of muscle. Most hernias are in the stomach area.

### Stage 4 - arm `naive`

**output:** There is a hernia on the left side.

| metric | value |
|---|---:|
| bertscore_f1 | 0.350 |
| coleman_liau | 0.07 |
| coleman_liau_drop | 0.00 |
| copy_jargon_rate | 1.000 |
| critical_error | 0.000 |
| fkgl | 2.28 |
| fkgl_drop | 0.00 |
| fre | 93.0 |
| fre_gain | 0.0 |
| human_edit_recall | 0.000 |
| laterality_preservation | 1.000 |
| length_ratio | 0.67 |
| n_words | 8.0 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.994 |
| replacement_f1 | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 17.50 |
| smog | 8.84 |
| smog_drop | 0.00 |

### Stage 4 - arm `termonly`

**output:** There is a bulge on the left side.

| metric | value |
|---|---:|
| bertscore_f1 | 0.406 |
| coleman_liau | -0.65 |
| coleman_liau_drop | 0.72 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | -0.67 |
| fkgl_drop | 2.95 |
| fre | 114.1 |
| fre_gain | 21.1 |
| human_edit_recall | 1.000 |
| laterality_preservation | 1.000 |
| length_ratio | 0.67 |
| n_words | 8.0 |
| nli_completeness | 0.064 |
| nli_faithfulness | 0.746 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 60.64 |
| smog | 3.13 |
| smog_drop | 5.71 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `hernia` -> `bulge` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** There is a bulge on the left side.

| metric | value |
|---|---:|
| bertscore_f1 | 0.406 |
| coleman_liau | -0.65 |
| coleman_liau_drop | 0.72 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | -0.67 |
| fkgl_drop | 2.95 |
| fre | 114.1 |
| fre_gain | 21.1 |
| human_edit_recall | 1.000 |
| laterality_preservation | 1.000 |
| length_ratio | 0.67 |
| n_words | 8.0 |
| nli_completeness | 0.064 |
| nli_faithfulness | 0.746 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 60.64 |
| smog | 3.13 |
| smog_drop | 5.71 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `hernia` -> `bulge` | replace | attributed | 0.043 | 0.307 | - | 0.830 | 0.870 | - |

**edit `hernia` -> `bulge`**

- status: `attributed`
- log p full -0.1305, empty -0.1735
- masks scored: 10/10 (+2 top-k)
- ranked sources:
    - `+0.870` [justplainclear] hernia: When part of an organ or tissue inside of you bulges through a weak area of muscle. Most hernias are i
    - `-0.179` [readme] hernia: A hernia is when an organ pokes through a hole in a muscle.

- rationale: The original term refers to a protrusion of tissue through a weak spot in the body wall, so "bulge" captures this visible swelling in simple language. Phrase frequency rises from 3.00 to 3.24, and age of acquisition drops from 12.29 to 8.10. Patients can now recognize the physical sign without needing to know the specific medical condition.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

==============================================================================

## Note 100 - `496`

**ORIGINAL**  Other systems were reviewed and were found to be unremarkable.

**REFERENCE** Other systems were reviewed and were found to be normal.

| | FKGL | FRE | SMOG | Coleman-Liau | words |
|---|---:|---:|---:|---:|---:|
| ORIGINAL | 8.37 | 52.87 | 8.84 | 11.40 | 10 |
| REFERENCE | 4.83 | 78.25 | 3.13 | 7.92 | 10 |

### Stage 2 - extraction + classification

| term | kind | category | action | Zipf | AoA | syll |
|---|---|---|---|---:|---:|---:|
| `unremarkable` | word | medical_descriptor | replace | 2.83 | 11.06 | 5 |

### Stage 3 - retrieval

coverage **1.0** (1/1), glossary budget 1/16

| term | Zipf stratum | defs | sources | matched via | origin |
|---|---|---:|---|---|---|
| `unremarkable` | rare | 1 | wiktionary.json | exact | extracted |

Glossary shown to the model:

1. `[wiktionary]` unremarkable: If something is unremarkable, it is common and ordinary.

### Stage 4 - arm `naive`

**output:** The rest of the patient's body was checked and found to be normal.

| metric | value |
|---|---:|
| bertscore_f1 | 0.544 |
| coleman_liau | 5.12 |
| coleman_liau_drop | 6.28 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 4.00 |
| fkgl_drop | 4.37 |
| fre | 89.5 |
| fre_gain | 36.6 |
| human_edit_recall | 1.000 |
| length_ratio | 1.40 |
| n_words | 14.0 |
| negation_preservation | 0.000 |
| nli_completeness | 0.355 |
| nli_faithfulness | 0.098 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.750 |
| sari | 21.34 |
| smog | 3.13 |
| smog_drop | 5.71 |

### Stage 4 - arm `termonly`

**output:** Other systems were checked and found to be normal.

| metric | value |
|---|---:|
| bertscore_f1 | 0.885 |
| coleman_liau | 7.33 |
| coleman_liau_drop | 4.07 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 3.65 |
| fkgl_drop | 4.72 |
| fre | 84.9 |
| fre_gain | 32.0 |
| human_edit_recall | 1.000 |
| length_ratio | 0.90 |
| n_words | 9.0 |
| negation_preservation | 0.000 |
| nli_completeness | 0.982 |
| nli_faithfulness | 0.993 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 39.50 |
| smog | 3.13 |
| smog_drop | 5.71 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `unremarkable` -> `normal` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Other systems were reviewed and found to be normal.

| metric | value |
|---|---:|
| bertscore_f1 | 0.958 |
| coleman_liau | 7.98 |
| coleman_liau_drop | 3.42 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 4.96 |
| fkgl_drop | 3.41 |
| fre | 75.5 |
| fre_gain | 22.6 |
| human_edit_recall | 1.000 |
| length_ratio | 0.90 |
| n_words | 9.0 |
| negation_preservation | 0.000 |
| nli_completeness | 0.973 |
| nli_faithfulness | 0.993 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 61.95 |
| smog | 3.13 |
| smog_drop | 5.71 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `unremarkable` -> `normal` | replace | attributed | -0.025 | -0.411 | - | - | - | - |

**edit `unremarkable` -> `normal`**

- status: `attributed`
- log p full -0.0775, empty -0.0521
- masks scored: 4/4 (+1 top-k)
- ranked sources:
    - `-0.391` [wiktionary] unremarkable: If something is unremarkable, it is common and ordinary.

- rationale: The original term "unremarkable" means showing no special features or being ordinary, so "normal" conveys that standard state in plain words. Phrase frequency rises from Zipf 2.83 to 5.01, while age of acquisition drops from 11.06 to 5.53. Readers can now recognize that the medical finding is standard without needing to parse a complex adjective.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True
