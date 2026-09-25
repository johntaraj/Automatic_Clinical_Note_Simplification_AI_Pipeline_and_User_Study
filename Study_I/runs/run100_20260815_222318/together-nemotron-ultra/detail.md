# Step-by-step detail - together-nemotron-ultra (`run100_20260815_222318`)

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

**output:** He lost interest in things he used to enjoy and stopped wanting to be around people, and he had trouble sleeping because he kept waking up and felt restless.

| metric | value |
|---|---:|
| bertscore_f1 | 0.487 |
| coleman_liau | 8.58 |
| coleman_liau_drop | 10.39 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 11.59 |
| fkgl_drop | 4.44 |
| fre | 63.6 |
| fre_gain | 53.2 |
| human_edit_recall | 1.000 |
| length_ratio | 1.45 |
| n_words | 29.0 |
| nli_completeness | 0.983 |
| nli_faithfulness | 0.992 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.750 |
| sari | 11.77 |
| smog | 3.13 |
| smog_drop | 12.77 |

### Stage 4 - arm `termonly`

**output:** He lost interest in things he used to enjoy and stopped caring about social activities, and had trouble sleeping because he woke up often and felt restless.

| metric | value |
|---|---:|
| bertscore_f1 | 0.556 |
| coleman_liau | 10.60 |
| coleman_liau_drop | 8.36 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 12.42 |
| fkgl_drop | 3.61 |
| fre | 54.1 |
| fre_gain | 43.7 |
| human_edit_recall | 1.000 |
| length_ratio | 1.35 |
| n_words | 27.0 |
| nli_completeness | 0.983 |
| nli_faithfulness | 0.991 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.714 |
| sari | 19.71 |
| smog | 8.84 |
| smog_drop | 7.06 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `anhedonic` -> `lost interest in things he used to enjoy` | replace | - | - | - | - | - | - | - |
| `disinterested` -> `stopped caring` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** He lost interest in things he used to enjoy and stopped caring about social activities, and had trouble sleeping because he woke up often and felt restless.

| metric | value |
|---|---:|
| bertscore_f1 | 0.556 |
| coleman_liau | 10.60 |
| coleman_liau_drop | 8.36 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 12.42 |
| fkgl_drop | 3.61 |
| fre | 54.1 |
| fre_gain | 43.7 |
| human_edit_recall | 1.000 |
| length_ratio | 1.35 |
| n_words | 27.0 |
| nli_completeness | 0.983 |
| nli_faithfulness | 0.991 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.714 |
| sari | 19.71 |
| smog | 8.84 |
| smog_drop | 7.06 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `anhedonic` -> `lost interest in things he used to enjoy` | replace | attributed | -0.266 | -0.360 | - | 0.447 | 0.104 | - |
| `disinterested` -> `stopped caring` | replace | attributed | 0.103 | 0.237 | - | 0.400 | 0.072 | - |

**edit `anhedonic` -> `lost interest in things he used to enjoy`**

- status: `attributed`
- log p full -1.4826, empty -1.2165
- masks scored: 6/6 (+1 top-k)
- ranked sources:
    - `-0.104` [wiktionary] disinterested: If someone is disinterested, they are not affected by a situation, so they can make fair decisi

- rationale: "Anhedonic" describes a state in which someone no longer feels pleasure or interest in activities they once enjoyed, and the replacement spells that out in everyday language. Phrase frequency rises from Zipf 1.11 to 4.64, showing the new wording is far more common. Readers can now grasp the symptom immediately without needing a clinical vocabulary.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `disinterested` -> `stopped caring`**

- status: `attributed`
- log p full -0.5205, empty -0.6234
- masks scored: 6/6 (+1 top-k)
- ranked sources:
    - `+0.185` [wiktionary] disinterested: If someone is disinterested, they are not interested in something; they find it boring.
    - `+0.113` [wiktionary] disinterested: If someone is disinterested, they are not affected by a situation, so they can make fair decisi

- rationale: "Disinterested" means having lost interest or concern, and "stopped caring" expresses that same shift in plain, everyday language. Phrase frequency rises from Zipf 2.91 to 4.11, while the syllable count drops from four to three. Readers can now grasp the idea of waning engagement without pausing to decode a more formal word.
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
| `Myocardial infarction` -> `heart attack` | replace | attributed | 0.000 | 1.313 | 0.511 | 0.870 | 0.245 | - |
| `can not be excluded` -> `ruled out` | replace | attributed | -0.000 | -0.016 | 0.411 | 0.839 | 0.076 | - |

**edit `Myocardial infarction` -> `heart attack`**

- status: `attributed`
- log p full -0.0001, empty -0.0002
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.594` [iowa] MYOCARDIAL INFARCTION: heart attack
    - `+0.349` [justplainclear] myocardial infarction: A heart attack
    - `+0.146` [readme] inferior myocardial infarction: A heart attack caused by a blockage in a blood vessel that affects the lower p
    - `+0.048` [wiktionary] excluded: If you exclude someone or something, you keep them out.
    - `+0.007` [wiktionary] can: If someone can do something, they are able to do it.

- rationale: Myocardial infarction is the medical name for a heart attack, so the replacement uses the everyday term that patients already recognize. Phrase frequency rises from Zipf 2.58 to 4.89, and age of acquisition drops from 16.64 to 6.58. Readers can immediately grasp the urgency and nature of the condition without decoding clinical terminology.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `can not be excluded` -> `ruled out`**

- status: `attributed`
- log p full -0.0006, empty -0.0005
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.305` [michigan] myocardial infarction: Occurs when the flow of blood to the heart is stopped by a blood clot or a spasm of an 
    - `+0.229` [iowa] MYOCARDIAL INFARCTION: heart attack
    - `+0.214` [wiktionary] excluded: If you exclude someone or something, you keep them out.
    - `+0.108` [wiktionary] be: Go somewhere; visit someone (only in the perfect tense).

- rationale: "Cannot be excluded" means a possibility remains open because there is not enough evidence to dismiss it, and "ruled out" conveys the same idea in two familiar words. Phrase frequency rises from Zipf 3.89 to 4.30, while age of acquisition drops from 5.11 to 3.28. Readers can now grasp the uncertainty immediately without wading through a formal, multi-word construction.
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

**output:** There was a large bruise and swelling in the fluid-filled sac under the deltoid muscle.

| metric | value |
|---|---:|
| bertscore_f1 | 0.493 |
| coleman_liau | 9.68 |
| coleman_liau_drop | 4.62 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 6.78 |
| fkgl_drop | -0.77 |
| fre | 73.2 |
| fre_gain | 3.4 |
| human_edit_recall | 1.000 |
| length_ratio | 1.14 |
| n_words | 16.0 |
| nli_completeness | 0.974 |
| nli_faithfulness | 0.885 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.200 |
| sari | 39.14 |
| severity_downgrade | 0.000 |
| severity_preservation | 1.000 |
| severity_tier_input | 2.000 |
| severity_tier_output | 2.000 |
| smog | 8.84 |
| smog_drop | 0.00 |

### Stage 4 - arm `termonly`

**output:** There was a large collection of blood and swelling in the fluid sac under the shoulder muscle.

| metric | value |
|---|---:|
| bertscore_f1 | 0.699 |
| coleman_liau | 8.73 |
| coleman_liau_drop | 5.57 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 7.70 |
| fkgl_drop | -1.69 |
| fre | 70.1 |
| fre_gain | 0.4 |
| human_edit_recall | 1.000 |
| length_ratio | 1.21 |
| n_words | 17.0 |
| nli_completeness | 0.770 |
| nli_faithfulness | 0.774 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.200 |
| sari | 49.35 |
| severity_downgrade | 0.000 |
| severity_preservation | 1.000 |
| severity_tier_input | 2.000 |
| severity_tier_output | 2.000 |
| smog | 8.84 |
| smog_drop | 0.00 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `marked` -> `large` | replace | - | - | - | - | - | - | - |
| `hematoma` -> `collection of blood` | replace | - | - | - | - | - | - | - |
| `subdeltoid bursa` -> `fluid sac under the shoulder muscle` | replace | - | - | - | - | - | - | - |

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
| `marked` -> `large` | replace | attributed | -0.028 | -0.665 | 0.075 | 0.571 | 0.128 | - |
| `hematoma` -> `bruise` | replace | attributed | 0.980 | 3.657 | 0.923 | 0.920 | 1.438 | - |
| `subdeltoid bursa` -> `fluid sac under the shoulder muscle` | replace | attributed | 0.349 | 0.652 | 0.567 | 0.664 | 0.247 | - |

**edit `marked` -> `large`**

- status: `attributed`
- log p full -0.0584, empty -0.0305
- masks scored: 66/66 (+5 top-k)
- ranked sources:
    - `+0.199` [justplainclear] bursa: A small sac (pouch) found in your body which is filled with fluid. Bursa help your tendons or muscles m
    - `+0.071` [wiktionary] marked: A mark is a single line left by a pen or pencil, or any small bit of color that got onto something.
    - `+0.058` [justplainclear] hematoma: A collection of blood under the skin or in the body that is typically caused by a broken blood vesse
    - `+0.007` [readme] bursa: A small sac of fluid that cushions joints as they move.
    - `-0.008` [iowa] HEMATOMA: a bruise, a black and blue mark

- rationale: In this context "marked" means noticeably big or distinct, and "large" conveys that same sense of size in a more familiar word. Word frequency rises from Zipf 4.50 to 5.39, while age of acquisition drops from 10.2 to 6.8. Readers can grasp the degree of change without pausing on a less common adjective.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `hematoma` -> `bruise`**

- status: `attributed`
- log p full -0.0451, empty -1.0249
- masks scored: 66/66 (+5 top-k)
- ranked sources:
    - `+3.437` [iowa] HEMATOMA: a bruise, a black and blue mark
    - `+1.999` [michigan] hematoma: A bruise or when your skin is black and blue after an injury.
    - `-0.152` [justplainclear] bursa: A small sac (pouch) found in your body which is filled with fluid. Bursa help your tendons or muscles m
    - `-0.549` [wiktionary] marked: A mark is a single line left by a pen or pencil, or any small bit of color that got onto something.

- rationale: The Iowa glossary defines hematoma as a bruise or a black-and-blue mark, so the word "bruise" preserves the exact meaning in everyday language. Phrase frequency rises from Zipf 2.61 to 3.18, and age of acquisition drops from 14.78 to 5.45. Readers can now recognize the injury immediately without needing a medical dictionary.
- audit: coverage 0.833, grounding_error=True, omission=False, source_ok=False, passage_ok=True

**edit `subdeltoid bursa` -> `fluid sac under the shoulder muscle`**

- status: `attributed`
- log p full -0.6057, empty -0.9548
- masks scored: 66/66 (+5 top-k)
- ranked sources:
    - `+0.765` [justplainclear] bursa: A small sac (pouch) found in your body which is filled with fluid. Bursa help your tendons or muscles m
    - `+0.518` [readme] bursa: A small sac of fluid that cushions joints as they move.
    - `+0.082` [wiktionary] marked: A mark is a single line left by a pen or pencil, or any small bit of color that got onto something.
    - `+0.079` [michigan] hematoma: A bruise or when your skin is black and blue after an injury.

- rationale: The subdeltoid bursa is a small, fluid-filled cushion that sits beneath the deltoid muscle of the shoulder, and "fluid sac under the shoulder muscle" describes that same structure using everyday words. Phrase frequency rises from Zipf 0.00 to 3.46, while age of acquisition drops from 15.78 to 9.00. Readers can now picture the anatomy and its location without needing specialized medical vocabulary.
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
| `hypertension` -> `high blood pressure` | replace | attributed | 0.000 | 0.506 | 0.424 | 0.638 | 0.007 | - |
| `hyperlipidemia` -> `high cholesterol` | replace | attributed | 0.278 | 3.294 | 0.788 | 0.903 | 2.572 | - |

**edit `hypertension` -> `high blood pressure`**

- status: `attributed`
- log p full -0.0003, empty -0.0005
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.129` [michigan] hypertension: When your low pressure (diastolic) is 90 or higher or the high pressure (systolic) is 140 or hig
    - `+0.122` [iowa] HYPERTENSION: high blood pressure
    - `+0.105` [readme] hypertension: High blood pressure is when the force of blood in the arteries is too high.
    - `+0.062` [nih] hypertension: A blood pressure of 140/90 or higher. Hypertension usually has no symptoms. It can harm the arte
    - `+0.010` [justplainclear] hyperlipidemia: High cholesterol

- rationale: Hypertension is the medical name for blood pressure that stays too high, and "high blood pressure" states that same condition in everyday words. Phrase frequency rises from Zipf 3.41 to 4.71, while age of acquisition drops from 16.28 to 8.95. Readers can now grasp the health concern immediately without needing to translate a clinical term.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `hyperlipidemia` -> `high cholesterol`**

- status: `attributed`
- log p full -0.0125, empty -0.2909
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+3.468` [justplainclear] hyperlipidemia: High cholesterol
    - `+0.896` [justplainclear] hypertension: Also known as: high blood pressure, HBP A condition of having high blood pressure for a long per
    - `+0.562` [iowa] HYPERTENSION: high blood pressure
    - `+0.132` [michigan] hyperlipidemia: High levels of fat or fat-like substances (cholesterol). Hyperlipidemia is also called high ch

- rationale: Hyperlipidemia refers to elevated levels of fats in the blood, and "high cholesterol" captures the most familiar form of that condition in everyday language. Phrase frequency rises from Zipf 1.95 to 3.72, making the wording substantially more common for readers. Patients can now recognize the core health concern without needing to decode a clinical term.
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

**output:** She said her bladder hurt when she peed and that she has had bladder infections that keep coming back.

| metric | value |
|---|---:|
| bertscore_f1 | 0.505 |
| coleman_liau | 7.98 |
| coleman_liau_drop | -1.16 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 6.73 |
| fkgl_drop | 2.17 |
| fre | 80.7 |
| fre_gain | 12.0 |
| human_edit_recall | 1.000 |
| length_ratio | 0.83 |
| n_words | 19.0 |
| nli_completeness | 0.977 |
| nli_faithfulness | 0.990 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 11.59 |
| smog | 8.84 |
| smog_drop | 2.37 |
| temporality_preservation | 0.000 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `bladder spasms` -> `bladder hurt` | replace | - | - | - | - | - | - | - |
| `urinated` -> `peed` | replace | - | - | - | - | - | - | - |
| `chronic UTIs` -> `bladder infections that keep coming back` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** She said her bladder hurt with sudden cramps when she peed and that she has had urinary infections that keep coming back.

| metric | value |
|---|---:|
| bertscore_f1 | 0.501 |
| coleman_liau | 8.95 |
| coleman_liau_drop | -2.14 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 9.08 |
| fkgl_drop | -0.19 |
| fre | 69.1 |
| fre_gain | 0.5 |
| human_edit_recall | 1.000 |
| length_ratio | 0.96 |
| n_words | 22.0 |
| nli_completeness | 0.993 |
| nli_faithfulness | 0.989 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 12.28 |
| smog | 11.21 |
| smog_drop | 0.00 |
| temporality_preservation | 0.000 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `bladder spasms` -> `bladder hurt with sudden cramps` | replace | attributed | 7.692 | 7.747 | 0.752 | 0.853 | 3.644 | - |
| `urinated` -> `peed` | replace | attributed | 0.781 | 2.676 | 0.473 | 0.805 | 0.365 | - |
| `chronic UTIs` -> `urinary infections that keep coming back` | replace | attributed | 2.333 | 2.445 | 0.752 | 0.918 | 0.809 | - |

**edit `bladder spasms` -> `bladder hurt with sudden cramps`**

- status: `attributed`
- log p full -2.9135, empty -10.6051
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+5.409` [wiktionary] spasms: A spasm is a sudden and jerky movement.
    - `+1.765` [readme] UTIs: UTIs are infections in the urinary system.
    - `+1.327` [readme] spasms: When your muscles suddenly tighten up and hurt.
    - `+1.324` [readme] chronic: An ongoing or frequently recurring health issue.
    - `+0.941` [michigan] bladder: A hollow organ that stores pee (urine).

- rationale: The glossary defines a spasm as a sudden, jerky movement, so "bladder hurt with sudden cramps" keeps that core idea while using everyday words. Phrase frequency rises from Zipf 2.89 to 3.11, while age of acquisition stays at 10.78. Readers can now picture the sharp, brief pain without needing the clinical term.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `urinated` -> `peed`**

- status: `attributed`
- log p full -0.0916, empty -0.8726
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+1.305` [readme] bladder: A bladder is a sac in your body that holds pee.
    - `+0.940` [readme] BLADDER: Bladder: Holds pee in your body.
    - `+0.877` [michigan] bladder: A hollow organ that stores pee (urine).
    - `+0.370` [justplainclear] bladder: An organ where urine collects so the body can get rid of it
    - `+0.317` [dorland] UTIs: urinary tract infections

- rationale: "Urinated" is the formal verb for passing urine, and "peed" conveys the same action in everyday language. Word frequency rises from Zipf 2.31 to 3.10, and the word shrinks from three syllables to one. Readers can grasp the bodily function immediately without stumbling over clinical terminology.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `chronic UTIs` -> `urinary infections that keep coming back`**

- status: `attributed`
- log p full -2.1578, empty -4.4909
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+1.549` [readme] UTIs: UTIs are infections in the urinary system.
    - `+0.741` [justplainclear] chronic: Long term, long lasting, lifelong, constant, never ending, never goes away, happens again and again
    - `+0.341` [justplainclear] bladder: An organ where urine collects so the body can get rid of it
    - `+0.061` [readme] Chronic: A long-lasting or recurring health issue.
    - `+0.020` [iowa] CHRONIC: continuing for a long time, ongoing

- rationale: The readme defines UTIs as infections in the urinary system, so "urinary infections that keep coming back" spells out both the location and the recurring nature in everyday words. Phrase frequency rises from Zipf 2.05 to 3.22, while age of acquisition shifts from 11.25 to 12.56. Readers can now grasp the condition without needing to decode the abbreviation or the clinical shorthand for "chronic."
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

**output:** The user's no effusion. The sentence: There was no instability of the knee and no effusion." The user wants me to rewrite the sentence. The user wants me to rewrite the sentence. The user wants me to rewrite the sentence. The user wants me to rewrite the sentence. The user wants me to rewrite the sentence. The user wants me to rewrite the sentence. The user wants me to rewrite the sentence. The user wants me to rewrite the sentence. The user wants me to rewrite the sentence. The user wants me to rewrite the sentence. The user wants me to rewrite the sentence. The user wants me to rewrite the sentence. The user wants me to rewrite the sentence. The user wants me to rewrite the sentence. The user wants me to rewrite the sentence. The user wants me to rewrite the sentence. The user wants me to rewrite the sentence. The user wants me to rewrite the sentence. The user wants me to rewrite the sentence. The user wants me to rewrite the sentence. The user wants me to rewrite the sentence. The user wants me to rewrite the sentence. The user wants me to rewrite the sentence. The user wants me to rewrite the sentence. The user wants me to rewrite the sentence. The user wants me to rewrite the sentence. The user wants me to rewrite the sentence. The user wants me to rewrite the sentence. The user wants me to rewrite the sentence. The user wants me to rewrite the sentence. The user wants me to rewrite the sentence. The user wants me to rewrite the sentence. The user wants me to rewrite the sentence. The user wants me to rewrite the sentence. The user wants me to rewrite the sentence. The user wants me to rewrite the sentence. The user wants me to rewrite the sentence. The user wants me to rewrite the sentence. The user wants me to rewrite the sentence. The user wants me to rewrite the sentence. The user wants me to rewrite the sentence. The user wants me to rewrite the sentence. The user wants me to rewrite the sentence. The user wants me to rewrite the sentence. The user wants me to rewrite the sentence. The user wants me to rewrite the sentence. The user wants me to rewrite the sentence. The user wants me to rewrite the sentence. The user wants me to rewrite the sentence. The user wants me to rewrite the sentence. The user wants me to rewrite the sentence. The user wants me to rewrite the sentence. The user wants me to rewrite the sentence. The user wants me to rewrite the sentence. The user wants me to rewrite the sentence. The user wants me to rewrite the sentence. The user wants me to rewrite the sentence. The user wants me to rewrite the sentence. The user wants me to rewrite the sentence. The user wants me to rewrite the sentence. The user wants me to rewrite the sentence. The user wants me to rewrite the sentence.

| metric | value |
|---|---:|
| bertscore_f1 | -0.416 |
| coleman_liau | 5.20 |
| coleman_liau_drop | 0.98 |
| copy_jargon_rate | 1.000 |
| critical_error | 0.000 |
| fkgl | 3.85 |
| fkgl_drop | 3.34 |
| fre | 81.7 |
| fre_gain | 20.4 |
| human_edit_recall | 0.000 |
| length_ratio | 46.64 |
| n_words | 513.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.985 |
| nli_faithfulness | 0.059 |
| replacement_f1 | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 31.21 |
| smog | 4.37 |
| smog_drop | 6.84 |

### Stage 4 - arm `termonly`

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

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `instability` -> `stable` | replace | - | - | - | - | - | - | - |
| `effusion` -> `swelling` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** The knee was stable and had no extra fluid.

| metric | value |
|---|---:|
| bertscore_f1 | 0.643 |
| coleman_liau | 2.82 |
| coleman_liau_drop | 3.36 |
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
| nli_faithfulness | 0.995 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 16.40 |
| smog | 3.13 |
| smog_drop | 8.08 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `instability` -> `stable` | replace | attributed | 0.161 | 0.395 | - | 0.800 | 0.734 | - |
| `effusion` -> `extra fluid` | replace | attributed | 2.324 | 2.902 | - | 1.000 | 3.347 | - |

**edit `instability` -> `stable`**

- status: `attributed`
- log p full -0.4471, empty -0.6081
- masks scored: 6/6 (+1 top-k)
- ranked sources:
    - `+0.034` [nih] effusion: An abnormal collection of fluid in hollow spaces or between tissues of the body. For example, a pleu
    - `-0.700` [wiktionary] instability: Instability is the condition of not being stable, which can make things uncertain or unsafe.

- rationale: Instability refers to a condition that is unsteady or likely to change without warning, and using "stable" flips the wording to describe the desired state of being steady and reliable. Phrase frequency rises from Zipf 3.71 to 4.48, while age of acquisition drops from 12.55 to 8.90. Readers can now grasp the concept by recognizing a familiar, everyday word instead of processing a longer, abstract noun.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `effusion` -> `extra fluid`**

- status: `attributed`
- log p full -0.7672, empty -3.0915
- masks scored: 6/6 (+1 top-k)
- ranked sources:
    - `+3.804` [nih] effusion: An abnormal collection of fluid in hollow spaces or between tissues of the body. For example, a pleu
    - `+0.456` [wiktionary] instability: Instability is the condition of not being stable, which can make things uncertain or unsafe.

- rationale: An effusion is an abnormal buildup of fluid in a body space, and "extra fluid" conveys that same idea in everyday words. Phrase frequency rises from Zipf 2.41 to 4.15, while age of acquisition drops from 14.29 to 7.94. Readers can now grasp the concept immediately without needing a medical dictionary.
- audit: coverage 1.0, grounding_error=True, omission=False, source_ok=False, passage_ok=True

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

**output:** Two days later, the pain went away and she has not had it again.

| metric | value |
|---|---:|
| bertscore_f1 | 0.844 |
| coleman_liau | 2.39 |
| coleman_liau_drop | 3.18 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 4.20 |
| fkgl_drop | 0.71 |
| fre | 89.9 |
| fre_gain | 6.9 |
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
| `resolved` -> `went away` | replace | attributed | -0.000 | -0.080 | - | 0.669 | 0.282 | - |
| `recurrence` -> `it come back` | replace | attributed | 0.039 | 0.805 | - | 0.890 | 0.613 | - |

**edit `resolved` -> `went away`**

- status: `attributed`
- log p full -0.0035, empty -0.0033
- masks scored: 34/34 (+4 top-k)
- ranked sources:
    - `+0.422` [wiktionary] resolved: To resolve means to create a solution for a problem.
    - `+0.140` [nih] recurrence: Cancer that has recurred (come back), usually after a period of time during which the cancer could
    - `-0.137` [readme] recurrence: When a disease comes back after being treated.
    - `-0.226` [wiktionary] resolved: When a problem is resolved, it has been brought to a successful solution.

- rationale: "Resolved" means a symptom or problem has ended, and "went away" conveys that same outcome in everyday language. Phrase frequency rises from Zipf 4.10 to 5.26, making the wording noticeably more common. Readers can immediately grasp that the issue is over without pausing on a more formal verb.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `recurrence` -> `it come back`**

- status: `attributed`
- log p full -0.0325, empty -0.0712
- masks scored: 34/34 (+4 top-k)
- ranked sources:
    - `+1.181` [readme] recurrence: When a disease comes back after being treated.
    - `+0.568` [nih] recurrence: Cancer that has recurred (come back), usually after a period of time during which the cancer could
    - `+0.161` [wiktionary] resolved: When a problem is resolved, it has been brought to a successful solution.
    - `+0.136` [wiktionary] resolved: To resolve means to create a solution for a problem.
    - `-1.211` [wiktionary] recurrence: A recurrence is something that happens again.

- rationale: Recurrence means a disease or symptom returning after a period of improvement, and "it come back" expresses that same idea in everyday words. Phrase frequency rises from Zipf 3.20 to 5.57, while age of acquisition drops from 11.79 to 5.31. Readers can grasp the possibility of the illness returning without needing the formal medical noun.
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

**output:** The patient has a fever, an ear infection, and possible sepsis.

| metric | value |
|---|---:|
| bertscore_f1 | 0.511 |
| coleman_liau | 7.87 |
| coleman_liau_drop | 8.56 |
| copy_jargon_rate | 0.500 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| diagnostic_identity_preservation | 1.000 |
| fkgl | 8.01 |
| fkgl_drop | 6.10 |
| fre | 57.2 |
| fre_gain | 50.9 |
| human_edit_recall | 0.500 |
| length_ratio | 1.38 |
| n_words | 11.0 |
| nli_completeness | 0.871 |
| nli_faithfulness | 0.781 |
| replacement_f1 | 0.667 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 48.45 |
| smog | 11.21 |
| smog_drop | 1.82 |
| uncertainty_preservation | 1.000 |

### Stage 4 - arm `termonly`

**output:** Description: Fever, an ear infection, and a possible severe body-wide infection.

| metric | value |
|---|---:|
| bertscore_f1 | 0.712 |
| coleman_liau | 15.78 |
| coleman_liau_drop | 0.65 |
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
| nli_completeness | 0.653 |
| nli_faithfulness | 0.857 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 52.15 |
| smog | 14.55 |
| smog_drop | -1.53 |
| uncertainty_preservation | 1.000 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `otitis media` -> `an ear infection` | replace | - | - | - | - | - | - | - |
| `sepsis` -> `severe body-wide infection` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Description: Fever, an ear infection, and possible severe blood infection.

| metric | value |
|---|---:|
| bertscore_f1 | 0.755 |
| coleman_liau | 16.62 |
| coleman_liau_drop | -0.19 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| diagnostic_identity_preservation | 1.000 |
| fkgl | 11.91 |
| fkgl_drop | 2.20 |
| fre | 27.5 |
| fre_gain | 21.1 |
| human_edit_recall | 1.000 |
| length_ratio | 1.25 |
| n_words | 10.0 |
| nli_completeness | 0.751 |
| nli_faithfulness | 0.741 |
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
| `otitis media` -> `an ear infection` | replace | attributed | 0.433 | 0.618 | 0.916 | 0.941 | 0.814 | - |
| `sepsis` -> `severe blood infection` | replace | attributed | 2.351 | 2.718 | 0.805 | 0.933 | 0.388 | - |

**edit `otitis media` -> `an ear infection`**

- status: `attributed`
- log p full -1.0055, empty -1.4389
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+3.027` [michigan] otitis media: Ear infection, often in the middle ear.
    - `+2.212` [readme] otitis media: An ear infection causing inflammation in the middle ear.
    - `+0.737` [michigan] sepsis: A very serious infection in your blood caused by a germ (a bacteria). Also called septicemia.
    - `+0.469` [readme] Sepsis: When bacteria get into the blood, the body's reaction can lead to tissue and organ damage, potentially
    - `+0.349` [nih] sepsis: The presence of bacteria or their toxins in the blood or tissues.

- rationale: Otitis media is the medical name for inflammation or infection of the middle ear, so "an ear infection" conveys the same condition in everyday language. Phrase frequency rises from Zipf 2.16 to 4.08. Readers can immediately recognize the common illness without needing to translate the clinical terminology.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `sepsis` -> `severe blood infection`**

- status: `attributed`
- log p full -1.1102, empty -3.4609
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+1.528` [readme] sepsis: A severe condition where the body reacts to bacteria in the bloodstream by harming tissues and organs,
    - `+1.140` [michigan] sepsis: A very serious infection in your blood caused by a germ (a bacteria). Also called septicemia.
    - `+0.173` [readme] otitis media: An ear infection causing inflammation in the middle ear.
    - `+0.088` [readme] Sepsis: When bacteria get into the blood, the body's reaction can lead to tissue and organ damage, potentially
    - `+0.085` [michigan] otitis media: Ear infection, often in the middle ear.

- rationale: The readme defines sepsis as a severe condition in which the body's response to bacteria in the bloodstream damages tissues and organs, so "severe blood infection" preserves that core idea in everyday words. Phrase frequency rises from Zipf 3.01 to 4.09, and age of acquisition drops from 16.33 to 9.05. Readers can now grasp the life‑threatening nature of the illness without needing the clinical term.
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

**output:** Her main complaint right now is feeling tired all day.

| metric | value |
|---|---:|
| bertscore_f1 | 0.573 |
| coleman_liau | 6.76 |
| coleman_liau_drop | 5.06 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.333 |
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
| rewrite_aggressiveness | 0.667 |
| sari | 16.25 |
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

**output:** Right now, the main problem she tells the doctor about is feeling very tired all day.

| metric | value |
|---|---:|
| bertscore_f1 | 0.497 |
| coleman_liau | 7.00 |
| coleman_liau_drop | 4.82 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 6.88 |
| fkgl_drop | 0.76 |
| fre | 74.3 |
| fre_gain | 10.8 |
| human_edit_recall | 1.000 |
| length_ratio | 1.14 |
| n_words | 16.0 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.089 |
| number_unit_preservation | 0.500 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.571 |
| sari | 14.65 |
| smog | 3.13 |
| smog_drop | 8.08 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `primary complaint` -> `main problem she tells the doctor about` | replace | attributed | 8.248 | 8.428 | 0.768 | 0.871 | 1.614 | - |
| `fatigue` -> `feeling very tired` | replace | attributed | -0.136 | -0.203 | 0.663 | 0.880 | 0.216 | - |

**edit `primary complaint` -> `main problem she tells the doctor about`**

- status: `attributed`
- log p full -1.8019, empty -10.0495
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+3.316` [readme] COMPLAINT: A complaint is when someone tells the doctor about an illness or issue they are experiencing.
    - `+1.702` [readme] complaint: A complaint is when a patient talks about their illness or problem.
    - `+1.448` [michigan] complaint: Your illness or symptom that is most important; the main reason you go to the doctor. Also known as
    - `+0.835` [wiktionary] fatigue: Fatigue is the material failure, such as cracking or separation, caused by stress on the material.
    - `+0.823` [wiktionary] primary: A primary is a kind of election held by a political party to choose the people it prefers for public 

- rationale: The readme explains that a complaint is simply what a patient tells the doctor about an illness or issue, so "main problem she tells the doctor about" preserves that meaning in everyday words. Phrase frequency rises from Zipf 4.21 to 4.40, and age of acquisition drops from 8.89 to 6.55. Readers can now grasp the reason for the visit without needing the clinical phrase "primary complaint."
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `fatigue` -> `feeling very tired`**

- status: `attributed`
- log p full -1.1772, empty -1.0412
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+1.012` [nih] fatigue: A condition marked by extreme tiredness and inability to function due to lack of energy. Fatigue may 
    - `+0.796` [wiktionary] fatigue: Fatigue is the extreme tiredness which is the result of having mental or physical exertion or illness
    - `+0.307` [readme] COMPLAINT: A complaint is when someone tells the doctor about an illness or issue they are experiencing.
    - `+0.063` [readme] fatigue: Feeling exhausted and lacking energy.

- rationale: Fatigue means a deep, lingering exhaustion that goes beyond ordinary sleepiness, and "feeling very tired" conveys that same sense of drained energy in everyday words. Phrase frequency rises from Zipf 3.86 to 4.55, while age of acquisition drops from 11.83 to 5.31. Readers can immediately grasp the symptom without needing to know the more formal label.
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

**output:** He

| metric | value |
|---|---:|
| bertscore_f1 | -0.057 |
| coleman_liau | -33.80 |
| coleman_liau_drop | 45.75 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.000 |
| fkgl | -3.40 |
| fkgl_drop | 15.71 |
| fre | 121.2 |
| fre_gain | 80.6 |
| human_edit_recall | 1.000 |
| laterality_preservation | 0.000 |
| length_ratio | 0.05 |
| n_words | 1.0 |
| nli_completeness | 0.008 |
| nli_faithfulness | 0.749 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.462 |
| sari | 10.81 |
| smog | 3.13 |
| smog_drop | 9.89 |
| temporality_preservation | 0.000 |

### Stage 4 - arm `termonly`

**output:** He has noticed some changes in his bowel movements with occasional diarrhea and pain that started recently, mainly in the left side of his neck.

| metric | value |
|---|---:|
| bertscore_f1 | 0.596 |
| coleman_liau | 10.39 |
| coleman_liau_drop | 1.56 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.125 |
| fkgl | 12.57 |
| fkgl_drop | -0.25 |
| fre | 49.5 |
| fre_gain | 8.9 |
| human_edit_recall | 1.000 |
| laterality_preservation | 1.000 |
| length_ratio | 1.32 |
| n_words | 25.0 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.958 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.125 |
| sari | 19.91 |
| smog | 13.02 |
| smog_drop | 0.00 |
| temporality_preservation | 0.000 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `loose stools` -> `diarrhea` | replace | - | - | - | - | - | - | - |
| `new onset` -> `pain that started recently` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** He has noticed some changes in his poop with occasional watery poop and a new start of pain mostly in the left neck.

| metric | value |
|---|---:|
| bertscore_f1 | 0.748 |
| coleman_liau | 6.37 |
| coleman_liau_drop | 5.58 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.429 |
| fkgl | 9.28 |
| fkgl_drop | 3.03 |
| fre | 69.5 |
| fre_gain | 28.9 |
| human_edit_recall | 1.000 |
| laterality_preservation | 1.000 |
| length_ratio | 1.21 |
| n_words | 23.0 |
| nli_completeness | 0.995 |
| nli_faithfulness | 0.966 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.143 |
| sari | 24.89 |
| smog | 11.21 |
| smog_drop | 1.82 |
| temporality_preservation | 0.000 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `new onset` -> `new start` | replace | attributed | 0.037 | 0.196 | 0.605 | 0.946 | 1.289 | - |
| `predominantly` -> `mostly` | replace | attributed | 0.102 | 0.250 | -0.044 | 0.279 | 0.027 | - |

**edit `new onset` -> `new start`**

- status: `attributed`
- log p full -0.1914, empty -0.2285
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+1.943` [readme] loose stools: Watery poop.
    - `+0.654` [michigan] onset: The start.
    - `+0.605` [dictionary] Predominantly (adv.): In a predominant manner.
    - `+0.294` [wiktionary] onset: The onset of something is the time when it begins (usually something bad).
    - `+0.071` [nih] stool: The material in a bowel movement. Stool is made up of undigested food, bacteria, mucus, and cells from 

- rationale: "New onset" means something has just begun, and "new start" conveys that same idea in simpler words. Phrase frequency rises from Zipf 3.72 to 5.48, and age of acquisition drops from 10.72 to 4.72. Readers can grasp the timing immediately without pausing over a clinical phrase.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `predominantly` -> `mostly`**

- status: `attributed`
- log p full -0.4743, empty -0.5764
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.050` [dictionary] Predominantly (adv.): In a predominant manner.
    - `+0.022` [wiktionary] new: If somebody is new, they are not experienced.
    - `+0.009` [wiktionary] new: If something is new, it is not old.

- rationale: "Predominantly" means mainly or for the most part, and "mostly" conveys that same idea in a shorter, more familiar word. Phrase frequency rises from Zipf 3.80 to 4.83, while the syllable count drops from five to two. Readers can grasp the intended emphasis immediately without stumbling over a longer, less common adverb.
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

**output:** The patient is here for a follow-up visit because of a past case of erythema nodosum.

| metric | value |
|---|---:|
| bertscore_f1 | 0.222 |
| coleman_liau | 7.00 |
| coleman_liau_drop | 7.60 |
| copy_jargon_rate | 1.000 |
| critical_error | 0.000 |
| fkgl | 8.35 |
| fkgl_drop | 3.36 |
| fre | 63.7 |
| fre_gain | 31.2 |
| human_edit_recall | 0.000 |
| length_ratio | 1.00 |
| n_words | 17.0 |
| nli_completeness | 0.972 |
| nli_faithfulness | 0.977 |
| replacement_f1 | 0.000 |
| rewrite_aggressiveness | 1.000 |
| sari | 10.55 |
| smog | 11.21 |
| smog_drop | 3.35 |
| temporality_preservation | 1.000 |

### Stage 4 - arm `termonly`

**output:** The patient is here for a follow-up visit for a history of painful red bumps under the skin.

| metric | value |
|---|---:|
| bertscore_f1 | 0.521 |
| coleman_liau | 6.08 |
| coleman_liau_drop | 8.52 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 8.47 |
| fkgl_drop | 3.23 |
| fre | 66.4 |
| fre_gain | 33.9 |
| human_edit_recall | 1.000 |
| length_ratio | 1.12 |
| n_words | 19.0 |
| nli_completeness | 0.595 |
| nli_faithfulness | 0.326 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.600 |
| sari | 21.93 |
| smog | 11.21 |
| smog_drop | 3.35 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `erythema nodosum` -> `painful red bumps under the skin` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** The patient comes back for a check-up because of a past problem with painful red lumps under the skin.

| metric | value |
|---|---:|
| bertscore_f1 | 0.506 |
| coleman_liau | 7.67 |
| coleman_liau_drop | 6.93 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 7.35 |
| fkgl_drop | 4.36 |
| fre | 76.2 |
| fre_gain | 43.7 |
| human_edit_recall | 1.000 |
| length_ratio | 1.18 |
| n_words | 20.0 |
| nli_completeness | 0.453 |
| nli_faithfulness | 0.335 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.667 |
| sari | 19.63 |
| smog | 3.13 |
| smog_drop | 11.43 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `erythema nodosum` -> `painful red lumps under the skin` | replace | attributed | -0.366 | -0.614 | - | 0.764 | 0.000 | - |

**edit `erythema nodosum` -> `painful red lumps under the skin`**

- status: `attributed`
- log p full -1.1019, empty -0.7363
- masks scored: 10/10 (+2 top-k)
- ranked sources:
    - `-0.401` [readme] Erythema: Red skin.

- rationale: Erythema nodosum is a condition that produces tender, reddened nodules beneath the skin, and the phrase "painful red lumps under the skin" conveys that same picture in everyday language. Phrase frequency rises from Zipf 1.39 to 3.15. Readers can now picture the visible, sore bumps without needing to decode a Latin medical name.
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

**output:** She did not have enough iron in her blood last year, and because she has had several surgeries and has not been eating well, she may have low iron again.

| metric | value |
|---|---:|
| bertscore_f1 | 0.631 |
| coleman_liau | 6.61 |
| coleman_liau_drop | 1.27 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.200 |
| fkgl | 11.45 |
| fkgl_drop | -3.98 |
| fre | 66.4 |
| fre_gain | 5.3 |
| human_edit_recall | 1.000 |
| length_ratio | 1.30 |
| n_words | 30.0 |
| nli_completeness | 0.813 |
| nli_faithfulness | 0.098 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.800 |
| sari | 17.35 |
| smog | 8.84 |
| smog_drop | 2.37 |
| uncertainty_preservation | 1.000 |

### Stage 4 - arm `termonly`

**output:** She was low on iron last year, and with her multiple surgeries and poor eating by mouth, may have become low on iron again.

| metric | value |
|---|---:|
| bertscore_f1 | 0.845 |
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
| nli_completeness | 0.818 |
| nli_faithfulness | 0.100 |
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
| `iron deficient` -> `low on iron` | replace | - | - | - | - | - | - | - |
| `p. o.` -> `by mouth` | replace | - | - | - | - | - | - | - |
| `iron deficient` -> `low on iron` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** She did not have enough iron last year, and with her many surgeries and poor eating by mouth, she may not have enough iron again.

| metric | value |
|---|---:|
| bertscore_f1 | 0.688 |
| coleman_liau | 6.68 |
| coleman_liau_drop | 1.19 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.200 |
| fkgl | 10.21 |
| fkgl_drop | -2.74 |
| fre | 66.4 |
| fre_gain | 5.3 |
| human_edit_recall | 1.000 |
| length_ratio | 1.09 |
| n_words | 25.0 |
| nli_completeness | 0.804 |
| nli_faithfulness | 0.265 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.750 |
| sari | 24.73 |
| smog | 8.84 |
| smog_drop | 2.37 |
| uncertainty_preservation | 1.000 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `p. o.` -> `by mouth` | replace | attributed | -0.024 | -0.217 | 0.346 | 0.835 | 0.036 | - |

**edit `p. o.` -> `by mouth`**

- status: `attributed`
- log p full -0.1314, empty -0.1071
- masks scored: 66/66 (+2 top-k)
- ranked sources:
    - `+0.133` [wiktionary] o: The fifteenth (15th) letter of the alphabet. It is a vowel.
    - `+0.097` [michigan] deficient: To not have enough.
    - `+0.071` [thesaurus] deficient: lacking, not enough, poor
    - `+0.020` [michigan] iron: A mineral that can helps your body work in many ways. For example, it help blood carry oxygen and muscle

- rationale: "p. o." is a medical abbreviation meaning "by mouth," so the replacement simply spells out the same instruction in full words. Phrase frequency remains unchanged at Zipf 4.82, and syllable count stays at two. Patients can now follow the dosing direction without having to decode the Latin shorthand.
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

**output:** We will schedule him for a Holter monitor and send him back to his cardiologist.

| metric | value |
|---|---:|
| bertscore_f1 | 0.834 |
| coleman_liau | 7.36 |
| coleman_liau_drop | 1.16 |
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
| sari | 34.69 |
| smog | 11.21 |
| smog_drop | 0.00 |

### Stage 4 - arm `termonly`

**output:** We will schedule him for a heart-rhythm recorder and refer him back to his heart doctor.

| metric | value |
|---|---:|
| bertscore_f1 | 0.748 |
| coleman_liau | 8.09 |
| coleman_liau_drop | 0.43 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 6.14 |
| fkgl_drop | 3.00 |
| fre | 79.6 |
| fre_gain | 23.3 |
| human_edit_recall | 1.000 |
| length_ratio | 1.06 |
| n_words | 17.0 |
| nli_completeness | 0.680 |
| nli_faithfulness | 0.918 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 44.48 |
| smog | 8.84 |
| smog_drop | 2.37 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `Holter monitor` -> `heart-rhythm recorder` | replace | - | - | - | - | - | - | - |
| `cardiologist` -> `heart doctor` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** We will schedule him for a portable machine that records heart beats and send him back to his heart doctor.

| metric | value |
|---|---:|
| bertscore_f1 | 0.759 |
| coleman_liau | 7.95 |
| coleman_liau_drop | 0.57 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 7.55 |
| fkgl_drop | 1.59 |
| fre | 76.6 |
| fre_gain | 20.3 |
| human_edit_recall | 1.000 |
| length_ratio | 1.25 |
| n_words | 20.0 |
| nli_completeness | 0.166 |
| nli_faithfulness | 0.701 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.250 |
| sari | 35.58 |
| smog | 8.84 |
| smog_drop | 2.37 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `Holter monitor` -> `portable machine that records heart beats` | replace | attributed | 15.416 | 16.539 | - | 0.860 | 16.056 | - |
| `cardiologist` -> `heart doctor` | replace | attributed | 0.003 | 4.173 | - | 0.938 | 1.946 | - |

**edit `Holter monitor` -> `portable machine that records heart beats`**

- status: `attributed`
- log p full -0.3937, empty -15.8099
- masks scored: 34/34 (+4 top-k)
- ranked sources:
    - `+16.211` [iowa] HOLTER MONITOR: a portable machine for recording heart beats
    - `+0.155` [michigan] cardiologist: A doctor who treats heart and blood vessel problems.
    - `-0.325` [justplainclear] cardiologist: Heart doctor

- rationale: A Holter monitor is a wearable device that continuously tracks the heart's electrical activity, and "portable machine that records heart beats" describes that function in everyday words. Phrase frequency rises from Zipf 2.12 to 3.70, while age of acquisition drops from 9.68 to 7.95. Readers can now picture the test as a simple recorder they carry with them rather than puzzling over a brand-name term.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `cardiologist` -> `heart doctor`**

- status: `attributed`
- log p full -0.0000, empty -0.0026
- masks scored: 34/34 (+4 top-k)
- ranked sources:
    - `+2.697` [justplainclear] cardiologist: Heart doctor
    - `+0.751` [iowa] HOLTER MONITOR: a portable machine for recording heart beats
    - `+0.341` [wiktionary] cardiologist: A cardiologist is a doctor who specializes in medical problems related to the heart.
    - `-0.001` [nih] cardiologist: A doctor who has special training to diagnose and treat diseases of the heart and blood vessels.
    - `-0.248` [michigan] cardiologist: A doctor who treats heart and blood vessel problems.

- rationale: A cardiologist is a physician who specializes in diagnosing and treating heart conditions, so "heart doctor" conveys that same role in everyday language. Phrase frequency rises from Zipf 2.90 to 4.76, and age of acquisition drops from 13.42 to 5.17. Readers can immediately grasp the specialist's focus without needing the formal medical title.
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
| `proceed` -> `go ahead` | replace | attributed | 0.002 | 0.016 | 0.391 | 0.652 | 0.121 | - |
| `operative intervention` -> `surgery` | replace | attributed | 0.034 | 1.445 | 0.464 | 0.847 | 0.558 | - |

**edit `proceed` -> `go ahead`**

- status: `attributed`
- log p full -0.1156, empty -0.1173
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.224` [wiktionary] proceed: When you proceed, you go forward with something.
    - `+0.103` [wiktionary] intervention: An intervention is an activity designed to change or stop a situation.
    - `+0.081` [wiktionary] proceed: (formal) The proceeds of some individual project or sale are the money earned from doing it.
    - `+0.080` [nih] intervention: In medicine, a treatment, procedure, or other action taken to prevent or treat disease, or impro

- rationale: "Proceed" means to move forward or continue with an action, and "go ahead" carries that same sense of permission or continuation in everyday language. Word frequency rises from Zipf 4.18 to 4.97, and age of acquisition drops from 8.33 to 5.45. Readers can grasp the instruction immediately without pausing on a more formal verb.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `operative intervention` -> `surgery`**

- status: `attributed`
- log p full -0.0107, empty -0.0448
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+1.469` [readme] Operative: Operative means related to surgery.
    - `+0.911` [readme] intervention: An intervention is a step taken to help treat or prevent a health problem.
    - `+0.674` [wiktionary] operative: If something is operative, it is able to work.
    - `+0.411` [wiktionary] proceed: (formal) The proceeds of some individual project or sale are the money earned from doing it.
    - `+0.242` [wiktionary] operative: An operative is an employee with some particular function or skill.

- rationale: "Operative intervention" refers to a medical procedure performed by a surgeon to treat a condition, and "surgery" conveys that same meaning in a single, familiar word. Phrase frequency rises from Zipf 3.71 to 4.63, while age of acquisition drops from 13.11 to 7.68. Readers can immediately recognize the treatment being described without wading through formal terminology.
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

**output:** An abdominal X-ray was taken and showed an unusual pattern of gas in the bowels.

| metric | value |
|---|---:|
| bertscore_f1 | 0.603 |
| coleman_liau | 6.97 |
| coleman_liau_drop | 1.53 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.400 |
| fkgl | 9.14 |
| fkgl_drop | -1.95 |
| fre | 56.3 |
| fre_gain | -5.1 |
| human_edit_recall | 1.000 |
| length_ratio | 0.94 |
| n_words | 16.0 |
| nli_completeness | 0.921 |
| nli_faithfulness | 0.857 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.200 |
| sari | 19.73 |
| smog | 11.21 |
| smog_drop | -2.37 |

### Stage 4 - arm `termonly`

**output:** A belly X-ray was taken and showed an unusual pattern of gas in the bowels.

| metric | value |
|---|---:|
| bertscore_f1 | 0.588 |
| coleman_liau | 5.04 |
| coleman_liau_drop | 3.46 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.600 |
| fkgl | 7.57 |
| fkgl_drop | -0.38 |
| fre | 67.5 |
| fre_gain | 6.2 |
| human_edit_recall | 1.000 |
| length_ratio | 0.94 |
| n_words | 16.0 |
| nli_completeness | 0.926 |
| nli_faithfulness | 0.901 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.200 |
| sari | 18.19 |
| smog | 8.84 |
| smog_drop | 0.00 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `obtained` -> `taken` | replace | - | - | - | - | - | - | - |
| `abnormal bowel gas pattern` -> `unusual pattern of gas in the bowels` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** An expert review.

| metric | value |
|---|---:|
| bertscore_f1 | 0.062 |
| coleman_liau | 1.40 |
| coleman_liau_drop | 7.10 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 5.25 |
| fkgl_drop | 1.94 |
| fre | 62.8 |
| fre_gain | 1.5 |
| human_edit_recall | 1.000 |
| length_ratio | 0.18 |
| n_words | 3.0 |
| nli_completeness | 0.003 |
| nli_faithfulness | 0.250 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.143 |
| sari | 10.02 |
| smog | 3.13 |
| smog_drop | 5.71 |

annotation backend `novita`, 0 edits kept


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

**output:** She was given Ativan to make her sleepy and came to the emergency room barely conscious and unable to tell the doctors what happened.

| metric | value |
|---|---:|
| bertscore_f1 | 0.598 |
| coleman_liau | 9.31 |
| coleman_liau_drop | -0.11 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 11.47 |
| fkgl_drop | 0.84 |
| fre | 55.6 |
| fre_gain | 15.0 |
| human_edit_recall | 1.000 |
| length_ratio | 1.20 |
| n_words | 24.0 |
| nli_completeness | 0.966 |
| nli_faithfulness | 0.586 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.714 |
| sari | 17.96 |
| severity_downgrade | 0.000 |
| severity_tier_input | 3.000 |
| severity_tier_output | 3.000 |
| smog | 11.21 |
| smog_drop | 4.70 |

### Stage 4 - arm `termonly`

**output:** She was given a calming medicine and came to the emergency room very sleepy and not fully awake, so she could not tell the doctors what happened.

| metric | value |
|---|---:|
| bertscore_f1 | 0.541 |
| coleman_liau | 8.24 |
| coleman_liau_drop | 0.96 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.667 |
| fkgl | 12.42 |
| fkgl_drop | -0.11 |
| fre | 54.1 |
| fre_gain | 13.5 |
| human_edit_recall | 1.000 |
| length_ratio | 1.35 |
| n_words | 27.0 |
| nli_completeness | 0.085 |
| nli_faithfulness | 0.479 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.667 |
| sari | 17.12 |
| severity_downgrade | 0.000 |
| severity_tier_input | 3.000 |
| severity_tier_output | 3.000 |
| smog | 11.21 |
| smog_drop | 4.70 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `sedated` -> `given a calming medicine` | replace | - | - | - | - | - | - | - |
| `obtunded` -> `very sleepy and not fully awake` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** She was given a medicine to make her sleepy and came into the emergency room not fully alert and unable to give any history.

| metric | value |
|---|---:|
| bertscore_f1 | 0.660 |
| coleman_liau | 7.13 |
| coleman_liau_drop | 2.07 |
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
| nli_completeness | 0.043 |
| nli_faithfulness | 0.992 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.250 |
| sari | 34.60 |
| severity_downgrade | 0.000 |
| severity_tier_input | 3.000 |
| severity_tier_output | 3.000 |
| smog | 14.55 |
| smog_drop | 1.35 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `sedated` -> `given a medicine to make her sleepy` | replace | attributed | 2.539 | 2.574 | - | 0.604 | 0.168 | - |
| `obtunded` -> `not fully alert` | replace | attributed | 7.113 | 9.369 | - | 0.876 | 7.837 | - |

**edit `sedated` -> `given a medicine to make her sleepy`**

- status: `attributed`
- log p full -3.2986, empty -5.8378
- masks scored: 18/18 (+4 top-k)
- ranked sources:
    - `+0.646` [readme] SEDATED: Feeling calm, relaxed, or sleepy because of certain medications.
    - `+0.478` [readme] Sedated: When you're sedated, you feel calm, relaxed, or sleepy because of specific medication.
    - `+0.233` [wiktionary] sedated: A sedate person is calm and dignified.

- rationale: "Sedated" means a drug was used to calm someone or make them drowsy, and "given a medicine to make her sleepy" spells out that same action in everyday words. Phrase frequency rises from Zipf 2.78 to 3.63, showing the longer wording is considerably more common in everyday language. Readers can now picture the clinical step without needing to know the single technical verb.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `obtunded` -> `not fully alert`**

- status: `attributed`
- log p full -0.1106, empty -7.2233
- masks scored: 18/18 (+4 top-k)
- ranked sources:
    - `+8.171` [readme] obtunded: Being not fully alert.
    - `+0.335` [wiktionary] sedated: A sedate person is calm and dignified.
    - `+0.076` [readme] SEDATED: Feeling calm, relaxed, or sleepy because of certain medications.

- rationale: "Obtunded" describes a state of reduced consciousness where a person is difficult to arouse and responds only to strong stimulation, so "not fully alert" conveys that same diminished responsiveness in everyday language. Phrase frequency rises from Zipf 1.01 to 4.22, while age of acquisition drops from 14.6 to 9.2. Readers can now grasp the patient's level of consciousness without needing specialized medical vocabulary.
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

**output:** He does not have swelling now, but he has had some mild leg swelling in the past.

| metric | value |
|---|---:|
| bertscore_f1 | 0.907 |
| coleman_liau | 3.95 |
| coleman_liau_drop | -1.62 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 4.23 |
| fkgl_drop | 0.19 |
| fre | 95.0 |
| fre_gain | 4.9 |
| human_edit_recall | 1.000 |
| length_ratio | 1.13 |
| n_words | 17.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.394 |
| nli_faithfulness | 0.994 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 51.24 |
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
| `edema` -> `swelling` | replace | attributed | 0.004 | 0.868 | - | 0.549 | 0.006 | - |

**edit `edema` -> `swelling`**

- status: `attributed`
- log p full -0.0031, empty -0.0073
- masks scored: 34/34 (+2 top-k)
- ranked sources:
    - `+0.727` [readme] edema: Swelling due to too much fluid in the body tissues.
    - `+0.721` [nih] edema: Swelling caused by excess fluid in body tissues.
    - `+0.457` [michigan] edema: Swelling caused by too much fluid in your body.
    - `+0.164` [readme] Edema: Swelling in the body caused by too much fluid.
    - `-0.729` [iowa] EDEMA: excess fluid collecting in tissue

- rationale: Edema is the medical term for fluid buildup that makes body tissues puff up, and "swelling" conveys that same visible change in everyday language. Phrase frequency rises from Zipf 2.95 to 3.68, and the word shortens from three syllables to two. Readers can immediately picture the symptom without needing to translate a clinical label.
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

**output:** Mild overactive parathyroid glands caused by another problem.

| metric | value |
|---|---:|
| bertscore_f1 | 0.575 |
| coleman_liau | 18.93 |
| coleman_liau_drop | 17.27 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.333 |
| fkgl | 9.66 |
| fkgl_drop | 11.33 |
| fre | 40.1 |
| fre_gain | 90.1 |
| human_edit_recall | 1.000 |
| length_ratio | 1.60 |
| n_words | 8.0 |
| nli_completeness | 0.920 |
| nli_faithfulness | 0.886 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 23.89 |
| severity_downgrade | 0.000 |
| severity_preservation | 1.000 |
| severity_tier_input | 1.000 |
| severity_tier_output | 1.000 |
| smog | 11.21 |
| smog_drop | 0.00 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `secondary hyperparathyroidism` -> `overactive parathyroid glands caused by another problem` | replace | attributed | 0.057 | 0.068 | - | 0.609 | 0.532 | - |

**edit `secondary hyperparathyroidism` -> `overactive parathyroid glands caused by another problem`**

- status: `attributed`
- log p full -1.7993, empty -1.8561
- masks scored: 18/18 (+2 top-k)
- ranked sources:
    - `+0.492` [nih] hyperparathyroidism: A condition in which the parathyroid gland (one of four pea-sized organs found on the thy
    - `-0.039` [wiktionary] secondary: of less than primary importance.
    - `-0.269` [wiktionary] secondary: second, next in order to the first or primary.
    - `-0.398` [justplainclear] hyperparathyroidism: A condition where your parathyroid glands work too hard and raise the calcium level in yo

- rationale: Secondary hyperparathyroidism means the parathyroid glands are working too hard because of a separate underlying condition, and the replacement spells that out by calling them "overactive parathyroid glands caused by another problem." Phrase frequency rises from Zipf 1.88 to 2.08, while age of acquisition drops from 19.11 to 15.50. Readers can now grasp the cause-and-effect relationship without needing to decode the specialized medical label.
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

**output:** Otherwise, a full review of the patient's symptoms was done and showed no other problems except those already mentioned.

| metric | value |
|---|---:|
| bertscore_f1 | 0.477 |
| coleman_liau | 12.86 |
| coleman_liau_drop | -0.43 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.667 |
| fkgl | 10.45 |
| fkgl_drop | 0.11 |
| fre | 54.0 |
| fre_gain | 6.1 |
| human_edit_recall | 1.000 |
| length_ratio | 1.25 |
| n_words | 20.0 |
| nli_completeness | 0.953 |
| nli_faithfulness | 0.282 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.400 |
| sari | 15.11 |
| smog | 11.21 |
| smog_drop | 0.00 |

### Stage 4 - arm `termonly`

**output:** Otherwise, a full check of all body systems was done and showed no other problems except those already mentioned.

| metric | value |
|---|---:|
| bertscore_f1 | 0.514 |
| coleman_liau | 11.03 |
| coleman_liau_drop | 1.41 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.667 |
| fkgl | 9.83 |
| fkgl_drop | 0.73 |
| fre | 58.4 |
| fre_gain | 10.6 |
| human_edit_recall | 1.000 |
| length_ratio | 1.19 |
| n_words | 19.0 |
| nli_completeness | 0.993 |
| nli_faithfulness | 0.049 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.400 |
| sari | 15.11 |
| smog | 11.21 |
| smog_drop | 0.00 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `obtained` -> `done` | replace | - | - | - | - | - | - | - |
| `negative` -> `no other problems` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Otherwise, a full check of body systems was done and showed no other problems except those already mentioned.

| metric | value |
|---|---:|
| bertscore_f1 | 0.516 |
| coleman_liau | 11.56 |
| coleman_liau_drop | 0.88 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.667 |
| fkgl | 9.79 |
| fkgl_drop | 0.78 |
| fre | 57.0 |
| fre_gain | 9.1 |
| human_edit_recall | 1.000 |
| length_ratio | 1.12 |
| n_words | 18.0 |
| nli_completeness | 0.993 |
| nli_faithfulness | 0.123 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.400 |
| sari | 15.11 |
| smog | 11.21 |
| smog_drop | 0.00 |

annotation backend `novita`, 0 edits kept


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

**output:** Symptoms get worse when sitting for any length of time, such as driving a car.

| metric | value |
|---|---:|
| bertscore_f1 | 0.930 |
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
| nli_completeness | 0.984 |
| nli_faithfulness | 0.994 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 66.85 |
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
| `motor vehicle` -> `car` | replace | attributed | -0.004 | -0.627 | - | - | - | - |

**edit `motor vehicle` -> `car`**

- status: `attributed`
- log p full -0.0088, empty -0.0047
- masks scored: 4/4 (+1 top-k)
- ranked sources:
    - `+0.593` [wiktionary] motor vehicle: A motor vehicle a road vehicle powered by an internal combustion engine to provide power to rot

- rationale: "Motor vehicle" is a formal phrase for any powered road vehicle, and "car" conveys the same everyday idea in a single, familiar word. Phrase frequency rises from Zipf 4.33 to 5.45, while age of acquisition drops from 7.42 to 3.37. Readers can now grasp the reference immediately without wading through technical language.
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

**output:** Forearm, elbow and shoulder exams show no nerve problems.

| metric | value |
|---|---:|
| bertscore_f1 | 0.939 |
| coleman_liau | 11.20 |
| coleman_liau_drop | 5.80 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 6.28 |
| fkgl_drop | 6.56 |
| fre | 66.1 |
| fre_gain | 47.0 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 9.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.953 |
| nli_faithfulness | 0.971 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 59.22 |
| smog | 3.13 |
| smog_drop | 8.08 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `neurologic compromise` -> `nerve problems` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Forearm, elbow and shoulder exams show no nerve problems.

| metric | value |
|---|---:|
| bertscore_f1 | 0.939 |
| coleman_liau | 11.20 |
| coleman_liau_drop | 5.80 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 6.28 |
| fkgl_drop | 6.56 |
| fre | 66.1 |
| fre_gain | 47.0 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 9.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.953 |
| nli_faithfulness | 0.971 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 59.22 |
| smog | 3.13 |
| smog_drop | 8.08 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `neurologic compromise` -> `nerve problems` | replace | attributed | 0.208 | 1.215 | 0.699 | 0.534 | 0.070 | - |

**edit `neurologic compromise` -> `nerve problems`**

- status: `attributed`
- log p full -0.1028, empty -0.3110
- masks scored: 66/66 (+2 top-k)
- ranked sources:
    - `+0.370` [nih] neurologic: Having to do with nerves or the nervous system.
    - `+0.300` [readme] Neurologic: Having to do with nerves in the body, brain, or spinal cord.
    - `+0.184` [justplainclear] neurologic: Relating to the nervous system, brain or spinal cord
    - `+0.116` [wiktionary] compromise: A compromise is an agreement in which everyone gets only some of what they wanted.
    - `+0.083` [readme] NEUROLOGIC: Having to do with the nerves in the body, brain, or spinal cord.

- rationale: "Neurologic compromise" refers to damage or impaired function of the nervous system, and "nerve problems" conveys that same idea using everyday words. Phrase frequency rises from Zipf 2.55 to 4.15, while age of acquisition drops from 13.85 to 9.67. Readers can now grasp the concept of nervous system dysfunction without needing specialized medical vocabulary.
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

**output:** After that, the doctor injected numbing medicine into the area around the tumor.

| metric | value |
|---|---:|
| bertscore_f1 | 0.718 |
| coleman_liau | 11.37 |
| coleman_liau_drop | 1.30 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 12.17 |
| fkgl_drop | 1.50 |
| fre | 30.9 |
| fre_gain | 12.5 |
| human_edit_recall | 1.000 |
| length_ratio | 1.08 |
| n_words | 13.0 |
| nli_completeness | 0.658 |
| nli_faithfulness | 0.897 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 48.56 |
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

**output:** After that, a numbing drug was injected into the area around the growth.

| metric | value |
|---|---:|
| bertscore_f1 | 0.740 |
| coleman_liau | 7.80 |
| coleman_liau_drop | 4.87 |
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
| nli_completeness | 0.546 |
| nli_faithfulness | 0.982 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 54.00 |
| smog | 11.21 |
| smog_drop | 3.35 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `local anesthesia` -> `numbing drug` | replace | attributed | 4.993 | 5.640 | 0.942 | 0.843 | 0.723 | - |
| `tumor` -> `growth` | replace | attributed | -0.447 | -1.271 | 0.330 | 0.790 | 0.373 | - |

**edit `local anesthesia` -> `numbing drug`**

- status: `attributed`
- log p full -0.7382, empty -5.7317
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+1.805` [readme] local anesthesia: A drug that numbs a specific part of your body without affecting the rest.
    - `+1.082` [michigan] local anesthesia: A drug that causes only in the area of the body where the drug is put, as when a tooth is pu
    - `+1.041` [iowa] LOCAL ANESTHESIA: creation of insensitivity to pain in a small, local area of the body, usually by injection o
    - `+0.273` [justplainclear] tumor: Growth or lump
    - `+0.178` [nih] local anesthesia: A temporary loss of feeling in one small area of the body caused by special drugs called ane

- rationale: The readme defines local anesthesia as a drug that numbs a specific part of the body without affecting the rest, so "numbing drug" preserves that core idea in everyday words. Phrase frequency drops from Zipf 3.39 to 2.90, while age of acquisition falls from 12.53 to 8.11. Readers can now grasp the concept of targeted pain relief without needing the clinical term.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `tumor` -> `growth`**

- status: `attributed`
- log p full -0.6951, empty -0.2481
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.557` [justplainclear] tumor: Growth or lump
    - `+0.184` [dictionary] Thereafter (adv.): After that; afterward.
    - `+0.162` [nih] tumor: An abnormal mass of tissue that results when cells divide more than they should or do not die when th
    - `+0.149` [michigan] local anesthesia: A drug that causes only in the area of the body where the drug is put, as when a tooth is pu
    - `+0.089` [michigan] tumor: A growth or lump in your body. It may be cancer, but it also may not be cancer.

- rationale: A tumor is an abnormal mass of tissue, and "growth" conveys that same idea in a single, familiar word. Phrase frequency rises from Zipf 3.97 to 5.03, and age of acquisition drops from 10.32 to 6.70. Readers can grasp the basic concept without needing the clinical label.
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

**output:** I do not think she has a clear, current abscess, although there is some drainage.

| metric | value |
|---|---:|
| bertscore_f1 | 0.796 |
| coleman_liau | 6.97 |
| coleman_liau_drop | 2.56 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 5.21 |
| fkgl_drop | 2.41 |
| fre | 84.5 |
| fre_gain | 15.5 |
| human_edit_recall | 1.000 |
| length_ratio | 0.88 |
| n_words | 15.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.994 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 46.41 |
| severity_preservation | 0.000 |
| smog | 3.13 |
| smog_drop | 5.71 |

### Stage 4 - arm `termonly`

**output:** I do not think she has a clear, current pocket of pus, although there is some fluid leaking out.

| metric | value |
|---|---:|
| bertscore_f1 | 0.766 |
| coleman_liau | 5.54 |
| coleman_liau_drop | 4.00 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.667 |
| fkgl | 6.73 |
| fkgl_drop | 0.89 |
| fre | 80.7 |
| fre_gain | 11.7 |
| human_edit_recall | 1.000 |
| length_ratio | 1.12 |
| n_words | 19.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.991 |
| nli_faithfulness | 0.977 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.250 |
| sari | 50.85 |
| severity_preservation | 0.000 |
| smog | 3.13 |
| smog_drop | 5.71 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `abscessed lesion` -> `pocket of pus` | replace | - | - | - | - | - | - | - |
| `drainage` -> `fluid leaking out` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** I do not think she has a clear, current sore with pus, although some fluid is leaking out.

| metric | value |
|---|---:|
| bertscore_f1 | 0.709 |
| coleman_liau | 5.11 |
| coleman_liau_drop | 4.43 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.667 |
| fkgl | 5.85 |
| fkgl_drop | 1.76 |
| fre | 85.2 |
| fre_gain | 16.2 |
| human_edit_recall | 1.000 |
| length_ratio | 1.06 |
| n_words | 18.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.992 |
| nli_faithfulness | 0.713 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.400 |
| sari | 36.49 |
| severity_preservation | 0.000 |
| smog | 3.13 |
| smog_drop | 5.71 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `abscessed lesion` -> `sore with pus` | replace | attributed | 1.939 | 2.217 | 0.868 | 0.829 | 0.802 | - |
| `drainage` -> `fluid is leaking out` | replace | attributed | 0.467 | 3.294 | 0.877 | 0.846 | 3.514 | - |

**edit `abscessed lesion` -> `sore with pus`**

- status: `attributed`
- log p full -1.3014, empty -3.2404
- masks scored: 66/66 (+3 top-k)
- ranked sources:
    - `+1.229` [michigan] lesion: A sore or any part of your sking that looks different from the rest.
    - `+0.427` [readme] drainage: When any fluid is leaking out of a body part.
    - `+0.344` [readme] DRAINAGE: Fluid leaving an organ or body area.
    - `+0.329` [wiktionary] drainage: To use a drainage is engage in the action or process of draining something.
    - `+0.098` [readme] LESION: A lesion is a type of damage or change in tissue caused by disease or injury.

- rationale: The Michigan glossary describes an abscessed lesion as a sore or any area of skin that looks different, so "sore with pus" keeps that core idea while adding the key detail of infection in everyday words. Phrase frequency rises from Zipf 1.60 to 2.98, and age of acquisition drops from 12.82 to 7.78. Readers can now picture the problem — a sore that contains pus — without needing to know the clinical term.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `drainage` -> `fluid is leaking out`**

- status: `attributed`
- log p full -0.0232, empty -0.4899
- masks scored: 66/66 (+3 top-k)
- ranked sources:
    - `+3.565` [readme] drainage: When any fluid is leaking out of a body part.
    - `+0.051` [readme] DRAINAGE: Fluid leaving an organ or body area.

- rationale: Drainage refers to fluid escaping from a wound or body cavity, and "fluid is leaking out" spells out that same process in everyday words. Phrase frequency shifts from Zipf 3.77 to 3.58, while age of acquisition drops from 10.84 to 7.94. Readers can picture the leak immediately without needing the clinical noun.
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

**output:** Right now, the team would give the patient fluids through a vein and then check how she is doing.

| metric | value |
|---|---:|
| bertscore_f1 | 0.437 |
| coleman_liau | 6.15 |
| coleman_liau_drop | 5.94 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.333 |
| fkgl | 5.48 |
| fkgl_drop | 3.60 |
| fre | 89.6 |
| fre_gain | 40.0 |
| human_edit_recall | 1.000 |
| length_ratio | 1.46 |
| n_words | 19.0 |
| nli_completeness | 0.939 |
| nli_faithfulness | 0.507 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.250 |
| sari | 19.49 |
| smog | 3.13 |
| smog_drop | 9.89 |

### Stage 4 - arm `termonly`

**output:** At this time, we would give fluids by vein to replace lost water and check again.

| metric | value |
|---|---:|
| bertscore_f1 | 0.639 |
| coleman_liau | 5.55 |
| coleman_liau_drop | 6.54 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 5.40 |
| fkgl_drop | 3.68 |
| fre | 84.8 |
| fre_gain | 35.3 |
| human_edit_recall | 1.000 |
| length_ratio | 1.23 |
| n_words | 16.0 |
| nli_completeness | 0.950 |
| nli_faithfulness | 0.858 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 43.48 |
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
| `rehydrate` -> `give fluids by vein to add water back` | replace | attributed | 1.885 | 2.048 | - | 1.000 | 2.029 | - |
| `reassess` -> `check again` | replace | attributed | -0.002 | -0.069 | - | 0.781 | 0.023 | - |

**edit `rehydrate` -> `give fluids by vein to add water back`**

- status: `attributed`
- log p full -1.7583, empty -3.6433
- masks scored: 10/10 (+2 top-k)
- ranked sources:
    - `+2.312` [wiktionary] rehydrate: If you rehydrate something, you supply it with water to make it moist or wet again.
    - `+0.283` [wiktionary] reassess: If you reassess a person, idea, skill, process, etc., you judge or measure them again.
    - `-0.778` [readme] intravenous fluid: Fluids that go straight into a vein through a needle.

- rationale: To rehydrate means to restore the body's water balance, and "give fluids by vein to add water back" spells out exactly how that is done in everyday language. Phrase frequency rises from Zipf 2.20 to 3.43, while age of acquisition drops from 13.63 to 8.53. Readers can now picture the treatment — an IV drip — without needing to know the clinical verb.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `reassess` -> `check again`**

- status: `attributed`
- log p full -0.0286, empty -0.0268
- masks scored: 10/10 (+2 top-k)
- ranked sources:
    - `+0.023` [wiktionary] rehydrate: If you rehydrate something, you supply it with water to make it moist or wet again.
    - `-0.417` [wiktionary] reassess: If you reassess a person, idea, skill, process, etc., you judge or measure them again.

- rationale: "Reassess" means to evaluate something a second time, and "check again" conveys that same idea using everyday words. Phrase frequency rises from Zipf 2.80 to 5.16, while age of acquisition drops from 12.79 to 5.78. Readers can grasp the instruction immediately without pausing to decode a formal verb.
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

**output:** The findings match acute appendicitis.

| metric | value |
|---|---:|
| bertscore_f1 | 0.473 |
| coleman_liau | 16.56 |
| coleman_liau_drop | 3.31 |
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
| nli_completeness | 0.979 |
| nli_faithfulness | 0.982 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 11.81 |
| smog | 8.84 |
| smog_drop | 2.37 |
| temporality_preservation | 1.000 |
| uncertainty_preservation | 0.000 |

### Stage 4 - arm `termonly`

**output:** The test results match a sudden swelling of the appendix.

| metric | value |
|---|---:|
| bertscore_f1 | 0.476 |
| coleman_liau | 8.50 |
| coleman_liau_drop | 11.37 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.286 |
| fkgl | 6.01 |
| fkgl_drop | 8.27 |
| fre | 69.8 |
| fre_gain | 66.4 |
| human_edit_recall | 1.000 |
| length_ratio | 1.11 |
| n_words | 10.0 |
| nli_completeness | 0.927 |
| nli_faithfulness | 0.819 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 15.72 |
| smog | 8.84 |
| smog_drop | 2.37 |
| temporality_preservation | 0.000 |
| uncertainty_preservation | 0.000 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `compatible with` -> `match` | replace | - | - | - | - | - | - | - |
| `acute appendicitis` -> `a sudden swelling of the appendix` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** The test results match a sudden swelling of the appendix.

| metric | value |
|---|---:|
| bertscore_f1 | 0.476 |
| coleman_liau | 8.50 |
| coleman_liau_drop | 11.37 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.286 |
| fkgl | 6.01 |
| fkgl_drop | 8.27 |
| fre | 69.8 |
| fre_gain | 66.4 |
| human_edit_recall | 1.000 |
| length_ratio | 1.11 |
| n_words | 10.0 |
| nli_completeness | 0.927 |
| nli_faithfulness | 0.819 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 15.72 |
| smog | 8.84 |
| smog_drop | 2.37 |
| temporality_preservation | 0.000 |
| uncertainty_preservation | 0.000 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `compatible with` -> `match` | replace | attributed | -0.095 | -0.202 | -0.004 | 0.593 | 0.007 | - |
| `acute appendicitis` -> `sudden swelling of the appendix` | replace | attributed | 0.533 | 1.393 | 0.451 | 0.544 | 0.266 | - |

**edit `compatible with` -> `match`**

- status: `attributed`
- log p full -0.6846, empty -0.5898
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.168` [wiktionary] compatible: Things or people are compatible when they can work and communicate with each other without problem
    - `+0.161` [wiktionary] with: With is used to show the other people or things present when something happened.
    - `+0.074` [wiktionary] acute: If an angle is acute, it is less than 90 degrees in size.
    - `+0.042` [thesaurus] acute: sudden start, short term, quick
    - `+0.033` [wiktionary] findings: A finding is the information from a research or an investigation.

- rationale: "Compatible with" means that two things can work together or agree without conflict, and "match" conveys that same idea of a suitable fit in a single, familiar word. Phrase frequency rises from Zipf 3.97 to 5.13, and age of acquisition drops from 10.16 to 5.72. Readers can now grasp the concept of a good fit immediately, without wading through a longer, more abstract phrase.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `acute appendicitis` -> `sudden swelling of the appendix`**

- status: `attributed`
- log p full -0.2643, empty -0.7969
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.266` [readme] appendicitis: Appendicitis is when your appendix gets swollen and inflamed, typically causing stomach pain.

- rationale: Acute appendicitis means the appendix has become inflamed very quickly, and "sudden swelling of the appendix" conveys that same urgent inflammation in everyday words. Phrase frequency rises from Zipf 2.74 to 3.25, while age of acquisition drops from 12.00 to 10.56. Readers can now grasp the seriousness and speed of the condition without needing to decode a clinical diagnosis.
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

**output:** She says she has not lost weight, but she has had less appetite and has felt more tired than usual for the past three to four months.

| metric | value |
|---|---:|
| bertscore_f1 | 0.561 |
| coleman_liau | 5.66 |
| coleman_liau_drop | 10.58 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.286 |
| fkgl | 8.93 |
| fkgl_drop | 1.55 |
| fre | 79.2 |
| fre_gain | 28.9 |
| human_edit_recall | 1.000 |
| length_ratio | 1.50 |
| n_words | 27.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.992 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.143 |
| sari | 28.45 |
| smog | 11.21 |
| smog_drop | 1.82 |
| temporality_preservation | 1.000 |

### Stage 4 - arm `termonly`

**output:** She says she has not lost weight, but she has felt less hungry and more tired all over for the past 3-4 months.

| metric | value |
|---|---:|
| bertscore_f1 | 0.602 |
| coleman_liau | 4.60 |
| coleman_liau_drop | 11.64 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.375 |
| fkgl | 6.72 |
| fkgl_drop | 3.76 |
| fre | 87.9 |
| fre_gain | 37.6 |
| human_edit_recall | 1.000 |
| length_ratio | 1.33 |
| n_words | 24.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.994 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.125 |
| sari | 44.00 |
| smog | 3.13 |
| smog_drop | 9.89 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `decreased appetite` -> `less hungry` | replace | - | - | - | - | - | - | - |
| `generalized fatigue` -> `more tired all over` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** She says she has not lost weight, but she admits she has been less hungry and has felt very tired all over for the past 3-4 months.

| metric | value |
|---|---:|
| bertscore_f1 | 0.580 |
| coleman_liau | 5.01 |
| coleman_liau_drop | 11.22 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.375 |
| fkgl | 8.93 |
| fkgl_drop | 1.55 |
| fre | 79.2 |
| fre_gain | 28.9 |
| human_edit_recall | 1.000 |
| length_ratio | 1.56 |
| n_words | 28.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.994 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.125 |
| sari | 42.08 |
| smog | 3.13 |
| smog_drop | 9.89 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `acknowledged` -> `admits` | replace | attributed | 4.966 | 6.973 | 0.758 | 0.918 | 6.368 | - |
| `decreased appetite` -> `less hungry` | replace | attributed | 1.970 | 4.843 | 0.828 | 0.945 | 1.572 | - |
| `generalized fatigue` -> `very tired all over` | replace | attributed | 0.089 | 0.191 | 0.391 | 0.864 | 0.501 | - |

**edit `acknowledged` -> `admits`**

- status: `attributed`
- log p full -0.1433, empty -5.1091
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+6.839` [wiktionary] acknowledged: If you acknowledge a fact or a situation, you accept or admit that it is true or that it exists.
    - `+0.471` [nih] fatigue: A condition marked by extreme tiredness and inability to function due to lack of energy. Fatigue may 
    - `+0.467` [wiktionary] denies: If you deny something, you say it didn't happen or isn't true.
    - `+0.384` [wiktionary] decreased: If something decreases, it goes down in number or value.
    - `+0.345` [wiktionary] generalized: When you generalize you speak in general, or in vague terms.

- rationale: Wiktionary defines "acknowledge" as accepting or admitting that something is true, so "admits" preserves that core meaning in a shorter, more direct word. Word frequency shifts from Zipf 4.08 to 3.94, and the syllable count drops from three to two. Readers can now grasp the act of conceding a point without wading through a longer, more formal verb.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `decreased appetite` -> `less hungry`**

- status: `attributed`
- log p full -0.0502, empty -2.0199
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+2.180` [wiktionary] appetite: When you have appetite, you feel hungry and would like to eat some food.
    - `+0.608` [wiktionary] denies: If you deny something, you say it didn't happen or isn't true.
    - `+0.371` [readme] fatigue: Feeling exhausted and lacking energy.
    - `+0.365` [wiktionary] decreased: If something decreases, it goes down in number or value.
    - `+0.105` [nih] fatigue: A condition marked by extreme tiredness and inability to function due to lack of energy. Fatigue may 

- rationale: Wiktionary defines appetite as the feeling of hunger and the desire to eat, so "less hungry" preserves that core idea in everyday words. Phrase frequency rises from Zipf 3.63 to 4.41, and age of acquisition drops from 8.83 to 3.63. Readers can immediately grasp the symptom without needing the more formal phrasing.
- audit: coverage 1.0, grounding_error=True, omission=False, source_ok=True, passage_ok=True

**edit `generalized fatigue` -> `very tired all over`**

- status: `attributed`
- log p full -0.5833, empty -0.6723
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+1.309` [wiktionary] fatigue: Fatigue is the extreme tiredness which is the result of having mental or physical exertion or illness
    - `+0.808` [nih] fatigue: A condition marked by extreme tiredness and inability to function due to lack of energy. Fatigue may 
    - `+0.385` [wiktionary] acknowledged: If you acknowledge a fact or a situation, you accept or admit that it is true or that it exists.
    - `+0.381` [readme] generalized: Not specific, covers a broad range.
    - `+0.309` [wiktionary] decreased: If something decreases, it goes down in number or value.

- rationale: "Generalized fatigue" means a widespread, whole-body sense of exhaustion, and "very tired all over" conveys that same feeling in everyday words. Phrase frequency rises from Zipf 3.29 to 4.66, while age of acquisition drops from 11.83 to 5.57. Readers can now grasp the symptom immediately without needing a clinical label.
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

**output:** The doctors considered doing a completion thyroidectomy.

| metric | value |
|---|---:|
| bertscore_f1 | 0.191 |
| coleman_liau | 20.57 |
| coleman_liau_drop | 7.59 |
| copy_jargon_rate | 1.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 14.11 |
| fkgl_drop | 7.65 |
| fre | 6.4 |
| fre_gain | 58.4 |
| human_edit_recall | 0.000 |
| length_ratio | 0.78 |
| n_words | 7.0 |
| nli_completeness | 0.992 |
| nli_faithfulness | 0.357 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 18.18 |
| smog | 13.02 |
| smog_drop | 0.00 |
| uncertainty_preservation | 0.000 |

### Stage 4 - arm `termonly`

**output:** Doctors thought about doing surgery to take out the rest of the thyroid.

| metric | value |
|---|---:|
| bertscore_f1 | 0.403 |
| coleman_liau | 8.25 |
| coleman_liau_drop | 19.91 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.333 |
| fkgl | 6.73 |
| fkgl_drop | 15.03 |
| fre | 70.0 |
| fre_gain | 122.0 |
| human_edit_recall | 1.000 |
| length_ratio | 1.44 |
| n_words | 13.0 |
| nli_completeness | 0.970 |
| nli_faithfulness | 0.548 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 32.16 |
| smog | 8.84 |
| smog_drop | 4.18 |
| uncertainty_preservation | 0.000 |

annotation backend `novita`, 0 edits kept


### Stage 4 - arm `grounded`

**output:** The doctors thought about doing surgery to take out the rest of the thyroid gland.

| metric | value |
|---|---:|
| bertscore_f1 | 0.374 |
| coleman_liau | 8.13 |
| coleman_liau_drop | 20.03 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.333 |
| fkgl | 6.78 |
| fkgl_drop | 14.98 |
| fre | 73.2 |
| fre_gain | 125.2 |
| human_edit_recall | 1.000 |
| length_ratio | 1.67 |
| n_words | 15.0 |
| nli_completeness | 0.967 |
| nli_faithfulness | 0.471 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 31.71 |
| smog | 8.84 |
| smog_drop | 4.18 |
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

**output:** She says she had a nosebleed a few days ago that needed nasal packing, and it has now stopped.

| metric | value |
|---|---:|
| bertscore_f1 | 0.692 |
| coleman_liau | 5.23 |
| coleman_liau_drop | 5.19 |
| copy_jargon_rate | 0.667 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.333 |
| fkgl | 6.73 |
| fkgl_drop | 3.73 |
| fre | 80.7 |
| fre_gain | 26.7 |
| human_edit_recall | 0.333 |
| length_ratio | 0.90 |
| n_words | 19.0 |
| nli_completeness | 0.752 |
| nli_faithfulness | 0.963 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.400 |
| sari | 28.04 |
| smog | 3.13 |
| smog_drop | 8.08 |
| temporality_preservation | 1.000 |

### Stage 4 - arm `termonly`

**output:** She says she had a nosebleed a few days ago, needing gauze put in her nose, and luckily that has cleared up now.

| metric | value |
|---|---:|
| bertscore_f1 | 0.722 |
| coleman_liau | 4.85 |
| coleman_liau_drop | 5.57 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 7.75 |
| fkgl_drop | 2.71 |
| fre | 80.5 |
| fre_gain | 26.5 |
| human_edit_recall | 1.000 |
| length_ratio | 1.10 |
| n_words | 23.0 |
| nli_completeness | 0.935 |
| nli_faithfulness | 0.966 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.286 |
| sari | 29.83 |
| smog | 8.84 |
| smog_drop | 2.37 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `epistaxis` -> `nosebleed` | replace | - | - | - | - | - | - | - |
| `nasal packing` -> `gauze put in her nose` | replace | - | - | - | - | - | - | - |
| `resolved` -> `cleared up` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** She notes that she had a nosebleed a few days ago, needing nose packing and fortunately that had cleared up now.

| metric | value |
|---|---:|
| bertscore_f1 | 0.917 |
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
| nli_completeness | 0.864 |
| nli_faithfulness | 0.957 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 56.93 |
| smog | 8.84 |
| smog_drop | 2.37 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 4 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `epistaxis` -> `a nosebleed` | replace | attributed | 0.007 | 1.542 | 0.610 | 0.896 | 0.074 | - |
| `requiring` -> `needing` | replace | attributed | 0.139 | 1.599 | 0.629 | 0.783 | 0.039 | - |
| `nasal packing` -> `nose packing` | replace | attributed | 0.389 | 0.914 | 0.039 | 0.416 | 0.054 | - |
| `resolved` -> `cleared up` | replace | attributed | 0.302 | 0.764 | 0.594 | 0.808 | 0.114 | - |

**edit `epistaxis` -> `a nosebleed`**

- status: `attributed`
- log p full -0.0019, empty -0.0090
- masks scored: 66/66 (+8 top-k)
- ranked sources:
    - `+1.330` [readme] EPISTAXIS: EPISTAXIS: It's a nosebleed.
    - `+1.256` [readme] Epistaxis: A nosebleed.
    - `+0.667` [wiktionary] resolved: When a problem is resolved, it has been brought to a successful solution.
    - `+0.265` [wiktionary] packing: When you pack something, you put it in a container to carry with you.
    - `+0.137` [readme] packing: Putting something into a wound to help it heal.

- rationale: Epistaxis is the medical name for bleeding from the nose, so "a nosebleed" conveys the same condition in everyday language. Phrase frequency rises from Zipf 1.60 to 2.51, while age of acquisition drops from 14.6 to 9.2. Readers can immediately recognize the problem without needing to decode a clinical term.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `requiring` -> `needing`**

- status: `attributed`
- log p full -0.0385, empty -0.1776
- masks scored: 66/66 (+8 top-k)
- ranked sources:
    - `+0.452` [wiktionary] resolved: When a problem is resolved, it has been brought to a successful solution.
    - `+0.413` [wiktionary] requiring: If you require something, you need it.
    - `+0.245` [readme] packing: Putting something into a wound to help it heal.
    - `+0.214` [wiktionary] resolved: To resolve means to create a solution for a problem.
    - `+0.166` [readme] EPISTAXIS: EPISTAXIS: It's a nosebleed.

- rationale: "Requiring" means that something is necessary or obligatory, and "needing" conveys that same sense of necessity in a shorter, more familiar word. Word frequency shifts slightly from Zipf 4.14 to 4.02, while the syllable count drops from four to two. Readers can grasp the idea of a mandatory condition without stumbling over a longer, more formal verb.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `nasal packing` -> `nose packing`**

- status: `attributed`
- log p full -0.3829, empty -0.7719
- masks scored: 66/66 (+8 top-k)
- ranked sources:
    - `+0.275` [readme] Epistaxis: A nosebleed.
    - `+0.221` [wiktionary] packing: You put packing around an object to protect it.
    - `+0.220` [wiktionary] requiring: If you require something, you need it.
    - `+0.200` [readme] nasal: It's all about your nose when we talk about "nasal."
    - `+0.155` [wiktionary] resolved: To resolve means to create a solution for a problem.

- rationale: Nasal packing means placing gauze or another material inside the nostrils to stop bleeding or support healing, and "nose packing" conveys the same idea with a simpler, more familiar word. Phrase frequency rises from Zipf 3.39 to 3.93, while age of acquisition drops from 8.75 to 2.95. Readers can immediately picture the procedure without pausing over the less common adjective.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `resolved` -> `cleared up`**

- status: `attributed`
- log p full -0.3668, empty -0.6685
- masks scored: 66/66 (+8 top-k)
- ranked sources:
    - `+0.504` [wiktionary] resolved: To resolve means to create a solution for a problem.
    - `+0.390` [wiktionary] resolved: When a problem is resolved, it has been brought to a successful solution.
    - `+0.238` [readme] nasal: It's all about your nose when we talk about "nasal."
    - `+0.127` [wiktionary] packing: You put packing around an object to protect it.
    - `+0.105` [nih] nasal: By or having to do with the nose.

- rationale: "Resolved" means a problem or symptom has come to an end, and "cleared up" conveys that same outcome in everyday language. Phrase frequency rises from Zipf 4.10 to 4.20. Readers can grasp that the issue is gone without needing a more formal verb.
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

**output:** I also explained to the patient about medicine that makes you relaxed and sleepy but still awake.

| metric | value |
|---|---:|
| bertscore_f1 | 0.623 |
| coleman_liau | 9.75 |
| coleman_liau_drop | 2.09 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 9.09 |
| fkgl_drop | -0.19 |
| fre | 60.2 |
| fre_gain | 12.9 |
| human_edit_recall | 1.000 |
| length_ratio | 1.89 |
| n_words | 17.0 |
| nli_completeness | 0.579 |
| nli_faithfulness | 0.092 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 63.46 |
| smog | 8.84 |
| smog_drop | 0.00 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `conscious sedation` -> `medicine that makes you relaxed and sleepy but still awake` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** I also explained to the patient about medicine that makes you sleepy and forgetful during a procedure, but you can still wake up if someone talks to you or touches you.

| metric | value |
|---|---:|
| bertscore_f1 | 0.491 |
| coleman_liau | 8.69 |
| coleman_liau_drop | 3.15 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 13.63 |
| fkgl_drop | -4.73 |
| fre | 52.6 |
| fre_gain | 5.3 |
| human_edit_recall | 1.000 |
| length_ratio | 3.44 |
| n_words | 31.0 |
| nli_completeness | 0.357 |
| nli_faithfulness | 0.003 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 61.94 |
| smog | 13.02 |
| smog_drop | -4.18 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `conscious sedation` -> `medicine that makes you sleepy and forgetful during a procedure, but you can still wake up if someone talks to you or touches you` | replace | attributed | 24.537 | 24.542 | - | 1.000 | 1.666 | - |

**edit `conscious sedation` -> `medicine that makes you sleepy and forgetful during a procedure, but you can still wake up if someone talks to you or touches you`**

- status: `attributed`
- log p full -5.1947, empty -29.7313
- masks scored: 6/6 (+1 top-k)
- ranked sources:
    - `+12.564` [readme] conscious sedation: Medication given to a patient to make them lightly sedated and forgetful during a procedur
    - `+10.898` [nih] conscious sedation: A level of sedation in which a person is asleep but wakes when spoken to or touched. Consc

- rationale: Conscious sedation means giving drugs that keep a patient relaxed, drowsy, and unlikely to remember the procedure while still allowing them to respond to voice or touch, and the longer phrase spells out each of those effects in everyday language. Phrase frequency shifts slightly from Zipf 2.93 to 2.75, while age of acquisition drops from 13.20 to 9.67. Readers can now grasp the level of awareness and memory loss involved without needing to know the clinical term.
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

**output:** The doctor feels her right knee and does not feel any grinding or crackling.

| metric | value |
|---|---:|
| bertscore_f1 | 0.546 |
| coleman_liau | 7.77 |
| coleman_liau_drop | 1.73 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 5.04 |
| fkgl_drop | 0.19 |
| fre | 83.9 |
| fre_gain | 12.0 |
| human_edit_recall | 1.000 |
| laterality_preservation | 1.000 |
| length_ratio | 1.56 |
| n_words | 14.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.847 |
| nli_faithfulness | 0.439 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 26.98 |
| smog | 3.13 |
| smog_drop | 5.71 |

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

**output:** Feeling her right knee with the hands shows no crackling or grating feeling.

| metric | value |
|---|---:|
| bertscore_f1 | 0.632 |
| coleman_liau | 10.03 |
| coleman_liau_drop | -0.53 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 4.91 |
| fkgl_drop | 0.32 |
| fre | 83.0 |
| fre_gain | 11.2 |
| human_edit_recall | 1.000 |
| laterality_preservation | 1.000 |
| length_ratio | 1.44 |
| n_words | 13.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.932 |
| nli_faithfulness | 0.548 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 30.60 |
| smog | 3.13 |
| smog_drop | 5.71 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `crepitus` -> `crackling or grating feeling` | replace | attributed | -0.825 | -0.911 | - | 0.681 | 0.081 | - |

**edit `crepitus` -> `crackling or grating feeling`**

- status: `attributed`
- log p full -2.7994, empty -1.9748
- masks scored: 34/34 (+2 top-k)
- ranked sources:
    - `+0.218` [dictionary] Crepitus (n.): Same as Crepitation, 2.
    - `+0.138` [nih] palpation: Examination by pressing on the surface of the body to feel the organs or tissues underneath.
    - `-0.041` [readme] Palpation: Feeling a part of the body.
    - `-0.205` [readme] palpation: Feeling a part of the body with your hands.
    - `-0.338` [dictionary] Crepitus (n.): The noise produced by a sudden discharge of wind from the bowels.

- rationale: Crepitus refers to the audible or palpable crackling or grating sensation produced when rough joint surfaces or air bubbles move against each other, and the replacement phrase spells out that exact sensation in everyday words. Phrase frequency rises from Zipf 1.39 to 2.71, indicating the new wording is substantially more common in general language. Readers can now recognize the symptom immediately without needing to know the technical Latin term.
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

**output:** She stepped on something the evening before and twisted her ankle.

| metric | value |
|---|---:|
| bertscore_f1 | 0.831 |
| coleman_liau | 10.51 |
| coleman_liau_drop | 1.82 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 5.86 |
| fkgl_drop | 4.23 |
| fre | 72.6 |
| fre_gain | 25.0 |
| length_ratio | 1.00 |
| n_words | 11.0 |
| nli_completeness | 0.003 |
| nli_faithfulness | 0.994 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 47.52 |
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
| `the evening prior` -> `the night before` | replace | attributed | 0.190 | 1.025 | - | 0.390 | 0.180 | - |

**edit `the evening prior` -> `the night before`**

- status: `attributed`
- log p full -0.1242, empty -0.3138
- masks scored: 10/10 (+2 top-k)
- ranked sources:
    - `+0.180` [wiktionary] evening: You use even to focus on the most surprising or unlikely case.
    - `-0.002` [wiktionary] evening: Period from dusk to midnight.

- rationale: "The evening prior" refers to the night immediately preceding a given day, and "the night before" conveys that same timeframe in simpler, more familiar wording. Phrase frequency rises from Zipf 4.55 to 5.44, and age of acquisition drops from 10.63 to 5.45. Readers can grasp the timing without pausing to parse a more formal construction.
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

**output:** Things that change how the patient feels: The patient's condition gets worse with throwing.

| metric | value |
|---|---:|
| bertscore_f1 | 0.407 |
| coleman_liau | 13.16 |
| coleman_liau_drop | 3.20 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.750 |
| fkgl | 5.88 |
| fkgl_drop | 8.26 |
| fre | 77.8 |
| fre_gain | 68.1 |
| human_edit_recall | 1.000 |
| length_ratio | 1.50 |
| n_words | 15.0 |
| nli_completeness | 0.975 |
| nli_faithfulness | 0.979 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 27.35 |
| smog | 8.84 |
| smog_drop | 4.18 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `aggravated` -> `worse` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Things that change the condition: The patient's condition gets worse with throwing.

| metric | value |
|---|---:|
| bertscore_f1 | 0.448 |
| coleman_liau | 15.08 |
| coleman_liau_drop | 1.27 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.750 |
| fkgl | 6.79 |
| fkgl_drop | 7.35 |
| fre | 67.8 |
| fre_gain | 58.0 |
| human_edit_recall | 1.000 |
| length_ratio | 1.30 |
| n_words | 13.0 |
| nli_completeness | 0.976 |
| nli_faithfulness | 0.990 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 27.69 |
| smog | 11.21 |
| smog_drop | 1.82 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `aggravated` -> `worse` | replace | attributed | 0.000 | 0.179 | - | 0.764 | 0.247 | - |

**edit `aggravated` -> `worse`**

- status: `attributed`
- log p full -0.0000, empty -0.0000
- masks scored: 18/18 (+2 top-k)
- ranked sources:
    - `+0.381` [wiktionary] aggravated: To aggravate is to make something worse.
    - `+0.134` [readme] aggravated: To make a problem or injury worse.
    - `-0.075` [wiktionary] modifying: If you modify something, you change it, often only in small ways, and often because you want to use
    - `-0.118` [wiktionary] factors: A factor is one of a number of things that causes a result.

- rationale: "Aggravated" means made more severe or intense, and "worse" conveys that same idea in a single, familiar word. Phrase frequency rises from Zipf 3.47 to 4.89, and the syllable count drops from four to one. Readers can immediately grasp that a condition has deteriorated without pausing over a longer, less common term.
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

**output:** History of joint wear, bone thinning, underactive thyroid, nasal allergies, and kidney stones.

| metric | value |
|---|---:|
| bertscore_f1 | 0.788 |
| coleman_liau | 16.28 |
| coleman_liau_drop | 11.36 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.750 |
| fkgl | 11.26 |
| fkgl_drop | 10.09 |
| fre | 37.5 |
| fre_gain | 77.7 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 13.0 |
| nli_completeness | 0.968 |
| nli_faithfulness | 0.930 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 65.19 |
| smog | 13.02 |
| smog_drop | 2.88 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 4 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `osteoarthritis` -> `joint wear` | replace | - | - | - | - | - | - | - |
| `osteoporosis` -> `bone thinning` | replace | - | - | - | - | - | - | - |
| `hypothyroidism` -> `underactive thyroid` | replace | - | - | - | - | - | - | - |
| `allergic rhinitis` -> `nasal allergies` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** History of joint wear and tear, weak bones that break easily, underactive thyroid, hay fever, and hard mineral deposits in the kidneys.

| metric | value |
|---|---:|
| bertscore_f1 | 0.584 |
| coleman_liau | 11.59 |
| coleman_liau_drop | 16.05 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 12.30 |
| fkgl_drop | 9.05 |
| fre | 46.1 |
| fre_gain | 86.3 |
| human_edit_recall | 1.000 |
| length_ratio | 1.69 |
| n_words | 22.0 |
| nli_completeness | 0.787 |
| nli_faithfulness | 0.677 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 47.69 |
| smog | 15.90 |
| smog_drop | 0.00 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 5 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `osteoarthritis` -> `joint wear and tear` | replace | attributed | 0.439 | 0.640 | 0.759 | 0.936 | 0.840 | - |
| `osteoporosis` -> `weak bones that break easily` | replace | attributed | 7.141 | 7.509 | 0.617 | 0.772 | 0.521 | - |
| `hypothyroidism` -> `underactive thyroid` | replace | attributed | 1.198 | 2.406 | 0.731 | 0.922 | 0.867 | - |
| `allergic rhinitis` -> `hay fever` | replace | attributed | 0.745 | 5.209 | 0.812 | 0.879 | 3.704 | - |
| `kidney stones` -> `hard mineral deposits in the kidneys` | replace | attributed | 7.906 | 8.680 | 0.691 | 0.812 | 8.207 | - |

**edit `osteoarthritis` -> `joint wear and tear`**

- status: `attributed`
- log p full -0.9545, empty -1.3934
- masks scored: 66/66 (+10 top-k)
- ranked sources:
    - `+1.253` [justplainclear] osteoarthritis: A form of arthritis caused by the wear and tear of joints
    - `+0.413` [justplainclear] hypothyroidism: A condition where your thyroid isn't active enough, so you have low hormone levels Hypothyroid
    - `+0.309` [readme] osteoarthritis: Osteoarthritis is a painful joint condition caused by the wearing down of bone tissue, leading
    - `+0.190` [michigan] allergic rhinitis: Caused by your body's reaction in your nose to mold, pollen, or dust. Also called hay fever
    - `+0.143` [readme] Osteoporosis: Osteoporosis is a condition where bones become weak and more prone to fractures.

- rationale: Osteoarthritis refers to the gradual breakdown of cartilage that cushions the ends of bones, and "joint wear and tear" conveys that same degenerative process in everyday language. Phrase frequency rises from Zipf 2.76 to 4.12, while the syllable count drops from six to four. Readers can now grasp the condition as a familiar mechanical wearing down of joints rather than a technical diagnosis.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `osteoporosis` -> `weak bones that break easily`**

- status: `attributed`
- log p full -1.1784, empty -8.3196
- masks scored: 66/66 (+10 top-k)
- ranked sources:
    - `+1.299` [michigan] osteoporosis: When your bones are weak break easily. Also called brittle done disease.
    - `+0.778` [nih] osteoporosis: A condition in which there is a decrease in the amount and thickness of bone tissue. This causes
    - `+0.640` [readme] osteoporosis: Osteoporosis is when bones become weak and prone to breaking because they lose density.
    - `+0.360` [nih] hypothyroidism: Too little thyroid hormone. Symptoms include weight gain, constipation, dry skin, and sensitiv
    - `+0.232` [readme] osteoarthritis: Osteoarthritis is a painful joint condition caused by the wearing down of bone tissue, leading

- rationale: The Michigan glossary describes osteoporosis as bones that are weak and break easily, so the replacement keeps that core idea in everyday words. Phrase frequency rises from Zipf 2.99 to 4.05, and age of acquisition drops from 14.29 to 5.58. Readers can now grasp the condition without needing to know the medical term.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `hypothyroidism` -> `underactive thyroid`**

- status: `attributed`
- log p full -0.2602, empty -1.4578
- masks scored: 66/66 (+10 top-k)
- ranked sources:
    - `+1.316` [nih] hypothyroidism: Too little thyroid hormone. Symptoms include weight gain, constipation, dry skin, and sensitiv
    - `+0.449` [justplainclear] allergic rhinitis: Also known as: hay fever A condition where you have an allergic reaction that affects the n
    - `+0.395` [justplainclear] osteoarthritis: A form of arthritis caused by the wear and tear of joints
    - `+0.304` [nih] osteoporosis: A condition in which there is a decrease in the amount and thickness of bone tissue. This causes
    - `+0.234` [michigan] osteoporosis: When your bones are weak break easily. Also called brittle done disease.

- rationale: The NIH glossary defines hypothyroidism as too little thyroid hormone and notes it is also called underactive thyroid, so the replacement keeps the core meaning in everyday words. Phrase frequency drops from Zipf 2.68 to 1.67, while age of acquisition falls from 15.43 to 13.83. Readers can now recognize the condition from its plain description without needing the medical label.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `allergic rhinitis` -> `hay fever`**

- status: `attributed`
- log p full -0.0061, empty -0.7514
- masks scored: 66/66 (+10 top-k)
- ranked sources:
    - `+4.618` [justplainclear] allergic rhinitis: Also known as: hay fever A condition where you have an allergic reaction that affects the n
    - `+0.915` [michigan] osteoporosis: When your bones are weak break easily. Also called brittle done disease.
    - `+0.826` [michigan] allergic rhinitis: Caused by your body's reaction in your nose to mold, pollen, or dust. Also called hay fever
    - `+0.738` [readme] Osteoporosis: Osteoporosis is a condition where bones become weak and more prone to fractures.
    - `+0.668` [iowa] OSTEOPOROSIS: softening of the bones

- rationale: The glossary notes that allergic rhinitis is also called hay fever, a condition where an allergic reaction affects the nose, so the replacement keeps the same meaning in everyday words. Phrase frequency rises from Zipf 2.37 to 3.74, and age of acquisition drops from 18.07 to 5.84. Readers can now recognize the condition instantly without needing a medical label.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `kidney stones` -> `hard mineral deposits in the kidneys`**

- status: `attributed`
- log p full -0.6182, empty -8.5242
- masks scored: 66/66 (+10 top-k)
- ranked sources:
    - `+10.388` [readme] kidney stones: Hard mineral deposits in the kidneys causing pain and blockage.
    - `+2.182` [readme] Kidney Stones: Painful mineral deposits that can form in your kidney and block urine flow.
    - `+1.653` [nih] osteoporosis: A condition in which there is a decrease in the amount and thickness of bone tissue. This causes
    - `+0.528` [wiktionary] osteoporosis: Osteoporosis is a disease in which the bones become very porous and brittle.
    - `+0.438` [justplainclear] hypothyroidism: A condition where your thyroid isn't active enough, so you have low hormone levels Hypothyroid

- rationale: The readme defines kidney stones as hard mineral deposits in the kidneys that cause pain and blockage, so the replacement spells out that exact description in everyday words. Phrase frequency decreases from Zipf 3.85 to 3.28, while age of acquisition drops from 9.33 to 8.67. Readers can now picture the condition as solid mineral buildup inside the kidneys without needing the shorthand label.
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

**output:** The ultrasound did not show any bleeding in the brain.

| metric | value |
|---|---:|
| bertscore_f1 | 0.845 |
| coleman_liau | 6.76 |
| coleman_liau_drop | 13.81 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| diagnostic_identity_preservation | 1.000 |
| fkgl | 4.83 |
| fkgl_drop | 10.97 |
| fre | 78.2 |
| fre_gain | 84.0 |
| human_edit_recall | 1.000 |
| length_ratio | 1.11 |
| n_words | 10.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.908 |
| nli_faithfulness | 0.982 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 35.72 |
| smog | 8.84 |
| smog_drop | 5.71 |

### Stage 4 - arm `termonly`

**output:** The ultrasound did not find bleeding inside the skull.

| metric | value |
|---|---:|
| bertscore_f1 | 0.745 |
| coleman_liau | 9.91 |
| coleman_liau_drop | 10.66 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| diagnostic_identity_preservation | 1.000 |
| fkgl | 4.96 |
| fkgl_drop | 10.83 |
| fre | 75.5 |
| fre_gain | 81.2 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 9.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.945 |
| nli_faithfulness | 0.976 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 24.11 |
| smog | 8.84 |
| smog_drop | 5.71 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `intracranial hemorrhage` -> `bleeding inside the skull` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** The ultrasound did not find bleeding in the brain.

| metric | value |
|---|---:|
| bertscore_f1 | 0.840 |
| coleman_liau | 7.33 |
| coleman_liau_drop | 13.24 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| diagnostic_identity_preservation | 1.000 |
| fkgl | 3.65 |
| fkgl_drop | 12.14 |
| fre | 84.9 |
| fre_gain | 90.6 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 9.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.892 |
| nli_faithfulness | 0.988 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 37.06 |
| smog | 8.84 |
| smog_drop | 5.71 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `intracranial hemorrhage` -> `bleeding in the brain` | replace | attributed | 1.911 | 2.375 | - | 1.000 | 3.592 | - |

**edit `intracranial hemorrhage` -> `bleeding in the brain`**

- status: `attributed`
- log p full -0.8940, empty -2.8053
- masks scored: 6/6 (+1 top-k)
- ranked sources:
    - `+3.040` [readme] intracranial hemorrhage: Bleeding within the brain.
    - `-0.553` [readme] INTRACRANIAL HEMORRHAGE: Bleeding inside your brain.

- rationale: "Intracranial hemorrhage" refers to bleeding that occurs inside the skull, and "bleeding in the brain" conveys that same event in everyday language. Phrase frequency rises from Zipf 2.55 to 4.03, while age of acquisition drops from 14.94 to 5.76. Readers can now grasp the seriousness of the condition without needing specialized medical vocabulary.
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

**output:** He had his appendix taken out through small cuts, and he is eating regular food.

| metric | value |
|---|---:|
| bertscore_f1 | 0.458 |
| coleman_liau | 6.97 |
| coleman_liau_drop | 6.18 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.333 |
| fkgl | 6.78 |
| fkgl_drop | 7.88 |
| fre | 73.2 |
| fre_gain | 61.8 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 15.0 |
| nli_completeness | 0.918 |
| nli_faithfulness | 0.678 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 31.40 |
| smog | 11.21 |
| smog_drop | 1.82 |
| temporality_preservation | 0.000 |

### Stage 4 - arm `termonly`

**output:** He had his appendix taken out through small cuts, and he is eating by mouth without trouble.

| metric | value |
|---|---:|
| bertscore_f1 | 0.441 |
| coleman_liau | 7.71 |
| coleman_liau_drop | 5.44 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.222 |
| fkgl | 7.00 |
| fkgl_drop | 7.65 |
| fre | 75.1 |
| fre_gain | 63.8 |
| human_edit_recall | 1.000 |
| length_ratio | 1.13 |
| n_words | 17.0 |
| nli_completeness | 0.944 |
| nli_faithfulness | 0.574 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 31.30 |
| smog | 8.84 |
| smog_drop | 4.18 |
| temporality_preservation | 0.000 |

annotation backend `novita`, 0 edits kept


### Stage 4 - arm `grounded`

**output:** He had keyhole surgery to take out his appendix, and he is eating and drinking by mouth without trouble.

| metric | value |
|---|---:|
| bertscore_f1 | 0.577 |
| coleman_liau | 8.28 |
| coleman_liau_drop | 4.87 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.222 |
| fkgl | 9.21 |
| fkgl_drop | 5.45 |
| fre | 62.9 |
| fre_gain | 51.5 |
| human_edit_recall | 1.000 |
| length_ratio | 1.27 |
| n_words | 19.0 |
| nli_completeness | 0.955 |
| nli_faithfulness | 0.711 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 37.99 |
| smog | 11.21 |
| smog_drop | 1.82 |
| temporality_preservation | 0.000 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `laparoscopic appendicectomy` -> `keyhole surgery to take out his appendix` | replace | attributed | 0.557 | 0.611 | 0.505 | 0.635 | 0.049 | - |
| `tolerating oral diet` -> `eating and drinking by mouth without trouble` | replace | attributed | 2.827 | 3.087 | 0.884 | 0.923 | 1.269 | - |

**edit `laparoscopic appendicectomy` -> `keyhole surgery to take out his appendix`**

- status: `attributed`
- log p full -2.1645, empty -2.7216
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.543` [wiktionary] post: Post is the letters and parcels that you send to other people.
    - `+0.495` [wiktionary] tolerating: If you tolerate something, you put up with it, or allow it.
    - `+0.336` [readme] Laparoscopic: A surgery that uses a small tube and camera to see inside your body.
    - `+0.187` [nih] diet: The things a person eats and drinks.
    - `+0.149` [justplainclear] status: State, condition

- rationale: "Laparoscopic appendicectomy" is the medical name for removing the appendix through tiny incisions using a camera and instruments, and "keyhole surgery to take out his appendix" describes that same procedure in everyday words. Phrase frequency rises from Zipf 0.00 to 2.74, showing the replacement is far more common in ordinary language. Readers can now picture the operation without needing to decode a technical compound term.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `tolerating oral diet` -> `eating and drinking by mouth without trouble`**

- status: `attributed`
- log p full -1.4286, empty -4.2560
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+1.747` [nih] diet: The things a person eats and drinks.
    - `+0.478` [readme] Oral: Oral means something you take by mouth.
    - `+0.439` [readme] oral: "Oral means something you take through your mouth."
    - `+0.105` [readme] status: The current condition of something.
    - `+0.030` [michigan] status: The state or condition that you or something else is in.

- rationale: The NIH glossary defines diet as the things a person eats and drinks, so "eating and drinking by mouth without trouble" keeps that everyday meaning while adding the clinical idea of tolerating it well. Phrase frequency rises from Zipf 2.73 to 4.17, and age of acquisition drops from 9.39 to 6.53. Readers can now grasp the concept without needing to interpret the abstract phrase "tolerating oral diet."
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

**output:** We think her walking is most likely not affected by the hydrocephalus.

| metric | value |
|---|---:|
| bertscore_f1 | 0.746 |
| coleman_liau | 9.77 |
| coleman_liau_drop | 0.90 |
| copy_jargon_rate | 1.000 |
| critical_error | 0.000 |
| fkgl | 6.79 |
| fkgl_drop | 1.62 |
| fre | 67.8 |
| fre_gain | 8.1 |
| human_edit_recall | 0.000 |
| length_ratio | 0.67 |
| n_words | 12.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.993 |
| nli_faithfulness | 0.992 |
| replacement_f1 | 0.000 |
| rewrite_aggressiveness | 1.000 |
| sari | 21.25 |
| smog | 11.21 |
| smog_drop | 0.00 |
| uncertainty_preservation | 1.000 |

### Stage 4 - arm `termonly`

**output:** We believe that her walking is most likely not being affected by fluid buildup in the brain.

| metric | value |
|---|---:|
| bertscore_f1 | 0.934 |
| coleman_liau | 8.05 |
| coleman_liau_drop | 2.62 |
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
| nli_completeness | 0.317 |
| nli_faithfulness | 0.777 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 64.22 |
| smog | 8.84 |
| smog_drop | 2.37 |
| uncertainty_preservation | 1.000 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `hydrocephalus` -> `fluid buildup in the brain` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** We believe that her walking is most likely not being affected by the extra fluid in her brain.

| metric | value |
|---|---:|
| bertscore_f1 | 0.959 |
| coleman_liau | 7.04 |
| coleman_liau_drop | 3.63 |
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
| nli_completeness | 0.248 |
| nli_faithfulness | 0.543 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 74.58 |
| smog | 8.84 |
| smog_drop | 2.37 |
| uncertainty_preservation | 1.000 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `hydrocephalus` -> `extra fluid in her brain` | replace | attributed | 2.624 | 3.088 | - | 0.882 | 0.501 | - |

**edit `hydrocephalus` -> `extra fluid in her brain`**

- status: `attributed`
- log p full -0.9451, empty -3.5694
- masks scored: 18/18 (+2 top-k)
- ranked sources:
    - `+1.514` [justplainclear] hydrocephalus: Also known as: water on the brain A condition where there is too much cerebrospinal fluid in yo
    - `+1.014` [nih] hydrocephalus: The abnormal buildup of cerebrospinal fluid in the ventricles of the brain.
    - `+0.986` [readme] hydrocephalus: Swelling of brain due to excess fluid.

- rationale: Hydrocephalus is a condition in which excess cerebrospinal fluid builds up inside the skull, and "extra fluid in her brain" conveys that same idea in everyday language. Phrase frequency rises from Zipf 2.32 to 4.08, while age of acquisition drops from 15.78 to 7.94. The reader can now grasp the core problem without needing a specialized medical term.
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

**output:** She noted complaints of fatigue, lightheadedness, and severe dyspnea on exertion.

| metric | value |
|---|---:|
| bertscore_f1 | 0.704 |
| coleman_liau | 17.36 |
| coleman_liau_drop | 0.00 |
| copy_jargon_rate | 1.000 |
| critical_error | 0.000 |
| fkgl | 12.30 |
| fkgl_drop | 0.00 |
| fre | 26.5 |
| fre_gain | 0.0 |
| human_edit_recall | 0.000 |
| length_ratio | 0.73 |
| n_words | 11.0 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.994 |
| replacement_f1 | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 18.59 |
| severity_downgrade | 0.000 |
| severity_preservation | 1.000 |
| severity_tier_input | 3.000 |
| severity_tier_output | 3.000 |
| smog | 13.02 |
| smog_drop | 0.00 |

### Stage 4 - arm `termonly`

**output:** She said she felt very tired, dizzy, and very short of breath when she moved around.

| metric | value |
|---|---:|
| bertscore_f1 | 0.582 |
| coleman_liau | 6.27 |
| coleman_liau_drop | 11.09 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.333 |
| fkgl | 6.14 |
| fkgl_drop | 6.16 |
| fre | 79.6 |
| fre_gain | 53.1 |
| human_edit_recall | 1.000 |
| length_ratio | 1.07 |
| n_words | 16.0 |
| nli_completeness | 0.983 |
| nli_faithfulness | 0.990 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.143 |
| sari | 26.42 |
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
| `dyspnea on exertion` -> `very short of breath when she moved around` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** She noted complaints of fatigue, lightheadedness, and severe dyspnea on exertion.

| metric | value |
|---|---:|
| bertscore_f1 | 0.704 |
| coleman_liau | 17.36 |
| coleman_liau_drop | 0.00 |
| copy_jargon_rate | 1.000 |
| critical_error | 0.000 |
| fkgl | 12.30 |
| fkgl_drop | 0.00 |
| fre | 26.5 |
| fre_gain | 0.0 |
| human_edit_recall | 0.000 |
| length_ratio | 0.73 |
| n_words | 11.0 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.994 |
| replacement_f1 | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 18.59 |
| severity_downgrade | 0.000 |
| severity_preservation | 1.000 |
| severity_tier_input | 3.000 |
| severity_tier_output | 3.000 |
| smog | 13.02 |
| smog_drop | 0.00 |

annotation backend `novita`, 0 edits kept


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

**output:** There is no large swelling linked to these on the back of the hand.

| metric | value |
|---|---:|
| bertscore_f1 | 0.659 |
| coleman_liau | 4.04 |
| coleman_liau_drop | 4.97 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.667 |
| fkgl | 2.51 |
| fkgl_drop | 8.43 |
| fre | 102.0 |
| fre_gain | 60.4 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 14.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.940 |
| nli_faithfulness | 0.842 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 36.58 |
| severity_downgrade | 0.000 |
| severity_preservation | 1.000 |
| severity_tier_input | 2.000 |
| severity_tier_output | 2.000 |
| smog | 3.13 |
| smog_drop | 9.89 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `significant amount` -> `large` | replace | - | - | - | - | - | - | - |
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
| `edema` -> `swelling` | replace | attributed | 0.005 | 1.451 | 0.656 | 0.474 | 0.185 | - |
| `associated with` -> `linked to` | replace | attributed | 0.112 | 0.518 | 0.484 | 0.838 | 0.274 | - |
| `dorsum` -> `back` | replace | attributed | 0.001 | 1.015 | 0.764 | 0.897 | 1.207 | - |

**edit `edema` -> `swelling`**

- status: `attributed`
- log p full -0.0016, empty -0.0070
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+0.479` [readme] Edema: Swelling in the body caused by too much fluid.
    - `+0.293` [justplainclear] significant: Big, serious, important, major
    - `+0.276` [wiktionary] significant: If something is significant, it is important, or large, enough to pay attention to or to believe.
    - `+0.261` [michigan] edema: Swelling caused by too much fluid in your body.
    - `+0.238` [michigan] significant: Big or important.

- rationale: Edema is the medical name for fluid collecting in body tissues, and "swelling" conveys that same visible puffiness in everyday language. Word frequency rises from Zipf 2.95 to 3.68, and the term shortens from three syllables to two. Readers can immediately picture the physical sign without needing to recognize the clinical label.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `associated with` -> `linked to`**

- status: `attributed`
- log p full -0.1911, empty -0.3028
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+0.948` [justplainclear] associated with: Linked to, related to, goes along with, is part of
    - `+0.674` [readme] Edema: Swelling in the body caused by too much fluid.
    - `+0.652` [readme] associated with: Linked to something.
    - `+0.621` [michigan] edema: Swelling caused by too much fluid in your body.
    - `+0.487` [justplainclear] significant: Big, serious, important, major

- rationale: "Associated with" signals that two things occur together or share a connection, and "linked to" preserves that relationship in fewer syllables and more familiar words. Phrase frequency shifts from Zipf 4.89 to 4.54, while age of acquisition drops from 4.44 to 3.95. Readers can grasp the connection between factors without wading through a longer, more abstract phrase.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `dorsum` -> `back`**

- status: `attributed`
- log p full -0.0004, empty -0.0010
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+1.414` [readme] dorsum: The dorsum is basically the back or upper surface.
    - `+0.208` [readme] Edema: Swelling in the body caused by too much fluid.
    - `+0.152` [wiktionary] significant: If something is significant, it is important, or large, enough to pay attention to or to believe.
    - `+0.143` [justplainclear] significant: Big, serious, important, major
    - `+0.073` [readme] associated with: Linked to something.

- rationale: "Dorsum" is an anatomical term for the back surface of a body part, and "back" conveys that same location in everyday language. Word frequency rises from Zipf 2.47 to 6.04, marking a substantial jump in familiarity. Readers can now locate the body area instantly without pausing to translate a technical term.
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
| `cardio` -> `heart` | replace | attributed | -0.006 | -0.942 | 0.572 | 0.818 | 0.010 | - |
| `pulmonary` -> `lung` | replace | attributed | 0.009 | 1.018 | -0.060 | 0.526 | 0.028 | - |

**edit `cardio` -> `heart`**

- status: `attributed`
- log p full -0.0097, empty -0.0038
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.010` [justplainclear] pulmonary: About the lungs
    - `-0.055` [nih] pulmonary: Having to do with the lungs.
    - `-0.086` [readme] pulmonary: Related to the lungs.
    - `-0.173` [thesaurus] pulmonary: related to the lungs

- rationale: "Cardio" is a shortened form of "cardiac" or "cardiovascular" that refers to the heart, so "heart" preserves the exact meaning in a single, familiar word. Phrase frequency rises from Zipf 3.44 to 5.31, and the syllable count drops from three to one. Readers can immediately recognize the organ being discussed without decoding a clinical abbreviation.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `pulmonary` -> `lung`**

- status: `attributed`
- log p full -0.0052, empty -0.0143
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.123` [thesaurus] pulmonary: related to the lungs
    - `+0.095` [justplainclear] pulmonary: About the lungs
    - `-0.009` [readme] Pulmonary: About the lungs.
    - `-0.021` [readme] pulmonary: Related to the lungs.
    - `-0.114` [iowa] PULMONARY: pertaining to the lungs

- rationale: "Pulmonary" is a medical adjective meaning "relating to the lungs," so "lung" preserves that connection by using the familiar organ name directly. Phrase frequency rises from Zipf 3.50 to 4.10, and age of acquisition drops from 13.05 to 7.16. Readers can now grasp the reference to the respiratory organ without needing specialized vocabulary.
- audit: coverage 1.0, grounding_error=True, omission=False, source_ok=True, passage_ok=False

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

**output:** At that time, the Coreg was stopped because the patient's blood pressure was too low.

| metric | value |
|---|---:|
| bertscore_f1 | 0.587 |
| coleman_liau | 8.52 |
| coleman_liau_drop | -0.12 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.250 |
| fkgl | 4.42 |
| fkgl_drop | 2.52 |
| fre | 90.1 |
| fre_gain | 25.2 |
| human_edit_recall | 1.000 |
| length_ratio | 1.23 |
| n_words | 16.0 |
| nli_completeness | 0.666 |
| nli_faithfulness | 0.558 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 45.26 |
| smog | 3.13 |
| smog_drop | 8.08 |

### Stage 4 - arm `termonly`

**output:** At that time, the heart medicine was held because of low blood pressure.

| metric | value |
|---|---:|
| bertscore_f1 | 0.660 |
| coleman_liau | 7.80 |
| coleman_liau_drop | 0.60 |
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
| nli_completeness | 0.577 |
| nli_faithfulness | 0.742 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.250 |
| sari | 53.93 |
| smog | 8.84 |
| smog_drop | 2.37 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `Coreg` -> `heart medicine` | replace | - | - | - | - | - | - | - |
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
| `Coreg` -> `blood pressure medicine` | replace | attributed | 0.935 | 1.072 | 0.866 | 0.888 | 1.185 | - |
| `secondary to` -> `because of` | replace | attributed | 0.033 | 0.716 | 0.734 | 0.722 | 0.093 | - |
| `hypotension` -> `low blood pressure` | replace | attributed | 0.001 | 1.719 | 0.694 | 0.850 | 0.273 | - |

**edit `Coreg` -> `blood pressure medicine`**

- status: `attributed`
- log p full -1.6357, empty -2.5707
- masks scored: 66/66 (+5 top-k)
- ranked sources:
    - `+1.378` [nih] Coreg: A drug used to treat high blood pressure and certain heart problems. It is also being studied in the pr
    - `+0.193` [wiktionary] to: To has no meaning. It is used with a bare infinitival clause.
    - `+0.193` [readme] hypotension: Low blood pressure.
    - `+0.156` [nih] hypotension: Abnormally low blood pressure.

- rationale: The NIH glossary describes Coreg as a drug used to treat high blood pressure and certain heart problems, so "blood pressure medicine" captures its main purpose in everyday words. Phrase frequency rises from Zipf 1.16 to 4.44. Readers can now recognize the medication's role without needing to know the brand name.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `secondary to` -> `because of`**

- status: `attributed`
- log p full -0.0326, empty -0.0656
- masks scored: 66/66 (+5 top-k)
- ranked sources:
    - `+0.497` [readme] Hypotension: Hypotension means low blood pressure.
    - `+0.404` [iowa] HYPOTENSION: low blood pressure
    - `+0.249` [wiktionary] hypotension: Hypotension is the disease of having low blood pressure.
    - `+0.177` [wiktionary] to: To shows where something goes, the goal of movement.
    - `+0.106` [wiktionary] to: To has no meaning. It is used with a bare infinitival clause.

- rationale: "Secondary to" signals that one condition results from another, and "because of" expresses that same causal link in everyday language. Phrase frequency rises from Zipf 4.53 to 6.01, and age of acquisition drops from 9.11 to 4.55. Readers can now grasp the cause-and-effect relationship without stumbling over formal phrasing.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `hypotension` -> `low blood pressure`**

- status: `attributed`
- log p full -0.0003, empty -0.0017
- masks scored: 66/66 (+5 top-k)
- ranked sources:
    - `+0.711` [readme] Hypotension: Hypotension means low blood pressure.
    - `+0.438` [iowa] HYPOTENSION: low blood pressure
    - `+0.245` [wiktionary] to: To shows where something goes, the goal of movement.
    - `+0.242` [wiktionary] to: To has no meaning. It is used with a bare infinitival clause.
    - `+0.119` [readme] hypotension: Low blood pressure.

- rationale: Hypotension means blood pressure that is lower than normal, and "low blood pressure" states that directly in everyday words. Phrase frequency rises from Zipf 2.52 to 4.65, while age of acquisition drops from 14.41 to 8.95. Readers can now grasp the condition immediately without needing to decode a medical term.
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

**output:** Her diarrhea has settled down, and she has less urinary incontinence and less swelling in her feet.

| metric | value |
|---|---:|
| bertscore_f1 | 0.611 |
| coleman_liau | 10.09 |
| coleman_liau_drop | 0.89 |
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
| nli_completeness | 0.882 |
| nli_faithfulness | 0.493 |
| replacement_f1 | 0.500 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 38.87 |
| smog | 13.02 |
| smog_drop | 1.53 |
| temporality_preservation | 0.000 |

### Stage 4 - arm `termonly`

**output:** Her loose stools have settled down and she is having less trouble holding her urine, less swelling in her feet.

| metric | value |
|---|---:|
| bertscore_f1 | 0.685 |
| coleman_liau | 8.82 |
| coleman_liau_drop | 2.17 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 7.55 |
| fkgl_drop | 5.23 |
| fre | 76.6 |
| fre_gain | 44.6 |
| human_edit_recall | 1.000 |
| length_ratio | 1.18 |
| n_words | 20.0 |
| nli_completeness | 0.951 |
| nli_faithfulness | 0.951 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.167 |
| sari | 54.76 |
| smog | 3.13 |
| smog_drop | 11.43 |
| temporality_preservation | 0.000 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `diarrhea` -> `loose stools` | replace | - | - | - | - | - | - | - |
| `urinary incontinence` -> `trouble holding her urine` | replace | - | - | - | - | - | - | - |
| `pedal edema` -> `swelling in her feet` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Her loose, watery poop has settled down and she is having less trouble holding her pee, less swollen feet.

| metric | value |
|---|---:|
| bertscore_f1 | 0.703 |
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
| nli_completeness | 0.952 |
| nli_faithfulness | 0.967 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.167 |
| sari | 63.06 |
| smog | 8.84 |
| smog_drop | 5.71 |
| temporality_preservation | 0.000 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `diarrhea` -> `loose, watery poop` | replace | attributed | 8.574 | 9.321 | 0.864 | 0.939 | 4.118 | - |
| `urinary incontinence` -> `trouble holding her pee` | replace | attributed | 0.467 | 1.119 | 0.778 | 0.830 | 1.349 | - |
| `pedal edema` -> `swollen feet` | replace | attributed | 2.369 | 4.720 | 0.852 | 0.968 | 4.020 | - |

**edit `diarrhea` -> `loose, watery poop`**

- status: `attributed`
- log p full -0.6412, empty -9.2148
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+5.368` [readme] diarrhea: Having loose, watery poop with cramps and bloating.
    - `+1.250` [justplainclear] diarrhea: A bowel movement that is loose and watery If your poop is like water or very runny, or if you have m
    - `+0.886` [readme] urinary incontinence: When you can't control your pee.
    - `+0.886` [wiktionary] diarrhea: Diarrhea is an illness where the person's poop or feces are soft like water.
    - `+0.457` [michigan] urinary incontinence: When you lose control of your bladder and the fluids it holds.

- rationale: The glossary defines diarrhea as having loose, watery poop with cramps and bloating, so the replacement spells out the core symptom in everyday words. Phrase frequency drops from Zipf 3.55 to 3.05, while age of acquisition falls from 10.1 to 4.5. Readers can now recognize the condition immediately without needing to know the medical term.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `urinary incontinence` -> `trouble holding her pee`**

- status: `attributed`
- log p full -0.3404, empty -0.8069
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+1.544` [readme] urinary incontinence: When you can't control your pee.
    - `+0.195` [justplainclear] diarrhea: A bowel movement that is loose and watery If your poop is like water or very runny, or if you have m
    - `+0.167` [readme] pedal edema: Swollen feet.
    - `+0.113` [wiktionary] diarrhea: Diarrhea is an illness where the person's poop or feces are soft like water.
    - `+0.092` [michigan] diarrhea: Loose, watery stools three or more times a day. It can be sudden (due to a virus, for example), pers

- rationale: Urinary incontinence means the involuntary loss of bladder control, and "trouble holding her pee" conveys that same experience in everyday language. Phrase frequency rises from Zipf 2.77 to 3.86, while age of acquisition drops from 14.41 to 5.09. The reader can now grasp the condition immediately without needing a medical vocabulary.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `pedal edema` -> `swollen feet`**

- status: `attributed`
- log p full -0.0911, empty -2.4596
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+4.706` [readme] pedal edema: Swollen feet.
    - `+0.686` [readme] diarrhea: Having loose, watery poop with cramps and bloating.
    - `+0.359` [readme] urinary incontinence: When you can't control your pee.
    - `+0.299` [wiktionary] diarrhea: Diarrhea is an illness where the person's poop or feces are soft like water.
    - `+0.232` [michigan] diarrhea: Loose, watery stools three or more times a day. It can be sudden (due to a virus, for example), pers

- rationale: The readme glossary defines pedal edema simply as swollen feet, so the replacement keeps the exact same meaning in everyday words. Phrase frequency rises from Zipf 2.87 to 3.55, and the syllable count drops from five to three. Readers can now picture the symptom immediately without decoding a clinical term.
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

**output:** The patient has nausea and abdominal pain after eating due to gallbladder disease, and a laparoscopic cholecystectomy is scheduled.

| metric | value |
|---|---:|
| bertscore_f1 | 0.418 |
| coleman_liau | 16.53 |
| coleman_liau_drop | 9.12 |
| copy_jargon_rate | 1.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 16.04 |
| fkgl_drop | 3.39 |
| fre | 13.9 |
| fre_gain | 35.0 |
| human_edit_recall | 0.000 |
| length_ratio | 1.06 |
| n_words | 19.0 |
| nli_completeness | 0.949 |
| nli_faithfulness | 0.989 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 34.95 |
| smog | 15.90 |
| smog_drop | 0.00 |
| temporality_preservation | 1.000 |

### Stage 4 - arm `termonly`

**output:** Description: Feeling sick to the stomach and belly pain after eating - gallbladder disease - surgery to take out the gallbladder through small cuts is scheduled.

| metric | value |
|---|---:|
| bertscore_f1 | 0.604 |
| coleman_liau | 14.87 |
| coleman_liau_drop | 10.78 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 12.95 |
| fkgl_drop | 6.49 |
| fre | 45.0 |
| fre_gain | 66.1 |
| human_edit_recall | 1.000 |
| length_ratio | 1.33 |
| n_words | 24.0 |
| nli_completeness | 0.667 |
| nli_faithfulness | 0.132 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 24.87 |
| smog | 14.55 |
| smog_drop | 1.35 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 3 edits kept

- rejected: DROP noop      'Gall bladder disease' -> 'gallbladder disease'  (nothing changed)

| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `Nausea` -> `Feeling sick to the stomach` | replace | - | - | - | - | - | - | - |
| `abdominal pain` -> `belly pain` | replace | - | - | - | - | - | - | - |
| `Laparoscopic cholecystectomy` -> `surgery to take out the gallbladder through small cuts` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** The patient feels sick to the stomach and has a stomach ache after eating. The gallbladder is not working right. Surgery to take out the gallbladder using a small tube and camera is planned.

| metric | value |
|---|---:|
| bertscore_f1 | 0.348 |
| coleman_liau | 7.86 |
| coleman_liau_drop | 17.79 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 5.84 |
| fkgl_drop | 13.60 |
| fre | 73.4 |
| fre_gain | 94.5 |
| human_edit_recall | 1.000 |
| length_ratio | 1.89 |
| n_words | 34.0 |
| nli_completeness | 0.303 |
| nli_faithfulness | 0.637 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.200 |
| sari | 16.24 |
| smog | 9.73 |
| smog_drop | 6.18 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 4 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `Nausea` -> `sick to the stomach` | replace | attributed | -0.343 | -0.784 | 0.836 | 0.858 | 0.098 | - |
| `abdominal pain` -> `a stomach ache` | replace | attributed | 1.957 | 2.409 | 0.726 | 0.899 | 2.245 | - |
| `Gall bladder disease` -> `The gallbladder is not working right` | replace | attributed | 1.858 | 1.934 | 0.462 | 0.714 | 0.371 | - |
| `Laparoscopic cholecystectomy` -> `Surgery to take out the gallbladder using a small tube and camera` | replace | attributed | 14.553 | 14.876 | 0.819 | 0.826 | 7.375 | - |

**edit `Nausea` -> `sick to the stomach`**

- status: `attributed`
- log p full -0.7650, empty -0.4218
- masks scored: 66/66 (+8 top-k)
- ranked sources:
    - `+0.233` [justplainclear] cholecystectomy: A surgery to take out your gallbladder
    - `+0.134` [wiktionary] nausea: Nausea is the feeling of discomfort in the stomach, and the person will usually have a strong urge to 
    - `+0.126` [readme] Laparoscopic: A surgery that uses a small tube and camera to see inside your body.
    - `+0.081` [nih] nausea: A feeling of sickness or discomfort in the stomach that may come with an urge to vomit. Nausea is a si
    - `+0.077` [readme] cholecystectomy: A surgery to remove the gallbladder, a digestion-assisting organ in the stomach.

- rationale: Nausea is the uneasy, queasy feeling that often comes before vomiting, and "sick to the stomach" captures that same sensation in everyday language. Phrase frequency rises from Zipf 3.54 to 4.29, while age of acquisition drops from 8.63 to 5.26. Readers can immediately recognize the uncomfortable feeling without needing the clinical term.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `abdominal pain` -> `a stomach ache`**

- status: `attributed`
- log p full -0.9181, empty -2.8753
- masks scored: 66/66 (+8 top-k)
- ranked sources:
    - `+2.502` [readme] epigastric abdominal pain: Stomach ache that's felt below the ribs.
    - `+0.257` [wiktionary] gall: Gall is anger or hatred.
    - `+0.139` [wiktionary] gall: If you have the gall to do something, you do it even though it is very rude or unreasonable.
    - `+0.006` [readme] cholecystectomy: A surgery to remove the gallbladder, a digestion-assisting organ in the stomach.

- rationale: The glossary defines abdominal pain as a stomach ache felt below the ribs, so the replacement keeps the same everyday meaning in simpler words. Phrase frequency shifts from Zipf 3.56 to 3.39, while age of acquisition drops from 10.24 to 5.79. Readers can now recognize the symptom immediately without needing a clinical label.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `Gall bladder disease` -> `The gallbladder is not working right`**

- status: `attributed`
- log p full -2.4574, empty -4.3152
- masks scored: 66/66 (+8 top-k)
- ranked sources:
    - `+0.743` [wiktionary] gall: If you have the gall to do something, you do it even though it is very rude or unreasonable.
    - `+0.372` [readme] Cholecystectomy: A surgery to remove the gallbladder, an organ in your stomach that helps with digestion.
    - `+0.357` [wiktionary] gall: Gall is anger or hatred.
    - `+0.235` [readme] laparoscopic: A surgery where a small tube with a camera is used to see inside the body.
    - `+0.187` [readme] Laparoscopic: A surgery that uses a small tube and camera to see inside your body.

- rationale: The glossary text defines "gall" as bold rudeness, which is unrelated to the medical organ, so the replacement simply states in plain language that the gallbladder is malfunctioning. Phrase frequency decreases from Zipf 3.12 to 2.81, while age of acquisition falls from 12.44 to 11.68. Readers can now grasp that the organ itself is the problem without needing to interpret a clinical label.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `Laparoscopic cholecystectomy` -> `Surgery to take out the gallbladder using a small tube and camera`**

- status: `attributed`
- log p full -1.2867, empty -15.8396
- masks scored: 66/66 (+8 top-k)
- ranked sources:
    - `+9.861` [readme] Laparoscopic: A surgery that uses a small tube and camera to see inside your body.
    - `+2.486` [readme] laparoscopic: A surgery where a small tube with a camera is used to see inside the body.
    - `+0.688` [readme] Cholecystectomy: A surgery to remove the gallbladder, an organ in your stomach that helps with digestion.
    - `+0.427` [wiktionary] gall: Gall is anger or hatred.
    - `+0.303` [justplainclear] bladder disease: A disease or disorder of your bladder. Some bladder diseases may include: • urinary incontine

- rationale: The readme defines laparoscopic cholecystectomy as a surgery that uses a small tube and camera to see inside the body, so the replacement spells out that same technique in everyday words. Phrase frequency rises from Zipf 1.73 to 2.79, indicating the new wording is substantially more common. Readers can now grasp the procedure without needing to decode the clinical name.
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

**output:** There was a little swelling on his fourth finger, and he is still wearing his wedding ring on that finger.

| metric | value |
|---|---:|
| bertscore_f1 | 0.781 |
| coleman_liau | 7.37 |
| coleman_liau_drop | -0.33 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.667 |
| fkgl | 7.55 |
| fkgl_drop | -1.04 |
| fre | 76.6 |
| fre_gain | -3.9 |
| human_edit_recall | 1.000 |
| length_ratio | 1.11 |
| n_words | 20.0 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.993 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.667 |
| sari | 27.83 |
| severity_downgrade | 0.000 |
| severity_preservation | 0.000 |
| severity_tier_input | 1.000 |
| severity_tier_output | 1.000 |
| smog | 3.13 |
| smog_drop | 5.71 |

### Stage 4 - arm `termonly`

**output:** There was a little swelling of the fourth finger, on which he still is wearing his wedding band.

| metric | value |
|---|---:|
| bertscore_f1 | 0.951 |
| coleman_liau | 7.37 |
| coleman_liau_drop | -0.32 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.667 |
| fkgl | 6.51 |
| fkgl_drop | 0.00 |
| fre | 80.5 |
| fre_gain | 0.0 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 18.0 |
| nli_completeness | 0.992 |
| nli_faithfulness | 0.992 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 74.12 |
| severity_downgrade | 0.000 |
| severity_preservation | 0.000 |
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

**output:** There was a little swelling of the fourth finger, on which he still is wearing his wedding band.

| metric | value |
|---|---:|
| bertscore_f1 | 0.951 |
| coleman_liau | 7.37 |
| coleman_liau_drop | -0.32 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.667 |
| fkgl | 6.51 |
| fkgl_drop | 0.00 |
| fre | 80.5 |
| fre_gain | 0.0 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 18.0 |
| nli_completeness | 0.992 |
| nli_faithfulness | 0.992 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 74.12 |
| severity_downgrade | 0.000 |
| severity_preservation | 0.000 |
| severity_tier_input | 1.000 |
| severity_tier_output | 1.000 |
| smog | 3.13 |
| smog_drop | 5.71 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `edema` -> `swelling` | replace | attributed | 0.026 | 1.645 | 0.342 | 0.854 | 0.405 | - |
| `digit` -> `finger` | replace | attributed | 0.008 | 2.553 | 0.041 | 0.680 | 0.052 | - |

**edit `edema` -> `swelling`**

- status: `attributed`
- log p full -0.0063, empty -0.0320
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.563` [readme] edema: Swelling due to too much fluid in the body tissues.
    - `+0.158` [michigan] edema: Swelling caused by too much fluid in your body.
    - `+0.067` [nih] edema: Swelling caused by excess fluid in body tissues.
    - `+0.044` [readme] DIGIT: A digit is a finger or a toe.
    - `+0.030` [readme] Edema: Swelling in the body caused by too much fluid.

- rationale: Edema is the medical name for fluid collecting in body tissues, and "swelling" conveys that same visible puffiness in everyday language. Phrase frequency rises from Zipf 2.95 to 3.68, and the word shortens from three syllables to two. Readers can immediately picture the physical sign without needing to recall a clinical term.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `digit` -> `finger`**

- status: `attributed`
- log p full -0.0007, empty -0.0089
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.394` [readme] Edema: Swelling in the body caused by too much fluid.
    - `+0.342` [nih] edema: Swelling caused by excess fluid in body tissues.
    - `+0.270` [readme] edema: Swelling due to too much fluid in the body tissues.
    - `+0.100` [michigan] digit: A finger or toe.
    - `+0.071` [michigan] edema: Swelling caused by too much fluid in your body.

- rationale: "Digit" is a formal word for a finger or toe, so using "finger" keeps the same meaning in everyday language. Phrase frequency rises from Zipf 3.77 to 4.48, and age of acquisition drops from 9.26 to 3.43. Readers can picture the body part immediately without pausing on a technical term.
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

**output:** The parents say she seems to breathe fast, gets tired while eating, and has more trouble breathing and sweating.

| metric | value |
|---|---:|
| bertscore_f1 | 0.466 |
| coleman_liau | 10.42 |
| coleman_liau_drop | 4.96 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 7.35 |
| fkgl_drop | 5.48 |
| fre | 76.2 |
| fre_gain | 35.7 |
| human_edit_recall | 1.000 |
| length_ratio | 0.90 |
| n_words | 19.0 |
| nli_completeness | 0.950 |
| nli_faithfulness | 0.906 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.545 |
| sari | 18.82 |
| smog | 3.13 |
| smog_drop | 9.89 |

### Stage 4 - arm `termonly`

**output:** Parents say she seems to breathe fast, gets tired while eating with harder breathing and sweating.

| metric | value |
|---|---:|
| bertscore_f1 | 0.553 |
| coleman_liau | 11.71 |
| coleman_liau_drop | 3.67 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 6.88 |
| fkgl_drop | 5.95 |
| fre | 74.3 |
| fre_gain | 33.8 |
| human_edit_recall | 1.000 |
| length_ratio | 0.76 |
| n_words | 16.0 |
| nli_completeness | 0.938 |
| nli_faithfulness | 0.709 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.545 |
| sari | 19.58 |
| smog | 3.13 |
| smog_drop | 9.89 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `rapidly` -> `fast` | replace | - | - | - | - | - | - | - |
| `respiratory effort` -> `harder breathing` | replace | - | - | - | - | - | - | - |
| `diaphoresis` -> `sweating` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Parents say she seems to breathe fast, gets tired while eating with more work to breathe and heavy sweating.

| metric | value |
|---|---:|
| bertscore_f1 | 0.516 |
| coleman_liau | 9.51 |
| coleman_liau_drop | 5.88 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.667 |
| fkgl | 6.73 |
| fkgl_drop | 6.10 |
| fre | 80.7 |
| fre_gain | 40.2 |
| human_edit_recall | 1.000 |
| length_ratio | 0.90 |
| n_words | 19.0 |
| nli_completeness | 0.927 |
| nli_faithfulness | 0.208 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.545 |
| sari | 17.33 |
| smog | 3.13 |
| smog_drop | 9.89 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `rapidly` -> `fast` | replace | attributed | -0.338 | -3.587 | 0.799 | 0.854 | 0.025 | - |
| `respiratory effort` -> `work to breathe` | replace | attributed | -0.336 | -0.838 | 0.605 | 0.815 | 0.019 | - |
| `diaphoresis` -> `heavy sweating` | replace | attributed | 3.043 | 6.350 | 0.909 | 0.960 | 5.202 | - |

**edit `rapidly` -> `fast`**

- status: `attributed`
- log p full -0.3492, empty -0.0115
- masks scored: 66/66 (+5 top-k)
- ranked sources:
    - `+0.121` [readme] Respiratory: Related to how you breathe and the organs involved in breathing like the lungs and airways.
    - `+0.096` [justplainclear] diaphoresis: Sweating
    - `+0.052` [wiktionary] respiratory: A respiratory problem refers to something that affects breathing or the lungs.
    - `+0.043` [wiktionary] state: Any sovereign nation (nation that rules itself) is a state.
    - `+0.023` [readme] Diaphoresis: Intense sweating.

- rationale: "Rapidly" means happening with great speed, and "fast" conveys the same idea in a shorter, more familiar word. Word frequency rises from Zipf 4.34 to 5.13, and the syllable count drops from three to one. Readers can grasp the pace of an event without stumbling over a longer adverb.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `respiratory effort` -> `work to breathe`**

- status: `attributed`
- log p full -0.6991, empty -0.3631
- masks scored: 66/66 (+5 top-k)
- ranked sources:
    - `+0.136` [readme] Respiratory: Related to how you breathe and the organs involved in breathing like the lungs and airways.
    - `+0.117` [wiktionary] effort: The amount of work that is done on something.
    - `+0.084` [michigan] diaphoresis: Sweating, a clear, salty liquid produced by glands in your skin. Sweating is how your body cools 
    - `+0.048` [readme] diaphoresis: Heavy sweating.

- rationale: "Respiratory effort" refers to the physical exertion the body makes to move air in and out of the lungs, and "work to breathe" conveys that same idea using everyday language. Phrase frequency rises from Zipf 3.78 to 4.25, while age of acquisition drops from 11.00 to 5.86. Readers can immediately grasp the concept of labored breathing without needing to interpret a clinical phrase.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `diaphoresis` -> `heavy sweating`**

- status: `attributed`
- log p full -0.0356, empty -3.0789
- masks scored: 66/66 (+5 top-k)
- ranked sources:
    - `+7.173` [readme] diaphoresis: Heavy sweating.
    - `+1.971` [readme] Diaphoresis: Intense sweating.
    - `+0.602` [wiktionary] rapidly: If something is done rapidly, then it is done quickly or swiftly.
    - `+0.572` [michigan] state: To say or tell. In medicine, how you are doing.
    - `+0.559` [wiktionary] state: Any sovereign nation (nation that rules itself) is a state.

- rationale: The glossary defines diaphoresis simply as heavy sweating, so the replacement keeps the exact meaning in everyday words. Phrase frequency rises from Zipf 1.28 to 3.64, and age of acquisition drops from 15.22 to 4.05. Readers can now grasp the symptom immediately without needing a medical dictionary.
- audit: coverage 0.833, grounding_error=True, omission=False, source_ok=False, passage_ok=True

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

**output:** The patient has not used stimulant drugs for at least four to five months, according to the patient; however, he had start of chest pain this evening.

| metric | value |
|---|---:|
| bertscore_f1 | 0.849 |
| coleman_liau | 8.88 |
| coleman_liau_drop | 0.50 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 10.67 |
| fkgl_drop | 0.67 |
| fre | 66.6 |
| fre_gain | 6.6 |
| human_edit_recall | 1.000 |
| length_ratio | 1.12 |
| n_words | 27.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.197 |
| nli_faithfulness | 0.975 |
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
| `amphetamines` -> `stimulant drugs` | replace | - | - | - | - | - | - | - |
| `onset` -> `start` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** The patient has not used stimulant drugs for at least four to five months, according to the patient; however, he had the start of chest pain this evening.

| metric | value |
|---|---:|
| bertscore_f1 | 0.849 |
| coleman_liau | 8.62 |
| coleman_liau_drop | 0.76 |
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
| nli_completeness | 0.218 |
| nli_faithfulness | 0.974 |
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
| `amphetamines` -> `stimulant drugs` | replace | attributed | -0.140 | -0.266 | - | 0.762 | 0.674 | - |
| `onset` -> `the start` | replace | attributed | 0.817 | 1.586 | - | 0.833 | 1.296 | - |

**edit `amphetamines` -> `stimulant drugs`**

- status: `attributed`
- log p full -0.8210, empty -0.6808
- masks scored: 10/10 (+3 top-k)
- ranked sources:
    - `+0.821` [wiktionary] amphetamines: Amphetamine is a synthetic drug. It is a stimulant that helps people keep the focus and stay awa
    - `+0.146` [wiktionary] onset: The onset of something is the time when it begins (usually something bad).
    - `-0.395` [michigan] onset: The start.

- rationale: Amphetamines are a class of powerful stimulant drugs that speed up the central nervous system, and the replacement phrase names that broader category directly. Phrase frequency rises from Zipf 2.82 to 3.05, while age of acquisition drops from 14.6 to 9.2. Readers can now grasp the general drug type and its activating effect without needing to recognize the specific chemical class name.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `onset` -> `the start`**

- status: `attributed`
- log p full -0.3937, empty -1.2108
- masks scored: 10/10 (+3 top-k)
- ranked sources:
    - `+1.620` [michigan] onset: The start.
    - `+0.324` [wiktionary] onset: The onset of something is the time when it begins (usually something bad).
    - `+0.222` [wiktionary] amphetamines: Amphetamine is a synthetic drug. It is a stimulant that helps people keep the focus and stay awa

- rationale: "Onset" refers to the moment something begins, and "the start" conveys that same idea in everyday language. Phrase frequency rises from Zipf 3.72 to 5.56, and age of acquisition drops from 10.72 to 4.37. Readers can grasp the timing of a symptom or condition without pausing over a more formal word.
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

**output:** Orogastric suction was done and only a small amount of clear stomach fluid came out.

| metric | value |
|---|---:|
| bertscore_f1 | 0.366 |
| coleman_liau | 8.91 |
| coleman_liau_drop | 7.13 |
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
| nli_completeness | 0.993 |
| nli_faithfulness | 0.992 |
| replacement_f1 | 0.500 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 34.86 |
| smog | 8.84 |
| smog_drop | 0.00 |

### Stage 4 - arm `termonly`

**output:** A tube through the mouth into the stomach was used to pull out only a small amount of clear fluid.

| metric | value |
|---|---:|
| bertscore_f1 | 0.441 |
| coleman_liau | 5.34 |
| coleman_liau_drop | 10.70 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.250 |
| fkgl | 6.96 |
| fkgl_drop | 1.41 |
| fre | 80.8 |
| fre_gain | 27.9 |
| human_edit_recall | 1.000 |
| length_ratio | 1.25 |
| n_words | 20.0 |
| nli_completeness | 0.944 |
| nli_faithfulness | 0.860 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 35.12 |
| smog | 3.13 |
| smog_drop | 5.71 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `clear stomach contents` -> `clear fluid` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** A tube through the mouth sucked out only a little clear fluid from the stomach.

| metric | value |
|---|---:|
| bertscore_f1 | 0.439 |
| coleman_liau | 6.97 |
| coleman_liau_drop | 9.07 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.375 |
| fkgl | 5.21 |
| fkgl_drop | 3.16 |
| fre | 84.5 |
| fre_gain | 31.6 |
| human_edit_recall | 1.000 |
| length_ratio | 0.94 |
| n_words | 15.0 |
| nli_completeness | 0.974 |
| nli_faithfulness | 0.915 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 31.33 |
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

**output:** There is probably some restrictive element because of fibrosis.

| metric | value |
|---|---:|
| bertscore_f1 | 0.673 |
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
| sari | 23.42 |
| smog | 14.55 |
| smog_drop | 0.00 |
| uncertainty_preservation | 1.000 |

### Stage 4 - arm `termonly`

**output:** There is likely some stiffening because of scarring.

| metric | value |
|---|---:|
| bertscore_f1 | 0.555 |
| coleman_liau | 12.40 |
| coleman_liau_drop | 3.31 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 6.71 |
| fkgl_drop | 4.82 |
| fre | 61.2 |
| fre_gain | 32.7 |
| human_edit_recall | 1.000 |
| length_ratio | 0.73 |
| n_words | 8.0 |
| nli_completeness | 0.836 |
| nli_faithfulness | 0.907 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.250 |
| sari | 23.43 |
| smog | 8.84 |
| smog_drop | 5.71 |
| uncertainty_preservation | 1.000 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `restrictive element` -> `stiffening` | replace | - | - | - | - | - | - | - |
| `fibrosis` -> `scarring` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** There is likely some part that limits movement because of thick, scarred tissue.

| metric | value |
|---|---:|
| bertscore_f1 | 0.500 |
| coleman_liau | 11.37 |
| coleman_liau_drop | 4.34 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.750 |
| fkgl | 5.82 |
| fkgl_drop | 5.70 |
| fre | 76.5 |
| fre_gain | 48.0 |
| human_edit_recall | 1.000 |
| length_ratio | 1.18 |
| n_words | 13.0 |
| nli_completeness | 0.869 |
| nli_faithfulness | 0.690 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.250 |
| sari | 16.17 |
| smog | 3.13 |
| smog_drop | 11.43 |
| uncertainty_preservation | 1.000 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `restrictive element` -> `part that limits movement` | replace | attributed | 5.276 | 5.559 | 0.883 | 0.900 | 0.321 | - |
| `fibrosis` -> `thick, scarred tissue` | replace | attributed | 10.221 | 10.740 | 0.932 | 0.934 | 12.896 | - |

**edit `restrictive element` -> `part that limits movement`**

- status: `attributed`
- log p full -1.3977, empty -6.6739
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+1.737` [wiktionary] restrictive: If something is restrictive, it limits or controls what people can do.
    - `+1.416` [wiktionary] element: An element is one part of something bigger, such as a plan, an engine, or a business.
    - `+0.726` [nih] element: A basic part of a whole. In chemistry, refers to a simple substance that cannot be broken down into s
    - `+0.190` [readme] FIBROSIS: Fibrosis is tissue that becomes thick and scarred due to injury.
    - `-0.086` [wiktionary] element: An element is one basic kind of substance, such as iron (Fe), oxygen (O), or sodium (Na).

- rationale: Wiktionary defines "restrictive" as something that limits or controls what people can do, so "part that limits movement" preserves that core idea in everyday words. Phrase frequency rises from Zipf 3.49 to 4.33, and age of acquisition drops from 11.00 to 6.58. Readers can now picture the mechanical constraint without needing the abstract adjective.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `fibrosis` -> `thick, scarred tissue`**

- status: `attributed`
- log p full -0.9038, empty -11.1248
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+13.053` [readme] FIBROSIS: Fibrosis is tissue that becomes thick and scarred due to injury.
    - `+0.156` [wiktionary] element: An element is one basic kind of substance, such as iron (Fe), oxygen (O), or sodium (Na).
    - `+0.021` [wiktionary] restrictive: If something is restrictive, it limits or controls what people can do.

- rationale: The readme defines fibrosis as tissue that becomes thick and scarred after injury, so "thick, scarred tissue" preserves that exact description in everyday words. Phrase frequency rises from Zipf 3.19 to 3.21, and age of acquisition drops from 14.94 to 5.61. Readers can now picture the physical change in the body without needing a medical vocabulary.
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
| `uterus` -> `womb` | replace | attributed | 0.006 | 0.804 | 0.492 | 0.568 | 0.200 | - |
| `abdominal cavity` -> `belly` | replace | attributed | 0.001 | 1.532 | 0.740 | 0.832 | 2.202 | - |

**edit `uterus` -> `womb`**

- status: `attributed`
- log p full -0.0050, empty -0.0112
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.246` [justplainclear] uterus: Also known as: womb An organ in a woman's body where babies may grow during pregnancy Uterus
    - `+0.046` [thesaurus] uterus: womb
    - `+0.023` [michigan] uterus: Womb, or where a baby grows when a woman is pregnant.
    - `-0.095` [wiktionary] uterus: The uterus is the internal organ inside of a female mammal where an embryo grows into an infant ready 
    - `-0.171` [readme] abdominal cavity: The belly area where your stomach and other organs are located.

- rationale: The uterus is the muscular organ where a fetus develops during pregnancy, and "womb" is the everyday word that carries the same meaning in a single syllable. Phrase frequency rises from Zipf 3.40 to 3.63, while age of acquisition drops from 12.84 to 9.48. Readers can now recognize the organ immediately without needing the clinical term.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `abdominal cavity` -> `belly`**

- status: `attributed`
- log p full -0.0002, empty -0.0009
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+2.219` [readme] abdominal cavity: The belly area where your stomach and other organs are located.
    - `+0.017` [nih] uterus: The hollow, pear-shaped organ in a woman's pelvis. The uterus is where a fetus (unborn baby) develops 
    - `+0.016` [justplainclear] uterus: Also known as: womb An organ in a woman's body where babies may grow during pregnancy Uterus

- rationale: The abdominal cavity is the space inside the torso that holds the stomach, intestines, and other digestive organs, and "belly" points to that same region in everyday language. Phrase frequency rises from Zipf 3.29 to 4.10, while age of acquisition drops from 10.24 to 4.05. Readers can now picture the body area being discussed without needing anatomical terminology.
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

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `AP` -> `front` | replace | - | - | - | - | - | - | - |
| `lateral projections` -> `side views` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** This was viewed from the front and back and from the side.

| metric | value |
|---|---:|
| bertscore_f1 | 0.823 |
| coleman_liau | 3.97 |
| coleman_liau_drop | 3.37 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 0.89 |
| fkgl_drop | 4.07 |
| fre | 110.1 |
| fre_gain | 34.5 |
| human_edit_recall | 1.000 |
| laterality_preservation | 0.000 |
| length_ratio | 1.50 |
| n_words | 12.0 |
| nli_completeness | 0.594 |
| nli_faithfulness | 0.860 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 77.75 |
| smog | 3.13 |
| smog_drop | 8.08 |

annotation backend `novita`, 0 edits kept


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

**output:** The vocal cords move normally when the patient makes sounds and when they breathe.

| metric | value |
|---|---:|
| bertscore_f1 | 0.589 |
| coleman_liau | 10.26 |
| coleman_liau_drop | 4.32 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 5.04 |
| fkgl_drop | 3.14 |
| fre | 83.9 |
| fre_gain | 33.2 |
| human_edit_recall | 1.000 |
| length_ratio | 1.75 |
| n_words | 14.0 |
| nli_completeness | 0.989 |
| nli_faithfulness | 0.900 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 53.89 |
| smog | 8.84 |
| smog_drop | 2.37 |

### Stage 4 - arm `termonly`

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

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `phonation` -> `speaks` | replace | - | - | - | - | - | - | - |
| `ventilation` -> `breathes` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

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

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `phonation` -> `speaks` | replace | attributed | 0.127 | 0.410 | - | 0.466 | 0.101 | - |
| `ventilation` -> `breathes` | replace | attributed | 0.004 | 0.119 | - | 0.301 | 0.064 | - |

**edit `phonation` -> `speaks`**

- status: `attributed`
- log p full -0.3117, empty -0.4387
- masks scored: 34/34 (+4 top-k)
- ranked sources:
    - `+0.248` [wiktionary] cords: A long, thin rope or wire.
    - `+0.146` [wiktionary] ventilation: Ventilation is the replacement of stale air with fresh air.
    - `+0.118` [dictionary] Phonation (n.): The act or process by which articulate sounds are uttered; the utterance of articulate sounds;
    - `+0.096` [readme] ventilation: Ventilation is about bringing in fresh air.
    - `+0.060` [wiktionary] ventilation: Ventilation is the bodily process of breathing; the inhalation of air to provide oxygen, and the 

- rationale: Phonation refers to the physical act of producing vocal sound, and "speaks" conveys that same action in everyday language. Word frequency rises from Zipf 1.80 to 4.43, while the syllable count drops from two to one. Readers can immediately grasp that the topic involves using the voice without needing a technical term.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `ventilation` -> `breathes`**

- status: `attributed`
- log p full -0.0304, empty -0.0341
- masks scored: 34/34 (+4 top-k)
- ranked sources:
    - `+0.064` [readme] ventilation: Ventilation is about bringing in fresh air.
    - `-0.022` [dictionary] Phonation (n.): The act or process by which articulate sounds are uttered; the utterance of articulate sounds;
    - `-0.239` [wiktionary] ventilation: Ventilation is the replacement of stale air with fresh air.
    - `-0.248` [wiktionary] ventilation: Ventilation is the bodily process of breathing; the inhalation of air to provide oxygen, and the 

- rationale: Ventilation refers to the mechanical process of moving air in and out of the lungs, and "breathes" conveys that same action using a familiar, everyday verb. Word frequency shifts slightly from Zipf 3.60 to 3.30, while the syllable count drops from four to one. Readers can immediately picture the act of breathing without needing to interpret a clinical noun.
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

**output:** When the abdomen was opened, doctors saw a large amount of pus draining out.

| metric | value |
|---|---:|
| bertscore_f1 | 0.760 |
| coleman_liau | 7.36 |
| coleman_liau_drop | 1.78 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.750 |
| fkgl | 6.73 |
| fkgl_drop | 0.91 |
| fre | 71.8 |
| fre_gain | 8.3 |
| human_edit_recall | 1.000 |
| length_ratio | 0.93 |
| n_words | 14.0 |
| nli_completeness | 0.980 |
| nli_faithfulness | 0.649 |
| number_unit_preservation | 0.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 33.95 |
| smog | 8.84 |
| smog_drop | 2.37 |

### Stage 4 - arm `termonly`

**output:** Once the belly was opened, there was a lot of thick, yellow fluid.

| metric | value |
|---|---:|
| bertscore_f1 | 0.702 |
| coleman_liau | 4.68 |
| coleman_liau_drop | 4.46 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.400 |
| fkgl | 4.91 |
| fkgl_drop | 2.72 |
| fre | 83.0 |
| fre_gain | 19.5 |
| human_edit_recall | 1.000 |
| length_ratio | 0.87 |
| n_words | 13.0 |
| nli_completeness | 0.915 |
| nli_faithfulness | 0.273 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.200 |
| sari | 36.97 |
| smog | 3.13 |
| smog_drop | 8.08 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `abdomen` -> `belly` | replace | - | - | - | - | - | - | - |
| `gross purulent drainage` -> `a lot of thick, yellow fluid` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Once the belly was opened, there was a lot of pus leaking out.

| metric | value |
|---|---:|
| bertscore_f1 | 0.769 |
| coleman_liau | 3.34 |
| coleman_liau_drop | 5.80 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.600 |
| fkgl | 4.00 |
| fkgl_drop | 3.63 |
| fre | 89.5 |
| fre_gain | 26.0 |
| human_edit_recall | 1.000 |
| length_ratio | 0.87 |
| n_words | 13.0 |
| nli_completeness | 0.972 |
| nli_faithfulness | 0.937 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.200 |
| sari | 42.02 |
| smog | 3.13 |
| smog_drop | 8.08 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `abdomen` -> `belly` | replace | attributed | 0.033 | 1.306 | 0.536 | 0.683 | 0.189 | - |
| `gross purulent drainage` -> `a lot of pus leaking out` | replace | attributed | 4.702 | 5.649 | 0.904 | 0.941 | 2.315 | - |

**edit `abdomen` -> `belly`**

- status: `attributed`
- log p full -0.0125, empty -0.0453
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.377` [nih] abdomen: The area of the body that contains the pancreas, stomach, intestines, liver, gallbladder, and other o
    - `+0.188` [wiktionary] abdomen: The abdomen is the last of the three parts of an insect's body.
    - `+0.160` [wiktionary] gross: The gross amount is the total before you take away losses or expenses.
    - `+0.089` [readme] DRAINAGE: Fluid leaving an organ or body area.
    - `+0.048` [thesaurus] abdomen: stomach, stomach area, belly, tummy

- rationale: The abdomen is the part of the body between the chest and the hips that holds the stomach, intestines, and other organs, and "belly" is the everyday word people use for that same area. Phrase frequency rises from Zipf 3.56 to 4.10, while age of acquisition drops from 8.61 to 4.05. Readers can immediately picture the body region without pausing over a clinical term.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `gross purulent drainage` -> `a lot of pus leaking out`**

- status: `attributed`
- log p full -0.4874, empty -5.1893
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+3.152` [readme] drainage: When any fluid is leaking out of a body part.
    - `+0.837` [michigan] purulent: Pus.
    - `+0.796` [readme] DRAINAGE: Fluid leaving an organ or body area.
    - `+0.414` [wiktionary] gross: A gross violation or abuse is very bad and clearly wrong.
    - `+0.382` [wiktionary] abdomen: The abdomen is the last of the three parts of an insect's body.

- rationale: The readme glossary defines the concept as any fluid leaking out of a body part, so "a lot of pus leaking out" keeps that core idea while naming the specific fluid in everyday words. Phrase frequency rises from Zipf 1.92 to 2.94, and age of acquisition drops from 15.50 to 7.78. Readers can now picture the symptom immediately without needing to decode clinical terminology.
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

**output:** After the right upper quadrant was then explored. the ports were placed, the right upper quadrant was then explored.

| metric | value |
|---|---:|
| bertscore_f1 | 0.333 |
| coleman_liau | 10.08 |
| coleman_liau_drop | -0.50 |
| copy_jargon_rate | 1.000 |
| critical_error | 1.000 |
| fkgl | 4.26 |
| fkgl_drop | -0.26 |
| fre | 81.4 |
| fre_gain | -8.1 |
| human_edit_recall | 0.000 |
| laterality_preservation | 1.000 |
| length_ratio | 1.19 |
| n_words | 19.0 |
| nli_completeness | 0.039 |
| nli_faithfulness | 0.984 |
| number_unit_preservation | 0.000 |
| replacement_f1 | 0.000 |
| rewrite_aggressiveness | 1.000 |
| sari | 29.97 |
| smog | 3.13 |
| smog_drop | 0.00 |

### Stage 4 - arm `termonly`

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

**output:** Options such as keeping an eye on things, removing the prostate with a robot, and putting in tiny seeds with and without extra beams

| metric | value |
|---|---:|
| bertscore_f1 | 0.449 |
| coleman_liau | 8.82 |
| coleman_liau_drop | 12.07 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.286 |
| fkgl | 10.49 |
| fkgl_drop | 4.95 |
| fre | 62.6 |
| fre_gain | 51.5 |
| human_edit_recall | 1.000 |
| length_ratio | 1.04 |
| n_words | 24.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.982 |
| nli_faithfulness | 0.950 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.125 |
| sari | 38.85 |
| smog | 8.84 |
| smog_drop | 5.71 |

annotation backend `novita`, 4 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `watchful waiting` -> `keeping an eye on things` | replace | - | - | - | - | - | - | - |
| `robotic prostatectomy` -> `removing the prostate with a robot` | replace | - | - | - | - | - | - | - |
| `seed implantation` -> `putting in tiny seeds` | replace | - | - | - | - | - | - | - |
| `radiation` -> `extra beams` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Options such as close monitoring without treatment right away, surgery to remove the prostate using a robot, and placing tiny radioactive seeds with and without high-energy rays were discussed.

| metric | value |
|---|---:|
| bertscore_f1 | 0.588 |
| coleman_liau | 15.38 |
| coleman_liau_drop | 5.51 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.571 |
| fkgl | 17.29 |
| fkgl_drop | -1.85 |
| fre | 22.8 |
| fre_gain | 11.7 |
| human_edit_recall | 1.000 |
| length_ratio | 1.30 |
| n_words | 30.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.931 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 38.67 |
| smog | 14.55 |
| smog_drop | 0.00 |

annotation backend `novita`, 4 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `watchful waiting` -> `close monitoring without treatment right away` | replace | attributed | 4.978 | 5.043 | 0.648 | 0.895 | 5.079 | - |
| `robotic prostatectomy` -> `surgery to remove the prostate using a robot` | replace | attributed | -0.933 | -1.728 | 0.452 | 0.670 | 0.000 | - |
| `seed implantation` -> `placing tiny radioactive seeds` | replace | attributed | -1.061 | -1.926 | 0.249 | 0.610 | 0.012 | - |
| `radiation` -> `high-energy rays` | replace | attributed | 1.342 | 2.983 | 0.938 | 0.949 | 3.876 | - |

**edit `watchful waiting` -> `close monitoring without treatment right away`**

- status: `attributed`
- log p full -2.7636, empty -7.7421
- masks scored: 66/66 (+7 top-k)
- ranked sources:
    - `+5.242` [nih] watchful waiting: Closely watching a patient’s condition but not giving treatment unless symptoms appear or ch
    - `+0.163` [readme] prostatectomy: A prostatectomy is a surgery to remove part or all of the prostate and some surrounding tissue.
    - `+0.141` [nih] radiation: Energy released in the form of particle or electromagnetic waves. Common sources of radiation inclu

- rationale: The NIH glossary defines watchful waiting as closely observing a patient’s condition and delaying treatment until symptoms appear or change, so “close monitoring without treatment right away” preserves that exact approach in everyday words. Phrase frequency rises from Zipf 3.09 to 4.18, and age of acquisition drops slightly from 8.16 to 8.11. Readers can now grasp the strategy of active observation without needing to know the clinical label.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `robotic prostatectomy` -> `surgery to remove the prostate using a robot`**

- status: `attributed`
- log p full -1.3374, empty -0.4047
- masks scored: 66/66 (+7 top-k)
- ranked sources:

- rationale: "Robotic prostatectomy" names the operation that removes the prostate with the help of a surgical robot, and the replacement spells out that same procedure in everyday words. Phrase frequency rises from Zipf 2.13 to 3.50, while age of acquisition drops from 15.27 to 15.00. Readers can now grasp exactly what the surgery involves without needing to decode the technical label.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `seed implantation` -> `placing tiny radioactive seeds`**

- status: `attributed`
- log p full -1.4490, empty -0.3885
- masks scored: 66/66 (+7 top-k)
- ranked sources:
    - `+0.193` [readme] radiation: High energy rays used to kill cancer cells.
    - `+0.182` [nih] radiation: Energy released in the form of particle or electromagnetic waves. Common sources of radiation inclu
    - `-0.005` [readme] Radiation: Radiation is powerful energy waves that are sometimes utilized to destroy cancer cells.

- rationale: Seed implantation refers to a procedure in which small radioactive pellets are inserted into the body to treat cancer, and the replacement spells out that action by describing it as placing tiny radioactive seeds. Phrase frequency rises from Zipf 2.99 to 3.48, while age of acquisition shifts slightly from 11.95 to 12.11. Readers can now picture the treatment step without needing to interpret a compact medical label.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `radiation` -> `high-energy rays`**

- status: `attributed`
- log p full -0.1634, empty -1.5057
- masks scored: 66/66 (+7 top-k)
- ranked sources:
    - `+4.117` [readme] radiation: High energy rays used to kill cancer cells.
    - `+0.240` [nih] radiation: Energy released in the form of particle or electromagnetic waves. Common sources of radiation inclu
    - `+0.138` [thesaurus] radiation: see ionizing radiation and non-ionizing radiation
    - `+0.059` [wiktionary] radiation: Radiation is the emission or transmission of energy in the form of waves or particles through space

- rationale: The readme defines radiation as high-energy rays used to kill cancer cells, so the replacement simply restates that definition in everyday words. Phrase frequency decreases from Zipf 4.27 to 4.00. Readers can now picture the treatment as powerful beams rather than an abstract technical term.
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

**output:** He was also reportedly taking Lasix before he was hospitalized, possibly.

| metric | value |
|---|---:|
| bertscore_f1 | 0.587 |
| coleman_liau | 13.67 |
| coleman_liau_drop | 0.05 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 12.30 |
| fkgl_drop | 1.97 |
| fre | 26.5 |
| fre_gain | 15.9 |
| human_edit_recall | 1.000 |
| length_ratio | 0.73 |
| n_words | 11.0 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.993 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 36.01 |
| smog | 13.02 |
| smog_drop | 0.00 |
| temporality_preservation | 1.000 |
| uncertainty_preservation | 1.000 |

### Stage 4 - arm `termonly`

**output:** He was also said to be on a water pill before the hospital stay, maybe.

| metric | value |
|---|---:|
| bertscore_f1 | 0.578 |
| coleman_liau | 3.49 |
| coleman_liau_drop | 10.23 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 6.78 |
| fkgl_drop | 7.49 |
| fre | 73.2 |
| fre_gain | 62.6 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 15.0 |
| nli_completeness | 0.069 |
| nli_faithfulness | 0.003 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.200 |
| sari | 38.36 |
| smog | 8.84 |
| smog_drop | 4.18 |
| temporality_preservation | 1.000 |
| uncertainty_preservation | 0.000 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `reportedly` -> `said to be` | replace | - | - | - | - | - | - | - |
| `Lasix` -> `a water pill` | replace | - | - | - | - | - | - | - |
| `prior to` -> `before` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** He was also said to be on a water pill before the hospital stay, maybe.

| metric | value |
|---|---:|
| bertscore_f1 | 0.578 |
| coleman_liau | 3.49 |
| coleman_liau_drop | 10.23 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 6.78 |
| fkgl_drop | 7.49 |
| fre | 73.2 |
| fre_gain | 62.6 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 15.0 |
| nli_completeness | 0.069 |
| nli_faithfulness | 0.003 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.200 |
| sari | 38.36 |
| smog | 8.84 |
| smog_drop | 4.18 |
| temporality_preservation | 1.000 |
| uncertainty_preservation | 0.000 |

annotation backend `novita`, 4 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `reportedly` -> `said to be` | replace | attributed | 0.544 | 1.142 | 0.653 | 0.720 | 0.267 | - |
| `Lasix` -> `a water pill` | replace | attributed | -0.012 | -0.260 | 0.216 | 0.468 | 0.138 | - |
| `prior to` -> `before` | replace | attributed | -0.005 | -1.012 | 0.802 | 0.903 | 0.258 | - |
| `hospitalization` -> `hospital stay` | replace | attributed | 0.000 | 0.085 | 0.387 | 0.563 | 0.090 | - |

**edit `reportedly` -> `said to be`**

- status: `attributed`
- log p full -0.4138, empty -0.9581
- masks scored: 66/66 (+7 top-k)
- ranked sources:
    - `+0.431` [wiktionary] reportedly: If something is reportedly true, people say it happened, but we don't have other reasons to believ
    - `+0.164` [readme] Hospitalization: Being admitted to a hospital for an extended period of time.
    - `+0.012` [readme] hospitalization: Being admitted to and staying in a hospital.
    - `+0.005` [wiktionary] hospitalization: Hospitalization is the period of time when a person is in hospital for medical care.

- rationale: "Reportedly" signals that information comes from others rather than direct knowledge, and "said to be" conveys that same attribution in everyday words. Phrase frequency rises from Zipf 4.13 to 5.93, while the syllable count drops from four to three. Readers can immediately grasp that the claim is second‑hand without tripping over a longer, less familiar adverb.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `Lasix` -> `a water pill`**

- status: `attributed`
- log p full -0.0532, empty -0.0413
- masks scored: 66/66 (+7 top-k)
- ranked sources:
    - `+0.138` [wiktionary] reportedly: If something is reportedly true, people say it happened, but we don't have other reasons to believ

- rationale: Lasix is a brand name for furosemide, a diuretic that helps the body get rid of extra fluid, so "a water pill" conveys the same idea in everyday language. Phrase frequency rises from Zipf 1.98 to 4.02. Patients can now recognize the medication's purpose without needing to know the proprietary name.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `prior to` -> `before`**

- status: `attributed`
- log p full -0.0078, empty -0.0028
- masks scored: 66/66 (+7 top-k)
- ranked sources:
    - `+0.258` [wiktionary] hospitalization: Hospitalization is the process of putting a person in hospital for medical care.
    - `-0.180` [readme] Hospitalization: Being admitted to a hospital for an extended period of time.
    - `-0.220` [readme] hospitalization: Being admitted to and staying in a hospital.

- rationale: "Prior to" simply means "before," so the replacement keeps the exact same temporal relationship in a shorter, more familiar word. Phrase frequency rises from Zipf 4.85 to 5.93, and age of acquisition drops from 10.63 to 5.45. Readers can grasp the sequence of events without pausing on a formal, three-syllable preposition.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `hospitalization` -> `hospital stay`**

- status: `attributed`
- log p full -0.0008, empty -0.0009
- masks scored: 66/66 (+7 top-k)
- ranked sources:
    - `+0.261` [readme] hospitalization: Being admitted to and staying in a hospital.
    - `+0.171` [wiktionary] hospitalization: Hospitalization is the period of time when a person is in hospital for medical care.
    - `+0.124` [wiktionary] reportedly: If something is reportedly true, people say it happened, but we don't have other reasons to believ
    - `+0.066` [wiktionary] hospitalization: Hospitalization is the process of putting a person in hospital for medical care.
    - `-0.083` [readme] Hospitalization: Being admitted to a hospital for an extended period of time.

- rationale: Hospitalization refers to the period when someone is admitted to a hospital for care, and "hospital stay" conveys that same idea in everyday language. Phrase frequency rises from Zipf 3.09 to 4.88, while age of acquisition drops from 9.53 to 5.55. Readers can immediately grasp the concept without needing to process a longer, more formal word.
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

**output:** The four heart rooms are normal in size.

| metric | value |
|---|---:|
| bertscore_f1 | 0.477 |
| coleman_liau | 3.70 |
| coleman_liau_drop | 11.37 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.143 |
| fkgl | 0.80 |
| fkgl_drop | 9.40 |
| fre | 103.5 |
| fre_gain | 65.6 |
| human_edit_recall | 1.000 |
| length_ratio | 0.62 |
| n_words | 8.0 |
| nli_completeness | 0.969 |
| nli_faithfulness | 0.972 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 34.74 |
| smog | 3.13 |
| smog_drop | 8.08 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `cardiac chambers` -> `heart rooms` | replace | - | - | - | - | - | - | - |
| `within normal limits` -> `normal in size` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** The size of the four heart rooms is normal.

| metric | value |
|---|---:|
| bertscore_f1 | 0.647 |
| coleman_liau | 2.82 |
| coleman_liau_drop | 12.24 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.143 |
| fkgl | 1.03 |
| fkgl_drop | 9.18 |
| fre | 103.7 |
| fre_gain | 65.8 |
| human_edit_recall | 1.000 |
| length_ratio | 0.69 |
| n_words | 9.0 |
| nli_completeness | 0.972 |
| nli_faithfulness | 0.976 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 36.65 |
| smog | 3.13 |
| smog_drop | 8.08 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `cardiac chambers` -> `heart rooms` | replace | attributed | 0.377 | 1.352 | 0.826 | 0.881 | 1.141 | - |
| `within normal limits` -> `normal` | replace | attributed | -0.033 | -4.596 | 0.847 | 0.880 | 0.028 | - |

**edit `cardiac chambers` -> `heart rooms`**

- status: `attributed`
- log p full -0.1741, empty -0.5511
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+1.249` [wiktionary] chambers: A chamber is a room that is often used for sleeping.
    - `+0.109` [readme] cardiac: Related to the heart.
    - `+0.092` [wiktionary] limits: The limit is the edge of how far something can go. It can go up to the limit but no farther.
    - `+0.044` [justplainclear] normal: Whats expected for a person similar to you or to what's usual for you

- rationale: "Cardiac chambers" refers to the four hollow spaces inside the heart that collect and pump blood, and "heart rooms" conveys that same anatomy using everyday words. Phrase frequency rises from Zipf 3.64 to 4.49, while age of acquisition drops from 11.74 to 5.17. Readers can now picture the heart's basic structure without needing specialized vocabulary.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `within normal limits` -> `normal`**

- status: `attributed`
- log p full -0.0335, empty -0.0003
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.590` [iowa] CARDIAC: related to the heart
    - `+0.561` [nih] cardiac: Having to do with the heart.
    - `+0.489` [justplainclear] limits: A certain point that you can't go past; a certain amount but no more
    - `+0.417` [wiktionary] limits: The limit is the edge of how far something can go. It can go up to the limit but no farther.
    - `+0.395` [michigan] cardiac: Related to your heart.

- rationale: "Within normal limits" means the test result falls inside the expected healthy range, and the single word "normal" conveys that same idea in plain language. Phrase frequency rises from Zipf 4.32 to 5.01, while age of acquisition drops from 7.65 to 5.53. Readers can grasp the result immediately without parsing a multi-word phrase.
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

**output:** A digital rectal exam was done and no masses were found.

| metric | value |
|---|---:|
| bertscore_f1 | 0.483 |
| coleman_liau | 5.24 |
| coleman_liau_drop | 11.12 |
| copy_jargon_rate | 0.500 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 5.86 |
| fkgl_drop | 5.66 |
| fre | 72.6 |
| fre_gain | 44.1 |
| human_edit_recall | 0.500 |
| length_ratio | 1.00 |
| n_words | 11.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.993 |
| nli_faithfulness | 0.994 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 16.13 |
| smog | 8.84 |
| smog_drop | 2.37 |

### Stage 4 - arm `termonly`

**output:** A doctor checked the patient's bottom with a gloved finger and felt no lumps.

| metric | value |
|---|---:|
| bertscore_f1 | 0.402 |
| coleman_liau | 7.77 |
| coleman_liau_drop | 8.58 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.333 |
| fkgl | 5.04 |
| fkgl_drop | 6.48 |
| fre | 83.9 |
| fre_gain | 55.4 |
| human_edit_recall | 1.000 |
| length_ratio | 1.36 |
| n_words | 15.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.652 |
| nli_faithfulness | 0.070 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.286 |
| sari | 22.68 |
| smog | 3.13 |
| smog_drop | 8.08 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `masses` -> `lumps` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** A doctor checked the rectum with a gloved finger and felt no lumps.

| metric | value |
|---|---:|
| bertscore_f1 | 0.431 |
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
| nli_completeness | 0.697 |
| nli_faithfulness | 0.025 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.286 |
| sari | 23.00 |
| smog | 3.13 |
| smog_drop | 8.08 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `masses` -> `lumps` | replace | attributed | 0.006 | 0.516 | - | 0.738 | 0.084 | - |

**edit `masses` -> `lumps`**

- status: `attributed`
- log p full -0.0093, empty -0.0155
- masks scored: 18/18 (+2 top-k)
- ranked sources:
    - `+0.504` [wiktionary] performed: When you perform something, you do it.
    - `+0.420` [wiktionary] masses: A measure of how much material is in something.
    - `+0.142` [nih] digital rectal examination: An examination in which a doctor inserts a lubricated, gloved finger into the rect
    - `-0.330` [wiktionary] masses: The masses are the regular people, not those in power.

- rationale: "Masses" in a medical context refers to abnormal growths or swellings in the body, and "lumps" conveys the same idea in everyday language. Phrase frequency drops from Zipf frequency falls from 3.94 to 3.194, while syllable count drops from two to one. Readers can now recognize the physical finding immediately without technical terminology.
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

**output:** He then had seizures and weakness on one side of his body, went to the hospital, got a C. difficile infection, and is now in a nursing home.

| metric | value |
|---|---:|
| bertscore_f1 | 0.624 |
| coleman_liau | 4.46 |
| coleman_liau_drop | 5.82 |
| copy_jargon_rate | 0.333 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 5.88 |
| fkgl_drop | 5.34 |
| fre | 77.8 |
| fre_gain | 24.1 |
| human_edit_recall | 0.667 |
| length_ratio | 0.97 |
| n_words | 28.0 |
| nli_completeness | 0.021 |
| nli_faithfulness | 0.936 |
| replacement_f1 | 0.800 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.667 |
| sari | 32.91 |
| smog | 10.13 |
| smog_drop | 4.43 |
| temporality_preservation | 1.000 |

### Stage 4 - arm `termonly`

**output:** He then had a problem with fits, weakness on one side of the body, has been to the hospital, developed a gut infection from a germ called C. difficile, and is in the nursing home currently.

| metric | value |
|---|---:|
| bertscore_f1 | 0.823 |
| coleman_liau | 6.40 |
| coleman_liau_drop | 3.87 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.667 |
| fkgl | 7.82 |
| fkgl_drop | 3.41 |
| fre | 71.1 |
| fre_gain | 17.3 |
| human_edit_recall | 1.000 |
| length_ratio | 1.24 |
| n_words | 36.0 |
| nli_completeness | 0.005 |
| nli_faithfulness | 0.884 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 79.30 |
| smog | 12.16 |
| smog_drop | 2.39 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `seizures` -> `fits` | replace | - | - | - | - | - | - | - |
| `hemiparesis` -> `weakness on one side of the body` | replace | - | - | - | - | - | - | - |
| `C-diff` -> `a gut infection from a germ called C. difficile` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** He then had a problem with seizures, weakness on one side of the body, has been to the hospital, developed a gut infection that causes diarrhea, and is in the nursing home currently.

| metric | value |
|---|---:|
| bertscore_f1 | 0.829 |
| coleman_liau | 8.79 |
| coleman_liau_drop | 1.48 |
| copy_jargon_rate | 0.333 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 15.16 |
| fkgl_drop | -3.93 |
| fre | 45.2 |
| fre_gain | -8.6 |
| human_edit_recall | 0.667 |
| length_ratio | 1.14 |
| n_words | 33.0 |
| nli_completeness | 0.235 |
| nli_faithfulness | 0.794 |
| replacement_f1 | 0.800 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 74.23 |
| smog | 15.90 |
| smog_drop | -1.35 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `hemiparesis` -> `weakness on one side of the body` | replace | attributed | -0.192 | -1.147 | 0.888 | 0.869 | 0.999 | - |
| `C-diff` -> `a gut infection that causes diarrhea` | replace | attributed | 3.946 | 4.630 | 0.876 | 0.901 | 0.708 | - |

**edit `hemiparesis` -> `weakness on one side of the body`**

- status: `attributed`
- log p full -0.2960, empty -0.1038
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+1.098` [readme] hemiparesis: Weakness on one side of the body.
    - `+0.099` [wiktionary] seizures: If someone seizes (takes) something from someone by force, or arrests someone, it is a seizure.
    - `-0.160` [readme] Seizures: Seizures are when the brain has sudden abnormal activity that can lead to loss of consciousness and 
    - `-0.217` [dorland] C-diff: Clostridioides difficile
    - `-0.228` [readme] Clostridium difficile colitis: A type of gut infection that causes symptoms like fever, diarrhea, and cramps.

- rationale: Hemiparesis means weakness affecting one side of the body, and the replacement spells that out directly in everyday words. Phrase frequency rises from Zipf 1.49 to 4.14. Readers can now grasp the symptom immediately without needing to decode a technical label.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `C-diff` -> `a gut infection that causes diarrhea`**

- status: `attributed`
- log p full -0.6922, empty -4.6379
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+3.376` [readme] Clostridium difficile colitis: A type of gut infection that causes symptoms like fever, diarrhea, and cramps.
    - `+2.668` [nih] Clostridium difficile: A type of bacterium found in human and animal waste. Clostridium difficile is a common 
    - `+0.664` [wiktionary] seizures: If someone seizes (takes) something from someone by force, or arrests someone, it is a seizure.
    - `+0.550` [readme] Seizures: Seizures are when the brain has sudden abnormal activity that can lead to loss of consciousness and 
    - `+0.032` [readme] seizures: Seizures are when the brain has strange electrical activity that may make someone lose consciousness

- rationale: The readme defines C-diff as a gut infection that brings fever, diarrhea, and cramps, so the longer phrase keeps the core idea while spelling it out in everyday words. Patients can now recognize the illness from its most obvious symptom without needing to know the clinical shorthand.
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

**output:** He has been using continuous positive airway pressure for several months and is back for a follow-up visit to see how the treatment is working.

| metric | value |
|---|---:|
| bertscore_f1 | 0.684 |
| coleman_liau | 10.16 |
| coleman_liau_drop | 2.49 |
| copy_jargon_rate | 0.833 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 12.57 |
| fkgl_drop | -0.27 |
| fre | 49.5 |
| fre_gain | 3.4 |
| human_edit_recall | 0.167 |
| length_ratio | 1.04 |
| n_words | 26.0 |
| nli_completeness | 0.993 |
| nli_faithfulness | 0.994 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 0.286 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.600 |
| sari | 50.21 |
| smog | 13.02 |
| smog_drop | 0.00 |
| temporality_preservation | 0.000 |

### Stage 4 - arm `termonly`

**output:** He has been using a machine that keeps his airway open with steady air pressure for several months, and comes back for a check-up to see how the treatment is working.

| metric | value |
|---|---:|
| bertscore_f1 | 0.674 |
| coleman_liau | 8.13 |
| coleman_liau_drop | 4.52 |
| copy_jargon_rate | 0.333 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.250 |
| fkgl | 12.11 |
| fkgl_drop | 0.19 |
| fre | 63.5 |
| fre_gain | 17.4 |
| human_edit_recall | 0.667 |
| length_ratio | 1.28 |
| n_words | 32.0 |
| nli_completeness | 0.980 |
| nli_faithfulness | 0.770 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 0.800 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.429 |
| sari | 53.65 |
| smog | 3.13 |
| smog_drop | 9.89 |
| temporality_preservation | 0.000 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `continuous positive airway pressure` -> `a machine that keeps his airway open with steady air pressure` | replace | - | - | - | - | - | - | - |
| `followup` -> `check-up` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** He has been using a machine that keeps his breathing open with steady air pressure for several months, and comes back for a checkup to see how the treatment is working.

| metric | value |
|---|---:|
| bertscore_f1 | 0.698 |
| coleman_liau | 8.69 |
| coleman_liau_drop | 3.96 |
| copy_jargon_rate | 0.167 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.200 |
| fkgl | 12.11 |
| fkgl_drop | 0.19 |
| fre | 63.5 |
| fre_gain | 17.4 |
| human_edit_recall | 0.833 |
| length_ratio | 1.24 |
| n_words | 31.0 |
| nli_completeness | 0.982 |
| nli_faithfulness | 0.879 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 0.909 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.375 |
| sari | 53.91 |
| smog | 3.13 |
| smog_drop | 9.89 |
| temporality_preservation | 0.000 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `continuous positive airway pressure` -> `a machine that keeps his breathing open with steady air pressure` | replace | attributed | 4.588 | 4.612 | 0.793 | 0.789 | 0.480 | - |
| `followup` -> `checkup` | replace | attributed | 2.148 | 4.595 | 0.937 | 0.952 | 6.263 | - |

**edit `continuous positive airway pressure` -> `a machine that keeps his breathing open with steady air pressure`**

- status: `attributed`
- log p full -3.7102, empty -8.2977
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+1.859` [wiktionary] airway: An airway is a path an aircraft takes.
    - `+1.379` [wiktionary] airway: The airway in our body refers to the trachea.
    - `+0.428` [readme] Positive: Something is there.
    - `+0.193` [wiktionary] positive: If you are positive about something, you are sure that you are not mistaken.
    - `+0.023` [wiktionary] continuous: Something that is continuous happens without stopping.

- rationale: The glossary source defines "airway" as a path an aircraft takes, so the replacement "keeps his breathing open with steady air pressure" preserves the idea of an open passage for air while using everyday words. Phrase frequency rises from Zipf 3.14 to 3.81, and age of acquisition drops from 11.39 to 8.95. Readers can now picture the treatment as a simple machine that holds the breathing passage open with constant pressure.
- audit: coverage 0.833, grounding_error=True, omission=False, source_ok=True, passage_ok=False

**edit `followup` -> `checkup`**

- status: `attributed`
- log p full -0.0804, empty -2.2287
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+6.516` [readme] followup: Going back to your doctor for a checkup or follow-up appointment.
    - `+0.253` [readme] continuous: Continuous means something that never stops or has interruptions.
    - `+0.232` [wiktionary] positive: If you are positive about something, you are sure that you are not mistaken.
    - `+0.214` [wiktionary] pressure: If a person is under pressure, they feel stressed.

- rationale: The readme text treats "followup" and "checkup" as interchangeable reasons to return to the doctor, so "checkup" preserves the intended meaning in a more familiar word. Phrase frequency rises slightly from Zipf 2.87 to 2.88, and the syllable count drops from three to two. Readers can now recognize the purpose of the visit without pausing over a compound term.
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

**output:** The patient should take small bites and small sips to help lower the chance of food or liquid going into the airway or lungs.

| metric | value |
|---|---:|
| bertscore_f1 | 0.651 |
| coleman_liau | 7.38 |
| coleman_liau_drop | 2.25 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 8.52 |
| fkgl_drop | -0.05 |
| fre | 76.7 |
| fre_gain | 10.4 |
| human_edit_recall | 1.000 |
| length_ratio | 0.80 |
| n_words | 24.0 |
| nli_completeness | 0.773 |
| nli_faithfulness | 0.757 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.600 |
| sari | 34.61 |
| severity_downgrade | 0.000 |
| severity_preservation | 1.000 |
| severity_tier_input | 1.000 |
| severity_tier_output | 1.000 |
| smog | 3.13 |
| smog_drop | 8.08 |

annotation backend `novita`, 0 edits kept


### Stage 4 - arm `grounded`

**output:** The patient should take small bites and small sips to help lower the chance of breathing food or liquid into the lungs by mistake and of food or liquid going into the airway.

| metric | value |
|---|---:|
| bertscore_f1 | 0.602 |
| coleman_liau | 8.08 |
| coleman_liau_drop | 1.54 |
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
| nli_completeness | 0.861 |
| nli_faithfulness | 0.958 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.600 |
| sari | 34.30 |
| severity_downgrade | 0.000 |
| severity_preservation | 1.000 |
| severity_tier_input | 1.000 |
| severity_tier_output | 1.000 |
| smog | 3.13 |
| smog_drop | 8.08 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `aspiration` -> `breathing food or liquid into the lungs by mistake` | replace | attributed | 16.924 | 17.278 | 0.838 | 0.835 | 3.131 | - |
| `penetration` -> `food or liquid going into the airway` | replace | attributed | 1.300 | 1.827 | 0.804 | 0.716 | 0.029 | - |

**edit `aspiration` -> `breathing food or liquid into the lungs by mistake`**

- status: `attributed`
- log p full -1.2096, empty -18.1333
- masks scored: 66/66 (+3 top-k)
- ranked sources:
    - `+9.381` [readme] aspiration: Breathing food or liquid into your lungs by mistake.
    - `+6.250` [readme] aspiration: Breathing in food or liquid by mistake.
    - `+0.103` [nih] aspiration: Removal of fluid or tissue through a needle. Also, the accidental breathing in of food or fluid in
    - `-0.200` [iowa] ASPIRATION: fluid entering the lungs, such as after vomiting
    - `-0.519` [wiktionary] penetration: Penetration is the penis being inserted into the vagina or another part of the body during sex.

- rationale: The readme defines aspiration as breathing food or liquid into your lungs by mistake, so the replacement simply restates that definition in full. Phrase frequency rises from Zipf 3.30 to 3.64, and age of acquisition drops from 11.47 to 6.52. Readers can now grasp the dangerous event immediately without needing to know the clinical label.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `penetration` -> `food or liquid going into the airway`**

- status: `attributed`
- log p full -0.7174, empty -2.0172
- masks scored: 66/66 (+3 top-k)
- ranked sources:
    - `+0.627` [readme] aspiration: Breathing food or liquid into your lungs by mistake.
    - `+0.598` [readme] aspiration: Breathing in food or liquid by mistake.
    - `+0.235` [wiktionary] penetration: Penetration is the action of penetrating into something.

- rationale: Penetration in this context means that food or liquid enters the airway instead of staying in the throat, so the replacement spells out that exact event in everyday words. Phrase frequency decreases from Zipf 3.71 to 3.16, while age of acquisition rises slightly from 11.05 to 11.16. Readers can now picture the problem immediately without needing to know the clinical term.
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

**output:** The patient was woken up, the breathing tube was taken out, and they were moved to the recovery room in satisfactory condition.

| metric | value |
|---|---:|
| bertscore_f1 | 0.756 |
| coleman_liau | 10.01 |
| coleman_liau_drop | 3.54 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 10.69 |
| fkgl_drop | 1.60 |
| fre | 57.6 |
| fre_gain | 23.9 |
| human_edit_recall | 1.000 |
| length_ratio | 1.10 |
| n_words | 22.0 |
| nli_completeness | 0.988 |
| nli_faithfulness | 0.986 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 47.11 |
| smog | 13.02 |
| smog_drop | 2.88 |

### Stage 4 - arm `termonly`

**output:** The patient was woken up, had the breathing tube taken out, and was moved to the recovery room in good condition.

| metric | value |
|---|---:|
| bertscore_f1 | 0.731 |
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
| nli_completeness | 0.989 |
| nli_faithfulness | 0.987 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 37.26 |
| smog | 11.21 |
| smog_drop | 4.70 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `awakened` -> `woken up` | replace | - | - | - | - | - | - | - |
| `extubated` -> `had the breathing tube taken out` | replace | - | - | - | - | - | - | - |
| `satisfactory` -> `good` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** The patient was woken up, the breathing tube was taken out, and they were moved to the recovery room in good condition.

| metric | value |
|---|---:|
| bertscore_f1 | 0.741 |
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
| nli_completeness | 0.987 |
| nli_faithfulness | 0.989 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 37.94 |
| smog | 11.21 |
| smog_drop | 4.70 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `awakened` -> `woken up` | replace | attributed | 0.001 | 0.137 | - | 0.770 | 0.318 | - |
| `extubated` -> `the breathing tube was taken out` | replace | attributed | 0.337 | 0.595 | - | 0.723 | 0.041 | - |
| `satisfactory` -> `good` | replace | attributed | 0.351 | 2.462 | - | 0.751 | 1.323 | - |

**edit `awakened` -> `woken up`**

- status: `attributed`
- log p full -0.0041, empty -0.0047
- masks scored: 34/34 (+6 top-k)
- ranked sources:
    - `+0.379` [wiktionary] awakened: If you awaken somebody, they stop sleeping because of something you do.
    - `+0.061` [wiktionary] satisfactory: If something is satisfactory, it is good enough.
    - `-0.219` [readme] extubated: Not having a breathing tube anymore.

- rationale: "Awakened" means to stop sleeping, and "woken up" conveys the same idea using the everyday phrasing people actually use. Phrase frequency rises from Zipf 3.30 to 3.37, making the wording noticeably more familiar. Readers can grasp the meaning instantly without pausing on a more formal verb form.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `extubated` -> `the breathing tube was taken out`**

- status: `attributed`
- log p full -0.6804, empty -1.0178
- masks scored: 34/34 (+6 top-k)
- ranked sources:
    - `+0.219` [readme] extubated: Taking out a tube used for breathing.
    - `+0.178` [wiktionary] awakened: If you awaken somebody, they stop sleeping because of something you do.
    - `+0.141` [michigan] satisfactory: When something is okay or good.
    - `+0.119` [readme] extubated: Not having a breathing tube anymore.
    - `+0.062` [wiktionary] satisfactory: If something is satisfactory, it is good enough.

- rationale: "Extubated" means the breathing tube was removed, and the replacement spells out that action in everyday words. Phrase frequency rises from Zipf 1.26 to 3.99, showing the new wording is far more common. Readers can now picture the step without needing the technical verb.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `satisfactory` -> `good`**

- status: `attributed`
- log p full -0.0400, empty -0.3907
- masks scored: 34/34 (+6 top-k)
- ranked sources:
    - `+2.026` [wiktionary] satisfactory: If something is satisfactory, it is good enough.
    - `+0.702` [michigan] satisfactory: When something is okay or good.
    - `+0.387` [wiktionary] awakened: If you awaken somebody, they stop sleeping because of something you do.
    - `+0.087` [readme] extubated: Taking out a tube used for breathing.
    - `+0.086` [readme] extubated: Not having a breathing tube anymore.

- rationale: "Satisfactory" means meeting an acceptable standard, and "good" conveys that same idea in a shorter, more familiar word. Phrase frequency rises from Zipf 3.57 to 6.12, while age of acquisition drops from 8.84 to 3.55. Readers can grasp the positive assessment immediately without pausing on a longer, less common term.
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

**output:** Physical examination: General: The patient was asleep, but easily woken up.

| metric | value |
|---|---:|
| bertscore_f1 | 0.715 |
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
| nli_completeness | 0.982 |
| nli_faithfulness | 0.990 |
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
| `aroused` -> `woken up` | replace | attributed | -0.252 | -0.721 | - | - | - | - |

**edit `aroused` -> `woken up`**

- status: `attributed`
- log p full -0.5694, empty -0.3170
- masks scored: 4/4 (+1 top-k)
- ranked sources:
    - `-0.465` [wiktionary] aroused: If something arouses a feeling or emotion, it causes that feeling or emotion.

- rationale: "Aroused" means brought out of sleep into a conscious state, and "woken up" conveys that same shift in plain, everyday language. Phrase frequency rises slightly from Zipf 3.35 to 3.37. The reader can now grasp the change in alertness without pausing on a word that can also carry sexual or emotional overtones.
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

**output:** He should follow up in about 10 days for a recheck and to get a prescription for the planned AFOs, which he will need for up to 6 months.

| metric | value |
|---|---:|
| bertscore_f1 | 0.640 |
| coleman_liau | 4.58 |
| coleman_liau_drop | 2.13 |
| copy_jargon_rate | 1.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 9.55 |
| fkgl_drop | 1.33 |
| fre | 78.2 |
| fre_gain | 14.9 |
| human_edit_recall | 0.000 |
| length_ratio | 1.04 |
| n_words | 29.0 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.994 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.667 |
| sari | 24.01 |
| smog | 8.84 |
| smog_drop | 4.18 |

### Stage 4 - arm `termonly`

**output:** He is to follow up in about 10 days for a recheck and a prescription for the intended ankle-foot braces, which he will need for up to 6 months.

| metric | value |
|---|---:|
| bertscore_f1 | 0.755 |
| coleman_liau | 5.58 |
| coleman_liau_drop | 1.13 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 11.59 |
| fkgl_drop | -0.70 |
| fre | 63.6 |
| fre_gain | 0.3 |
| human_edit_recall | 1.000 |
| length_ratio | 1.07 |
| n_words | 30.0 |
| nli_completeness | 0.959 |
| nli_faithfulness | 0.595 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 31.22 |
| smog | 13.02 |
| smog_drop | 0.00 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `approximately` -> `about` | replace | - | - | - | - | - | - | - |
| `AFOs` -> `ankle-foot braces` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** He is to follow up in about 10 days for a recheck and a prescription for ankle-foot braces, which he will need for up to 6 months.

| metric | value |
|---|---:|
| bertscore_f1 | 0.727 |
| coleman_liau | 4.80 |
| coleman_liau_drop | 1.91 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 10.24 |
| fkgl_drop | 0.65 |
| fre | 69.8 |
| fre_gain | 6.5 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 28.0 |
| nli_completeness | 0.950 |
| nli_faithfulness | 0.725 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 31.14 |
| smog | 11.21 |
| smog_drop | 1.82 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `approximately` -> `about` | replace | attributed | -0.008 | -1.885 | - | 0.833 | 0.220 | - |
| `AFOs` -> `ankle-foot braces` | replace | attributed | 2.216 | 2.766 | - | 0.905 | 0.291 | - |

**edit `approximately` -> `about`**

- status: `attributed`
- log p full -0.0095, empty -0.0014
- masks scored: 10/10 (+3 top-k)
- ranked sources:
    - `+0.403` [dorland] AFOs: ankle-foot orthosis
    - `+0.184` [justplainclear] AFO: Also known as: ankle-foot orthosis, walking boot A brace that supports your ankle or foot An AFO is a bra
    - `-1.431` [wiktionary] approximately: Approximately is close to, but not exactly.

- rationale: "Approximately" means roughly or close to a certain amount, and "about" conveys that same sense of estimation in a shorter, more familiar word. Word frequency rises from Zipf 4.64 to 6.40, and the syllable count drops from five to two. Readers can grasp the intended approximation immediately without stumbling over a longer, less common term.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `AFOs` -> `ankle-foot braces`**

- status: `attributed`
- log p full -0.7955, empty -3.0114
- masks scored: 10/10 (+3 top-k)
- ranked sources:
    - `+1.076` [justplainclear] AFO: Also known as: ankle-foot orthosis, walking boot A brace that supports your ankle or foot An AFO is a bra
    - `+0.786` [dorland] AFOs: ankle-foot orthosis
    - `+0.348` [wiktionary] approximately: Approximately is close to, but not exactly.

- rationale: AFOs stands for ankle-foot orthoses, which are rigid or semi-rigid supports that hold the foot and ankle in a stable position, and "ankle-foot braces" conveys that same function in everyday language. Phrase frequency rises from Zipf 1.36 to 3.35, while age of acquisition drops from 14.6 to 9.2. Readers can now picture the device and its purpose without needing to decode a clinical abbreviation.
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

**output:** The external genitalia looked normal.

| metric | value |
|---|---:|
| bertscore_f1 | 0.506 |
| coleman_liau | 15.40 |
| coleman_liau_drop | 2.07 |
| copy_jargon_rate | 0.750 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 12.32 |
| fkgl_drop | 1.76 |
| fre | 15.6 |
| fre_gain | 7.3 |
| human_edit_recall | 0.250 |
| length_ratio | 0.62 |
| n_words | 5.0 |
| nli_completeness | 0.302 |
| nli_faithfulness | 0.995 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 20.79 |
| smog | 11.21 |
| smog_drop | 1.82 |

### Stage 4 - arm `termonly`

**output:** The private parts looked normal.

| metric | value |
|---|---:|
| bertscore_f1 | 0.464 |
| coleman_liau | 9.60 |
| coleman_liau_drop | 7.88 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 2.88 |
| fkgl_drop | 11.20 |
| fre | 83.3 |
| fre_gain | 75.0 |
| human_edit_recall | 1.000 |
| length_ratio | 0.62 |
| n_words | 5.0 |
| nli_completeness | 0.136 |
| nli_faithfulness | 0.291 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.250 |
| sari | 25.91 |
| smog | 3.13 |
| smog_drop | 9.89 |

annotation backend `novita`, 0 edits kept


### Stage 4 - arm `grounded`

**output:** The private parts looked normal.

| metric | value |
|---|---:|
| bertscore_f1 | 0.464 |
| coleman_liau | 9.60 |
| coleman_liau_drop | 7.88 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 2.88 |
| fkgl_drop | 11.20 |
| fre | 83.3 |
| fre_gain | 75.0 |
| human_edit_recall | 1.000 |
| length_ratio | 0.62 |
| n_words | 5.0 |
| nli_completeness | 0.136 |
| nli_faithfulness | 0.291 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.250 |
| sari | 25.91 |
| smog | 3.13 |
| smog_drop | 9.89 |

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

**output:** She is 21 days after an exploratory laparotomy for ovarian cancer staging.

| metric | value |
|---|---:|
| bertscore_f1 | 0.575 |
| coleman_liau | 11.70 |
| coleman_liau_drop | -0.78 |
| copy_jargon_rate | 0.750 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 13.67 |
| fkgl_drop | -1.50 |
| fre | 18.4 |
| fre_gain | -12.5 |
| human_edit_recall | 0.250 |
| length_ratio | 0.71 |
| n_words | 12.0 |
| nli_completeness | 0.969 |
| nli_faithfulness | 0.991 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 0.400 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 55.55 |
| smog | 13.02 |
| smog_drop | 0.00 |

### Stage 4 - arm `termonly`

**output:** She is 21 days after surgery to look inside the belly and check how far the ovarian cancer has spread.

| metric | value |
|---|---:|
| bertscore_f1 | 0.624 |
| coleman_liau | 6.50 |
| coleman_liau_drop | 4.42 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.750 |
| fkgl | 9.32 |
| fkgl_drop | 2.85 |
| fre | 63.9 |
| fre_gain | 32.9 |
| human_edit_recall | 1.000 |
| length_ratio | 1.18 |
| n_words | 20.0 |
| nli_completeness | 0.627 |
| nli_faithfulness | 0.283 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 56.11 |
| smog | 11.21 |
| smog_drop | 1.82 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `postop` -> `21 days after` | replace | - | - | - | - | - | - | - |
| `ovarian cancer staging` -> `ovarian cancer has spread` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** She is 21 days after surgery to check the organs in the belly for issues and to find out how far the cancer has spread.

| metric | value |
|---|---:|
| bertscore_f1 | 0.554 |
| coleman_liau | 4.82 |
| coleman_liau_drop | 6.10 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.600 |
| fkgl | 9.26 |
| fkgl_drop | 2.91 |
| fre | 73.2 |
| fre_gain | 42.2 |
| human_edit_recall | 1.000 |
| length_ratio | 1.47 |
| n_words | 25.0 |
| nli_completeness | 0.021 |
| nli_faithfulness | 0.076 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 48.84 |
| smog | 8.84 |
| smog_drop | 4.18 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `postop` -> `21 days after surgery` | replace | attributed | 0.280 | 2.431 | 0.759 | 0.781 | 0.107 | - |

**edit `postop` -> `21 days after surgery`**

- status: `attributed`
- log p full -0.0317, empty -0.3117
- masks scored: 66/66 (+2 top-k)
- ranked sources:
    - `+0.787` [readme] Exploratory laparotomy: Exploratory laparotomy: Surgery to check the organs in the belly for issues.
    - `+0.680` [readme] exploratory laparotomy: Surgery to check for problems in your belly.
    - `+0.624` [readme] postop: After surgery.
    - `+0.327` [readme] PostOP: PostOP means after surgery.
    - `+0.035` [readme] Ovarian: Ovarian means related to the ovaries where eggs are produced.

- rationale: "Postop" is a brief medical shorthand for the period following an operation, and spelling it out as "21 days after surgery" makes the specific timeframe immediately clear. Phrase frequency rises from Zipf 1.53 to 4.46, showing the longer wording is far more common in everyday language. Readers can now grasp exactly when the follow-up occurs without having to decode an abbreviation or guess the length of the recovery window.
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

**output:** He has been given to him. The prescription for prednisone as part of his chemotherapy. He was given a prescription for prednisone as part of his chemotherapy. He was given a prescription for prednisone as part of his chemotherapy. He was given a prescription for prednisone as part of his chemotherapy. He was given a prescription for prednisone as part of his chemotherapy. He was given a prescription for prednisone as part of his chemotherapy. He was given a prescription for prednisone as part of his chemotherapy. He was given a prescription for prednisone as part of his chemotherapy. He was given a prescription for prednisone as part of his chemotherapy. He was given a prescription for prednisone as part of his chemotherapy. He was given a prescription for prednisone as part of his chemotherapy. He was given a prescription for prednisone as part of his chemotherapy. He was given a prescription for prednisone as part of his chemotherapy. He was given a prescription for prednisone as part of his chemotherapy. He was given a prescription for prednisone as part of his chemotherapy. He was given a prescription for prednisone as part of his chemotherapy. He was given a prescription for prednisone as part of his chemotherapy. He was given a prescription for prednisone as part of his chemotherapy. He was given a prescription for prednisone as part of his chemotherapy. He was given a prescription for prednisone as part of his chemotherapy. He was given a prescription for prednisone as part of his chemotherapy. He was given a prescription for prednisone as part of his chemotherapy. He was given a prescription for prednisone as part of his chemotherapy. He was given a prescription for prednisone as part of his chemotherapy. He was given a prescription for prednisone as part of his chemotherapy. He was given a prescription for prednisone as part of his chemotherapy. He was given a prescription for prednisone as part of his chemotherapy. He was given a prescription for prednisone as part of his chemotherapy. He was given a prescription for prednisone as part of his chemotherapy. He was given a prescription for prednisone as part of his chemotherapy. He was given a prescription for prednisone as part of his chemotherapy. He was given a prescription for prednisone as part of his chemotherapy. He was given a prescription for prednisone as part of his chemotherapy. He was given a prescription for prednisone as part of his chemotherapy. He was given a prescription for prednisone as part of his chemotherapy. He was given a prescription for prednisone as part of his chemotherapy. He was given a prescription for prednisone as part of his chemotherapy. He was given a prescription for prednisone as part of his chemotherapy. He was given a prescription for prednisone as part of his chemotherapy. He was given a prescription for prednisone as part of his chemotherapy. He was given a prescription for prednisone as part of his chemotherapy. He was given a prescription for prednisone as part of his chemotherapy. He was given a prescription for prednisone as part of his chemotherapy. He was given a prescription for prednisone as part of his chemotherapy. He was given a prescription for prednisone as part of his chemotherapy. He was given a prescription for prednisone as part of his chemotherapy. He was given a prescription for prednisone as part of his chemotherapy. He was given a prescription for prednisone as part of his chemotherapy. He was given a prescription for prednisone as part of his chemotherapy. He was given a prescription for prednisone as part of his chemotherapy. He was given a prescription for prednisone as part of his chemotherapy. He was given a prescription for prednisone as part of his chemotherapy. He was given a prescription for prednisone as part of his chemotherapy. He was given a prescription for prednisone as part of his chemotherapy. He was given a prescription for prednisone as part of his chemotherapy. He was given a prescription for prednisone as part of his chemotherapy. He was given a prescription for prednisone as part of his chemotherapy. He was given a prescription for prednisone as part of his chemotherapy. He was given a prescription for prednisone as part of his chemotherapy. He was given a prescription for prednisone as part of his chemotherapy. He was given a prescription for prednisone as part of his chemotherapy. He was given a prescription for prednisone as part of his chemotherapy. He was given a prescription for prednisone as part of his chemotherapy. He was given a prescription for prednisone as part of his chemotherapy. He was given a prescription for prednisone as part of his chemotherapy. He was given a prescription for prednisone as part of his chemotherapy. He was given a prescription for prednisone as part of his chemotherapy. He was given a prescription for prednisone as part of his chemotherapy.

| metric | value |
|---|---:|
| bertscore_f1 | -0.251 |
| coleman_liau | 10.20 |
| coleman_liau_drop | 0.73 |
| copy_jargon_rate | 1.000 |
| critical_error | 0.000 |
| drug_preservation | 1.000 |
| fkgl | 8.68 |
| fkgl_drop | -0.14 |
| fre | 54.0 |
| fre_gain | -3.0 |
| human_edit_recall | 0.000 |
| length_ratio | 54.60 |
| n_words | 819.0 |
| nli_completeness | 0.988 |
| nli_faithfulness | 0.991 |
| replacement_f1 | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 50.61 |
| smog | 11.15 |
| smog_drop | 0.06 |

### Stage 4 - arm `termonly`

**output:** A prescription for a steroid medicine as part of his cancer drug treatment has been given to him.

| metric | value |
|---|---:|
| bertscore_f1 | 0.773 |
| coleman_liau | 8.01 |
| coleman_liau_drop | 2.91 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| drug_preservation | 0.000 |
| fkgl | 8.47 |
| fkgl_drop | 0.07 |
| fre | 66.4 |
| fre_gain | 9.4 |
| human_edit_recall | 1.000 |
| length_ratio | 1.20 |
| n_words | 18.0 |
| nli_completeness | 0.039 |
| nli_faithfulness | 0.351 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 77.23 |
| smog | 11.21 |
| smog_drop | 0.00 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `prednisone` -> `a steroid medicine` | replace | - | - | - | - | - | - | - |
| `chemotherapy` -> `cancer drug treatment` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** A prescription for a medicine that lowers the body's immune response and inflammation as part of his treatment that uses drugs to kill cancer cells has been given to him.

| metric | value |
|---|---:|
| bertscore_f1 | 0.558 |
| coleman_liau | 10.09 |
| coleman_liau_drop | 0.84 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| drug_preservation | 0.000 |
| fkgl | 13.81 |
| fkgl_drop | -5.27 |
| fre | 49.5 |
| fre_gain | -7.5 |
| human_edit_recall | 1.000 |
| length_ratio | 2.07 |
| n_words | 31.0 |
| nli_completeness | 0.006 |
| nli_faithfulness | 0.296 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 68.25 |
| smog | 13.02 |
| smog_drop | -1.82 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `prednisone` -> `a medicine that lowers the body's immune response and inflammation` | replace | attributed | 20.053 | 20.527 | 0.697 | 0.698 | 11.846 | - |
| `chemotherapy` -> `treatment that uses drugs to kill cancer cells` | replace | attributed | 3.461 | 3.789 | 0.867 | 0.883 | 2.202 | - |

**edit `prednisone` -> `a medicine that lowers the body's immune response and inflammation`**

- status: `attributed`
- log p full -0.9745, empty -21.0278
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+15.912` [readme] Prednisone: A medication that lowers the body's immune response and inflammation.
    - `+4.066` [nih] prednisone: A drug used to reduce inflammation and lower the body’s immune response.  It is used with other dr
    - `+2.833` [readme] chemotherapy: Using drugs to treat cancer or other diseases.
    - `+1.676` [wiktionary] chemotherapy: Chemotherapy is the chemical treatment intended to be kill the cancerous cells in a patient.
    - `+0.610` [michigan] chemotherapy: A drug that kills cancer cells.

- rationale: The readme defines prednisone as a medication that lowers the body's immune response and inflammation, so the replacement spells out that exact mechanism in everyday words. Phrase frequency rises from Zipf 2.56 to 3.02, and age of acquisition drops from 17.17 to 12.32. Readers can now grasp what the drug does without needing to recognize the brand or generic name.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `chemotherapy` -> `treatment that uses drugs to kill cancer cells`**

- status: `attributed`
- log p full -1.2525, empty -4.7135
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+4.913` [justplainclear] chemotherapy: A treatment where drugs are used to kill cancer cells These drugs can be given into the vein (in
    - `+2.710` [nih] chemotherapy: Treatment that uses drugs to stop the growth of cancer cells, either by killing the cells or by 
    - `+2.399` [michigan] chemotherapy: A drug that kills cancer cells.
    - `+1.597` [wiktionary] chemotherapy: Chemotherapy is the chemical treatment intended to be kill the cancerous cells in a patient.
    - `+0.768` [nih] prednisone: A drug used to reduce inflammation and lower the body’s immune response.  It is used with other dr

- rationale: The glossary defines chemotherapy as a treatment where drugs are used to kill cancer cells, so the replacement spells out that exact meaning in everyday words. Phrase frequency rises from Zipf 3.56 to 4.11, and age of acquisition drops from 12.53 to 8.39. Readers can now grasp the core idea of the therapy without needing to know the technical label.
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

**output:** The doctor used flashing lights to test the patient's brain waves, but the brain did not clearly follow the rhythm of the lights.

| metric | value |
|---|---:|
| bertscore_f1 | 0.387 |
| coleman_liau | 9.14 |
| coleman_liau_drop | 5.06 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 8.26 |
| fkgl_drop | 0.82 |
| fre | 76.8 |
| fre_gain | 27.3 |
| human_edit_recall | 1.000 |
| length_ratio | 1.41 |
| n_words | 24.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.898 |
| nli_faithfulness | 0.077 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 18.81 |
| smog | 3.13 |
| smog_drop | 5.71 |

### Stage 4 - arm `termonly`

**output:** Light stimulation was done, but no clear brain-wave response to the light was seen.

| metric | value |
|---|---:|
| bertscore_f1 | 0.779 |
| coleman_liau | 9.84 |
| coleman_liau_drop | 4.36 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.200 |
| fkgl | 5.88 |
| fkgl_drop | 3.20 |
| fre | 77.8 |
| fre_gain | 28.3 |
| human_edit_recall | 1.000 |
| length_ratio | 0.88 |
| n_words | 15.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.811 |
| nli_faithfulness | 0.855 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.250 |
| sari | 37.37 |
| smog | 8.84 |
| smog_drop | 0.00 |

annotation backend `novita`, 2 edits kept

- rejected: DROP non-term  'performed' -> 'done'  (orig is not exactly one extracted hard term)

| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `Photic stimulation` -> `stimulation` | replace | - | - | - | - | - | - | - |
| `photic driving` -> `brain-wave response to the light` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** The doctor used flashing lights, but the brain did not clearly follow the rhythm.

| metric | value |
|---|---:|
| bertscore_f1 | 0.406 |
| coleman_liau | 9.43 |
| coleman_liau_drop | 4.77 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 5.88 |
| fkgl_drop | 3.20 |
| fre | 77.8 |
| fre_gain | 28.3 |
| human_edit_recall | 1.000 |
| length_ratio | 0.82 |
| n_words | 14.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.899 |
| nli_faithfulness | 0.093 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 18.28 |
| smog | 3.13 |
| smog_drop | 5.71 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `Photic stimulation` -> `flashing lights` | replace | attributed | -0.117 | -1.751 | 0.359 | 0.689 | 0.375 | - |

**edit `Photic stimulation` -> `flashing lights`**

- status: `attributed`
- log p full -0.1436, empty -0.0265
- masks scored: 66/66 (+2 top-k)
- ranked sources:
    - `+0.535` [wiktionary] driving: If you drive a car or other vehicle, you control its movement and direction.
    - `+0.161` [dictionary] Clear-cut (a.): Concisely and distinctly expressed.
    - `+0.053` [dictionary] Clear-cut (a.): Having a sharp, distinct outline, like that of a cameo.
    - `-0.149` [wiktionary] driving: If something is driving, it is moving quickly and strongly.
    - `-0.185` [readme] stimulation: Making something more active or alert.

- rationale: Photic stimulation refers to exposing the eyes to repeated bright flashes, so "flashing lights" names the very thing the patient sees. Phrase frequency rises from Zipf 1.80 to 3.63, and the syllable count drops from six to three. The reader can now picture the procedure immediately without decoding a technical label.
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

**output:** Both parents died of heart attacks.

| metric | value |
|---|---:|
| bertscore_f1 | 0.632 |
| coleman_liau | 7.30 |
| coleman_liau_drop | 11.62 |
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
| nli_completeness | 0.572 |
| nli_faithfulness | 0.920 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 36.98 |
| smog | 3.13 |
| smog_drop | 11.43 |

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
| `myocardial infarctions` -> `heart attacks` | replace | attributed | -0.000 | -0.235 | - | 0.471 | 0.472 | - |

**edit `myocardial infarctions` -> `heart attacks`**

- status: `attributed`
- log p full -0.0006, empty -0.0005
- masks scored: 34/34 (+2 top-k)
- ranked sources:
    - `+0.694` [iowa] MYOCARDIAL INFARCTION: heart attack
    - `+0.223` [readme] inferior myocardial infarction: A heart attack caused by a blockage in a blood vessel that affects the lower p
    - `+0.146` [justplainclear] myocardial infarction: A heart attack
    - `-0.126` [readme] inferior wall myocardial infarction: Heart damage at the bottom of the left ventricle due to a blocked artery.

- rationale: Myocardial infarctions are the medical name for heart attacks, and the simpler phrase keeps the same meaning in everyday language. Phrase frequency rises from Zipf 1.57 to 4.59, while age of acquisition drops from 16.64 to 5.17. Readers can now recognize the condition immediately without needing specialized vocabulary.
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

**output:** Both legs have moderate swelling that leaves a dent when pressed, and the swelling goes up to the knees.

| metric | value |
|---|---:|
| bertscore_f1 | 0.470 |
| coleman_liau | 8.28 |
| coleman_liau_drop | 1.17 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 6.10 |
| fkgl_drop | 5.12 |
| fre | 85.1 |
| fre_gain | 51.0 |
| human_edit_recall | 1.000 |
| laterality_preservation | 1.000 |
| length_ratio | 0.68 |
| n_words | 19.0 |
| nli_completeness | 0.751 |
| nli_faithfulness | 0.178 |
| number_unit_preservation | 0.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.200 |
| sari | 37.27 |
| smog | 8.84 |
| smog_drop | 4.18 |

### Stage 4 - arm `termonly`

**output:** Arms and legs: moderate swelling that leaves a dent when pressed, on both sides, up to the knees.

| metric | value |
|---|---:|
| bertscore_f1 | 0.533 |
| coleman_liau | 7.04 |
| coleman_liau_drop | 2.41 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 5.20 |
| fkgl_drop | 6.03 |
| fre | 89.9 |
| fre_gain | 55.7 |
| human_edit_recall | 1.000 |
| laterality_preservation | 1.000 |
| length_ratio | 0.64 |
| n_words | 18.0 |
| nli_completeness | 0.811 |
| nli_faithfulness | 0.525 |
| number_unit_preservation | 0.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.200 |
| sari | 36.78 |
| smog | 8.84 |
| smog_drop | 4.18 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `bilateral pitting edema` -> `moderate swelling that leaves a dent when pressed, on both sides` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Both legs and arms have moderate swelling that leaves a dent when pressed, reaching up to the knees.

| metric | value |
|---|---:|
| bertscore_f1 | 0.445 |
| coleman_liau | 8.66 |
| coleman_liau_drop | 0.80 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 5.85 |
| fkgl_drop | 5.38 |
| fre | 85.2 |
| fre_gain | 51.0 |
| human_edit_recall | 1.000 |
| laterality_preservation | 1.000 |
| length_ratio | 0.64 |
| n_words | 18.0 |
| nli_completeness | 0.629 |
| nli_faithfulness | 0.088 |
| number_unit_preservation | 0.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.200 |
| sari | 36.78 |
| smog | 8.84 |
| smog_drop | 4.18 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `bilateral pitting edema` -> `moderate swelling that leaves a dent when pressed` | replace | attributed | -0.355 | -0.684 | 0.700 | 0.764 | 0.210 | - |

**edit `bilateral pitting edema` -> `moderate swelling that leaves a dent when pressed`**

- status: `attributed`
- log p full -0.9238, empty -0.5689
- masks scored: 66/66 (+2 top-k)
- ranked sources:
    - `+0.357` [readme] pitting edema: Swelling in the body that leaves an indention (pit) when pressed.
    - `+0.147` [michigan] bilateral: On both sides.
    - `+0.080` [nih] bilateral: Affecting both the right and left sides of the body.

- rationale: "Bilateral pitting edema" means swelling on both sides of the body that leaves a temporary dent when pressed, and the replacement spells out that exact physical sign in everyday words. Phrase frequency rises from Zipf 2.64 to 3.25, while age of acquisition drops from 15.07 to 11.22. Readers can now picture the symptom and recognize it without needing specialized medical vocabulary.
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

**output:** The questions that follow are mostly part of a psychosocial donor evaluation.

| metric | value |
|---|---:|
| bertscore_f1 | 0.470 |
| coleman_liau | 13.15 |
| coleman_liau_drop | 5.79 |
| copy_jargon_rate | 1.000 |
| critical_error | 0.000 |
| fkgl | 10.72 |
| fkgl_drop | 3.55 |
| fre | 39.6 |
| fre_gain | 29.0 |
| human_edit_recall | 0.000 |
| length_ratio | 0.80 |
| n_words | 12.0 |
| nli_completeness | 0.993 |
| nli_faithfulness | 0.993 |
| replacement_f1 | 0.000 |
| rewrite_aggressiveness | 1.000 |
| sari | 14.96 |
| smog | 11.21 |
| smog_drop | 1.82 |

### Stage 4 - arm `termonly`

**output:** The questions that follow are mainly part of a donor check-up that looks at mental and social health.

| metric | value |
|---|---:|
| bertscore_f1 | 0.462 |
| coleman_liau | 8.98 |
| coleman_liau_drop | 9.96 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 7.82 |
| fkgl_drop | 6.45 |
| fre | 71.1 |
| fre_gain | 60.5 |
| human_edit_recall | 1.000 |
| length_ratio | 1.27 |
| n_words | 19.0 |
| nli_completeness | 0.987 |
| nli_faithfulness | 0.885 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.800 |
| sari | 17.40 |
| smog | 3.13 |
| smog_drop | 9.89 |

annotation backend `novita`, 0 edits kept


### Stage 4 - arm `grounded`

**output:** The questions that follow are mostly about the mental and social parts of checking a donor.

| metric | value |
|---|---:|
| bertscore_f1 | 0.388 |
| coleman_liau | 9.54 |
| coleman_liau_drop | 9.40 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 8.35 |
| fkgl_drop | 5.92 |
| fre | 63.7 |
| fre_gain | 53.1 |
| human_edit_recall | 1.000 |
| length_ratio | 1.07 |
| n_words | 16.0 |
| nli_completeness | 0.981 |
| nli_faithfulness | 0.923 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.750 |
| sari | 21.36 |
| smog | 3.13 |
| smog_drop | 9.89 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `psychosocial` -> `mental and social parts` | replace | attributed | 1.994 | 2.712 | - | 1.000 | 7.526 | - |

**edit `psychosocial` -> `mental and social parts`**

- status: `attributed`
- log p full -0.5999, empty -2.5934
- masks scored: 6/6 (+1 top-k)
- ranked sources:
    - `+5.495` [michigan] psychosocial: Including both the mental and social aspects of disease.
    - `-2.031` [nih] psychosocial: In medicine, having to do with the mental, emotional, social, and spiritual effects of a disease

- rationale: "Psychosocial" refers to the interplay between a person's mental state and their social environment, and "mental and social parts" breaks that combined idea into its two clear components. Phrase frequency rises from Zipf 2.88 to 4.57, while age of acquisition drops from 15.44 to 10.43. Readers can now grasp the concept without needing to know the technical label that merges psychology and sociology.
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

**output:** The patient has mild hardening of the descending aorta that does not move.

| metric | value |
|---|---:|
| bertscore_f1 | 0.380 |
| coleman_liau | 9.14 |
| coleman_liau_drop | 20.18 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.250 |
| fkgl | 7.63 |
| fkgl_drop | 16.49 |
| fre | 63.5 |
| fre_gain | 132.4 |
| human_edit_recall | 1.000 |
| length_ratio | 0.59 |
| n_words | 13.0 |
| nli_completeness | 0.559 |
| nli_faithfulness | 0.952 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 43.67 |
| severity_downgrade | 0.000 |
| severity_preservation | 1.000 |
| severity_tier_input | 1.000 |
| severity_tier_output | 1.000 |
| smog | 13.02 |
| smog_drop | 1.53 |

### Stage 4 - arm `termonly`

**output:** Mild, fixed buildup in the lower part of the main artery.

| metric | value |
|---|---:|
| bertscore_f1 | 0.384 |
| coleman_liau | 5.24 |
| coleman_liau_drop | 24.08 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 4.79 |
| fkgl_drop | 19.33 |
| fre | 80.3 |
| fre_gain | 149.3 |
| human_edit_recall | 1.000 |
| length_ratio | 0.50 |
| n_words | 11.0 |
| nli_completeness | 0.672 |
| nli_faithfulness | 0.954 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 45.44 |
| severity_downgrade | 0.000 |
| severity_preservation | 1.000 |
| severity_tier_input | 1.000 |
| severity_tier_output | 1.000 |
| smog | 8.84 |
| smog_drop | 5.71 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `nonmobile` -> `fixed` | replace | - | - | - | - | - | - | - |
| `descending aortic` -> `lower part of the main artery` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Mild hardening of the main chest artery that does not move.

| metric | value |
|---|---:|
| bertscore_f1 | 0.517 |
| coleman_liau | 6.82 |
| coleman_liau_drop | 22.50 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 4.79 |
| fkgl_drop | 19.33 |
| fre | 80.3 |
| fre_gain | 149.3 |
| human_edit_recall | 1.000 |
| length_ratio | 0.50 |
| n_words | 11.0 |
| nli_completeness | 0.478 |
| nli_faithfulness | 0.942 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 47.20 |
| severity_downgrade | 0.000 |
| severity_preservation | 1.000 |
| severity_tier_input | 1.000 |
| severity_tier_output | 1.000 |
| smog | 11.21 |
| smog_drop | 3.35 |

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

**output:** The ear tube was blocked with a wax-like paste.

| metric | value |
|---|---:|
| bertscore_f1 | 0.578 |
| coleman_liau | 4.76 |
| coleman_liau_drop | 5.47 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.250 |
| fkgl | 1.03 |
| fkgl_drop | 5.67 |
| fre | 103.7 |
| fre_gain | 42.5 |
| human_edit_recall | 1.000 |
| length_ratio | 0.77 |
| n_words | 10.0 |
| nli_completeness | 0.118 |
| nli_faithfulness | 0.896 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 37.35 |
| smog | 3.13 |
| smog_drop | 8.08 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `eustachian tube` -> `ear tube` | replace | - | - | - | - | - | - | - |
| `obstructed` -> `blocked` | replace | - | - | - | - | - | - | - |
| `bone wax` -> `wax-like paste` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** The tube that connects the middle ear to the back of the throat was blocked with a sticky paste used during surgery.

| metric | value |
|---|---:|
| bertscore_f1 | 0.529 |
| coleman_liau | 7.64 |
| coleman_liau_drop | 2.59 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.400 |
| fkgl | 8.01 |
| fkgl_drop | -1.30 |
| fre | 76.8 |
| fre_gain | 15.6 |
| human_edit_recall | 1.000 |
| length_ratio | 1.69 |
| n_words | 22.0 |
| nli_completeness | 0.066 |
| nli_faithfulness | 0.173 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 33.38 |
| smog | 8.84 |
| smog_drop | 2.37 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `eustachian tube` -> `tube that connects the middle ear to the back of the throat` | replace | attributed | 2.430 | 2.666 | 0.776 | 0.870 | 3.079 | - |
| `obstructed` -> `blocked` | replace | attributed | 0.001 | 0.655 | 0.286 | 0.614 | 0.010 | - |
| `bone wax` -> `a sticky paste used during surgery` | replace | attributed | 3.818 | 3.846 | 0.700 | 0.866 | 0.002 | - |

**edit `eustachian tube` -> `tube that connects the middle ear to the back of the throat`**

- status: `attributed`
- log p full -1.4865, empty -3.9166
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+3.103` [justplainclear] eustachian tube: The tube that connects your middle ear to the back of your throat and pharynx area. The openi
    - `+0.025` [wiktionary] wax: If you wax something, you put wax on it, for example, a car.

- rationale: The justplainclear glossary defines the eustachian tube as the passage linking the middle ear to the back of the throat and pharynx, so the replacement spells out that connection in everyday words. Phrase frequency rises from Zipf 1.90 to 3.54, while age of acquisition shifts only slightly from 5.50 to 5.53. Readers can now picture the anatomy and its location without needing to recognize the technical name.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `obstructed` -> `blocked`**

- status: `attributed`
- log p full -0.0015, empty -0.0030
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+0.159` [wiktionary] bone: When two man bone, they have sex.
    - `+0.148` [wiktionary] obstructed: If something obstructs your way, it blocks your path from point A to point B.
    - `+0.127` [justplainclear] eustachian tube: The tube that connects your middle ear to the back of your throat and pharynx area. The openi
    - `-0.010` [readme] wax: Yellow sticky stuff in your ear that keeps it clean and dry.
    - `-0.068` [wiktionary] wax: If you wax something, you put wax on it, for example, a car.

- rationale: "Obstructed" means something is clogged or stopped up, and "blocked" conveys that same idea in a shorter, more familiar word. Phrase frequency rises from Zipf 2.98 to 4.31, and the syllable count drops from three to one. Readers can grasp the concept of a barrier or stoppage immediately without pausing over a longer, less common term.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `bone wax` -> `a sticky paste used during surgery`**

- status: `attributed`
- log p full -3.5994, empty -7.4178
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+1.666` [wiktionary] wax: If you wax something, you put wax on it, for example, a car.
    - `+1.665` [readme] wax: Yellow sticky stuff in your ear that keeps it clean and dry.
    - `+0.424` [wiktionary] bone: When two man bone, they have sex.

- rationale: Bone wax is a sterile, putty-like material surgeons press into bleeding bone edges to stop oozing, and the phrase "a sticky paste used during surgery" conveys that same function in everyday words. Phrase frequency shifts from Zipf 3.81 to 3.51, while age of acquisition rises from 6.00 to 7.68. Readers can now picture what the material is and why it is applied without needing the specialized product name.
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

**output:** He was laid on his back on the operating room table.

| metric | value |
|---|---:|
| bertscore_f1 | 0.682 |
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
| nli_completeness | 0.941 |
| nli_faithfulness | 0.972 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 55.14 |
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
| `supine` -> `lying on his back` | replace | attributed | 0.194 | 0.670 | - | 0.509 | 0.219 | - |

**edit `supine` -> `lying on his back`**

- status: `attributed`
- log p full -0.2539, empty -0.4478
- masks scored: 18/18 (+2 top-k)
- ranked sources:
    - `+0.362` [iowa] SUPINE: lying on the back
    - `+0.143` [readme] Supine: Lying down on your back.
    - `-0.553` [michigan] supine: To lie on your back.

- rationale: "Supine" means lying flat with the face upward, and "lying on his back" conveys that same body position in everyday words. Phrase frequency rises from Zipf 2.42 to 4.64, while age of acquisition drops from 16.43 to 5.31. Readers can picture the posture immediately without needing a technical term.
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

**output:** A pee test was not done this time.

| metric | value |
|---|---:|
| bertscore_f1 | 0.931 |
| coleman_liau | -0.65 |
| coleman_liau_drop | 8.79 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | -0.67 |
| fkgl_drop | 8.04 |
| fre | 114.1 |
| fre_gain | 59.4 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 8.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.984 |
| nli_faithfulness | 0.990 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 36.23 |
| smog | 3.13 |
| smog_drop | 5.71 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `urinalysis` -> `pee test` | replace | attributed | 6.918 | 8.134 | - | 0.869 | 0.887 | - |

**edit `urinalysis` -> `pee test`**

- status: `attributed`
- log p full -0.3511, empty -7.2690
- masks scored: 34/34 (+2 top-k)
- ranked sources:
    - `+3.228` [readme] Urinalysis: A test that checks what's in your pee.
    - `+2.342` [readme] urinalysis: A test that checks the contents of your pee to see what's in there.
    - `+1.169` [justplainclear] urinalysis: Also known as: urine test, pee test A test of your urine used to find certain medical conditions
    - `-0.351` [michigan] urinalysis: A test of your urine to check for diseases, such as diabetes, urinary tract infections, or kidney 
    - `-0.404` [nih] urinalysis: A test that determines the content of the urine.

- rationale: A urinalysis is a laboratory examination of urine to check for signs of disease or infection, and "pee test" conveys that same procedure in everyday language. Phrase frequency rises from Zipf 2.20 to 3.94, while age of acquisition drops from 14.68 to 6.26. Readers can immediately grasp that a simple bodily sample is being checked without needing to decode a technical term.
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

**output:** Her vision and hearing were good enough for the testing, but she said she needed a new eyeglass prescription.

| metric | value |
|---|---:|
| bertscore_f1 | 0.591 |
| coleman_liau | 9.81 |
| coleman_liau_drop | 3.91 |
| copy_jargon_rate | 0.667 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.250 |
| fkgl | 8.59 |
| fkgl_drop | 3.68 |
| fre | 67.3 |
| fre_gain | 22.8 |
| human_edit_recall | 0.333 |
| length_ratio | 0.90 |
| n_words | 19.0 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.995 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 16.66 |
| smog | 8.84 |
| smog_drop | 4.18 |

### Stage 4 - arm `termonly`

**output:** Vision and hearing seemed good enough for testing, although she said she needed a new glasses prescription.

| metric | value |
|---|---:|
| bertscore_f1 | 0.791 |
| coleman_liau | 12.82 |
| coleman_liau_drop | 0.90 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.167 |
| fkgl | 9.09 |
| fkgl_drop | 3.18 |
| fre | 60.2 |
| fre_gain | 15.7 |
| human_edit_recall | 1.000 |
| length_ratio | 0.81 |
| n_words | 17.0 |
| nli_completeness | 0.991 |
| nli_faithfulness | 0.995 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 27.00 |
| smog | 8.84 |
| smog_drop | 4.18 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `adequate` -> `good enough` | replace | - | - | - | - | - | - | - |
| `did indicate` -> `said` | replace | - | - | - | - | - | - | - |
| `eyeglass prescription` -> `new glasses prescription` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Vision and hearing seemed good enough for testing, although she said she needed a new glasses order.

| metric | value |
|---|---:|
| bertscore_f1 | 0.744 |
| coleman_liau | 10.44 |
| coleman_liau_drop | 3.29 |
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
| nli_completeness | 0.986 |
| nli_faithfulness | 0.989 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.286 |
| sari | 25.11 |
| smog | 3.13 |
| smog_drop | 9.89 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `adequate` -> `good enough` | replace | attributed | 0.024 | 0.959 | 0.848 | 0.929 | 1.946 | - |
| `did indicate` -> `said` | replace | attributed | -0.032 | -1.682 | 0.208 | 0.828 | 0.055 | - |
| `eyeglass prescription` -> `new glasses order` | replace | attributed | 2.715 | 3.216 | 0.503 | 0.606 | 0.194 | - |

**edit `adequate` -> `good enough`**

- status: `attributed`
- log p full -0.0154, empty -0.0398
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+2.351` [wiktionary] adequate: If something is adequate, it is good enough.
    - `+0.405` [nih] prescription: A doctor's order for medicine or another intervention.
    - `+0.354` [justplainclear] eyeglass: A single lens used to help you see more clearly.
    - `+0.289` [wiktionary] did: Do is an auxiliary verb. It is used in questions, negative statements, short answers, and for emphasis wh
    - `+0.234` [thesaurus] indicate: suggest, point to

- rationale: "Adequate" means meeting the required standard, and "good enough" conveys that same idea in everyday language. Word frequency rises from Zipf 4.05 to 5.44, and age of acquisition drops from 10.35 to 6.96. Readers can grasp the point without pausing on a more formal word.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `did indicate` -> `said`**

- status: `attributed`
- log p full -0.0390, empty -0.0074
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+0.697` [wiktionary] did: Do is an auxiliary verb. It is used in questions, negative statements, short answers, and for emphasis wh
    - `+0.642` [thesaurus] adequate: enough, the right amount
    - `+0.429` [michigan] prescription: An order from your doctor, nurse, or physician assistant for drugs or other treatment.
    - `+0.354` [readme] Prescription: A prescription is a doctor's recommendation for medication or treatment.
    - `+0.127` [wiktionary] indicate: If someone indicates something, they show signs of something; they show it.

- rationale: "Did indicate" is a formal, multi-word way of saying that someone communicated or confirmed something, and the single word "said" conveys that same act of speaking in the most direct language possible. Phrase frequency rises from Zipf 4.34 to 6.01, and the syllable count drops from four to one. Readers can now grasp who communicated the information without wading through extra grammatical scaffolding.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `eyeglass prescription` -> `new glasses order`**

- status: `attributed`
- log p full -0.8908, empty -3.6061
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+0.918` [thesaurus] prescription: doctors orders, medicine, drug order
    - `+0.724` [readme] Prescription: A prescription is a doctor's recommendation for medication or treatment.
    - `+0.648` [michigan] prescription: An order from your doctor, nurse, or physician assistant for drugs or other treatment.
    - `+0.270` [wiktionary] prescription: A written order, as by a physician, to tell which medicine to take and how many doses of it is n
    - `+0.187` [nih] prescription: A doctor's order for medicine or another intervention.

- rationale: The thesaurus treats an eyeglass prescription as a doctor's order for corrective lenses, so "new glasses order" keeps that same idea in everyday words. Phrase frequency rises from Zipf 2.32 to 4.31, and age of acquisition drops from 9.22 to 6.26. Readers can now see the instruction as a simple request for glasses rather than a technical document.
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

**output:** The doctor has talked to him several times about a colonoscopy, which he has refused, so they have been doing stool tests for occult blood.

| metric | value |
|---|---:|
| bertscore_f1 | 0.612 |
| coleman_liau | 9.00 |
| coleman_liau_drop | -1.38 |
| copy_jargon_rate | 0.667 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 8.79 |
| fkgl_drop | -0.76 |
| fre | 76.6 |
| fre_gain | -3.7 |
| human_edit_recall | 0.333 |
| length_ratio | 0.54 |
| n_words | 25.0 |
| nli_completeness | 0.989 |
| nli_faithfulness | 0.705 |
| replacement_f1 | 0.500 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 34.20 |
| smog | 3.13 |
| smog_drop | 0.00 |

### Stage 4 - arm `termonly`

**output:** I have talked to him several times about a test where a doctor looks inside the large bowel with a camera, which he has refused, and so we have been checking his poop for hidden blood.

| metric | value |
|---|---:|
| bertscore_f1 | 0.603 |
| coleman_liau | 6.90 |
| coleman_liau_drop | 0.72 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.750 |
| fkgl | 13.53 |
| fkgl_drop | -5.50 |
| fre | 62.2 |
| fre_gain | -18.1 |
| human_edit_recall | 1.000 |
| length_ratio | 0.78 |
| n_words | 36.0 |
| nli_completeness | 0.947 |
| nli_faithfulness | 0.878 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 61.81 |
| smog | 8.84 |
| smog_drop | -5.71 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `colonoscopy` -> `a test where a doctor looks inside the large bowel with a camera` | replace | - | - | - | - | - | - | - |
| `stools` -> `poop` | replace | - | - | - | - | - | - | - |
| `occult blood` -> `hidden blood` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** I have talked to him several times about a test to check the large intestine for cancer, which he has refused, and so we have been testing his poop for hidden blood.

| metric | value |
|---|---:|
| bertscore_f1 | 0.616 |
| coleman_liau | 7.02 |
| coleman_liau_drop | 0.60 |
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
| nli_completeness | 0.878 |
| nli_faithfulness | 0.919 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 62.74 |
| smog | 8.84 |
| smog_drop | -5.71 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `colonoscopy` -> `test to check the large intestine for cancer` | replace | attributed | 11.938 | 11.984 | 0.727 | 0.919 | 0.009 | - |
| `stools` -> `poop` | replace | attributed | 1.211 | 4.438 | 0.723 | 0.973 | 4.223 | - |
| `occult blood` -> `hidden blood` | replace | attributed | 0.001 | 0.799 | 0.664 | 0.910 | 0.345 | - |

**edit `colonoscopy` -> `test to check the large intestine for cancer`**

- status: `attributed`
- log p full -3.0999, empty -15.0374
- masks scored: 66/66 (+5 top-k)
- ranked sources:
    - `+7.935` [readme] colonoscopy: A colonoscopy is a test that checks the inside of your large intestine for signs of cancer.
    - `+7.925` [readme] colonoscopy: A procedure to check for colon cancer by examining the inside of the large intestine.
    - `+2.038` [readme] occult: Obscure and mysterious, not easily understood.
    - `+1.700` [readme] Occult: Secret knowledge or practices that are mysterious or not easily understood.
    - `+1.517` [wiktionary] stools: A stool is a seat for one person that does not have a back or an armrest.

- rationale: A colonoscopy is a procedure that examines the large intestine for signs of cancer, and the replacement spells out that purpose in everyday words. Phrase frequency rises from Zipf 2.74 to 3.21, while age of acquisition drops from 15.76 to 9.28. Readers can now grasp what the test looks for without needing to know the technical name.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `stools` -> `poop`**

- status: `attributed`
- log p full -0.0286, empty -1.2397
- masks scored: 66/66 (+5 top-k)
- ranked sources:
    - `+4.790` [readme] stools: Poop.
    - `+0.566` [michigan] colonoscopy: Looks at the inside of the large intestine using a flexible tube with a ltiny camera at the end.
    - `+0.400` [michigan] blood: A fluid in your body that carries things that are needed for your body to work well, such as vitamins, 
    - `+0.234` [readme] Occult: Secret knowledge or practices that are mysterious or not easily understood.
    - `+0.145` [readme] colonoscopy: A procedure to check for colon cancer by examining the inside of the large intestine.

- rationale: The readme glossary simply lists "Poop" as the plain-language equivalent, so the replacement keeps the same meaning in everyday words. Phrase frequency rises from Zipf 3.05 to 3.66, while syllables stay at one. Readers can now recognize the term instantly without pausing to translate a clinical word.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `occult blood` -> `hidden blood`**

- status: `attributed`
- log p full -0.0011, empty -0.0024
- masks scored: 66/66 (+5 top-k)
- ranked sources:
    - `+1.202` [readme] colonoscopy: A colonoscopy is a test that checks the inside of your large intestine for signs of cancer.
    - `+0.858` [readme] colonoscopy: A procedure to check for colon cancer by examining the inside of the large intestine.
    - `+0.586` [wiktionary] occult: If something is occult it is hidden or secret—or it is about hidden or secret things.
    - `+0.333` [wiktionary] stools: A stool is a seat for one person that does not have a back or an armrest.
    - `+0.216` [readme] blood: Blood is a fluid that carries nutrients and oxygen to different parts of the body.

- rationale: "Occult blood" means blood that cannot be seen with the naked eye, and "hidden blood" conveys that same idea in everyday language. Phrase frequency rises from Zipf 3.28 to 4.43, while age of acquisition drops from 12.65 to 4.89. Readers can now grasp the finding immediately without needing to know a technical term.
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

**output:** The knee was washed out with a large amount of fluid and then dried with suction again.

| metric | value |
|---|---:|
| bertscore_f1 | 0.616 |
| coleman_liau | 6.34 |
| coleman_liau_drop | 5.06 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 5.62 |
| fkgl_drop | 2.75 |
| fre | 85.1 |
| fre_gain | 32.2 |
| human_edit_recall | 1.000 |
| length_ratio | 1.06 |
| n_words | 17.0 |
| nli_completeness | 0.967 |
| nli_faithfulness | 0.984 |
| number_unit_preservation | 0.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 61.10 |
| smog | 3.13 |
| smog_drop | 8.08 |

### Stage 4 - arm `termonly`

**output:** The knee was washed out with a lot of fluid and then dried with suction.

| metric | value |
|---|---:|
| bertscore_f1 | 0.578 |
| coleman_liau | 4.27 |
| coleman_liau_drop | 7.13 |
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
| nli_completeness | 0.954 |
| nli_faithfulness | 0.985 |
| number_unit_preservation | 0.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 59.73 |
| smog | 3.13 |
| smog_drop | 8.08 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `copiously irrigated` -> `washed out with a lot of fluid` | replace | - | - | - | - | - | - | - |
| `suction dried` -> `dried with suction` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** The knee was washed with a lot of fluid and then dried with suction again.

| metric | value |
|---|---:|
| bertscore_f1 | 0.617 |
| coleman_liau | 5.04 |
| coleman_liau_drop | 6.36 |
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
| nli_completeness | 0.969 |
| nli_faithfulness | 0.990 |
| number_unit_preservation | 0.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 58.89 |
| smog | 3.13 |
| smog_drop | 8.08 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `copiously irrigated` -> `washed with a lot of fluid` | replace | attributed | 1.561 | 2.040 | 0.769 | 0.809 | 0.174 | - |
| `suction dried` -> `dried with suction` | replace | attributed | -0.523 | -1.056 | 0.804 | 0.790 | 0.214 | - |

**edit `copiously irrigated` -> `washed with a lot of fluid`**

- status: `attributed`
- log p full -0.8268, empty -2.3876
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.435` [wiktionary] irrigated: To supply farms with water to grow crops.
    - `+0.261` [wiktionary] dried: If something is dry, it has no water or liquid on it.
    - `+0.124` [readme] suction: Suction is when a machine pulls in gas, liquid, or mucus.
    - `+0.093` [wiktionary] suction: A suction is a device that removes saliva from a patient's mouth during dental operations.

- rationale: The glossary defines "irrigated" as supplying water to land for crops, so "washed with a lot of fluid" keeps that sense of abundant liquid applied to a surface but shifts the setting from fields to a wound or cavity. Phrase frequency rises from Zipf 1.98 to 3.85, marking a clear jump in everyday familiarity. Readers can now picture the thorough rinsing without needing the technical verb.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `suction dried` -> `dried with suction`**

- status: `attributed`
- log p full -0.9798, empty -0.4567
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.300` [wiktionary] suction: A suction is a device that removes saliva from a patient's mouth during dental operations.
    - `+0.085` [dictionary] Copiously (adv.): In a copious manner.
    - `-0.008` [readme] suction: Suction is when a machine pulls in gas, liquid, or mucus.
    - `-0.031` [wiktionary] irrigated: To supply farms with water to grow crops.
    - `-0.356` [wiktionary] dried: If something is dry, it has no water or liquid on it.

- rationale: "Suction dried" describes something that has had moisture removed by pulling air through it, and "dried with suction" simply reorders those same words to make the action and the tool clearer. Phrase frequency stays at Zipf 3.28, and age of acquisition remains 9.42. The reader can now see the drying method spelled out in a familiar subject‑verb order without learning any new vocabulary.
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

**output:** She does not have painful urination, blood in the urine, frequent urination, or trouble starting to urinate.

| metric | value |
|---|---:|
| bertscore_f1 | 0.657 |
| coleman_liau | 12.48 |
| coleman_liau_drop | -2.23 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 10.48 |
| fkgl_drop | 0.47 |
| fre | 50.2 |
| fre_gain | 8.7 |
| human_edit_recall | 1.000 |
| length_ratio | 0.85 |
| n_words | 17.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.993 |
| nli_faithfulness | 0.993 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 30.61 |
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

**output:** She is not having painful urination, any blood in the urine, needing to go often, or trouble starting to pee.

| metric | value |
|---|---:|
| bertscore_f1 | 0.797 |
| coleman_liau | 7.66 |
| coleman_liau_drop | 2.60 |
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
| nli_completeness | 0.987 |
| nli_faithfulness | 0.987 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 65.41 |
| smog | 8.84 |
| smog_drop | 4.18 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `frequency` -> `needing to go often` | replace | attributed | -0.147 | -0.243 | - | 0.790 | 0.012 | - |
| `hesitancy` -> `trouble starting to pee` | replace | attributed | 2.716 | 4.044 | - | 0.786 | 1.144 | - |

**edit `frequency` -> `needing to go often`**

- status: `attributed`
- log p full -1.0032, empty -0.8563
- masks scored: 34/34 (+4 top-k)
- ranked sources:
    - `+0.305` [readme] FREQUENCY: Frequency is how often something happens.
    - `+0.293` [wiktionary] frequency: Something's frequency is how often it happens.
    - `+0.212` [readme] frequency: How often something happens.
    - `-0.201` [readme] hesitancy: Having difficulty starting to pee or keeping the flow steady.
    - `-0.401` [readme] hesitancy: Having difficulty starting or maintaining a steady flow while peeing.

- rationale: "Frequency" in a medical context means how often something happens, such as needing to urinate, and "needing to go often" spells out that specific meaning in everyday words. Word frequency shifts from Zipf 4.36 to 4.00, while age of acquisition drops from 9.79 to 6.53. Readers can immediately grasp the symptom without translating a technical noun into a concrete action.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `hesitancy` -> `trouble starting to pee`**

- status: `attributed`
- log p full -0.2900, empty -3.0058
- masks scored: 34/34 (+4 top-k)
- ranked sources:
    - `+2.592` [readme] hesitancy: Having difficulty starting to pee or keeping the flow steady.
    - `+1.448` [readme] hesitancy: Having difficulty starting or maintaining a steady flow while peeing.
    - `-0.023` [readme] frequency: How often something happens.

- rationale: Hesitancy in a medical context means difficulty beginning to urinate, and "trouble starting to pee" states that problem in everyday words. Phrase frequency rises from Zipf 2.35 to 3.87, while age of acquisition drops from 12.12 to 4.56. Readers can now grasp the symptom immediately without knowing the clinical label.
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

**output:** The patient has chest pain behind the breastbone, occasional angina pain, and describes it as a feeling of tightness.

| metric | value |
|---|---:|
| bertscore_f1 | 0.476 |
| coleman_liau | 11.95 |
| coleman_liau_drop | 3.97 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 10.45 |
| fkgl_drop | 4.35 |
| fre | 54.0 |
| fre_gain | 31.2 |
| human_edit_recall | 1.000 |
| length_ratio | 0.63 |
| n_words | 19.0 |
| nli_completeness | 0.782 |
| nli_faithfulness | 0.984 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 50.19 |
| smog | 11.21 |
| smog_drop | 4.70 |

### Stage 4 - arm `termonly`

**output:** Heart and blood vessels: Chest pain behind the breastbone, occasional heart-related pain and the patient describes it as a feeling of tightness.

| metric | value |
|---|---:|
| bertscore_f1 | 0.679 |
| coleman_liau | 14.23 |
| coleman_liau_drop | 1.69 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.333 |
| fkgl | 11.23 |
| fkgl_drop | 3.57 |
| fre | 53.8 |
| fre_gain | 31.0 |
| human_edit_recall | 1.000 |
| length_ratio | 0.77 |
| n_words | 23.0 |
| nli_completeness | 0.964 |
| nli_faithfulness | 0.896 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 65.41 |
| smog | 11.21 |
| smog_drop | 4.70 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `retrosternal area` -> `breastbone` | replace | - | - | - | - | - | - | - |
| `anginal pain` -> `heart-related pain` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Heart and blood vessels: Chest pain behind the breastbone, occasional heart-related pain and the patient describes it as a feeling of tightness.

| metric | value |
|---|---:|
| bertscore_f1 | 0.679 |
| coleman_liau | 14.23 |
| coleman_liau_drop | 1.69 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.333 |
| fkgl | 11.23 |
| fkgl_drop | 3.57 |
| fre | 53.8 |
| fre_gain | 31.0 |
| human_edit_recall | 1.000 |
| length_ratio | 0.77 |
| n_words | 23.0 |
| nli_completeness | 0.964 |
| nli_faithfulness | 0.896 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 65.41 |
| smog | 11.21 |
| smog_drop | 4.70 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `retrosternal area` -> `breastbone` | replace | attributed | -0.001 | -0.260 | 0.162 | 0.676 | 0.061 | - |
| `anginal pain` -> `heart-related pain` | replace | attributed | -0.077 | -0.097 | -0.175 | 0.430 | 0.018 | - |

**edit `retrosternal area` -> `breastbone`**

- status: `attributed`
- log p full -0.0034, empty -0.0026
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.090` [michigan] cardiovascular: Having to do with your heart and blood vessels.
    - `+0.029` [wiktionary] pain: to sadden or hurt
    - `+0.008` [justplainclear] cardiovascular: About the heart and blood vessels

- rationale: "Retrosternal area" refers to the space behind the breastbone, so using "breastbone" itself names the familiar landmark patients can feel. Phrase frequency rises from Zipf 0.00 to 1.93, while age of acquisition increases from 6.58 to 10.75. Readers can now picture the exact spot without decoding a Latin-based anatomical term.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `anginal pain` -> `heart-related pain`**

- status: `attributed`
- log p full -1.6099, empty -1.5328
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.104` [michigan] pain: An unplesant feeling, a sign from your nerves that something may be wrong. It ca be sharp or dull, sting
    - `+0.087` [justplainclear] cardiovascular: About the heart and blood vessels

- rationale: Anginal pain refers to chest discomfort caused by reduced blood flow to the heart, and "heart-related pain" conveys that same idea in everyday language. Phrase frequency rises from Zipf 1.10 to 4.65, while age of acquisition remains at 4.26. Readers can now recognize the symptom as a heart issue without needing to know the clinical term.
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

**output:** We took out a good bit of his joint lining and joint sac.

| metric | value |
|---|---:|
| bertscore_f1 | 0.519 |
| coleman_liau | 1.55 |
| coleman_liau_drop | 4.21 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 2.19 |
| fkgl_drop | 2.60 |
| fre | 102.5 |
| fre_gain | 22.2 |
| human_edit_recall | 1.000 |
| length_ratio | 1.08 |
| n_words | 13.0 |
| nli_completeness | 0.801 |
| nli_faithfulness | 0.937 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 46.74 |
| smog | 3.13 |
| smog_drop | 5.71 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `synovium` -> `joint lining` | replace | - | - | - | - | - | - | - |
| `synovial pouch` -> `joint sac` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** We took out a good bit of the soft tissue that lines his joint and the pocket-like part of that tissue.

| metric | value |
|---|---:|
| bertscore_f1 | 0.574 |
| coleman_liau | 5.16 |
| coleman_liau_drop | 0.60 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.400 |
| fkgl | 6.65 |
| fkgl_drop | -1.86 |
| fre | 84.8 |
| fre_gain | 4.5 |
| human_edit_recall | 1.000 |
| length_ratio | 1.83 |
| n_words | 22.0 |
| nli_completeness | 0.497 |
| nli_faithfulness | 0.743 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 53.95 |
| smog | 8.84 |
| smog_drop | 0.00 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `excised` -> `took out` | replace | attributed | 0.026 | 0.049 | 0.376 | 0.564 | 0.058 | - |
| `synovium` -> `the soft tissue that lines his joint` | replace | attributed | 6.372 | 6.439 | 0.837 | 0.938 | 0.184 | - |
| `synovial pouch` -> `the pocket-like part of that tissue` | replace | attributed | 9.903 | 10.032 | 0.820 | 0.914 | 7.322 | - |

**edit `excised` -> `took out`**

- status: `attributed`
- log p full -0.7447, empty -0.7708
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+0.112` [readme] SYNOVIUM: The slimy layer that covers your joints.
    - `+0.054` [wiktionary] pouch: A pouch is a small bag or pocket used for carrying things.
    - `+0.030` [wiktionary] excised: Excise it the tax that is charged on goods produced within the country.
    - `-0.027` [wiktionary] pouch: A pouch is a pocket-like part of an animal's body, used to carry young or store food.
    - `-0.058` [readme] Synovial: Relating to the soft tissue that lines joints.

- rationale: "Excised" means surgically removed or cut out, and "took out" conveys that same action in everyday language. Phrase frequency rises from Zipf 2.58 to 5.45. Readers can now grasp the procedure immediately without pausing to decode a formal medical verb.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `synovium` -> `the soft tissue that lines his joint`**

- status: `attributed`
- log p full -2.7330, empty -9.1050
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+4.001` [readme] SYNOVIAL: Synovial means having to do with the soft tissue that lines joints.
    - `+3.817` [readme] Synovial: Relating to the soft tissue that lines joints.
    - `-0.143` [wiktionary] excised: Excise it the tax that is charged on goods produced within the country.
    - `-0.979` [wiktionary] pouch: A pouch is a pocket-like part of an animal's body, used to carry young or store food.

- rationale: Synovium is the thin membrane that lines the inside of a joint and produces the fluid that keeps it moving smoothly, so "the soft tissue that lines his joint" preserves that definition in everyday words. Phrase frequency rises from Zipf 1.46 to 4.00. The reader can now picture the joint lining without needing a specialized anatomy term.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `synovial pouch` -> `the pocket-like part of that tissue`**

- status: `attributed`
- log p full -2.1079, empty -12.0107
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+8.873` [wiktionary] pouch: A pouch is a pocket-like part of an animal's body, used to carry young or store food.
    - `+1.551` [readme] SYNOVIAL: Synovial means having to do with the soft tissue that lines joints.
    - `+1.430` [wiktionary] pouch: A pouch is a small bag or pocket used for carrying things.
    - `+0.649` [readme] Synovial: Relating to the soft tissue that lines joints.
    - `+0.245` [wiktionary] excised: Excise it the tax that is charged on goods produced within the country.

- rationale: Wiktionary defines a pouch as a pocket-like part of an animal's body, so the replacement spells out that same image in everyday words. Phrase frequency rises from Zipf 2.32 to 4.08, and age of acquisition drops from 16.00 to 5.53. Readers can now picture the structure instantly without needing a specialized anatomy term.
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

**output:** An inflammatory process, such as an infection or a lack of blood flow, must be considered.

| metric | value |
|---|---:|
| bertscore_f1 | 0.852 |
| coleman_liau | 8.45 |
| coleman_liau_drop | 5.75 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| diagnostic_identity_preservation | 1.000 |
| fkgl | 9.09 |
| fkgl_drop | 4.29 |
| fre | 58.4 |
| fre_gain | 39.6 |
| human_edit_recall | 1.000 |
| length_ratio | 1.23 |
| n_words | 16.0 |
| nli_completeness | 0.861 |
| nli_faithfulness | 0.989 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 63.91 |
| smog | 13.02 |
| smog_drop | 1.53 |

### Stage 4 - arm `termonly`

**output:** Swelling such as infection or poor blood flow must be considered.

| metric | value |
|---|---:|
| bertscore_f1 | 0.729 |
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
| nli_completeness | 0.963 |
| nli_faithfulness | 0.973 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 50.57 |
| smog | 11.21 |
| smog_drop | 3.35 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `inflammatory process` -> `such as infection or poor blood flow` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** A problem like an infection or not enough blood flow must be considered.

| metric | value |
|---|---:|
| bertscore_f1 | 0.728 |
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
| length_ratio | 1.00 |
| n_words | 13.0 |
| nli_completeness | 0.805 |
| nli_faithfulness | 0.910 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.250 |
| sari | 34.72 |
| smog | 11.21 |
| smog_drop | 3.35 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `inflammatory process` -> `problem` | replace | attributed | 0.590 | 1.619 | 0.809 | 0.816 | 1.600 | - |
| `ischemia` -> `not enough blood flow` | replace | attributed | 1.817 | 2.733 | 0.862 | 0.870 | 0.374 | - |

**edit `inflammatory process` -> `problem`**

- status: `attributed`
- log p full -0.2212, empty -0.8110
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+1.651` [readme] inflammatory process: When your body gets inflamed, it's like it's telling you there's something wrong by show
    - `+0.050` [readme] ischemia: Not enough blood flow due to blocked or narrowed blood vessels.
    - `-0.114` [nih] ischemia: Lack of blood supply to a part of the body. Ischemia may cause tissue damage due to the lack of oxyg

- rationale: An inflammatory process is the body's response to injury or infection, and "problem" conveys that something is wrong in a single, familiar word. Phrase frequency rises from Zipf 3.71 to 5.40, and age of acquisition drops from 13.33 to 6.06. Readers can immediately grasp that a medical issue exists without needing to interpret a technical description of the immune response.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `ischemia` -> `not enough blood flow`**

- status: `attributed`
- log p full -0.4433, empty -2.2599
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+1.315` [readme] ischemia: Not enough blood flow due to blocked or narrowed blood vessels.
    - `+0.941` [michigan] ischemia: When blood supply to an organ or a body part isn't enough, especially the heart.
    - `-0.389` [readme] inflammatory process: When your body gets inflamed, it's like it's telling you there's something wrong by show

- rationale: The readme defines ischemia as not enough blood flow caused by blocked or narrowed vessels, so the replacement keeps that core idea in everyday words. Phrase frequency rises from Zipf 2.85 to 4.50, and age of acquisition drops from 18.00 to 7.40. Readers can now grasp the problem immediately without needing a medical dictionary.
- audit: coverage 0.833, grounding_error=True, omission=False, source_ok=False, passage_ok=True

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

**output:** I asked her to increase her prednisone when she goes home.

| metric | value |
|---|---:|
| bertscore_f1 | 0.781 |
| coleman_liau | 6.29 |
| coleman_liau_drop | 0.09 |
| copy_jargon_rate | 1.000 |
| critical_error | 0.000 |
| drug_preservation | 1.000 |
| fkgl | 2.65 |
| fkgl_drop | 0.21 |
| fre | 95.7 |
| fre_gain | -0.3 |
| human_edit_recall | 0.000 |
| length_ratio | 0.92 |
| n_words | 11.0 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.993 |
| replacement_f1 | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 23.78 |
| smog | 3.13 |
| smog_drop | 0.00 |

### Stage 4 - arm `termonly`

**output:** I have asked her to take more of a steroid medicine when she goes home.

| metric | value |
|---|---:|
| bertscore_f1 | 0.814 |
| coleman_liau | 3.88 |
| coleman_liau_drop | 2.50 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| drug_preservation | 0.000 |
| fkgl | 4.42 |
| fkgl_drop | -1.56 |
| fre | 90.1 |
| fre_gain | -5.9 |
| human_edit_recall | 1.000 |
| length_ratio | 1.25 |
| n_words | 15.0 |
| nli_completeness | 0.033 |
| nli_faithfulness | 0.817 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 49.65 |
| smog | 8.84 |
| smog_drop | -5.71 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `prednisone` -> `steroid medicine` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** I have asked her to take more of a medicine that lowers the body's immune response and inflammation when she goes home.

| metric | value |
|---|---:|
| bertscore_f1 | 0.622 |
| coleman_liau | 8.16 |
| coleman_liau_drop | -1.78 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| drug_preservation | 0.000 |
| fkgl | 9.62 |
| fkgl_drop | -6.76 |
| fre | 65.3 |
| fre_gain | -30.7 |
| human_edit_recall | 1.000 |
| length_ratio | 1.92 |
| n_words | 23.0 |
| nli_completeness | 0.001 |
| nli_faithfulness | 0.443 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 47.27 |
| smog | 11.21 |
| smog_drop | -8.08 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `prednisone` -> `a medicine that lowers the body's immune response and inflammation` | replace | attributed | 18.629 | 18.770 | - | 0.786 | 11.416 | - |

**edit `prednisone` -> `a medicine that lowers the body's immune response and inflammation`**

- status: `attributed`
- log p full -2.0285, empty -20.6579
- masks scored: 10/10 (+2 top-k)
- ranked sources:
    - `+14.621` [readme] Prednisone: A medication that lowers the body's immune response and inflammation.
    - `+3.204` [nih] prednisone: A drug used to reduce inflammation and lower the body’s immune response.  It is used with other dr
    - `+0.944` [readme] prednisone: A medication that helps lower the body's immune system reactions.

- rationale: Prednisone is a corticosteroid drug that dampens the immune system and reduces inflammation, and the replacement spells out that action in everyday language. Phrase frequency rises from Zipf 2.56 to 3.02, while age of acquisition drops from 17.17 to 12.32. Readers can now grasp what the medication does without needing to recognize the technical name.
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

**output:** She might need other medicines for nerve pain if she needs them.

| metric | value |
|---|---:|
| bertscore_f1 | 0.694 |
| coleman_liau | 6.87 |
| coleman_liau_drop | 5.62 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 3.84 |
| fkgl_drop | 6.37 |
| fre | 88.9 |
| fre_gain | 51.0 |
| human_edit_recall | 1.000 |
| length_ratio | 1.33 |
| n_words | 12.0 |
| nli_completeness | 0.905 |
| nli_faithfulness | 0.964 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.750 |
| sari | 24.58 |
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
| `neuropathic` -> `nerve pain` | replace | attributed | 1.029 | 2.093 | - | 0.400 | 0.188 | - |

**edit `neuropathic` -> `nerve pain`**

- status: `attributed`
- log p full -0.2914, empty -1.3199
- masks scored: 6/6 (+1 top-k)
- ranked sources:
    - `+0.874` [readme] Neuropathic: Neuropathic means nerve pain.
    - `+0.686` [readme] neuropathic: Nerve pain.

- rationale: "Neuropathic" describes pain that comes from damaged or malfunctioning nerves, and "nerve pain" conveys that same idea in everyday language. Phrase frequency rises from Zipf 2.35 to 4.13, while age of acquisition drops from 15.40 to 9.67. Readers can now grasp the concept without needing a medical vocabulary.
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

**output:** The patient received a preventive dose of antibiotics.

| metric | value |
|---|---:|
| bertscore_f1 | 0.582 |
| coleman_liau | 13.85 |
| coleman_liau_drop | -2.39 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 11.13 |
| fkgl_drop | 1.30 |
| fre | 29.5 |
| fre_gain | 11.1 |
| human_edit_recall | 1.000 |
| length_ratio | 1.14 |
| n_words | 8.0 |
| nli_completeness | 0.648 |
| nli_faithfulness | 0.981 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 31.67 |
| smog | 11.21 |
| smog_drop | 0.00 |

### Stage 4 - arm `termonly`

**output:** A dose of medicine to prevent infection was given.

| metric | value |
|---|---:|
| bertscore_f1 | 0.674 |
| coleman_liau | 7.33 |
| coleman_liau_drop | 4.12 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 7.59 |
| fkgl_drop | 4.84 |
| fre | 56.7 |
| fre_gain | 38.3 |
| human_edit_recall | 1.000 |
| length_ratio | 1.29 |
| n_words | 9.0 |
| nli_completeness | 0.286 |
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
| `prophylactic` -> `dose of medicine to prevent infection` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** A dose of medicine to prevent infection was given.

| metric | value |
|---|---:|
| bertscore_f1 | 0.674 |
| coleman_liau | 7.33 |
| coleman_liau_drop | 4.12 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 7.59 |
| fkgl_drop | 4.84 |
| fre | 56.7 |
| fre_gain | 38.3 |
| human_edit_recall | 1.000 |
| length_ratio | 1.29 |
| n_words | 9.0 |
| nli_completeness | 0.286 |
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
| `prophylactic` -> `dose of medicine to prevent infection` | replace | attributed | -0.341 | -0.514 | 0.649 | 0.850 | 0.058 | - |

**edit `prophylactic` -> `dose of medicine to prevent infection`**

- status: `attributed`
- log p full -1.2700, empty -0.9287
- masks scored: 66/66 (+2 top-k)
- ranked sources:
    - `+0.268` [readme] prophylactic: A prophylactic is like a protective shield that helps prevent diseases.
    - `+0.210` [wiktionary] prophylactic: Something that is prophylactic serves to prevent or protect against a disease or pregnancy.
    - `+0.162` [justplainclear] prophylactic: Drugs given to prevent sickness or pregnancy, birth control, condom
    - `+0.053` [nih] prophylactic: In medicine, something that prevents or protects.

- rationale: "Prophylactic" means a treatment given to stop an illness before it starts, and the phrase "dose of medicine to prevent infection" spells out that preventive purpose in everyday words. Phrase frequency rises from Zipf 2.59 to 3.84, while age of acquisition drops from 15.20 to 10.10. Readers can now grasp the protective intent of the medication without needing to know the technical adjective.
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

**output:** The patient has long-lasting low potassium caused by long-lasting diarrhea.

| metric | value |
|---|---:|
| bertscore_f1 | 0.621 |
| coleman_liau | 17.78 |
| coleman_liau_drop | 4.02 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.286 |
| fkgl | 13.09 |
| fkgl_drop | 3.16 |
| fre | 19.0 |
| fre_gain | 29.8 |
| human_edit_recall | 1.000 |
| length_ratio | 1.33 |
| n_words | 12.0 |
| nli_completeness | 0.956 |
| nli_faithfulness | 0.979 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 41.77 |
| smog | 14.55 |
| smog_drop | -3.35 |
| temporality_preservation | 0.000 |

### Stage 4 - arm `termonly`

**output:** Long-lasting low potassium caused by long-lasting loose stools.

| metric | value |
|---|---:|
| bertscore_f1 | 0.530 |
| coleman_liau | 18.93 |
| coleman_liau_drop | 2.88 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.375 |
| fkgl | 9.66 |
| fkgl_drop | 6.59 |
| fre | 40.1 |
| fre_gain | 50.8 |
| human_edit_recall | 1.000 |
| length_ratio | 1.11 |
| n_words | 10.0 |
| nli_completeness | 0.856 |
| nli_faithfulness | 0.962 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 35.51 |
| smog | 13.02 |
| smog_drop | -1.82 |
| temporality_preservation | 0.000 |

annotation backend `novita`, 0 edits kept


### Stage 4 - arm `grounded`

**output:** Long-lasting low blood potassium caused by long-lasting loose, watery poop.

| metric | value |
|---|---:|
| bertscore_f1 | 0.455 |
| coleman_liau | 17.20 |
| coleman_liau_drop | 4.60 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.375 |
| fkgl | 10.73 |
| fkgl_drop | 5.52 |
| fre | 35.9 |
| fre_gain | 46.7 |
| human_edit_recall | 1.000 |
| length_ratio | 1.33 |
| n_words | 12.0 |
| nli_completeness | 0.882 |
| nli_faithfulness | 0.960 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 33.89 |
| smog | 14.55 |
| smog_drop | -3.35 |
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

**output:** The liver and spleen are not enlarged, and there is no tenderness.

| metric | value |
|---|---:|
| bertscore_f1 | 0.450 |
| coleman_liau | 7.35 |
| coleman_liau_drop | 15.85 |
| copy_jargon_rate | 0.500 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 4.82 |
| fkgl_drop | 1.80 |
| fre | 81.9 |
| fre_gain | 27.1 |
| human_edit_recall | 0.500 |
| length_ratio | 1.33 |
| n_words | 12.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.985 |
| nli_faithfulness | 0.965 |
| replacement_f1 | 0.667 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 36.67 |
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
| `hepatosplenomegaly` -> `enlarged liver or spleen` | replace | attributed | -0.262 | -0.731 | - | 0.298 | 0.000 | - |
| `tenderness` -> `pain when touched` | replace | attributed | 0.775 | 1.299 | - | 0.805 | 0.575 | - |

**edit `hepatosplenomegaly` -> `enlarged liver or spleen`**

- status: `attributed`
- log p full -0.5874, empty -0.3255
- masks scored: 18/18 (+4 top-k)
- ranked sources:
    - `-0.072` [wiktionary] tenderness: Tenderness is the pain or discomfort when an affected area is touched.

- rationale: Hepatosplenomegaly is a single medical word that means both the liver and the spleen are larger than normal, and the replacement spells that out directly as "enlarged liver or spleen." Phrase frequency rises from Zipf 1.12 to 2.99, making the wording far more familiar to everyday readers. Patients can now grasp the core finding — that one or both organs are swollen — without needing to decode a compound Greek term.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `tenderness` -> `pain when touched`**

- status: `attributed`
- log p full -0.5779, empty -1.3527
- masks scored: 18/18 (+4 top-k)
- ranked sources:
    - `+0.775` [wiktionary] tenderness: Tenderness is the pain or discomfort when an affected area is touched.
    - `+0.200` [readme] tenderness: Tenderness is when an area hurts when you touch it.
    - `+0.069` [readme] Tenderness: Tenderness is when an area hurts or is sensitive to touch.

- rationale: Tenderness means that an area hurts when pressure is applied, and "pain when touched" spells out that same idea in everyday words. Phrase frequency rises from Zipf 3.24 to 4.22, while age of acquisition drops from 8.79 to 4.26. Readers can immediately grasp the symptom without needing to interpret a more abstract medical term.
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

**output:** He did not have left front chest pain when he exercised.

| metric | value |
|---|---:|
| bertscore_f1 | 0.872 |
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
| laterality_preservation | 0.000 |
| length_ratio | 1.00 |
| n_words | 11.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.978 |
| nli_faithfulness | 0.973 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 35.97 |
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
| `experience` -> `feel` | replace | attributed | 0.374 | 1.241 | 0.964 | 0.960 | 2.907 | - |
| `anterior` -> `front` | replace | attributed | -0.000 | -0.273 | 0.416 | 0.750 | 0.272 | - |

**edit `experience` -> `feel`**

- status: `attributed`
- log p full -0.2039, empty -0.5778
- masks scored: 66/66 (+3 top-k)
- ranked sources:
    - `+3.167` [thesaurus] experience: feel, have, go through
    - `+0.260` [readme] Anterior: The front part of the body or an organ.
    - `+0.090` [nih] anterior: In human anatomy, has to do with the front of a structure, or a structure found toward the front of 
    - `+0.074` [michigan] anterior: The front of the body.
    - `-0.183` [readme] anterior: Having to do with the front part of the body or an organ.

- rationale: "Experience" means to go through or live through something, and "feel" keeps that sense of direct personal encounter in a simpler verb. Word frequency rises from Zipf 5.27 to 5.67, and age of acquisition drops from 8.95 to 5.11. Readers can now grasp the idea of a personal sensation or event without tripping over a longer, later-learned word.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `anterior` -> `front`**

- status: `attributed`
- log p full -0.0006, empty -0.0004
- masks scored: 66/66 (+3 top-k)
- ranked sources:
    - `+0.420` [thesaurus] experience: feel, have, go through
    - `+0.148` [nih] anterior: In human anatomy, has to do with the front of a structure, or a structure found toward the front of 
    - `+0.127` [wiktionary] experience: Experience is the amount of time you have been doing something (especially, a job).
    - `+0.060` [wiktionary] anterior: Anterior is a word used in biology to refer to the front of an animal.
    - `+0.029` [wiktionary] experience: An experience is an event that happens to you or that you are a part of.

- rationale: "Anterior" is a formal word meaning the front side of something, and "front" conveys that same spatial idea in everyday language. Word frequency rises from Zipf 3.51 to 5.28, and age of acquisition drops from 14.12 to 5.19. Readers can now grasp the location immediately without pausing to translate a technical term.
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

**output:** The doctor would also use it to control the atrial fibrillation.

| metric | value |
|---|---:|
| bertscore_f1 | 0.520 |
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
| nli_completeness | 0.989 |
| nli_faithfulness | 0.029 |
| replacement_f1 | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 22.01 |
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
| `atrial fibrillation` -> `irregular heartbeat` | replace | attributed | -0.184 | -0.486 | - | 0.952 | 2.129 | - |

**edit `atrial fibrillation` -> `irregular heartbeat`**

- status: `attributed`
- log p full -0.5727, empty -0.3890
- masks scored: 10/10 (+2 top-k)
- ranked sources:
    - `+1.640` [readme] Atrial fibrillation: Atrial fibrillation is when your heart beats irregularly and can make you tired or more l
    - `-0.489` [readme] atrial fibrillation: Atrial fibrillation is when your heart beats in a weird way that can make you tired and i
    - `-1.070` [justplainclear] atrial fibrillation: A problem with the speed or rhythm that your heart beats It is the most common type of ar

- rationale: Atrial fibrillation is a heart rhythm disorder in which the upper chambers beat chaotically and often too fast, and "irregular heartbeat" captures that core idea in everyday language. Phrase frequency rises from Zipf 2.58 to 3.38, while age of acquisition drops from 14.58 to 9.16. Readers can now grasp the basic problem without needing to know the clinical term.
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

**output:** The patient seems to give a clear and accurate history.

| metric | value |
|---|---:|
| bertscore_f1 | 0.380 |
| coleman_liau | 7.34 |
| coleman_liau_drop | 3.61 |
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
| nli_completeness | 0.888 |
| nli_faithfulness | 0.614 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.250 |
| sari | 26.61 |
| smog | 11.21 |
| smog_drop | 1.82 |

### Stage 4 - arm `termonly`

**output:** Overall the patient appears to give a clear history.

| metric | value |
|---|---:|
| bertscore_f1 | 0.475 |
| coleman_liau | 8.62 |
| coleman_liau_drop | 2.33 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.250 |
| fkgl | 7.59 |
| fkgl_drop | 3.54 |
| fre | 56.7 |
| fre_gain | 27.2 |
| human_edit_recall | 1.000 |
| length_ratio | 0.90 |
| n_words | 9.0 |
| nli_completeness | 0.928 |
| nli_faithfulness | 0.951 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 38.38 |
| smog | 11.21 |
| smog_drop | 1.82 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `seemingly` -> `appears` | replace | - | - | - | - | - | - | - |
| `good historian` -> `clear history` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Overall the patient appears to give a clear history.

| metric | value |
|---|---:|
| bertscore_f1 | 0.475 |
| coleman_liau | 8.62 |
| coleman_liau_drop | 2.33 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.250 |
| fkgl | 7.59 |
| fkgl_drop | 3.54 |
| fre | 56.7 |
| fre_gain | 27.2 |
| human_edit_recall | 1.000 |
| length_ratio | 0.90 |
| n_words | 9.0 |
| nli_completeness | 0.928 |
| nli_faithfulness | 0.951 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 38.38 |
| smog | 11.21 |
| smog_drop | 1.82 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `seemingly` -> `appears` | replace | attributed | 0.431 | 1.539 | - | 0.856 | 1.467 | - |
| `good historian` -> `clear history` | replace | attributed | -0.094 | -0.265 | - | 0.844 | 0.933 | - |

**edit `seemingly` -> `appears`**

- status: `attributed`
- log p full -0.1592, empty -0.5903
- masks scored: 18/18 (+2 top-k)
- ranked sources:
    - `+1.448` [dictionary] Seemingly (adv.): In appearance; in show; in semblance; apparently; ostensibly.
    - `-0.020` [wiktionary] good: If something is good it is useful or helpful. This also means high quality.
    - `-0.295` [wiktionary] good: When you are good, you do the right things. That is, you do things that are kind or helpful. You do not 
    - `-0.580` [wiktionary] historian: A historian is a person who studies or writes about history.

- rationale: "Seemingly" signals that something gives the impression of being true without confirming it, and "appears" conveys that same sense of outward impression in a shorter, more direct verb. Word frequency rises from Zipf 4.10 to 4.84, and the syllable count drops from three to two. Readers can grasp the tentative quality of the statement without tripping over a longer, less familiar adverb.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `good historian` -> `clear history`**

- status: `attributed`
- log p full -0.4872, empty -0.3931
- masks scored: 18/18 (+2 top-k)
- ranked sources:
    - `+0.750` [dictionary] Seemingly (adv.): In appearance; in show; in semblance; apparently; ostensibly.
    - `-0.184` [wiktionary] good: When you are good, you do the right things. That is, you do things that are kind or helpful. You do not 
    - `-0.495` [wiktionary] good: If something is good it is useful or helpful. This also means high quality.
    - `-0.730` [wiktionary] historian: A historian is a person who studies or writes about history.

- rationale: "Good historian" is medical shorthand for a patient who can describe their symptoms and past care in an organized, reliable way, and "clear history" states that same idea in everyday language. Phrase frequency rises from Zipf 3.90 to 5.01, and age of acquisition drops from 11.58 to 6.42. The reader no longer has to decode a clinician’s idiom to grasp that the patient’s own account is trustworthy.
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

**output:** The colonoscopy did not find any active Crohn's disease.

| metric | value |
|---|---:|
| bertscore_f1 | 0.441 |
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
| nli_faithfulness | 0.992 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 1.000 |
| sari | 18.58 |
| smog | 3.13 |
| smog_drop | 0.00 |

### Stage 4 - arm `termonly`

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
| `colonoscopy` -> `colon exam` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** No current Crohn's disease was found during the test that checks the inside of the large intestine.

| metric | value |
|---|---:|
| bertscore_f1 | 0.599 |
| coleman_liau | 10.09 |
| coleman_liau_drop | -0.43 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.333 |
| fkgl | 7.00 |
| fkgl_drop | -3.35 |
| fre | 75.1 |
| fre_gain | -11.6 |
| human_edit_recall | 1.000 |
| length_ratio | 1.29 |
| n_words | 18.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.314 |
| nli_faithfulness | 0.866 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 42.49 |
| smog | 8.84 |
| smog_drop | -5.71 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `colonoscopy` -> `test that checks the inside of the large intestine` | replace | attributed | 7.807 | 8.002 | 0.860 | 0.919 | 5.640 | - |

**edit `colonoscopy` -> `test that checks the inside of the large intestine`**

- status: `attributed`
- log p full -1.7298, empty -9.5366
- masks scored: 66/66 (+2 top-k)
- ranked sources:
    - `+6.636` [readme] colonoscopy: A colonoscopy is a test that checks the inside of your large intestine for signs of cancer.
    - `+0.996` [readme] colonoscopy: A procedure to check for colon cancer by examining the inside of the large intestine.
    - `+0.269` [readme] Active: Happening right now.
    - `+0.227` [readme] von Willebrand 's disease: A condition where blood can't clot properly, causing abnormal bleeding.
    - `+0.135` [wiktionary] active: Something is active if it is turned on or started.

- rationale: The readme defines a colonoscopy as a test that checks the inside of the large intestine for signs of cancer, so the replacement preserves that exact description in everyday words. Phrase frequency rises from Zipf 2.74 to 3.18, and age of acquisition drops from 15.76 to 9.28. Readers can now grasp the purpose of the procedure without needing to know the technical name.
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

**output:** Shortly after the first check-up, the patient started to complain of chest pain and seemed to the nurse to be getting very tired and having trouble breathing.

| metric | value |
|---|---:|
| bertscore_f1 | 0.740 |
| coleman_liau | 10.81 |
| coleman_liau_drop | 5.16 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.250 |
| fkgl | 11.98 |
| fkgl_drop | 4.37 |
| fre | 57.2 |
| fre_gain | 31.3 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 28.0 |
| nli_completeness | 0.993 |
| nli_faithfulness | 0.992 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.556 |
| sari | 28.11 |
| smog | 3.13 |
| smog_drop | 12.77 |
| temporality_preservation | 1.000 |

### Stage 4 - arm `termonly`

**output:** Shortly after the patient's first check, the patient seemed to start complaining of chest pain and looked to the nurse like they were getting very tired and having trouble breathing.

| metric | value |
|---|---:|
| bertscore_f1 | 0.722 |
| coleman_liau | 12.21 |
| coleman_liau_drop | 3.76 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.250 |
| fkgl | 12.63 |
| fkgl_drop | 3.72 |
| fre | 57.9 |
| fre_gain | 32.0 |
| human_edit_recall | 1.000 |
| length_ratio | 1.11 |
| n_words | 31.0 |
| nli_completeness | 0.993 |
| nli_faithfulness | 0.993 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.600 |
| sari | 25.87 |
| smog | 8.84 |
| smog_drop | 7.06 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `mounting exhaustion` -> `very tired` | replace | - | - | - | - | - | - | - |
| `respiratory distress` -> `trouble breathing` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Shortly after the patient's first check, the patient seemed to start complaining of chest pain and looked to the nurse to have worsening extreme tiredness and trouble breathing.

| metric | value |
|---|---:|
| bertscore_f1 | 0.790 |
| coleman_liau | 13.59 |
| coleman_liau_drop | 2.38 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 12.61 |
| fkgl_drop | 3.75 |
| fre | 54.5 |
| fre_gain | 28.6 |
| human_edit_recall | 1.000 |
| length_ratio | 1.04 |
| n_words | 29.0 |
| nli_completeness | 0.993 |
| nli_faithfulness | 0.991 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.600 |
| sari | 33.48 |
| smog | 13.02 |
| smog_drop | 2.88 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `mounting exhaustion` -> `worsening extreme tiredness` | replace | attributed | 4.974 | 5.288 | - | 0.921 | 3.404 | - |
| `respiratory distress` -> `trouble breathing` | replace | attributed | 0.077 | 0.861 | - | 0.689 | 0.690 | - |

**edit `mounting exhaustion` -> `worsening extreme tiredness`**

- status: `attributed`
- log p full -1.3063, empty -6.2800
- masks scored: 34/34 (+4 top-k)
- ranked sources:
    - `+4.300` [wiktionary] exhaustion: Exhaustion is the state of extreme tiredness.
    - `+0.896` [wiktionary] exhaustion: Exhaustion is the point where something is completely depleted.
    - `+0.433` [wiktionary] mounting: If you mount something you get on to it.
    - `-0.102` [readme] Respiratory Distress: Having difficulty breathing.

- rationale: "Mounting exhaustion" describes a state of extreme tiredness that is steadily increasing, and "worsening extreme tiredness" conveys that same progression using more direct language. Phrase frequency decreases from Zipf 3.34 to 2.71, while age of acquisition rises from 7.61 to 10.84. The reader can now grasp the idea of deepening fatigue without needing to interpret the less common phrasing.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `respiratory distress` -> `trouble breathing`**

- status: `attributed`
- log p full -0.0605, empty -0.1377
- masks scored: 34/34 (+4 top-k)
- ranked sources:
    - `+0.739` [readme] Respiratory Distress: Having difficulty breathing.
    - `+0.049` [wiktionary] exhaustion: Exhaustion is the point where something is completely depleted.
    - `+0.040` [wiktionary] exhaustion: Exhaustion is the state of extreme tiredness.
    - `-0.073` [wiktionary] mounting: If you mount something you get on to it.
    - `-0.412` [readme] acute respiratory distress syndrome: A serious lung condition that causes low levels of oxygen in the blood, w

- rationale: "Respiratory distress" means a person is struggling to get enough air, and "trouble breathing" conveys that same difficulty in everyday words. Phrase frequency rises from Zipf 3.57 to 4.16, and age of acquisition drops from 11.16 to 4.56. Readers can immediately recognize the urgency of the symptom without needing clinical vocabulary.
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

### Stage 4 - arm `termonly`

**output:** She has been sent to get a device put in that helps her heart beat regularly.

| metric | value |
|---|---:|
| bertscore_f1 | 0.444 |
| coleman_liau | 4.46 |
| coleman_liau_drop | 7.21 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 5.40 |
| fkgl_drop | 2.78 |
| fre | 84.8 |
| fre_gain | 34.2 |
| human_edit_recall | 1.000 |
| length_ratio | 1.78 |
| n_words | 16.0 |
| nli_completeness | 0.076 |
| nli_faithfulness | 0.913 |
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
| `pacemaker implantation` -> `device put in that helps her heart beat regularly` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** She has been sent to another doctor to have a small device put in her chest to help control her heartbeat.

| metric | value |
|---|---:|
| bertscore_f1 | 0.463 |
| coleman_liau | 6.27 |
| coleman_liau_drop | 5.41 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.750 |
| fkgl | 7.77 |
| fkgl_drop | 0.41 |
| fre | 76.7 |
| fre_gain | 26.1 |
| human_edit_recall | 1.000 |
| length_ratio | 2.33 |
| n_words | 21.0 |
| nli_completeness | 0.205 |
| nli_faithfulness | 0.551 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 20.09 |
| smog | 8.84 |
| smog_drop | 2.37 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `referred` -> `sent to another doctor` | replace | attributed | 9.065 | 9.732 | 0.874 | 0.878 | 10.371 | - |
| `pacemaker implantation` -> `small device put in her chest to help control her heartbeat` | replace | attributed | 4.090 | 4.525 | 0.887 | 0.942 | 2.164 | - |

**edit `referred` -> `sent to another doctor`**

- status: `attributed`
- log p full -0.7202, empty -9.7852
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+10.708` [readme] REFERRED: Sending a patient to another person or place for medical care.
    - `+0.337` [readme] implantation: Surgery where a device is placed inside your body.
    - `+0.208` [wiktionary] referred: If you refer to something, you talk or write about it, usually in passing.
    - `+0.011` [readme] pacemaker: A pacemaker is a device that uses electrical signals to regulate the heartbeat.
    - `-0.002` [readme] IMPLANTATION: A surgery where a device is placed inside the body.

- rationale: The readme defines "referred" as sending a patient to another person or place for medical care, so "sent to another doctor" keeps that exact meaning in everyday words. Phrase frequency rises from Zipf 4.61 to 4.67. Readers can now see the action of directing care elsewhere without needing the clinical verb.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `pacemaker implantation` -> `small device put in her chest to help control her heartbeat`**

- status: `attributed`
- log p full -1.0309, empty -5.1213
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+3.820` [readme] pacemaker: A small device that helps regulate the heartbeat when placed in the chest.
    - `+1.656` [justplainclear] pacemaker: A medical device placed inside your chest or abdomen that helps control your heartbeat
    - `+0.226` [readme] IMPLANTATION: A surgery where a device is placed inside the body.

- rationale: The readme defines a pacemaker as a small device that helps regulate the heartbeat when placed in the chest, and the replacement spells out that exact idea in everyday words. Phrase frequency rises from Zipf 2.69 to 3.56, while age of acquisition drops from 12.42 to 8.06. Readers can now picture the device and its purpose without needing to know the technical term.
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

**output:** There was some bruising at the catheter site.

| metric | value |
|---|---:|
| bertscore_f1 | 0.782 |
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
| nli_completeness | 0.313 |
| nli_faithfulness | 0.725 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 66.08 |
| smog | 8.84 |
| smog_drop | -5.71 |

### Stage 4 - arm `termonly`

**output:** There was some bruising where the tube went in.

| metric | value |
|---|---:|
| bertscore_f1 | 0.584 |
| coleman_liau | 5.40 |
| coleman_liau_drop | -0.98 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 1.03 |
| fkgl_drop | -1.70 |
| fre | 103.7 |
| fre_gain | -10.4 |
| human_edit_recall | 1.000 |
| length_ratio | 0.69 |
| n_words | 9.0 |
| nli_completeness | 0.194 |
| nli_faithfulness | 0.530 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 49.17 |
| smog | 3.13 |
| smog_drop | 0.00 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `hematoma` -> `bruising` | replace | - | - | - | - | - | - | - |
| `cath site` -> `where the tube went in` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** There was some bruising where the tube went in.

| metric | value |
|---|---:|
| bertscore_f1 | 0.584 |
| coleman_liau | 5.40 |
| coleman_liau_drop | -0.98 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 1.03 |
| fkgl_drop | -1.70 |
| fre | 103.7 |
| fre_gain | -10.4 |
| human_edit_recall | 1.000 |
| length_ratio | 0.69 |
| n_words | 9.0 |
| nli_completeness | 0.194 |
| nli_faithfulness | 0.530 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 49.17 |
| smog | 3.13 |
| smog_drop | 0.00 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `hematoma` -> `bruising` | replace | attributed | 0.181 | 1.472 | 0.746 | 0.795 | 0.462 | - |
| `cath site` -> `where the tube went in` | replace | attributed | 0.505 | 1.004 | 0.585 | 0.764 | 0.184 | - |

**edit `hematoma` -> `bruising`**

- status: `attributed`
- log p full -0.0609, empty -0.2418
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+1.756` [michigan] hematoma: A bruise or when your skin is black and blue after an injury.
    - `+1.294` [iowa] HEMATOMA: a bruise, a black and blue mark
    - `+0.378` [wiktionary] site: A site is a website.
    - `+0.171` [wiktionary] site: A site is a location or a place.
    - `+0.004` [nih] hematoma: A pool of clotted or partially clotted blood in an organ, tissue, or body space, usually caused by a

- rationale: A hematoma is a collection of blood outside a blood vessel, and "bruising" conveys that same idea in everyday language. Phrase frequency rises from Zipf 2.61 to 3.18, while age of acquisition drops from 14.78 to 9.44. Readers can now recognize the injury without needing a clinical term.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `cath site` -> `where the tube went in`**

- status: `attributed`
- log p full -0.4781, empty -0.9833
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.552` [wiktionary] site: A site is a website.
    - `+0.368` [justplainclear] hematoma: A collection of blood under the skin or in the body that is typically caused by a broken blood vesse
    - `+0.304` [nih] hematoma: A pool of clotted or partially clotted blood in an organ, tissue, or body space, usually caused by a
    - `+0.040` [wiktionary] site: A site is a location or a place.

- rationale: "Cath site" is medical shorthand for the spot on the body where a catheter was inserted, and "where the tube went in" spells out that same location in everyday words. Phrase frequency rises from Zipf 2.90 to 4.32, and age of acquisition drops from 8.63 to 5.50. The reader can now picture the exact entry point without needing to know the abbreviated clinical term.
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

**output:** The dead tissue was taken out of the belly.

| metric | value |
|---|---:|
| bertscore_f1 | 0.792 |
| coleman_liau | 2.82 |
| coleman_liau_drop | 4.51 |
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
| rewrite_aggressiveness | 0.667 |
| sari | 33.77 |
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
| `necrotic tissue` -> `dead tissue` | replace | attributed | -0.030 | -2.768 | 0.241 | 0.605 | 0.145 | - |

**edit `necrotic tissue` -> `dead tissue`**

- status: `attributed`
- log p full -0.0324, empty -0.0021
- masks scored: 66/66 (+2 top-k)
- ranked sources:
    - `+0.347` [readme] Necrotic: Necrotic means when tissue or skin dies.
    - `+0.202` [readme] tissue: A group of cells that work together to form body structures and organs.
    - `+0.198` [wiktionary] tissue: Tissue is a group of cells that work together to do a job.
    - `-0.042` [readme] necrotic: Tissue or skin death.

- rationale: Necrotic tissue refers to body tissue that has died, and "dead tissue" conveys that same meaning in plain language. Phrase frequency rises from Zipf 2.54 to 4.26, while age of acquisition drops from 15.07 to 5.17. Readers can immediately grasp the condition without needing specialized medical vocabulary.
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

**output:** Pressure was applied and the bleeding stopped.

| metric | value |
|---|---:|
| bertscore_f1 | 0.725 |
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
| nli_completeness | 0.301 |
| nli_faithfulness | 0.535 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.667 |
| sari | 30.32 |
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
| `hemostatic` -> `bleeding stopped` | replace | attributed | 0.303 | 1.481 | - | 0.800 | 1.085 | - |

**edit `hemostatic` -> `bleeding stopped`**

- status: `attributed`
- log p full -0.1099, empty -0.4125
- masks scored: 6/6 (+1 top-k)
- ranked sources:
    - `+1.195` [readme] hemostatic: Hemostatic means stopping bleeding.
    - `+0.110` [readme] hemostatic: Stopping blood flow.

- rationale: Hemostatic describes something that causes bleeding to stop, so the phrase "bleeding stopped" conveys the same idea in everyday language. Phrase frequency rises from Zipf 1.73 to 4.01, making the wording far more familiar to readers. Patients can now grasp the outcome immediately without needing to decode a technical adjective.
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

**output:** The area was washed with some salt water and cleaned.

| metric | value |
|---|---:|
| bertscore_f1 | 0.837 |
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
| nli_completeness | 0.990 |
| nli_faithfulness | 0.990 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 71.64 |
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

**output:** The area was washed out with some salt water and cleared.

| metric | value |
|---|---:|
| bertscore_f1 | 1.000 |
| coleman_liau | 5.76 |
| coleman_liau_drop | 1.57 |
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
| nli_completeness | 0.987 |
| nli_faithfulness | 0.987 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 91.67 |
| smog | 8.84 |
| smog_drop | 0.00 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `lavaged` -> `washed out` | replace | attributed | 0.402 | 0.686 | - | 0.909 | 1.188 | - |
| `saline` -> `salt water` | replace | attributed | -0.000 | -0.082 | - | 0.894 | 1.461 | - |

**edit `lavaged` -> `washed out`**

- status: `attributed`
- log p full -0.6958, empty -1.0976
- masks scored: 34/34 (+4 top-k)
- ranked sources:
    - `+1.395` [readme] lavaged: To clean out an organ or wound with fluid.
    - `+0.207` [readme] saline: A solution made of saltwater that matches the body's fluid concentration and can be used to replace lo
    - `+0.108` [readme] Saline: Salt water solution used to replace body fluids.
    - `-0.132` [wiktionary] saline: If something is saline it is salty, especially water containing salt.
    - `-0.164` [nih] saline: A solution of salt and water.

- rationale: "Lavaged" is a technical verb meaning to flush or cleanse a body cavity with fluid, and "washed out" conveys that same action in everyday language. Phrase frequency rises from Zipf 0.00 to 4.10, showing the replacement is far more common in general use. Readers can now picture the procedure immediately without needing a medical dictionary.
- audit: coverage 1.0, grounding_error=True, omission=False, source_ok=False, passage_ok=True

**edit `saline` -> `salt water`**

- status: `attributed`
- log p full -0.0030, empty -0.0028
- masks scored: 34/34 (+4 top-k)
- ranked sources:
    - `+1.997` [readme] Saline: Salt water solution used to replace body fluids.
    - `+0.536` [nih] saline: A solution of salt and water.
    - `+0.411` [readme] lavaged: To clean out an organ or wound with fluid.
    - `-0.539` [wiktionary] saline: If something is saline it is salty, especially water containing salt.
    - `-1.774` [readme] saline: A solution made of saltwater that matches the body's fluid concentration and can be used to replace lo

- rationale: Saline is a sterile solution of salt dissolved in water, and "salt water" conveys that same mixture in everyday words. Phrase frequency rises from Zipf 3.33 to 4.55, while age of acquisition drops from 11.71 to 5.05. Readers can immediately picture the familiar liquid without needing the technical label.
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
| `inability to ambulate` -> `not being able to walk` | replace | attributed | 0.164 | 0.538 | 0.861 | 0.875 | 0.111 | - |

**edit `inability to ambulate` -> `not being able to walk`**

- status: `attributed`
- log p full -0.2882, empty -0.4522
- masks scored: 66/66 (+2 top-k)
- ranked sources:
    - `+1.085` [michigan] inability: Not able to.
    - `+0.974` [wiktionary] inability: An inability is something that you can not do.
    - `+0.283` [readme] ambulate: To ambulate means to walk or move around.

- rationale: "Inability to ambulate" means a person cannot walk, and "not being able to walk" states that same fact in everyday words. Phrase frequency rises from Zipf 1.40 to 4.87, and age of acquisition drops from 10.67 to 7.79. Readers can now grasp the mobility limitation immediately without stumbling over formal phrasing.
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

**output:** An organ is pushing through a weak spot in the muscle on the left side.

| metric | value |
|---|---:|
| bertscore_f1 | 0.459 |
| coleman_liau | 3.88 |
| coleman_liau_drop | -3.80 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 4.42 |
| fkgl_drop | -2.14 |
| fre | 90.1 |
| fre_gain | -2.9 |
| human_edit_recall | 1.000 |
| laterality_preservation | 1.000 |
| length_ratio | 1.25 |
| n_words | 15.0 |
| nli_completeness | 0.028 |
| nli_faithfulness | 0.518 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 66.19 |
| smog | 3.13 |
| smog_drop | 5.71 |

annotation backend `novita`, 0 edits kept


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

**output:** The doctor checked the other body systems and found nothing wrong.

| metric | value |
|---|---:|
| bertscore_f1 | 0.427 |
| coleman_liau | 10.51 |
| coleman_liau_drop | 0.89 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 5.86 |
| fkgl_drop | 2.51 |
| fre | 72.6 |
| fre_gain | 19.8 |
| human_edit_recall | 1.000 |
| length_ratio | 1.10 |
| n_words | 11.0 |
| negation_preservation | 0.000 |
| nli_completeness | 0.983 |
| nli_faithfulness | 0.045 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 9.68 |
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
| `unremarkable` -> `normal` | replace | attributed | -0.009 | -1.434 | - | - | - | - |

**edit `unremarkable` -> `normal`**

- status: `attributed`
- log p full -0.0117, empty -0.0028
- masks scored: 4/4 (+1 top-k)
- ranked sources:
    - `-0.507` [wiktionary] unremarkable: If something is unremarkable, it is common and ordinary.

- rationale: "Unremarkable" in a medical report means that nothing abnormal was found, so "normal" conveys the same idea in a single, familiar word. Phrase frequency rises from Zipf 2.83 to 5.01, and age of acquisition drops from 11.06 to 5.53. Readers can grasp the result immediately without stumbling over a long, technical-sounding term.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True
