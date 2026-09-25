# Step-by-step detail - qwen3p7-plus (`run100_20260815_222318`)

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

**output:** He lost interest in things he used to enjoy and stopped wanting to spend time with others. He also had trouble sleeping because he kept waking up and felt restless.

| metric | value |
|---|---:|
| bertscore_f1 | 0.481 |
| coleman_liau | 7.94 |
| coleman_liau_drop | 11.02 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 5.99 |
| fkgl_drop | 10.03 |
| fre | 78.8 |
| fre_gain | 68.4 |
| human_edit_recall | 1.000 |
| length_ratio | 1.50 |
| n_words | 30.0 |
| nli_completeness | 0.024 |
| nli_faithfulness | 0.988 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.750 |
| sari | 11.45 |
| smog | 3.13 |
| smog_drop | 12.77 |

### Stage 4 - arm `termonly`

**output:** He lost interest in things and did not care about social activities, and had trouble sleeping because he woke up often and felt restless.

| metric | value |
|---|---:|
| bertscore_f1 | 0.592 |
| coleman_liau | 10.03 |
| coleman_liau_drop | 8.93 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 10.98 |
| fkgl_drop | 5.05 |
| fre | 59.1 |
| fre_gain | 48.7 |
| human_edit_recall | 1.000 |
| length_ratio | 1.20 |
| n_words | 24.0 |
| nli_completeness | 0.988 |
| nli_faithfulness | 0.994 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.714 |
| sari | 18.88 |
| smog | 8.84 |
| smog_drop | 7.06 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `anhedonic` -> `lost interest in things` | replace | - | - | - | - | - | - | - |
| `disinterested` -> `did not care` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** He lost interest in things and did not care about social activities, and had trouble sleeping because he woke up often and felt restless.

| metric | value |
|---|---:|
| bertscore_f1 | 0.592 |
| coleman_liau | 10.03 |
| coleman_liau_drop | 8.93 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 10.98 |
| fkgl_drop | 5.05 |
| fre | 59.1 |
| fre_gain | 48.7 |
| human_edit_recall | 1.000 |
| length_ratio | 1.20 |
| n_words | 24.0 |
| nli_completeness | 0.988 |
| nli_faithfulness | 0.994 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.714 |
| sari | 18.88 |
| smog | 8.84 |
| smog_drop | 7.06 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `anhedonic` -> `lost interest in things` | replace | attributed | -0.602 | -0.670 | - | 0.800 | 0.821 | - |
| `disinterested` -> `did not care` | replace | attributed | -0.322 | -0.389 | - | 0.894 | 0.335 | - |

**edit `anhedonic` -> `lost interest in things`**

- status: `attributed`
- log p full -2.6118, empty -2.0098
- masks scored: 6/6 (+1 top-k)
- ranked sources:
    - `+0.075` [wiktionary] disinterested: If someone is disinterested, they are not affected by a situation, so they can make fair decisi
    - `-0.745` [wiktionary] disinterested: If someone is disinterested, they are not interested in something; they find it boring.

- rationale: "Anhedonic" means an inability to feel pleasure, so "lost interest in things" conveys that same emotional flatness in everyday language. Word frequency rises from Zipf 1.11 to 4.90, making the phrase far more common, though syllable count increases from 4 to 5. Readers can grasp the core symptom of diminished enjoyment without needing to decode a specialized psychological term.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `disinterested` -> `did not care`**

- status: `attributed`
- log p full -1.9298, empty -1.6076
- masks scored: 6/6 (+1 top-k)
- ranked sources:
    - `-0.335` [wiktionary] disinterested: If someone is disinterested, they are not interested in something; they find it boring.

- rationale: "Disinterested" means lacking interest or concern, so "did not care" conveys that same lack of engagement in everyday language. Phrase frequency rises from Zipf 2.91 to 5.39, age of acquisition drops from 12.40 to 5.65, and syllable count decreases from 4 to 3. Readers can immediately grasp the person's indifference without stumbling over a formal term.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

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

**output:** It is possible that the patient had a heart attack.

| metric | value |
|---|---:|
| bertscore_f1 | 0.372 |
| coleman_liau | 5.02 |
| coleman_liau_drop | 9.05 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.167 |
| diagnostic_identity_preservation | 1.000 |
| fkgl | 4.83 |
| fkgl_drop | 9.45 |
| fre | 78.2 |
| fre_gain | 74.9 |
| human_edit_recall | 1.000 |
| length_ratio | 1.67 |
| n_words | 10.0 |
| negation_preservation | 0.000 |
| nli_completeness | 0.504 |
| nli_faithfulness | 0.859 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 20.13 |
| smog | 8.84 |
| smog_drop | 4.18 |
| uncertainty_preservation | 1.000 |

### Stage 4 - arm `termonly`

**output:** A heart attack is still possible.

| metric | value |
|---|---:|
| bertscore_f1 | 0.548 |
| coleman_liau | 5.37 |
| coleman_liau_drop | 8.70 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.167 |
| diagnostic_identity_preservation | 1.000 |
| fkgl | 4.45 |
| fkgl_drop | 9.83 |
| fre | 73.8 |
| fre_gain | 70.5 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 6.0 |
| negation_preservation | 0.000 |
| nli_completeness | 0.868 |
| nli_faithfulness | 0.807 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 22.38 |
| smog | 8.84 |
| smog_drop | 4.18 |
| uncertainty_preservation | 1.000 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `Myocardial infarction` -> `heart attack` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** A heart attack is still possible.

| metric | value |
|---|---:|
| bertscore_f1 | 0.548 |
| coleman_liau | 5.37 |
| coleman_liau_drop | 8.70 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.167 |
| diagnostic_identity_preservation | 1.000 |
| fkgl | 4.45 |
| fkgl_drop | 9.83 |
| fre | 73.8 |
| fre_gain | 70.5 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 6.0 |
| negation_preservation | 0.000 |
| nli_completeness | 0.868 |
| nli_faithfulness | 0.807 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 22.38 |
| smog | 8.84 |
| smog_drop | 4.18 |
| uncertainty_preservation | 1.000 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `Myocardial infarction` -> `heart attack` | replace | attributed | 0.005 | 2.613 | 0.656 | 0.784 | 0.002 | - |

**edit `Myocardial infarction` -> `heart attack`**

- status: `attributed`
- log p full -0.0004, empty -0.0055
- masks scored: 66/66 (+2 top-k)
- ranked sources:
    - `+0.387` [wiktionary] can: If someone can do something, they are allowed to do it.
    - `+0.384` [justplainclear] myocardial infarction: A heart attack
    - `+0.368` [wiktionary] can: If someone can do something, they are able to do it.
    - `+0.209` [wiktionary] excluded: If you exclude someone or something, you keep them out.
    - `+0.205` [iowa] MYOCARDIAL INFARCTION: heart attack

- rationale: "Myocardial infarction" refers to the death of heart muscle tissue due to blocked blood flow, which "heart attack" conveys in everyday language. Phrase frequency rises from Zipf 2.58 to 4.89, and age of acquisition drops from 16.64 to 6.58. Readers can immediately recognize the urgent cardiac event without needing specialized medical training.
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

**output:** There was a large bruise and swelling inside the subdeltoid bursa.

| metric | value |
|---|---:|
| bertscore_f1 | 0.485 |
| coleman_liau | 10.51 |
| coleman_liau_drop | 3.79 |
| copy_jargon_rate | 0.500 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 5.86 |
| fkgl_drop | 0.15 |
| fre | 72.6 |
| fre_gain | 2.8 |
| human_edit_recall | 0.500 |
| length_ratio | 0.79 |
| n_words | 11.0 |
| nli_completeness | 0.981 |
| nli_faithfulness | 0.981 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 34.23 |
| severity_downgrade | 0.000 |
| severity_preservation | 1.000 |
| severity_tier_input | 2.000 |
| severity_tier_output | 2.000 |
| smog | 8.84 |
| smog_drop | 0.00 |

### Stage 4 - arm `termonly`

**output:** There was a large bruise and swelling under the shoulder pad.

| metric | value |
|---|---:|
| bertscore_f1 | 0.603 |
| coleman_liau | 7.87 |
| coleman_liau_drop | 6.43 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 3.72 |
| fkgl_drop | 2.29 |
| fre | 88.0 |
| fre_gain | 18.2 |
| human_edit_recall | 1.000 |
| length_ratio | 0.79 |
| n_words | 11.0 |
| nli_completeness | 0.710 |
| nli_faithfulness | 0.456 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.200 |
| sari | 41.51 |
| severity_downgrade | 0.000 |
| severity_preservation | 1.000 |
| severity_tier_input | 2.000 |
| severity_tier_output | 2.000 |
| smog | 3.13 |
| smog_drop | 5.71 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `marked` -> `large` | replace | - | - | - | - | - | - | - |
| `hematoma` -> `bruise` | replace | - | - | - | - | - | - | - |
| `subdeltoid bursa` -> `under the shoulder pad` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** There was a large bruise and swelling in the fluid sac under the shoulder muscle.

| metric | value |
|---|---:|
| bertscore_f1 | 0.560 |
| coleman_liau | 7.75 |
| coleman_liau_drop | 6.55 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 5.99 |
| fkgl_drop | 0.02 |
| fre | 78.8 |
| fre_gain | 9.0 |
| human_edit_recall | 1.000 |
| length_ratio | 1.07 |
| n_words | 15.0 |
| nli_completeness | 0.871 |
| nli_faithfulness | 0.785 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.200 |
| sari | 41.05 |
| severity_downgrade | 0.000 |
| severity_preservation | 1.000 |
| severity_tier_input | 2.000 |
| severity_tier_output | 2.000 |
| smog | 3.13 |
| smog_drop | 5.71 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `marked` -> `large` | replace | attributed | -0.256 | -0.615 | 0.949 | 0.968 | 0.365 | - |
| `hematoma` -> `bruise` | replace | attributed | 0.146 | 0.904 | 0.891 | 0.951 | 1.300 | - |
| `subdeltoid bursa` -> `fluid sac under the shoulder muscle` | replace | attributed | 1.391 | 1.560 | 0.451 | 0.830 | 0.044 | - |

**edit `marked` -> `large`**

- status: `attributed`
- log p full -0.6758, empty -0.4199
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+0.510` [nih] hematoma: A pool of clotted or partially clotted blood in an organ, tissue, or body space, usually caused by a
    - `+0.145` [justplainclear] hematoma: A collection of blood under the skin or in the body that is typically caused by a broken blood vesse
    - `+0.012` [justplainclear] bursa: A small sac (pouch) found in your body which is filled with fluid. Bursa help your tendons or muscles m
    - `-0.043` [wiktionary] marked: A mark is a single line left by a pen or pencil, or any small bit of color that got onto something.

- rationale: "Marked" means clearly noticeable or significant, so "large" conveys that same sense of size or extent in everyday language. Word frequency increases from Zipf 4.50 to 5.39, while the syllable count remains at 1. Readers can grasp the extent of the finding without needing to interpret a formal descriptor.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `hematoma` -> `bruise`**

- status: `attributed`
- log p full -0.1135, empty -0.2599
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+2.154` [iowa] HEMATOMA: a bruise, a black and blue mark
    - `+0.853` [michigan] hematoma: A bruise or when your skin is black and blue after an injury.
    - `+0.488` [readme] bursa: A small sac of fluid that cushions joints as they move.
    - `-0.017` [wiktionary] marked: A mark is a single line left by a pen or pencil, or any small bit of color that got onto something.

- rationale: A hematoma is a collection of blood outside the blood vessels, and "bruise" conveys this idea in everyday language. Phrase frequency increases from Zipf 2.61 to 3.18, while age of acquisition falls from 14.78 to 5.45. Readers can grasp the nature of the injury without needing specialized medical vocabulary.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `subdeltoid bursa` -> `fluid sac under the shoulder muscle`**

- status: `attributed`
- log p full -1.6254, empty -3.0165
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+0.752` [justplainclear] bursa: A small sac (pouch) found in your body which is filled with fluid. Bursa help your tendons or muscles m
    - `+0.708` [readme] bursa: A small sac of fluid that cushions joints as they move.
    - `+0.116` [wiktionary] marked: A mark is a single line left by a pen or pencil, or any small bit of color that got onto something.
    - `+0.104` [michigan] hematoma: A bruise or when your skin is black and blue after an injury.

- rationale: A subdeltoid bursa is a small, fluid-filled sac that reduces friction under the shoulder muscle, so the replacement phrase describes this structure in everyday language. Phrase frequency rises from Zipf 0.00 to 3.46, and age of acquisition drops from 15.78 to 9.00, making the concept significantly more accessible. Readers can grasp the location and purpose of this cushioning tissue without needing specialized anatomical vocabulary.
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
| `hypertension` -> `high blood pressure` | replace | attributed | 0.001 | 1.134 | 0.532 | 0.647 | 0.017 | - |
| `hyperlipidemia` -> `high cholesterol` | replace | attributed | 0.359 | 1.429 | 0.819 | 0.934 | 3.886 | - |

**edit `hypertension` -> `high blood pressure`**

- status: `attributed`
- log p full -0.0007, empty -0.0020
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.066` [michigan] hypertension: When your low pressure (diastolic) is 90 or higher or the high pressure (systolic) is 140 or hig
    - `+0.049` [nih] hypertension: A blood pressure of 140/90 or higher. Hypertension usually has no symptoms. It can harm the arte
    - `+0.046` [justplainclear] hypertension: Also known as: high blood pressure, HBP A condition of having high blood pressure for a long per
    - `+0.046` [readme] HYPERTENSION: High blood pressure: when the force of blood in your arteries is too high.
    - `+0.044` [readme] hypertension: High blood pressure is when the force of blood in the arteries is too high.

- rationale: Hypertension refers to elevated pressure within the arteries, a concept directly conveyed by the plain-language phrase "high blood pressure." Word frequency rises from Zipf 3.41 to 4.71, and age of acquisition drops from 16.28 to 8.95, indicating the replacement is both more common and learned earlier. This allows patients to immediately grasp the nature of their condition without needing to interpret specialized medical terminology.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `hyperlipidemia` -> `high cholesterol`**

- status: `attributed`
- log p full -0.1464, empty -0.5056
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+4.075` [justplainclear] hyperlipidemia: High cholesterol
    - `+0.189` [michigan] hyperlipidemia: High levels of fat or fat-like substances (cholesterol). Hyperlipidemia is also called high ch
    - `+0.080` [justplainclear] hypertension: Also known as: high blood pressure, HBP A condition of having high blood pressure for a long per
    - `+0.077` [readme] hypertension: High blood pressure is when the force of blood in the arteries is too high.

- rationale: Hyperlipidemia refers to elevated levels of fats in the blood, so "high cholesterol" conveys this concept using a more familiar term. Word frequency increases from Zipf 1.95 to 3.72, indicating the replacement is more common, though syllable count rises from 4 to 5. Patients can grasp the issue of excess blood fats without needing to interpret specialized medical terminology.
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

**output:** She said she had bladder spasms when she urinated and mentioned that she has a history of chronic UTIs.

| metric | value |
|---|---:|
| bertscore_f1 | 0.750 |
| coleman_liau | 8.28 |
| coleman_liau_drop | -1.47 |
| copy_jargon_rate | 1.000 |
| critical_error | 0.000 |
| fkgl | 8.59 |
| fkgl_drop | 0.31 |
| fre | 67.3 |
| fre_gain | -1.4 |
| human_edit_recall | 0.000 |
| length_ratio | 0.83 |
| n_words | 19.0 |
| nli_completeness | 0.995 |
| nli_faithfulness | 0.995 |
| replacement_f1 | 0.000 |
| rewrite_aggressiveness | 1.000 |
| sari | 23.08 |
| smog | 11.21 |
| smog_drop | 0.00 |
| temporality_preservation | 1.000 |

### Stage 4 - arm `termonly`

**output:** She complained of bladder cramps when she peed and said she has a history of long-lasting urine infections.

| metric | value |
|---|---:|
| bertscore_f1 | 0.704 |
| coleman_liau | 10.91 |
| coleman_liau_drop | -4.09 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 9.13 |
| fkgl_drop | -0.23 |
| fre | 61.7 |
| fre_gain | -7.0 |
| human_edit_recall | 1.000 |
| length_ratio | 0.83 |
| n_words | 19.0 |
| nli_completeness | 0.993 |
| nli_faithfulness | 0.994 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.429 |
| sari | 18.32 |
| smog | 13.02 |
| smog_drop | -1.82 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `bladder spasms` -> `bladder cramps` | replace | - | - | - | - | - | - | - |
| `urinated` -> `peed` | replace | - | - | - | - | - | - | - |
| `chronic UTIs` -> `long-lasting urine infections` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** She said her bladder muscles tightened and hurt when she peed, and she has a history of long-lasting urinary infections.

| metric | value |
|---|---:|
| bertscore_f1 | 0.576 |
| coleman_liau | 11.14 |
| coleman_liau_drop | -4.32 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.667 |
| fkgl | 11.09 |
| fkgl_drop | -2.19 |
| fre | 51.2 |
| fre_gain | -17.5 |
| human_edit_recall | 1.000 |
| length_ratio | 0.91 |
| n_words | 21.0 |
| nli_completeness | 0.995 |
| nli_faithfulness | 0.994 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.429 |
| sari | 19.21 |
| smog | 14.55 |
| smog_drop | -3.35 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `bladder spasms` -> `bladder muscles tightened and hurt` | replace | attributed | 9.196 | 9.432 | 0.942 | 0.950 | 9.938 | - |
| `urinated` -> `peed` | replace | attributed | 0.299 | 0.903 | 0.682 | 0.922 | 0.029 | - |
| `chronic UTIs` -> `long-lasting urinary infections` | replace | attributed | 2.493 | 2.783 | 0.875 | 0.953 | 0.922 | - |

**edit `bladder spasms` -> `bladder muscles tightened and hurt`**

- status: `attributed`
- log p full -1.5604, empty -10.7568
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+10.220` [readme] spasms: When your muscles suddenly tighten up and hurt.
    - `+0.282` [wiktionary] urinated: When a person or animal urinates, it passes urine to empty the bladder.
    - `+0.227` [dorland] UTIs: urinary tract infections
    - `+0.096` [iowa] CHRONIC: continuing for a long time, ongoing

- rationale: The glossary defines bladder spasms as muscles suddenly tightening and hurting, so the replacement conveys this sensation in everyday language. Word frequency rises from Zipf 2.89 to 3.08, while age of acquisition remains unchanged at 10.78. Readers can grasp the physical discomfort without needing to interpret the clinical term.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `urinated` -> `peed`**

- status: `attributed`
- log p full -0.2716, empty -0.5706
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+0.397` [readme] bladder: A bladder is a sac in your body that holds pee.
    - `+0.369` [readme] BLADDER: Bladder: Holds pee in your body.
    - `+0.329` [readme] Chronic: A long-lasting or recurring health issue.
    - `+0.158` [wiktionary] bladder: The bladder is the internal organ where urine collects.
    - `+0.117` [michigan] bladder: A hollow organ that stores pee (urine).

- rationale: "Urinated" means to pass urine from the body, and "peed" conveys this same action in everyday language. Word frequency increases from Zipf 2.31 to 3.10, and the word becomes shorter, dropping from 3 syllables to 1. Readers can immediately grasp the bodily function without encountering formal medical terminology.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `chronic UTIs` -> `long-lasting urinary infections`**

- status: `attributed`
- log p full -1.3157, empty -3.8086
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+1.940` [readme] UTIs: UTIs are infections in the urinary system.
    - `+1.018` [readme] Chronic: A long-lasting or recurring health issue.
    - `+0.566` [michigan] chronic: Something, like a disease or symptom, that lasts for a long time.
    - `+0.273` [readme] spasms: When your muscles suddenly tighten up and hurt.
    - `+0.118` [iowa] CHRONIC: continuing for a long time, ongoing

- rationale: The glossary defines UTIs as infections in the urinary system, so "long-lasting urinary infections" preserves this meaning in everyday language. Phrase frequency rises from Zipf 2.05 to 3.17, though age of acquisition increases from 11.25 to 12.56. Readers can grasp that these are persistent infections in the urinary tract without needing the medical abbreviation.
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

**output:** The knee was stable and had no swelling.

| metric | value |
|---|---:|
| bertscore_f1 | 0.590 |
| coleman_liau | 3.70 |
| coleman_liau_drop | 2.48 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 2.28 |
| fkgl_drop | 4.91 |
| fre | 93.0 |
| fre_gain | 31.6 |
| human_edit_recall | 1.000 |
| length_ratio | 0.73 |
| n_words | 8.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.992 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 13.62 |
| smog | 3.13 |
| smog_drop | 8.08 |

### Stage 4 - arm `termonly`

**output:** The knee was steady and had no swelling.

| metric | value |
|---|---:|
| bertscore_f1 | 0.570 |
| coleman_liau | 3.70 |
| coleman_liau_drop | 2.48 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 2.28 |
| fkgl_drop | 4.91 |
| fre | 93.0 |
| fre_gain | 31.6 |
| human_edit_recall | 1.000 |
| length_ratio | 0.73 |
| n_words | 8.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.993 |
| nli_faithfulness | 0.989 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 13.62 |
| smog | 3.13 |
| smog_drop | 8.08 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `instability` -> `steady` | replace | - | - | - | - | - | - | - |
| `effusion` -> `swelling` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** The knee was steady and had no fluid buildup.

| metric | value |
|---|---:|
| bertscore_f1 | 0.658 |
| coleman_liau | 4.11 |
| coleman_liau_drop | 2.07 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 3.65 |
| fkgl_drop | 3.54 |
| fre | 84.9 |
| fre_gain | 23.6 |
| human_edit_recall | 1.000 |
| length_ratio | 0.82 |
| n_words | 9.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.993 |
| nli_faithfulness | 0.993 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 18.25 |
| smog | 3.13 |
| smog_drop | 8.08 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `instability` -> `steady` | replace | attributed | 0.441 | 0.979 | - | 1.000 | 0.087 | - |
| `effusion` -> `fluid buildup` | replace | attributed | 0.651 | 0.866 | - | 0.894 | 1.234 | - |

**edit `instability` -> `steady`**

- status: `attributed`
- log p full -0.4062, empty -0.8477
- masks scored: 6/6 (+1 top-k)
- ranked sources:
    - `+0.369` [nih] effusion: An abnormal collection of fluid in hollow spaces or between tissues of the body. For example, a pleu
    - `+0.282` [wiktionary] instability: Instability is the condition of not being stable, which can make things uncertain or unsafe.

- rationale: "Instability" refers to a lack of steadiness or balance, so "steady" conveys the desired state of stability in simpler terms. Word frequency increases from Zipf 3.71 to 4.31, and age of acquisition decreases from 12.55 to 6.70. Readers can grasp the concept of maintaining balance without needing to interpret the abstract notion of instability.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `effusion` -> `fluid buildup`**

- status: `attributed`
- log p full -1.0986, empty -1.7500
- masks scored: 6/6 (+1 top-k)
- ranked sources:
    - `+1.234` [nih] effusion: An abnormal collection of fluid in hollow spaces or between tissues of the body. For example, a pleu

- rationale: "Effusion" refers to the escape of fluid into a body cavity, so "fluid buildup" conveys this accumulation in everyday terms. Phrase frequency increases from Zipf 2.41 to 3.31, and age of acquisition falls from 14.29 to 9.63. Readers can grasp that excess fluid is collecting in the body without needing specialized medical vocabulary.
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

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `resolved` -> `went away` | replace | - | - | - | - | - | - | - |
| `recurrence` -> `it come back` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

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

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `resolved` -> `went away` | replace | attributed | -0.017 | -0.145 | - | 0.422 | 0.050 | - |
| `recurrence` -> `it come back` | replace | attributed | 0.242 | 1.053 | - | 0.956 | 0.526 | - |

**edit `resolved` -> `went away`**

- status: `attributed`
- log p full -0.1338, empty -0.1167
- masks scored: 34/34 (+4 top-k)
- ranked sources:
    - `+0.050` [wiktionary] resolved: To resolve means to create a solution for a problem.
    - `-0.024` [wiktionary] recurrence: A recurrence is something that happens again.
    - `-0.172` [wiktionary] resolved: When a problem is resolved, it has been brought to a successful solution.

- rationale: "Resolved" means a condition has ended or cleared up, and "went away" conveys that same outcome in everyday language. Word frequency increases from Zipf 4.10 to 5.26, though syllable count rises from 2 to 3. Patients can clearly see that the health issue is no longer present.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `recurrence` -> `it come back`**

- status: `attributed`
- log p full -0.1588, empty -0.4010
- masks scored: 34/34 (+4 top-k)
- ranked sources:
    - `+1.010` [readme] recurrence: When a disease comes back after being treated.
    - `+0.483` [nih] recurrence: Cancer that has recurred (come back), usually after a period of time during which the cancer could
    - `-0.318` [wiktionary] recurrence: A recurrence is something that happens again.

- rationale: "Recurrence" means that a condition returns after a period of improvement, and "it come back" conveys this same idea in everyday language. Phrase frequency rises from Zipf 3.20 to 5.57, and age of acquisition drops from 11.79 to 5.31. Readers can grasp that the health issue has returned without needing to interpret a clinical term.
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

**output:** Description: Fever, middle ear infection, and possible severe infection.

| metric | value |
|---|---:|
| bertscore_f1 | 0.784 |
| coleman_liau | 19.58 |
| coleman_liau_drop | -3.15 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| diagnostic_identity_preservation | 1.000 |
| fkgl | 14.14 |
| fkgl_drop | -0.03 |
| fre | 9.7 |
| fre_gain | 3.3 |
| human_edit_recall | 1.000 |
| length_ratio | 1.12 |
| n_words | 9.0 |
| nli_completeness | 0.648 |
| nli_faithfulness | 0.675 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 61.87 |
| smog | 14.55 |
| smog_drop | -1.53 |
| uncertainty_preservation | 1.000 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `otitis media` -> `middle ear infection` | replace | - | - | - | - | - | - | - |
| `sepsis` -> `severe infection` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Description: Fever, ear infection, and possible severe blood infection.

| metric | value |
|---|---:|
| bertscore_f1 | 0.799 |
| coleman_liau | 18.93 |
| coleman_liau_drop | -2.50 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| diagnostic_identity_preservation | 1.000 |
| fkgl | 12.83 |
| fkgl_drop | 1.28 |
| fre | 19.1 |
| fre_gain | 12.7 |
| human_edit_recall | 1.000 |
| length_ratio | 1.12 |
| n_words | 9.0 |
| nli_completeness | 0.695 |
| nli_faithfulness | 0.669 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 68.98 |
| smog | 14.55 |
| smog_drop | -1.53 |
| uncertainty_preservation | 1.000 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `otitis media` -> `ear infection` | replace | attributed | 1.013 | 1.881 | 0.895 | 0.969 | 1.058 | - |
| `sepsis` -> `severe blood infection` | replace | attributed | 1.640 | 2.085 | 0.918 | 0.948 | 0.873 | - |

**edit `otitis media` -> `ear infection`**

- status: `attributed`
- log p full -0.3790, empty -1.3917
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+2.484` [michigan] otitis media: Ear infection, often in the middle ear.
    - `+1.426` [readme] otitis media: An ear infection causing inflammation in the middle ear.
    - `+0.707` [michigan] sepsis: A very serious infection in your blood caused by a germ (a bacteria). Also called septicemia.
    - `+0.075` [nih] sepsis: The presence of bacteria or their toxins in the blood or tissues.

- rationale: The glossary defines otitis media as an ear infection, often in the middle ear, so the replacement uses plain language to convey this meaning. Phrase frequency increases from Zipf 2.16 to 4.08, and syllable count decreases from 5 to 4. Patients can recognize the condition as a common ear infection without needing the medical term.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `sepsis` -> `severe blood infection`**

- status: `attributed`
- log p full -0.8914, empty -2.5314
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+1.277` [readme] sepsis: A severe condition where the body reacts to bacteria in the bloodstream by harming tissues and organs,
    - `+0.404` [michigan] sepsis: A very serious infection in your blood caused by a germ (a bacteria). Also called septicemia.
    - `+0.077` [readme] otitis media: An ear infection causing inflammation in the middle ear.
    - `+0.044` [readme] Sepsis: When bacteria get into the blood, the body's reaction can lead to tissue and organ damage, potentially
    - `+0.036` [nih] sepsis: The presence of bacteria or their toxins in the blood or tissues.

- rationale: The glossary defines sepsis as a severe reaction to bacteria in the bloodstream, so "severe blood infection" captures this critical meaning in everyday language. Phrase frequency rises from Zipf 3.01 to 4.09, and age of acquisition drops from 16.33 to 9.05, making the concept more accessible. Readers can grasp the seriousness of the bloodstream infection without needing to understand the clinical term.
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

**output:** Her main problem right now is feeling tired all day.

| metric | value |
|---|---:|
| bertscore_f1 | 0.526 |
| coleman_liau | 5.60 |
| coleman_liau_drop | 6.22 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 3.65 |
| fkgl_drop | 3.98 |
| fre | 86.7 |
| fre_gain | 23.2 |
| human_edit_recall | 1.000 |
| length_ratio | 0.71 |
| n_words | 10.0 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.994 |
| number_unit_preservation | 0.500 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.571 |
| sari | 14.86 |
| smog | 3.13 |
| smog_drop | 8.08 |
| temporality_preservation | 1.000 |

### Stage 4 - arm `termonly`

**output:** Right now, her main problem is feeling tired all day.

| metric | value |
|---|---:|
| bertscore_f1 | 0.586 |
| coleman_liau | 5.60 |
| coleman_liau_drop | 6.22 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 3.65 |
| fkgl_drop | 3.98 |
| fre | 86.7 |
| fre_gain | 23.2 |
| human_edit_recall | 1.000 |
| length_ratio | 0.71 |
| n_words | 10.0 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.994 |
| number_unit_preservation | 0.500 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.571 |
| sari | 14.86 |
| smog | 3.13 |
| smog_drop | 8.08 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `primary complaint` -> `main problem` | replace | - | - | - | - | - | - | - |
| `fatigue` -> `feeling tired` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Her main problem is feeling tired all day.

| metric | value |
|---|---:|
| bertscore_f1 | 0.598 |
| coleman_liau | 5.15 |
| coleman_liau_drop | 6.67 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 3.76 |
| fkgl_drop | 3.88 |
| fre | 82.4 |
| fre_gain | 18.9 |
| human_edit_recall | 1.000 |
| length_ratio | 0.57 |
| n_words | 8.0 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.994 |
| number_unit_preservation | 0.500 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.571 |
| sari | 15.97 |
| smog | 3.13 |
| smog_drop | 8.08 |
| temporality_preservation | 0.000 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `primary complaint` -> `main problem` | replace | attributed | 0.354 | 1.170 | 0.905 | 0.923 | 1.609 | - |
| `fatigue` -> `feeling tired` | replace | attributed | 0.443 | 0.867 | 0.821 | 0.845 | 0.626 | - |

**edit `primary complaint` -> `main problem`**

- status: `attributed`
- log p full -0.2122, empty -0.5662
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+1.928` [readme] complaint: A complaint is when a patient talks about their illness or problem.
    - `+0.319` [wiktionary] primary: most basic, simplest.
    - `+0.313` [wiktionary] fatigue: Fatigue is the material failure, such as cracking or separation, caused by stress on the material.
    - `+0.229` [wiktionary] complaint: A complaint is a small medical problem.
    - `+0.105` [michigan] fatigue: tired, weak feeling of the whole body, feeling tired all over

- rationale: "Primary complaint" refers to the main health issue a patient reports, and "main problem" conveys this idea in everyday language. Phrase frequency rises from Zipf 4.21 to 5.01, age of acquisition drops from 8.89 to 6.55, and syllable count decreases from 5 to 3. Readers can immediately identify the central health concern without navigating clinical terminology.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `fatigue` -> `feeling tired`**

- status: `attributed`
- log p full -0.5176, empty -0.9609
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.846` [justplainclear] fatigue: Tired, weak feeling of the whole body, feeling tired
    - `+0.220` [readme] complaint: A complaint is when a patient talks about their illness or problem.
    - `+0.182` [michigan] fatigue: tired, weak feeling of the whole body, feeling tired all over
    - `+0.157` [wiktionary] primary: most basic, simplest.
    - `+0.098` [wiktionary] primary: A primary is a kind of election held by a political party to choose the people it prefers for public 

- rationale: Fatigue refers to a state of exhaustion, which "feeling tired" expresses in everyday language. Word frequency rises from Zipf 3.86 to 4.57, and age of acquisition drops from 11.83 to 5.31. Readers can grasp the sense of weariness without needing medical terminology.
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

**output:** He has noticed some changes in his bowel movements, including occasional loose stools, and has recently started having pain mostly in the left side of his neck.

| metric | value |
|---|---:|
| bertscore_f1 | 0.591 |
| coleman_liau | 11.24 |
| coleman_liau_drop | 0.70 |
| copy_jargon_rate | 0.333 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.143 |
| fkgl | 12.86 |
| fkgl_drop | -0.54 |
| fre | 51.0 |
| fre_gain | 10.3 |
| human_edit_recall | 0.667 |
| laterality_preservation | 1.000 |
| length_ratio | 1.42 |
| n_words | 27.0 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.994 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.167 |
| sari | 16.67 |
| smog | 13.02 |
| smog_drop | 0.00 |
| temporality_preservation | 0.000 |

### Stage 4 - arm `termonly`

**output:** He has noted some changes in bowel movements with occasional watery stools and recent start of pain mostly in left neck.

| metric | value |
|---|---:|
| bertscore_f1 | 0.719 |
| coleman_liau | 10.13 |
| coleman_liau_drop | 1.81 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.375 |
| fkgl | 10.58 |
| fkgl_drop | 1.73 |
| fre | 56.6 |
| fre_gain | 16.0 |
| human_edit_recall | 1.000 |
| laterality_preservation | 1.000 |
| length_ratio | 1.11 |
| n_words | 21.0 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.990 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 29.30 |
| smog | 11.21 |
| smog_drop | 1.82 |
| temporality_preservation | 0.000 |

annotation backend `novita`, 4 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `stool irregularity` -> `changes in bowel movements` | replace | - | - | - | - | - | - | - |
| `loose stools` -> `watery stools` | replace | - | - | - | - | - | - | - |
| `new onset` -> `recent start` | replace | - | - | - | - | - | - | - |
| `predominantly` -> `mostly` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** He has noted some bowel changes with occasional watery poop and recently started pain mostly in the left neck.

| metric | value |
|---|---:|
| bertscore_f1 | 0.713 |
| coleman_liau | 10.42 |
| coleman_liau_drop | 1.53 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.250 |
| fkgl | 11.07 |
| fkgl_drop | 1.24 |
| fre | 49.5 |
| fre_gain | 8.9 |
| human_edit_recall | 1.000 |
| laterality_preservation | 1.000 |
| length_ratio | 1.00 |
| n_words | 19.0 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.990 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 30.61 |
| smog | 13.02 |
| smog_drop | 0.00 |
| temporality_preservation | 0.000 |

annotation backend `novita`, 4 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `stool irregularity` -> `bowel changes` | replace | attributed | -0.402 | -0.481 | 0.557 | 0.728 | 0.009 | - |
| `loose stools` -> `watery poop` | replace | attributed | 3.200 | 5.862 | 0.692 | 0.880 | 4.636 | - |
| `new onset` -> `recently started` | replace | attributed | 0.408 | 0.473 | 0.367 | 0.777 | 0.053 | - |
| `predominantly` -> `mostly` | replace | attributed | 0.035 | 0.148 | 0.308 | 0.631 | 0.022 | - |

**edit `stool irregularity` -> `bowel changes`**

- status: `attributed`
- log p full -2.0234, empty -1.6211
- masks scored: 66/66 (+7 top-k)
- ranked sources:
    - `+0.103` [readme] Stool: Stool is the waste material that comes out during a bowel movement.
    - `+0.093` [wiktionary] new: If something is new, it is not old.
    - `+0.064` [michigan] onset: The start.
    - `+0.043` [dictionary] Predominantly (adv.): In a predominant manner.

- rationale: "Stool irregularity" refers to changes in bowel habits, and "bowel changes" conveys this idea in simpler terms. Phrase frequency increases from Zipf 2.52 to 3.54, while age of acquisition falls from 12.63 to 9.72. Patients can grasp the concept of altered digestion without needing to interpret clinical jargon.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `loose stools` -> `watery poop`**

- status: `attributed`
- log p full -0.0695, empty -3.2696
- masks scored: 66/66 (+7 top-k)
- ranked sources:
    - `+4.987` [readme] loose stools: Watery poop.
    - `+0.351` [wiktionary] stool: A stool is a piece of feces.
    - `+0.187` [wiktionary] new: If somebody is new, they are not experienced.
    - `+0.177` [readme] stool: The stuff that comes out when you go to the bathroom.
    - `+0.145` [wiktionary] onset: The onset of something is the time when it begins (usually something bad).

- rationale: The glossary defines "loose stools" as "watery poop," so the replacement uses everyday language to convey the same meaning. Phrase frequency increases from Zipf 3.03 to 3.06, and age of acquisition falls from 7.71 to 6.65. Patients can recognize the symptom using familiar words instead of clinical terms.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `new onset` -> `recently started`**

- status: `attributed`
- log p full -1.7927, empty -2.2007
- masks scored: 66/66 (+7 top-k)
- ranked sources:
    - `+0.173` [wiktionary] new: If something is new, it is not old.
    - `+0.120` [michigan] onset: The start.
    - `+0.117` [wiktionary] new: If somebody is new, they are not experienced.
    - `+0.088` [wiktionary] onset: The onset of something is the time when it begins (usually something bad).
    - `+0.087` [readme] loose stools: Watery poop.

- rationale: "New onset" means a condition has just begun, and "recently started" conveys that same timing in everyday language. Word frequency rises from Zipf 3.72 to 4.87, though syllable count increases from 3 to 5. Readers can grasp when the symptoms first appeared without interpreting clinical jargon.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `predominantly` -> `mostly`**

- status: `attributed`
- log p full -0.2539, empty -0.2891
- masks scored: 66/66 (+7 top-k)
- ranked sources:
    - `+0.166` [readme] Stool: Stool is the waste material that comes out during a bowel movement.
    - `+0.144` [readme] stool: The stuff that comes out when you go to the bathroom.
    - `+0.134` [nih] stool: The material in a bowel movement. Stool is made up of undigested food, bacteria, mucus, and cells from 
    - `+0.035` [wiktionary] onset: The onset of something is the time when it begins (usually something bad).
    - `+0.017` [readme] loose stools: Watery poop.

- rationale: "Predominantly" means for the most part or mainly, so "mostly" conveys that same idea in simpler language. Word frequency rises from Zipf 3.80 to 4.83, and the syllable count drops from 5 to 2. Readers can quickly grasp that something happens in the majority of cases without stumbling over a complex adverb.
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

**output:** The patient is coming for a follow-up visit because of a past case of erythema nodosum.

| metric | value |
|---|---:|
| bertscore_f1 | 0.243 |
| coleman_liau | 7.72 |
| coleman_liau_drop | 6.88 |
| copy_jargon_rate | 1.000 |
| critical_error | 0.000 |
| fkgl | 9.09 |
| fkgl_drop | 2.62 |
| fre | 58.4 |
| fre_gain | 25.9 |
| human_edit_recall | 0.000 |
| length_ratio | 1.00 |
| n_words | 17.0 |
| nli_completeness | 0.971 |
| nli_faithfulness | 0.977 |
| replacement_f1 | 0.000 |
| rewrite_aggressiveness | 1.000 |
| sari | 10.55 |
| smog | 11.21 |
| smog_drop | 3.35 |
| temporality_preservation | 1.000 |

### Stage 4 - arm `termonly`

**output:** The patient comes for a follow-up visit for a history of painful red skin lumps.

| metric | value |
|---|---:|
| bertscore_f1 | 0.606 |
| coleman_liau | 6.97 |
| coleman_liau_drop | 7.63 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 7.57 |
| fkgl_drop | 4.14 |
| fre | 67.5 |
| fre_gain | 35.0 |
| human_edit_recall | 1.000 |
| length_ratio | 0.94 |
| n_words | 16.0 |
| nli_completeness | 0.546 |
| nli_faithfulness | 0.380 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.600 |
| sari | 23.30 |
| smog | 11.21 |
| smog_drop | 3.35 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `erythema nodosum` -> `painful red skin lumps` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** The patient comes for a follow-up for a history of red skin bumps.

| metric | value |
|---|---:|
| bertscore_f1 | 0.575 |
| coleman_liau | 5.12 |
| coleman_liau_drop | 9.48 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 5.82 |
| fkgl_drop | 5.89 |
| fre | 76.5 |
| fre_gain | 44.0 |
| human_edit_recall | 1.000 |
| length_ratio | 0.82 |
| n_words | 14.0 |
| nli_completeness | 0.593 |
| nli_faithfulness | 0.600 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.600 |
| sari | 23.17 |
| smog | 11.21 |
| smog_drop | 3.35 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `erythema nodosum` -> `red skin bumps` | replace | attributed | 1.449 | 1.559 | - | 0.488 | 0.333 | - |

**edit `erythema nodosum` -> `red skin bumps`**

- status: `attributed`
- log p full -2.0234, empty -3.4727
- masks scored: 10/10 (+2 top-k)
- ranked sources:
    - `+0.650` [readme] Erythema: Red skin.
    - `+0.316` [nih] erythema: Redness of the skin.

- rationale: "Erythema nodosum" refers to a specific type of inflammation that causes tender red lumps under the skin, so "red skin bumps" captures the visible symptom in everyday language. The phrase frequency rises from Zipf 1.39 to 3.57, and the syllable count drops from 5 to 3. This allows patients to recognize the physical sign without needing to recall the complex medical label.
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

**output:** She was low on iron last year. Because she had several surgeries and did not eat or drink enough by mouth, she may be low on iron again.

| metric | value |
|---|---:|
| bertscore_f1 | 0.665 |
| coleman_liau | 4.04 |
| coleman_liau_drop | 3.83 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.200 |
| fkgl | 5.04 |
| fkgl_drop | 2.43 |
| fre | 83.9 |
| fre_gain | 22.8 |
| human_edit_recall | 1.000 |
| length_ratio | 1.22 |
| n_words | 28.0 |
| nli_completeness | 0.570 |
| nli_faithfulness | 0.504 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.800 |
| sari | 14.89 |
| smog | 7.17 |
| smog_drop | 4.04 |
| uncertainty_preservation | 1.000 |

### Stage 4 - arm `termonly`

**output:** She had low iron last year, and with her multiple surgeries and poor intake by mouth, may have low iron again.

| metric | value |
|---|---:|
| bertscore_f1 | 0.782 |
| coleman_liau | 6.82 |
| coleman_liau_drop | 1.05 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.200 |
| fkgl | 8.90 |
| fkgl_drop | -1.42 |
| fre | 68.7 |
| fre_gain | 7.6 |
| human_edit_recall | 1.000 |
| length_ratio | 0.91 |
| n_words | 21.0 |
| nli_completeness | 0.821 |
| nli_faithfulness | 0.102 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 33.67 |
| smog | 11.21 |
| smog_drop | 0.00 |
| uncertainty_preservation | 1.000 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `iron deficient` -> `low iron` | replace | - | - | - | - | - | - | - |
| `p. o.` -> `by mouth` | replace | - | - | - | - | - | - | - |
| `iron deficient` -> `low iron` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** She did not have enough iron last year, and with her multiple surgeries and poor intake by mouth, may have become low in iron again.

| metric | value |
|---|---:|
| bertscore_f1 | 0.782 |
| coleman_liau | 7.38 |
| coleman_liau_drop | 0.50 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.200 |
| fkgl | 10.68 |
| fkgl_drop | -3.21 |
| fre | 63.0 |
| fre_gain | 1.9 |
| human_edit_recall | 1.000 |
| length_ratio | 1.09 |
| n_words | 25.0 |
| nli_completeness | 0.836 |
| nli_faithfulness | 0.101 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 35.75 |
| smog | 11.21 |
| smog_drop | 0.00 |
| uncertainty_preservation | 1.000 |

annotation backend `novita`, 2 edits kept

- rejected: DROP noop      'iron' -> 'iron'  (nothing changed)

| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `p. o.` -> `by mouth` | replace | attributed | 0.022 | 0.645 | 0.350 | 0.648 | 0.221 | - |
| `iron deficient` -> `low in iron` | replace | attributed | 0.058 | 0.091 | 0.366 | 0.650 | 0.066 | - |

**edit `p. o.` -> `by mouth`**

- status: `attributed`
- log p full -0.0249, empty -0.0470
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.302` [michigan] deficient: To not have enough.
    - `+0.081` [thesaurus] deficient: lacking, not enough, poor
    - `+0.039` [michigan] iron: A mineral that can helps your body work in many ways. For example, it help blood carry oxygen and muscle

- rationale: The abbreviation "p. o." stands for the Latin phrase "per os," meaning "by mouth," so the replacement directly states the route of administration in plain English. Word frequency remains unchanged at Zipf 4.82, and the syllable count stays at 2. Patients can immediately recognize that the medication should be taken orally without needing to interpret a Latin abbreviation.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `iron deficient` -> `low in iron`**

- status: `attributed`
- log p full -1.0004, empty -1.0587
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.148` [michigan] iron: A mineral that can helps your body work in many ways. For example, it help blood carry oxygen and muscle
    - `+0.082` [thesaurus] deficient: lacking, not enough, poor
    - `+0.043` [wiktionary] iron: A metal from the element.

- rationale: "Iron deficient" means the body lacks enough iron, and "low in iron" expresses that same shortfall in everyday language. Phrase frequency rises from Zipf 3.31 to 4.64, age of acquisition drops from 11.61 to 7.32, and syllable count falls from 5 to 4. Readers can grasp that their iron levels are below normal without needing to interpret a clinical descriptor.
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

**output:** We will set up a time for him to wear a Holter monitor and send him back to his heart doctor.

| metric | value |
|---|---:|
| bertscore_f1 | 0.729 |
| coleman_liau | 2.68 |
| coleman_liau_drop | 5.84 |
| copy_jargon_rate | 1.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 6.65 |
| fkgl_drop | 2.49 |
| fre | 84.8 |
| fre_gain | 28.6 |
| human_edit_recall | 0.000 |
| length_ratio | 1.31 |
| n_words | 21.0 |
| nli_completeness | 0.957 |
| nli_faithfulness | 0.984 |
| replacement_f1 | 0.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.667 |
| sari | 23.12 |
| smog | 8.84 |
| smog_drop | 2.37 |

### Stage 4 - arm `termonly`

**output:** We will schedule him for the heart monitor and refer him back to his heart doctor.

| metric | value |
|---|---:|
| bertscore_f1 | 0.928 |
| coleman_liau | 6.27 |
| coleman_liau_drop | 2.25 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 6.14 |
| fkgl_drop | 3.00 |
| fre | 79.6 |
| fre_gain | 23.3 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 16.0 |
| nli_completeness | 0.487 |
| nli_faithfulness | 0.931 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 64.22 |
| smog | 8.84 |
| smog_drop | 2.37 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `Holter monitor` -> `heart monitor` | replace | - | - | - | - | - | - | - |
| `cardiologist` -> `heart doctor` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** We will schedule him for a portable heart monitor and refer him back to his heart doctor.

| metric | value |
|---|---:|
| bertscore_f1 | 0.915 |
| coleman_liau | 7.02 |
| coleman_liau_drop | 1.50 |
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
| nli_completeness | 0.187 |
| nli_faithfulness | 0.696 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 54.75 |
| smog | 11.21 |
| smog_drop | 0.00 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `Holter monitor` -> `portable heart monitor` | replace | attributed | 0.214 | 0.341 | - | 0.697 | 0.122 | - |
| `cardiologist` -> `heart doctor` | replace | attributed | 0.034 | 3.752 | - | 0.833 | 1.777 | - |

**edit `Holter monitor` -> `portable heart monitor`**

- status: `attributed`
- log p full -0.8848, empty -1.0989
- masks scored: 34/34 (+4 top-k)
- ranked sources:
    - `+0.198` [iowa] HOLTER MONITOR: a portable machine for recording heart beats
    - `+0.075` [nih] cardiologist: A doctor who has special training to diagnose and treat diseases of the heart and blood vessels.
    - `+0.031` [wiktionary] cardiologist: A cardiologist is a doctor who specializes in medical problems related to the heart.

- rationale: A Holter monitor is a device that records heart activity over time, and "portable heart monitor" conveys this function using everyday terms. Word frequency increases from Zipf 2.12 to 3.81, while age of acquisition remains unchanged at 9.68. Readers can grasp that the device tracks heart rhythms without needing to know the specific brand name.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `cardiologist` -> `heart doctor`**

- status: `attributed`
- log p full -0.0008, empty -0.0349
- masks scored: 34/34 (+4 top-k)
- ranked sources:
    - `+1.995` [justplainclear] cardiologist: Heart doctor
    - `+0.218` [michigan] cardiologist: A doctor who treats heart and blood vessel problems.
    - `+0.210` [iowa] HOLTER MONITOR: a portable machine for recording heart beats
    - `+0.061` [wiktionary] cardiologist: A cardiologist is a doctor who specializes in medical problems related to the heart.

- rationale: A cardiologist is a physician who specializes in heart conditions, so "heart doctor" conveys that role in everyday language. Word frequency rises from Zipf 2.90 to 4.76, and age of acquisition drops from 13.42 to 5.17. Readers can immediately identify the type of specialist involved without needing medical terminology.
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

**output:** The patient wanted to go ahead with surgery.

| metric | value |
|---|---:|
| bertscore_f1 | 0.781 |
| coleman_liau | 6.60 |
| coleman_liau_drop | 10.15 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.250 |
| fkgl | 6.71 |
| fkgl_drop | 4.43 |
| fre | 61.2 |
| fre_gain | 31.7 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 8.0 |
| nli_completeness | 0.986 |
| nli_faithfulness | 0.993 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.250 |
| sari | 22.50 |
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
| `operative intervention` -> `surgery` | replace | attributed | 0.025 | 2.348 | 0.600 | 0.883 | 0.011 | - |

**edit `operative intervention` -> `surgery`**

- status: `attributed`
- log p full -0.0027, empty -0.0281
- masks scored: 66/66 (+2 top-k)
- ranked sources:
    - `+0.768` [readme] Operative: Operative means related to surgery.
    - `+0.757` [readme] intervention: An intervention is a step taken to help treat or prevent a health problem.
    - `+0.469` [wiktionary] operative: An operative is an employee with some particular function or skill.
    - `+0.435` [readme] operative: Dealing with surgeries.
    - `+0.340` [wiktionary] operative: If something is operative, it is able to work.

- rationale: "Operative intervention" refers to a medical procedure involving manual or instrumental treatment, which "surgery" conveys more directly in everyday language. Word frequency rises from Zipf 3.71 to 4.63, and age of acquisition drops from 13.11 to 7.68. Readers can immediately recognize the type of medical procedure being discussed without navigating formal terminology.
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

**output:** An X-ray of the abdomen was taken, and it showed an unusual pattern of gas in the intestines.

| metric | value |
|---|---:|
| bertscore_f1 | 0.617 |
| coleman_liau | 6.08 |
| coleman_liau_drop | 2.42 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.600 |
| fkgl | 9.13 |
| fkgl_drop | -1.94 |
| fre | 61.7 |
| fre_gain | 0.3 |
| human_edit_recall | 1.000 |
| length_ratio | 1.12 |
| n_words | 19.0 |
| nli_completeness | 0.897 |
| nli_faithfulness | 0.881 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.200 |
| sari | 24.54 |
| smog | 13.02 |
| smog_drop | -4.18 |

### Stage 4 - arm `termonly`

**output:** An X-ray of the belly was taken showing an unusual gas pattern in the intestines.

| metric | value |
|---|---:|
| bertscore_f1 | 0.674 |
| coleman_liau | 7.36 |
| coleman_liau_drop | 1.14 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.600 |
| fkgl | 9.14 |
| fkgl_drop | -1.95 |
| fre | 56.3 |
| fre_gain | -5.1 |
| human_edit_recall | 1.000 |
| length_ratio | 0.94 |
| n_words | 16.0 |
| nli_completeness | 0.795 |
| nli_faithfulness | 0.766 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 30.93 |
| smog | 11.21 |
| smog_drop | -2.37 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `obtained` -> `taken` | replace | - | - | - | - | - | - | - |
| `abnormal bowel gas pattern` -> `unusual gas pattern in the intestines` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** An x-ray of the belly showed unusual gas in the intestines.

| metric | value |
|---|---:|
| bertscore_f1 | 0.589 |
| coleman_liau | 6.29 |
| coleman_liau_drop | 2.21 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 6.94 |
| fkgl_drop | 0.25 |
| fre | 64.9 |
| fre_gain | 3.6 |
| human_edit_recall | 1.000 |
| length_ratio | 0.71 |
| n_words | 12.0 |
| nli_completeness | 0.902 |
| nli_faithfulness | 0.902 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.167 |
| sari | 23.47 |
| smog | 11.21 |
| smog_drop | -2.37 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `abnormal bowel gas pattern` -> `unusual gas in the intestines` | replace | attributed | 1.079 | 1.333 | 0.579 | 0.802 | 0.418 | - |

**edit `abnormal bowel gas pattern` -> `unusual gas in the intestines`**

- status: `attributed`
- log p full -1.1865, empty -2.2653
- masks scored: 66/66 (+2 top-k)
- ranked sources:
    - `+0.689` [readme] bowel: The intestines in your belly that break down food.
    - `+0.271` [readme] Bowel: Your intestines in the belly that break down food.
    - `+0.199` [wiktionary] abnormal: When something is abnormal, it often means that it is bigger than [[normal].
    - `+0.024` [nih] abnormal: Not normal. Describes a state, condition, or behavior that is unusual or different from what is cons

- rationale: The glossary defines the intestines as the belly organs that break down food, so "unusual gas in the intestines" conveys the original concept of an abnormal bowel gas pattern in plain language. Phrase frequency decreases from Zipf 3.29 to 3.19, while age of acquisition falls from 10.05 to 8.56. Patients can grasp that there is unexpected gas in their digestive tract without needing to interpret clinical imaging terminology.
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

**output:** She was given Ativan to make her sleepy. When she arrived at the emergency room, she was very drowsy and could not answer any questions about her health.

| metric | value |
|---|---:|
| bertscore_f1 | 0.578 |
| coleman_liau | 7.56 |
| coleman_liau_drop | 1.64 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 7.15 |
| fkgl_drop | 5.17 |
| fre | 68.7 |
| fre_gain | 28.1 |
| human_edit_recall | 1.000 |
| length_ratio | 1.40 |
| n_words | 28.0 |
| nli_completeness | 0.004 |
| nli_faithfulness | 0.804 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.750 |
| sari | 17.48 |
| severity_downgrade | 0.000 |
| severity_tier_input | 3.000 |
| severity_tier_output | 3.000 |
| smog | 7.17 |
| smog_drop | 8.73 |

### Stage 4 - arm `termonly`

**output:** She was given a medicine to make her sleepy and came into the emergency room very drowsy and unable to give any history.

| metric | value |
|---|---:|
| bertscore_f1 | 0.753 |
| coleman_liau | 7.37 |
| coleman_liau_drop | 1.83 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.333 |
| fkgl | 12.88 |
| fkgl_drop | -0.56 |
| fre | 43.7 |
| fre_gain | 3.1 |
| human_edit_recall | 1.000 |
| length_ratio | 1.15 |
| n_words | 23.0 |
| nli_completeness | 0.046 |
| nli_faithfulness | 0.985 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.250 |
| sari | 49.27 |
| severity_downgrade | 0.000 |
| severity_tier_input | 3.000 |
| severity_tier_output | 3.000 |
| smog | 14.55 |
| smog_drop | 1.35 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `sedated` -> `given a medicine to make her sleepy` | replace | - | - | - | - | - | - | - |
| `obtunded` -> `very drowsy` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** She was made sleepy with a medicine and came into the emergency room not fully alert and unable to give any history.

| metric | value |
|---|---:|
| bertscore_f1 | 0.692 |
| coleman_liau | 7.64 |
| coleman_liau_drop | 1.56 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.667 |
| fkgl | 12.30 |
| fkgl_drop | 0.02 |
| fre | 46.1 |
| fre_gain | 5.5 |
| human_edit_recall | 1.000 |
| length_ratio | 1.10 |
| n_words | 22.0 |
| nli_completeness | 0.031 |
| nli_faithfulness | 0.993 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.250 |
| sari | 35.18 |
| severity_downgrade | 0.000 |
| severity_tier_input | 3.000 |
| severity_tier_output | 3.000 |
| smog | 14.55 |
| smog_drop | 1.35 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `sedated` -> `made sleepy` | replace | attributed | 1.944 | 2.688 | - | 0.718 | 0.509 | - |
| `Ativan` -> `a medicine` | replace | attributed | 0.780 | 1.353 | - | 0.838 | 0.138 | - |
| `obtunded` -> `not fully alert` | replace | attributed | 6.272 | 9.562 | - | 0.885 | 8.893 | - |

**edit `sedated` -> `made sleepy`**

- status: `attributed`
- log p full -0.5740, empty -2.5176
- masks scored: 18/18 (+3 top-k)
- ranked sources:
    - `+1.385` [readme] SEDATED: Feeling calm, relaxed, or sleepy because of certain medications.
    - `+0.876` [readme] Sedated: When you're sedated, you feel calm, relaxed, or sleepy because of specific medication.
    - `+0.060` [readme] obtunded: Being not fully alert.
    - `-0.079` [wiktionary] sedated: A sedate person is calm and dignified.

- rationale: "Sedated" means being in a state of reduced consciousness or calmness, which "made sleepy" conveys in everyday language. The word frequency increases from Zipf 2.78 to 3.68, indicating the replacement is more common, while the syllable count remains unchanged at 3. This allows patients to grasp that they will feel drowsy without needing to understand clinical terminology.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `Ativan` -> `a medicine`**

- status: `attributed`
- log p full -0.5303, empty -1.3101
- masks scored: 18/18 (+3 top-k)
- ranked sources:
    - `+0.364` [readme] SEDATED: Feeling calm, relaxed, or sleepy because of certain medications.
    - `+0.226` [readme] obtunded: Being not fully alert.
    - `+0.224` [readme] Sedated: When you're sedated, you feel calm, relaxed, or sleepy because of specific medication.
    - `-0.127` [wiktionary] sedated: A sedate person is calm and dignified.

- rationale: Ativan is a brand name for a specific medication, so "a medicine" conveys the general category in plain language. Word frequency increases from Zipf 2.31 to 4.73, while syllable count rises from 2 to 4. Patients can recognize that a drug is involved without needing to know the specific brand name.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `obtunded` -> `not fully alert`**

- status: `attributed`
- log p full -0.0379, empty -6.3101
- masks scored: 18/18 (+3 top-k)
- ranked sources:
    - `+9.180` [readme] obtunded: Being not fully alert.
    - `+0.287` [readme] SEDATED: Feeling calm, relaxed, or sleepy because of certain medications.
    - `+0.150` [readme] Sedated: When you're sedated, you feel calm, relaxed, or sleepy because of specific medication.
    - `-0.099` [wiktionary] sedated: A sedate person is calm and dignified.

- rationale: "Obtunded" means a reduced level of alertness, so "not fully alert" conveys that state in everyday language. Word frequency rises from Zipf 1.01 to 4.22, indicating the replacement is more common, though syllable count increases from 3 to 5. Readers can grasp the patient’s diminished awareness without needing to know the specialized medical term.
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

**output:** He does not have swelling now, but he had some mild swelling in his legs in the past.

| metric | value |
|---|---:|
| bertscore_f1 | 0.841 |
| coleman_liau | 3.82 |
| coleman_liau_drop | -1.49 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 4.54 |
| fkgl_drop | -0.12 |
| fre | 94.6 |
| fre_gain | 4.5 |
| human_edit_recall | 1.000 |
| length_ratio | 1.20 |
| n_words | 18.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.366 |
| nli_faithfulness | 0.995 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 26.34 |
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
| `edema` -> `swelling` | replace | attributed | 0.048 | 2.904 | - | 0.860 | 0.430 | - |

**edit `edema` -> `swelling`**

- status: `attributed`
- log p full -0.0028, empty -0.0505
- masks scored: 34/34 (+2 top-k)
- ranked sources:
    - `+0.924` [readme] Edema: Swelling in the body caused by too much fluid.
    - `+0.494` [readme] edema: Swelling due to too much fluid in the body tissues.
    - `+0.181` [nih] edema: Swelling caused by excess fluid in body tissues.
    - `+0.010` [michigan] edema: Swelling caused by too much fluid in your body.
    - `-0.244` [iowa] EDEMA: excess fluid collecting in tissue

- rationale: Edema refers to fluid buildup in tissues, so "swelling" conveys that same physical change in everyday language. Word frequency rises from Zipf 2.95 to 3.68, and the word shortens from three syllables to two. Readers can recognize the visible sign of fluid retention without needing medical terminology.
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

**output:** The patient has a mild case of secondary hyperparathyroidism.

| metric | value |
|---|---:|
| bertscore_f1 | 0.426 |
| coleman_liau | 14.42 |
| coleman_liau_drop | 21.78 |
| copy_jargon_rate | 1.000 |
| critical_error | 0.000 |
| fkgl | 8.90 |
| fkgl_drop | 12.08 |
| fre | 47.3 |
| fre_gain | 97.3 |
| human_edit_recall | 0.000 |
| length_ratio | 1.80 |
| n_words | 9.0 |
| nli_completeness | 0.993 |
| nli_faithfulness | 0.963 |
| replacement_f1 | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 15.00 |
| severity_downgrade | 0.000 |
| severity_preservation | 1.000 |
| severity_tier_input | 1.000 |
| severity_tier_output | 1.000 |
| smog | 11.21 |
| smog_drop | 0.00 |

### Stage 4 - arm `termonly`

**output:** Mild overactive parathyroid glands caused by another condition.

| metric | value |
|---|---:|
| bertscore_f1 | 0.562 |
| coleman_liau | 20.37 |
| coleman_liau_drop | 15.82 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.333 |
| fkgl | 11.13 |
| fkgl_drop | 9.85 |
| fre | 29.5 |
| fre_gain | 79.5 |
| human_edit_recall | 1.000 |
| length_ratio | 1.60 |
| n_words | 8.0 |
| nli_completeness | 0.899 |
| nli_faithfulness | 0.912 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 23.89 |
| severity_downgrade | 0.000 |
| severity_preservation | 1.000 |
| severity_tier_input | 1.000 |
| severity_tier_output | 1.000 |
| smog | 13.02 |
| smog_drop | -1.82 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `secondary hyperparathyroidism` -> `overactive parathyroid glands caused by another condition` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Mild overactive parathyroid glands from another cause.

| metric | value |
|---|---:|
| bertscore_f1 | 0.576 |
| coleman_liau | 18.91 |
| coleman_liau_drop | 17.29 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.333 |
| fkgl | 9.05 |
| fkgl_drop | 11.93 |
| fre | 42.6 |
| fre_gain | 92.6 |
| human_edit_recall | 1.000 |
| length_ratio | 1.40 |
| n_words | 7.0 |
| nli_completeness | 0.920 |
| nli_faithfulness | 0.942 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 24.07 |
| severity_downgrade | 0.000 |
| severity_preservation | 1.000 |
| severity_tier_input | 1.000 |
| severity_tier_output | 1.000 |
| smog | 11.21 |
| smog_drop | 0.00 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `secondary hyperparathyroidism` -> `overactive parathyroid glands from another cause` | replace | attributed | 0.806 | 0.839 | - | 0.643 | 0.087 | - |

**edit `secondary hyperparathyroidism` -> `overactive parathyroid glands from another cause`**

- status: `attributed`
- log p full -2.8504, empty -3.6560
- masks scored: 18/18 (+2 top-k)
- ranked sources:
    - `+0.296` [justplainclear] hyperparathyroidism: A condition where your parathyroid glands work too hard and raise the calcium level in yo
    - `+0.209` [wiktionary] secondary: second, next in order to the first or primary.

- rationale: "Secondary hyperparathyroidism" refers to overactive parathyroid glands triggered by another underlying condition, so the replacement "overactive parathyroid glands from another cause" conveys this mechanism in everyday language. Phrase frequency rises from Zipf 1.88 to 2.08, and age of acquisition drops from 19.11 to 15.50. Readers can grasp that the gland issue is a reaction to a different health problem rather than a primary disease.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

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

**output:** The doctor checked the patient’s overall health and found no other problems, except for the ones already mentioned.

| metric | value |
|---|---:|
| bertscore_f1 | 0.293 |
| coleman_liau | 13.17 |
| coleman_liau_drop | -0.73 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 9.79 |
| fkgl_drop | 0.78 |
| fre | 57.0 |
| fre_gain | 9.1 |
| human_edit_recall | 1.000 |
| length_ratio | 1.19 |
| n_words | 19.0 |
| nli_completeness | 0.838 |
| nli_faithfulness | 0.103 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.429 |
| sari | 10.93 |
| smog | 11.21 |
| smog_drop | 0.00 |

### Stage 4 - arm `termonly`

**output:** Otherwise, a check of all body systems was done and showed no problems except for those mentioned above.

| metric | value |
|---|---:|
| bertscore_f1 | 0.541 |
| coleman_liau | 9.94 |
| coleman_liau_drop | 2.49 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.667 |
| fkgl | 8.47 |
| fkgl_drop | 2.09 |
| fre | 66.4 |
| fre_gain | 18.5 |
| human_edit_recall | 1.000 |
| length_ratio | 1.12 |
| n_words | 18.0 |
| nli_completeness | 0.993 |
| nli_faithfulness | 0.232 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.250 |
| sari | 18.40 |
| smog | 8.84 |
| smog_drop | 2.37 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `review of systems` -> `check of all body systems` | replace | - | - | - | - | - | - | - |
| `obtained` -> `done` | replace | - | - | - | - | - | - | - |
| `negative` -> `no problems` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Otherwise, questions about symptoms in different body parts were asked and showed no issues except as mentioned above.

| metric | value |
|---|---:|
| bertscore_f1 | 0.463 |
| coleman_liau | 14.46 |
| coleman_liau_drop | -2.02 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.667 |
| fkgl | 11.10 |
| fkgl_drop | -0.53 |
| fre | 47.6 |
| fre_gain | -0.3 |
| human_edit_recall | 1.000 |
| length_ratio | 1.12 |
| n_words | 18.0 |
| nli_completeness | 0.927 |
| nli_faithfulness | 0.235 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.200 |
| sari | 14.98 |
| smog | 11.21 |
| smog_drop | 0.00 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `review of systems` -> `questions about symptoms in different body parts` | replace | attributed | 14.960 | 14.982 | - | 0.817 | 14.884 | - |
| `obtained` -> `asked` | replace | attributed | 0.137 | 1.002 | - | 0.926 | 1.097 | - |
| `negative` -> `no issues` | replace | attributed | 0.235 | 0.381 | - | 0.840 | 0.496 | - |

**edit `review of systems` -> `questions about symptoms in different body parts`**

- status: `attributed`
- log p full -3.8544, empty -18.8146
- masks scored: 18/18 (+2 top-k)
- ranked sources:
    - `+14.909` [readme] Review of systems: Questions that ask patients about any symptoms they might be experiencing in different part
    - `+0.025` [wiktionary] obtained: If you obtain something, you get it.
    - `-0.023` [wiktionary] negative: If something is negative, it is harmful, sad, or otherwise not good.

- rationale: "Review of systems" is a medical checklist of symptoms across body areas, so "questions about symptoms in different body parts" conveys that idea in everyday language. Phrase frequency decreases from Zipf 4.79 to 4.26, while age of acquisition drops from 8.84 to 5.50. Patients can grasp that the clinician will ask about symptoms in various body regions.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `obtained` -> `asked`**

- status: `attributed`
- log p full -0.0889, empty -0.2256
- masks scored: 18/18 (+2 top-k)
- ranked sources:
    - `+1.091` [readme] Review of systems: Questions that ask patients about any symptoms they might be experiencing in different part
    - `-0.006` [wiktionary] obtained: If you obtain something, you get it.
    - `-0.085` [wiktionary] negative: If a word, sentence, answer, etc. is negative, it uses a word like no, not, never, etc.
    - `-0.133` [wiktionary] negative: If something is negative, it is harmful, sad, or otherwise not good.

- rationale: "Obtained" means to get or receive something, and "asked" conveys the action of requesting information in simpler terms. Word frequency increases from Zipf 4.49 to 5.30, and the word becomes shorter, dropping from 2 syllables to 1. Patients can easily grasp that the doctor requested details rather than just receiving them.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `negative` -> `no issues`**

- status: `attributed`
- log p full -0.8496, empty -1.0850
- masks scored: 18/18 (+2 top-k)
- ranked sources:
    - `+0.530` [readme] Review of systems: Questions that ask patients about any symptoms they might be experiencing in different part
    - `+0.034` [wiktionary] obtained: If you obtain something, you get it.
    - `-0.028` [wiktionary] negative: If something is negative, it is harmful, sad, or otherwise not good.

- rationale: The term "negative" in a medical context indicates the absence of a condition, which "no issues" conveys in everyday language. Word frequency rises from Zipf 4.79 to 5.16, and age of acquisition drops from 7.47 to 2.72. Readers can immediately grasp that nothing abnormal was found.
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

**output:** The symptoms get worse when sitting for any amount of time, like when driving a car.

| metric | value |
|---|---:|
| bertscore_f1 | 0.786 |
| coleman_liau | 6.64 |
| coleman_liau_drop | 1.45 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 6.14 |
| fkgl_drop | 1.48 |
| fre | 79.6 |
| fre_gain | 10.6 |
| human_edit_recall | 1.000 |
| length_ratio | 1.07 |
| n_words | 16.0 |
| nli_completeness | 0.990 |
| nli_faithfulness | 0.994 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 31.60 |
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
| `motor vehicle` -> `car` | replace | attributed | 0.000 | 0.150 | - | - | - | - |

**edit `motor vehicle` -> `car`**

- status: `attributed`
- log p full -0.0017, empty -0.0020
- masks scored: 4/4 (+1 top-k)
- ranked sources:
    - `-0.452` [wiktionary] motor vehicle: A motor vehicle a road vehicle powered by an internal combustion engine to provide power to rot

- rationale: "Motor vehicle" refers to any self-propelled road transport, and "car" captures this idea using a familiar, everyday word. Word frequency rises from Zipf 4.33 to 5.45, and age of acquisition drops from 7.42 to 3.37. Readers can instantly picture the type of vehicle involved without pausing over formal terminology.
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

**output:** Exams of the forearm, elbow, and shoulder show no nerve problems.

| metric | value |
|---|---:|
| bertscore_f1 | 0.637 |
| coleman_liau | 8.93 |
| coleman_liau_drop | 8.07 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 5.86 |
| fkgl_drop | 6.97 |
| fre | 72.6 |
| fre_gain | 53.5 |
| human_edit_recall | 1.000 |
| length_ratio | 1.22 |
| n_words | 11.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.966 |
| nli_faithfulness | 0.987 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 47.22 |
| smog | 3.13 |
| smog_drop | 8.08 |

### Stage 4 - arm `termonly`

**output:** Exams of the forearm, elbow, and shoulder show no nerve damage.

| metric | value |
|---|---:|
| bertscore_f1 | 0.601 |
| coleman_liau | 7.87 |
| coleman_liau_drop | 9.13 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 5.86 |
| fkgl_drop | 6.97 |
| fre | 72.6 |
| fre_gain | 53.5 |
| human_edit_recall | 1.000 |
| length_ratio | 1.22 |
| n_words | 11.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.936 |
| nli_faithfulness | 0.951 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 41.13 |
| smog | 3.13 |
| smog_drop | 8.08 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `neurologic compromise` -> `nerve damage` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Exams of the forearm, elbow, and shoulder show no nerve damage.

| metric | value |
|---|---:|
| bertscore_f1 | 0.601 |
| coleman_liau | 7.87 |
| coleman_liau_drop | 9.13 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 5.86 |
| fkgl_drop | 6.97 |
| fre | 72.6 |
| fre_gain | 53.5 |
| human_edit_recall | 1.000 |
| length_ratio | 1.22 |
| n_words | 11.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.936 |
| nli_faithfulness | 0.951 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 41.13 |
| smog | 3.13 |
| smog_drop | 8.08 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `neurologic compromise` -> `nerve damage` | replace | attributed | 0.163 | 0.409 | 0.351 | 0.629 | 0.190 | - |

**edit `neurologic compromise` -> `nerve damage`**

- status: `attributed`
- log p full -0.4325, empty -0.5957
- masks scored: 66/66 (+2 top-k)
- ranked sources:
    - `+0.259` [readme] NEUROLOGIC: Having to do with the nerves in the body, brain, or spinal cord.
    - `+0.070` [readme] Neurologic: Having to do with nerves in the body, brain, or spinal cord.
    - `+0.028` [wiktionary] compromise: Compromise is the act making this type of agreement.

- rationale: "Neurologic compromise" refers to impaired function of the nervous system, which "nerve damage" expresses in everyday terms. Phrase frequency rises from Zipf 2.55 to 4.11, age of acquisition drops from 13.85 to 9.67, and syllable count falls from 7 to 3. Readers can grasp that the nerves are harmed without needing specialized medical vocabulary.
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

**output:** After that, the local anesthesia was injected into the area around the tumor.

| metric | value |
|---|---:|
| bertscore_f1 | 0.708 |
| coleman_liau | 10.03 |
| coleman_liau_drop | 2.64 |
| copy_jargon_rate | 1.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 12.17 |
| fkgl_drop | 1.50 |
| fre | 30.9 |
| fre_gain | 12.5 |
| human_edit_recall | 0.000 |
| length_ratio | 1.08 |
| n_words | 13.0 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.992 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 43.37 |
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

**output:** After that, the numbing drug was injected into the area around the growth.

| metric | value |
|---|---:|
| bertscore_f1 | 0.779 |
| coleman_liau | 8.69 |
| coleman_liau_drop | 3.97 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 8.54 |
| fkgl_drop | 5.13 |
| fre | 57.0 |
| fre_gain | 38.6 |
| human_edit_recall | 1.000 |
| length_ratio | 1.08 |
| n_words | 13.0 |
| nli_completeness | 0.784 |
| nli_faithfulness | 0.981 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 56.27 |
| smog | 11.21 |
| smog_drop | 3.35 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `local anesthesia` -> `numbing drug` | replace | attributed | 5.586 | 6.601 | 0.934 | 0.868 | 0.845 | - |
| `tumor` -> `growth` | replace | attributed | 0.012 | 0.028 | 0.301 | 0.758 | 0.105 | - |

**edit `local anesthesia` -> `numbing drug`**

- status: `attributed`
- log p full -0.4489, empty -6.0352
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+1.318` [readme] local anesthesia: A drug that numbs a specific part of your body without affecting the rest.
    - `+0.473` [michigan] local anesthesia: A drug that causes only in the area of the body where the drug is put, as when a tooth is pu
    - `+0.369` [iowa] LOCAL ANESTHESIA: creation of insensitivity to pain in a small, local area of the body, usually by injection o
    - `+0.117` [dictionary] Thereafter (adv.): After that; afterward.

- rationale: The glossary defines local anesthesia as a drug that numbs a specific part of your body without affecting the rest, so "numbing drug" captures this core function in everyday language. Phrase frequency decreases from Zipf 3.39 to 2.90, while age of acquisition drops from 12.53 to 8.11. Patients can grasp that the medication targets only one area for pain relief.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `tumor` -> `growth`**

- status: `attributed`
- log p full -0.5352, empty -0.5469
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.462` [justplainclear] tumor: Growth or lump
    - `+0.357` [michigan] tumor: A growth or lump in your body. It may be cancer, but it also may not be cancer.
    - `+0.223` [nih] tumor: An abnormal mass of tissue that results when cells divide more than they should or do not die when th
    - `+0.083` [nih] local anesthesia: A temporary loss of feeling in one small area of the body caused by special drugs called ane
    - `+0.016` [michigan] local anesthesia: A drug that causes only in the area of the body where the drug is put, as when a tooth is pu

- rationale: A tumor is an abnormal mass of tissue, and "growth" conveys this idea in everyday language. Word frequency rises from Zipf 3.97 to 5.03, age of acquisition drops from 10.32 to 6.70, and syllable count falls from 2 to 1. Readers can grasp that an unusual lump is present without needing medical terminology.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

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

**output:** The patient does not have numbness or tingling in the hand or arm.

| metric | value |
|---|---:|
| bertscore_f1 | 0.698 |
| coleman_liau | 5.57 |
| coleman_liau_drop | -0.33 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 4.91 |
| fkgl_drop | -1.19 |
| fre | 83.0 |
| fre_gain | -5.0 |
| human_edit_recall | 1.000 |
| length_ratio | 1.08 |
| n_words | 13.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.981 |
| nli_faithfulness | 0.984 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 39.52 |
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

**output:** The patient does not appear to have an obvious infected sore right now, even though there is some drainage.

| metric | value |
|---|---:|
| bertscore_f1 | 0.596 |
| coleman_liau | 9.20 |
| coleman_liau_drop | 0.34 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 8.59 |
| fkgl_drop | -0.98 |
| fre | 67.3 |
| fre_gain | -1.6 |
| human_edit_recall | 1.000 |
| length_ratio | 1.12 |
| n_words | 19.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.994 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.600 |
| sari | 24.73 |
| severity_preservation | 1.000 |
| smog | 11.21 |
| smog_drop | -2.37 |

### Stage 4 - arm `termonly`

**output:** I do not think she has an obvious current pus-filled sore, although there is some fluid leaking out.

| metric | value |
|---|---:|
| bertscore_f1 | 0.770 |
| coleman_liau | 8.33 |
| coleman_liau_drop | 1.20 |
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
| nli_completeness | 0.989 |
| nli_faithfulness | 0.977 |
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
| `drainage` -> `fluid leaking out` | replace | - | - | - | - | - | - | - |

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
| `abscessed lesion` -> `infected sore` | replace | attributed | 1.194 | 1.950 | 0.789 | 0.905 | 0.008 | - |
| `drainage` -> `fluid leaking out` | replace | attributed | 0.351 | 0.517 | 0.836 | 0.889 | 0.846 | - |

**edit `abscessed lesion` -> `infected sore`**

- status: `attributed`
- log p full -0.4807, empty -1.6748
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.468` [michigan] lesion: A sore or any part of your sking that looks different from the rest.
    - `+0.460` [nih] lesion: An area of abnormal tissue. A lesion may be benign (not cancer) or malignant (cancer).
    - `+0.382` [justplainclear] lesion: Wound; sore; infected patch of skin
    - `+0.357` [readme] LESION: A lesion is a type of damage or change in tissue caused by disease or injury.
    - `+0.252` [readme] drainage: When any fluid is leaking out of a body part.

- rationale: An abscessed lesion is a pocket of pus caused by infection, so "infected sore" conveys the same idea in everyday language. Phrase frequency rises from Zipf 1.60 to 3.75, and age of acquisition drops from 12.82 to 5.84. Readers can grasp that the area is infected and painful without needing medical terminology.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `drainage` -> `fluid leaking out`**

- status: `attributed`
- log p full -0.9687, empty -1.3193
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+1.007` [readme] drainage: When any fluid is leaking out of a body part.
    - `+0.161` [justplainclear] lesion: Wound; sore; infected patch of skin
    - `+0.112` [readme] LESION: A lesion is a type of damage or change in tissue caused by disease or injury.
    - `+0.057` [iowa] LESION: wound or injury; a diseased patch of skin
    - `+0.023` [wiktionary] drainage: To use a drainage is engage in the action or process of draining something.

- rationale: "Drainage" refers to the removal or flow of liquid from a body area, and "fluid leaking out" conveys this process in everyday terms. Word frequency decreases from Zipf 3.77 to 3.58, while age of acquisition drops from 10.84 to 7.94. Readers can grasp that liquid is escaping the body without needing medical terminology.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

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

**output:** At this time, the patient would receive fluids through a vein and be checked again.

| metric | value |
|---|---:|
| bertscore_f1 | 0.652 |
| coleman_liau | 8.13 |
| coleman_liau_drop | 3.96 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 5.21 |
| fkgl_drop | 3.88 |
| fre | 84.5 |
| fre_gain | 34.9 |
| human_edit_recall | 1.000 |
| length_ratio | 1.15 |
| n_words | 15.0 |
| nli_completeness | 0.797 |
| nli_faithfulness | 0.886 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 31.98 |
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
| `rehydrate` -> `give fluids by vein` | replace | attributed | -0.181 | -0.437 | - | 0.873 | 0.000 | - |
| `reassess` -> `check again` | replace | attributed | 0.028 | 0.324 | - | 0.857 | 0.253 | - |

**edit `rehydrate` -> `give fluids by vein`**

- status: `attributed`
- log p full -0.6320, empty -0.4508
- masks scored: 10/10 (+3 top-k)
- ranked sources:
    - `-0.421` [wiktionary] rehydrate: If you rehydrate something, you supply it with water to make it moist or wet again.

- rationale: "Rehydrate" means to restore lost body fluids, and "give fluids by vein" conveys this action in everyday terms. Phrase frequency rises from Zipf 2.20 to 3.45, and age of acquisition drops from 13.63 to 8.53. Readers can grasp how the treatment restores hydration without needing medical jargon.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `reassess` -> `check again`**

- status: `attributed`
- log p full -0.0770, empty -0.1050
- masks scored: 10/10 (+3 top-k)
- ranked sources:
    - `+0.263` [readme] intravenous fluid: Fluids that go straight into a vein through a needle.
    - `+0.010` [wiktionary] reassess: If you reassess a person, idea, skill, process, etc., you judge or measure them again.
    - `-0.030` [wiktionary] rehydrate: If you rehydrate something, you supply it with water to make it moist or wet again.

- rationale: "Reassess" means to evaluate something once more, and "check again" conveys that same action in everyday language. Phrase frequency rises from Zipf 2.80 to 5.16, and age of acquisition drops from 12.79 to 5.78. This phrasing helps patients recognize that their condition will be reviewed another time.
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

**output:** The findings suggest acute appendicitis.

| metric | value |
|---|---:|
| bertscore_f1 | 0.454 |
| coleman_liau | 18.88 |
| coleman_liau_drop | 0.99 |
| copy_jargon_rate | 1.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 12.32 |
| fkgl_drop | 1.96 |
| fre | 15.6 |
| fre_gain | 12.3 |
| human_edit_recall | 0.000 |
| length_ratio | 0.56 |
| n_words | 5.0 |
| nli_completeness | 0.955 |
| nli_faithfulness | 0.976 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 11.81 |
| smog | 8.84 |
| smog_drop | 2.37 |
| temporality_preservation | 1.000 |
| uncertainty_preservation | 0.000 |

### Stage 4 - arm `termonly`

**output:** The results suggest a sudden inflamed appendix.

| metric | value |
|---|---:|
| bertscore_f1 | 0.465 |
| coleman_liau | 13.11 |
| coleman_liau_drop | 6.75 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.286 |
| fkgl | 9.05 |
| fkgl_drop | 5.23 |
| fre | 42.6 |
| fre_gain | 39.3 |
| human_edit_recall | 1.000 |
| length_ratio | 0.78 |
| n_words | 7.0 |
| nli_completeness | 0.894 |
| nli_faithfulness | 0.845 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 10.95 |
| smog | 8.84 |
| smog_drop | 2.37 |
| temporality_preservation | 0.000 |
| uncertainty_preservation | 0.000 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `acute appendicitis` -> `sudden inflamed appendix` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** The results suggest sudden appendix swelling.

| metric | value |
|---|---:|
| bertscore_f1 | 0.470 |
| coleman_liau | 16.97 |
| coleman_liau_drop | 2.90 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.286 |
| fkgl | 10.35 |
| fkgl_drop | 3.93 |
| fre | 31.5 |
| fre_gain | 28.2 |
| human_edit_recall | 1.000 |
| length_ratio | 0.67 |
| n_words | 6.0 |
| nli_completeness | 0.851 |
| nli_faithfulness | 0.899 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 11.25 |
| smog | 8.84 |
| smog_drop | 2.37 |
| temporality_preservation | 0.000 |
| uncertainty_preservation | 0.000 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `compatible with` -> `suggest` | replace | attributed | 0.248 | 0.640 | 0.090 | 0.815 | 0.018 | - |
| `acute appendicitis` -> `sudden appendix swelling` | replace | attributed | 0.997 | 1.237 | 0.810 | 0.931 | 0.620 | - |

**edit `compatible with` -> `suggest`**

- status: `attributed`
- log p full -0.3770, empty -0.6250
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.188` [wiktionary] acute: If an angle is acute, it is less than 90 degrees in size.
    - `+0.170` [wiktionary] compatible: Things or people are compatible when they can work and communicate with each other without problem
    - `+0.067` [iowa] ACUTE: new, recent, sudden, urgent
    - `+0.032` [wiktionary] with: With is used to show the other people or things present when something happened.
    - `+0.027` [thesaurus] acute: sudden start, short term, quick

- rationale: "Compatible with" indicates that findings align with a particular diagnosis, and "suggest" conveys this supportive relationship in simpler terms. Word frequency rises from Zipf 3.97 to 4.75, age of acquisition drops from 10.16 to 8.67, and syllable count decreases from 5 to 2. Readers can grasp that the evidence points toward a condition without navigating formal diagnostic phrasing.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `acute appendicitis` -> `sudden appendix swelling`**

- status: `attributed`
- log p full -1.2007, empty -2.1973
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.745` [readme] appendicitis: Appendicitis is when your appendix gets swollen and inflamed, typically causing stomach pain.
    - `+0.125` [wiktionary] acute: If an angle is acute, it is less than 90 degrees in size.
    - `+0.077` [wiktionary] with: With is used to describe something added to something else.
    - `+0.018` [wiktionary] findings: A finding is the information from a research or an investigation.
    - `+0.003` [justplainclear] acute: Sudden start, doesn't last long

- rationale: The glossary defines appendicitis as swelling and inflammation of the appendix, so "sudden appendix swelling" captures that core idea in everyday words. Phrase frequency rises from Zipf 2.74 to 3.25, and age of acquisition drops from 12.00 to 10.56. Readers can grasp that the appendix is inflamed without needing the clinical label.
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

**output:** She says she has not lost weight, but she has had less appetite and more tiredness all over her body for the past 3-4 months.

| metric | value |
|---|---:|
| bertscore_f1 | 0.631 |
| coleman_liau | 5.75 |
| coleman_liau_drop | 10.48 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.286 |
| fkgl | 8.79 |
| fkgl_drop | 1.68 |
| fre | 76.6 |
| fre_gain | 26.3 |
| human_edit_recall | 1.000 |
| length_ratio | 1.44 |
| n_words | 26.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.994 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.143 |
| sari | 47.48 |
| smog | 11.21 |
| smog_drop | 1.82 |
| temporality_preservation | 1.000 |

### Stage 4 - arm `termonly`

**output:** She says she has not lost weight, but she said she has had less hunger and more tiredness all over for the past 3-4 months.

| metric | value |
|---|---:|
| bertscore_f1 | 0.626 |
| coleman_liau | 5.29 |
| coleman_liau_drop | 10.95 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.250 |
| fkgl | 7.85 |
| fkgl_drop | 2.63 |
| fre | 83.3 |
| fre_gain | 33.1 |
| human_edit_recall | 1.000 |
| length_ratio | 1.44 |
| n_words | 26.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.994 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.125 |
| sari | 44.97 |
| smog | 8.84 |
| smog_drop | 4.18 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `decreased appetite` -> `less hunger` | replace | - | - | - | - | - | - | - |
| `generalized fatigue` -> `tiredness all over` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** She says she did not lose weight, but admitted she wanted to eat less and felt tired all over for the past 3-4 months.

| metric | value |
|---|---:|
| bertscore_f1 | 0.608 |
| coleman_liau | 5.20 |
| coleman_liau_drop | 11.04 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.375 |
| fkgl | 8.03 |
| fkgl_drop | 2.45 |
| fre | 80.3 |
| fre_gain | 30.0 |
| human_edit_recall | 1.000 |
| length_ratio | 1.39 |
| n_words | 25.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.991 |
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
| `acknowledged` -> `admitted` | replace | attributed | 0.648 | 1.063 | 0.756 | 0.916 | 0.931 | - |

**edit `acknowledged` -> `admitted`**

- status: `attributed`
- log p full -0.6562, empty -1.3047
- masks scored: 66/66 (+2 top-k)
- ranked sources:
    - `+1.245` [wiktionary] acknowledged: If you acknowledge a fact or a situation, you accept or admit that it is true or that it exists.
    - `+0.314` [wiktionary] appetite: When you have appetite, you feel hungry and would like to eat some food.
    - `+0.150` [nih] appetite: A desire to satisfy a physical or mental need, such as for food, sex, or adventure.
    - `+0.115` [wiktionary] fatigue: Fatigue is the material failure, such as cracking or separation, caused by stress on the material.
    - `+0.066` [wiktionary] denies: If you deny something, you say it didn't happen or isn't true.

- rationale: "Acknowledged" means to accept or recognize something as true, and "admitted" conveys this same idea of openly accepting a fact in simpler terms. The word frequency increases from Zipf 4.08 to 4.49, indicating the replacement is more common, while the syllable count remains unchanged at 3. This allows readers to grasp the concept of accepting information without encountering less familiar vocabulary.
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

**output:** The doctors are thinking about doing surgery to remove the rest of the thyroid gland.

| metric | value |
|---|---:|
| bertscore_f1 | 0.377 |
| coleman_liau | 9.29 |
| coleman_liau_drop | 18.87 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.333 |
| fkgl | 8.35 |
| fkgl_drop | 13.41 |
| fre | 61.9 |
| fre_gain | 113.9 |
| human_edit_recall | 1.000 |
| length_ratio | 1.67 |
| n_words | 15.0 |
| nli_completeness | 0.942 |
| nli_faithfulness | 0.108 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 33.47 |
| smog | 8.84 |
| smog_drop | 4.18 |
| uncertainty_preservation | 0.000 |

### Stage 4 - arm `termonly`

**output:** The doctors thought about finishing the surgery to remove the thyroid.

| metric | value |
|---|---:|
| bertscore_f1 | 0.335 |
| coleman_liau | 12.62 |
| coleman_liau_drop | 15.54 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.333 |
| fkgl | 9.08 |
| fkgl_drop | 12.68 |
| fre | 49.5 |
| fre_gain | 101.6 |
| human_edit_recall | 1.000 |
| length_ratio | 1.22 |
| n_words | 11.0 |
| nli_completeness | 0.990 |
| nli_faithfulness | 0.413 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 32.04 |
| smog | 11.21 |
| smog_drop | 1.82 |
| uncertainty_preservation | 0.000 |

annotation backend `novita`, 0 edits kept


### Stage 4 - arm `grounded`

**output:** They thought about finishing the surgery to remove the thyroid.

| metric | value |
|---|---:|
| bertscore_f1 | 0.363 |
| coleman_liau | 11.98 |
| coleman_liau_drop | 16.18 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.333 |
| fkgl | 8.37 |
| fkgl_drop | 13.39 |
| fre | 52.9 |
| fre_gain | 104.9 |
| human_edit_recall | 1.000 |
| length_ratio | 1.11 |
| n_words | 10.0 |
| nli_completeness | 0.985 |
| nli_faithfulness | 0.942 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 32.18 |
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

**output:** She says she had a nosebleed a few days ago. It needed packing in her nose to stop the bleeding, but it has now healed.

| metric | value |
|---|---:|
| bertscore_f1 | 0.643 |
| coleman_liau | 3.18 |
| coleman_liau_drop | 7.25 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.400 |
| fkgl | 3.45 |
| fkgl_drop | 7.01 |
| fre | 92.6 |
| fre_gain | 38.7 |
| human_edit_recall | 1.000 |
| length_ratio | 1.19 |
| n_words | 25.0 |
| nli_completeness | 0.173 |
| nli_faithfulness | 0.758 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 28.39 |
| smog | 3.13 |
| smog_drop | 8.08 |
| temporality_preservation | 1.000 |

### Stage 4 - arm `termonly`

**output:** She notes that she had a nosebleed a few days ago, needing cotton in her nose, and fortunately that had stopped now.

| metric | value |
|---|---:|
| bertscore_f1 | 0.792 |
| coleman_liau | 7.11 |
| coleman_liau_drop | 3.31 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.333 |
| fkgl | 8.54 |
| fkgl_drop | 1.91 |
| fre | 73.0 |
| fre_gain | 19.0 |
| human_edit_recall | 1.000 |
| length_ratio | 1.05 |
| n_words | 22.0 |
| nli_completeness | 0.878 |
| nli_faithfulness | 0.949 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 48.86 |
| smog | 8.84 |
| smog_drop | 2.37 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 4 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `epistaxis` -> `a nosebleed` | replace | - | - | - | - | - | - | - |
| `requiring` -> `needing` | replace | - | - | - | - | - | - | - |
| `nasal packing` -> `cotton in her nose` | replace | - | - | - | - | - | - | - |
| `resolved` -> `stopped` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** She notes that she had a nosebleed a few days ago, needing material put in her nose to help it heal, and fortunately that has stopped now.

| metric | value |
|---|---:|
| bertscore_f1 | 0.727 |
| coleman_liau | 6.52 |
| coleman_liau_drop | 3.90 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 10.67 |
| fkgl_drop | -0.22 |
| fre | 66.6 |
| fre_gain | 12.7 |
| human_edit_recall | 1.000 |
| length_ratio | 1.29 |
| n_words | 27.0 |
| nli_completeness | 0.855 |
| nli_faithfulness | 0.925 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 44.12 |
| smog | 11.21 |
| smog_drop | 0.00 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 4 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `epistaxis` -> `a nosebleed` | replace | attributed | 0.056 | 2.748 | 0.644 | 0.911 | 0.134 | - |
| `requiring` -> `needing` | replace | attributed | 0.098 | 1.110 | 0.754 | 0.901 | 0.416 | - |
| `nasal packing` -> `material put in her nose to help it heal` | replace | attributed | 14.878 | 14.986 | 0.831 | 0.885 | 11.421 | - |
| `resolved` -> `stopped` | replace | attributed | 0.262 | 0.453 | 0.566 | 0.870 | 0.378 | - |

**edit `epistaxis` -> `a nosebleed`**

- status: `attributed`
- log p full -0.0040, empty -0.0605
- masks scored: 66/66 (+8 top-k)
- ranked sources:
    - `+2.027` [readme] Epistaxis: A nosebleed.
    - `+1.893` [readme] EPISTAXIS: EPISTAXIS: It's a nosebleed.
    - `+0.509` [wiktionary] resolved: When a problem is resolved, it has been brought to a successful solution.
    - `+0.410` [wiktionary] requiring: If you require something, you need it.
    - `+0.263` [readme] Nasal: Nasal means having to do with the nose.

- rationale: "Epistaxis" is the medical term for bleeding from the nose, so "a nosebleed" conveys the same condition in everyday language. Word frequency increases from Zipf 1.60 to 2.51, while syllable count rises from 2 to 3. Patients can immediately recognize the symptom without needing to decode clinical terminology.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `requiring` -> `needing`**

- status: `attributed`
- log p full -0.0518, empty -0.1494
- masks scored: 66/66 (+8 top-k)
- ranked sources:
    - `+0.526` [wiktionary] requiring: If you require something, you need it.
    - `+0.110` [justplainclear] nasal: Relating to your nose
    - `+0.092` [readme] packing: Putting something into a wound to help it heal.
    - `+0.052` [readme] EPISTAXIS: EPISTAXIS: It's a nosebleed.
    - `+0.029` [wiktionary] packing: When you pack something, you put it in a container to carry with you.

- rationale: "Requiring" means something is necessary, and "needing" conveys that same necessity in simpler terms. Word frequency decreases from Zipf 4.14 to 4.02, while syllable count drops from 4 to 2. Readers can grasp the necessity of the action without encountering a more formal verb.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `nasal packing` -> `material put in her nose to help it heal`**

- status: `attributed`
- log p full -2.2734, empty -17.1509
- masks scored: 66/66 (+8 top-k)
- ranked sources:
    - `+11.830` [readme] packing: Putting something into a wound to help it heal.
    - `+0.408` [readme] EPISTAXIS: EPISTAXIS: It's a nosebleed.
    - `+0.238` [wiktionary] packing: You put packing around an object to protect it.
    - `+0.135` [readme] nasal: It's all about your nose when we talk about "nasal."
    - `+0.077` [wiktionary] requiring: If you require something, you need it.

- rationale: The glossary defines nasal packing as putting something into a wound to help it heal, so "material put in her nose to help it heal" conveys that purpose in everyday language. Phrase frequency rises from Zipf 3.39 to 3.91, and age of acquisition drops from 8.75 to 8.06. Patients can grasp how the treatment supports healing without needing the clinical term.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `resolved` -> `stopped`**

- status: `attributed`
- log p full -0.7383, empty -1.0000
- masks scored: 66/66 (+8 top-k)
- ranked sources:
    - `+0.639` [wiktionary] epistaxis: Epistaxis is bleeding from the nose.
    - `+0.261` [wiktionary] requiring: If you require something, you need it.
    - `+0.242` [michigan] nasal: Things that are related to the nose.
    - `+0.157` [wiktionary] resolved: When a problem is resolved, it has been brought to a successful solution.
    - `+0.129` [readme] Nasal: Nasal means having to do with the nose.

- rationale: "Resolved" means that a condition or symptom has come to an end, and "stopped" conveys this same idea in simpler, everyday language. The word becomes more common, with its Zipf frequency rising from 4.10 to 4.84, and shorter, dropping from 2 syllables to 1. This allows patients to immediately grasp that the issue is no longer present without needing to interpret clinical terminology.
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

**output:** I also explained conscious sedation to the patient.

| metric | value |
|---|---:|
| bertscore_f1 | 0.850 |
| coleman_liau | 11.68 |
| coleman_liau_drop | 0.17 |
| copy_jargon_rate | 1.000 |
| critical_error | 0.000 |
| fkgl | 8.18 |
| fkgl_drop | 0.72 |
| fre | 50.7 |
| fre_gain | 3.4 |
| human_edit_recall | 0.000 |
| length_ratio | 0.89 |
| n_words | 8.0 |
| nli_completeness | 0.993 |
| nli_faithfulness | 0.994 |
| replacement_f1 | 0.000 |
| rewrite_aggressiveness | 1.000 |
| sari | 27.00 |
| smog | 8.84 |
| smog_drop | 0.00 |

### Stage 4 - arm `termonly`

**output:** I also explained to the patient about being awake but relaxed during the procedure.

| metric | value |
|---|---:|
| bertscore_f1 | 0.723 |
| coleman_liau | 10.67 |
| coleman_liau_drop | 1.17 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 10.10 |
| fkgl_drop | -1.20 |
| fre | 47.6 |
| fre_gain | 0.3 |
| human_edit_recall | 1.000 |
| length_ratio | 1.56 |
| n_words | 14.0 |
| nli_completeness | 0.218 |
| nli_faithfulness | 0.038 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 64.33 |
| smog | 8.84 |
| smog_drop | 0.00 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `conscious sedation` -> `being awake but relaxed during the procedure` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** I also explained to the patient about light sedation.

| metric | value |
|---|---:|
| bertscore_f1 | 0.913 |
| coleman_liau | 9.27 |
| coleman_liau_drop | 2.58 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 7.59 |
| fkgl_drop | 1.31 |
| fre | 56.7 |
| fre_gain | 9.4 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 9.0 |
| nli_completeness | 0.039 |
| nli_faithfulness | 0.015 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 66.67 |
| smog | 8.84 |
| smog_drop | 0.00 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `conscious sedation` -> `light sedation` | replace | attributed | 1.699 | 2.056 | - | 1.000 | 2.027 | - |

**edit `conscious sedation` -> `light sedation`**

- status: `attributed`
- log p full -1.0666, empty -2.7660
- masks scored: 6/6 (+1 top-k)
- ranked sources:
    - `+1.910` [readme] conscious sedation: Medication given to a patient to make them lightly sedated and forgetful during a procedur
    - `-0.116` [nih] conscious sedation: A level of sedation in which a person is asleep but wakes when spoken to or touched. Consc

- rationale: Conscious sedation refers to a state where patients remain responsive but relaxed, which "light sedation" conveys in simpler terms. Phrase frequency increases from Zipf 2.93 to 2.95, and syllable count decreases from 5 to 4. Patients can grasp the level of sedation without needing to interpret the clinical terminology.
- audit: coverage 0.5, grounding_error=False, omission=True, source_ok=True, passage_ok=True

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

**output:** When the doctor felt her right knee, there was no grinding or crackling sound.

| metric | value |
|---|---:|
| bertscore_f1 | 0.525 |
| coleman_liau | 8.19 |
| coleman_liau_drop | 1.31 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 4.20 |
| fkgl_drop | 1.03 |
| fre | 89.9 |
| fre_gain | 18.1 |
| human_edit_recall | 1.000 |
| laterality_preservation | 1.000 |
| length_ratio | 1.56 |
| n_words | 14.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.702 |
| nli_faithfulness | 0.468 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 28.93 |
| smog | 3.13 |
| smog_drop | 5.71 |

### Stage 4 - arm `termonly`

**output:** Feeling her right knee shows no grinding.

| metric | value |
|---|---:|
| bertscore_f1 | 0.608 |
| coleman_liau | 8.14 |
| coleman_liau_drop | 1.36 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 2.31 |
| fkgl_drop | 2.92 |
| fre | 91.0 |
| fre_gain | 19.1 |
| human_edit_recall | 1.000 |
| laterality_preservation | 1.000 |
| length_ratio | 0.78 |
| n_words | 7.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.930 |
| nli_faithfulness | 0.942 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 32.26 |
| smog | 3.13 |
| smog_drop | 5.71 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `crepitus` -> `grinding` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Feeling her right knee shows no grinding.

| metric | value |
|---|---:|
| bertscore_f1 | 0.608 |
| coleman_liau | 8.14 |
| coleman_liau_drop | 1.36 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 2.31 |
| fkgl_drop | 2.92 |
| fre | 91.0 |
| fre_gain | 19.1 |
| human_edit_recall | 1.000 |
| laterality_preservation | 1.000 |
| length_ratio | 0.78 |
| n_words | 7.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.930 |
| nli_faithfulness | 0.942 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 32.26 |
| smog | 3.13 |
| smog_drop | 5.71 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `crepitus` -> `grinding` | replace | attributed | 0.004 | 0.007 | - | 0.716 | 0.064 | - |

**edit `crepitus` -> `grinding`**

- status: `attributed`
- log p full -0.7383, empty -0.7422
- masks scored: 34/34 (+2 top-k)
- ranked sources:
    - `+0.066` [nih] palpation: Examination by pressing on the surface of the body to feel the organs or tissues underneath.
    - `+0.001` [readme] palpation: Feeling a part of the body with your hands.
    - `-0.083` [readme] Palpation: Feeling a part of the body.
    - `-0.223` [dictionary] Crepitus (n.): The noise produced by a sudden discharge of wind from the bowels.

- rationale: Crepitus refers to a grating or crackling sensation, so "grinding" conveys that tactile experience in everyday language. Word frequency rises from Zipf 1.39 to 3.94, while the syllable count remains at two. Readers can grasp the physical sensation of the joint without needing the clinical term.
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

**output:** She twisted her ankle the evening before.

| metric | value |
|---|---:|
| bertscore_f1 | 0.757 |
| coleman_liau | 8.14 |
| coleman_liau_drop | 4.19 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 5.68 |
| fkgl_drop | 4.42 |
| fre | 66.8 |
| fre_gain | 19.2 |
| length_ratio | 0.64 |
| n_words | 7.0 |
| nli_completeness | 0.002 |
| nli_faithfulness | 0.994 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.200 |
| sari | 29.95 |
| smog | 3.13 |
| smog_drop | 8.08 |
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
| `the evening prior` -> `the night before` | replace | attributed | -0.131 | -0.392 | - | 0.439 | 0.014 | - |

**edit `the evening prior` -> `the night before`**

- status: `attributed`
- log p full -0.4758, empty -0.3447
- masks scored: 10/10 (+2 top-k)
- ranked sources:
    - `-0.014` [wiktionary] prior: If something happens prior to something else, it happens before it.
    - `-0.252` [wiktionary] evening: You use even to focus on the most surprising or unlikely case.

- rationale: "The evening prior" refers to the night before a specific event, and "the night before" expresses this same timing in everyday language. Phrase frequency rises from Zipf 4.55 to 5.44, age of acquisition drops from 10.63 to 5.45, and syllable count decreases from 5 to 4. Readers can immediately grasp when to prepare without parsing formal phrasing.
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

**output:** Things that change the condition: The patient's condition is made worse by throwing.

| metric | value |
|---|---:|
| bertscore_f1 | 0.505 |
| coleman_liau | 12.71 |
| coleman_liau_drop | 3.65 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.750 |
| fkgl | 6.73 |
| fkgl_drop | 7.42 |
| fre | 70.0 |
| fre_gain | 60.3 |
| human_edit_recall | 1.000 |
| length_ratio | 1.40 |
| n_words | 14.0 |
| nli_completeness | 0.981 |
| nli_faithfulness | 0.990 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 58.33 |
| smog | 11.21 |
| smog_drop | 1.82 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `aggravated` -> `made worse` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Things that change the condition: The patient's condition is made worse by throwing.

| metric | value |
|---|---:|
| bertscore_f1 | 0.505 |
| coleman_liau | 12.71 |
| coleman_liau_drop | 3.65 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.750 |
| fkgl | 6.73 |
| fkgl_drop | 7.42 |
| fre | 70.0 |
| fre_gain | 60.3 |
| human_edit_recall | 1.000 |
| length_ratio | 1.40 |
| n_words | 14.0 |
| nli_completeness | 0.981 |
| nli_faithfulness | 0.990 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 58.33 |
| smog | 11.21 |
| smog_drop | 1.82 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `aggravated` -> `made worse` | replace | attributed | 0.128 | 1.506 | - | 0.738 | 0.602 | - |

**edit `aggravated` -> `made worse`**

- status: `attributed`
- log p full -0.0398, empty -0.1682
- masks scored: 18/18 (+2 top-k)
- ranked sources:
    - `+0.928` [wiktionary] aggravated: To aggravate is to make something worse.
    - `+0.326` [readme] aggravated: To make a problem or injury worse.
    - `+0.057` [wiktionary] factors: A factor is one of a number of things that causes a result.
    - `-0.062` [wiktionary] modifying: If you modify something, you change it, often only in small ways, and often because you want to use

- rationale: "Aggravated" means to make a condition more severe, so "made worse" conveys that same idea in everyday language. Word frequency rises from Zipf 3.47 to 4.85, and the syllable count drops from 4 to 2. This phrasing helps patients clearly see that their symptoms have intensified.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

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

**output:** History of joint wear, weak bones, low thyroid, nose allergies and kidney stones.

| metric | value |
|---|---:|
| bertscore_f1 | 0.632 |
| coleman_liau | 10.92 |
| coleman_liau_drop | 16.72 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 6.73 |
| fkgl_drop | 14.62 |
| fre | 70.0 |
| fre_gain | 110.2 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 13.0 |
| nli_completeness | 0.947 |
| nli_faithfulness | 0.876 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 62.18 |
| smog | 11.21 |
| smog_drop | 4.70 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 4 edits kept

- rejected: DROP noop      'kidney stones' -> 'kidney stones'  (nothing changed)

| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `osteoarthritis` -> `joint wear` | replace | - | - | - | - | - | - | - |
| `osteoporosis` -> `weak bones` | replace | - | - | - | - | - | - | - |
| `hypothyroidism` -> `low thyroid` | replace | - | - | - | - | - | - | - |
| `allergic rhinitis` -> `nose allergies` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** History of joint wear, weak bones, low thyroid, hay fever, and kidney stones.

| metric | value |
|---|---:|
| bertscore_f1 | 0.737 |
| coleman_liau | 8.69 |
| coleman_liau_drop | 18.95 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 5.82 |
| fkgl_drop | 15.53 |
| fre | 76.5 |
| fre_gain | 116.7 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 13.0 |
| nli_completeness | 0.919 |
| nli_faithfulness | 0.943 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 72.04 |
| smog | 8.84 |
| smog_drop | 7.06 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 4 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `osteoarthritis` -> `joint wear` | replace | attributed | 0.314 | 0.753 | 0.849 | 0.906 | 0.592 | - |
| `osteoporosis` -> `weak bones` | replace | attributed | 0.268 | 2.528 | 0.640 | 0.821 | 0.263 | - |
| `hypothyroidism` -> `low thyroid` | replace | attributed | -0.460 | -1.665 | 0.762 | 0.911 | 0.072 | - |
| `allergic rhinitis` -> `hay fever` | replace | attributed | 2.399 | 3.359 | 0.643 | 0.766 | 0.438 | - |

**edit `osteoarthritis` -> `joint wear`**

- status: `attributed`
- log p full -0.3984, empty -0.7129
- masks scored: 66/66 (+8 top-k)
- ranked sources:
    - `+0.834` [justplainclear] osteoarthritis: A form of arthritis caused by the wear and tear of joints
    - `+0.242` [wiktionary] osteoporosis: Osteoporosis is a disease in which the bones become very porous and brittle.
    - `+0.160` [justplainclear] hypothyroidism: A condition where your thyroid isn't active enough, so you have low hormone levels Hypothyroid
    - `+0.116` [readme] Osteoporosis: Osteoporosis is a condition where bones become weak and more prone to fractures.
    - `+0.084` [readme] osteoarthritis: Arthritis that happens when the cushioning between joints wears out.

- rationale: Osteoarthritis refers to the gradual breakdown of joint cartilage, so "joint wear" captures this degenerative process in everyday language. Word frequency rises from Zipf 2.76 to 4.50, and the syllable count drops from 6 to 2. Readers can grasp the physical cause of their pain without needing to decode a complex medical label.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `osteoporosis` -> `weak bones`**

- status: `attributed`
- log p full -0.0271, empty -0.2954
- masks scored: 66/66 (+8 top-k)
- ranked sources:
    - `+1.025` [readme] Osteoporosis: Osteoporosis is a condition where bones become weak and more prone to fractures.
    - `+0.763` [readme] osteoporosis: Osteoporosis is when bones become weak and prone to breaking because they lose density.
    - `+0.423` [readme] osteoarthritis: Osteoarthritis is a painful joint condition caused by the wearing down of bone tissue, leading
    - `+0.373` [michigan] osteoporosis: When your bones are weak break easily. Also called brittle done disease.
    - `+0.265` [nih] osteoporosis: A condition in which there is a decrease in the amount and thickness of bone tissue. This causes

- rationale: Osteoporosis refers to a condition where bones become fragile and prone to breaking, so "weak bones" conveys this physical state in everyday language. Phrase frequency rises from Zipf 2.99 to 4.16, age of acquisition drops from 14.29 to 5.58, and syllable count decreases from 6 to 2. Readers can grasp the core issue of bone fragility without needing to interpret a complex medical diagnosis.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `hypothyroidism` -> `low thyroid`**

- status: `attributed`
- log p full -0.6059, empty -0.1464
- masks scored: 66/66 (+8 top-k)
- ranked sources:
    - `+0.131` [readme] kidney stones: Hard mineral deposits in the kidneys causing pain and blockage.
    - `+0.059` [readme] Osteoporosis: Osteoporosis is a condition where bones become weak and more prone to fractures.
    - `+0.057` [justplainclear] hypothyroidism: A condition where your thyroid isn't active enough, so you have low hormone levels Hypothyroid
    - `+0.014` [wiktionary] osteoporosis: Osteoporosis is a disease in which the bones become very porous and brittle.

- rationale: Hypothyroidism refers to an underactive thyroid gland, so "low thyroid" conveys this condition using everyday language. Phrase frequency increases from Zipf 2.68 to 3.52, and age of acquisition decreases from 15.43 to 13.83. Readers can grasp that the thyroid is not producing enough hormone without needing the clinical term.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `allergic rhinitis` -> `hay fever`**

- status: `attributed`
- log p full -0.4474, empty -2.8460
- masks scored: 66/66 (+8 top-k)
- ranked sources:
    - `+1.279` [justplainclear] allergic rhinitis: Also known as: hay fever A condition where you have an allergic reaction that affects the n
    - `+0.841` [michigan] allergic rhinitis: Caused by your body's reaction in your nose to mold, pollen, or dust. Also called hay fever
    - `+0.365` [iowa] OSTEOPOROSIS: softening of the bones
    - `+0.296` [justplainclear] osteoarthritis: A form of arthritis caused by the wear and tear of joints
    - `+0.236` [justplainclear] hypothyroidism: A condition where your thyroid isn't active enough, so you have low hormone levels Hypothyroid

- rationale: The glossary defines allergic rhinitis as a nasal allergic reaction, so "hay fever" conveys this condition in everyday language. Phrase frequency rises from Zipf 2.37 to 3.74, and age of acquisition drops from 18.07 to 5.84. Readers can recognize the familiar term for their nasal allergy symptoms.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

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

**output:** The ultrasound did not show any bleeding inside the skull.

| metric | value |
|---|---:|
| bertscore_f1 | 0.755 |
| coleman_liau | 9.08 |
| coleman_liau_drop | 11.49 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| diagnostic_identity_preservation | 1.000 |
| fkgl | 6.01 |
| fkgl_drop | 9.79 |
| fre | 69.8 |
| fre_gain | 75.5 |
| human_edit_recall | 1.000 |
| length_ratio | 1.11 |
| n_words | 10.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.952 |
| nli_faithfulness | 0.960 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 23.93 |
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
| `intracranial hemorrhage` -> `bleeding inside the brain` | replace | attributed | 4.939 | 6.364 | - | 0.800 | 2.982 | - |

**edit `intracranial hemorrhage` -> `bleeding inside the brain`**

- status: `attributed`
- log p full -0.2733, empty -5.2126
- masks scored: 6/6 (+1 top-k)
- ranked sources:
    - `+4.698` [readme] INTRACRANIAL HEMORRHAGE: Bleeding inside your brain.
    - `+1.717` [readme] intracranial hemorrhage: Bleeding within the brain.

- rationale: "Intracranial hemorrhage" refers to bleeding within the skull, so "bleeding inside the brain" conveys this critical event in everyday language. Phrase frequency rises from Zipf 2.55 to 4.00, and age of acquisition drops from 14.94 to 5.76. Readers can immediately grasp the nature of the injury without needing specialized medical vocabulary.
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

**output:** He had his appendix removed using small cuts and a camera, and he is able to eat food without any problems.

| metric | value |
|---|---:|
| bertscore_f1 | 0.399 |
| coleman_liau | 6.27 |
| coleman_liau_drop | 6.88 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.333 |
| fkgl | 10.02 |
| fkgl_drop | 4.64 |
| fre | 60.6 |
| fre_gain | 49.3 |
| human_edit_recall | 1.000 |
| length_ratio | 1.40 |
| n_words | 21.0 |
| nli_completeness | 0.937 |
| nli_faithfulness | 0.401 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 31.94 |
| smog | 11.21 |
| smog_drop | 1.82 |
| temporality_preservation | 0.000 |

### Stage 4 - arm `termonly`

**output:** He had his appendix removed through small cuts, and he can eat food by mouth.

| metric | value |
|---|---:|
| bertscore_f1 | 0.464 |
| coleman_liau | 5.81 |
| coleman_liau_drop | 7.34 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.333 |
| fkgl | 4.42 |
| fkgl_drop | 10.24 |
| fre | 90.1 |
| fre_gain | 78.7 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 15.0 |
| nli_completeness | 0.888 |
| nli_faithfulness | 0.617 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 23.01 |
| smog | 8.84 |
| smog_drop | 4.18 |
| temporality_preservation | 0.000 |

annotation backend `novita`, 0 edits kept


### Stage 4 - arm `grounded`

**output:** He had surgery to remove his appendix through small cuts, and he can eat food by mouth.

| metric | value |
|---|---:|
| bertscore_f1 | 0.487 |
| coleman_liau | 6.00 |
| coleman_liau_drop | 7.15 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.333 |
| fkgl | 6.31 |
| fkgl_drop | 8.35 |
| fre | 80.1 |
| fre_gain | 68.7 |
| human_edit_recall | 1.000 |
| length_ratio | 1.13 |
| n_words | 17.0 |
| nli_completeness | 0.876 |
| nli_faithfulness | 0.720 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 27.66 |
| smog | 11.21 |
| smog_drop | 1.82 |
| temporality_preservation | 0.000 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `laparoscopic appendicectomy` -> `surgery to remove his appendix through small cuts` | replace | attributed | 0.469 | 0.492 | 0.314 | 0.697 | 0.245 | - |
| `oral` -> `by mouth` | replace | attributed | 0.072 | 0.432 | 0.444 | 0.878 | 0.077 | - |

**edit `laparoscopic appendicectomy` -> `surgery to remove his appendix through small cuts`**

- status: `attributed`
- log p full -2.8038, empty -3.2725
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.353` [readme] laparoscopic: A surgery where a small tube with a camera is used to see inside the body.
    - `+0.107` [readme] Laparoscopic: A surgery that uses a small tube and camera to see inside your body.
    - `+0.049` [wiktionary] post: Post is the letters and parcels that you send to other people.

- rationale: "Laparoscopic appendicectomy" refers to the surgical removal of the appendix using a minimally invasive technique, which the replacement phrase clarifies by describing the procedure as surgery through small cuts. The word frequency increases significantly from a Zipf score of 0.00 to 3.40, although the syllable count rises from 10 to 13. This allows the patient to grasp the nature of the operation without needing to understand complex medical terminology.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `oral` -> `by mouth`**

- status: `attributed`
- log p full -0.1494, empty -0.2217
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.320` [readme] Oral: Oral means something you take by mouth.
    - `+0.244` [nih] oral: By or having to do with the mouth.
    - `+0.203` [nih] diet: The things a person eats and drinks.
    - `+0.185` [wiktionary] diet: A diet is a controlled set of foods chosen for health purposes.
    - `+0.142` [wiktionary] diet: A diet is the food that an animal, person, or group usually eats.

- rationale: "Oral" means relating to the mouth, so "by mouth" conveys the same route of administration in everyday language. Phrase frequency increases from Zipf 4.26 to 4.82, and age of acquisition falls from 9.39 to 5.41. Patients can clearly understand how to take the medication without needing to interpret clinical terminology.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

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

**output:** We think that her walking is most likely not affected by the hydrocephalus.

| metric | value |
|---|---:|
| bertscore_f1 | 0.773 |
| coleman_liau | 9.58 |
| coleman_liau_drop | 1.09 |
| copy_jargon_rate | 1.000 |
| critical_error | 0.000 |
| fkgl | 6.73 |
| fkgl_drop | 1.69 |
| fre | 70.0 |
| fre_gain | 10.3 |
| human_edit_recall | 0.000 |
| length_ratio | 0.72 |
| n_words | 13.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.993 |
| nli_faithfulness | 0.992 |
| replacement_f1 | 0.000 |
| rewrite_aggressiveness | 1.000 |
| sari | 23.68 |
| smog | 11.21 |
| smog_drop | 0.00 |
| uncertainty_preservation | 1.000 |

### Stage 4 - arm `termonly`

**output:** We believe that her walking is most likely not being affected by the buildup of fluid in the brain.

| metric | value |
|---|---:|
| bertscore_f1 | 0.943 |
| coleman_liau | 7.06 |
| coleman_liau_drop | 3.61 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 8.59 |
| fkgl_drop | -0.18 |
| fre | 67.3 |
| fre_gain | 7.7 |
| human_edit_recall | 1.000 |
| length_ratio | 1.06 |
| n_words | 19.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.332 |
| nli_faithfulness | 0.701 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 81.31 |
| smog | 8.84 |
| smog_drop | 2.37 |
| uncertainty_preservation | 1.000 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `hydrocephalus` -> `buildup of fluid in the brain` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** We believe that her walking is most likely not being affected by the fluid buildup in her brain.

| metric | value |
|---|---:|
| bertscore_f1 | 0.926 |
| coleman_liau | 7.69 |
| coleman_liau_drop | 2.98 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 8.47 |
| fkgl_drop | -0.06 |
| fre | 66.4 |
| fre_gain | 6.7 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 18.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.395 |
| nli_faithfulness | 0.432 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 72.92 |
| smog | 8.84 |
| smog_drop | 2.37 |
| uncertainty_preservation | 1.000 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `hydrocephalus` -> `fluid buildup in her brain` | replace | attributed | 1.707 | 1.978 | - | 0.832 | 0.731 | - |

**edit `hydrocephalus` -> `fluid buildup in her brain`**

- status: `attributed`
- log p full -1.2874, empty -2.9941
- masks scored: 18/18 (+2 top-k)
- ranked sources:
    - `+1.338` [nih] hydrocephalus: The abnormal buildup of cerebrospinal fluid in the ventricles of the brain.
    - `+0.606` [justplainclear] hydrocephalus: Also known as: water on the brain A condition where there is too much cerebrospinal fluid in yo
    - `+0.494` [readme] HYDROCEPHALUS: When fluid around the brain builds up too much.
    - `+0.128` [readme] hydrocephalus: Swelling of brain due to excess fluid.

- rationale: Hydrocephalus refers to an abnormal accumulation of cerebrospinal fluid within the brain, so "fluid buildup in her brain" conveys this condition using everyday language. Phrase frequency increases from Zipf 2.32 to 3.30, and age of acquisition falls from 15.78 to 9.63. This phrasing helps patients grasp the physical cause of their symptoms without needing to interpret a complex medical label.
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

**output:** She reported feeling tired, lightheaded, and very short of breath when she was active.

| metric | value |
|---|---:|
| bertscore_f1 | 0.667 |
| coleman_liau | 11.09 |
| coleman_liau_drop | 6.28 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.333 |
| fkgl | 8.41 |
| fkgl_drop | 3.89 |
| fre | 59.7 |
| fre_gain | 33.2 |
| human_edit_recall | 1.000 |
| length_ratio | 0.93 |
| n_words | 14.0 |
| nli_completeness | 0.987 |
| nli_faithfulness | 0.985 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.143 |
| sari | 26.48 |
| severity_downgrade | 1.000 |
| severity_preservation | 0.000 |
| severity_tier_input | 3.000 |
| smog | 11.21 |
| smog_drop | 1.82 |

### Stage 4 - arm `termonly`

**output:** She reported feeling tired, dizzy, and very short of breath when active.

| metric | value |
|---|---:|
| bertscore_f1 | 0.662 |
| coleman_liau | 9.77 |
| coleman_liau_drop | 7.60 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.333 |
| fkgl | 7.77 |
| fkgl_drop | 4.53 |
| fre | 60.7 |
| fre_gain | 34.2 |
| human_edit_recall | 1.000 |
| length_ratio | 0.80 |
| n_words | 12.0 |
| nli_completeness | 0.991 |
| nli_faithfulness | 0.992 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.143 |
| sari | 26.63 |
| severity_downgrade | 1.000 |
| severity_preservation | 0.000 |
| severity_tier_input | 3.000 |
| smog | 8.84 |
| smog_drop | 4.18 |

annotation backend `novita`, 4 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `noted complaints of` -> `reported` | replace | - | - | - | - | - | - | - |
| `fatigue` -> `tired` | replace | - | - | - | - | - | - | - |
| `lightheadedness` -> `dizzy` | replace | - | - | - | - | - | - | - |
| `dyspnea on exertion` -> `very short of breath when active` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** She reported feeling tired, dizzy, and very short of breath when active.

| metric | value |
|---|---:|
| bertscore_f1 | 0.662 |
| coleman_liau | 9.77 |
| coleman_liau_drop | 7.60 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.333 |
| fkgl | 7.77 |
| fkgl_drop | 4.53 |
| fre | 60.7 |
| fre_gain | 34.2 |
| human_edit_recall | 1.000 |
| length_ratio | 0.80 |
| n_words | 12.0 |
| nli_completeness | 0.991 |
| nli_faithfulness | 0.992 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.143 |
| sari | 26.63 |
| severity_downgrade | 1.000 |
| severity_preservation | 0.000 |
| severity_tier_input | 3.000 |
| smog | 8.84 |
| smog_drop | 4.18 |

annotation backend `novita`, 4 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `noted complaints of` -> `reported` | replace | attributed | 0.137 | 0.329 | 0.451 | 0.775 | 0.053 | - |
| `fatigue` -> `tired` | replace | attributed | -0.508 | -3.114 | 0.827 | 0.950 | 0.650 | - |
| `lightheadedness` -> `dizzy` | replace | attributed | 0.056 | 1.754 | 0.829 | 0.933 | 1.551 | - |
| `dyspnea on exertion` -> `very short of breath when active` | replace | attributed | -0.471 | -0.735 | 0.506 | 0.595 | 0.062 | - |

**edit `noted complaints of` -> `reported`**

- status: `attributed`
- log p full -0.4727, empty -0.6094
- masks scored: 66/66 (+8 top-k)
- ranked sources:
    - `+0.147` [wiktionary] on: positioned at the upper surface of, touching from above
    - `+0.095` [dictionary] Of (prep.): Denoting that from which anything proceeds; indicating origin, source, descent, and the like; as, 
    - `+0.087` [readme] lightheadedness: Feeling dizzy or almost faint.
    - `+0.036` [dictionary] Of (prep.): In a general sense, from, or out from; proceeding from; belonging to; relating to; concerning; -- 
    - `+0.024` [nih] fatigue: A condition marked by extreme tiredness and inability to function due to lack of energy. Fatigue may 

- rationale: "Noted complaints of" means that a patient mentioned symptoms, and "reported" conveys this action more directly. Word frequency increases from Zipf 4.10 to 5.00, while syllable count drops from 5 to 3. Readers can quickly grasp that the patient shared their symptoms without navigating complex phrasing.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `fatigue` -> `tired`**

- status: `attributed`
- log p full -0.5391, empty -0.0312
- masks scored: 66/66 (+8 top-k)
- ranked sources:
    - `+1.173` [wiktionary] exertion: An exertion is the expenditure of physical or mental effort.
    - `+0.523` [wiktionary] on: positioned at the upper surface of, touching from above
    - `+0.470` [thesaurus] exertion: effort, work
    - `+0.446` [dictionary] Of (prep.): In a general sense, from, or out from; proceeding from; belonging to; relating to; concerning; -- 
    - `+0.172` [wiktionary] on: at the date of

- rationale: "Fatigue" refers to a state of extreme tiredness, so "tired" conveys the same feeling in simpler terms. Word frequency increases from Zipf 3.86 to 4.71, and age of acquisition falls from 11.83 to 4.62. Patients can recognize the sensation of exhaustion without needing to interpret a clinical term.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `lightheadedness` -> `dizzy`**

- status: `attributed`
- log p full -0.0121, empty -0.0679
- masks scored: 66/66 (+8 top-k)
- ranked sources:
    - `+2.059` [readme] lightheadedness: Feeling dizzy or almost faint.
    - `+0.507` [readme] dyspnea: Having a hard time breathing or feeling like you can't catch your breath.
    - `+0.299` [wiktionary] noted: A note is a single sound in music.
    - `+0.202` [readme] Dyspnea: Struggling to breathe, feeling out of breath.
    - `+0.164` [wiktionary] on: positioned at the upper surface of, touching from above

- rationale: "Lightheadedness" refers to a sensation of faintness or unsteadiness, which "dizzy" captures in a more familiar and concise way. Word frequency rises from Zipf 1.92 to 3.43, age of acquisition drops from 10.11 to 5.50, and syllable count decreases from 4 to 2. Readers can quickly grasp the feeling of imbalance without navigating a complex medical descriptor.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `dyspnea on exertion` -> `very short of breath when active`**

- status: `attributed`
- log p full -1.2796, empty -0.8083
- masks scored: 66/66 (+8 top-k)
- ranked sources:
    - `+0.066` [readme] Dyspnea: Struggling to breathe, feeling out of breath.
    - `+0.004` [readme] Complaints: A problem or sickness that a person talks about.

- rationale: "Dyspnea on exertion" means breathlessness triggered by physical activity, so "very short of breath when active" conveys that same idea in everyday language. Phrase frequency rises from Zipf 2.09 to 4.32, and age of acquisition drops from 11.58 to 6.53. Readers can recognize the symptom without needing medical terminology.
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

**output:** There is no significant swelling on the back of the hand related to these.

| metric | value |
|---|---:|
| bertscore_f1 | 0.664 |
| coleman_liau | 6.94 |
| coleman_liau_drop | 2.07 |
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
| nli_completeness | 0.925 |
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

**output:** No major swelling linked to these on the back of the hand.

| metric | value |
|---|---:|
| bertscore_f1 | 0.784 |
| coleman_liau | 3.97 |
| coleman_liau_drop | 5.05 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.667 |
| fkgl | 2.86 |
| fkgl_drop | 8.08 |
| fre | 96.0 |
| fre_gain | 54.4 |
| human_edit_recall | 1.000 |
| length_ratio | 0.86 |
| n_words | 12.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.914 |
| nli_faithfulness | 0.601 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 38.22 |
| severity_downgrade | 1.000 |
| severity_preservation | 0.000 |
| severity_tier_input | 2.000 |
| smog | 3.13 |
| smog_drop | 9.89 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `significant amount` -> `major` | replace | - | - | - | - | - | - | - |
| `associated with` -> `linked to` | replace | - | - | - | - | - | - | - |
| `dorsum` -> `back` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** No big swelling linked to these on the back of the hand.

| metric | value |
|---|---:|
| bertscore_f1 | 0.724 |
| coleman_liau | 3.00 |
| coleman_liau_drop | 6.01 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.667 |
| fkgl | 1.87 |
| fkgl_drop | 9.07 |
| fre | 103.0 |
| fre_gain | 61.5 |
| human_edit_recall | 1.000 |
| length_ratio | 0.86 |
| n_words | 12.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.918 |
| nli_faithfulness | 0.572 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 38.22 |
| severity_downgrade | 0.000 |
| severity_preservation | 0.000 |
| severity_tier_input | 2.000 |
| severity_tier_output | 2.000 |
| smog | 3.13 |
| smog_drop | 9.89 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `edema` -> `swelling` | replace | attributed | 0.072 | 1.280 | 0.179 | 0.768 | 0.033 | - |
| `associated with` -> `linked to` | replace | attributed | 0.312 | 1.147 | 0.509 | 0.819 | 0.305 | - |
| `dorsum` -> `back` | replace | attributed | 0.172 | 0.745 | 0.454 | 0.786 | 0.003 | - |

**edit `edema` -> `swelling`**

- status: `attributed`
- log p full -0.0293, empty -0.1016
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+0.480` [nih] significant: In statistics, describes a mathematical measure of difference between groups. The difference is s
    - `+0.447` [justplainclear] associated with: Linked to, related to, goes along with, is part of
    - `+0.416` [nih] edema: Swelling caused by excess fluid in body tissues.
    - `+0.090` [justplainclear] significant: Big, serious, important, major
    - `+0.048` [wiktionary] significant: If something is significant, it is important, or large, enough to pay attention to or to believe.

- rationale: Edema refers to fluid buildup in tissues, so "swelling" conveys that same physical change in everyday language. Word frequency rises from Zipf 2.95 to 3.68, and the word shortens from three syllables to two. Readers can recognize the visible sign of fluid retention without needing a medical term.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `associated with` -> `linked to`**

- status: `attributed`
- log p full -0.1865, empty -0.4980
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+0.586` [readme] associated with: Linked to something.
    - `+0.281` [nih] significant: In statistics, describes a mathematical measure of difference between groups. The difference is s
    - `+0.246` [michigan] significant: Big or important.
    - `+0.140` [justplainclear] associated with: Linked to, related to, goes along with, is part of
    - `+0.096` [michigan] edema: Swelling caused by too much fluid in your body.

- rationale: "Associated with" means that two things tend to occur together, and "linked to" expresses that same connection in simpler terms. Word frequency decreases from Zipf 4.89 to 4.54, while age of acquisition drops from 4.44 to 3.95. Readers can grasp the relationship between the conditions without navigating formal academic phrasing.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `dorsum` -> `back`**

- status: `attributed`
- log p full -0.1855, empty -0.3574
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+0.171` [readme] edema: Swelling due to too much fluid in the body tissues.
    - `+0.168` [nih] edema: Swelling caused by excess fluid in body tissues.
    - `+0.125` [readme] dorsum: The dorsum is basically the back or upper surface.
    - `+0.121` [justplainclear] significant: Big, serious, important, major
    - `+0.066` [nih] significant: In statistics, describes a mathematical measure of difference between groups. The difference is s

- rationale: "Dorsum" refers to the upper surface or back of a body part, so "back" conveys this anatomical direction in everyday language. Word frequency rises from Zipf 2.47 to 6.04, and the word becomes shorter, dropping from 2 syllables to 1. Readers can instantly recognize the location being described without needing specialized anatomical vocabulary.
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

**output:** The patient has no heart or lung problems.

| metric | value |
|---|---:|
| bertscore_f1 | 0.578 |
| coleman_liau | 5.15 |
| coleman_liau_drop | 6.77 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 2.28 |
| fkgl_drop | 10.04 |
| fre | 93.0 |
| fre_gain | 77.3 |
| human_edit_recall | 1.000 |
| length_ratio | 1.60 |
| n_words | 8.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.992 |
| nli_faithfulness | 0.980 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 52.02 |
| smog | 3.13 |
| smog_drop | 8.08 |

### Stage 4 - arm `termonly`

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
| `cardio` -> `heart` | replace | attributed | 0.004 | 0.285 | 0.449 | 0.701 | 0.074 | - |
| `pulmonary` -> `lung` | replace | attributed | 0.000 | 0.934 | 0.582 | 0.835 | 0.271 | - |

**edit `cardio` -> `heart`**

- status: `attributed`
- log p full -0.0134, empty -0.0178
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.231` [readme] pulmonary: Related to the lungs.
    - `+0.157` [readme] Pulmonary: About the lungs.
    - `+0.019` [thesaurus] pulmonary: related to the lungs
    - `-0.026` [iowa] PULMONARY: pertaining to the lungs

- rationale: "Cardio" refers to the heart, so "heart" conveys the same meaning in plain language. Word frequency increases from Zipf 3.44 to 5.31, and syllables decrease from 3 to 1. Patients can understand the reference to the heart without needing to know the medical prefix.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `pulmonary` -> `lung`**

- status: `attributed`
- log p full -0.0003, empty -0.0007
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.457` [readme] Pulmonary: About the lungs.
    - `+0.186` [readme] pulmonary: Related to the lungs.
    - `+0.186` [nih] pulmonary: Having to do with the lungs.
    - `+0.102` [thesaurus] pulmonary: related to the lungs
    - `+0.062` [iowa] PULMONARY: pertaining to the lungs

- rationale: "Pulmonary" refers to the lungs, so "lung" conveys the same anatomical meaning in everyday language. Word frequency rises from Zipf 3.50 to 4.10, and age of acquisition drops from 13.05 to 7.16. Readers can immediately identify the body part involved without needing specialized medical vocabulary.
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

**output:** At that time, the Coreg had been stopped because of low blood pressure.

| metric | value |
|---|---:|
| bertscore_f1 | 0.791 |
| coleman_liau | 7.35 |
| coleman_liau_drop | 1.05 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.250 |
| fkgl | 3.10 |
| fkgl_drop | 3.84 |
| fre | 96.0 |
| fre_gain | 31.1 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 13.0 |
| nli_completeness | 0.817 |
| nli_faithfulness | 0.859 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 76.67 |
| smog | 3.13 |
| smog_drop | 8.08 |

### Stage 4 - arm `termonly`

**output:** At that time, the blood pressure medicine had been held because of low blood pressure.

| metric | value |
|---|---:|
| bertscore_f1 | 0.712 |
| coleman_liau | 9.29 |
| coleman_liau_drop | -0.89 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.400 |
| fkgl | 5.99 |
| fkgl_drop | 0.94 |
| fre | 78.8 |
| fre_gain | 13.9 |
| human_edit_recall | 1.000 |
| length_ratio | 1.15 |
| n_words | 15.0 |
| nli_completeness | 0.183 |
| nli_faithfulness | 0.772 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 66.79 |
| smog | 8.84 |
| smog_drop | 2.37 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `Coreg` -> `blood pressure medicine` | replace | - | - | - | - | - | - | - |
| `secondary to` -> `because of` | replace | - | - | - | - | - | - | - |
| `hypotension` -> `low blood pressure` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** At that time, the blood pressure medicine had been held because of low blood pressure.

| metric | value |
|---|---:|
| bertscore_f1 | 0.712 |
| coleman_liau | 9.29 |
| coleman_liau_drop | -0.89 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.400 |
| fkgl | 5.99 |
| fkgl_drop | 0.94 |
| fre | 78.8 |
| fre_gain | 13.9 |
| human_edit_recall | 1.000 |
| length_ratio | 1.15 |
| n_words | 15.0 |
| nli_completeness | 0.183 |
| nli_faithfulness | 0.772 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 66.79 |
| smog | 8.84 |
| smog_drop | 2.37 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `Coreg` -> `blood pressure medicine` | replace | attributed | -0.291 | -0.393 | 0.828 | 0.854 | 0.094 | - |
| `secondary to` -> `because of` | replace | attributed | 0.021 | 0.115 | 0.071 | 0.589 | 0.038 | - |
| `hypotension` -> `low blood pressure` | replace | attributed | 0.002 | 2.437 | 0.551 | 0.786 | 0.007 | - |

**edit `Coreg` -> `blood pressure medicine`**

- status: `attributed`
- log p full -1.4980, empty -1.2075
- masks scored: 66/66 (+5 top-k)
- ranked sources:
    - `+0.184` [wiktionary] secondary: second, next in order to the first or primary.
    - `+0.090` [wiktionary] to: To shows where something goes, the goal of movement.
    - `+0.069` [nih] hypotension: Abnormally low blood pressure.
    - `+0.013` [wiktionary] to: To has no meaning. It is used with a bare infinitival clause.
    - `+0.001` [wiktionary] hypotension: Hypotension is the disease of having low blood pressure.

- rationale: "Coreg" is a brand name for a medication that lowers blood pressure, so "blood pressure medicine" conveys its purpose in everyday language. Word frequency rises from Zipf 1.16 to 4.44, making the phrase more common, though syllable count increases from 1 to 6. Patients can recognize the treatment’s goal without needing to know the specific brand name.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `secondary to` -> `because of`**

- status: `attributed`
- log p full -0.1855, empty -0.2061
- masks scored: 66/66 (+5 top-k)
- ranked sources:
    - `+0.107` [wiktionary] secondary: second, next in order to the first or primary.
    - `+0.069` [michigan] hypotension: When your blood pressure is low. For some people, this is normal, but it may cause problems for o
    - `-0.001` [wiktionary] to: To shows where something goes, the goal of movement.

- rationale: "Secondary to" means that one condition arises as a result of another, so "because of" conveys this causal link in everyday language. Phrase frequency rises from Zipf 4.53 to 6.01, age of acquisition drops from 9.11 to 4.55, and syllable count decreases from 5 to 3. Readers can immediately grasp why one health issue led to another without parsing formal medical phrasing.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `hypotension` -> `low blood pressure`**

- status: `attributed`
- log p full -0.0001, empty -0.0017
- masks scored: 66/66 (+5 top-k)
- ranked sources:
    - `+0.264` [readme] hypotension: Low blood pressure.
    - `+0.257` [readme] Hypotension: Hypotension means low blood pressure.
    - `+0.132` [wiktionary] secondary: of less than primary importance.
    - `+0.107` [wiktionary] to: To shows where something goes, the goal of movement.
    - `+0.052` [wiktionary] hypotension: Hypotension is the disease of having low blood pressure.

- rationale: Hypotension refers to abnormally low blood pressure, so the replacement "low blood pressure" conveys the same clinical meaning in everyday language. Phrase frequency rises from Zipf 2.52 to 4.65, and age of acquisition drops from 14.41 to 8.95. Readers can immediately grasp that their blood pressure is below the normal range without needing to interpret a medical term.
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

**output:** Her diarrhea has improved, and she is having less trouble with bladder control and less swelling in her feet.

| metric | value |
|---|---:|
| bertscore_f1 | 0.563 |
| coleman_liau | 9.81 |
| coleman_liau_drop | 1.18 |
| copy_jargon_rate | 0.333 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 9.21 |
| fkgl_drop | 3.57 |
| fre | 62.9 |
| fre_gain | 30.9 |
| human_edit_recall | 0.667 |
| length_ratio | 1.12 |
| n_words | 19.0 |
| nli_completeness | 0.916 |
| nli_faithfulness | 0.816 |
| replacement_f1 | 0.800 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.429 |
| sari | 42.52 |
| smog | 8.84 |
| smog_drop | 5.71 |
| temporality_preservation | 0.000 |

### Stage 4 - arm `termonly`

**output:** Her loose stools have settled down and she is having less urine leakage, less swelling in her feet.

| metric | value |
|---|---:|
| bertscore_f1 | 0.743 |
| coleman_liau | 8.33 |
| coleman_liau_drop | 2.65 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 6.51 |
| fkgl_drop | 6.27 |
| fre | 80.5 |
| fre_gain | 48.5 |
| human_edit_recall | 1.000 |
| length_ratio | 1.06 |
| n_words | 18.0 |
| nli_completeness | 0.920 |
| nli_faithfulness | 0.939 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.167 |
| sari | 54.84 |
| smog | 3.13 |
| smog_drop | 11.43 |
| temporality_preservation | 0.000 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `diarrhea` -> `loose stools` | replace | - | - | - | - | - | - | - |
| `urinary incontinence` -> `urine leakage` | replace | - | - | - | - | - | - | - |
| `pedal edema` -> `swelling in her feet` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Her loose, watery poop has settled down and she is having less loss of bladder control, less swollen feet.

| metric | value |
|---|---:|
| bertscore_f1 | 0.752 |
| coleman_liau | 8.59 |
| coleman_liau_drop | 2.40 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 7.97 |
| fkgl_drop | 4.81 |
| fre | 71.8 |
| fre_gain | 39.8 |
| human_edit_recall | 1.000 |
| length_ratio | 1.12 |
| n_words | 19.0 |
| nli_completeness | 0.961 |
| nli_faithfulness | 0.970 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.167 |
| sari | 62.90 |
| smog | 8.84 |
| smog_drop | 5.71 |
| temporality_preservation | 0.000 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `diarrhea` -> `loose, watery poop` | replace | attributed | 8.145 | 8.310 | 0.864 | 0.913 | 2.929 | - |
| `urinary incontinence` -> `loss of bladder control` | replace | attributed | 1.454 | 1.738 | 0.882 | 0.870 | 1.680 | - |
| `pedal edema` -> `swollen feet` | replace | attributed | 3.853 | 5.946 | 0.759 | 0.927 | 7.363 | - |

**edit `diarrhea` -> `loose, watery poop`**

- status: `attributed`
- log p full -1.8843, empty -10.0298
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+4.030` [readme] diarrhea: Having loose, watery poop with cramps and bloating.
    - `+1.101` [wiktionary] diarrhea: Diarrhea is an illness where the person's poop or feces are soft like water.
    - `+1.071` [justplainclear] diarrhea: A bowel movement that is loose and watery If your poop is like water or very runny, or if you have m
    - `+0.432` [michigan] urinary incontinence: When you lose control of your bladder and the fluids it holds.
    - `+0.298` [readme] urinary incontinence: When you can't control your pee.

- rationale: The glossary defines diarrhea as having loose, watery poop with cramps and bloating, so the replacement captures this core description in everyday language. Word frequency decreases from Zipf 3.55 to 3.05, and syllable count increases from 4 to 5. Readers can recognize the symptom by its physical characteristics rather than its medical label.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `urinary incontinence` -> `loss of bladder control`**

- status: `attributed`
- log p full -1.2036, empty -2.6571
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+1.895` [michigan] urinary incontinence: When you lose control of your bladder and the fluids it holds.
    - `+0.214` [wiktionary] diarrhea: Diarrhea is an illness where the person's poop or feces are soft like water.
    - `+0.211` [readme] diarrhea: Having loose, watery poop with cramps and bloating.

- rationale: The Michigan glossary defines urinary incontinence as losing control of the bladder and its fluids, so "loss of bladder control" captures this meaning in everyday language. Phrase frequency rises from Zipf 2.77 to 3.60, and age of acquisition drops from 14.41 to 10.78. Readers can grasp the core issue of involuntary leakage without needing the clinical term.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `pedal edema` -> `swollen feet`**

- status: `attributed`
- log p full -0.1289, empty -3.9814
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+7.946` [readme] pedal edema: Swollen feet.
    - `+0.583` [michigan] diarrhea: Loose, watery stools three or more times a day. It can be sudden (due to a virus, for example), pers
    - `+0.270` [michigan] urinary incontinence: When you lose control of your bladder and the fluids it holds.
    - `+0.182` [readme] urinary incontinence: When you can't control your pee.
    - `+0.073` [readme] diarrhea: Having loose, watery poop with cramps and bloating.

- rationale: The glossary defines pedal edema as swollen feet, so the replacement directly conveys this physical symptom in everyday language. Phrase frequency increases from Zipf 2.87 to 3.55, and the syllable count drops from 5 to 3. Readers can immediately recognize the condition as swelling in the feet without needing medical terminology.
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

**output:** The patient has nausea and belly pain after eating because of gallbladder disease. A laparoscopic cholecystectomy is scheduled.

| metric | value |
|---|---:|
| bertscore_f1 | 0.399 |
| coleman_liau | 15.71 |
| coleman_liau_drop | 9.94 |
| copy_jargon_rate | 1.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 12.18 |
| fkgl_drop | 7.26 |
| fre | 23.8 |
| fre_gain | 44.9 |
| human_edit_recall | 0.000 |
| length_ratio | 1.00 |
| n_words | 18.0 |
| nli_completeness | 0.364 |
| nli_faithfulness | 0.985 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.250 |
| sari | 19.81 |
| smog | 11.21 |
| smog_drop | 4.70 |
| temporality_preservation | 1.000 |

### Stage 4 - arm `termonly`

**output:** Feeling sick and belly pain after eating - gallbladder problem - surgery to remove the gallbladder scheduled.

| metric | value |
|---|---:|
| bertscore_f1 | 0.570 |
| coleman_liau | 17.03 |
| coleman_liau_drop | 8.62 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.375 |
| fkgl | 12.29 |
| fkgl_drop | 7.15 |
| fre | 33.7 |
| fre_gain | 54.8 |
| human_edit_recall | 1.000 |
| length_ratio | 0.83 |
| n_words | 15.0 |
| nli_completeness | 0.933 |
| nli_faithfulness | 0.992 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.125 |
| sari | 29.57 |
| smog | 13.02 |
| smog_drop | 2.88 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 0 edits kept


### Stage 4 - arm `grounded`

**output:** Feeling sick and belly pain after eating - gallbladder problem - surgery to remove the gallbladder is planned.

| metric | value |
|---|---:|
| bertscore_f1 | 0.558 |
| coleman_liau | 14.97 |
| coleman_liau_drop | 10.67 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.375 |
| fkgl | 11.30 |
| fkgl_drop | 8.13 |
| fre | 42.5 |
| fre_gain | 63.7 |
| human_edit_recall | 1.000 |
| length_ratio | 0.89 |
| n_words | 16.0 |
| nli_completeness | 0.917 |
| nli_faithfulness | 0.991 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.222 |
| sari | 27.73 |
| smog | 13.02 |
| smog_drop | 2.88 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `abdominal pain` -> `belly pain` | replace | attributed | -0.351 | -1.118 | 0.755 | 0.919 | 0.199 | - |
| `Gall bladder disease` -> `gallbladder problem` | replace | attributed | 1.463 | 1.647 | 0.469 | 0.841 | 0.070 | - |
| `Laparoscopic cholecystectomy` -> `surgery to remove the gallbladder` | replace | attributed | 0.261 | 0.412 | 0.494 | 0.748 | 0.061 | - |

**edit `abdominal pain` -> `belly pain`**

- status: `attributed`
- log p full -0.5791, empty -0.2283
- masks scored: 66/66 (+5 top-k)
- ranked sources:
    - `+0.253` [justplainclear] bladder disease: A disease or disorder of your bladder. Some bladder diseases may include: • urinary incontine
    - `+0.054` [justplainclear] nausea: Feeling like you want to throw up, stomach feels upset
    - `+0.053` [wiktionary] gall: If you have the gall to do something, you do it even though it is very rude or unreasonable.
    - `+0.007` [nih] nausea: A feeling of sickness or discomfort in the stomach that may come with an urge to vomit. Nausea is a si

- rationale: "Abdominal pain" refers to discomfort in the stomach area, and "belly pain" conveys this same sensation using everyday language. The phrase becomes more common, with Zipf frequency rising from 3.56 to 4.05, and easier to process, as age of acquisition drops from 10.24 to 4.26 while syllable count decreases from 5 to 3. This allows patients to immediately recognize the location of their discomfort without needing medical terminology.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `Gall bladder disease` -> `gallbladder problem`**

- status: `attributed`
- log p full -1.5718, empty -3.0352
- masks scored: 66/66 (+5 top-k)
- ranked sources:
    - `+0.484` [readme] cholecystectomy: A surgery to remove the gallbladder, a digestion-assisting organ in the stomach.
    - `+0.414` [justplainclear] bladder disease: A disease or disorder of your bladder. Some bladder diseases may include: • urinary incontine
    - `+0.280` [readme] Cholecystectomy: A surgery to remove the gallbladder, an organ in your stomach that helps with digestion.
    - `+0.011` [justplainclear] cholecystectomy: A surgery to take out your gallbladder

- rationale: "Gall bladder disease" refers to medical conditions affecting the organ that stores bile, and "gallbladder problem" conveys this same idea using simpler, everyday language. Word frequency decreases from Zipf 3.12 to 2.81, while age of acquisition drops from 12.44 to 11.68. This phrasing helps patients recognize the issue without needing to interpret formal diagnostic terminology.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `Laparoscopic cholecystectomy` -> `surgery to remove the gallbladder`**

- status: `attributed`
- log p full -0.8781, empty -1.1387
- masks scored: 66/66 (+5 top-k)
- ranked sources:
    - `+0.223` [readme] cholecystectomy: A surgery to remove the gallbladder, a digestion-assisting organ in the stomach.
    - `+0.162` [readme] Cholecystectomy: A surgery to remove the gallbladder, an organ in your stomach that helps with digestion.
    - `+0.083` [wiktionary] gall: Gall is anger or hatred.
    - `+0.080` [nih] nausea: A feeling of sickness or discomfort in the stomach that may come with an urge to vomit. Nausea is a si

- rationale: Laparoscopic cholecystectomy is a minimally invasive procedure to remove the gallbladder, and the replacement "surgery to remove the gallbladder" conveys this core action in everyday language. Word frequency increases from Zipf 1.73 to 2.80, indicating the new phrase is more common, while the syllable count remains unchanged at 10. Patients can now grasp the essential nature of the operation without needing to decode specialized surgical terminology.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

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

**output:** She says she has a history of heart disease, but she cannot give many details.

| metric | value |
|---|---:|
| bertscore_f1 | 0.623 |
| coleman_liau | 6.20 |
| coleman_liau_drop | 4.07 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.125 |
| fkgl | 6.78 |
| fkgl_drop | 5.49 |
| fre | 73.2 |
| fre_gain | 30.4 |
| human_edit_recall | 1.000 |
| length_ratio | 0.68 |
| n_words | 15.0 |
| negation_preservation | 0.000 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.994 |
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

**output:** She says she has a history of heart disease but cannot give many details.

| metric | value |
|---|---:|
| bertscore_f1 | 0.621 |
| coleman_liau | 6.53 |
| coleman_liau_drop | 3.74 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.125 |
| fkgl | 6.73 |
| fkgl_drop | 5.54 |
| fre | 71.8 |
| fre_gain | 29.1 |
| human_edit_recall | 1.000 |
| length_ratio | 0.64 |
| n_words | 14.0 |
| negation_preservation | 0.000 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.994 |
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

annotation backend `novita`, 0 edits kept


### Stage 4 - arm `grounded`

**output:** She says she has a history of heart disease but cannot give many details.

| metric | value |
|---|---:|
| bertscore_f1 | 0.621 |
| coleman_liau | 6.53 |
| coleman_liau_drop | 3.74 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.125 |
| fkgl | 6.73 |
| fkgl_drop | 5.54 |
| fre | 71.8 |
| fre_gain | 29.1 |
| human_edit_recall | 1.000 |
| length_ratio | 0.64 |
| n_words | 14.0 |
| negation_preservation | 0.000 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.994 |
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

annotation backend `novita`, 0 edits kept


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

**output:** The fourth toe was slightly swollen, and he was still wearing his wedding band on it.

| metric | value |
|---|---:|
| bertscore_f1 | 0.656 |
| coleman_liau | 7.00 |
| coleman_liau_drop | 0.04 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.333 |
| fkgl | 5.40 |
| fkgl_drop | 1.11 |
| fre | 84.8 |
| fre_gain | 4.4 |
| human_edit_recall | 1.000 |
| length_ratio | 0.89 |
| n_words | 16.0 |
| nli_completeness | 0.992 |
| nli_faithfulness | 0.984 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.667 |
| sari | 28.17 |
| severity_downgrade | 0.000 |
| severity_preservation | 1.000 |
| severity_tier_input | 1.000 |
| severity_tier_output | 1.000 |
| smog | 3.13 |
| smog_drop | 5.71 |

### Stage 4 - arm `termonly`

**output:** There was some slight swelling of the fourth toe, on which he still is wearing his wedding band.

| metric | value |
|---|---:|
| bertscore_f1 | 0.962 |
| coleman_liau | 7.37 |
| coleman_liau_drop | -0.32 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.667 |
| fkgl | 5.20 |
| fkgl_drop | 1.31 |
| fre | 89.9 |
| fre_gain | 9.4 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 18.0 |
| nli_completeness | 0.987 |
| nli_faithfulness | 0.926 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 83.33 |
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
| `fourth digit` -> `fourth toe` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** There was slight swelling of the fourth finger, on which he still is wearing his wedding band.

| metric | value |
|---|---:|
| bertscore_f1 | 0.980 |
| coleman_liau | 8.39 |
| coleman_liau_drop | -1.34 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.667 |
| fkgl | 5.62 |
| fkgl_drop | 0.89 |
| fre | 85.1 |
| fre_gain | 4.6 |
| human_edit_recall | 1.000 |
| length_ratio | 0.94 |
| n_words | 17.0 |
| nli_completeness | 0.990 |
| nli_faithfulness | 0.989 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 83.97 |
| severity_downgrade | 0.000 |
| severity_preservation | 1.000 |
| severity_tier_input | 1.000 |
| severity_tier_output | 1.000 |
| smog | 3.13 |
| smog_drop | 5.71 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `edema` -> `swelling` | replace | attributed | -0.000 | -0.361 | 0.032 | 0.486 | 0.608 | - |
| `fourth digit` -> `fourth finger` | replace | attributed | 0.798 | 1.658 | 0.378 | 0.790 | 0.228 | - |

**edit `edema` -> `swelling`**

- status: `attributed`
- log p full -0.0014, empty -0.0010
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.742` [nih] edema: Swelling caused by excess fluid in body tissues.
    - `+0.134` [readme] Edema: Swelling in the body caused by too much fluid.
    - `+0.132` [michigan] digit: A finger or toe.
    - `+0.120` [readme] edema: Swelling due to too much fluid in the body tissues.
    - `+0.061` [readme] digit: A digit is a finger or toe.

- rationale: Edema refers to fluid buildup in tissues, so "swelling" conveys that same physical change in everyday language. Word frequency rises from Zipf 2.95 to 3.68, and the word shortens from three syllables to two. Readers can recognize the visible sign of fluid retention without needing a medical term.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `fourth digit` -> `fourth finger`**

- status: `attributed`
- log p full -0.3389, empty -1.1367
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.510` [readme] digit: A digit is a finger or toe.
    - `+0.281` [iowa] EDEMA: excess fluid collecting in tissue
    - `+0.249` [michigan] digit: A finger or toe.
    - `+0.168` [readme] Edema: Swelling in the body caused by too much fluid.
    - `+0.095` [readme] DIGIT: A digit is a finger or a toe.

- rationale: The term "fourth digit" refers to the fourth finger, so "fourth finger" conveys the same anatomical location in everyday language. Phrase frequency increases from Zipf 3.73 to 4.32, and age of acquisition decreases from 9.26 to 4.68. Readers can immediately identify which finger is involved without needing to interpret clinical terminology.
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

**output:** Her parents say she breathes fast, gets tired while feeding, works harder to breathe, and sweats.

| metric | value |
|---|---:|
| bertscore_f1 | 0.448 |
| coleman_liau | 10.62 |
| coleman_liau_drop | 4.76 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.333 |
| fkgl | 5.40 |
| fkgl_drop | 7.43 |
| fre | 84.8 |
| fre_gain | 44.4 |
| human_edit_recall | 1.000 |
| length_ratio | 0.76 |
| n_words | 16.0 |
| nli_completeness | 0.902 |
| nli_faithfulness | 0.134 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 15.84 |
| smog | 3.13 |
| smog_drop | 9.89 |

### Stage 4 - arm `termonly`

**output:** Parents say she seems to breathe fast, gets tired during feeding, works harder to breathe, and sweats.

| metric | value |
|---|---:|
| bertscore_f1 | 0.536 |
| coleman_liau | 10.44 |
| coleman_liau_drop | 4.95 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.333 |
| fkgl | 6.31 |
| fkgl_drop | 6.52 |
| fre | 80.1 |
| fre_gain | 39.6 |
| human_edit_recall | 1.000 |
| length_ratio | 0.81 |
| n_words | 17.0 |
| nli_completeness | 0.875 |
| nli_faithfulness | 0.200 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 15.84 |
| smog | 3.13 |
| smog_drop | 9.89 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `rapidly` -> `fast` | replace | - | - | - | - | - | - | - |
| `respiratory effort` -> `works harder to breathe` | replace | - | - | - | - | - | - | - |
| `diaphoresis` -> `sweats` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Parents say she seems to breathe fast, gets tired during feeding, works harder to breathe, and sweats.

| metric | value |
|---|---:|
| bertscore_f1 | 0.536 |
| coleman_liau | 10.44 |
| coleman_liau_drop | 4.95 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.333 |
| fkgl | 6.31 |
| fkgl_drop | 6.52 |
| fre | 80.1 |
| fre_gain | 39.6 |
| human_edit_recall | 1.000 |
| length_ratio | 0.81 |
| n_words | 17.0 |
| nli_completeness | 0.875 |
| nli_faithfulness | 0.200 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 15.84 |
| smog | 3.13 |
| smog_drop | 9.89 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `rapidly` -> `fast` | replace | attributed | -0.161 | -2.120 | 0.774 | 0.851 | 0.044 | - |
| `respiratory effort` -> `works harder to breathe` | replace | attributed | -0.116 | -0.275 | 0.367 | 0.649 | 0.000 | - |
| `diaphoresis` -> `sweats` | replace | attributed | 0.000 | 0.084 | 0.048 | 0.601 | 0.143 | - |

**edit `rapidly` -> `fast`**

- status: `attributed`
- log p full -0.1855, empty -0.0242
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+0.157` [justplainclear] diaphoresis: Sweating
    - `+0.112` [readme] RESPIRATORY: Related to breathing or the lungs and airways.
    - `+0.069` [readme] diaphoresis: Heavy sweating.
    - `+0.062` [michigan] state: To say or tell. In medicine, how you are doing.
    - `+0.062` [wiktionary] state: Any sovereign nation (nation that rules itself) is a state.

- rationale: "Rapidly" means happening at high speed, and "fast" conveys that same idea in simpler language. Word frequency increases from Zipf 4.34 to 5.13, and the word becomes shorter, dropping from 3 syllables to 1. Readers can grasp the quick pace of the action without stumbling over a longer adverb.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `respiratory effort` -> `works harder to breathe`**

- status: `attributed`
- log p full -0.6087, empty -0.4924
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+0.064` [thesaurus] state: say, tell, condition
    - `+0.063` [michigan] state: To say or tell. In medicine, how you are doing.

- rationale: "Respiratory effort" refers to the physical work involved in breathing, which "works harder to breathe" expresses in everyday language. Phrase frequency rises from Zipf 3.78 to 4.06, age of acquisition drops from 11.00 to 4.11, and syllable count decreases from 7 to 5. This phrasing helps patients recognize when their body is struggling to take in air.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `diaphoresis` -> `sweats`**

- status: `attributed`
- log p full -0.0029, empty -0.0031
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+0.250` [readme] Respiratory: Related to how you breathe and the organs involved in breathing like the lungs and airways.
    - `+0.107` [readme] Diaphoresis: Intense sweating.
    - `+0.062` [readme] diaphoresis: Heavy sweating.
    - `+0.057` [wiktionary] state: Any sovereign nation (nation that rules itself) is a state.
    - `+0.047` [wiktionary] effort: The amount of work that is done on something.

- rationale: Diaphoresis refers to excessive sweating, so the word "sweats" conveys this symptom in everyday language. Word frequency rises from Zipf 1.28 to 3.10, and the syllable count drops from 3 to 1. Readers can immediately recognize the physical sign without needing medical terminology.
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

**output:** The patient said he has not used amphetamines for at least four to five months, but he started having chest pain this evening.

| metric | value |
|---|---:|
| bertscore_f1 | 0.822 |
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

**output:** The patient has not used stimulant drugs for at least four to five months, according to the patient; however, he started having chest pain this evening.

| metric | value |
|---|---:|
| bertscore_f1 | 0.850 |
| coleman_liau | 10.50 |
| coleman_liau_drop | -1.12 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 11.34 |
| fkgl_drop | 0.00 |
| fre | 60.1 |
| fre_gain | 0.0 |
| human_edit_recall | 1.000 |
| length_ratio | 1.08 |
| n_words | 26.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.284 |
| nli_faithfulness | 0.979 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 46.76 |
| smog | 13.02 |
| smog_drop | 0.00 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `amphetamines` -> `stimulant drugs` | replace | - | - | - | - | - | - | - |
| `onset` -> `started having` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** The patient has not used stimulants for at least four to five months, according to the patient; however, he had the start of chest pain this evening.

| metric | value |
|---|---:|
| bertscore_f1 | 0.832 |
| coleman_liau | 8.67 |
| coleman_liau_drop | 0.72 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 10.67 |
| fkgl_drop | 0.67 |
| fre | 66.6 |
| fre_gain | 6.6 |
| human_edit_recall | 1.000 |
| length_ratio | 1.12 |
| n_words | 27.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.823 |
| nli_faithfulness | 0.980 |
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
| `amphetamines` -> `stimulants` | replace | attributed | 0.234 | 0.318 | - | 0.683 | 0.196 | - |
| `onset` -> `the start` | replace | attributed | 1.238 | 2.452 | - | 0.905 | 1.943 | - |

**edit `amphetamines` -> `stimulants`**

- status: `attributed`
- log p full -1.2266, empty -1.4610
- masks scored: 10/10 (+2 top-k)
- ranked sources:
    - `+0.196` [michigan] onset: The start.
    - `-0.020` [wiktionary] amphetamines: Amphetamine is a synthetic drug. It is a stimulant that helps people keep the focus and stay awa

- rationale: Amphetamines are a type of drug that speeds up the body's systems, so the broader term "stimulants" captures this effect in more familiar language. The word frequency rises slightly from Zipf 2.82 to 2.94, and the word becomes shorter, dropping from four syllables to three. This change helps patients recognize the general class of medication without needing to know the specific chemical name.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `onset` -> `the start`**

- status: `attributed`
- log p full -0.2621, empty -1.4998
- masks scored: 10/10 (+2 top-k)
- ranked sources:
    - `+2.219` [michigan] onset: The start.
    - `+0.276` [wiktionary] amphetamines: Amphetamine is a synthetic drug. It is a stimulant that helps people keep the focus and stay awa
    - `-0.350` [wiktionary] onset: The onset of something is the time when it begins (usually something bad).

- rationale: "Onset" refers to the beginning of a condition, so "the start" conveys this timing in everyday language. Phrase frequency rises from Zipf 3.72 to 5.56, and age of acquisition drops from 10.72 to 4.37. Readers can grasp when symptoms began without needing a clinical term.
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

**output:** The doctor used a tube through the mouth to suction the stomach, but only a small amount of clear fluid came out.

| metric | value |
|---|---:|
| bertscore_f1 | 0.410 |
| coleman_liau | 6.58 |
| coleman_liau_drop | 9.46 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.143 |
| fkgl | 8.01 |
| fkgl_drop | 0.36 |
| fre | 76.8 |
| fre_gain | 24.0 |
| human_edit_recall | 1.000 |
| length_ratio | 1.38 |
| n_words | 22.0 |
| nli_completeness | 0.977 |
| nli_faithfulness | 0.164 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 36.19 |
| smog | 3.13 |
| smog_drop | 5.71 |

### Stage 4 - arm `termonly`

**output:** Suction through the mouth was done with only a small amount of clear fluid from the stomach.

| metric | value |
|---|---:|
| bertscore_f1 | 0.644 |
| coleman_liau | 8.05 |
| coleman_liau_drop | 7.99 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.125 |
| fkgl | 6.31 |
| fkgl_drop | 2.06 |
| fre | 80.1 |
| fre_gain | 27.2 |
| human_edit_recall | 1.000 |
| length_ratio | 1.06 |
| n_words | 17.0 |
| nli_completeness | 0.979 |
| nli_faithfulness | 0.968 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 42.70 |
| smog | 3.13 |
| smog_drop | 5.71 |

annotation backend `novita`, 0 edits kept


### Stage 4 - arm `grounded`

**output:** Suction through the mouth was done with very little clear fluid from the stomach.

| metric | value |
|---|---:|
| bertscore_f1 | 0.580 |
| coleman_liau | 9.84 |
| coleman_liau_drop | 6.20 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.250 |
| fkgl | 5.88 |
| fkgl_drop | 2.49 |
| fre | 77.8 |
| fre_gain | 24.9 |
| human_edit_recall | 1.000 |
| length_ratio | 0.88 |
| n_words | 14.0 |
| nli_completeness | 0.976 |
| nli_faithfulness | 0.973 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.167 |
| sari | 29.69 |
| smog | 3.13 |
| smog_drop | 5.71 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `scant` -> `very little` | replace | attributed | 1.782 | 2.743 | 0.698 | 0.897 | 2.164 | - |

**edit `scant` -> `very little`**

- status: `attributed`
- log p full -0.4154, empty -2.1974
- masks scored: 66/66 (+2 top-k)
- ranked sources:
    - `+2.327` [wiktionary] scant: If something is scant, there is very little or very few of it; very little, very few.
    - `+0.164` [nih] stomach: An organ that is part of the digestive system. The stomach helps digest food by mixing it with digest
    - `+0.154` [wiktionary] stomach: The place in the body where food is digested.
    - `+0.099` [readme] suction: Suction is when a machine pulls in gas, liquid, or mucus.
    - `+0.093` [wiktionary] suction: Suction is a force which pushes matter from one space into another due to the pressure difference in 

- rationale: The glossary defines "scant" as meaning "very little," so the replacement directly uses those plain words to convey the same idea. Phrase frequency rises from Zipf 3.10 to 5.56, and age of acquisition drops from 12.16 to 4.90, making the phrase more common and learned earlier. Readers can grasp that the amount is small without needing to interpret a less familiar adjective.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

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

**output:** There is likely a restrictive element due to fibrosis.

| metric | value |
|---|---:|
| bertscore_f1 | 0.586 |
| coleman_liau | 9.91 |
| coleman_liau_drop | 5.80 |
| copy_jargon_rate | 1.000 |
| critical_error | 0.000 |
| fkgl | 8.90 |
| fkgl_drop | 2.62 |
| fre | 47.3 |
| fre_gain | 18.8 |
| human_edit_recall | 0.000 |
| length_ratio | 0.82 |
| n_words | 9.0 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.994 |
| replacement_f1 | 0.000 |
| rewrite_aggressiveness | 1.000 |
| sari | 12.80 |
| smog | 13.02 |
| smog_drop | 1.53 |
| uncertainty_preservation | 1.000 |

### Stage 4 - arm `termonly`

**output:** There is likely some tightness because of scarring.

| metric | value |
|---|---:|
| bertscore_f1 | 0.550 |
| coleman_liau | 11.68 |
| coleman_liau_drop | 4.04 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 5.23 |
| fkgl_drop | 6.29 |
| fre | 71.8 |
| fre_gain | 43.3 |
| human_edit_recall | 1.000 |
| length_ratio | 0.73 |
| n_words | 8.0 |
| nli_completeness | 0.851 |
| nli_faithfulness | 0.906 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.250 |
| sari | 23.43 |
| smog | 3.13 |
| smog_drop | 11.43 |
| uncertainty_preservation | 1.000 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `restrictive element` -> `tightness` | replace | - | - | - | - | - | - | - |
| `fibrosis` -> `scarring` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** There is likely a limiting part because of scarring.

| metric | value |
|---|---:|
| bertscore_f1 | 0.534 |
| coleman_liau | 8.62 |
| coleman_liau_drop | 7.09 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.250 |
| fkgl | 6.28 |
| fkgl_drop | 5.24 |
| fre | 66.1 |
| fre_gain | 37.6 |
| human_edit_recall | 1.000 |
| length_ratio | 0.82 |
| n_words | 9.0 |
| nli_completeness | 0.814 |
| nli_faithfulness | 0.890 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.400 |
| sari | 20.79 |
| smog | 8.84 |
| smog_drop | 5.71 |
| uncertainty_preservation | 1.000 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `restrictive element` -> `limiting part` | replace | attributed | 4.475 | 4.890 | 0.854 | 0.800 | 0.615 | - |
| `fibrosis` -> `scarring` | replace | attributed | -0.125 | -0.325 | 0.454 | 0.557 | 0.399 | - |

**edit `restrictive element` -> `limiting part`**

- status: `attributed`
- log p full -1.0723, empty -5.5469
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+1.633` [wiktionary] restrictive: If something is restrictive, it limits or controls what people can do.
    - `+1.018` [wiktionary] element: An element is one part of something bigger, such as a plan, an engine, or a business.
    - `+0.940` [nih] element: A basic part of a whole. In chemistry, refers to a simple substance that cannot be broken down into s

- rationale: The glossary defines "restrictive" as something that limits or controls actions, so "limiting part" conveys this constraint in everyday language. Phrase frequency rises from Zipf 3.49 to 3.94, age of acquisition drops from 11.00 to 5.11, and syllable count decreases from 6 to 4. Readers can grasp how this component restricts function without needing technical terminology.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `fibrosis` -> `scarring`**

- status: `attributed`
- log p full -0.5508, empty -0.4258
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.531` [readme] FIBROSIS: Fibrosis is tissue that becomes thick and scarred due to injury.
    - `+0.132` [wiktionary] element: An element is one part of something bigger, such as a plan, an engine, or a business.
    - `+0.120` [nih] element: A basic part of a whole. In chemistry, refers to a simple substance that cannot be broken down into s
    - `+0.083` [wiktionary] element: An element is one basic kind of substance, such as iron (Fe), oxygen (O), or sodium (Na).

- rationale: Fibrosis refers to the formation of excess fibrous connective tissue, which is commonly understood as scarring in everyday language. The word frequency decreases slightly from Zipf 3.19 to 3.07, while the syllable count drops from 3 to 2. This change helps patients recognize the physical process of tissue hardening without needing specialized medical terminology.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

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

**output:** The uterus was put back into the belly.

| metric | value |
|---|---:|
| bertscore_f1 | 0.815 |
| coleman_liau | 2.98 |
| coleman_liau_drop | 6.29 |
| copy_jargon_rate | 0.500 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 5.23 |
| fkgl_drop | 4.98 |
| fre | 71.8 |
| fre_gain | 33.9 |
| human_edit_recall | 0.500 |
| length_ratio | 1.00 |
| n_words | 8.0 |
| nli_completeness | 0.980 |
| nli_faithfulness | 0.987 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 34.72 |
| smog | 8.84 |
| smog_drop | 4.18 |

### Stage 4 - arm `termonly`

**output:** The womb was placed back into the belly.

| metric | value |
|---|---:|
| bertscore_f1 | 0.878 |
| coleman_liau | 3.70 |
| coleman_liau_drop | 5.57 |
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
| nli_completeness | 0.985 |
| nli_faithfulness | 0.984 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 87.50 |
| smog | 3.13 |
| smog_drop | 9.89 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `uterus` -> `womb` | replace | - | - | - | - | - | - | - |
| `abdominal cavity` -> `belly` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** The womb was placed back into the belly.

| metric | value |
|---|---:|
| bertscore_f1 | 0.878 |
| coleman_liau | 3.70 |
| coleman_liau_drop | 5.57 |
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
| nli_completeness | 0.985 |
| nli_faithfulness | 0.984 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 87.50 |
| smog | 3.13 |
| smog_drop | 9.89 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `uterus` -> `womb` | replace | attributed | 0.015 | 0.969 | 0.702 | 0.816 | 0.090 | - |
| `abdominal cavity` -> `belly` | replace | attributed | 0.042 | 2.493 | 0.850 | 0.799 | 2.404 | - |

**edit `uterus` -> `womb`**

- status: `attributed`
- log p full -0.0095, empty -0.0249
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.358` [thesaurus] uterus: womb
    - `+0.268` [michigan] uterus: Womb, or where a baby grows when a woman is pregnant.
    - `+0.024` [justplainclear] uterus: Also known as: womb An organ in a woman's body where babies may grow during pregnancy Uterus
    - `+0.013` [readme] abdominal cavity: The belly area where your stomach and other organs are located.
    - `-0.133` [wiktionary] uterus: The uterus is the internal organ inside of a female mammal where an embryo grows into an infant ready 

- rationale: The uterus is the organ where a baby grows, and "womb" is a common, everyday word for the same body part. Word frequency rises from Zipf 3.40 to 3.63, and age of acquisition drops from 12.84 to 9.48. Readers can grasp which organ is involved without needing to recall a clinical term.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `abdominal cavity` -> `belly`**

- status: `attributed`
- log p full -0.0039, empty -0.0459
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+2.483` [readme] abdominal cavity: The belly area where your stomach and other organs are located.
    - `+0.078` [michigan] uterus: Womb, or where a baby grows when a woman is pregnant.
    - `+0.038` [nih] uterus: The hollow, pear-shaped organ in a woman's pelvis. The uterus is where a fetus (unborn baby) develops 

- rationale: The abdominal cavity is the space inside the body that holds organs like the stomach and intestines, and "belly" is a common word for that same area. Word frequency rises from Zipf 3.29 to 4.10, and age of acquisition drops from 10.24 to 4.05. Readers can quickly grasp which part of the body is being discussed.
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

**output:** This was seen on the front and side views.

| metric | value |
|---|---:|
| bertscore_f1 | 0.706 |
| coleman_liau | 2.18 |
| coleman_liau_drop | 5.16 |
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
| nli_completeness | 0.897 |
| nli_faithfulness | 0.974 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 46.30 |
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
| `AP` -> `front-to-back` | replace | attributed | 2.540 | 5.210 | 0.889 | 0.939 | 2.496 | - |
| `lateral projections` -> `side views` | replace | attributed | 0.334 | 0.916 | 0.431 | 0.549 | 0.048 | - |

**edit `AP` -> `front-to-back`**

- status: `attributed`
- log p full -0.0663, empty -2.6062
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+3.846` [readme] anteroposterior: Front to back.
    - `+1.350` [dorland] AP: anteroposterior
    - `+0.328` [michigan] lateral: The side or on the side.
    - `+0.318` [wiktionary] lateral: An object's lateral refers to the side of it.
    - `+0.022` [dorland] AP: alkaline phosphatase

- rationale: The glossary defines "AP" as "front to back," so the replacement spells out this directional relationship in plain language. Syllable count increases from 1 to 3. Patients can grasp the spatial orientation without needing to decode the medical abbreviation.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `lateral projections` -> `side views`**

- status: `attributed`
- log p full -0.3075, empty -0.6420
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.153` [michigan] lateral: The side or on the side.
    - `+0.105` [readme] Lateral: To the side or relating to the side of the body or a body part.
    - `+0.066` [readme] lateral: Lateral means on or related to the side of the body or a body part.
    - `+0.057` [wiktionary] lateral: An object's lateral refers to the side of it.
    - `+0.023` [dorland] AP: anteroposterior

- rationale: "Lateral projections" refers to images taken from the side of the body, which "side views" expresses in everyday language. Phrase frequency rises from Zipf 3.43 to 4.75, age of acquisition drops from 12.41 to 4.72, and syllable count decreases from 6 to 2. This allows patients to immediately grasp the imaging angle without needing technical radiology vocabulary.
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

**output:** The vocal cords move normally when the patient speaks and breathes.

| metric | value |
|---|---:|
| bertscore_f1 | 0.698 |
| coleman_liau | 11.04 |
| coleman_liau_drop | 3.54 |
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
| nli_completeness | 0.986 |
| nli_faithfulness | 0.904 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 55.14 |
| smog | 8.84 |
| smog_drop | 2.37 |

### Stage 4 - arm `termonly`

**output:** The vocal folds move normally when speaking and breathing.

| metric | value |
|---|---:|
| bertscore_f1 | 0.771 |
| coleman_liau | 12.49 |
| coleman_liau_drop | 2.09 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.333 |
| fkgl | 6.28 |
| fkgl_drop | 1.90 |
| fre | 66.1 |
| fre_gain | 15.4 |
| human_edit_recall | 1.000 |
| length_ratio | 1.12 |
| n_words | 9.0 |
| nli_completeness | 0.985 |
| nli_faithfulness | 0.984 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 58.97 |
| smog | 8.84 |
| smog_drop | 2.37 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `phonation` -> `speaking` | replace | - | - | - | - | - | - | - |
| `ventilation` -> `breathing` | replace | - | - | - | - | - | - | - |

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
| `phonation` -> `speaking` | replace | attributed | 0.026 | 0.123 | - | 0.750 | 0.004 | - |
| `ventilation` -> `breathing` | replace | attributed | 0.002 | 0.547 | - | 0.850 | 0.375 | - |

**edit `phonation` -> `speaking`**

- status: `attributed`
- log p full -0.2275, empty -0.2539
- masks scored: 34/34 (+4 top-k)
- ranked sources:
    - `+0.144` [dictionary] Phonation (n.): The act or process by which articulate sounds are uttered; the utterance of articulate sounds;
    - `+0.140` [wiktionary] ventilation: Ventilation is the bodily process of breathing; the inhalation of air to provide oxygen, and the 
    - `+0.031` [wiktionary] ventilation: Ventilation is the replacement of stale air with fresh air.
    - `-0.071` [wiktionary] cords: A long, thin rope or wire.

- rationale: Phonation refers to the production of vocal sound, so "speaking" conveys this action in everyday language. Word frequency increases from Zipf 1.80 to 4.91, while the syllable count remains at 2. Patients can grasp that the issue involves their ability to produce voice without needing technical terminology.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `ventilation` -> `breathing`**

- status: `attributed`
- log p full -0.0028, empty -0.0048
- masks scored: 34/34 (+4 top-k)
- ranked sources:
    - `+0.682` [wiktionary] ventilation: Ventilation is the bodily process of breathing; the inhalation of air to provide oxygen, and the 
    - `+0.307` [wiktionary] cords: A long, thin rope or wire.
    - `-0.071` [dictionary] Phonation (n.): The act or process by which articulate sounds are uttered; the utterance of articulate sounds;
    - `-0.081` [wiktionary] ventilation: Ventilation is the replacement of stale air with fresh air.
    - `-0.368` [readme] ventilation: Ventilation is about bringing in fresh air.

- rationale: Ventilation refers to the movement of air in and out of the lungs, so "breathing" conveys this physiological process in everyday language. Word frequency increases from Zipf 3.60 to 4.28, and the word becomes shorter, dropping from 4 syllables to 2. Readers can grasp how air exchange works without needing to interpret clinical terminology.
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

**output:** After the abdomen was opened, there was a large amount of pus.

| metric | value |
|---|---:|
| bertscore_f1 | 0.797 |
| coleman_liau | 5.42 |
| coleman_liau_drop | 3.72 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 5.81 |
| fkgl_drop | 1.83 |
| fre | 74.8 |
| fre_gain | 11.3 |
| human_edit_recall | 1.000 |
| length_ratio | 0.80 |
| n_words | 12.0 |
| nli_completeness | 0.941 |
| nli_faithfulness | 0.836 |
| number_unit_preservation | 0.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.400 |
| sari | 43.10 |
| smog | 8.84 |
| smog_drop | 2.37 |

### Stage 4 - arm `termonly`

**output:** Once the belly was opened, there was thick pus.

| metric | value |
|---|---:|
| bertscore_f1 | 0.726 |
| coleman_liau | 4.76 |
| coleman_liau_drop | 4.38 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.400 |
| fkgl | 2.34 |
| fkgl_drop | 5.29 |
| fre | 94.3 |
| fre_gain | 30.8 |
| human_edit_recall | 1.000 |
| length_ratio | 0.60 |
| n_words | 9.0 |
| nli_completeness | 0.930 |
| nli_faithfulness | 0.666 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.200 |
| sari | 31.13 |
| smog | 3.13 |
| smog_drop | 8.08 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `abdomen` -> `belly` | replace | - | - | - | - | - | - | - |
| `gross purulent drainage` -> `thick pus` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Once the belly was opened, thick pus was leaking out.

| metric | value |
|---|---:|
| bertscore_f1 | 0.677 |
| coleman_liau | 5.60 |
| coleman_liau_drop | 3.54 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.600 |
| fkgl | 3.65 |
| fkgl_drop | 3.98 |
| fre | 86.7 |
| fre_gain | 23.2 |
| human_edit_recall | 1.000 |
| length_ratio | 0.67 |
| n_words | 10.0 |
| nli_completeness | 0.966 |
| nli_faithfulness | 0.786 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 20.65 |
| smog | 3.13 |
| smog_drop | 8.08 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `abdomen` -> `belly` | replace | attributed | 0.005 | 0.555 | 0.549 | 0.675 | 0.067 | - |
| `gross purulent drainage` -> `thick pus was leaking out` | replace | attributed | 6.185 | 6.365 | 0.871 | 0.920 | 6.699 | - |

**edit `abdomen` -> `belly`**

- status: `attributed`
- log p full -0.0065, empty -0.0114
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.628` [wiktionary] gross: The gross amount is the total before you take away losses or expenses.
    - `+0.561` [wiktionary] abdomen: The abdomen is the last of the three parts of an insect's body.
    - `+0.533` [nih] abdomen: The area of the body that contains the pancreas, stomach, intestines, liver, gallbladder, and other o
    - `+0.202` [wiktionary] gross: A gross violation or abuse is very bad and clearly wrong.
    - `+0.159` [wiktionary] drainage: To use a drainage is engage in the action or process of draining something.

- rationale: "Abdomen" refers to the part of the body between the chest and hips, and "belly" conveys this same anatomical region in everyday language. Word frequency rises from Zipf 3.56 to 4.10, while age of acquisition drops from 8.61 to 4.05. Readers can immediately identify the body area without needing to recall clinical terminology.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `gross purulent drainage` -> `thick pus was leaking out`**

- status: `attributed`
- log p full -1.8015, empty -7.9863
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+6.925` [readme] drainage: When any fluid is leaking out of a body part.
    - `+0.226` [readme] DRAINAGE: Fluid leaving an organ or body area.
    - `+0.121` [wiktionary] drainage: To use a drainage is engage in the action or process of draining something.
    - `+0.012` [wiktionary] gross: A gross violation or abuse is very bad and clearly wrong.

- rationale: The glossary source defines the original term as fluid leaking from a body part, so "thick pus was leaking out" conveys that specific discharge in everyday language. Phrase frequency rises from Zipf 1.92 to 2.92, and age of acquisition drops from 15.50 to 7.78. Readers can now recognize the sign of infection without needing to interpret clinical jargon.
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

**output:** After all four ports were placed, the doctor examined the upper right part of the abdomen.

| metric | value |
|---|---:|
| bertscore_f1 | 0.762 |
| coleman_liau | 8.81 |
| coleman_liau_drop | 0.77 |
| copy_jargon_rate | 0.250 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 7.61 |
| fkgl_drop | -3.61 |
| fre | 69.0 |
| fre_gain | -20.5 |
| human_edit_recall | 0.750 |
| laterality_preservation | 1.000 |
| length_ratio | 1.00 |
| n_words | 16.0 |
| nli_completeness | 0.981 |
| nli_faithfulness | 0.483 |
| number_unit_preservation | 0.500 |
| replacement_f1 | 0.857 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 35.97 |
| smog | 11.21 |
| smog_drop | -8.08 |

### Stage 4 - arm `termonly`

**output:** Once all four small openings were made, the doctor looked inside the upper right belly area.

| metric | value |
|---|---:|
| bertscore_f1 | 0.617 |
| coleman_liau | 9.54 |
| coleman_liau_drop | 0.05 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.200 |
| fkgl | 8.35 |
| fkgl_drop | -4.35 |
| fre | 63.7 |
| fre_gain | -25.8 |
| human_edit_recall | 1.000 |
| laterality_preservation | 1.000 |
| length_ratio | 1.00 |
| n_words | 16.0 |
| nli_completeness | 0.963 |
| nli_faithfulness | 0.378 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.250 |
| sari | 36.99 |
| smog | 11.21 |
| smog_drop | -8.08 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `ports` -> `small openings` | replace | - | - | - | - | - | - | - |
| `explored` -> `looked inside` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Once all four small tubes were placed, the doctor looked at the upper right belly area.

| metric | value |
|---|---:|
| bertscore_f1 | 0.701 |
| coleman_liau | 7.72 |
| coleman_liau_drop | 1.86 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.200 |
| fkgl | 6.14 |
| fkgl_drop | -2.13 |
| fre | 79.6 |
| fre_gain | -10.0 |
| human_edit_recall | 1.000 |
| laterality_preservation | 1.000 |
| length_ratio | 1.00 |
| n_words | 16.0 |
| nli_completeness | 0.953 |
| nli_faithfulness | 0.346 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 48.62 |
| smog | 8.84 |
| smog_drop | -5.71 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `ports` -> `small tubes` | replace | attributed | 0.557 | 0.704 | 0.136 | 0.586 | 0.017 | - |
| `explored` -> `looked at` | replace | attributed | 0.082 | 0.116 | 0.393 | 0.550 | 0.096 | - |

**edit `ports` -> `small tubes`**

- status: `attributed`
- log p full -1.3047, empty -1.8613
- masks scored: 66/66 (+3 top-k)
- ranked sources:
    - `+0.125` [readme] right upper lobe: A section of the right lung.
    - `+0.109` [wiktionary] ports: A port is a place for ships to stop to trade or refuel.

- rationale: "Ports" refers to access points for medical devices, so "small tubes" conveys this idea using familiar physical objects. Word frequency decreases from Zipf 4.07 to 3.93, and syllable count increases from 1 to 2. Patients can visualize the physical connection used for treatment without needing to know the technical term.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `explored` -> `looked at`**

- status: `attributed`
- log p full -1.1875, empty -1.2695
- masks scored: 66/66 (+3 top-k)
- ranked sources:
    - `+0.096` [readme] right upper lobe: A section of the right lung.
    - `-0.024` [wiktionary] explored: If you explore a possibility, plan, idea, etc. you think about it carefully.

- rationale: "Explored" means to examine or investigate something, and "looked at" conveys this same idea in everyday language. Word frequency increases from Zipf 3.90 to 5.10, making the phrase more common and easier to process. Readers can grasp that the medical team examined the issue without encountering formal academic vocabulary.
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

**output:** The doctor discussed options such as watchful waiting, robotic prostatectomy, and seed implantation with or without radiation.

| metric | value |
|---|---:|
| bertscore_f1 | 0.553 |
| coleman_liau | 18.96 |
| coleman_liau_drop | 1.93 |
| copy_jargon_rate | 1.000 |
| critical_error | 0.000 |
| fkgl | 15.33 |
| fkgl_drop | 0.10 |
| fre | 15.4 |
| fre_gain | 4.3 |
| human_edit_recall | 0.000 |
| length_ratio | 0.74 |
| n_words | 17.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.150 |
| replacement_f1 | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 22.42 |
| smog | 14.55 |
| smog_drop | 0.00 |

### Stage 4 - arm `termonly`

**output:** Options such as close monitoring, robot-assisted surgery, and placing seeds with or without energy beams were discussed.

| metric | value |
|---|---:|
| bertscore_f1 | 0.572 |
| coleman_liau | 16.58 |
| coleman_liau_drop | 4.32 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.429 |
| fkgl | 13.25 |
| fkgl_drop | 2.18 |
| fre | 30.3 |
| fre_gain | 19.2 |
| human_edit_recall | 1.000 |
| length_ratio | 0.78 |
| n_words | 18.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.844 |
| nli_faithfulness | 0.988 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 31.72 |
| smog | 14.55 |
| smog_drop | 0.00 |

annotation backend `novita`, 4 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `watchful waiting` -> `close monitoring` | replace | - | - | - | - | - | - | - |
| `robotic prostatectomy` -> `robot-assisted surgery` | replace | - | - | - | - | - | - | - |
| `seed implantation` -> `placing seeds` | replace | - | - | - | - | - | - | - |
| `radiation` -> `energy beams` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Options such as close watching, robot-assisted prostate removal, and placing seeds with or without high-energy rays were discussed.

| metric | value |
|---|---:|
| bertscore_f1 | 0.608 |
| coleman_liau | 17.68 |
| coleman_liau_drop | 3.22 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.429 |
| fkgl | 13.06 |
| fkgl_drop | 2.37 |
| fre | 33.5 |
| fre_gain | 22.3 |
| human_edit_recall | 1.000 |
| length_ratio | 0.87 |
| n_words | 20.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.992 |
| nli_faithfulness | 0.969 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 32.43 |
| smog | 13.02 |
| smog_drop | 1.53 |

annotation backend `novita`, 4 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `watchful waiting` -> `close watching` | replace | attributed | 1.469 | 1.747 | 0.822 | 0.923 | 0.860 | - |
| `robotic prostatectomy` -> `robot-assisted prostate removal` | replace | attributed | 1.156 | 1.299 | 0.728 | 0.869 | 0.892 | - |
| `seed implantation` -> `placing seeds` | replace | attributed | 0.129 | 0.174 | 0.603 | 0.717 | 0.067 | - |
| `radiation` -> `high-energy rays` | replace | attributed | 0.922 | 1.336 | 0.931 | 0.967 | 5.014 | - |

**edit `watchful waiting` -> `close watching`**

- status: `attributed`
- log p full -1.2227, empty -2.6914
- masks scored: 66/66 (+8 top-k)
- ranked sources:
    - `+1.047` [nih] watchful waiting: Closely watching a patient’s condition but not giving treatment unless symptoms appear or ch
    - `+0.187` [readme] radiation: High energy rays used to kill cancer cells.
    - `+0.117` [readme] prostatectomy: A prostatectomy is a surgery to remove part or all of the prostate and some surrounding tissue.
    - `+0.050` [wiktionary] seed: A seed is a small round thing that can grow to be a plant, a flower or a tree.

- rationale: The glossary defines watchful waiting as closely monitoring a patient’s condition without immediate treatment, so "close watching" captures this active observation in simpler terms. Phrase frequency rises from Zipf 3.09 to 4.86, and age of acquisition drops from 8.16 to 4.50. Readers can grasp that their health is being monitored carefully without assuming treatment has started.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `robotic prostatectomy` -> `robot-assisted prostate removal`**

- status: `attributed`
- log p full -1.6995, empty -2.8556
- masks scored: 66/66 (+8 top-k)
- ranked sources:
    - `+0.983` [nih] prostatectomy: Surgery to remove part or all of the prostate and some of the tissue around it, including the s
    - `+0.091` [readme] prostatectomy: A prostatectomy is a surgery to remove part or all of the prostate and some surrounding tissue.
    - `+0.051` [thesaurus] radiation: see ionizing radiation and non-ionizing radiation
    - `+0.007` [nih] radiation: Energy released in the form of particle or electromagnetic waves. Common sources of radiation inclu

- rationale: The glossary explains that robotic prostatectomy uses a special robotic system to remove the prostate, so "robot-assisted prostate removal" keeps that meaning in plain words. Phrase frequency increases from Zipf 2.13 to 3.40, while age of acquisition falls from 15.27 to 15.00. Patients can understand that a robotic tool helps remove the prostate without needing the technical surgical name.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `seed implantation` -> `placing seeds`**

- status: `attributed`
- log p full -1.2930, empty -1.4219
- masks scored: 66/66 (+8 top-k)
- ranked sources:
    - `+0.469` [readme] IMPLANTATION: A surgery where a device is placed inside the body.
    - `+0.402` [readme] implantation: Surgery where a device is placed inside your body.
    - `+0.099` [readme] Radiation: Radiation is powerful energy waves that are sometimes utilized to destroy cancer cells.

- rationale: "Seed implantation" refers to the procedure of inserting radioactive seeds into tissue, which "placing seeds" describes using everyday verbs. The phrase becomes more common, with Zipf frequency rising from 2.99 to 3.92, and shorter, dropping from 5 syllables to 3. This wording helps patients grasp the physical action of the treatment without needing technical terminology.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `radiation` -> `high-energy rays`**

- status: `attributed`
- log p full -0.7765, empty -1.6987
- masks scored: 66/66 (+8 top-k)
- ranked sources:
    - `+5.314` [readme] radiation: High energy rays used to kill cancer cells.
    - `+0.300` [thesaurus] radiation: see ionizing radiation and non-ionizing radiation
    - `+0.075` [readme] prostatectomy: A prostatectomy is a surgery to remove part or all of the prostate and some surrounding tissue.
    - `+0.023` [wiktionary] seed: A seed is a small round thing that can grow to be a plant, a flower or a tree.

- rationale: The glossary defines radiation as high-energy rays used to kill cancer cells, so the replacement directly conveys this mechanism in plain language. Word frequency decreases from Zipf 4.27 to 4.00, and syllable count increases from 4 to 5. Patients can grasp that the treatment uses powerful rays to target cancer without needing to understand the technical term.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

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

**output:** He also reportedly was on Lasix before going to the hospital, possibly.

| metric | value |
|---|---:|
| bertscore_f1 | 0.596 |
| coleman_liau | 9.77 |
| coleman_liau_drop | 3.95 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 10.72 |
| fkgl_drop | 3.55 |
| fre | 39.6 |
| fre_gain | 29.0 |
| human_edit_recall | 1.000 |
| length_ratio | 0.80 |
| n_words | 12.0 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.990 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 48.79 |
| smog | 13.02 |
| smog_drop | 0.00 |
| temporality_preservation | 1.000 |
| uncertainty_preservation | 1.000 |

### Stage 4 - arm `termonly`

**output:** He also reportedly was on Lasix prior to hospitalization, possible

| metric | value |
|---|---:|
| bertscore_f1 | 0.648 |
| coleman_liau | 13.72 |
| coleman_liau_drop | 0.00 |
| copy_jargon_rate | 1.000 |
| critical_error | 0.000 |
| fkgl | 14.27 |
| fkgl_drop | 0.00 |
| fre | 10.6 |
| fre_gain | 0.0 |
| human_edit_recall | 0.000 |
| length_ratio | 0.67 |
| n_words | 10.0 |
| nli_completeness | 0.989 |
| nli_faithfulness | 0.989 |
| replacement_f1 | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 9.07 |
| smog | 13.02 |
| smog_drop | 0.00 |
| temporality_preservation | 1.000 |
| uncertainty_preservation | 1.000 |

annotation backend `novita`, 0 edits kept


### Stage 4 - arm `grounded`

**output:** He also reportedly was on Lasix prior to hospitalization, possible

| metric | value |
|---|---:|
| bertscore_f1 | 0.648 |
| coleman_liau | 13.72 |
| coleman_liau_drop | 0.00 |
| copy_jargon_rate | 1.000 |
| critical_error | 0.000 |
| fkgl | 14.27 |
| fkgl_drop | 0.00 |
| fre | 10.6 |
| fre_gain | 0.0 |
| human_edit_recall | 0.000 |
| length_ratio | 0.67 |
| n_words | 10.0 |
| nli_completeness | 0.989 |
| nli_faithfulness | 0.989 |
| replacement_f1 | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 9.07 |
| smog | 13.02 |
| smog_drop | 0.00 |
| temporality_preservation | 1.000 |
| uncertainty_preservation | 1.000 |

annotation backend `novita`, 0 edits kept


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

**output:** The four heart chambers are normal in size.

| metric | value |
|---|---:|
| bertscore_f1 | 0.595 |
| coleman_liau | 5.88 |
| coleman_liau_drop | 9.19 |
| copy_jargon_rate | 0.250 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.167 |
| fkgl | 2.28 |
| fkgl_drop | 7.93 |
| fre | 93.0 |
| fre_gain | 55.1 |
| human_edit_recall | 0.750 |
| length_ratio | 0.62 |
| n_words | 8.0 |
| nli_completeness | 0.963 |
| nli_faithfulness | 0.967 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 0.857 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 33.60 |
| smog | 3.13 |
| smog_drop | 8.08 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `cardiac chambers` -> `heart chambers` | replace | - | - | - | - | - | - | - |
| `within normal limits` -> `normal in size` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

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

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `cardiac chambers` -> `heart room` | replace | attributed | 0.932 | 1.115 | 0.755 | 0.850 | 0.651 | - |
| `dimensions` -> `sizes` | replace | attributed | -0.005 | -0.383 | 0.746 | 0.912 | 0.182 | - |
| `within normal limits` -> `normal` | replace | attributed | -0.571 | -1.759 | 0.671 | 0.895 | 0.161 | - |

**edit `cardiac chambers` -> `heart room`**

- status: `attributed`
- log p full -1.3940, empty -2.3264
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+0.732` [wiktionary] chambers: A chamber is a room that is often used for sleeping.
    - `+0.082` [readme] cardiac: Related to the heart.
    - `+0.080` [wiktionary] within: before the time ends
    - `+0.042` [wiktionary] normal: A normal thing, or situation, is one that is not special.
    - `+0.008` [wiktionary] normal: When someone is back to normal, he is healthier and no longer sick.

- rationale: The glossary defines a chamber as a room, so "heart room" conveys the idea of an internal space in plain language. Phrase frequency increases from Zipf 3.64 to 5.05, and age of acquisition falls from 11.74 to 5.17. Readers can grasp the concept of the heart's internal compartments without needing anatomical terminology.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `dimensions` -> `sizes`**

- status: `attributed`
- log p full -0.0156, empty -0.0107
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+0.434` [justplainclear] limits: A certain point that you can't go past; a certain amount but no more
    - `+0.252` [wiktionary] normal: A normal thing, or situation, is one that is not special.
    - `+0.239` [michigan] cardiac: Related to your heart.
    - `+0.189` [wiktionary] within: before the time ends
    - `+0.145` [nih] cardiac: Having to do with the heart.

- rationale: "Dimensions" refers to the measurable extents of an object, so "sizes" conveys this concept using more familiar language. The word frequency increases from Zipf 4.05 to 4.18, and the syllable count decreases from 3 to 2. This allows readers to quickly grasp the physical measurements without encountering technical terminology.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `within normal limits` -> `normal`**

- status: `attributed`
- log p full -0.7461, empty -0.1748
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+0.297` [nih] cardiac: Having to do with the heart.
    - `+0.136` [wiktionary] dimensions: A dimension is a part of a problem, issue, or situation.
    - `+0.129` [iowa] CARDIAC: related to the heart
    - `+0.107` [readme] cardiac: Related to the heart.
    - `+0.079` [wiktionary] limits: The limit is the edge of how far something can go. It can go up to the limit but no farther.

- rationale: "Within normal limits" means that test results fall inside the expected healthy range, and the single word "normal" conveys this same idea more directly. Word frequency rises from Zipf 4.32 to 5.01, age of acquisition drops from 7.65 to 5.53, and syllable count falls from 6 to 2. Readers can quickly grasp that their results are healthy without parsing a multi-word clinical phrase.
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

**output:** The doctor checked the patient's rectum with a finger and did not find any lumps.

| metric | value |
|---|---:|
| bertscore_f1 | 0.438 |
| coleman_liau | 7.36 |
| coleman_liau_drop | 9.00 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.667 |
| fkgl | 5.99 |
| fkgl_drop | 5.53 |
| fre | 78.8 |
| fre_gain | 50.3 |
| human_edit_recall | 1.000 |
| length_ratio | 1.45 |
| n_words | 16.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.695 |
| nli_faithfulness | 0.179 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.286 |
| sari | 18.93 |
| smog | 3.13 |
| smog_drop | 8.08 |

### Stage 4 - arm `termonly`

**output:** The doctor checked the rectum with a finger and found no lumps.

| metric | value |
|---|---:|
| bertscore_f1 | 0.487 |
| coleman_liau | 6.38 |
| coleman_liau_drop | 9.97 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.333 |
| fkgl | 3.84 |
| fkgl_drop | 7.68 |
| fre | 88.9 |
| fre_gain | 60.4 |
| human_edit_recall | 1.000 |
| length_ratio | 1.09 |
| n_words | 12.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.735 |
| nli_faithfulness | 0.070 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.286 |
| sari | 23.19 |
| smog | 3.13 |
| smog_drop | 8.08 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `performed` -> `checked` | replace | - | - | - | - | - | - | - |
| `masses` -> `lumps` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** The doctor checked the rectum with a finger and found no lumps.

| metric | value |
|---|---:|
| bertscore_f1 | 0.487 |
| coleman_liau | 6.38 |
| coleman_liau_drop | 9.97 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.333 |
| fkgl | 3.84 |
| fkgl_drop | 7.68 |
| fre | 88.9 |
| fre_gain | 60.4 |
| human_edit_recall | 1.000 |
| length_ratio | 1.09 |
| n_words | 12.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.735 |
| nli_faithfulness | 0.070 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.286 |
| sari | 23.19 |
| smog | 3.13 |
| smog_drop | 8.08 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `performed` -> `checked` | replace | attributed | -0.326 | -0.964 | - | 0.894 | 0.082 | - |
| `Digital rectal examination` -> `rectum with a finger` | replace | attributed | 0.010 | 0.023 | - | 0.911 | 0.399 | - |
| `masses` -> `lumps` | replace | attributed | -0.024 | -0.498 | - | 0.638 | 0.007 | - |

**edit `performed` -> `checked`**

- status: `attributed`
- log p full -0.5977, empty -0.2715
- masks scored: 18/18 (+4 top-k)
- ranked sources:
    - `+0.090` [wiktionary] masses: A measure of how much material is in something.
    - `+0.007` [wiktionary] masses: The masses are the regular people, not those in power.
    - `-0.130` [wiktionary] performed: When you perform something, you do it.
    - `-1.004` [nih] digital rectal examination: An examination in which a doctor inserts a lubricated, gloved finger into the rect

- rationale: "Performed" means to carry out an action, and "checked" conveys this idea of examining or verifying in simpler terms. The word frequency decreases slightly from Zipf 4.68 to 4.54, while the syllable count drops from 2 to 1. This change helps patients grasp that a specific examination took place without using formal procedural language.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `Digital rectal examination` -> `rectum with a finger`**

- status: `attributed`
- log p full -0.5701, empty -0.5802
- masks scored: 18/18 (+4 top-k)
- ranked sources:
    - `+0.399` [nih] digital rectal examination: An examination in which a doctor inserts a lubricated, gloved finger into the rect
    - `-0.088` [wiktionary] performed: When you perform something, you do it.
    - `-0.166` [wiktionary] masses: A measure of how much material is in something.

- rationale: A digital rectal examination is a check of the rectum using a finger, so the phrase "rectum with a finger" conveys the same action in everyday language. Phrase frequency rises from Zipf 2.88 to 2.95, age of acquisition drops from 13.06 to 9.84, and syllable count falls from 10 to 6. This wording helps patients grasp exactly what the physical check involves without needing to decode clinical terminology.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `masses` -> `lumps`**

- status: `attributed`
- log p full -0.0615, empty -0.0378
- masks scored: 18/18 (+4 top-k)
- ranked sources:
    - `-0.088` [nih] digital rectal examination: An examination in which a doctor inserts a lubricated, gloved finger into the rect
    - `-0.095` [wiktionary] masses: The masses are the regular people, not those in power.
    - `-0.238` [wiktionary] performed: When you perform something, you do it.
    - `-0.327` [wiktionary] masses: A measure of how much material is in something.

- rationale: "Masses" refers to abnormal growths or clumps of tissue, and "lumps" conveys this idea in everyday language. Word frequency decreases from Zipf 3.94 to 3.19, while the syllable count drops from 2 to 1. Readers can grasp the physical nature of the growth without needing medical terminology.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

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

**output:** He then had seizures and weakness on one side of his body. He went to the hospital, got an infection called C-diff, and is now in a nursing home.

| metric | value |
|---|---:|
| bertscore_f1 | 0.616 |
| coleman_liau | 4.56 |
| coleman_liau_drop | 5.71 |
| copy_jargon_rate | 0.667 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 5.53 |
| fkgl_drop | 5.70 |
| fre | 81.3 |
| fre_gain | 27.5 |
| human_edit_recall | 0.333 |
| length_ratio | 1.03 |
| n_words | 30.0 |
| nli_completeness | 0.026 |
| nli_faithfulness | 0.944 |
| replacement_f1 | 0.500 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.800 |
| sari | 30.77 |
| smog | 8.84 |
| smog_drop | 5.71 |
| temporality_preservation | 1.000 |

### Stage 4 - arm `termonly`

**output:** He then had a problem with seizures, weakness on one side, has been to the hospital, developed a gut infection, and is in the nursing home currently.

| metric | value |
|---|---:|
| bertscore_f1 | 0.902 |
| coleman_liau | 8.45 |
| coleman_liau_drop | 1.82 |
| copy_jargon_rate | 0.333 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 11.98 |
| fkgl_drop | -0.76 |
| fre | 57.2 |
| fre_gain | 3.5 |
| human_edit_recall | 0.667 |
| length_ratio | 0.93 |
| n_words | 27.0 |
| nli_completeness | 0.381 |
| nli_faithfulness | 0.911 |
| replacement_f1 | 0.800 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 80.94 |
| smog | 14.55 |
| smog_drop | 0.00 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `hemiparesis` -> `weakness on one side` | replace | - | - | - | - | - | - | - |
| `C-diff` -> `a gut infection` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** He then had a problem with seizures, weakness on one side of the body, has been to the hospital, developed a gut infection, and is in the nursing home currently.

| metric | value |
|---|---:|
| bertscore_f1 | 0.864 |
| coleman_liau | 7.77 |
| coleman_liau_drop | 2.51 |
| copy_jargon_rate | 0.333 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 13.02 |
| fkgl_drop | -1.80 |
| fre | 55.1 |
| fre_gain | 1.4 |
| human_edit_recall | 0.667 |
| length_ratio | 1.03 |
| n_words | 30.0 |
| nli_completeness | 0.394 |
| nli_faithfulness | 0.925 |
| replacement_f1 | 0.800 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 75.63 |
| smog | 14.55 |
| smog_drop | 0.00 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `hemiparesis` -> `weakness on one side of the body` | replace | attributed | 0.932 | 2.389 | 0.830 | 0.896 | 2.506 | - |
| `C-diff` -> `a gut infection` | replace | attributed | 0.860 | 1.408 | 0.897 | 0.956 | 3.238 | - |

**edit `hemiparesis` -> `weakness on one side of the body`**

- status: `attributed`
- log p full -0.1689, empty -1.1006
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+2.558` [readme] hemiparesis: Weakness on one side of the body.
    - `+0.052` [dorland] C-diff: Clostridioides difficile

- rationale: The glossary defines hemiparesis as weakness on one side of the body, so the replacement conveys this specific symptom in plain language. Word frequency increases from Zipf 1.49 to 4.14, making the phrase significantly more common and easier to process. Patients can now clearly recognize which part of their body is affected without needing to interpret a complex medical term.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `C-diff` -> `a gut infection`**

- status: `attributed`
- log p full -0.5830, empty -1.4431
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+3.431` [readme] Clostridium difficile colitis: A type of gut infection that causes symptoms like fever, diarrhea, and cramps.
    - `+0.193` [readme] Seizures: Seizures are when the brain has sudden abnormal activity that can lead to loss of consciousness and 
    - `-0.020` [readme] seizures: Seizures are when the brain has strange electrical activity that may make someone lose consciousness
    - `-0.261` [wiktionary] seizures: If someone seizes (takes) something from someone by force, or arrests someone, it is a seizure.
    - `-0.368` [readme] hemiparesis: Weakness on one side of the body.

- rationale: The glossary defines C-diff as a type of gut infection causing fever, diarrhea, and cramps, so the replacement directly names the condition in everyday terms. Syllable count increases from 2 to 5. Patients can recognize the specific infection and its common symptoms without needing to know the abbreviated medical name.
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

**output:** He has used continuous positive airway pressure for several months and is coming back for a checkup to see how well the treatment is working.

| metric | value |
|---|---:|
| bertscore_f1 | 0.647 |
| coleman_liau | 9.93 |
| coleman_liau_drop | 2.72 |
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
| nli_faithfulness | 0.993 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 0.286 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.667 |
| sari | 42.23 |
| smog | 11.21 |
| smog_drop | 1.82 |
| temporality_preservation | 0.000 |

### Stage 4 - arm `termonly`

**output:** He has used a breathing machine for several months and comes back to check how well the treatment is working.

| metric | value |
|---|---:|
| bertscore_f1 | 0.715 |
| coleman_liau | 8.53 |
| coleman_liau_drop | 4.12 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.167 |
| fkgl | 6.96 |
| fkgl_drop | 5.34 |
| fre | 80.8 |
| fre_gain | 34.7 |
| human_edit_recall | 1.000 |
| length_ratio | 0.80 |
| n_words | 20.0 |
| nli_completeness | 0.876 |
| nli_faithfulness | 0.830 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.400 |
| sari | 48.89 |
| smog | 3.13 |
| smog_drop | 9.89 |
| temporality_preservation | 0.000 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `continuous positive airway pressure` -> `a breathing machine` | replace | - | - | - | - | - | - | - |
| `followup` -> `check how well the treatment is working` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

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
| `continuous positive airway pressure` -> `a breathing machine` | replace | attributed | -0.509 | -0.764 | 0.526 | 0.872 | 0.113 | - |
| `followup` -> `a checkup` | replace | attributed | 0.166 | 0.780 | 0.874 | 0.944 | 2.885 | - |

**edit `continuous positive airway pressure` -> `a breathing machine`**

- status: `attributed`
- log p full -1.3730, empty -0.8643
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.167` [wiktionary] airway: An airway is a path an aircraft takes.
    - `+0.054` [readme] continuous: Continuous means something that never stops or has interruptions.
    - `+0.007` [readme] followup: Going back to your doctor for a checkup or follow-up appointment.
    - `+0.007` [wiktionary] pressure: In science, pressure is force applied over an area.

- rationale: Continuous positive airway pressure refers to a treatment that keeps airways open with steady airflow, so "a breathing machine" conveys the device's role in supporting respiration using everyday language. Phrase frequency rises from Zipf 3.14 to 4.19, age of acquisition drops from 11.39 to 6.53, and syllable count decreases from 11 to 5. Readers can grasp that a device helps them breathe without needing to decode the technical acronym.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `followup` -> `a checkup`**

- status: `attributed`
- log p full -0.1660, empty -0.3320
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+3.758` [readme] followup: Going back to your doctor for a checkup or follow-up appointment.
    - `+0.873` [wiktionary] positive: If you are positive about something, you are sure that you are not mistaken.
    - `+0.782` [wiktionary] pressure: If a person is under pressure, they feel stressed.
    - `+0.314` [readme] Positive: Something is there.
    - `+0.252` [readme] POSITIVE: Something is good or beneficial.

- rationale: "Followup" refers to a subsequent visit to monitor health, which "a checkup" conveys in everyday language. Word frequency rises slightly from Zipf 2.87 to 2.88, while syllable count remains at 3. Readers can grasp the need for a routine health review without encountering clinical jargon.
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

**output:** The patient should take small bites and small sips to help lower the risk of food or liquid going into the airway.

| metric | value |
|---|---:|
| bertscore_f1 | 0.688 |
| coleman_liau | 7.11 |
| coleman_liau_drop | 2.51 |
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
| nli_completeness | 0.646 |
| nli_faithfulness | 0.661 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 39.02 |
| severity_downgrade | 0.000 |
| severity_preservation | 1.000 |
| severity_tier_input | 1.000 |
| severity_tier_output | 1.000 |
| smog | 3.13 |
| smog_drop | 8.08 |

### Stage 4 - arm `termonly`

**output:** The patient should take small bites and small sips to help lower the risk of food going into the airway or lungs.

| metric | value |
|---|---:|
| bertscore_f1 | 0.663 |
| coleman_liau | 6.85 |
| coleman_liau_drop | 2.78 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 7.47 |
| fkgl_drop | 1.00 |
| fre | 80.7 |
| fre_gain | 14.3 |
| human_edit_recall | 1.000 |
| length_ratio | 0.73 |
| n_words | 22.0 |
| nli_completeness | 0.768 |
| nli_faithfulness | 0.551 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 38.44 |
| severity_downgrade | 0.000 |
| severity_preservation | 1.000 |
| severity_tier_input | 1.000 |
| severity_tier_output | 1.000 |
| smog | 3.13 |
| smog_drop | 8.08 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `aspiration` -> `food going into the airway or lungs` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** The patient should take small bites and sips to lower the risk of breathing food into the lungs or throat.

| metric | value |
|---|---:|
| bertscore_f1 | 0.599 |
| coleman_liau | 7.66 |
| coleman_liau_drop | 1.96 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 6.37 |
| fkgl_drop | 2.10 |
| fre | 85.0 |
| fre_gain | 18.6 |
| human_edit_recall | 1.000 |
| length_ratio | 0.67 |
| n_words | 20.0 |
| nli_completeness | 0.705 |
| nli_faithfulness | 0.733 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.600 |
| sari | 26.69 |
| severity_downgrade | 0.000 |
| severity_preservation | 1.000 |
| severity_tier_input | 1.000 |
| severity_tier_output | 1.000 |
| smog | 3.13 |
| smog_drop | 8.08 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `aspiration` -> `breathing food into the lungs` | replace | attributed | 3.299 | 3.603 | 0.863 | 0.846 | 1.198 | - |
| `penetration` -> `throat` | replace | attributed | 0.074 | 0.195 | 0.708 | 0.738 | 0.505 | - |

**edit `aspiration` -> `breathing food into the lungs`**

- status: `attributed`
- log p full -1.3120, empty -4.6111
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+2.053` [readme] aspiration: Breathing food or liquid into your lungs by mistake.
    - `+0.855` [nih] aspiration: Removal of fluid or tissue through a needle. Also, the accidental breathing in of food or fluid in
    - `+0.624` [wiktionary] penetration: Penetration is the action of penetrating into something.
    - `+0.221` [wiktionary] penetration: Penetration is the penis being inserted into the vagina or another part of the body during sex.
    - `+0.113` [readme] aspiration: Breathing in food or liquid by mistake.

- rationale: The glossary defines aspiration as breathing food or liquid into your lungs by mistake, so the replacement phrase captures this exact mechanism in everyday language. Phrase frequency rises from Zipf 3.30 to 3.78, and age of acquisition drops from 11.47 to 6.52, indicating the new wording is both more common and learned earlier. This clarity helps patients recognize the specific danger of food entering the airway rather than the stomach.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `penetration` -> `throat`**

- status: `attributed`
- log p full -0.4414, empty -0.5156
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.840` [readme] aspiration: Breathing in food or liquid by mistake.
    - `+0.336` [nih] aspiration: Removal of fluid or tissue through a needle. Also, the accidental breathing in of food or fluid in
    - `+0.107` [wiktionary] penetration: Penetration is the action of penetrating into something.
    - `-0.085` [iowa] ASPIRATION: fluid entering the lungs, such as after vomiting
    - `-0.270` [readme] aspiration: Breathing food or liquid into your lungs by mistake.

- rationale: "Penetration" refers to the act of entering or piercing through something, so "throat" specifies the exact body part involved in plain language. Word frequency increases from Zipf 3.71 to 4.30, age of acquisition falls from 11.05 to 5.09, and syllables drop from 4 to 1. Patients can immediately identify the affected area without interpreting an abstract action.
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

**output:** The patient woke up, had the breathing tube removed, and moved to the recovery room in good condition.

| metric | value |
|---|---:|
| bertscore_f1 | 0.733 |
| coleman_liau | 8.98 |
| coleman_liau_drop | 4.57 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.667 |
| fkgl | 7.82 |
| fkgl_drop | 4.47 |
| fre | 71.1 |
| fre_gain | 37.4 |
| human_edit_recall | 1.000 |
| length_ratio | 0.90 |
| n_words | 18.0 |
| nli_completeness | 0.991 |
| nli_faithfulness | 0.986 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 39.28 |
| smog | 11.21 |
| smog_drop | 4.70 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `awakened` -> `woke up` | replace | - | - | - | - | - | - | - |
| `extubated` -> `had the breathing tube removed` | replace | - | - | - | - | - | - | - |
| `satisfactory` -> `good` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** The patient woke up, had the breathing tube removed, and moved to the recovery room in good condition.

| metric | value |
|---|---:|
| bertscore_f1 | 0.733 |
| coleman_liau | 8.98 |
| coleman_liau_drop | 4.57 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.667 |
| fkgl | 7.82 |
| fkgl_drop | 4.47 |
| fre | 71.1 |
| fre_gain | 37.4 |
| human_edit_recall | 1.000 |
| length_ratio | 0.90 |
| n_words | 18.0 |
| nli_completeness | 0.991 |
| nli_faithfulness | 0.986 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 39.28 |
| smog | 11.21 |
| smog_drop | 4.70 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `awakened` -> `woke up` | replace | attributed | 0.067 | 0.293 | - | 0.640 | 0.221 | - |
| `extubated` -> `had the breathing tube removed` | replace | attributed | 0.009 | 0.058 | - | 0.703 | 0.002 | - |
| `satisfactory` -> `good` | replace | attributed | 0.022 | 0.334 | - | 0.863 | 0.310 | - |

**edit `awakened` -> `woke up`**

- status: `attributed`
- log p full -0.2262, empty -0.2928
- masks scored: 34/34 (+4 top-k)
- ranked sources:
    - `+0.288` [readme] extubated: Not having a breathing tube anymore.
    - `+0.067` [readme] extubated: Taking out a tube used for breathing.
    - `+0.064` [wiktionary] satisfactory: If something is satisfactory, it is good enough.
    - `-0.316` [wiktionary] awakened: If you awaken somebody, they stop sleeping because of something you do.

- rationale: The term "awakened" means to stop sleeping, and "woke up" expresses this same idea in everyday language. Word frequency increases from Zipf 3.30 to 4.22, and the word becomes shorter, dropping from 3 syllables to 2. Readers can immediately grasp that the person stopped sleeping without encountering a formal or literary tone.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `extubated` -> `had the breathing tube removed`**

- status: `attributed`
- log p full -0.1569, empty -0.1654
- masks scored: 34/34 (+4 top-k)
- ranked sources:
    - `+0.019` [wiktionary] satisfactory: If something is satisfactory, it is good enough.
    - `+0.016` [readme] extubated: Not having a breathing tube anymore.
    - `-0.136` [readme] extubated: Taking out a tube used for breathing.

- rationale: "Extubated" means the breathing tube was taken out, so "had the breathing tube removed" states that action in everyday language. Word frequency rises from Zipf 1.26 to 3.95, though syllable count increases from 4 to 7. Readers can clearly grasp that the airway device is no longer in place.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `satisfactory` -> `good`**

- status: `attributed`
- log p full -0.0569, empty -0.0786
- masks scored: 34/34 (+4 top-k)
- ranked sources:
    - `+0.458` [wiktionary] satisfactory: If something is satisfactory, it is good enough.
    - `+0.148` [readme] extubated: Not having a breathing tube anymore.
    - `+0.074` [readme] extubated: Taking out a tube used for breathing.
    - `-0.150` [wiktionary] awakened: If you awaken somebody, they stop sleeping because of something you do.
    - `-0.536` [michigan] satisfactory: When something is okay or good.

- rationale: "Satisfactory" means meeting a required standard, and "good" conveys this positive assessment in simpler terms. Word frequency rises from Zipf 3.57 to 6.12, while age of acquisition drops from 8.84 to 3.55. Readers can quickly grasp that the result meets expectations without parsing formal language.
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

**output:** The patient was asleep but woke up easily.

| metric | value |
|---|---:|
| bertscore_f1 | 0.857 |
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
| nli_completeness | 0.439 |
| nli_faithfulness | 0.981 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 62.05 |
| smog | 8.84 |
| smog_drop | 5.71 |

### Stage 4 - arm `termonly`

**output:** The patient was asleep, but easily woken.

| metric | value |
|---|---:|
| bertscore_f1 | 0.952 |
| coleman_liau | 7.31 |
| coleman_liau_drop | 9.31 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 7.37 |
| fkgl_drop | 8.08 |
| fre | 54.7 |
| fre_gain | 52.6 |
| human_edit_recall | 1.000 |
| length_ratio | 0.88 |
| n_words | 7.0 |
| nli_completeness | 0.355 |
| nli_faithfulness | 0.991 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 88.89 |
| smog | 8.84 |
| smog_drop | 5.71 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `aroused` -> `woken` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** PHYSICAL EXAMINATION : GENERAL : The patient was asleep, but easily woken.

| metric | value |
|---|---:|
| bertscore_f1 | 0.524 |
| coleman_liau | 15.46 |
| coleman_liau_drop | 1.16 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 15.45 |
| fkgl_drop | 0.00 |
| fre | 2.1 |
| fre_gain | 0.0 |
| human_edit_recall | 1.000 |
| length_ratio | 1.25 |
| n_words | 10.0 |
| nli_completeness | 0.976 |
| nli_faithfulness | 0.985 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 80.25 |
| smog | 14.55 |
| smog_drop | 0.00 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `aroused` -> `woken` | replace | attributed | -0.154 | -0.327 | - | - | - | - |

**edit `aroused` -> `woken`**

- status: `attributed`
- log p full -0.7147, empty -0.5612
- masks scored: 4/4 (+1 top-k)
- ranked sources:
    - `-0.287` [wiktionary] aroused: If something arouses a feeling or emotion, it causes that feeling or emotion.

- rationale: The term "aroused" refers to being awakened from sleep, and "woken" conveys this same idea in more everyday language. Word frequency increases slightly from Zipf 3.35 to 3.37, while the syllable count remains unchanged at two. This allows readers to immediately grasp that the person was roused from slumber without encountering a less common verb.
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

**output:** He should come back in about 10 days for a checkup and to get a prescription for the AFOs he needs. He will need to use them for up to 6 months.

| metric | value |
|---|---:|
| bertscore_f1 | 0.586 |
| coleman_liau | 2.47 |
| coleman_liau_drop | 4.24 |
| copy_jargon_rate | 1.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 3.93 |
| fkgl_drop | 6.96 |
| fre | 95.4 |
| fre_gain | 32.1 |
| human_edit_recall | 0.000 |
| length_ratio | 1.14 |
| n_words | 32.0 |
| nli_completeness | 0.005 |
| nli_faithfulness | 0.990 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 0.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.667 |
| sari | 28.71 |
| smog | 7.17 |
| smog_drop | 5.86 |

### Stage 4 - arm `termonly`

**output:** He is to follow up in about 10 days for recheck as well as prescription for intended ankle braces, which he will need up to 6 months.

| metric | value |
|---|---:|
| bertscore_f1 | 0.881 |
| coleman_liau | 5.66 |
| coleman_liau_drop | 1.05 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 10.67 |
| fkgl_drop | 0.22 |
| fre | 66.6 |
| fre_gain | 3.3 |
| human_edit_recall | 1.000 |
| length_ratio | 0.96 |
| n_words | 27.0 |
| nli_completeness | 0.362 |
| nli_faithfulness | 0.381 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 54.83 |
| smog | 11.21 |
| smog_drop | 1.82 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `approximately` -> `about` | replace | - | - | - | - | - | - | - |
| `AFOs` -> `ankle braces` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** He is to follow up in about 10 days for recheck as well as prescription for intended ankle and foot braces, which he will need up to 6 months.

| metric | value |
|---|---:|
| bertscore_f1 | 0.868 |
| coleman_liau | 5.58 |
| coleman_liau_drop | 1.13 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 11.18 |
| fkgl_drop | -0.29 |
| fre | 66.5 |
| fre_gain | 3.2 |
| human_edit_recall | 1.000 |
| length_ratio | 1.04 |
| n_words | 29.0 |
| nli_completeness | 0.872 |
| nli_faithfulness | 0.613 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 55.69 |
| smog | 11.21 |
| smog_drop | 1.82 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `approximately` -> `about` | replace | attributed | -0.071 | -1.658 | - | 0.810 | 0.139 | - |
| `AFOs` -> `ankle and foot braces` | replace | attributed | 2.969 | 3.575 | - | 0.976 | 0.459 | - |

**edit `approximately` -> `about`**

- status: `attributed`
- log p full -0.0884, empty -0.0175
- masks scored: 10/10 (+2 top-k)
- ranked sources:
    - `+0.151` [justplainclear] AFO: Also known as: ankle-foot orthosis, walking boot A brace that supports your ankle or foot An AFO is a bra
    - `+0.013` [dorland] AFOs: ankle-foot orthosis
    - `-2.637` [wiktionary] approximately: Approximately is close to, but not exactly.

- rationale: "Approximately" means close to a value without being exact, and "about" conveys that same sense of estimation in simpler terms. Word frequency rises from Zipf 4.64 to 6.40, and the syllable count drops from 5 to 2. Readers can grasp the estimated nature of the figure without stumbling over a formal adverb.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `AFOs` -> `ankle and foot braces`**

- status: `attributed`
- log p full -0.7596, empty -3.7281
- masks scored: 10/10 (+2 top-k)
- ranked sources:
    - `+1.922` [justplainclear] AFO: Also known as: ankle-foot orthosis, walking boot A brace that supports your ankle or foot An AFO is a bra
    - `+1.463` [dorland] AFOs: ankle-foot orthosis
    - `+0.100` [wiktionary] approximately: Approximately is close to, but not exactly.

- rationale: AFOs are orthotic devices that support the ankle and foot, so "ankle and foot braces" conveys this function using everyday language. Word frequency rises from Zipf 1.36 to 3.35, while syllable count increases from 1 to 6. Readers can recognize the supportive equipment without needing to know the clinical abbreviation.
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

**output:** The outside parts of the genitals looked normal.

| metric | value |
|---|---:|
| bertscore_f1 | 0.467 |
| coleman_liau | 9.50 |
| coleman_liau_drop | 7.97 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.750 |
| fkgl | 5.23 |
| fkgl_drop | 8.85 |
| fre | 71.8 |
| fre_gain | 63.5 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 8.0 |
| nli_completeness | 0.901 |
| nli_faithfulness | 0.995 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.250 |
| sari | 28.00 |
| smog | 8.84 |
| smog_drop | 4.18 |

### Stage 4 - arm `termonly`

**output:** Genitourinary system: The outside sex organs looked normal.

| metric | value |
|---|---:|
| bertscore_f1 | 0.226 |
| coleman_liau | 16.75 |
| coleman_liau_drop | 0.73 |
| copy_jargon_rate | 0.250 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.667 |
| fkgl | 9.66 |
| fkgl_drop | 4.43 |
| fre | 40.1 |
| fre_gain | 31.7 |
| human_edit_recall | 0.750 |
| length_ratio | 1.00 |
| n_words | 8.0 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.948 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 24.48 |
| smog | 8.84 |
| smog_drop | 4.18 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `external genitalia` -> `outside sex organs` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Genitourinary: The outside sex organs looked normal.

| metric | value |
|---|---:|
| bertscore_f1 | 0.237 |
| coleman_liau | 16.43 |
| coleman_liau_drop | 1.05 |
| copy_jargon_rate | 0.250 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.667 |
| fkgl | 9.05 |
| fkgl_drop | 5.03 |
| fre | 42.6 |
| fre_gain | 34.2 |
| human_edit_recall | 0.750 |
| length_ratio | 0.88 |
| n_words | 7.0 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.962 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 23.89 |
| smog | 8.84 |
| smog_drop | 4.18 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `external genitalia` -> `outside sex organs` | replace | attributed | -0.101 | -0.120 | 0.715 | 0.895 | 0.224 | - |

**edit `external genitalia` -> `outside sex organs`**

- status: `attributed`
- log p full -1.9009, empty -1.7997
- masks scored: 66/66 (+2 top-k)
- ranked sources:
    - `+0.224` [iowa] EXTERNAL: outside the body
    - `-0.165` [wiktionary] external: Something that is external is not on the inside.
    - `-0.433` [wiktionary] genitalia: Genitalia are the body parts used for sex and reproduction, especially the parts on the outside of 

- rationale: "External genitalia" refers to the reproductive structures located on the outside of the body, so "outside sex organs" conveys this anatomical location in everyday language. Phrase frequency rises from Zipf 3.08 to 3.95, age of acquisition drops from 11.84 to 9.79, and syllable count decreases from 7 to 5. Readers can immediately identify the specific body parts involved without needing medical terminology.
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

**output:** She is 21 days past surgery, which was an exploratory laparotomy to stage her ovarian cancer.

| metric | value |
|---|---:|
| bertscore_f1 | 0.498 |
| coleman_liau | 9.90 |
| coleman_liau_drop | 1.02 |
| copy_jargon_rate | 0.250 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.667 |
| fkgl | 12.04 |
| fkgl_drop | 0.13 |
| fre | 37.3 |
| fre_gain | 6.3 |
| human_edit_recall | 0.750 |
| length_ratio | 0.94 |
| n_words | 16.0 |
| nli_completeness | 0.985 |
| nli_faithfulness | 0.991 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 0.857 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 51.80 |
| smog | 14.55 |
| smog_drop | -1.53 |

### Stage 4 - arm `termonly`

**output:** She is 21 days after surgery to look inside her belly and check for ovarian cancer.

| metric | value |
|---|---:|
| bertscore_f1 | 0.601 |
| coleman_liau | 6.64 |
| coleman_liau_drop | 4.29 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 9.09 |
| fkgl_drop | 3.08 |
| fre | 58.4 |
| fre_gain | 27.5 |
| human_edit_recall | 1.000 |
| length_ratio | 0.94 |
| n_words | 16.0 |
| nli_completeness | 0.464 |
| nli_faithfulness | 0.734 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 54.53 |
| smog | 11.21 |
| smog_drop | 1.82 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `postop` -> `21 days after` | replace | - | - | - | - | - | - | - |
| `ovarian cancer staging` -> `ovarian cancer` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** She is 21 days after surgery to check her belly and see how far ovarian cancer has spread.

| metric | value |
|---|---:|
| bertscore_f1 | 0.614 |
| coleman_liau | 5.76 |
| coleman_liau_drop | 5.17 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.750 |
| fkgl | 8.47 |
| fkgl_drop | 3.70 |
| fre | 66.4 |
| fre_gain | 35.4 |
| human_edit_recall | 1.000 |
| length_ratio | 1.06 |
| n_words | 18.0 |
| nli_completeness | 0.516 |
| nli_faithfulness | 0.254 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 54.77 |
| smog | 11.21 |
| smog_drop | 1.82 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `postop` -> `21 days after surgery` | replace | attributed | 0.255 | 0.951 | 0.538 | 0.411 | 0.086 | - |
| `ovarian cancer staging` -> `ovarian cancer has spread` | replace | attributed | 0.778 | 0.938 | 0.815 | 0.901 | 0.010 | - |

**edit `postop` -> `21 days after surgery`**

- status: `attributed`
- log p full -0.2019, empty -0.4568
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.153` [readme] postop: After surgery.
    - `+0.068` [readme] PostOP: PostOP means after surgery.
    - `+0.061` [readme] exploratory laparotomy: Surgery to check for problems in your belly.
    - `+0.045` [readme] cancer staging: Determining the extent to which cancer has spread in the body based on a numerical scale.

- rationale: "Postop" is a common abbreviation for the period following a surgical procedure, so "21 days after surgery" specifies the exact timeframe in clear, everyday language. Word frequency increases from Zipf 1.53 to 4.46, while the syllable count rises from 1 to 7. Patients can now grasp the precise timing of their recovery phase without needing to interpret medical shorthand.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `ovarian cancer staging` -> `ovarian cancer has spread`**

- status: `attributed`
- log p full -1.4161, empty -2.1939
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.368` [readme] exploratory laparotomy: Surgery to check for problems in your belly.
    - `+0.358` [readme] cancer staging: Determining the extent to which cancer has spread in the body based on a numerical scale.
    - `+0.157` [readme] Ovarian: Ovarian means related to the ovaries where eggs are produced.
    - `+0.135` [readme] PostOP: PostOP means after surgery.
    - `+0.087` [nih] ovarian: Having to do with the ovaries, the female reproductive glands in which the ova (eggs) are formed. The

- rationale: "Ovarian cancer staging" refers to the process of determining how far the cancer has progressed, which "ovarian cancer has spread" conveys in everyday language. Word frequency increases from Zipf 3.24 to 3.43, while age of acquisition remains unchanged at 14.44. This phrasing helps patients grasp the extent of the disease without needing to understand clinical classification systems.
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

**output:** He was given a prescription for prednisone as part of his chemotherapy.

| metric | value |
|---|---:|
| bertscore_f1 | 0.538 |
| coleman_liau | 10.25 |
| coleman_liau_drop | 0.67 |
| copy_jargon_rate | 1.000 |
| critical_error | 0.000 |
| drug_preservation | 1.000 |
| fkgl | 8.76 |
| fkgl_drop | -0.22 |
| fre | 53.7 |
| fre_gain | -3.3 |
| human_edit_recall | 0.000 |
| length_ratio | 0.80 |
| n_words | 12.0 |
| nli_completeness | 0.988 |
| nli_faithfulness | 0.992 |
| replacement_f1 | 0.000 |
| rewrite_aggressiveness | 1.000 |
| sari | 25.39 |
| smog | 11.21 |
| smog_drop | 0.00 |

### Stage 4 - arm `termonly`

**output:** He was given a medicine that is part of his cancer treatment.

| metric | value |
|---|---:|
| bertscore_f1 | 0.512 |
| coleman_liau | 5.42 |
| coleman_liau_drop | 5.51 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| drug_preservation | 0.000 |
| fkgl | 5.81 |
| fkgl_drop | 2.73 |
| fre | 74.8 |
| fre_gain | 17.8 |
| human_edit_recall | 1.000 |
| length_ratio | 0.80 |
| n_words | 12.0 |
| nli_completeness | 0.018 |
| nli_faithfulness | 0.983 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.600 |
| sari | 35.39 |
| smog | 8.84 |
| smog_drop | 2.37 |

annotation backend `novita`, 0 edits kept


### Stage 4 - arm `grounded`

**output:** He was given a medicine that lowers immune response as part of his cancer drug treatment.

| metric | value |
|---|---:|
| bertscore_f1 | 0.456 |
| coleman_liau | 8.81 |
| coleman_liau_drop | 2.11 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| drug_preservation | 0.000 |
| fkgl | 8.35 |
| fkgl_drop | 0.19 |
| fre | 63.7 |
| fre_gain | 6.7 |
| human_edit_recall | 1.000 |
| length_ratio | 1.07 |
| n_words | 16.0 |
| nli_completeness | 0.056 |
| nli_faithfulness | 0.549 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.600 |
| sari | 41.28 |
| smog | 8.84 |
| smog_drop | 2.37 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `chemotherapy` -> `cancer drug treatment` | replace | attributed | 0.397 | 0.551 | 0.580 | 0.844 | 0.201 | - |

**edit `chemotherapy` -> `cancer drug treatment`**

- status: `attributed`
- log p full -1.0886, empty -1.4856
- masks scored: 66/66 (+2 top-k)
- ranked sources:
    - `+0.372` [nih] chemotherapy: Treatment that uses drugs to stop the growth of cancer cells, either by killing the cells or by 
    - `+0.171` [nih] prednisone: A drug used to reduce inflammation and lower the body’s immune response.  It is used with other dr
    - `-0.046` [iowa] CHEMOTHERAPY: treatment of disease, usually cancer, by chemical agents

- rationale: Chemotherapy refers to the use of powerful drugs to kill cancer cells, and "cancer drug treatment" conveys this concept using everyday language. Phrase frequency rises from Zipf 3.56 to 4.46, while age of acquisition drops from 12.53 to 8.39. Readers can grasp that the therapy involves medication aimed at fighting cancer without needing specialized medical vocabulary.
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

**output:** The patient was exposed to flashing lights, but there was no clear sign that the brain was responding to them.

| metric | value |
|---|---:|
| bertscore_f1 | 0.460 |
| coleman_liau | 8.53 |
| coleman_liau_drop | 5.67 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 6.96 |
| fkgl_drop | 2.12 |
| fre | 80.8 |
| fre_gain | 31.2 |
| human_edit_recall | 1.000 |
| length_ratio | 1.18 |
| n_words | 20.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.873 |
| nli_faithfulness | 0.383 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 27.23 |
| smog | 8.84 |
| smog_drop | 0.00 |

### Stage 4 - arm `termonly`

**output:** The patient was shown flashing lights, but no clear brain response was seen.

| metric | value |
|---|---:|
| bertscore_f1 | 0.527 |
| coleman_liau | 9.58 |
| coleman_liau_drop | 4.62 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 4.00 |
| fkgl_drop | 5.08 |
| fre | 89.5 |
| fre_gain | 40.0 |
| human_edit_recall | 1.000 |
| length_ratio | 0.76 |
| n_words | 13.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.808 |
| nli_faithfulness | 0.192 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.200 |
| sari | 34.26 |
| smog | 3.13 |
| smog_drop | 5.71 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `Photic stimulation` -> `shown flashing lights` | replace | - | - | - | - | - | - | - |
| `photic driving` -> `brain response` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Light flashes were used, but no clear brain response was seen.

| metric | value |
|---|---:|
| bertscore_f1 | 0.645 |
| coleman_liau | 7.87 |
| coleman_liau_drop | 6.33 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.167 |
| fkgl | 2.65 |
| fkgl_drop | 6.44 |
| fre | 95.7 |
| fre_gain | 46.1 |
| human_edit_recall | 1.000 |
| length_ratio | 0.65 |
| n_words | 11.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.947 |
| nli_faithfulness | 0.824 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.200 |
| sari | 32.97 |
| smog | 3.13 |
| smog_drop | 5.71 |

annotation backend `novita`, 0 edits kept


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

**output:** Both of the patient's parents died from heart attacks.

| metric | value |
|---|---:|
| bertscore_f1 | 0.545 |
| coleman_liau | 9.27 |
| coleman_liau_drop | 9.66 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 3.65 |
| fkgl_drop | 11.90 |
| fre | 84.9 |
| fre_gain | 87.1 |
| human_edit_recall | 1.000 |
| laterality_preservation | 1.000 |
| length_ratio | 1.25 |
| n_words | 10.0 |
| nli_completeness | 0.754 |
| nli_faithfulness | 0.912 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 25.93 |
| smog | 3.13 |
| smog_drop | 11.43 |

### Stage 4 - arm `termonly`

**output:** FAMILY HISTORY : Both parents died with heart attacks.

| metric | value |
|---|---:|
| bertscore_f1 | 0.744 |
| coleman_liau | 12.40 |
| coleman_liau_drop | 6.52 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 8.18 |
| fkgl_drop | 7.38 |
| fre | 50.7 |
| fre_gain | 52.9 |
| human_edit_recall | 1.000 |
| laterality_preservation | 1.000 |
| length_ratio | 1.00 |
| n_words | 8.0 |
| nli_completeness | 0.788 |
| nli_faithfulness | 0.946 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 100.00 |
| smog | 11.21 |
| smog_drop | 3.35 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `myocardial infarctions` -> `heart attacks` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** FAMILY HISTORY: Both parents died with heart attacks.

| metric | value |
|---|---:|
| bertscore_f1 | 0.782 |
| coleman_liau | 12.40 |
| coleman_liau_drop | 6.52 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 8.18 |
| fkgl_drop | 7.38 |
| fre | 50.7 |
| fre_gain | 52.9 |
| human_edit_recall | 1.000 |
| laterality_preservation | 1.000 |
| length_ratio | 1.00 |
| n_words | 8.0 |
| nli_completeness | 0.780 |
| nli_faithfulness | 0.947 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 100.00 |
| smog | 11.21 |
| smog_drop | 3.35 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `myocardial infarctions` -> `heart attacks` | replace | attributed | 0.003 | 1.253 | - | 0.377 | 0.001 | - |

**edit `myocardial infarctions` -> `heart attacks`**

- status: `attributed`
- log p full -0.0012, empty -0.0043
- masks scored: 34/34 (+2 top-k)
- ranked sources:
    - `+0.062` [michigan] myocardial infarction: Occurs when the flow of blood to the heart is stopped by a blood clot or a spasm of an 
    - `+0.060` [readme] inferior wall myocardial infarction: Heart damage at the bottom of the left ventricle due to a blocked artery.
    - `+0.045` [iowa] MYOCARDIAL INFARCTION: heart attack
    - `+0.002` [readme] inferior myocardial infarction: A heart attack caused by a blockage in a blood vessel that affects the lower p
    - `-0.202` [justplainclear] myocardial infarction: A heart attack

- rationale: "Myocardial infarctions" refers to damage to the heart muscle caused by blocked blood flow, which "heart attacks" conveys in everyday language. Phrase frequency rises from Zipf 1.57 to 4.59, age of acquisition drops from 16.64 to 5.17, and syllable count decreases from 8 to 3. Readers can immediately recognize this common emergency condition without needing specialized medical training.
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

**output:** The patient has moderate swelling in both legs that leaves a dent when pressed, reaching up to the knees.

| metric | value |
|---|---:|
| bertscore_f1 | 0.452 |
| coleman_liau | 8.59 |
| coleman_liau_drop | 0.87 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 6.73 |
| fkgl_drop | 4.50 |
| fre | 80.7 |
| fre_gain | 46.5 |
| human_edit_recall | 1.000 |
| laterality_preservation | 1.000 |
| length_ratio | 0.68 |
| n_words | 19.0 |
| nli_completeness | 0.650 |
| nli_faithfulness | 0.600 |
| number_unit_preservation | 0.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.200 |
| sari | 38.47 |
| smog | 8.84 |
| smog_drop | 4.18 |

### Stage 4 - arm `termonly`

**output:** Arms and legs: 2+ swelling on both sides that leaves a dent, up to the knees.

| metric | value |
|---|---:|
| bertscore_f1 | 0.464 |
| coleman_liau | 3.38 |
| coleman_liau_drop | 6.08 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 3.19 |
| fkgl_drop | 8.04 |
| fre | 100.7 |
| fre_gain | 66.5 |
| human_edit_recall | 1.000 |
| laterality_preservation | 1.000 |
| length_ratio | 0.57 |
| n_words | 16.0 |
| nli_completeness | 0.955 |
| nli_faithfulness | 0.565 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.200 |
| sari | 34.55 |
| smog | 3.13 |
| smog_drop | 9.89 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `bilateral pitting edema` -> `swelling on both sides that leaves a dent` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Arms and legs: 2+ swelling on both sides that leaves a dent when pressed, up to the knees.

| metric | value |
|---|---:|
| bertscore_f1 | 0.508 |
| coleman_liau | 4.79 |
| coleman_liau_drop | 4.67 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 3.89 |
| fkgl_drop | 7.34 |
| fre | 99.3 |
| fre_gain | 65.1 |
| human_edit_recall | 1.000 |
| laterality_preservation | 1.000 |
| length_ratio | 0.64 |
| n_words | 18.0 |
| nli_completeness | 0.953 |
| nli_faithfulness | 0.388 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.200 |
| sari | 35.79 |
| smog | 3.13 |
| smog_drop | 9.89 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `bilateral pitting edema` -> `swelling on both sides that leaves a dent when pressed` | replace | attributed | 1.102 | 1.136 | 0.879 | 0.933 | 2.330 | - |

**edit `bilateral pitting edema` -> `swelling on both sides that leaves a dent when pressed`**

- status: `attributed`
- log p full -3.0050, empty -4.1068
- masks scored: 66/66 (+2 top-k)
- ranked sources:
    - `+2.780` [readme] pitting edema: Swelling in the body that leaves an indention (pit) when pressed.
    - `+0.450` [wiktionary] extremities: An extremity is a part of an animal's body that is used to move around and to hold objects.
    - `+0.288` [thesaurus] bilateral: with both sides considered, two-sided, when both sides get a say, even, balanced

- rationale: The glossary defines the condition as swelling that leaves an indention when pressed, so the replacement phrase captures this physical sign in everyday language. Phrase frequency rises from Zipf 2.64 to 3.27, and age of acquisition drops from 15.07 to 7.33. Readers can recognize the specific type of swelling by its visible effect rather than needing the clinical term.
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

**output:** The following questions are mostly used in a psychosocial donor evaluation.

| metric | value |
|---|---:|
| bertscore_f1 | 0.517 |
| coleman_liau | 15.25 |
| coleman_liau_drop | 3.69 |
| copy_jargon_rate | 1.000 |
| critical_error | 0.000 |
| fkgl | 12.30 |
| fkgl_drop | 1.97 |
| fre | 26.5 |
| fre_gain | 15.9 |
| human_edit_recall | 0.000 |
| length_ratio | 0.73 |
| n_words | 11.0 |
| nli_completeness | 0.986 |
| nli_faithfulness | 0.985 |
| replacement_f1 | 0.000 |
| rewrite_aggressiveness | 1.000 |
| sari | 21.16 |
| smog | 13.02 |
| smog_drop | 0.00 |

### Stage 4 - arm `termonly`

**output:** The questions mostly involve a social and mental donor check.

| metric | value |
|---|---:|
| bertscore_f1 | 0.468 |
| coleman_liau | 10.82 |
| coleman_liau_drop | 8.12 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 7.19 |
| fkgl_drop | 7.08 |
| fre | 61.3 |
| fre_gain | 50.8 |
| human_edit_recall | 1.000 |
| length_ratio | 0.67 |
| n_words | 10.0 |
| nli_completeness | 0.961 |
| nli_faithfulness | 0.852 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.750 |
| sari | 16.45 |
| smog | 3.13 |
| smog_drop | 9.89 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `psychosocial` -> `social and mental` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** The questions mostly involve a donor check of mental and social factors.

| metric | value |
|---|---:|
| bertscore_f1 | 0.513 |
| coleman_liau | 10.73 |
| coleman_liau_drop | 8.21 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 7.77 |
| fkgl_drop | 6.50 |
| fre | 60.7 |
| fre_gain | 50.1 |
| human_edit_recall | 1.000 |
| length_ratio | 0.80 |
| n_words | 12.0 |
| nli_completeness | 0.979 |
| nli_faithfulness | 0.915 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.750 |
| sari | 18.37 |
| smog | 3.13 |
| smog_drop | 9.89 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `psychosocial` -> `mental and social factors` | replace | attributed | 2.868 | 3.671 | - | 1.000 | 0.267 | - |

**edit `psychosocial` -> `mental and social factors`**

- status: `attributed`
- log p full -0.5688, empty -3.4368
- masks scored: 6/6 (+1 top-k)
- ranked sources:
    - `+1.889` [nih] psychosocial: In medicine, having to do with the mental, emotional, social, and spiritual effects of a disease
    - `+1.622` [michigan] psychosocial: Including both the mental and social aspects of disease.

- rationale: "Psychosocial" refers to the interplay between psychological and social aspects of health, so "mental and social factors" expresses this concept in everyday language. Phrase frequency rises from Zipf 2.88 to 4.38, and age of acquisition drops from 15.44 to 10.43. Readers can grasp how both mind and environment influence well-being without needing specialized terminology.
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

**output:** The patient has mild atherosclerosis in the descending aorta that does not move.

| metric | value |
|---|---:|
| bertscore_f1 | 0.261 |
| coleman_liau | 11.82 |
| coleman_liau_drop | 17.50 |
| copy_jargon_rate | 0.250 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 10.36 |
| fkgl_drop | 13.76 |
| fre | 44.0 |
| fre_gain | 112.9 |
| human_edit_recall | 0.750 |
| length_ratio | 0.59 |
| n_words | 13.0 |
| nli_completeness | 0.991 |
| nli_faithfulness | 0.980 |
| replacement_f1 | 0.857 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 39.50 |
| severity_downgrade | 0.000 |
| severity_preservation | 1.000 |
| severity_tier_input | 1.000 |
| severity_tier_output | 1.000 |
| smog | 13.02 |
| smog_drop | 1.53 |

### Stage 4 - arm `termonly`

**output:** Mild plaque in the lower part of the main artery that does not move.

| metric | value |
|---|---:|
| bertscore_f1 | 0.417 |
| coleman_liau | 4.46 |
| coleman_liau_drop | 24.86 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 4.20 |
| fkgl_drop | 19.92 |
| fre | 89.9 |
| fre_gain | 158.9 |
| human_edit_recall | 1.000 |
| length_ratio | 0.64 |
| n_words | 14.0 |
| nli_completeness | 0.776 |
| nli_faithfulness | 0.954 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 45.65 |
| severity_downgrade | 0.000 |
| severity_preservation | 1.000 |
| severity_tier_input | 1.000 |
| severity_tier_output | 1.000 |
| smog | 8.84 |
| smog_drop | 5.71 |

annotation backend `novita`, 0 edits kept


### Stage 4 - arm `grounded`

**output:** Mild clogging in the main chest artery that does not move.

| metric | value |
|---|---:|
| bertscore_f1 | 0.383 |
| coleman_liau | 6.29 |
| coleman_liau_drop | 23.03 |
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
| nli_completeness | 0.494 |
| nli_faithfulness | 0.904 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 44.23 |
| severity_downgrade | 0.000 |
| severity_preservation | 1.000 |
| severity_tier_input | 1.000 |
| severity_tier_output | 1.000 |
| smog | 8.84 |
| smog_drop | 5.71 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `atherosclerosis` -> `clogging` | replace | attributed | 5.148 | 5.458 | - | 0.962 | 0.266 | - |

**edit `atherosclerosis` -> `clogging`**

- status: `attributed`
- log p full -1.3203, empty -6.4688
- masks scored: 18/18 (+2 top-k)
- ranked sources:
    - `+2.325` [michigan] atherosclerosis: A disease where your arteries get stiff and clogged by things in your blood, such as fat and 
    - `+2.059` [thesaurus] atherosclerosis: hardening of the arteries, clogged blood vessels
    - `+0.422` [readme] descending aortic: Descending aortic: The area of the main artery as it travels through the chest.
    - `+0.097` [justplainclear] atherosclerosis: A disease where arteries get thick and prevent the flow of blood Normal artery and atheroscle

- rationale: Atherosclerosis refers to the buildup of plaque in arteries, and "clogging" captures this narrowing process in everyday language. Word frequency rises from Zipf 2.78 to 2.91, while syllable count drops from 6 to 2. Readers can grasp how blocked arteries affect blood flow without needing the technical diagnosis.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

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

**output:** The tube to the ear was blocked with a waxy material.

| metric | value |
|---|---:|
| bertscore_f1 | 0.629 |
| coleman_liau | 3.65 |
| coleman_liau_drop | 6.57 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.400 |
| fkgl | 4.79 |
| fkgl_drop | 1.91 |
| fre | 80.3 |
| fre_gain | 19.1 |
| human_edit_recall | 1.000 |
| length_ratio | 0.85 |
| n_words | 11.0 |
| nli_completeness | 0.083 |
| nli_faithfulness | 0.974 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 34.89 |
| smog | 8.84 |
| smog_drop | 2.37 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `eustachian tube` -> `tube to the ear` | replace | - | - | - | - | - | - | - |
| `obstructed` -> `blocked` | replace | - | - | - | - | - | - | - |
| `bone wax` -> `a waxy material` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** The tube from the middle ear to the throat was blocked with a waxy material.

| metric | value |
|---|---:|
| bertscore_f1 | 0.618 |
| coleman_liau | 5.81 |
| coleman_liau_drop | 4.41 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.400 |
| fkgl | 5.99 |
| fkgl_drop | 0.71 |
| fre | 78.8 |
| fre_gain | 17.6 |
| human_edit_recall | 1.000 |
| length_ratio | 1.15 |
| n_words | 15.0 |
| nli_completeness | 0.092 |
| nli_faithfulness | 0.932 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 34.18 |
| smog | 8.84 |
| smog_drop | 2.37 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `obstructed` -> `blocked` | replace | attributed | 0.008 | 0.810 | 0.590 | 0.792 | 0.193 | - |
| `bone wax` -> `waxy material` | replace | attributed | 0.360 | 0.466 | 0.493 | 0.778 | 0.037 | - |

**edit `obstructed` -> `blocked`**

- status: `attributed`
- log p full -0.0066, empty -0.0148
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.425` [justplainclear] eustachian tube: The tube that connects your middle ear to the back of your throat and pharynx area. The openi
    - `+0.232` [wiktionary] obstructed: If something obstructs your way, it blocks your path from point A to point B.
    - `+0.072` [wiktionary] wax: Wax is a solid material made of animal fat.
    - `+0.038` [wiktionary] bone: Bones are the hard, white things inside your body. They give your body its shape.

- rationale: "Obstructed" means something is in the way, and "blocked" conveys that same idea in simpler terms. Word frequency rises from Zipf 2.98 to 4.31, and the word becomes shorter, dropping from 3 syllables to 1. Readers can quickly grasp that a passage is closed off without stumbling over a longer, less common word.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `bone wax` -> `waxy material`**

- status: `attributed`
- log p full -1.3092, empty -1.6692
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.385` [wiktionary] wax: If you wax something, you put wax on it, for example, a car.
    - `+0.348` [wiktionary] wax: Wax is a solid material made of animal fat.
    - `-0.059` [wiktionary] obstructed: If something obstructs your way, it blocks your path from point A to point B.

- rationale: Bone wax is a substance used to stop bleeding from bone surfaces, and "waxy material" conveys this texture and function in everyday terms. Word frequency decreases from Zipf 3.81 to 2.71, while age of acquisition rises from 6.00 to 8.06. Readers can grasp the nature of the substance used to control bleeding without needing specialized surgical vocabulary.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

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

### Stage 4 - arm `termonly`

**output:** He lay on his back on the operating room table.

| metric | value |
|---|---:|
| bertscore_f1 | 0.566 |
| coleman_liau | 2.70 |
| coleman_liau_drop | 3.99 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 4.83 |
| fkgl_drop | 1.45 |
| fre | 78.2 |
| fre_gain | 12.1 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 10.0 |
| nli_completeness | 0.945 |
| nli_faithfulness | 0.970 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 50.81 |
| smog | 8.84 |
| smog_drop | 0.00 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `supine` -> `on his back` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** He lay on his back on the operating room table.

| metric | value |
|---|---:|
| bertscore_f1 | 0.566 |
| coleman_liau | 2.70 |
| coleman_liau_drop | 3.99 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 4.83 |
| fkgl_drop | 1.45 |
| fre | 78.2 |
| fre_gain | 12.1 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 10.0 |
| nli_completeness | 0.945 |
| nli_faithfulness | 0.970 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 50.81 |
| smog | 8.84 |
| smog_drop | 0.00 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `supine` -> `on his back` | replace | attributed | 0.779 | 3.042 | - | 0.656 | 0.035 | - |

**edit `supine` -> `on his back`**

- status: `attributed`
- log p full -0.0610, empty -0.8404
- masks scored: 18/18 (+2 top-k)
- ranked sources:
    - `+0.527` [michigan] supine: To lie on your back.
    - `+0.491` [iowa] SUPINE: lying on the back
    - `+0.384` [readme] supine: Lying on your back.
    - `+0.094` [readme] Supine: Lying down on your back.

- rationale: "Supine" means lying face up, so "on his back" conveys the same position in everyday language. Phrase frequency rises from Zipf 2.42 to 5.87, and age of acquisition drops from 16.43 to 5.31. Readers can picture the body position without needing a medical term.
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

**output:** The doctors did not test the patient's urine this time.

| metric | value |
|---|---:|
| bertscore_f1 | 0.637 |
| coleman_liau | 6.76 |
| coleman_liau_drop | 1.38 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 3.65 |
| fkgl_drop | 3.72 |
| fre | 86.7 |
| fre_gain | 32.0 |
| human_edit_recall | 1.000 |
| length_ratio | 1.38 |
| n_words | 11.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.991 |
| nli_faithfulness | 0.540 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 25.51 |
| smog | 3.13 |
| smog_drop | 5.71 |

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
| `urinalysis` -> `urine test` | replace | attributed | -0.122 | -0.582 | - | 0.943 | 0.513 | - |
| `urinalysis` -> `done` | replace | attributed | -0.043 | -0.259 | - | 0.617 | 0.080 | - |

**edit `urinalysis` -> `urine test`**

- status: `attributed`
- log p full -0.3010, empty -0.1791
- masks scored: 34/34 (+4 top-k)
- ranked sources:
    - `+1.170` [justplainclear] urinalysis: Also known as: urine test, pee test A test of your urine used to find certain medical conditions
    - `+0.657` [michigan] urinalysis: A test of your urine to check for diseases, such as diabetes, urinary tract infections, or kidney 
    - `+0.336` [nih] urinalysis: A test that determines the content of the urine.
    - `-1.288` [readme] urinalysis: A test that checks the contents of your pee to see what's in there.
    - `-1.651` [readme] Urinalysis: A test that checks what's in your pee.

- rationale: "Urinalysis" refers to the laboratory examination of urine, which "urine test" expresses in everyday language. Phrase frequency rises from Zipf 2.20 to 3.82, age of acquisition drops from 14.68 to 9.83, and syllable count falls from 5 to 3. Readers can grasp that a sample of urine will be checked without needing the technical term.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `urinalysis` -> `done`**

- status: `attributed`
- log p full -0.2041, empty -0.1611
- masks scored: 34/34 (+4 top-k)
- ranked sources:
    - `+0.226` [michigan] urinalysis: A test of your urine to check for diseases, such as diabetes, urinary tract infections, or kidney 
    - `+0.146` [readme] Urinalysis: A test that checks what's in your pee.
    - `-0.012` [readme] urinalysis: A test that checks the contents of your pee to see what's in there.
    - `-0.223` [justplainclear] urinalysis: Also known as: urine test, pee test A test of your urine used to find certain medical conditions
    - `-0.244` [nih] urinalysis: A test that determines the content of the urine.

- rationale: "Urinalysis" refers to a laboratory test of urine, and replacing it with "done" signals that this check has been completed in simple terms. Word frequency rises from Zipf 2.20 to 5.58, and syllable count drops from 5 to 1. Readers can quickly grasp that the test is finished without needing to know the technical name.
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

**output:** Her vision and hearing were good enough for the tests, but she said she needed to update her eyeglass prescription.

| metric | value |
|---|---:|
| bertscore_f1 | 0.649 |
| coleman_liau | 9.98 |
| coleman_liau_drop | 3.74 |
| copy_jargon_rate | 0.667 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.250 |
| fkgl | 8.73 |
| fkgl_drop | 3.54 |
| fre | 68.1 |
| fre_gain | 23.6 |
| human_edit_recall | 0.333 |
| length_ratio | 0.95 |
| n_words | 20.0 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.995 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 22.43 |
| smog | 8.84 |
| smog_drop | 4.18 |

### Stage 4 - arm `termonly`

**output:** Her sight and hearing were good enough for testing, though she said she needed new glasses.

| metric | value |
|---|---:|
| bertscore_f1 | 0.607 |
| coleman_liau | 9.18 |
| coleman_liau_drop | 4.55 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.286 |
| fkgl | 6.14 |
| fkgl_drop | 6.13 |
| fre | 79.6 |
| fre_gain | 35.0 |
| human_edit_recall | 1.000 |
| length_ratio | 0.76 |
| n_words | 16.0 |
| nli_completeness | 0.992 |
| nli_faithfulness | 0.995 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.444 |
| sari | 17.45 |
| smog | 3.13 |
| smog_drop | 9.89 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `eyeglass prescription` -> `new glasses` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Vision and hearing seemed good enough for testing, although she said she needed to update her glasses.

| metric | value |
|---|---:|
| bertscore_f1 | 0.804 |
| coleman_liau | 11.12 |
| coleman_liau_drop | 2.61 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.286 |
| fkgl | 8.39 |
| fkgl_drop | 3.87 |
| fre | 65.2 |
| fre_gain | 20.6 |
| human_edit_recall | 1.000 |
| length_ratio | 0.81 |
| n_words | 17.0 |
| nli_completeness | 0.982 |
| nli_faithfulness | 0.994 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.167 |
| sari | 38.72 |
| smog | 3.13 |
| smog_drop | 9.89 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `adequate` -> `good enough` | replace | attributed | 0.096 | 2.077 | 0.743 | 0.919 | 1.173 | - |
| `did indicate` -> `said` | replace | attributed | -0.053 | -0.534 | 0.671 | 0.753 | 0.048 | - |
| `eyeglass prescription` -> `glasses` | replace | attributed | 0.080 | 0.594 | 0.395 | 0.857 | 0.373 | - |

**edit `adequate` -> `good enough`**

- status: `attributed`
- log p full -0.0145, empty -0.1101
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+1.274` [wiktionary] adequate: If something is adequate, it is good enough.
    - `+0.101` [justplainclear] eyeglass: A single lens used to help you see more clearly.
    - `+0.097` [wiktionary] did: Do is an auxiliary verb. It is used in questions, negative statements, short answers, and for emphasis wh
    - `+0.050` [nih] prescription: A doctor's order for medicine or another intervention.

- rationale: "Adequate" means sufficient or acceptable, and "good enough" conveys that same idea in everyday language. Word frequency rises from Zipf 4.05 to 5.44, and age of acquisition drops from 10.35 to 6.96. Readers can grasp that the result meets the necessary standard without wrestling with formal vocabulary.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `did indicate` -> `said`**

- status: `attributed`
- log p full -0.1338, empty -0.0806
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+0.140` [thesaurus] prescription: doctors orders, medicine, drug order
    - `+0.092` [justplainclear] adequate: Enough
    - `+0.068` [wiktionary] did: Do is an auxiliary verb. It is used in questions, negative statements, short answers, and for emphasis wh
    - `+0.029` [michigan] prescription: An order from your doctor, nurse, or physician assistant for drugs or other treatment.

- rationale: "Did indicate" means to point out or state something, and "said" conveys that same act of speaking in simpler terms. Word frequency rises from Zipf 4.34 to 6.01, and syllable count drops from 4 to 1. Readers can quickly grasp that the doctor or test result communicated a finding without parsing extra words.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `eyeglass prescription` -> `glasses`**

- status: `attributed`
- log p full -0.1084, empty -0.1885
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+0.522` [justplainclear] eyeglass: A single lens used to help you see more clearly.
    - `+0.149` [thesaurus] prescription: doctors orders, medicine, drug order
    - `+0.105` [nih] prescription: A doctor's order for medicine or another intervention.
    - `+0.105` [thesaurus] indicate: suggest, point to
    - `+0.095` [michigan] prescription: An order from your doctor, nurse, or physician assistant for drugs or other treatment.

- rationale: "Eyeglass prescription" refers to the specific lens measurements needed for vision correction, so "glasses" captures the everyday object that fulfills this need. Word frequency rises from Zipf 2.32 to 4.34, age of acquisition drops from 9.22 to 4.35, and syllable count decreases from 5 to 2. Readers can quickly grasp that the discussion concerns their corrective eyewear rather than technical optical data.
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

**output:** The doctor has talked to him several times about a colonoscopy, but he has refused it. So, they have been testing his stool for hidden blood.

| metric | value |
|---|---:|
| bertscore_f1 | 0.600 |
| coleman_liau | 6.91 |
| coleman_liau_drop | 0.71 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.667 |
| fkgl | 4.00 |
| fkgl_drop | 4.03 |
| fre | 89.5 |
| fre_gain | 9.3 |
| human_edit_recall | 1.000 |
| length_ratio | 0.57 |
| n_words | 26.0 |
| nli_completeness | 0.001 |
| nli_faithfulness | 0.921 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.250 |
| sari | 37.72 |
| smog | 3.13 |
| smog_drop | 0.00 |

### Stage 4 - arm `termonly`

**output:** I have talked to him several times about a test to look inside the large intestine, which he has refused, and so we have been checking his bowel movements for hidden blood.

| metric | value |
|---|---:|
| bertscore_f1 | 0.648 |
| coleman_liau | 8.29 |
| coleman_liau_drop | -0.67 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 12.38 |
| fkgl_drop | -4.35 |
| fre | 63.3 |
| fre_gain | -16.9 |
| human_edit_recall | 1.000 |
| length_ratio | 0.70 |
| n_words | 32.0 |
| nli_completeness | 0.904 |
| nli_faithfulness | 0.961 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 63.73 |
| smog | 8.84 |
| smog_drop | -5.71 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `colonoscopy` -> `test to look inside the large intestine` | replace | - | - | - | - | - | - | - |
| `stools` -> `bowel movements` | replace | - | - | - | - | - | - | - |
| `occult blood` -> `hidden blood` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** I have talked to him several times about a test to check the inside of the large intestine, which he has refused, and so we have been testing poop for hidden blood.

| metric | value |
|---|---:|
| bertscore_f1 | 0.636 |
| coleman_liau | 6.84 |
| coleman_liau_drop | 0.78 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.750 |
| fkgl | 11.64 |
| fkgl_drop | -3.61 |
| fre | 68.6 |
| fre_gain | -11.7 |
| human_edit_recall | 1.000 |
| length_ratio | 0.70 |
| n_words | 32.0 |
| nli_completeness | 0.906 |
| nli_faithfulness | 0.966 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 63.38 |
| smog | 8.84 |
| smog_drop | -5.71 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `colonoscopy` -> `test to check the inside of the large intestine` | replace | attributed | 3.996 | 4.248 | 0.841 | 0.977 | 0.435 | - |
| `stools` -> `poop` | replace | attributed | 1.152 | 1.662 | 0.828 | 0.934 | 0.873 | - |
| `occult blood` -> `hidden blood` | replace | attributed | 0.005 | 1.273 | 0.475 | 0.898 | 0.045 | - |

**edit `colonoscopy` -> `test to check the inside of the large intestine`**

- status: `attributed`
- log p full -1.4889, empty -5.4852
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+2.020` [readme] colonoscopy: A colonoscopy is a test that checks the inside of your large intestine for signs of cancer.
    - `+1.585` [readme] colonoscopy: A procedure to check for colon cancer by examining the inside of the large intestine.
    - `+0.395` [nih] colonoscopy: Examination of the inside of the colon using a colonoscope, inserted into the rectum. A colonosco
    - `+0.056` [readme] Occult: Secret knowledge or practices that are mysterious or not easily understood.

- rationale: The glossary defines a colonoscopy as a test that checks the inside of the large intestine for signs of cancer, so the replacement phrase captures this core purpose in everyday language. Phrase frequency rises from Zipf 2.74 to 3.21, and age of acquisition drops from 15.76 to 9.28, indicating the new wording is more familiar and learned earlier. Patients can now grasp what the procedure involves without needing to know the specific medical term.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `stools` -> `poop`**

- status: `attributed`
- log p full -0.7070, empty -1.8594
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+1.051` [readme] stools: Poop.
    - `+0.178` [wiktionary] occult: If something is occult it is part of the universe most people do not see. An occult thing is something
    - `+0.151` [readme] Blood: Blood is a vital fluid that carries nutrients and oxygen to our body's tissues through the heart's pump
    - `+0.125` [michigan] blood: A fluid in your body that carries things that are needed for your body to work well, such as vitamins, 
    - `+0.078` [readme] stools: Stools are the stuff that comes out when you go to the bathroom.

- rationale: The glossary source simply states "Poop," so the replacement uses this direct, everyday term to convey the meaning of "stools." Word frequency increases from Zipf 3.05 to 3.66, making the term more common and easier to process. Patients can immediately recognize the reference to bowel movements without encountering clinical jargon.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `occult blood` -> `hidden blood`**

- status: `attributed`
- log p full -0.0018, empty -0.0064
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+0.826` [wiktionary] occult: If something is occult it is hidden or secret—or it is about hidden or secret things.
    - `+0.781` [readme] occult: Obscure and mysterious, not easily understood.
    - `+0.539` [readme] colonoscopy: A procedure to check for colon cancer by examining the inside of the large intestine.
    - `+0.360` [readme] Occult: Secret knowledge or practices that are mysterious or not easily understood.
    - `+0.315` [readme] colonoscopy: A colonoscopy is a test that checks the inside of your large intestine for signs of cancer.

- rationale: "Occult blood" refers to blood that is not visible to the naked eye, so "hidden blood" conveys this same idea using everyday language. Phrase frequency rises from Zipf 3.28 to 4.43, and age of acquisition drops from 12.65 to 4.89. Readers can grasp that the bleeding is internal or microscopic without needing to interpret a clinical term.
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

**output:** The knee was washed out with a lot of fluid and then dried with suction again.

| metric | value |
|---|---:|
| bertscore_f1 | 0.638 |
| coleman_liau | 4.82 |
| coleman_liau_drop | 6.57 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 4.66 |
| fkgl_drop | 3.71 |
| fre | 90.1 |
| fre_gain | 37.3 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 16.0 |
| nli_completeness | 0.968 |
| nli_faithfulness | 0.987 |
| number_unit_preservation | 0.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 61.54 |
| smog | 3.13 |
| smog_drop | 8.08 |

### Stage 4 - arm `termonly`

**output:** The knee was washed with lots of fluid and dried with suction again.

| metric | value |
|---|---:|
| bertscore_f1 | 0.628 |
| coleman_liau | 6.46 |
| coleman_liau_drop | 4.94 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 4.00 |
| fkgl_drop | 4.37 |
| fre | 89.5 |
| fre_gain | 36.6 |
| human_edit_recall | 1.000 |
| length_ratio | 0.81 |
| n_words | 13.0 |
| nli_completeness | 0.982 |
| nli_faithfulness | 0.991 |
| number_unit_preservation | 0.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 59.15 |
| smog | 3.13 |
| smog_drop | 8.08 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `copiously irrigated` -> `washed with lots of fluid` | replace | - | - | - | - | - | - | - |
| `suction dried` -> `dried with suction` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** The knee was washed with lots of fluid and dried with suction again.

| metric | value |
|---|---:|
| bertscore_f1 | 0.628 |
| coleman_liau | 6.46 |
| coleman_liau_drop | 4.94 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 4.00 |
| fkgl_drop | 4.37 |
| fre | 89.5 |
| fre_gain | 36.6 |
| human_edit_recall | 1.000 |
| length_ratio | 0.81 |
| n_words | 13.0 |
| nli_completeness | 0.982 |
| nli_faithfulness | 0.991 |
| number_unit_preservation | 0.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 59.15 |
| smog | 3.13 |
| smog_drop | 8.08 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `copiously irrigated` -> `washed with lots of fluid` | replace | attributed | -0.089 | -0.108 | 0.237 | 0.735 | 0.054 | - |
| `suction dried` -> `dried with suction` | replace | attributed | -0.554 | -1.140 | 0.886 | 0.909 | 0.186 | - |

**edit `copiously irrigated` -> `washed with lots of fluid`**

- status: `attributed`
- log p full -1.7775, empty -1.6884
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.066` [dictionary] Copiously (adv.): In a copious manner.
    - `+0.012` [readme] suction: Suction is when a machine pulls in gas, liquid, or mucus.
    - `+0.003` [wiktionary] suction: A suction is a device that removes saliva from a patient's mouth during dental operations.

- rationale: "Copiously irrigated" means thoroughly flushed with liquid, so "washed with lots of fluid" conveys the same idea in everyday language. Word frequency rises from Zipf 1.98 to 3.81, and the syllable count drops from 7 to 6. This helps patients visualize the cleaning process without needing to interpret technical jargon.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `suction dried` -> `dried with suction`**

- status: `attributed`
- log p full -0.9813, empty -0.4275
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.220` [wiktionary] irrigated: To supply farms with water to grow crops.
    - `+0.034` [wiktionary] suction: Suction is a force which pushes matter from one space into another due to the pressure difference in 
    - `+0.012` [dictionary] Copiously (adv.): In a copious manner.
    - `-0.019` [wiktionary] suction: A suction is a device that removes saliva from a patient's mouth during dental operations.
    - `-0.181` [wiktionary] dried: If something is dry, it has no water or liquid on it.

- rationale: "Suction dried" means removing moisture by applying suction, and "dried with suction" expresses the same process in a more natural word order. Word frequency remains at Zipf 3.28, age of acquisition stays at 9.42, and syllable count increases from 3 to 4. Readers can grasp how the drying is performed without stumbling over an unusual compound adjective.
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

**output:** She does not have pain when urinating, blood in her urine, frequent urination, or trouble starting to urinate.

| metric | value |
|---|---:|
| bertscore_f1 | 0.627 |
| coleman_liau | 11.23 |
| coleman_liau_drop | -0.98 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 10.44 |
| fkgl_drop | 0.50 |
| fre | 52.3 |
| fre_gain | 10.7 |
| human_edit_recall | 1.000 |
| length_ratio | 0.90 |
| n_words | 18.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.993 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.600 |
| sari | 25.38 |
| smog | 13.02 |
| smog_drop | 0.00 |

### Stage 4 - arm `termonly`

**output:** She is not having painful urination, any blood in the urine, needing to go often, or trouble starting.

| metric | value |
|---|---:|
| bertscore_f1 | 0.771 |
| coleman_liau | 8.66 |
| coleman_liau_drop | 1.60 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 9.79 |
| fkgl_drop | 1.16 |
| fre | 57.0 |
| fre_gain | 15.4 |
| human_edit_recall | 1.000 |
| length_ratio | 0.90 |
| n_words | 18.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.981 |
| nli_faithfulness | 0.985 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 63.87 |
| smog | 8.84 |
| smog_drop | 4.18 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `frequency` -> `needing to go often` | replace | - | - | - | - | - | - | - |
| `hesitancy` -> `trouble starting` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** She is not having painful urination, any blood in the urine, needing to pee often, or trouble starting to pee.

| metric | value |
|---|---:|
| bertscore_f1 | 0.818 |
| coleman_liau | 7.95 |
| coleman_liau_drop | 2.31 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 9.91 |
| fkgl_drop | 1.03 |
| fre | 59.6 |
| fre_gain | 18.1 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 20.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.985 |
| nli_faithfulness | 0.987 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 66.66 |
| smog | 8.84 |
| smog_drop | 4.18 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `frequency` -> `needing to pee often` | replace | attributed | 1.342 | 1.779 | - | 0.657 | 0.244 | - |
| `hesitancy` -> `trouble starting to pee` | replace | attributed | 0.306 | 0.704 | - | 0.915 | 0.402 | - |

**edit `frequency` -> `needing to pee often`**

- status: `attributed`
- log p full -0.8534, empty -2.1953
- masks scored: 34/34 (+3 top-k)
- ranked sources:
    - `+1.062` [readme] hesitancy: Having difficulty starting to pee or keeping the flow steady.
    - `+0.818` [readme] hesitancy: Having difficulty starting or maintaining a steady flow while peeing.

- rationale: "Frequency" refers to how often something happens, so "needing to pee often" expresses that idea in everyday language. Word frequency decreases from Zipf 4.36 to 3.68, while age of acquisition drops from 9.79 to 6.53. Readers can grasp the symptom of repeated urination without interpreting a technical term.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `hesitancy` -> `trouble starting to pee`**

- status: `attributed`
- log p full -0.4322, empty -0.7385
- masks scored: 34/34 (+3 top-k)
- ranked sources:
    - `+0.731` [readme] hesitancy: Having difficulty starting to pee or keeping the flow steady.
    - `+0.329` [readme] hesitancy: Having difficulty starting or maintaining a steady flow while peeing.
    - `-0.000` [readme] frequency: How often something happens.
    - `-0.070` [wiktionary] frequency: Something's frequency is how often it happens.

- rationale: "Hesitancy" refers to difficulty initiating urination, so "trouble starting to pee" conveys this specific symptom in everyday language. Phrase frequency rises from Zipf 2.35 to 3.87, and age of acquisition drops from 12.12 to 4.56. This phrasing helps patients clearly recognize the issue of delayed urine flow.
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

**output:** The patient has chest pain behind the breastbone. They sometimes have angina pain and describe it as a feeling of tightness.

| metric | value |
|---|---:|
| bertscore_f1 | 0.462 |
| coleman_liau | 9.55 |
| coleman_liau_drop | 6.36 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 5.36 |
| fkgl_drop | 9.44 |
| fre | 75.3 |
| fre_gain | 52.5 |
| human_edit_recall | 1.000 |
| length_ratio | 0.70 |
| n_words | 21.0 |
| nli_completeness | 0.277 |
| nli_faithfulness | 0.791 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.286 |
| sari | 40.06 |
| smog | 7.17 |
| smog_drop | 8.73 |

### Stage 4 - arm `termonly`

**output:** Heart: Chest pain behind the breastbone, occasional heart pain, and the patient describes it as a feeling of tightness.

| metric | value |
|---|---:|
| bertscore_f1 | 0.564 |
| coleman_liau | 12.25 |
| coleman_liau_drop | 3.66 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.333 |
| fkgl | 9.21 |
| fkgl_drop | 5.59 |
| fre | 62.9 |
| fre_gain | 40.1 |
| human_edit_recall | 1.000 |
| length_ratio | 0.63 |
| n_words | 19.0 |
| nli_completeness | 0.961 |
| nli_faithfulness | 0.915 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 60.23 |
| smog | 8.84 |
| smog_drop | 7.06 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `retrosternal area` -> `breastbone` | replace | - | - | - | - | - | - | - |
| `anginal pain` -> `heart pain` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Heart and blood vessels: Chest pain behind the breastbone, occasional heart pain, and the patient describes it as a feeling of tightness.

| metric | value |
|---|---:|
| bertscore_f1 | 0.691 |
| coleman_liau | 12.38 |
| coleman_liau_drop | 3.53 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.333 |
| fkgl | 10.15 |
| fkgl_drop | 4.65 |
| fre | 61.5 |
| fre_gain | 38.6 |
| human_edit_recall | 1.000 |
| length_ratio | 0.73 |
| n_words | 22.0 |
| nli_completeness | 0.967 |
| nli_faithfulness | 0.904 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 65.77 |
| smog | 8.84 |
| smog_drop | 7.06 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `retrosternal area` -> `breastbone` | replace | attributed | -0.002 | -0.212 | 0.167 | 0.389 | 0.104 | - |
| `anginal pain` -> `heart pain` | replace | attributed | 0.314 | 0.574 | 0.394 | 0.755 | 0.106 | - |

**edit `retrosternal area` -> `breastbone`**

- status: `attributed`
- log p full -0.0113, empty -0.0092
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.167` [nih] cardiovascular: Having to do with the heart and blood vessels.
    - `+0.063` [readme] Cardiovascular: Related to the blood vessels and heart.

- rationale: The retrosternal area refers to the space behind the breastbone, so using "breastbone" directly names the familiar anatomical landmark. Word frequency rises from Zipf 0.00 to 1.93, though age of acquisition increases from 6.58 to 10.75. Readers can locate the relevant chest region without needing to interpret Latin-based positional terms.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `anginal pain` -> `heart pain`**

- status: `attributed`
- log p full -0.6465, empty -0.9609
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.235` [readme] CARDIOVASCULAR: Having to do with the blood vessels and the heart.
    - `+0.129` [thesaurus] cardiovascular: having to do with the heart and blood vessels
    - `+0.107` [michigan] cardiovascular: Having to do with your heart and blood vessels.
    - `+0.044` [justplainclear] cardiovascular: About the heart and blood vessels

- rationale: "Anginal pain" refers to discomfort caused by reduced blood flow to the heart, so "heart pain" conveys this specific location and sensation in everyday language. Word frequency rises from Zipf 1.10 to 4.85, though age of acquisition increases from 4.26 to 5.17. Readers can immediately recognize the symptom's connection to the heart without needing medical terminology.
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

**output:** The doctors removed a large part of his synovium and synovial pouch.

| metric | value |
|---|---:|
| bertscore_f1 | 0.323 |
| coleman_liau | 8.80 |
| coleman_liau_drop | -3.04 |
| copy_jargon_rate | 0.800 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 5.81 |
| fkgl_drop | -1.02 |
| fre | 74.8 |
| fre_gain | -5.5 |
| human_edit_recall | 0.200 |
| length_ratio | 1.00 |
| n_words | 12.0 |
| nli_completeness | 0.993 |
| nli_faithfulness | 0.959 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 32.05 |
| smog | 8.84 |
| smog_drop | 0.00 |

### Stage 4 - arm `termonly`

**output:** We cut out much of his joint lining and joint pouch.

| metric | value |
|---|---:|
| bertscore_f1 | 0.570 |
| coleman_liau | 3.13 |
| coleman_liau_drop | 2.64 |
| copy_jargon_rate | 0.200 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 1.57 |
| fkgl_drop | 3.22 |
| fre | 103.4 |
| fre_gain | 23.1 |
| human_edit_recall | 0.800 |
| length_ratio | 0.92 |
| n_words | 11.0 |
| nli_completeness | 0.944 |
| nli_faithfulness | 0.988 |
| replacement_f1 | 0.889 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.200 |
| sari | 40.61 |
| smog | 3.13 |
| smog_drop | 5.71 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `synovium` -> `joint lining` | replace | - | - | - | - | - | - | - |
| `synovial pouch` -> `joint pouch` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** We cut out much of his joint lining and joint pocket.

| metric | value |
|---|---:|
| bertscore_f1 | 0.534 |
| coleman_liau | 3.65 |
| coleman_liau_drop | 2.11 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.200 |
| fkgl | 2.65 |
| fkgl_drop | 2.15 |
| fre | 95.7 |
| fre_gain | 15.4 |
| human_edit_recall | 1.000 |
| length_ratio | 0.92 |
| n_words | 11.0 |
| nli_completeness | 0.858 |
| nli_faithfulness | 0.916 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.167 |
| sari | 41.09 |
| smog | 3.13 |
| smog_drop | 5.71 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `synovium` -> `joint lining` | replace | attributed | 0.000 | 0.005 | 0.177 | 0.617 | 0.140 | - |
| `synovial pouch` -> `joint pocket` | replace | attributed | 2.805 | 4.007 | 0.853 | 0.842 | 0.974 | - |

**edit `synovium` -> `joint lining`**

- status: `attributed`
- log p full -0.0187, empty -0.0188
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.195` [wiktionary] pouch: A pouch is a pocket-like part of an animal's body, used to carry young or store food.
    - `+0.055` [readme] SYNOVIAL: Synovial means having to do with the soft tissue that lines joints.
    - `-0.062` [readme] SYNOVIUM: The slimy layer that covers your joints.
    - `-0.140` [readme] Synovial: Relating to the soft tissue that lines joints.

- rationale: The synovium is the thin tissue that lines the inside of a joint, so "joint lining" conveys that anatomical role in everyday language. Word frequency rises from Zipf 1.46 to 3.82, while the syllable count remains at three. This phrasing helps patients recognize which part of the joint is involved without needing specialized medical vocabulary.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `synovial pouch` -> `joint pocket`**

- status: `attributed`
- log p full -0.3389, empty -3.1436
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+2.031` [wiktionary] pouch: A pouch is a small bag or pocket used for carrying things.
    - `+1.058` [wiktionary] pouch: A pouch is a pocket-like part of an animal's body, used to carry young or store food.
    - `+0.455` [readme] SYNOVIUM: The slimy layer that covers your joints.
    - `+0.125` [readme] SYNOVIAL: Synovial means having to do with the soft tissue that lines joints.

- rationale: The glossary defines a pouch as a small bag or pocket, so "joint pocket" preserves the idea of a contained space in everyday terms. Phrase frequency rises from Zipf 2.32 to 4.28, and age of acquisition drops from 16.00 to 9.05. Readers can grasp the anatomical concept without needing specialized vocabulary.
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

**output:** Doctors must consider whether an inflammatory process, such as an infection or ischemia, is the cause.

| metric | value |
|---|---:|
| bertscore_f1 | 0.559 |
| coleman_liau | 12.80 |
| coleman_liau_drop | 1.40 |
| copy_jargon_rate | 1.000 |
| critical_error | 0.000 |
| diagnostic_identity_preservation | 1.000 |
| fkgl | 12.78 |
| fkgl_drop | 0.60 |
| fre | 32.0 |
| fre_gain | 13.2 |
| human_edit_recall | 0.000 |
| length_ratio | 1.23 |
| n_words | 16.0 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.233 |
| replacement_f1 | 0.000 |
| rewrite_aggressiveness | 1.000 |
| sari | 34.50 |
| smog | 14.55 |
| smog_drop | 0.00 |

### Stage 4 - arm `termonly`

**output:** A problem like infection or poor blood flow must be considered.

| metric | value |
|---|---:|
| bertscore_f1 | 0.779 |
| coleman_liau | 8.93 |
| coleman_liau_drop | 5.27 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| diagnostic_identity_preservation | 1.000 |
| fkgl | 5.86 |
| fkgl_drop | 7.51 |
| fre | 72.6 |
| fre_gain | 53.8 |
| human_edit_recall | 1.000 |
| length_ratio | 0.85 |
| n_words | 11.0 |
| nli_completeness | 0.767 |
| nli_faithfulness | 0.983 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.250 |
| sari | 35.22 |
| smog | 11.21 |
| smog_drop | 3.35 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `inflammatory process` -> `problem` | replace | - | - | - | - | - | - | - |
| `ischemia` -> `poor blood flow` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** A body reaction like infection or low blood flow must be considered.

| metric | value |
|---|---:|
| bertscore_f1 | 0.762 |
| coleman_liau | 8.80 |
| coleman_liau_drop | 5.40 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| diagnostic_identity_preservation | 1.000 |
| fkgl | 7.77 |
| fkgl_drop | 5.60 |
| fre | 60.7 |
| fre_gain | 41.9 |
| human_edit_recall | 1.000 |
| length_ratio | 0.92 |
| n_words | 12.0 |
| nli_completeness | 0.937 |
| nli_faithfulness | 0.981 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.250 |
| sari | 34.26 |
| smog | 13.02 |
| smog_drop | 1.53 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `inflammatory process` -> `body reaction` | replace | attributed | 2.098 | 2.192 | 0.801 | 0.918 | 1.566 | - |
| `ischemia` -> `low blood flow` | replace | attributed | 0.443 | 0.718 | 0.808 | 0.676 | 0.075 | - |

**edit `inflammatory process` -> `body reaction`**

- status: `attributed`
- log p full -2.2891, empty -4.3867
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+1.873` [readme] inflammatory process: When your body gets inflamed, it's like it's telling you there's something wrong by show
    - `+0.307` [readme] ischemia: Not enough blood flow due to blocked or narrowed blood vessels.

- rationale: The glossary explains that inflammation is the body's way of signaling a problem through redness, warmth, and swelling, so "body reaction" captures this protective response in everyday terms. Phrase frequency rises from Zipf 3.71 to 4.65, and age of acquisition drops from 13.33 to 8.30, making the concept significantly more accessible. Readers can now grasp that their body is actively responding to an issue without needing to understand complex medical terminology.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `ischemia` -> `low blood flow`**

- status: `attributed`
- log p full -0.7549, empty -1.1977
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.341` [michigan] ischemia: When blood supply to an organ or a body part isn't enough, especially the heart.
    - `+0.267` [readme] ischemia: Not enough blood flow due to blocked or narrowed blood vessels.
    - `+0.222` [iowa] ISCHEMIA: decreased oxygen in a tissue (usually because of decreased blood flow)
    - `+0.073` [readme] inflammatory process: When your body gets inflamed, it's like it's telling you there's something wrong by show
    - `+0.015` [readme] Ischemia: Ischemia is when there's a lack of blood flow due to blocked blood vessels.

- rationale: Ischemia refers to a restriction in blood supply to tissues, so "low blood flow" conveys this concept in everyday language. Phrase frequency increases from Zipf 2.85 to 4.47, age of acquisition falls from 18.00 to 7.40, and syllable count drops from 4 to 3. Readers can grasp the cause of tissue distress without needing specialized medical vocabulary.
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

**output:** The doctor asked her to take more prednisone when she goes home.

| metric | value |
|---|---:|
| bertscore_f1 | 0.644 |
| coleman_liau | 6.87 |
| coleman_liau_drop | -0.48 |
| copy_jargon_rate | 1.000 |
| critical_error | 0.000 |
| drug_preservation | 1.000 |
| fkgl | 2.86 |
| fkgl_drop | 0.00 |
| fre | 96.0 |
| fre_gain | 0.0 |
| human_edit_recall | 0.000 |
| length_ratio | 1.00 |
| n_words | 12.0 |
| nli_completeness | 0.962 |
| nli_faithfulness | 0.567 |
| replacement_f1 | 0.000 |
| rewrite_aggressiveness | 1.000 |
| sari | 26.98 |
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
| `prednisone` -> `steroid medicine` | replace | attributed | -0.676 | -1.227 | - | 0.810 | 0.368 | - |

**edit `prednisone` -> `steroid medicine`**

- status: `attributed`
- log p full -1.1875, empty -0.5117
- masks scored: 10/10 (+2 top-k)
- ranked sources:
    - `+0.129` [nih] prednisone: A drug used to reduce inflammation and lower the body’s immune response.  It is used with other dr
    - `-0.239` [readme] prednisone: A medication that helps lower the body's immune system reactions.
    - `-0.506` [readme] Prednisone: A medication that lowers the body's immune response and inflammation.

- rationale: Prednisone is a specific type of steroid medicine, so the replacement uses the broader category name to convey its general class in plain language. Phrase frequency increases from Zipf 2.56 to 3.31, while age of acquisition falls from 17.17 to 13.67. Patients can recognize the medication type without needing to recall the specific drug name.
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

**output:** She may need other medicines for nerve pain as needed.

| metric | value |
|---|---:|
| bertscore_f1 | 0.920 |
| coleman_liau | 6.76 |
| coleman_liau_drop | 5.73 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 4.83 |
| fkgl_drop | 5.38 |
| fre | 78.2 |
| fre_gain | 40.3 |
| human_edit_recall | 1.000 |
| length_ratio | 1.11 |
| n_words | 10.0 |
| nli_completeness | 0.861 |
| nli_faithfulness | 0.960 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 52.10 |
| smog | 8.84 |
| smog_drop | 2.37 |
| uncertainty_preservation | 1.000 |

### Stage 4 - arm `termonly`

**output:** She may need other nerve pain medications as needed.

| metric | value |
|---|---:|
| bertscore_f1 | 1.000 |
| coleman_liau | 8.62 |
| coleman_liau_drop | 3.87 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 6.28 |
| fkgl_drop | 3.93 |
| fre | 66.1 |
| fre_gain | 28.2 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 9.0 |
| nli_completeness | 0.880 |
| nli_faithfulness | 0.953 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 100.00 |
| smog | 8.84 |
| smog_drop | 2.37 |
| uncertainty_preservation | 1.000 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `neuropathic` -> `nerve pain` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** She may need other nerve pain medications as needed.

| metric | value |
|---|---:|
| bertscore_f1 | 1.000 |
| coleman_liau | 8.62 |
| coleman_liau_drop | 3.87 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 6.28 |
| fkgl_drop | 3.93 |
| fre | 66.1 |
| fre_gain | 28.2 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 9.0 |
| nli_completeness | 0.880 |
| nli_faithfulness | 0.953 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 100.00 |
| smog | 8.84 |
| smog_drop | 2.37 |
| uncertainty_preservation | 1.000 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `neuropathic` -> `nerve pain` | replace | attributed | 0.185 | 1.279 | - | 0.800 | 0.129 | - |

**edit `neuropathic` -> `nerve pain`**

- status: `attributed`
- log p full -0.0818, empty -0.2671
- masks scored: 6/6 (+1 top-k)
- ranked sources:
    - `+0.664` [readme] neuropathic: Nerve pain.
    - `+0.535` [readme] Neuropathic: Neuropathic means nerve pain.

- rationale: "Neuropathic" refers to pain caused by nerve damage, so "nerve pain" conveys this specific type of discomfort in everyday language. Phrase frequency rises from Zipf 2.35 to 4.13, age of acquisition drops from 15.40 to 9.67, and syllable count decreases from 4 to 2. Readers can immediately recognize the nature of their pain without needing to interpret complex medical terminology.
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

**output:** The patient was given a dose of antibiotics to prevent infection.

| metric | value |
|---|---:|
| bertscore_f1 | 0.493 |
| coleman_liau | 9.98 |
| coleman_liau_drop | 1.48 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 10.15 |
| fkgl_drop | 2.27 |
| fre | 41.9 |
| fre_gain | 23.4 |
| human_edit_recall | 1.000 |
| length_ratio | 1.57 |
| n_words | 11.0 |
| nli_completeness | 0.984 |
| nli_faithfulness | 0.930 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 41.87 |
| smog | 11.21 |
| smog_drop | 0.00 |

### Stage 4 - arm `termonly`

**output:** A dose of germ-fighting medicine was given to prevent illness.

| metric | value |
|---|---:|
| bertscore_f1 | 0.600 |
| coleman_liau | 10.82 |
| coleman_liau_drop | 0.64 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 7.19 |
| fkgl_drop | 5.24 |
| fre | 61.3 |
| fre_gain | 42.9 |
| human_edit_recall | 1.000 |
| length_ratio | 1.57 |
| n_words | 11.0 |
| nli_completeness | 0.227 |
| nli_faithfulness | 0.973 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 28.96 |
| smog | 8.84 |
| smog_drop | 2.37 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `antibiotics` -> `germ-fighting medicine` | replace | - | - | - | - | - | - | - |
| `prophylactic` -> `to prevent illness` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** A preventive dose of germ-killing medicine was given.

| metric | value |
|---|---:|
| bertscore_f1 | 0.764 |
| coleman_liau | 12.40 |
| coleman_liau_drop | -0.94 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 6.71 |
| fkgl_drop | 5.72 |
| fre | 61.2 |
| fre_gain | 42.8 |
| human_edit_recall | 1.000 |
| length_ratio | 1.29 |
| n_words | 9.0 |
| nli_completeness | 0.348 |
| nli_faithfulness | 0.980 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 28.96 |
| smog | 11.21 |
| smog_drop | 0.00 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `prophylactic` -> `preventive` | replace | attributed | 1.570 | 2.261 | 0.917 | 0.977 | 1.636 | - |
| `antibiotics` -> `germ-killing medicine` | replace | attributed | 1.475 | 1.712 | 0.866 | 0.903 | 0.927 | - |

**edit `prophylactic` -> `preventive`**

- status: `attributed`
- log p full -0.5859, empty -2.1562
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+2.003` [readme] PROPHYLACTIC: Preventive measures or treatments to avoid getting sick.
    - `+0.367` [readme] prophylactic: A prophylactic is like a protective shield that helps prevent diseases.
    - `+0.230` [nih] prophylactic: In medicine, something that prevents or protects.
    - `+0.176` [readme] Antibiotics: Medicine that kills bacteria.
    - `+0.117` [wiktionary] prophylactic: Something that is prophylactic serves to prevent or protect against a disease or pregnancy.

- rationale: The glossary defines prophylactic as preventive measures or treatments to avoid getting sick, so "preventive" conveys this protective intent in everyday language. Word frequency rises from Zipf 2.59 to 3.50, and age of acquisition drops from 15.20 to 10.50. Readers can grasp that the treatment aims to stop illness before it starts.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `antibiotics` -> `germ-killing medicine`**

- status: `attributed`
- log p full -1.3577, empty -2.8328
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+1.079` [readme] Antibiotics: Medicine that kills bacteria.
    - `+0.153` [wiktionary] antibiotics: An antibiotic is a drug that stops the growth of or destroys bacteria and other such microorganis
    - `+0.088` [wiktionary] prophylactic: A prophylactic is a medicine which preserves or defends against disease.

- rationale: The glossary defines antibiotics as medicine that kills bacteria, so "germ-killing medicine" conveys this function in everyday terms. Word frequency decreases from Zipf 3.74 to 3.18, while age of acquisition drops from 9.55 to 4.89. Readers can grasp that the treatment targets harmful germs without needing the clinical term.
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

**output:** The patient has long-term low potassium levels caused by long-term diarrhea.

| metric | value |
|---|---:|
| bertscore_f1 | 0.670 |
| coleman_liau | 14.73 |
| coleman_liau_drop | 7.07 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.143 |
| fkgl | 11.23 |
| fkgl_drop | 5.02 |
| fre | 34.2 |
| fre_gain | 44.9 |
| human_edit_recall | 1.000 |
| length_ratio | 1.44 |
| n_words | 13.0 |
| nli_completeness | 0.935 |
| nli_faithfulness | 0.977 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 49.19 |
| smog | 11.21 |
| smog_drop | 0.00 |
| temporality_preservation | 0.000 |

### Stage 4 - arm `termonly`

**output:** Long-term low potassium caused by long-term loose stools.

| metric | value |
|---|---:|
| bertscore_f1 | 0.634 |
| coleman_liau | 14.58 |
| coleman_liau_drop | 7.22 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.250 |
| fkgl | 6.71 |
| fkgl_drop | 9.54 |
| fre | 61.2 |
| fre_gain | 72.0 |
| human_edit_recall | 1.000 |
| length_ratio | 1.11 |
| n_words | 10.0 |
| nli_completeness | 0.856 |
| nli_faithfulness | 0.973 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 42.52 |
| smog | 8.84 |
| smog_drop | 2.37 |
| temporality_preservation | 0.000 |

annotation backend `novita`, 0 edits kept


### Stage 4 - arm `grounded`

**output:** Long-term low blood potassium caused by long-term runny bowel movements.

| metric | value |
|---|---:|
| bertscore_f1 | 0.623 |
| coleman_liau | 16.04 |
| coleman_liau_drop | 5.76 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.250 |
| fkgl | 9.55 |
| fkgl_drop | 6.70 |
| fre | 44.4 |
| fre_gain | 55.2 |
| human_edit_recall | 1.000 |
| length_ratio | 1.33 |
| n_words | 12.0 |
| nli_completeness | 0.922 |
| nli_faithfulness | 0.977 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 37.94 |
| smog | 8.84 |
| smog_drop | 2.37 |
| temporality_preservation | 0.000 |

annotation backend `novita`, 0 edits kept


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

**output:** The patient's liver and spleen are not enlarged, and there is no tenderness.

| metric | value |
|---|---:|
| bertscore_f1 | 0.392 |
| coleman_liau | 9.14 |
| coleman_liau_drop | 14.06 |
| copy_jargon_rate | 0.500 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 5.82 |
| fkgl_drop | 0.80 |
| fre | 76.5 |
| fre_gain | 21.8 |
| human_edit_recall | 0.500 |
| length_ratio | 1.56 |
| n_words | 14.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.982 |
| nli_faithfulness | 0.927 |
| replacement_f1 | 0.667 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 36.27 |
| smog | 8.84 |
| smog_drop | 0.00 |

### Stage 4 - arm `termonly`

**output:** The liver and spleen are not enlarged, and there is no pain when touched.

| metric | value |
|---|---:|
| bertscore_f1 | 0.540 |
| coleman_liau | 6.11 |
| coleman_liau_drop | 17.09 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 3.36 |
| fkgl_drop | 3.26 |
| fre | 95.9 |
| fre_gain | 41.2 |
| human_edit_recall | 1.000 |
| length_ratio | 1.56 |
| n_words | 14.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.930 |
| nli_faithfulness | 0.123 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 41.53 |
| smog | 3.13 |
| smog_drop | 5.71 |

annotation backend `novita`, 0 edits kept


### Stage 4 - arm `grounded`

**output:** No enlarged liver or spleen, and no pain when touched.

| metric | value |
|---|---:|
| bertscore_f1 | 0.776 |
| coleman_liau | 6.18 |
| coleman_liau_drop | 17.02 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 2.47 |
| fkgl_drop | 4.15 |
| fre | 95.2 |
| fre_gain | 40.4 |
| human_edit_recall | 1.000 |
| length_ratio | 1.11 |
| n_words | 10.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.932 |
| nli_faithfulness | 0.078 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 58.88 |
| smog | 3.13 |
| smog_drop | 5.71 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `hepatosplenomegaly` -> `enlarged liver or spleen` | replace | attributed | 0.282 | 0.599 | - | 0.703 | 0.035 | - |
| `tenderness` -> `pain when touched` | replace | attributed | 0.613 | 1.132 | - | 0.846 | 0.000 | - |

**edit `hepatosplenomegaly` -> `enlarged liver or spleen`**

- status: `attributed`
- log p full -0.5047, empty -0.7864
- masks scored: 18/18 (+4 top-k)
- ranked sources:
    - `+0.121` [readme] Tenderness: Tenderness is when an area hurts or is sensitive to touch.
    - `+0.085` [readme] tenderness: Tenderness is when an area hurts when you touch it.

- rationale: "Hepatosplenomegaly" refers to the enlargement of both the liver and spleen, so the replacement "enlarged liver or spleen" conveys this condition using familiar anatomical terms. Word frequency increases from Zipf 1.12 to 2.99, indicating the new phrase is significantly more common, while the syllable count rises from 2 to 6. This change allows patients to immediately recognize which organs are affected without needing to decode complex medical terminology.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `tenderness` -> `pain when touched`**

- status: `attributed`
- log p full -0.5150, empty -1.1279
- masks scored: 18/18 (+4 top-k)
- ranked sources:
    - `+0.576` [wiktionary] tenderness: Tenderness is the pain or discomfort when an affected area is touched.
    - `+0.576` [readme] tenderness: Tenderness is when an area hurts when you touch it.
    - `-0.476` [readme] Tenderness: Tenderness is when an area hurts or is sensitive to touch.

- rationale: "Tenderness" refers to discomfort elicited by pressure, which "pain when touched" conveys using everyday language. Phrase frequency rises from Zipf 3.24 to 4.22, and age of acquisition drops from 8.79 to 4.26. This phrasing helps patients recognize that the area hurts specifically when it is pressed.
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

**output:** He did not have pain in the front left side of his chest when he exercised.

| metric | value |
|---|---:|
| bertscore_f1 | 0.756 |
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
| nli_completeness | 0.971 |
| nli_faithfulness | 0.987 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 25.89 |
| smog | 8.84 |
| smog_drop | 4.18 |

### Stage 4 - arm `termonly`

**output:** He did not feel his left front chest pain with exercise.

| metric | value |
|---|---:|
| bertscore_f1 | 0.955 |
| coleman_liau | 5.24 |
| coleman_liau_drop | 4.75 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 2.65 |
| fkgl_drop | 6.44 |
| fre | 95.7 |
| fre_gain | 46.1 |
| human_edit_recall | 1.000 |
| laterality_preservation | 0.500 |
| length_ratio | 1.00 |
| n_words | 11.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.974 |
| nli_faithfulness | 0.975 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 62.40 |
| smog | 8.84 |
| smog_drop | 4.18 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `experience` -> `feel` | replace | - | - | - | - | - | - | - |
| `anterior` -> `front` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** He did not feel his left front chest pain with exercise.

| metric | value |
|---|---:|
| bertscore_f1 | 0.955 |
| coleman_liau | 5.24 |
| coleman_liau_drop | 4.75 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 2.65 |
| fkgl_drop | 6.44 |
| fre | 95.7 |
| fre_gain | 46.1 |
| human_edit_recall | 1.000 |
| laterality_preservation | 0.500 |
| length_ratio | 1.00 |
| n_words | 11.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.974 |
| nli_faithfulness | 0.975 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 62.40 |
| smog | 8.84 |
| smog_drop | 4.18 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `experience` -> `feel` | replace | attributed | 0.047 | 0.151 | 0.611 | 0.750 | 0.155 | - |
| `anterior` -> `front` | replace | attributed | 0.037 | 1.835 | 0.576 | 0.667 | 0.021 | - |

**edit `experience` -> `feel`**

- status: `attributed`
- log p full -0.3496, empty -0.3965
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.462` [thesaurus] experience: feel, have, go through
    - `+0.307` [readme] Anterior: The front part of the body or an organ.
    - `+0.250` [readme] anterior: Having to do with the front part of the body or an organ.
    - `+0.187` [nih] anterior: In human anatomy, has to do with the front of a structure, or a structure found toward the front of 
    - `-0.131` [michigan] anterior: The front of the body.

- rationale: "Experience" refers to undergoing or sensing something, and "feel" conveys that same idea in simpler, everyday language. Word frequency rises from Zipf 5.27 to 5.67, age of acquisition drops from 8.95 to 5.11, and syllable count falls from 4 to 1. Readers can grasp the sensation being described without stumbling over a more abstract term.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `anterior` -> `front`**

- status: `attributed`
- log p full -0.0073, empty -0.0447
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.262` [wiktionary] anterior: Anterior is a word used in biology to refer to the front of an animal.
    - `+0.242` [thesaurus] experience: feel, have, go through
    - `+0.182` [readme] Anterior: The front part of the body or an organ.
    - `+0.099` [wiktionary] experience: Experience is the amount of time you have been doing something (especially, a job).

- rationale: "Anterior" refers to the front part of the body, so "front" conveys this spatial direction in everyday language. Phrase frequency rises from Zipf 3.51 to 5.28, age of acquisition drops from 14.12 to 5.19, and syllable count decreases from 4 to 1. Readers can immediately identify the body area involved without needing anatomical terminology.
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

**output:** Also, it would be used to control the atrial fibrillation.

| metric | value |
|---|---:|
| bertscore_f1 | 0.599 |
| coleman_liau | 8.50 |
| coleman_liau_drop | 0.77 |
| copy_jargon_rate | 1.000 |
| critical_error | 0.000 |
| fkgl | 7.19 |
| fkgl_drop | 0.40 |
| fre | 61.3 |
| fre_gain | 4.6 |
| human_edit_recall | 0.000 |
| length_ratio | 1.00 |
| n_words | 10.0 |
| nli_completeness | 0.990 |
| nli_faithfulness | 0.992 |
| replacement_f1 | 0.000 |
| rewrite_aggressiveness | 1.000 |
| sari | 12.08 |
| smog | 8.84 |
| smog_drop | 0.00 |

### Stage 4 - arm `termonly`

**output:** Also, would use it to control the irregular heartbeat.

| metric | value |
|---|---:|
| bertscore_f1 | 0.893 |
| coleman_liau | 9.27 |
| coleman_liau_drop | 0.00 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 7.59 |
| fkgl_drop | 0.00 |
| fre | 56.7 |
| fre_gain | 0.0 |
| human_edit_recall | 1.000 |
| length_ratio | 0.90 |
| n_words | 9.0 |
| nli_completeness | 0.703 |
| nli_faithfulness | 0.964 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 80.00 |
| smog | 8.84 |
| smog_drop | 0.00 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `atrial fibrillation` -> `irregular heartbeat` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Also, would use it to control the irregular heartbeat.

| metric | value |
|---|---:|
| bertscore_f1 | 0.893 |
| coleman_liau | 9.27 |
| coleman_liau_drop | 0.00 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 7.59 |
| fkgl_drop | 0.00 |
| fre | 56.7 |
| fre_gain | 0.0 |
| human_edit_recall | 1.000 |
| length_ratio | 0.90 |
| n_words | 9.0 |
| nli_completeness | 0.703 |
| nli_faithfulness | 0.964 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 80.00 |
| smog | 8.84 |
| smog_drop | 0.00 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `atrial fibrillation` -> `irregular heartbeat` | replace | attributed | 0.029 | 0.127 | - | 0.683 | 0.480 | - |

**edit `atrial fibrillation` -> `irregular heartbeat`**

- status: `attributed`
- log p full -0.2476, empty -0.2769
- masks scored: 10/10 (+2 top-k)
- ranked sources:
    - `+0.480` [readme] Atrial fibrillation: Atrial fibrillation is when your heart beats irregularly and can make you tired or more l
    - `-0.277` [readme] atrial fibrillation: Atrial fibrillation is when your heart beats in a weird way that can make you tired and i

- rationale: Atrial fibrillation refers to an irregular and often rapid heart rhythm, which "irregular heartbeat" conveys in everyday language. Phrase frequency increases from Zipf 2.58 to 3.38, and age of acquisition decreases from 14.58 to 9.16. Readers can grasp the nature of the heart rhythm issue without needing specialized medical terminology.
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

**output:** The patient seems to give a clear and accurate account of their medical history.

| metric | value |
|---|---:|
| bertscore_f1 | 0.425 |
| coleman_liau | 9.43 |
| coleman_liau_drop | 1.52 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.250 |
| fkgl | 8.41 |
| fkgl_drop | 2.72 |
| fre | 59.7 |
| fre_gain | 30.2 |
| human_edit_recall | 1.000 |
| length_ratio | 1.40 |
| n_words | 14.0 |
| nli_completeness | 0.474 |
| nli_faithfulness | 0.004 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.250 |
| sari | 27.31 |
| smog | 13.02 |
| smog_drop | 0.00 |

### Stage 4 - arm `termonly`

**output:** The patient seems to give a clear history.

| metric | value |
|---|---:|
| bertscore_f1 | 0.394 |
| coleman_liau | 5.15 |
| coleman_liau_drop | 5.80 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.250 |
| fkgl | 3.76 |
| fkgl_drop | 7.38 |
| fre | 82.4 |
| fre_gain | 52.9 |
| human_edit_recall | 1.000 |
| length_ratio | 0.80 |
| n_words | 8.0 |
| nli_completeness | 0.780 |
| nli_faithfulness | 0.940 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.250 |
| sari | 26.94 |
| smog | 8.84 |
| smog_drop | 4.18 |

annotation backend `novita`, 0 edits kept


### Stage 4 - arm `grounded`

**output:** The patient seems to give a clear history.

| metric | value |
|---|---:|
| bertscore_f1 | 0.394 |
| coleman_liau | 5.15 |
| coleman_liau_drop | 5.80 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.250 |
| fkgl | 3.76 |
| fkgl_drop | 7.38 |
| fre | 82.4 |
| fre_gain | 52.9 |
| human_edit_recall | 1.000 |
| length_ratio | 0.80 |
| n_words | 8.0 |
| nli_completeness | 0.780 |
| nli_faithfulness | 0.940 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.250 |
| sari | 26.94 |
| smog | 8.84 |
| smog_drop | 4.18 |

annotation backend `novita`, 0 edits kept


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

**output:** The colonoscopy did not show any active Crohn's disease.

| metric | value |
|---|---:|
| bertscore_f1 | 0.431 |
| coleman_liau | 10.56 |
| coleman_liau_drop | -0.90 |
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
| nli_completeness | 0.993 |
| nli_faithfulness | 0.993 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 1.000 |
| sari | 18.58 |
| smog | 3.13 |
| smog_drop | 0.00 |

### Stage 4 - arm `termonly`

**output:** No signs of ongoing Crohn's disease were seen during the scope exam.

| metric | value |
|---|---:|
| bertscore_f1 | 0.565 |
| coleman_liau | 8.32 |
| coleman_liau_drop | 1.34 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.333 |
| fkgl | 5.81 |
| fkgl_drop | -2.16 |
| fre | 74.8 |
| fre_gain | -11.9 |
| human_edit_recall | 1.000 |
| length_ratio | 0.93 |
| n_words | 13.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.556 |
| nli_faithfulness | 0.985 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 19.15 |
| smog | 8.84 |
| smog_drop | -5.71 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `active` -> `ongoing` | replace | - | - | - | - | - | - | - |
| `colonoscopy` -> `scope exam` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** No current Crohn's disease was found during the colon exam.

| metric | value |
|---|---:|
| bertscore_f1 | 0.667 |
| coleman_liau | 9.08 |
| coleman_liau_drop | 0.58 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.333 |
| fkgl | 6.01 |
| fkgl_drop | -2.36 |
| fre | 69.8 |
| fre_gain | -16.9 |
| human_edit_recall | 1.000 |
| length_ratio | 0.79 |
| n_words | 11.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.411 |
| nli_faithfulness | 0.979 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 41.10 |
| smog | 3.13 |
| smog_drop | 0.00 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `colonoscopy` -> `colon exam` | replace | attributed | 2.510 | 2.910 | 0.743 | 0.892 | 1.423 | - |

**edit `colonoscopy` -> `colon exam`**

- status: `attributed`
- log p full -1.0527, empty -3.5625
- masks scored: 66/66 (+2 top-k)
- ranked sources:
    - `+1.625` [nih] colonoscopy: Examination of the inside of the colon using a colonoscope, inserted into the rectum. A colonosco
    - `+0.203` [readme] Active: Happening right now.
    - `+0.145` [readme] active: Currently happening.
    - `+0.131` [readme] Hashimoto 's disease: When the immune system attacks the thyroid gland in the neck.

- rationale: The glossary defines colonoscopy as an examination of the inside of the colon, so "colon exam" captures this core action in everyday terms. Phrase frequency rises from Zipf 2.74 to 3.51, and age of acquisition drops from 15.76 to 10.75. Readers can grasp that the procedure involves looking inside the colon without needing to know the specific medical instrument name.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

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

**output:** Soon after the first check-up, the patient started to complain of chest pain. The nurse saw that the patient was getting very tired and having trouble breathing.

| metric | value |
|---|---:|
| bertscore_f1 | 0.672 |
| coleman_liau | 10.15 |
| coleman_liau_drop | 5.82 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.250 |
| fkgl | 6.72 |
| fkgl_drop | 9.64 |
| fre | 70.9 |
| fre_gain | 45.0 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 28.0 |
| nli_completeness | 0.008 |
| nli_faithfulness | 0.993 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.600 |
| sari | 21.73 |
| smog | 3.13 |
| smog_drop | 12.77 |
| temporality_preservation | 1.000 |

### Stage 4 - arm `termonly`

**output:** Shortly after the patient's initial assessment, the patient apparently began to complain of chest pain and appeared to the nurse to have growing tiredness and trouble breathing.

| metric | value |
|---|---:|
| bertscore_f1 | 0.902 |
| coleman_liau | 14.90 |
| coleman_liau_drop | 1.07 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 15.04 |
| fkgl_drop | 1.31 |
| fre | 35.3 |
| fre_gain | 9.4 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 28.0 |
| nli_completeness | 0.995 |
| nli_faithfulness | 0.994 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 63.09 |
| smog | 14.55 |
| smog_drop | 1.35 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `mounting exhaustion` -> `growing tiredness` | replace | - | - | - | - | - | - | - |
| `respiratory distress` -> `trouble breathing` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Shortly after the patient's initial assessment, the patient apparently began to complain of chest pain and appeared to the nurse to have growing extreme tiredness and difficulty breathing.

| metric | value |
|---|---:|
| bertscore_f1 | 0.876 |
| coleman_liau | 15.87 |
| coleman_liau_drop | 0.10 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 16.40 |
| fkgl_drop | -0.05 |
| fre | 27.3 |
| fre_gain | 1.4 |
| human_edit_recall | 1.000 |
| length_ratio | 1.04 |
| n_words | 29.0 |
| nli_completeness | 0.995 |
| nli_faithfulness | 0.994 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 62.70 |
| smog | 15.90 |
| smog_drop | 0.00 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `mounting exhaustion` -> `growing extreme tiredness` | replace | attributed | 4.610 | 5.096 | - | 0.818 | 3.971 | - |
| `respiratory distress` -> `difficulty breathing` | replace | attributed | 7.498 | 8.868 | - | 0.827 | 7.324 | - |

**edit `mounting exhaustion` -> `growing extreme tiredness`**

- status: `attributed`
- log p full -0.9483, empty -5.5580
- masks scored: 34/34 (+4 top-k)
- ranked sources:
    - `+4.309` [wiktionary] exhaustion: Exhaustion is the state of extreme tiredness.
    - `+0.338` [readme] Respiratory Distress: Having difficulty breathing.
    - `-0.003` [wiktionary] exhaustion: Exhaustion is the point where something is completely depleted.
    - `-0.224` [readme] acute respiratory distress syndrome: A serious lung condition that causes low levels of oxygen in the blood, w

- rationale: "Mounting exhaustion" means a steadily increasing state of severe fatigue, which "growing extreme tiredness" expresses using more familiar words. Word frequency decreases from Zipf 3.34 to 2.91, and age of acquisition rises from 7.61 to 9.47. Readers can grasp the progressive nature of their fatigue without encountering less common vocabulary.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `respiratory distress` -> `difficulty breathing`**

- status: `attributed`
- log p full -0.2930, empty -7.7913
- masks scored: 34/34 (+4 top-k)
- ranked sources:
    - `+8.004` [readme] Respiratory Distress: Having difficulty breathing.
    - `+0.680` [wiktionary] exhaustion: Exhaustion is the state of extreme tiredness.
    - `+0.172` [wiktionary] exhaustion: Exhaustion is the point where something is completely depleted.
    - `+0.026` [wiktionary] mounting: If you mount something you get on to it.
    - `-0.295` [readme] acute respiratory distress syndrome: A serious lung condition that causes low levels of oxygen in the blood, w

- rationale: "Respiratory distress" refers to the struggle to breathe, which "difficulty breathing" expresses in everyday language. Phrase frequency rises from Zipf 3.57 to 4.00, and age of acquisition drops from 11.16 to 6.83. Readers can immediately grasp the physical sensation of breathlessness without medical jargon.
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

**output:** She has been sent to have a pacemaker put in.

| metric | value |
|---|---:|
| bertscore_f1 | 0.659 |
| coleman_liau | 1.54 |
| coleman_liau_drop | 10.14 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 2.47 |
| fkgl_drop | 5.71 |
| fre | 95.2 |
| fre_gain | 44.5 |
| human_edit_recall | 1.000 |
| length_ratio | 1.11 |
| n_words | 10.0 |
| nli_completeness | 0.993 |
| nli_faithfulness | 0.993 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 23.47 |
| smog | 8.84 |
| smog_drop | 2.37 |

### Stage 4 - arm `termonly`

**output:** She has been sent to get a pacemaker put in.

| metric | value |
|---|---:|
| bertscore_f1 | 0.628 |
| coleman_liau | 0.96 |
| coleman_liau_drop | 10.71 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 2.47 |
| fkgl_drop | 5.71 |
| fre | 95.2 |
| fre_gain | 44.5 |
| human_edit_recall | 1.000 |
| length_ratio | 1.11 |
| n_words | 10.0 |
| nli_completeness | 0.993 |
| nli_faithfulness | 0.994 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 23.47 |
| smog | 8.84 |
| smog_drop | 2.37 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `referred` -> `sent` | replace | - | - | - | - | - | - | - |
| `pacemaker implantation` -> `pacemaker put in` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** She was sent to have a pacemaker put in.

| metric | value |
|---|---:|
| bertscore_f1 | 0.602 |
| coleman_liau | 0.89 |
| coleman_liau_drop | 10.79 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 2.34 |
| fkgl_drop | 5.84 |
| fre | 94.3 |
| fre_gain | 43.6 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 9.0 |
| nli_completeness | 0.992 |
| nli_faithfulness | 0.993 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 13.49 |
| smog | 8.84 |
| smog_drop | 2.37 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `referred` -> `sent` | replace | attributed | 0.043 | 1.421 | 0.769 | 0.926 | 1.724 | - |
| `implantation` -> `put in` | replace | attributed | -0.490 | -2.133 | 0.695 | 0.768 | 0.213 | - |

**edit `referred` -> `sent`**

- status: `attributed`
- log p full -0.0142, empty -0.0574
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+1.945` [readme] REFERRED: Sending a patient to another person or place for medical care.
    - `+0.221` [readme] implantation: Surgery where a device is placed inside your body.
    - `+0.078` [readme] pacemaker: A pacemaker is a device that uses electrical signals to regulate the heartbeat.
    - `+0.059` [wiktionary] referred: If you refer to something, you talk or write about it, usually in passing.
    - `+0.035` [readme] pacemaker: A small device that helps regulate the heartbeat when placed in the chest.

- rationale: "Referred" means to direct or send someone to another place or person, so "sent" captures this action in simpler terms. Word frequency increases from Zipf 4.61 to 5.16, and the word becomes shorter from 2 syllables to 1. Patients can easily grasp that they are being directed to another provider without encountering formal medical jargon.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `implantation` -> `put in`**

- status: `attributed`
- log p full -0.5792, empty -0.0889
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.290` [nih] pacemaker: An electronic device that is implanted in the body to monitor heart rate and rhythm. It gives the h
    - `+0.077` [wiktionary] referred: If you refer to something, you talk or write about it, usually in passing.
    - `-0.275` [justplainclear] pacemaker: A medical device placed inside your chest or abdomen that helps control your heartbeat

- rationale: "Implantation" refers to the act of placing something inside the body, which "put in" expresses using everyday language. Phrase frequency rises from Zipf 3.01 to 5.65, age of acquisition drops from 11.95 to 3.72, and syllable count decreases from 4 to 2. This allows patients to grasp the procedure without needing specialized medical vocabulary.
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

**output:** There was a bruise at the catheter site.

| metric | value |
|---|---:|
| bertscore_f1 | 0.664 |
| coleman_liau | 3.70 |
| coleman_liau_drop | 0.72 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 2.28 |
| fkgl_drop | -2.95 |
| fre | 93.0 |
| fre_gain | -21.1 |
| human_edit_recall | 1.000 |
| length_ratio | 0.62 |
| n_words | 8.0 |
| nli_completeness | 0.422 |
| nli_faithfulness | 0.130 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 48.98 |
| smog | 8.84 |
| smog_drop | -5.71 |

### Stage 4 - arm `termonly`

**output:** There was some bruising at the tube site.

| metric | value |
|---|---:|
| bertscore_f1 | 0.661 |
| coleman_liau | 4.43 |
| coleman_liau_drop | 0.00 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 0.80 |
| fkgl_drop | -1.47 |
| fre | 103.5 |
| fre_gain | -10.6 |
| human_edit_recall | 1.000 |
| length_ratio | 0.62 |
| n_words | 8.0 |
| nli_completeness | 0.182 |
| nli_faithfulness | 0.443 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 58.33 |
| smog | 3.13 |
| smog_drop | 0.00 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `hematoma` -> `bruising` | replace | - | - | - | - | - | - | - |
| `cath site` -> `tube site` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** There was some bruising at the catheter spot.

| metric | value |
|---|---:|
| bertscore_f1 | 0.741 |
| coleman_liau | 7.33 |
| coleman_liau_drop | -2.90 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 3.76 |
| fkgl_drop | -4.43 |
| fre | 82.4 |
| fre_gain | -31.7 |
| human_edit_recall | 1.000 |
| length_ratio | 0.62 |
| n_words | 8.0 |
| nli_completeness | 0.439 |
| nli_faithfulness | 0.843 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 58.86 |
| smog | 8.84 |
| smog_drop | -5.71 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `hematoma` -> `bruising` | replace | attributed | 0.095 | 1.133 | 0.654 | 0.694 | 0.452 | - |
| `cath site` -> `catheter spot` | replace | attributed | 1.383 | 1.580 | 0.693 | 0.811 | 0.153 | - |

**edit `hematoma` -> `bruising`**

- status: `attributed`
- log p full -0.0485, empty -0.1436
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+1.260` [michigan] hematoma: A bruise or when your skin is black and blue after an injury.
    - `+0.808` [iowa] HEMATOMA: a bruise, a black and blue mark
    - `+0.162` [wiktionary] site: A site is a website.
    - `-0.135` [justplainclear] hematoma: A collection of blood under the skin or in the body that is typically caused by a broken blood vesse

- rationale: A hematoma is a collection of blood outside the blood vessels, so "bruising" conveys this concept in everyday language. Phrase frequency increases from Zipf 2.61 to 3.18, and age of acquisition falls from 14.78 to 9.44. Readers can grasp the nature of the injury without needing to know the clinical term.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `cath site` -> `catheter spot`**

- status: `attributed`
- log p full -1.4907, empty -2.8740
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.487` [wiktionary] site: A site is a location or a place.
    - `+0.334` [wiktionary] site: A site is a website.
    - `+0.287` [nih] hematoma: A pool of clotted or partially clotted blood in an organ, tissue, or body space, usually caused by a
    - `+0.180` [michigan] hematoma: A bruise or when your skin is black and blue after an injury.
    - `+0.017` [iowa] HEMATOMA: a bruise, a black and blue mark

- rationale: The glossary defines a site as a location or place, so "catheter spot" conveys the same idea using everyday language. Phrase frequency increases from Zipf 2.90 to 3.23, though age of acquisition rises from 8.63 to 14.37. Readers can identify the specific area where the catheter was inserted without needing medical jargon.
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

**output:** The dead tissue was removed from the belly.

| metric | value |
|---|---:|
| bertscore_f1 | 0.735 |
| coleman_liau | 5.88 |
| coleman_liau_drop | 1.46 |
| copy_jargon_rate | 0.333 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| diagnostic_identity_preservation | 1.000 |
| fkgl | 3.76 |
| fkgl_drop | 2.52 |
| fre | 82.4 |
| fre_gain | 16.3 |
| human_edit_recall | 0.667 |
| length_ratio | 0.89 |
| n_words | 8.0 |
| nli_completeness | 0.992 |
| nli_faithfulness | 0.994 |
| replacement_f1 | 0.800 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.750 |
| sari | 20.96 |
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
| `necrotic tissue` -> `dead tissue` | replace | attributed | -0.164 | -1.082 | 0.300 | 0.449 | 0.135 | - |

**edit `necrotic tissue` -> `dead tissue`**

- status: `attributed`
- log p full -0.2602, empty -0.0959
- masks scored: 66/66 (+2 top-k)
- ranked sources:
    - `+0.147` [wiktionary] tissue: Tissue is a group of cells that work together to do a job.
    - `+0.012` [readme] Necrotic: Necrotic means when tissue or skin dies.
    - `-0.043` [nih] tissue: A group or layer of cells that work together to perform a specific function.

- rationale: "Necrotic tissue" refers to body matter that has died due to injury or disease, so "dead tissue" conveys this state in everyday language. Phrase frequency rises from Zipf 2.54 to 4.26, age of acquisition drops from 15.07 to 5.17, and syllable count decreases from 4 to 3. Readers can immediately grasp that the affected area is no longer alive without needing medical terminology.
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

**output:** Pressure was applied, and the bleeding stopped.

| metric | value |
|---|---:|
| bertscore_f1 | 0.711 |
| coleman_liau | 12.29 |
| coleman_liau_drop | -4.24 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 4.00 |
| fkgl_drop | 2.71 |
| fre | 78.9 |
| fre_gain | 17.6 |
| human_edit_recall | 1.000 |
| length_ratio | 0.88 |
| n_words | 7.0 |
| nli_completeness | 0.263 |
| nli_faithfulness | 0.583 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.667 |
| sari | 30.32 |
| smog | 3.13 |
| smog_drop | 8.08 |

### Stage 4 - arm `termonly`

**output:** Pressure was held and the area stopped bleeding.

| metric | value |
|---|---:|
| bertscore_f1 | 1.000 |
| coleman_liau | 9.50 |
| coleman_liau_drop | -1.45 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 5.23 |
| fkgl_drop | 1.47 |
| fre | 71.8 |
| fre_gain | 10.6 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 8.0 |
| nli_completeness | 0.539 |
| nli_faithfulness | 0.518 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 100.00 |
| smog | 8.84 |
| smog_drop | 2.37 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `hemostatic` -> `stopped bleeding` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Pressure was held and the area stopped bleeding.

| metric | value |
|---|---:|
| bertscore_f1 | 1.000 |
| coleman_liau | 9.50 |
| coleman_liau_drop | -1.45 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 5.23 |
| fkgl_drop | 1.47 |
| fre | 71.8 |
| fre_gain | 10.6 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 8.0 |
| nli_completeness | 0.539 |
| nli_faithfulness | 0.518 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 100.00 |
| smog | 8.84 |
| smog_drop | 2.37 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `hemostatic` -> `stopped bleeding` | replace | attributed | -0.072 | -0.199 | - | 1.000 | 0.961 | - |

**edit `hemostatic` -> `stopped bleeding`**

- status: `attributed`
- log p full -0.4864, empty -0.4145
- masks scored: 6/6 (+1 top-k)
- ranked sources:
    - `+0.381` [readme] hemostatic: Stopping blood flow.
    - `-0.580` [readme] hemostatic: Hemostatic means stopping bleeding.

- rationale: "Hemostatic" refers to the process of stopping bleeding, so "stopped bleeding" conveys this action in everyday language. Word frequency increases from Zipf 1.73 to 4.01, while syllable count remains at 3. Patients can grasp that the bleeding has been controlled without needing to know the technical term.
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

**output:** The area was washed with some saline and cleared.

| metric | value |
|---|---:|
| bertscore_f1 | 0.778 |
| coleman_liau | 6.69 |
| coleman_liau_drop | 0.64 |
| copy_jargon_rate | 0.500 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 3.65 |
| fkgl_drop | 0.00 |
| fre | 84.9 |
| fre_gain | 0.0 |
| human_edit_recall | 0.500 |
| length_ratio | 0.82 |
| n_words | 9.0 |
| nli_completeness | 0.947 |
| nli_faithfulness | 0.991 |
| replacement_f1 | 0.667 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 59.43 |
| smog | 8.84 |
| smog_drop | 0.00 |

### Stage 4 - arm `termonly`

**output:** The area was washed with salt water and cleared.

| metric | value |
|---|---:|
| bertscore_f1 | 0.874 |
| coleman_liau | 6.04 |
| coleman_liau_drop | 1.29 |
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
| nli_completeness | 0.979 |
| nli_faithfulness | 0.977 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 69.70 |
| smog | 8.84 |
| smog_drop | 0.00 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `lavaged` -> `washed` | replace | - | - | - | - | - | - | - |
| `saline` -> `salt water` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** The area was washed with salt water and cleared.

| metric | value |
|---|---:|
| bertscore_f1 | 0.874 |
| coleman_liau | 6.04 |
| coleman_liau_drop | 1.29 |
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
| nli_completeness | 0.979 |
| nli_faithfulness | 0.977 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 69.70 |
| smog | 8.84 |
| smog_drop | 0.00 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `lavaged` -> `washed` | replace | attributed | -0.521 | -1.311 | - | 0.774 | 0.000 | - |
| `saline` -> `salt water` | replace | attributed | 0.277 | 1.126 | - | 0.880 | 0.514 | - |

**edit `lavaged` -> `washed`**

- status: `attributed`
- log p full -0.8125, empty -0.2910
- masks scored: 34/34 (+4 top-k)
- ranked sources:
    - `-0.004` [readme] saline: A solution made of saltwater that matches the body's fluid concentration and can be used to replace lo
    - `-1.000` [readme] lavaged: To clean out an organ or wound with fluid.

- rationale: "Lavaged" means to wash out a body cavity or wound, so "washed" conveys that same cleansing action in everyday language. Word frequency rises from Zipf 0.00 to 4.10, making the term significantly more common while syllable count remains at 1. Patients can grasp that the area was cleaned without needing to know the specialized medical verb.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `saline` -> `salt water`**

- status: `attributed`
- log p full -0.1665, empty -0.4438
- masks scored: 34/34 (+4 top-k)
- ranked sources:
    - `+0.881` [readme] Saline: Salt water solution used to replace body fluids.
    - `+0.367` [nih] saline: A solution of salt and water.
    - `+0.281` [readme] lavaged: To clean out an organ or wound with fluid.
    - `-0.033` [readme] saline: A solution made of saltwater that matches the body's fluid concentration and can be used to replace lo
    - `-0.345` [wiktionary] saline: If something is saline it is salty, especially water containing salt.

- rationale: "Saline" refers to a sterile solution of sodium chloride, which "salt water" conveys using everyday vocabulary. Word frequency rises from Zipf 3.33 to 4.55, and age of acquisition drops from 11.71 to 5.05. Readers immediately recognize the familiar liquid used in medical treatments.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

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

**output:** He came in because of pain and because he could not walk.

| metric | value |
|---|---:|
| bertscore_f1 | 0.417 |
| coleman_liau | 3.48 |
| coleman_liau_drop | 4.57 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 2.86 |
| fkgl_drop | 5.32 |
| fre | 96.0 |
| fre_gain | 45.3 |
| human_edit_recall | 1.000 |
| length_ratio | 1.33 |
| n_words | 12.0 |
| nli_completeness | 0.992 |
| nli_faithfulness | 0.994 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 23.06 |
| smog | 3.13 |
| smog_drop | 8.08 |

### Stage 4 - arm `termonly`

**output:** Pain and trouble walking brought him in.

| metric | value |
|---|---:|
| bertscore_f1 | 0.596 |
| coleman_liau | 7.31 |
| coleman_liau_drop | 0.74 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 2.31 |
| fkgl_drop | 5.87 |
| fre | 91.0 |
| fre_gain | 40.3 |
| human_edit_recall | 1.000 |
| length_ratio | 0.78 |
| n_words | 7.0 |
| nli_completeness | 0.988 |
| nli_faithfulness | 0.990 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 35.97 |
| smog | 3.13 |
| smog_drop | 8.08 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `inability to ambulate` -> `trouble walking` | replace | - | - | - | - | - | - | - |

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
| `inability to ambulate` -> `not being able to walk` | replace | attributed | 0.777 | 1.130 | 0.902 | 0.885 | 0.837 | - |

**edit `inability to ambulate` -> `not being able to walk`**

- status: `attributed`
- log p full -0.8224, empty -1.5995
- masks scored: 66/66 (+2 top-k)
- ranked sources:
    - `+0.982` [michigan] inability: Not able to.
    - `+0.145` [wiktionary] inability: An inability is something that you can not do.

- rationale: The Michigan glossary defines the original phrase as "not able to," so "not being able to walk" conveys that same restriction in everyday language. Phrase frequency rises from Zipf 1.40 to 4.87, and age of acquisition drops from 10.67 to 7.79. Readers can grasp the patient's mobility limitation without needing to interpret clinical jargon.
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

**output:** The patient has a hernia on the left side.

| metric | value |
|---|---:|
| bertscore_f1 | 0.382 |
| coleman_liau | 2.18 |
| coleman_liau_drop | -2.10 |
| copy_jargon_rate | 1.000 |
| critical_error | 0.000 |
| fkgl | 3.65 |
| fkgl_drop | -1.37 |
| fre | 84.9 |
| fre_gain | -8.1 |
| human_edit_recall | 0.000 |
| laterality_preservation | 1.000 |
| length_ratio | 0.75 |
| n_words | 9.0 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.970 |
| replacement_f1 | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 55.97 |
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
| `hernia` -> `bulge` | replace | attributed | 0.082 | 0.909 | - | 0.881 | 0.610 | - |

**edit `hernia` -> `bulge`**

- status: `attributed`
- log p full -0.0594, empty -0.1415
- masks scored: 10/10 (+2 top-k)
- ranked sources:
    - `+1.179` [justplainclear] hernia: When part of an organ or tissue inside of you bulges through a weak area of muscle. Most hernias are i
    - `+0.569` [nih] hernia: The bulging of an internal organ through a weak area or tear in the muscle or other tissue that holds 
    - `-0.588` [readme] hernia: A hernia is when an organ pokes through a hole in a muscle.

- rationale: A hernia is a protrusion of tissue through a weak spot, so "bulge" captures that physical sign in everyday language. Word frequency rises from Zipf 3.00 to 3.24, age of acquisition drops from 12.29 to 8.10, and syllable count falls from 3 to 1. Readers can recognize the visible swelling without needing the clinical label.
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

**output:** The doctor checked the rest of the body and found nothing wrong.

| metric | value |
|---|---:|
| bertscore_f1 | 0.404 |
| coleman_liau | 6.87 |
| coleman_liau_drop | 4.53 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 3.84 |
| fkgl_drop | 4.53 |
| fre | 88.9 |
| fre_gain | 36.0 |
| human_edit_recall | 1.000 |
| length_ratio | 1.20 |
| n_words | 12.0 |
| negation_preservation | 0.000 |
| nli_completeness | 0.475 |
| nli_faithfulness | 0.056 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.750 |
| sari | 7.23 |
| smog | 3.13 |
| smog_drop | 5.71 |

### Stage 4 - arm `termonly`

**output:** Other systems were checked and seemed normal.

| metric | value |
|---|---:|
| bertscore_f1 | 0.725 |
| coleman_liau | 11.46 |
| coleman_liau_drop | -0.06 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 4.00 |
| fkgl_drop | 4.37 |
| fre | 78.9 |
| fre_gain | 26.0 |
| human_edit_recall | 1.000 |
| length_ratio | 0.70 |
| n_words | 7.0 |
| negation_preservation | 0.000 |
| nli_completeness | 0.979 |
| nli_faithfulness | 0.987 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.667 |
| sari | 20.38 |
| smog | 3.13 |
| smog_drop | 5.71 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `unremarkable` -> `normal` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Other systems were checked and seemed normal.

| metric | value |
|---|---:|
| bertscore_f1 | 0.725 |
| coleman_liau | 11.46 |
| coleman_liau_drop | -0.06 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 4.00 |
| fkgl_drop | 4.37 |
| fre | 78.9 |
| fre_gain | 26.0 |
| human_edit_recall | 1.000 |
| length_ratio | 0.70 |
| n_words | 7.0 |
| negation_preservation | 0.000 |
| nli_completeness | 0.979 |
| nli_faithfulness | 0.987 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.667 |
| sari | 20.38 |
| smog | 3.13 |
| smog_drop | 5.71 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `unremarkable` -> `normal` | replace | attributed | 0.029 | 0.668 | - | - | - | - |

**edit `unremarkable` -> `normal`**

- status: `attributed`
- log p full -0.0312, empty -0.0601
- masks scored: 4/4 (+1 top-k)
- ranked sources:
    - `+0.648` [wiktionary] unremarkable: If something is unremarkable, it is common and ordinary.

- rationale: "Unremarkable" means nothing unusual was found, so "normal" conveys that same idea in everyday language. Word frequency rises from Zipf 2.83 to 5.01, age of acquisition drops from 11.06 to 5.53, and syllables decrease from 5 to 2. You can see that the results show no signs of disease.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True
