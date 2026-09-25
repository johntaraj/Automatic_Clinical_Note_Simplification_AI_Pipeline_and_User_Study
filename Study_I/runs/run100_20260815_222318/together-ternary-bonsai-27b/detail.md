# Step-by-step detail - together-ternary-bonsai-27b (`run100`)

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

**output:** He lost the ability to feel pleasure and lost interest in social activities, and he had trouble sleeping because he woke up often and felt restless.

| metric | value |
|---|---:|
| bertscore_f1 | 0.657 |
| coleman_liau | 10.05 |
| coleman_liau_drop | 8.91 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 12.70 |
| fkgl_drop | 3.32 |
| fre | 50.3 |
| fre_gain | 39.9 |
| human_edit_recall | 1.000 |
| length_ratio | 1.30 |
| n_words | 26.0 |
| nli_completeness | 0.992 |
| nli_faithfulness | 0.991 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.714 |
| sari | 25.30 |
| smog | 11.21 |
| smog_drop | 4.70 |

### Stage 4 - arm `termonly`

**output:** He became unable to feel pleasure and uninterested in social activities, and had difficulty sleeping for frequent waking and restlessness.

| metric | value |
|---|---:|
| bertscore_f1 | 0.988 |
| coleman_liau | 16.65 |
| coleman_liau_drop | 2.31 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 15.22 |
| fkgl_drop | 0.81 |
| fre | 21.6 |
| fre_gain | 11.1 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 20.0 |
| nli_completeness | 0.990 |
| nli_faithfulness | 0.994 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 74.23 |
| smog | 15.90 |
| smog_drop | 0.00 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `anhedonic` -> `unable to feel pleasure` | replace | - | - | - | - | - | - | - |
| `disinterested` -> `uninterested` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** He became unable to feel pleasure and not interested in social activities, and had difficulty sleeping for frequent waking and restlessness.

| metric | value |
|---|---:|
| bertscore_f1 | 0.951 |
| coleman_liau | 15.38 |
| coleman_liau_drop | 3.58 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 14.51 |
| fkgl_drop | 1.51 |
| fre | 28.4 |
| fre_gain | 18.0 |
| human_edit_recall | 1.000 |
| length_ratio | 1.05 |
| n_words | 21.0 |
| nli_completeness | 0.991 |
| nli_faithfulness | 0.991 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 72.24 |
| smog | 15.90 |
| smog_drop | 0.00 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `anhedonic` -> `unable to feel pleasure` | replace | attributed | -0.023 | -0.023 | - | 0.400 | 0.175 | -0.12307850000000009 |
| `disinterested` -> `not interested` | replace | attributed | 1.929 | 2.012 | - | 0.800 | 2.922 | 2.987269359999999 |

**edit `anhedonic` -> `unable to feel pleasure`**

- status: `attributed`
- log p full -4.1028, empty -4.0800
- masks scored: 6/6 (+2 top-k)
- ranked sources:
    - `+0.076` [wiktionary] disinterested: If someone is disinterested, they are not affected by a situation, so they can make fair decisi
    - `-0.099` [wiktionary] disinterested: If someone is disinterested, they are not interested in something; they find it boring.

- rationale: The original term describes a clinical state where a person loses the capacity to experience joy or satisfaction, so replacing it with "unable to feel pleasure" keeps that core emotional reality in plain language. Phrase frequency increases from Zipf 1.11 to 4.27, making the expression more common, while the syllable count rises from 4 to 7. You can now clearly recognize the specific type of emotional numbness you are experiencing without needing to decode specialized medical terminology.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `disinterested` -> `not interested`**

- status: `attributed`
- log p full -2.3887, empty -4.3179
- masks scored: 6/6 (+2 top-k)
- ranked sources:
    - `+2.467` [wiktionary] disinterested: If someone is disinterested, they are not interested in something; they find it boring.
    - `-0.455` [wiktionary] disinterested: If someone is disinterested, they are not affected by a situation, so they can make fair decisi

- rationale: The original term describes a state of having no personal stake or emotional involvement in a situation, so replacing it with "not interested" keeps that exact idea in plain language. Phrase frequency increases from Zipf 2.91 to 4.94, while age of acquisition drops from 12.40 to 8.83. Patients can now clearly understand the emotional distance without needing to decode academic vocabulary.
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

**output:** Doctors cannot rule out that the patient has a heart attack.

| metric | value |
|---|---:|
| bertscore_f1 | 0.468 |
| coleman_liau | 7.35 |
| coleman_liau_drop | 6.72 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.333 |
| diagnostic_identity_preservation | 1.000 |
| fkgl | 4.79 |
| fkgl_drop | 9.49 |
| fre | 80.3 |
| fre_gain | 77.0 |
| human_edit_recall | 1.000 |
| length_ratio | 1.83 |
| n_words | 11.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.844 |
| nli_faithfulness | 0.803 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 19.79 |
| smog | 3.13 |
| smog_drop | 9.89 |
| uncertainty_preservation | 0.000 |

### Stage 4 - arm `termonly`

**output:** A heart attack might still be happening.

| metric | value |
|---|---:|
| bertscore_f1 | 0.345 |
| coleman_liau | 7.31 |
| coleman_liau_drop | 6.75 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.200 |
| diagnostic_identity_preservation | 1.000 |
| fkgl | 4.00 |
| fkgl_drop | 10.29 |
| fre | 78.9 |
| fre_gain | 75.5 |
| human_edit_recall | 1.000 |
| length_ratio | 1.17 |
| n_words | 7.0 |
| negation_preservation | 0.000 |
| nli_completeness | 0.561 |
| nli_faithfulness | 0.628 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 25.97 |
| smog | 8.84 |
| smog_drop | 4.18 |
| uncertainty_preservation | 1.000 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `Myocardial infarction` -> `heart attack` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

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
| `Myocardial infarction` -> `heart attack` | replace | attributed | 1.359 | 1.388 | 0.486 | 0.949 | 0.018 | 0.4052274109999998 |
| `can not be excluded` -> `ruled out` | replace | attributed | -0.020 | -0.261 | 0.539 | 0.800 | 0.043 | 0.00858067600000001 |

**edit `Myocardial infarction` -> `heart attack`**

- status: `attributed`
- log p full -3.2767, empty -4.6359
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.860` [readme] inferior myocardial infarction: A heart attack caused by a blockage in a blood vessel that affects the lower p
    - `+0.842` [justplainclear] myocardial infarction: A heart attack
    - `+0.473` [readme] inferior wall myocardial infarction: Heart damage at the bottom of the left ventricle due to a blocked artery.
    - `+0.276` [michigan] myocardial infarction: Occurs when the flow of blood to the heart is stopped by a blood clot or a spasm of an 
    - `+0.111` [wiktionary] be: This verb tells us that a thing is present, or in a place.

- rationale: Myocardial infarction refers to the sudden blockage of blood flow to the heart muscle, and swapping it for heart attack preserves that exact medical reality while stripping away the clinical jargon. Phrase frequency increases from Zipf 2.58 to 4.89 (higher = more common = easier), while age of acquisition falls from 16.64 to 6.58 (lower = learned younger = easier). You can now grasp the severity of the condition immediately without needing to decode a foreign medical label.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `can not be excluded` -> `ruled out`**

- status: `attributed`
- log p full -0.0881, empty -0.0685
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.137` [michigan] myocardial infarction: Occurs when the flow of blood to the heart is stopped by a blood clot or a spasm of an 
    - `+0.094` [readme] inferior myocardial infarction: A heart attack caused by a blockage in a blood vessel that affects the lower p
    - `+0.091` [wiktionary] not: "Not" makes a phrase have the opposite meaning.
    - `+0.068` [readme] inferior wall myocardial infarction: Heart damage at the bottom of the left ventricle due to a blocked artery.
    - `+0.004` [wiktionary] can: If someone can do something, they are allowed to do it.

- rationale: The original phrase means that a specific illness cannot be definitively dismissed, and replacing it with "ruled out" keeps that exact warning while speaking in plain English. Phrase frequency increases from Zipf 3.89 to 4.30, while age of acquisition drops from 5.11 to 3.28, showing that the replacement is both more common and learned younger. You can now understand the doctor’s assessment of your condition without wrestling with complicated medical phrasing.
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

**output:** The patient had a large collection of blood and swelling inside the small sac under the shoulder.

| metric | value |
|---|---:|
| bertscore_f1 | 0.645 |
| coleman_liau | 9.75 |
| coleman_liau_drop | 4.55 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.750 |
| fkgl | 7.70 |
| fkgl_drop | -1.69 |
| fre | 70.1 |
| fre_gain | 0.4 |
| human_edit_recall | 1.000 |
| length_ratio | 1.21 |
| n_words | 17.0 |
| nli_completeness | 0.620 |
| nli_faithfulness | 0.635 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 42.12 |
| severity_downgrade | 0.000 |
| severity_preservation | 1.000 |
| severity_tier_input | 2.000 |
| severity_tier_output | 2.000 |
| smog | 8.84 |
| smog_drop | 0.00 |

### Stage 4 - arm `termonly`

**output:** There was clear blood collection and swelling within the fluid sac under the shoulder.

| metric | value |
|---|---:|
| bertscore_f1 | 0.694 |
| coleman_liau | 11.91 |
| coleman_liau_drop | 2.39 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 7.57 |
| fkgl_drop | -1.56 |
| fre | 65.7 |
| fre_gain | -4.1 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 14.0 |
| nli_completeness | 0.661 |
| nli_faithfulness | 0.817 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 71.44 |
| severity_downgrade | 1.000 |
| severity_preservation | 0.000 |
| severity_tier_input | 2.000 |
| smog | 8.84 |
| smog_drop | 0.00 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `marked` -> `clear` | replace | - | - | - | - | - | - | - |
| `hematoma` -> `blood collection` | replace | - | - | - | - | - | - | - |
| `subdeltoid bursa` -> `fluid sac under the shoulder` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** There was severe bruise and swelling within the shoulder fluid pouch.

| metric | value |
|---|---:|
| bertscore_f1 | 0.599 |
| coleman_liau | 12.09 |
| coleman_liau_drop | 2.21 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 5.86 |
| fkgl_drop | 0.15 |
| fre | 72.6 |
| fre_gain | 2.8 |
| human_edit_recall | 1.000 |
| length_ratio | 0.79 |
| n_words | 11.0 |
| nli_completeness | 0.682 |
| nli_faithfulness | 0.690 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 69.29 |
| severity_downgrade | 0.000 |
| severity_preservation | 1.000 |
| severity_tier_input | 2.000 |
| severity_tier_output | 3.000 |
| smog | 3.13 |
| smog_drop | 5.71 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `marked` -> `severe` | replace | attributed | -1.746 | -1.781 | 0.931 | 0.953 | 0.000 | -0.2730485699999994 |
| `hematoma` -> `bruise` | replace | attributed | -0.960 | -0.960 | 0.748 | 0.885 | 0.465 | -0.3534143400000005 |
| `subdeltoid bursa` -> `shoulder fluid pouch` | replace | attributed | 4.525 | 4.528 | 0.935 | 0.903 | 5.997 | 6.72038912 |

**edit `marked` -> `severe`**

- status: `attributed`
- log p full -4.9383, empty -3.1924
- masks scored: 66/66 (+5 top-k)
- ranked sources:
    - `-0.011` [readme] bursa: A small sac of fluid that cushions joints as they move.
    - `-0.056` [wiktionary] marked: A mark is a single line left by a pen or pencil, or any small bit of color that got onto something.
    - `-0.128` [michigan] hematoma: A bruise or when your skin is black and blue after an injury.

- rationale: "Marked" indicates a noticeable or distinct level of a symptom, and swapping it for "severe" preserves that clear sense of intensity while using a more direct clinical descriptor. Word frequency increases from Zipf 4.50 to 4.56, meaning the updated term is slightly more common and therefore easier to process. You can now grasp the exact level of your condition without needing to decode specialized medical jargon.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `hematoma` -> `bruise`**

- status: `attributed`
- log p full -8.4229, empty -7.4627
- masks scored: 66/66 (+5 top-k)
- ranked sources:
    - `+0.465` [iowa] HEMATOMA: a bruise, a black and blue mark
    - `-0.017` [justplainclear] bursa: A small sac (pouch) found in your body which is filled with fluid. Bursa help your tendons or muscles m
    - `-0.098` [readme] bursa: A small sac of fluid that cushions joints as they move.

- rationale: A hematoma describes a pool of blood that has escaped a broken vessel and pooled in the surrounding tissue, and replacing it with "bruise" keeps that exact idea by using the common everyday word for the visible swelling and discoloration that follows such a leak. Phrase frequency increases from Zipf 2.61 to 3.18, making the term more common and easier to process, while age of acquisition falls from 14.78 to 5.45, meaning the replacement is learned much younger. You can now instantly grasp what your body is doing after an injury without having to memorize or decode clinical terminology.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `subdeltoid bursa` -> `shoulder fluid pouch`**

- status: `attributed`
- log p full -5.7279, empty -10.2525
- masks scored: 66/66 (+5 top-k)
- ranked sources:
    - `+6.277` [justplainclear] bursa: A small sac (pouch) found in your body which is filled with fluid. Bursa help your tendons or muscles m
    - `+0.280` [wiktionary] marked: A mark is a single line left by a pen or pencil, or any small bit of color that got onto something.
    - `+0.262` [iowa] HEMATOMA: a bruise, a black and blue mark
    - `+0.196` [justplainclear] hematoma: A collection of blood under the skin or in the body that is typically caused by a broken blood vesse
    - `+0.027` [wiktionary] marked: Something that is marked is significant or notable.

- rationale: The justplainclear glossary describes a bursa as a small, fluid-filled sac located near your joints, so "shoulder fluid pouch" preserves that exact anatomical idea using everyday language. Phrase frequency increases from Zipf 0.00 to 3.33, and age of acquisition decreases from 15.78 to 7.94, making the updated wording more common and easier to learn. You can now grasp the location and purpose of the structure without needing to memorize a complex medical label.
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
| `hypertension` -> `high blood pressure` | replace | no_source_effect | -0.005 | -0.044 | - | - | - | None |
| `hyperlipidemia` -> `high cholesterol` | replace | attributed | 0.379 | 1.407 | 0.944 | 0.971 | 2.100 | 1.280800547 |

**edit `hypertension` -> `high blood pressure`**

- status: `no_source_effect` - LASSO shrank every source weight to zero; no individual source is load-bearing
- log p full -0.1167, empty -0.1120
- masks scored: 66/66 (+2 top-k)

- rationale: Hypertension refers to persistently elevated force in your circulatory system, so swapping it for "high blood pressure" preserves that core idea while using everyday words. Phrase frequency increases from Zipf 3.41 to 4.71, while age of acquisition falls from 16.28 to 8.95, making the replacement more common and learned earlier. You can now grasp the underlying circulatory issue without needing to memorize a clinical label first.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `hyperlipidemia` -> `high cholesterol`**

- status: `attributed`
- log p full -0.1618, empty -0.5406
- masks scored: 66/66 (+2 top-k)
- ranked sources:
    - `+2.841` [justplainclear] hyperlipidemia: High cholesterol
    - `+0.741` [michigan] hyperlipidemia: High levels of fat or fat-like substances (cholesterol). Hyperlipidemia is also called high ch
    - `+0.060` [readme] hypertension: High blood pressure is when the force of blood in the arteries is too high.

- rationale: Hyperlipidemia refers to an elevated level of lipids in the blood, so switching to "high cholesterol" preserves that core idea while using everyday language. Phrase frequency increases from Zipf 1.95 to 3.72, and syllable count shifts from 4 to 5, making the updated wording more common and easier to process. You can now grasp the exact nature of your blood lipid levels without needing to decode a specialized medical label.
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

**output:** She said she gets bladder cramps when she pees and that she has had long-term bladder infections.

| metric | value |
|---|---:|
| bertscore_f1 | 0.580 |
| coleman_liau | 9.41 |
| coleman_liau_drop | -2.59 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.333 |
| fkgl | 6.31 |
| fkgl_drop | 2.58 |
| fre | 80.1 |
| fre_gain | 11.4 |
| human_edit_recall | 1.000 |
| length_ratio | 0.78 |
| n_words | 18.0 |
| nli_completeness | 0.977 |
| nli_faithfulness | 0.993 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 11.95 |
| smog | 8.84 |
| smog_drop | 2.37 |
| temporality_preservation | 0.000 |

### Stage 4 - arm `termonly`

**output:** She complained of bladder cramps when she peed and she said she has a history of long-lasting bladder infections.

| metric | value |
|---|---:|
| bertscore_f1 | 0.708 |
| coleman_liau | 11.03 |
| coleman_liau_drop | -4.21 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 9.21 |
| fkgl_drop | -0.31 |
| fre | 62.9 |
| fre_gain | -5.8 |
| human_edit_recall | 1.000 |
| length_ratio | 0.87 |
| n_words | 20.0 |
| nli_completeness | 0.976 |
| nli_faithfulness | 0.994 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.429 |
| sari | 19.15 |
| smog | 13.02 |
| smog_drop | -1.82 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `bladder spasms` -> `bladder cramps` | replace | - | - | - | - | - | - | - |
| `urinated` -> `peed` | replace | - | - | - | - | - | - | - |
| `chronic UTIs` -> `long-lasting bladder infections` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** She did complain of sudden painful bladder tightness when she emptied her bladder and she did say that she has a history of long-lasting urinary tract infections.

| metric | value |
|---|---:|
| bertscore_f1 | 0.756 |
| coleman_liau | 11.89 |
| coleman_liau_drop | -5.07 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.667 |
| fkgl | 13.73 |
| fkgl_drop | -4.84 |
| fre | 44.7 |
| fre_gain | -24.0 |
| human_edit_recall | 1.000 |
| length_ratio | 1.22 |
| n_words | 28.0 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.991 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 37.43 |
| smog | 14.55 |
| smog_drop | -3.35 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `bladder spasms` -> `sudden painful bladder tightness` | replace | attributed | 3.605 | 3.605 | 0.843 | 0.921 | 4.327 | 4.6786007519999995 |
| `urinated` -> `emptied her bladder` | replace | attributed | 1.828 | 1.913 | 0.867 | 0.935 | 2.536 | 2.54590475 |
| `chronic UTIs` -> `long-lasting urinary tract infections` | replace | attributed | 2.130 | 2.299 | 0.927 | 0.953 | 0.204 | 1.0325175970999998 |

**edit `bladder spasms` -> `sudden painful bladder tightness`**

- status: `attributed`
- log p full -9.2100, empty -12.8151
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+5.341` [readme] spasms: When your muscles suddenly tighten up and hurt.
    - `+1.014` [wiktionary] spasms: A spasm is a sudden and jerky movement.
    - `+0.504` [justplainclear] bladder: An organ where urine collects so the body can get rid of it
    - `+0.391` [readme] chronic: An ongoing or frequently recurring health issue.
    - `+0.128` [readme] UTIs: UTIs are infections in the urinary system.

- rationale: The readme explains that bladder spasms occur when your muscles suddenly tighten up and hurt, so "sudden painful bladder tightness" preserves that exact physical sensation in everyday language. Phrase frequency increases from Zipf 2.89 to 2.85, meaning a higher score indicates more common and easier usage, while age of acquisition remains at 10.78, showing no shift in how early the concept is typically learned. Patients can now grasp the exact physical discomfort they are experiencing without needing to memorize a clinical diagnosis.
- audit: coverage 1.0, grounding_error=True, omission=False, source_ok=True, passage_ok=True

**edit `urinated` -> `emptied her bladder`**

- status: `attributed`
- log p full -2.3521, empty -4.1803
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+2.661` [wiktionary] urinated: When a person or animal urinates, it passes urine to empty the bladder.
    - `+0.125` [readme] chronic: An ongoing or frequently recurring health issue.
    - `+0.113` [readme] UTIs: UTIs are infections in the urinary system.
    - `+0.090` [readme] spasms: When your muscles suddenly tighten up and hurt.
    - `+0.068` [justplainclear] chronic: Long term, long lasting, lifelong, constant, never ending, never goes away, happens again and again

- rationale: The glossary defines urinating as the process of passing urine to empty the bladder, so "emptied her bladder" preserves that exact physical action in everyday language. Phrase frequency increases from Zipf 2.31 to 3.14, so the higher value confirms the replacement is more common and easier to process. This adjustment allows patients to grasp the bodily function immediately without needing to decode clinical terminology.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `chronic UTIs` -> `long-lasting urinary tract infections`**

- status: `attributed`
- log p full -1.7539, empty -3.8838
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+1.311` [dorland] UTIs: urinary tract infections
    - `+1.107` [readme] Chronic: A long-lasting or recurring health issue.
    - `+0.542` [michigan] chronic: Something, like a disease or symptom, that lasts for a long time.
    - `+0.261` [justplainclear] bladder: An organ where urine collects so the body can get rid of it
    - `+0.214` [nih] bladder: The organ that stores urine.

- rationale: Dorland identifies the original term as urinary tract infections, so "long-lasting urinary tract infections" carries that exact meaning into plain language. Phrase frequency increases from Zipf 2.05 to 3.06, while age of acquisition rises from 11.25 to 13.67, quantifying the exact statistical shift in term accessibility. Patients can now grasp the underlying infection pattern without needing to decode clinical abbreviations or memorize specialized medical jargon.
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

**output:** The patient's knee did not feel loose or give way, and there was no swelling.

| metric | value |
|---|---:|
| bertscore_f1 | 0.520 |
| coleman_liau | 5.43 |
| coleman_liau_drop | 0.75 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 3.63 |
| fkgl_drop | 3.56 |
| fre | 95.7 |
| fre_gain | 34.4 |
| human_edit_recall | 1.000 |
| length_ratio | 1.45 |
| n_words | 16.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.993 |
| nli_faithfulness | 0.964 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 18.91 |
| smog | 3.13 |
| smog_drop | 8.08 |

### Stage 4 - arm `termonly`

**output:** There was no giving way of the knee and no fluid buildup.

| metric | value |
|---|---:|
| bertscore_f1 | 0.699 |
| coleman_liau | 3.48 |
| coleman_liau_drop | 2.70 |
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
| sari | 45.00 |
| smog | 3.13 |
| smog_drop | 8.08 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `instability` -> `giving way` | replace | - | - | - | - | - | - | - |
| `effusion` -> `fluid buildup` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** There was no wobbling of the knee and no fluid buildup.

| metric | value |
|---|---:|
| bertscore_f1 | 0.844 |
| coleman_liau | 4.71 |
| coleman_liau_drop | 1.47 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 4.79 |
| fkgl_drop | 2.40 |
| fre | 80.3 |
| fre_gain | 19.0 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 11.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.993 |
| nli_faithfulness | 0.994 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 46.48 |
| smog | 8.84 |
| smog_drop | 2.37 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `instability` -> `wobbling` | replace | attributed | -0.046 | -0.047 | - | 0.400 | 0.085 | 0.2874061840000004 |
| `effusion` -> `fluid buildup` | replace | attributed | -0.627 | -0.641 | - | 0.894 | 0.612 | -0.17557316799999967 |

**edit `instability` -> `wobbling`**

- status: `attributed`
- log p full -3.8772, empty -3.8310
- masks scored: 6/6 (+1 top-k)
- ranked sources:
    - `+0.019` [wiktionary] instability: Instability is the condition of not being stable, which can make things uncertain or unsafe.
    - `-0.066` [nih] effusion: An abnormal collection of fluid in hollow spaces or between tissues of the body. For example, a pleu

- rationale: The original term describes a lack of steady control, so "wobbling" keeps that core idea in plain language. Phrase frequency increases from Zipf 3.71 to 2.62, while syllable count drops from 5 to 3. Patients can grasp the basic idea of unsteady control without needing to know the technical term.
- audit: coverage 1.0, grounding_error=True, omission=False, source_ok=True, passage_ok=True

**edit `effusion` -> `fluid buildup`**

- status: `attributed`
- log p full -4.1555, empty -3.5285
- masks scored: 6/6 (+1 top-k)
- ranked sources:
    - `-0.612` [nih] effusion: An abnormal collection of fluid in hollow spaces or between tissues of the body. For example, a pleu

- rationale: An effusion refers to excess liquid collecting in a body cavity, so "fluid buildup" captures that exact physical change using everyday language. Phrase frequency increases from Zipf 2.41 to 3.31, while age of acquisition decreases from 14.29 to 9.63, making the replacement both more common and learned earlier. You can now picture exactly what is happening inside your body without needing to memorize a specialized medical label.
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

**output:** Two days later, the pain stopped and she did not get it again.

| metric | value |
|---|---:|
| bertscore_f1 | 0.784 |
| coleman_liau | 3.34 |
| coleman_liau_drop | 2.23 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 3.10 |
| fkgl_drop | 1.82 |
| fre | 96.0 |
| fre_gain | 13.0 |
| human_edit_recall | 1.000 |
| length_ratio | 0.93 |
| n_words | 13.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.995 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 32.27 |
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
| `resolved` -> `went away` | replace | attributed | 0.155 | 0.183 | - | 0.656 | 0.030 | -0.025559563299999866 |
| `recurrence` -> `it come back` | replace | attributed | 0.350 | 0.630 | - | 0.817 | 0.083 | 0.17905341149999987 |

**edit `resolved` -> `went away`**

- status: `attributed`
- log p full -1.7945, empty -1.9490
- masks scored: 34/34 (+4 top-k)
- ranked sources:
    - `+0.060` [wiktionary] resolved: When a problem is resolved, it has been brought to a successful solution.
    - `+0.030` [wiktionary] recurrence: A recurrence is something that happens again.
    - `+0.029` [nih] recurrence: Cancer that has recurred (come back), usually after a period of time during which the cancer could

- rationale: The original term "resolved" means that a condition or symptom has completely disappeared, and "went away" carries that same idea in everyday language. Phrase frequency increases from Zipf 4.10 to 5.26, while syllables increase from 2 to 3. The reader can now grasp the improvement without needing to know the clinical term.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `recurrence` -> `it come back`**

- status: `attributed`
- log p full -0.6487, empty -0.9988
- masks scored: 34/34 (+4 top-k)
- ranked sources:
    - `+0.323` [wiktionary] recurrence: A recurrence is something that happens again.
    - `+0.241` [nih] recurrence: Cancer that has recurred (come back), usually after a period of time during which the cancer could
    - `+0.047` [readme] recurrence: When a disease comes back after being treated.
    - `-0.020` [wiktionary] resolved: To resolve means to create a solution for a problem.

- rationale: "Recurrence" simply means a symptom or illness reappearing after it has been cleared, and saying "it come back" carries that exact idea in plain, everyday words. Phrase frequency increases from Zipf 3.20 to 5.57, while age of acquisition falls from 11.79 to 5.31, making the replacement both more common and learned much younger. You can now clearly understand that your health issue is just returning instead of worsening into a new problem.
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

**output:** The patient has a fever, a middle ear infection, and possible sepsis.

| metric | value |
|---|---:|
| bertscore_f1 | 0.478 |
| coleman_liau | 8.32 |
| coleman_liau_drop | 8.11 |
| copy_jargon_rate | 0.500 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| diagnostic_identity_preservation | 1.000 |
| fkgl | 8.76 |
| fkgl_drop | 5.35 |
| fre | 53.7 |
| fre_gain | 47.3 |
| human_edit_recall | 0.500 |
| length_ratio | 1.50 |
| n_words | 12.0 |
| nli_completeness | 0.909 |
| nli_faithfulness | 0.772 |
| replacement_f1 | 0.667 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 48.02 |
| smog | 11.21 |
| smog_drop | 1.82 |
| uncertainty_preservation | 1.000 |

### Stage 4 - arm `termonly`

**output:** Description : Fever, middle ear infection, and possible whole-body infection.

| metric | value |
|---|---:|
| bertscore_f1 | 0.818 |
| coleman_liau | 21.51 |
| coleman_liau_drop | -5.08 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| diagnostic_identity_preservation | 1.000 |
| fkgl | 14.14 |
| fkgl_drop | -0.03 |
| fre | 9.7 |
| fre_gain | 3.3 |
| human_edit_recall | 1.000 |
| length_ratio | 1.25 |
| n_words | 10.0 |
| nli_completeness | 0.586 |
| nli_faithfulness | 0.673 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 60.71 |
| smog | 14.55 |
| smog_drop | -1.53 |
| uncertainty_preservation | 1.000 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `otitis media` -> `middle ear infection` | replace | - | - | - | - | - | - | - |
| `sepsis` -> `whole-body infection` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Description: Fever, ear infection, and possible serious blood infection.

| metric | value |
|---|---:|
| bertscore_f1 | 0.788 |
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
| nli_completeness | 0.671 |
| nli_faithfulness | 0.681 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 68.98 |
| smog | 15.90 |
| smog_drop | -2.88 |
| uncertainty_preservation | 1.000 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `otitis media` -> `ear infection` | replace | attributed | -0.613 | -1.050 | 0.733 | 0.836 | 1.200 | 1.3683835609999995 |
| `sepsis` -> `serious blood infection` | replace | attributed | 2.897 | 2.961 | 0.757 | 0.833 | 1.294 | 0.8628997460000001 |

**edit `otitis media` -> `ear infection`**

- status: `attributed`
- log p full -1.2214, empty -0.6080
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+1.529` [michigan] otitis media: Ear infection, often in the middle ear.
    - `+0.329` [michigan] sepsis: A very serious infection in your blood caused by a germ (a bacteria). Also called septicemia.
    - `+0.173` [readme] Sepsis: When bacteria get into the blood, the body's reaction can lead to tissue and organ damage, potentially

- rationale: Otitis media refers to inflammation or infection in the middle ear, so "ear infection" carries that same physical reality into plain, everyday language. Phrase frequency increases from Zipf 2.16 to 4.08, meaning the replacement is more common and easier to encounter, while syllable count drops from 5 to 4. You can now understand exactly where the problem occurs and what it involves without first learning a specialized medical term.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `sepsis` -> `serious blood infection`**

- status: `attributed`
- log p full -2.7236, empty -5.6208
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+1.683` [michigan] sepsis: A very serious infection in your blood caused by a germ (a bacteria). Also called septicemia.
    - `+0.390` [nih] sepsis: The presence of bacteria or their toxins in the blood or tissues.
    - `+0.128` [readme] Sepsis: When bacteria get into the blood, the body's reaction can lead to tissue and organ damage, potentially
    - `+0.062` [thesaurus] otitis media: middle ear infection
    - `+0.031` [readme] sepsis: A severe condition where the body reacts to bacteria in the bloodstream by harming tissues and organs,

- rationale: The Michigan source defines sepsis as a very serious infection in your blood caused by a germ, so "serious blood infection" preserves that core idea in everyday language. Phrase frequency increases from Zipf 3.01 to 4.20, while age of acquisition falls from 16.33 to 8.05, marking a clear shift toward more common and earlier-learned vocabulary. This adjustment allows patients to grasp the severity of the condition immediately without needing to memorize a clinical label.
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

**output:** Right now, her main problem is fatigue that she feels throughout the day.

| metric | value |
|---|---:|
| bertscore_f1 | 0.643 |
| coleman_liau | 8.25 |
| coleman_liau_drop | 3.57 |
| copy_jargon_rate | 1.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.333 |
| fkgl | 4.00 |
| fkgl_drop | 3.63 |
| fre | 89.5 |
| fre_gain | 26.0 |
| human_edit_recall | 0.000 |
| length_ratio | 0.93 |
| n_words | 13.0 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.994 |
| number_unit_preservation | 0.500 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 29.50 |
| smog | 3.13 |
| smog_drop | 8.08 |
| temporality_preservation | 1.000 |

### Stage 4 - arm `termonly`

**output:** Currently, the main problem is tiredness that she feels throughout the day.

| metric | value |
|---|---:|
| bertscore_f1 | 0.754 |
| coleman_liau | 11.70 |
| coleman_liau_drop | 0.12 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 6.79 |
| fkgl_drop | 0.84 |
| fre | 67.8 |
| fre_gain | 4.3 |
| human_edit_recall | 1.000 |
| length_ratio | 0.86 |
| n_words | 12.0 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.994 |
| number_unit_preservation | 0.500 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.250 |
| sari | 35.71 |
| smog | 11.21 |
| smog_drop | 0.00 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `primary complaint` -> `main problem` | replace | - | - | - | - | - | - | - |
| `fatigue` -> `tiredness` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Currently, her main problem is tiredness that she feels throughout the day.

| metric | value |
|---|---:|
| bertscore_f1 | 0.771 |
| coleman_liau | 11.70 |
| coleman_liau_drop | 0.12 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 6.79 |
| fkgl_drop | 0.84 |
| fre | 67.8 |
| fre_gain | 4.3 |
| human_edit_recall | 1.000 |
| length_ratio | 0.86 |
| n_words | 12.0 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.994 |
| number_unit_preservation | 0.500 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.250 |
| sari | 35.71 |
| smog | 11.21 |
| smog_drop | 0.00 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `primary complaint` -> `main problem` | replace | attributed | 0.882 | 0.986 | 0.892 | 0.948 | 0.403 | 0.7580983299999999 |
| `fatigue` -> `tiredness` | replace | attributed | -2.406 | -2.778 | 0.797 | 0.896 | 0.478 | 0.2987018260000007 |

**edit `primary complaint` -> `main problem`**

- status: `attributed`
- log p full -1.8497, empty -2.7320
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.942` [readme] complaint: A complaint is when a patient talks about their illness or problem.
    - `+0.539` [wiktionary] complaint: A complaint is a small medical problem.
    - `+0.022` [wiktionary] fatigue: Fatigue is the extreme tiredness which is the result of having mental or physical exertion or illness

- rationale: The readme explains that a complaint simply refers to what a patient describes as their illness or issue, so swapping it for "main problem" preserves that straightforward idea in everyday language. Phrase frequency increases from Zipf 4.21 to 5.01, while age of acquisition decreases from 8.89 to 6.55, showing that the new phrasing is more common and learned younger. With this clearer wording, you can immediately recognize what your doctor is focusing on without getting tangled in clinical jargon.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `fatigue` -> `tiredness`**

- status: `attributed`
- log p full -3.5104, empty -1.1045
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.634` [justplainclear] fatigue: Tired, weak feeling of the whole body, feeling tired
    - `+0.156` [wiktionary] primary: A primary is a kind of election held by a political party to choose the people it prefers for public 
    - `+0.131` [wiktionary] complaint: A complaint is an expression of dissatisfaction
    - `+0.077` [michigan] fatigue: tired, weak feeling of the whole body, feeling tired all over
    - `+0.042` [michigan] complaint: Your illness or symptom that is most important; the main reason you go to the doctor. Also known as

- rationale: The original term describes a state of extreme physical or mental exhaustion, and "tiredness" captures that same feeling in everyday language. Phrase frequency increases from Zipf 3.86 to 2.92, while age of acquisition falls from 11.83 to 7.22. Patients can now grasp the symptom without needing to know the clinical label.
- audit: coverage 1.0, grounding_error=True, omission=False, source_ok=True, passage_ok=True

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

**output:** He has noticed irregular bowel movements with occasional loose stools, and he recently started feeling pain mostly in the left side of his neck.

| metric | value |
|---|---:|
| bertscore_f1 | 0.631 |
| coleman_liau | 11.72 |
| coleman_liau_drop | 0.22 |
| copy_jargon_rate | 0.333 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.286 |
| fkgl | 12.45 |
| fkgl_drop | -0.14 |
| fre | 48.5 |
| fre_gain | 7.9 |
| human_edit_recall | 0.667 |
| laterality_preservation | 1.000 |
| length_ratio | 1.26 |
| n_words | 24.0 |
| nli_completeness | 0.993 |
| nli_faithfulness | 0.994 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.286 |
| sari | 18.57 |
| smog | 13.02 |
| smog_drop | 0.00 |
| temporality_preservation | 0.000 |

### Stage 4 - arm `termonly`

**output:** He has noted some irregular bowel movements with occasional runny stools and sudden pain mostly in left neck.

| metric | value |
|---|---:|
| bertscore_f1 | 0.695 |
| coleman_liau | 11.88 |
| coleman_liau_drop | 0.07 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.250 |
| fkgl | 11.10 |
| fkgl_drop | 1.22 |
| fre | 47.6 |
| fre_gain | 7.0 |
| human_edit_recall | 1.000 |
| laterality_preservation | 1.000 |
| length_ratio | 0.95 |
| n_words | 18.0 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.994 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 27.99 |
| smog | 11.21 |
| smog_drop | 1.82 |
| temporality_preservation | 0.000 |

annotation backend `novita`, 4 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `stool irregularity` -> `irregular bowel movements` | replace | - | - | - | - | - | - | - |
| `loose stools` -> `runny stools` | replace | - | - | - | - | - | - | - |
| `new onset` -> `sudden` | replace | - | - | - | - | - | - | - |
| `predominantly` -> `mostly` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** He has noted some irregular bowel movements with occasional watery poop and a recent start of pain mostly in the left neck.

| metric | value |
|---|---:|
| bertscore_f1 | 0.761 |
| coleman_liau | 9.48 |
| coleman_liau_drop | 2.47 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 11.76 |
| fkgl_drop | 0.55 |
| fre | 49.9 |
| fre_gain | 9.3 |
| human_edit_recall | 1.000 |
| laterality_preservation | 1.000 |
| length_ratio | 1.16 |
| n_words | 22.0 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.988 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 31.64 |
| smog | 13.02 |
| smog_drop | 0.00 |
| temporality_preservation | 0.000 |

annotation backend `novita`, 4 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `stool irregularity` -> `irregular bowel movements` | replace | attributed | 0.440 | 0.471 | 0.885 | 0.927 | 0.770 | 1.3016158660000006 |
| `loose stools` -> `watery poop` | replace | attributed | 4.089 | 5.733 | 0.775 | 0.899 | 5.972 | 4.7254300359 |
| `new onset` -> `recent start` | replace | attributed | 1.716 | 1.851 | 0.896 | 0.934 | 0.108 | 0.5295485829999997 |
| `predominantly` -> `mostly` | replace | attributed | 0.046 | 0.158 | 0.444 | 0.760 | 0.015 | 0.002272435999999989 |

**edit `stool irregularity` -> `irregular bowel movements`**

- status: `attributed`
- log p full -2.5059, empty -2.9457
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+0.897` [dictionary] Irregularity (n.): The state or quality of being irregular; that which is irregular.
    - `+0.127` [justplainclear] stool: Also known as: bowel movement, BM, feces, poop The solid or semi-solid waste that passes out of your re
    - `+0.050` [nih] stool: The material in a bowel movement. Stool is made up of undigested food, bacteria, mucus, and cells from 

- rationale: "Stool irregularity" simply refers to changes in the consistency or timing of your waste, and swapping it for "irregular bowel movements" keeps that exact idea while using everyday language. Phrase frequency increases from Zipf 2.52 to 3.28, meaning it is more common and easier to encounter, while age of acquisition drops from 12.63 to 9.72, indicating it is learned younger and easier to understand. You can now grasp the core digestive issue without needing to decode clinical jargon.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `loose stools` -> `watery poop`**

- status: `attributed`
- log p full -0.2113, empty -4.3000
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+6.091` [readme] loose stools: Watery poop.
    - `+0.120` [readme] Stool: Stool is the waste material that comes out during a bowel movement.
    - `+0.050` [wiktionary] onset: The onset of something is the time when it begins (usually something bad).

- rationale: The readme glossary identifies loose stools as a digestive symptom, so replacing it with watery poop keeps that core idea intact while using plain language. Phrase frequency increases from Zipf 3.03 to 3.06, while age of acquisition falls from 7.71 to 6.65, making the replacement statistically easier to process. You can now grasp the exact nature of your digestive issue without needing to decode clinical terminology.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `new onset` -> `recent start`**

- status: `attributed`
- log p full -1.8998, empty -3.6162
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+0.668` [readme] loose stools: Watery poop.
    - `+0.559` [michigan] onset: The start.
    - `+0.272` [wiktionary] new: If somebody is new, they are not experienced.
    - `+0.162` [wiktionary] new: If something is new, it is not old.

- rationale: "New onset" refers to a condition that has just begun, and swapping it for "recent start" preserves that exact idea while using everyday language. Phrase frequency increases from Zipf 3.72 to 4.93, while age of acquisition falls from 10.72 to 8.13. You can now grasp the timing of your symptoms without needing to decode clinical jargon.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `predominantly` -> `mostly`**

- status: `attributed`
- log p full -0.3236, empty -0.3698
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+0.048` [readme] loose stools: Watery poop.
    - `+0.033` [dictionary] Irregularity (n.): The state or quality of being irregular; that which is irregular.
    - `+0.013` [justplainclear] stool: Also known as: bowel movement, BM, feces, poop The solid or semi-solid waste that passes out of your re
    - `+0.011` [readme] stool: The stuff that comes out when you go to the bathroom.

- rationale: "Predominantly" means that something happens or exists in the greatest amount, and swapping it for "mostly" keeps that exact idea while using everyday language. Word frequency increases from Zipf 3.80 to 4.83, and syllable count drops from 5 to 2, making the phrasing noticeably easier to process. Patients can now grasp the core clinical point without getting tangled in complex vocabulary.
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

**output:** The patient comes in for a follow-up visit because of a past case of erythema nodosum.

| metric | value |
|---|---:|
| bertscore_f1 | 0.261 |
| coleman_liau | 7.36 |
| coleman_liau_drop | 7.24 |
| copy_jargon_rate | 1.000 |
| critical_error | 0.000 |
| fkgl | 8.35 |
| fkgl_drop | 3.36 |
| fre | 63.7 |
| fre_gain | 31.2 |
| human_edit_recall | 0.000 |
| length_ratio | 1.00 |
| n_words | 17.0 |
| nli_completeness | 0.974 |
| nli_faithfulness | 0.980 |
| replacement_f1 | 0.000 |
| rewrite_aggressiveness | 1.000 |
| sari | 10.55 |
| smog | 11.21 |
| smog_drop | 3.35 |
| temporality_preservation | 1.000 |

### Stage 4 - arm `termonly`

**output:** Description : The patient comes in for a followup for a history of red skin bumps.

| metric | value |
|---|---:|
| bertscore_f1 | 0.653 |
| coleman_liau | 7.36 |
| coleman_liau_drop | 7.24 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 7.57 |
| fkgl_drop | 4.14 |
| fre | 67.5 |
| fre_gain | 35.0 |
| human_edit_recall | 1.000 |
| length_ratio | 0.88 |
| n_words | 15.0 |
| nli_completeness | 0.305 |
| nli_faithfulness | 0.565 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 38.10 |
| smog | 13.02 |
| smog_drop | 1.53 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `erythema nodosum` -> `red skin bumps` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Description : The patient presents for a followup for history of red skin.

| metric | value |
|---|---:|
| bertscore_f1 | 0.769 |
| coleman_liau | 10.73 |
| coleman_liau_drop | 3.87 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 8.76 |
| fkgl_drop | 2.95 |
| fre | 53.7 |
| fre_gain | 21.1 |
| human_edit_recall | 1.000 |
| length_ratio | 0.71 |
| n_words | 12.0 |
| nli_completeness | 0.121 |
| nli_faithfulness | 0.602 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 74.07 |
| smog | 13.02 |
| smog_drop | 1.53 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `erythema nodosum` -> `red skin` | replace | attributed | 3.814 | 4.331 | - | 0.905 | 2.640 | 2.1530387465 |

**edit `erythema nodosum` -> `red skin`**

- status: `attributed`
- log p full -0.8940, empty -4.7078
- masks scored: 10/10 (+2 top-k)
- ranked sources:
    - `+3.252` [readme] Erythema: Red skin.
    - `+0.612` [nih] erythema: Redness of the skin.
    - `-0.367` [readme] erythema: Skin redness.

- rationale: Erythema nodosum describes painful, inflamed bumps that appear on the skin, so "red skin" carries that same visual meaning in plain language. Phrase frequency increases from Zipf 1.39 to 4.77, and syllable count drops from 5 to 2, making the wording more common and easier to process. You can now recognize the visible signs of the condition without needing to memorize a complex medical label.
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

**output:** She did not have enough iron last year, and because she had many surgeries and did not eat well, she might not have enough iron again.

| metric | value |
|---|---:|
| bertscore_f1 | 0.640 |
| coleman_liau | 6.71 |
| coleman_liau_drop | 1.17 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.200 |
| fkgl | 10.43 |
| fkgl_drop | -2.96 |
| fre | 66.6 |
| fre_gain | 5.5 |
| human_edit_recall | 1.000 |
| length_ratio | 1.13 |
| n_words | 26.0 |
| nli_completeness | 0.792 |
| nli_faithfulness | 0.173 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.833 |
| sari | 15.64 |
| smog | 8.84 |
| smog_drop | 2.37 |
| uncertainty_preservation | 1.000 |

### Stage 4 - arm `termonly`

**output:** She was low on iron last year, and with her multiple surgeries and poor intake by mouth, may have become low on iron again.

| metric | value |
|---|---:|
| bertscore_f1 | 0.849 |
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
| nli_completeness | 0.827 |
| nli_faithfulness | 0.076 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 37.42 |
| smog | 11.21 |
| smog_drop | 0.00 |
| uncertainty_preservation | 1.000 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `iron deficient` -> `low on iron` | replace | - | - | - | - | - | - | - |
| `p. o.` -> `by mouth` | replace | - | - | - | - | - | - | - |
| `iron deficient` -> `low on iron` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** She was lacking iron last year, and with her multiple surgeries and poor intake by mouth, may have become lacking iron again.

| metric | value |
|---|---:|
| bertscore_f1 | 0.857 |
| coleman_liau | 9.48 |
| coleman_liau_drop | -1.61 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.200 |
| fkgl | 10.69 |
| fkgl_drop | -3.22 |
| fre | 57.6 |
| fre_gain | -3.5 |
| human_edit_recall | 1.000 |
| length_ratio | 0.96 |
| n_words | 22.0 |
| nli_completeness | 0.824 |
| nli_faithfulness | 0.056 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 37.42 |
| smog | 11.21 |
| smog_drop | 0.00 |
| uncertainty_preservation | 1.000 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `iron deficient` -> `lacking iron` | replace | attributed | 0.368 | 0.401 | 0.820 | 0.946 | 0.969 | 0.6543765700000002 |
| `p. o.` -> `by mouth` | replace | attributed | -1.096 | -1.097 | 0.788 | 0.801 | 0.127 | 0.18541034999999972 |
| `iron deficient` -> `lacking iron` | replace | attributed | -0.005 | -0.027 | 0.865 | 0.950 | 0.251 | 0.02118740699999999 |

**edit `iron deficient` -> `lacking iron`**

- status: `attributed`
- log p full -2.3261, empty -2.6945
- masks scored: 66/66 (+5 top-k)
- ranked sources:
    - `+1.054` [thesaurus] deficient: lacking, not enough, poor
    - `+0.085` [wiktionary] p: post, meaning after

- rationale: "Iron deficient" simply means your body does not have enough iron, and switching to "lacking iron" keeps that exact idea while using everyday words. Phrase frequency increases from Zipf 3.31 to 3.99 (higher values mean more common and easier), while age of acquisition decreases from 11.61 to 7.32 (lower values mean learned younger and easier). You can now grasp the core nutritional issue without needing to decode clinical jargon.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `p. o.` -> `by mouth`**

- status: `attributed`
- log p full -7.6613, empty -6.5652
- masks scored: 66/66 (+5 top-k)
- ranked sources:
    - `+0.333` [nih] iron: An important mineral the body needs to make hemoglobin, a substance in the blood that carries oxygen fro
    - `+0.206` [thesaurus] deficient: lacking, not enough, poor
    - `+0.070` [wiktionary] iron: A metal from the element.
    - `+0.016` [michigan] deficient: To not have enough.

- rationale: "p. o." is a clinical abbreviation for taking a medication orally, so changing it to "by mouth" keeps the same instruction while using familiar everyday words. Phrase frequency shifts from Zipf 4.82 to 4.82, while the syllable count remains at two. You can now confidently follow the dosing directions without needing to decode medical shorthand.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `iron deficient` -> `lacking iron`**

- status: `attributed`
- log p full -0.2256, empty -0.2202
- masks scored: 66/66 (+5 top-k)
- ranked sources:
    - `+0.251` [thesaurus] deficient: lacking, not enough, poor

- rationale: "Iron deficient" simply means your body does not have enough iron, and switching to "lacking iron" keeps that exact idea while using everyday words. Phrase frequency increases from Zipf 3.31 to 3.99, making it more common and easier to encounter, while age of acquisition falls from 11.61 to 7.32, meaning it is learned younger and more easily. You can now grasp the core nutritional issue without needing to decode clinical jargon.
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

**output:** We will set up an appointment for him to wear a Holter monitor and send him back to see his heart doctor.

| metric | value |
|---|---:|
| bertscore_f1 | 0.707 |
| coleman_liau | 4.74 |
| coleman_liau_drop | 3.78 |
| copy_jargon_rate | 1.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 8.01 |
| fkgl_drop | 1.13 |
| fre | 76.8 |
| fre_gain | 20.6 |
| human_edit_recall | 0.000 |
| length_ratio | 1.38 |
| n_words | 22.0 |
| nli_completeness | 0.970 |
| nli_faithfulness | 0.985 |
| replacement_f1 | 0.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.667 |
| sari | 18.58 |
| smog | 11.21 |
| smog_drop | 0.00 |

### Stage 4 - arm `termonly`

**output:** We will schedule him for the heart recorder and refer him back to his heart doctor.

| metric | value |
|---|---:|
| bertscore_f1 | 0.826 |
| coleman_liau | 6.64 |
| coleman_liau_drop | 1.88 |
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
| nli_completeness | 0.730 |
| nli_faithfulness | 0.899 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 50.65 |
| smog | 8.84 |
| smog_drop | 2.37 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `Holter monitor` -> `heart recorder` | replace | - | - | - | - | - | - | - |
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
| `Holter monitor` -> `portable machine for recording heart beats` | replace | attributed | 23.691 | 23.895 | - | 0.924 | 24.948 | 25.235772552 |
| `cardiologist` -> `heart doctor` | replace | attributed | 0.425 | 1.412 | - | 0.928 | 2.048 | 0.9293968510000001 |

**edit `Holter monitor` -> `portable machine for recording heart beats`**

- status: `attributed`
- log p full -1.6909, empty -25.3823
- masks scored: 34/34 (+4 top-k)
- ranked sources:
    - `+24.948` [iowa] HOLTER MONITOR: a portable machine for recording heart beats
    - `-0.022` [michigan] cardiologist: A doctor who treats heart and blood vessel problems.
    - `-0.042` [wiktionary] cardiologist: A cardiologist is a doctor who specializes in medical problems related to the heart.
    - `-0.600` [justplainclear] cardiologist: Heart doctor

- rationale: A Holter monitor is a small device that tracks heart activity over time, so "portable machine for recording heart beats" simply describes its practical function in everyday language. Phrase frequency increases from Zipf 2.12 to 3.67, while age of acquisition falls from 9.68 to 7.95. You can now grasp exactly what the device does without needing to memorize a specialized medical label.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `cardiologist` -> `heart doctor`**

- status: `attributed`
- log p full -0.1871, empty -0.6124
- masks scored: 34/34 (+4 top-k)
- ranked sources:
    - `+2.158` [justplainclear] cardiologist: Heart doctor
    - `+0.110` [wiktionary] cardiologist: A cardiologist is a doctor who specializes in medical problems related to the heart.
    - `-0.277` [nih] cardiologist: A doctor who has special training to diagnose and treat diseases of the heart and blood vessels.
    - `-0.344` [michigan] cardiologist: A doctor who treats heart and blood vessel problems.
    - `-0.538` [iowa] HOLTER MONITOR: a portable machine for recording heart beats

- rationale: The original term refers to a medical specialist who diagnoses and treats heart conditions, and "heart doctor" keeps that core idea in everyday language. Word frequency rises from Zipf 2.90 to 4.76, and age of acquisition drops from 13.42 to 5.17. Patients can now grasp who is treating them without needing to know the specialized title.
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

**output:** The patient wished to go forward with surgery.

| metric | value |
|---|---:|
| bertscore_f1 | 0.827 |
| coleman_liau | 8.05 |
| coleman_liau_drop | 8.70 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 5.23 |
| fkgl_drop | 5.90 |
| fre | 71.8 |
| fre_gain | 42.3 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 8.0 |
| nli_completeness | 0.981 |
| nli_faithfulness | 0.993 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 41.60 |
| smog | 8.84 |
| smog_drop | 2.37 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `proceed` -> `go forward` | replace | attributed | 4.004 | 4.674 | 0.681 | 0.798 | 0.297 | 0.20736431100000008 |
| `operative intervention` -> `surgery` | replace | attributed | -0.142 | -0.527 | 0.547 | 0.780 | 0.783 | 0.10327471299999996 |

**edit `proceed` -> `go forward`**

- status: `attributed`
- log p full -0.7075, empty -4.7120
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+1.767` [wiktionary] proceed: When you proceed, you go forward with something.
    - `+1.470` [michigan] proceed: To go or move forward.
    - `+0.591` [thesaurus] proceed: go, move forward
    - `+0.433` [wiktionary] operative: If something is operative, it is able to work.
    - `+0.262` [wiktionary] proceed: (formal) The proceeds of some individual project or sale are the money earned from doing it.

- rationale: Wiktionary notes that when you proceed, you go forward with something, so swapping the single word for that exact phrase keeps the core instruction clear in everyday language. Phrase frequency increases from Zipf 4.18 to 5.07, while age of acquisition falls from 8.33 to 4.24. Patients can now grasp the intended direction of care without needing to decode clinical jargon.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `operative intervention` -> `surgery`**

- status: `attributed`
- log p full -0.3889, empty -0.2473
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+1.836` [readme] Operative: Operative means related to surgery.
    - `+1.053` [readme] intervention: An intervention is a step taken to help treat or prevent a health problem.
    - `+0.893` [readme] operative: Dealing with surgeries.
    - `+0.750` [wiktionary] proceed: When you proceed, you go forward with something.
    - `+0.640` [wiktionary] operative: If something is operative, it is able to work.

- rationale: "Operative intervention" describes a planned medical procedure that involves cutting into the body to treat a condition, and "surgery" preserves that core idea using straightforward everyday language. Phrase frequency increases from Zipf 3.71 to 4.63, meaning it is more common and easier to process, while age of acquisition decreases from 13.11 to 7.68, indicating it is learned younger and easier to grasp. You can now understand the essential treatment approach without needing to decode specialized clinical terminology.
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

**output:** An abdominal X-ray was taken and showed unusual gas in the intestines.

| metric | value |
|---|---:|
| bertscore_f1 | 0.563 |
| coleman_liau | 9.28 |
| coleman_liau_drop | -0.78 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 9.74 |
| fkgl_drop | -2.55 |
| fre | 46.6 |
| fre_gain | -14.7 |
| human_edit_recall | 1.000 |
| length_ratio | 0.76 |
| n_words | 13.0 |
| nli_completeness | 0.854 |
| nli_faithfulness | 0.877 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.167 |
| sari | 17.74 |
| smog | 13.02 |
| smog_drop | -4.18 |

### Stage 4 - arm `termonly`

**output:** A stomach X-ray was taken showing unusual gas spots.

| metric | value |
|---|---:|
| bertscore_f1 | 0.557 |
| coleman_liau | 7.98 |
| coleman_liau_drop | 0.52 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.333 |
| fkgl | 7.59 |
| fkgl_drop | -0.40 |
| fre | 56.7 |
| fre_gain | -4.6 |
| human_edit_recall | 1.000 |
| length_ratio | 0.59 |
| n_words | 10.0 |
| nli_completeness | 0.663 |
| nli_faithfulness | 0.686 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 15.18 |
| smog | 8.84 |
| smog_drop | 0.00 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `obtained` -> `taken` | replace | - | - | - | - | - | - | - |
| `abnormal bowel gas pattern` -> `unusual gas spots` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** A kidney and bladder x-ray was done showing an unusual gas pattern in the intestines.

| metric | value |
|---|---:|
| bertscore_f1 | 0.692 |
| coleman_liau | 8.91 |
| coleman_liau_drop | -0.41 |
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
| nli_completeness | 0.933 |
| nli_faithfulness | 0.483 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 25.66 |
| smog | 11.21 |
| smog_drop | -2.37 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `obtained` -> `done` | replace | attributed | 0.228 | 0.308 | 0.804 | 0.820 | 0.094 | 0.25972466000000005 |
| `abnormal bowel gas pattern` -> `unusual gas pattern in the intestines` | replace | attributed | 0.776 | 0.827 | 0.702 | 0.917 | 0.077 | 0.4255376058000002 |

**edit `obtained` -> `done`**

- status: `attributed`
- log p full -1.2393, empty -1.4673
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.161` [wiktionary] obtained: If you obtain something, you get it.
    - `+0.067` [nih] abnormal: Not normal. Describes a state, condition, or behavior that is unusual or different from what is cons
    - `+0.060` [justplainclear] abnormal: Not normal, different from usual
    - `+0.054` [wiktionary] gas: Gas is a substance such as methane, ethane, propane, or butane that is burned for heat or to make electri
    - `+0.000` [wiktionary] gas: A gas is a substance, such as air, that is not liquid or solid.

- rationale: "Obtained" simply means to get or acquire something, and swapping it for "done" keeps that straightforward idea of completing a procedure in everyday language. Word frequency increases from Zipf 4.49 to 5.58, while the syllable count drops from 2 to 1. You can now clearly understand what procedure was actually performed without needing to decode formal medical terminology.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `abnormal bowel gas pattern` -> `unusual gas pattern in the intestines`**

- status: `attributed`
- log p full -2.4372, empty -3.2134
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.787` [readme] bowel: The intestines in your belly that break down food.
    - `+0.710` [readme] Bowel: Your intestines in the belly that break down food.
    - `+0.525` [nih] abnormal: Not normal. Describes a state, condition, or behavior that is unusual or different from what is cons
    - `+0.326` [wiktionary] abnormal: When something is abnormal, it often means that it is bigger than [[normal].
    - `+0.294` [michigan] abnormal: Something that is not usual, like a growth or low or high amounts of blood cells.

- rationale: "Abnormal bowel gas pattern" refers to an unexpected or atypical arrangement of gas in the digestive tract, so "unusual gas pattern in the intestines" preserves that core idea by swapping clinical jargon for everyday language. Phrase frequency increases from Zipf 3.29 to 3.17, while age of acquisition falls from 10.05 to 8.56, meaning the revised wording is both more common and learned earlier. You can now grasp exactly what your doctor is describing about your digestive symptoms without needing to decode specialized medical terminology.
- audit: coverage 1.0, grounding_error=True, omission=False, source_ok=True, passage_ok=True

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

**output:** She was given a sedative called Ativan and went to the emergency room feeling very confused and unable to tell the doctors what happened before.

| metric | value |
|---|---:|
| bertscore_f1 | 0.582 |
| coleman_liau | 10.62 |
| coleman_liau_drop | -1.42 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 13.04 |
| fkgl_drop | -0.73 |
| fre | 46.1 |
| fre_gain | 5.5 |
| human_edit_recall | 1.000 |
| length_ratio | 1.25 |
| n_words | 25.0 |
| nli_completeness | 0.989 |
| nli_faithfulness | 0.739 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.750 |
| sari | 18.51 |
| severity_downgrade | 0.000 |
| severity_tier_input | 3.000 |
| severity_tier_output | 3.000 |
| smog | 13.02 |
| smog_drop | 2.88 |

### Stage 4 - arm `termonly`

**output:** She has been put to sleep with a sleeping medicine and came into the emergency room confused and unable to give any history.

| metric | value |
|---|---:|
| bertscore_f1 | 0.756 |
| coleman_liau | 8.38 |
| coleman_liau_drop | 0.82 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 11.85 |
| fkgl_drop | 0.47 |
| fre | 51.1 |
| fre_gain | 10.5 |
| human_edit_recall | 1.000 |
| length_ratio | 1.15 |
| n_words | 23.0 |
| nli_completeness | 0.031 |
| nli_faithfulness | 0.987 |
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
| `sedated` -> `put to sleep` | replace | - | - | - | - | - | - | - |
| `Ativan` -> `a sleeping medicine` | replace | - | - | - | - | - | - | - |
| `obtunded` -> `confused` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** She has been made sleepy with a calming medicine and came into the emergency room not fully alert and unable to give any history.

| metric | value |
|---|---:|
| bertscore_f1 | 0.731 |
| coleman_liau | 8.34 |
| coleman_liau_drop | 0.86 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.667 |
| fkgl | 12.95 |
| fkgl_drop | -0.63 |
| fre | 45.0 |
| fre_gain | 4.4 |
| human_edit_recall | 1.000 |
| length_ratio | 1.20 |
| n_words | 24.0 |
| nli_completeness | 0.026 |
| nli_faithfulness | 0.988 |
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
| `sedated` -> `made sleepy` | replace | attributed | 2.098 | 2.187 | - | 0.844 | 0.609 | 0.3975741850000003 |
| `Ativan` -> `a calming medicine` | replace | attributed | 0.303 | 0.313 | - | 0.544 | 0.120 | -0.030937540000000485 |
| `obtunded` -> `not fully alert` | replace | attributed | 10.708 | 11.937 | - | 0.923 | 11.416 | 10.128384317 |

**edit `sedated` -> `made sleepy`**

- status: `attributed`
- log p full -2.3444, empty -4.4419
- masks scored: 18/18 (+5 top-k)
- ranked sources:
    - `+1.658` [readme] SEDATED: Feeling calm, relaxed, or sleepy because of certain medications.
    - `+1.050` [readme] Sedated: When you're sedated, you feel calm, relaxed, or sleepy because of specific medication.
    - `-0.184` [wiktionary] sedated: A sedate person is calm and dignified.
    - `-0.201` [readme] obtunded: Being not fully alert.

- rationale: "Sedated" describes a state where a person is chemically relaxed and less responsive, and "made sleepy" preserves that core idea by using everyday language to describe the same reduced alertness. Phrase frequency increases from Zipf 2.78 to 3.68, meaning the new wording is more common and therefore easier to process. You can now grasp the intended effect of the medication without needing to decode clinical jargon.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `Ativan` -> `a calming medicine`**

- status: `attributed`
- log p full -3.3363, empty -3.6395
- masks scored: 18/18 (+5 top-k)
- ranked sources:
    - `+0.159` [readme] Sedated: When you're sedated, you feel calm, relaxed, or sleepy because of specific medication.
    - `+0.040` [wiktionary] sedated: A sedate person is calm and dignified.
    - `-0.055` [readme] obtunded: Being not fully alert.

- rationale: Ativan is a prescription drug designed to ease nervousness and promote relaxation, so "a calming medicine" preserves that core purpose while stripping away clinical jargon. Phrase frequency increases from Zipf 2.31 to 3.33, meaning the higher score reflects a more common and easier-to-process term. You can now grasp exactly what the treatment aims to do without needing to memorize a specialized drug name.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `obtunded` -> `not fully alert`**

- status: `attributed`
- log p full -0.3462, empty -11.0542
- masks scored: 18/18 (+5 top-k)
- ranked sources:
    - `+11.585` [readme] obtunded: Being not fully alert.
    - `+0.169` [readme] Sedated: When you're sedated, you feel calm, relaxed, or sleepy because of specific medication.
    - `+0.079` [readme] SEDATED: Feeling calm, relaxed, or sleepy because of certain medications.

- rationale: The original term describes a clouded or confused mental state, often caused by illness or fatigue, so "not fully alert" preserves that core idea using everyday language. Word frequency increases from Zipf 1.01 to 4.22, making the replacement significantly more common and easier to process. You can now grasp the exact level of mental confusion without needing to decode a clinical label.
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

**output:** He does not have any swelling now, but he did have a little swelling in his legs in the past.

| metric | value |
|---|---:|
| bertscore_f1 | 0.776 |
| coleman_liau | 3.60 |
| coleman_liau_drop | -1.27 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 6.37 |
| fkgl_drop | -1.95 |
| fre | 85.0 |
| fre_gain | -5.1 |
| human_edit_recall | 1.000 |
| length_ratio | 1.33 |
| n_words | 20.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.633 |
| nli_faithfulness | 0.994 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.750 |
| sari | 20.62 |
| severity_downgrade | 0.000 |
| severity_preservation | 0.000 |
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
| `edema` -> `swelling` | replace | attributed | 0.118 | 0.680 | - | 0.777 | 0.085 | 0.01924558400000001 |

**edit `edema` -> `swelling`**

- status: `attributed`
- log p full -0.1371, empty -0.2548
- masks scored: 34/34 (+2 top-k)
- ranked sources:
    - `+0.327` [readme] Edema: Swelling in the body caused by too much fluid.
    - `+0.242` [michigan] edema: Swelling caused by too much fluid in your body.
    - `+0.222` [nih] edema: Swelling caused by excess fluid in body tissues.
    - `+0.029` [readme] edema: Swelling due to too much fluid in the body tissues.
    - `-0.042` [iowa] EDEMA: excess fluid collecting in tissue

- rationale: Edema refers to an abnormal accumulation of fluid in the body's tissues, and swapping it for "swelling" preserves that core idea while using everyday language. Phrase frequency increases from Zipf 2.95 to 3.68, so the higher score indicates a more common and easier-to-process term. Patients can now grasp the physical symptom without needing to memorize a clinical label.
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

**output:** The patient has a mild overactivity of the parathyroid glands that is caused by another health issue rather than a problem with the glands themselves.

| metric | value |
|---|---:|
| bertscore_f1 | 0.273 |
| coleman_liau | 12.02 |
| coleman_liau_drop | 24.18 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.333 |
| fkgl | 11.62 |
| fkgl_drop | 9.36 |
| fre | 56.3 |
| fre_gain | 106.3 |
| human_edit_recall | 1.000 |
| length_ratio | 5.00 |
| n_words | 25.0 |
| nli_completeness | 0.920 |
| nli_faithfulness | 0.730 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 22.95 |
| severity_downgrade | 0.000 |
| severity_preservation | 1.000 |
| severity_tier_input | 1.000 |
| severity_tier_output | 1.000 |
| smog | 11.21 |
| smog_drop | 0.00 |

### Stage 4 - arm `termonly`

**output:** Mild high calcium from another condition.

| metric | value |
|---|---:|
| bertscore_f1 | 0.198 |
| coleman_liau | 13.10 |
| coleman_liau_drop | 23.10 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.333 |
| fkgl | 10.35 |
| fkgl_drop | 10.63 |
| fre | 31.5 |
| fre_gain | 81.5 |
| human_edit_recall | 1.000 |
| length_ratio | 1.20 |
| n_words | 6.0 |
| nli_completeness | 0.135 |
| nli_faithfulness | 0.103 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 22.22 |
| severity_downgrade | 0.000 |
| severity_preservation | 1.000 |
| severity_tier_input | 1.000 |
| severity_tier_output | 1.000 |
| smog | 13.02 |
| smog_drop | -1.82 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `secondary hyperparathyroidism` -> `high calcium from another condition` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Mild second condition where blood calcium rises.

| metric | value |
|---|---:|
| bertscore_f1 | 0.186 |
| coleman_liau | 13.94 |
| coleman_liau_drop | 22.26 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.667 |
| fkgl | 9.05 |
| fkgl_drop | 11.93 |
| fre | 42.6 |
| fre_gain | 92.6 |
| human_edit_recall | 1.000 |
| length_ratio | 1.40 |
| n_words | 7.0 |
| nli_completeness | 0.139 |
| nli_faithfulness | 0.297 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 22.22 |
| severity_downgrade | 0.000 |
| severity_preservation | 1.000 |
| severity_tier_input | 1.000 |
| severity_tier_output | 1.000 |
| smog | 11.21 |
| smog_drop | 0.00 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `secondary hyperparathyroidism` -> `second condition where blood calcium rises` | replace | attributed | 13.579 | 13.579 | - | 0.793 | 1.775 | -0.013554292999998552 |

**edit `secondary hyperparathyroidism` -> `second condition where blood calcium rises`**

- status: `attributed`
- log p full -15.3340, empty -28.9126
- masks scored: 18/18 (+2 top-k)
- ranked sources:
    - `+6.654` [justplainclear] hyperparathyroidism: A condition where your parathyroid glands work too hard and raise the calcium level in yo
    - `+4.879` [wiktionary] secondary: second, next in order to the first or primary.
    - `+4.155` [nih] hyperparathyroidism: A condition in which the parathyroid gland (one of four pea-sized organs found on the thy

- rationale: Secondary hyperparathyroidism refers to a follow-up calcium imbalance that develops after another medical issue, so "second condition where blood calcium rises" captures that exact sequence in everyday language. Phrase frequency increases from Zipf 1.88 to 3.58 (higher = more common = easier), while age of acquisition falls from 19.11 to 9.89 (lower = learned younger = easier). You can now grasp the core calcium problem without needing to memorize a complex medical label.
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

**output:** Otherwise, the patient's body systems were checked and found to be normal, except for the problems already mentioned.

| metric | value |
|---|---:|
| bertscore_f1 | 0.499 |
| coleman_liau | 13.49 |
| coleman_liau_drop | -1.05 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.667 |
| fkgl | 10.44 |
| fkgl_drop | 0.12 |
| fre | 52.3 |
| fre_gain | 4.4 |
| human_edit_recall | 1.000 |
| length_ratio | 1.19 |
| n_words | 19.0 |
| nli_completeness | 0.102 |
| nli_faithfulness | 0.040 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.400 |
| sari | 15.32 |
| smog | 11.21 |
| smog_drop | 0.00 |

### Stage 4 - arm `termonly`

**output:** Otherwise, a full body check was done and showed no problems except for what was mentioned above.

| metric | value |
|---|---:|
| bertscore_f1 | 0.551 |
| coleman_liau | 9.41 |
| coleman_liau_drop | 3.03 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.667 |
| fkgl | 7.70 |
| fkgl_drop | 2.86 |
| fre | 70.1 |
| fre_gain | 22.3 |
| human_edit_recall | 1.000 |
| length_ratio | 1.06 |
| n_words | 17.0 |
| nli_completeness | 0.963 |
| nli_faithfulness | 0.952 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.200 |
| sari | 16.30 |
| smog | 8.84 |
| smog_drop | 2.37 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `review of systems` -> `full body check` | replace | - | - | - | - | - | - | - |
| `obtained` -> `done` | replace | - | - | - | - | - | - | - |
| `negative` -> `no problems` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Otherwise, a complete body symptom check was asked and was nothing wrong except for as mentioned above.

| metric | value |
|---|---:|
| bertscore_f1 | 0.542 |
| coleman_liau | 11.46 |
| coleman_liau_drop | 0.98 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.667 |
| fkgl | 9.09 |
| fkgl_drop | 1.48 |
| fre | 60.2 |
| fre_gain | 12.4 |
| human_edit_recall | 1.000 |
| length_ratio | 1.06 |
| n_words | 17.0 |
| nli_completeness | 0.982 |
| nli_faithfulness | 0.766 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 29.64 |
| smog | 8.84 |
| smog_drop | 2.37 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `review of systems` -> `body symptom check` | replace | attributed | 4.984 | 4.984 | - | 0.947 | 5.794 | 5.643286090000001 |
| `obtained` -> `asked` | replace | attributed | 1.172 | 1.230 | - | 0.876 | 1.865 | 2.111877821 |
| `negative` -> `nothing wrong` | replace | attributed | -1.057 | -1.058 | - | 0.765 | 0.338 | 0.329543300000001 |

**edit `review of systems` -> `body symptom check`**

- status: `attributed`
- log p full -7.8449, empty -12.8286
- masks scored: 18/18 (+4 top-k)
- ranked sources:
    - `+5.630` [readme] Review of systems: Questions that ask patients about any symptoms they might be experiencing in different part
    - `-0.164` [wiktionary] negative: If something is negative, it is harmful, sad, or otherwise not good.
    - `-0.307` [wiktionary] negative: If a word, sentence, answer, etc. is negative, it uses a word like no, not, never, etc.
    - `-0.349` [wiktionary] obtained: If you obtain something, you get it.

- rationale: A review of systems is a standard medical practice where a clinician asks about every part of the body to catch any early signs of illness, and "body symptom check" keeps that same thorough, head-to-toe assessment in everyday language. Phrase frequency increases from 4.79 to 3.62, while age of acquisition falls from 8.84 to 8.68. You can now grasp exactly what your doctor is asking about without needing to decode clinical jargon.
- audit: coverage 1.0, grounding_error=True, omission=False, source_ok=True, passage_ok=True

**edit `obtained` -> `asked`**

- status: `attributed`
- log p full -2.5301, empty -3.7024
- masks scored: 18/18 (+4 top-k)
- ranked sources:
    - `+1.750` [readme] Review of systems: Questions that ask patients about any symptoms they might be experiencing in different part
    - `-0.115` [wiktionary] negative: If a word, sentence, answer, etc. is negative, it uses a word like no, not, never, etc.
    - `-0.139` [wiktionary] negative: If something is negative, it is harmful, sad, or otherwise not good.
    - `-0.360` [wiktionary] obtained: If you obtain something, you get it.

- rationale: The original term "obtained" refers to successfully acquiring or receiving something, so switching to "asked" preserves that core idea of seeking a response while using everyday language. Word frequency increases from Zipf 4.49 to 5.30, and the syllable count drops from 2 to 1. This clearer phrasing allows patients to quickly grasp the request for information without needing to decode formal clinical terminology.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `negative` -> `nothing wrong`**

- status: `attributed`
- log p full -7.9859, empty -6.9288
- masks scored: 18/18 (+4 top-k)
- ranked sources:
    - `+0.037` [wiktionary] negative: If a word, sentence, answer, etc. is negative, it uses a word like no, not, never, etc.
    - `-0.301` [wiktionary] obtained: If you obtain something, you get it.
    - `-0.417` [readme] Review of systems: Questions that ask patients about any symptoms they might be experiencing in different part
    - `-0.597` [wiktionary] negative: If something is negative, it is harmful, sad, or otherwise not good.

- rationale: In medical testing, "negative" simply means the condition or marker was not detected, so swapping it for "nothing wrong" preserves that clear, reassuring message in everyday language. Phrase frequency increases from Zipf 4.79 to 5.16, while age of acquisition falls from 7.47 to 5.21. With this adjustment, you can immediately grasp the test result without needing to decode clinical jargon.
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

**output:** The patient's symptoms get worse when they sit for any amount of time, such as when driving a car.

| metric | value |
|---|---:|
| bertscore_f1 | 0.689 |
| coleman_liau | 6.15 |
| coleman_liau_drop | 1.94 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 6.73 |
| fkgl_drop | 0.89 |
| fre | 80.7 |
| fre_gain | 11.7 |
| human_edit_recall | 1.000 |
| length_ratio | 1.33 |
| n_words | 20.0 |
| nli_completeness | 0.992 |
| nli_faithfulness | 0.992 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 28.35 |
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
| `motor vehicle` -> `car` | replace | attributed | 0.038 | 0.257 | - | - | - | 0.03844763500000001 |

**edit `motor vehicle` -> `car`**

- status: `attributed`
- log p full -0.1439, empty -0.1824
- masks scored: 4/4 (+1 top-k)
- ranked sources:
    - `+0.217` [wiktionary] motor vehicle: A motor vehicle a road vehicle powered by an internal combustion engine to provide power to rot

- rationale: A motor vehicle refers to any self-propelled road machine, so swapping it for "car" preserves that core idea while using everyday language. Phrase frequency rises from Zipf 4.33 to 5.45, and age of acquisition falls from 7.42 to 3.37, showing that the new term is more common and learned younger. You can now grasp the basic transportation concept without needing to decode clinical jargon.
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

**output:** The exams of the forearm, elbow, and shoulder show that the patient's nerves are working normally.

| metric | value |
|---|---:|
| bertscore_f1 | 0.561 |
| coleman_liau | 10.99 |
| coleman_liau_drop | 6.01 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.333 |
| fkgl | 8.35 |
| fkgl_drop | 4.48 |
| fre | 63.7 |
| fre_gain | 44.6 |
| human_edit_recall | 1.000 |
| length_ratio | 1.89 |
| n_words | 17.0 |
| negation_preservation | 0.000 |
| nli_completeness | 0.950 |
| nli_faithfulness | 0.723 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 34.76 |
| smog | 8.84 |
| smog_drop | 2.37 |

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
| `neurologic compromise` -> `nerve damage` | replace | attributed | -0.282 | -0.380 | 0.778 | 0.863 | 0.241 | 0.12912296899999998 |

**edit `neurologic compromise` -> `nerve damage`**

- status: `attributed`
- log p full -1.4946, empty -1.2129
- masks scored: 66/66 (+2 top-k)
- ranked sources:
    - `+0.573` [readme] NEUROLOGIC: Having to do with the nerves in the body, brain, or spinal cord.
    - `+0.332` [readme] Neurologic: Having to do with nerves in the body, brain, or spinal cord.
    - `+0.155` [nih] neurologic: Having to do with nerves or the nervous system.
    - `+0.141` [wiktionary] compromise: Compromise is the act making this type of agreement.

- rationale: "Neurologic compromise" describes any injury or disruption to the nervous system, and "nerve damage" carries that same idea by plainly stating that the body’s signaling pathways have been harmed. Phrase frequency increases from Zipf 2.55 to 4.11, while age of acquisition falls from 13.85 to 9.67, confirming that the replacement is both more common and learned younger. You can now clearly understand that your nervous system has been injured without getting lost in medical terminology.
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

**output:** After that, the numbing medicine was injected into the area around the tumor.

| metric | value |
|---|---:|
| bertscore_f1 | 0.836 |
| coleman_liau | 10.03 |
| coleman_liau_drop | 2.64 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 11.26 |
| fkgl_drop | 2.41 |
| fre | 37.5 |
| fre_gain | 19.1 |
| human_edit_recall | 1.000 |
| length_ratio | 1.08 |
| n_words | 13.0 |
| nli_completeness | 0.759 |
| nli_faithfulness | 0.987 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 65.67 |
| smog | 13.02 |
| smog_drop | 1.53 |

### Stage 4 - arm `termonly`

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
| `local anesthesia` -> `numbing medicine` | replace | - | - | - | - | - | - | - |
| `tumor` -> `lump` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** After that, a numbing medicine was injected into the area around the lump.

| metric | value |
|---|---:|
| bertscore_f1 | 0.748 |
| coleman_liau | 8.69 |
| coleman_liau_drop | 3.97 |
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
| nli_completeness | 0.361 |
| nli_faithfulness | 0.938 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 54.00 |
| smog | 13.02 |
| smog_drop | 1.53 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `Thereafter` -> `After that` | replace | attributed | -3.902 | -3.903 | 0.957 | 0.981 | 1.020 | 0.9800597199999999 |
| `local anesthesia` -> `numbing medicine` | replace | attributed | 0.551 | 0.620 | 0.853 | 0.802 | 0.482 | 0.2863663710000002 |
| `tumor` -> `lump` | replace | attributed | 0.717 | 0.927 | 0.777 | 0.822 | 1.041 | -0.034456083000000026 |

**edit `Thereafter` -> `After that`**

- status: `attributed`
- log p full -11.8808, empty -7.9785
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+1.307` [dictionary] Thereafter (adv.): After that; afterward.
    - `+0.287` [dictionary] Thereafter (adv.): According to that; accordingly.
    - `+0.141` [michigan] local anesthesia: A drug that causes only in the area of the body where the drug is put, as when a tooth is pu
    - `+0.092` [readme] local anesthesia: A drug that numbs a specific part of your body without affecting the rest.
    - `+0.025` [wiktionary] tumor: A tumor is an abnormal growth of tissue in a human or animal.

- rationale: "Thereafter" simply means at a later time, so swapping it for "after that" preserves that exact timeline in everyday language. Word frequency increases from Zipf 3.97 to 6.06, which means the replacement is more common and easier to process. You can now follow the sequence of your treatment steps without pausing to decode formal medical phrasing.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `local anesthesia` -> `numbing medicine`**

- status: `attributed`
- log p full -1.9342, empty -2.4848
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+0.647` [readme] local anesthesia: A drug that numbs a specific part of your body without affecting the rest.
    - `+0.166` [iowa] LOCAL ANESTHESIA: creation of insensitivity to pain in a small, local area of the body, usually by injection o
    - `+0.074` [wiktionary] tumor: A tumor is an abnormal growth of tissue in a human or animal.
    - `+0.032` [michigan] tumor: A growth or lump in your body. It may be cancer, but it also may not be cancer.

- rationale: Local anesthesia refers to a treatment that blocks pain signals in a specific body area, and calling it "numbing medicine" keeps that core idea clear by using everyday words instead of clinical jargon. Phrase frequency increases from Zipf 3.39 to 2.89 (higher values mean more common and easier), while age of acquisition falls from 12.53 to 4.89 (lower values mean learned younger and easier). You can now understand exactly what the procedure will do to your body without needing to decode specialized medical terminology first.
- audit: coverage 1.0, grounding_error=True, omission=False, source_ok=True, passage_ok=True

**edit `tumor` -> `lump`**

- status: `attributed`
- log p full -1.1574, empty -1.8740
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+1.768` [justplainclear] tumor: Growth or lump
    - `+0.727` [michigan] tumor: A growth or lump in your body. It may be cancer, but it also may not be cancer.
    - `+0.589` [thesaurus] tumor: growth, lump
    - `+0.295` [readme] local anesthesia: A drug that numbs a specific part of your body without affecting the rest.
    - `+0.036` [dictionary] Thereafter (adv.): After that; afterward.

- rationale: The justplainclear glossary defines a tumor as a growth or lump, so replacing the clinical label with the everyday word "lump" preserves that core idea in plain language. Word frequency increases from Zipf 3.97 to 3.71, and age of acquisition decreases from 10.32 to 5.89, indicating a clear shift toward more common and earlier-learned vocabulary. You can now grasp the basic nature of the abnormal tissue without first memorizing a specialized medical term.
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

**output:** The patient has no numbness or tingling in the hand or arm.

| metric | value |
|---|---:|
| bertscore_f1 | 0.731 |
| coleman_liau | 4.45 |
| coleman_liau_drop | 0.79 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 4.82 |
| fkgl_drop | -1.11 |
| fre | 81.9 |
| fre_gain | -6.1 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 12.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.969 |
| nli_faithfulness | 0.966 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 44.27 |
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

**output:** I do not think she has a clear pocket of pus right now, although some fluid is still coming out.

| metric | value |
|---|---:|
| bertscore_f1 | 0.666 |
| coleman_liau | 4.47 |
| coleman_liau_drop | 5.07 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.667 |
| fkgl | 6.37 |
| fkgl_drop | 1.24 |
| fre | 85.0 |
| fre_gain | 16.0 |
| human_edit_recall | 1.000 |
| length_ratio | 1.18 |
| n_words | 20.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.990 |
| nli_faithfulness | 0.980 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 36.42 |
| severity_preservation | 0.000 |
| smog | 3.13 |
| smog_drop | 5.71 |

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
| `abscessed lesion` -> `pus-filled sore` | replace | attributed | -2.885 | -2.913 | 0.535 | 0.789 | 0.132 | 0.44159997999999945 |
| `drainage` -> `fluid leaking out` | replace | attributed | 2.219 | 3.058 | 0.767 | 0.820 | 3.844 | 3.458094783 |

**edit `abscessed lesion` -> `pus-filled sore`**

- status: `attributed`
- log p full -6.4324, empty -3.5475
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.750` [readme] DRAINAGE: Fluid leaving an organ or body area.
    - `+0.618` [michigan] lesion: A sore or any part of your sking that looks different from the rest.
    - `+0.209` [readme] drainage: When any fluid is leaking out of a body part.
    - `+0.139` [nih] lesion: An area of abnormal tissue. A lesion may be benign (not cancer) or malignant (cancer).

- rationale: An abscessed lesion describes a damaged patch of tissue that has become infected and filled with pus, so "pus-filled sore" preserves that exact physical reality in plain language. Phrase frequency increases from Zipf 1.60 to 2.97, while age of acquisition drops from 12.82 to 5.84, meaning the replacement is more common and learned much younger. You can now clearly picture what is happening in your body without needing to decode clinical jargon.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `drainage` -> `fluid leaking out`**

- status: `attributed`
- log p full -0.5177, empty -2.7366
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+3.960` [readme] drainage: When any fluid is leaking out of a body part.
    - `+0.115` [michigan] lesion: A sore or any part of your sking that looks different from the rest.
    - `+0.094` [iowa] LESION: wound or injury; a diseased patch of skin
    - `+0.001` [wiktionary] drainage: To use a drainage is engage in the action or process of draining something.

- rationale: The readme explains that drainage refers to when any fluid is leaking out of a body part, so "fluid leaking out" preserves that exact idea in everyday language. Phrase frequency rises from Zipf 3.77 to 3.58, while age of acquisition drops from 10.84 to 7.94. You can now clearly picture what is happening in your body without first learning a specialized medical term.
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

**output:** At this time, the medical team would give IV fluids to restore hydration and check the patient's condition again.

| metric | value |
|---|---:|
| bertscore_f1 | 0.544 |
| coleman_liau | 10.73 |
| coleman_liau_drop | 1.36 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.667 |
| fkgl | 9.83 |
| fkgl_drop | -0.75 |
| fre | 58.4 |
| fre_gain | 8.9 |
| human_edit_recall | 1.000 |
| length_ratio | 1.54 |
| n_words | 20.0 |
| nli_completeness | 0.993 |
| nli_faithfulness | 0.407 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 26.90 |
| smog | 13.02 |
| smog_drop | 0.00 |

### Stage 4 - arm `termonly`

**output:** At this time, we would restore water with fluids through a vein and check again.

| metric | value |
|---|---:|
| bertscore_f1 | 0.752 |
| coleman_liau | 6.97 |
| coleman_liau_drop | 5.12 |
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
| nli_completeness | 0.981 |
| nli_faithfulness | 0.959 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 51.04 |
| smog | 3.13 |
| smog_drop | 9.89 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `rehydrate` -> `restore water` | replace | - | - | - | - | - | - | - |
| `intravenous fluids` -> `fluids through a vein` | replace | - | - | - | - | - | - | - |
| `reassess` -> `check again` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** At this time, we would restore fluids with fluids given through a vein and check again.

| metric | value |
|---|---:|
| bertscore_f1 | 0.709 |
| coleman_liau | 7.72 |
| coleman_liau_drop | 4.37 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 6.14 |
| fkgl_drop | 2.94 |
| fre | 79.6 |
| fre_gain | 30.0 |
| human_edit_recall | 1.000 |
| length_ratio | 1.23 |
| n_words | 16.0 |
| nli_completeness | 0.974 |
| nli_faithfulness | 0.961 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 48.75 |
| smog | 3.13 |
| smog_drop | 9.89 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `rehydrate` -> `restore fluids` | replace | attributed | -1.397 | -1.401 | - | 1.000 | 0.193 | -0.3742594859999997 |
| `intravenous fluids` -> `fluids given through a vein` | replace | attributed | 0.854 | 0.854 | - | 0.830 | 0.225 | 0.34238722999999993 |
| `reassess` -> `check again` | replace | attributed | -1.606 | -1.829 | - | 0.781 | 0.039 | -0.05966778000000028 |

**edit `rehydrate` -> `restore fluids`**

- status: `attributed`
- log p full -6.7479, empty -5.3509
- masks scored: 10/10 (+3 top-k)
- ranked sources:
    - `-0.218` [wiktionary] rehydrate: If you rehydrate something, you supply it with water to make it moist or wet again.
    - `-0.411` [wiktionary] reassess: If you reassess a person, idea, skill, process, etc., you judge or measure them again.
    - `-0.729` [readme] intravenous fluid: Fluids that go straight into a vein through a needle.

- rationale: "Rehydrate" simply means to replenish the water your body has lost, and "restore fluids" keeps that exact idea by using everyday words to describe the same physical process. Phrase frequency increases from Zipf 2.20 to 3.60, while age of acquisition falls from 13.63 to 10.78. You can now grasp the treatment goal without needing to decode a clinical instruction.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `intravenous fluids` -> `fluids given through a vein`**

- status: `attributed`
- log p full -8.4789, empty -9.3327
- masks scored: 10/10 (+3 top-k)
- ranked sources:
    - `+0.397` [readme] intravenous fluid: Fluids that go straight into a vein through a needle.
    - `+0.172` [wiktionary] rehydrate: If you rehydrate something, you supply it with water to make it moist or wet again.

- rationale: The original term refers to liquids administered directly into a vein, and the replacement keeps that core idea by saying the fluids are given through a vein. Phrase frequency increases from Zipf 3.03 to 3.44, while age of acquisition falls from 15.29 to 8.53. Patients can now grasp the basic delivery method without needing to know the medical label.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `reassess` -> `check again`**

- status: `attributed`
- log p full -3.0414, empty -1.4355
- masks scored: 10/10 (+3 top-k)
- ranked sources:
    - `-0.039` [wiktionary] rehydrate: If you rehydrate something, you supply it with water to make it moist or wet again.
    - `-1.649` [wiktionary] reassess: If you reassess a person, idea, skill, process, etc., you judge or measure them again.

- rationale: "Reassess" means to evaluate a condition a second time, and "check again" keeps that core idea by using simple, everyday words to describe looking at something once more. Phrase frequency increases from Zipf 2.80 to 5.16 (higher = more common = easier), while age of acquisition falls from 12.79 to 5.78 (lower = learned younger = easier). This clearer wording lets you instantly see that your care team will revisit your symptoms without needing to decode clinical jargon.
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

**output:** The test results match what doctors expect for acute appendicitis.

| metric | value |
|---|---:|
| bertscore_f1 | 0.406 |
| coleman_liau | 13.72 |
| coleman_liau_drop | 6.15 |
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
| nli_completeness | 0.988 |
| nli_faithfulness | 0.292 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 8.63 |
| smog | 8.84 |
| smog_drop | 2.37 |
| temporality_preservation | 1.000 |
| uncertainty_preservation | 0.000 |

### Stage 4 - arm `termonly`

**output:** The test results suggest an inflamed appendix.

| metric | value |
|---|---:|
| bertscore_f1 | 0.435 |
| coleman_liau | 12.29 |
| coleman_liau_drop | 7.58 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.143 |
| fkgl | 7.37 |
| fkgl_drop | 6.91 |
| fre | 54.7 |
| fre_gain | 51.4 |
| human_edit_recall | 1.000 |
| length_ratio | 0.78 |
| n_words | 7.0 |
| nli_completeness | 0.847 |
| nli_faithfulness | 0.924 |
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
| `acute appendicitis` -> `inflamed appendix` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** The results suggest a swollen appendix.

| metric | value |
|---|---:|
| bertscore_f1 | 0.481 |
| coleman_liau | 11.17 |
| coleman_liau_drop | 8.70 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.143 |
| fkgl | 8.38 |
| fkgl_drop | 5.90 |
| fre | 45.6 |
| fre_gain | 42.3 |
| human_edit_recall | 1.000 |
| length_ratio | 0.67 |
| n_words | 6.0 |
| nli_completeness | 0.848 |
| nli_faithfulness | 0.883 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 11.25 |
| smog | 8.84 |
| smog_drop | 2.37 |
| temporality_preservation | 0.000 |
| uncertainty_preservation | 0.000 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `acute appendicitis` -> `swollen appendix` | replace | attributed | -0.856 | -0.859 | 0.880 | 0.953 | 4.438 | 4.549462420000001 |

**edit `acute appendicitis` -> `swollen appendix`**

- status: `attributed`
- log p full -6.1206, empty -5.2648
- masks scored: 66/66 (+2 top-k)
- ranked sources:
    - `+4.843` [readme] appendicitis: Appendicitis is when your appendix gets swollen and inflamed, typically causing stomach pain.
    - `+0.405` [wiktionary] compatible: Things or people are compatible when they can work and communicate with each other without problem
    - `+0.264` [nih] acute: Symptoms or signs that begin and worsen quickly; not chronic.
    - `+0.224` [wiktionary] with: With is used to describe something added to something else.
    - `+0.051` [wiktionary] findings: A finding is the information from a research or an investigation.

- rationale: Acute appendicitis describes a sudden, painful inflammation of the small intestine tube attached to the colon, and replacing it with "swollen appendix" keeps that core medical reality by describing the same inflamed organ in plain language. Phrase frequency increases from Zipf 2.74 to 3.24 (higher = more common = easier), while age of acquisition decreases from 12.00 to 10.56 (lower = learned younger = easier). You can now clearly recognize what is happening in your abdomen without first decoding a specialized medical label.
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

**output:** She says she has not lost any weight, but she admits she has been eating less and feeling more tired all over for the past 3-4 months.

| metric | value |
|---|---:|
| bertscore_f1 | 0.616 |
| coleman_liau | 5.66 |
| coleman_liau_drop | 10.58 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.250 |
| fkgl | 9.36 |
| fkgl_drop | 1.11 |
| fre | 76.0 |
| fre_gain | 25.8 |
| human_edit_recall | 1.000 |
| length_ratio | 1.56 |
| n_words | 28.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.994 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.125 |
| sari | 43.06 |
| smog | 3.13 |
| smog_drop | 9.89 |
| temporality_preservation | 1.000 |

### Stage 4 - arm `termonly`

**output:** She says she did not have weight loss, but said she was eating less and felt more tired for the past 3-4 months.

| metric | value |
|---|---:|
| bertscore_f1 | 0.646 |
| coleman_liau | 4.85 |
| coleman_liau_drop | 11.38 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.250 |
| fkgl | 6.21 |
| fkgl_drop | 4.27 |
| fre | 91.5 |
| fre_gain | 41.3 |
| human_edit_recall | 1.000 |
| length_ratio | 1.33 |
| n_words | 24.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.995 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 47.57 |
| smog | 3.13 |
| smog_drop | 9.89 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `acknowledged` -> `said` | replace | - | - | - | - | - | - | - |
| `decreased appetite` -> `eating less` | replace | - | - | - | - | - | - | - |
| `generalized fatigue` -> `tired` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** She says she did not have weight loss, but admitted she wants less food and feels tired all over for the past 3-4 months.

| metric | value |
|---|---:|
| bertscore_f1 | 0.605 |
| coleman_liau | 5.93 |
| coleman_liau_drop | 10.31 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.375 |
| fkgl | 7.54 |
| fkgl_drop | 2.94 |
| fre | 83.8 |
| fre_gain | 33.5 |
| human_edit_recall | 1.000 |
| length_ratio | 1.39 |
| n_words | 25.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.994 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 46.38 |
| smog | 8.84 |
| smog_drop | 4.18 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 4 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `denies` -> `did not have` | replace | attributed | 1.098 | 1.115 | 0.723 | 0.703 | 0.026 | 0.18213878599999989 |
| `acknowledged` -> `admitted` | replace | attributed | 0.101 | 0.124 | 0.539 | 0.747 | 0.024 | 0.1679795959999999 |
| `decreased appetite` -> `less food` | replace | attributed | 3.385 | 3.395 | 0.725 | 0.877 | 1.663 | 1.3448333100000003 |
| `generalized fatigue` -> `tired all over` | replace | attributed | 0.700 | 0.898 | 0.770 | 0.959 | 1.132 | 0.8421511550000003 |

**edit `denies` -> `did not have`**

- status: `attributed`
- log p full -3.6828, empty -4.7810
- masks scored: 66/66 (+8 top-k)
- ranked sources:
    - `+0.106` [wiktionary] denies: If you deny something, you say it didn't happen or isn't true.
    - `+0.080` [readme] appetite: Wanting to eat food.
    - `+0.026` [justplainclear] fatigue: Tired, weak feeling of the whole body, feeling tired
    - `+0.018` [wiktionary] acknowledged: If you acknowledge a fact or a situation, you accept or admit that it is true or that it exists.

- rationale: The original term "denies" simply means a patient lacks or refuses to report a specific symptom, so changing it to "did not have" keeps that exact idea while speaking in everyday language. Word frequency increases from a Zipf score of 3.73 to 5.83, while the syllable count changes from 2 to 3. This clearer phrasing allows patients to immediately grasp their health status without getting tangled in clinical jargon.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `acknowledged` -> `admitted`**

- status: `attributed`
- log p full -1.6275, empty -1.7285
- masks scored: 66/66 (+8 top-k)
- ranked sources:
    - `+0.038` [wiktionary] acknowledged: If you acknowledge a fact or a situation, you accept or admit that it is true or that it exists.
    - `+0.015` [wiktionary] appetite: When you have appetite, you feel hungry and would like to eat some food.
    - `+0.010` [wiktionary] generalized: When you generalize you speak in general, or in vague terms.
    - `+0.002` [readme] fatigue: Feeling exhausted and lacking energy.

- rationale: When a clinician notes that a symptom was acknowledged, they simply mean you recognized it as real, and switching to admitted preserves that exact idea of openly recognizing a fact in everyday speech. Word frequency increases from Zipf 4.08 to 4.49, which means the new term is more common and therefore easier to process. You can now focus on the actual health message without pausing to decode formal medical wording.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `decreased appetite` -> `less food`**

- status: `attributed`
- log p full -4.5832, empty -7.9681
- masks scored: 66/66 (+8 top-k)
- ranked sources:
    - `+2.953` [readme] appetite: Wanting to eat food.
    - `+1.291` [nih] appetite: A desire to satisfy a physical or mental need, such as for food, sex, or adventure.
    - `+0.924` [readme] fatigue: Feeling exhausted and lacking energy.
    - `+0.522` [nih] fatigue: A condition marked by extreme tiredness and inability to function due to lack of energy. Fatigue may 
    - `+0.134` [wiktionary] acknowledged: If you acknowledge a fact or a situation, you accept or admit that it is true or that it exists.

- rationale: The readme glossary defines "decreased appetite" as simply wanting to eat food, so swapping it for "less food" preserves that core idea in everyday language. Phrase frequency increases from Zipf 3.63 to 5.14 (higher = more common = easier), while age of acquisition falls from 8.83 to 3.25 (lower = learned younger = easier). You can now grasp the basic nutritional change without needing to decode clinical terminology.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `generalized fatigue` -> `tired all over`**

- status: `attributed`
- log p full -1.1951, empty -1.8951
- masks scored: 66/66 (+8 top-k)
- ranked sources:
    - `+1.537` [michigan] fatigue: tired, weak feeling of the whole body, feeling tired all over
    - `+0.405` [readme] fatigue: Feeling exhausted and lacking energy.
    - `+0.383` [readme] Generalized: Generalized means not focusing on one specific area.
    - `+0.199` [wiktionary] appetite: When you have appetite, you feel hungry and would like to eat some food.
    - `+0.033` [wiktionary] acknowledged: If you acknowledge a fact or a situation, you accept or admit that it is true or that it exists.

- rationale: The Michigan glossary defines generalized fatigue as a weak, whole-body tiredness, so "tired all over" preserves that core idea in everyday language. Phrase frequency increases from Zipf 3.29 to 4.69, while age of acquisition drops from 11.83 to 5.57, showing that the new phrasing is both more common and learned younger. You can now grasp the physical sensation of your condition without needing to decode clinical jargon.
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

**output:** The doctors are thinking about removing the rest of the patient's thyroid gland.

| metric | value |
|---|---:|
| bertscore_f1 | 0.393 |
| coleman_liau | 11.37 |
| coleman_liau_drop | 16.79 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.286 |
| fkgl | 7.63 |
| fkgl_drop | 14.13 |
| fre | 63.5 |
| fre_gain | 115.5 |
| human_edit_recall | 1.000 |
| length_ratio | 1.56 |
| n_words | 14.0 |
| nli_completeness | 0.935 |
| nli_faithfulness | 0.340 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 25.04 |
| smog | 8.84 |
| smog_drop | 4.18 |
| uncertainty_preservation | 0.000 |

### Stage 4 - arm `termonly`

**output:** The doctors are thinking about finishing thyroid surgery.

| metric | value |
|---|---:|
| bertscore_f1 | 0.268 |
| coleman_liau | 16.02 |
| coleman_liau_drop | 12.14 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.286 |
| fkgl | 11.13 |
| fkgl_drop | 10.63 |
| fre | 29.5 |
| fre_gain | 81.5 |
| human_edit_recall | 1.000 |
| length_ratio | 0.89 |
| n_words | 8.0 |
| nli_completeness | 0.975 |
| nli_faithfulness | 0.598 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 23.77 |
| smog | 11.21 |
| smog_drop | 1.82 |
| uncertainty_preservation | 0.000 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `Consideration given to` -> `finishing` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** The doctors are thinking about surgery to remove the rest of the thyroid.

| metric | value |
|---|---:|
| bertscore_f1 | 0.404 |
| coleman_liau | 8.69 |
| coleman_liau_drop | 19.47 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.333 |
| fkgl | 7.63 |
| fkgl_drop | 14.13 |
| fre | 63.5 |
| fre_gain | 115.5 |
| human_edit_recall | 1.000 |
| length_ratio | 1.44 |
| n_words | 13.0 |
| nli_completeness | 0.953 |
| nli_faithfulness | 0.143 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 34.31 |
| smog | 8.84 |
| smog_drop | 4.18 |
| uncertainty_preservation | 0.000 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `Consideration given to` -> `thinking about` | replace | attributed | -0.104 | -0.131 | 0.711 | 0.826 | 0.173 | 0.11677144999999989 |

**edit `Consideration given to` -> `thinking about`**

- status: `attributed`
- log p full -1.6264, empty -1.5223
- masks scored: 66/66 (+2 top-k)
- ranked sources:
    - `+0.223` [wiktionary] consideration: Consideration is the process of thinking carefully about something.
    - `+0.051` [wiktionary] to: To shows where something goes, the goal of movement.

- rationale: "Consideration given to" simply means paying attention to or weighing something carefully, and switching to "thinking about" preserves that exact idea while using everyday language. Phrase frequency increases from Zipf 4.25 to 5.21, while age of acquisition falls from 9.50 to 5.07, meaning the higher frequency makes it more common and the lower age of acquisition means it is learned younger. Patients can now grasp the core idea of careful evaluation without getting tangled in formal medical phrasing.
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

**output:** She mentions that she had a nosebleed a few days ago that needed packing in her nose, and luckily it has stopped now.

| metric | value |
|---|---:|
| bertscore_f1 | 0.750 |
| coleman_liau | 6.37 |
| coleman_liau_drop | 4.06 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.400 |
| fkgl | 8.77 |
| fkgl_drop | 1.68 |
| fre | 73.1 |
| fre_gain | 19.2 |
| human_edit_recall | 1.000 |
| length_ratio | 1.10 |
| n_words | 23.0 |
| nli_completeness | 0.946 |
| nli_faithfulness | 0.977 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 33.64 |
| smog | 8.84 |
| smog_drop | 2.37 |
| temporality_preservation | 1.000 |

### Stage 4 - arm `termonly`

**output:** She notes that she had a nosebleed a few days ago, needing packing in the nose and fortunately that stopped now.

| metric | value |
|---|---:|
| bertscore_f1 | 0.802 |
| coleman_liau | 7.65 |
| coleman_liau_drop | 2.77 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.400 |
| fkgl | 8.33 |
| fkgl_drop | 2.12 |
| fre | 72.7 |
| fre_gain | 18.8 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 21.0 |
| nli_completeness | 0.906 |
| nli_faithfulness | 0.965 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 46.80 |
| smog | 8.84 |
| smog_drop | 2.37 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 4 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `epistaxis` -> `a nosebleed` | replace | - | - | - | - | - | - | - |
| `requiring` -> `needing` | replace | - | - | - | - | - | - | - |
| `nasal packing` -> `packing in the nose` | replace | - | - | - | - | - | - | - |
| `resolved` -> `stopped` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** She notes that she had a nosebleed a few days ago, needing packing in her nose and fortunately that had gone now.

| metric | value |
|---|---:|
| bertscore_f1 | 0.829 |
| coleman_liau | 6.58 |
| coleman_liau_drop | 3.84 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.400 |
| fkgl | 8.54 |
| fkgl_drop | 1.91 |
| fre | 73.0 |
| fre_gain | 19.0 |
| human_edit_recall | 1.000 |
| length_ratio | 1.05 |
| n_words | 22.0 |
| nli_completeness | 0.882 |
| nli_faithfulness | 0.957 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 50.21 |
| smog | 8.84 |
| smog_drop | 2.37 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 4 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `epistaxis` -> `a nosebleed` | replace | attributed | 0.313 | 1.019 | 0.627 | 0.567 | 0.033 | 0.0005159399999999925 |
| `requiring` -> `needing` | replace | attributed | 0.191 | 0.374 | 0.792 | 0.832 | 0.404 | 0.416097096 |
| `nasal packing` -> `packing in her nose` | replace | attributed | 1.707 | 1.753 | 0.853 | 0.885 | 0.394 | 0.3425241099999998 |
| `resolved` -> `gone` | replace | attributed | 0.287 | 0.330 | 0.246 | 0.794 | 0.001 | -0.08020344000000001 |

**edit `epistaxis` -> `a nosebleed`**

- status: `attributed`
- log p full -0.2330, empty -0.5464
- masks scored: 66/66 (+8 top-k)
- ranked sources:
    - `+0.706` [readme] EPISTAXIS: EPISTAXIS: It's a nosebleed.
    - `+0.674` [readme] Epistaxis: A nosebleed.
    - `+0.190` [wiktionary] resolved: When a problem is resolved, it has been brought to a successful solution.
    - `+0.089` [wiktionary] epistaxis: Epistaxis is bleeding from the nose.
    - `+0.024` [wiktionary] requiring: If you require something, you need it.

- rationale: Epistaxis refers to bleeding from the nose, so swapping it for "a nosebleed" preserves that exact physical description while using everyday language. Phrase frequency increases from Zipf 1.60 to 2.51, while syllable count shifts from 2 to 3, making the new phrasing more familiar to most people. You can now grasp the exact symptom without needing to memorize a clinical label.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `requiring` -> `needing`**

- status: `attributed`
- log p full -0.6222, empty -0.8129
- masks scored: 66/66 (+8 top-k)
- ranked sources:
    - `+0.438` [wiktionary] requiring: If you require something, you need it.
    - `+0.033` [justplainclear] nasal: Relating to your nose
    - `+0.021` [readme] packing: Putting something into a wound to help it heal.
    - `+0.015` [readme] Nasal: Nasal means having to do with the nose.

- rationale: The original word describes a situation where something is necessary or demanded, and swapping it for "needing" preserves that exact idea while using everyday language. Word frequency increases from Zipf 4.14 to 4.02, and the syllable count drops from 4 to 2. You can now grasp the essential requirement without getting tangled in clinical jargon.
- audit: coverage 1.0, grounding_error=True, omission=False, source_ok=True, passage_ok=True

**edit `nasal packing` -> `packing in her nose`**

- status: `attributed`
- log p full -2.9035, empty -4.6102
- masks scored: 66/66 (+8 top-k)
- ranked sources:
    - `+0.791` [readme] packing: Putting something into a wound to help it heal.
    - `+0.397` [wiktionary] packing: You put packing around an object to protect it.
    - `+0.162` [wiktionary] requiring: If you require something, you need it.

- rationale: The readme explains that nasal packing involves putting something into a wound to help it heal, so "packing in her nose" preserves that core idea by describing the action in everyday language. Phrase frequency increases from Zipf 3.39 to 3.93, while age of acquisition falls from 8.75 to 5.09, making the new phrasing statistically easier to grasp. You can now picture exactly what the doctor is doing to help your nose heal without needing to decode clinical jargon.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `resolved` -> `gone`**

- status: `attributed`
- log p full -1.9154, empty -2.2027
- masks scored: 66/66 (+8 top-k)
- ranked sources:
    - `+0.065` [readme] nasal: It's all about your nose when we talk about "nasal."
    - `+0.064` [wiktionary] resolved: When a problem is resolved, it has been brought to a successful solution.
    - `+0.031` [wiktionary] resolved: To resolve means to create a solution for a problem.

- rationale: The original term "resolved" means that a condition or symptom has completely disappeared, and "gone" carries that same idea in everyday language. Phrase frequency increases from Zipf 4.10 to 5.17, while syllables decrease from 2 to 1. Patients can now grasp the improvement without needing to know the clinical word.
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

**output:** The doctor also explained to the patient about conscious sedation.

| metric | value |
|---|---:|
| bertscore_f1 | 0.847 |
| coleman_liau | 13.72 |
| coleman_liau_drop | -1.88 |
| copy_jargon_rate | 1.000 |
| critical_error | 0.000 |
| fkgl | 9.55 |
| fkgl_drop | -0.65 |
| fre | 44.4 |
| fre_gain | -2.9 |
| human_edit_recall | 0.000 |
| length_ratio | 1.11 |
| n_words | 10.0 |
| nli_completeness | 0.910 |
| nli_faithfulness | 0.394 |
| replacement_f1 | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 25.32 |
| smog | 8.84 |
| smog_drop | 0.00 |

### Stage 4 - arm `termonly`

**output:** I also explained to the patient about calming medicine.

| metric | value |
|---|---:|
| bertscore_f1 | 0.828 |
| coleman_liau | 10.56 |
| coleman_liau_drop | 1.29 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 8.90 |
| fkgl_drop | 0.00 |
| fre | 47.3 |
| fre_gain | 0.0 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 9.0 |
| nli_completeness | 0.527 |
| nli_faithfulness | 0.916 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 61.94 |
| smog | 8.84 |
| smog_drop | 0.00 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `conscious sedation` -> `calming medicine` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** I also explained to the patient about light sedation where they wake when touched.

| metric | value |
|---|---:|
| bertscore_f1 | 0.717 |
| coleman_liau | 10.26 |
| coleman_liau_drop | 1.59 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 6.73 |
| fkgl_drop | 2.17 |
| fre | 71.8 |
| fre_gain | 24.5 |
| human_edit_recall | 1.000 |
| length_ratio | 1.56 |
| n_words | 14.0 |
| nli_completeness | 0.033 |
| nli_faithfulness | 0.004 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 66.67 |
| smog | 8.84 |
| smog_drop | 0.00 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `conscious sedation` -> `light sedation where they wake when touched` | replace | attributed | 16.041 | 16.041 | - | 1.000 | 11.312 | 12.262534558999995 |

**edit `conscious sedation` -> `light sedation where they wake when touched`**

- status: `attributed`
- log p full -14.2542, empty -30.2948
- masks scored: 6/6 (+1 top-k)
- ranked sources:
    - `+13.526` [nih] conscious sedation: A level of sedation in which a person is asleep but wakes when spoken to or touched. Consc
    - `+2.214` [readme] conscious sedation: Medication given to a patient to make them lightly sedated and forgetful during a procedur

- rationale: Conscious sedation refers to a state where a patient feels relaxed and drowsy but remains aware of their surroundings, and the replacement phrase captures this by describing a gentle drug effect that allows the person to stay responsive enough to wake up if someone touches them. Phrase frequency increases from Zipf 2.93 to 2.92, making it slightly more common and easier to process, while age of acquisition remains at 13.20, meaning it is learned just as young as before. You can now picture exactly how the medication will feel and when you will regain full awareness without needing to memorize a clinical label.
- audit: coverage 1.0, grounding_error=True, omission=False, source_ok=True, passage_ok=True

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

**output:** Touching her right knee shows no grinding or clicking sound.

| metric | value |
|---|---:|
| bertscore_f1 | 0.611 |
| coleman_liau | 10.24 |
| coleman_liau_drop | -0.74 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 3.65 |
| fkgl_drop | 1.58 |
| fre | 86.7 |
| fre_gain | 14.9 |
| human_edit_recall | 1.000 |
| laterality_preservation | 1.000 |
| length_ratio | 1.11 |
| n_words | 10.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.903 |
| nli_faithfulness | 0.773 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 28.93 |
| smog | 3.13 |
| smog_drop | 5.71 |

### Stage 4 - arm `termonly`

**output:** Touching her right knee reveals no cracking sounds.

| metric | value |
|---|---:|
| bertscore_f1 | 0.677 |
| coleman_liau | 11.68 |
| coleman_liau_drop | -2.18 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 3.76 |
| fkgl_drop | 1.48 |
| fre | 82.4 |
| fre_gain | 10.6 |
| human_edit_recall | 1.000 |
| laterality_preservation | 1.000 |
| length_ratio | 0.89 |
| n_words | 8.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.943 |
| nli_faithfulness | 0.966 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 51.01 |
| smog | 3.13 |
| smog_drop | 5.71 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `crepitus` -> `cracking sounds` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Feeling her right knee reveals no popping sound.

| metric | value |
|---|---:|
| bertscore_f1 | 0.748 |
| coleman_liau | 9.50 |
| coleman_liau_drop | 0.00 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 3.76 |
| fkgl_drop | 1.48 |
| fre | 82.4 |
| fre_gain | 10.6 |
| human_edit_recall | 1.000 |
| laterality_preservation | 1.000 |
| length_ratio | 0.89 |
| n_words | 8.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.927 |
| nli_faithfulness | 0.977 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 54.35 |
| smog | 3.13 |
| smog_drop | 5.71 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `crepitus` -> `popping sound` | replace | attributed | 0.532 | 0.548 | - | 0.918 | 0.648 | 0.508842628 |

**edit `crepitus` -> `popping sound`**

- status: `attributed`
- log p full -3.3126, empty -3.8448
- masks scored: 34/34 (+2 top-k)
- ranked sources:
    - `+0.722` [dictionary] Crepitus (n.): The noise produced by a sudden discharge of wind from the bowels.
    - `+0.074` [dictionary] Crepitus (n.): Same as Crepitation, 2.
    - `-0.012` [readme] Palpation: Feeling a part of the body.
    - `-0.062` [readme] palpation: Feeling a part of the body with your hands.
    - `-0.122` [nih] palpation: Examination by pressing on the surface of the body to feel the organs or tissues underneath.

- rationale: Crepitus refers to the crackling or snapping noise that occurs when joints or tendons move, so "popping sound" captures that exact physical sensation in everyday language. Phrase frequency increases from Zipf 1.39 to 3.81, making it more common and easier to process, while the syllable count rises from 2 to 3. You can now recognize the joint movement warning sign without needing to memorize a specialized medical label.
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

**output:** She was distracted by her thoughts, worries, and expectations the evening before, so she twisted her ankle.

| metric | value |
|---|---:|
| bertscore_f1 | 0.443 |
| coleman_liau | 12.14 |
| coleman_liau_drop | 0.19 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 9.78 |
| fkgl_drop | 0.32 |
| fre | 55.2 |
| fre_gain | 7.6 |
| length_ratio | 1.55 |
| n_words | 17.0 |
| nli_completeness | 0.926 |
| nli_faithfulness | 0.933 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.250 |
| sari | 27.34 |
| smog | 11.21 |
| smog_drop | 0.00 |
| temporality_preservation | 1.000 |

### Stage 4 - arm `termonly`

**output:** She stepped on ideas, concerns and expectations the evening before and twisted her ankle.

| metric | value |
|---|---:|
| bertscore_f1 | 0.609 |
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

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `prior` -> `before` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** She stepped on ideas, concerns and expectations the evening before and twisted her ankle.

| metric | value |
|---|---:|
| bertscore_f1 | 0.609 |
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

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `prior` -> `before` | replace | attributed | -0.054 | -0.099 | - | 1.000 | 1.319 | 0.84554734 |

**edit `prior` -> `before`**

- status: `attributed`
- log p full -0.8010, empty -0.7475
- masks scored: 10/10 (+2 top-k)
- ranked sources:
    - `+0.914` [wiktionary] prior: If something happens prior to something else, it happens before it.
    - `-0.406` [wiktionary] evening: Period from dusk to midnight.
    - `-0.606` [wiktionary] evening: You use even to focus on the most surprising or unlikely case.

- rationale: "Prior" simply means something that happened earlier in time, and swapping it for "before" preserves that exact timeline in everyday language. Word frequency increases from Zipf 4.85 to 5.93, while age of acquisition drops from 10.63 to 5.45. You can now easily track the sequence of your medical events without getting tangled in formal terminology.
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

**output:** What affects it : The patient's condition is made worse by throwing.

| metric | value |
|---|---:|
| bertscore_f1 | 0.581 |
| coleman_liau | 9.98 |
| coleman_liau_drop | 6.37 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.250 |
| fkgl | 5.86 |
| fkgl_drop | 8.28 |
| fre | 72.6 |
| fre_gain | 62.9 |
| human_edit_recall | 1.000 |
| length_ratio | 1.20 |
| n_words | 12.0 |
| nli_completeness | 0.936 |
| nli_faithfulness | 0.983 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 60.75 |
| smog | 8.84 |
| smog_drop | 4.18 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `Modifying Factors` -> `affects it` | replace | - | - | - | - | - | - | - |
| `aggravated` -> `made worse` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Things that change it : The patient's condition is made worse by throwing.

| metric | value |
|---|---:|
| bertscore_f1 | 0.561 |
| coleman_liau | 10.25 |
| coleman_liau_drop | 6.11 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.750 |
| fkgl | 4.82 |
| fkgl_drop | 9.32 |
| fre | 81.9 |
| fre_gain | 72.2 |
| human_edit_recall | 1.000 |
| length_ratio | 1.30 |
| n_words | 13.0 |
| nli_completeness | 0.983 |
| nli_faithfulness | 0.989 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 58.98 |
| smog | 8.84 |
| smog_drop | 4.18 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `aggravated` -> `made worse` | replace | attributed | 0.396 | 0.489 | - | 0.793 | 0.052 | 0.270698632 |

**edit `aggravated` -> `made worse`**

- status: `attributed`
- log p full -1.4667, empty -1.8623
- masks scored: 18/18 (+2 top-k)
- ranked sources:
    - `+0.164` [readme] aggravated: To make a problem or injury worse.
    - `+0.112` [wiktionary] aggravated: To aggravate is to make something worse.
    - `+0.065` [wiktionary] factors: A factor is one of a number of things that causes a result.

- rationale: The original term describes a condition that has become more severe, and "made worse" keeps that core idea in plain language. Phrase frequency increases from Zipf 3.47 to 4.85, while syllables drop from 4 to 2. Patients can now grasp the worsening state without needing to know the formal word.
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

**output:** The patient has a history of joint wear and tear, weak bones, an underactive thyroid, allergic nose, and kidney stones.

| metric | value |
|---|---:|
| bertscore_f1 | 0.447 |
| coleman_liau | 10.27 |
| coleman_liau_drop | 17.37 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 9.91 |
| fkgl_drop | 11.44 |
| fre | 59.6 |
| fre_gain | 99.8 |
| human_edit_recall | 1.000 |
| length_ratio | 1.54 |
| n_words | 20.0 |
| nli_completeness | 0.957 |
| nli_faithfulness | 0.973 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 61.91 |
| smog | 13.02 |
| smog_drop | 2.88 |
| temporality_preservation | 1.000 |

### Stage 4 - arm `termonly`

**output:** History of stiff joints, weak bones, slow thyroid, nose allergies and stones in the kidneys.

| metric | value |
|---|---:|
| bertscore_f1 | 0.544 |
| coleman_liau | 10.84 |
| coleman_liau_drop | 16.80 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 6.78 |
| fkgl_drop | 14.57 |
| fre | 73.2 |
| fre_gain | 113.4 |
| human_edit_recall | 1.000 |
| length_ratio | 1.15 |
| n_words | 15.0 |
| nli_completeness | 0.917 |
| nli_faithfulness | 0.953 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 41.27 |
| smog | 11.21 |
| smog_drop | 4.70 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 5 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `osteoarthritis` -> `stiff joints` | replace | - | - | - | - | - | - | - |
| `osteoporosis` -> `weak bones` | replace | - | - | - | - | - | - | - |
| `hypothyroidism` -> `slow thyroid` | replace | - | - | - | - | - | - | - |
| `allergic rhinitis` -> `nose allergies` | replace | - | - | - | - | - | - | - |
| `kidney stones` -> `stones in the kidneys` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** History of worn-out joints, weak bones, an underactive thyroid, hay fever, and stones in the kidneys.

| metric | value |
|---|---:|
| bertscore_f1 | 0.670 |
| coleman_liau | 11.35 |
| coleman_liau_drop | 16.29 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 8.35 |
| fkgl_drop | 13.00 |
| fre | 63.7 |
| fre_gain | 103.9 |
| human_edit_recall | 1.000 |
| length_ratio | 1.31 |
| n_words | 17.0 |
| nli_completeness | 0.876 |
| nli_faithfulness | 0.964 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 49.73 |
| smog | 11.21 |
| smog_drop | 4.70 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 5 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `osteoarthritis` -> `worn-out joints` | replace | attributed | 1.092 | 1.101 | 0.801 | 0.856 | 0.125 | 0.6499863769999994 |
| `osteoporosis` -> `weak bones` | replace | attributed | 0.884 | 1.563 | 0.592 | 0.672 | 0.101 | -0.011191078999999993 |
| `hypothyroidism` -> `an underactive thyroid` | replace | attributed | 1.252 | 1.320 | 0.773 | 0.947 | 0.478 | 0.7933676400999996 |
| `allergic rhinitis` -> `hay fever` | replace | attributed | 3.682 | 4.010 | 0.764 | 0.839 | 1.415 | 0.8365865052000001 |
| `kidney stones` -> `stones in the kidneys` | replace | attributed | -2.378 | -2.419 | 0.745 | 0.913 | 0.109 | 0.2685251279999994 |

**edit `osteoarthritis` -> `worn-out joints`**

- status: `attributed`
- log p full -4.2795, empty -5.3716
- masks scored: 66/66 (+10 top-k)
- ranked sources:
    - `+0.956` [justplainclear] osteoarthritis: A form of arthritis caused by the wear and tear of joints
    - `+0.832` [readme] osteoarthritis: Osteoarthritis is a painful joint condition caused by the wearing down of bone tissue, leading
    - `+0.309` [nih] osteoporosis: A condition in which there is a decrease in the amount and thickness of bone tissue. This causes
    - `+0.133` [wiktionary] osteoporosis: Osteoporosis is a disease in which the bones become very porous and brittle.
    - `+0.132` [readme] osteoarthritis: Arthritis that happens when the cushioning between joints wears out.

- rationale: The justplainclear glossary describes osteoarthritis as a form of arthritis caused by the wear and tear of joints, so "worn-out joints" carries that exact meaning in plain words. Phrase frequency increases from Zipf 2.76 to 3.68, confirming that the higher score means the phrase is more common and easier to read. This change allows patients to understand the physical breakdown of their joints without first decoding a medical term.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `osteoporosis` -> `weak bones`**

- status: `attributed`
- log p full -0.4730, empty -1.3573
- masks scored: 66/66 (+10 top-k)
- ranked sources:
    - `+0.361` [readme] Osteoporosis: Osteoporosis is a condition where bones become weak and more prone to fractures.
    - `+0.259` [readme] osteoarthritis: Osteoarthritis is a painful joint condition caused by the wearing down of bone tissue, leading
    - `+0.235` [readme] osteoporosis: Osteoporosis is when bones become weak and prone to breaking because they lose density.
    - `+0.097` [nih] osteoporosis: A condition in which there is a decrease in the amount and thickness of bone tissue. This causes
    - `+0.093` [justplainclear] allergic rhinitis: Also known as: hay fever A condition where you have an allergic reaction that affects the n

- rationale: The source describes osteoporosis as a condition where bones become weak and more prone to fractures, so "weak bones" keeps that core idea in plain language. Phrase frequency increases from Zipf 2.99 to 4.16, while age of acquisition falls from 14.29 to 5.58. Patients can grasp the bone-fragility problem without first learning the medical name.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `hypothyroidism` -> `an underactive thyroid`**

- status: `attributed`
- log p full -2.4239, empty -3.6764
- masks scored: 66/66 (+10 top-k)
- ranked sources:
    - `+0.596` [nih] hypothyroidism: Too little thyroid hormone. Symptoms include weight gain, constipation, dry skin, and sensitiv
    - `+0.117` [justplainclear] allergic rhinitis: Also known as: hay fever A condition where you have an allergic reaction that affects the n
    - `+0.112` [justplainclear] hypothyroidism: A condition where your thyroid isn't active enough, so you have low hormone levels Hypothyroid
    - `+0.072` [justplainclear] osteoarthritis: A form of arthritis caused by the wear and tear of joints
    - `+0.042` [readme] osteoporosis: Osteoporosis is when bones become weak and prone to breaking because they lose density.

- rationale: The NIH glossary defines hypothyroidism as a condition with too little thyroid hormone, so "an underactive thyroid" preserves that core idea in everyday language. Phrase frequency increases from Zipf 2.68 to 1.67, while age of acquisition falls from 15.43 to 13.83. This shift allows patients to grasp the core hormonal imbalance without needing to memorize a complex medical label.
- audit: coverage 1.0, grounding_error=True, omission=False, source_ok=True, passage_ok=True

**edit `allergic rhinitis` -> `hay fever`**

- status: `attributed`
- log p full -1.2552, empty -4.9371
- masks scored: 66/66 (+10 top-k)
- ranked sources:
    - `+2.728` [justplainclear] allergic rhinitis: Also known as: hay fever A condition where you have an allergic reaction that affects the n
    - `+1.313` [michigan] allergic rhinitis: Caused by your body's reaction in your nose to mold, pollen, or dust. Also called hay fever
    - `+0.597` [iowa] OSTEOPOROSIS: softening of the bones
    - `+0.354` [readme] Osteoporosis: Osteoporosis is a condition where bones become weak and more prone to fractures.
    - `+0.340` [wiktionary] osteoporosis: Osteoporosis is a disease in which the bones become very porous and brittle.

- rationale: The justplainclear glossary describes allergic rhinitis as a condition where you have an allergic reaction that affects the nose, so "hay fever" keeps that exact meaning in plain language. Phrase frequency increases from Zipf 2.37 to 3.74 (HIGHER = more common = easier), while age of acquisition drops from 18.07 to 5.84 (LOWER = learned younger = easier). You can now easily recognize your symptoms without needing to decode a clinical label.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `kidney stones` -> `stones in the kidneys`**

- status: `attributed`
- log p full -5.4847, empty -3.1068
- masks scored: 66/66 (+10 top-k)
- ranked sources:
    - `+0.179` [michigan] kidney stones: A solid piece of material that forms in the kidney from material in the urine. They can be tiny
    - `+0.070` [nih] hypothyroidism: Too little thyroid hormone. Symptoms include weight gain, constipation, dry skin, and sensitiv
    - `-0.003` [justplainclear] hypothyroidism: A condition where your thyroid isn't active enough, so you have low hormone levels Hypothyroid

- rationale: "Kidney stones" refers to hard mineral deposits that form inside the urinary organs, and changing it to "stones in the kidneys" simply unpacks that same idea into everyday language by placing the location after the object. Phrase frequency increases from Zipf 3.85 to 3.43, so the higher value means the wording is more common and easier, while age of acquisition drops from 9.33 to 3.98, so the lower value means the words are learned younger and easier. You can now picture exactly where the hard deposits form without needing to memorize a specialized medical label.
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

**output:** The ultrasound showed no bleeding in the brain.

| metric | value |
|---|---:|
| bertscore_f1 | 0.862 |
| coleman_liau | 8.78 |
| coleman_liau_drop | 11.80 |
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
| nli_completeness | 0.893 |
| nli_faithfulness | 0.970 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 38.70 |
| smog | 8.84 |
| smog_drop | 5.71 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `intracranial hemorrhage` -> `bleeding in the brain` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** The ultrasound was negative for bleeding inside the brain.

| metric | value |
|---|---:|
| bertscore_f1 | 0.948 |
| coleman_liau | 12.49 |
| coleman_liau_drop | 8.08 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| diagnostic_identity_preservation | 1.000 |
| fkgl | 7.59 |
| fkgl_drop | 8.21 |
| fre | 56.7 |
| fre_gain | 62.4 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 9.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.826 |
| nli_faithfulness | 0.979 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 80.56 |
| smog | 11.21 |
| smog_drop | 3.35 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `intracranial hemorrhage` -> `bleeding inside the brain` | replace | attributed | 2.904 | 3.584 | - | 0.800 | 2.943 | 2.128526644 |

**edit `intracranial hemorrhage` -> `bleeding inside the brain`**

- status: `attributed`
- log p full -0.6784, empty -3.5822
- masks scored: 6/6 (+1 top-k)
- ranked sources:
    - `+3.160` [readme] INTRACRANIAL HEMORRHAGE: Bleeding inside your brain.
    - `+0.217` [readme] intracranial hemorrhage: Bleeding within the brain.

- rationale: "Intracranial hemorrhage" describes blood leaking from damaged vessels within the skull, so "bleeding inside the brain" keeps that exact physical reality while translating it into everyday language. Phrase frequency increases from Zipf 2.55 to 4.00, while age of acquisition falls from 14.94 to 5.76, making the new phrasing more common and easier to learn. You can now clearly picture the injury without first memorizing a complex clinical label.
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

**output:** He had a keyhole surgery to remove his appendix, and he can eat and drink without any problems.

| metric | value |
|---|---:|
| bertscore_f1 | 0.550 |
| coleman_liau | 7.04 |
| coleman_liau_drop | 6.11 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.111 |
| fkgl | 9.13 |
| fkgl_drop | 5.53 |
| fre | 61.7 |
| fre_gain | 50.3 |
| human_edit_recall | 1.000 |
| length_ratio | 1.20 |
| n_words | 18.0 |
| nli_completeness | 0.927 |
| nli_faithfulness | 0.598 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 31.93 |
| smog | 11.21 |
| smog_drop | 1.82 |
| temporality_preservation | 0.000 |

### Stage 4 - arm `termonly`

**output:** He is after keyhole appendix surgery, and he can eat food normally.

| metric | value |
|---|---:|
| bertscore_f1 | 0.644 |
| coleman_liau | 7.83 |
| coleman_liau_drop | 5.32 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.222 |
| fkgl | 8.76 |
| fkgl_drop | 5.90 |
| fre | 53.7 |
| fre_gain | 42.3 |
| human_edit_recall | 1.000 |
| length_ratio | 0.80 |
| n_words | 12.0 |
| nli_completeness | 0.920 |
| nli_faithfulness | 0.647 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 32.99 |
| smog | 13.02 |
| smog_drop | 0.00 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `status post` -> `after` | replace | - | - | - | - | - | - | - |
| `laparoscopic appendicectomy` -> `keyhole appendix surgery` | replace | - | - | - | - | - | - | - |
| `tolerating oral diet` -> `eat food normally` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** He is after appendix removal with a small camera, and he is eating and drinking by mouth.

| metric | value |
|---|---:|
| bertscore_f1 | 0.469 |
| coleman_liau | 6.68 |
| coleman_liau_drop | 6.47 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.222 |
| fkgl | 9.09 |
| fkgl_drop | 5.57 |
| fre | 60.2 |
| fre_gain | 48.8 |
| human_edit_recall | 1.000 |
| length_ratio | 1.13 |
| n_words | 17.0 |
| nli_completeness | 0.899 |
| nli_faithfulness | 0.825 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 33.61 |
| smog | 13.02 |
| smog_drop | 0.00 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `status post` -> `after` | replace | attributed | 0.987 | 1.011 | 0.551 | 0.731 | 0.104 | -0.11969420000000008 |
| `laparoscopic appendicectomy` -> `appendix removal with a small camera` | replace | attributed | 5.925 | 5.925 | 0.541 | 0.870 | 0.290 | 2.402344150000001 |
| `tolerating oral diet` -> `eating and drinking by mouth` | replace | attributed | 0.454 | 0.456 | 0.951 | 0.975 | 2.159 | 2.7388039599999994 |

**edit `status post` -> `after`**

- status: `attributed`
- log p full -3.2795, empty -4.2660
- masks scored: 66/66 (+5 top-k)
- ranked sources:
    - `+0.146` [readme] laparoscopic: A surgery where a small tube with a camera is used to see inside the body.
    - `+0.042` [wiktionary] post: Post is the letters and parcels that you send to other people.
    - `+0.012` [michigan] status: The state or condition that you or something else is in.
    - `+0.001` [readme] Status: Status means the condition or state of something.

- rationale: "Status post" is a clinical shorthand for a patient's condition following a specific procedure or event, so swapping it for "after" preserves that timeline reference in everyday language. Phrase frequency increases from Zipf 4.76 to 6.11, while age of acquisition falls from 11.63 to 6.00, meaning the new wording is more common and learned younger. You can now easily track your recovery timeline without needing to decode specialized medical jargon.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `laparoscopic appendicectomy` -> `appendix removal with a small camera`**

- status: `attributed`
- log p full -16.8352, empty -22.7605
- masks scored: 66/66 (+5 top-k)
- ranked sources:
    - `+2.708` [readme] laparoscopic: A surgery where a small tube with a camera is used to see inside the body.
    - `+2.418` [readme] Laparoscopic: A surgery that uses a small tube and camera to see inside your body.
    - `+1.757` [wiktionary] post: Post is the letters and parcels that you send to other people.
    - `+0.659` [wiktionary] tolerating: If you tolerate something, you put up with it, or allow it.
    - `+0.407` [nih] diet: The things a person eats and drinks.

- rationale: The readme explains that the original term refers to a surgery where a small tube with a camera is used to see inside the body, so "appendix removal with a small camera" carries that exact meaning in plain words. Phrase frequency rises from Zipf 0.00 to 3.43, meaning the higher score makes the wording more common and easier to process. You can now understand the basic surgical procedure without first learning the specialized medical name.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `tolerating oral diet` -> `eating and drinking by mouth`**

- status: `attributed`
- log p full -5.2335, empty -5.6874
- masks scored: 66/66 (+5 top-k)
- ranked sources:
    - `+2.542` [nih] diet: The things a person eats and drinks.
    - `+0.383` [readme] Oral: Oral means something you take by mouth.
    - `+0.117` [readme] status: The current condition of something.

- rationale: "Tolerating an oral diet" simply means a patient can safely swallow food and liquids without choking or vomiting, so replacing it with "eating and drinking by mouth" keeps that exact safety idea in plain language. Phrase frequency increases from Zipf 2.73 to 4.31, meaning the higher value indicates a more common and easier term, while age of acquisition drops from 9.39 to 5.41, meaning the lower value indicates it is learned younger and easier. You can now grasp the nutritional instruction immediately without needing to decode clinical jargon.
- audit: coverage 1.0, grounding_error=True, omission=False, source_ok=True, passage_ok=False

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

**output:** The doctors think that her walking is probably not being affected by the hydrocephalus.

| metric | value |
|---|---:|
| bertscore_f1 | 0.726 |
| coleman_liau | 12.33 |
| coleman_liau_drop | -1.66 |
| copy_jargon_rate | 1.000 |
| critical_error | 0.000 |
| fkgl | 9.26 |
| fkgl_drop | -0.84 |
| fre | 53.6 |
| fre_gain | -6.0 |
| human_edit_recall | 0.000 |
| length_ratio | 0.78 |
| n_words | 14.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.991 |
| nli_faithfulness | 0.241 |
| replacement_f1 | 0.000 |
| rewrite_aggressiveness | 1.000 |
| sari | 20.83 |
| smog | 13.02 |
| smog_drop | -1.82 |
| uncertainty_preservation | 1.000 |

### Stage 4 - arm `termonly`

**output:** We believe that her walking is most likely not being affected by the fluid buildup in the brain.

| metric | value |
|---|---:|
| bertscore_f1 | 0.958 |
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
| nli_completeness | 0.432 |
| nli_faithfulness | 0.707 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 77.92 |
| smog | 8.84 |
| smog_drop | 2.37 |
| uncertainty_preservation | 1.000 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `hydrocephalus` -> `fluid buildup in the brain` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** We believe that her walking is most likely not being affected by excess fluid in the brain.

| metric | value |
|---|---:|
| bertscore_f1 | 0.972 |
| coleman_liau | 7.71 |
| coleman_liau_drop | 2.97 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 8.39 |
| fkgl_drop | 0.02 |
| fre | 65.2 |
| fre_gain | 5.5 |
| human_edit_recall | 1.000 |
| length_ratio | 0.94 |
| n_words | 17.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.310 |
| nli_faithfulness | 0.835 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 76.30 |
| smog | 8.84 |
| smog_drop | 2.37 |
| uncertainty_preservation | 1.000 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `hydrocephalus` -> `excess fluid in the brain` | replace | attributed | 0.786 | 0.786 | - | 0.917 | 1.463 | 2.229586285 |

**edit `hydrocephalus` -> `excess fluid in the brain`**

- status: `attributed`
- log p full -7.5583, empty -8.3441
- masks scored: 18/18 (+2 top-k)
- ranked sources:
    - `+1.858` [readme] hydrocephalus: Swelling of brain due to excess fluid.
    - `+0.395` [justplainclear] hydrocephalus: Also known as: water on the brain A condition where there is too much cerebrospinal fluid in yo
    - `-1.639` [readme] HYDROCEPHALUS: When fluid around the brain builds up too much.

- rationale: Hydrocephalus describes a dangerous accumulation of fluid that pushes against the brain tissue, so "excess fluid in the brain" keeps that essential idea in plain language. Phrase frequency increases from Zipf 2.32 to 3.87, while age of acquisition falls from 15.78 to 9.58, making the new phrasing more common and learned younger. You can now understand the actual physical issue without first learning a specialized diagnostic label.
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

**output:** She said she felt very tired, dizzy, and had trouble breathing when she got active.

| metric | value |
|---|---:|
| bertscore_f1 | 0.522 |
| coleman_liau | 7.75 |
| coleman_liau_drop | 9.62 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.300 |
| fkgl | 6.78 |
| fkgl_drop | 5.52 |
| fre | 73.2 |
| fre_gain | 46.7 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 15.0 |
| nli_completeness | 0.980 |
| nli_faithfulness | 0.987 |
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

**output:** She said she felt tired, dizzy, and had severe trouble breathing when she moved.

| metric | value |
|---|---:|
| bertscore_f1 | 0.511 |
| coleman_liau | 8.60 |
| coleman_liau_drop | 8.76 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.300 |
| fkgl | 5.88 |
| fkgl_drop | 6.42 |
| fre | 77.8 |
| fre_gain | 51.3 |
| human_edit_recall | 1.000 |
| length_ratio | 0.93 |
| n_words | 14.0 |
| nli_completeness | 0.992 |
| nli_faithfulness | 0.988 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 24.68 |
| severity_downgrade | 0.000 |
| severity_preservation | 1.000 |
| severity_tier_input | 3.000 |
| severity_tier_output | 3.000 |
| smog | 3.13 |
| smog_drop | 9.89 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `fatigue` -> `tired` | replace | - | - | - | - | - | - | - |
| `lightheadedness` -> `dizzy` | replace | - | - | - | - | - | - | - |
| `dyspnea on exertion` -> `trouble breathing when she moved` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** She reported tiredness, dizziness, and severe shortness of breath with activity.

| metric | value |
|---|---:|
| bertscore_f1 | 0.756 |
| coleman_liau | 16.84 |
| coleman_liau_drop | 0.53 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.222 |
| fkgl | 12.30 |
| fkgl_drop | 0.00 |
| fre | 26.5 |
| fre_gain | 0.0 |
| human_edit_recall | 1.000 |
| length_ratio | 0.73 |
| n_words | 11.0 |
| nli_completeness | 0.993 |
| nli_faithfulness | 0.994 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 40.39 |
| severity_downgrade | 0.000 |
| severity_preservation | 1.000 |
| severity_tier_input | 3.000 |
| severity_tier_output | 3.000 |
| smog | 14.55 |
| smog_drop | -1.53 |

annotation backend `novita`, 4 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `noted complaints of` -> `reported` | replace | attributed | 0.041 | 0.042 | 0.449 | 0.723 | 0.008 | 0.05957059999999981 |
| `fatigue` -> `tiredness` | replace | attributed | -0.477 | -0.479 | 0.453 | 0.847 | 0.027 | -0.2315993169999997 |
| `lightheadedness` -> `dizziness` | replace | attributed | 0.278 | 0.433 | 0.924 | 0.881 | 0.380 | 0.252622872 |
| `dyspnea on exertion` -> `shortness of breath with activity` | replace | attributed | -3.395 | -3.398 | 0.810 | 0.849 | 0.040 | -0.4488172059999993 |

**edit `noted complaints of` -> `reported`**

- status: `attributed`
- log p full -3.3056, empty -3.3464
- masks scored: 66/66 (+8 top-k)
- ranked sources:
    - `+0.097` [wiktionary] noted: If somebody is a noted person, they are well known.
    - `+0.088` [wiktionary] on: at the date of
    - `+0.049` [dictionary] Of (prep.): Denoting that from which anything proceeds; indicating origin, source, descent, and the like; as, 
    - `+0.041` [wiktionary] on: positioned at the upper surface of, touching from above
    - `+0.037` [thesaurus] exertion: effort, work

- rationale: "Noted complaints of" simply means symptoms or concerns a person brings to attention during a visit, and "reported" captures that exact idea by directly stating what the patient shared. Phrase frequency increases from Zipf 4.10 to 5.00, making it more common and easier to process, while the syllable count drops from 5 to 3. Patients can now grasp the core message about their symptoms without getting tangled in clinical phrasing.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `fatigue` -> `tiredness`**

- status: `attributed`
- log p full -5.7732, empty -5.2958
- masks scored: 66/66 (+8 top-k)
- ranked sources:
    - `+0.248` [readme] fatigue: Feeling exhausted and lacking energy.
    - `+0.221` [wiktionary] noted: A note is a single sound in music.
    - `+0.200` [dictionary] Of (prep.): Denoting that from which anything proceeds; indicating origin, source, descent, and the like; as, 
    - `+0.198` [wiktionary] on: at the date of
    - `+0.186` [wiktionary] exertion: An exertion is the expenditure of physical or mental effort.

- rationale: The original term describes a state of extreme physical or mental exhaustion, and "tiredness" captures that same feeling in everyday language. Phrase frequency increases from Zipf 3.86 to 2.92, while age of acquisition falls from 11.83 to 7.22. Patients can now grasp the symptom without needing to know the clinical label.
- audit: coverage 1.0, grounding_error=True, omission=False, source_ok=True, passage_ok=True

**edit `lightheadedness` -> `dizziness`**

- status: `attributed`
- log p full -0.8925, empty -1.1700
- masks scored: 66/66 (+8 top-k)
- ranked sources:
    - `+0.408` [readme] lightheadedness: Feeling dizzy or almost faint.
    - `+0.028` [readme] fatigue: Feeling exhausted and lacking energy.

- rationale: Lightheadedness describes that sudden, floating sensation when your head feels unsteady, and swapping it for dizziness keeps that exact physical feeling while using a more everyday word. Word frequency increases from Zipf 1.92 to 3.11, and age of acquisition falls from 10.11 to 8.06, meaning the replacement is more common and learned younger. You can now grasp the symptom without needing to decode a clinical label.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `dyspnea on exertion` -> `shortness of breath with activity`**

- status: `attributed`
- log p full -9.3990, empty -6.0036
- masks scored: 66/66 (+8 top-k)
- ranked sources:
    - `+0.265` [michigan] exertion: Effort or work.
    - `+0.226` [wiktionary] exertion: An exertion is the expenditure of physical or mental effort.
    - `+0.168` [dictionary] Of (prep.): Denoting that from which anything proceeds; indicating origin, source, descent, and the like; as, 
    - `+0.140` [wiktionary] noted: If somebody is a noted person, they are well known.
    - `+0.081` [wiktionary] on: positioned at the upper surface of, touching from above

- rationale: "Dyspnea on exertion" simply describes the struggle to catch your breath when you move or work, so swapping it for "shortness of breath with activity" keeps that exact physical sensation while using everyday language. Phrase frequency increases from Zipf 2.09 to 2.87, which is a higher value meaning the new wording is more common and easier to process, while age of acquisition drops from 11.58 to 8.11, a lower value meaning those words are learned younger and more intuitively. You can now clearly understand how your body reacts to physical effort without having to decode clinical jargon.
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

**output:** The patient had no noticeable swelling on the top of the hand related to these.

| metric | value |
|---|---:|
| bertscore_f1 | 0.530 |
| coleman_liau | 6.97 |
| coleman_liau_drop | 2.04 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.333 |
| fkgl | 7.57 |
| fkgl_drop | 3.37 |
| fre | 67.5 |
| fre_gain | 26.0 |
| human_edit_recall | 1.000 |
| length_ratio | 1.07 |
| n_words | 15.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.965 |
| nli_faithfulness | 0.924 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 28.98 |
| severity_downgrade | 1.000 |
| severity_preservation | 0.000 |
| severity_tier_input | 2.000 |
| smog | 11.21 |
| smog_drop | 1.82 |

### Stage 4 - arm `termonly`

**output:** No large amount of swelling linked to these on the back of the hand.

| metric | value |
|---|---:|
| bertscore_f1 | 0.869 |
| coleman_liau | 4.46 |
| coleman_liau_drop | 4.56 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.800 |
| fkgl | 3.36 |
| fkgl_drop | 7.59 |
| fre | 95.9 |
| fre_gain | 54.4 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 14.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.854 |
| nli_faithfulness | 0.541 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 42.37 |
| severity_downgrade | 0.000 |
| severity_preservation | 1.000 |
| severity_tier_input | 2.000 |
| severity_tier_output | 2.000 |
| smog | 3.13 |
| smog_drop | 9.89 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `associated with` -> `linked to` | replace | - | - | - | - | - | - | - |
| `dorsum` -> `back` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** No large amount of swelling linked to these in the back of the hand.

| metric | value |
|---|---:|
| bertscore_f1 | 0.883 |
| coleman_liau | 4.46 |
| coleman_liau_drop | 4.56 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.800 |
| fkgl | 3.36 |
| fkgl_drop | 7.59 |
| fre | 95.9 |
| fre_gain | 54.4 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 14.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.828 |
| nli_faithfulness | 0.423 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 52.43 |
| severity_downgrade | 0.000 |
| severity_preservation | 1.000 |
| severity_tier_input | 2.000 |
| severity_tier_output | 2.000 |
| smog | 3.13 |
| smog_drop | 9.89 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `associated with` -> `linked to` | replace | attributed | 0.479 | 0.987 | 0.697 | 0.710 | 0.257 | 0.008966913999999937 |
| `dorsum` -> `back` | replace | attributed | 0.066 | 0.747 | 0.810 | 0.901 | 0.570 | 0.053007969 |

**edit `associated with` -> `linked to`**

- status: `attributed`
- log p full -0.4538, empty -0.9328
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.876` [readme] associated with: Linked to something.
    - `+0.619` [justplainclear] associated with: Linked to, related to, goes along with, is part of
    - `+0.293` [nih] significant: In statistics, describes a mathematical measure of difference between groups. The difference is s
    - `+0.199` [justplainclear] amount: How much or how many
    - `+0.155` [readme] dorsum: The dorsum is basically the back or upper surface.

- rationale: "Associated with" simply means that two things happen together or share a connection, and swapping it for "linked to" preserves that exact relationship while using everyday language. Phrase frequency shifts from Zipf 4.89 to 4.54, and age of acquisition falls from 4.44 to 3.95, making the phrasing easier to process. You can now grasp the medical connection without getting tangled in clinical jargon.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `dorsum` -> `back`**

- status: `attributed`
- log p full -0.0639, empty -0.1303
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.593` [readme] dorsum: The dorsum is basically the back or upper surface.
    - `+0.023` [readme] Associated with: Connected with something.
    - `+0.017` [readme] Edema: Swelling in the body caused by too much fluid.
    - `+0.012` [nih] significant: In statistics, describes a mathematical measure of difference between groups. The difference is s
    - `+0.003` [readme] edema: Swelling due to too much fluid in the body tissues.

- rationale: "Dorsum" refers to the posterior part of the body, so swapping it for "back" preserves that exact anatomical location in everyday language. Word frequency increases from Zipf 2.47 to 6.04, and the syllable count drops from 2 to 1, both of which lower the reading difficulty. Patients can now quickly grasp the physical location of the condition without first decoding a Latin medical term.
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

**output:** The patient has no heart or lung symptoms.

| metric | value |
|---|---:|
| bertscore_f1 | 0.577 |
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
| nli_faithfulness | 0.985 |
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
| `cardio` -> `heart` | replace | attributed | -0.802 | -0.923 | 0.375 | 0.701 | 0.097 | 0.13220489999999963 |
| `pulmonary` -> `lung` | replace | attributed | 0.046 | 0.456 | 0.623 | 0.652 | 0.018 | 0.004190157 |

**edit `cardio` -> `heart`**

- status: `attributed`
- log p full -2.4639, empty -1.6619
- masks scored: 66/66 (+3 top-k)
- ranked sources:
    - `+0.316` [nih] pulmonary: Having to do with the lungs.
    - `+0.219` [readme] pulmonary: Related to the lungs.

- rationale: The original term refers to the heart, and "heart" carries that meaning in plain words. Word frequency increases from Zipf 3.44 to 5.31. Patients can understand the basic heart-rhythm problem without first knowing the diagnostic name.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `pulmonary` -> `lung`**

- status: `attributed`
- log p full -0.0846, empty -0.1305
- masks scored: 66/66 (+3 top-k)
- ranked sources:
    - `+0.018` [nih] pulmonary: Having to do with the lungs.

- rationale: "Pulmonary" describes anything related to the respiratory system, so replacing it with "lung" keeps that core idea while speaking in plain language. Phrase frequency increases from Zipf 3.50 to 4.10, and age of acquisition decreases from 13.05 to 7.16, meaning the new term is both more common and learned younger. You can now clearly identify the specific organ involved without needing to decode a specialized medical label.
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

**output:** At that time, the patient was not given Coreg because of low blood pressure.

| metric | value |
|---|---:|
| bertscore_f1 | 0.608 |
| coleman_liau | 7.36 |
| coleman_liau_drop | 1.04 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.250 |
| fkgl | 5.04 |
| fkgl_drop | 1.89 |
| fre | 83.9 |
| fre_gain | 18.9 |
| human_edit_recall | 1.000 |
| length_ratio | 1.08 |
| n_words | 14.0 |
| nli_completeness | 0.733 |
| nli_faithfulness | 0.683 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 49.19 |
| smog | 3.13 |
| smog_drop | 8.08 |

### Stage 4 - arm `termonly`

**output:** At that time, the diabetes medicine had been held because of low blood pressure.

| metric | value |
|---|---:|
| bertscore_f1 | 0.698 |
| coleman_liau | 9.01 |
| coleman_liau_drop | -0.61 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.400 |
| fkgl | 7.57 |
| fkgl_drop | -0.63 |
| fre | 65.7 |
| fre_gain | 0.8 |
| human_edit_recall | 1.000 |
| length_ratio | 1.08 |
| n_words | 14.0 |
| nli_completeness | 0.415 |
| nli_faithfulness | 0.476 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 66.91 |
| smog | 11.21 |
| smog_drop | 0.00 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `Coreg` -> `diabetes medicine` | replace | - | - | - | - | - | - | - |
| `secondary to` -> `because of` | replace | - | - | - | - | - | - | - |
| `hypotension` -> `low blood pressure` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** At that time, the medication had been stopped because of low blood pressure.

| metric | value |
|---|---:|
| bertscore_f1 | 0.664 |
| coleman_liau | 9.58 |
| coleman_liau_drop | -1.18 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.400 |
| fkgl | 5.82 |
| fkgl_drop | 1.12 |
| fre | 76.5 |
| fre_gain | 11.6 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 13.0 |
| nli_completeness | 0.142 |
| nli_faithfulness | 0.591 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.250 |
| sari | 54.48 |
| smog | 8.84 |
| smog_drop | 2.37 |

annotation backend `novita`, 3 edits kept

- rejected: DROP non-term  'held' -> 'stopped'  (orig is not exactly one extracted hard term)

| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `Coreg` -> `medication` | replace | attributed | -3.070 | -3.125 | 0.788 | 0.915 | 0.062 | 0.13107952000000012 |
| `secondary to` -> `because of` | replace | attributed | 0.088 | 0.093 | 0.497 | 0.735 | 0.092 | 0.0828688500000001 |
| `hypotension` -> `low blood pressure` | replace | attributed | 0.343 | 1.106 | 0.859 | 0.801 | 0.028 | 0.015849214000000028 |

**edit `Coreg` -> `medication`**

- status: `attributed`
- log p full -5.9539, empty -2.8838
- masks scored: 66/66 (+5 top-k)
- ranked sources:
    - `+0.062` [wiktionary] to: To has no meaning. It is used with a bare infinitival clause.

- rationale: "Coreg" refers to a specific prescription drug used to manage blood pressure, and replacing it with "medication" keeps that essential treatment idea while using everyday language. Phrase frequency increases from Zipf 1.16 to 4.15, making it more common and easier to process, while syllable count shifts from 1 to 4. This adjustment allows you to grasp the treatment plan without needing to memorize a specialized brand name.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `secondary to` -> `because of`**

- status: `attributed`
- log p full -2.7704, empty -2.8582
- masks scored: 66/66 (+5 top-k)
- ranked sources:
    - `+0.225` [readme] hypotension: Low blood pressure.
    - `+0.133` [wiktionary] to: To has no meaning. It is used with a bare infinitival clause.
    - `+0.067` [iowa] HYPOTENSION: low blood pressure
    - `+0.049` [nih] Coreg: A drug used to treat high blood pressure and certain heart problems. It is also being studied in the pr
    - `+0.015` [readme] Hypotension: Hypotension means low blood pressure.

- rationale: "Secondary to" indicates that one health issue developed as a direct result of another, and replacing it with "because of" keeps that cause-and-effect link in plain language. Phrase frequency increases from Zipf 4.53 to 6.01, while age of acquisition falls from 9.11 to 4.55. You can now easily see how your symptoms are linked without needing to decode medical shorthand.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `hypotension` -> `low blood pressure`**

- status: `attributed`
- log p full -0.2264, empty -0.5696
- masks scored: 66/66 (+5 top-k)
- ranked sources:
    - `+0.240` [readme] hypotension: Low blood pressure.
    - `+0.211` [iowa] HYPOTENSION: low blood pressure
    - `+0.055` [wiktionary] to: To shows where something goes, the goal of movement.

- rationale: Hypotension refers to a condition where the force of blood pushing against artery walls drops below normal levels, so swapping it for "low blood pressure" preserves that exact physiological idea in everyday language. Phrase frequency increases from Zipf 2.52 to 4.65, while age of acquisition falls from 14.41 to 8.95, marking a clear shift toward more common and earlier-learned vocabulary. Patients can now grasp the core circulatory issue without needing to decode a specialized clinical label.
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

**output:** Her diarrhea has gotten better, and she is losing control of her bladder less often and has less swelling in her feet.

| metric | value |
|---|---:|
| bertscore_f1 | 0.525 |
| coleman_liau | 7.90 |
| coleman_liau_drop | 3.09 |
| copy_jargon_rate | 0.333 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 10.15 |
| fkgl_drop | 2.62 |
| fre | 61.5 |
| fre_gain | 29.5 |
| human_edit_recall | 0.667 |
| length_ratio | 1.29 |
| n_words | 22.0 |
| nli_completeness | 0.898 |
| nli_faithfulness | 0.840 |
| replacement_f1 | 0.800 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 29.60 |
| smog | 8.84 |
| smog_drop | 5.71 |
| temporality_preservation | 0.000 |

### Stage 4 - arm `termonly`

**output:** Her loose stools now have settled down and she is having less accidental urination, less swelling in her feet.

| metric | value |
|---|---:|
| bertscore_f1 | 0.767 |
| coleman_liau | 10.12 |
| coleman_liau_drop | 0.87 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.667 |
| fkgl | 8.59 |
| fkgl_drop | 4.19 |
| fre | 67.3 |
| fre_gain | 35.4 |
| human_edit_recall | 1.000 |
| length_ratio | 1.12 |
| n_words | 19.0 |
| nli_completeness | 0.935 |
| nli_faithfulness | 0.935 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 56.27 |
| smog | 11.21 |
| smog_drop | 3.35 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `diarrhea` -> `loose stools` | replace | - | - | - | - | - | - | - |
| `urinary incontinence` -> `accidental urination` | replace | - | - | - | - | - | - | - |
| `pedal edema` -> `swelling in her feet` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Her loose, watery poop now has settled down and she is having less loss of bladder control, less swollen feet.

| metric | value |
|---|---:|
| bertscore_f1 | 0.780 |
| coleman_liau | 8.24 |
| coleman_liau_drop | 2.75 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 8.14 |
| fkgl_drop | 4.63 |
| fre | 72.3 |
| fre_gain | 40.4 |
| human_edit_recall | 1.000 |
| length_ratio | 1.18 |
| n_words | 20.0 |
| nli_completeness | 0.958 |
| nli_faithfulness | 0.968 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 74.15 |
| smog | 8.84 |
| smog_drop | 5.71 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `diarrhea` -> `loose, watery poop` | replace | attributed | 10.946 | 11.000 | 0.882 | 0.889 | 2.831 | 2.8946928203000004 |
| `urinary incontinence` -> `loss of bladder control` | replace | attributed | 3.881 | 4.073 | 0.867 | 0.951 | 3.588 | 3.902716295 |
| `pedal edema` -> `swollen feet` | replace | attributed | 2.525 | 3.998 | 0.862 | 0.947 | 3.163 | 2.1399535705 |

**edit `diarrhea` -> `loose, watery poop`**

- status: `attributed`
- log p full -2.9419, empty -13.8876
- masks scored: 66/66 (+5 top-k)
- ranked sources:
    - `+4.263` [readme] diarrhea: Having loose, watery poop with cramps and bloating.
    - `+1.432` [justplainclear] diarrhea: A bowel movement that is loose and watery If your poop is like water or very runny, or if you have m
    - `+0.906` [wiktionary] diarrhea: Diarrhea is an illness where the person's poop or feces are soft like water.
    - `+0.810` [readme] urinary incontinence: When you can't control your pee.
    - `+0.663` [michigan] urinary incontinence: When you lose control of your bladder and the fluids it holds.

- rationale: The readme defines diarrhea as having loose, watery poop with cramps and bloating, so swapping it for "loose, watery poop" preserves that core physical description in plain language. Phrase frequency rises from Zipf 3.55 to 3.05, while syllable count increases from 4 to 5. This adjustment allows the patient to immediately recognize their symptoms without needing to memorize a clinical label.
- audit: coverage 1.0, grounding_error=True, omission=False, source_ok=True, passage_ok=True

**edit `urinary incontinence` -> `loss of bladder control`**

- status: `attributed`
- log p full -1.7250, empty -5.6059
- masks scored: 66/66 (+5 top-k)
- ranked sources:
    - `+3.725` [michigan] urinary incontinence: When you lose control of your bladder and the fluids it holds.
    - `+0.137` [readme] pedal edema: Swollen feet.
    - `+0.049` [readme] diarrhea: Having loose, watery poop with cramps and bloating.

- rationale: The Michigan source describes urinary incontinence as losing control of your bladder and the fluids it holds, so "loss of bladder control" preserves that exact idea in everyday language. Phrase frequency increases from Zipf 2.77 to 3.60, while age of acquisition decreases from 14.41 to 10.78. You can now recognize the core symptom without needing to decode a clinical label.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `pedal edema` -> `swollen feet`**

- status: `attributed`
- log p full -0.2418, empty -2.7663
- masks scored: 66/66 (+5 top-k)
- ranked sources:
    - `+3.358` [readme] pedal edema: Swollen feet.
    - `+0.195` [michigan] urinary incontinence: When you lose control of your bladder and the fluids it holds.
    - `+0.076` [readme] diarrhea: Having loose, watery poop with cramps and bloating.
    - `+0.070` [readme] urinary incontinence: When you can't control your pee.

- rationale: The readme explains that pedal edema refers to fluid accumulation in the lower legs, so "swollen feet" keeps that exact idea in plain language. Phrase frequency increases from Zipf 2.87 to 3.55, meaning the replacement is more common and easier to process. You can now understand the physical symptom without first learning a specialized medical label.
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

**output:** The patient felt sick to their stomach and had pain in their belly after eating because of gallbladder disease, and they have a scheduled surgery to remove the gallbladder using small incisions.

| metric | value |
|---|---:|
| bertscore_f1 | 0.417 |
| coleman_liau | 12.46 |
| coleman_liau_drop | 13.19 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 15.33 |
| fkgl_drop | 4.11 |
| fre | 42.2 |
| fre_gain | 63.3 |
| human_edit_recall | 1.000 |
| length_ratio | 1.78 |
| n_words | 32.0 |
| nli_completeness | 0.821 |
| nli_faithfulness | 0.345 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.143 |
| sari | 22.22 |
| smog | 14.55 |
| smog_drop | 1.35 |
| temporality_preservation | 1.000 |

### Stage 4 - arm `termonly`

**output:** The patient has an upset stomach and belly pain after eating because of a sick gallbladder, and a gallbladder removal is scheduled.

| metric | value |
|---|---:|
| bertscore_f1 | 0.435 |
| coleman_liau | 11.33 |
| coleman_liau_drop | 14.32 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.375 |
| fkgl | 12.30 |
| fkgl_drop | 7.13 |
| fre | 46.1 |
| fre_gain | 67.2 |
| human_edit_recall | 1.000 |
| length_ratio | 1.22 |
| n_words | 22.0 |
| nli_completeness | 0.847 |
| nli_faithfulness | 0.941 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.125 |
| sari | 20.55 |
| smog | 13.02 |
| smog_drop | 2.88 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `abdominal pain` -> `belly pain` | replace | - | - | - | - | - | - | - |
| `Gall bladder disease` -> `a sick gallbladder` | replace | - | - | - | - | - | - | - |
| `Laparoscopic cholecystectomy` -> `gallbladder removal` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Description : feeling like they want to throw up and stomach ache after eating - illness of the gallbladder - surgery to remove the gallbladder via camera scheduled.

| metric | value |
|---|---:|
| bertscore_f1 | 0.527 |
| coleman_liau | 14.10 |
| coleman_liau_drop | 11.54 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 14.46 |
| fkgl_drop | 4.98 |
| fre | 35.9 |
| fre_gain | 57.1 |
| human_edit_recall | 1.000 |
| length_ratio | 1.39 |
| n_words | 25.0 |
| nli_completeness | 0.769 |
| nli_faithfulness | 0.961 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 22.39 |
| smog | 15.90 |
| smog_drop | 0.00 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 4 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `Nausea` -> `feeling like they want to throw up` | replace | attributed | -0.697 | -0.697 | 0.976 | 0.970 | 4.727 | 4.9682773460000025 |
| `abdominal pain` -> `stomach ache` | replace | attributed | 2.585 | 3.234 | 0.774 | 0.849 | 1.432 | 0.638008138 |
| `Gall bladder disease` -> `illness of the gallbladder` | replace | attributed | -0.592 | -0.593 | 0.069 | 0.794 | 0.213 | 0.0021442819999979434 |
| `Laparoscopic cholecystectomy` -> `surgery to remove the gallbladder via camera` | replace | attributed | 3.885 | 3.885 | 0.696 | 0.840 | 1.791 | 2.0197458054000013 |

**edit `Nausea` -> `feeling like they want to throw up`**

- status: `attributed`
- log p full -15.8902, empty -15.1930
- masks scored: 66/66 (+8 top-k)
- ranked sources:
    - `+5.170` [justplainclear] nausea: Feeling like you want to throw up, stomach feels upset
    - `+0.443` [wiktionary] nausea: Nausea is the feeling of discomfort in the stomach, and the person will usually have a strong urge to 
    - `+0.334` [wiktionary] gall: If you have the gall to do something, you do it even though it is very rude or unreasonable.

- rationale: Nausea describes a distinct stomach upset that makes you feel sick, and swapping it for "feeling like they want to throw up" keeps that exact physical sensation in everyday language. Phrase frequency increases from Zipf 3.54 to 4.61, while age of acquisition drops from 8.63 to 5.31. Patients can now grasp the core stomach symptom without needing to decode clinical jargon first.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `abdominal pain` -> `stomach ache`**

- status: `attributed`
- log p full -0.6988, empty -3.2839
- masks scored: 66/66 (+8 top-k)
- ranked sources:
    - `+1.993` [readme] epigastric abdominal pain: Stomach ache that's felt below the ribs.
    - `+0.562` [justplainclear] bladder disease: A disease or disorder of your bladder. Some bladder diseases may include: • urinary incontine
    - `+0.433` [justplainclear] nausea: Feeling like you want to throw up, stomach feels upset
    - `+0.064` [readme] Laparoscopic: A surgery that uses a small tube and camera to see inside your body.
    - `+0.045` [wiktionary] gall: If you have the gall to do something, you do it even though it is very rude or unreasonable.

- rationale: The readme glossary describes abdominal pain as a stomach ache felt below the ribs, so "stomach ache" carries that exact physical location in plain language. Phrase frequency increases from Zipf 3.56 to 3.39, and age of acquisition falls from 10.24 to 5.79, making the replacement more common and learned younger. You can now clearly identify where your discomfort originates without needing to decode clinical terminology.
- audit: coverage 1.0, grounding_error=True, omission=False, source_ok=True, passage_ok=True

**edit `Gall bladder disease` -> `illness of the gallbladder`**

- status: `attributed`
- log p full -6.9735, empty -6.3811
- masks scored: 66/66 (+8 top-k)
- ranked sources:
    - `+0.419` [justplainclear] cholecystectomy: A surgery to take out your gallbladder
    - `+0.206` [nih] nausea: A feeling of sickness or discomfort in the stomach that may come with an urge to vomit. Nausea is a si
    - `+0.125` [justplainclear] bladder disease: A disease or disorder of your bladder. Some bladder diseases may include: • urinary incontine
    - `+0.059` [wiktionary] gall: Gall is anger or hatred.
    - `+0.019` [readme] epigastric abdominal pain: Stomach ache that's felt below the ribs.

- rationale: "Gall bladder disease" refers to any condition that harms the small organ responsible for storing bile, and swapping it for "illness of the gallbladder" preserves that core idea while using everyday language to describe the same physical problem. Phrase frequency increases from Zipf 3.12 to 2.80, and age of acquisition drops from 12.44 to 11.68, making the updated phrasing both more familiar and easier to learn. You can now grasp the nature of your condition without needing to memorize a clinical label first.
- audit: coverage 1.0, grounding_error=True, omission=False, source_ok=True, passage_ok=True

**edit `Laparoscopic cholecystectomy` -> `surgery to remove the gallbladder via camera`**

- status: `attributed`
- log p full -8.8721, empty -12.7567
- masks scored: 66/66 (+8 top-k)
- ranked sources:
    - `+2.174` [justplainclear] bladder disease: A disease or disorder of your bladder. Some bladder diseases may include: • urinary incontine
    - `+0.383` [readme] cholecystectomy: A surgery to remove the gallbladder, a digestion-assisting organ in the stomach.
    - `+0.089` [justplainclear] cholecystectomy: A surgery to take out your gallbladder
    - `+0.066` [readme] Cholecystectomy: A surgery to remove the gallbladder, an organ in your stomach that helps with digestion.
    - `+0.033` [wiktionary] nausea: Nausea is the feeling of discomfort in the stomach, and the person will usually have a strong urge to 

- rationale: Laparoscopic cholecystectomy refers to a minimally invasive procedure for taking out the gallbladder using small incisions and a video monitor, so "surgery to remove the gallbladder via camera" preserves that core idea by describing the action and tool in everyday terms. Phrase frequency increases from 1.73 to 2.79, while syllable count rises from 10 to 15. You can now grasp exactly what the doctor plans to do without needing to memorize a complex medical label.
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

**output:** She says she has a history of heart disease, but she cannot give any more details about it.

| metric | value |
|---|---:|
| bertscore_f1 | 0.613 |
| coleman_liau | 5.76 |
| coleman_liau_drop | 4.51 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.143 |
| fkgl | 7.82 |
| fkgl_drop | 4.45 |
| fre | 71.1 |
| fre_gain | 28.4 |
| human_edit_recall | 1.000 |
| length_ratio | 0.82 |
| n_words | 18.0 |
| negation_preservation | 0.000 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.994 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.286 |
| sari | 19.98 |
| severity_downgrade | 1.000 |
| severity_preservation | 0.000 |
| severity_tier_input | 2.000 |
| smog | 8.84 |
| smog_drop | 5.71 |
| temporality_preservation | 1.000 |

### Stage 4 - arm `termonly`

**output:** She says that she has an existing history of heart disease but is not able to explain it in detail.

| metric | value |
|---|---:|
| bertscore_f1 | 0.748 |
| coleman_liau | 5.63 |
| coleman_liau_drop | 4.64 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.286 |
| fkgl | 8.73 |
| fkgl_drop | 3.54 |
| fre | 68.1 |
| fre_gain | 25.4 |
| human_edit_recall | 1.000 |
| length_ratio | 0.91 |
| n_words | 20.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.994 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 34.66 |
| severity_downgrade | 1.000 |
| severity_preservation | 0.000 |
| severity_tier_input | 2.000 |
| smog | 11.21 |
| smog_drop | 3.35 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `underlying` -> `existing` | replace | - | - | - | - | - | - | - |
| `elaborate` -> `explain it` | replace | - | - | - | - | - | - | - |
| `to any significant extent` -> `in detail` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** She says that she has a past history of heart disease but is not able to give details at all.

| metric | value |
|---|---:|
| bertscore_f1 | 0.741 |
| coleman_liau | 3.89 |
| coleman_liau_drop | 6.38 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.286 |
| fkgl | 6.96 |
| fkgl_drop | 5.31 |
| fre | 80.8 |
| fre_gain | 38.1 |
| human_edit_recall | 1.000 |
| length_ratio | 0.91 |
| n_words | 20.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.994 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 32.99 |
| severity_downgrade | 1.000 |
| severity_preservation | 0.000 |
| severity_tier_input | 2.000 |
| smog | 8.84 |
| smog_drop | 5.71 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `underlying` -> `past` | replace | attributed | -0.182 | -0.202 | 0.873 | 0.958 | 0.003 | 0.07412583999999978 |
| `elaborate` -> `give details` | replace | attributed | 0.446 | 0.457 | 0.780 | 0.934 | 0.394 | 0.5345934960000003 |
| `to any significant extent` -> `at all` | replace | attributed | 0.928 | 0.930 | 0.824 | 0.945 | 0.407 | 0.5360752700000004 |

**edit `underlying` -> `past`**

- status: `attributed`
- log p full -2.3946, empty -2.2127
- masks scored: 66/66 (+5 top-k)
- ranked sources:
    - `+0.168` [nih] significant: In statistics, describes a mathematical measure of difference between groups. The difference is s
    - `+0.165` [wiktionary] elaborate: When something is supposed to be elaborated, it is needed to be expanded or add details to.
    - `+0.080` [wiktionary] any: some or even the smallest amount or number
    - `+0.050` [wiktionary] significant: A significant look, movement, etc. is one that has a particular meaning.
    - `+0.048` [wiktionary] any: it does not matter which

- rationale: "Underlying" refers to a hidden factor that contributes to a current health issue, so replacing it with "past" simply points to a previous experience that still influences your present symptoms. Word frequency increases from Zipf 4.17 to 5.36, and age of acquisition drops from 12.10 to 6.78, making the new term more common and learned younger. You can now clearly see how earlier life events connect to your current health without needing to decode complex medical terminology.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `elaborate` -> `give details`**

- status: `attributed`
- log p full -3.5065, empty -3.9525
- masks scored: 66/66 (+5 top-k)
- ranked sources:
    - `+0.567` [wiktionary] elaborate: When something is supposed to be elaborated, it is needed to be expanded or add details to.
    - `+0.173` [nih] significant: In statistics, describes a mathematical measure of difference between groups. The difference is s
    - `+0.048` [wiktionary] to: To has no meaning. It is used with a bare infinitival clause.
    - `+0.017` [wiktionary] any: it does not matter which

- rationale: The word "elaborate" means to develop or explain something thoroughly, and switching to "give details" preserves that core idea by using everyday language to describe the same action. Phrase frequency increases from Zipf 4.06 to 4.85, making the expression more common and easier to encounter, while age of acquisition falls from 11.53 to 4.28, indicating it is learned younger and more easily. With this simpler phrasing, you can immediately grasp what your care team is asking you to do without getting stuck on unfamiliar vocabulary.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `to any significant extent` -> `at all`**

- status: `attributed`
- log p full -6.1474, empty -7.0757
- masks scored: 66/66 (+5 top-k)
- ranked sources:
    - `+0.697` [wiktionary] elaborate: When something is supposed to be elaborated, it is needed to be expanded or add details to.
    - `+0.291` [wiktionary] any: some or even the smallest amount or number
    - `+0.090` [wiktionary] any: it does not matter which
    - `+0.088` [wiktionary] to: To has no meaning. It is used with a bare infinitival clause.

- rationale: The original phrase means that something happens to a noticeable or important degree, and swapping it for "at all" preserves that idea by simply asking whether the effect exists in any measurable way. Phrase frequency increases from Zipf 4.34 to 6.30, meaning it is higher, more common, and easier, while age of acquisition decreases from 10.72 to 4.24, meaning it is lower, learned younger, and easier. You can now quickly grasp whether a treatment or symptom actually matters without getting tangled in complicated wording.
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

**output:** There was a little bit of swelling on his fourth finger, and he is still wearing his wedding ring on it.

| metric | value |
|---|---:|
| bertscore_f1 | 0.770 |
| coleman_liau | 5.44 |
| coleman_liau_drop | 1.61 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.667 |
| fkgl | 7.21 |
| fkgl_drop | -0.70 |
| fre | 80.8 |
| fre_gain | 0.3 |
| human_edit_recall | 1.000 |
| length_ratio | 1.17 |
| n_words | 21.0 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.994 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.667 |
| sari | 28.10 |
| severity_downgrade | 0.000 |
| severity_preservation | 0.000 |
| severity_tier_input | 1.000 |
| severity_tier_output | 1.000 |
| smog | 3.13 |
| smog_drop | 5.71 |

### Stage 4 - arm `termonly`

**output:** There was some slight swelling of the fourth finger, on which he still is wearing his wedding band.

| metric | value |
|---|---:|
| bertscore_f1 | 1.000 |
| coleman_liau | 8.33 |
| coleman_liau_drop | -1.29 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.667 |
| fkgl | 5.85 |
| fkgl_drop | 0.66 |
| fre | 85.2 |
| fre_gain | 4.7 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 18.0 |
| nli_completeness | 0.990 |
| nli_faithfulness | 0.989 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 100.00 |
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

**output:** There was some slight swelling of the fourth finger, on which he still is wearing his wedding band.

| metric | value |
|---|---:|
| bertscore_f1 | 1.000 |
| coleman_liau | 8.33 |
| coleman_liau_drop | -1.29 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.667 |
| fkgl | 5.85 |
| fkgl_drop | 0.66 |
| fre | 85.2 |
| fre_gain | 4.7 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 18.0 |
| nli_completeness | 0.990 |
| nli_faithfulness | 0.989 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 100.00 |
| severity_downgrade | 0.000 |
| severity_preservation | 1.000 |
| severity_tier_input | 1.000 |
| severity_tier_output | 1.000 |
| smog | 3.13 |
| smog_drop | 5.71 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `edema` -> `swelling` | replace | attributed | 0.061 | 0.459 | 0.119 | 0.582 | 0.043 | 0.005148515999999992 |
| `fourth digit` -> `fourth finger` | replace | attributed | 0.700 | 1.712 | 0.898 | 0.938 | 0.469 | 0.28840966700000004 |

**edit `edema` -> `swelling`**

- status: `attributed`
- log p full -0.1144, empty -0.1755
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.058` [nih] edema: Swelling caused by excess fluid in body tissues.
    - `+0.015` [wiktionary] digit: A digit is any of the numerals from 0 to 9, especially when forming part of a number.

- rationale: Edema describes fluid accumulation in the skin and underlying tissues, and replacing it with "swelling" keeps that core idea while speaking in everyday terms. Phrase frequency increases from Zipf 2.95 to 3.68, showing a higher score that means the term is more common and easier to encounter. You can now recognize the physical symptom without first learning a specialized medical label.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `fourth digit` -> `fourth finger`**

- status: `attributed`
- log p full -0.2525, empty -0.9521
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.663` [wiktionary] fourth: The fourth thing is something that is number four (4) in order.
    - `+0.194` [readme] digit: A digit is a finger or toe.
    - `+0.183` [wiktionary] digit: A digit is any of the numerals from 0 to 9, especially when forming part of a number.
    - `+0.142` [readme] DIGIT: A digit is a finger or a toe.
    - `+0.031` [michigan] edema: Swelling caused by too much fluid in your body.

- rationale: Wiktionary explains that "fourth digit" simply refers to whatever item comes in number four, so changing it to "fourth finger" keeps that exact counting meaning in plain language. Phrase frequency increases from Zipf 3.73 to 4.32, while age of acquisition falls from 9.26 to 4.68. You can now instantly recognize which body part is being discussed without having to translate medical jargon.
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

**output:** Parents say that she appears to breathe fast, gets a bit tired while feeding, works harder to breathe, and sweats.

| metric | value |
|---|---:|
| bertscore_f1 | 0.562 |
| coleman_liau | 9.11 |
| coleman_liau_drop | 6.27 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.333 |
| fkgl | 6.96 |
| fkgl_drop | 5.87 |
| fre | 80.8 |
| fre_gain | 40.3 |
| human_edit_recall | 1.000 |
| length_ratio | 0.95 |
| n_words | 20.0 |
| nli_completeness | 0.893 |
| nli_faithfulness | 0.167 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 17.50 |
| smog | 3.13 |
| smog_drop | 9.89 |

### Stage 4 - arm `termonly`

**output:** Parents do say that she does appear to breathe fast, tires somewhat with the feeding with increased working hard to breathe and sweating.

| metric | value |
|---|---:|
| bertscore_f1 | 0.855 |
| coleman_liau | 11.41 |
| coleman_liau_drop | 3.97 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 9.28 |
| fkgl_drop | 3.54 |
| fre | 69.5 |
| fre_gain | 29.0 |
| human_edit_recall | 1.000 |
| length_ratio | 1.10 |
| n_words | 23.0 |
| nli_completeness | 0.424 |
| nli_faithfulness | 0.615 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 54.63 |
| smog | 3.13 |
| smog_drop | 9.89 |

annotation backend `novita`, 4 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `state` -> `say` | replace | - | - | - | - | - | - | - |
| `rapidly` -> `fast` | replace | - | - | - | - | - | - | - |
| `respiratory effort` -> `working hard to breathe` | replace | - | - | - | - | - | - | - |
| `diaphoresis` -> `sweating` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Parents do say that she does appear to breathe quickly, tires somewhat with the feeding with increased breathing work and sweating.

| metric | value |
|---|---:|
| bertscore_f1 | 0.934 |
| coleman_liau | 12.90 |
| coleman_liau_drop | 2.49 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.833 |
| fkgl | 9.46 |
| fkgl_drop | 3.37 |
| fre | 64.7 |
| fre_gain | 24.2 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 21.0 |
| nli_completeness | 0.434 |
| nli_faithfulness | 0.594 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 71.04 |
| smog | 3.13 |
| smog_drop | 9.89 |

annotation backend `novita`, 4 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `state` -> `say` | replace | attributed | -0.315 | -0.325 | 0.915 | 0.929 | 0.056 | 0.2171602899999998 |
| `rapidly` -> `quickly` | replace | attributed | 1.208 | 2.043 | 0.873 | 0.929 | 2.012 | 1.13975362 |
| `respiratory effort` -> `breathing work` | replace | attributed | 0.558 | 0.714 | 0.361 | 0.708 | 0.066 | -0.015026079999999942 |
| `diaphoresis` -> `sweating` | replace | attributed | -1.445 | -2.349 | 0.919 | 0.966 | 1.641 | 2.5581161074 |

**edit `state` -> `say`**

- status: `attributed`
- log p full -3.6096, empty -3.2945
- masks scored: 66/66 (+8 top-k)
- ranked sources:
    - `+0.131` [readme] RESPIRATORY: Related to breathing or the lungs and airways.
    - `+0.074` [wiktionary] rapidly: If something is done rapidly, then it is done quickly or swiftly.
    - `+0.044` [wiktionary] effort: The amount of work that is done on something.
    - `+0.041` [readme] diaphoresis: Heavy sweating.
    - `+0.006` [readme] Diaphoresis: Intense sweating.

- rationale: The original term "state" refers to a person's condition or situation, and "say" captures the act of expressing that condition in everyday language. Phrase frequency increases from Zipf 5.78 to 5.89, while age of acquisition falls from 6.39 to 3.42. This change allows patients to grasp the idea of verbal expression without needing to know the clinical context.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `rapidly` -> `quickly`**

- status: `attributed`
- log p full -0.4303, empty -1.6384
- masks scored: 66/66 (+8 top-k)
- ranked sources:
    - `+2.052` [wiktionary] rapidly: If something is done rapidly, then it is done quickly or swiftly.
    - `+0.040` [thesaurus] state: say, tell, condition

- rationale: The glossary explains that "rapidly" indicates swift action, so swapping it for "quickly" preserves that exact speed in plain language. Word frequency increases from Zipf 4.34 to 5.00, meaning the replacement is more common and easier to read. You can now understand the intended timing of the treatment without getting stuck on unfamiliar medical jargon.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `respiratory effort` -> `breathing work`**

- status: `attributed`
- log p full -1.2644, empty -1.8228
- masks scored: 66/66 (+8 top-k)
- ranked sources:
    - `+0.188` [wiktionary] state: Any sovereign nation (nation that rules itself) is a state.
    - `+0.122` [wiktionary] respiratory: A respiratory problem refers to something that affects breathing or the lungs.
    - `+0.049` [readme] Respiratory: Related to how you breathe and the organs involved in breathing like the lungs and airways.
    - `+0.015` [wiktionary] state: A state is a condition or a situation.
    - `+0.001` [wiktionary] effort: The amount of work that is done on something.

- rationale: "Respiratory effort" simply describes the physical strain required to move air in and out of the lungs, and "breathing work" keeps that exact idea by translating the clinical concept into everyday language. Phrase frequency increases from Zipf 3.78 to 4.27, while age of acquisition falls from 11.00 to 5.86, meaning the updated phrasing is both more common and learned earlier. You can now grasp the physical demand of your treatment without needing to decode clinical jargon.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `diaphoresis` -> `sweating`**

- status: `attributed`
- log p full -1.8631, empty -0.4184
- masks scored: 66/66 (+8 top-k)
- ranked sources:
    - `+2.422` [justplainclear] diaphoresis: Sweating
    - `+0.781` [readme] RESPIRATORY: Related to breathing or the lungs and airways.
    - `+0.366` [readme] Respiratory: Related to how you breathe and the organs involved in breathing like the lungs and airways.
    - `+0.303` [michigan] diaphoresis: Sweating, a clear, salty liquid produced by glands in your skin. Sweating is how your body cools 
    - `+0.132` [thesaurus] state: say, tell, condition

- rationale: Diaphoresis simply refers to the body producing sweat, so replacing it with the common word sweating keeps that exact physical sensation in plain language. Word frequency increases from Zipf 1.28 to 3.66, while the syllable count drops from 3 to 2. You can now grasp the symptom immediately without needing to decode a clinical label.
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

**output:** According to the patient, he has not used amphetamines for at least four to five months; however, he started having chest pain this evening.

| metric | value |
|---|---:|
| bertscore_f1 | 0.830 |
| coleman_liau | 10.27 |
| coleman_liau_drop | -0.89 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 10.98 |
| fkgl_drop | 0.36 |
| fre | 59.1 |
| fre_gain | -0.9 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 24.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.995 |
| nli_faithfulness | 0.995 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 43.48 |
| smog | 13.02 |
| smog_drop | 0.00 |

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

**output:** The patient had a suction performed from the mouth to the stomach, but there was only a small amount of clear liquid inside.

| metric | value |
|---|---:|
| bertscore_f1 | 0.421 |
| coleman_liau | 8.13 |
| coleman_liau_drop | 7.91 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.250 |
| fkgl | 9.28 |
| fkgl_drop | -0.91 |
| fre | 69.5 |
| fre_gain | 16.6 |
| human_edit_recall | 1.000 |
| length_ratio | 1.44 |
| n_words | 23.0 |
| nli_completeness | 0.974 |
| nli_faithfulness | 0.914 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 32.38 |
| smog | 3.13 |
| smog_drop | 5.71 |

### Stage 4 - arm `termonly`

**output:** A stomach tube was used, but only a small amount of clear fluid came out.

| metric | value |
|---|---:|
| bertscore_f1 | 0.398 |
| coleman_liau | 4.27 |
| coleman_liau_drop | 11.77 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.125 |
| fkgl | 5.21 |
| fkgl_drop | 3.16 |
| fre | 84.5 |
| fre_gain | 31.6 |
| human_edit_recall | 1.000 |
| length_ratio | 0.94 |
| n_words | 15.0 |
| nli_completeness | 0.970 |
| nli_faithfulness | 0.972 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 32.48 |
| smog | 3.13 |
| smog_drop | 5.71 |

annotation backend `novita`, 0 edits kept


### Stage 4 - arm `grounded`

**output:** A mouth tube pull was done with only very little plain liquid in the stomach.

| metric | value |
|---|---:|
| bertscore_f1 | 0.475 |
| coleman_liau | 6.20 |
| coleman_liau_drop | 9.84 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.300 |
| fkgl | 5.99 |
| fkgl_drop | 2.38 |
| fre | 78.8 |
| fre_gain | 25.9 |
| human_edit_recall | 1.000 |
| length_ratio | 0.94 |
| n_words | 15.0 |
| nli_completeness | 0.831 |
| nli_faithfulness | 0.925 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 28.85 |
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

**output:** Probably there is some tightness because of scar tissue.

| metric | value |
|---|---:|
| bertscore_f1 | 0.677 |
| coleman_liau | 11.20 |
| coleman_liau_drop | 4.51 |
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
| nli_completeness | 0.875 |
| nli_faithfulness | 0.933 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 28.34 |
| smog | 8.84 |
| smog_drop | 5.71 |
| uncertainty_preservation | 1.000 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `restrictive element` -> `tightness` | replace | - | - | - | - | - | - | - |
| `fibrosis` -> `scar tissue` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Probably there is some limiting factor because of thick, scarred tissue.

| metric | value |
|---|---:|
| bertscore_f1 | 0.763 |
| coleman_liau | 13.15 |
| coleman_liau_drop | 2.57 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.250 |
| fkgl | 8.01 |
| fkgl_drop | 3.51 |
| fre | 57.2 |
| fre_gain | 28.7 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 11.0 |
| nli_completeness | 0.703 |
| nli_faithfulness | 0.736 |
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
| `restrictive element` -> `limiting factor` | replace | attributed | 0.907 | 0.924 | 0.761 | 0.903 | 0.952 | 1.0681828300000005 |
| `fibrosis` -> `thick, scarred tissue` | replace | attributed | 6.167 | 6.229 | 0.966 | 0.934 | 7.906 | 9.207836309000001 |

**edit `restrictive element` -> `limiting factor`**

- status: `attributed`
- log p full -3.6063, empty -4.5135
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.981` [wiktionary] restrictive: If something is restrictive, it limits or controls what people can do.
    - `+0.029` [nih] fibrosis: The growth of fibrous tissue.
    - `-0.093` [wiktionary] element: An element is one basic kind of substance, such as iron (Fe), oxygen (O), or sodium (Na).

- rationale: Wiktionary explains that a restrictive element limits or controls what people can do, so "limiting factor" preserves that core idea in everyday language. Phrase frequency increases from Zipf 3.49 to 3.87, while age of acquisition falls from 11.00 to 9.72. You can now clearly see how your condition affects your daily routine without needing to decipher specialized medical terminology.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `fibrosis` -> `thick, scarred tissue`**

- status: `attributed`
- log p full -2.8137, empty -8.9807
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+8.180` [readme] FIBROSIS: Fibrosis is tissue that becomes thick and scarred due to injury.
    - `+0.273` [nih] element: A basic part of a whole. In chemistry, refers to a simple substance that cannot be broken down into s
    - `-0.133` [wiktionary] restrictive: If something is restrictive, it limits or controls what people can do.

- rationale: The readme explains that fibrosis is tissue that becomes thick and scarred due to injury, so swapping it for "thick, scarred tissue" preserves that core idea in everyday language. Phrase frequency increases from Zipf 3.19 to 3.21, while age of acquisition drops from 14.94 to 5.61, making the updated wording both more common and learned younger. You can now clearly grasp how your body repairs damage without first memorizing a clinical label.
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

**output:** The uterus was moved back inside the belly.

| metric | value |
|---|---:|
| bertscore_f1 | 0.728 |
| coleman_liau | 5.88 |
| coleman_liau_drop | 3.39 |
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
| nli_completeness | 0.988 |
| nli_faithfulness | 0.990 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 22.73 |
| smog | 8.84 |
| smog_drop | 4.18 |

### Stage 4 - arm `termonly`

**output:** The womb was put back into the belly area.

| metric | value |
|---|---:|
| bertscore_f1 | 0.807 |
| coleman_liau | 2.18 |
| coleman_liau_drop | 7.09 |
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
| nli_completeness | 0.984 |
| nli_faithfulness | 0.981 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.250 |
| sari | 48.55 |
| smog | 8.84 |
| smog_drop | 4.18 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `uterus` -> `womb` | replace | - | - | - | - | - | - | - |
| `abdominal cavity` -> `belly area` | replace | - | - | - | - | - | - | - |

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
| `uterus` -> `womb` | replace | attributed | 0.153 | 0.205 | 0.556 | 0.714 | 0.088 | 0.07688658500000001 |
| `abdominal cavity` -> `belly` | replace | attributed | 0.207 | 1.066 | 0.920 | 0.913 | 2.531 | 1.198839821 |

**edit `uterus` -> `womb`**

- status: `attributed`
- log p full -1.3068, empty -1.4601
- masks scored: 66/66 (+3 top-k)
- ranked sources:
    - `+0.133` [michigan] uterus: Womb, or where a baby grows when a woman is pregnant.
    - `+0.045` [readme] abdominal cavity: The belly area where your stomach and other organs are located.
    - `-0.047` [thesaurus] uterus: womb

- rationale: The uterus is the female reproductive organ that houses and nurtures a developing baby, so switching to "womb" preserves that core biological function while using everyday language. Phrase frequency increases from Zipf 3.40 to 3.63, making it more common and easier to encounter, while age of acquisition falls from 12.84 to 9.48, meaning it is learned younger and more familiar. Patients can now grasp the basic anatomical concept without needing to memorize a clinical label.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `abdominal cavity` -> `belly`**

- status: `attributed`
- log p full -0.1285, empty -0.3351
- masks scored: 66/66 (+3 top-k)
- ranked sources:
    - `+2.565` [readme] abdominal cavity: The belly area where your stomach and other organs are located.
    - `+0.034` [wiktionary] uterus: The uterus is the internal organ inside of a female mammal where an embryo grows into an infant ready 
    - `-0.019` [thesaurus] uterus: womb
    - `-0.035` [justplainclear] uterus: Also known as: womb An organ in a woman's body where babies may grow during pregnancy Uterus

- rationale: The abdominal cavity refers to the hollow space inside your torso that houses your digestive organs, and swapping it for "belly" keeps that same anatomical location clear and familiar. Phrase frequency increases from Zipf 3.29 to 4.10, while age of acquisition decreases from 10.24 to 4.05, making the updated wording more common and learned much younger. You can now picture exactly where your doctor is referring to without needing to memorize a clinical label.
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

**output:** This was viewed on the AP and lateral projections.

| metric | value |
|---|---:|
| bertscore_f1 | 0.495 |
| coleman_liau | 7.33 |
| coleman_liau_drop | 0.00 |
| copy_jargon_rate | 1.000 |
| critical_error | 0.000 |
| fkgl | 4.96 |
| fkgl_drop | 0.00 |
| fre | 75.5 |
| fre_gain | 0.0 |
| human_edit_recall | 0.000 |
| laterality_preservation | 1.000 |
| length_ratio | 1.12 |
| n_words | 9.0 |
| nli_completeness | 0.993 |
| nli_faithfulness | 0.993 |
| replacement_f1 | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 11.37 |
| smog | 11.21 |
| smog_drop | 0.00 |

### Stage 4 - arm `termonly`

**output:** This was viewed on the front and side X-rays.

| metric | value |
|---|---:|
| bertscore_f1 | 0.633 |
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
| length_ratio | 1.25 |
| n_words | 10.0 |
| nli_completeness | 0.222 |
| nli_faithfulness | 0.382 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 58.01 |
| smog | 3.13 |
| smog_drop | 8.08 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `AP` -> `front` | replace | - | - | - | - | - | - | - |
| `lateral projections` -> `side X-rays` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

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
| `AP` -> `front` | replace | attributed | 0.927 | 1.965 | 0.891 | 0.838 | 1.324 | 0.431864356 |
| `lateral projections` -> `side views` | replace | attributed | 0.466 | 0.556 | 0.851 | 0.927 | 0.166 | 0.35612962000000015 |

**edit `AP` -> `front`**

- status: `attributed`
- log p full -0.2864, empty -1.2137
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+2.020` [readme] anteroposterior: Front to back.
    - `+0.696` [dorland] AP: anteroposterior
    - `+0.098` [justplainclear] alkaline phosphatase test: Also known as: ALP test A test to determine how well your liver or gallbladder are 
    - `+0.095` [wiktionary] projections: A projection is when something juts out.

- rationale: The source describes AP as the front of the body, so "front" keeps that location in plain language. Syllable count stays at 1. Patients can now locate the area without needing the medical abbreviation.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `lateral projections` -> `side views`**

- status: `attributed`
- log p full -1.5968, empty -2.0629
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.418` [wiktionary] projections: A projection is when something juts out.
    - `+0.252` [readme] Lateral: To the side or relating to the side of the body or a body part.
    - `+0.152` [readme] lateral: Lateral means on or related to the side of the body or a body part.
    - `+0.063` [michigan] lateral: The side or on the side.
    - `+0.011` [wiktionary] lateral: An object's lateral refers to the side of it.

- rationale: "Lateral projections" refers to images captured from the side of the body, so "side views" keeps that exact imaging perspective in plain language. Phrase frequency increases from Zipf 3.43 to 4.75, and age of acquisition falls from 12.41 to 4.72, making the replacement more common and learned younger. You can now easily visualize how your imaging was captured without having to decipher specialized medical terminology.
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
| `phonation` -> `speaking` | replace | - | - | - | - | - | - | - |
| `ventilation` -> `breathing` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** The vocal cords move normally with speaking and breathing.

| metric | value |
|---|---:|
| bertscore_f1 | 0.775 |
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
| nli_completeness | 0.986 |
| nli_faithfulness | 0.989 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 55.49 |
| smog | 8.84 |
| smog_drop | 2.37 |

annotation backend `novita`, 2 edits kept

- rejected: DROP noop      'cords' -> 'cords'  (nothing changed)

| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `phonation` -> `speaking` | replace | attributed | 0.653 | 0.733 | - | 0.767 | 0.264 | 0.23998954000000006 |
| `ventilation` -> `breathing` | replace | attributed | 0.005 | 0.176 | - | 0.914 | 0.941 | 0.10579782100000001 |

**edit `phonation` -> `speaking`**

- status: `attributed`
- log p full -1.9133, empty -2.5662
- masks scored: 34/34 (+2 top-k)
- ranked sources:
    - `+0.307` [wiktionary] ventilation: Ventilation is the bodily process of breathing; the inhalation of air to provide oxygen, and the 
    - `+0.044` [wiktionary] ventilation: Ventilation is the replacement of stale air with fresh air.
    - `+0.041` [wiktionary] cords: A long, thin rope or wire.
    - `-0.007` [readme] ventilation: Ventilation is about bringing in fresh air.
    - `-0.158` [dictionary] Phonation (n.): The act or process by which articulate sounds are uttered; the utterance of articulate sounds;

- rationale: Phonation describes the physical vibration of the vocal cords to create sound, so replacing it with "speaking" keeps that essential idea in plain language. Word frequency increases from Zipf 1.80 to 4.91, indicating the replacement is more common and easier to process. You can now understand the basic vocal process without first learning a specialized clinical term.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `ventilation` -> `breathing`**

- status: `attributed`
- log p full -0.0274, empty -0.0326
- masks scored: 34/34 (+2 top-k)
- ranked sources:
    - `+0.964` [wiktionary] ventilation: Ventilation is the bodily process of breathing; the inhalation of air to provide oxygen, and the 
    - `+0.022` [wiktionary] cords: A long, thin rope or wire.
    - `-0.083` [dictionary] Phonation (n.): The act or process by which articulate sounds are uttered; the utterance of articulate sounds;
    - `-0.439` [readme] ventilation: Ventilation is about bringing in fresh air.

- rationale: Ventilation refers to the process of moving air into and out of the lungs, so switching to "breathing" preserves that core idea in everyday language. Word frequency increases from Zipf 3.60 to 4.28, and the syllable count drops from 4 to 2, both of which simplify the phrase for everyday readers. Patients can now grasp the essential air-exchange process without needing to decode a clinical label.
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

**output:** Once the patient's abdomen was opened, the doctors found a large amount of thick, yellow pus.

| metric | value |
|---|---:|
| bertscore_f1 | 0.620 |
| coleman_liau | 9.18 |
| coleman_liau_drop | -0.04 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 7.61 |
| fkgl_drop | 0.02 |
| fre | 69.0 |
| fre_gain | 5.5 |
| human_edit_recall | 1.000 |
| length_ratio | 1.13 |
| n_words | 17.0 |
| nli_completeness | 0.955 |
| nli_faithfulness | 0.067 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.400 |
| sari | 26.45 |
| smog | 8.84 |
| smog_drop | 2.37 |

### Stage 4 - arm `termonly`

**output:** Once the belly was opened, there was noted to be a lot of pus.

| metric | value |
|---|---:|
| bertscore_f1 | 0.891 |
| coleman_liau | 1.56 |
| coleman_liau_drop | 7.58 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.400 |
| fkgl | 4.20 |
| fkgl_drop | 3.44 |
| fre | 89.9 |
| fre_gain | 26.4 |
| human_edit_recall | 1.000 |
| length_ratio | 0.93 |
| n_words | 14.0 |
| nli_completeness | 0.905 |
| nli_faithfulness | 0.933 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 71.08 |
| smog | 3.13 |
| smog_drop | 8.08 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `abdomen` -> `belly` | replace | - | - | - | - | - | - | - |
| `gross purulent drainage` -> `a lot of pus` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Once the belly was opened, there was visible pus leaking out.

| metric | value |
|---|---:|
| bertscore_f1 | 0.726 |
| coleman_liau | 7.35 |
| coleman_liau_drop | 1.79 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.600 |
| fkgl | 5.86 |
| fkgl_drop | 1.77 |
| fre | 72.6 |
| fre_gain | 9.1 |
| human_edit_recall | 1.000 |
| length_ratio | 0.73 |
| n_words | 11.0 |
| nli_completeness | 0.956 |
| nli_faithfulness | 0.878 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.200 |
| sari | 30.71 |
| smog | 8.84 |
| smog_drop | 2.37 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `abdomen` -> `belly` | replace | attributed | 0.754 | 1.213 | 0.820 | 0.896 | 1.165 | 0.9631632000000001 |
| `gross purulent drainage` -> `visible pus leaking out` | replace | attributed | 2.105 | 2.105 | 0.900 | 0.947 | 2.057 | 4.233910978000001 |

**edit `abdomen` -> `belly`**

- status: `attributed`
- log p full -0.6468, empty -1.4011
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+1.432` [thesaurus] abdomen: stomach, stomach area, belly, tummy
    - `+0.267` [wiktionary] abdomen: The abdomen is the last of the three parts of an insect's body.
    - `+0.144` [readme] drainage: When any fluid is leaking out of a body part.
    - `+0.111` [wiktionary] gross: The gross amount is the total before you take away losses or expenses.
    - `+0.067` [wiktionary] gross: A gross violation or abuse is very bad and clearly wrong.

- rationale: The thesaurus lists "stomach, stomach area, belly, tummy" as synonyms for abdomen, so swapping to "belly" preserves that core anatomical reference while using everyday language. Word frequency increases from Zipf 3.56 to 4.10, and age of acquisition decreases from 8.61 to 4.05, making the updated phrasing more common and easier to learn. You can now easily picture where your digestive organs sit without needing to decode clinical terminology first.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `gross purulent drainage` -> `visible pus leaking out`**

- status: `attributed`
- log p full -9.5313, empty -11.6365
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+3.076` [michigan] purulent: Pus.
    - `+1.019` [readme] drainage: When any fluid is leaking out of a body part.
    - `+0.483` [wiktionary] drainage: To use a drainage is engage in the action or process of draining something.
    - `-0.083` [wiktionary] abdomen: The abdomen is the front part of the lower torso containing many internal organs.

- rationale: The glossary defines pus as a thick, yellowish-white fluid, so "visible pus leaking out" captures that core idea in everyday language. Phrase frequency rises from Zipf 1.92 to 2.92, and age of acquisition drops from 15.50 to 8.05. This makes the wound's condition clear without medical jargon.
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

**output:** Once all four tubes were placed, the upper right area was then looked at.

| metric | value |
|---|---:|
| bertscore_f1 | 0.789 |
| coleman_liau | 6.11 |
| coleman_liau_drop | 3.47 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.200 |
| fkgl | 4.20 |
| fkgl_drop | -0.20 |
| fre | 89.9 |
| fre_gain | 0.4 |
| human_edit_recall | 1.000 |
| laterality_preservation | 1.000 |
| length_ratio | 0.88 |
| n_words | 14.0 |
| nli_completeness | 0.952 |
| nli_faithfulness | 0.881 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 58.97 |
| smog | 8.84 |
| smog_drop | -5.71 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `ports` -> `tubes` | replace | - | - | - | - | - | - | - |
| `right upper quadrant` -> `upper right area` | replace | - | - | - | - | - | - | - |
| `explored` -> `looked at` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

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

annotation backend `novita`, 0 edits kept


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

**output:** Options like waiting to see how it goes, surgery to remove the prostate using robots, and putting tiny seeds into the prostate with or without radiation were discussed.

| metric | value |
|---|---:|
| bertscore_f1 | 0.605 |
| coleman_liau | 11.73 |
| coleman_liau_drop | 9.16 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 14.29 |
| fkgl_drop | 1.14 |
| fre | 42.5 |
| fre_gain | 31.3 |
| human_edit_recall | 1.000 |
| length_ratio | 1.22 |
| n_words | 28.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.975 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.167 |
| sari | 36.64 |
| smog | 11.21 |
| smog_drop | 3.35 |

### Stage 4 - arm `termonly`

**output:** Options such as waiting to see, surgery to remove the prostate, placing small seeds with and without energy treatment were discussed.

| metric | value |
|---|---:|
| bertscore_f1 | 0.593 |
| coleman_liau | 13.17 |
| coleman_liau_drop | 7.72 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.714 |
| fkgl | 11.14 |
| fkgl_drop | 4.29 |
| fre | 52.6 |
| fre_gain | 41.5 |
| human_edit_recall | 1.000 |
| length_ratio | 0.91 |
| n_words | 21.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.629 |
| nli_faithfulness | 0.985 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 36.79 |
| smog | 11.21 |
| smog_drop | 3.35 |

annotation backend `novita`, 4 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `watchful waiting` -> `waiting to see` | replace | - | - | - | - | - | - | - |
| `robotic prostatectomy` -> `surgery to remove the prostate` | replace | - | - | - | - | - | - | - |
| `seed implantation` -> `placing small seeds` | replace | - | - | - | - | - | - | - |
| `radiation` -> `energy treatment` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Options such as close monitoring without treatment, robot-assisted prostate surgery, placing small seeds inside with and without high-energy rays were discussed.

| metric | value |
|---|---:|
| bertscore_f1 | 0.568 |
| coleman_liau | 20.35 |
| coleman_liau_drop | 0.54 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.714 |
| fkgl | 15.64 |
| fkgl_drop | -0.20 |
| fre | 20.3 |
| fre_gain | 9.2 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 23.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.991 |
| nli_faithfulness | 0.975 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 36.92 |
| smog | 14.55 |
| smog_drop | 0.00 |

annotation backend `novita`, 4 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `watchful waiting` -> `close monitoring without treatment` | replace | attributed | 6.049 | 6.074 | 0.846 | 0.898 | 5.748 | 6.436758042999999 |
| `robotic prostatectomy` -> `robot-assisted prostate surgery` | replace | attributed | 2.210 | 2.217 | 0.575 | 0.901 | 0.198 | 0.8256144110000001 |
| `seed implantation` -> `placing small seeds inside` | replace | attributed | 2.701 | 2.717 | 0.808 | 0.879 | 0.688 | 0.4306547839999997 |
| `radiation` -> `high-energy rays` | replace | attributed | 1.152 | 1.243 | 0.942 | 0.980 | 3.978 | 4.1443906044 |

**edit `watchful waiting` -> `close monitoring without treatment`**

- status: `attributed`
- log p full -3.6915, empty -9.7402
- masks scored: 66/66 (+8 top-k)
- ranked sources:
    - `+5.882` [nih] watchful waiting: Closely watching a patient’s condition but not giving treatment unless symptoms appear or ch
    - `+0.134` [nih] prostatectomy: Surgery to remove part or all of the prostate and some of the tissue around it, including the s

- rationale: The NIH glossary defines watchful waiting as closely observing a patient’s condition without starting therapy unless symptoms develop, so "close monitoring without treatment" preserves that exact idea in everyday language. Phrase frequency increases from Zipf 3.09 to 4.21, while age of acquisition falls from 8.16 to 8.11, meaning the replacement is more common and learned younger. You can now grasp exactly what your care team will do and why they are holding off on any immediate interventions.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `robotic prostatectomy` -> `robot-assisted prostate surgery`**

- status: `attributed`
- log p full -4.8461, empty -7.0563
- masks scored: 66/66 (+8 top-k)
- ranked sources:
    - `+1.210` [nih] prostatectomy: Surgery to remove part or all of the prostate and some of the tissue around it, including the s
    - `+1.012` [nih] watchful waiting: Closely watching a patient’s condition but not giving treatment unless symptoms appear or ch
    - `+0.311` [readme] IMPLANTATION: A surgery where a device is placed inside the body.
    - `+0.274` [wiktionary] radiation: Radiation is the emission or transmission of energy in the form of waves or particles through space
    - `+0.018` [readme] radiation: High energy rays used to kill cancer cells.

- rationale: The glossary explains that the original term refers to a procedure for removing prostate tissue that may be performed with a specialized robotic system, so the replacement phrase keeps that essential idea by plainly describing it as surgery where a machine assists in the removal. Phrase frequency rises from Zipf 2.13 to 3.43, while age of acquisition drops from 15.27 to 15.00. Patients can now grasp the general nature of the procedure without needing to memorize a highly technical medical label.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `seed implantation` -> `placing small seeds inside`**

- status: `attributed`
- log p full -4.1174, empty -6.8186
- masks scored: 66/66 (+8 top-k)
- ranked sources:
    - `+1.625` [readme] implantation: Surgery where a device is placed inside your body.
    - `+0.937` [readme] IMPLANTATION: A surgery where a device is placed inside the body.
    - `+0.710` [wiktionary] seed: A seed is a small round thing that can grow to be a plant, a flower or a tree.
    - `+0.262` [readme] Radiation: Radiation is powerful energy waves that are sometimes utilized to destroy cancer cells.
    - `+0.043` [wiktionary] seed: The seed of a man is his semen.

- rationale: The readme explains that seed implantation refers to surgery where a device is placed inside your body, so "placing small seeds inside" preserves that core idea using everyday language. Phrase frequency increases from Zipf 2.99 to 3.89, while age of acquisition falls from 11.95 to 4.77. You can now grasp exactly what the procedure involves without needing to decode specialized medical jargon first.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `radiation` -> `high-energy rays`**

- status: `attributed`
- log p full -2.0999, empty -3.2518
- masks scored: 66/66 (+8 top-k)
- ranked sources:
    - `+4.206` [readme] radiation: High energy rays used to kill cancer cells.
    - `+0.228` [nih] prostatectomy: Surgery to remove part or all of the prostate and some of the tissue around it, including the s
    - `+0.118` [nih] radiation: Energy released in the form of particle or electromagnetic waves. Common sources of radiation inclu
    - `+0.090` [thesaurus] radiation: see ionizing radiation and non-ionizing radiation

- rationale: The readme explains that radiation refers to high energy rays used to kill cancer cells, so replacing it with "high-energy rays" keeps that core medical purpose in plain language. Phrase frequency shifts from Zipf 4.27 to 4.00, marking a measured change in commonality that influences readability. Patients can now grasp the treatment's purpose without needing to decode a technical diagnostic label.
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

**output:** He was also said to be taking Lasix before he went to the hospital, which could be possible.

| metric | value |
|---|---:|
| bertscore_f1 | 0.507 |
| coleman_liau | 6.08 |
| coleman_liau_drop | 7.64 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.667 |
| fkgl | 7.82 |
| fkgl_drop | 6.45 |
| fre | 71.1 |
| fre_gain | 60.5 |
| human_edit_recall | 1.000 |
| length_ratio | 1.20 |
| n_words | 18.0 |
| nli_completeness | 0.995 |
| nli_faithfulness | 0.994 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 40.75 |
| smog | 11.21 |
| smog_drop | 1.82 |
| temporality_preservation | 1.000 |
| uncertainty_preservation | 1.000 |

### Stage 4 - arm `termonly`

**output:** He also, according to reports, was on a diuretic before his hospital stay, possible

| metric | value |
|---|---:|
| bertscore_f1 | 0.525 |
| coleman_liau | 9.84 |
| coleman_liau_drop | 3.88 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 11.78 |
| fkgl_drop | 2.49 |
| fre | 35.5 |
| fre_gain | 24.9 |
| human_edit_recall | 1.000 |
| length_ratio | 0.93 |
| n_words | 14.0 |
| nli_completeness | 0.075 |
| nli_faithfulness | 0.799 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 45.89 |
| smog | 14.55 |
| smog_drop | -1.53 |
| temporality_preservation | 1.000 |
| uncertainty_preservation | 1.000 |

annotation backend `novita`, 4 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `reportedly` -> `according to reports` | replace | - | - | - | - | - | - | - |
| `Lasix` -> `a diuretic` | replace | - | - | - | - | - | - | - |
| `prior to` -> `before` | replace | - | - | - | - | - | - | - |
| `hospitalization` -> `hospital stay` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** He also people say took a water pill before a hospital stay, possible

| metric | value |
|---|---:|
| bertscore_f1 | 0.357 |
| coleman_liau | 6.91 |
| coleman_liau_drop | 6.81 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.750 |
| fkgl | 8.54 |
| fkgl_drop | 5.73 |
| fre | 57.0 |
| fre_gain | 46.4 |
| human_edit_recall | 1.000 |
| length_ratio | 0.87 |
| n_words | 13.0 |
| nli_completeness | 0.144 |
| nli_faithfulness | 0.008 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 43.38 |
| smog | 11.21 |
| smog_drop | 1.82 |
| temporality_preservation | 1.000 |
| uncertainty_preservation | 1.000 |

annotation backend `novita`, 4 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `reportedly` -> `people say` | replace | attributed | 5.309 | 5.310 | 0.871 | 0.893 | 5.683 | 5.6254379199999995 |
| `Lasix` -> `a water pill` | replace | attributed | -2.157 | -2.157 | 0.528 | 0.735 | 0.178 | 0.18459801999999925 |
| `prior to` -> `before` | replace | attributed | -0.083 | -0.198 | 0.577 | 0.808 | 0.022 | 0.052077290000000054 |
| `hospitalization` -> `hospital stay` | replace | attributed | 2.604 | 2.615 | 0.804 | 0.901 | 0.225 | 0.9124992590000005 |

**edit `reportedly` -> `people say`**

- status: `attributed`
- log p full -6.9072, empty -12.2166
- masks scored: 66/66 (+7 top-k)
- ranked sources:
    - `+5.683` [wiktionary] reportedly: If something is reportedly true, people say it happened, but we don't have other reasons to believ
    - `-0.028` [michigan] prior to: Earlier or before.
    - `-0.097` [wiktionary] hospitalization: Hospitalization is the period of time when a person is in hospital for medical care.

- rationale: The source explains that "reportedly" means people claim something happened without other proof, so "people say" keeps that idea in plain language. Phrase frequency rises from Zipf 4.13 to 5.73, making it more common and easier to find. Readers can now grasp the idea of hearsay without needing to know the exact word.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `Lasix` -> `a water pill`**

- status: `attributed`
- log p full -10.6545, empty -8.4973
- masks scored: 66/66 (+7 top-k)
- ranked sources:
    - `+0.183` [wiktionary] reportedly: If something is reportedly true, people say it happened, but we don't have other reasons to believ
    - `+0.006` [readme] hospitalization: Being admitted to and staying in a hospital.
    - `-0.018` [wiktionary] hospitalization: Hospitalization is the period of time when a person is in hospital for medical care.
    - `-0.063` [wiktionary] hospitalization: Hospitalization is the process of putting a person in hospital for medical care.
    - `-0.101` [readme] Hospitalization: Being admitted to a hospital for an extended period of time.

- rationale: Lasix is a brand name for a medication that helps your kidneys remove excess fluid, so calling it a water pill keeps that core function clear and simple. Phrase frequency increases from Zipf 1.98 to 4.02, shifting toward more common and easier-to-process language, while syllable count rises from 1 to 4. You can now grasp exactly what the medication does for your body without needing to memorize a specialized brand name.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `prior to` -> `before`**

- status: `attributed`
- log p full -0.5822, empty -0.4997
- masks scored: 66/66 (+7 top-k)
- ranked sources:
    - `+0.055` [wiktionary] hospitalization: Hospitalization is the period of time when a person is in hospital for medical care.
    - `+0.032` [readme] Hospitalization: Being admitted to a hospital for an extended period of time.
    - `+0.020` [readme] hospitalization: Being admitted to and staying in a hospital.
    - `+0.017` [wiktionary] hospitalization: Hospitalization is the process of putting a person in hospital for medical care.
    - `-0.004` [wiktionary] reportedly: If something is reportedly true, people say it happened, but we don't have other reasons to believ

- rationale: "Prior to" simply means that something happened earlier in time, and swapping it for "before" keeps that exact timeline clear without using formal medical phrasing. Phrase frequency increases from Zipf 4.85 to 5.93 (higher = more common = easier), while age of acquisition falls from 10.63 to 5.45 (lower = learned younger = easier). You can now quickly grasp the sequence of your treatment steps without getting tangled in unfamiliar vocabulary.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `hospitalization` -> `hospital stay`**

- status: `attributed`
- log p full -4.5169, empty -7.1213
- masks scored: 66/66 (+7 top-k)
- ranked sources:
    - `+1.023` [readme] Hospitalization: Being admitted to a hospital for an extended period of time.
    - `+0.798` [readme] hospitalization: Being admitted to and staying in a hospital.
    - `+0.209` [michigan] prior to: Earlier or before.
    - `+0.123` [wiktionary] reportedly: If something is reportedly true, people say it happened, but we don't have other reasons to believ

- rationale: The readme defines hospitalization as being admitted to a hospital for an extended period of time, so "hospital stay" preserves that core idea using everyday language. Phrase frequency increases from Zipf 3.09 to 4.88 (higher = more common = easier), while age of acquisition decreases from 9.53 to 5.55 (lower = learned younger = easier). With this clearer wording, you can immediately grasp the expected length of your treatment without needing to decode clinical jargon.
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

**output:** The patient's four heart chambers are a normal size.

| metric | value |
|---|---:|
| bertscore_f1 | 0.540 |
| coleman_liau | 7.98 |
| coleman_liau_drop | 7.09 |
| copy_jargon_rate | 0.250 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.167 |
| fkgl | 3.65 |
| fkgl_drop | 6.56 |
| fre | 84.9 |
| fre_gain | 47.0 |
| human_edit_recall | 0.750 |
| length_ratio | 0.77 |
| n_words | 10.0 |
| nli_completeness | 0.969 |
| nli_faithfulness | 0.892 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 0.857 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 29.14 |
| smog | 3.13 |
| smog_drop | 8.08 |

### Stage 4 - arm `termonly`

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
| `cardiac chambers` -> `heart rooms` | replace | - | - | - | - | - | - | - |
| `within normal limits` -> `the right size` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** The heart's four rooms are the right size.

| metric | value |
|---|---:|
| bertscore_f1 | 0.440 |
| coleman_liau | 4.43 |
| coleman_liau_drop | 10.64 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.125 |
| fkgl | -0.67 |
| fkgl_drop | 10.88 |
| fre | 114.1 |
| fre_gain | 76.2 |
| human_edit_recall | 1.000 |
| length_ratio | 0.69 |
| n_words | 9.0 |
| nli_completeness | 0.905 |
| nli_faithfulness | 0.961 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 29.75 |
| smog | 3.13 |
| smog_drop | 8.08 |

annotation backend `novita`, 0 edits kept


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

**output:** The patient had a finger check of the rectum, which showed no lumps.

| metric | value |
|---|---:|
| bertscore_f1 | 0.584 |
| coleman_liau | 6.02 |
| coleman_liau_drop | 10.34 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.333 |
| fkgl | 4.00 |
| fkgl_drop | 7.52 |
| fre | 89.5 |
| fre_gain | 61.0 |
| human_edit_recall | 1.000 |
| length_ratio | 1.18 |
| n_words | 13.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.369 |
| nli_faithfulness | 0.198 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 43.85 |
| smog | 3.13 |
| smog_drop | 8.08 |

### Stage 4 - arm `termonly`

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
| `Digital rectal examination` -> `finger check of the rectum` | replace | - | - | - | - | - | - | - |
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
| `Digital rectal examination` -> `finger check of the rectum` | replace | attributed | -1.401 | -1.401 | - | 0.876 | 0.350 | -0.47363288000000026 |
| `performed` -> `done` | replace | attributed | 0.097 | 0.307 | - | 0.853 | 0.030 | 0.10943749000000003 |
| `masses` -> `lumps` | replace | attributed | -0.141 | -0.521 | - | 0.821 | 0.357 | 0.18697064359999993 |

**edit `Digital rectal examination` -> `finger check of the rectum`**

- status: `attributed`
- log p full -12.1859, empty -10.7847
- masks scored: 18/18 (+4 top-k)
- ranked sources:
    - `+0.376` [nih] digital rectal examination: An examination in which a doctor inserts a lubricated, gloved finger into the rect
    - `+0.026` [wiktionary] masses: A measure of how much material is in something.
    - `-0.508` [wiktionary] performed: When you perform something, you do it.
    - `-0.624` [wiktionary] masses: The masses are the regular people, not those in power.

- rationale: A digital rectal examination involves a clinician gently inserting a gloved finger into the rectum to assess internal structures, so "finger check of the rectum" preserves that exact physical action while stripping away clinical jargon. Phrase frequency increases from Zipf 2.88 to 2.94, while age of acquisition falls from 13.06 to 9.84, indicating a shift toward more common and younger-learned vocabulary. Patients can now grasp the purpose of the procedure without needing to decode specialized medical terminology.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `performed` -> `done`**

- status: `attributed`
- log p full -0.3331, empty -0.4300
- masks scored: 18/18 (+4 top-k)
- ranked sources:
    - `+0.214` [wiktionary] performed: When you perform something, you do it.
    - `+0.185` [nih] digital rectal examination: An examination in which a doctor inserts a lubricated, gloved finger into the rect
    - `+0.012` [wiktionary] masses: The masses are the regular people, not those in power.
    - `-0.083` [wiktionary] masses: A measure of how much material is in something.

- rationale: The original term simply means to carry out a task, and replacing it with "done" keeps that practical idea in plain language. Word frequency increases from Zipf 4.68 to 5.58, while the syllable count drops from 2 to 1. Patients can now easily understand the medical action without wrestling with clinical terminology.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `masses` -> `lumps`**

- status: `attributed`
- log p full -0.3919, empty -0.2508
- masks scored: 18/18 (+4 top-k)
- ranked sources:
    - `+0.276` [nih] digital rectal examination: An examination in which a doctor inserts a lubricated, gloved finger into the rect
    - `-0.082` [wiktionary] performed: When you perform something, you do it.
    - `-0.247` [wiktionary] masses: A measure of how much material is in something.
    - `-0.271` [wiktionary] masses: The masses are the regular people, not those in power.

- rationale: The original term refers to abnormal collections of tissue in the body, and switching to "lumps" preserves that exact idea while using everyday language. Phrase frequency increases from Zipf 3.94 to 3.19, while the syllable count drops from two to one. You can now easily grasp what the doctor is describing without needing to memorize clinical terminology.
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

**output:** He then had seizures and weakness on one side of his body, went to the hospital, developed C-diff, and is now in a nursing home.

| metric | value |
|---|---:|
| bertscore_f1 | 0.620 |
| coleman_liau | 5.98 |
| coleman_liau_drop | 4.29 |
| copy_jargon_rate | 0.667 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 10.21 |
| fkgl_drop | 1.02 |
| fre | 66.4 |
| fre_gain | 12.6 |
| human_edit_recall | 0.333 |
| length_ratio | 0.90 |
| n_words | 26.0 |
| nli_completeness | 0.806 |
| nli_faithfulness | 0.944 |
| replacement_f1 | 0.500 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.750 |
| sari | 31.07 |
| smog | 11.21 |
| smog_drop | 3.35 |
| temporality_preservation | 1.000 |

### Stage 4 - arm `termonly`

**output:** He then had a problem with fits, weakness on one side, has been to the hospital, developed a dangerous gut infection, and is in the nursing home currently.

| metric | value |
|---|---:|
| bertscore_f1 | 0.953 |
| coleman_liau | 8.62 |
| coleman_liau_drop | 1.65 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.667 |
| fkgl | 12.61 |
| fkgl_drop | -1.38 |
| fre | 54.5 |
| fre_gain | 0.8 |
| human_edit_recall | 1.000 |
| length_ratio | 0.97 |
| n_words | 28.0 |
| nli_completeness | 0.271 |
| nli_faithfulness | 0.802 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 87.13 |
| smog | 15.90 |
| smog_drop | -1.35 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `seizures` -> `fits` | replace | - | - | - | - | - | - | - |
| `hemiparesis` -> `weakness on one side` | replace | - | - | - | - | - | - | - |
| `C-diff` -> `a dangerous gut infection` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** He then had a problem with sudden jerky movements, one-sided weakness, has been to the hospital, developed a gut infection, and is in the nursing home currently.

| metric | value |
|---|---:|
| bertscore_f1 | 0.768 |
| coleman_liau | 10.81 |
| coleman_liau_drop | -0.54 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 13.30 |
| fkgl_drop | -2.07 |
| fre | 47.8 |
| fre_gain | -5.9 |
| human_edit_recall | 1.000 |
| length_ratio | 0.97 |
| n_words | 28.0 |
| nli_completeness | 0.442 |
| nli_faithfulness | 0.898 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 70.83 |
| smog | 14.55 |
| smog_drop | 0.00 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `seizures` -> `sudden jerky movements` | replace | attributed | 5.633 | 5.728 | 0.871 | 0.927 | 5.760 | 6.002062587000001 |
| `hemiparesis` -> `one-sided weakness` | replace | attributed | -1.204 | -1.263 | 0.906 | 0.937 | 0.189 | -0.1598045740000007 |
| `C-diff` -> `a gut infection` | replace | attributed | 2.139 | 3.128 | 0.895 | 0.867 | 3.549 | 3.8767256160000003 |

**edit `seizures` -> `sudden jerky movements`**

- status: `attributed`
- log p full -2.4063, empty -8.0398
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+5.884` [readme] seizures: Seizures are when the brain has strange electrical activity that may make someone lose consciousness
    - `+0.124` [readme] Seizures: Seizures are when the brain has sudden abnormal activity that can lead to loss of consciousness and 
    - `+0.104` [nih] Clostridium difficile: A type of bacterium found in human and animal waste. Clostridium difficile is a common 

- rationale: The readme notes that seizures involve strange brain activity that can cause jerky movements, so "sudden jerky movements" preserves that key physical symptom in everyday language. Phrase frequency shifts from Zipf 3.59 to 3.06, while syllable count rises from 2 to 6. Patients can now grasp the visible symptoms without needing to decode specialized clinical jargon.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `hemiparesis` -> `one-sided weakness`**

- status: `attributed`
- log p full -3.7377, empty -2.5336
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+0.257` [readme] hemiparesis: Weakness on one side of the body.
    - `+0.068` [nih] Clostridium difficile: A type of bacterium found in human and animal waste. Clostridium difficile is a common 
    - `+0.060` [wiktionary] seizures: If someone seizes (takes) something from someone by force, or arrests someone, it is a seizure.

- rationale: Hemiparesis refers to a reduced ability to move or feel on just one side of the body, so "one-sided weakness" preserves that exact physical description using everyday language. Phrase frequency increases from Zipf 1.49 to 3.75, while syllable count rises from 3 to 4. Patients can now grasp the core physical symptom without needing to decode a specialized clinical label.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `C-diff` -> `a gut infection`**

- status: `attributed`
- log p full -0.4199, empty -2.5586
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+3.593` [readme] Clostridium difficile colitis: A type of gut infection that causes symptoms like fever, diarrhea, and cramps.
    - `+0.045` [readme] seizures: Seizures are when the brain has strange electrical activity that may make someone lose consciousness

- rationale: The readme describes C-diff as a type of gut infection that causes symptoms like fever, diarrhea, and cramps, so replacing it with "a gut infection" preserves that core medical reality in everyday language. The syllable count increases from 2 to 5, reflecting a modest shift in reading complexity. Patients can now grasp the nature of the illness and its common symptoms without needing to decode a clinical abbreviation.
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

**output:** He has been using a continuous positive airway pressure machine for several months, and he is coming back for a follow-up visit to see how well the treatment is helping him.

| metric | value |
|---|---:|
| bertscore_f1 | 0.660 |
| coleman_liau | 9.44 |
| coleman_liau_drop | 3.21 |
| copy_jargon_rate | 0.833 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 14.39 |
| fkgl_drop | -2.09 |
| fre | 47.1 |
| fre_gain | 1.0 |
| human_edit_recall | 0.167 |
| length_ratio | 1.28 |
| n_words | 32.0 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.950 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 0.286 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.600 |
| sari | 50.67 |
| smog | 13.02 |
| smog_drop | 0.00 |
| temporality_preservation | 0.000 |

### Stage 4 - arm `termonly`

**output:** He has been on a mask that blows air now for several months, and returns for a check-up to review his response to treatment.

| metric | value |
|---|---:|
| bertscore_f1 | 0.769 |
| coleman_liau | 6.65 |
| coleman_liau_drop | 6.00 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.167 |
| fkgl | 8.52 |
| fkgl_drop | 3.78 |
| fre | 76.7 |
| fre_gain | 30.7 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 25.0 |
| nli_completeness | 0.899 |
| nli_faithfulness | 0.624 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 62.84 |
| smog | 3.13 |
| smog_drop | 9.89 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `continuous positive airway pressure` -> `a mask that blows air` | replace | - | - | - | - | - | - | - |
| `followup` -> `a check-up` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** He has been on steady air pressure now for several months, and returns for a checkup to review his response to treatment.

| metric | value |
|---|---:|
| bertscore_f1 | 0.755 |
| coleman_liau | 8.69 |
| coleman_liau_drop | 3.95 |
| copy_jargon_rate | 0.167 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.200 |
| fkgl | 9.08 |
| fkgl_drop | 3.22 |
| fre | 69.1 |
| fre_gain | 23.1 |
| human_edit_recall | 0.833 |
| length_ratio | 0.88 |
| n_words | 22.0 |
| nli_completeness | 0.975 |
| nli_faithfulness | 0.990 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 58.67 |
| smog | 3.13 |
| smog_drop | 9.89 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `continuous positive airway pressure` -> `steady air pressure` | replace | attributed | 1.238 | 1.238 | 0.763 | 0.810 | 0.112 | 1.1481413200000006 |
| `followup` -> `a checkup` | replace | attributed | 0.191 | 0.385 | 0.640 | 0.875 | 0.383 | 0.03236014500000006 |

**edit `continuous positive airway pressure` -> `steady air pressure`**

- status: `attributed`
- log p full -9.8402, empty -11.0780
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.876` [wiktionary] airway: The airway in our body refers to the trachea.
    - `+0.764` [wiktionary] pressure: In science, pressure is force applied over an area.
    - `+0.486` [readme] continuous: Continuous means something that never stops or has interruptions.
    - `+0.201` [wiktionary] continuous: Something that is continuous happens without stopping.
    - `+0.048` [wiktionary] positive: If you are positive about something, you are sure that you are not mistaken.

- rationale: The glossary explains that the airway in our body refers to the trachea, so replacing "continuous positive airway pressure" with "steady air pressure" preserves that core idea in everyday language. Phrase frequency increases from Zipf 3.14 to 4.20, while age of acquisition falls from 11.39 to 8.95. You can now understand how the device supports your breathing without first learning a complicated medical name.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `followup` -> `a checkup`**

- status: `attributed`
- log p full -0.5929, empty -0.7839
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.533` [readme] followup: Going back to your doctor for a checkup or follow-up appointment.
    - `+0.150` [wiktionary] positive: If something is positive, it is good, happy, or wanted.
    - `+0.026` [wiktionary] airway: The airway in our body refers to the trachea.

- rationale: The original term refers to a scheduled visit to review your health after an initial treatment, and swapping it for "a checkup" preserves that idea by using everyday language to describe a routine medical review. Phrase frequency increases from Zipf 2.87 to 2.88, meaning the higher value indicates a more common and easier-to-process term. You can now grasp the purpose of the appointment without needing to decode clinical jargon.
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

**output:** The patient should take small bites and small sips to help decrease the risk of swallowing food or liquid into the lungs or going down the wrong way.

| metric | value |
|---|---:|
| bertscore_f1 | 0.662 |
| coleman_liau | 8.21 |
| coleman_liau_drop | 1.42 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 10.08 |
| fkgl_drop | -1.61 |
| fre | 72.7 |
| fre_gain | 6.3 |
| human_edit_recall | 1.000 |
| length_ratio | 0.93 |
| n_words | 28.0 |
| nli_completeness | 0.779 |
| nli_faithfulness | 0.765 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 54.78 |
| severity_downgrade | 0.000 |
| severity_preservation | 1.000 |
| severity_tier_input | 1.000 |
| severity_tier_output | 1.000 |
| smog | 8.84 |
| smog_drop | 2.37 |

### Stage 4 - arm `termonly`

**output:** The patient should take small bites and small sips to help decrease the risk of swallowing into the lungs and going down the wrong tube.

| metric | value |
|---|---:|
| bertscore_f1 | 0.683 |
| coleman_liau | 8.77 |
| coleman_liau_drop | 0.85 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 8.79 |
| fkgl_drop | -0.32 |
| fre | 76.6 |
| fre_gain | 10.2 |
| human_edit_recall | 1.000 |
| length_ratio | 0.83 |
| n_words | 25.0 |
| nli_completeness | 0.799 |
| nli_faithfulness | 0.533 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 53.41 |
| severity_downgrade | 0.000 |
| severity_preservation | 1.000 |
| severity_tier_input | 1.000 |
| severity_tier_output | 1.000 |
| smog | 8.84 |
| smog_drop | 2.37 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `aspiration` -> `swallowing into the lungs` | replace | - | - | - | - | - | - | - |
| `penetration` -> `going down the wrong tube` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** The patient to take small bite and small sips to help decrease the risk of breathing food into the lungs and going down the wrong way.

| metric | value |
|---|---:|
| bertscore_f1 | 0.659 |
| coleman_liau | 7.15 |
| coleman_liau_drop | 2.47 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 8.62 |
| fkgl_drop | -0.14 |
| fre | 79.6 |
| fre_gain | 13.2 |
| human_edit_recall | 1.000 |
| length_ratio | 0.87 |
| n_words | 26.0 |
| nli_completeness | 0.722 |
| nli_faithfulness | 0.283 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 72.25 |
| severity_downgrade | 0.000 |
| severity_preservation | 1.000 |
| severity_tier_input | 1.000 |
| severity_tier_output | 1.000 |
| smog | 3.13 |
| smog_drop | 8.08 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `aspiration` -> `breathing food into the lungs` | replace | attributed | 4.981 | 4.990 | 0.835 | 0.827 | 3.379 | 2.804173616699999 |
| `penetration` -> `going down the wrong way` | replace | attributed | -3.169 | -3.174 | 0.736 | 0.757 | 0.462 | 0.9794104299999997 |

**edit `aspiration` -> `breathing food into the lungs`**

- status: `attributed`
- log p full -4.7155, empty -9.6968
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+4.740` [readme] aspiration: Breathing food or liquid into your lungs by mistake.
    - `+1.361` [nih] aspiration: Removal of fluid or tissue through a needle. Also, the accidental breathing in of food or fluid in
    - `+0.110` [readme] aspiration: Breathing in food or liquid by mistake.
    - `+0.095` [iowa] ASPIRATION: fluid entering the lungs, such as after vomiting
    - `+0.034` [wiktionary] penetration: Penetration is the penis being inserted into the vagina or another part of the body during sex.

- rationale: The glossary defines aspiration as breathing food or liquid into the lungs by mistake, so "breathing food into the lungs" keeps that core idea in plain language. Phrase frequency rises from Zipf 3.30 to 3.78, and age of acquisition drops from 11.47 to 6.52. Patients can now grasp the actual swallowing problem without needing to know the medical label.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `penetration` -> `going down the wrong way`**

- status: `attributed`
- log p full -8.2646, empty -5.0961
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.462` [iowa] ASPIRATION: fluid entering the lungs, such as after vomiting
    - `-0.180` [wiktionary] penetration: Penetration is the action of penetrating into something.
    - `-0.280` [readme] aspiration: Breathing in food or liquid by mistake.
    - `-0.932` [wiktionary] penetration: Penetration is the penis being inserted into the vagina or another part of the body during sex.

- rationale: "Penetration" refers to something moving deeply into a space or tissue, and "going down the wrong way" captures that same directional movement in everyday language. Phrase frequency increases from Zipf 3.71 to 5.12, meaning it is higher, more common, and easier, while age of acquisition decreases from 11.05 to 5.41, meaning it is lower, learned younger, and easier. You can now picture exactly how the procedure moves through your body without getting stuck on unfamiliar clinical jargon.
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

**output:** The patient was woken up and had the tube removed from their airway and moved to the recovery room in good condition.

| metric | value |
|---|---:|
| bertscore_f1 | 0.817 |
| coleman_liau | 7.90 |
| coleman_liau_drop | 5.65 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.667 |
| fkgl | 9.08 |
| fkgl_drop | 3.21 |
| fre | 69.1 |
| fre_gain | 35.5 |
| human_edit_recall | 1.000 |
| length_ratio | 1.10 |
| n_words | 22.0 |
| nli_completeness | 0.988 |
| nli_faithfulness | 0.977 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 47.71 |
| smog | 11.21 |
| smog_drop | 4.70 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `awakened` -> `woken up` | replace | - | - | - | - | - | - | - |
| `extubated` -> `had the tube removed from their airway` | replace | - | - | - | - | - | - | - |
| `satisfactory` -> `good` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** The patient was woken up and had the breathing tube removed and moved to the recovery room in good condition.

| metric | value |
|---|---:|
| bertscore_f1 | 0.772 |
| coleman_liau | 8.53 |
| coleman_liau_drop | 5.02 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.667 |
| fkgl | 8.73 |
| fkgl_drop | 3.56 |
| fre | 68.1 |
| fre_gain | 34.4 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 20.0 |
| nli_completeness | 0.988 |
| nli_faithfulness | 0.984 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 42.49 |
| smog | 11.21 |
| smog_drop | 4.70 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `awakened` -> `woken up` | replace | attributed | 0.056 | 0.085 | - | 0.675 | 0.038 | 0.0286954589999997 |
| `extubated` -> `had the breathing tube removed` | replace | attributed | 1.204 | 1.380 | - | 0.639 | 0.130 | 0.09426779000000018 |
| `satisfactory` -> `good` | replace | attributed | 0.001 | 0.003 | - | 0.932 | 0.684 | 0.7417077799999999 |

**edit `awakened` -> `woken up`**

- status: `attributed`
- log p full -1.0590, empty -1.1152
- masks scored: 34/34 (+4 top-k)
- ranked sources:
    - `+0.038` [readme] extubated: Taking out a tube used for breathing.
    - `-0.027` [wiktionary] awakened: If you awaken somebody, they stop sleeping because of something you do.

- rationale: The original term describes the act of regaining consciousness, and "woken up" keeps that core idea in everyday language. Phrase frequency increases from Zipf 3.30 to 3.37, while syllable count stays at 3. The reader can now grasp the basic idea of regaining awareness without needing a more formal term.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `extubated` -> `had the breathing tube removed`**

- status: `attributed`
- log p full -1.5343, empty -2.7382
- masks scored: 34/34 (+4 top-k)
- ranked sources:
    - `+0.764` [readme] extubated: Taking out a tube used for breathing.
    - `+0.634` [readme] extubated: Not having a breathing tube anymore.

- rationale: The original term describes the removal of a breathing tube from a patient's airway, and the replacement phrase keeps that core action in plain language. Phrase frequency increases from Zipf 1.26 to 3.95, while syllables increase from 4 to 7. Patients can now understand the medical procedure without needing to know the specialized term.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `satisfactory` -> `good`**

- status: `attributed`
- log p full -0.5629, empty -0.5641
- masks scored: 34/34 (+4 top-k)
- ranked sources:
    - `+0.787` [wiktionary] satisfactory: If something is satisfactory, it is good enough.
    - `+0.103` [wiktionary] awakened: If you awaken somebody, they stop sleeping because of something you do.
    - `-0.014` [readme] extubated: Taking out a tube used for breathing.
    - `-0.141` [readme] extubated: Not having a breathing tube anymore.
    - `-0.776` [michigan] satisfactory: When something is okay or good.

- rationale: The original term describes a state of being pleased or content, so "good" keeps that positive feeling in plain language. Word frequency increases from Zipf 3.57 to 6.12, while age of acquisition falls from 8.84 to 3.55. Patients can now grasp the positive outcome without needing to know the exact word.
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

**output:** Physical examination: General: The patient was asleep, but it was easy to wake them up.

| metric | value |
|---|---:|
| bertscore_f1 | 0.588 |
| coleman_liau | 8.91 |
| coleman_liau_drop | 7.71 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 10.71 |
| fkgl_drop | 4.74 |
| fre | 45.0 |
| fre_gain | 42.9 |
| human_edit_recall | 1.000 |
| length_ratio | 1.88 |
| n_words | 15.0 |
| nli_completeness | 0.974 |
| nli_faithfulness | 0.984 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 39.42 |
| smog | 13.02 |
| smog_drop | 1.53 |

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
| `aroused` -> `woke up` | replace | attributed | 0.274 | 0.391 | - | - | - | 0.2770041750000003 |

**edit `aroused` -> `woke up`**

- status: `attributed`
- log p full -1.0798, empty -1.3542
- masks scored: 4/4 (+1 top-k)
- ranked sources:
    - `+0.329` [wiktionary] aroused: If something arouses a feeling or emotion, it causes that feeling or emotion.

- rationale: The original term describes a state of heightened alertness or readiness, and "woke up" captures that shift from rest to active awareness in everyday language. Phrase frequency increases from Zipf 3.35 to 4.22, while syllable count remains at 2. The reader can now grasp the transition from sleep to alertness without needing a clinical description.
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

**output:** He needs to see the doctor again in about 10 days for a check-up and to get a prescription for his AFOs, which he will need for up to 6 months.

| metric | value |
|---|---:|
| bertscore_f1 | 0.556 |
| coleman_liau | 3.83 |
| coleman_liau_drop | 2.88 |
| copy_jargon_rate | 1.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 10.58 |
| fkgl_drop | 0.30 |
| fre | 74.4 |
| fre_gain | 11.1 |
| human_edit_recall | 0.000 |
| length_ratio | 1.14 |
| n_words | 32.0 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.980 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.600 |
| sari | 26.71 |
| smog | 8.84 |
| smog_drop | 4.18 |

### Stage 4 - arm `termonly`

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
| `approximately` -> `about` | replace | - | - | - | - | - | - | - |
| `AFOs` -> `ankle and foot braces` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

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
| `approximately` -> `about` | replace | attributed | -0.024 | -0.107 | - | 0.927 | 0.816 | 0.5386316299999999 |
| `AFOs` -> `ankle-foot braces` | replace | attributed | 5.228 | 5.805 | - | 0.833 | 1.740 | 1.42802983 |

**edit `approximately` -> `about`**

- status: `attributed`
- log p full -0.2639, empty -0.2401
- masks scored: 10/10 (+2 top-k)
- ranked sources:
    - `+0.816` [justplainclear] AFO: Also known as: ankle-foot orthosis, walking boot A brace that supports your ankle or foot An AFO is a bra
    - `-0.906` [wiktionary] approximately: Approximately is close to, but not exactly.

- rationale: "Approximately" signals a rough estimate rather than a precise value, and replacing it with "about" keeps that same practical meaning in plain language. Word frequency increases from Zipf 4.64 to 6.40, while the syllable count drops from 5 to 2, making the phrasing more common and easier to read. Patients can now understand the intended measurement without stumbling over unnecessary linguistic complexity.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `AFOs` -> `ankle-foot braces`**

- status: `attributed`
- log p full -0.8220, empty -6.0502
- masks scored: 10/10 (+2 top-k)
- ranked sources:
    - `+3.865` [justplainclear] AFO: Also known as: ankle-foot orthosis, walking boot A brace that supports your ankle or foot An AFO is a bra
    - `+2.125` [dorland] AFOs: ankle-foot orthosis
    - `-0.151` [wiktionary] approximately: Approximately is close to, but not exactly.

- rationale: AFOs are supportive devices that stabilize the ankle and foot, so "ankle-foot braces" preserves that exact stabilizing function in everyday language. Phrase frequency increases from Zipf 1.36 to 3.35, making the replacement more common and easier to encounter, while the syllable count rises from 1 to 5. Patients can immediately grasp the supportive purpose of the device without needing to decode a medical acronym.
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

**output:** Urinary and reproductive system: The patient's outside genital organs looked normal.

| metric | value |
|---|---:|
| bertscore_f1 | 0.356 |
| coleman_liau | 18.95 |
| coleman_liau_drop | -1.47 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 14.45 |
| fkgl_drop | -0.37 |
| fre | 11.1 |
| fre_gain | 2.7 |
| human_edit_recall | 1.000 |
| length_ratio | 1.50 |
| n_words | 12.0 |
| nli_completeness | 0.969 |
| nli_faithfulness | 0.719 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.250 |
| sari | 25.91 |
| smog | 13.02 |
| smog_drop | 0.00 |

### Stage 4 - arm `termonly`

**output:** Urinary and reproductive: The outside reproductive parts appeared normal.

| metric | value |
|---|---:|
| bertscore_f1 | 0.294 |
| coleman_liau | 21.51 |
| coleman_liau_drop | -4.04 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.750 |
| fkgl | 15.45 |
| fkgl_drop | -1.37 |
| fre | 0.3 |
| fre_gain | -8.1 |
| human_edit_recall | 1.000 |
| length_ratio | 1.12 |
| n_words | 9.0 |
| nli_completeness | 0.911 |
| nli_faithfulness | 0.708 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 28.23 |
| smog | 13.02 |
| smog_drop | 0.00 |

annotation backend `novita`, 0 edits kept


### Stage 4 - arm `grounded`

**output:** Body parts for peeing and sex : The outside sex parts appeared to be normal.

| metric | value |
|---|---:|
| bertscore_f1 | 0.333 |
| coleman_liau | 6.94 |
| coleman_liau_drop | 10.53 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.750 |
| fkgl | 5.88 |
| fkgl_drop | 8.20 |
| fre | 77.8 |
| fre_gain | 69.5 |
| human_edit_recall | 1.000 |
| length_ratio | 1.75 |
| n_words | 14.0 |
| nli_completeness | 0.952 |
| nli_faithfulness | 0.773 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 66.67 |
| smog | 3.13 |
| smog_drop | 9.89 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `external genitalia` -> `outside sex parts` | replace | attributed | 1.296 | 1.346 | 0.886 | 0.920 | 1.522 | 1.9724240000000006 |

**edit `external genitalia` -> `outside sex parts`**

- status: `attributed`
- log p full -2.7140, empty -4.0102
- masks scored: 66/66 (+2 top-k)
- ranked sources:
    - `+2.092` [wiktionary] genitalia: Genitalia are the body parts used for sex and reproduction, especially the parts on the outside of 
    - `+0.570` [readme] Genitourinary: Important body parts involved in sex and peeing.
    - `+0.456` [readme] genitourinary: Body parts used for peeing and sex stuff.
    - `-0.028` [iowa] EXTERNAL: outside the body

- rationale: The source describes genitalia as the body parts used for sex and reproduction, especially the parts on the outside of the body, so "outside sex parts" keeps that core idea in plain language. Phrase frequency increases from Zipf 3.08 to 4.70, while age of acquisition falls from 11.84 to 9.79. Patients can understand the basic anatomy without first knowing the clinical name.
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

**output:** She is day 21 after surgery to open her abdomen and check how far the ovarian cancer has spread.

| metric | value |
|---|---:|
| bertscore_f1 | 0.627 |
| coleman_liau | 6.15 |
| coleman_liau_drop | 4.78 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.750 |
| fkgl | 9.83 |
| fkgl_drop | 2.34 |
| fre | 58.4 |
| fre_gain | 27.5 |
| human_edit_recall | 1.000 |
| length_ratio | 1.12 |
| n_words | 19.0 |
| nli_completeness | 0.682 |
| nli_faithfulness | 0.696 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 49.63 |
| smog | 13.02 |
| smog_drop | 0.00 |

### Stage 4 - arm `termonly`

**output:** She is after surgery day 21 of a belly surgery to check how far the cancer spread.

| metric | value |
|---|---:|
| bertscore_f1 | 0.554 |
| coleman_liau | 4.64 |
| coleman_liau_drop | 6.29 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.600 |
| fkgl | 7.70 |
| fkgl_drop | 4.47 |
| fre | 70.1 |
| fre_gain | 39.2 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 17.0 |
| nli_completeness | 0.154 |
| nli_faithfulness | 0.140 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 41.30 |
| smog | 11.21 |
| smog_drop | 1.82 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `postop` -> `after surgery` | replace | - | - | - | - | - | - | - |
| `exploratory laparotomy` -> `belly surgery` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** She is after surgery day 21 of a surgery to check her belly with checking how far the ovarian cancer spread.

| metric | value |
|---|---:|
| bertscore_f1 | 0.539 |
| coleman_liau | 6.82 |
| coleman_liau_drop | 4.10 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.750 |
| fkgl | 10.58 |
| fkgl_drop | 1.59 |
| fre | 56.6 |
| fre_gain | 25.7 |
| human_edit_recall | 1.000 |
| length_ratio | 1.24 |
| n_words | 21.0 |
| nli_completeness | 0.536 |
| nli_faithfulness | 0.624 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 46.41 |
| smog | 13.02 |
| smog_drop | 0.00 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `postop` -> `after surgery` | replace | attributed | 4.784 | 4.812 | 0.772 | 0.800 | 1.059 | 0.27998403999999955 |
| `exploratory laparotomy` -> `surgery to check her belly` | replace | attributed | 7.965 | 8.020 | 0.838 | 0.835 | 1.595 | 1.1966795579999996 |
| `ovarian cancer staging` -> `checking how far the ovarian cancer spread` | replace | attributed | 10.433 | 10.433 | 0.922 | 0.927 | 1.284 | 6.7420747100000025 |

**edit `postop` -> `after surgery`**

- status: `attributed`
- log p full -3.5804, empty -8.3646
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+2.492` [readme] postop: After surgery.
    - `+1.433` [readme] PostOP: PostOP means after surgery.
    - `+0.561` [readme] exploratory laparotomy: Surgery to check for problems in your belly.
    - `+0.380` [readme] Exploratory laparotomy: Exploratory laparotomy: Surgery to check the organs in the belly for issues.
    - `+0.346` [nih] ovarian: Having to do with the ovaries, the female reproductive glands in which the ova (eggs) are formed. The

- rationale: The glossary defines "postop" as "after surgery," so "after surgery" keeps that meaning in plain words. Phrase frequency increases from Zipf 1.53 to 4.62. Patients can understand the timing of the procedure without knowing the medical shorthand.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `exploratory laparotomy` -> `surgery to check her belly`**

- status: `attributed`
- log p full -2.9292, empty -10.8944
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+6.327` [readme] exploratory laparotomy: Surgery to check for problems in your belly.
    - `+4.732` [readme] Exploratory laparotomy: Exploratory laparotomy: Surgery to check the organs in the belly for issues.
    - `+1.018` [readme] PostOP: PostOP means after surgery.
    - `+0.714` [nih] ovarian: Having to do with the ovaries, the female reproductive glands in which the ova (eggs) are formed. The

- rationale: The readme explains that an exploratory laparotomy is simply surgery to check for problems in your belly, so "surgery to check her belly" preserves that core idea using everyday language. Phrase frequency increases from Zipf 2.01 to 3.97 (higher = more common = easier), while age of acquisition decreases from 12.89 to 7.68 (lower = learned younger = easier). You can now clearly picture what the doctor plans to do without needing to memorize a complex medical label.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `ovarian cancer staging` -> `checking how far the ovarian cancer spread`**

- status: `attributed`
- log p full -12.0550, empty -22.4876
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+5.357` [readme] cancer staging: Determining the extent to which cancer has spread in the body based on a numerical scale.
    - `+4.073` [readme] exploratory laparotomy: Surgery to check for problems in your belly.
    - `+0.425` [nih] ovarian: Having to do with the ovaries, the female reproductive glands in which the ova (eggs) are formed. The
    - `+0.357` [readme] PostOP: PostOP means after surgery.

- rationale: The readme explains that staging determines the extent to which cancer has spread in the body based on a numerical scale, so "checking how far the ovarian cancer spread" preserves that core idea in everyday language. Phrase frequency increases from Zipf 3.24 to 3.38, while age of acquisition remains steady at 14.44. You can now grasp the practical goal of the evaluation without needing to memorize clinical terminology.
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

**output:** Prescription for a steroid medicine as part of his cancer treatment has been given to him.

| metric | value |
|---|---:|
| bertscore_f1 | 0.922 |
| coleman_liau | 9.18 |
| coleman_liau_drop | 1.75 |
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
| nli_completeness | 0.036 |
| nli_faithfulness | 0.388 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 84.38 |
| smog | 11.21 |
| smog_drop | 0.00 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `prednisone` -> `a steroid medicine` | replace | - | - | - | - | - | - | - |
| `chemotherapy` -> `cancer treatment` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Prescription for a medicine that lowers inflammation as part of his treatment with cancer drugs has been given to him.

| metric | value |
|---|---:|
| bertscore_f1 | 0.764 |
| coleman_liau | 11.14 |
| coleman_liau_drop | -0.22 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| drug_preservation | 0.000 |
| fkgl | 10.50 |
| fkgl_drop | -1.96 |
| fre | 55.4 |
| fre_gain | -1.6 |
| human_edit_recall | 1.000 |
| length_ratio | 1.33 |
| n_words | 20.0 |
| nli_completeness | 0.003 |
| nli_faithfulness | 0.676 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 69.23 |
| smog | 13.02 |
| smog_drop | -1.82 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `prednisone` -> `a medicine that lowers inflammation` | replace | attributed | 4.660 | 4.700 | 0.868 | 0.853 | 2.673 | 2.511007619999999 |
| `chemotherapy` -> `treatment with cancer drugs` | replace | attributed | -1.756 | -1.757 | 0.921 | 0.970 | 0.364 | 1.995730344 |

**edit `prednisone` -> `a medicine that lowers inflammation`**

- status: `attributed`
- log p full -3.2382, empty -7.8984
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+4.679` [readme] Prednisone: A medication that lowers the body's immune response and inflammation.
    - `+2.006` [nih] prednisone: A drug used to reduce inflammation and lower the body’s immune response.  It is used with other dr
    - `+0.915` [readme] prednisone: A medication that helps lower the body's immune system reactions.
    - `+0.558` [iowa] CHEMOTHERAPY: treatment of disease, usually cancer, by chemical agents
    - `+0.513` [readme] CHEMOTHERAPY: Using drugs to treat diseases like cancer.

- rationale: The glossary defines prednisone as a medication that lowers the body's immune response and inflammation, so "a medicine that lowers inflammation" keeps that core idea in plain language. Phrase frequency rises from Zipf 2.56 to 3.19, and age of acquisition drops from 17.17 to 11.00. Patients can now grasp the drug's purpose without needing to know its specific name.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `chemotherapy` -> `treatment with cancer drugs`**

- status: `attributed`
- log p full -8.8182, empty -7.0618
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+1.772` [readme] chemotherapy: Using drugs to treat cancer or other diseases.
    - `+1.408` [readme] CHEMOTHERAPY: Using drugs to treat diseases like cancer.
    - `+0.150` [nih] prednisone: A drug used to reduce inflammation and lower the body’s immune response.  It is used with other dr
    - `+0.013` [readme] prednisone: A medication that helps lower the body's immune system reactions.

- rationale: Chemotherapy refers to using powerful medications to attack rapidly dividing cells, so "treatment with cancer drugs" preserves that core idea by describing the exact purpose and method in everyday language. Phrase frequency increases from Zipf 3.56 to 4.41, while age of acquisition falls from 12.53 to 8.39. Patients can now grasp the practical purpose of the procedure without needing to memorize a specialized medical label.
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

**output:** Light was used to stimulate the patient's eyes, but no clear eye movements that followed the light were seen.

| metric | value |
|---|---:|
| bertscore_f1 | 0.523 |
| coleman_liau | 9.51 |
| coleman_liau_drop | 4.69 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.167 |
| fkgl | 6.73 |
| fkgl_drop | 2.36 |
| fre | 80.7 |
| fre_gain | 31.1 |
| human_edit_recall | 1.000 |
| length_ratio | 1.18 |
| n_words | 20.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.964 |
| nli_faithfulness | 0.632 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.200 |
| sari | 30.82 |
| smog | 8.84 |
| smog_drop | 0.00 |

### Stage 4 - arm `termonly`

**output:** Flashing lights were used, but no obvious brain wave syncing was seen.

| metric | value |
|---|---:|
| bertscore_f1 | 0.520 |
| coleman_liau | 9.28 |
| coleman_liau_drop | 4.92 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 4.82 |
| fkgl_drop | 4.26 |
| fre | 81.9 |
| fre_gain | 32.3 |
| human_edit_recall | 1.000 |
| length_ratio | 0.71 |
| n_words | 12.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.904 |
| nli_faithfulness | 0.452 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.200 |
| sari | 26.37 |
| smog | 8.84 |
| smog_drop | 0.00 |

annotation backend `novita`, 0 edits kept


### Stage 4 - arm `grounded`

**output:** Light stimulation was performed, but no clear light reaction was seen.

| metric | value |
|---|---:|
| bertscore_f1 | 0.742 |
| coleman_liau | 12.09 |
| coleman_liau_drop | 2.11 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.200 |
| fkgl | 6.94 |
| fkgl_drop | 2.15 |
| fre | 64.9 |
| fre_gain | 15.4 |
| human_edit_recall | 1.000 |
| length_ratio | 0.65 |
| n_words | 11.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.903 |
| nli_faithfulness | 0.826 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 56.89 |
| smog | 11.21 |
| smog_drop | -2.37 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `Photic stimulation` -> `stimulation` | replace | attributed | 1.727 | 1.731 | 0.536 | 0.844 | 0.268 | 0.6309745499999995 |
| `photic driving` -> `light reaction` | replace | attributed | -1.153 | -1.168 | 0.823 | 0.939 | 0.410 | 0.309114000000001 |

**edit `Photic stimulation` -> `stimulation`**

- status: `attributed`
- log p full -5.2414, empty -6.9681
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.606` [wiktionary] stimulation: Stimulation is an action that encourages something to develop or become more active.
    - `+0.338` [readme] stimulation: Making something more active or alert.
    - `+0.320` [dictionary] Photic (a.): Relating to the production of light by the lower animals.
    - `+0.085` [dictionary] Photic (a.): Relating to the production of light by the lower animals.
    - `+0.013` [wiktionary] driving: If something is driving, it is moving quickly and strongly.

- rationale: The glossary source explains that photic stimulation is an action that encourages something to develop or become more active, so "stimulation" carries that exact meaning in plain words. Phrase frequency increases from Zipf 1.80 to 3.70, while age of acquisition remains at 8.63, making the replacement significantly more common and easier to learn. Patients can now understand the basic treatment goal without first learning a specialized diagnostic name.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `photic driving` -> `light reaction`**

- status: `attributed`
- log p full -4.9538, empty -3.8012
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.577` [dictionary] Photic (a.): Relating to the production of light by the lower animals.
    - `+0.167` [dictionary] Clear-cut (a.): Having a sharp, distinct outline, like that of a cameo.
    - `+0.141` [dictionary] Photic (a.): Relating to the production of light by the lower animals.

- rationale: "Photic driving" describes how your eyes automatically adjust their focus when exposed to changing brightness, and replacing it with "light reaction" preserves that exact idea while using familiar everyday words. Phrase frequency increases from Zipf 1.81 to 4.63, meaning the replacement is more common and easier to process. You can now grasp how your vision naturally responds to brightness without needing to memorize a specialized clinical label.
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
| `myocardial infarctions` -> `heart attacks` | replace | attributed | 0.096 | 0.279 | - | 0.841 | 0.111 | 0.15186794800000003 |

**edit `myocardial infarctions` -> `heart attacks`**

- status: `attributed`
- log p full -0.3741, empty -0.4698
- masks scored: 34/34 (+2 top-k)
- ranked sources:
    - `+0.193` [iowa] MYOCARDIAL INFARCTION: heart attack
    - `+0.082` [justplainclear] myocardial infarction: A heart attack
    - `+0.046` [readme] inferior myocardial infarction: A heart attack caused by a blockage in a blood vessel that affects the lower p
    - `-0.104` [readme] inferior wall myocardial infarction: Heart damage at the bottom of the left ventricle due to a blocked artery.

- rationale: Myocardial infarctions describes the sudden loss of oxygen to heart muscle due to a blocked artery, and replacing it with heart attacks keeps that vital warning intact while speaking in plain English. Phrase frequency increases from Zipf 1.57 to 4.59, which is higher and therefore more common and easier, while age of acquisition decreases from 16.64 to 5.17, which is lower and therefore learned younger and easier. You can now understand the basic warning about blocked blood flow without first memorizing a clinical label.
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

**output:** The patient has 2+ swelling on both arms and legs that leaves a dent when pressed, extending up to the knees.

| metric | value |
|---|---:|
| bertscore_f1 | 0.420 |
| coleman_liau | 6.54 |
| coleman_liau_drop | 2.91 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 6.65 |
| fkgl_drop | 4.58 |
| fre | 84.8 |
| fre_gain | 50.6 |
| human_edit_recall | 1.000 |
| laterality_preservation | 1.000 |
| length_ratio | 0.75 |
| n_words | 21.0 |
| nli_completeness | 0.893 |
| nli_faithfulness | 0.338 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.200 |
| sari | 36.00 |
| smog | 8.84 |
| smog_drop | 4.18 |

### Stage 4 - arm `termonly`

**output:** The patient has swollen legs that leave indentations when pressed, extending to the knees.

| metric | value |
|---|---:|
| bertscore_f1 | 0.431 |
| coleman_liau | 13.16 |
| coleman_liau_drop | -3.70 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.250 |
| fkgl | 7.57 |
| fkgl_drop | 3.66 |
| fre | 65.7 |
| fre_gain | 31.6 |
| human_edit_recall | 1.000 |
| laterality_preservation | 0.000 |
| length_ratio | 0.50 |
| n_words | 14.0 |
| nli_completeness | 0.232 |
| nli_faithfulness | 0.574 |
| number_unit_preservation | 0.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.200 |
| sari | 34.08 |
| smog | 11.21 |
| smog_drop | 1.82 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `bilateral pitting edema` -> `swollen legs that leave indentations when pressed` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** The arms and legs have a swelling that leaves a dent when you press down. It reaches up to the knees on both sides.

| metric | value |
|---|---:|
| bertscore_f1 | 0.387 |
| coleman_liau | 3.48 |
| coleman_liau_drop | 5.97 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 1.87 |
| fkgl_drop | 9.35 |
| fre | 103.0 |
| fre_gain | 68.8 |
| human_edit_recall | 1.000 |
| laterality_preservation | 1.000 |
| length_ratio | 0.86 |
| n_words | 24.0 |
| nli_completeness | 0.376 |
| nli_faithfulness | 0.525 |
| number_unit_preservation | 0.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.200 |
| sari | 35.83 |
| smog | 3.13 |
| smog_drop | 9.89 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `pitting edema` -> `swelling that leaves a dent when you press down` | replace | attributed | 2.524 | 2.524 | 0.761 | 0.937 | 1.254 | 1.644037335000002 |

**edit `pitting edema` -> `swelling that leaves a dent when you press down`**

- status: `attributed`
- log p full -9.9293, empty -12.4530
- masks scored: 66/66 (+2 top-k)
- ranked sources:
    - `+1.695` [readme] pitting edema: Swelling in the body that leaves an indention (pit) when pressed.
    - `+0.440` [thesaurus] bilateral: with both sides considered, two-sided, when both sides get a say, even, balanced

- rationale: The readme defines pitting edema as swelling that leaves an indentation when pressed, so the replacement carries that exact physical description in everyday language. Phrase frequency increases from Zipf 2.67 to 3.35, while age of acquisition falls from 15.07 to 7.33. You can now recognize the exact type of fluid buildup in your tissues without needing to memorize a clinical label.
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

**output:** The questions listed below are usually used to check a donor's mental and social background.

| metric | value |
|---|---:|
| bertscore_f1 | 0.400 |
| coleman_liau | 11.61 |
| coleman_liau_drop | 7.33 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 9.93 |
| fkgl_drop | 4.34 |
| fre | 50.6 |
| fre_gain | 40.0 |
| human_edit_recall | 1.000 |
| length_ratio | 1.07 |
| n_words | 16.0 |
| nli_completeness | 0.967 |
| nli_faithfulness | 0.784 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.800 |
| sari | 16.75 |
| smog | 8.84 |
| smog_drop | 4.18 |

### Stage 4 - arm `termonly`

**output:** The following questions are mostly used in a mental and social donor evaluation.

| metric | value |
|---|---:|
| bertscore_f1 | 0.517 |
| coleman_liau | 11.82 |
| coleman_liau_drop | 7.12 |
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
| nli_completeness | 0.967 |
| nli_faithfulness | 0.824 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 41.06 |
| smog | 11.21 |
| smog_drop | 1.82 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `psychosocial` -> `mental and social` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Following questions are mostly involved in a mental and social donor evaluation.

| metric | value |
|---|---:|
| bertscore_f1 | 0.686 |
| coleman_liau | 14.60 |
| coleman_liau_drop | 4.34 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 12.69 |
| fkgl_drop | 1.58 |
| fre | 25.5 |
| fre_gain | 14.9 |
| human_edit_recall | 1.000 |
| length_ratio | 0.80 |
| n_words | 12.0 |
| nli_completeness | 0.955 |
| nli_faithfulness | 0.842 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 68.52 |
| smog | 11.21 |
| smog_drop | 1.82 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `psychosocial` -> `mental and social` | replace | attributed | 1.159 | 1.209 | - | 1.000 | 3.594 | 2.1339529139999995 |

**edit `psychosocial` -> `mental and social`**

- status: `attributed`
- log p full -2.6598, empty -3.8183
- masks scored: 6/6 (+1 top-k)
- ranked sources:
    - `+2.385` [michigan] psychosocial: Including both the mental and social aspects of disease.
    - `-1.209` [nih] psychosocial: In medicine, having to do with the mental, emotional, social, and spiritual effects of a disease

- rationale: The original term refers to the interconnected ways that a person’s thoughts, emotions, and relationships with others shape their overall well-being, so splitting it into "mental and social" preserves that core idea using everyday language. Phrase frequency increases from Zipf 2.88 to 4.73, while age of acquisition decreases from 15.44 to 10.43, showing that the new phrasing is both more common and learned younger. You can now grasp how your inner thoughts and outside relationships work together to affect your health without needing to memorize a clinical label.
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

**output:** The patient has a slight, fixed plaque buildup in the lower part of the main artery.

| metric | value |
|---|---:|
| bertscore_f1 | 0.307 |
| coleman_liau | 6.64 |
| coleman_liau_drop | 22.68 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 6.14 |
| fkgl_drop | 17.98 |
| fre | 79.6 |
| fre_gain | 148.5 |
| human_edit_recall | 1.000 |
| length_ratio | 0.73 |
| n_words | 16.0 |
| nli_completeness | 0.827 |
| nli_faithfulness | 0.846 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.200 |
| sari | 34.84 |
| severity_downgrade | 0.000 |
| severity_preservation | 1.000 |
| severity_tier_input | 1.000 |
| severity_tier_output | 1.000 |
| smog | 8.84 |
| smog_drop | 5.71 |

### Stage 4 - arm `termonly`

**output:** Mild fixed plaque buildup in the lower main artery.

| metric | value |
|---|---:|
| bertscore_f1 | 0.312 |
| coleman_liau | 7.98 |
| coleman_liau_drop | 21.34 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 4.96 |
| fkgl_drop | 19.16 |
| fre | 75.5 |
| fre_gain | 144.5 |
| human_edit_recall | 1.000 |
| length_ratio | 0.41 |
| n_words | 9.0 |
| nli_completeness | 0.843 |
| nli_faithfulness | 0.907 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 43.06 |
| severity_downgrade | 0.000 |
| severity_preservation | 1.000 |
| severity_tier_input | 1.000 |
| severity_tier_output | 1.000 |
| smog | 8.84 |
| smog_drop | 5.71 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `nonmobile` -> `fixed` | replace | - | - | - | - | - | - | - |
| `atherosclerosis` -> `plaque buildup` | replace | - | - | - | - | - | - | - |
| `descending aortic` -> `lower main artery` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Mild fixed clogged artery in the chest.

| metric | value |
|---|---:|
| bertscore_f1 | 0.296 |
| coleman_liau | 6.49 |
| coleman_liau_drop | 22.83 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 2.31 |
| fkgl_drop | 21.81 |
| fre | 91.0 |
| fre_gain | 159.9 |
| human_edit_recall | 1.000 |
| length_ratio | 0.32 |
| n_words | 7.0 |
| nli_completeness | 0.494 |
| nli_faithfulness | 0.792 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 44.58 |
| severity_downgrade | 0.000 |
| severity_preservation | 1.000 |
| severity_tier_input | 1.000 |
| severity_tier_output | 1.000 |
| smog | 8.84 |
| smog_drop | 5.71 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `nonmobile` -> `fixed` | replace | attributed | -3.211 | -3.227 | - | 0.879 | 0.342 | -0.03696388699999975 |
| `descending aortic atherosclerosis` -> `clogged artery in the chest` | replace | attributed | 1.237 | 1.237 | - | 0.859 | 2.634 | 3.9879113699999973 |

**edit `nonmobile` -> `fixed`**

- status: `attributed`
- log p full -7.3440, empty -4.1325
- masks scored: 18/18 (+3 top-k)
- ranked sources:
    - `+0.152` [justplainclear] atherosclerosis: A disease where arteries get thick and prevent the flow of blood Normal artery and atheroscle
    - `-0.189` [michigan] atherosclerosis: A disease where your arteries get stiff and clogged by things in your blood, such as fat and 
    - `-0.488` [readme] descending aortic: Descending aortic: The area of the main artery as it travels through the chest.
    - `-2.028` [thesaurus] atherosclerosis: hardening of the arteries, clogged blood vessels

- rationale: Nonmobile simply means unable to move or change position, and fixed carries that exact idea by signaling a state of complete stillness. Word frequency increases from Zipf 0.00 to 4.70, while syllable count drops from 3 to 1. Patients can now grasp the immobility of the condition without wrestling with clinical jargon.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `descending aortic atherosclerosis` -> `clogged artery in the chest`**

- status: `attributed`
- log p full -12.6262, empty -13.8632
- masks scored: 18/18 (+3 top-k)
- ranked sources:
    - `+3.093` [readme] descending aortic: Descending aortic: The area of the main artery as it travels through the chest.
    - `+0.459` [justplainclear] atherosclerosis: A disease where arteries get thick and prevent the flow of blood Normal artery and atheroscle
    - `+0.295` [michigan] atherosclerosis: A disease where your arteries get stiff and clogged by things in your blood, such as fat and 
    - `-1.104` [thesaurus] atherosclerosis: hardening of the arteries, clogged blood vessels

- rationale: The original phrase describes a buildup of plaque that narrows the large blood vessel running down from the heart, so "clogged artery in the chest" captures that same physical blockage using everyday language. Phrase frequency increases from Zipf 2.55 to 3.11, and age of acquisition falls from 13.12 to 13.06, making the new wording more common and learned younger. You can now picture exactly where the blockage sits and what it does to your blood flow without needing to memorize a complex medical label.
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

**output:** The eustachian tube was blocked by bone wax.

| metric | value |
|---|---:|
| bertscore_f1 | 0.523 |
| coleman_liau | 6.60 |
| coleman_liau_drop | 3.62 |
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
| sari | 36.51 |
| smog | 8.84 |
| smog_drop | 2.37 |

### Stage 4 - arm `termonly`

**output:** The ear tube was blocked by a hard paste.

| metric | value |
|---|---:|
| bertscore_f1 | 0.554 |
| coleman_liau | 1.53 |
| coleman_liau_drop | 8.69 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.600 |
| fkgl | -0.28 |
| fkgl_drop | 6.99 |
| fre | 113.1 |
| fre_gain | 51.9 |
| human_edit_recall | 1.000 |
| length_ratio | 0.69 |
| n_words | 9.0 |
| nli_completeness | 0.267 |
| nli_faithfulness | 0.722 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 30.70 |
| smog | 3.13 |
| smog_drop | 8.08 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `eustachian tube` -> `ear tube` | replace | - | - | - | - | - | - | - |
| `obstructed` -> `blocked` | replace | - | - | - | - | - | - | - |
| `bone wax` -> `a hard paste` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** The ear throat tube was blocked with ear wax.

| metric | value |
|---|---:|
| bertscore_f1 | 0.576 |
| coleman_liau | 4.11 |
| coleman_liau_drop | 6.11 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.250 |
| fkgl | -0.28 |
| fkgl_drop | 6.99 |
| fre | 113.1 |
| fre_gain | 51.9 |
| human_edit_recall | 1.000 |
| length_ratio | 0.69 |
| n_words | 9.0 |
| nli_completeness | 0.207 |
| nli_faithfulness | 0.083 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 37.85 |
| smog | 3.13 |
| smog_drop | 8.08 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `eustachian tube` -> `ear throat tube` | replace | attributed | 4.483 | 4.485 | 0.884 | 0.904 | 5.811 | 6.400741549999999 |
| `obstructed` -> `blocked` | replace | attributed | -0.042 | -0.136 | 0.821 | 0.842 | 0.062 | 0.0042595999999999745 |
| `bone wax` -> `ear wax` | replace | attributed | 3.956 | 4.058 | 0.867 | 0.919 | 4.623 | 4.857657900000001 |

**edit `eustachian tube` -> `ear throat tube`**

- status: `attributed`
- log p full -5.9278, empty -10.4106
- masks scored: 66/66 (+5 top-k)
- ranked sources:
    - `+5.874` [justplainclear] eustachian tube: The tube that connects your middle ear to the back of your throat and pharynx area. The openi
    - `+0.063` [wiktionary] wax: If you wax something, you put wax on it, for example, a car.

- rationale: The source describes the eustachian tube as the passage linking the middle ear to the back of the throat, so "ear throat tube" keeps that connection in plain language. Phrase frequency increases from Zipf 1.90 to 3.88, while age of acquisition stays at 5.50. Patients can now picture the anatomical link without needing the medical name.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `obstructed` -> `blocked`**

- status: `attributed`
- log p full -0.3960, empty -0.3536
- masks scored: 66/66 (+5 top-k)
- ranked sources:
    - `+0.111` [justplainclear] eustachian tube: The tube that connects your middle ear to the back of your throat and pharynx area. The openi
    - `+0.050` [wiktionary] obstructed: If something obstructs your way, it blocks your path from point A to point B.
    - `+0.013` [wiktionary] wax: Wax is a solid material made of animal fat.

- rationale: When a doctor says a blood vessel is obstructed, they mean something is physically preventing flow through it, and swapping that word for blocked preserves that exact physical barrier idea while using everyday language. Word frequency increases from Zipf 2.98 to 4.31, making the term more common and easier to recognize, while the syllable count drops from 3 to 1. You can now picture exactly what is happening in your body without needing to decode a clinical label.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `bone wax` -> `ear wax`**

- status: `attributed`
- log p full -2.3119, empty -6.2677
- masks scored: 66/66 (+5 top-k)
- ranked sources:
    - `+5.142` [readme] wax: Yellow sticky stuff in your ear that keeps it clean and dry.
    - `+0.519` [wiktionary] obstructed: If something obstructs your way, it blocks your path from point A to point B.
    - `+0.486` [justplainclear] eustachian tube: The tube that connects your middle ear to the back of your throat and pharynx area. The openi
    - `+0.138` [wiktionary] wax: If you wax something, you put wax on it, for example, a car.
    - `+0.049` [wiktionary] wax: Wax is a solid material made of animal fat.

- rationale: The source describes ear wax as yellow sticky stuff in your ear that keeps it clean and dry, so "ear wax" keeps its central feature in plain language. Phrase frequency increases from Zipf 3.81 to 3.80, while age of acquisition falls from 6.00 to 6.00. Patients can understand the basic ear-cleaning problem without first knowing the diagnostic name.
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
| `supine` -> `on his back` | replace | - | - | - | - | - | - | - |

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
| `supine` -> `on his back` | replace | attributed | 0.051 | 0.069 | - | 0.906 | 0.042 | 0.19002031900000027 |

**edit `supine` -> `on his back`**

- status: `attributed`
- log p full -1.3239, empty -1.3754
- masks scored: 18/18 (+2 top-k)
- ranked sources:
    - `+0.139` [readme] supine: Lying on your back.
    - `+0.097` [michigan] supine: To lie on your back.
    - `-0.124` [iowa] SUPINE: lying on the back
    - `-0.415` [readme] Supine: Lying down on your back.

- rationale: The original term describes a patient lying flat with their chest facing upward, so switching to "on his back" preserves that exact physical position using everyday language. Phrase frequency increases from Zipf 2.42 to 5.87, while age of acquisition falls from 16.43 to 5.31, making the phrasing both more common and learned younger. Patients can now grasp the required body position without needing to decode clinical jargon.
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

**output:** The patient did not have a urine test done this time.

| metric | value |
|---|---:|
| bertscore_f1 | 0.738 |
| coleman_liau | 3.65 |
| coleman_liau_drop | 4.49 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 2.65 |
| fkgl_drop | 4.72 |
| fre | 95.7 |
| fre_gain | 41.0 |
| human_edit_recall | 1.000 |
| length_ratio | 1.38 |
| n_words | 11.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.991 |
| nli_faithfulness | 0.968 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 31.48 |
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
| `urinalysis` -> `urine test` | replace | attributed | 0.109 | 0.143 | - | 0.937 | 0.472 | 0.500525857 |
| `urinalysis` -> `done` | replace | attributed | -0.016 | -0.035 | - | 0.864 | 0.017 | 0.11983029099999998 |

**edit `urinalysis` -> `urine test`**

- status: `attributed`
- log p full -1.3877, empty -1.4967
- masks scored: 34/34 (+4 top-k)
- ranked sources:
    - `+0.559` [justplainclear] urinalysis: Also known as: urine test, pee test A test of your urine used to find certain medical conditions
    - `+0.087` [michigan] urinalysis: A test of your urine to check for diseases, such as diabetes, urinary tract infections, or kidney 
    - `+0.032` [nih] urinalysis: A test that determines the content of the urine.
    - `-0.141` [readme] urinalysis: A test that checks the contents of your pee to see what's in there.
    - `-0.280` [readme] Urinalysis: A test that checks what's in your pee.

- rationale: A urinalysis is simply a lab check of your urine to look for signs of infection or disease, so swapping it for "urine test" keeps that exact purpose in everyday language. Phrase frequency increases from Zipf 2.20 to 3.82, while age of acquisition falls from 14.68 to 9.83. You can now grasp the basic lab procedure without needing to memorize a clinical label.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `urinalysis` -> `done`**

- status: `attributed`
- log p full -0.6171, empty -0.6009
- masks scored: 34/34 (+4 top-k)
- ranked sources:
    - `+0.032` [readme] urinalysis: A test that checks the contents of your pee to see what's in there.
    - `+0.014` [michigan] urinalysis: A test of your urine to check for diseases, such as diabetes, urinary tract infections, or kidney 
    - `-0.320` [justplainclear] urinalysis: Also known as: urine test, pee test A test of your urine used to find certain medical conditions

- rationale: A urinalysis is simply a routine urine test that checks for signs of illness, so replacing it with "done" keeps that core idea by just stating the procedure was completed. Phrase frequency increases from Zipf 2.20 to 5.58, while the syllable count drops from five to one. You can now easily grasp that your doctor simply completed the routine urine test without needing to decode a technical label.
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

**output:** Her vision and hearing were good enough for the test, but she said she needed to get a new eyeglass prescription.

| metric | value |
|---|---:|
| bertscore_f1 | 0.594 |
| coleman_liau | 7.92 |
| coleman_liau_drop | 5.80 |
| copy_jargon_rate | 0.667 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.250 |
| fkgl | 8.33 |
| fkgl_drop | 3.93 |
| fre | 72.7 |
| fre_gain | 28.2 |
| human_edit_recall | 0.333 |
| length_ratio | 1.00 |
| n_words | 21.0 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.995 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.571 |
| sari | 18.83 |
| smog | 8.84 |
| smog_drop | 4.18 |

### Stage 4 - arm `termonly`

**output:** Vision and hearing seemed good enough for testing, although she said she needed to update her glasses fitting.

| metric | value |
|---|---:|
| bertscore_f1 | 0.787 |
| coleman_liau | 11.88 |
| coleman_liau_drop | 1.85 |
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
| nli_completeness | 0.982 |
| nli_faithfulness | 0.966 |
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
| `eyeglass prescription` -> `glasses fitting` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Vision and hearing appeared to be good enough for testing, although she said that she needed to update her glasses order.

| metric | value |
|---|---:|
| bertscore_f1 | 0.818 |
| coleman_liau | 10.13 |
| coleman_liau_drop | 3.59 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.286 |
| fkgl | 10.02 |
| fkgl_drop | 2.25 |
| fre | 60.6 |
| fre_gain | 16.1 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 21.0 |
| nli_completeness | 0.980 |
| nli_faithfulness | 0.983 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 51.51 |
| smog | 3.13 |
| smog_drop | 9.89 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `adequate` -> `good enough` | replace | attributed | 0.907 | 1.182 | 0.903 | 0.947 | 2.281 | 1.698276938 |
| `did indicate` -> `said` | replace | attributed | -1.492 | -2.166 | 0.706 | 0.837 | 0.185 | 0.0405707590000004 |
| `eyeglass prescription` -> `glasses order` | replace | attributed | 2.027 | 2.045 | 0.758 | 0.842 | 0.936 | 0.6092124859999997 |

**edit `adequate` -> `good enough`**

- status: `attributed`
- log p full -1.0567, empty -1.9634
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+2.452` [wiktionary] adequate: If something is adequate, it is good enough.
    - `+0.171` [wiktionary] did: Do is an auxiliary verb. It is used in questions, negative statements, short answers, and for emphasis wh
    - `+0.012` [readme] Prescription: A prescription is a doctor's recommendation for medication or treatment.
    - `+0.010` [wiktionary] prescription: A written order, as by a physician, to tell which medicine to take and how many doses of it is n
    - `+0.008` [justplainclear] eyeglass: A single lens used to help you see more clearly.

- rationale: The source defines adequate as meeting a minimum standard, so "good enough" keeps that threshold idea in plain language. Phrase frequency rises from Zipf 4.05 to 5.44, and age of acquisition drops from 10.35 to 6.96. Patients can grasp the required level without needing the formal word.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `did indicate` -> `said`**

- status: `attributed`
- log p full -2.0841, empty -0.5916
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+0.409` [wiktionary] did: Do is an auxiliary verb. It is used in questions, negative statements, short answers, and for emphasis wh
    - `+0.224` [michigan] prescription: An order from your doctor, nurse, or physician assistant for drugs or other treatment.
    - `+0.160` [wiktionary] prescription: A written order, as by a physician, to tell which medicine to take and how many doses of it is n
    - `+0.104` [readme] Prescription: A prescription is a doctor's recommendation for medication or treatment.

- rationale: The original term "did indicate" is a formal way of saying that something showed or pointed to a fact, and "said" keeps that core idea in everyday language. Phrase frequency rises from Zipf 4.34 to 6.01, making the expression more common and easier to process. This change lets patients grasp the meaning without stumbling over stiff, outdated phrasing.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `eyeglass prescription` -> `glasses order`**

- status: `attributed`
- log p full -3.9244, empty -5.9518
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+1.781` [michigan] prescription: An order from your doctor, nurse, or physician assistant for drugs or other treatment.
    - `+0.845` [thesaurus] prescription: doctors orders, medicine, drug order
    - `+0.681` [wiktionary] prescription: A written order, as by a physician, to tell which medicine to take and how many doses of it is n
    - `+0.549` [readme] Prescription: A prescription is a doctor's recommendation for medication or treatment.
    - `+0.224` [thesaurus] indicate: suggest, point to

- rationale: The Michigan glossary describes the original term as an order from a doctor or nurse for treatment, so "glasses order" carries that same idea in plain language. Phrase frequency increases from Zipf 2.32 to 4.31, while age of acquisition falls from 9.22 to 6.26. Patients can now understand the routine request without first learning the clinical name.
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

**output:** The doctor has talked to him several times about a colonoscopy, which he has refused, so the doctors have been testing his stool for hidden blood.

| metric | value |
|---|---:|
| bertscore_f1 | 0.595 |
| coleman_liau | 9.38 |
| coleman_liau_drop | -1.77 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.667 |
| fkgl | 9.53 |
| fkgl_drop | -1.50 |
| fre | 73.1 |
| fre_gain | -7.2 |
| human_edit_recall | 1.000 |
| length_ratio | 0.57 |
| n_words | 26.0 |
| nli_completeness | 0.985 |
| nli_faithfulness | 0.826 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 41.73 |
| smog | 3.13 |
| smog_drop | 0.00 |

### Stage 4 - arm `termonly`

**output:** I have talked to him several times about a test to look inside the large intestine, which he has refused, and so we have been testing bowel movements for hidden blood.

| metric | value |
|---|---:|
| bertscore_f1 | 0.665 |
| coleman_liau | 8.32 |
| coleman_liau_drop | -0.70 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 12.11 |
| fkgl_drop | -4.08 |
| fre | 63.5 |
| fre_gain | -16.8 |
| human_edit_recall | 1.000 |
| length_ratio | 0.67 |
| n_words | 31.0 |
| nli_completeness | 0.909 |
| nli_faithfulness | 0.966 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 65.62 |
| smog | 8.84 |
| smog_drop | -5.71 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `colonoscopy` -> `test to look inside the large intestine` | replace | - | - | - | - | - | - | - |
| `stools` -> `bowel movements` | replace | - | - | - | - | - | - | - |
| `occult blood` -> `hidden blood` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** The doctor has talked to him several times about a large intestine exam, which he has refused, and so the team has been doing bowel movements for hidden blood.

| metric | value |
|---|---:|
| bertscore_f1 | 0.534 |
| coleman_liau | 8.78 |
| coleman_liau_drop | -1.16 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 12.00 |
| fkgl_drop | -3.97 |
| fre | 60.7 |
| fre_gain | -19.5 |
| human_edit_recall | 1.000 |
| length_ratio | 0.63 |
| n_words | 29.0 |
| nli_completeness | 0.925 |
| nli_faithfulness | 0.893 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 41.51 |
| smog | 8.84 |
| smog_drop | -5.71 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `colonoscopy` -> `large intestine exam` | replace | attributed | 6.333 | 6.347 | 0.692 | 0.910 | 3.073 | 2.5030860479999992 |
| `occult blood` -> `hidden blood` | replace | attributed | 0.014 | 0.044 | 0.640 | 0.911 | 0.006 | 0.033482762 |

**edit `colonoscopy` -> `large intestine exam`**

- status: `attributed`
- log p full -4.2807, empty -10.6139
- masks scored: 66/66 (+3 top-k)
- ranked sources:
    - `+3.295` [justplainclear] colonoscopy: An exam of the inside of the large intestine that uses a flexible tube with a lens at the end
    - `+0.222` [wiktionary] occult: If something is occult it is part of the universe most people do not see. An occult thing is something
    - `+0.125` [readme] colonoscopy: A procedure to check for colon cancer by examining the inside of the large intestine.
    - `+0.116` [readme] occult: Obscure and mysterious, not easily understood.
    - `+0.096` [readme] Blood: Blood is a vital fluid that carries nutrients and oxygen to our body's tissues through the heart's pump

- rationale: The justplainclear glossary describes colonoscopy as an exam of the inside of the large intestine that uses a flexible tube with a lens at the end, so "large intestine exam" preserves that core idea in everyday language. Phrase frequency increases from Zipf 2.74 to 3.19, while age of acquisition falls from 15.76 to 9.28, shifting the vocabulary toward more common and younger-learned terms. You can now clearly picture what the test actually involves without first decoding a technical medical label.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `occult blood` -> `hidden blood`**

- status: `attributed`
- log p full -0.3698, empty -0.3838
- masks scored: 66/66 (+3 top-k)
- ranked sources:
    - `+0.054` [justplainclear] colonoscopy: An exam of the inside of the large intestine that uses a flexible tube with a lens at the end
    - `+0.048` [michigan] colonoscopy: Looks at the inside of the large intestine using a flexible tube with a ltiny camera at the end.

- rationale: "Occult blood" refers to bleeding that is not immediately visible, so swapping it for "hidden blood" preserves that core idea while using everyday language. Phrase frequency increases from Zipf 3.28 to 4.43, and age of acquisition decreases from 12.65 to 4.89, making the expression more common and learned younger. You can now grasp exactly where the bleeding is occurring without needing to decode a clinical label.
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

**output:** The knee was washed thoroughly with fluid and dried with suction again.

| metric | value |
|---|---:|
| bertscore_f1 | 0.652 |
| coleman_liau | 10.25 |
| coleman_liau_drop | 1.15 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 5.81 |
| fkgl_drop | 2.56 |
| fre | 74.8 |
| fre_gain | 21.9 |
| human_edit_recall | 1.000 |
| length_ratio | 0.75 |
| n_words | 12.0 |
| nli_completeness | 0.980 |
| nli_faithfulness | 0.988 |
| number_unit_preservation | 0.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 60.96 |
| smog | 8.84 |
| smog_drop | 2.37 |

### Stage 4 - arm `termonly`

**output:** The knee was washed out with a lot of fluid and dried with a vacuum.

| metric | value |
|---|---:|
| bertscore_f1 | 0.597 |
| coleman_liau | 2.72 |
| coleman_liau_drop | 8.68 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 3.63 |
| fkgl_drop | 4.74 |
| fre | 95.7 |
| fre_gain | 42.9 |
| human_edit_recall | 1.000 |
| length_ratio | 0.94 |
| n_words | 15.0 |
| nli_completeness | 0.923 |
| nli_faithfulness | 0.947 |
| number_unit_preservation | 0.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.400 |
| sari | 62.05 |
| smog | 3.13 |
| smog_drop | 8.08 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `copiously irrigated` -> `washed out with a lot of fluid` | replace | - | - | - | - | - | - | - |
| `suction dried` -> `dried with a vacuum` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** The knee was washed thoroughly with fluid and made dry with a suction machine once again.

| metric | value |
|---|---:|
| bertscore_f1 | 0.623 |
| coleman_liau | 8.81 |
| coleman_liau_drop | 2.59 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.200 |
| fkgl | 6.88 |
| fkgl_drop | 1.49 |
| fre | 74.3 |
| fre_gain | 21.4 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 16.0 |
| nli_completeness | 0.980 |
| nli_faithfulness | 0.970 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 63.17 |
| smog | 8.84 |
| smog_drop | 2.37 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `copiously irrigated` -> `washed thoroughly with fluid` | replace | attributed | -1.321 | -1.327 | 0.876 | 0.827 | 0.000 | -0.29954345400000104 |
| `suction dried` -> `made dry with a suction machine` | replace | attributed | 3.067 | 3.067 | 0.963 | 0.953 | 0.726 | 2.322716079000001 |

**edit `copiously irrigated` -> `washed thoroughly with fluid`**

- status: `attributed`
- log p full -6.1496, empty -4.8290
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.000` [dictionary] Copiously (adv.): In a copious manner.
    - `-0.153` [wiktionary] irrigated: To supply farms with water to grow crops.
    - `-0.174` [readme] suction: Suction is when a machine pulls in gas, liquid, or mucus.

- rationale: "Copiously irrigated" simply means a lot of liquid was poured over something, and "washed thoroughly with fluid" keeps that exact idea by using everyday words to describe the same heavy rinsing process. Phrase frequency increases from Zipf 1.98 to 3.66, meaning the higher score indicates the new wording is more common and easier to process. You can now picture exactly how much cleaning happened without getting stuck on unfamiliar medical jargon.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `suction dried` -> `made dry with a suction machine`**

- status: `attributed`
- log p full -11.3859, empty -14.4530
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+2.038` [readme] suction: Suction is when a machine pulls in gas, liquid, or mucus.
    - `+1.312` [wiktionary] dried: If something is dry, it has no water or liquid on it.
    - `-0.067` [dictionary] Copiously (adv.): In a copious manner.
    - `-0.479` [wiktionary] suction: A suction is a device that removes saliva from a patient's mouth during dental operations.

- rationale: The readme explains that suction involves a machine pulling away fluids or mucus, so "made dry with a suction machine" simply restates that clinical action in plain language. Phrase frequency increases from Zipf 3.28 to 3.33, while age of acquisition remains 9.42 to 9.42. You can now clearly picture how the device removes moisture without needing to decode medical shorthand.
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

**output:** She does not have pain when she pees, blood in her urine, frequent bathroom trips, or trouble starting to pee.

| metric | value |
|---|---:|
| bertscore_f1 | 0.636 |
| coleman_liau | 7.95 |
| coleman_liau_drop | 2.31 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 6.96 |
| fkgl_drop | 3.98 |
| fre | 80.8 |
| fre_gain | 39.2 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 20.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.965 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 27.73 |
| smog | 3.13 |
| smog_drop | 9.89 |

### Stage 4 - arm `termonly`

**output:** She is not having painful urination, any blood in the urine, needing to pee often or trouble starting to pee.

| metric | value |
|---|---:|
| bertscore_f1 | 0.842 |
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
| nli_completeness | 0.988 |
| nli_faithfulness | 0.989 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 66.66 |
| smog | 8.84 |
| smog_drop | 4.18 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `frequency` -> `needing to pee often` | replace | - | - | - | - | - | - | - |
| `hesitancy` -> `trouble starting to pee` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** She is not having painful urination, any blood in the urine, how often she pees or difficulty starting to pee.

| metric | value |
|---|---:|
| bertscore_f1 | 0.737 |
| coleman_liau | 8.24 |
| coleman_liau_drop | 2.02 |
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
| nli_completeness | 0.992 |
| nli_faithfulness | 0.950 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 63.83 |
| smog | 11.21 |
| smog_drop | 1.82 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `frequency` -> `how often she pees` | replace | attributed | 6.188 | 6.296 | - | 0.706 | 0.206 | 0.6818588089999995 |
| `hesitancy` -> `difficulty starting to pee` | replace | attributed | 1.127 | 1.201 | - | 0.928 | 1.438 | 1.5821860270000005 |

**edit `frequency` -> `how often she pees`**

- status: `attributed`
- log p full -2.2805, empty -8.4685
- masks scored: 34/34 (+4 top-k)
- ranked sources:
    - `+1.805` [readme] frequency: How often something happens.
    - `+1.599` [wiktionary] frequency: Something's frequency is how often it happens.
    - `+1.492` [readme] FREQUENCY: Frequency is how often something happens.
    - `+0.002` [readme] hesitancy: Having difficulty starting to pee or keeping the flow steady.

- rationale: Frequency simply refers to how many times something happens within a set period, so swapping it for "how often she pees" keeps that exact timing concept but translates it into everyday language. Phrase frequency shifts from Zipf 4.36 to 2.56, while age of acquisition falls from 9.79 to 6.53. You can now picture the exact timing of her bathroom visits without needing to decode clinical jargon.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `hesitancy` -> `difficulty starting to pee`**

- status: `attributed`
- log p full -2.2769, empty -3.4036
- masks scored: 34/34 (+4 top-k)
- ranked sources:
    - `+1.495` [readme] hesitancy: Having difficulty starting to pee or keeping the flow steady.
    - `+0.058` [readme] frequency: How often something happens.
    - `+0.037` [readme] FREQUENCY: Frequency is how often something happens.
    - `-0.604` [readme] hesitancy: Having difficulty starting or maintaining a steady flow while peeing.

- rationale: Hesitancy describes a hesitant or delayed action, so "difficulty starting to pee" preserves that core idea by translating it into straightforward everyday language. Phrase frequency increases from Zipf 2.35 to 3.78, while age of acquisition falls from 12.12 to 6.83, meaning the new phrasing is both more common and learned younger. Patients can now clearly recognize the specific urinary symptom without first learning a specialized medical label.
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

**output:** Cardiovascular: The patient has occasional chest pain behind the breastbone, which is related to the heart and feels like a tightness.

| metric | value |
|---|---:|
| bertscore_f1 | 0.453 |
| coleman_liau | 13.45 |
| coleman_liau_drop | 2.47 |
| copy_jargon_rate | 0.333 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 12.27 |
| fkgl_drop | 2.53 |
| fre | 44.5 |
| fre_gain | 21.7 |
| human_edit_recall | 0.667 |
| length_ratio | 0.70 |
| n_words | 21.0 |
| nli_completeness | 0.861 |
| nli_faithfulness | 0.900 |
| replacement_f1 | 0.800 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.200 |
| sari | 39.81 |
| smog | 13.02 |
| smog_drop | 2.88 |

### Stage 4 - arm `termonly`

**output:** Heart and blood vessels : Chest pain behind the breastbone, occasional heart muscle pain and the patient describes it as a sensation of tightness.

| metric | value |
|---|---:|
| bertscore_f1 | 0.683 |
| coleman_liau | 13.17 |
| coleman_liau_drop | 2.74 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.333 |
| fkgl | 11.34 |
| fkgl_drop | 3.46 |
| fre | 54.8 |
| fre_gain | 31.9 |
| human_edit_recall | 1.000 |
| length_ratio | 0.77 |
| n_words | 23.0 |
| nli_completeness | 0.963 |
| nli_faithfulness | 0.853 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 60.10 |
| smog | 11.21 |
| smog_drop | 4.70 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `retrosternal area` -> `breastbone` | replace | - | - | - | - | - | - | - |
| `anginal pain` -> `heart muscle pain` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Heart and blood vessels: Chest pain in the area behind the breastbone, occasional chest pain and the patient describes it as a sensation of tightness.

| metric | value |
|---|---:|
| bertscore_f1 | 0.707 |
| coleman_liau | 11.55 |
| coleman_liau_drop | 4.36 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.333 |
| fkgl | 12.10 |
| fkgl_drop | 2.70 |
| fre | 52.9 |
| fre_gain | 30.1 |
| human_edit_recall | 1.000 |
| length_ratio | 0.83 |
| n_words | 25.0 |
| nli_completeness | 0.930 |
| nli_faithfulness | 0.864 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 59.82 |
| smog | 13.02 |
| smog_drop | 2.88 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `anginal pain` -> `chest pain` | replace | attributed | 0.646 | 0.814 | 0.903 | 0.910 | 0.168 | 0.006103590000000159 |
| `retrosternal area` -> `area behind the breastbone` | replace | attributed | -0.520 | -0.611 | 0.699 | 0.559 | 0.000 | -0.05729775799999981 |

**edit `anginal pain` -> `chest pain`**

- status: `attributed`
- log p full -1.2786, empty -1.9242
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.204` [justplainclear] cardiovascular: About the heart and blood vessels
    - `+0.036` [nih] cardiovascular: Having to do with the heart and blood vessels.
    - `+0.034` [michigan] cardiovascular: Having to do with your heart and blood vessels.

- rationale: Anginal pain refers to the sharp, squeezing discomfort that occurs in the heart muscle, and swapping it for chest pain preserves that core sensation while using everyday language. Phrase frequency increases from Zipf 1.10 to 4.40, and age of acquisition falls from 4.26 to 5.05, indicating the new wording is both more common and learned earlier. You can now recognize the warning signs of a heart issue without needing to memorize specialized medical terminology.
- audit: coverage 1.0, grounding_error=True, omission=False, source_ok=True, passage_ok=True

**edit `retrosternal area` -> `area behind the breastbone`**

- status: `attributed`
- log p full -2.1797, empty -1.6596
- masks scored: 66/66 (+4 top-k)
- ranked sources:

- rationale: The original term points to the chest region directly behind the sternum, so replacing it with "area behind the breastbone" keeps that exact location clear while using everyday words. Phrase frequency increases from Zipf 0.00 to 1.93, and age of acquisition rises from 6.58 to 10.75, mapping the precise difficulty shift. You can now easily visualize where the discomfort originates without needing to memorize a specialized medical label.
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

**output:** The surgeons removed a large part of his synovium and synovial pouch.

| metric | value |
|---|---:|
| bertscore_f1 | 0.320 |
| coleman_liau | 9.28 |
| coleman_liau_drop | -3.52 |
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
| nli_faithfulness | 0.866 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 32.05 |
| smog | 8.84 |
| smog_drop | 0.00 |

### Stage 4 - arm `termonly`

**output:** We removed a good bit of his joint lining and joint fluid sac.

| metric | value |
|---|---:|
| bertscore_f1 | 0.534 |
| coleman_liau | 3.78 |
| coleman_liau_drop | 1.98 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 4.00 |
| fkgl_drop | 0.79 |
| fre | 89.5 |
| fre_gain | 9.2 |
| human_edit_recall | 1.000 |
| length_ratio | 1.08 |
| n_words | 13.0 |
| nli_completeness | 0.807 |
| nli_faithfulness | 0.958 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 44.24 |
| smog | 3.13 |
| smog_drop | 5.71 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `synovium` -> `joint lining` | replace | - | - | - | - | - | - | - |
| `synovial pouch` -> `joint fluid sac` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** We cut out a good bit of his joint lining and joint lining pocket.

| metric | value |
|---|---:|
| bertscore_f1 | 0.553 |
| coleman_liau | 3.63 |
| coleman_liau_drop | 2.14 |
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
| nli_completeness | 0.659 |
| nli_faithfulness | 0.727 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 52.89 |
| smog | 3.13 |
| smog_drop | 5.71 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `synovium` -> `joint lining` | replace | attributed | 0.045 | 0.087 | 0.535 | 0.783 | 0.067 | 0.03987998000000015 |
| `synovial pouch` -> `joint lining pocket` | replace | attributed | 0.878 | 0.914 | 0.626 | 0.669 | 0.037 | 0.15114709000000026 |

**edit `synovium` -> `joint lining`**

- status: `attributed`
- log p full -0.7031, empty -0.7478
- masks scored: 66/66 (+3 top-k)
- ranked sources:
    - `+0.225` [readme] Synovial: Relating to the soft tissue that lines joints.
    - `+0.158` [readme] SYNOVIAL: Synovial means having to do with the soft tissue that lines joints.
    - `+0.085` [wiktionary] pouch: A pouch is a small bag or pocket used for carrying things.

- rationale: The synovium is the thin, protective tissue that cushions and covers the inside of your joints, so "joint lining" simply describes that same protective layer in everyday language. Phrase frequency increases from Zipf 1.46 to 3.82, meaning the replacement is more common and easier to process. You can now picture exactly where that protective tissue lives and how it helps your joints move smoothly without needing to memorize a specialized medical label.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `synovial pouch` -> `joint lining pocket`**

- status: `attributed`
- log p full -2.8283, empty -3.7063
- masks scored: 66/66 (+3 top-k)
- ranked sources:
    - `+0.302` [wiktionary] pouch: A pouch is a small bag or pocket used for carrying things.
    - `+0.265` [readme] Synovial: Relating to the soft tissue that lines joints.
    - `+0.196` [readme] SYNOVIAL: Synovial means having to do with the soft tissue that lines joints.

- rationale: A synovial pouch is a small, fluid-filled sac that cushions and protects the moving parts of a joint, so "joint lining pocket" simply describes that same protective, cushioning space in everyday language. Phrase frequency increases from Zipf 2.32 to 3.73, while age of acquisition falls from 16.00 to 9.30. You can now picture exactly how your joint is cushioned without needing to memorize a specialized anatomical label.
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

**output:** The patient's condition should be checked for inflammation, such as an infection or reduced blood flow.

| metric | value |
|---|---:|
| bertscore_f1 | 0.625 |
| coleman_liau | 13.16 |
| coleman_liau_drop | 1.04 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| diagnostic_identity_preservation | 1.000 |
| fkgl | 9.09 |
| fkgl_drop | 4.29 |
| fre | 58.4 |
| fre_gain | 39.6 |
| human_edit_recall | 1.000 |
| length_ratio | 1.31 |
| n_words | 17.0 |
| nli_completeness | 0.966 |
| nli_faithfulness | 0.927 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.400 |
| sari | 30.79 |
| smog | 13.02 |
| smog_drop | 1.53 |

### Stage 4 - arm `termonly`

**output:** Swelling, such as infection or poor blood flow, must be considered.

| metric | value |
|---|---:|
| bertscore_f1 | 0.711 |
| coleman_liau | 9.98 |
| coleman_liau_drop | 4.22 |
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
| nli_completeness | 0.967 |
| nli_faithfulness | 0.976 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 50.57 |
| smog | 11.21 |
| smog_drop | 3.35 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `ischemia` -> `poor blood flow` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** An inflammation such as infection or low blood flow must be considered.

| metric | value |
|---|---:|
| bertscore_f1 | 0.857 |
| coleman_liau | 10.25 |
| coleman_liau_drop | 3.95 |
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
| nli_completeness | 0.833 |
| nli_faithfulness | 0.962 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 51.00 |
| smog | 13.02 |
| smog_drop | 1.53 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `inflammatory process` -> `inflammation` | replace | attributed | 0.164 | 0.166 | 0.537 | 0.710 | 0.124 | 0.12822180000000039 |
| `ischemia` -> `low blood flow` | replace | attributed | 0.025 | 0.027 | 0.846 | 0.917 | 0.042 | 0.29725272400000025 |

**edit `inflammatory process` -> `inflammation`**

- status: `attributed`
- log p full -4.4681, empty -4.6324
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.136` [nih] ischemia: Lack of blood supply to a part of the body. Ischemia may cause tissue damage due to the lack of oxyg
    - `+0.013` [readme] Ischemia: Ischemia is when there's a lack of blood flow due to blocked blood vessels.
    - `-0.008` [readme] inflammatory process: When your body gets inflamed, it's like it's telling you there's something wrong by show
    - `-0.030` [readme] ischemia: Not enough blood flow due to blocked or narrowed blood vessels.

- rationale: An inflammatory process simply describes how the body reacts to injury or infection by sending white blood cells to the affected area, and using the single word "inflammation" preserves that exact biological reaction in everyday language. Phrase frequency increases from Zipf 3.71 to 3.73, while age of acquisition decreases from 13.33 to 11.00, meaning the replacement is more common and learned younger. You can now grasp the core body reaction without needing to decode a longer, more clinical description.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `ischemia` -> `low blood flow`**

- status: `attributed`
- log p full -2.9062, empty -2.9315
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.727` [readme] ischemia: Not enough blood flow due to blocked or narrowed blood vessels.
    - `+0.685` [iowa] ISCHEMIA: decreased oxygen in a tissue (usually because of decreased blood flow)
    - `+0.068` [michigan] ischemia: When blood supply to an organ or a body part isn't enough, especially the heart.
    - `-0.217` [readme] Ischemia: Ischemia is when there's a lack of blood flow due to blocked blood vessels.

- rationale: Ischemia describes a state where body tissues are starved of oxygen, so replacing it with "low blood flow" keeps that vital concept clear in everyday speech. Phrase frequency increases from Zipf 2.85 to 4.47, making it more common and easier, while age of acquisition drops from 18.00 to 7.40, meaning it is learned younger and easier. You can now understand how restricted circulation impacts your health without first decoding a specialized medical label.
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

**output:** The doctor asked her to increase her prednisone when she goes home.

| metric | value |
|---|---:|
| bertscore_f1 | 0.725 |
| coleman_liau | 8.32 |
| coleman_liau_drop | -1.93 |
| copy_jargon_rate | 1.000 |
| critical_error | 0.000 |
| drug_preservation | 1.000 |
| fkgl | 3.84 |
| fkgl_drop | -0.98 |
| fre | 88.9 |
| fre_gain | -7.0 |
| human_edit_recall | 0.000 |
| length_ratio | 1.00 |
| n_words | 12.0 |
| nli_completeness | 0.957 |
| nli_faithfulness | 0.314 |
| replacement_f1 | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 23.35 |
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

**output:** I have asked her to increase her anti-inflammatory medicine when she goes home.

| metric | value |
|---|---:|
| bertscore_f1 | 0.868 |
| coleman_liau | 10.92 |
| coleman_liau_drop | -4.54 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| drug_preservation | 0.000 |
| fkgl | 9.45 |
| fkgl_drop | -6.59 |
| fre | 50.5 |
| fre_gain | -45.5 |
| human_edit_recall | 1.000 |
| length_ratio | 1.17 |
| n_words | 14.0 |
| nli_completeness | 0.017 |
| nli_faithfulness | 0.530 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 66.67 |
| smog | 11.21 |
| smog_drop | -8.08 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `prednisone` -> `anti-inflammatory medicine` | replace | attributed | 3.461 | 3.553 | - | 0.881 | 0.196 | 0.4722057049999999 |

**edit `prednisone` -> `anti-inflammatory medicine`**

- status: `attributed`
- log p full -2.4015, empty -5.8628
- masks scored: 10/10 (+2 top-k)
- ranked sources:
    - `+1.354` [readme] Prednisone: A medication that lowers the body's immune response and inflammation.
    - `+1.158` [nih] prednisone: A drug used to reduce inflammation and lower the body’s immune response.  It is used with other dr
    - `+0.412` [readme] prednisone: A medication that helps lower the body's immune system reactions.

- rationale: Prednisone is a prescription drug that reduces swelling and pain in the body, so calling it an anti-inflammatory medicine keeps that core healing action clear in everyday language. Phrase frequency increases from Zipf 2.56 to 3.66, while age of acquisition falls from 17.17 to 4.89. You can now grasp exactly how the treatment works without needing to memorize a specialized drug name.
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

**output:** She may need other medications for nerve pain as needed.

| metric | value |
|---|---:|
| bertscore_f1 | 0.941 |
| coleman_liau | 7.92 |
| coleman_liau_drop | 4.57 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 6.01 |
| fkgl_drop | 4.20 |
| fre | 69.8 |
| fre_gain | 31.9 |
| human_edit_recall | 1.000 |
| length_ratio | 1.11 |
| n_words | 10.0 |
| nli_completeness | 0.831 |
| nli_faithfulness | 0.951 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 58.21 |
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
| `neuropathic` -> `nerve pain` | replace | attributed | 0.656 | 1.587 | - | 0.800 | 0.260 | 0.012591381000000013 |

**edit `neuropathic` -> `nerve pain`**

- status: `attributed`
- log p full -0.2719, empty -0.9275
- masks scored: 6/6 (+1 top-k)
- ranked sources:
    - `+0.863` [readme] neuropathic: Nerve pain.
    - `+0.604` [readme] Neuropathic: Neuropathic means nerve pain.

- rationale: Neuropathic describes abnormal electrical signals traveling along damaged nerves, so "nerve pain" preserves that core physical sensation in plain language. Phrase frequency increases from Zipf 2.35 to 4.13, while age of acquisition falls from 15.40 to 9.67. You can now grasp the exact type of discomfort without first learning a specialized medical label.
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

**output:** The patient was given a preventive dose of antibiotics.

| metric | value |
|---|---:|
| bertscore_f1 | 0.619 |
| coleman_liau | 10.56 |
| coleman_liau_drop | 0.90 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 10.21 |
| fkgl_drop | 2.22 |
| fre | 37.9 |
| fre_gain | 19.5 |
| human_edit_recall | 1.000 |
| length_ratio | 1.29 |
| n_words | 9.0 |
| nli_completeness | 0.668 |
| nli_faithfulness | 0.971 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 41.87 |
| smog | 11.21 |
| smog_drop | 0.00 |

### Stage 4 - arm `termonly`

**output:** A preventive dose of bacterial medicines was given.

| metric | value |
|---|---:|
| bertscore_f1 | 0.811 |
| coleman_liau | 11.68 |
| coleman_liau_drop | -0.22 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 11.13 |
| fkgl_drop | 1.30 |
| fre | 29.5 |
| fre_gain | 11.1 |
| human_edit_recall | 1.000 |
| length_ratio | 1.14 |
| n_words | 8.0 |
| nli_completeness | 0.859 |
| nli_faithfulness | 0.979 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 28.96 |
| smog | 13.02 |
| smog_drop | -1.82 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `prophylactic` -> `preventive` | replace | - | - | - | - | - | - | - |
| `antibiotics` -> `bacterial medicines` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** A preventive dose of bacteria-killing medicine was given.

| metric | value |
|---|---:|
| bertscore_f1 | 0.777 |
| coleman_liau | 15.30 |
| coleman_liau_drop | -3.84 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 11.13 |
| fkgl_drop | 1.30 |
| fre | 29.5 |
| fre_gain | 11.1 |
| human_edit_recall | 1.000 |
| length_ratio | 1.29 |
| n_words | 9.0 |
| nli_completeness | 0.883 |
| nli_faithfulness | 0.982 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 28.96 |
| smog | 13.02 |
| smog_drop | -1.82 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `prophylactic` -> `preventive` | replace | attributed | 0.140 | 0.157 | 0.719 | 0.896 | 0.279 | 0.12139760000000033 |
| `antibiotics` -> `bacteria-killing medicine` | replace | attributed | 4.228 | 4.325 | 0.906 | 0.917 | 1.619 | 1.8807034284000004 |

**edit `prophylactic` -> `preventive`**

- status: `attributed`
- log p full -2.1582, empty -2.2981
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.378` [readme] PROPHYLACTIC: Preventive measures or treatments to avoid getting sick.
    - `+0.099` [nih] prophylactic: In medicine, something that prevents or protects.

- rationale: Prophylactic originally refers to measures taken to stop a disease from starting, and switching to preventive keeps that exact idea while using everyday language. Word frequency increases from Zipf 2.59 to 3.50, while age of acquisition falls from 15.20 to 10.50, confirming that the replacement is more common and learned younger. You can now clearly understand the basic goal of stopping illness before it begins.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `antibiotics` -> `bacteria-killing medicine`**

- status: `attributed`
- log p full -2.3625, empty -6.5902
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+3.727` [readme] Antibiotics: Medicine that kills bacteria.
    - `+2.107` [wiktionary] antibiotics: An antibiotic is a drug that stops the growth of or destroys bacteria and other such microorganis
    - `+0.307` [wiktionary] prophylactic: A prophylactic is a medicine which preserves or defends against disease.
    - `+0.272` [wiktionary] prophylactic: Something that is prophylactic serves to prevent or protect against a disease or pregnancy.
    - `+0.231` [nih] prophylactic: In medicine, something that prevents or protects.

- rationale: The readme explains that antibiotics are medicine that kills bacteria, so "bacteria-killing medicine" keeps that essential meaning in plain language. Phrase frequency increases from Zipf 3.74 to 4.02, while age of acquisition drops from 9.55 to 4.89. You can now understand exactly what the treatment does without first learning a specialized medical term.
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

**output:** The patient has long-term low potassium levels in the blood caused by long-lasting diarrhea.

| metric | value |
|---|---:|
| bertscore_f1 | 0.580 |
| coleman_liau | 13.57 |
| coleman_liau_drop | 8.23 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.286 |
| fkgl | 10.94 |
| fkgl_drop | 5.31 |
| fre | 41.6 |
| fre_gain | 52.3 |
| human_edit_recall | 1.000 |
| length_ratio | 1.78 |
| n_words | 16.0 |
| nli_completeness | 0.845 |
| nli_faithfulness | 0.968 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 45.66 |
| smog | 13.02 |
| smog_drop | -1.82 |
| temporality_preservation | 0.000 |

### Stage 4 - arm `termonly`

**output:** Long-lasting low blood potassium caused by long-lasting loose stools.

| metric | value |
|---|---:|
| bertscore_f1 | 0.475 |
| coleman_liau | 18.29 |
| coleman_liau_drop | 3.51 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.375 |
| fkgl | 8.90 |
| fkgl_drop | 7.35 |
| fre | 47.3 |
| fre_gain | 58.1 |
| human_edit_recall | 1.000 |
| length_ratio | 1.22 |
| n_words | 11.0 |
| nli_completeness | 0.907 |
| nli_faithfulness | 0.961 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 34.13 |
| smog | 13.02 |
| smog_drop | -1.82 |
| temporality_preservation | 0.000 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `hypokalemia` -> `low blood potassium` | replace | - | - | - | - | - | - | - |
| `diarrhea` -> `loose stools` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Long-lasting low blood potassium caused by long-lasting loose stools.

| metric | value |
|---|---:|
| bertscore_f1 | 0.475 |
| coleman_liau | 18.29 |
| coleman_liau_drop | 3.51 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.375 |
| fkgl | 8.90 |
| fkgl_drop | 7.35 |
| fre | 47.3 |
| fre_gain | 58.1 |
| human_edit_recall | 1.000 |
| length_ratio | 1.22 |
| n_words | 11.0 |
| nli_completeness | 0.907 |
| nli_faithfulness | 0.961 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 34.13 |
| smog | 13.02 |
| smog_drop | -1.82 |
| temporality_preservation | 0.000 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `hypokalemia` -> `low blood potassium` | replace | attributed | 4.126 | 4.426 | 0.832 | 0.899 | 0.150 | 1.3474087604999998 |
| `diarrhea` -> `loose stools` | replace | attributed | -0.901 | -1.150 | 0.847 | 0.951 | 2.142 | 2.49428217 |

**edit `hypokalemia` -> `low blood potassium`**

- status: `attributed`
- log p full -1.3382, empty -5.4644
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.857` [iowa] HYPOKALEMIA: low blood potassium level
    - `+0.707` [readme] Chronic: A long-lasting or recurring health issue.
    - `+0.458` [readme] Chronic: A long-lasting or recurring health issue.
    - `+0.043` [readme] hypokalemia: Not enough potassium in your blood causing muscle cramps, weakness, heart issues, or kidney probl

- rationale: The Iowa glossary defines hypokalemia as a low blood potassium level, so switching to "low blood potassium" preserves that exact clinical idea while speaking in everyday terms. Phrase frequency increases from Zipf 1.76 to 3.56, confirming that the higher value means the phrase is more common and easier to process. You can now grasp the core electrolyte imbalance without needing to memorize a specialized medical label.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `diarrhea` -> `loose stools`**

- status: `attributed`
- log p full -2.0316, empty -1.1310
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+2.448` [readme] diarrhea: Having loose, watery poop with cramps and bloating.
    - `+0.307` [iowa] CHRONIC: continuing for a long time, ongoing
    - `+0.193` [wiktionary] secondary: of less than primary importance.
    - `+0.179` [readme] hypokalemia: Not enough potassium in your blood causing muscle cramps, weakness, heart issues, or kidney probl
    - `+0.110` [wiktionary] secondary: second, next in order to the first or primary.

- rationale: Diarrhea describes frequent, watery bowel movements, and replacing it with loose stools keeps that exact physical description while using everyday vocabulary. Phrase frequency shifts from Zipf 3.55 to 3.03, and the syllable count drops from 4 to 2, making the new phrasing statistically easier to process. You can now picture the exact symptom without needing to decode a clinical label first.
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

**output:** The patient had no enlarged liver or spleen, and the area did not hurt when touched.

| metric | value |
|---|---:|
| bertscore_f1 | 0.477 |
| coleman_liau | 6.64 |
| coleman_liau_drop | 16.56 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 6.14 |
| fkgl_drop | 0.48 |
| fre | 79.6 |
| fre_gain | 24.8 |
| human_edit_recall | 1.000 |
| length_ratio | 1.78 |
| n_words | 16.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.927 |
| nli_faithfulness | 0.084 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 52.21 |
| smog | 8.84 |
| smog_drop | 0.00 |

### Stage 4 - arm `termonly`

**output:** No swollen liver and spleen or pain when touched.

| metric | value |
|---|---:|
| bertscore_f1 | 0.820 |
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
| nli_completeness | 0.958 |
| nli_faithfulness | 0.294 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 53.69 |
| smog | 3.13 |
| smog_drop | 5.71 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `hepatosplenomegaly` -> `swollen liver and spleen` | replace | - | - | - | - | - | - | - |
| `tenderness` -> `pain when touched` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** No swollen liver and spleen or pain when touched.

| metric | value |
|---|---:|
| bertscore_f1 | 0.820 |
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
| nli_completeness | 0.958 |
| nli_faithfulness | 0.294 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 53.69 |
| smog | 3.13 |
| smog_drop | 5.71 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `hepatosplenomegaly` -> `swollen liver and spleen` | replace | attributed | 0.931 | 0.935 | - | 0.858 | 0.095 | 0.17036245000000072 |
| `tenderness` -> `pain when touched` | replace | attributed | 1.913 | 2.004 | - | 0.868 | 1.281 | 0.8469121899999998 |

**edit `hepatosplenomegaly` -> `swollen liver and spleen`**

- status: `attributed`
- log p full -4.9707, empty -5.9019
- masks scored: 18/18 (+3 top-k)
- ranked sources:
    - `+0.246` [readme] tenderness: Tenderness is when an area hurts when you touch it.
    - `+0.151` [wiktionary] tenderness: Tenderness is the pain or discomfort when an affected area is touched.
    - `+0.094` [wiktionary] tenderness: Tenderness is a tendency to show concern or kindness towards others.

- rationale: Hepatosplenomegaly refers to an enlargement of the liver and spleen, so "swollen liver and spleen" preserves that exact physical description using everyday vocabulary. Phrase frequency increases from Zipf 1.12 to 2.97, meaning the higher score makes the wording more common and easier to read. You can now grasp the core physical change without needing to memorize a specialized medical label.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `tenderness` -> `pain when touched`**

- status: `attributed`
- log p full -2.2932, empty -4.2059
- masks scored: 18/18 (+3 top-k)
- ranked sources:
    - `+1.610` [wiktionary] tenderness: Tenderness is the pain or discomfort when an affected area is touched.
    - `+0.329` [readme] tenderness: Tenderness is when an area hurts when you touch it.
    - `+0.046` [wiktionary] tenderness: Tenderness is a tendency to show concern or kindness towards others.
    - `-0.681` [readme] Tenderness: Tenderness is when an area hurts or is sensitive to touch.

- rationale: Tenderness refers to a sensitive or aching sensation in a specific area, so "pain when touched" captures that exact physical response in everyday language. Phrase frequency increases from Zipf 3.24 to 4.22, while age of acquisition falls from 8.79 to 4.26. Patients can now recognize the exact physical symptom without needing to decode clinical jargon.
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

**output:** He did not feel pain in the front of his left chest when he exercised.

| metric | value |
|---|---:|
| bertscore_f1 | 0.780 |
| coleman_liau | 3.49 |
| coleman_liau_drop | 6.49 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 3.63 |
| fkgl_drop | 5.45 |
| fre | 95.7 |
| fre_gain | 46.2 |
| human_edit_recall | 1.000 |
| laterality_preservation | 0.500 |
| length_ratio | 1.36 |
| n_words | 15.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.986 |
| nli_faithfulness | 0.993 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 27.63 |
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

**output:** He did not feel pain in the front of his left chest with exercise.

| metric | value |
|---|---:|
| bertscore_f1 | 0.839 |
| coleman_liau | 3.63 |
| coleman_liau_drop | 6.35 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 3.36 |
| fkgl_drop | 5.73 |
| fre | 95.9 |
| fre_gain | 46.4 |
| human_edit_recall | 1.000 |
| laterality_preservation | 0.500 |
| length_ratio | 1.27 |
| n_words | 14.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.975 |
| nli_faithfulness | 0.992 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 32.85 |
| smog | 8.84 |
| smog_drop | 4.18 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `experience` -> `feel` | replace | attributed | 0.271 | 0.679 | 0.723 | 0.863 | 0.949 | 0.20619158199999993 |
| `anterior` -> `front of his left` | replace | attributed | 0.699 | 1.344 | 0.583 | 0.747 | 0.118 | 0.01710692500000005 |

**edit `experience` -> `feel`**

- status: `attributed`
- log p full -0.3868, empty -0.6582
- masks scored: 66/66 (+3 top-k)
- ranked sources:
    - `+0.952` [thesaurus] experience: feel, have, go through
    - `+0.003` [nih] anterior: In human anatomy, has to do with the front of a structure, or a structure found toward the front of 

- rationale: The original term "experience" refers to the personal process of going through or perceiving something, so replacing it with "feel" keeps that core idea by using a simpler, everyday word to describe what a person actually perceives. Word frequency increases from Zipf 5.27 to 5.67, meaning it is higher and therefore more common and easier, while age of acquisition falls from 8.95 to 5.11, meaning it is lower and therefore learned younger and easier. This adjustment allows patients to immediately grasp the intended message without getting tangled in unfamiliar vocabulary.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `anterior` -> `front of his left`**

- status: `attributed`
- log p full -0.4417, empty -1.1410
- masks scored: 66/66 (+3 top-k)
- ranked sources:
    - `+0.120` [thesaurus] experience: feel, have, go through
    - `+0.001` [readme] Anterior: The front part of the body or an organ.

- rationale: The original term refers to the front part of the body, and "front of his left" keeps that location clear in everyday language. Phrase frequency increases from Zipf 3.51 to 5.10, while age of acquisition falls from 14.12 to 5.57. Patients can now picture the exact spot without needing to know anatomical labels.
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
| `atrial fibrillation` -> `irregular heartbeat` | replace | attributed | -0.254 | -0.281 | - | 0.929 | 0.491 | 0.9763328260000002 |

**edit `atrial fibrillation` -> `irregular heartbeat`**

- status: `attributed`
- log p full -2.4794, empty -2.2253
- masks scored: 10/10 (+2 top-k)
- ranked sources:
    - `+0.484` [readme] Atrial fibrillation: Atrial fibrillation is when your heart beats irregularly and can make you tired or more l
    - `-0.006` [justplainclear] atrial fibrillation: A problem with the speed or rhythm that your heart beats It is the most common type of ar
    - `-0.675` [readme] atrial fibrillation: Atrial fibrillation is when your heart beats in a weird way that can make you tired and i

- rationale: Atrial fibrillation describes a condition where the heart’s electrical signals fire out of sync, causing the chambers to quiver rather than pump steadily, and swapping it for "irregular heartbeat" preserves that core idea by describing the same unpredictable rhythm in everyday terms. Phrase frequency increases from Zipf 2.58 to 3.38, while age of acquisition decreases from 14.58 to 9.16, meaning the replacement is both more common and learned younger. You can now grasp the fundamental nature of your heart rhythm without needing to memorize a specialized medical label.
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

**output:** Overall, the patient gives a clear and detailed account of their past.

| metric | value |
|---|---:|
| bertscore_f1 | 0.468 |
| coleman_liau | 9.28 |
| coleman_liau_drop | 1.67 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 5.81 |
| fkgl_drop | 5.32 |
| fre | 74.8 |
| fre_gain | 45.3 |
| human_edit_recall | 1.000 |
| length_ratio | 1.20 |
| n_words | 12.0 |
| nli_completeness | 0.118 |
| nli_faithfulness | 0.178 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 37.92 |
| smog | 8.84 |
| smog_drop | 4.18 |

### Stage 4 - arm `termonly`

**output:** Overall the patient appears to be clear about their health.

| metric | value |
|---|---:|
| bertscore_f1 | 0.594 |
| coleman_liau | 9.66 |
| coleman_liau_drop | 1.29 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.250 |
| fkgl | 6.01 |
| fkgl_drop | 5.12 |
| fre | 69.8 |
| fre_gain | 40.3 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 10.0 |
| nli_completeness | 0.035 |
| nli_faithfulness | 0.123 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 39.85 |
| smog | 8.84 |
| smog_drop | 4.18 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `good historian` -> `clear about their health` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Overall the patient is apparently good at sharing past events.

| metric | value |
|---|---:|
| bertscore_f1 | 0.657 |
| coleman_liau | 11.40 |
| coleman_liau_drop | -0.45 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.333 |
| fkgl | 9.55 |
| fkgl_drop | 1.58 |
| fre | 44.4 |
| fre_gain | 14.9 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 10.0 |
| nli_completeness | 0.916 |
| nli_faithfulness | 0.981 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 63.22 |
| smog | 11.21 |
| smog_drop | 1.82 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `seemingly` -> `apparently` | replace | attributed | 1.026 | 1.029 | - | 0.988 | 2.185 | 2.162282519999999 |
| `good historian` -> `good at sharing past events` | replace | attributed | 2.152 | 2.152 | - | 0.982 | 1.973 | 2.5937974800000028 |

**edit `seemingly` -> `apparently`**

- status: `attributed`
- log p full -5.3766, empty -6.4024
- masks scored: 18/18 (+2 top-k)
- ranked sources:
    - `+1.985` [dictionary] Seemingly (adv.): In appearance; in show; in semblance; apparently; ostensibly.
    - `-0.200` [wiktionary] good: When you are good, you do the right things. That is, you do things that are kind or helpful. You do not 
    - `-0.253` [wiktionary] historian: A historian is a person who studies or writes about history.
    - `-0.306` [wiktionary] good: If something is good it is useful or helpful. This also means high quality.

- rationale: "Seemingly" indicates how something appears based on surface clues, and "apparently" preserves that exact idea by describing what seems true at first glance. Word frequency increases from Zipf 4.10 to 4.80, while the syllable count rises from 3 to 4. You can now grasp the intended meaning of the statement without getting tangled up in less familiar phrasing.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `good historian` -> `good at sharing past events`**

- status: `attributed`
- log p full -16.4002, empty -18.5517
- masks scored: 18/18 (+2 top-k)
- ranked sources:
    - `+2.296` [dictionary] Seemingly (adv.): In appearance; in show; in semblance; apparently; ostensibly.
    - `+0.323` [wiktionary] historian: A historian is a person who studies or writes about history.
    - `-0.142` [wiktionary] good: When you are good, you do the right things. That is, you do things that are kind or helpful. You do not 
    - `-0.440` [wiktionary] good: If something is good it is useful or helpful. This also means high quality.

- rationale: A good historian is someone who carefully studies and remembers past events, so saying someone is good at sharing past events keeps that same idea in everyday language. Phrase frequency increases from Zipf 3.90 to 4.45 (higher = more common = easier), while age of acquisition falls from 11.58 to 6.78 (lower = learned younger = easier). Patients can now grasp the core idea of historical knowledge without needing to decode specialized academic labels.
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

**output:** The colonoscopy did not show any signs of active Crohn's disease in the patient.

| metric | value |
|---|---:|
| bertscore_f1 | 0.414 |
| coleman_liau | 9.01 |
| coleman_liau_drop | 0.65 |
| copy_jargon_rate | 1.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 5.04 |
| fkgl_drop | -1.39 |
| fre | 83.9 |
| fre_gain | -2.9 |
| human_edit_recall | 0.000 |
| length_ratio | 1.07 |
| n_words | 15.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.993 |
| nli_faithfulness | 0.984 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 1.000 |
| sari | 18.58 |
| smog | 3.13 |
| smog_drop | 0.00 |

### Stage 4 - arm `termonly`

**output:** No active gut disease was found during the bowel exam.

| metric | value |
|---|---:|
| bertscore_f1 | 0.654 |
| coleman_liau | 6.76 |
| coleman_liau_drop | 2.90 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.333 |
| fkgl | 6.01 |
| fkgl_drop | -2.36 |
| fre | 69.8 |
| fre_gain | -16.9 |
| human_edit_recall | 1.000 |
| length_ratio | 0.71 |
| n_words | 10.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.044 |
| nli_faithfulness | 0.969 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 33.44 |
| smog | 3.13 |
| smog_drop | 0.00 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `active Crohn 's disease` -> `gut disease` | replace | - | - | - | - | - | - | - |
| `colonoscopy` -> `bowel exam` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** No currently happening Crohn's disease was found during the large intestine exam.

| metric | value |
|---|---:|
| bertscore_f1 | 0.581 |
| coleman_liau | 14.60 |
| coleman_liau_drop | -4.94 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.667 |
| fkgl | 9.74 |
| fkgl_drop | -6.09 |
| fre | 46.6 |
| fre_gain | -40.1 |
| human_edit_recall | 1.000 |
| length_ratio | 0.93 |
| n_words | 13.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.536 |
| nli_faithfulness | 0.956 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 41.10 |
| smog | 13.02 |
| smog_drop | -9.89 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `active` -> `currently happening` | replace | attributed | 5.356 | 5.356 | 0.777 | 0.860 | 0.761 | 1.3967985600000006 |
| `colonoscopy` -> `large intestine exam` | replace | attributed | 4.967 | 4.987 | 0.630 | 0.836 | 1.990 | 1.9665715640000005 |

**edit `active` -> `currently happening`**

- status: `attributed`
- log p full -9.0811, empty -14.4375
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+2.446` [readme] active: Currently happening.
    - `+1.685` [readme] Active: Happening right now.
    - `+1.596` [wiktionary] active: Something is active if it is turned on or started.
    - `+0.875` [justplainclear] active: Moving; changing; keeping busy

- rationale: The readme defines "active" as something currently happening, so replacing it with "currently happening" preserves that exact meaning in everyday language. Word frequency changes from Zipf 4.93 to 4.62, and age of acquisition rises from 6.53 to 8.22. This clear substitution allows you to instantly understand your condition's status without decoding medical jargon.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `colonoscopy` -> `large intestine exam`**

- status: `attributed`
- log p full -3.9067, empty -8.8735
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+3.625` [justplainclear] colonoscopy: An exam of the inside of the large intestine that uses a flexible tube with a lens at the end
    - `+1.636` [readme] colonoscopy: A procedure to check for colon cancer by examining the inside of the large intestine.
    - `+0.747` [readme] colonoscopy: A colonoscopy is a test that checks the inside of your large intestine for signs of cancer.
    - `+0.710` [readme] Active: Happening right now.
    - `+0.594` [michigan] colonoscopy: Looks at the inside of the large intestine using a flexible tube with a ltiny camera at the end.

- rationale: The justplainclear glossary defines colonoscopy as an internal inspection of the large intestine using a flexible tube, so "large intestine exam" preserves that core idea in everyday language. Phrase frequency increases from Zipf 2.74 to 3.19, while age of acquisition falls from 15.76 to 9.28, marking a clear shift toward more common and younger-learned vocabulary. Patients can now grasp the procedure’s purpose without needing to memorize a specialized medical label.
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

**output:** Not long after the first check-up, the patient started saying they had chest pain and looked to the nurse like they were getting very tired and having trouble breathing.

| metric | value |
|---|---:|
| bertscore_f1 | 0.647 |
| coleman_liau | 10.78 |
| coleman_liau_drop | 5.19 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.250 |
| fkgl | 12.00 |
| fkgl_drop | 4.36 |
| fre | 60.7 |
| fre_gain | 34.8 |
| human_edit_recall | 1.000 |
| length_ratio | 1.07 |
| n_words | 30.0 |
| nli_completeness | 0.993 |
| nli_faithfulness | 0.994 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.636 |
| sari | 17.51 |
| smog | 3.13 |
| smog_drop | 12.77 |
| temporality_preservation | 1.000 |

### Stage 4 - arm `termonly`

**output:** Shortly after the patient's initial assessment, the patient apparently began to complain of chest pain and appeared to the nurse to have increasing tiredness and trouble breathing.

| metric | value |
|---|---:|
| bertscore_f1 | 0.897 |
| coleman_liau | 15.54 |
| coleman_liau_drop | 0.43 |
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
| nli_completeness | 0.995 |
| nli_faithfulness | 0.994 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 63.09 |
| smog | 15.90 |
| smog_drop | 0.00 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `mounting exhaustion` -> `increasing tiredness` | replace | - | - | - | - | - | - | - |
| `respiratory distress` -> `trouble breathing` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Shortly after the patient's initial assessment, the patient apparently began to complain of chest pain and appeared to the nurse to have increasing tiredness and difficulty breathing.

| metric | value |
|---|---:|
| bertscore_f1 | 0.901 |
| coleman_liau | 16.19 |
| coleman_liau_drop | -0.21 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 16.35 |
| fkgl_drop | 0.00 |
| fre | 25.9 |
| fre_gain | 0.0 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 28.0 |
| nli_completeness | 0.995 |
| nli_faithfulness | 0.994 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 63.09 |
| smog | 17.12 |
| smog_drop | -1.22 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `mounting exhaustion` -> `increasing tiredness` | replace | attributed | 0.001 | 0.001 | - | 0.606 | 0.237 | 0.43727108999999986 |
| `respiratory distress` -> `difficulty breathing` | replace | attributed | 1.294 | 1.885 | - | 0.888 | 1.698 | 1.557007248 |

**edit `mounting exhaustion` -> `increasing tiredness`**

- status: `attributed`
- log p full -2.6337, empty -2.6345
- masks scored: 34/34 (+3 top-k)
- ranked sources:
    - `+0.322` [readme] Respiratory Distress: Having difficulty breathing.
    - `+0.084` [wiktionary] mounting: If you mount something you get on to it.
    - `+0.015` [wiktionary] exhaustion: Exhaustion is the point where something is completely depleted.
    - `-0.109` [wiktionary] exhaustion: Exhaustion is the state of extreme tiredness.

- rationale: "Mounting exhaustion" describes a steadily worsening fatigue that builds over time, and "increasing tiredness" preserves this core idea by using everyday words that clearly convey a gradual deepening of fatigue. Phrase frequency changes from Zipf 3.34 to 2.91, with higher values meaning more common and easier wording, while age of acquisition changes from 7.61 to 7.22, with lower values meaning words learned younger and more easily. You can now grasp the exact nature of your symptom without needing to decode clinical jargon.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `respiratory distress` -> `difficulty breathing`**

- status: `attributed`
- log p full -0.6413, empty -1.9348
- masks scored: 34/34 (+3 top-k)
- ranked sources:
    - `+1.721` [readme] Respiratory Distress: Having difficulty breathing.
    - `+0.023` [wiktionary] mounting: If you mount something you get on to it.
    - `-0.131` [readme] acute respiratory distress syndrome: A serious lung condition that causes low levels of oxygen in the blood, w

- rationale: "Respiratory distress" describes a state where the body struggles to get enough oxygen, and swapping it for "difficulty breathing" preserves that core idea while using everyday words. Phrase frequency increases from Zipf 3.57 to 4.00, while age of acquisition falls from 11.16 to 6.83, making the new phrasing both more common and easier to learn. You can now grasp the urgency of your symptoms without needing to decode clinical jargon.
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

**output:** She has been sent to see a doctor to have a pacemaker put in her heart.

| metric | value |
|---|---:|
| bertscore_f1 | 0.589 |
| coleman_liau | 2.29 |
| coleman_liau_drop | 9.39 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 4.66 |
| fkgl_drop | 3.52 |
| fre | 90.1 |
| fre_gain | 39.5 |
| human_edit_recall | 1.000 |
| length_ratio | 1.78 |
| n_words | 16.0 |
| nli_completeness | 0.993 |
| nli_faithfulness | 0.904 |
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

**output:** She has been sent to see another doctor for surgery to place a heart device.

| metric | value |
|---|---:|
| bertscore_f1 | 0.611 |
| coleman_liau | 5.81 |
| coleman_liau_drop | 5.86 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.750 |
| fkgl | 6.78 |
| fkgl_drop | 1.40 |
| fre | 73.2 |
| fre_gain | 22.5 |
| human_edit_recall | 1.000 |
| length_ratio | 1.67 |
| n_words | 15.0 |
| nli_completeness | 0.271 |
| nli_faithfulness | 0.559 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 23.18 |
| smog | 11.21 |
| smog_drop | 0.00 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `referred` -> `sent to see another doctor` | replace | attributed | 5.263 | 5.284 | 0.902 | 0.924 | 3.922 | 6.126885836 |
| `pacemaker implantation` -> `surgery to place a heart device` | replace | attributed | 6.109 | 6.114 | 0.774 | 0.785 | 0.480 | 0.5303133060000009 |

**edit `referred` -> `sent to see another doctor`**

- status: `attributed`
- log p full -3.9017, empty -9.1650
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+5.004` [readme] REFERRED: Sending a patient to another person or place for medical care.
    - `+1.082` [wiktionary] referred: If you refer to something, you talk or write about it, usually in passing.

- rationale: The readme explains that "referred" means sending a patient to another person or place for medical care, so "sent to see another doctor" preserves that core idea in everyday language. Phrase frequency increases from Zipf 4.61 to 4.65, making the wording slightly more common and easier to process. You can now grasp exactly how your care will move forward without needing to decode clinical jargon.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `pacemaker implantation` -> `surgery to place a heart device`**

- status: `attributed`
- log p full -5.3796, empty -11.4887
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+2.486` [readme] implantation: Surgery where a device is placed inside your body.
    - `+2.006` [readme] IMPLANTATION: A surgery where a device is placed inside the body.
    - `+0.839` [readme] pacemaker: A small device that helps regulate the heartbeat when placed in the chest.
    - `+0.809` [nih] pacemaker: An electronic device that is implanted in the body to monitor heart rate and rhythm. It gives the h
    - `+0.783` [readme] REFERRED: Sending a patient to another person or place for medical care.

- rationale: The readme explains that the original term refers to a surgery where a device is placed inside your body, so "surgery to place a heart device" keeps that exact idea in plain language. Phrase frequency increases from Zipf 2.69 to 4.29, while age of acquisition drops from 12.42 to 8.06. You can now clearly understand what the medical procedure actually involves without needing to look up specialized terminology.
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

**output:** The patient had some bruising at the catheter site.

| metric | value |
|---|---:|
| bertscore_f1 | 0.670 |
| coleman_liau | 7.98 |
| coleman_liau_drop | -3.55 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 4.96 |
| fkgl_drop | -5.63 |
| fre | 75.5 |
| fre_gain | -38.6 |
| human_edit_recall | 1.000 |
| length_ratio | 0.69 |
| n_words | 9.0 |
| nli_completeness | 0.357 |
| nli_faithfulness | 0.758 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 42.43 |
| smog | 8.84 |
| smog_drop | -5.71 |

### Stage 4 - arm `termonly`

**output:** There was some bruise at the tube spot.

| metric | value |
|---|---:|
| bertscore_f1 | 0.500 |
| coleman_liau | 2.98 |
| coleman_liau_drop | 1.45 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.333 |
| fkgl | -0.67 |
| fkgl_drop | 0.00 |
| fre | 114.1 |
| fre_gain | 0.0 |
| human_edit_recall | 1.000 |
| length_ratio | 0.62 |
| n_words | 8.0 |
| nli_completeness | 0.253 |
| nli_faithfulness | 0.187 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 54.80 |
| smog | 3.13 |
| smog_drop | 0.00 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `hematoma` -> `bruise` | replace | - | - | - | - | - | - | - |
| `cath site` -> `tube spot` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** There was some bruise at the catheter spot.

| metric | value |
|---|---:|
| bertscore_f1 | 0.692 |
| coleman_liau | 5.88 |
| coleman_liau_drop | -1.45 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.333 |
| fkgl | 2.28 |
| fkgl_drop | -2.95 |
| fre | 93.0 |
| fre_gain | -21.1 |
| human_edit_recall | 1.000 |
| length_ratio | 0.62 |
| n_words | 8.0 |
| nli_completeness | 0.438 |
| nli_faithfulness | 0.432 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 58.86 |
| smog | 8.84 |
| smog_drop | -5.71 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `hematoma` -> `bruise` | replace | attributed | 1.459 | 1.558 | 0.854 | 0.817 | 1.061 | 0.6482515599999998 |
| `cath site` -> `catheter spot` | replace | attributed | -0.609 | -0.621 | 0.902 | 0.926 | 0.049 | 1.389840614999999 |

**edit `hematoma` -> `bruise`**

- status: `attributed`
- log p full -2.1192, empty -3.5778
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+1.497` [iowa] HEMATOMA: a bruise, a black and blue mark
    - `+0.436` [michigan] hematoma: A bruise or when your skin is black and blue after an injury.
    - `+0.253` [wiktionary] site: A site is a location or a place.
    - `+0.189` [wiktionary] site: A site is a website.
    - `-0.537` [justplainclear] hematoma: A collection of blood under the skin or in the body that is typically caused by a broken blood vesse

- rationale: The Iowa glossary describes hematoma as a bruise, a black and blue mark, so replacing it with "bruise" keeps that straightforward visual meaning in plain language. Phrase frequency increases from Zipf 2.61 to 3.18, while age of acquisition falls from 14.78 to 5.45. You can now easily recognize the physical change on your body without first decoding a specialized medical label.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `cath site` -> `catheter spot`**

- status: `attributed`
- log p full -4.2611, empty -3.6525
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.846` [nih] hematoma: A pool of clotted or partially clotted blood in an organ, tissue, or body space, usually caused by a
    - `+0.797` [justplainclear] hematoma: A collection of blood under the skin or in the body that is typically caused by a broken blood vesse
    - `+0.094` [michigan] hematoma: A bruise or when your skin is black and blue after an injury.
    - `-0.028` [wiktionary] site: A site is a website.
    - `-0.321` [iowa] HEMATOMA: a bruise, a black and blue mark

- rationale: "Cath site" refers to the exact location where a thin tube was inserted into your vein, and swapping it for "catheter spot" keeps that same idea while using everyday words. Phrase frequency increases from Zipf 2.90 to 3.23, so the higher value means the wording is more common and easier to encounter, while age of acquisition shifts from 8.63 to 14.37, indicating the new phrase is learned later but still more straightforward. With this clearer wording, you can easily picture where the tube was placed without needing to decode medical shorthand.
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

**output:** The dead tissue was removed from the abdomen.

| metric | value |
|---|---:|
| bertscore_f1 | 0.742 |
| coleman_liau | 7.33 |
| coleman_liau_drop | 0.01 |
| copy_jargon_rate | 0.333 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| diagnostic_identity_preservation | 1.000 |
| fkgl | 5.23 |
| fkgl_drop | 1.05 |
| fre | 71.8 |
| fre_gain | 5.7 |
| human_edit_recall | 0.667 |
| length_ratio | 0.89 |
| n_words | 8.0 |
| nli_completeness | 0.992 |
| nli_faithfulness | 0.994 |
| replacement_f1 | 0.800 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.667 |
| sari | 25.95 |
| smog | 8.84 |
| smog_drop | 0.00 |

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
| `necrotic tissue` -> `dead tissue` | replace | attributed | -0.970 | -1.090 | 0.197 | 0.776 | 0.001 | -0.10708534999999975 |

**edit `necrotic tissue` -> `dead tissue`**

- status: `attributed`
- log p full -2.7430, empty -1.7726
- masks scored: 66/66 (+2 top-k)
- ranked sources:
    - `+0.001` [readme] TISSUE: A bunch of cells teaming up to do a job.
    - `-0.005` [justplainclear] tissue: A group of cells in the body that are alike. Organs, muscles, skin and other body parts are made up of
    - `-0.024` [nih] tissue: A group or layer of cells that work together to perform a specific function.
    - `-0.039` [wiktionary] tissue: A piece of tissue is a sheet of paper that can absorb very well.

- rationale: Necrotic tissue refers to cells that have lost their function and begun to break down, so swapping it for dead tissue preserves that core idea while using everyday language. Phrase frequency increases from Zipf 2.54 to 4.26, while age of acquisition falls from 15.07 to 5.17, making the updated phrasing both more common and easier to learn. You can now grasp the exact nature of the injury without needing to decode specialized medical jargon.
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

**output:** The patient kept pressure on the area and the bleeding stopped.

| metric | value |
|---|---:|
| bertscore_f1 | 0.620 |
| coleman_liau | 8.93 |
| coleman_liau_drop | -0.88 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 5.86 |
| fkgl_drop | 0.84 |
| fre | 72.6 |
| fre_gain | 11.4 |
| human_edit_recall | 1.000 |
| length_ratio | 1.38 |
| n_words | 11.0 |
| nli_completeness | 0.542 |
| nli_faithfulness | 0.204 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 27.11 |
| smog | 8.84 |
| smog_drop | 2.37 |

### Stage 4 - arm `termonly`

**output:** Pressure was held and the area was not bleeding.

| metric | value |
|---|---:|
| bertscore_f1 | 0.828 |
| coleman_liau | 6.04 |
| coleman_liau_drop | 2.01 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 4.96 |
| fkgl_drop | 1.74 |
| fre | 75.5 |
| fre_gain | 14.3 |
| human_edit_recall | 1.000 |
| length_ratio | 1.12 |
| n_words | 9.0 |
| nli_completeness | 0.530 |
| nli_faithfulness | 0.713 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 67.96 |
| smog | 8.84 |
| smog_drop | 2.37 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `hemostatic` -> `not bleeding` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Pressure was held and the area had stopped bleeding.

| metric | value |
|---|---:|
| bertscore_f1 | 0.923 |
| coleman_liau | 8.62 |
| coleman_liau_drop | -0.57 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 4.96 |
| fkgl_drop | 1.74 |
| fre | 75.5 |
| fre_gain | 14.3 |
| human_edit_recall | 1.000 |
| length_ratio | 1.12 |
| n_words | 9.0 |
| nli_completeness | 0.585 |
| nli_faithfulness | 0.304 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 76.67 |
| smog | 8.84 |
| smog_drop | 2.37 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `hemostatic` -> `stopped bleeding` | replace | attributed | 0.557 | 0.568 | - | 0.400 | 0.306 | -0.16124735700000015 |

**edit `hemostatic` -> `stopped bleeding`**

- status: `attributed`
- log p full -3.6997, empty -4.2567
- masks scored: 6/6 (+1 top-k)
- ranked sources:
    - `+0.363` [readme] hemostatic: Stopping blood flow.
    - `+0.057` [readme] hemostatic: Hemostatic means stopping bleeding.

- rationale: The term hemostatic describes a property that halts or controls blood flow, so replacing it with stopped bleeding preserves that core idea while speaking in plain language. Phrase frequency increases from Zipf 1.73 to 4.01, meaning the new phrasing is more common and easier to process. You can now clearly see what the medical intervention actually does without needing to memorize a technical label.
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

**output:** The area was washed with some salt water and made clean.

| metric | value |
|---|---:|
| bertscore_f1 | 0.822 |
| coleman_liau | 5.24 |
| coleman_liau_drop | 2.10 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 3.72 |
| fkgl_drop | -0.06 |
| fre | 88.0 |
| fre_gain | 3.1 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 11.0 |
| nli_completeness | 0.989 |
| nli_faithfulness | 0.989 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 70.03 |
| smog | 8.84 |
| smog_drop | 0.00 |

### Stage 4 - arm `termonly`

**output:** The area was rinsed with some salt water and cleared.

| metric | value |
|---|---:|
| bertscore_f1 | 0.800 |
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
| nli_completeness | 0.984 |
| nli_faithfulness | 0.987 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 75.42 |
| smog | 8.84 |
| smog_drop | 0.00 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `lavaged` -> `rinsed` | replace | - | - | - | - | - | - | - |
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
| `lavaged` -> `cleaned` | replace | attributed | 1.632 | 2.691 | - | 0.923 | 2.794 | 1.540894242 |
| `saline` -> `salt water` | replace | attributed | -2.154 | -2.862 | - | 0.765 | 0.447 | 1.2916119200000002 |

**edit `lavaged` -> `cleaned`**

- status: `attributed`
- log p full -0.3558, empty -1.9883
- masks scored: 34/34 (+4 top-k)
- ranked sources:
    - `+2.794` [readme] lavaged: To clean out an organ or wound with fluid.
    - `-0.196` [wiktionary] saline: If something is saline it is salty, especially water containing salt.

- rationale: The original term refers to a thorough washing or rinsing of a body cavity, so replacing it with "cleaned" keeps that essential idea of removing unwanted material in everyday language. Word frequency increases from Zipf 0.00 to 4.02, while the syllable count remains unchanged at 1. You can now understand the procedure’s purpose without needing to decode a specialized medical term.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `saline` -> `salt water`**

- status: `attributed`
- log p full -2.7739, empty -0.6199
- masks scored: 34/34 (+4 top-k)
- ranked sources:
    - `+0.447` [readme] Saline: Salt water solution used to replace body fluids.
    - `-0.010` [nih] saline: A solution of salt and water.
    - `-1.011` [readme] saline: A solution made of saltwater that matches the body's fluid concentration and can be used to replace lo
    - `-1.517` [readme] lavaged: To clean out an organ or wound with fluid.

- rationale: Saline refers to a clear liquid made by dissolving salt in water, so switching to "salt water" preserves that exact composition while using everyday language. Phrase frequency increases from Zipf 3.33 to 4.55, while age of acquisition falls from 11.71 to 5.05. You can now picture exactly what the solution contains without needing to memorize a clinical label.
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

**output:** He came in because he was in pain and could not walk.

| metric | value |
|---|---:|
| bertscore_f1 | 0.369 |
| coleman_liau | 1.55 |
| coleman_liau_drop | 6.50 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 1.87 |
| fkgl_drop | 6.31 |
| fre | 103.0 |
| fre_gain | 52.3 |
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

**output:** Pain and being unable to walk brought him in.

| metric | value |
|---|---:|
| bertscore_f1 | 0.762 |
| coleman_liau | 4.11 |
| coleman_liau_drop | 3.94 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.333 |
| fkgl | 3.65 |
| fkgl_drop | 4.53 |
| fre | 84.9 |
| fre_gain | 34.2 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 9.0 |
| nli_completeness | 0.978 |
| nli_faithfulness | 0.992 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 38.11 |
| smog | 8.84 |
| smog_drop | 2.37 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `inability to ambulate` -> `being unable to walk` | replace | - | - | - | - | - | - | - |

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
| `inability to ambulate` -> `not being able to walk` | replace | attributed | 1.487 | 1.667 | 0.931 | 0.971 | 0.716 | 0.8311254399999994 |

**edit `inability to ambulate` -> `not being able to walk`**

- status: `attributed`
- log p full -1.5932, empty -3.0803
- masks scored: 66/66 (+2 top-k)
- ranked sources:
    - `+1.306` [michigan] inability: Not able to.
    - `+0.590` [wiktionary] inability: An inability is something that you can not do.
    - `+0.121` [wiktionary] ambulate: If you ambulate yourself, you relocate yourself under the power of your own legs.

- rationale: The Michigan glossary defines the original term as simply "not able to," so "not being able to walk" preserves that straightforward idea in everyday language. Phrase frequency increases from Zipf 1.40 to 4.87, while age of acquisition decreases from 10.67 to 7.79, marking a clear shift toward more common and earlier-learned language. You can now grasp the core mobility issue without needing to decode clinical jargon.
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

**output:** There is an organ bulging through a weak muscle on the left side.

| metric | value |
|---|---:|
| bertscore_f1 | 0.469 |
| coleman_liau | 5.12 |
| coleman_liau_drop | -5.05 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 4.00 |
| fkgl_drop | -1.72 |
| fre | 89.5 |
| fre_gain | -3.5 |
| human_edit_recall | 1.000 |
| laterality_preservation | 1.000 |
| length_ratio | 1.08 |
| n_words | 13.0 |
| nli_completeness | 0.125 |
| nli_faithfulness | 0.828 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 64.59 |
| smog | 3.13 |
| smog_drop | 5.71 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `hernia` -> `organ bulging through a weak muscle` | replace | attributed | 17.704 | 17.706 | - | 0.952 | 1.251 | 2.3005318805000003 |

**edit `hernia` -> `organ bulging through a weak muscle`**

- status: `attributed`
- log p full -6.0369, empty -23.7406
- masks scored: 10/10 (+2 top-k)
- ranked sources:
    - `+9.022` [justplainclear] hernia: When part of an organ or tissue inside of you bulges through a weak area of muscle. Most hernias are i
    - `+7.772` [nih] hernia: The bulging of an internal organ through a weak area or tear in the muscle or other tissue that holds 
    - `+1.530` [readme] hernia: A hernia is when an organ pokes through a hole in a muscle.

- rationale: A hernia refers to a part of the body pushing out of its normal position, so describing it as an organ bulging through a weak muscle keeps that core idea in everyday language. Phrase frequency shifts from Zipf 3.00 to 2.97, while age of acquisition falls from 12.29 to 8.72, indicating a move toward more familiar and earlier-learned vocabulary. You can now picture exactly what is happening in your body without needing to memorize a clinical label.
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

**output:** The patient's other body systems were checked and found to be normal.

| metric | value |
|---|---:|
| bertscore_f1 | 0.577 |
| coleman_liau | 8.80 |
| coleman_liau_drop | 2.60 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 5.81 |
| fkgl_drop | 2.56 |
| fre | 74.8 |
| fre_gain | 21.9 |
| human_edit_recall | 1.000 |
| length_ratio | 1.30 |
| n_words | 13.0 |
| negation_preservation | 0.000 |
| nli_completeness | 0.986 |
| nli_faithfulness | 0.498 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 29.42 |
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
| `unremarkable` -> `common and ordinary` | replace | attributed | 17.021 | 17.611 | - | - | - | 17.020538694 |

**edit `unremarkable` -> `common and ordinary`**

- status: `attributed`
- log p full -0.8078, empty -17.8283
- masks scored: 4/4 (+1 top-k)
- ranked sources:
    - `+17.564` [wiktionary] unremarkable: If something is unremarkable, it is common and ordinary.

- rationale: The original term simply describes something that lacks any notable features, so replacing it with "common and ordinary" preserves that straightforward idea in everyday language. Phrase frequency increases from Zipf 2.83 to 4.35, while age of acquisition falls from 11.06 to 8.63, making the phrasing both more common and easier to learn. You can now understand the clinical observation without first learning specialized medical vocabulary.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True
