# Step-by-step detail - together-muse-glimmer (`run100_20260815_222318`)

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

**output:** He lost interest in things he used to enjoy and stopped caring about social activities. He also had trouble sleeping because he woke up often and felt restless.

| metric | value |
|---|---:|
| bertscore_f1 | 0.527 |
| coleman_liau | 9.22 |
| coleman_liau_drop | 9.74 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 7.57 |
| fkgl_drop | 8.46 |
| fre | 65.7 |
| fre_gain | 55.3 |
| human_edit_recall | 1.000 |
| length_ratio | 1.40 |
| n_words | 28.0 |
| nli_completeness | 0.018 |
| nli_faithfulness | 0.991 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.714 |
| sari | 13.31 |
| smog | 7.17 |
| smog_drop | 8.73 |

### Stage 4 - arm `termonly`

**output:** He lost the ability to feel pleasure and was not interested in social activities, and had difficulty sleeping for frequent waking and restlessness.

| metric | value |
|---|---:|
| bertscore_f1 | 0.873 |
| coleman_liau | 13.93 |
| coleman_liau_drop | 5.03 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 14.41 |
| fkgl_drop | 1.61 |
| fre | 32.7 |
| fre_gain | 22.2 |
| human_edit_recall | 1.000 |
| length_ratio | 1.15 |
| n_words | 23.0 |
| nli_completeness | 0.982 |
| nli_faithfulness | 0.986 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 56.21 |
| smog | 15.90 |
| smog_drop | 0.00 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `anhedonic` -> `lost the ability to feel pleasure` | replace | - | - | - | - | - | - | - |
| `disinterested` -> `not interested` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** He lost interest in things and was not interested in social activities, and had difficulty sleeping for frequent waking and restlessness.

| metric | value |
|---|---:|
| bertscore_f1 | 0.791 |
| coleman_liau | 14.55 |
| coleman_liau_drop | 4.41 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 12.83 |
| fkgl_drop | 3.20 |
| fre | 40.5 |
| fre_gain | 30.1 |
| human_edit_recall | 1.000 |
| length_ratio | 1.05 |
| n_words | 21.0 |
| nli_completeness | 0.988 |
| nli_faithfulness | 0.993 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 46.30 |
| smog | 14.55 |
| smog_drop | 1.35 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `anhedonic` -> `lost interest in things` | replace | attributed | 0.120 | 0.138 | - | 0.400 | 0.429 | - |
| `disinterested` -> `not interested` | replace | attributed | 0.338 | 0.730 | - | 1.000 | 1.371 | - |

**edit `anhedonic` -> `lost interest in things`**

- status: `attributed`
- log p full -1.9406, empty -2.0602
- masks scored: 6/6 (+2 top-k)
- ranked sources:
    - `+0.284` [wiktionary] disinterested: If someone is disinterested, they are not affected by a situation, so they can make fair decisi
    - `-0.145` [wiktionary] disinterested: If someone is disinterested, they are not interested in something; they find it boring.

- rationale: The original term describes a reduced ability to feel pleasure, so "lost interest in things" conveys that loss of enjoyment in plain words. Phrase frequency rises from Zipf 1.11 to 4.90, while syllable count goes from 4 to 5. Readers can grasp the mood symptom without needing a clinical label.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `disinterested` -> `not interested`**

- status: `attributed`
- log p full -0.4674, empty -0.8050
- masks scored: 6/6 (+2 top-k)
- ranked sources:
    - `+1.050` [wiktionary] disinterested: If someone is disinterested, they are not interested in something; they find it boring.
    - `-0.320` [wiktionary] disinterested: If someone is disinterested, they are not affected by a situation, so they can make fair decisi

- rationale: The original term means not interested, and the replacement carries that meaning in plain words. Word frequency increases from Zipf 2.91 to 4.94, while age of acquisition falls from 12.40 to 8.83. Patients can understand the basic heart-rhythm problem without first knowing the diagnostic name.
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

**output:** Myocardial infarction cannot be ruled out.

| metric | value |
|---|---:|
| bertscore_f1 | 0.361 |
| coleman_liau | 14.07 |
| coleman_liau_drop | 0.00 |
| copy_jargon_rate | 1.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.250 |
| diagnostic_identity_preservation | 1.000 |
| fkgl | 12.32 |
| fkgl_drop | 1.97 |
| fre | 17.4 |
| fre_gain | 14.1 |
| human_edit_recall | 0.000 |
| length_ratio | 1.00 |
| n_words | 6.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.993 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 14.19 |
| smog | 11.21 |
| smog_drop | 1.82 |
| uncertainty_preservation | 1.000 |

### Stage 4 - arm `termonly`

**output:** A heart attack can still happen.

| metric | value |
|---|---:|
| bertscore_f1 | 0.457 |
| coleman_liau | 4.40 |
| coleman_liau_drop | 9.67 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.200 |
| diagnostic_identity_preservation | 1.000 |
| fkgl | 2.48 |
| fkgl_drop | 11.80 |
| fre | 87.9 |
| fre_gain | 84.6 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 6.0 |
| negation_preservation | 0.000 |
| nli_completeness | 0.858 |
| nli_faithfulness | 0.835 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 32.02 |
| smog | 3.13 |
| smog_drop | 9.89 |
| uncertainty_preservation | 0.000 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `Myocardial infarction` -> `heart attack` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** A heart attack may still be present.

| metric | value |
|---|---:|
| bertscore_f1 | 0.469 |
| coleman_liau | 4.00 |
| coleman_liau_drop | 10.07 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.200 |
| diagnostic_identity_preservation | 1.000 |
| fkgl | 2.31 |
| fkgl_drop | 11.97 |
| fre | 91.0 |
| fre_gain | 87.6 |
| human_edit_recall | 1.000 |
| length_ratio | 1.17 |
| n_words | 7.0 |
| negation_preservation | 0.000 |
| nli_completeness | 0.671 |
| nli_faithfulness | 0.772 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 25.97 |
| smog | 3.13 |
| smog_drop | 9.89 |
| uncertainty_preservation | 1.000 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `Myocardial infarction` -> `heart attack` | replace | attributed | 0.070 | 2.623 | 0.654 | 0.799 | 0.332 | - |

**edit `Myocardial infarction` -> `heart attack`**

- status: `attributed`
- log p full -0.0057, empty -0.0761
- masks scored: 66/66 (+2 top-k)
- ranked sources:
    - `+0.855` [readme] inferior myocardial infarction: A heart attack caused by a blockage in a blood vessel that affects the lower p
    - `+0.523` [iowa] MYOCARDIAL INFARCTION: heart attack
    - `+0.503` [justplainclear] myocardial infarction: A heart attack
    - `+0.225` [readme] inferior wall myocardial infarction: Heart damage at the bottom of the left ventricle due to a blocked artery.
    - `+0.136` [wiktionary] not: The item before "not" is more correct or better than the item after "not".

- rationale: The original term refers to death of heart muscle tissue from loss of blood supply, and "heart attack" conveys that same life-threatening heart injury in everyday language. Phrase frequency rises from Zipf 2.58 to 4.89, while age of acquisition falls from 16.64 to 6.58. Readers can grasp the seriousness of the event without needing medical training.
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

**output:** There was a large bruise and swelling in the bursa under the deltoid muscle.

| metric | value |
|---|---:|
| bertscore_f1 | 0.459 |
| coleman_liau | 7.77 |
| coleman_liau_drop | 6.53 |
| copy_jargon_rate | 0.250 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.333 |
| fkgl | 5.88 |
| fkgl_drop | 0.13 |
| fre | 77.8 |
| fre_gain | 8.0 |
| human_edit_recall | 0.750 |
| length_ratio | 1.00 |
| n_words | 14.0 |
| nli_completeness | 0.981 |
| nli_faithfulness | 0.917 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.250 |
| sari | 38.10 |
| severity_downgrade | 0.000 |
| severity_preservation | 1.000 |
| severity_tier_input | 2.000 |
| severity_tier_output | 2.000 |
| smog | 3.13 |
| smog_drop | 5.71 |

### Stage 4 - arm `termonly`

**output:** There was a lot of blood pooling and swelling in the fluid sac under the shoulder muscle.

| metric | value |
|---|---:|
| bertscore_f1 | 0.626 |
| coleman_liau | 7.02 |
| coleman_liau_drop | 7.28 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 7.00 |
| fkgl_drop | -0.99 |
| fre | 75.1 |
| fre_gain | 5.3 |
| human_edit_recall | 1.000 |
| length_ratio | 1.21 |
| n_words | 17.0 |
| nli_completeness | 0.726 |
| nli_faithfulness | 0.728 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.200 |
| sari | 43.53 |
| severity_downgrade | 1.000 |
| severity_preservation | 0.000 |
| severity_tier_input | 2.000 |
| smog | 3.13 |
| smog_drop | 5.71 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `marked` -> `a lot of` | replace | - | - | - | - | - | - | - |
| `hematoma` -> `blood pooling` | replace | - | - | - | - | - | - | - |
| `subdeltoid bursa` -> `fluid sac under the shoulder muscle` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** There was a lot of a blood pool and swelling within the small fluid sac under the shoulder muscle.

| metric | value |
|---|---:|
| bertscore_f1 | 0.593 |
| coleman_liau | 6.76 |
| coleman_liau_drop | 7.54 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.750 |
| fkgl | 7.35 |
| fkgl_drop | -1.34 |
| fre | 76.2 |
| fre_gain | 6.5 |
| human_edit_recall | 1.000 |
| length_ratio | 1.36 |
| n_words | 19.0 |
| nli_completeness | 0.588 |
| nli_faithfulness | 0.774 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 70.33 |
| severity_downgrade | 1.000 |
| severity_preservation | 1.000 |
| severity_tier_input | 2.000 |
| severity_tier_output | 1.000 |
| smog | 3.13 |
| smog_drop | 5.71 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `marked` -> `a lot of` | replace | attributed | -0.665 | -0.784 | 0.814 | 0.834 | 0.199 | - |
| `hematoma` -> `a blood pool` | replace | attributed | 1.251 | 1.368 | 0.896 | 0.935 | 2.151 | - |
| `subdeltoid bursa` -> `small fluid sac under the shoulder muscle` | replace | attributed | 0.942 | 0.969 | 0.860 | 0.896 | 0.271 | - |

**edit `marked` -> `a lot of`**

- status: `attributed`
- log p full -2.2428, empty -1.5778
- masks scored: 66/66 (+5 top-k)
- ranked sources:
    - `+0.334` [readme] bursa: A small sac of fluid that cushions joints as they move.
    - `+0.135` [nih] hematoma: A pool of clotted or partially clotted blood in an organ, tissue, or body space, usually caused by a

- rationale: The original term "marked" means noticeable or significant, and "a lot of" carries that sense of a large amount or clear presence in plain words. Phrase frequency increases from Zipf 4.50 to 5.60, while syllables increase from 1 to 3. Readers can grasp the degree being described without needing the more formal adjective.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `hematoma` -> `a blood pool`**

- status: `attributed`
- log p full -1.9104, empty -3.1611
- masks scored: 66/66 (+5 top-k)
- ranked sources:
    - `+2.494` [nih] hematoma: A pool of clotted or partially clotted blood in an organ, tissue, or body space, usually caused by a
    - `+0.343` [justplainclear] hematoma: A collection of blood under the skin or in the body that is typically caused by a broken blood vesse
    - `+0.180` [readme] bursa: A small sac of fluid that cushions joints as they move.

- rationale: The source describes a hematoma as a pool of clotted or partially clotted blood in an organ, tissue, or body space, usually caused by a broken blood vessel, so "a blood pool" keeps the core idea of collected blood in plain words. Phrase frequency rises from Zipf 2.61 to 4.53, while age of acquisition falls from 14.78 to 5.15. Readers can grasp that bleeding has collected under the skin or in tissue without needing the medical label.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `subdeltoid bursa` -> `small fluid sac under the shoulder muscle`**

- status: `attributed`
- log p full -3.1428, empty -4.0848
- masks scored: 66/66 (+5 top-k)
- ranked sources:
    - `+0.722` [justplainclear] bursa: A small sac (pouch) found in your body which is filled with fluid. Bursa help your tendons or muscles m
    - `+0.451` [readme] bursa: A small sac of fluid that cushions joints as they move.
    - `+0.025` [iowa] HEMATOMA: a bruise, a black and blue mark

- rationale: The source describes a bursa as a small fluid-filled sac that lets tendons or muscles glide around joints, so "small fluid sac under the shoulder muscle" keeps that cushioning role in plain words. Phrase frequency rises from Zipf 0.00 to 3.46, while age of acquisition falls from 15.78 to 9.00. Readers can picture where the structure sits and what it does without needing the anatomical label.
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

### Stage 4 - arm `termonly`

**output:** Smoking history, high blood pressure, and high blood fats.

| metric | value |
|---|---:|
| bertscore_f1 | 0.854 |
| coleman_liau | 11.20 |
| coleman_liau_drop | 16.96 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 4.96 |
| fkgl_drop | 14.44 |
| fre | 75.5 |
| fre_gain | 110.6 |
| human_edit_recall | 1.000 |
| length_ratio | 0.82 |
| n_words | 9.0 |
| nli_completeness | 0.924 |
| nli_faithfulness | 0.971 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 70.53 |
| smog | 8.84 |
| smog_drop | 4.18 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `hypertension` -> `high blood pressure` | replace | - | - | - | - | - | - | - |
| `hyperlipidemia` -> `high blood fats` | replace | - | - | - | - | - | - | - |

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
| `hypertension` -> `high blood pressure` | replace | attributed | 0.042 | 2.378 | 0.294 | 0.695 | 0.093 | - |
| `hyperlipidemia` -> `high cholesterol` | replace | attributed | 5.623 | 8.842 | 0.948 | 0.905 | 4.558 | - |

**edit `hypertension` -> `high blood pressure`**

- status: `attributed`
- log p full -0.0044, empty -0.0465
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.532` [iowa] HYPERTENSION: high blood pressure
    - `+0.439` [readme] HYPERTENSION: High blood pressure: when the force of blood in your arteries is too high.
    - `+0.111` [justplainclear] hypertension: Also known as: high blood pressure, HBP A condition of having high blood pressure for a long per
    - `+0.019` [justplainclear] hyperlipidemia: High cholesterol
    - `+0.002` [wiktionary] hypertension: Hypertension is the disease of having high blood pressure.

- rationale: High blood pressure is the common name for hypertension, a condition where the force of blood against artery walls is higher than normal, and the replacement keeps that pressure idea in everyday words. Phrase frequency rises from Zipf 3.41 to 4.71, while age of acquisition falls from 16.28 to 8.95. Readers can now recognize the condition from familiar language about blood pressure rather than a medical label.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `hyperlipidemia` -> `high cholesterol`**

- status: `attributed`
- log p full -0.0407, empty -5.6641
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+7.002` [justplainclear] hyperlipidemia: High cholesterol
    - `+2.444` [michigan] hyperlipidemia: High levels of fat or fat-like substances (cholesterol). Hyperlipidemia is also called high ch
    - `+0.584` [readme] hypertension: High blood pressure is when the force of blood in the arteries is too high.
    - `+0.143` [iowa] HYPERTENSION: high blood pressure

- rationale: The source describes hyperlipidemia as high cholesterol, so "high cholesterol" keeps the core idea in plain words. Phrase frequency increases from Zipf 1.95 to 3.72, while syllable count rises from 4 to 5. Patients can understand the basic blood-fat problem without first knowing the diagnostic name.
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

**output:** She said she had bladder spasms when she urinated, and she has a history of chronic UTIs.

| metric | value |
|---|---:|
| bertscore_f1 | 0.704 |
| coleman_liau | 6.68 |
| coleman_liau_drop | 0.14 |
| copy_jargon_rate | 1.000 |
| critical_error | 0.000 |
| fkgl | 7.70 |
| fkgl_drop | 1.20 |
| fre | 70.1 |
| fre_gain | 1.4 |
| human_edit_recall | 0.000 |
| length_ratio | 0.74 |
| n_words | 17.0 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.994 |
| replacement_f1 | 0.000 |
| rewrite_aggressiveness | 1.000 |
| sari | 22.80 |
| smog | 11.21 |
| smog_drop | 0.00 |
| temporality_preservation | 1.000 |

### Stage 4 - arm `termonly`

**output:** She did complain of bladder cramps when she passed urine and she did say that she has a history of long-term bladder infections.

| metric | value |
|---|---:|
| bertscore_f1 | 0.803 |
| coleman_liau | 9.14 |
| coleman_liau_drop | -2.32 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.333 |
| fkgl | 9.80 |
| fkgl_drop | -0.90 |
| fre | 65.8 |
| fre_gain | -2.9 |
| human_edit_recall | 1.000 |
| length_ratio | 1.04 |
| n_words | 24.0 |
| nli_completeness | 0.982 |
| nli_faithfulness | 0.994 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 34.11 |
| smog | 11.21 |
| smog_drop | 0.00 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `bladder spasms` -> `bladder cramps` | replace | - | - | - | - | - | - | - |
| `urinated` -> `passed urine` | replace | - | - | - | - | - | - | - |
| `chronic UTIs` -> `long-term bladder infections` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** She did complain of sudden tight, painful muscle cramps in the sac that holds pee when she passed urine and she did say that she has a history of long-lasting infections in the urinary system.

| metric | value |
|---|---:|
| bertscore_f1 | 0.607 |
| coleman_liau | 9.04 |
| coleman_liau_drop | -2.22 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.714 |
| fkgl | 14.92 |
| fkgl_drop | -6.02 |
| fre | 50.5 |
| fre_gain | -18.2 |
| human_edit_recall | 1.000 |
| length_ratio | 1.57 |
| n_words | 36.0 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.980 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 31.75 |
| smog | 14.55 |
| smog_drop | -3.35 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `bladder spasms` -> `sudden tight, painful muscle cramps in the sac that holds pee` | replace | attributed | 25.721 | 25.722 | 0.952 | 0.968 | 2.828 | - |
| `urinated` -> `passed urine` | replace | attributed | 2.987 | 4.197 | 0.815 | 0.935 | 2.442 | - |
| `chronic UTIs` -> `long-lasting infections in the urinary system` | replace | attributed | 10.342 | 11.204 | 0.842 | 0.952 | 5.754 | - |

**edit `bladder spasms` -> `sudden tight, painful muscle cramps in the sac that holds pee`**

- status: `attributed`
- log p full -7.4800, empty -33.2015
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+11.980` [readme] bladder: A bladder is a sac in your body that holds pee.
    - `+9.152` [readme] spasms: When your muscles suddenly tighten up and hurt.
    - `+1.604` [wiktionary] spasms: A spasm is a sudden and jerky movement.
    - `+0.865` [readme] BLADDER: Bladder: Holds pee in your body.
    - `+0.660` [readme] chronic: An ongoing or frequently recurring health issue.

- rationale: The readme describes a bladder as a sac in your body that holds pee, so “sudden tight, painful muscle cramps in the sac that holds pee” keeps the location and the cramp-like sensation in plain words. Phrase frequency rises from Zipf 2.89 to 3.01, while age of acquisition falls from 10.78 to 9.00. Readers can picture where the pain comes from and what it feels like without needing the medical label.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `urinated` -> `passed urine`**

- status: `attributed`
- log p full -0.3390, empty -3.3264
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+2.721` [wiktionary] urinated: When a person or animal urinates, it passes urine to empty the bladder.
    - `+0.279` [dorland] UTIs: urinary tract infections
    - `+0.229` [readme] bladder: A bladder is a sac in your body that holds pee.
    - `+0.218` [readme] BLADDER: Bladder: Holds pee in your body.
    - `+0.202` [michigan] chronic: Something, like a disease or symptom, that lasts for a long time.

- rationale: The source describes urinating as passing urine to empty the bladder, so "passed urine" keeps the same bodily action in plain words. Phrase frequency increases from Zipf 2.31 to 3.81, while syllable count stays at 3. Readers can follow what happened without needing the verb "urinated".
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `chronic UTIs` -> `long-lasting infections in the urinary system`**

- status: `attributed`
- log p full -0.5490, empty -10.8908
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+7.427` [readme] UTIs: UTIs are infections in the urinary system.
    - `+1.673` [justplainclear] chronic: Long term, long lasting, lifelong, constant, never ending, never goes away, happens again and again
    - `+1.043` [michigan] chronic: Something, like a disease or symptom, that lasts for a long time.
    - `+1.017` [dorland] UTIs: urinary tract infections
    - `+0.260` [iowa] CHRONIC: continuing for a long time, ongoing

- rationale: The source describes UTIs as infections in the urinary system, so "long-lasting infections in the urinary system" keeps the infection location and adds the duration implied by chronic. Phrase frequency increases from Zipf 2.05 to 3.17, while age of acquisition rises from 11.25 to 12.56. Readers can see that the problem is a persistent infection where urine is made and passed.
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

**output:** There was no knee instability and no fluid buildup in the knee.

| metric | value |
|---|---:|
| bertscore_f1 | 0.832 |
| coleman_liau | 6.38 |
| coleman_liau_drop | -0.20 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 6.79 |
| fkgl_drop | 0.40 |
| fre | 67.8 |
| fre_gain | 6.4 |
| human_edit_recall | 1.000 |
| length_ratio | 1.09 |
| n_words | 12.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.993 |
| nli_faithfulness | 0.993 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 30.40 |
| smog | 8.84 |
| smog_drop | 2.37 |

### Stage 4 - arm `termonly`

**output:** There was no looseness of the knee and no fluid build-up.

| metric | value |
|---|---:|
| bertscore_f1 | 0.782 |
| coleman_liau | 5.24 |
| coleman_liau_drop | 0.94 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 3.72 |
| fkgl_drop | 3.47 |
| fre | 88.0 |
| fre_gain | 26.7 |
| human_edit_recall | 1.000 |
| length_ratio | 1.09 |
| n_words | 12.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.993 |
| nli_faithfulness | 0.994 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 45.00 |
| smog | 3.13 |
| smog_drop | 8.08 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `instability` -> `looseness` | replace | - | - | - | - | - | - | - |
| `effusion` -> `fluid build-up` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** There was no wobble of the knee and no extra fluid.

| metric | value |
|---|---:|
| bertscore_f1 | 0.775 |
| coleman_liau | 2.60 |
| coleman_liau_drop | 3.58 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 3.72 |
| fkgl_drop | 3.47 |
| fre | 88.0 |
| fre_gain | 26.7 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 11.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.994 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 39.24 |
| smog | 3.13 |
| smog_drop | 8.08 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `instability` -> `wobble` | replace | attributed | 0.062 | 0.073 | - | 0.894 | 0.015 | - |
| `effusion` -> `extra fluid` | replace | attributed | 1.735 | 2.329 | - | 1.000 | 0.741 | - |

**edit `instability` -> `wobble`**

- status: `attributed`
- log p full -1.8731, empty -1.9349
- masks scored: 6/6 (+2 top-k)
- ranked sources:
    - `-0.015` [nih] effusion: An abnormal collection of fluid in hollow spaces or between tissues of the body. For example, a pleu

- rationale: Instability means a lack of firmness or steadiness that can make something unsteady or prone to change, and wobble conveys that same sense of unsteady movement in plain, everyday language. Phrase frequency falls from Zipf 3.71 to 3.02, while age of acquisition falls from 12.55 to 6.56. Readers can grasp the idea of something being unsteady without needing a more abstract term.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `effusion` -> `extra fluid`**

- status: `attributed`
- log p full -0.7013, empty -2.4364
- masks scored: 6/6 (+2 top-k)
- ranked sources:
    - `+1.586` [nih] effusion: An abnormal collection of fluid in hollow spaces or between tissues of the body. For example, a pleu
    - `+0.845` [wiktionary] instability: Instability is the condition of not being stable, which can make things uncertain or unsafe.

- rationale: Effusion means fluid that has collected where it should not be, and "extra fluid" keeps that idea of an unwanted buildup in plain words. Phrase frequency rises from Zipf 2.41 to 4.15, while age of acquisition falls from 14.29 to 7.94. Readers can grasp the problem of fluid accumulation without needing the medical label.
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

**output:** Two days later, the pain went away and she has not had a come-back.

| metric | value |
|---|---:|
| bertscore_f1 | 0.832 |
| coleman_liau | 3.21 |
| coleman_liau_drop | 2.35 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 4.20 |
| fkgl_drop | 0.71 |
| fre | 89.9 |
| fre_gain | 6.9 |
| human_edit_recall | 1.000 |
| length_ratio | 1.07 |
| n_words | 15.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.994 |
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
| `resolved` -> `went away` | replace | - | - | - | - | - | - | - |
| `recurrence` -> `come-back` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Two days later, the pain ended and she has not had a come-back.

| metric | value |
|---|---:|
| bertscore_f1 | 0.786 |
| coleman_liau | 3.34 |
| coleman_liau_drop | 2.23 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 4.00 |
| fkgl_drop | 0.91 |
| fre | 89.5 |
| fre_gain | 6.5 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 14.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.994 |
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
| `resolved` -> `ended` | replace | attributed | 0.277 | 0.540 | - | 0.818 | 0.874 | - |
| `recurrence` -> `come-back` | replace | attributed | 0.987 | 1.411 | - | 0.927 | 0.017 | - |

**edit `resolved` -> `ended`**

- status: `attributed`
- log p full -0.5894, empty -0.8664
- masks scored: 34/34 (+4 top-k)
- ranked sources:
    - `+0.888` [wiktionary] resolved: When a problem is resolved, it has been brought to a successful solution.
    - `+0.014` [wiktionary] resolved: To resolve means to create a solution for a problem.
    - `-0.054` [nih] recurrence: Cancer that has recurred (come back), usually after a period of time during which the cancer could
    - `-0.116` [wiktionary] recurrence: A recurrence is something that happens again.
    - `-0.239` [readme] recurrence: When a disease comes back after being treated.

- rationale: The original term "resolved" means settled or brought to a conclusion, and "ended" carries that same sense of something coming to a close in plain words. Phrase frequency increases from Zipf 4.10 to 4.92, while syllable count stays the same from 2 to 2. Readers can now see that the issue is finished without needing a formal word.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `recurrence` -> `come-back`**

- status: `attributed`
- log p full -0.7833, empty -1.7707
- masks scored: 34/34 (+4 top-k)
- ranked sources:
    - `+0.707` [readme] recurrence: When a disease comes back after being treated.
    - `+0.690` [nih] recurrence: Cancer that has recurred (come back), usually after a period of time during which the cancer could
    - `+0.066` [wiktionary] resolved: When a problem is resolved, it has been brought to a successful solution.
    - `-0.362` [wiktionary] recurrence: A recurrence is something that happens again.

- rationale: The original term recurrence means an event happening again, and come-back carries that same idea of something returning in plain words. Syllables decrease from 3 to 2. Readers can now grasp the idea of repetition without a technical label.
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

**output:** Description: The patient has a fever, an ear infection, and may have sepsis.

| metric | value |
|---|---:|
| bertscore_f1 | 0.500 |
| coleman_liau | 8.69 |
| coleman_liau_drop | 7.74 |
| copy_jargon_rate | 0.500 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| diagnostic_identity_preservation | 1.000 |
| fkgl | 7.63 |
| fkgl_drop | 6.48 |
| fre | 63.5 |
| fre_gain | 57.1 |
| human_edit_recall | 0.500 |
| length_ratio | 1.62 |
| n_words | 13.0 |
| nli_completeness | 0.910 |
| nli_faithfulness | 0.807 |
| replacement_f1 | 0.667 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 39.75 |
| smog | 11.21 |
| smog_drop | 1.82 |
| uncertainty_preservation | 1.000 |

### Stage 4 - arm `termonly`

**output:** Fever, middle ear infection, and possible body-wide infection.

| metric | value |
|---|---:|
| bertscore_f1 | 0.597 |
| coleman_liau | 17.47 |
| coleman_liau_drop | -1.05 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| diagnostic_identity_preservation | 1.000 |
| fkgl | 12.61 |
| fkgl_drop | 1.51 |
| fre | 18.9 |
| fre_gain | 12.6 |
| human_edit_recall | 1.000 |
| length_ratio | 1.12 |
| n_words | 9.0 |
| nli_completeness | 0.778 |
| nli_faithfulness | 0.830 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.250 |
| sari | 53.31 |
| smog | 13.02 |
| smog_drop | 0.00 |
| uncertainty_preservation | 1.000 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `otitis media` -> `middle ear infection` | replace | - | - | - | - | - | - | - |
| `sepsis` -> `body-wide infection` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Description: Fever, middle ear infection, and possible body-wide infection from germs.

| metric | value |
|---|---:|
| bertscore_f1 | 0.685 |
| coleman_liau | 18.95 |
| coleman_liau_drop | -2.52 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| diagnostic_identity_preservation | 1.000 |
| fkgl | 12.30 |
| fkgl_drop | 1.81 |
| fre | 26.5 |
| fre_gain | 20.1 |
| human_edit_recall | 1.000 |
| length_ratio | 1.50 |
| n_words | 12.0 |
| nli_completeness | 0.601 |
| nli_faithfulness | 0.603 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 58.99 |
| smog | 14.55 |
| smog_drop | -1.53 |
| uncertainty_preservation | 1.000 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `otitis media` -> `middle ear infection` | replace | attributed | 0.685 | 1.224 | 0.624 | 0.844 | 1.535 | - |
| `sepsis` -> `body-wide infection from germs` | replace | attributed | 7.855 | 7.944 | 0.658 | 0.667 | 0.407 | - |

**edit `otitis media` -> `middle ear infection`**

- status: `attributed`
- log p full -0.5274, empty -1.2125
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+1.736` [thesaurus] otitis media: middle ear infection
    - `+0.201` [readme] sepsis: A severe condition where the body reacts to bacteria in the bloodstream by harming tissues and organs,
    - `-0.144` [readme] Sepsis: When bacteria get into the blood, the body's reaction can lead to tissue and organ damage, potentially
    - `-0.148` [nih] sepsis: The presence of bacteria or their toxins in the blood or tissues.
    - `-0.184` [michigan] sepsis: A very serious infection in your blood caused by a germ (a bacteria). Also called septicemia.

- rationale: The original term otitis media refers to inflammation or infection of the middle ear, and the replacement middle ear infection names the same location and problem in plain words. Phrase frequency rises from Zipf 2.16 to 4.04, while syllable count changes from 5 to 6. Readers can recognize the condition as an infection in the middle ear without needing the Latin medical label.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `sepsis` -> `body-wide infection from germs`**

- status: `attributed`
- log p full -2.4696, empty -10.3249
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+1.742` [readme] sepsis: A severe condition where the body reacts to bacteria in the bloodstream by harming tissues and organs,
    - `+1.335` [nih] sepsis: The presence of bacteria or their toxins in the blood or tissues.
    - `+1.074` [readme] Sepsis: When bacteria get into the blood, the body's reaction can lead to tissue and organ damage, potentially
    - `+0.676` [readme] otitis media: An ear infection causing inflammation in the middle ear.
    - `+0.109` [thesaurus] otitis media: middle ear infection

- rationale: The source describes sepsis as a severe body reaction to bacteria in the bloodstream that can harm tissues and organs and potentially lead to death, so "body-wide infection from germs" keeps that systemic, infection-driven danger in plain words. Phrase frequency rises from Zipf 3.01 to 3.33, while age of acquisition falls from 16.33 to 8.05. Readers can grasp the life-threatening spread without needing the clinical label.
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

**output:** Currently, the main problem is tiredness that she feels all day.

| metric | value |
|---|---:|
| bertscore_f1 | 0.734 |
| coleman_liau | 8.93 |
| coleman_liau_drop | 2.89 |
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
| nli_completeness | 0.994 |
| nli_faithfulness | 0.994 |
| number_unit_preservation | 0.500 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.400 |
| sari | 19.66 |
| smog | 11.21 |
| smog_drop | 0.00 |
| temporality_preservation | 1.000 |

### Stage 4 - arm `termonly`

**output:** Currently, the main issue is one of tiredness that she feels throughout the day.

| metric | value |
|---|---:|
| bertscore_f1 | 0.819 |
| coleman_liau | 9.01 |
| coleman_liau_drop | 2.80 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 6.73 |
| fkgl_drop | 0.91 |
| fre | 71.8 |
| fre_gain | 8.3 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 14.0 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.994 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 41.44 |
| smog | 11.21 |
| smog_drop | 0.00 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `primary complaint` -> `main issue` | replace | - | - | - | - | - | - | - |
| `fatigue` -> `tiredness` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Currently, the main reason she went to the doctor is feeling tired all over that she feels throughout the day.

| metric | value |
|---|---:|
| bertscore_f1 | 0.629 |
| coleman_liau | 8.53 |
| coleman_liau_drop | 3.29 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 8.73 |
| fkgl_drop | -1.10 |
| fre | 68.1 |
| fre_gain | 4.6 |
| human_edit_recall | 1.000 |
| length_ratio | 1.43 |
| n_words | 20.0 |
| nli_completeness | 0.993 |
| nli_faithfulness | 0.005 |
| number_unit_preservation | 0.500 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.250 |
| sari | 39.72 |
| smog | 8.84 |
| smog_drop | 2.37 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `primary complaint` -> `main reason she went to the doctor` | replace | attributed | 5.751 | 5.862 | 0.853 | 0.935 | 6.173 | - |

**edit `primary complaint` -> `main reason she went to the doctor`**

- status: `attributed`
- log p full -2.2485, empty -7.9992
- masks scored: 66/66 (+2 top-k)
- ranked sources:
    - `+6.505` [michigan] complaint: Your illness or symptom that is most important; the main reason you go to the doctor. Also known as
    - `+0.332` [wiktionary] fatigue: Fatigue is the material failure, such as cracking or separation, caused by stress on the material.
    - `+0.246` [wiktionary] primary: A primary is a kind of election held by a political party to choose the people it prefers for public 
    - `+0.169` [wiktionary] complaint: A complaint is an expression of dissatisfaction
    - `+0.074` [wiktionary] fatigue: Fatigue is the extreme tiredness which is the result of having mental or physical exertion or illness

- rationale: The source describes the primary complaint as the illness or symptom that is most important, the main reason you go to the doctor, also known as chief complaint, so "main reason she went to the doctor" keeps that central idea in plain words. Phrase frequency rises from Zipf 4.21 to 4.57, while age of acquisition falls from 8.89 to 7.84. Patients can now see at a glance why the visit happened without needing the clinical label.
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

**output:** He has noticed some changes in his bowel movements with occasional loose stools and new pain mostly in the left side of his neck.

| metric | value |
|---|---:|
| bertscore_f1 | 0.688 |
| coleman_liau | 8.34 |
| coleman_liau_drop | 3.61 |
| copy_jargon_rate | 0.333 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.167 |
| fkgl | 9.50 |
| fkgl_drop | 2.81 |
| fre | 69.7 |
| fre_gain | 29.1 |
| human_edit_recall | 0.667 |
| laterality_preservation | 1.000 |
| length_ratio | 1.26 |
| n_words | 24.0 |
| nli_completeness | 0.993 |
| nli_faithfulness | 0.992 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.200 |
| sari | 19.62 |
| smog | 8.84 |
| smog_drop | 4.18 |
| temporality_preservation | 0.000 |

### Stage 4 - arm `termonly`

**output:** He has noted some change in bowel habits with occasional watery stools and a recent start of pain mostly in left neck.

| metric | value |
|---|---:|
| bertscore_f1 | 0.721 |
| coleman_liau | 8.16 |
| coleman_liau_drop | 3.78 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.375 |
| fkgl | 10.15 |
| fkgl_drop | 2.16 |
| fre | 61.5 |
| fre_gain | 20.8 |
| human_edit_recall | 1.000 |
| laterality_preservation | 1.000 |
| length_ratio | 1.16 |
| n_words | 22.0 |
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
| `stool irregularity` -> `change in bowel habits` | replace | - | - | - | - | - | - | - |
| `loose stools` -> `watery stools` | replace | - | - | - | - | - | - | - |
| `new onset` -> `recent start` | replace | - | - | - | - | - | - | - |
| `predominantly` -> `mostly` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** He has noted some bowel movement change with occasional watery poop and start of pain mostly in left neck.

| metric | value |
|---|---:|
| bertscore_f1 | 0.744 |
| coleman_liau | 9.20 |
| coleman_liau_drop | 2.75 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.375 |
| fkgl | 9.21 |
| fkgl_drop | 3.11 |
| fre | 62.9 |
| fre_gain | 22.3 |
| human_edit_recall | 1.000 |
| laterality_preservation | 1.000 |
| length_ratio | 1.00 |
| n_words | 19.0 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.987 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 34.50 |
| smog | 11.21 |
| smog_drop | 1.82 |
| temporality_preservation | 0.000 |

annotation backend `novita`, 4 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `stool irregularity` -> `bowel movement change` | replace | attributed | 1.802 | 1.883 | 0.644 | 0.869 | 0.092 | - |
| `loose stools` -> `watery poop` | replace | attributed | 3.735 | 6.505 | 0.647 | 0.919 | 5.359 | - |
| `new onset` -> `start` | replace | attributed | 2.182 | 2.559 | 0.825 | 0.902 | 2.617 | - |
| `predominantly` -> `mostly` | replace | attributed | 0.011 | 0.083 | 0.218 | 0.433 | 0.005 | - |

**edit `stool irregularity` -> `bowel movement change`**

- status: `attributed`
- log p full -2.3898, empty -4.1918
- masks scored: 66/66 (+8 top-k)
- ranked sources:
    - `+0.364` [justplainclear] stool: Also known as: bowel movement, BM, feces, poop The solid or semi-solid waste that passes out of your re
    - `+0.272` [readme] loose stools: Watery poop.
    - `+0.241` [michigan] onset: The start.
    - `+0.195` [dictionary] Predominantly (adv.): In a predominant manner.
    - `+0.170` [nih] stool: The material in a bowel movement. Stool is made up of undigested food, bacteria, mucus, and cells from 

- rationale: Bowel movement change describes a deviation from a person’s usual pattern of passing stool, and the replacement keeps that idea of a change in bowel habits in everyday language. Phrase frequency rises from Zipf 2.52 to 3.53, while age of acquisition falls from 12.63 to 9.72. Readers can recognize the symptom as a shift in normal bowel habits without needing the clinical phrasing.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `loose stools` -> `watery poop`**

- status: `attributed`
- log p full -0.0632, empty -3.7987
- masks scored: 66/66 (+8 top-k)
- ranked sources:
    - `+5.561` [readme] loose stools: Watery poop.
    - `+0.202` [justplainclear] stool: Also known as: bowel movement, BM, feces, poop The solid or semi-solid waste that passes out of your re
    - `+0.169` [wiktionary] stool: A stool is a piece of feces.
    - `+0.072` [readme] Stool: Stool is the waste material that comes out during a bowel movement.
    - `+0.008` [wiktionary] new: If somebody is new, they are not experienced.

- rationale: The source describes loose stools as watery poop, so "watery poop" keeps the core idea in plain words. Phrase frequency increases from Zipf 3.03 to 3.06, while age of acquisition falls from 7.71 to 6.65. Patients can understand the symptom description without first knowing the clinical term.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `new onset` -> `start`**

- status: `attributed`
- log p full -1.0771, empty -3.2591
- masks scored: 66/66 (+8 top-k)
- ranked sources:
    - `+2.904` [michigan] onset: The start.
    - `+0.286` [justplainclear] stool: Also known as: bowel movement, BM, feces, poop The solid or semi-solid waste that passes out of your re
    - `+0.193` [dictionary] Predominantly (adv.): In a predominant manner.
    - `+0.177` [dictionary] Irregularity (n.): The state or quality of being irregular; that which is irregular.
    - `+0.107` [wiktionary] new: If somebody is new, they are not experienced.

- rationale: The source describes new onset as the start, so "start" keeps the idea of something beginning now in plain words. Phrase frequency increases from Zipf 3.72 to 5.56, while age of acquisition falls from 10.72 to 4.37. Patients can understand when a condition began without needing the clinical phrasing.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `predominantly` -> `mostly`**

- status: `attributed`
- log p full -0.1408, empty -0.1520
- masks scored: 66/66 (+8 top-k)
- ranked sources:
    - `+0.112` [wiktionary] stool: A stool is a piece of feces.
    - `+0.108` [michigan] onset: The start.
    - `+0.095` [readme] stool: The stuff that comes out when you go to the bathroom.
    - `+0.038` [dictionary] Predominantly (adv.): In a predominant manner.
    - `+0.036` [readme] loose stools: Watery poop.

- rationale: The original term means mainly or for the most part, and "mostly" carries that same sense of a clear majority in plain words. Phrase frequency rises from Zipf 3.80 to 4.83, while syllables fall from 5 to 2. Readers can grasp the proportion being described without a formal adverb.
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

**output:** The patient comes back for a checkup because they have a history of erythema nodosum.

| metric | value |
|---|---:|
| bertscore_f1 | 0.311 |
| coleman_liau | 9.29 |
| coleman_liau_drop | 5.31 |
| copy_jargon_rate | 1.000 |
| critical_error | 0.000 |
| fkgl | 8.35 |
| fkgl_drop | 3.35 |
| fre | 61.9 |
| fre_gain | 29.4 |
| human_edit_recall | 0.000 |
| length_ratio | 0.88 |
| n_words | 15.0 |
| nli_completeness | 0.981 |
| nli_faithfulness | 0.991 |
| replacement_f1 | 0.000 |
| rewrite_aggressiveness | 1.000 |
| sari | 10.50 |
| smog | 11.21 |
| smog_drop | 3.35 |
| temporality_preservation | 1.000 |

### Stage 4 - arm `termonly`

**output:** The patient comes back for a check on a history of tender red bumps on the shins.

| metric | value |
|---|---:|
| bertscore_f1 | 0.545 |
| coleman_liau | 4.29 |
| coleman_liau_drop | 10.31 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 5.62 |
| fkgl_drop | 6.09 |
| fre | 85.1 |
| fre_gain | 52.6 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 17.0 |
| nli_completeness | 0.520 |
| nli_faithfulness | 0.175 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.600 |
| sari | 21.99 |
| smog | 8.84 |
| smog_drop | 5.71 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `erythema nodosum` -> `tender red bumps on the shins` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** The patient comes back for a check on a history of red skin nodules.

| metric | value |
|---|---:|
| bertscore_f1 | 0.504 |
| coleman_liau | 4.46 |
| coleman_liau_drop | 10.14 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 5.04 |
| fkgl_drop | 6.67 |
| fre | 83.9 |
| fre_gain | 51.4 |
| human_edit_recall | 1.000 |
| length_ratio | 0.82 |
| n_words | 14.0 |
| nli_completeness | 0.879 |
| nli_faithfulness | 0.829 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.600 |
| sari | 22.82 |
| smog | 8.84 |
| smog_drop | 5.71 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `erythema nodosum` -> `red skin nodules` | replace | attributed | 11.674 | 11.855 | - | 0.929 | 3.676 | - |

**edit `erythema nodosum` -> `red skin nodules`**

- status: `attributed`
- log p full -1.7984, empty -13.4728
- masks scored: 10/10 (+2 top-k)
- ranked sources:
    - `+6.614` [readme] Erythema: Red skin.
    - `+2.937` [nih] erythema: Redness of the skin.
    - `+1.529` [readme] erythema: Skin redness.

- rationale: The original term erythema nodosum refers to a condition marked by red, tender nodules on the skin, and “red skin nodules” keeps that visual and tactile feature in plain words. Phrase frequency rises from Zipf 1.39 to 2.73, while syllable count falls from 5 to 4. Readers can picture the symptom without needing the Latin diagnostic label.
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

**output:** She was low on iron last year, and with many surgeries and poor food intake by mouth, she may be low on iron again.

| metric | value |
|---|---:|
| bertscore_f1 | 0.775 |
| coleman_liau | 4.48 |
| coleman_liau_drop | 3.40 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.200 |
| fkgl | 9.01 |
| fkgl_drop | -1.54 |
| fre | 73.2 |
| fre_gain | 12.1 |
| human_edit_recall | 1.000 |
| length_ratio | 1.04 |
| n_words | 24.0 |
| nli_completeness | 0.826 |
| nli_faithfulness | 0.145 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.667 |
| sari | 26.89 |
| smog | 8.84 |
| smog_drop | 2.37 |
| uncertainty_preservation | 1.000 |

### Stage 4 - arm `termonly`

**output:** She had too little iron in her blood last year, and with her many operations and poor intake by mouth, may have too little iron in her blood again.

| metric | value |
|---|---:|
| bertscore_f1 | 0.680 |
| coleman_liau | 6.38 |
| coleman_liau_drop | 1.49 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.200 |
| fkgl | 11.59 |
| fkgl_drop | -4.12 |
| fre | 63.6 |
| fre_gain | 2.5 |
| human_edit_recall | 1.000 |
| length_ratio | 1.26 |
| n_words | 29.0 |
| nli_completeness | 0.820 |
| nli_faithfulness | 0.188 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.750 |
| sari | 23.91 |
| smog | 8.84 |
| smog_drop | 2.37 |
| uncertainty_preservation | 1.000 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `iron deficient` -> `too little iron in her blood` | replace | - | - | - | - | - | - | - |
| `p. o.` -> `by mouth` | replace | - | - | - | - | - | - | - |
| `iron deficient` -> `too little iron in her blood` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** She had not enough iron in her blood last year, and with her many operations and poor intake by mouth, may have not enough iron in her blood again.

| metric | value |
|---|---:|
| bertscore_f1 | 0.657 |
| coleman_liau | 6.38 |
| coleman_liau_drop | 1.49 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.200 |
| fkgl | 11.59 |
| fkgl_drop | -4.12 |
| fre | 63.6 |
| fre_gain | 2.5 |
| human_edit_recall | 1.000 |
| length_ratio | 1.26 |
| n_words | 29.0 |
| nli_completeness | 0.823 |
| nli_faithfulness | 0.203 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.750 |
| sari | 23.91 |
| smog | 8.84 |
| smog_drop | 2.37 |
| uncertainty_preservation | 1.000 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `iron deficient` -> `not enough iron in her blood` | replace | attributed | 2.713 | 3.259 | 0.700 | 0.868 | 0.774 | - |
| `p. o.` -> `by mouth` | replace | attributed | -0.002 | -1.824 | 0.489 | 0.844 | 0.261 | - |
| `iron deficient` -> `not enough iron in her blood` | replace | attributed | -0.346 | -2.417 | 0.582 | 0.668 | -0.000 | - |

**edit `iron deficient` -> `not enough iron in her blood`**

- status: `attributed`
- log p full -0.8276, empty -3.5410
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+1.457` [thesaurus] deficient: lacking, not enough, poor
    - `+0.682` [readme] deficient: Not having as much of something as needed.
    - `+0.589` [nih] iron: An important mineral the body needs to make hemoglobin, a substance in the blood that carries oxygen fro
    - `+0.111` [michigan] deficient: To not have enough.

- rationale: The thesaurus lists "iron deficient" as meaning lacking, not enough, or poor, so "not enough iron in her blood" keeps that sense of insufficiency in plain language. Phrase frequency rises from Zipf 3.31 to 4.53, while age of acquisition falls from 11.61 to 7.32. Readers can grasp the nutritional shortfall without needing the clinical label.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `p. o.` -> `by mouth`**

- status: `attributed`
- log p full -0.0030, empty -0.0005
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.285` [thesaurus] deficient: lacking, not enough, poor
    - `+0.025` [wiktionary] iron: An element with the symbol Fe and the atomic number 26.

- rationale: You explain, to a patient, why one phrase in a medical sentence was replaced with another.
- audit: coverage 0.0, grounding_error=False, omission=True, source_ok=True, passage_ok=True

**edit `iron deficient` -> `not enough iron in her blood`**

- status: `attributed`
- log p full -0.3877, empty -0.0414
- masks scored: 66/66 (+4 top-k)
- ranked sources:

- rationale: The original term means the body lacks sufficient iron, and the replacement says the same idea in plain words by stating there is not enough iron in her blood. Phrase frequency rises from Zipf 3.31 to 4.53, while age of acquisition falls from 11.61 to 7.32. Readers can grasp the nutritional shortfall without needing the medical label.
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

**output:** We will set up a Holter monitor for him and send him back to his heart doctor.

| metric | value |
|---|---:|
| bertscore_f1 | 0.717 |
| coleman_liau | 3.27 |
| coleman_liau_drop | 5.25 |
| copy_jargon_rate | 1.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 5.62 |
| fkgl_drop | 3.52 |
| fre | 85.1 |
| fre_gain | 28.8 |
| human_edit_recall | 0.000 |
| length_ratio | 1.06 |
| n_words | 17.0 |
| nli_completeness | 0.965 |
| nli_faithfulness | 0.981 |
| replacement_f1 | 0.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.667 |
| sari | 23.53 |
| smog | 8.84 |
| smog_drop | 2.37 |

### Stage 4 - arm `termonly`

**output:** We will schedule him for a heart rhythm recorder worn for a day or two and refer him back to his heart doctor.

| metric | value |
|---|---:|
| bertscore_f1 | 0.688 |
| coleman_liau | 4.85 |
| coleman_liau_drop | 3.67 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 8.26 |
| fkgl_drop | 0.88 |
| fre | 76.8 |
| fre_gain | 20.6 |
| human_edit_recall | 1.000 |
| length_ratio | 1.44 |
| n_words | 23.0 |
| nli_completeness | 0.568 |
| nli_faithfulness | 0.114 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 43.61 |
| smog | 8.84 |
| smog_drop | 2.37 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `Holter monitor` -> `heart rhythm recorder worn for a day or two` | replace | - | - | - | - | - | - | - |
| `cardiologist` -> `heart doctor` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** We will schedule him for a portable machine for recording heart beats and refer him back to his heart doctor.

| metric | value |
|---|---:|
| bertscore_f1 | 0.812 |
| coleman_liau | 8.53 |
| coleman_liau_drop | -0.01 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 8.73 |
| fkgl_drop | 0.41 |
| fre | 68.1 |
| fre_gain | 11.8 |
| human_edit_recall | 1.000 |
| length_ratio | 1.25 |
| n_words | 20.0 |
| nli_completeness | 0.162 |
| nli_faithfulness | 0.740 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 43.95 |
| smog | 11.21 |
| smog_drop | 0.00 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `Holter monitor` -> `portable machine for recording heart beats` | replace | attributed | 26.237 | 27.858 | - | 0.874 | 26.902 | - |
| `cardiologist` -> `heart doctor` | replace | attributed | 0.274 | 2.941 | - | 0.928 | 5.564 | - |

**edit `Holter monitor` -> `portable machine for recording heart beats`**

- status: `attributed`
- log p full -0.2205, empty -26.4580
- masks scored: 34/34 (+4 top-k)
- ranked sources:
    - `+26.913` [iowa] HOLTER MONITOR: a portable machine for recording heart beats
    - `+0.012` [michigan] cardiologist: A doctor who treats heart and blood vessel problems.
    - `-0.302` [nih] cardiologist: A doctor who has special training to diagnose and treat diseases of the heart and blood vessels.

- rationale: A Holter monitor is a small, wearable device that continuously records the heart’s electrical activity over a day or more, and “portable machine for recording heart beats” conveys that same idea of a mobile recorder that tracks heart beats. Phrase frequency rises from Zipf 2.12 to 3.67, while age of acquisition falls from 9.68 to 7.95. Readers can grasp that the device is a portable recorder for heart beats without needing prior medical vocabulary.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `cardiologist` -> `heart doctor`**

- status: `attributed`
- log p full -0.0178, empty -0.2920
- masks scored: 34/34 (+4 top-k)
- ranked sources:
    - `+6.123` [justplainclear] cardiologist: Heart doctor
    - `+0.559` [nih] cardiologist: A doctor who has special training to diagnose and treat diseases of the heart and blood vessels.
    - `-0.376` [wiktionary] cardiologist: A cardiologist is a doctor who specializes in medical problems related to the heart.
    - `-1.652` [michigan] cardiologist: A doctor who treats heart and blood vessel problems.
    - `-3.569` [iowa] HOLTER MONITOR: a portable machine for recording heart beats

- rationale: A cardiologist is a medical specialist who diagnoses and treats diseases of the heart and blood vessels, so "heart doctor" keeps that specialist role in everyday words. Phrase frequency rises from Zipf 2.90 to 4.76, while age of acquisition falls from 13.42 to 5.17. Readers can immediately grasp who will care for heart problems without needing specialist vocabulary.
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

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `proceed` -> `go ahead` | replace | - | - | - | - | - | - | - |
| `operative intervention` -> `surgery` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** The patient wanted to go forward with surgery.

| metric | value |
|---|---:|
| bertscore_f1 | 0.804 |
| coleman_liau | 8.05 |
| coleman_liau_drop | 8.70 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
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

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `proceed` -> `go forward` | replace | attributed | 2.424 | 3.927 | 0.607 | 0.873 | 0.984 | - |
| `operative intervention` -> `surgery` | replace | attributed | 0.348 | 1.055 | 0.247 | 0.741 | 0.746 | - |

**edit `proceed` -> `go forward`**

- status: `attributed`
- log p full -0.2318, empty -2.6562
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+1.938` [wiktionary] proceed: When you proceed, you go forward with something.
    - `+0.954` [michigan] proceed: To go or move forward.
    - `+0.618` [readme] operative: Dealing with surgeries.
    - `+0.463` [wiktionary] operative: If something is operative, it is able to work.
    - `+0.346` [michigan] intervention: A treatment or program.

- rationale: The source describes proceed as moving forward with something, so "go forward" keeps that sense of continuing onward in plain words. Phrase frequency rises from Zipf 4.18 to 5.07, while age of acquisition falls from 8.33 to 4.24. Readers can follow the intended action without needing the more formal verb.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `operative intervention` -> `surgery`**

- status: `attributed`
- log p full -0.2516, empty -0.5997
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+1.398` [readme] Operative: Operative means related to surgery.
    - `+0.652` [readme] operative: Dealing with surgeries.
    - `+0.582` [readme] intervention: An intervention is a step taken to help treat or prevent a health problem.
    - `+0.573` [wiktionary] operative: If something is operative, it is able to work.
    - `+0.545` [wiktionary] proceed: (formal) The proceeds of some individual project or sale are the money earned from doing it.

- rationale: You explain, to a patient, why one phrase in a medical sentence was replaced with another.
- audit: coverage 0.0, grounding_error=False, omission=True, source_ok=True, passage_ok=True

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

**output:** A KUB X-ray was taken and it showed an unusual pattern of gas in the bowel.

| metric | value |
|---|---:|
| bertscore_f1 | 0.553 |
| coleman_liau | 3.38 |
| coleman_liau_drop | 5.12 |
| copy_jargon_rate | 1.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.333 |
| fkgl | 6.88 |
| fkgl_drop | 0.31 |
| fre | 74.3 |
| fre_gain | 12.9 |
| human_edit_recall | 0.000 |
| length_ratio | 1.00 |
| n_words | 17.0 |
| nli_completeness | 0.991 |
| nli_faithfulness | 0.136 |
| replacement_f1 | 0.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 16.39 |
| smog | 8.84 |
| smog_drop | 0.00 |

### Stage 4 - arm `termonly`

**output:** A plain X-ray of the belly was done showing a bowel gas pattern that is not normal.

| metric | value |
|---|---:|
| bertscore_f1 | 0.622 |
| coleman_liau | 4.64 |
| coleman_liau_drop | 3.86 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 6.31 |
| fkgl_drop | 0.88 |
| fre | 80.1 |
| fre_gain | 18.8 |
| human_edit_recall | 1.000 |
| length_ratio | 1.06 |
| n_words | 18.0 |
| nli_completeness | 0.874 |
| nli_faithfulness | 0.635 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 28.94 |
| smog | 3.13 |
| smog_drop | 5.71 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `obtained` -> `done` | replace | - | - | - | - | - | - | - |
| `abnormal bowel gas pattern` -> `bowel gas pattern that is not normal` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** A x-ray of the kidneys, ureters, and bladder was done showing a not normal bowel gas design.

| metric | value |
|---|---:|
| bertscore_f1 | 0.806 |
| coleman_liau | 7.02 |
| coleman_liau_drop | 1.48 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.600 |
| fkgl | 7.00 |
| fkgl_drop | 0.19 |
| fre | 75.1 |
| fre_gain | 13.8 |
| human_edit_recall | 1.000 |
| length_ratio | 1.06 |
| n_words | 18.0 |
| nli_completeness | 0.889 |
| nli_faithfulness | 0.110 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 26.45 |
| smog | 3.13 |
| smog_drop | 5.71 |

annotation backend `novita`, 4 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `KUB` -> `x-ray of the kidneys, ureters, and bladder` | replace | attributed | 11.690 | 12.086 | 0.805 | 0.867 | 11.633 | - |
| `obtained` -> `done` | replace | attributed | -0.350 | -1.249 | 0.376 | 0.853 | 0.221 | - |
| `abnormal` -> `not normal` | replace | attributed | 3.428 | 4.636 | 0.188 | 0.698 | 2.135 | - |
| `pattern` -> `design` | replace | attributed | 4.382 | 4.832 | 0.699 | 0.908 | 4.761 | - |

**edit `KUB` -> `x-ray of the kidneys, ureters, and bladder`**

- status: `attributed`
- log p full -1.1188, empty -12.8089
- masks scored: 66/66 (+7 top-k)
- ranked sources:
    - `+11.708` [dorland] KUB: kidneys, ureters, and bladder (x-ray)
    - `+0.075` [wiktionary] abnormal: An abnormal thing, or situation, is one that is strange, or not typical.
    - `+0.029` [readme] Bowel: Your intestines in the belly that break down food.

- rationale: The source describes KUB as kidneys, ureters, and bladder (x-ray), so "x-ray of the kidneys, ureters, and bladder" keeps the anatomical scope and imaging modality in plain language. Syllables increase from 1 to 9. Patients can understand which body parts are being imaged and that it is an x-ray.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `obtained` -> `done`**

- status: `attributed`
- log p full -0.5340, empty -0.1843
- masks scored: 66/66 (+7 top-k)
- ranked sources:
    - `+0.412` [dorland] KUB: kidneys, ureters, and bladder (x-ray)
    - `+0.190` [nih] bowel: The long, tube-shaped organ in the abdomen that completes the process of digestion. The bowel has two p
    - `+0.084` [wiktionary] abnormal: When something is abnormal, it often means that it is bigger than [[normal].
    - `+0.068` [readme] Bowel: Your intestines in the belly that break down food.
    - `+0.064` [justplainclear] abnormal: Not normal, different from usual

- rationale: The original term "obtained" means got or acquired, and "done" carries that sense of something having been completed or carried out. Phrase frequency increases from Zipf 4.49 to 5.58, while syllables fall from 2 to 1. Readers can follow that a procedure or result was completed without needing a more formal word.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `abnormal` -> `not normal`**

- status: `attributed`
- log p full -0.3455, empty -3.7740
- masks scored: 66/66 (+7 top-k)
- ranked sources:
    - `+3.815` [justplainclear] abnormal: Not normal, different from usual
    - `+1.680` [nih] abnormal: Not normal. Describes a state, condition, or behavior that is unusual or different from what is cons
    - `+1.061` [wiktionary] bowel: The bowel is an internal organ which helps an organism digest food.
    - `+0.878` [readme] bowel: The intestines in your belly that break down food.
    - `+0.460` [wiktionary] gas: Gas is a substance such as methane, ethane, propane, or butane that is burned for heat or to make electri

- rationale: You explain, to a patient, why one phrase in a medical sentence was replaced with another.
- audit: coverage 0.0, grounding_error=False, omission=True, source_ok=True, passage_ok=True

**edit `pattern` -> `design`**

- status: `attributed`
- log p full -1.0060, empty -5.3879
- masks scored: 66/66 (+7 top-k)
- ranked sources:
    - `+5.324` [wiktionary] pattern: A pattern is a design that uses the same set of elements many times in the same order.
    - `+0.563` [wiktionary] gas: A gas is a substance, such as air, that is not liquid or solid.
    - `+0.261` [dorland] KUB: kidneys, ureters, and bladder (x-ray)
    - `+0.198` [justplainclear] abnormal: Not normal, different from usual
    - `+0.166` [michigan] abnormal: Something that is not usual, like a growth or low or high amounts of blood cells.

- rationale: The source describes a pattern as a design that uses the same set of elements many times in the same order, so "design" keeps the idea of a repeated arrangement in plain words. Phrase frequency increases from Zipf 4.56 to 5.17, while age of acquisition rises from 6.89 to 10.05. Readers can grasp the notion of a repeated arrangement without needing the technical term.
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

**output:** She was given Ativan to calm her, and she arrived at the emergency room very drowsy and unable to share any history.

| metric | value |
|---|---:|
| bertscore_f1 | 0.717 |
| coleman_liau | 7.37 |
| coleman_liau_drop | 1.83 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 11.76 |
| fkgl_drop | 0.55 |
| fre | 49.9 |
| fre_gain | 9.3 |
| human_edit_recall | 1.000 |
| length_ratio | 1.10 |
| n_words | 22.0 |
| nli_completeness | 0.993 |
| nli_faithfulness | 0.994 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.667 |
| sari | 30.61 |
| severity_downgrade | 0.000 |
| severity_tier_input | 3.000 |
| severity_tier_output | 3.000 |
| smog | 13.02 |
| smog_drop | 2.88 |

### Stage 4 - arm `termonly`

**output:** She has been calmed with a medicine that slows the brain and came into the emergency room very drowsy and unable to give any history.

| metric | value |
|---|---:|
| bertscore_f1 | 0.753 |
| coleman_liau | 8.07 |
| coleman_liau_drop | 1.13 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 12.10 |
| fkgl_drop | 0.22 |
| fre | 52.9 |
| fre_gain | 12.2 |
| human_edit_recall | 1.000 |
| length_ratio | 1.25 |
| n_words | 25.0 |
| nli_completeness | 0.015 |
| nli_faithfulness | 0.949 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 53.42 |
| severity_downgrade | 0.000 |
| severity_tier_input | 3.000 |
| severity_tier_output | 3.000 |
| smog | 14.55 |
| smog_drop | 1.35 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `sedated` -> `calmed` | replace | - | - | - | - | - | - | - |
| `Ativan` -> `a medicine that slows the brain` | replace | - | - | - | - | - | - | - |
| `obtunded` -> `very drowsy` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** She has been made sleepy with a medicine that calms and came into the emergency room not fully alert and unable to give any history.

| metric | value |
|---|---:|
| bertscore_f1 | 0.669 |
| coleman_liau | 7.84 |
| coleman_liau_drop | 1.36 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.667 |
| fkgl | 12.57 |
| fkgl_drop | -0.25 |
| fre | 49.5 |
| fre_gain | 8.9 |
| human_edit_recall | 1.000 |
| length_ratio | 1.25 |
| n_words | 25.0 |
| nli_completeness | 0.015 |
| nli_faithfulness | 0.985 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 39.08 |
| severity_downgrade | 0.000 |
| severity_tier_input | 3.000 |
| severity_tier_output | 3.000 |
| smog | 14.55 |
| smog_drop | 1.35 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `sedated` -> `made sleepy` | replace | attributed | 0.907 | 1.809 | - | 0.747 | 0.623 | - |
| `Ativan` -> `a medicine that calms` | replace | attributed | -0.144 | -0.297 | - | 0.515 | 0.049 | - |
| `obtunded` -> `not fully alert` | replace | attributed | 6.132 | 7.482 | - | 0.856 | 6.835 | - |

**edit `sedated` -> `made sleepy`**

- status: `attributed`
- log p full -0.3414, empty -1.2485
- masks scored: 18/18 (+4 top-k)
- ranked sources:
    - `+1.407` [readme] SEDATED: Feeling calm, relaxed, or sleepy because of certain medications.
    - `+0.784` [readme] Sedated: When you're sedated, you feel calm, relaxed, or sleepy because of specific medication.
    - `+0.286` [readme] obtunded: Being not fully alert.
    - `-0.439` [wiktionary] sedated: A sedate person is calm and dignified.

- rationale: You explain, to a patient, why one phrase in a medical sentence was replaced with another.
- audit: coverage 0.0, grounding_error=False, omission=True, source_ok=True, passage_ok=True

**edit `Ativan` -> `a medicine that calms`**

- status: `attributed`
- log p full -0.7341, empty -0.5906
- masks scored: 18/18 (+4 top-k)
- ranked sources:
    - `+0.049` [readme] obtunded: Being not fully alert.
    - `-0.007` [readme] Sedated: When you're sedated, you feel calm, relaxed, or sleepy because of specific medication.
    - `-0.164` [readme] SEDATED: Feeling calm, relaxed, or sleepy because of certain medications.

- rationale: You explain, to a patient, why one phrase in a medical sentence was replaced with another.
- audit: coverage 0.0, grounding_error=False, omission=True, source_ok=True, passage_ok=True

**edit `obtunded` -> `not fully alert`**

- status: `attributed`
- log p full -0.2993, empty -6.4310
- masks scored: 18/18 (+4 top-k)
- ranked sources:
    - `+7.302` [readme] obtunded: Being not fully alert.
    - `+0.467` [readme] SEDATED: Feeling calm, relaxed, or sleepy because of certain medications.
    - `+0.395` [readme] Sedated: When you're sedated, you feel calm, relaxed, or sleepy because of specific medication.
    - `+0.214` [wiktionary] sedated: A sedate person is calm and dignified.

- rationale: You explain, to a patient, why one phrase in a medical sentence was replaced with another.
- audit: coverage 0.0, grounding_error=False, omission=True, source_ok=True, passage_ok=True

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

**output:** He has no swelling now, but he had some mild leg swelling before.

| metric | value |
|---|---:|
| bertscore_f1 | 0.878 |
| coleman_liau | 4.68 |
| coleman_liau_drop | -2.34 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 4.00 |
| fkgl_drop | 0.42 |
| fre | 89.5 |
| fre_gain | -0.6 |
| human_edit_recall | 1.000 |
| length_ratio | 0.87 |
| n_words | 13.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.210 |
| nli_faithfulness | 0.994 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 45.99 |
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
| `edema` -> `swelling` | replace | attributed | 0.221 | 1.432 | - | 0.612 | 0.087 | - |

**edit `edema` -> `swelling`**

- status: `attributed`
- log p full -0.0809, empty -0.3022
- masks scored: 34/34 (+2 top-k)
- ranked sources:
    - `+0.530` [nih] edema: Swelling caused by excess fluid in body tissues.
    - `+0.444` [readme] Edema: Swelling in the body caused by too much fluid.
    - `+0.347` [michigan] edema: Swelling caused by too much fluid in your body.
    - `+0.335` [readme] edema: Swelling due to too much fluid in the body tissues.
    - `-0.459` [iowa] EDEMA: excess fluid collecting in tissue

- rationale: The original term edema refers to a build-up of fluid in tissues that makes an area puffy, and the replacement swelling carries that same idea of visible puffiness in everyday language. Phrase frequency rises from Zipf 2.95 to 3.68, while syllable count falls from 3 to 2. Readers can now recognize the physical change being described without needing a medical label.
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

### Stage 4 - arm `termonly`

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
| `secondary hyperparathyroidism` -> `overactive parathyroid glands from another cause` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Mild second too much parathyroid hormone.

| metric | value |
|---|---:|
| bertscore_f1 | 0.424 |
| coleman_liau | 13.10 |
| coleman_liau_drop | 23.10 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.667 |
| fkgl | 4.45 |
| fkgl_drop | 16.53 |
| fre | 73.8 |
| fre_gain | 123.8 |
| human_edit_recall | 1.000 |
| length_ratio | 1.20 |
| n_words | 6.0 |
| nli_completeness | 0.751 |
| nli_faithfulness | 0.765 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 24.31 |
| severity_downgrade | 0.000 |
| severity_preservation | 1.000 |
| severity_tier_input | 1.000 |
| severity_tier_output | 1.000 |
| smog | 3.13 |
| smog_drop | 8.08 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `secondary hyperparathyroidism` -> `too much parathyroid hormone` | replace | attributed | 5.736 | 5.782 | - | 0.859 | 2.152 | - |

**edit `secondary hyperparathyroidism` -> `too much parathyroid hormone`**

- status: `attributed`
- log p full -3.0843, empty -8.8200
- masks scored: 18/18 (+2 top-k)
- ranked sources:
    - `+4.142` [wiktionary] secondary: second, next in order to the first or primary.
    - `+1.991` [nih] hyperparathyroidism: A condition in which the parathyroid gland (one of four pea-sized organs found on the thy
    - `+0.354` [justplainclear] hyperparathyroidism: A condition where your parathyroid glands work too hard and raise the calcium level in yo
    - `-0.908` [wiktionary] secondary: of less than primary importance.

- rationale: You explain, to a patient, why one phrase in a medical sentence was replaced with another.
- audit: coverage 0.0, grounding_error=False, omission=True, source_ok=True, passage_ok=True

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

**output:** Otherwise, a full review of systems was done and was negative except for what was mentioned above.

| metric | value |
|---|---:|
| bertscore_f1 | 0.744 |
| coleman_liau | 9.75 |
| coleman_liau_drop | 2.68 |
| copy_jargon_rate | 1.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 9.09 |
| fkgl_drop | 1.48 |
| fre | 60.2 |
| fre_gain | 12.4 |
| human_edit_recall | 0.000 |
| length_ratio | 1.06 |
| n_words | 17.0 |
| nli_completeness | 0.993 |
| nli_faithfulness | 0.994 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 17.58 |
| smog | 11.21 |
| smog_drop | 0.00 |

### Stage 4 - arm `termonly`

**output:** Otherwise, a full check of body systems was done and showed no problems except for as mentioned above.

| metric | value |
|---|---:|
| bertscore_f1 | 0.641 |
| coleman_liau | 9.30 |
| coleman_liau_drop | 3.14 |
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
| nli_faithfulness | 0.207 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.250 |
| sari | 28.44 |
| smog | 8.84 |
| smog_drop | 2.37 |

annotation backend `novita`, 0 edits kept


### Stage 4 - arm `grounded`

**output:** Otherwise, a full set of symptom questions was asked and showed no problems except for as mentioned above.

| metric | value |
|---|---:|
| bertscore_f1 | 0.566 |
| coleman_liau | 10.59 |
| coleman_liau_drop | 1.85 |
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
| nli_completeness | 0.962 |
| nli_faithfulness | 0.644 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.200 |
| sari | 26.81 |
| smog | 8.84 |
| smog_drop | 2.37 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `review of systems` -> `full set of symptom questions` | replace | attributed | 2.818 | 3.099 | - | 0.849 | 3.018 | - |
| `obtained` -> `asked` | replace | attributed | -0.186 | -1.966 | - | 0.899 | 0.300 | - |
| `negative` -> `no problems` | replace | attributed | 0.054 | 0.132 | - | 0.638 | 0.457 | - |

**edit `review of systems` -> `full set of symptom questions`**

- status: `attributed`
- log p full -1.3624, empty -4.1806
- masks scored: 18/18 (+4 top-k)
- ranked sources:
    - `+3.018` [readme] Review of systems: Questions that ask patients about any symptoms they might be experiencing in different part
    - `-0.069` [wiktionary] negative: If something is negative, it is harmful, sad, or otherwise not good.

- rationale: A review of systems is a structured checklist of body systems used to ask about symptoms, and “full set of symptom questions” keeps that idea of a broad, systematic symptom inquiry in everyday language. Phrase frequency falls from Zipf 4.79 to 3.62, while age of acquisition falls from 8.84 to 8.68, and syllables rise from 5 to 7. Readers can grasp that the clinician is simply going through a comprehensive set of questions about how they feel.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `obtained` -> `asked`**

- status: `attributed`
- log p full -0.2195, empty -0.0338
- masks scored: 18/18 (+4 top-k)
- ranked sources:
    - `+0.300` [wiktionary] negative: If a word, sentence, answer, etc. is negative, it uses a word like no, not, never, etc.
    - `-0.297` [wiktionary] negative: If something is negative, it is harmful, sad, or otherwise not good.
    - `-2.087` [wiktionary] obtained: If you obtain something, you get it.

- rationale: The original term "obtained" means got or received, and "asked" carries that meaning in plain words by focusing on the act of requesting information. Phrase frequency increases from Zipf 4.49 to 5.30, while syllables decrease from 2 to 1. Patients can understand the basic heart-rhythm problem without first knowing the diagnostic name.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `negative` -> `no problems`**

- status: `attributed`
- log p full -0.4962, empty -0.5497
- masks scored: 18/18 (+4 top-k)
- ranked sources:
    - `+0.459` [wiktionary] negative: If a word, sentence, answer, etc. is negative, it uses a word like no, not, never, etc.
    - `+0.002` [wiktionary] obtained: If you obtain something, you get it.
    - `-0.144` [readme] Review of systems: Questions that ask patients about any symptoms they might be experiencing in different part
    - `-0.284` [wiktionary] negative: If something is negative, it is harmful, sad, or otherwise not good.

- rationale: The original term "negative" means a test result that did not detect the condition being looked for, and "no problems" carries that meaning in plain words by stating the absence of issues. Phrase frequency increases from Zipf 4.79 to 5.16, while age of acquisition falls from 7.47 to 2.72. Readers can now understand the result without needing the technical label.
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

**output:** Symptoms get worse when the person sits for a long time, like when driving a car.

| metric | value |
|---|---:|
| bertscore_f1 | 0.735 |
| coleman_liau | 5.55 |
| coleman_liau_drop | 2.54 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 4.66 |
| fkgl_drop | 2.95 |
| fre | 90.1 |
| fre_gain | 21.1 |
| human_edit_recall | 1.000 |
| length_ratio | 1.07 |
| n_words | 16.0 |
| nli_completeness | 0.925 |
| nli_faithfulness | 0.994 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.667 |
| sari | 17.77 |
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
| `motor vehicle` -> `car` | replace | attributed | -0.313 | -4.224 | - | - | - | - |

**edit `motor vehicle` -> `car`**

- status: `attributed`
- log p full -0.3180, empty -0.0055
- masks scored: 4/4 (+1 top-k)
- ranked sources:
    - `-4.541` [wiktionary] motor vehicle: A motor vehicle a road vehicle powered by an internal combustion engine to provide power to rot

- rationale: You explain, to a patient, why one phrase in a medical sentence was replaced with another.
- audit: coverage 0.0, grounding_error=False, omission=True, source_ok=True, passage_ok=True

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

**output:** The exam of the forearm, elbow, and shoulder shows no nerve or brain-related problems.

| metric | value |
|---|---:|
| bertscore_f1 | 0.607 |
| coleman_liau | 10.67 |
| coleman_liau_drop | 6.33 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 8.41 |
| fkgl_drop | 4.42 |
| fre | 59.7 |
| fre_gain | 40.6 |
| human_edit_recall | 1.000 |
| length_ratio | 1.67 |
| n_words | 15.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.992 |
| nli_faithfulness | 0.976 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 39.07 |
| smog | 8.84 |
| smog_drop | 2.37 |

### Stage 4 - arm `termonly`

**output:** Forearm, elbow and shoulder exams show no nerve or brain problem.

| metric | value |
|---|---:|
| bertscore_f1 | 0.875 |
| coleman_liau | 9.45 |
| coleman_liau_drop | 7.55 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.333 |
| fkgl | 5.86 |
| fkgl_drop | 6.97 |
| fre | 72.6 |
| fre_gain | 53.5 |
| human_edit_recall | 1.000 |
| length_ratio | 1.22 |
| n_words | 11.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.990 |
| nli_faithfulness | 0.943 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 48.68 |
| smog | 3.13 |
| smog_drop | 8.08 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `neurologic compromise` -> `nerve or brain problem` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Forearm, elbow and shoulder exams show no nerve harm.

| metric | value |
|---|---:|
| bertscore_f1 | 0.894 |
| coleman_liau | 8.62 |
| coleman_liau_drop | 8.38 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 4.96 |
| fkgl_drop | 7.87 |
| fre | 75.5 |
| fre_gain | 56.4 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 9.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.930 |
| nli_faithfulness | 0.957 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 50.33 |
| smog | 3.13 |
| smog_drop | 8.08 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `neurologic compromise` -> `nerve harm` | replace | attributed | 2.183 | 2.567 | 0.770 | 0.868 | 0.054 | - |

**edit `neurologic compromise` -> `nerve harm`**

- status: `attributed`
- log p full -1.0632, empty -3.2467
- masks scored: 66/66 (+2 top-k)
- ranked sources:
    - `+1.157` [readme] NEUROLOGIC: Having to do with the nerves in the body, brain, or spinal cord.
    - `+1.102` [readme] Neurologic: Having to do with nerves in the body, brain, or spinal cord.
    - `+0.394` [nih] neurologic: Having to do with nerves or the nervous system.
    - `-0.179` [wiktionary] compromise: Compromise is the act making this type of agreement.

- rationale: You explain, to a patient, why one phrase in a medical sentence was replaced with another.
- audit: coverage 0.0, grounding_error=False, omission=True, source_ok=True, passage_ok=True

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

**output:** Thereafter, the local anesthesia was injected into the area around the tumor.

| metric | value |
|---|---:|
| bertscore_f1 | 0.845 |
| coleman_liau | 12.67 |
| coleman_liau_drop | 0.00 |
| copy_jargon_rate | 1.000 |
| critical_error | 0.000 |
| fkgl | 13.67 |
| fkgl_drop | 0.00 |
| fre | 18.4 |
| fre_gain | 0.0 |
| human_edit_recall | 0.000 |
| length_ratio | 1.00 |
| n_words | 12.0 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.994 |
| replacement_f1 | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 26.80 |
| smog | 14.55 |
| smog_drop | 0.00 |

### Stage 4 - arm `termonly`

**output:** After that, a numbing medicine was put into the area around the growth.

| metric | value |
|---|---:|
| bertscore_f1 | 0.664 |
| coleman_liau | 7.35 |
| coleman_liau_drop | 5.31 |
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
| nli_completeness | 0.651 |
| nli_faithfulness | 0.982 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.200 |
| sari | 40.82 |
| smog | 11.21 |
| smog_drop | 3.35 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `Thereafter` -> `After that` | replace | - | - | - | - | - | - | - |
| `local anesthesia` -> `numbing medicine` | replace | - | - | - | - | - | - | - |
| `tumor` -> `growth` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** After that, the numbing drug was put into the area around the growth.

| metric | value |
|---|---:|
| bertscore_f1 | 0.700 |
| coleman_liau | 6.46 |
| coleman_liau_drop | 6.21 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 6.73 |
| fkgl_drop | 6.95 |
| fre | 70.0 |
| fre_gain | 51.6 |
| human_edit_recall | 1.000 |
| length_ratio | 1.08 |
| n_words | 13.0 |
| nli_completeness | 0.829 |
| nli_faithfulness | 0.985 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.200 |
| sari | 42.76 |
| smog | 8.84 |
| smog_drop | 5.71 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `local anesthesia` -> `numbing drug` | replace | attributed | 5.373 | 6.340 | 0.936 | 0.871 | 1.455 | - |
| `tumor` -> `growth` | replace | attributed | 0.080 | 1.509 | 0.656 | 0.885 | 0.184 | - |

**edit `local anesthesia` -> `numbing drug`**

- status: `attributed`
- log p full -0.4769, empty -5.8501
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+2.106` [readme] local anesthesia: A drug that numbs a specific part of your body without affecting the rest.
    - `+0.651` [iowa] LOCAL ANESTHESIA: creation of insensitivity to pain in a small, local area of the body, usually by injection o
    - `+0.612` [michigan] local anesthesia: A drug that causes only in the area of the body where the drug is put, as when a tooth is pu
    - `+0.099` [wiktionary] tumor: A tumor is an abnormal growth of tissue in a human or animal.
    - `+0.080` [justplainclear] tumor: Growth or lump

- rationale: The source describes local anesthesia as a drug that numbs a specific part of your body without affecting the rest, so "numbing drug" keeps that localized numbing idea in plain words. Phrase frequency decreases from Zipf 3.39 to 2.90, while age of acquisition falls from 12.53 to 8.11. Patients can now understand the purpose and scope of the medication without needing the clinical label.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `tumor` -> `growth`**

- status: `attributed`
- log p full -0.0241, empty -0.1046
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+1.403` [michigan] tumor: A growth or lump in your body. It may be cancer, but it also may not be cancer.
    - `+1.219` [thesaurus] tumor: growth, lump
    - `+1.077` [justplainclear] tumor: Growth or lump
    - `+0.469` [wiktionary] tumor: A tumor is an abnormal growth of tissue in a human or animal.
    - `+0.407` [michigan] local anesthesia: A drug that causes only in the area of the body where the drug is put, as when a tooth is pu

- rationale: A tumor is a mass of abnormal tissue that can be benign or malignant, and "growth" keeps that core idea of an abnormal mass in everyday language. Phrase frequency rises from Zipf 3.97 to 5.03, while age of acquisition falls from 10.32 to 6.70. Readers can grasp that something is growing where it should not without needing a medical label.
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

**output:** There is no numbness or odd tingling in the hand or arm.

| metric | value |
|---|---:|
| bertscore_f1 | 0.824 |
| coleman_liau | 3.00 |
| coleman_liau_drop | 2.24 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 3.84 |
| fkgl_drop | -0.12 |
| fre | 88.9 |
| fre_gain | 0.9 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 12.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.854 |
| nli_faithfulness | 0.877 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 66.67 |
| smog | 8.84 |
| smog_drop | 0.00 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `paresthesias` -> `odd tingling` | replace | - | - | - | - | - | - | - |

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

**output:** I do not think she has a clear current abscessed lesion, although there is some drainage.

| metric | value |
|---|---:|
| bertscore_f1 | 0.759 |
| coleman_liau | 8.45 |
| coleman_liau_drop | 1.09 |
| copy_jargon_rate | 1.000 |
| critical_error | 0.000 |
| fkgl | 6.14 |
| fkgl_drop | 1.48 |
| fre | 79.6 |
| fre_gain | 10.6 |
| human_edit_recall | 0.000 |
| length_ratio | 0.94 |
| n_words | 16.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.994 |
| replacement_f1 | 0.000 |
| rewrite_aggressiveness | 1.000 |
| sari | 29.85 |
| severity_preservation | 0.000 |
| smog | 3.13 |
| smog_drop | 5.71 |

### Stage 4 - arm `termonly`

**output:** I do not think she has an obvious current pocket of pus, although there is some fluid coming out.

| metric | value |
|---|---:|
| bertscore_f1 | 0.829 |
| coleman_liau | 6.15 |
| coleman_liau_drop | 3.39 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.667 |
| fkgl | 7.97 |
| fkgl_drop | -0.35 |
| fre | 71.8 |
| fre_gain | 2.8 |
| human_edit_recall | 1.000 |
| length_ratio | 1.12 |
| n_words | 19.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.984 |
| nli_faithfulness | 0.964 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 68.61 |
| severity_preservation | 1.000 |
| smog | 8.84 |
| smog_drop | 0.00 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `abscessed lesion` -> `pocket of pus` | replace | - | - | - | - | - | - | - |
| `drainage` -> `fluid coming out` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** I do not think she has an obvious current wound or sore, although there is some fluid leaking out.

| metric | value |
|---|---:|
| bertscore_f1 | 0.760 |
| coleman_liau | 6.45 |
| coleman_liau_drop | 3.08 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.667 |
| fkgl | 7.35 |
| fkgl_drop | 0.27 |
| fre | 76.2 |
| fre_gain | 7.2 |
| human_edit_recall | 1.000 |
| length_ratio | 1.12 |
| n_words | 19.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.988 |
| nli_faithfulness | 0.978 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 57.08 |
| severity_preservation | 1.000 |
| smog | 8.84 |
| smog_drop | 0.00 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `abscessed lesion` -> `wound or sore` | replace | attributed | 9.830 | 10.021 | 0.905 | 0.926 | 3.192 | - |
| `drainage` -> `fluid leaking out` | replace | attributed | 1.995 | 3.723 | 0.795 | 0.845 | 5.819 | - |

**edit `abscessed lesion` -> `wound or sore`**

- status: `attributed`
- log p full -1.7472, empty -11.5771
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+5.952` [justplainclear] lesion: Wound; sore; infected patch of skin
    - `+2.760` [iowa] LESION: wound or injury; a diseased patch of skin
    - `+0.682` [wiktionary] drainage: To use a drainage is engage in the action or process of draining something.
    - `+0.667` [michigan] lesion: A sore or any part of your sking that looks different from the rest.
    - `+0.429` [readme] LESION: A lesion is a type of damage or change in tissue caused by disease or injury.

- rationale: The source describes an abscessed lesion as a wound, sore, or infected patch of skin, so "wound or sore" keeps the core idea of a localized, infected skin problem in plain words. Phrase frequency rises from Zipf 1.60 to 3.80, while age of acquisition falls from 12.82 to 7.52, and syllables drop from 4 to 3. Readers can now picture the problem as a familiar skin injury rather than a technical lesion term.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `drainage` -> `fluid leaking out`**

- status: `attributed`
- log p full -0.1710, empty -2.1657
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+6.855` [readme] drainage: When any fluid is leaking out of a body part.
    - `+1.036` [michigan] lesion: A sore or any part of your sking that looks different from the rest.
    - `+0.031` [readme] lesion: It's any damage or abnormal change in tissue from disease or injury.

- rationale: The readme describes drainage as when any fluid is leaking out of a body part, so "fluid leaking out" keeps that same idea in plain words. Phrase frequency decreases from Zipf 3.77 to 3.58, while age of acquisition falls from 10.84 to 7.94. Readers can picture the process without needing the clinical label.
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

**output:** At this time, the team would give fluids through a vein and then check again.

| metric | value |
|---|---:|
| bertscore_f1 | 0.655 |
| coleman_liau | 5.81 |
| coleman_liau_drop | 6.28 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 3.63 |
| fkgl_drop | 5.45 |
| fre | 95.7 |
| fre_gain | 46.2 |
| human_edit_recall | 1.000 |
| length_ratio | 1.15 |
| n_words | 15.0 |
| nli_completeness | 0.767 |
| nli_faithfulness | 0.796 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 31.98 |
| smog | 3.13 |
| smog_drop | 9.89 |

### Stage 4 - arm `termonly`

**output:** At this time, we would give fluids by vein to replace lost water and then check again.

| metric | value |
|---|---:|
| bertscore_f1 | 0.627 |
| coleman_liau | 5.66 |
| coleman_liau_drop | 6.43 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 5.62 |
| fkgl_drop | 3.47 |
| fre | 85.1 |
| fre_gain | 35.5 |
| human_edit_recall | 1.000 |
| length_ratio | 1.31 |
| n_words | 17.0 |
| nli_completeness | 0.957 |
| nli_faithfulness | 0.800 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 43.37 |
| smog | 3.13 |
| smog_drop | 9.89 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `rehydrate` -> `give fluids by vein to replace lost water` | replace | - | - | - | - | - | - | - |
| `reassess` -> `check again` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** At this time, we would give fluids by vein to add water back and check again.

| metric | value |
|---|---:|
| bertscore_f1 | 0.631 |
| coleman_liau | 4.10 |
| coleman_liau_drop | 7.99 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 4.66 |
| fkgl_drop | 4.42 |
| fre | 90.1 |
| fre_gain | 40.6 |
| human_edit_recall | 1.000 |
| length_ratio | 1.23 |
| n_words | 16.0 |
| nli_completeness | 0.942 |
| nli_faithfulness | 0.889 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 43.48 |
| smog | 3.13 |
| smog_drop | 9.89 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `rehydrate` -> `give fluids by vein to add water back` | replace | attributed | -0.528 | -0.571 | - | 0.732 | 0.203 | - |
| `reassess` -> `check again` | replace | attributed | -0.699 | -1.644 | - | 0.976 | 0.863 | - |

**edit `rehydrate` -> `give fluids by vein to add water back`**

- status: `attributed`
- log p full -2.8533, empty -2.3255
- masks scored: 10/10 (+2 top-k)
- ranked sources:
    - `+0.203` [wiktionary] rehydrate: If you rehydrate something, you supply it with water to make it moist or wet again.
    - `-0.280` [readme] intravenous fluid: Fluids that go straight into a vein through a needle.

- rationale: You explain, to a patient, why one phrase in a medical sentence was replaced with another.
- audit: coverage 0.0, grounding_error=False, omission=True, source_ok=True, passage_ok=True

**edit `reassess` -> `check again`**

- status: `attributed`
- log p full -0.9770, empty -0.2776
- masks scored: 10/10 (+2 top-k)
- ranked sources:
    - `+0.863` [wiktionary] rehydrate: If you rehydrate something, you supply it with water to make it moist or wet again.
    - `-2.031` [wiktionary] reassess: If you reassess a person, idea, skill, process, etc., you judge or measure them again.

- rationale: You explain, to a patient, why one phrase in a medical sentence was replaced with another.
- audit: coverage 0.0, grounding_error=False, omission=True, source_ok=True, passage_ok=True

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

**output:** Findings fit with acute appendicitis.

| metric | value |
|---|---:|
| bertscore_f1 | 0.582 |
| coleman_liau | 15.40 |
| coleman_liau_drop | 4.47 |
| copy_jargon_rate | 1.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 9.96 |
| fkgl_drop | 4.32 |
| fre | 32.6 |
| fre_gain | 29.2 |
| human_edit_recall | 0.000 |
| length_ratio | 0.56 |
| n_words | 5.0 |
| nli_completeness | 0.968 |
| nli_faithfulness | 0.983 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 11.11 |
| smog | 8.84 |
| smog_drop | 2.37 |
| temporality_preservation | 1.000 |
| uncertainty_preservation | 0.000 |

### Stage 4 - arm `termonly`

**output:** The results match a sudden belly infection near the appendix.

| metric | value |
|---|---:|
| bertscore_f1 | 0.466 |
| coleman_liau | 10.82 |
| coleman_liau_drop | 9.05 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.286 |
| fkgl | 8.37 |
| fkgl_drop | 5.91 |
| fre | 52.9 |
| fre_gain | 49.5 |
| human_edit_recall | 1.000 |
| length_ratio | 1.11 |
| n_words | 10.0 |
| nli_completeness | 0.898 |
| nli_faithfulness | 0.599 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 11.76 |
| smog | 11.21 |
| smog_drop | 0.00 |
| temporality_preservation | 0.000 |
| uncertainty_preservation | 0.000 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `compatible with` -> `match` | replace | - | - | - | - | - | - | - |
| `acute appendicitis` -> `sudden belly infection near the appendix` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** The test results fit a sudden, short-term appendix swelling.

| metric | value |
|---|---:|
| bertscore_f1 | 0.420 |
| coleman_liau | 12.49 |
| coleman_liau_drop | 7.38 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.286 |
| fkgl | 7.59 |
| fkgl_drop | 6.70 |
| fre | 56.7 |
| fre_gain | 53.4 |
| human_edit_recall | 1.000 |
| length_ratio | 1.11 |
| n_words | 10.0 |
| nli_completeness | 0.965 |
| nli_faithfulness | 0.943 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 10.30 |
| smog | 8.84 |
| smog_drop | 2.37 |
| temporality_preservation | 0.000 |
| uncertainty_preservation | 0.000 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `compatible with` -> `fit` | replace | attributed | 0.110 | 0.171 | 0.081 | 0.776 | 0.106 | - |
| `acute appendicitis` -> `sudden, short-term appendix swelling` | replace | attributed | 11.490 | 11.530 | 0.883 | 0.911 | 0.870 | - |

**edit `compatible with` -> `fit`**

- status: `attributed`
- log p full -0.9726, empty -1.0826
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.198` [wiktionary] compatible: Things or people are compatible when they can work and communicate with each other without problem
    - `+0.091` [thesaurus] acute: sudden start, short term, quick
    - `+0.004` [justplainclear] acute: Sudden start, doesn't last long
    - `+0.003` [readme] appendicitis: Appendicitis is when your appendix gets swollen and inflamed, typically causing stomach pain.

- rationale: The phrase "compatible with" means that something can exist together with or be consistent with something else, and "fit" carries that same sense of matching or being consistent in plain words. Phrase frequency rises from Zipf 3.97 to 4.95, while age of acquisition falls from 10.16 to 5.74, and syllables drop from 5 to 1. Readers can now see the intended match or consistency without the formal phrasing.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `acute appendicitis` -> `sudden, short-term appendix swelling`**

- status: `attributed`
- log p full -3.2369, empty -14.7271
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+3.371` [thesaurus] acute: sudden start, short term, quick
    - `+2.501` [readme] appendicitis: Appendicitis is when your appendix gets swollen and inflamed, typically causing stomach pain.
    - `+1.671` [justplainclear] acute: Sudden start, doesn't last long
    - `+1.143` [michigan] acute: An illness or symptom that begins suddenly or lasts a short time. It can also be an intense flare-up of
    - `+0.557` [nih] acute: Symptoms or signs that begin and worsen quickly; not chronic.

- rationale: The source describes acute appendicitis as a sudden start, short term, quick condition, so "sudden, short-term appendix swelling" keeps that onset and duration in plain words. Phrase frequency increases from Zipf 2.74 to 3.25, while age of acquisition falls from 12.00 to 10.56. Patients can understand the basic heart-rhythm problem without first knowing the diagnostic name.
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

**output:** She says she has not lost weight, but she says her appetite has gone down and she has felt very tired all over for the past 3 to 4 months.

| metric | value |
|---|---:|
| bertscore_f1 | 0.562 |
| coleman_liau | 3.90 |
| coleman_liau_drop | 12.34 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.429 |
| fkgl | 9.88 |
| fkgl_drop | 0.60 |
| fre | 77.7 |
| fre_gain | 27.4 |
| human_edit_recall | 1.000 |
| length_ratio | 1.67 |
| n_words | 30.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.995 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.143 |
| sari | 34.75 |
| smog | 8.84 |
| smog_drop | 4.18 |
| temporality_preservation | 1.000 |

### Stage 4 - arm `termonly`

**output:** She says no to weight loss, but said she has had less hunger and more whole-body tiredness for the past 3-4 months.

| metric | value |
|---|---:|
| bertscore_f1 | 0.669 |
| coleman_liau | 6.58 |
| coleman_liau_drop | 9.65 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.125 |
| fkgl | 6.94 |
| fkgl_drop | 3.54 |
| fre | 84.5 |
| fre_gain | 34.3 |
| human_edit_recall | 1.000 |
| length_ratio | 1.33 |
| n_words | 24.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.994 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 51.40 |
| smog | 8.84 |
| smog_drop | 4.18 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `decreased appetite` -> `less hunger` | replace | - | - | - | - | - | - | - |
| `generalized fatigue` -> `whole-body tiredness` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** She says no to weight loss, but said she has less want to eat food and more whole-body tired for the past 3-4 months.

| metric | value |
|---|---:|
| bertscore_f1 | 0.546 |
| coleman_liau | 4.72 |
| coleman_liau_drop | 11.52 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.250 |
| fkgl | 6.55 |
| fkgl_drop | 3.92 |
| fre | 90.8 |
| fre_gain | 40.6 |
| human_edit_recall | 1.000 |
| length_ratio | 1.44 |
| n_words | 26.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.995 |
| nli_faithfulness | 0.994 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 48.12 |
| smog | 3.13 |
| smog_drop | 9.89 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 4 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `denies` -> `no to` | replace | attributed | -0.601 | -1.330 | 0.489 | 0.682 | 0.218 | - |
| `acknowledged` -> `said she has` | replace | attributed | -1.507 | -2.041 | 0.824 | 0.917 | 0.138 | - |
| `decreased appetite` -> `less want to eat food` | replace | attributed | 19.117 | 19.256 | 0.826 | 0.857 | 11.298 | - |
| `generalized fatigue` -> `whole-body tired` | replace | attributed | -0.000 | -0.001 | 0.364 | 0.562 | 0.094 | - |

**edit `denies` -> `no to`**

- status: `attributed`
- log p full -0.9521, empty -0.3512
- masks scored: 66/66 (+8 top-k)
- ranked sources:
    - `+0.218` [wiktionary] appetite: When you have appetite, you feel hungry and would like to eat some food.

- rationale: The original term "denies" means the patient says no to or rejects a symptom or history item, and "no to" carries that same meaning in plain words. Phrase frequency increases from Zipf 3.73 to 6.32, while syllable count stays the same from 2 to 2. Patients can read the chart note and immediately see which items were not reported.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `acknowledged` -> `said she has`**

- status: `attributed`
- log p full -2.2506, empty -0.7433
- masks scored: 66/66 (+8 top-k)
- ranked sources:
    - `+0.209` [nih] appetite: A desire to satisfy a physical or mental need, such as for food, sex, or adventure.
    - `+0.070` [nih] fatigue: A condition marked by extreme tiredness and inability to function due to lack of energy. Fatigue may 
    - `+0.033` [michigan] fatigue: tired, weak feeling of the whole body, feeling tired all over

- rationale: The original term "acknowledged" means recognized or accepted as true, and "said she has" conveys that the person stated the condition in plain words. Phrase frequency increases from Zipf 4.08 to 5.71, while syllable count stays the same at 3. Readers can now see the statement as a direct report rather than a formal admission.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `decreased appetite` -> `less want to eat food`**

- status: `attributed`
- log p full -2.0409, empty -21.1582
- masks scored: 66/66 (+8 top-k)
- ranked sources:
    - `+13.937` [readme] appetite: Wanting to eat food.
    - `+2.639` [wiktionary] appetite: When you have appetite, you feel hungry and would like to eat some food.
    - `+0.713` [readme] fatigue: Feeling exhausted and lacking energy.
    - `+0.427` [readme] Generalized: Generalized means not focusing on one specific area.

- rationale: The source describes decreased appetite as wanting to eat food, so "less want to eat food" keeps that core idea in plain words. Phrase frequency rises from Zipf 3.63 to 4.81, while age of acquisition falls from 8.83 to 4.16. Patients can now grasp the change in hunger without needing the clinical label.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `generalized fatigue` -> `whole-body tired`**

- status: `attributed`
- log p full -0.4192, empty -0.4188
- masks scored: 66/66 (+8 top-k)
- ranked sources:
    - `+0.251` [wiktionary] fatigue: Fatigue is the extreme tiredness which is the result of having mental or physical exertion or illness
    - `+0.157` [readme] appetite: Wanting to eat food.
    - `+0.132` [nih] fatigue: A condition marked by extreme tiredness and inability to function due to lack of energy. Fatigue may 
    - `+0.111` [wiktionary] appetite: When you have appetite, you feel hungry and would like to eat some food.
    - `+0.105` [readme] generalized: Not specific, covers a broad range.

- rationale: The original term means tiredness that affects the whole body rather than a single part, and "whole-body tired" keeps that broad, systemic sense in plain words. Phrase frequency rises from Zipf 3.29 to 4.57, while age of acquisition falls from 11.83 to 4.62. Readers can grasp the extent of the tiredness without needing a medical label.
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

**output:** Consider thyroid removal is being thought about.

| metric | value |
|---|---:|
| bertscore_f1 | 0.275 |
| coleman_liau | 13.94 |
| coleman_liau_drop | 14.22 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.286 |
| fkgl | 10.74 |
| fkgl_drop | 11.02 |
| fre | 30.5 |
| fre_gain | 82.6 |
| human_edit_recall | 1.000 |
| length_ratio | 0.78 |
| n_words | 7.0 |
| nli_completeness | 0.904 |
| nli_faithfulness | 0.969 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 22.67 |
| smog | 11.21 |
| smog_drop | 1.82 |
| uncertainty_preservation | 0.000 |

### Stage 4 - arm `termonly`

**output:** Consideration is given to finishing the removal of the thyroid.

| metric | value |
|---|---:|
| bertscore_f1 | 0.592 |
| coleman_liau | 11.98 |
| coleman_liau_drop | 16.18 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.250 |
| fkgl | 11.91 |
| fkgl_drop | 9.85 |
| fre | 27.5 |
| fre_gain | 79.5 |
| human_edit_recall | 1.000 |
| length_ratio | 1.11 |
| n_words | 10.0 |
| nli_completeness | 0.985 |
| nli_faithfulness | 0.994 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 49.40 |
| smog | 13.02 |
| smog_drop | 0.00 |
| uncertainty_preservation | 1.000 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `completion thyroidectomy` -> `finishing the removal of the thyroid` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** The team is thinking about finishing the surgery to take out the thyroid gland.

| metric | value |
|---|---:|
| bertscore_f1 | 0.339 |
| coleman_liau | 9.01 |
| coleman_liau_drop | 19.15 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.333 |
| fkgl | 7.57 |
| fkgl_drop | 14.19 |
| fre | 65.7 |
| fre_gain | 117.8 |
| human_edit_recall | 1.000 |
| length_ratio | 1.56 |
| n_words | 14.0 |
| nli_completeness | 0.981 |
| nli_faithfulness | 0.785 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 29.23 |
| smog | 11.21 |
| smog_drop | 1.82 |
| uncertainty_preservation | 0.000 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `Consideration given to` -> `finishing the surgery to take out the thyroid gland` | replace | attributed | 10.887 | 11.146 | 0.916 | 0.887 | 0.820 | - |

**edit `Consideration given to` -> `finishing the surgery to take out the thyroid gland`**

- status: `attributed`
- log p full -1.4773, empty -12.3642
- masks scored: 66/66 (+2 top-k)
- ranked sources:
    - `+2.592` [readme] Thyroidectomy: A thyroidectomy is surgery to take out the thyroid gland.
    - `+1.772` [readme] thyroidectomy: Surgery to remove the thyroid gland.
    - `+1.094` [thesaurus] completion: end, finish
    - `+0.440` [wiktionary] to: To shows where something goes, the goal of movement.
    - `+0.356` [wiktionary] completion: Completion is the action from the verb complete.

- rationale: The original term means the attention or thought paid to something, and the replacement restates that as the specific action of finishing the surgery to take out the thyroid gland. Phrase frequency decreases from Zipf 4.25 to 3.10, while age of acquisition rises from 9.50 to 13.83. Readers can now see the concrete surgical step that was being referred to.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

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

**output:** She says she had a nosebleed a few days ago. It needed packing in the nose, and it is better now.

| metric | value |
|---|---:|
| bertscore_f1 | 0.670 |
| coleman_liau | 1.82 |
| coleman_liau_drop | 8.60 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.400 |
| fkgl | 3.11 |
| fkgl_drop | 7.34 |
| fre | 91.4 |
| fre_gain | 37.5 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 21.0 |
| nli_completeness | 0.020 |
| nli_faithfulness | 0.887 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 29.71 |
| smog | 3.13 |
| smog_drop | 8.08 |
| temporality_preservation | 1.000 |

### Stage 4 - arm `termonly`

**output:** She notes that she had a nose bleed a few days ago, needing a nose plug and fortunately that had gone away now.

| metric | value |
|---|---:|
| bertscore_f1 | 0.883 |
| coleman_liau | 4.85 |
| coleman_liau_drop | 5.57 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.333 |
| fkgl | 8.26 |
| fkgl_drop | 2.19 |
| fre | 76.8 |
| fre_gain | 22.9 |
| human_edit_recall | 1.000 |
| length_ratio | 1.10 |
| n_words | 23.0 |
| nli_completeness | 0.860 |
| nli_faithfulness | 0.928 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 60.29 |
| smog | 8.84 |
| smog_drop | 2.37 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 4 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `epistaxis` -> `a nose bleed` | replace | - | - | - | - | - | - | - |
| `requiring` -> `needing` | replace | - | - | - | - | - | - | - |
| `nasal packing` -> `a nose plug` | replace | - | - | - | - | - | - | - |
| `resolved` -> `gone away` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** She notes that she had a nosebleed a few days ago, needing something put into her nose to help it heal and fortunately that had been brought to a successful solution now.

| metric | value |
|---|---:|
| bertscore_f1 | 0.700 |
| coleman_liau | 8.11 |
| coleman_liau_drop | 2.31 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.833 |
| fkgl | 13.12 |
| fkgl_drop | -2.66 |
| fre | 58.0 |
| fre_gain | 4.1 |
| human_edit_recall | 1.000 |
| length_ratio | 1.52 |
| n_words | 32.0 |
| nli_completeness | 0.801 |
| nli_faithfulness | 0.921 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 47.18 |
| smog | 13.02 |
| smog_drop | -1.82 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 4 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `epistaxis` -> `a nosebleed` | replace | attributed | 1.904 | 4.647 | 0.718 | 0.935 | 0.313 | - |
| `requiring` -> `needing` | replace | attributed | -0.044 | -0.435 | 0.428 | 0.834 | 0.433 | - |
| `nasal packing` -> `something put into her nose to help it heal` | replace | attributed | 26.461 | 26.627 | 0.765 | 0.955 | 16.488 | - |
| `resolved` -> `been brought to a successful solution` | replace | attributed | 28.729 | 30.191 | 0.672 | 0.846 | 20.552 | - |

**edit `epistaxis` -> `a nosebleed`**

- status: `attributed`
- log p full -0.0569, empty -1.9610
- masks scored: 66/66 (+7 top-k)
- ranked sources:
    - `+3.719` [readme] Epistaxis: A nosebleed.
    - `+3.406` [readme] EPISTAXIS: EPISTAXIS: It's a nosebleed.
    - `+1.224` [wiktionary] resolved: When a problem is resolved, it has been brought to a successful solution.
    - `+1.120` [wiktionary] requiring: If you require something, you need it.
    - `+0.939` [wiktionary] packing: When you pack something, you put it in a container to carry with you.

- rationale: The source describes epistaxis as a nosebleed, so "a nosebleed" keeps the meaning in plain words. Phrase frequency increases from Zipf 1.60 to 2.51. Patients can understand the basic bleeding problem without first knowing the diagnostic name.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `requiring` -> `needing`**

- status: `attributed`
- log p full -0.1291, empty -0.0854
- masks scored: 66/66 (+7 top-k)
- ranked sources:
    - `+0.594` [readme] Epistaxis: A nosebleed.
    - `+0.161` [readme] EPISTAXIS: EPISTAXIS: It's a nosebleed.
    - `+0.119` [readme] Nasal: Nasal means having to do with the nose.
    - `+0.099` [readme] nasal: It's all about your nose when we talk about "nasal."
    - `+0.052` [wiktionary] packing: You put packing around an object to protect it.

- rationale: The original term means that something is necessary or obligatory, and the replacement carries that meaning in plain words. Phrase frequency decreases from Zipf 4.14 to 4.02, while syllable count falls from 4 to 2. Readers can now see the requirement expressed with a shorter, more familiar word.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `nasal packing` -> `something put into her nose to help it heal`**

- status: `attributed`
- log p full -1.8794, empty -28.3407
- masks scored: 66/66 (+7 top-k)
- ranked sources:
    - `+18.664` [readme] packing: Putting something into a wound to help it heal.
    - `+2.177` [readme] EPISTAXIS: EPISTAXIS: It's a nosebleed.
    - `+0.239` [readme] Nasal: Nasal means having to do with the nose.
    - `+0.222` [readme] nasal: It's all about your nose when we talk about "nasal."
    - `+0.130` [wiktionary] epistaxis: Epistaxis is bleeding from the nose.

- rationale: The readme describes nasal packing as putting something into a wound to help it heal, so "something put into her nose to help it heal" keeps that idea in plain words. Phrase frequency rises from Zipf 3.39 to 3.94, while age of acquisition falls from 8.75 to 7.47. Readers can picture the procedure and its purpose without needing the clinical label.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `resolved` -> `been brought to a successful solution`**

- status: `attributed`
- log p full -0.2637, empty -28.9928
- masks scored: 66/66 (+7 top-k)
- ranked sources:
    - `+24.287` [wiktionary] resolved: When a problem is resolved, it has been brought to a successful solution.
    - `+3.735` [wiktionary] resolved: To resolve means to create a solution for a problem.
    - `+2.449` [readme] nasal: It's all about your nose when we talk about "nasal."
    - `+1.765` [wiktionary] packing: When you pack something, you put it in a container to carry with you.
    - `+1.543` [readme] packing: Putting something into a wound to help it heal.

- rationale: The source describes resolved as when a problem has been brought to a successful solution, so "been brought to a successful solution" keeps that sense of a problem ending with a successful outcome in plain words. Phrase frequency increases from Zipf 4.10 to 4.48, while syllables increase from 2 to 10. Readers can see the intended outcome without needing the shorthand term.
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

**output:** I also explained to the patient about a calm, sleepy medicine that lets them stay awake.

| metric | value |
|---|---:|
| bertscore_f1 | 0.599 |
| coleman_liau | 8.09 |
| coleman_liau_drop | 3.76 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 8.35 |
| fkgl_drop | 0.55 |
| fre | 63.7 |
| fre_gain | 16.4 |
| human_edit_recall | 1.000 |
| length_ratio | 1.78 |
| n_words | 16.0 |
| nli_completeness | 0.384 |
| nli_faithfulness | 0.175 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 63.61 |
| smog | 8.84 |
| smog_drop | 0.00 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `conscious sedation` -> `a calm, sleepy medicine that lets them stay awake` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** I also told the patient about light sleep medicine for a procedure.

| metric | value |
|---|---:|
| bertscore_f1 | 0.638 |
| coleman_liau | 8.32 |
| coleman_liau_drop | 3.53 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 7.77 |
| fkgl_drop | 1.12 |
| fre | 60.7 |
| fre_gain | 13.4 |
| human_edit_recall | 1.000 |
| length_ratio | 1.33 |
| n_words | 12.0 |
| nli_completeness | 0.472 |
| nli_faithfulness | 0.214 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 25.72 |
| smog | 11.21 |
| smog_drop | -2.37 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `conscious sedation` -> `light sleep medicine for a procedure` | replace | attributed | 3.394 | 3.443 | - | 1.000 | 4.659 | - |

**edit `conscious sedation` -> `light sleep medicine for a procedure`**

- status: `attributed`
- log p full -2.9996, empty -6.3936
- masks scored: 6/6 (+1 top-k)
- ranked sources:
    - `+3.868` [readme] conscious sedation: Medication given to a patient to make them lightly sedated and forgetful during a procedur
    - `-0.790` [nih] conscious sedation: A level of sedation in which a person is asleep but wakes when spoken to or touched. Consc

- rationale: You explain, to a patient, why one phrase in a medical sentence was replaced with another.
- audit: coverage 0.0, grounding_error=False, omission=True, source_ok=True, passage_ok=True

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

**output:** Palpation of her right knee reveals no crepitus.

| metric | value |
|---|---:|
| bertscore_f1 | 0.588 |
| coleman_liau | 9.50 |
| coleman_liau_drop | 0.00 |
| copy_jargon_rate | 1.000 |
| critical_error | 0.000 |
| fkgl | 5.23 |
| fkgl_drop | 0.00 |
| fre | 71.8 |
| fre_gain | 0.0 |
| human_edit_recall | 0.000 |
| laterality_preservation | 1.000 |
| length_ratio | 0.89 |
| n_words | 8.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.994 |
| replacement_f1 | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 27.00 |
| smog | 8.84 |
| smog_drop | 0.00 |

### Stage 4 - arm `termonly`

**output:** Feeling her right knee shows no crackling.

| metric | value |
|---|---:|
| bertscore_f1 | 0.695 |
| coleman_liau | 8.97 |
| coleman_liau_drop | 0.53 |
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
| nli_completeness | 0.943 |
| nli_faithfulness | 0.953 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 32.26 |
| smog | 3.13 |
| smog_drop | 5.71 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `crepitus` -> `crackling` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Feeling her right knee with her hands shows no crackling sound.

| metric | value |
|---|---:|
| bertscore_f1 | 0.590 |
| coleman_liau | 8.93 |
| coleman_liau_drop | 0.57 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 2.65 |
| fkgl_drop | 2.58 |
| fre | 95.7 |
| fre_gain | 23.9 |
| human_edit_recall | 1.000 |
| laterality_preservation | 1.000 |
| length_ratio | 1.22 |
| n_words | 11.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.913 |
| nli_faithfulness | 0.621 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 31.01 |
| smog | 3.13 |
| smog_drop | 5.71 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `crepitus` -> `crackling sound` | replace | attributed | -0.298 | -0.430 | - | 0.230 | 0.000 | - |

**edit `crepitus` -> `crackling sound`**

- status: `attributed`
- log p full -1.3364, empty -1.0387
- masks scored: 34/34 (+2 top-k)
- ranked sources:
    - `-0.026` [dictionary] Crepitus (n.): The noise produced by a sudden discharge of wind from the bowels.

- rationale: The original term crepitus refers to a fine crackling or grating sensation that can be heard or felt, and the replacement crackling sound keeps that audible quality in everyday language. Phrase frequency rises from Zipf 1.39 to 2.91, while syllable count changes from 2 to 3. Readers can now picture the sound without needing a medical label.
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

**output:** She stepped on ideas, concerns and expectations the evening prior and twisted her ankle.

| metric | value |
|---|---:|
| bertscore_f1 | 0.631 |
| coleman_liau | 12.33 |
| coleman_liau_drop | 0.00 |
| critical_error | 0.000 |
| fkgl | 10.10 |
| fkgl_drop | 0.00 |
| fre | 47.6 |
| fre_gain | 0.0 |
| length_ratio | 1.27 |
| n_words | 14.0 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.994 |
| rewrite_aggressiveness | 0.000 |
| sari | 23.68 |
| smog | 11.21 |
| smog_drop | 0.00 |
| temporality_preservation | 1.000 |

### Stage 4 - arm `termonly`

**output:** She stepped on ideas, concerns and expectations last night and twisted her ankle.

| metric | value |
|---|---:|
| bertscore_f1 | 0.479 |
| coleman_liau | 11.82 |
| coleman_liau_drop | 0.51 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 8.54 |
| fkgl_drop | 1.56 |
| fre | 57.0 |
| fre_gain | 9.4 |
| length_ratio | 1.18 |
| n_words | 13.0 |
| nli_completeness | 0.984 |
| nli_faithfulness | 0.994 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 26.24 |
| smog | 11.21 |
| smog_drop | 0.00 |
| temporality_preservation | 0.000 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `the evening prior` -> `last night` | replace | - | - | - | - | - | - | - |

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
| `the evening prior` -> `the night before` | replace | attributed | 0.134 | 0.195 | - | 0.690 | 0.827 | - |

**edit `the evening prior` -> `the night before`**

- status: `attributed`
- log p full -1.0983, empty -1.2324
- masks scored: 10/10 (+2 top-k)
- ranked sources:
    - `+0.940` [wiktionary] prior: If something happens prior to something else, it happens before it.
    - `+0.113` [wiktionary] evening: You use even to focus on the most surprising or unlikely case.
    - `-0.461` [wiktionary] evening: Period from dusk to midnight.

- rationale: The original term refers to the night that comes just before a particular day, and the replacement carries that same timing in plain words. Phrase frequency increases from Zipf 4.55 to 5.44, while age of acquisition falls from 10.63 to 5.45. Readers can now see the time reference immediately without parsing a formal phrase.
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

**output:** The patient's condition gets worse when he or she throws.

| metric | value |
|---|---:|
| bertscore_f1 | 0.371 |
| coleman_liau | 7.92 |
| coleman_liau_drop | 8.44 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.250 |
| fkgl | 3.65 |
| fkgl_drop | 10.49 |
| fre | 86.7 |
| fre_gain | 77.0 |
| human_edit_recall | 1.000 |
| length_ratio | 1.10 |
| n_words | 11.0 |
| nli_completeness | 0.859 |
| nli_faithfulness | 0.988 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.250 |
| sari | 26.21 |
| smog | 8.84 |
| smog_drop | 4.18 |

### Stage 4 - arm `termonly`

**output:** The patient’s condition is made worse by throwing.

| metric | value |
|---|---:|
| bertscore_f1 | 0.549 |
| coleman_liau | 10.23 |
| coleman_liau_drop | 6.13 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.250 |
| fkgl | 5.23 |
| fkgl_drop | 8.91 |
| fre | 71.8 |
| fre_gain | 62.1 |
| human_edit_recall | 1.000 |
| length_ratio | 0.90 |
| n_words | 9.0 |
| nli_completeness | 0.842 |
| nli_faithfulness | 0.993 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 69.10 |
| smog | 8.84 |
| smog_drop | 4.18 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `aggravated` -> `made worse` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** The patient’s condition is made worse by throwing.

| metric | value |
|---|---:|
| bertscore_f1 | 0.549 |
| coleman_liau | 10.23 |
| coleman_liau_drop | 6.13 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.250 |
| fkgl | 5.23 |
| fkgl_drop | 8.91 |
| fre | 71.8 |
| fre_gain | 62.1 |
| human_edit_recall | 1.000 |
| length_ratio | 0.90 |
| n_words | 9.0 |
| nli_completeness | 0.842 |
| nli_faithfulness | 0.993 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 69.10 |
| smog | 8.84 |
| smog_drop | 4.18 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `aggravated` -> `made worse` | replace | attributed | -0.053 | -0.737 | - | 0.858 | 0.021 | - |

**edit `aggravated` -> `made worse`**

- status: `attributed`
- log p full -0.1052, empty -0.0517
- masks scored: 18/18 (+2 top-k)
- ranked sources:
    - `+0.021` [wiktionary] aggravated: To aggravate is to make something worse.
    - `-0.273` [wiktionary] factors: A factor is one of a number of things that causes a result.
    - `-0.474` [wiktionary] modifying: If you modify something, you change it, often only in small ways, and often because you want to use

- rationale: The original term means increased in severity or intensity, and "made worse" carries that same sense of a condition becoming more serious in plain words. Word frequency rises from Zipf 3.47 to 4.85, while syllables fall from 4 to 2. Readers can now see at a glance that the situation has deteriorated without needing a formal medical term.
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

**output:** History of osteoarthritis, osteoporosis, hypothyroidism, allergic rhinitis and kidney stones.

| metric | value |
|---|---:|
| bertscore_f1 | 0.408 |
| coleman_liau | 27.64 |
| coleman_liau_drop | 0.00 |
| copy_jargon_rate | 1.000 |
| critical_error | 0.000 |
| fkgl | 21.35 |
| fkgl_drop | 0.00 |
| fre | -40.2 |
| fre_gain | 0.0 |
| human_edit_recall | 0.000 |
| length_ratio | 0.77 |
| n_words | 10.0 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.994 |
| replacement_f1 | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 11.57 |
| smog | 15.90 |
| smog_drop | 0.00 |
| temporality_preservation | 1.000 |

### Stage 4 - arm `termonly`

**output:** History of joint wear, bone loss, low thyroid, hay fever and kidney stones.

| metric | value |
|---|---:|
| bertscore_f1 | 0.785 |
| coleman_liau | 8.25 |
| coleman_liau_drop | 19.39 |
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
| nli_completeness | 0.918 |
| nli_faithfulness | 0.940 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 73.08 |
| smog | 8.84 |
| smog_drop | 7.06 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 4 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `osteoarthritis` -> `joint wear` | replace | - | - | - | - | - | - | - |
| `osteoporosis` -> `bone loss` | replace | - | - | - | - | - | - | - |
| `hypothyroidism` -> `low thyroid` | replace | - | - | - | - | - | - | - |
| `allergic rhinitis` -> `hay fever` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** History of worn-out joints, weak bones that break easily, low thyroid activity, nose allergy, and hard mineral deposits in the kidneys.

| metric | value |
|---|---:|
| bertscore_f1 | 0.441 |
| coleman_liau | 12.90 |
| coleman_liau_drop | 14.74 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 12.83 |
| fkgl_drop | 8.52 |
| fre | 40.5 |
| fre_gain | 80.7 |
| human_edit_recall | 1.000 |
| length_ratio | 1.69 |
| n_words | 22.0 |
| nli_completeness | 0.806 |
| nli_faithfulness | 0.751 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 38.86 |
| smog | 17.12 |
| smog_drop | -1.22 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 5 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `osteoarthritis` -> `worn-out joints` | replace | attributed | 1.446 | 1.765 | 0.775 | 0.747 | 0.129 | - |
| `osteoporosis` -> `weak bones that break easily` | replace | attributed | 6.320 | 6.707 | 0.647 | 0.908 | 0.680 | - |
| `hypothyroidism` -> `low thyroid activity` | replace | attributed | 0.167 | 0.219 | 0.939 | 0.962 | 0.885 | - |
| `allergic rhinitis` -> `nose allergy` | replace | attributed | 0.785 | 2.243 | 0.723 | 0.889 | 0.730 | - |
| `kidney stones` -> `hard mineral deposits in the kidneys` | replace | attributed | 12.612 | 12.875 | 0.785 | 0.945 | 10.062 | - |

**edit `osteoarthritis` -> `worn-out joints`**

- status: `attributed`
- log p full -1.1105, empty -2.5566
- masks scored: 66/66 (+10 top-k)
- ranked sources:
    - `+1.207` [readme] osteoarthritis: Osteoarthritis is a painful joint condition caused by the wearing down of bone tissue, leading
    - `+1.078` [nih] osteoporosis: A condition in which there is a decrease in the amount and thickness of bone tissue. This causes
    - `+0.601` [justplainclear] osteoarthritis: A form of arthritis caused by the wear and tear of joints
    - `+0.452` [readme] Osteoporosis: Osteoporosis is a condition where bones become weak and more prone to fractures.
    - `+0.447` [justplainclear] hypothyroidism: A condition where your thyroid isn't active enough, so you have low hormone levels Hypothyroid

- rationale: The source describes osteoarthritis as a painful joint condition caused by wearing down of bone tissue with inflammation and cartilage loss, so "worn-out joints" keeps the core idea of joints that have worn down in plain words. Phrase frequency increases from Zipf 2.76 to 3.68, while syllables fall from 6 to 2. Patients can grasp the basic joint problem without first knowing the medical name.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `osteoporosis` -> `weak bones that break easily`**

- status: `attributed`
- log p full -1.1355, empty -7.4553
- masks scored: 66/66 (+10 top-k)
- ranked sources:
    - `+1.797` [readme] osteoporosis: Osteoporosis is when bones become weak and prone to breaking because they lose density.
    - `+1.116` [michigan] osteoporosis: When your bones are weak break easily. Also called brittle done disease.
    - `+1.009` [readme] Osteoporosis: Osteoporosis is a condition where bones become weak and more prone to fractures.
    - `+0.717` [readme] osteoarthritis: Osteoarthritis is a painful joint condition caused by the wearing down of bone tissue, leading
    - `+0.509` [justplainclear] allergic rhinitis: Also known as: hay fever A condition where you have an allergic reaction that affects the n

- rationale: The source describes osteoporosis as bones becoming weak and prone to breaking because they lose density, so "weak bones that break easily" keeps that loss-of-strength and fracture risk in plain language. Phrase frequency rises from Zipf 2.99 to 4.05, while age of acquisition falls from 14.29 to 5.58. Patients can grasp why their bones are fragile and what the condition means for everyday safety.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `hypothyroidism` -> `low thyroid activity`**

- status: `attributed`
- log p full -1.3563, empty -1.5234
- masks scored: 66/66 (+10 top-k)
- ranked sources:
    - `+1.249` [justplainclear] hypothyroidism: A condition where your thyroid isn't active enough, so you have low hormone levels Hypothyroid
    - `+0.365` [readme] osteoporosis: Osteoporosis is when bones become weak and prone to breaking because they lose density.
    - `+0.293` [readme] Osteoporosis: Osteoporosis is a condition where bones become weak and more prone to fractures.
    - `+0.092` [readme] kidney stones: Hard mineral deposits in the kidneys causing pain and blockage.
    - `+0.082` [nih] osteoporosis: A condition in which there is a decrease in the amount and thickness of bone tissue. This causes

- rationale: The original term refers to an underactive thyroid gland, and the replacement conveys that same idea as reduced thyroid activity in plain words. Phrase frequency rises from Zipf 2.68 to 3.50, while age of acquisition falls from 15.43 to 13.83. Readers can grasp the condition’s basic meaning without specialized medical vocabulary.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `allergic rhinitis` -> `nose allergy`**

- status: `attributed`
- log p full -0.1526, empty -0.9374
- masks scored: 66/66 (+10 top-k)
- ranked sources:
    - `+1.217` [michigan] allergic rhinitis: Caused by your body's reaction in your nose to mold, pollen, or dust. Also called hay fever
    - `+0.488` [justplainclear] allergic rhinitis: Also known as: hay fever A condition where you have an allergic reaction that affects the n
    - `+0.310` [readme] Osteoporosis: Osteoporosis is a condition where bones become weak and more prone to fractures.
    - `+0.267` [wiktionary] osteoporosis: Osteoporosis is a disease in which the bones become very porous and brittle.
    - `+0.187` [justplainclear] osteoarthritis: A form of arthritis caused by the wear and tear of joints

- rationale: The source describes allergic rhinitis as a nose reaction to mold, pollen, or dust, also called hay fever, so "nose allergy" keeps that nasal allergy idea in plain words. Phrase frequency rises from Zipf 2.37 to 3.55, while age of acquisition falls from 18.07 to 8.11. Readers can grasp the condition as a nose allergy without needing the medical label.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `kidney stones` -> `hard mineral deposits in the kidneys`**

- status: `attributed`
- log p full -1.4653, empty -14.0775
- masks scored: 66/66 (+10 top-k)
- ranked sources:
    - `+12.095` [readme] kidney stones: Hard mineral deposits in the kidneys causing pain and blockage.
    - `+2.033` [nih] osteoporosis: A condition in which there is a decrease in the amount and thickness of bone tissue. This causes
    - `+2.023` [readme] Kidney Stones: Painful mineral deposits that can form in your kidney and block urine flow.
    - `+1.348` [wiktionary] osteoporosis: Osteoporosis is a disease in which the bones become very porous and brittle.
    - `+0.672` [justplainclear] osteoarthritis: A form of arthritis caused by the wear and tear of joints

- rationale: The source describes kidney stones as hard mineral deposits in the kidneys causing pain and blockage, so "hard mineral deposits in the kidneys" keeps that core idea in plain words. Phrase frequency decreases from Zipf 3.85 to 3.28, while age of acquisition falls from 9.33 to 8.67. Readers can picture what is forming in the kidneys and why it matters without needing the medical label.
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

**output:** The ultrasound showed no bleeding inside the head.

| metric | value |
|---|---:|
| bertscore_f1 | 0.774 |
| coleman_liau | 10.95 |
| coleman_liau_drop | 9.62 |
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
| nli_completeness | 0.935 |
| nli_faithfulness | 0.940 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 24.35 |
| smog | 8.84 |
| smog_drop | 5.71 |

### Stage 4 - arm `termonly`

**output:** The ultrasound showed no bleed inside the skull.

| metric | value |
|---|---:|
| bertscore_f1 | 0.704 |
| coleman_liau | 9.50 |
| coleman_liau_drop | 11.07 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| diagnostic_identity_preservation | 1.000 |
| fkgl | 3.76 |
| fkgl_drop | 12.04 |
| fre | 82.4 |
| fre_gain | 88.1 |
| human_edit_recall | 1.000 |
| length_ratio | 0.89 |
| n_words | 8.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.942 |
| nli_faithfulness | 0.942 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 22.26 |
| smog | 8.84 |
| smog_drop | 5.71 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `intracranial hemorrhage` -> `bleed inside the skull` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** The ultrasound showed no bleeding within the brain.

| metric | value |
|---|---:|
| bertscore_f1 | 0.822 |
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
| nli_completeness | 0.934 |
| nli_faithfulness | 0.972 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 28.10 |
| smog | 8.84 |
| smog_drop | 5.71 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `intracranial hemorrhage` -> `within the brain` | replace | attributed | 9.048 | 10.398 | - | 0.800 | 8.395 | - |

**edit `intracranial hemorrhage` -> `within the brain`**

- status: `attributed`
- log p full -0.3000, empty -9.3480
- masks scored: 6/6 (+1 top-k)
- ranked sources:
    - `+9.251` [readme] intracranial hemorrhage: Bleeding within the brain.
    - `+0.856` [readme] INTRACRANIAL HEMORRHAGE: Bleeding inside your brain.

- rationale: You explain, to a patient, why one phrase in a medical sentence was replaced with another.
- audit: coverage 0.0, grounding_error=False, omission=True, source_ok=True, passage_ok=True

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

**output:** He had a laparoscopic appendectomy, and he is tolerating an oral diet.

| metric | value |
|---|---:|
| bertscore_f1 | 0.635 |
| coleman_liau | 9.28 |
| coleman_liau_drop | 3.87 |
| copy_jargon_rate | 0.250 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 13.67 |
| fkgl_drop | 0.98 |
| fre | 18.4 |
| fre_gain | 7.0 |
| human_edit_recall | 0.750 |
| length_ratio | 0.80 |
| n_words | 12.0 |
| nli_completeness | 0.959 |
| nli_faithfulness | 0.994 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 45.46 |
| smog | 13.02 |
| smog_drop | 0.00 |
| temporality_preservation | 0.000 |

### Stage 4 - arm `termonly`

**output:** He had a keyhole appendix removal in the past, and he can keep food down by mouth.

| metric | value |
|---|---:|
| bertscore_f1 | 0.478 |
| coleman_liau | 4.29 |
| coleman_liau_drop | 8.86 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.222 |
| fkgl | 6.31 |
| fkgl_drop | 8.35 |
| fre | 80.1 |
| fre_gain | 68.7 |
| human_edit_recall | 1.000 |
| length_ratio | 1.13 |
| n_words | 17.0 |
| nli_completeness | 0.931 |
| nli_faithfulness | 0.769 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 23.75 |
| smog | 11.21 |
| smog_drop | 1.82 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `laparoscopic appendicectomy` -> `keyhole appendix removal` | replace | - | - | - | - | - | - | - |
| `oral` -> `by mouth` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** He had a keyhole surgery to remove his appendix, and he is able to eat and drink by mouth.

| metric | value |
|---|---:|
| bertscore_f1 | 0.572 |
| coleman_liau | 4.01 |
| coleman_liau_drop | 9.14 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.222 |
| fkgl | 7.97 |
| fkgl_drop | 6.69 |
| fre | 71.8 |
| fre_gain | 60.4 |
| human_edit_recall | 1.000 |
| length_ratio | 1.27 |
| n_words | 19.0 |
| nli_completeness | 0.926 |
| nli_faithfulness | 0.818 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 41.12 |
| smog | 11.21 |
| smog_drop | 1.82 |
| temporality_preservation | 0.000 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `laparoscopic appendicectomy` -> `keyhole surgery to remove his appendix` | replace | attributed | 0.513 | 0.548 | -0.033 | 0.387 | 0.000 | - |
| `oral` -> `by mouth` | replace | attributed | 0.178 | 1.982 | 0.886 | 0.962 | 0.622 | - |

**edit `laparoscopic appendicectomy` -> `keyhole surgery to remove his appendix`**

- status: `attributed`
- log p full -2.4986, empty -3.0116
- masks scored: 66/66 (+4 top-k)
- ranked sources:

- rationale: You explain, to a patient, why one phrase in a medical sentence was replaced with another.
- audit: coverage 0.0, grounding_error=False, omission=True, source_ok=True, passage_ok=True

**edit `oral` -> `by mouth`**

- status: `attributed`
- log p full -0.0317, empty -0.2099
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+1.119` [readme] Oral: Oral means something you take by mouth.
    - `+0.497` [nih] diet: The things a person eats and drinks.
    - `+0.191` [wiktionary] tolerating: If you tolerate something, you put up with it, or allow it.
    - `+0.137` [wiktionary] post: Post is the letters and parcels that you send to other people.
    - `+0.126` [readme] status: The current condition of something.

- rationale: Oral means relating to the mouth, and “by mouth” carries that same meaning in plain words. Phrase frequency increases from Zipf 4.26 to 4.82, while age of acquisition falls from 9.39 to 5.41. Readers can now see the route of administration without needing the Latin-derived adjective.
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

**output:** We think her walking is most likely not being affected by the hydrocephalus.

| metric | value |
|---|---:|
| bertscore_f1 | 0.776 |
| coleman_liau | 10.03 |
| coleman_liau_drop | 0.64 |
| copy_jargon_rate | 1.000 |
| critical_error | 0.000 |
| fkgl | 7.63 |
| fkgl_drop | 0.78 |
| fre | 63.5 |
| fre_gain | 3.8 |
| human_edit_recall | 0.000 |
| length_ratio | 0.72 |
| n_words | 13.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.993 |
| replacement_f1 | 0.000 |
| rewrite_aggressiveness | 1.000 |
| sari | 27.30 |
| smog | 11.21 |
| smog_drop | 0.00 |
| uncertainty_preservation | 1.000 |

### Stage 4 - arm `termonly`

**output:** We believe that her walking is most likely not being affected by a buildup of fluid in the brain.

| metric | value |
|---|---:|
| bertscore_f1 | 0.923 |
| coleman_liau | 6.45 |
| coleman_liau_drop | 4.22 |
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
| nli_completeness | 0.238 |
| nli_faithfulness | 0.782 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 66.30 |
| smog | 8.84 |
| smog_drop | 2.37 |
| uncertainty_preservation | 1.000 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `hydrocephalus` -> `a buildup of fluid in the brain` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** We believe that her walking is most likely not being affected by too much fluid in the brain.

| metric | value |
|---|---:|
| bertscore_f1 | 0.923 |
| coleman_liau | 6.72 |
| coleman_liau_drop | 3.95 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 7.82 |
| fkgl_drop | 0.59 |
| fre | 71.1 |
| fre_gain | 11.4 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 18.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.306 |
| nli_faithfulness | 0.754 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 67.62 |
| smog | 8.84 |
| smog_drop | 2.37 |
| uncertainty_preservation | 1.000 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `hydrocephalus` -> `too much fluid in the brain` | replace | attributed | 1.867 | 2.155 | - | 0.797 | 0.019 | - |

**edit `hydrocephalus` -> `too much fluid in the brain`**

- status: `attributed`
- log p full -1.2640, empty -3.1314
- masks scored: 18/18 (+2 top-k)
- ranked sources:
    - `+2.174` [justplainclear] hydrocephalus: Also known as: water on the brain A condition where there is too much cerebrospinal fluid in yo
    - `+2.155` [nih] hydrocephalus: The abnormal buildup of cerebrospinal fluid in the ventricles of the brain.
    - `+0.859` [readme] hydrocephalus: Swelling of brain due to excess fluid.
    - `-1.996` [readme] HYDROCEPHALUS: When fluid around the brain builds up too much.

- rationale: You explain, to a patient, why one phrase in a medical sentence was replaced with another.
- audit: coverage 0.0, grounding_error=False, omission=True, source_ok=True, passage_ok=True

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

**output:** She said she felt tired, dizzy, and had very hard trouble breathing when she tried to do things.

| metric | value |
|---|---:|
| bertscore_f1 | 0.481 |
| coleman_liau | 7.04 |
| coleman_liau_drop | 10.32 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.300 |
| fkgl | 6.51 |
| fkgl_drop | 5.79 |
| fre | 80.5 |
| fre_gain | 54.0 |
| human_edit_recall | 1.000 |
| length_ratio | 1.20 |
| n_words | 18.0 |
| nli_completeness | 0.990 |
| nli_faithfulness | 0.955 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.143 |
| sari | 23.12 |
| severity_downgrade | 1.000 |
| severity_preservation | 0.000 |
| severity_tier_input | 3.000 |
| smog | 3.13 |
| smog_drop | 9.89 |

### Stage 4 - arm `termonly`

**output:** She said she had tiredness, feeling faint, and severe shortness of breath with activity.

| metric | value |
|---|---:|
| bertscore_f1 | 0.653 |
| coleman_liau | 11.91 |
| coleman_liau_drop | 5.45 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.333 |
| fkgl | 8.41 |
| fkgl_drop | 3.89 |
| fre | 59.7 |
| fre_gain | 33.2 |
| human_edit_recall | 1.000 |
| length_ratio | 0.93 |
| n_words | 14.0 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.994 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 38.88 |
| severity_downgrade | 0.000 |
| severity_preservation | 1.000 |
| severity_tier_input | 3.000 |
| severity_tier_output | 3.000 |
| smog | 11.21 |
| smog_drop | 1.82 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `fatigue` -> `tiredness` | replace | - | - | - | - | - | - | - |
| `lightheadedness` -> `feeling faint` | replace | - | - | - | - | - | - | - |
| `dyspnea on exertion` -> `shortness of breath with activity` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** She said she had tiredness, feeling dizzy or almost faint, and severe trouble breathing with effort.

| metric | value |
|---|---:|
| bertscore_f1 | 0.450 |
| coleman_liau | 12.07 |
| coleman_liau_drop | 5.29 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.400 |
| fkgl | 9.09 |
| fkgl_drop | 3.21 |
| fre | 58.4 |
| fre_gain | 31.9 |
| human_edit_recall | 1.000 |
| length_ratio | 1.07 |
| n_words | 16.0 |
| nli_completeness | 0.993 |
| nli_faithfulness | 0.991 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 28.85 |
| severity_downgrade | 0.000 |
| severity_preservation | 1.000 |
| severity_tier_input | 3.000 |
| severity_tier_output | 3.000 |
| smog | 8.84 |
| smog_drop | 4.18 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `fatigue` -> `tiredness` | replace | attributed | -0.826 | -2.965 | 0.925 | 0.887 | 0.543 | - |
| `lightheadedness` -> `feeling dizzy or almost faint` | replace | attributed | 21.271 | 22.070 | 0.727 | 0.926 | 17.518 | - |
| `dyspnea on exertion` -> `trouble breathing with effort` | replace | attributed | 3.361 | 3.534 | 0.723 | 0.792 | 0.010 | - |

**edit `fatigue` -> `tiredness`**

- status: `attributed`
- log p full -0.8985, empty -0.0724
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+1.119` [wiktionary] exertion: An exertion is the expenditure of physical or mental effort.
    - `+0.577` [thesaurus] exertion: effort, work
    - `+0.576` [readme] fatigue: Feeling exhausted and lacking energy.
    - `+0.515` [wiktionary] on: positioned at the upper surface of, touching from above
    - `+0.406` [wiktionary] on: at the date of

- rationale: Tiredness is a state of weariness or lack of energy, and "tiredness" carries that same sense of being worn out in everyday language. Phrase frequency decreases from Zipf 3.86 to 2.92, while age of acquisition falls from 11.83 to 7.22. Readers can grasp the symptom as ordinary exhaustion without needing a clinical label.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `lightheadedness` -> `feeling dizzy or almost faint`**

- status: `attributed`
- log p full -0.5972, empty -21.8682
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+17.799` [readme] lightheadedness: Feeling dizzy or almost faint.
    - `+0.280` [dictionary] Of (prep.): In a general sense, from, or out from; proceeding from; belonging to; relating to; concerning; -- 
    - `+0.108` [nih] fatigue: A condition marked by extreme tiredness and inability to function due to lack of energy. Fatigue may 
    - `+0.105` [dictionary] Of (prep.): Denoting that from which anything proceeds; indicating origin, source, descent, and the like; as, 
    - `+0.017` [readme] fatigue: Feeling exhausted and lacking energy.

- rationale: The readme describes lightheadedness as feeling dizzy or almost faint, so "feeling dizzy or almost faint" keeps that sensation in plain words. Phrase frequency rises from Zipf 1.92 to 3.26, while age of acquisition falls from 10.11 to 7.53. Readers can recognize the symptom from everyday experience without needing the clinical label.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `dyspnea on exertion` -> `trouble breathing with effort`**

- status: `attributed`
- log p full -1.8081, empty -5.1689
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+1.080` [thesaurus] exertion: effort, work
    - `+1.071` [michigan] exertion: Effort or work.
    - `+0.906` [readme] Dyspnea: Struggling to breathe, feeling out of breath.
    - `+0.387` [wiktionary] exertion: An exertion is the expenditure of physical or mental effort.

- rationale: The original term describes shortness of breath that appears when a person is physically active, and “trouble breathing with effort” keeps that same idea of breathlessness tied to exertion in everyday words. Phrase frequency rises from Zipf 2.09 to 4.09, while age of acquisition falls from 11.58 to 8.16. Readers can now recognize the symptom from its plain description rather than a clinical label.
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

**output:** No significant amount of edema associated with these in the dorsum of the hand.

| metric | value |
|---|---:|
| bertscore_f1 | 0.801 |
| coleman_liau | 9.01 |
| coleman_liau_drop | 0.00 |
| copy_jargon_rate | 1.000 |
| critical_error | 0.000 |
| fkgl | 10.94 |
| fkgl_drop | 0.00 |
| fre | 41.6 |
| fre_gain | 0.0 |
| human_edit_recall | 0.000 |
| length_ratio | 1.00 |
| n_words | 14.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.993 |
| nli_faithfulness | 0.993 |
| replacement_f1 | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 23.64 |
| severity_downgrade | 0.000 |
| severity_preservation | 1.000 |
| severity_tier_input | 2.000 |
| severity_tier_output | 2.000 |
| smog | 13.02 |
| smog_drop | 0.00 |

### Stage 4 - arm `termonly`

**output:** No clear swelling linked to these on the back of the hand.

| metric | value |
|---|---:|
| bertscore_f1 | 0.723 |
| coleman_liau | 3.97 |
| coleman_liau_drop | 5.05 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 1.87 |
| fkgl_drop | 9.07 |
| fre | 103.0 |
| fre_gain | 61.5 |
| human_edit_recall | 1.000 |
| length_ratio | 0.86 |
| n_words | 12.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.916 |
| nli_faithfulness | 0.692 |
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
| `edema` -> `swelling` | replace | - | - | - | - | - | - | - |
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

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `edema` -> `swelling` | replace | attributed | 0.052 | 0.100 | 0.481 | 0.699 | 0.613 | - |
| `dorsum` -> `back` | replace | attributed | 0.015 | 1.544 | 0.877 | 0.956 | 1.996 | - |

**edit `edema` -> `swelling`**

- status: `attributed`
- log p full -0.7083, empty -0.7603
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+1.106` [justplainclear] significant: Big, serious, important, major
    - `+0.493` [readme] Associated with: Connected with something.
    - `+0.383` [readme] Edema: Swelling in the body caused by too much fluid.
    - `+0.204` [justplainclear] associated with: Linked to, related to, goes along with, is part of
    - `+0.158` [michigan] significant: Big or important.

- rationale: The original term edema refers to a build-up of fluid in tissues that makes an area puffy, and the replacement swelling carries that same idea of visible puffiness in everyday language. Phrase frequency rises from Zipf 2.95 to 3.68, while syllable count falls from 3 to 2. Readers can now recognize the physical change being described without needing a medical label.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `dorsum` -> `back`**

- status: `attributed`
- log p full -0.0040, empty -0.0186
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+2.173` [readme] dorsum: The dorsum is basically the back or upper surface.
    - `+0.177` [justplainclear] significant: Big, serious, important, major
    - `+0.118` [michigan] edema: Swelling caused by too much fluid in your body.
    - `+0.097` [nih] significant: In statistics, describes a mathematical measure of difference between groups. The difference is s
    - `+0.087` [justplainclear] amount: How much or how many

- rationale: The original term dorsum refers to the back surface of a body part, and "back" carries that same anatomical sense in everyday language. Phrase frequency increases from Zipf 2.47 to 6.04, while syllables fall from 2 to 1. Readers can now picture the location without needing a specialized anatomical label.
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

**output:** The patient has no heart or lung complaints.

| metric | value |
|---|---:|
| bertscore_f1 | 0.616 |
| coleman_liau | 6.60 |
| coleman_liau_drop | 5.32 |
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
| nli_completeness | 0.987 |
| nli_faithfulness | 0.974 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 62.81 |
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
| `cardio` -> `heart` | replace | attributed | -0.223 | -1.611 | 0.520 | 0.847 | 0.070 | - |
| `pulmonary` -> `lung` | replace | attributed | 0.001 | 0.082 | 0.609 | 0.728 | 0.103 | - |

**edit `cardio` -> `heart`**

- status: `attributed`
- log p full -0.2871, empty -0.0643
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.172` [readme] pulmonary: Related to the lungs.
    - `+0.102` [iowa] PULMONARY: pertaining to the lungs
    - `-0.020` [thesaurus] pulmonary: related to the lungs
    - `-0.097` [nih] pulmonary: Having to do with the lungs.
    - `-0.106` [justplainclear] pulmonary: About the lungs

- rationale: The original term "cardio" is short for cardiovascular, referring to the heart and its blood vessels, and "heart" keeps that core meaning in plain words. Word frequency rises from Zipf 3.44 to 5.31, while syllables fall from 3 to 1. Readers can now recognize the body part being discussed without needing the abbreviated medical prefix.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `pulmonary` -> `lung`**

- status: `attributed`
- log p full -0.0131, empty -0.0142
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.292` [nih] pulmonary: Having to do with the lungs.
    - `+0.189` [readme] pulmonary: Related to the lungs.
    - `+0.072` [thesaurus] pulmonary: related to the lungs
    - `-0.022` [iowa] PULMONARY: pertaining to the lungs
    - `-0.309` [justplainclear] pulmonary: About the lungs

- rationale: The original term refers to the lungs, the organs that handle breathing, and "lung" carries that same anatomical meaning in plain words. Phrase frequency increases from Zipf 3.50 to 4.10, while age of acquisition falls from 13.05 to 7.16. Readers can now recognize the body part being discussed without needing a medical label.
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

**output:** At that time, the doctor had stopped Coreg because the patient’s blood pressure was low.

| metric | value |
|---|---:|
| bertscore_f1 | 0.606 |
| coleman_liau | 9.68 |
| coleman_liau_drop | -1.28 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.250 |
| fkgl | 5.21 |
| fkgl_drop | 1.73 |
| fre | 84.5 |
| fre_gain | 19.5 |
| human_edit_recall | 1.000 |
| length_ratio | 1.23 |
| n_words | 16.0 |
| nli_completeness | 0.704 |
| nli_faithfulness | 0.167 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 40.54 |
| smog | 3.13 |
| smog_drop | 8.08 |

### Stage 4 - arm `termonly`

**output:** At that time, the medicine had been held because of low blood pressure.

| metric | value |
|---|---:|
| bertscore_f1 | 0.757 |
| coleman_liau | 7.35 |
| coleman_liau_drop | 1.05 |
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
| nli_completeness | 0.072 |
| nli_faithfulness | 0.851 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 68.93 |
| smog | 8.84 |
| smog_drop | 2.37 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `Coreg` -> `medicine` | replace | - | - | - | - | - | - | - |
| `secondary to` -> `because of` | replace | - | - | - | - | - | - | - |
| `hypotension` -> `low blood pressure` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** At that time, the medicine had been held because of low blood pressure.

| metric | value |
|---|---:|
| bertscore_f1 | 0.757 |
| coleman_liau | 7.35 |
| coleman_liau_drop | 1.05 |
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
| nli_completeness | 0.072 |
| nli_faithfulness | 0.851 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 68.93 |
| smog | 8.84 |
| smog_drop | 2.37 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `Coreg` -> `medicine` | replace | attributed | -0.655 | -1.392 | 0.845 | 0.888 | 0.005 | - |
| `secondary to` -> `because of` | replace | attributed | 0.056 | 0.292 | 0.495 | 0.610 | 0.059 | - |
| `hypotension` -> `low blood pressure` | replace | attributed | 0.007 | 1.472 | 0.584 | 0.501 | 0.178 | - |

**edit `Coreg` -> `medicine`**

- status: `attributed`
- log p full -1.0210, empty -0.3657
- masks scored: 66/66 (+5 top-k)
- ranked sources:
    - `+0.081` [wiktionary] secondary: second, next in order to the first or primary.
    - `+0.077` [wiktionary] to: To has no meaning. It is used with a bare infinitival clause.
    - `+0.018` [readme] hypotension: Low blood pressure.
    - `+0.017` [readme] Hypotension: Hypotension means low blood pressure.

- rationale: The original term refers to a specific prescription drug, and the replacement uses a general category word that still signals a treatment is involved. Word frequency rises from Zipf 1.16 to 4.73, while syllable count goes from 1 to 3. Readers can now recognize the mention of a treatment without needing to know the brand name.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `secondary to` -> `because of`**

- status: `attributed`
- log p full -0.1852, empty -0.2410
- masks scored: 66/66 (+5 top-k)
- ranked sources:
    - `+0.318` [readme] Hypotension: Hypotension means low blood pressure.
    - `+0.259` [readme] hypotension: Low blood pressure.
    - `+0.153` [wiktionary] secondary: of less than primary importance.
    - `+0.150` [iowa] HYPOTENSION: low blood pressure
    - `+0.132` [wiktionary] hypotension: Hypotension is the disease of having low blood pressure.

- rationale: You explain, to a patient, why one phrase in a medical sentence was replaced with another.
- audit: coverage 0.0, grounding_error=False, omission=True, source_ok=True, passage_ok=True

**edit `hypotension` -> `low blood pressure`**

- status: `attributed`
- log p full -0.0022, empty -0.0096
- masks scored: 66/66 (+5 top-k)
- ranked sources:
    - `+0.343` [readme] Hypotension: Hypotension means low blood pressure.
    - `+0.165` [nih] Coreg: A drug used to treat high blood pressure and certain heart problems. It is also being studied in the pr
    - `+0.073` [wiktionary] secondary: of less than primary importance.
    - `+0.043` [wiktionary] hypotension: Hypotension is the disease of having low blood pressure.
    - `+0.039` [readme] hypotension: Low blood pressure.

- rationale: Hypotension means abnormally low blood pressure, and "low blood pressure" carries that same meaning in plain words. Phrase frequency increases from Zipf 2.52 to 4.65, while age of acquisition falls from 14.41 to 8.95. Patients can understand the basic heart-rhythm problem without first knowing the diagnostic name.
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

**output:** Her diarrhea has eased, and she is having less urine leakage and less swelling in her feet.

| metric | value |
|---|---:|
| bertscore_f1 | 0.620 |
| coleman_liau | 7.36 |
| coleman_liau_drop | 3.62 |
| copy_jargon_rate | 0.333 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 7.70 |
| fkgl_drop | 5.08 |
| fre | 70.1 |
| fre_gain | 38.2 |
| human_edit_recall | 0.667 |
| length_ratio | 1.00 |
| n_words | 17.0 |
| nli_completeness | 0.961 |
| nli_faithfulness | 0.861 |
| replacement_f1 | 0.800 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.429 |
| sari | 42.72 |
| smog | 8.84 |
| smog_drop | 5.71 |
| temporality_preservation | 0.000 |

### Stage 4 - arm `termonly`

**output:** Her loose stools have settled down and she is leaking urine less, with less swelling in her feet.

| metric | value |
|---|---:|
| bertscore_f1 | 0.682 |
| coleman_liau | 7.69 |
| coleman_liau_drop | 3.30 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 5.85 |
| fkgl_drop | 6.92 |
| fre | 85.2 |
| fre_gain | 53.2 |
| human_edit_recall | 1.000 |
| length_ratio | 1.06 |
| n_words | 18.0 |
| nli_completeness | 0.860 |
| nli_faithfulness | 0.808 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.286 |
| sari | 43.97 |
| smog | 3.13 |
| smog_drop | 11.43 |
| temporality_preservation | 0.000 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `diarrhea` -> `loose stools` | replace | - | - | - | - | - | - | - |
| `urinary incontinence` -> `leaking urine` | replace | - | - | - | - | - | - | - |
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
| `diarrhea` -> `loose, watery poop` | replace | attributed | 11.829 | 12.537 | 0.860 | 0.910 | 5.708 | - |
| `urinary incontinence` -> `loss of bladder control` | replace | attributed | 1.174 | 1.711 | 0.774 | 0.889 | 1.094 | - |
| `pedal edema` -> `swollen feet` | replace | attributed | 5.784 | 7.308 | 0.854 | 0.944 | 7.305 | - |

**edit `diarrhea` -> `loose, watery poop`**

- status: `attributed`
- log p full -0.6780, empty -12.5065
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+6.944` [readme] diarrhea: Having loose, watery poop with cramps and bloating.
    - `+1.236` [michigan] diarrhea: Loose, watery stools three or more times a day. It can be sudden (due to a virus, for example), pers
    - `+0.395` [wiktionary] diarrhea: Diarrhea is an illness where the person's poop or feces are soft like water.
    - `+0.164` [readme] urinary incontinence: When you can't control your pee.
    - `+0.158` [justplainclear] diarrhea: A bowel movement that is loose and watery If your poop is like water or very runny, or if you have m

- rationale: The source describes diarrhea as having loose, watery poop with cramps and bloating, so "loose, watery poop" keeps the core symptom in plain words. Phrase frequency decreases from Zipf 3.55 to 3.05, while syllable count rises from 4 to 5. Patients can picture the symptom directly without needing the medical label.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `urinary incontinence` -> `loss of bladder control`**

- status: `attributed`
- log p full -0.6788, empty -1.8523
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+1.310` [michigan] urinary incontinence: When you lose control of your bladder and the fluids it holds.
    - `+0.216` [justplainclear] diarrhea: A bowel movement that is loose and watery If your poop is like water or very runny, or if you have m
    - `+0.188` [wiktionary] diarrhea: Diarrhea is an illness where the person's poop or feces are soft like water.
    - `+0.085` [readme] diarrhea: Having loose, watery poop with cramps and bloating.
    - `+0.049` [michigan] diarrhea: Loose, watery stools three or more times a day. It can be sudden (due to a virus, for example), pers

- rationale: The source describes urinary incontinence as when you lose control of your bladder and the fluids it holds, so "loss of bladder control" keeps that loss-of-control idea in plain words. Phrase frequency rises from Zipf 2.77 to 3.60, while age of acquisition falls from 14.41 to 10.78. Readers can grasp the everyday bodily problem without needing the clinical label.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `pedal edema` -> `swollen feet`**

- status: `attributed`
- log p full -0.2450, empty -6.0289
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+7.605` [readme] pedal edema: Swollen feet.
    - `+0.300` [michigan] urinary incontinence: When you lose control of your bladder and the fluids it holds.
    - `+0.233` [michigan] diarrhea: Loose, watery stools three or more times a day. It can be sudden (due to a virus, for example), pers
    - `+0.067` [readme] diarrhea: Having loose, watery poop with cramps and bloating.
    - `+0.033` [wiktionary] diarrhea: Diarrhea is an illness where the person's poop or feces are soft like water.

- rationale: The source describes pedal edema as swollen feet, so "swollen feet" keeps the meaning in plain words. Phrase frequency increases from Zipf 2.87 to 3.55, while syllable count falls from 5 to 3. Patients can understand the basic swelling problem without first knowing the diagnostic name.
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

**output:** The patient has nausea and belly pain after eating. This is from gallbladder disease. A laparoscopic cholecystectomy is scheduled.

| metric | value |
|---|---:|
| bertscore_f1 | 0.395 |
| coleman_liau | 12.80 |
| coleman_liau_drop | 12.85 |
| copy_jargon_rate | 1.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 9.86 |
| fkgl_drop | 9.57 |
| fre | 35.7 |
| fre_gain | 56.8 |
| human_edit_recall | 0.000 |
| length_ratio | 1.06 |
| n_words | 19.0 |
| nli_completeness | 0.176 |
| nli_faithfulness | 0.976 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.250 |
| sari | 19.81 |
| smog | 9.73 |
| smog_drop | 6.18 |
| temporality_preservation | 1.000 |

### Stage 4 - arm `termonly`

**output:** The patient has a stomach ache after eating and feels sick to the stomach. The patient has a gallbladder problem. A planned keyhole gallbladder removal is set.

| metric | value |
|---|---:|
| bertscore_f1 | 0.439 |
| coleman_liau | 8.84 |
| coleman_liau_drop | 16.81 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.375 |
| fkgl | 5.84 |
| fkgl_drop | 13.60 |
| fre | 69.2 |
| fre_gain | 90.3 |
| human_edit_recall | 1.000 |
| length_ratio | 1.50 |
| n_words | 27.0 |
| nli_completeness | 0.266 |
| nli_faithfulness | 0.819 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.200 |
| sari | 16.33 |
| smog | 8.84 |
| smog_drop | 7.06 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 4 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `abdominal pain` -> `stomach ache` | replace | - | - | - | - | - | - | - |
| `Nausea` -> `feels sick to the stomach` | replace | - | - | - | - | - | - | - |
| `Gall bladder disease` -> `gallbladder problem` | replace | - | - | - | - | - | - | - |
| `Laparoscopic cholecystectomy` -> `keyhole gallbladder removal` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** The patient has a sick gallbladder and feels sick to the stomach and has a stomach ache after eating, and a planned small-tube camera surgery to take out the gallbladder is set.

| metric | value |
|---|---:|
| bertscore_f1 | 0.361 |
| coleman_liau | 9.19 |
| coleman_liau_drop | 16.45 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 13.85 |
| fkgl_drop | 5.58 |
| fre | 52.7 |
| fre_gain | 73.9 |
| human_edit_recall | 1.000 |
| length_ratio | 1.83 |
| n_words | 33.0 |
| nli_completeness | 0.878 |
| nli_faithfulness | 0.838 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.200 |
| sari | 16.48 |
| smog | 14.55 |
| smog_drop | 1.35 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `Nausea` -> `sick to the stomach` | replace | attributed | -0.785 | -1.722 | 0.792 | 0.882 | 0.044 | - |
| `abdominal pain` -> `stomach ache` | replace | attributed | 4.684 | 5.178 | 0.726 | 0.920 | 2.382 | - |
| `Laparoscopic cholecystectomy` -> `small-tube camera surgery to take out the gallbladder` | replace | attributed | 24.025 | 24.112 | 0.790 | 0.640 | 3.199 | - |

**edit `Nausea` -> `sick to the stomach`**

- status: `attributed`
- log p full -1.0852, empty -0.3004
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+0.203` [justplainclear] bladder disease: A disease or disorder of your bladder. Some bladder diseases may include: • urinary incontine
    - `+0.159` [readme] laparoscopic: A surgery where a small tube with a camera is used to see inside the body.
    - `+0.081` [readme] cholecystectomy: A surgery to remove the gallbladder, a digestion-assisting organ in the stomach.
    - `+0.067` [wiktionary] gall: Gall is anger or hatred.
    - `+0.037` [wiktionary] nausea: Nausea is the feeling of discomfort in the stomach, and the person will usually have a strong urge to 

- rationale: You explain, to a patient, why one phrase in a medical sentence was replaced with another.
- audit: coverage 0.0, grounding_error=False, omission=True, source_ok=True, passage_ok=True

**edit `abdominal pain` -> `stomach ache`**

- status: `attributed`
- log p full -0.9360, empty -5.6202
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+2.691` [readme] epigastric abdominal pain: Stomach ache that's felt below the ribs.
    - `+0.309` [readme] Cholecystectomy: A surgery to remove the gallbladder, an organ in your stomach that helps with digestion.
    - `+0.249` [justplainclear] nausea: Feeling like you want to throw up, stomach feels upset
    - `+0.106` [wiktionary] gall: If you have the gall to do something, you do it even though it is very rude or unreasonable.
    - `+0.099` [nih] nausea: A feeling of sickness or discomfort in the stomach that may come with an urge to vomit. Nausea is a si

- rationale: The source describes abdominal pain as a stomach ache that's felt below the ribs, so "stomach ache" keeps the location and sensation in plain words. Phrase frequency decreases from Zipf 3.56 to 3.39, while age of acquisition falls from 10.24 to 5.79. Patients can understand where the pain is and what it feels like without first knowing the anatomical term.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `Laparoscopic cholecystectomy` -> `small-tube camera surgery to take out the gallbladder`**

- status: `attributed`
- log p full -2.4859, empty -26.5107
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+10.176` [readme] Laparoscopic: A surgery that uses a small tube and camera to see inside your body.
    - `+6.977` [readme] laparoscopic: A surgery where a small tube with a camera is used to see inside the body.
    - `+2.097` [readme] Cholecystectomy: A surgery to remove the gallbladder, an organ in your stomach that helps with digestion.
    - `+1.455` [wiktionary] gall: If you have the gall to do something, you do it even though it is very rude or unreasonable.
    - `+0.859` [wiktionary] gall: Gall is anger or hatred.

- rationale: The readme describes laparoscopic cholecystectomy as a surgery that uses a small tube and camera to see inside your body, so "small-tube camera surgery to take out the gallbladder" keeps that minimally invasive approach and the gallbladder removal in plain words. Phrase frequency increases from Zipf 1.73 to 2.79, while syllables increase from 10 to 15. Patients can understand the procedure’s method and purpose without first knowing the surgical name.
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

**output:** She says she has a history of heart disease, but she cannot give more details.

| metric | value |
|---|---:|
| bertscore_f1 | 0.621 |
| coleman_liau | 6.20 |
| coleman_liau_drop | 4.07 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.125 |
| fkgl | 5.99 |
| fkgl_drop | 6.28 |
| fre | 78.8 |
| fre_gain | 36.1 |
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

**output:** She says she has long-standing heart disease but cannot give more detail.

| metric | value |
|---|---:|
| bertscore_f1 | 0.551 |
| coleman_liau | 10.73 |
| coleman_liau_drop | -0.46 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 5.81 |
| fkgl_drop | 6.46 |
| fre | 74.8 |
| fre_gain | 32.1 |
| human_edit_recall | 1.000 |
| length_ratio | 0.59 |
| n_words | 13.0 |
| negation_preservation | 0.000 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.994 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 14.28 |
| severity_downgrade | 1.000 |
| severity_preservation | 0.000 |
| severity_tier_input | 2.000 |
| smog | 8.84 |
| smog_drop | 5.71 |
| temporality_preservation | 0.000 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `underlying` -> `long-standing` | replace | - | - | - | - | - | - | - |
| `elaborate` -> `give more detail` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** She says she has a long-standing heart disease but cannot give much detail.

| metric | value |
|---|---:|
| bertscore_f1 | 0.605 |
| coleman_liau | 9.14 |
| coleman_liau_drop | 1.13 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.125 |
| fkgl | 5.82 |
| fkgl_drop | 6.45 |
| fre | 76.5 |
| fre_gain | 33.8 |
| human_edit_recall | 1.000 |
| length_ratio | 0.64 |
| n_words | 14.0 |
| negation_preservation | 0.000 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.994 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 14.13 |
| severity_downgrade | 1.000 |
| severity_preservation | 0.000 |
| severity_tier_input | 2.000 |
| smog | 8.84 |
| smog_drop | 5.71 |
| temporality_preservation | 0.000 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `underlying` -> `long-standing` | replace | attributed | -0.643 | -1.347 | 0.417 | 0.862 | 0.072 | - |
| `elaborate` -> `give much detail` | replace | attributed | 0.918 | 1.030 | 0.336 | 0.886 | 0.025 | - |

**edit `underlying` -> `long-standing`**

- status: `attributed`
- log p full -1.0244, empty -0.3814
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.148` [wiktionary] to: To shows where something goes, the goal of movement.
    - `+0.076` [wiktionary] extent: You use "to an extent" to explain how true something is or how much it happens.
    - `+0.067` [wiktionary] states: A state is a condition or a situation.
    - `+0.040` [wiktionary] significant: A significant look, movement, etc. is one that has a particular meaning.
    - `+0.009` [nih] significant: In statistics, describes a mathematical measure of difference between groups. The difference is s

- rationale: The original term means something that exists for a long time, and the replacement carries that meaning in plain words. Phrase frequency increases from Zipf 4.17 to 4.81, while syllable count falls from 4 to 3. Readers can now understand the time frame without needing a technical label.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `elaborate` -> `give much detail`**

- status: `attributed`
- log p full -1.7996, empty -2.7171
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.379` [wiktionary] extent: The extent of something is how far it goes, how much area it covers, or how much it does.
    - `+0.354` [wiktionary] underlying: An underlying cause, problem, or assumption, is important but hard to notice.
    - `+0.214` [wiktionary] any: it does not matter which
    - `+0.129` [wiktionary] extent: You use "to an extent" to explain how true something is or how much it happens.
    - `+0.106` [wiktionary] elaborate: When something is supposed to be elaborated, it is needed to be expanded or add details to.

- rationale: The original term means to produce or work out in a detailed or complex way, and the replacement carries that meaning by saying to give much detail. Phrase frequency increases from Zipf 4.06 to 4.53, while age of acquisition falls from 11.53 to 9.79. Readers can grasp the idea of adding detail without needing the more formal verb.
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

**output:** There was a little swelling of the fourth finger, and he is still wearing his wedding band on it.

| metric | value |
|---|---:|
| bertscore_f1 | 0.825 |
| coleman_liau | 6.15 |
| coleman_liau_drop | 0.90 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.667 |
| fkgl | 6.73 |
| fkgl_drop | -0.22 |
| fre | 80.7 |
| fre_gain | 0.2 |
| human_edit_recall | 1.000 |
| length_ratio | 1.06 |
| n_words | 19.0 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.992 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.600 |
| sari | 43.00 |
| severity_downgrade | 0.000 |
| severity_preservation | 0.000 |
| severity_tier_input | 1.000 |
| severity_tier_output | 1.000 |
| smog | 3.13 |
| smog_drop | 5.71 |

### Stage 4 - arm `termonly`

**output:** There was some slight swelling of the ring finger, on which he still is wearing his wedding band.

| metric | value |
|---|---:|
| bertscore_f1 | 0.948 |
| coleman_liau | 7.69 |
| coleman_liau_drop | -0.64 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 5.85 |
| fkgl_drop | 0.66 |
| fre | 85.2 |
| fre_gain | 4.7 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 18.0 |
| nli_completeness | 0.405 |
| nli_faithfulness | 0.238 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 81.51 |
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
| `fourth digit` -> `ring finger` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** There was some slight swelling of the ring finger, on which he still is wearing his wedding band.

| metric | value |
|---|---:|
| bertscore_f1 | 0.948 |
| coleman_liau | 7.69 |
| coleman_liau_drop | -0.64 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 5.85 |
| fkgl_drop | 0.66 |
| fre | 85.2 |
| fre_gain | 4.7 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 18.0 |
| nli_completeness | 0.405 |
| nli_faithfulness | 0.238 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 81.51 |
| severity_downgrade | 0.000 |
| severity_preservation | 1.000 |
| severity_tier_input | 1.000 |
| severity_tier_output | 1.000 |
| smog | 3.13 |
| smog_drop | 5.71 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `edema` -> `swelling` | replace | attributed | 0.015 | 1.609 | 0.252 | 0.500 | 1.012 | - |
| `fourth digit` -> `ring finger` | replace | attributed | 0.313 | 0.867 | 0.485 | 0.823 | 0.324 | - |

**edit `edema` -> `swelling`**

- status: `attributed`
- log p full -0.0038, empty -0.0190
- masks scored: 66/66 (+3 top-k)
- ranked sources:
    - `+1.433` [nih] edema: Swelling caused by excess fluid in body tissues.
    - `+0.420` [readme] Edema: Swelling in the body caused by too much fluid.
    - `+0.345` [readme] edema: Swelling due to too much fluid in the body tissues.
    - `+0.184` [readme] digit: A digit is a finger or toe.
    - `+0.162` [michigan] edema: Swelling caused by too much fluid in your body.

- rationale: Swelling is the plain-language way to say edema, the excess fluid that makes a body part look puffy and feel tight, so the replacement keeps the core idea of fluid buildup in everyday terms. Phrase frequency rises from Zipf 2.95 to 3.68, while syllables drop from 3 to 2. Readers can now recognize the symptom without needing a medical label.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `fourth digit` -> `ring finger`**

- status: `attributed`
- log p full -0.3105, empty -0.6240
- masks scored: 66/66 (+3 top-k)
- ranked sources:
    - `+0.367` [nih] edema: Swelling caused by excess fluid in body tissues.
    - `+0.043` [readme] Edema: Swelling in the body caused by too much fluid.
    - `+0.031` [michigan] edema: Swelling caused by too much fluid in your body.
    - `-0.006` [iowa] EDEMA: excess fluid collecting in tissue

- rationale: The original term refers to the fourth digit on a hand, and "ring finger" carries that meaning by naming the finger commonly associated with a wedding ring. Phrase frequency increases from Zipf 3.73 to 4.31, while age of acquisition falls from 9.26 to 4.53. Readers can now identify the intended finger without counting from the thumb.
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

**output:** Parents say she seems to breathe fast, gets a bit tired during feeds, works harder to breathe, and sweats.

| metric | value |
|---|---:|
| bertscore_f1 | 0.541 |
| coleman_liau | 8.28 |
| coleman_liau_drop | 7.10 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.333 |
| fkgl | 6.10 |
| fkgl_drop | 6.72 |
| fre | 85.1 |
| fre_gain | 44.6 |
| human_edit_recall | 1.000 |
| length_ratio | 0.90 |
| n_words | 19.0 |
| nli_completeness | 0.890 |
| nli_faithfulness | 0.179 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.545 |
| sari | 15.19 |
| smog | 3.13 |
| smog_drop | 9.89 |

### Stage 4 - arm `termonly`

**output:** Parents say she seems to breathe fast, gets a bit tired with feeding with more work to breathe and sweating.

| metric | value |
|---|---:|
| bertscore_f1 | 0.621 |
| coleman_liau | 7.95 |
| coleman_liau_drop | 7.43 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.667 |
| fkgl | 6.37 |
| fkgl_drop | 6.46 |
| fre | 85.0 |
| fre_gain | 44.5 |
| human_edit_recall | 1.000 |
| length_ratio | 0.95 |
| n_words | 20.0 |
| nli_completeness | 0.936 |
| nli_faithfulness | 0.727 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 20.18 |
| smog | 3.13 |
| smog_drop | 9.89 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `rapidly` -> `fast` | replace | - | - | - | - | - | - | - |
| `respiratory effort` -> `more work to breathe` | replace | - | - | - | - | - | - | - |
| `diaphoresis` -> `sweating` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Parents say she seems to breathe quickly, gets a bit tired with feeding with more work to breathe and heavy sweating.

| metric | value |
|---|---:|
| bertscore_f1 | 0.610 |
| coleman_liau | 9.03 |
| coleman_liau_drop | 6.35 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.833 |
| fkgl | 7.77 |
| fkgl_drop | 5.06 |
| fre | 76.7 |
| fre_gain | 36.3 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 21.0 |
| nli_completeness | 0.940 |
| nli_faithfulness | 0.121 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 21.88 |
| smog | 3.13 |
| smog_drop | 9.89 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `rapidly` -> `quickly` | replace | attributed | 1.884 | 2.633 | 0.881 | 0.923 | 1.747 | - |
| `respiratory effort` -> `more work to breathe` | replace | attributed | 0.265 | 0.682 | 0.460 | 0.842 | 0.381 | - |
| `diaphoresis` -> `heavy sweating` | replace | attributed | 3.717 | 7.036 | 0.827 | 0.916 | 4.501 | - |

**edit `rapidly` -> `quickly`**

- status: `attributed`
- log p full -0.5664, empty -2.4509
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+1.864` [wiktionary] rapidly: If something is done rapidly, then it is done quickly or swiftly.
    - `+0.117` [wiktionary] effort: The amount of work that is done on something.
    - `+0.080` [wiktionary] respiratory: A respiratory problem refers to something that affects breathing or the lungs.

- rationale: The source describes rapidly as done quickly or swiftly, so "quickly" keeps the sense of speed in plain words. Phrase frequency increases from Zipf 4.34 to 5.00, while syllables fall from 3 to 2. Readers can grasp the pace of the action without a more formal adverb.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `respiratory effort` -> `more work to breathe`**

- status: `attributed`
- log p full -0.3723, empty -0.6375
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+0.727` [wiktionary] effort: The amount of work that is done on something.
    - `+0.346` [wiktionary] rapidly: If something is done rapidly, then it is done quickly or swiftly.
    - `+0.129` [michigan] diaphoresis: Sweating, a clear, salty liquid produced by glands in your skin. Sweating is how your body cools 

- rationale: The original term refers to the work the lungs and chest muscles do to move air in and out, and "more work to breathe" keeps that idea of increased breathing effort in everyday language. Phrase frequency increases from Zipf 3.78 to 4.25, while age of acquisition falls from 11.00 to 5.86, and syllables drop from 7 to 4. Readers can grasp that breathing is becoming harder without needing technical respiratory vocabulary.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `diaphoresis` -> `heavy sweating`**

- status: `attributed`
- log p full -0.0360, empty -3.7528
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+6.017` [readme] diaphoresis: Heavy sweating.
    - `+1.516` [readme] Diaphoresis: Intense sweating.
    - `+1.398` [wiktionary] effort: The amount of work that is done on something.
    - `+0.955` [wiktionary] state: Any sovereign nation (nation that rules itself) is a state.
    - `+0.775` [michigan] state: To say or tell. In medicine, how you are doing.

- rationale: The source describes diaphoresis as heavy sweating, so "heavy sweating" keeps the core idea in plain words. Phrase frequency rises from Zipf 1.28 to 3.64, while age of acquisition falls from 15.22 to 4.05. Readers can recognize the symptom without needing the medical label.
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

**output:** The patient says he has not used amphetamines for at least four to five months. However, he had chest pain start this evening.

| metric | value |
|---|---:|
| bertscore_f1 | 0.826 |
| coleman_liau | 7.10 |
| coleman_liau_drop | 2.29 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 4.29 |
| fkgl_drop | 7.06 |
| fre | 84.8 |
| fre_gain | 24.8 |
| human_edit_recall | 1.000 |
| length_ratio | 0.96 |
| n_words | 23.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.002 |
| nli_faithfulness | 0.994 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 46.12 |
| smog | 8.84 |
| smog_drop | 4.18 |

### Stage 4 - arm `termonly`

**output:** The patient says he has not used a medicine that raises energy and mood for at least four to five months; however, he had start of chest pain this evening.

| metric | value |
|---|---:|
| bertscore_f1 | 0.686 |
| coleman_liau | 6.99 |
| coleman_liau_drop | 2.39 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 11.45 |
| fkgl_drop | -0.11 |
| fre | 66.4 |
| fre_gain | 6.3 |
| human_edit_recall | 1.000 |
| length_ratio | 1.25 |
| n_words | 30.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.049 |
| nli_faithfulness | 0.126 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 31.05 |
| smog | 13.02 |
| smog_drop | 0.00 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `amphetamines` -> `a medicine that raises energy and mood` | replace | - | - | - | - | - | - | - |
| `onset` -> `start` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** The patient says he has not used a stimulant drug that helps people stay awake and focus for at least four to five months; however, he had the start of chest pain this evening.

| metric | value |
|---|---:|
| bertscore_f1 | 0.661 |
| coleman_liau | 7.21 |
| coleman_liau_drop | 2.17 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 12.59 |
| fkgl_drop | -1.25 |
| fre | 65.3 |
| fre_gain | 5.3 |
| human_edit_recall | 1.000 |
| length_ratio | 1.42 |
| n_words | 34.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.013 |
| nli_faithfulness | 0.145 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 31.08 |
| smog | 11.21 |
| smog_drop | 1.82 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `amphetamines` -> `a stimulant drug that helps people stay awake and focus` | replace | attributed | 11.673 | 11.681 | - | 0.878 | 11.221 | - |
| `onset` -> `the start` | replace | attributed | 0.567 | 1.746 | - | 0.786 | 0.176 | - |

**edit `amphetamines` -> `a stimulant drug that helps people stay awake and focus`**

- status: `attributed`
- log p full -4.8736, empty -16.5470
- masks scored: 10/10 (+3 top-k)
- ranked sources:
    - `+11.277` [wiktionary] amphetamines: Amphetamine is a synthetic drug. It is a stimulant that helps people keep the focus and stay awa
    - `+0.056` [wiktionary] onset: The onset of something is the time when it begins (usually something bad).

- rationale: The original term refers to a class of synthetic stimulant medicines, and the replacement carries that meaning by naming a stimulant drug and describing its alerting and focusing effects in plain words. Phrase frequency rises from Zipf 2.82 to 3.00, while syllable count rises from 4 to 15. Readers can now grasp the kind of drug and what it does without needing prior medical vocabulary.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `onset` -> `the start`**

- status: `attributed`
- log p full -0.1760, empty -0.7432
- masks scored: 10/10 (+3 top-k)
- ranked sources:
    - `+0.958` [wiktionary] onset: The onset of something is the time when it begins (usually something bad).
    - `+0.782` [michigan] onset: The start.
    - `+0.471` [wiktionary] amphetamines: Amphetamine is a synthetic drug. It is a stimulant that helps people keep the focus and stay awa

- rationale: You explain, to a patient, why one phrase in a medical sentence was replaced with another.
- audit: coverage 0.0, grounding_error=False, omission=True, source_ok=True, passage_ok=True

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

**output:** Orogastric suction was done and only a small amount of clear stomach contents came out.

| metric | value |
|---|---:|
| bertscore_f1 | 0.412 |
| coleman_liau | 10.07 |
| coleman_liau_drop | 5.97 |
| copy_jargon_rate | 0.667 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 7.57 |
| fkgl_drop | 0.80 |
| fre | 67.5 |
| fre_gain | 14.7 |
| human_edit_recall | 0.333 |
| length_ratio | 0.94 |
| n_words | 15.0 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.994 |
| replacement_f1 | 0.500 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 44.01 |
| smog | 8.84 |
| smog_drop | 0.00 |

### Stage 4 - arm `termonly`

**output:** A tube placed through the mouth into the stomach to remove fluid was done, with only a small amount of clear fluid from the stomach.

| metric | value |
|---|---:|
| bertscore_f1 | 0.477 |
| coleman_liau | 7.61 |
| coleman_liau_drop | 8.43 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.222 |
| fkgl | 9.74 |
| fkgl_drop | -1.37 |
| fre | 69.8 |
| fre_gain | 16.9 |
| human_edit_recall | 1.000 |
| length_ratio | 1.56 |
| n_words | 25.0 |
| nli_completeness | 0.955 |
| nli_faithfulness | 0.928 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 38.25 |
| smog | 3.13 |
| smog_drop | 5.71 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `clear stomach contents` -> `clear fluid from the stomach` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** A tube through the mouth to the stomach was used to pull out fluid, and only a very small amount of easy-to-see stomach fluid came out.

| metric | value |
|---|---:|
| bertscore_f1 | 0.372 |
| coleman_liau | 6.71 |
| coleman_liau_drop | 9.33 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.333 |
| fkgl | 9.98 |
| fkgl_drop | -1.61 |
| fre | 69.8 |
| fre_gain | 16.9 |
| human_edit_recall | 1.000 |
| length_ratio | 1.75 |
| n_words | 28.0 |
| nli_completeness | 0.943 |
| nli_faithfulness | 0.762 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 29.90 |
| smog | 3.13 |
| smog_drop | 5.71 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `clear stomach contents` -> `easy-to-see stomach fluid` | replace | attributed | 5.374 | 5.529 | 0.908 | 0.956 | 2.595 | - |

**edit `clear stomach contents` -> `easy-to-see stomach fluid`**

- status: `attributed`
- log p full -1.9373, empty -7.3110
- masks scored: 66/66 (+2 top-k)
- ranked sources:
    - `+4.089` [wiktionary] clear: A clear idea is an idea that is easy to understand.
    - `+1.493` [wiktionary] clear: If it is clear that something is a certain way, there can be no mistake about it.
    - `+0.615` [justplainclear] stomach: A part of the body where food is digested Parts of the digestive system showing the stomach
    - `+0.214` [wiktionary] out: Something that is out is not in.
    - `+0.049` [wiktionary] out: If something using electricity is out, it is turned off or the electricity is not flowing..

- rationale: The source describes a clear idea as one that is easy to understand, so "easy-to-see stomach fluid" keeps the sense of visibility and clarity in plain words. Phrase frequency rises from Zipf 3.96 to 3.98, while age of acquisition falls from 8.50 to 7.94. Readers can grasp what is being visualized in the stomach without needing the technical phrasing.
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

**output:** Probably there is some restrictive element because of fibrosis.

| metric | value |
|---|---:|
| bertscore_f1 | 0.813 |
| coleman_liau | 15.71 |
| coleman_liau_drop | 0.00 |
| copy_jargon_rate | 1.000 |
| critical_error | 0.000 |
| fkgl | 11.52 |
| fkgl_drop | 0.00 |
| fre | 28.5 |
| fre_gain | 0.0 |
| human_edit_recall | 0.000 |
| length_ratio | 0.82 |
| n_words | 9.0 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.994 |
| replacement_f1 | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 30.89 |
| smog | 14.55 |
| smog_drop | 0.00 |
| uncertainty_preservation | 1.000 |

### Stage 4 - arm `termonly`

**output:** Probably there is some limiting part because of scar tissue.

| metric | value |
|---|---:|
| bertscore_f1 | 0.784 |
| coleman_liau | 10.24 |
| coleman_liau_drop | 5.47 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 7.19 |
| fkgl_drop | 4.33 |
| fre | 61.3 |
| fre_gain | 32.8 |
| human_edit_recall | 1.000 |
| length_ratio | 0.91 |
| n_words | 10.0 |
| nli_completeness | 0.783 |
| nli_faithfulness | 0.912 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 28.34 |
| smog | 11.21 |
| smog_drop | 3.35 |
| uncertainty_preservation | 1.000 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `restrictive element` -> `limiting part` | replace | - | - | - | - | - | - | - |
| `fibrosis` -> `scar tissue` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Probably there is some limiting part because of tissue that becomes thick and scarred due to injury.

| metric | value |
|---|---:|
| bertscore_f1 | 0.656 |
| coleman_liau | 10.78 |
| coleman_liau_drop | 4.93 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 9.09 |
| fkgl_drop | 2.43 |
| fre | 60.2 |
| fre_gain | 31.7 |
| human_edit_recall | 1.000 |
| length_ratio | 1.55 |
| n_words | 17.0 |
| nli_completeness | 0.554 |
| nli_faithfulness | 0.125 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 28.34 |
| smog | 13.02 |
| smog_drop | 1.53 |
| uncertainty_preservation | 1.000 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `restrictive element` -> `limiting part` | replace | attributed | 1.469 | 2.620 | 0.857 | 0.885 | 0.512 | - |
| `fibrosis` -> `tissue that becomes thick and scarred due to injury` | replace | attributed | 30.426 | 30.857 | 0.916 | 0.872 | 30.539 | - |

**edit `restrictive element` -> `limiting part`**

- status: `attributed`
- log p full -0.3049, empty -1.7740
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+1.333` [wiktionary] restrictive: If something is restrictive, it limits or controls what people can do.
    - `+0.821` [wiktionary] element: An element is one part of something bigger, such as a plan, an engine, or a business.
    - `+0.264` [nih] fibrosis: The growth of fibrous tissue.
    - `+0.184` [nih] element: A basic part of a whole. In chemistry, refers to a simple substance that cannot be broken down into s
    - `+0.128` [wiktionary] element: An element is one basic kind of substance, such as iron (Fe), oxygen (O), or sodium (Na).

- rationale: The source describes restrictive as limiting or controlling what people can do, so "limiting part" keeps that limiting sense in plain words. Phrase frequency increases from Zipf 3.49 to 3.94, while age of acquisition falls from 11.00 to 5.11. Readers can grasp the idea of a constraint without needing the technical label.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `fibrosis` -> `tissue that becomes thick and scarred due to injury`**

- status: `attributed`
- log p full -1.0504, empty -31.4766
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+31.335` [readme] FIBROSIS: Fibrosis is tissue that becomes thick and scarred due to injury.
    - `+0.797` [nih] element: A basic part of a whole. In chemistry, refers to a simple substance that cannot be broken down into s
    - `+0.427` [wiktionary] restrictive: If something is restrictive, it limits or controls what people can do.
    - `-0.065` [wiktionary] element: An element is one part of something bigger, such as a plan, an engine, or a business.

- rationale: The source describes fibrosis as tissue that becomes thick and scarred due to injury, so "tissue that becomes thick and scarred due to injury" keeps that definition in plain words. Word frequency falls from Zipf 3.19 to 3.18, while age of acquisition falls from 14.94 to 7.56. Patients can understand the condition as a change in tissue rather than an unfamiliar medical label.
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

**output:** The womb was placed back into the belly area where the stomach and other organs are located.

| metric | value |
|---|---:|
| bertscore_f1 | 0.649 |
| coleman_liau | 8.05 |
| coleman_liau_drop | 1.22 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 9.09 |
| fkgl_drop | 1.12 |
| fre | 60.2 |
| fre_gain | 22.3 |
| human_edit_recall | 1.000 |
| length_ratio | 2.12 |
| n_words | 17.0 |
| nli_completeness | 0.989 |
| nli_faithfulness | 0.322 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 74.72 |
| smog | 11.21 |
| smog_drop | 1.82 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `uterus` -> `womb` | replace | attributed | 0.001 | 0.121 | 0.480 | 0.901 | 0.053 | - |
| `abdominal cavity` -> `belly area where the stomach and other organs are located` | replace | attributed | 27.716 | 28.402 | 0.836 | 0.817 | 23.307 | - |

**edit `uterus` -> `womb`**

- status: `attributed`
- log p full -0.0067, empty -0.0076
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.612` [thesaurus] uterus: womb
    - `+0.559` [readme] abdominal cavity: The belly area where your stomach and other organs are located.
    - `+0.048` [michigan] uterus: Womb, or where a baby grows when a woman is pregnant.
    - `-0.302` [justplainclear] uterus: Also known as: womb An organ in a woman's body where babies may grow during pregnancy Uterus
    - `-0.645` [wiktionary] uterus: The uterus is the internal organ inside of a female mammal where an embryo grows into an infant ready 

- rationale: You explain, to a patient, why one phrase in a medical sentence was replaced with another.
- audit: coverage 0.0, grounding_error=False, omission=True, source_ok=True, passage_ok=True

**edit `abdominal cavity` -> `belly area where the stomach and other organs are located`**

- status: `attributed`
- log p full -0.7002, empty -28.4160
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+23.701` [readme] abdominal cavity: The belly area where your stomach and other organs are located.
    - `+0.394` [michigan] uterus: Womb, or where a baby grows when a woman is pregnant.
    - `+0.386` [nih] uterus: The hollow, pear-shaped organ in a woman's pelvis. The uterus is where a fetus (unborn baby) develops 

- rationale: The readme describes the abdominal cavity as the belly area where your stomach and other organs are located, so "belly area where the stomach and other organs are located" keeps that anatomical location in plain words. Phrase frequency rises from Zipf 3.29 to 3.63, while age of acquisition falls from 10.24 to 6.58. Readers can picture the body region being discussed without needing the formal anatomical label.
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

**output:** This was seen on the front and side X-ray views.

| metric | value |
|---|---:|
| bertscore_f1 | 0.548 |
| coleman_liau | 2.70 |
| coleman_liau_drop | 4.63 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 0.11 |
| fkgl_drop | 4.85 |
| fre | 112.1 |
| fre_gain | 36.6 |
| human_edit_recall | 1.000 |
| laterality_preservation | 0.000 |
| length_ratio | 1.38 |
| n_words | 11.0 |
| nli_completeness | 0.294 |
| nli_faithfulness | 0.358 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 45.11 |
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

**output:** This was viewed on the front to back and side views.

| metric | value |
|---|---:|
| bertscore_f1 | 0.730 |
| coleman_liau | 3.13 |
| coleman_liau_drop | 4.21 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 0.50 |
| fkgl_drop | 4.46 |
| fre | 111.1 |
| fre_gain | 35.6 |
| human_edit_recall | 1.000 |
| laterality_preservation | 0.000 |
| length_ratio | 1.38 |
| n_words | 11.0 |
| nli_completeness | 0.731 |
| nli_faithfulness | 0.887 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 54.23 |
| smog | 3.13 |
| smog_drop | 8.08 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `AP` -> `front to back` | replace | attributed | 8.562 | 9.512 | 0.858 | 0.950 | 2.891 | - |
| `lateral projections` -> `side views` | replace | attributed | 0.159 | 0.670 | 0.714 | 0.836 | 0.096 | - |

**edit `AP` -> `front to back`**

- status: `attributed`
- log p full -0.4888, empty -9.0503
- masks scored: 66/66 (+3 top-k)
- ranked sources:
    - `+4.916` [readme] anteroposterior: Front to back.
    - `+2.024` [dorland] AP: anteroposterior
    - `+0.620` [wiktionary] lateral: An object's lateral refers to the side of it.
    - `+0.469` [dorland] AP: alkaline phosphatase
    - `+0.270` [michigan] lateral: The side or on the side.

- rationale: The source describes AP as front to back, so "front to back" keeps that spatial direction in plain words. Syllables increase from 1 to 3. Patients can understand the basic spatial direction without first knowing the abbreviation.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `lateral projections` -> `side views`**

- status: `attributed`
- log p full -0.1987, empty -0.3574
- masks scored: 66/66 (+3 top-k)
- ranked sources:
    - `+0.517` [readme] anteroposterior: Front to back.
    - `+0.421` [readme] lateral: Lateral means on or related to the side of the body or a body part.
    - `+0.344` [dorland] AP: anteroposterior
    - `+0.188` [wiktionary] lateral: An object's lateral refers to the side of it.

- rationale: You explain, to a patient, why one phrase in a medical sentence was replaced with another.
- audit: coverage 0.0, grounding_error=False, omission=True, source_ok=True, passage_ok=True

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

**output:** The voice bands move normally with sound making and air moving.

| metric | value |
|---|---:|
| bertscore_f1 | 0.421 |
| coleman_liau | 8.93 |
| coleman_liau_drop | 5.65 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.333 |
| fkgl | 4.79 |
| fkgl_drop | 3.39 |
| fre | 80.3 |
| fre_gain | 29.6 |
| human_edit_recall | 1.000 |
| length_ratio | 1.38 |
| n_words | 11.0 |
| nli_completeness | 0.971 |
| nli_faithfulness | 0.938 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 32.22 |
| smog | 8.84 |
| smog_drop | 2.37 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `cords` -> `voice bands` | replace | - | - | - | - | - | - | - |
| `phonation` -> `sound making` | replace | - | - | - | - | - | - | - |
| `ventilation` -> `air moving` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** The long, thin ropes move normally with making sounds and breathing.

| metric | value |
|---|---:|
| bertscore_f1 | 0.458 |
| coleman_liau | 11.04 |
| coleman_liau_drop | 3.54 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 4.79 |
| fkgl_drop | 3.39 |
| fre | 80.3 |
| fre_gain | 29.6 |
| human_edit_recall | 1.000 |
| length_ratio | 1.38 |
| n_words | 11.0 |
| nli_completeness | 0.972 |
| nli_faithfulness | 0.102 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 35.46 |
| smog | 8.84 |
| smog_drop | 2.37 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `cords` -> `long, thin ropes` | replace | attributed | 22.206 | 22.369 | - | 0.876 | 21.165 | - |
| `phonation` -> `making sounds` | replace | attributed | 1.761 | 1.976 | - | 0.657 | 0.158 | - |
| `ventilation` -> `breathing` | replace | attributed | 0.297 | 1.150 | - | 0.896 | 3.114 | - |

**edit `cords` -> `long, thin ropes`**

- status: `attributed`
- log p full -1.8902, empty -24.0960
- masks scored: 34/34 (+6 top-k)
- ranked sources:
    - `+21.324` [wiktionary] cords: A long, thin rope or wire.
    - `+0.159` [readme] ventilation: Ventilation is about bringing in fresh air.
    - `-0.519` [wiktionary] ventilation: Ventilation is the bodily process of breathing; the inhalation of air to provide oxygen, and the 

- rationale: The original term refers to slender, flexible strands, and "long, thin ropes" keeps that idea of length and narrowness in everyday language. Phrase frequency rises from Zipf 3.35 to 3.59, while syllables increase from 1 to 3. Readers can picture the shape and size without needing a technical label.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `phonation` -> `making sounds`**

- status: `attributed`
- log p full -1.4912, empty -3.2518
- masks scored: 34/34 (+6 top-k)
- ranked sources:
    - `+0.401` [dictionary] Phonation (n.): The act or process by which articulate sounds are uttered; the utterance of articulate sounds;
    - `+0.243` [wiktionary] cords: A long, thin rope or wire.
    - `+0.232` [readme] ventilation: Ventilation is about bringing in fresh air.
    - `-0.092` [wiktionary] ventilation: Ventilation is the bodily process of breathing; the inhalation of air to provide oxygen, and the 

- rationale: The original term phonation refers to the production of sound with the vocal folds, so "making sounds" carries that meaning in plain words. Phrase frequency increases from Zipf 1.80 to 4.87, while syllables increase from 2 to 3. Readers can understand the basic idea of sound production without needing the technical term.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `ventilation` -> `breathing`**

- status: `attributed`
- log p full -0.1743, empty -0.4708
- masks scored: 34/34 (+6 top-k)
- ranked sources:
    - `+3.205` [wiktionary] ventilation: Ventilation is the bodily process of breathing; the inhalation of air to provide oxygen, and the 
    - `+0.091` [dictionary] Phonation (n.): The act or process by which articulate sounds are uttered; the utterance of articulate sounds;
    - `-0.303` [wiktionary] cords: A long, thin rope or wire.
    - `-0.736` [wiktionary] ventilation: Ventilation is the replacement of stale air with fresh air.
    - `-1.206` [readme] ventilation: Ventilation is about bringing in fresh air.

- rationale: You explain, to a patient, why one phrase in a medical sentence was replaced with another.
- audit: coverage 0.0, grounding_error=False, omission=True, source_ok=True, passage_ok=True

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

**output:** Once the abdomen was opened, there was noted to be gross purulent drainage.

| metric | value |
|---|---:|
| bertscore_f1 | 0.801 |
| coleman_liau | 9.14 |
| coleman_liau_drop | 0.00 |
| copy_jargon_rate | 1.000 |
| critical_error | 0.000 |
| fkgl | 7.63 |
| fkgl_drop | 0.00 |
| fre | 63.5 |
| fre_gain | 0.0 |
| human_edit_recall | 0.000 |
| length_ratio | 0.87 |
| n_words | 13.0 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.994 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 28.27 |
| smog | 11.21 |
| smog_drop | 0.00 |

### Stage 4 - arm `termonly`

**output:** Once the belly was opened, there was noted to be a lot of thick yellow-green pus draining.

| metric | value |
|---|---:|
| bertscore_f1 | 0.857 |
| coleman_liau | 6.68 |
| coleman_liau_drop | 2.46 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.600 |
| fkgl | 7.00 |
| fkgl_drop | 0.63 |
| fre | 75.1 |
| fre_gain | 11.6 |
| human_edit_recall | 1.000 |
| length_ratio | 1.20 |
| n_words | 18.0 |
| nli_completeness | 0.968 |
| nli_faithfulness | 0.009 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 63.89 |
| smog | 8.84 |
| smog_drop | 2.37 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `abdomen` -> `belly` | replace | - | - | - | - | - | - | - |
| `gross purulent drainage` -> `a lot of thick yellow-green pus draining` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Once the belly was opened, there was noted to be a lot of pus leaking out.

| metric | value |
|---|---:|
| bertscore_f1 | 0.875 |
| coleman_liau | 3.01 |
| coleman_liau_drop | 6.13 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.600 |
| fkgl | 5.40 |
| fkgl_drop | 2.23 |
| fre | 84.8 |
| fre_gain | 21.4 |
| human_edit_recall | 1.000 |
| length_ratio | 1.07 |
| n_words | 16.0 |
| nli_completeness | 0.961 |
| nli_faithfulness | 0.907 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 67.45 |
| smog | 3.13 |
| smog_drop | 8.08 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `abdomen` -> `belly` | replace | attributed | -0.033 | -1.352 | 0.399 | 0.663 | 0.194 | - |
| `gross purulent drainage` -> `a lot of pus leaking out` | replace | attributed | 3.924 | 4.107 | 0.898 | 0.932 | 2.402 | - |

**edit `abdomen` -> `belly`**

- status: `attributed`
- log p full -0.0448, empty -0.0118
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+1.032` [wiktionary] gross: The gross amount is the total before you take away losses or expenses.
    - `+0.838` [wiktionary] gross: A gross violation or abuse is very bad and clearly wrong.
    - `+0.538` [michigan] purulent: Pus.
    - `+0.513` [wiktionary] abdomen: The abdomen is the last of the three parts of an insect's body.
    - `+0.235` [nih] abdomen: The area of the body that contains the pancreas, stomach, intestines, liver, gallbladder, and other o

- rationale: The original term refers to the large cavity in the trunk that holds the digestive organs, and "belly" carries that meaning in everyday language as the front part of the torso where those organs sit. Phrase frequency increases from Zipf 3.56 to 4.10, while age of acquisition falls from 8.61 to 4.05. Readers can now picture the body region without needing anatomical vocabulary.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `gross purulent drainage` -> `a lot of pus leaking out`**

- status: `attributed`
- log p full -1.7672, empty -5.6907
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+3.034` [readme] drainage: When any fluid is leaking out of a body part.
    - `+0.632` [michigan] purulent: Pus.
    - `+0.369` [wiktionary] drainage: To use a drainage is engage in the action or process of draining something.
    - `+0.142` [wiktionary] gross: The gross amount is the total before you take away losses or expenses.

- rationale: The readme describes gross purulent drainage as any fluid leaking out of a body part, so "a lot of pus leaking out" keeps that idea of visible discharge in plain words. Phrase frequency rises from Zipf 1.92 to 2.94, while age of acquisition falls from 15.50 to 7.78. Readers can picture the amount and nature of the discharge without needing the medical label.
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

**output:** Once all four ports were placed, the right upper quadrant was then explored.

| metric | value |
|---|---:|
| bertscore_f1 | 0.742 |
| coleman_liau | 9.58 |
| coleman_liau_drop | 0.00 |
| copy_jargon_rate | 1.000 |
| critical_error | 0.000 |
| fkgl | 4.00 |
| fkgl_drop | 0.00 |
| fre | 89.5 |
| fre_gain | 0.0 |
| human_edit_recall | 0.000 |
| laterality_preservation | 1.000 |
| length_ratio | 0.81 |
| n_words | 13.0 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.994 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 16.37 |
| smog | 3.13 |
| smog_drop | 0.00 |

### Stage 4 - arm `termonly`

**output:** Once all four small openings were placed, the upper right belly area was then looked into.

| metric | value |
|---|---:|
| bertscore_f1 | 0.753 |
| coleman_liau | 8.81 |
| coleman_liau_drop | 0.77 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.200 |
| fkgl | 7.61 |
| fkgl_drop | -3.61 |
| fre | 69.0 |
| fre_gain | -20.5 |
| human_edit_recall | 1.000 |
| laterality_preservation | 1.000 |
| length_ratio | 1.00 |
| n_words | 16.0 |
| nli_completeness | 0.980 |
| nli_faithfulness | 0.840 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 50.18 |
| smog | 11.21 |
| smog_drop | -8.08 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `ports` -> `small openings` | replace | - | - | - | - | - | - | - |
| `right upper quadrant` -> `upper right belly area` | replace | - | - | - | - | - | - | - |
| `explored` -> `looked into` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Once all four entry points were placed, the upper right belly area was then looked at.

| metric | value |
|---|---:|
| bertscore_f1 | 0.717 |
| coleman_liau | 7.36 |
| coleman_liau_drop | 2.22 |
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
| nli_completeness | 0.981 |
| nli_faithfulness | 0.944 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 50.18 |
| smog | 8.84 |
| smog_drop | -5.71 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `ports` -> `entry points` | replace | attributed | 0.195 | 0.246 | 0.479 | 0.742 | 0.100 | - |
| `right upper quadrant` -> `upper right belly area` | replace | attributed | -0.039 | -0.072 | 0.111 | 0.667 | 0.278 | - |
| `explored` -> `looked at` | replace | attributed | -0.123 | -0.241 | 0.051 | 0.639 | 0.051 | - |

**edit `ports` -> `entry points`**

- status: `attributed`
- log p full -1.4829, empty -1.6778
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+0.227` [wiktionary] ports: A port is a place for ships to stop to trade or refuel.
    - `+0.127` [wiktionary] explored: If you explore a possibility, plan, idea, etc. you think about it carefully.
    - `+0.036` [readme] Right Upper Lobe: The upper right part of the right lung.

- rationale: The original term "ports" refers to openings or connections, and "entry points" carries that same idea of places where something can go in or out. Phrase frequency increases from Zipf 4.07 to 4.56, while syllable count rises from 1 to 3. Readers can now picture the concept as accessible locations rather than a technical label.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `right upper quadrant` -> `upper right belly area`**

- status: `attributed`
- log p full -0.8062, empty -0.7669
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+0.278` [readme] Right Upper Lobe: The upper right part of the right lung.
    - `-0.093` [wiktionary] ports: A port is a place for ships to stop to trade or refuel.
    - `-0.197` [readme] right upper lobe: A section of the right lung.

- rationale: The original term refers to the right upper part of the abdomen, and the replacement carries that meaning by naming the upper right belly area in plain words. Phrase frequency increases from Zipf 3.26 to 3.99, while age of acquisition falls from 12.76 to 7.56. Readers can now locate the region without needing anatomical terminology.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `explored` -> `looked at`**

- status: `attributed`
- log p full -0.7755, empty -0.6527
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+0.206` [wiktionary] explored: If you explore a possibility, plan, idea, etc. you think about it carefully.
    - `+0.155` [wiktionary] ports: A port is a place for ships to stop to trade or refuel.
    - `+0.074` [dictionary] Quadrant (n.): The quarter of a circle, or of the circumference of a circle, an arc of 90, or one subtending a

- rationale: The original term "explored" means examined or investigated, and "looked at" carries that same sense of visual inspection in plain words. Phrase frequency increases from Zipf 3.90 to 5.10, while syllable count stays the same at 2. Readers can grasp that something was inspected without needing a more formal verb.
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

**output:** Options such as watchful waiting, robotic prostatectomy, seed implantation with and without radiation were discussed.

| metric | value |
|---|---:|
| bertscore_f1 | 0.739 |
| coleman_liau | 20.89 |
| coleman_liau_drop | 0.00 |
| copy_jargon_rate | 1.000 |
| critical_error | 0.000 |
| fkgl | 15.43 |
| fkgl_drop | 0.00 |
| fre | 11.1 |
| fre_gain | 0.0 |
| human_edit_recall | 0.000 |
| length_ratio | 0.65 |
| n_words | 15.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.994 |
| replacement_f1 | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 24.31 |
| smog | 14.55 |
| smog_drop | 0.00 |

### Stage 4 - arm `termonly`

**output:** The patient talked about waiting and watching, surgery by robot to remove the prostate, and putting seeds in with and without rays.

| metric | value |
|---|---:|
| bertscore_f1 | 0.475 |
| coleman_liau | 11.06 |
| coleman_liau_drop | 9.83 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.571 |
| fkgl | 10.69 |
| fkgl_drop | 4.74 |
| fre | 57.6 |
| fre_gain | 46.5 |
| human_edit_recall | 1.000 |
| length_ratio | 0.96 |
| n_words | 22.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.447 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 25.82 |
| smog | 8.84 |
| smog_drop | 5.71 |

annotation backend `novita`, 4 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `watchful waiting` -> `waiting and watching` | replace | - | - | - | - | - | - | - |
| `robotic prostatectomy` -> `surgery by robot to remove the prostate` | replace | - | - | - | - | - | - | - |
| `seed implantation` -> `putting seeds in` | replace | - | - | - | - | - | - | - |
| `radiation` -> `rays` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Options such as close watch with no treatment for now, robot-assisted prostate removal, and placing tiny radioactive seeds in the prostate with and without high-energy rays to kill cancer cells were discussed.

| metric | value |
|---|---:|
| bertscore_f1 | 0.521 |
| coleman_liau | 14.63 |
| coleman_liau_drop | 6.26 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.429 |
| fkgl | 16.80 |
| fkgl_drop | -1.37 |
| fre | 31.6 |
| fre_gain | 20.5 |
| human_edit_recall | 1.000 |
| length_ratio | 1.48 |
| n_words | 34.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.993 |
| nli_faithfulness | 0.490 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 38.75 |
| smog | 14.55 |
| smog_drop | 0.00 |

annotation backend `novita`, 4 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `watchful waiting` -> `close watch with no treatment for now` | replace | attributed | 7.252 | 7.284 | 0.904 | 0.896 | 5.537 | - |
| `robotic prostatectomy` -> `robot-assisted prostate removal` | replace | attributed | 1.844 | 1.900 | 0.770 | 0.927 | 1.055 | - |
| `seed implantation` -> `placing tiny radioactive seeds in the prostate` | replace | attributed | 0.944 | 0.963 | 0.493 | 0.565 | 0.399 | - |
| `radiation` -> `high-energy rays to kill cancer cells` | replace | attributed | 12.799 | 13.406 | 0.862 | 0.885 | 9.608 | - |

**edit `watchful waiting` -> `close watch with no treatment for now`**

- status: `attributed`
- log p full -3.4495, empty -10.7010
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+5.816` [nih] watchful waiting: Closely watching a patient’s condition but not giving treatment unless symptoms appear or ch
    - `+0.279` [nih] prostatectomy: Surgery to remove part or all of the prostate and some of the tissue around it, including the s
    - `+0.083` [readme] implantation: Surgery where a device is placed inside your body.
    - `+0.054` [readme] prostatectomy: A prostatectomy is a surgery to remove part or all of the prostate and some surrounding tissue.
    - `+0.046` [readme] IMPLANTATION: A surgery where a device is placed inside the body.

- rationale: The source describes watchful waiting as closely watching a condition without giving treatment unless symptoms appear or change, so "close watch with no treatment for now" keeps that monitoring-without-intervention idea in plain words. Phrase frequency rises from Zipf 3.09 to 4.70, while age of acquisition falls from 8.16 to 8.11. Patients can grasp that the plan is observation rather than immediate therapy.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `robotic prostatectomy` -> `robot-assisted prostate removal`**

- status: `attributed`
- log p full -2.7510, empty -4.5949
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+1.331` [nih] watchful waiting: Closely watching a patient’s condition but not giving treatment unless symptoms appear or ch
    - `+0.276` [readme] prostatectomy: A prostatectomy is a surgery to remove part or all of the prostate and some surrounding tissue.
    - `+0.120` [readme] implantation: Surgery where a device is placed inside your body.
    - `+0.044` [wiktionary] seed: The seed of a man is his semen.
    - `+0.008` [readme] IMPLANTATION: A surgery where a device is placed inside the body.

- rationale: You explain, to a patient, why one phrase in a medical sentence was replaced with another.
- audit: coverage 0.0, grounding_error=False, omission=True, source_ok=True, passage_ok=True

**edit `seed implantation` -> `placing tiny radioactive seeds in the prostate`**

- status: `attributed`
- log p full -3.5165, empty -4.4608
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+0.425` [readme] radiation: High energy rays used to kill cancer cells.
    - `+0.026` [wiktionary] radiation: Radiation is the emission or transmission of energy in the form of waves or particles through space

- rationale: The original term refers to putting small radioactive particles into the prostate, and the replacement spells out that placement in plain words. Phrase frequency rises from Zipf 2.99 to 3.26, while age of acquisition rises from 11.95 to 15.00. Readers can picture the procedure without needing the technical label.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `radiation` -> `high-energy rays to kill cancer cells`**

- status: `attributed`
- log p full -0.7865, empty -13.5851
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+10.970` [readme] radiation: High energy rays used to kill cancer cells.
    - `+1.363` [readme] Radiation: Radiation is powerful energy waves that are sometimes utilized to destroy cancer cells.
    - `+1.316` [readme] IMPLANTATION: A surgery where a device is placed inside the body.
    - `+0.798` [thesaurus] radiation: see ionizing radiation and non-ionizing radiation
    - `+0.515` [wiktionary] seed: A seed is a small round thing that can grow to be a plant, a flower or a tree.

- rationale: The source describes radiation as high energy rays used to kill cancer cells, so "high-energy rays to kill cancer cells" keeps that treatment meaning in plain words. Phrase frequency decreases from Zipf 4.27 to 3.86, while age of acquisition falls from 11.44 to 8.39. Patients can understand the therapy is targeted energy for cancer without needing the technical term.
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

**output:** He was also said to have been on Lasix before he was hospitalized, possibly.

| metric | value |
|---|---:|
| bertscore_f1 | 0.565 |
| coleman_liau | 7.36 |
| coleman_liau_drop | 6.36 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.333 |
| fkgl | 7.57 |
| fkgl_drop | 6.70 |
| fre | 65.7 |
| fre_gain | 55.2 |
| human_edit_recall | 1.000 |
| length_ratio | 0.93 |
| n_words | 14.0 |
| nli_completeness | 0.995 |
| nli_faithfulness | 0.993 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.250 |
| sari | 37.24 |
| smog | 11.21 |
| smog_drop | 1.82 |
| temporality_preservation | 1.000 |
| uncertainty_preservation | 1.000 |

### Stage 4 - arm `termonly`

**output:** He also was said to be on a medicine that helps the body get rid of extra water before being in the hospital, possible.

| metric | value |
|---|---:|
| bertscore_f1 | 0.407 |
| coleman_liau | 5.68 |
| coleman_liau_drop | 8.04 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 11.47 |
| fkgl_drop | 2.80 |
| fre | 55.6 |
| fre_gain | 45.0 |
| human_edit_recall | 1.000 |
| length_ratio | 1.60 |
| n_words | 24.0 |
| nli_completeness | 0.010 |
| nli_faithfulness | 0.252 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 49.80 |
| smog | 13.02 |
| smog_drop | 0.00 |
| temporality_preservation | 1.000 |
| uncertainty_preservation | 1.000 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `reportedly` -> `was said to be` | replace | - | - | - | - | - | - | - |
| `Lasix` -> `a medicine that helps the body get rid of extra water` | replace | - | - | - | - | - | - | - |
| `prior to` -> `before` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** He also people say he was on a medicine that helps the body get rid of extra water before being admitted to a hospital, possible

| metric | value |
|---|---:|
| bertscore_f1 | 0.375 |
| coleman_liau | 6.91 |
| coleman_liau_drop | 6.81 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.750 |
| fkgl | 13.04 |
| fkgl_drop | 1.23 |
| fre | 46.1 |
| fre_gain | 35.5 |
| human_edit_recall | 1.000 |
| length_ratio | 1.67 |
| n_words | 25.0 |
| nli_completeness | 0.025 |
| nli_faithfulness | 0.272 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 45.12 |
| smog | 14.55 |
| smog_drop | -1.53 |
| temporality_preservation | 1.000 |
| uncertainty_preservation | 1.000 |

annotation backend `novita`, 4 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `reportedly` -> `people say` | replace | attributed | 9.247 | 11.076 | 0.900 | 0.886 | 10.275 | - |
| `Lasix` -> `a medicine that helps the body get rid of extra water` | replace | attributed | 1.305 | 1.435 | 0.865 | 0.851 | 0.383 | - |
| `prior to` -> `before` | replace | attributed | 0.035 | 0.135 | 0.801 | 0.795 | 0.034 | - |
| `hospitalization` -> `a hospital` | replace | attributed | 1.319 | 1.979 | 0.762 | 0.886 | 2.903 | - |

**edit `reportedly` -> `people say`**

- status: `attributed`
- log p full -0.1750, empty -9.4217
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+10.752` [wiktionary] reportedly: If something is reportedly true, people say it happened, but we don't have other reasons to believ
    - `+0.476` [readme] hospitalization: Being admitted to and staying in a hospital.
    - `+0.177` [readme] Hospitalization: Being admitted to a hospital for an extended period of time.
    - `-0.018` [wiktionary] hospitalization: Hospitalization is the process of putting a person in hospital for medical care.
    - `-0.039` [wiktionary] hospitalization: Hospitalization is the period of time when a person is in hospital for medical care.

- rationale: The source describes reportedly as something people say happened but without other reasons to believe it, so "people say" keeps that sense of hearsay in plain words. Phrase frequency increases from Zipf 4.13 to 5.73, while syllables fall from 4 to 3. Readers can now see the claim is second-hand rather than confirmed.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `Lasix` -> `a medicine that helps the body get rid of extra water`**

- status: `attributed`
- log p full -1.8289, empty -3.1335
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+0.383` [wiktionary] reportedly: If something is reportedly true, people say it happened, but we don't have other reasons to believ

- rationale: You explain, to a patient, why one phrase in a medical sentence was replaced with another.
- audit: coverage 0.0, grounding_error=False, omission=True, source_ok=True, passage_ok=True

**edit `prior to` -> `before`**

- status: `attributed`
- log p full -0.2866, empty -0.3220
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+0.252` [wiktionary] hospitalization: Hospitalization is the period of time when a person is in hospital for medical care.
    - `+0.218` [wiktionary] reportedly: If something is reportedly true, people say it happened, but we don't have other reasons to believ
    - `+0.203` [wiktionary] hospitalization: Hospitalization is the process of putting a person in hospital for medical care.
    - `+0.070` [readme] Hospitalization: Being admitted to a hospital for an extended period of time.
    - `+0.028` [readme] hospitalization: Being admitted to and staying in a hospital.

- rationale: You explain, to a patient, why one phrase in a medical sentence was replaced with another.
- audit: coverage 0.0, grounding_error=False, omission=True, source_ok=True, passage_ok=True

**edit `hospitalization` -> `a hospital`**

- status: `attributed`
- log p full -0.5785, empty -1.8971
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+3.112` [readme] Hospitalization: Being admitted to a hospital for an extended period of time.
    - `+0.209` [wiktionary] reportedly: If something is reportedly true, people say it happened, but we don't have other reasons to believ
    - `-0.013` [wiktionary] hospitalization: Hospitalization is the period of time when a person is in hospital for medical care.
    - `-0.042` [wiktionary] hospitalization: Hospitalization is the process of putting a person in hospital for medical care.
    - `-0.131` [michigan] prior to: Earlier or before.

- rationale: The readme describes hospitalization as being admitted to a hospital for an extended period of time, so "a hospital" keeps the core idea of being in a hospital in plain words. Phrase frequency rises from Zipf 3.09 to 5.07, while age of acquisition falls from 9.53 to 5.55. Readers can grasp the setting without needing the formal medical term.
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

**output:** The four chambers of the heart are normal in size.

| metric | value |
|---|---:|
| bertscore_f1 | 0.658 |
| coleman_liau | 4.44 |
| coleman_liau_drop | 10.63 |
| copy_jargon_rate | 0.250 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.167 |
| fkgl | 2.47 |
| fkgl_drop | 7.74 |
| fre | 95.2 |
| fre_gain | 57.3 |
| human_edit_recall | 0.750 |
| length_ratio | 0.77 |
| n_words | 10.0 |
| nli_completeness | 0.958 |
| nli_faithfulness | 0.977 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 0.857 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 41.72 |
| smog | 3.13 |
| smog_drop | 8.08 |

### Stage 4 - arm `termonly`

**output:** The four heart rooms sizes are normal.

| metric | value |
|---|---:|
| bertscore_f1 | 0.491 |
| coleman_liau | 5.66 |
| coleman_liau_drop | 9.41 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.143 |
| fkgl | 2.31 |
| fkgl_drop | 7.90 |
| fre | 91.0 |
| fre_gain | 53.1 |
| human_edit_recall | 1.000 |
| length_ratio | 0.54 |
| n_words | 7.0 |
| nli_completeness | 0.958 |
| nli_faithfulness | 0.965 |
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
| `cardiac chambers` -> `heart rooms` | replace | - | - | - | - | - | - | - |
| `dimensions` -> `sizes` | replace | - | - | - | - | - | - | - |
| `within normal limits` -> `normal` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** The four heart rooms sizes are as expected for a person similar to you.

| metric | value |
|---|---:|
| bertscore_f1 | 0.449 |
| coleman_liau | 5.70 |
| coleman_liau_drop | 9.37 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.250 |
| fkgl | 6.73 |
| fkgl_drop | 3.48 |
| fre | 71.8 |
| fre_gain | 33.9 |
| human_edit_recall | 1.000 |
| length_ratio | 1.08 |
| n_words | 14.0 |
| nli_completeness | 0.933 |
| nli_faithfulness | 0.183 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 32.94 |
| smog | 11.21 |
| smog_drop | 0.00 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `cardiac chambers` -> `heart rooms` | replace | attributed | 0.258 | 0.761 | 0.892 | 0.927 | 2.324 | - |
| `dimensions` -> `sizes` | replace | attributed | 0.438 | 1.200 | 0.623 | 0.837 | 0.374 | - |
| `within normal limits` -> `as expected for a person similar to you` | replace | attributed | 29.187 | 29.286 | 0.843 | 0.934 | 26.192 | - |

**edit `cardiac chambers` -> `heart rooms`**

- status: `attributed`
- log p full -0.2989, empty -0.5573
- masks scored: 66/66 (+5 top-k)
- ranked sources:
    - `+2.340` [wiktionary] chambers: A chamber is a room that is often used for sleeping.
    - `+0.015` [justplainclear] limits: A certain point that you can't go past; a certain amount but no more

- rationale: The original term refers to the four muscular compartments of the heart that receive and pump blood, and “heart rooms” keeps that idea of internal spaces that hold blood in plain language. Phrase frequency rises from Zipf 3.64 to 4.49, while age of acquisition falls from 11.74 to 5.17. Readers can picture where blood is held and moved inside the heart without needing anatomical terminology.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `dimensions` -> `sizes`**

- status: `attributed`
- log p full -0.2703, empty -0.7084
- masks scored: 66/66 (+5 top-k)
- ranked sources:
    - `+0.485` [wiktionary] chambers: A chamber is a room that is often used for sleeping.
    - `+0.111` [michigan] cardiac: Related to your heart.
    - `+0.078` [wiktionary] normal: A normal thing, or situation, is one that is not special.
    - `+0.076` [readme] cardiac: Related to the heart.
    - `+0.062` [wiktionary] within: before the time ends

- rationale: The original term "dimensions" refers to measurable extents such as length, width, and height, and "sizes" carries that same idea of how big or large something is in plain words. Phrase frequency increases from Zipf 4.05 to 4.18, while syllable count falls from 3 to 2. Readers can grasp the intended scale information without needing the more technical word.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `within normal limits` -> `as expected for a person similar to you`**

- status: `attributed`
- log p full -2.3590, empty -31.5461
- masks scored: 66/66 (+5 top-k)
- ranked sources:
    - `+26.361` [justplainclear] normal: Whats expected for a person similar to you or to what's usual for you
    - `+0.169` [wiktionary] chambers: A chamber is a room that is often used for sleeping.

- rationale: The source describes within normal limits as what is expected for a person similar to you or what is usual for you, so "as expected for a person similar to you" keeps that comparative, person-referenced meaning in plain words. Phrase frequency rises from Zipf 4.32 to 4.69, while age of acquisition falls from 7.65 to 7.33. Readers can see the result is being judged against a relevant peer group rather than an abstract range.
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

**output:** The doctor checked the rectum with a finger and did not feel any lumps.

| metric | value |
|---|---:|
| bertscore_f1 | 0.456 |
| coleman_liau | 5.70 |
| coleman_liau_drop | 10.66 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.667 |
| fkgl | 5.04 |
| fkgl_drop | 6.48 |
| fre | 83.9 |
| fre_gain | 55.4 |
| human_edit_recall | 1.000 |
| length_ratio | 1.27 |
| n_words | 14.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.698 |
| nli_faithfulness | 0.056 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.286 |
| sari | 19.11 |
| smog | 3.13 |
| smog_drop | 8.08 |

### Stage 4 - arm `termonly`

**output:** A finger check of the back passage was done, which showed no lumps.

| metric | value |
|---|---:|
| bertscore_f1 | 0.812 |
| coleman_liau | 5.57 |
| coleman_liau_drop | 10.79 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.333 |
| fkgl | 3.10 |
| fkgl_drop | 8.42 |
| fre | 96.0 |
| fre_gain | 67.5 |
| human_edit_recall | 1.000 |
| length_ratio | 1.18 |
| n_words | 13.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.075 |
| nli_faithfulness | 0.361 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 56.51 |
| smog | 3.13 |
| smog_drop | 8.08 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `Digital rectal examination` -> `finger check of the back passage` | replace | - | - | - | - | - | - | - |
| `performed` -> `done` | replace | - | - | - | - | - | - | - |
| `masses` -> `lumps` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** A finger check of the rectum was done, which showed no lumps.

| metric | value |
|---|---:|
| bertscore_f1 | 0.709 |
| coleman_liau | 4.93 |
| coleman_liau_drop | 11.42 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.333 |
| fkgl | 2.86 |
| fkgl_drop | 8.66 |
| fre | 96.0 |
| fre_gain | 67.5 |
| human_edit_recall | 1.000 |
| length_ratio | 1.09 |
| n_words | 12.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.128 |
| nli_faithfulness | 0.198 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 46.35 |
| smog | 3.13 |
| smog_drop | 8.08 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `Digital rectal examination` -> `finger check of the rectum` | replace | attributed | 0.547 | 0.615 | - | 0.680 | 0.645 | - |
| `performed` -> `done` | replace | attributed | -0.001 | -1.333 | - | 0.724 | 0.487 | - |
| `masses` -> `lumps` | replace | attributed | 0.003 | 0.410 | - | 0.865 | 1.037 | - |

**edit `Digital rectal examination` -> `finger check of the rectum`**

- status: `attributed`
- log p full -1.9422, empty -2.4888
- masks scored: 18/18 (+4 top-k)
- ranked sources:
    - `+0.686` [nih] digital rectal examination: An examination in which a doctor inserts a lubricated, gloved finger into the rect
    - `+0.041` [wiktionary] performed: When you perform something, you do it.
    - `+0.019` [wiktionary] masses: A measure of how much material is in something.

- rationale: A digital rectal examination is a physical exam in which a clinician inserts a gloved finger into the rectum to feel internal structures, so “finger check of the rectum” conveys the same procedure in plain language. Phrase frequency rises from Zipf 2.88 to 2.94, while age of acquisition falls from 13.06 to 9.84. Readers can grasp what the exam involves without specialized medical vocabulary.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `performed` -> `done`**

- status: `attributed`
- log p full -0.0010, empty -0.0003
- masks scored: 18/18 (+4 top-k)
- ranked sources:
    - `+0.212` [wiktionary] performed: When you perform something, you do it.
    - `-0.275` [wiktionary] masses: A measure of how much material is in something.
    - `-0.474` [nih] digital rectal examination: An examination in which a doctor inserts a lubricated, gloved finger into the rect
    - `-0.812` [wiktionary] masses: The masses are the regular people, not those in power.

- rationale: The original term "performed" means carried out or executed, and "done" carries that same sense of completion in everyday language. Word frequency rises from Zipf 4.68 to 5.58, while syllables drop from 2 to 1. Readers can grasp that an action was completed without needing a more formal verb.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `masses` -> `lumps`**

- status: `attributed`
- log p full -0.0068, empty -0.0103
- masks scored: 18/18 (+4 top-k)
- ranked sources:
    - `+0.990` [nih] digital rectal examination: An examination in which a doctor inserts a lubricated, gloved finger into the rect
    - `-0.047` [wiktionary] performed: When you perform something, you do it.
    - `-0.140` [wiktionary] masses: The masses are the regular people, not those in power.
    - `-0.366` [wiktionary] masses: A measure of how much material is in something.

- rationale: The original term refers to solid growths or swellings in the body, and "lumps" carries that same idea of a noticeable, localized bump in plain language. Phrase frequency decreases from Zipf 3.94 to 3.19, while syllables fall from 2 to 1. Readers can picture the physical finding without needing a clinical label.
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

**output:** He then had seizures and weakness on one side of the body, went to the hospital, developed C. diff, and is now in a nursing home.

| metric | value |
|---|---:|
| bertscore_f1 | 0.660 |
| coleman_liau | 4.01 |
| coleman_liau_drop | 6.27 |
| copy_jargon_rate | 0.333 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 4.91 |
| fkgl_drop | 6.32 |
| fre | 83.0 |
| fre_gain | 29.2 |
| human_edit_recall | 0.667 |
| length_ratio | 0.90 |
| n_words | 26.0 |
| nli_completeness | 0.017 |
| nli_faithfulness | 0.974 |
| replacement_f1 | 0.800 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.600 |
| sari | 31.42 |
| smog | 8.84 |
| smog_drop | 5.71 |
| temporality_preservation | 1.000 |

### Stage 4 - arm `termonly`

**output:** He then had a problem with fits, weakness on one side of the body, has been to the hospital, developed a C. difficile infection, and is in the nursing home currently.

| metric | value |
|---|---:|
| bertscore_f1 | 0.834 |
| coleman_liau | 6.61 |
| coleman_liau_drop | 3.66 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.667 |
| fkgl | 7.58 |
| fkgl_drop | 3.64 |
| fre | 68.3 |
| fre_gain | 14.5 |
| human_edit_recall | 1.000 |
| length_ratio | 1.07 |
| n_words | 31.0 |
| nli_completeness | 0.011 |
| nli_faithfulness | 0.943 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 80.90 |
| smog | 12.16 |
| smog_drop | 2.39 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `seizures` -> `fits` | replace | - | - | - | - | - | - | - |
| `hemiparesis` -> `weakness on one side of the body` | replace | - | - | - | - | - | - | - |
| `C-diff` -> `a C. difficile infection` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** He then had a problem with brain events that can cause loss of consciousness and jerky movements, weakness on one side of the body, has been to the hospital, developed a gut infection that causes fever, diarrhea, and cramps, and is in the nursing home currently.

| metric | value |
|---|---:|
| bertscore_f1 | 0.683 |
| coleman_liau | 10.03 |
| coleman_liau_drop | 0.24 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 19.79 |
| fkgl_drop | -8.57 |
| fre | 35.1 |
| fre_gain | -18.7 |
| human_edit_recall | 1.000 |
| length_ratio | 1.59 |
| n_words | 46.0 |
| nli_completeness | 0.119 |
| nli_faithfulness | 0.607 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 72.45 |
| smog | 17.12 |
| smog_drop | -2.57 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `seizures` -> `brain events that can cause loss of consciousness and jerky movements` | replace | attributed | 23.382 | 23.387 | 0.842 | 0.848 | 0.519 | - |
| `hemiparesis` -> `weakness on one side of the body` | replace | attributed | 0.205 | 1.003 | 0.728 | 0.802 | 0.581 | - |
| `C-diff` -> `a gut infection that causes fever, diarrhea, and cramps` | replace | attributed | 21.184 | 21.290 | 0.776 | 0.856 | 22.734 | - |

**edit `seizures` -> `brain events that can cause loss of consciousness and jerky movements`**

- status: `attributed`
- log p full -5.3110, empty -28.6933
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+11.655` [readme] Seizures: Seizures are when the brain has sudden abnormal activity that can lead to loss of consciousness and 
    - `+11.136` [readme] seizures: Seizures are when the brain has strange electrical activity that may make someone lose consciousness
    - `+0.843` [nih] Clostridium difficile: A type of bacterium found in human and animal waste. Clostridium difficile is a common 
    - `+0.377` [readme] hemiparesis: Weakness on one side of the body.
    - `-0.058` [dorland] C-diff: Clostridioides difficile

- rationale: The readme describes seizures as sudden abnormal brain activity that can lead to loss of consciousness and muscle movements, so "brain events that can cause loss of consciousness and jerky movements" keeps that core idea in plain words. Phrase frequency decreases from Zipf 3.59 to 3.03, while syllables increase from 2 to 16. Patients can picture what happens during an episode without needing the clinical label.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `hemiparesis` -> `weakness on one side of the body`**

- status: `attributed`
- log p full -0.1410, empty -0.3457
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+0.634` [readme] hemiparesis: Weakness on one side of the body.
    - `+0.052` [readme] seizures: Seizures are when the brain has strange electrical activity that may make someone lose consciousness
    - `+0.038` [wiktionary] seizures: If someone seizes (takes) something from someone by force, or arrests someone, it is a seizure.

- rationale: You explain, to a patient, why one phrase in a medical sentence was replaced with another.
- audit: coverage 0.0, grounding_error=False, omission=True, source_ok=True, passage_ok=True

**edit `C-diff` -> `a gut infection that causes fever, diarrhea, and cramps`**

- status: `attributed`
- log p full -2.2974, empty -23.4812
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+22.777` [readme] Clostridium difficile colitis: A type of gut infection that causes symptoms like fever, diarrhea, and cramps.
    - `+0.043` [wiktionary] seizures: If someone seizes (takes) something from someone by force, or arrests someone, it is a seizure.

- rationale: The readme describes C-diff as a type of gut infection that causes symptoms like fever, diarrhea, and cramps, so "a gut infection that causes fever, diarrhea, and cramps" keeps that cause-and-effect meaning in plain words. Syllables increase from 2 to 16. Patients can understand the basic heart-rhythm problem without first knowing the diagnostic name.
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

**output:** He has been using continuous positive airway pressure for several months and is back for a follow-up visit to review how the treatment is working.

| metric | value |
|---|---:|
| bertscore_f1 | 0.703 |
| coleman_liau | 10.86 |
| coleman_liau_drop | 1.79 |
| copy_jargon_rate | 0.833 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 13.04 |
| fkgl_drop | -0.74 |
| fre | 46.1 |
| fre_gain | 0.0 |
| human_edit_recall | 0.167 |
| length_ratio | 1.04 |
| n_words | 26.0 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.993 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 0.286 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 53.82 |
| smog | 13.02 |
| smog_drop | 0.00 |
| temporality_preservation | 0.000 |

### Stage 4 - arm `termonly`

**output:** He has been on a machine that keeps air pressure up in the lungs now for several months, and returns for a check-in to review his response to treatment.

| metric | value |
|---|---:|
| bertscore_f1 | 0.700 |
| coleman_liau | 7.38 |
| coleman_liau_drop | 5.27 |
| copy_jargon_rate | 0.167 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 10.37 |
| fkgl_drop | 1.93 |
| fre | 72.4 |
| fre_gain | 26.3 |
| human_edit_recall | 0.833 |
| length_ratio | 1.20 |
| n_words | 30.0 |
| nli_completeness | 0.961 |
| nli_faithfulness | 0.903 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 60.97 |
| smog | 3.13 |
| smog_drop | 9.89 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `continuous positive airway pressure` -> `a machine that keeps air pressure up in the lungs` | replace | - | - | - | - | - | - | - |
| `followup` -> `a check-in` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** He has been on a machine that keeps air pressure in his breathing tube now for several months, and returns for a checkup to review his response to treatment.

| metric | value |
|---|---:|
| bertscore_f1 | 0.705 |
| coleman_liau | 8.58 |
| coleman_liau_drop | 4.07 |
| copy_jargon_rate | 0.167 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.200 |
| fkgl | 11.18 |
| fkgl_drop | 1.12 |
| fre | 66.5 |
| fre_gain | 20.5 |
| human_edit_recall | 0.833 |
| length_ratio | 1.16 |
| n_words | 29.0 |
| nli_completeness | 0.919 |
| nli_faithfulness | 0.810 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 0.909 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 60.25 |
| smog | 3.13 |
| smog_drop | 9.89 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `continuous positive airway pressure` -> `a machine that keeps air pressure in his breathing tube` | replace | attributed | 3.720 | 3.735 | 0.473 | 0.797 | 1.612 | - |
| `followup` -> `a checkup` | replace | attributed | 2.269 | 2.813 | 0.918 | 0.951 | 5.403 | - |

**edit `continuous positive airway pressure` -> `a machine that keeps air pressure in his breathing tube`**

- status: `attributed`
- log p full -4.1700, empty -7.8897
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+2.325` [wiktionary] airway: The airway in our body refers to the trachea.
    - `+0.713` [wiktionary] airway: An airway is a path an aircraft takes.
    - `+0.529` [readme] Positive: Something is there.
    - `+0.270` [wiktionary] continuous: Something that is continuous happens without stopping.
    - `+0.217` [wiktionary] positive: If you are positive about something, you are sure that you are not mistaken.

- rationale: The source describes the airway as the trachea, so "a machine that keeps air pressure in his breathing tube" keeps the idea of pressure support applied to the trachea in plain words. Phrase frequency rises from Zipf 3.14 to 3.84, while age of acquisition falls from 11.39 to 8.95. Patients can picture the device’s role in the breathing passage without needing the technical name.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `followup` -> `a checkup`**

- status: `attributed`
- log p full -0.8064, empty -3.0756
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+5.913` [readme] followup: Going back to your doctor for a checkup or follow-up appointment.
    - `+0.509` [wiktionary] positive: If you are positive about something, you are sure that you are not mistaken.
    - `+0.327` [wiktionary] pressure: If a person is under pressure, they feel stressed.
    - `+0.240` [wiktionary] continuous: Something that is continuous happens without stopping.

- rationale: The source describes followup as going back to your doctor for a checkup or follow-up appointment, so "a checkup" keeps the idea of a return visit in plain words. Phrase frequency increases from Zipf 2.87 to 2.88, while syllable count stays the same at 3. Patients can understand the idea of a return visit without first knowing the clinical label.
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

**output:** The patient should take small bites and small sips to help lower the risk of aspiration and penetration.

| metric | value |
|---|---:|
| bertscore_f1 | 0.621 |
| coleman_liau | 10.27 |
| coleman_liau_drop | -0.64 |
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
| sari | 23.61 |
| severity_downgrade | 0.000 |
| severity_preservation | 1.000 |
| severity_tier_input | 1.000 |
| severity_tier_output | 1.000 |
| smog | 11.21 |
| smog_drop | 0.00 |

### Stage 4 - arm `termonly`

**output:** The patient should take small bites and small sips to help lower the risk of food or liquid going into the lungs and of food or liquid going past the voice box into the airway.

| metric | value |
|---|---:|
| bertscore_f1 | 0.588 |
| coleman_liau | 6.72 |
| coleman_liau_drop | 2.90 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 12.89 |
| fkgl_drop | -4.42 |
| fre | 65.0 |
| fre_gain | -1.4 |
| human_edit_recall | 1.000 |
| length_ratio | 1.17 |
| n_words | 35.0 |
| nli_completeness | 0.860 |
| nli_faithfulness | 0.376 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 38.48 |
| severity_downgrade | 0.000 |
| severity_preservation | 1.000 |
| severity_tier_input | 1.000 |
| severity_tier_output | 1.000 |
| smog | 3.13 |
| smog_drop | 8.08 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `aspiration` -> `food or liquid going into the lungs` | replace | - | - | - | - | - | - | - |
| `penetration` -> `food or liquid going past the voice box into the airway` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** The patient should take small bites and small sips to help lower the risk of breathing food or liquid into the lungs by mistake and of food or liquid going into the airways.

| metric | value |
|---|---:|
| bertscore_f1 | 0.603 |
| coleman_liau | 7.91 |
| coleman_liau_drop | 1.71 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 12.66 |
| fkgl_drop | -4.18 |
| fre | 63.1 |
| fre_gain | -3.3 |
| human_edit_recall | 1.000 |
| length_ratio | 1.10 |
| n_words | 33.0 |
| nli_completeness | 0.856 |
| nli_faithfulness | 0.947 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 38.48 |
| severity_downgrade | 0.000 |
| severity_preservation | 1.000 |
| severity_tier_input | 1.000 |
| severity_tier_output | 1.000 |
| smog | 3.13 |
| smog_drop | 8.08 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `aspiration` -> `breathing food or liquid into the lungs by mistake` | replace | attributed | 19.727 | 21.078 | 0.842 | 0.854 | 7.070 | - |
| `penetration` -> `food or liquid going into the airways` | replace | attributed | 1.598 | 1.660 | 0.635 | 0.368 | 0.050 | - |

**edit `aspiration` -> `breathing food or liquid into the lungs by mistake`**

- status: `attributed`
- log p full -0.3000, empty -20.0274
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+12.384` [readme] aspiration: Breathing food or liquid into your lungs by mistake.
    - `+5.314` [readme] aspiration: Breathing in food or liquid by mistake.
    - `+0.709` [nih] aspiration: Removal of fluid or tissue through a needle. Also, the accidental breathing in of food or fluid in
    - `+0.131` [iowa] ASPIRATION: fluid entering the lungs, such as after vomiting
    - `-0.475` [wiktionary] penetration: Penetration is the penis being inserted into the vagina or another part of the body during sex.

- rationale: The readme describes aspiration as breathing food or liquid into the lungs by mistake, so "breathing food or liquid into the lungs by mistake" restates that definition in plain words. Phrase frequency rises from Zipf 3.30 to 3.64, while age of acquisition falls from 11.47 to 6.52. Readers can grasp the risk without needing the medical label.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `penetration` -> `food or liquid going into the airways`**

- status: `attributed`
- log p full -2.5990, empty -4.1966
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.136` [readme] aspiration: Breathing in food or liquid by mistake.
    - `+0.086` [wiktionary] penetration: Penetration is the action of penetrating into something.

- rationale: The original term refers to something passing through a barrier or into a space, and the replacement makes that movement explicit by describing food or liquid going into the airways. Phrase frequency decreases from Zipf 3.71 to 3.62, while age of acquisition falls from 11.05 to 6.52. Readers can now picture the physical direction of the material without needing the abstract noun.
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

**output:** The patient woke up, the breathing tube was removed, and they were moved to the recovery room in good condition.

| metric | value |
|---|---:|
| bertscore_f1 | 0.740 |
| coleman_liau | 8.82 |
| coleman_liau_drop | 4.73 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.667 |
| fkgl | 8.14 |
| fkgl_drop | 4.15 |
| fre | 72.3 |
| fre_gain | 38.6 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 20.0 |
| nli_completeness | 0.990 |
| nli_faithfulness | 0.990 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 39.05 |
| smog | 11.21 |
| smog_drop | 4.70 |

### Stage 4 - arm `termonly`

**output:** The patient was woken up and the breathing tube was taken out and moved to the recovery room in good condition.

| metric | value |
|---|---:|
| bertscore_f1 | 0.791 |
| coleman_liau | 7.65 |
| coleman_liau_drop | 5.90 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.667 |
| fkgl | 8.90 |
| fkgl_drop | 3.39 |
| fre | 68.7 |
| fre_gain | 35.0 |
| human_edit_recall | 1.000 |
| length_ratio | 1.05 |
| n_words | 21.0 |
| nli_completeness | 0.986 |
| nli_faithfulness | 0.981 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 41.85 |
| smog | 11.21 |
| smog_drop | 4.70 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `awakened` -> `woken up` | replace | - | - | - | - | - | - | - |
| `extubated` -> `the breathing tube was taken out` | replace | - | - | - | - | - | - | - |
| `satisfactory` -> `good` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** The patient was woken up and the breathing tube was taken out and moved to the recovery room in good enough condition.

| metric | value |
|---|---:|
| bertscore_f1 | 0.775 |
| coleman_liau | 8.16 |
| coleman_liau_drop | 5.38 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.667 |
| fkgl | 9.62 |
| fkgl_drop | 2.67 |
| fre | 65.3 |
| fre_gain | 31.6 |
| human_edit_recall | 1.000 |
| length_ratio | 1.10 |
| n_words | 22.0 |
| nli_completeness | 0.990 |
| nli_faithfulness | 0.979 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 41.68 |
| smog | 11.21 |
| smog_drop | 4.70 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `awakened` -> `woken up` | replace | attributed | -0.104 | -0.239 | - | 0.247 | 0.000 | - |
| `extubated` -> `the breathing tube was taken out` | replace | attributed | -0.132 | -0.225 | - | 0.857 | 1.085 | - |
| `satisfactory` -> `good enough` | replace | attributed | 3.153 | 3.572 | - | 0.978 | 5.104 | - |

**edit `awakened` -> `woken up`**

- status: `attributed`
- log p full -0.6231, empty -0.5195
- masks scored: 34/34 (+5 top-k)
- ranked sources:
    - `-0.001` [michigan] satisfactory: When something is okay or good.
    - `-0.004` [wiktionary] awakened: If you awaken somebody, they stop sleeping because of something you do.
    - `-0.024` [readme] extubated: Taking out a tube used for breathing.

- rationale: The original term "awakened" means to become conscious after sleep or a period of unconsciousness, and "woken up" carries that same sense of coming out of sleep in everyday language. Phrase frequency increases from Zipf 3.30 to 3.37, while syllable count stays the same at 3. Readers can now see the change in state without needing a more formal verb.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `extubated` -> `the breathing tube was taken out`**

- status: `attributed`
- log p full -0.9510, empty -0.8189
- masks scored: 34/34 (+5 top-k)
- ranked sources:
    - `+1.085` [readme] extubated: Taking out a tube used for breathing.
    - `-1.015` [readme] extubated: Not having a breathing tube anymore.

- rationale: The original term means a person has had a breathing tube removed from their airway, and the replacement carries that meaning by describing the removal in plain words. Phrase frequency increases from Zipf 1.26 to 3.99, while syllable count rises from 4 to 8. Patients can understand that the tube is no longer in place without needing the clinical verb.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `satisfactory` -> `good enough`**

- status: `attributed`
- log p full -1.0428, empty -4.1955
- masks scored: 34/34 (+5 top-k)
- ranked sources:
    - `+5.322` [wiktionary] satisfactory: If something is satisfactory, it is good enough.
    - `+0.218` [readme] extubated: Not having a breathing tube anymore.
    - `+0.174` [readme] extubated: Taking out a tube used for breathing.
    - `+0.173` [wiktionary] awakened: If you awaken somebody, they stop sleeping because of something you do.
    - `-2.151` [michigan] satisfactory: When something is okay or good.

- rationale: The original term means meeting a standard in a way that is acceptable but not excellent, and "good enough" carries that same sense of adequacy without implying excellence. Word frequency rises from Zipf 3.57 to 5.44, while age of acquisition falls from 8.84 to 6.96. Readers can now grasp the level of acceptability being described without needing a more formal qualifier.
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

**output:** The patient was asleep but could be woken up easily.

| metric | value |
|---|---:|
| bertscore_f1 | 0.867 |
| coleman_liau | 5.60 |
| coleman_liau_drop | 11.02 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 6.01 |
| fkgl_drop | 9.44 |
| fre | 69.8 |
| fre_gain | 67.7 |
| human_edit_recall | 1.000 |
| length_ratio | 1.25 |
| n_words | 10.0 |
| nli_completeness | 0.459 |
| nli_faithfulness | 0.986 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 65.82 |
| smog | 8.84 |
| smog_drop | 5.71 |

### Stage 4 - arm `termonly`

**output:** PHYSICAL EXAMINATION : GENERAL : The patient was asleep, but easily woken up.

| metric | value |
|---|---:|
| bertscore_f1 | 0.593 |
| coleman_liau | 13.67 |
| coleman_liau_drop | 2.95 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 14.45 |
| fkgl_drop | 1.00 |
| fre | 11.1 |
| fre_gain | 9.0 |
| human_edit_recall | 1.000 |
| length_ratio | 1.38 |
| n_words | 11.0 |
| nli_completeness | 0.980 |
| nli_faithfulness | 0.983 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 91.36 |
| smog | 14.55 |
| smog_drop | 0.00 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `aroused` -> `woken up` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** The patient was asleep, but could be woken easily.

| metric | value |
|---|---:|
| bertscore_f1 | 0.846 |
| coleman_liau | 6.69 |
| coleman_liau_drop | 9.93 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 6.28 |
| fkgl_drop | 9.17 |
| fre | 66.1 |
| fre_gain | 64.0 |
| human_edit_recall | 1.000 |
| length_ratio | 1.12 |
| n_words | 9.0 |
| nli_completeness | 0.438 |
| nli_faithfulness | 0.982 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 61.22 |
| smog | 8.84 |
| smog_drop | 5.71 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `aroused` -> `woken` | replace | attributed | 0.030 | 0.286 | - | - | - | - |

**edit `aroused` -> `woken`**

- status: `attributed`
- log p full -0.0958, empty -0.1255
- masks scored: 4/4 (+1 top-k)
- ranked sources:
    - `-0.314` [wiktionary] aroused: If something arouses a feeling or emotion, it causes that feeling or emotion.

- rationale: The original term "aroused" means brought out of sleep or made alert, and "woken" carries that same sense of being brought out of sleep in plain words. Phrase frequency increases from Zipf 3.35 to 3.37, while syllable count stays the same from 2 to 2. Patients can understand the basic idea of being brought out of sleep without first knowing the diagnostic name.
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

**output:** He will return in about 10 days for a recheck and to get a prescription for the AFOs he plans to use. He may need them for up to 6 months.

| metric | value |
|---|---:|
| bertscore_f1 | 0.614 |
| coleman_liau | 2.12 |
| coleman_liau_drop | 4.59 |
| copy_jargon_rate | 1.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 4.16 |
| fkgl_drop | 6.73 |
| fre | 92.9 |
| fre_gain | 29.6 |
| human_edit_recall | 0.000 |
| length_ratio | 1.11 |
| n_words | 31.0 |
| nli_completeness | 0.005 |
| nli_faithfulness | 0.976 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.600 |
| sari | 24.14 |
| smog | 7.17 |
| smog_drop | 5.86 |

### Stage 4 - arm `termonly`

**output:** He is to follow up in about 10 days for recheck as well as prescription for intended ankle-foot braces, which he will need up to 6 months.

| metric | value |
|---|---:|
| bertscore_f1 | 0.887 |
| coleman_liau | 6.52 |
| coleman_liau_drop | 0.19 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 11.11 |
| fkgl_drop | -0.22 |
| fre | 63.5 |
| fre_gain | 0.2 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 28.0 |
| nli_completeness | 0.922 |
| nli_faithfulness | 0.628 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 56.24 |
| smog | 13.02 |
| smog_drop | 0.00 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `approximately` -> `about` | replace | - | - | - | - | - | - | - |
| `AFOs` -> `ankle-foot braces` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** He is to follow up in about 10 days for recheck as well as prescription for intended braces that support ankle or foot, which he will need up to 6 months.

| metric | value |
|---|---:|
| bertscore_f1 | 0.827 |
| coleman_liau | 6.07 |
| coleman_liau_drop | 0.64 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 12.11 |
| fkgl_drop | -1.22 |
| fre | 63.5 |
| fre_gain | 0.2 |
| human_edit_recall | 1.000 |
| length_ratio | 1.11 |
| n_words | 31.0 |
| nli_completeness | 0.589 |
| nli_faithfulness | 0.775 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 52.26 |
| smog | 11.21 |
| smog_drop | 1.82 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `approximately` -> `about` | replace | attributed | -0.090 | -1.281 | - | 0.833 | 0.125 | - |
| `AFOs` -> `braces that support ankle or foot` | replace | attributed | 17.596 | 17.970 | - | 0.927 | 17.476 | - |

**edit `approximately` -> `about`**

- status: `attributed`
- log p full -0.1266, empty -0.0368
- masks scored: 10/10 (+3 top-k)
- ranked sources:
    - `-0.065` [dorland] AFOs: ankle-foot orthosis
    - `-0.190` [justplainclear] AFO: Also known as: ankle-foot orthosis, walking boot A brace that supports your ankle or foot An AFO is a bra
    - `-0.784` [wiktionary] approximately: Approximately is close to, but not exactly.

- rationale: The original term means roughly or to a close estimate, and the replacement carries that same sense of an inexact quantity in everyday language. Phrase frequency rises from Zipf 4.64 to 6.40, while syllable count falls from 5 to 2. Readers can grasp the intended imprecision without needing a formal qualifier.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `AFOs` -> `braces that support ankle or foot`**

- status: `attributed`
- log p full -1.1636, empty -18.7593
- masks scored: 10/10 (+3 top-k)
- ranked sources:
    - `+17.519` [justplainclear] AFO: Also known as: ankle-foot orthosis, walking boot A brace that supports your ankle or foot An AFO is a bra
    - `+0.043` [wiktionary] approximately: Approximately is close to, but not exactly.

- rationale: AFOs are ankle–foot orthoses, devices that support or align the ankle and foot, so “braces that support ankle or foot” keeps that supportive-device meaning in everyday words. Phrase frequency rises from Zipf 1.36 to 3.35, while syllable count grows from 1 to 9. Readers can now picture the kind of supportive brace being discussed without needing the abbreviation.
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

**output:** The outside of the genitals looked normal.

| metric | value |
|---|---:|
| bertscore_f1 | 0.485 |
| coleman_liau | 8.97 |
| coleman_liau_drop | 8.50 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 5.68 |
| fkgl_drop | 8.40 |
| fre | 66.8 |
| fre_gain | 58.4 |
| human_edit_recall | 1.000 |
| length_ratio | 0.88 |
| n_words | 7.0 |
| nli_completeness | 0.908 |
| nli_faithfulness | 0.994 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.250 |
| sari | 28.29 |
| smog | 8.84 |
| smog_drop | 4.18 |

### Stage 4 - arm `termonly`

**output:** Urinary and sexual organs: The outside sexual parts looked normal.

| metric | value |
|---|---:|
| bertscore_f1 | 0.311 |
| coleman_liau | 13.14 |
| coleman_liau_drop | 4.33 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.750 |
| fkgl | 11.91 |
| fkgl_drop | 2.17 |
| fre | 27.5 |
| fre_gain | 19.1 |
| human_edit_recall | 1.000 |
| length_ratio | 1.25 |
| n_words | 10.0 |
| nli_completeness | 0.956 |
| nli_faithfulness | 0.670 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.250 |
| sari | 25.91 |
| smog | 13.02 |
| smog_drop | 0.00 |

annotation backend `novita`, 0 edits kept


### Stage 4 - arm `grounded`

**output:** The parts used for peeing and sex stuff: The outside sex and reproduction parts looked normal.

| metric | value |
|---|---:|
| bertscore_f1 | 0.203 |
| coleman_liau | 10.26 |
| coleman_liau_drop | 7.21 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.750 |
| fkgl | 6.88 |
| fkgl_drop | 7.20 |
| fre | 74.3 |
| fre_gain | 65.9 |
| human_edit_recall | 1.000 |
| length_ratio | 2.00 |
| n_words | 16.0 |
| nli_completeness | 0.899 |
| nli_faithfulness | 0.146 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.250 |
| sari | 25.91 |
| smog | 8.84 |
| smog_drop | 4.18 |

annotation backend `novita`, 0 edits kept


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

**output:** She is 21 days after surgery for an exploratory laparotomy with ovarian cancer staging.

| metric | value |
|---|---:|
| bertscore_f1 | 0.558 |
| coleman_liau | 12.33 |
| coleman_liau_drop | -1.41 |
| copy_jargon_rate | 0.750 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 14.31 |
| fkgl_drop | -2.14 |
| fre | 17.4 |
| fre_gain | -13.6 |
| human_edit_recall | 0.250 |
| length_ratio | 0.82 |
| n_words | 14.0 |
| nli_completeness | 0.984 |
| nli_faithfulness | 0.991 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 0.400 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 51.87 |
| smog | 14.55 |
| smog_drop | -1.53 |

### Stage 4 - arm `termonly`

**output:** She is 21 days after surgery for a look-inside belly operation with cancer spread check of the ovaries.

| metric | value |
|---|---:|
| bertscore_f1 | 0.524 |
| coleman_liau | 9.62 |
| coleman_liau_drop | 1.30 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.800 |
| fkgl | 10.44 |
| fkgl_drop | 1.73 |
| fre | 52.3 |
| fre_gain | 21.3 |
| human_edit_recall | 1.000 |
| length_ratio | 1.12 |
| n_words | 19.0 |
| nli_completeness | 0.905 |
| nli_faithfulness | 0.866 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 48.37 |
| smog | 13.02 |
| smog_drop | 0.00 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `postop` -> `21 days after surgery` | replace | - | - | - | - | - | - | - |
| `exploratory laparotomy` -> `look-inside belly operation` | replace | - | - | - | - | - | - | - |
| `ovarian cancer staging` -> `cancer spread check of the ovaries` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** She is 21 days after surgery from a belly check surgery with checking how far the ovary cancer has spread.

| metric | value |
|---|---:|
| bertscore_f1 | 0.601 |
| coleman_liau | 7.66 |
| coleman_liau_drop | 3.26 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.600 |
| fkgl | 9.91 |
| fkgl_drop | 2.26 |
| fre | 59.6 |
| fre_gain | 28.7 |
| human_edit_recall | 1.000 |
| length_ratio | 1.18 |
| n_words | 20.0 |
| nli_completeness | 0.821 |
| nli_faithfulness | 0.644 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 48.93 |
| smog | 13.02 |
| smog_drop | 0.00 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `postop` -> `21 days after surgery` | replace | attributed | 0.028 | 1.517 | 0.758 | 0.817 | 0.146 | - |
| `exploratory laparotomy` -> `belly check surgery` | replace | attributed | 9.269 | 9.917 | 0.672 | 0.795 | 1.955 | - |
| `ovarian cancer staging` -> `checking how far the ovary cancer has spread` | replace | attributed | 8.827 | 8.924 | 0.806 | 0.904 | 5.570 | - |

**edit `postop` -> `21 days after surgery`**

- status: `attributed`
- log p full -0.0081, empty -0.0366
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+1.052` [readme] PostOP: PostOP means after surgery.
    - `+0.906` [readme] postop: After surgery.
    - `+0.254` [readme] Exploratory laparotomy: Exploratory laparotomy: Surgery to check the organs in the belly for issues.
    - `+0.064` [readme] exploratory laparotomy: Surgery to check for problems in your belly.
    - `+0.039` [readme] OVARIAN: Related to the female reproductive gland that produces eggs.

- rationale: Postop is shorthand for the period after an operation, so "21 days after surgery" keeps the timing idea by naming the procedure and giving a concrete day count. Phrase frequency rises from Zipf 1.53 to 4.46, while syllables increase from 1 to 7. Readers can now see exactly when the event occurs without needing medical shorthand.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `exploratory laparotomy` -> `belly check surgery`**

- status: `attributed`
- log p full -0.7412, empty -10.0107
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+6.529` [readme] exploratory laparotomy: Surgery to check for problems in your belly.
    - `+4.575` [readme] Exploratory laparotomy: Exploratory laparotomy: Surgery to check the organs in the belly for issues.
    - `+1.069` [readme] PostOP: PostOP means after surgery.
    - `+0.792` [nih] ovarian: Having to do with the ovaries, the female reproductive glands in which the ova (eggs) are formed. The
    - `+0.022` [readme] OVARIAN: Related to the female reproductive gland that produces eggs.

- rationale: The source describes exploratory laparotomy as surgery to check for problems in your belly, so "belly check surgery" keeps that checking-for-problems meaning in plain words. Phrase frequency rises from Zipf 2.01 to 3.97, while age of acquisition falls from 12.89 to 7.68. Patients can grasp that the operation is an inspection of the abdomen without needing the technical name.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `ovarian cancer staging` -> `checking how far the ovary cancer has spread`**

- status: `attributed`
- log p full -2.3873, empty -11.2146
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+6.054` [readme] cancer staging: Determining the extent to which cancer has spread in the body based on a numerical scale.
    - `+0.484` [readme] OVARIAN: Related to the female reproductive gland that produces eggs.
    - `+0.319` [readme] Exploratory laparotomy: Exploratory laparotomy: Surgery to check the organs in the belly for issues.
    - `+0.298` [nih] ovarian: Having to do with the ovaries, the female reproductive glands in which the ova (eggs) are formed. The
    - `+0.157` [readme] PostOP: PostOP means after surgery.

- rationale: The source describes ovarian cancer staging as determining the extent to which cancer has spread in the body based on a numerical scale, so "checking how far the ovary cancer has spread" keeps that extent-of-spread idea in plain words. Phrase frequency decreases from Zipf 3.24 to 2.91, while age of acquisition falls from 14.44 to 12.26. Patients can grasp the purpose of staging as an assessment of spread rather than a technical label.
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

**output:** The patient has been given a prescription for prednisone as part of his chemotherapy.

| metric | value |
|---|---:|
| bertscore_f1 | 0.546 |
| coleman_liau | 11.50 |
| coleman_liau_drop | -0.58 |
| copy_jargon_rate | 1.000 |
| critical_error | 0.000 |
| drug_preservation | 1.000 |
| fkgl | 9.26 |
| fkgl_drop | -0.71 |
| fre | 53.6 |
| fre_gain | -3.3 |
| human_edit_recall | 0.000 |
| length_ratio | 0.93 |
| n_words | 14.0 |
| nli_completeness | 0.989 |
| nli_faithfulness | 0.993 |
| replacement_f1 | 0.000 |
| rewrite_aggressiveness | 1.000 |
| sari | 30.89 |
| smog | 11.21 |
| smog_drop | 0.00 |

### Stage 4 - arm `termonly`

**output:** Prescription for a medicine that lowers the immune system as part of his cancer treatment has been given to him.

| metric | value |
|---|---:|
| bertscore_f1 | 0.775 |
| coleman_liau | 9.40 |
| coleman_liau_drop | 1.52 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| drug_preservation | 0.000 |
| fkgl | 9.91 |
| fkgl_drop | -1.37 |
| fre | 59.6 |
| fre_gain | 2.7 |
| human_edit_recall | 1.000 |
| length_ratio | 1.33 |
| n_words | 20.0 |
| nli_completeness | 0.003 |
| nli_faithfulness | 0.626 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 78.97 |
| smog | 11.21 |
| smog_drop | 0.00 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `chemotherapy` -> `cancer treatment` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** The prescription for a medicine that lowers the body's immune response and inflammation as part of his drug treatment to stop the growth of cancer cells has been given to him.

| metric | value |
|---|---:|
| bertscore_f1 | 0.577 |
| coleman_liau | 10.00 |
| coleman_liau_drop | 0.92 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| drug_preservation | 0.000 |
| fkgl | 13.63 |
| fkgl_drop | -5.09 |
| fre | 52.6 |
| fre_gain | -4.4 |
| human_edit_recall | 1.000 |
| length_ratio | 2.13 |
| n_words | 32.0 |
| nli_completeness | 0.005 |
| nli_faithfulness | 0.240 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 68.25 |
| smog | 13.02 |
| smog_drop | -1.82 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `prednisone` -> `a medicine that lowers the body's immune response and inflammation` | replace | attributed | 10.786 | 11.037 | 0.776 | 0.771 | 11.912 | - |
| `chemotherapy` -> `drug treatment to stop the growth of cancer cells` | replace | attributed | 14.257 | 14.494 | 0.850 | 0.868 | 8.606 | - |

**edit `prednisone` -> `a medicine that lowers the body's immune response and inflammation`**

- status: `attributed`
- log p full -1.5069, empty -12.2930
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+13.713` [readme] Prednisone: A medication that lowers the body's immune response and inflammation.
    - `+1.801` [readme] chemotherapy: Using drugs to treat cancer or other diseases.
    - `+1.289` [michigan] chemotherapy: A drug that kills cancer cells.
    - `+0.633` [wiktionary] chemotherapy: Chemotherapy is the chemical treatment intended to be kill the cancerous cells in a patient.
    - `+0.377` [nih] prednisone: A drug used to reduce inflammation and lower the body’s immune response.  It is used with other dr

- rationale: The readme describes prednisone as a medication that lowers the body's immune response and inflammation, so "a medicine that lowers the body's immune response and inflammation" keeps that mechanism in plain language. Phrase frequency increases from Zipf 2.56 to 3.02, while age of acquisition falls from 17.17 to 12.32. Patients can understand what the drug does for their body without first knowing the prescription name.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `chemotherapy` -> `drug treatment to stop the growth of cancer cells`**

- status: `attributed`
- log p full -1.5559, empty -15.8128
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+9.180` [nih] chemotherapy: Treatment that uses drugs to stop the growth of cancer cells, either by killing the cells or by 
    - `+0.574` [readme] chemotherapy: Using drugs to treat cancer or other diseases.
    - `+0.518` [michigan] chemotherapy: A drug that kills cancer cells.
    - `+0.514` [readme] CHEMOTHERAPY: Using drugs to treat diseases like cancer.

- rationale: The source describes chemotherapy as treatment that uses drugs to stop the growth of cancer cells, either by killing the cells or by stopping them from dividing, so "drug treatment to stop the growth of cancer cells" keeps that mechanism in plain language. Word frequency rises from Zipf 3.56 to 4.18, while age of acquisition falls from 12.53 to 8.39. Patients can grasp what the therapy does without first knowing the clinical label.
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

**output:** Photic stimulation was done, but no clear photic driving was seen.

| metric | value |
|---|---:|
| bertscore_f1 | 0.588 |
| coleman_liau | 9.98 |
| coleman_liau_drop | 4.22 |
| copy_jargon_rate | 1.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 6.94 |
| fkgl_drop | 2.15 |
| fre | 64.9 |
| fre_gain | 15.4 |
| human_edit_recall | 0.000 |
| length_ratio | 0.65 |
| n_words | 11.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.990 |
| nli_faithfulness | 0.994 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 21.78 |
| smog | 8.84 |
| smog_drop | 0.00 |

### Stage 4 - arm `termonly`

**output:** A light flash test was done, but no clear light-driven brain waves were seen.

| metric | value |
|---|---:|
| bertscore_f1 | 0.619 |
| coleman_liau | 7.36 |
| coleman_liau_drop | 6.84 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.167 |
| fkgl | 3.36 |
| fkgl_drop | 5.73 |
| fre | 95.9 |
| fre_gain | 46.4 |
| human_edit_recall | 1.000 |
| length_ratio | 0.88 |
| n_words | 15.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.938 |
| nli_faithfulness | 0.737 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.200 |
| sari | 31.00 |
| smog | 8.84 |
| smog_drop | 0.00 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `Photic stimulation` -> `light flash test` | replace | - | - | - | - | - | - | - |
| `photic driving` -> `light-driven brain waves` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** A light test was done, but no clear light response was seen.

| metric | value |
|---|---:|
| bertscore_f1 | 0.607 |
| coleman_liau | 4.45 |
| coleman_liau_drop | 9.75 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.167 |
| fkgl | 1.87 |
| fkgl_drop | 7.21 |
| fre | 103.0 |
| fre_gain | 53.5 |
| human_edit_recall | 1.000 |
| length_ratio | 0.71 |
| n_words | 12.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.865 |
| nli_faithfulness | 0.921 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.200 |
| sari | 32.04 |
| smog | 3.13 |
| smog_drop | 5.71 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `Photic stimulation` -> `light test` | replace | attributed | 1.138 | 1.471 | 0.835 | 0.944 | 0.016 | - |
| `photic driving` -> `light response` | replace | attributed | -1.281 | -1.392 | 0.362 | 0.800 | 0.027 | - |

**edit `Photic stimulation` -> `light test`**

- status: `attributed`
- log p full -1.0016, empty -2.1400
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.470` [dictionary] Photic (a.): Relating to the production of light by the lower animals.
    - `+0.454` [readme] stimulation: Making something more active or alert.
    - `+0.387` [dictionary] Photic (a.): Relating to the production of light by the lower animals.
    - `+0.330` [wiktionary] stimulation: Stimulation is an action that encourages something to develop or become more active.
    - `+0.114` [wiktionary] driving: If you drive a car or other vehicle, you control its movement and direction.

- rationale: The original term refers to a brief exposure to flashing light used to provoke or observe a response, and “light test” keeps that idea of a simple illumination check in everyday words. Phrase frequency rises from Zipf 1.80 to 4.95, while age of acquisition falls from 8.63 to 6.26, and syllables drop from 6 to 2. Readers can grasp that the procedure involves light without needing the technical label.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `photic driving` -> `light response`**

- status: `attributed`
- log p full -3.2468, empty -1.9657
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.027` [wiktionary] stimulation: Stimulation is an action that encourages something to develop or become more active.
    - `-0.030` [dictionary] Clear-cut (a.): Having a sharp, distinct outline, like that of a cameo.
    - `-0.084` [readme] stimulation: Making something more active or alert.
    - `-0.130` [wiktionary] driving: If you drive a car or other vehicle, you control its movement and direction.

- rationale: The original term refers to a brain response that is driven by flashing light, and the replacement keeps that idea by naming the light response directly. Phrase frequency rises from Zipf 1.81 to 4.85, while syllables fall from 4 to 3. Readers can now grasp the concept without needing the technical label.
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

**output:** Family history: Both parents died from heart attacks.

| metric | value |
|---|---:|
| bertscore_f1 | 0.975 |
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
| nli_completeness | 0.769 |
| nli_faithfulness | 0.916 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 61.01 |
| smog | 11.21 |
| smog_drop | 3.35 |

### Stage 4 - arm `termonly`

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
| `myocardial infarctions` -> `heart attacks` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Family history: Both parents died with heart attacks.

| metric | value |
|---|---:|
| bertscore_f1 | 1.000 |
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
| nli_completeness | 0.758 |
| nli_faithfulness | 0.934 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 100.00 |
| smog | 11.21 |
| smog_drop | 3.35 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `myocardial infarctions` -> `heart attacks` | replace | attributed | -0.008 | -0.078 | - | 0.615 | 0.228 | - |

**edit `myocardial infarctions` -> `heart attacks`**

- status: `attributed`
- log p full -0.1091, empty -0.1014
- masks scored: 34/34 (+2 top-k)
- ranked sources:
    - `+0.446` [michigan] myocardial infarction: Occurs when the flow of blood to the heart is stopped by a blood clot or a spasm of an 
    - `+0.218` [iowa] MYOCARDIAL INFARCTION: heart attack
    - `+0.167` [readme] inferior myocardial infarction: A heart attack caused by a blockage in a blood vessel that affects the lower p
    - `-0.311` [readme] inferior wall myocardial infarction: Heart damage at the bottom of the left ventricle due to a blocked artery.

- rationale: The original term refers to a heart attack, a sudden loss of blood flow to heart muscle that can damage tissue, and the replacement names that event directly in everyday language. Phrase frequency rises from Zipf 1.57 to 4.59, while age of acquisition falls from 16.64 to 5.17, and syllable count drops from 8 to 3. Readers can recognize the serious cardiac event without needing medical terminology.
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

**output:** The patient's legs and arms show mild swelling that leaves small dents when pressed, and the swelling goes up to the knees on both sides.

| metric | value |
|---|---:|
| bertscore_f1 | 0.395 |
| coleman_liau | 8.54 |
| coleman_liau_drop | 0.92 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 7.38 |
| fkgl_drop | 3.85 |
| fre | 86.7 |
| fre_gain | 52.5 |
| human_edit_recall | 1.000 |
| laterality_preservation | 1.000 |
| length_ratio | 0.93 |
| n_words | 26.0 |
| nli_completeness | 0.588 |
| nli_faithfulness | 0.018 |
| number_unit_preservation | 0.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.200 |
| sari | 36.16 |
| smog | 3.13 |
| smog_drop | 9.89 |

### Stage 4 - arm `termonly`

**output:** The arms and legs show a mild two-plus swelling that holds a dent and is on both sides up to the knees.

| metric | value |
|---|---:|
| bertscore_f1 | 0.295 |
| coleman_liau | 3.95 |
| coleman_liau_drop | 5.51 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 5.33 |
| fkgl_drop | 5.90 |
| fre | 96.1 |
| fre_gain | 61.9 |
| human_edit_recall | 1.000 |
| laterality_preservation | 1.000 |
| length_ratio | 0.82 |
| n_words | 23.0 |
| nli_completeness | 0.917 |
| nli_faithfulness | 0.303 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.200 |
| sari | 35.99 |
| smog | 3.13 |
| smog_drop | 9.89 |

annotation backend `novita`, 0 edits kept


### Stage 4 - arm `grounded`

**output:** Body parts: both sides show swelling that leaves a pit up to the knees.

| metric | value |
|---|---:|
| bertscore_f1 | 0.404 |
| coleman_liau | 5.29 |
| coleman_liau_drop | 4.17 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.750 |
| fkgl | 3.36 |
| fkgl_drop | 7.87 |
| fre | 95.9 |
| fre_gain | 61.8 |
| human_edit_recall | 1.000 |
| laterality_preservation | 1.000 |
| length_ratio | 0.50 |
| n_words | 14.0 |
| nli_completeness | 0.930 |
| nli_faithfulness | 0.976 |
| number_unit_preservation | 0.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.200 |
| sari | 35.23 |
| smog | 3.13 |
| smog_drop | 9.89 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `pitting edema` -> `swelling that leaves a pit` | replace | attributed | 8.449 | 8.563 | 0.846 | 0.741 | 1.814 | - |

**edit `pitting edema` -> `swelling that leaves a pit`**

- status: `attributed`
- log p full -2.2287, empty -10.6777
- masks scored: 66/66 (+2 top-k)
- ranked sources:
    - `+4.677` [readme] pitting edema: Swelling in the body that leaves an indention (pit) when pressed.
    - `+2.863` [readme] Pitting edema: Swelling caused by trapped fluid in tissues where pressed skin leaves a temporary pit.
    - `+1.742` [thesaurus] bilateral: with both sides considered, two-sided, when both sides get a say, even, balanced
    - `+0.403` [wiktionary] bilateral: If something is bilateral, it involves two parties.
    - `+0.399` [wiktionary] extremities: An extremity is a part of an animal's body that is used to move around and to hold objects.

- rationale: The readme describes pitting edema as swelling that leaves an indentation when pressed, so "swelling that leaves a pit" keeps that press-and-pit feature in plain language. Phrase frequency rises from Zipf 2.67 to 3.55, while age of acquisition falls from 15.07 to 6.14. Readers can picture the physical sign without needing the medical label.
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

**output:** The questions mostly look at the donor’s psychosocial evaluation.

| metric | value |
|---|---:|
| bertscore_f1 | 0.546 |
| coleman_liau | 16.36 |
| coleman_liau_drop | 2.58 |
| copy_jargon_rate | 1.000 |
| critical_error | 0.000 |
| fkgl | 11.52 |
| fkgl_drop | 2.75 |
| fre | 28.5 |
| fre_gain | 17.9 |
| human_edit_recall | 0.000 |
| length_ratio | 0.67 |
| n_words | 10.0 |
| nli_completeness | 0.987 |
| nli_faithfulness | 0.988 |
| replacement_f1 | 0.000 |
| rewrite_aggressiveness | 1.000 |
| sari | 13.31 |
| smog | 11.21 |
| smog_drop | 1.82 |

### Stage 4 - arm `termonly`

**output:** Following questions are mostly involved in a social and emotional donor evaluation.

| metric | value |
|---|---:|
| bertscore_f1 | 0.714 |
| coleman_liau | 16.05 |
| coleman_liau_drop | 2.89 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 14.66 |
| fkgl_drop | -0.39 |
| fre | 11.4 |
| fre_gain | 0.8 |
| human_edit_recall | 1.000 |
| length_ratio | 0.80 |
| n_words | 12.0 |
| nli_completeness | 0.966 |
| nli_faithfulness | 0.776 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 68.52 |
| smog | 13.02 |
| smog_drop | 0.00 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `psychosocial` -> `social and emotional` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Following questions are mostly involved in a life effects donor evaluation.

| metric | value |
|---|---:|
| bertscore_f1 | 0.576 |
| coleman_liau | 15.25 |
| coleman_liau_drop | 3.69 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 12.30 |
| fkgl_drop | 1.97 |
| fre | 26.5 |
| fre_gain | 15.9 |
| human_edit_recall | 1.000 |
| length_ratio | 0.73 |
| n_words | 11.0 |
| nli_completeness | 0.005 |
| nli_faithfulness | 0.027 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 66.67 |
| smog | 11.21 |
| smog_drop | 1.82 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `psychosocial` -> `life effects` | replace | attributed | 12.238 | 12.384 | - | 1.000 | 15.127 | - |

**edit `psychosocial` -> `life effects`**

- status: `attributed`
- log p full -1.9975, empty -14.2357
- masks scored: 6/6 (+1 top-k)
- ranked sources:
    - `+13.755` [nih] psychosocial: In medicine, having to do with the mental, emotional, social, and spiritual effects of a disease
    - `-1.371` [michigan] psychosocial: Including both the mental and social aspects of disease.

- rationale: The original term "psychosocial" refers to the way psychological and social factors interact and affect a person, and "life effects" carries that meaning in plain words by pointing to the impacts on daily life. Phrase frequency increases from Zipf 2.88 to 4.85, while age of acquisition falls from 15.44 to 5.89. Readers can now grasp the idea of personal and social influences on health without needing the technical label.
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

**output:** Mild nonmobile descending aortic atherosclerosis.

| metric | value |
|---|---:|
| bertscore_f1 | 0.212 |
| coleman_liau | 29.32 |
| coleman_liau_drop | 0.00 |
| copy_jargon_rate | 1.000 |
| critical_error | 0.000 |
| fkgl | 24.12 |
| fkgl_drop | 0.00 |
| fre | -69.0 |
| fre_gain | 0.0 |
| human_edit_recall | 0.000 |
| length_ratio | 0.23 |
| n_words | 5.0 |
| nli_completeness | 0.990 |
| nli_faithfulness | 0.990 |
| replacement_f1 | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 2.78 |
| severity_downgrade | 0.000 |
| severity_preservation | 1.000 |
| severity_tier_input | 1.000 |
| severity_tier_output | 1.000 |
| smog | 14.55 |
| smog_drop | 0.00 |

### Stage 4 - arm `termonly`

**output:** Mild plaque buildup in the lower part of the body's main artery, and the plaque does not move.

| metric | value |
|---|---:|
| bertscore_f1 | 0.368 |
| coleman_liau | 6.40 |
| coleman_liau_drop | 22.92 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 6.51 |
| fkgl_drop | 17.61 |
| fre | 80.5 |
| fre_gain | 149.4 |
| human_edit_recall | 1.000 |
| length_ratio | 0.86 |
| n_words | 19.0 |
| nli_completeness | 0.605 |
| nli_faithfulness | 0.922 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 46.66 |
| severity_downgrade | 0.000 |
| severity_preservation | 1.000 |
| severity_tier_input | 1.000 |
| severity_tier_output | 1.000 |
| smog | 8.84 |
| smog_drop | 5.71 |

annotation backend `novita`, 0 edits kept


### Stage 4 - arm `grounded`

**output:** Mild plaque buildup in the lower part of the main artery in the chest that does not move.

| metric | value |
|---|---:|
| bertscore_f1 | 0.451 |
| coleman_liau | 5.43 |
| coleman_liau_drop | 23.89 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 5.85 |
| fkgl_drop | 18.27 |
| fre | 85.2 |
| fre_gain | 154.1 |
| human_edit_recall | 1.000 |
| length_ratio | 0.82 |
| n_words | 18.0 |
| nli_completeness | 0.510 |
| nli_faithfulness | 0.932 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 46.39 |
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

**output:** The tube that links the middle ear to the throat was blocked with a waxy material used in surgery.

| metric | value |
|---|---:|
| bertscore_f1 | 0.531 |
| coleman_liau | 6.76 |
| coleman_liau_drop | 3.47 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.400 |
| fkgl | 7.97 |
| fkgl_drop | -1.26 |
| fre | 71.8 |
| fre_gain | 10.5 |
| human_edit_recall | 1.000 |
| length_ratio | 1.46 |
| n_words | 19.0 |
| nli_completeness | 0.143 |
| nli_faithfulness | 0.266 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 33.64 |
| smog | 11.21 |
| smog_drop | 0.00 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `eustachian tube` -> `tube that links the middle ear to the throat` | replace | - | - | - | - | - | - | - |
| `obstructed` -> `blocked` | replace | - | - | - | - | - | - | - |
| `bone wax` -> `a waxy material used in surgery` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** The tube that connects the middle ear to the back of the throat was blocked with a hard white body shape material made of animal fat.

| metric | value |
|---|---:|
| bertscore_f1 | 0.480 |
| coleman_liau | 6.93 |
| coleman_liau_drop | 3.29 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.600 |
| fkgl | 9.98 |
| fkgl_drop | -3.28 |
| fre | 69.8 |
| fre_gain | 8.6 |
| human_edit_recall | 1.000 |
| length_ratio | 2.00 |
| n_words | 26.0 |
| nli_completeness | 0.049 |
| nli_faithfulness | 0.151 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 33.09 |
| smog | 11.21 |
| smog_drop | 0.00 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `eustachian tube` -> `tube that connects the middle ear to the back of the throat` | replace | attributed | 6.110 | 6.504 | 0.756 | 0.712 | 6.181 | - |
| `obstructed` -> `blocked` | replace | attributed | 0.002 | 0.575 | 0.771 | 0.889 | 0.669 | - |

**edit `eustachian tube` -> `tube that connects the middle ear to the back of the throat`**

- status: `attributed`
- log p full -1.1205, empty -7.2301
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+6.301` [justplainclear] eustachian tube: The tube that connects your middle ear to the back of your throat and pharynx area. The openi
    - `+0.119` [wiktionary] wax: If you wax something, you put wax on it, for example, a car.
    - `+0.008` [readme] wax: Yellow sticky stuff in your ear that keeps it clean and dry.

- rationale: The source describes the eustachian tube as the tube that connects your middle ear to the back of your throat and pharynx area, so "tube that connects the middle ear to the back of the throat" keeps that connection in plain language. Phrase frequency increases from Zipf 1.90 to 3.54, while age of acquisition rises from 5.50 to 5.53. Readers can picture the exact anatomical link without needing the Latin name.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `obstructed` -> `blocked`**

- status: `attributed`
- log p full -0.0021, empty -0.0037
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.885` [wiktionary] obstructed: If something obstructs your way, it blocks your path from point A to point B.
    - `+0.217` [wiktionary] bone: Bones are the hard, white things inside your body. They give your body its shape.
    - `+0.066` [justplainclear] eustachian tube: The tube that connects your middle ear to the back of your throat and pharynx area. The openi
    - `+0.036` [wiktionary] wax: If you wax something, you put wax on it, for example, a car.
    - `+0.036` [wiktionary] wax: Wax is a solid material made of animal fat.

- rationale: The original term means something is closed off or not able to pass through, and "blocked" carries that same sense of being stopped up in plain words. Phrase frequency increases from Zipf 2.98 to 4.31, while syllables fall from 3 to 1. Readers can now see at a glance that the passage is about something being stopped rather than having to decode a more formal word.
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

**output:** He was placed lying on his back on the operating room table.

| metric | value |
|---|---:|
| bertscore_f1 | 0.675 |
| coleman_liau | 4.93 |
| coleman_liau_drop | 1.76 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 5.81 |
| fkgl_drop | 0.47 |
| fre | 74.8 |
| fre_gain | 8.7 |
| human_edit_recall | 1.000 |
| length_ratio | 1.20 |
| n_words | 12.0 |
| nli_completeness | 0.902 |
| nli_faithfulness | 0.956 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 66.67 |
| smog | 8.84 |
| smog_drop | 0.00 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `supine` -> `lying on his back` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** He was placed lying on his back on the operating room table.

| metric | value |
|---|---:|
| bertscore_f1 | 0.675 |
| coleman_liau | 4.93 |
| coleman_liau_drop | 1.76 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 5.81 |
| fkgl_drop | 0.47 |
| fre | 74.8 |
| fre_gain | 8.7 |
| human_edit_recall | 1.000 |
| length_ratio | 1.20 |
| n_words | 12.0 |
| nli_completeness | 0.902 |
| nli_faithfulness | 0.956 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 66.67 |
| smog | 8.84 |
| smog_drop | 0.00 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `supine` -> `lying on his back` | replace | attributed | 0.306 | 1.340 | - | 0.750 | 0.295 | - |

**edit `supine` -> `lying on his back`**

- status: `attributed`
- log p full -0.1360, empty -0.4422
- masks scored: 18/18 (+2 top-k)
- ranked sources:
    - `+1.285` [readme] supine: Lying on your back.
    - `+0.990` [michigan] supine: To lie on your back.
    - `+0.711` [readme] Supine: Lying down on your back.
    - `-1.038` [iowa] SUPINE: lying on the back

- rationale: You explain, to a patient, why one phrase in a medical sentence was replaced with another.
- audit: coverage 0.0, grounding_error=False, omission=True, source_ok=True, passage_ok=True

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

**output:** A urinalysis was not performed this time.

| metric | value |
|---|---:|
| bertscore_f1 | 0.831 |
| coleman_liau | 8.14 |
| coleman_liau_drop | 0.00 |
| copy_jargon_rate | 1.000 |
| critical_error | 0.000 |
| fkgl | 7.37 |
| fkgl_drop | 0.00 |
| fre | 54.7 |
| fre_gain | 0.0 |
| human_edit_recall | 0.000 |
| length_ratio | 0.88 |
| n_words | 7.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.993 |
| nli_faithfulness | 0.993 |
| replacement_f1 | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 26.16 |
| smog | 8.84 |
| smog_drop | 0.00 |

### Stage 4 - arm `termonly`

**output:** A test of the urine was not done this time.

| metric | value |
|---|---:|
| bertscore_f1 | 0.869 |
| coleman_liau | 0.38 |
| coleman_liau_drop | 7.76 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 1.29 |
| fkgl_drop | 6.08 |
| fre | 103.6 |
| fre_gain | 48.9 |
| human_edit_recall | 1.000 |
| length_ratio | 1.25 |
| n_words | 10.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.985 |
| nli_faithfulness | 0.993 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 33.73 |
| smog | 3.13 |
| smog_drop | 5.71 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `urinalysis` -> `test of the urine` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** A test of the patient's pee was not done this time.

| metric | value |
|---|---:|
| bertscore_f1 | 0.786 |
| coleman_liau | 2.07 |
| coleman_liau_drop | 6.07 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 1.57 |
| fkgl_drop | 5.80 |
| fre | 103.4 |
| fre_gain | 48.7 |
| human_edit_recall | 1.000 |
| length_ratio | 1.50 |
| n_words | 12.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.971 |
| nli_faithfulness | 0.970 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 30.82 |
| smog | 3.13 |
| smog_drop | 5.71 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `urinalysis` -> `test of the patient's pee` | replace | attributed | 4.359 | 4.444 | - | 0.729 | 1.317 | - |

**edit `urinalysis` -> `test of the patient's pee`**

- status: `attributed`
- log p full -2.5033, empty -6.8626
- masks scored: 34/34 (+2 top-k)
- ranked sources:
    - `+3.195` [readme] urinalysis: A test that checks the contents of your pee to see what's in there.
    - `+1.877` [readme] Urinalysis: A test that checks what's in your pee.
    - `+0.563` [justplainclear] urinalysis: Also known as: urine test, pee test A test of your urine used to find certain medical conditions
    - `-0.069` [michigan] urinalysis: A test of your urine to check for diseases, such as diabetes, urinary tract infections, or kidney 
    - `-0.234` [nih] urinalysis: A test that determines the content of the urine.

- rationale: You explain, to a patient, why one phrase in a medical sentence was replaced with another.
- audit: coverage 0.0, grounding_error=False, omission=True, source_ok=True, passage_ok=True

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

**output:** Vision and hearing seemed good enough for testing, but she said her eyeglass prescription needed to be updated.

| metric | value |
|---|---:|
| bertscore_f1 | 0.742 |
| coleman_liau | 12.20 |
| coleman_liau_drop | 1.52 |
| copy_jargon_rate | 0.667 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.250 |
| fkgl | 9.79 |
| fkgl_drop | 2.48 |
| fre | 57.0 |
| fre_gain | 12.4 |
| human_edit_recall | 0.333 |
| length_ratio | 0.86 |
| n_words | 18.0 |
| nli_completeness | 0.993 |
| nli_faithfulness | 0.995 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 18.20 |
| smog | 11.21 |
| smog_drop | 1.82 |

### Stage 4 - arm `termonly`

**output:** Vision and hearing seemed good enough for testing, although she said she needed to update her glasses order.

| metric | value |
|---|---:|
| bertscore_f1 | 0.791 |
| coleman_liau | 11.23 |
| coleman_liau_drop | 2.49 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.286 |
| fkgl | 9.13 |
| fkgl_drop | 3.14 |
| fre | 61.7 |
| fre_gain | 17.1 |
| human_edit_recall | 1.000 |
| length_ratio | 0.86 |
| n_words | 18.0 |
| nli_completeness | 0.984 |
| nli_faithfulness | 0.984 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.167 |
| sari | 38.16 |
| smog | 3.13 |
| smog_drop | 9.89 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `adequate` -> `good enough` | replace | - | - | - | - | - | - | - |
| `did indicate` -> `said` | replace | - | - | - | - | - | - | - |
| `eyeglass prescription` -> `glasses order` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Vision and hearing seemed enough for testing, although she said she needed to update her glasses order.

| metric | value |
|---|---:|
| bertscore_f1 | 0.741 |
| coleman_liau | 11.46 |
| coleman_liau_drop | 2.26 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.286 |
| fkgl | 9.09 |
| fkgl_drop | 3.18 |
| fre | 60.2 |
| fre_gain | 15.7 |
| human_edit_recall | 1.000 |
| length_ratio | 0.81 |
| n_words | 17.0 |
| nli_completeness | 0.985 |
| nli_faithfulness | 0.985 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.167 |
| sari | 38.72 |
| smog | 3.13 |
| smog_drop | 9.89 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `adequate` -> `seemed enough` | replace | attributed | 2.341 | 2.909 | 0.846 | 0.883 | 0.751 | - |
| `did indicate` -> `said` | replace | attributed | -1.580 | -5.099 | 0.566 | 0.896 | 0.262 | - |
| `eyeglass prescription` -> `glasses order` | replace | attributed | 1.160 | 1.955 | 0.601 | 0.890 | 0.024 | - |

**edit `adequate` -> `seemed enough`**

- status: `attributed`
- log p full -0.7808, empty -3.1221
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+1.844` [thesaurus] adequate: enough, the right amount
    - `+1.094` [justplainclear] adequate: Enough
    - `+0.629` [wiktionary] indicate: If someone indicates something, they show signs of something; they show it.
    - `+0.235` [michigan] adequate: Enough or the right amount.
    - `+0.104` [michigan] prescription: An order from your doctor, nurse, or physician assistant for drugs or other treatment.

- rationale: The thesaurus defines adequate as enough, the right amount, so "seemed enough" keeps the sense of sufficiency in plain words. Phrase frequency rises from Zipf 4.05 to 4.74, while age of acquisition falls from 10.35 to 6.96. Readers can grasp the judgment of sufficiency without the formal term.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `did indicate` -> `said`**

- status: `attributed`
- log p full -1.6039, empty -0.0239
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+1.015` [wiktionary] did: Do is an auxiliary verb. It is used in questions, negative statements, short answers, and for emphasis wh
    - `+0.753` [wiktionary] prescription: A written order, as by a physician, to tell which medicine to take and how many doses of it is n
    - `+0.474` [readme] Prescription: A prescription is a doctor's recommendation for medication or treatment.
    - `+0.275` [michigan] prescription: An order from your doctor, nurse, or physician assistant for drugs or other treatment.
    - `+0.228` [nih] prescription: A doctor's order for medicine or another intervention.

- rationale: You explain, to a patient, why one phrase in a medical sentence was replaced with another.
- audit: coverage 0.0, grounding_error=False, omission=True, source_ok=True, passage_ok=True

**edit `eyeglass prescription` -> `glasses order`**

- status: `attributed`
- log p full -0.4475, empty -1.6073
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+0.661` [readme] Prescription: A prescription is a doctor's recommendation for medication or treatment.
    - `+0.636` [nih] prescription: A doctor's order for medicine or another intervention.
    - `+0.430` [thesaurus] prescription: doctors orders, medicine, drug order
    - `+0.321` [wiktionary] prescription: A written order, as by a physician, to tell which medicine to take and how many doses of it is n
    - `+0.212` [michigan] prescription: An order from your doctor, nurse, or physician assistant for drugs or other treatment.

- rationale: The original term refers to the written specification a clinician gives for lenses, and "glasses order" keeps that idea of a clinician's written specification for lenses in plain words. Phrase frequency rises from Zipf 2.32 to 4.31, while age of acquisition falls from 9.22 to 6.26. Readers can grasp that the clinician is providing a written specification for lenses without needing specialist vocabulary.
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

**output:** I have talked to him several times about a colonoscopy, which he has refused, and so we have been doing stools for occult blood.

| metric | value |
|---|---:|
| bertscore_f1 | 0.646 |
| coleman_liau | 7.62 |
| coleman_liau_drop | 0.00 |
| copy_jargon_rate | 1.000 |
| critical_error | 0.000 |
| fkgl | 8.03 |
| fkgl_drop | 0.00 |
| fre | 80.3 |
| fre_gain | 0.0 |
| human_edit_recall | 0.000 |
| length_ratio | 0.52 |
| n_words | 24.0 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.994 |
| replacement_f1 | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 27.99 |
| smog | 3.13 |
| smog_drop | 0.00 |

### Stage 4 - arm `termonly`

**output:** I have talked to him several times about a look inside the large bowel with a thin tube, which he has refused, and so we have been doing tests of his bowel movements for hidden blood.

| metric | value |
|---|---:|
| bertscore_f1 | 0.600 |
| coleman_liau | 6.74 |
| coleman_liau_drop | 0.88 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 13.20 |
| fkgl_drop | -5.17 |
| fre | 64.5 |
| fre_gain | -15.7 |
| human_edit_recall | 1.000 |
| length_ratio | 0.78 |
| n_words | 36.0 |
| nli_completeness | 0.946 |
| nli_faithfulness | 0.884 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 62.02 |
| smog | 3.13 |
| smog_drop | 0.00 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `colonoscopy` -> `look inside the large bowel with a thin tube` | replace | - | - | - | - | - | - | - |
| `stools` -> `tests of his bowel movements` | replace | - | - | - | - | - | - | - |
| `occult blood` -> `hidden blood` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** I have talked to him several times about a test to look inside his large intestine, which he has refused, and so we have been checking poop for hidden blood.

| metric | value |
|---|---:|
| bertscore_f1 | 0.652 |
| coleman_liau | 7.38 |
| coleman_liau_drop | 0.24 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.750 |
| fkgl | 11.06 |
| fkgl_drop | -3.03 |
| fre | 69.2 |
| fre_gain | -11.0 |
| human_edit_recall | 1.000 |
| length_ratio | 0.65 |
| n_words | 30.0 |
| nli_completeness | 0.909 |
| nli_faithfulness | 0.967 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 62.50 |
| smog | 8.84 |
| smog_drop | -5.71 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `colonoscopy` -> `test to look inside his large intestine` | replace | attributed | 5.514 | 5.604 | 0.860 | 0.827 | 0.497 | - |
| `stools` -> `poop` | replace | attributed | 0.824 | 1.292 | 0.943 | 0.981 | 2.218 | - |
| `occult blood` -> `hidden blood` | replace | attributed | -0.007 | -0.958 | 0.319 | 0.799 | 0.156 | - |

**edit `colonoscopy` -> `test to look inside his large intestine`**

- status: `attributed`
- log p full -2.4451, empty -7.9591
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+1.453` [readme] colonoscopy: A colonoscopy is a test that checks the inside of your large intestine for signs of cancer.
    - `+0.956` [readme] colonoscopy: A procedure to check for colon cancer by examining the inside of the large intestine.
    - `+0.334` [michigan] blood: A fluid in your body that carries things that are needed for your body to work well, such as vitamins, 
    - `+0.300` [readme] occult: Obscure and mysterious, not easily understood.
    - `+0.041` [michigan] colonoscopy: Looks at the inside of the large intestine using a flexible tube with a ltiny camera at the end.

- rationale: The source describes a colonoscopy as a test that checks the inside of your large intestine for signs of cancer, so "test to look inside his large intestine" keeps the core idea of an internal examination of the large bowel in plain words. Phrase frequency increases from Zipf 2.74 to 3.22, while age of acquisition falls from 15.76 to 9.28. Patients can understand the purpose and location of the procedure without first knowing the diagnostic name.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `stools` -> `poop`**

- status: `attributed`
- log p full -0.6631, empty -1.4875
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+2.669` [readme] stools: Poop.
    - `+0.450` [readme] blood: Blood is a fluid that carries nutrients and oxygen to different parts of the body.
    - `+0.338` [michigan] colonoscopy: Looks at the inside of the large intestine using a flexible tube with a ltiny camera at the end.
    - `+0.273` [readme] colonoscopy: A procedure to check for colon cancer by examining the inside of the large intestine.
    - `+0.236` [justplainclear] colonoscopy: An exam of the inside of the large intestine that uses a flexible tube with a lens at the end

- rationale: The source describes stools as poop, so "poop" keeps the same bodily-waste meaning in plain words. Phrase frequency increases from Zipf 3.05 to 3.66, while syllable count stays the same from 1 to 1. Patients can understand the basic bodily-waste reference without first knowing the clinical term.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `occult blood` -> `hidden blood`**

- status: `attributed`
- log p full -0.0119, empty -0.0046
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+0.540` [readme] occult: Obscure and mysterious, not easily understood.
    - `+0.384` [nih] colonoscopy: Examination of the inside of the colon using a colonoscope, inserted into the rectum. A colonosco
    - `+0.309` [wiktionary] occult: If something is occult it is hidden or secret—or it is about hidden or secret things.
    - `+0.217` [readme] blood: Blood is a fluid that carries nutrients and oxygen to different parts of the body.
    - `+0.214` [readme] colonoscopy: A procedure to check for colon cancer by examining the inside of the large intestine.

- rationale: Hidden blood means blood that is present but not visibly seen, so "hidden blood" keeps that idea of blood being present but concealed in plain words. Phrase frequency rises from Zipf 3.28 to 4.43, while age of acquisition falls from 12.65 to 4.89. Readers can now grasp that the test looks for blood that is not obvious to the eye.
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

**output:** The knee was washed out with a lot of fluid and dried with suction again.

| metric | value |
|---|---:|
| bertscore_f1 | 0.653 |
| coleman_liau | 4.65 |
| coleman_liau_drop | 6.75 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 4.42 |
| fkgl_drop | 3.95 |
| fre | 90.1 |
| fre_gain | 37.2 |
| human_edit_recall | 1.000 |
| length_ratio | 0.94 |
| n_words | 15.0 |
| nli_completeness | 0.977 |
| nli_faithfulness | 0.987 |
| number_unit_preservation | 0.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 63.39 |
| smog | 3.13 |
| smog_drop | 8.08 |

### Stage 4 - arm `termonly`

**output:** The knee was washed with a lot of fluid and dried with suction once again.

| metric | value |
|---|---:|
| bertscore_f1 | 0.658 |
| coleman_liau | 5.04 |
| coleman_liau_drop | 6.36 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 4.42 |
| fkgl_drop | 3.95 |
| fre | 90.1 |
| fre_gain | 37.2 |
| human_edit_recall | 1.000 |
| length_ratio | 0.94 |
| n_words | 15.0 |
| nli_completeness | 0.980 |
| nli_faithfulness | 0.990 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 66.80 |
| smog | 3.13 |
| smog_drop | 8.08 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `copiously irrigated` -> `washed with a lot of fluid` | replace | - | - | - | - | - | - | - |
| `suction dried` -> `dried with suction` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** The knee was washed with a lot of fluid and dried with a machine that pulls in liquid once again.

| metric | value |
|---|---:|
| bertscore_f1 | 0.516 |
| coleman_liau | 5.05 |
| coleman_liau_drop | 6.35 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.200 |
| fkgl | 6.37 |
| fkgl_drop | 2.00 |
| fre | 85.0 |
| fre_gain | 32.1 |
| human_edit_recall | 1.000 |
| length_ratio | 1.25 |
| n_words | 20.0 |
| nli_completeness | 0.968 |
| nli_faithfulness | 0.768 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 62.88 |
| smog | 3.13 |
| smog_drop | 8.08 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `copiously irrigated` -> `washed with a lot of fluid` | replace | attributed | 0.631 | 0.762 | 0.743 | 0.832 | 0.081 | - |
| `suction dried` -> `dried with a machine that pulls in liquid` | replace | attributed | 9.051 | 9.088 | 0.918 | 0.882 | 9.714 | - |

**edit `copiously irrigated` -> `washed with a lot of fluid`**

- status: `attributed`
- log p full -1.4648, empty -2.0956
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.229` [dictionary] Copiously (adv.): In a copious manner.
    - `+0.148` [wiktionary] irrigated: To supply farms with water to grow crops.

- rationale: You explain, to a patient, why one phrase in a medical sentence was replaced with another.
- audit: coverage 0.0, grounding_error=False, omission=True, source_ok=True, passage_ok=True

**edit `suction dried` -> `dried with a machine that pulls in liquid`**

- status: `attributed`
- log p full -3.2972, empty -12.3477
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+10.027` [readme] suction: Suction is when a machine pulls in gas, liquid, or mucus.
    - `+0.313` [wiktionary] suction: Suction is a force which pushes matter from one space into another due to the pressure difference in 
    - `-0.180` [wiktionary] suction: A suction is a device that removes saliva from a patient's mouth during dental operations.

- rationale: The readme explains suction as a machine pulling in gas, liquid, or mucus, so "dried with a machine that pulls in liquid" keeps that removal-by-pull idea in everyday terms. Phrase frequency rises from Zipf 3.28 to 3.61, while age of acquisition falls from 9.42 to 6.53. Readers can picture how the drying happens without needing the clinical label.
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

**output:** She is not having painful urination, any blood in the urine, frequency, or hesitancy.

| metric | value |
|---|---:|
| bertscore_f1 | 0.660 |
| coleman_liau | 10.26 |
| coleman_liau_drop | 0.00 |
| copy_jargon_rate | 1.000 |
| critical_error | 0.000 |
| fkgl | 10.94 |
| fkgl_drop | 0.00 |
| fre | 41.6 |
| fre_gain | 0.0 |
| human_edit_recall | 0.000 |
| length_ratio | 0.70 |
| n_words | 14.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.994 |
| replacement_f1 | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 21.25 |
| smog | 13.02 |
| smog_drop | 0.00 |

### Stage 4 - arm `termonly`

**output:** She is not having painful urination, any blood in the urine, needing to go often, or trouble starting to go.

| metric | value |
|---|---:|
| bertscore_f1 | 0.778 |
| coleman_liau | 7.37 |
| coleman_liau_drop | 2.89 |
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
| nli_completeness | 0.991 |
| nli_faithfulness | 0.990 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 63.78 |
| smog | 8.84 |
| smog_drop | 4.18 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `frequency` -> `needing to go often` | replace | - | - | - | - | - | - | - |
| `hesitancy` -> `trouble starting to go` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** She is not having painful urination, any blood in the urine, how often she pees or trouble starting to pee.

| metric | value |
|---|---:|
| bertscore_f1 | 0.728 |
| coleman_liau | 7.37 |
| coleman_liau_drop | 2.89 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 9.32 |
| fkgl_drop | 1.62 |
| fre | 63.9 |
| fre_gain | 22.3 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 20.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.983 |
| nli_faithfulness | 0.964 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 62.63 |
| smog | 8.84 |
| smog_drop | 4.18 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `frequency` -> `how often she pees` | replace | attributed | 8.751 | 8.891 | - | 0.541 | 0.255 | - |
| `hesitancy` -> `trouble starting to pee` | replace | attributed | -0.498 | -0.859 | - | 0.521 | 0.060 | - |

**edit `frequency` -> `how often she pees`**

- status: `attributed`
- log p full -2.0375, empty -10.7887
- masks scored: 34/34 (+3 top-k)
- ranked sources:
    - `+1.601` [readme] frequency: How often something happens.
    - `+1.346` [readme] FREQUENCY: Frequency is how often something happens.
    - `+1.136` [readme] hesitancy: Having difficulty starting to pee or keeping the flow steady.
    - `+1.113` [wiktionary] frequency: Something's frequency is how often it happens.
    - `+0.274` [readme] hesitancy: Having difficulty starting or maintaining a steady flow while peeing.

- rationale: You explain, to a patient, why one phrase in a medical sentence was replaced with another.
- audit: coverage 0.0, grounding_error=False, omission=True, source_ok=True, passage_ok=True

**edit `hesitancy` -> `trouble starting to pee`**

- status: `attributed`
- log p full -1.1424, empty -0.6441
- masks scored: 34/34 (+3 top-k)
- ranked sources:
    - `-0.060` [wiktionary] frequency: Something's frequency is how often it happens.
    - `-0.110` [readme] FREQUENCY: Frequency is how often something happens.
    - `-0.288` [readme] hesitancy: Having difficulty starting to pee or keeping the flow steady.
    - `-1.643` [readme] hesitancy: Having difficulty starting or maintaining a steady flow while peeing.

- rationale: You explain, to a patient, why one phrase in a medical sentence was replaced with another.
- audit: coverage 0.0, grounding_error=False, omission=True, source_ok=True, passage_ok=True

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

**output:** The patient has chest pain behind the breastbone. Sometimes the pain feels like angina, and the patient says it feels tight.

| metric | value |
|---|---:|
| bertscore_f1 | 0.409 |
| coleman_liau | 9.28 |
| coleman_liau_drop | 6.64 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 4.24 |
| fkgl_drop | 10.56 |
| fre | 83.4 |
| fre_gain | 60.6 |
| human_edit_recall | 1.000 |
| length_ratio | 0.70 |
| n_words | 21.0 |
| nli_completeness | 0.263 |
| nli_faithfulness | 0.791 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.375 |
| sari | 37.82 |
| smog | 7.17 |
| smog_drop | 8.73 |

### Stage 4 - arm `termonly`

**output:** Heart: Chest pain behind the breastbone, occasional chest pain from poor blood flow and the patient describes it as a sensation of tightness.

| metric | value |
|---|---:|
| bertscore_f1 | 0.575 |
| coleman_liau | 12.17 |
| coleman_liau_drop | 3.75 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.333 |
| fkgl | 10.31 |
| fkgl_drop | 4.49 |
| fre | 62.1 |
| fre_gain | 39.3 |
| human_edit_recall | 1.000 |
| length_ratio | 0.77 |
| n_words | 23.0 |
| nli_completeness | 0.955 |
| nli_faithfulness | 0.748 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 57.08 |
| smog | 11.21 |
| smog_drop | 4.70 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `retrosternal area` -> `behind the breastbone` | replace | - | - | - | - | - | - | - |
| `anginal pain` -> `chest pain from poor blood flow` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** The patient has heart and blood vessel symptoms: chest pain behind the breastbone, sometimes chest pain from poor blood flow to the heart and the patient describes it as a feeling of tightness.

| metric | value |
|---|---:|
| bertscore_f1 | 0.475 |
| coleman_liau | 11.07 |
| coleman_liau_drop | 4.84 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.333 |
| fkgl | 12.66 |
| fkgl_drop | 2.14 |
| fre | 63.1 |
| fre_gain | 40.3 |
| human_edit_recall | 1.000 |
| length_ratio | 1.10 |
| n_words | 33.0 |
| nli_completeness | 0.942 |
| nli_faithfulness | 0.896 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.167 |
| sari | 58.14 |
| smog | 3.13 |
| smog_drop | 12.77 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `Cardiovascular` -> `heart and blood vessel symptoms` | replace | attributed | 6.649 | 6.751 | 0.776 | 0.750 | 0.240 | - |
| `retrosternal area` -> `breastbone` | replace | attributed | 0.038 | 0.641 | 0.075 | 0.632 | 0.000 | - |
| `anginal pain` -> `chest pain from poor blood flow to the heart` | replace | attributed | -0.693 | -0.716 | 0.443 | 0.755 | 0.257 | - |

**edit `Cardiovascular` -> `heart and blood vessel symptoms`**

- status: `attributed`
- log p full -2.3329, empty -8.9822
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+0.957` [justplainclear] cardiovascular: About the heart and blood vessels
    - `+0.718` [michigan] cardiovascular: Having to do with your heart and blood vessels.
    - `+0.355` [thesaurus] cardiovascular: having to do with the heart and blood vessels
    - `+0.132` [nih] cardiovascular: Having to do with the heart and blood vessels.
    - `-0.036` [wiktionary] pain: A strong feeling of hurt or discomfort

- rationale: The source describes cardiovascular as about the heart and blood vessels, so "heart and blood vessel symptoms" keeps that system focus in plain words. Phrase frequency rises from Zipf 3.68 to 4.00, while age of acquisition falls from 13.32 to 9.94. Patients can now see which body system is involved without needing the technical label.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `retrosternal area` -> `breastbone`**

- status: `attributed`
- log p full -0.0435, empty -0.0810
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+0.000` [thesaurus] cardiovascular: having to do with the heart and blood vessels
    - `-0.035` [readme] Cardiovascular: Related to the blood vessels and heart.

- rationale: The original term refers to the space behind the breastbone, and "breastbone" keeps that anatomical location in plain words. Phrase frequency increases from Zipf 0.00 to 1.93, while age of acquisition rises from 6.58 to 10.75, and syllables fall from 6 to 2. Readers can now locate the area without needing the technical positional term.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `anginal pain` -> `chest pain from poor blood flow to the heart`**

- status: `attributed`
- log p full -3.7919, empty -3.0991
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+0.348` [readme] CARDIOVASCULAR: Having to do with the blood vessels and the heart.
    - `+0.091` [michigan] pain: An unplesant feeling, a sign from your nerves that something may be wrong. It ca be sharp or dull, sting

- rationale: The original term refers to a specific kind of chest discomfort caused by reduced blood flow to the heart muscle, and the replacement names that discomfort directly as chest pain while adding the cause of poor blood flow to the heart in plain language. Phrase frequency rises from Zipf 1.10 to 4.09, while age of acquisition rises from 4.26 to 7.40. Readers can recognize the symptom and its cardiac cause without needing the clinical label.
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

**output:** We removed a large amount of his synovium and synovial pouch.

| metric | value |
|---|---:|
| bertscore_f1 | 0.372 |
| coleman_liau | 7.87 |
| coleman_liau_drop | -2.11 |
| copy_jargon_rate | 0.800 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 5.86 |
| fkgl_drop | -1.07 |
| fre | 72.6 |
| fre_gain | -7.7 |
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

**output:** We cut out a good bit of his joint lining and joint lining sac.

| metric | value |
|---|---:|
| bertscore_f1 | 0.595 |
| coleman_liau | 2.39 |
| coleman_liau_drop | 3.38 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 3.36 |
| fkgl_drop | 1.44 |
| fre | 95.9 |
| fre_gain | 15.6 |
| human_edit_recall | 1.000 |
| length_ratio | 1.17 |
| n_words | 14.0 |
| nli_completeness | 0.696 |
| nli_faithfulness | 0.908 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 52.89 |
| smog | 3.13 |
| smog_drop | 5.71 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `synovium` -> `joint lining` | replace | - | - | - | - | - | - | - |
| `synovial pouch` -> `joint lining sac` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** We took out a good bit of his joint lining and joint lining pocket.

| metric | value |
|---|---:|
| bertscore_f1 | 0.470 |
| coleman_liau | 4.04 |
| coleman_liau_drop | 1.72 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.200 |
| fkgl | 4.20 |
| fkgl_drop | 0.59 |
| fre | 89.9 |
| fre_gain | 9.6 |
| human_edit_recall | 1.000 |
| length_ratio | 1.17 |
| n_words | 14.0 |
| nli_completeness | 0.703 |
| nli_faithfulness | 0.754 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 46.74 |
| smog | 3.13 |
| smog_drop | 5.71 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `synovium` -> `joint lining` | replace | attributed | 0.015 | 0.318 | 0.545 | 0.707 | 0.031 | - |
| `synovial pouch` -> `joint lining pocket` | replace | attributed | 3.754 | 4.234 | 0.892 | 0.871 | 1.540 | - |

**edit `synovium` -> `joint lining`**

- status: `attributed`
- log p full -0.0422, empty -0.0576
- masks scored: 66/66 (+3 top-k)
- ranked sources:
    - `+0.320` [wiktionary] pouch: A pouch is a small bag or pocket used for carrying things.
    - `+0.288` [readme] SYNOVIUM: The slimy layer that covers your joints.
    - `+0.286` [wiktionary] pouch: A pouch is a pocket-like part of an animal's body, used to carry young or store food.
    - `-0.026` [readme] Synovial: Relating to the soft tissue that lines joints.

- rationale: The original term synovium refers to the thin membrane that lines a joint cavity, so "joint lining" keeps that anatomical location and function in plain words. Phrase frequency increases from Zipf 1.46 to 3.82, while syllable count stays the same at 3. Readers can now picture the structure being described without needing specialized anatomy vocabulary.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `synovial pouch` -> `joint lining pocket`**

- status: `attributed`
- log p full -0.9504, empty -4.7046
- masks scored: 66/66 (+3 top-k)
- ranked sources:
    - `+2.279` [wiktionary] pouch: A pouch is a pocket-like part of an animal's body, used to carry young or store food.
    - `+0.739` [wiktionary] pouch: A pouch is a small bag or pocket used for carrying things.
    - `+0.351` [readme] SYNOVIUM: The slimy layer that covers your joints.
    - `+0.236` [readme] SYNOVIAL: Synovial means having to do with the soft tissue that lines joints.

- rationale: The source describes a pouch as a pocket-like part of an animal's body, so "joint lining pocket" keeps the idea of a small sac-like space in plain words. Phrase frequency rises from Zipf 2.32 to 3.73, while age of acquisition falls from 16.00 to 9.30. Readers can picture a tiny pocket within the joint lining without needing the anatomical label.
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

**output:** An inflammatory process such as infection or ischemia must be considered.

| metric | value |
|---|---:|
| bertscore_f1 | 0.813 |
| coleman_liau | 14.20 |
| coleman_liau_drop | 0.00 |
| copy_jargon_rate | 1.000 |
| critical_error | 0.000 |
| diagnostic_identity_preservation | 1.000 |
| fkgl | 13.37 |
| fkgl_drop | 0.00 |
| fre | 18.8 |
| fre_gain | 0.0 |
| human_edit_recall | 0.000 |
| length_ratio | 0.85 |
| n_words | 11.0 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.994 |
| replacement_f1 | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 27.57 |
| smog | 14.55 |
| smog_drop | 0.00 |

### Stage 4 - arm `termonly`

**output:** A flare-up such as infection or poor blood flow must be considered.

| metric | value |
|---|---:|
| bertscore_f1 | 0.748 |
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
| nli_completeness | 0.961 |
| nli_faithfulness | 0.985 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 48.03 |
| smog | 11.21 |
| smog_drop | 3.35 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `inflammatory process` -> `flare-up` | replace | - | - | - | - | - | - | - |
| `ischemia` -> `poor blood flow` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** A flare-up such as infection or not enough blood flow must be considered.

| metric | value |
|---|---:|
| bertscore_f1 | 0.712 |
| coleman_liau | 8.25 |
| coleman_liau_drop | 5.95 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| diagnostic_identity_preservation | 1.000 |
| fkgl | 6.73 |
| fkgl_drop | 6.65 |
| fre | 70.0 |
| fre_gain | 51.2 |
| human_edit_recall | 1.000 |
| length_ratio | 1.08 |
| n_words | 14.0 |
| nli_completeness | 0.940 |
| nli_faithfulness | 0.900 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 47.08 |
| smog | 11.21 |
| smog_drop | 3.35 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `inflammatory process` -> `flare-up` | replace | attributed | -0.161 | -0.349 | 0.842 | 0.884 | 0.069 | - |
| `ischemia` -> `not enough blood flow` | replace | attributed | 4.366 | 5.414 | 0.870 | 0.938 | 2.056 | - |

**edit `inflammatory process` -> `flare-up`**

- status: `attributed`
- log p full -0.7043, empty -0.5430
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.247` [readme] Ischemia: Ischemia is when there's a lack of blood flow due to blocked blood vessels.
    - `+0.177` [readme] ischemia: Not enough blood flow due to blocked or narrowed blood vessels.
    - `+0.155` [michigan] ischemia: When blood supply to an organ or a body part isn't enough, especially the heart.
    - `+0.060` [iowa] ISCHEMIA: decreased oxygen in a tissue (usually because of decreased blood flow)

- rationale: The original term refers to a body’s immune response that causes redness, swelling, and pain, and “flare-up” carries that meaning as a sudden worsening of symptoms in everyday language. Phrase frequency decreases from Zipf 3.71 to 3.64, while syllable count falls from 7 to 2. Readers can now grasp that the condition is an active, symptomatic episode without needing technical immunology vocabulary.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `ischemia` -> `not enough blood flow`**

- status: `attributed`
- log p full -0.4273, empty -4.7928
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+3.404` [readme] ischemia: Not enough blood flow due to blocked or narrowed blood vessels.
    - `+1.348` [michigan] ischemia: When blood supply to an organ or a body part isn't enough, especially the heart.
    - `+0.020` [readme] inflammatory process: When your body gets inflamed, it's like it's telling you there's something wrong by show
    - `-0.061` [readme] Ischemia: Ischemia is when there's a lack of blood flow due to blocked blood vessels.
    - `-0.170` [nih] ischemia: Lack of blood supply to a part of the body. Ischemia may cause tissue damage due to the lack of oxyg

- rationale: The source describes ischemia as not enough blood flow due to blocked or narrowed blood vessels, so "not enough blood flow" keeps that core idea in plain words. Phrase frequency increases from Zipf 2.85 to 4.50, while age of acquisition falls from 18.00 to 7.40. Readers can grasp the basic problem of reduced blood supply without needing the medical label.
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

**output:** The patient has been told to raise her prednisone dose after she leaves the hospital.

| metric | value |
|---|---:|
| bertscore_f1 | 0.521 |
| coleman_liau | 9.29 |
| coleman_liau_drop | -2.91 |
| copy_jargon_rate | 1.000 |
| critical_error | 0.000 |
| drug_preservation | 1.000 |
| fkgl | 5.99 |
| fkgl_drop | -3.14 |
| fre | 78.8 |
| fre_gain | -17.1 |
| human_edit_recall | 0.000 |
| length_ratio | 1.25 |
| n_words | 15.0 |
| nli_completeness | 0.992 |
| nli_faithfulness | 0.814 |
| replacement_f1 | 0.000 |
| rewrite_aggressiveness | 1.000 |
| sari | 10.61 |
| smog | 8.84 |
| smog_drop | -5.71 |

### Stage 4 - arm `termonly`

**output:** I have asked her to increase her medicine when she goes home.

| metric | value |
|---|---:|
| bertscore_f1 | 0.916 |
| coleman_liau | 5.42 |
| coleman_liau_drop | 0.97 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| drug_preservation | 0.000 |
| fkgl | 3.84 |
| fkgl_drop | -0.98 |
| fre | 88.9 |
| fre_gain | -7.0 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 12.0 |
| nli_completeness | 0.001 |
| nli_faithfulness | 0.984 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 66.67 |
| smog | 8.84 |
| smog_drop | -5.71 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `prednisone` -> `medicine` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** I have asked her to increase her medicine that lowers the body's immune response and inflammation when she goes home.

| metric | value |
|---|---:|
| bertscore_f1 | 0.691 |
| coleman_liau | 10.56 |
| coleman_liau_drop | -4.18 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| drug_preservation | 0.000 |
| fkgl | 9.91 |
| fkgl_drop | -7.05 |
| fre | 59.6 |
| fre_gain | -36.3 |
| human_edit_recall | 1.000 |
| length_ratio | 1.75 |
| n_words | 21.0 |
| nli_completeness | 0.002 |
| nli_faithfulness | 0.234 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 66.67 |
| smog | 11.21 |
| smog_drop | -8.08 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `prednisone` -> `medicine that lowers the body's immune response and inflammation` | replace | attributed | 17.503 | 17.684 | - | 0.810 | 14.981 | - |

**edit `prednisone` -> `medicine that lowers the body's immune response and inflammation`**

- status: `attributed`
- log p full -1.7965, empty -19.2995
- masks scored: 10/10 (+2 top-k)
- ranked sources:
    - `+16.537` [readme] Prednisone: A medication that lowers the body's immune response and inflammation.
    - `+1.556` [nih] prednisone: A drug used to reduce inflammation and lower the body’s immune response.  It is used with other dr
    - `-2.039` [readme] prednisone: A medication that helps lower the body's immune system reactions.

- rationale: The original term prednisone refers to a prescription steroid that is used to reduce inflammation and calm an overactive immune response, so "medicine that lowers the body's immune response and inflammation" keeps that therapeutic purpose in plain language. Phrase frequency increases from Zipf 2.56 to 3.02, while age of acquisition falls from 17.17 to 12.32. Patients can understand the drug's general role without needing the specific chemical name.
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

**output:** She may need other medicines for nerve pain when needed.

| metric | value |
|---|---:|
| bertscore_f1 | 0.852 |
| coleman_liau | 7.92 |
| coleman_liau_drop | 4.57 |
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
| nli_completeness | 0.897 |
| nli_faithfulness | 0.967 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 47.00 |
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

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `neuropathic` -> `nerve pain` | replace | attributed | 0.141 | 6.883 | - | 1.000 | 1.643 | - |

**edit `neuropathic` -> `nerve pain`**

- status: `attributed`
- log p full -0.0002, empty -0.1414
- masks scored: 6/6 (+1 top-k)
- ranked sources:
    - `+4.106` [readme] neuropathic: Nerve pain.
    - `+2.464` [readme] Neuropathic: Neuropathic means nerve pain.

- rationale: You explain, to a patient, why one phrase in a medical sentence was replaced with another.
- audit: coverage 0.0, grounding_error=False, omission=True, source_ok=True, passage_ok=True

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

**output:** A preventive dose of antibiotics was given.

| metric | value |
|---|---:|
| bertscore_f1 | 0.945 |
| coleman_liau | 9.80 |
| coleman_liau_drop | 1.66 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 10.74 |
| fkgl_drop | 1.69 |
| fre | 30.5 |
| fre_gain | 12.1 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 7.0 |
| nli_completeness | 0.394 |
| nli_faithfulness | 0.974 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 66.67 |
| smog | 11.21 |
| smog_drop | 0.00 |

### Stage 4 - arm `termonly`

**output:** A dose of medicine to help prevent infection was given.

| metric | value |
|---|---:|
| bertscore_f1 | 0.625 |
| coleman_liau | 7.34 |
| coleman_liau_drop | 4.12 |
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
| nli_completeness | 0.215 |
| nli_faithfulness | 0.986 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 28.96 |
| smog | 11.21 |
| smog_drop | 0.00 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `prophylactic` -> `dose of medicine to help prevent infection` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** A dose of medicine that kills bacteria to prevent sickness was given.

| metric | value |
|---|---:|
| bertscore_f1 | 0.566 |
| coleman_liau | 9.28 |
| coleman_liau_drop | 2.17 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 8.76 |
| fkgl_drop | 3.67 |
| fre | 53.7 |
| fre_gain | 35.2 |
| human_edit_recall | 1.000 |
| length_ratio | 1.71 |
| n_words | 12.0 |
| nli_completeness | 0.685 |
| nli_faithfulness | 0.884 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 28.96 |
| smog | 11.21 |
| smog_drop | 0.00 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `prophylactic` -> `dose of medicine that kills bacteria to prevent sickness` | replace | attributed | 17.871 | 17.921 | 0.893 | 0.946 | 10.230 | - |

**edit `prophylactic` -> `dose of medicine that kills bacteria to prevent sickness`**

- status: `attributed`
- log p full -3.0093, empty -20.8802
- masks scored: 66/66 (+2 top-k)
- ranked sources:
    - `+12.738` [readme] Antibiotics: Medicine that kills bacteria.
    - `+2.508` [wiktionary] antibiotics: An antibiotic is a drug that stops the growth of or destroys bacteria and other such microorganis
    - `+1.660` [justplainclear] prophylactic: Drugs given to prevent sickness or pregnancy, birth control, condom
    - `+0.937` [wiktionary] prophylactic: Something that is prophylactic serves to prevent or protect against a disease or pregnancy.
    - `+0.675` [readme] PROPHYLACTIC: Preventive measures or treatments to avoid getting sick.

- rationale: The original term prophylactic means intended to prevent disease, and the replacement "dose of medicine that kills bacteria to prevent sickness" conveys that preventive intent by naming the action and purpose in plain words. Phrase frequency increases from Zipf 2.59 to 3.45, while age of acquisition falls from 15.20 to 10.10. Readers can see the preventive purpose and the specific antibacterial action without needing the technical label.
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

**output:** The patient has long-term low potassium because of long-term diarrhea.

| metric | value |
|---|---:|
| bertscore_f1 | 0.714 |
| coleman_liau | 14.88 |
| coleman_liau_drop | 6.92 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.143 |
| fkgl | 11.91 |
| fkgl_drop | 4.34 |
| fre | 27.5 |
| fre_gain | 38.2 |
| human_edit_recall | 1.000 |
| length_ratio | 1.33 |
| n_words | 12.0 |
| nli_completeness | 0.945 |
| nli_faithfulness | 0.977 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 49.96 |
| smog | 11.21 |
| smog_drop | 0.00 |
| temporality_preservation | 0.000 |

### Stage 4 - arm `termonly`

**output:** The patient has long-term low potassium from long-term loose stools.

| metric | value |
|---|---:|
| bertscore_f1 | 0.548 |
| coleman_liau | 13.72 |
| coleman_liau_drop | 8.08 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.250 |
| fkgl | 7.19 |
| fkgl_drop | 9.06 |
| fre | 61.3 |
| fre_gain | 72.1 |
| human_edit_recall | 1.000 |
| length_ratio | 1.33 |
| n_words | 12.0 |
| nli_completeness | 0.872 |
| nli_faithfulness | 0.958 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 41.01 |
| smog | 8.84 |
| smog_drop | 2.37 |
| temporality_preservation | 0.000 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `Chronic hypokalemia` -> `long-term low potassium` | replace | - | - | - | - | - | - | - |
| `chronic diarrhea` -> `long-term loose stools` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** The patient has a long-lasting low blood potassium level because of long-lasting loose, watery poop.

| metric | value |
|---|---:|
| bertscore_f1 | 0.441 |
| coleman_liau | 13.93 |
| coleman_liau_drop | 7.87 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.375 |
| fkgl | 11.50 |
| fkgl_drop | 4.75 |
| fre | 39.3 |
| fre_gain | 50.1 |
| human_edit_recall | 1.000 |
| length_ratio | 1.89 |
| n_words | 17.0 |
| nli_completeness | 0.889 |
| nli_faithfulness | 0.941 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 33.06 |
| smog | 14.55 |
| smog_drop | -3.35 |
| temporality_preservation | 0.000 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `Chronic hypokalemia` -> `long-lasting low blood potassium level` | replace | attributed | 3.082 | 3.542 | 0.864 | 0.923 | 2.197 | - |
| `chronic diarrhea` -> `long-lasting loose, watery poop` | replace | attributed | 8.046 | 8.166 | 0.890 | 0.940 | 6.451 | - |

**edit `Chronic hypokalemia` -> `long-lasting low blood potassium level`**

- status: `attributed`
- log p full -0.9692, empty -4.0515
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+3.170` [iowa] HYPOKALEMIA: low blood potassium level
    - `+0.973` [readme] Chronic: A long-lasting or recurring health issue.
    - `+0.786` [readme] Chronic: A long-lasting or recurring health issue.
    - `+0.253` [readme] diarrhea: Having loose, watery poop with cramps and bloating.
    - `+0.150` [readme] chronic: An ongoing or frequently recurring health issue.

- rationale: The source describes chronic hypokalemia as a low blood potassium level, so "long-lasting low blood potassium level" keeps that meaning in plain words. Phrase frequency increases from Zipf 1.76 to 3.45, while age of acquisition rises from 11.25 to 11.89. Patients can understand the basic electrolyte problem without first knowing the diagnostic name.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `chronic diarrhea` -> `long-lasting loose, watery poop`**

- status: `attributed`
- log p full -2.1730, empty -10.2186
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+7.259` [readme] diarrhea: Having loose, watery poop with cramps and bloating.
    - `+0.807` [readme] Diarrhea: Having runny poop with stomach pains and bloating.
    - `+0.190` [readme] chronic: An ongoing or frequently recurring health issue.
    - `+0.172` [wiktionary] secondary: of less than primary importance.
    - `+0.126` [wiktionary] to: To shows where something goes, the goal of movement.

- rationale: The source describes chronic diarrhea as having loose, watery poop with cramps and bloating, so "long-lasting loose, watery poop" keeps that ongoing loose-stool idea in plain words. Phrase frequency decreases from Zipf 3.46 to 3.01, while age of acquisition falls from 11.25 to 7.71. Readers can picture the symptom and its duration without needing the medical label.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

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

**output:** No hepatosplenomegaly or tenderness.

| metric | value |
|---|---:|
| bertscore_f1 | 0.235 |
| coleman_liau | 23.20 |
| coleman_liau_drop | 0.00 |
| copy_jargon_rate | 1.000 |
| critical_error | 0.000 |
| fkgl | 6.62 |
| fkgl_drop | 0.00 |
| fre | 54.7 |
| fre_gain | 0.0 |
| human_edit_recall | 0.000 |
| length_ratio | 0.44 |
| n_words | 4.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.994 |
| replacement_f1 | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 5.56 |
| smog | 8.84 |
| smog_drop | 0.00 |

### Stage 4 - arm `termonly`

**output:** No enlarged liver or spleen or pain when touched.

| metric | value |
|---|---:|
| bertscore_f1 | 0.916 |
| coleman_liau | 6.69 |
| coleman_liau_drop | 16.51 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 2.34 |
| fkgl_drop | 4.28 |
| fre | 94.3 |
| fre_gain | 39.6 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 9.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.931 |
| nli_faithfulness | 0.482 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 69.99 |
| smog | 3.13 |
| smog_drop | 5.71 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `hepatosplenomegaly` -> `enlarged liver or spleen` | replace | - | - | - | - | - | - | - |
| `tenderness` -> `pain when touched` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** No enlarged liver or spleen or pain on touch.

| metric | value |
|---|---:|
| bertscore_f1 | 0.869 |
| coleman_liau | 4.11 |
| coleman_liau_drop | 19.09 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 2.34 |
| fkgl_drop | 4.28 |
| fre | 94.3 |
| fre_gain | 39.6 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 9.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.947 |
| nli_faithfulness | 0.622 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 64.98 |
| smog | 3.13 |
| smog_drop | 5.71 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `hepatosplenomegaly` -> `enlarged liver or spleen` | replace | attributed | 0.059 | 0.188 | - | 0.624 | 0.032 | - |
| `tenderness` -> `pain on touch` | replace | attributed | 0.575 | 0.695 | - | 0.651 | 0.017 | - |

**edit `hepatosplenomegaly` -> `enlarged liver or spleen`**

- status: `attributed`
- log p full -0.3444, empty -0.4029
- masks scored: 18/18 (+2 top-k)
- ranked sources:
    - `+0.032` [readme] Tenderness: Tenderness is when an area hurts or is sensitive to touch.

- rationale: Hepatosplenomegaly means the liver and spleen are both enlarged, so "enlarged liver or spleen" keeps that organ-size idea in plain words. Phrase frequency rises from Zipf 1.12 to 2.99, while syllable count rises from 2 to 6. Readers can now see which organs are affected without needing the combined medical term.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `tenderness` -> `pain on touch`**

- status: `attributed`
- log p full -1.4839, empty -2.0585
- masks scored: 18/18 (+2 top-k)
- ranked sources:
    - `+0.273` [readme] Tenderness: Tenderness is when an area hurts or is sensitive to touch.
    - `+0.256` [wiktionary] tenderness: Tenderness is the pain or discomfort when an affected area is touched.
    - `+0.165` [wiktionary] tenderness: Tenderness is a tendency to show concern or kindness towards others.

- rationale: You explain, to a patient, why one phrase in a medical sentence was replaced with another.
- audit: coverage 0.0, grounding_error=False, omission=True, source_ok=True, passage_ok=True

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

**output:** He did not get left front chest pain with exercise.

| metric | value |
|---|---:|
| bertscore_f1 | 0.892 |
| coleman_liau | 5.02 |
| coleman_liau_drop | 4.96 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 2.47 |
| fkgl_drop | 6.61 |
| fre | 95.2 |
| fre_gain | 45.6 |
| human_edit_recall | 1.000 |
| laterality_preservation | 0.500 |
| length_ratio | 0.91 |
| n_words | 10.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.974 |
| nli_faithfulness | 0.968 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 56.36 |
| smog | 8.84 |
| smog_drop | 4.18 |

### Stage 4 - arm `termonly`

**output:** He did not have his left front chest pain with exercise.

| metric | value |
|---|---:|
| bertscore_f1 | 0.946 |
| coleman_liau | 5.24 |
| coleman_liau_drop | 4.75 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 2.65 |
| fkgl_drop | 6.44 |
| fre | 95.7 |
| fre_gain | 46.1 |
| human_edit_recall | 1.000 |
| laterality_preservation | 0.500 |
| length_ratio | 1.00 |
| n_words | 11.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.973 |
| nli_faithfulness | 0.970 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 62.40 |
| smog | 8.84 |
| smog_drop | 4.18 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `experience` -> `have` | replace | - | - | - | - | - | - | - |
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
| `experience` -> `feel` | replace | attributed | 0.651 | 1.575 | 0.941 | 0.952 | 3.100 | - |
| `anterior` -> `front` | replace | attributed | -0.000 | -0.202 | 0.721 | 0.766 | 0.045 | - |

**edit `experience` -> `feel`**

- status: `attributed`
- log p full -0.2739, empty -0.9248
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+3.090` [thesaurus] experience: feel, have, go through
    - `-0.010` [nih] anterior: In human anatomy, has to do with the front of a structure, or a structure found toward the front of 
    - `-0.023` [readme] Anterior: The front part of the body or an organ.
    - `-0.121` [michigan] anterior: The front of the body.
    - `-0.156` [wiktionary] anterior: Anterior is a word used in biology to refer to the front of an animal.

- rationale: You explain, to a patient, why one phrase in a medical sentence was replaced with another.
- audit: coverage 0.0, grounding_error=False, omission=True, source_ok=True, passage_ok=True

**edit `anterior` -> `front`**

- status: `attributed`
- log p full -0.0015, empty -0.0012
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.325` [readme] Anterior: The front part of the body or an organ.
    - `+0.280` [wiktionary] anterior: Anterior is a word used in biology to refer to the front of an animal.
    - `+0.145` [michigan] anterior: The front of the body.
    - `+0.083` [wiktionary] experience: Experience is the amount of time you have been doing something (especially, a job).
    - `-0.063` [nih] anterior: In human anatomy, has to do with the front of a structure, or a structure found toward the front of 

- rationale: You explain, to a patient, why one phrase in a medical sentence was replaced with another.
- audit: coverage 0.0, grounding_error=False, omission=True, source_ok=True, passage_ok=True

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

**output:** Also, would use it to control the fast and irregular heart rhythm.

| metric | value |
|---|---:|
| bertscore_f1 | 0.814 |
| coleman_liau | 7.35 |
| coleman_liau_drop | 1.92 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 6.79 |
| fkgl_drop | 0.80 |
| fre | 67.8 |
| fre_gain | 11.1 |
| human_edit_recall | 1.000 |
| length_ratio | 1.20 |
| n_words | 12.0 |
| nli_completeness | 0.209 |
| nli_faithfulness | 0.804 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 72.92 |
| smog | 8.84 |
| smog_drop | 0.00 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `atrial fibrillation` -> `fast and irregular heart rhythm` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Also, would use it to control the heart rhythm problem.

| metric | value |
|---|---:|
| bertscore_f1 | 0.827 |
| coleman_liau | 6.76 |
| coleman_liau_drop | 2.51 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 4.83 |
| fkgl_drop | 2.76 |
| fre | 78.2 |
| fre_gain | 21.6 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 10.0 |
| nli_completeness | 0.133 |
| nli_faithfulness | 0.880 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 69.44 |
| smog | 3.13 |
| smog_drop | 5.71 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `atrial fibrillation` -> `heart rhythm problem` | replace | attributed | 1.045 | 1.286 | - | 0.833 | 1.032 | - |

**edit `atrial fibrillation` -> `heart rhythm problem`**

- status: `attributed`
- log p full -1.2177, empty -2.2628
- masks scored: 10/10 (+2 top-k)
- ranked sources:
    - `+1.304` [justplainclear] atrial fibrillation: A problem with the speed or rhythm that your heart beats It is the most common type of ar
    - `+0.271` [readme] atrial fibrillation: Atrial fibrillation is when your heart beats in a weird way that can make you tired and i
    - `-0.432` [readme] Atrial fibrillation: Atrial fibrillation is when your heart beats irregularly and can make you tired or more l

- rationale: The term atrial fibrillation names a specific irregular, often rapid heart rhythm, and the replacement "heart rhythm problem" keeps that core idea of a disordered beat in everyday language. Phrase frequency rises from Zipf 2.58 to 4.01, while age of acquisition falls from 14.58 to 7.16. Readers can grasp that the heart’s rhythm is abnormal without needing the clinical label.
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

**output:** The patient seems to give a clear and reliable history.

| metric | value |
|---|---:|
| bertscore_f1 | 0.363 |
| coleman_liau | 7.34 |
| coleman_liau_drop | 3.61 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.250 |
| fkgl | 7.19 |
| fkgl_drop | 3.94 |
| fre | 61.3 |
| fre_gain | 31.8 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 10.0 |
| nli_completeness | 0.919 |
| nli_faithfulness | 0.669 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.250 |
| sari | 26.61 |
| smog | 11.21 |
| smog_drop | 1.82 |

### Stage 4 - arm `termonly`

**output:** Overall the patient is a person who appears to give clear health history.

| metric | value |
|---|---:|
| bertscore_f1 | 0.385 |
| coleman_liau | 8.69 |
| coleman_liau_drop | 2.26 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.250 |
| fkgl | 7.63 |
| fkgl_drop | 3.50 |
| fre | 63.5 |
| fre_gain | 34.0 |
| human_edit_recall | 1.000 |
| length_ratio | 1.30 |
| n_words | 13.0 |
| nli_completeness | 0.761 |
| nli_faithfulness | 0.208 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 50.92 |
| smog | 11.21 |
| smog_drop | 1.82 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `good historian` -> `person who appears to give clear health history` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Overall the patient appears to be a reliable reporter.

| metric | value |
|---|---:|
| bertscore_f1 | 0.390 |
| coleman_liau | 9.91 |
| coleman_liau_drop | 1.04 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 11.52 |
| fkgl_drop | -0.39 |
| fre | 28.5 |
| fre_gain | -1.0 |
| human_edit_recall | 1.000 |
| length_ratio | 0.90 |
| n_words | 9.0 |
| nli_completeness | 0.064 |
| nli_faithfulness | 0.062 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 36.53 |
| smog | 13.02 |
| smog_drop | 0.00 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `seemingly` -> `appears to be` | replace | attributed | 0.112 | 0.136 | - | 0.787 | 0.991 | - |
| `good historian` -> `reliable reporter` | replace | attributed | -0.832 | -1.577 | - | 0.685 | 0.044 | - |

**edit `seemingly` -> `appears to be`**

- status: `attributed`
- log p full -1.6654, empty -1.7772
- masks scored: 18/18 (+4 top-k)
- ranked sources:
    - `+0.991` [dictionary] Seemingly (adv.): In appearance; in show; in semblance; apparently; ostensibly.
    - `-0.029` [wiktionary] good: If something is good it is useful or helpful. This also means high quality.
    - `-0.062` [wiktionary] good: When you are good, you do the right things. That is, you do things that are kind or helpful. You do not 

- rationale: You explain, to a patient, why one phrase in a medical sentence was replaced with another.
- audit: coverage 0.0, grounding_error=False, omission=True, source_ok=True, passage_ok=True

**edit `good historian` -> `reliable reporter`**

- status: `attributed`
- log p full -1.2455, empty -0.4130
- masks scored: 18/18 (+4 top-k)
- ranked sources:
    - `+0.857` [wiktionary] good: When you are good, you do the right things. That is, you do things that are kind or helpful. You do not 
    - `+0.813` [wiktionary] historian: A historian is a person who studies or writes about history.
    - `+0.491` [dictionary] Seemingly (adv.): In appearance; in show; in semblance; apparently; ostensibly.
    - `-2.250` [wiktionary] good: If something is good it is useful or helpful. This also means high quality.

- rationale: A "good historian" means a patient who gives clear, consistent, and useful information about their symptoms and past health, and "reliable reporter" keeps that idea of trustworthiness and usefulness in everyday words. Phrase frequency rises from Zipf 3.90 to 4.02, while age of acquisition falls from 11.58 to 9.32. Readers can now grasp the intended praise for the patient's account without needing clinical jargon.
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

**output:** No flare-up of Crohn’s disease was found during the look inside the colon.

| metric | value |
|---|---:|
| bertscore_f1 | 0.577 |
| coleman_liau | 8.25 |
| coleman_liau_drop | 1.41 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.333 |
| fkgl | 5.82 |
| fkgl_drop | -2.17 |
| fre | 76.5 |
| fre_gain | -10.2 |
| human_edit_recall | 1.000 |
| length_ratio | 1.07 |
| n_words | 15.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.910 |
| nli_faithfulness | 0.979 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 41.10 |
| smog | 3.13 |
| smog_drop | 0.00 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `active Crohn 's disease` -> `Crohn’s disease` | replace | - | - | - | - | - | - | - |
| `colonoscopy` -> `look inside the colon` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** No signs of a current Crohn’s flare-up were seen during the exam of the large intestine by a flexible tube.

| metric | value |
|---|---:|
| bertscore_f1 | 0.439 |
| coleman_liau | 7.37 |
| coleman_liau_drop | 2.29 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.250 |
| fkgl | 8.73 |
| fkgl_drop | -5.08 |
| fre | 68.1 |
| fre_gain | -18.6 |
| human_edit_recall | 1.000 |
| length_ratio | 1.57 |
| n_words | 22.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.810 |
| nli_faithfulness | 0.796 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.250 |
| sari | 14.38 |
| smog | 11.21 |
| smog_drop | -8.08 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `active Crohn 's disease` -> `Crohn’s flare-up` | replace | attributed | 2.090 | 2.273 | 0.576 | 0.899 | 0.208 | - |
| `colonoscopy` -> `exam of the large intestine by a flexible tube` | replace | attributed | 10.679 | 10.712 | 0.802 | 0.865 | 1.757 | - |

**edit `active Crohn 's disease` -> `Crohn’s flare-up`**

- status: `attributed`
- log p full -1.6804, empty -3.7703
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.506` [readme] colonoscopy: A colonoscopy is a test that checks the inside of your large intestine for signs of cancer.
    - `+0.297` [readme] active: Currently happening.
    - `+0.081` [nih] colonoscopy: Examination of the inside of the colon using a colonoscope, inserted into the rectum. A colonosco
    - `+0.066` [justplainclear] colonoscopy: An exam of the inside of the large intestine that uses a flexible tube with a lens at the end
    - `+0.063` [readme] Hashimoto 's disease: When the immune system attacks the thyroid gland in the neck.

- rationale: The original term refers to a period when Crohn’s disease is actively causing symptoms, and “Crohn’s flare-up” conveys that same idea of a worsening episode in everyday language. Phrase frequency rises from Zipf 1.52 to 2.74, while syllable count drops from 6 to 3. Readers can now recognize a flare-up as the active phase without needing the clinical label.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `colonoscopy` -> `exam of the large intestine by a flexible tube`**

- status: `attributed`
- log p full -3.4229, empty -14.1016
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+3.824` [justplainclear] colonoscopy: An exam of the inside of the large intestine that uses a flexible tube with a lens at the end
    - `+2.067` [michigan] colonoscopy: Looks at the inside of the large intestine using a flexible tube with a ltiny camera at the end.
    - `+1.243` [readme] colonoscopy: A procedure to check for colon cancer by examining the inside of the large intestine.
    - `+1.185` [readme] colonoscopy: A colonoscopy is a test that checks the inside of your large intestine for signs of cancer.
    - `+0.614` [readme] active: Currently happening.

- rationale: The source describes a colonoscopy as an exam of the inside of the large intestine that uses a flexible tube with a lens at the end, so "exam of the large intestine by a flexible tube" keeps the procedure and the tool in plain words. Phrase frequency increases from Zipf 2.74 to 3.12, while age of acquisition falls from 15.76 to 9.28. Patients can understand what is being looked at and how without first knowing the medical name.
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

**output:** Shortly after the first check, the patient seemed to start complaining of chest pain and looked to the nurse like exhaustion and trouble breathing were getting worse.

| metric | value |
|---|---:|
| bertscore_f1 | 0.756 |
| coleman_liau | 12.75 |
| coleman_liau_drop | 3.22 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.333 |
| fkgl | 11.11 |
| fkgl_drop | 5.24 |
| fre | 63.5 |
| fre_gain | 37.6 |
| human_edit_recall | 1.000 |
| length_ratio | 0.96 |
| n_words | 27.0 |
| nli_completeness | 0.993 |
| nli_faithfulness | 0.993 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.667 |
| sari | 23.01 |
| smog | 11.21 |
| smog_drop | 4.70 |
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

**output:** Shortly after the patient's initial assessment, the patient apparently began to complain of chest pain and appeared to the nurse to have growing tiredness and having difficulty breathing.

| metric | value |
|---|---:|
| bertscore_f1 | 0.884 |
| coleman_liau | 15.66 |
| coleman_liau_drop | 0.31 |
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
| nli_completeness | 0.994 |
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
| `mounting exhaustion` -> `growing tiredness` | replace | attributed | 0.366 | 0.614 | - | 0.822 | 0.102 | - |
| `respiratory distress` -> `having difficulty breathing` | replace | attributed | 14.321 | 14.940 | - | 0.880 | 12.733 | - |

**edit `mounting exhaustion` -> `growing tiredness`**

- status: `attributed`
- log p full -0.7378, empty -1.1039
- masks scored: 34/34 (+4 top-k)
- ranked sources:
    - `+0.380` [wiktionary] mounting: If you mount something you get on to it.
    - `+0.278` [wiktionary] exhaustion: Exhaustion is the point where something is completely depleted.
    - `+0.271` [readme] acute respiratory distress syndrome: A serious lung condition that causes low levels of oxygen in the blood, w
    - `-0.195` [readme] Respiratory Distress: Having difficulty breathing.
    - `-0.828` [wiktionary] exhaustion: Exhaustion is the state of extreme tiredness.

- rationale: The original term "mounting exhaustion" means a tiredness that is building up and getting worse, and "growing tiredness" carries that same sense of increasing fatigue in plain words. Phrase frequency decreases from Zipf 3.34 to 2.92, while age of acquisition falls from 7.61 to 7.22. Readers can now see the worsening fatigue described without the more formal, clinical phrasing.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `respiratory distress` -> `having difficulty breathing`**

- status: `attributed`
- log p full -0.7731, empty -15.0938
- masks scored: 34/34 (+4 top-k)
- ranked sources:
    - `+13.182` [readme] Respiratory Distress: Having difficulty breathing.
    - `+0.449` [wiktionary] mounting: If you mount something you get on to it.
    - `+0.419` [wiktionary] exhaustion: Exhaustion is the point where something is completely depleted.
    - `+0.354` [wiktionary] exhaustion: Exhaustion is the state of extreme tiredness.
    - `+0.257` [readme] acute respiratory distress syndrome: A serious lung condition that causes low levels of oxygen in the blood, w

- rationale: Having difficulty breathing means the body is not getting enough air, so "having difficulty breathing" keeps that core idea in everyday language. Phrase frequency rises from Zipf 3.57 to 3.99, while age of acquisition falls from 11.16 to 6.83. Readers can grasp the problem immediately without medical terminology.
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

**output:** She has been sent to a doctor to get a pacemaker put in.

| metric | value |
|---|---:|
| bertscore_f1 | 0.612 |
| coleman_liau | 1.11 |
| coleman_liau_drop | 10.57 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 4.00 |
| fkgl_drop | 4.18 |
| fre | 89.5 |
| fre_gain | 38.9 |
| human_edit_recall | 1.000 |
| length_ratio | 1.44 |
| n_words | 13.0 |
| nli_completeness | 0.993 |
| nli_faithfulness | 0.957 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 23.47 |
| smog | 8.84 |
| smog_drop | 2.37 |

### Stage 4 - arm `termonly`

**output:** She has been sent for a small device to be put in to help the heart beat.

| metric | value |
|---|---:|
| bertscore_f1 | 0.397 |
| coleman_liau | 1.56 |
| coleman_liau_drop | 10.11 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 3.53 |
| fkgl_drop | 4.65 |
| fre | 100.0 |
| fre_gain | 49.3 |
| human_edit_recall | 1.000 |
| length_ratio | 1.89 |
| n_words | 17.0 |
| nli_completeness | 0.050 |
| nli_faithfulness | 0.894 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 23.47 |
| smog | 3.13 |
| smog_drop | 8.08 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `referred` -> `sent` | replace | - | - | - | - | - | - | - |
| `pacemaker implantation` -> `small device to be put in to help the heart beat` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** She has been sent for care to have a small device placed in her chest to help control her heartbeat.

| metric | value |
|---|---:|
| bertscore_f1 | 0.473 |
| coleman_liau | 5.92 |
| coleman_liau_drop | 5.75 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.750 |
| fkgl | 5.78 |
| fkgl_drop | 2.40 |
| fre | 89.2 |
| fre_gain | 38.6 |
| human_edit_recall | 1.000 |
| length_ratio | 2.22 |
| n_words | 20.0 |
| nli_completeness | 0.183 |
| nli_faithfulness | 0.916 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 21.67 |
| smog | 3.13 |
| smog_drop | 8.08 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `referred` -> `sent for care` | replace | attributed | 9.317 | 10.025 | 0.838 | 0.889 | 9.917 | - |
| `pacemaker implantation` -> `small device placed in her chest to help control her heartbeat` | replace | attributed | 6.821 | 6.939 | 0.890 | 0.946 | 2.071 | - |

**edit `referred` -> `sent for care`**

- status: `attributed`
- log p full -0.6779, empty -9.9946
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+10.365` [readme] REFERRED: Sending a patient to another person or place for medical care.
    - `+0.448` [nih] pacemaker: An electronic device that is implanted in the body to monitor heart rate and rhythm. It gives the h
    - `+0.171` [justplainclear] pacemaker: A medical device placed inside your chest or abdomen that helps control your heartbeat
    - `+0.116` [readme] pacemaker: A pacemaker is a device that uses electrical signals to regulate the heartbeat.

- rationale: The readme defines referred as sending a patient to another person or place for medical care, so "sent for care" keeps that transfer-of-care idea in plain words. Phrase frequency rises from Zipf 4.61 to 5.01, while syllables increase from 2 to 3. Readers can see who is being moved and why without needing the clinical verb.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `pacemaker implantation` -> `small device placed in her chest to help control her heartbeat`**

- status: `attributed`
- log p full -2.1929, empty -9.0137
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+4.454` [readme] pacemaker: A small device that helps regulate the heartbeat when placed in the chest.
    - `+2.383` [justplainclear] pacemaker: A medical device placed inside your chest or abdomen that helps control your heartbeat
    - `+0.859` [readme] implantation: Surgery where a device is placed inside your body.
    - `+0.508` [readme] pacemaker: A pacemaker is a device that uses electrical signals to regulate the heartbeat.

- rationale: The readme describes a pacemaker implantation as a small device that helps regulate the heartbeat when placed in the chest, so "small device placed in her chest to help control her heartbeat" keeps that device-and-function meaning in plain words. Phrase frequency rises from Zipf 2.69 to 3.54, while age of acquisition falls from 12.42 to 8.06. Patients can picture the procedure and its purpose without needing the clinical label.
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

**output:** There was some bruising and a collection of blood at the site where the catheter was placed.

| metric | value |
|---|---:|
| bertscore_f1 | 0.711 |
| coleman_liau | 8.05 |
| coleman_liau_drop | -3.62 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 6.31 |
| fkgl_drop | -6.98 |
| fre | 80.1 |
| fre_gain | -34.0 |
| human_edit_recall | 1.000 |
| length_ratio | 1.31 |
| n_words | 17.0 |
| nli_completeness | 0.320 |
| nli_faithfulness | 0.447 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 69.00 |
| smog | 11.21 |
| smog_drop | -8.08 |

### Stage 4 - arm `termonly`

**output:** There was some bruising with a collection of blood at the place where the tube was put in.

| metric | value |
|---|---:|
| bertscore_f1 | 0.612 |
| coleman_liau | 5.76 |
| coleman_liau_drop | -1.33 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.667 |
| fkgl | 5.20 |
| fkgl_drop | -5.87 |
| fre | 89.9 |
| fre_gain | -24.2 |
| human_edit_recall | 1.000 |
| length_ratio | 1.38 |
| n_words | 18.0 |
| nli_completeness | 0.261 |
| nli_faithfulness | 0.569 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 63.08 |
| smog | 8.84 |
| smog_drop | -5.71 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `hematoma` -> `bruising with a collection of blood` | replace | - | - | - | - | - | - | - |
| `cath site` -> `place where the tube was put in` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** There was some bruise at the place where the tube went in.

| metric | value |
|---|---:|
| bertscore_f1 | 0.536 |
| coleman_liau | 3.97 |
| coleman_liau_drop | 0.46 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.667 |
| fkgl | 0.89 |
| fkgl_drop | -1.56 |
| fre | 110.1 |
| fre_gain | -4.1 |
| human_edit_recall | 1.000 |
| length_ratio | 0.92 |
| n_words | 12.0 |
| nli_completeness | 0.281 |
| nli_faithfulness | 0.397 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 54.80 |
| smog | 3.13 |
| smog_drop | 0.00 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `hematoma` -> `bruise` | replace | attributed | 1.291 | 1.668 | 0.863 | 0.880 | 1.567 | - |
| `cath site` -> `place where the tube went in` | replace | attributed | 1.117 | 1.214 | 0.657 | 0.724 | 0.221 | - |

**edit `hematoma` -> `bruise`**

- status: `attributed`
- log p full -0.9472, empty -2.2377
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+2.608` [iowa] HEMATOMA: a bruise, a black and blue mark
    - `+1.041` [michigan] hematoma: A bruise or when your skin is black and blue after an injury.
    - `+0.344` [wiktionary] site: A site is a website.
    - `-0.040` [wiktionary] site: A site is a location or a place.
    - `-0.230` [justplainclear] hematoma: A collection of blood under the skin or in the body that is typically caused by a broken blood vesse

- rationale: The source describes a hematoma as a bruise, a black and blue mark, so "bruise" keeps the idea of a localized collection of blood under the skin in plain words. Phrase frequency increases from Zipf 2.61 to 3.18, while age of acquisition falls from 14.78 to 5.45. Patients can now recognize the injury by a familiar everyday term rather than a medical label.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `cath site` -> `place where the tube went in`**

- status: `attributed`
- log p full -2.0245, empty -3.1411
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.414` [wiktionary] site: A site is a location or a place.
    - `+0.192` [iowa] HEMATOMA: a bruise, a black and blue mark
    - `+0.141` [michigan] hematoma: A bruise or when your skin is black and blue after an injury.
    - `+0.099` [wiktionary] site: A site is a website.

- rationale: The source describes a site as a location or a place, so "place where the tube went in" keeps the idea of a specific location in plain words. Phrase frequency increases from Zipf 2.90 to 4.30, while age of acquisition falls from 8.63 to 5.50. Patients can now picture exactly where the procedure entered the body without needing the shorthand "cath site".
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

**output:** The dead tissue was lifted out of the belly.

| metric | value |
|---|---:|
| bertscore_f1 | 0.846 |
| coleman_liau | 3.47 |
| coleman_liau_drop | 3.87 |
| copy_jargon_rate | 0.333 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| diagnostic_identity_preservation | 1.000 |
| fkgl | 3.65 |
| fkgl_drop | 2.62 |
| fre | 84.9 |
| fre_gain | 18.8 |
| human_edit_recall | 0.667 |
| length_ratio | 1.00 |
| n_words | 9.0 |
| nli_completeness | 0.991 |
| nli_faithfulness | 0.994 |
| replacement_f1 | 0.800 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 53.39 |
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
| `necrotic tissue` -> `dead tissue` | replace | attributed | -0.415 | -3.139 | 0.556 | 0.736 | 0.033 | - |

**edit `necrotic tissue` -> `dead tissue`**

- status: `attributed`
- log p full -0.4388, empty -0.0236
- masks scored: 66/66 (+2 top-k)
- ranked sources:
    - `+0.165` [readme] TISSUE: A bunch of cells teaming up to do a job.
    - `+0.132` [wiktionary] tissue: Tissue is a group of cells that work together to do a job.
    - `-0.032` [readme] necrotic: Tissue or skin death.
    - `-0.098` [wiktionary] tissue: A piece of tissue is a sheet of paper that can absorb very well.
    - `-0.121` [readme] Necrotic: Necrotic means when tissue or skin dies.

- rationale: You explain, to a patient, why one phrase in a medical sentence was replaced with another.
- audit: coverage 0.0, grounding_error=False, omission=True, source_ok=True, passage_ok=True

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

**output:** Pressure was kept on the area and it stopped bleeding.

| metric | value |
|---|---:|
| bertscore_f1 | 0.748 |
| coleman_liau | 6.76 |
| coleman_liau_drop | 1.29 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 4.83 |
| fkgl_drop | 1.88 |
| fre | 78.2 |
| fre_gain | 17.0 |
| human_edit_recall | 1.000 |
| length_ratio | 1.25 |
| n_words | 10.0 |
| nli_completeness | 0.627 |
| nli_faithfulness | 0.278 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 32.56 |
| smog | 8.84 |
| smog_drop | 2.37 |

### Stage 4 - arm `termonly`

**output:** Pressure was held and the area was no longer bleeding.

| metric | value |
|---|---:|
| bertscore_f1 | 0.858 |
| coleman_liau | 6.76 |
| coleman_liau_drop | 1.29 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 6.01 |
| fkgl_drop | 0.70 |
| fre | 69.8 |
| fre_gain | 8.6 |
| human_edit_recall | 1.000 |
| length_ratio | 1.25 |
| n_words | 10.0 |
| nli_completeness | 0.504 |
| nli_faithfulness | 0.476 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 67.13 |
| smog | 8.84 |
| smog_drop | 2.37 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `hemostatic` -> `no longer bleeding` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Pressure was held and the area was stopping bleeding.

| metric | value |
|---|---:|
| bertscore_f1 | 0.896 |
| coleman_liau | 9.27 |
| coleman_liau_drop | -1.22 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 6.28 |
| fkgl_drop | 0.43 |
| fre | 66.1 |
| fre_gain | 4.9 |
| human_edit_recall | 1.000 |
| length_ratio | 1.12 |
| n_words | 9.0 |
| nli_completeness | 0.524 |
| nli_faithfulness | 0.489 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 67.96 |
| smog | 8.84 |
| smog_drop | 2.37 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `hemostatic` -> `stopping bleeding` | replace | attributed | 8.381 | 9.543 | - | 1.000 | 4.135 | - |

**edit `hemostatic` -> `stopping bleeding`**

- status: `attributed`
- log p full -0.3752, empty -8.7559
- masks scored: 6/6 (+1 top-k)
- ranked sources:
    - `+6.799` [readme] hemostatic: Hemostatic means stopping bleeding.
    - `+2.664` [readme] hemostatic: Stopping blood flow.

- rationale: You explain, to a patient, why one phrase in a medical sentence was replaced with another.
- audit: coverage 0.0, grounding_error=False, omission=True, source_ok=True, passage_ok=True

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

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `lavaged` -> `washed` | replace | - | - | - | - | - | - | - |
| `saline` -> `salt water` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** The area was cleaned with some salt water and cleared.

| metric | value |
|---|---:|
| bertscore_f1 | 0.859 |
| coleman_liau | 6.76 |
| coleman_liau_drop | 0.57 |
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
| nli_completeness | 0.982 |
| nli_faithfulness | 0.991 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 75.42 |
| smog | 8.84 |
| smog_drop | 0.00 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `lavaged` -> `cleaned` | replace | attributed | 2.330 | 3.077 | - | 0.818 | 3.044 | - |
| `saline` -> `salt water` | replace | attributed | 0.103 | 0.584 | - | 0.912 | 2.154 | - |

**edit `lavaged` -> `cleaned`**

- status: `attributed`
- log p full -0.5953, empty -2.9257
- masks scored: 34/34 (+4 top-k)
- ranked sources:
    - `+3.044` [readme] lavaged: To clean out an organ or wound with fluid.
    - `-0.015` [readme] Saline: Salt water solution used to replace body fluids.
    - `-0.078` [readme] saline: A solution made of saltwater that matches the body's fluid concentration and can be used to replace lo

- rationale: The original term “lavaged” means washed out or rinsed, typically with fluid, and “cleaned” carries that same idea of removing material by washing in plain words. Phrase frequency rises from Zipf 0.00 to 4.02, while syllable count stays at 1. Readers can now grasp that the area was washed without needing a medical verb.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `saline` -> `salt water`**

- status: `attributed`
- log p full -0.1470, empty -0.2501
- masks scored: 34/34 (+4 top-k)
- ranked sources:
    - `+2.428` [readme] Saline: Salt water solution used to replace body fluids.
    - `+0.274` [readme] lavaged: To clean out an organ or wound with fluid.
    - `+0.260` [nih] saline: A solution of salt and water.
    - `-0.558` [readme] saline: A solution made of saltwater that matches the body's fluid concentration and can be used to replace lo
    - `-1.210` [wiktionary] saline: If something is saline it is salty, especially water containing salt.

- rationale: Saline is a sterile solution of salt dissolved in water used for medical irrigation and hydration, and "salt water" keeps that core idea in everyday words. Phrase frequency rises from Zipf 3.33 to 4.55, while age of acquisition falls from 11.71 to 5.05. Readers can picture the fluid being used without needing a clinical label.
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

### Stage 4 - arm `termonly`

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
| `inability to ambulate` -> `not being able to walk` | replace | - | - | - | - | - | - | - |

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
| `inability to ambulate` -> `not being able to walk` | replace | attributed | 0.040 | 0.066 | 0.641 | 0.791 | 0.018 | - |

**edit `inability to ambulate` -> `not being able to walk`**

- status: `attributed`
- log p full -0.9252, empty -0.9655
- masks scored: 66/66 (+2 top-k)
- ranked sources:
    - `+0.245` [justplainclear] ambulate: Walk, move around
    - `+0.227` [wiktionary] to: To has no meaning. It is used with a bare infinitival clause.
    - `+0.167` [michigan] ambulate: To walk or move around.
    - `+0.101` [readme] ambulate: To ambulate means to walk or move around.

- rationale: The original term means a person cannot walk, and the replacement says the same idea in everyday words. Phrase frequency rises from Zipf 1.40 to 4.87, while age of acquisition falls from 10.67 to 7.79, and syllables drop from 9 to 7. Readers can grasp the mobility limitation immediately without medical wording.
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
| `hernia` -> `bulge` | replace | attributed | 0.076 | 0.715 | - | 0.786 | 1.555 | - |

**edit `hernia` -> `bulge`**

- status: `attributed`
- log p full -0.0788, empty -0.1551
- masks scored: 10/10 (+2 top-k)
- ranked sources:
    - `+1.413` [justplainclear] hernia: When part of an organ or tissue inside of you bulges through a weak area of muscle. Most hernias are i
    - `-0.142` [readme] hernia: A hernia is when an organ pokes through a hole in a muscle.
    - `-0.364` [nih] hernia: The bulging of an internal organ through a weak area or tear in the muscle or other tissue that holds 

- rationale: A hernia is a bulge where tissue pushes through a weak spot in the muscle or connective tissue wall, so "bulge" keeps the visible protrusion idea in plain words. Phrase frequency increases from Zipf 3.00 to 3.24, while age of acquisition falls from 12.29 to 8.10. Readers can picture the physical sign without needing the medical label.
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

**output:** Other systems were checked and were normal.

| metric | value |
|---|---:|
| bertscore_f1 | 0.738 |
| coleman_liau | 9.80 |
| coleman_liau_drop | 1.60 |
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
| nli_completeness | 0.972 |
| nli_faithfulness | 0.989 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.667 |
| sari | 23.57 |
| smog | 3.13 |
| smog_drop | 5.71 |

### Stage 4 - arm `termonly`

**output:** Other systems were reviewed and were found to be normal.

| metric | value |
|---|---:|
| bertscore_f1 | 1.000 |
| coleman_liau | 7.92 |
| coleman_liau_drop | 3.48 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 4.83 |
| fkgl_drop | 3.54 |
| fre | 78.2 |
| fre_gain | 25.4 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 10.0 |
| negation_preservation | 0.000 |
| nli_completeness | 0.970 |
| nli_faithfulness | 0.992 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 100.00 |
| smog | 3.13 |
| smog_drop | 5.71 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `unremarkable` -> `normal` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Other systems were reviewed and were found to be common and ordinary.

| metric | value |
|---|---:|
| bertscore_f1 | 0.799 |
| coleman_liau | 9.28 |
| coleman_liau_drop | 2.12 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 7.77 |
| fkgl_drop | 0.60 |
| fre | 60.7 |
| fre_gain | 7.8 |
| human_edit_recall | 1.000 |
| length_ratio | 1.20 |
| n_words | 12.0 |
| negation_preservation | 0.000 |
| nli_completeness | 0.972 |
| nli_faithfulness | 0.825 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 66.67 |
| smog | 8.84 |
| smog_drop | 0.00 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `unremarkable` -> `common and ordinary` | replace | attributed | 13.375 | 14.206 | - | - | - | - |

**edit `unremarkable` -> `common and ordinary`**

- status: `attributed`
- log p full -0.5719, empty -13.9466
- masks scored: 4/4 (+1 top-k)
- ranked sources:
    - `+14.357` [wiktionary] unremarkable: If something is unremarkable, it is common and ordinary.

- rationale: The original term means not worthy of comment or not notable, so "common and ordinary" carries that sense of being unexceptional in plain words. Phrase frequency increases from Zipf 2.83 to 4.35, while age of acquisition falls from 11.06 to 8.63. Readers can now see the finding is routine rather than needing specialist interpretation.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True
