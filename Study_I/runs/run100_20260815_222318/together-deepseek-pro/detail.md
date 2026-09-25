# Step-by-step detail - together-deepseek-pro (`run100_20260815_222318`)

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

**output:** He lost interest in things he used to enjoy and did not want to be around other people. He also had trouble sleeping because he woke up often and felt restless.

| metric | value |
|---|---:|
| bertscore_f1 | 0.490 |
| coleman_liau | 6.24 |
| coleman_liau_drop | 12.73 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 6.44 |
| fkgl_drop | 9.59 |
| fre | 76.5 |
| fre_gain | 66.1 |
| human_edit_recall | 1.000 |
| length_ratio | 1.55 |
| n_words | 31.0 |
| nli_completeness | 0.056 |
| nli_faithfulness | 0.884 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.778 |
| sari | 10.76 |
| smog | 3.13 |
| smog_drop | 12.77 |

### Stage 4 - arm `termonly`

**output:** He lost the ability to feel pleasure and did not care about social activities, and had trouble sleeping because he often woke up and felt restless.

| metric | value |
|---|---:|
| bertscore_f1 | 0.651 |
| coleman_liau | 9.83 |
| coleman_liau_drop | 9.13 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 12.70 |
| fkgl_drop | 3.32 |
| fre | 50.3 |
| fre_gain | 39.9 |
| human_edit_recall | 1.000 |
| length_ratio | 1.30 |
| n_words | 26.0 |
| nli_completeness | 0.990 |
| nli_faithfulness | 0.993 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.714 |
| sari | 24.34 |
| smog | 11.21 |
| smog_drop | 4.70 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `anhedonic` -> `lost the ability to feel pleasure` | replace | - | - | - | - | - | - | - |
| `disinterested` -> `did not care` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** He lost the ability to feel pleasure and was not interested in social activities, and had trouble sleeping because he often woke up and felt restless.

| metric | value |
|---|---:|
| bertscore_f1 | 0.683 |
| coleman_liau | 10.50 |
| coleman_liau_drop | 8.46 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 13.16 |
| fkgl_drop | 2.87 |
| fre | 47.0 |
| fre_gain | 36.6 |
| human_edit_recall | 1.000 |
| length_ratio | 1.30 |
| n_words | 26.0 |
| nli_completeness | 0.989 |
| nli_faithfulness | 0.992 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.714 |
| sari | 28.47 |
| smog | 13.02 |
| smog_drop | 2.88 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `anhedonic` -> `lost the ability to feel pleasure` | replace | attributed | -0.197 | -0.262 | - | 0.400 | 0.025 | - |
| `disinterested` -> `not interested` | replace | attributed | 0.178 | 1.692 | - | 0.800 | 1.938 | - |

**edit `anhedonic` -> `lost the ability to feel pleasure`**

- status: `attributed`
- log p full -1.4969, empty -1.3000
- masks scored: 6/6 (+2 top-k)
- ranked sources:
    - `+0.327` [wiktionary] disinterested: If someone is disinterested, they are not affected by a situation, so they can make fair decisi
    - `+0.302` [wiktionary] disinterested: If someone is disinterested, they are not interested in something; they find it boring.

- rationale: Anhedonic describes a state where someone cannot experience enjoyment, so "lost the ability to feel pleasure" directly conveys that same emotional numbness in everyday terms. Word frequency rises sharply from Zipf 1.11 to 4.36, making the replacement far more familiar. The reader can now grasp the core experience without needing to decode a rare clinical adjective.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `disinterested` -> `not interested`**

- status: `attributed`
- log p full -0.0450, empty -0.2232
- masks scored: 6/6 (+2 top-k)
- ranked sources:
    - `+1.920` [wiktionary] disinterested: If someone is disinterested, they are not interested in something; they find it boring.
    - `-0.018` [wiktionary] disinterested: If someone is disinterested, they are not affected by a situation, so they can make fair decisi

- rationale: "Disinterested" means impartial or unbiased, but it is often mistaken for lacking interest, so "not interested" directly conveys that intended meaning. Word frequency rises from Zipf 2.91 to 4.94, and age of acquisition drops from 12.40 to 8.83. Readers can now grasp the emotional stance without stumbling over a commonly confused word.
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
| `Myocardial infarction` -> `heart attack` | replace | attributed | 0.000 | 1.213 | 0.559 | 0.714 | 0.436 | - |
| `can not be excluded` -> `ruled out` | replace | attributed | -0.001 | -1.824 | 0.633 | 0.826 | 0.091 | - |

**edit `Myocardial infarction` -> `heart attack`**

- status: `attributed`
- log p full -0.0000, empty -0.0001
- masks scored: 66/66 (+3 top-k)
- ranked sources:
    - `+1.059` [iowa] MYOCARDIAL INFARCTION: heart attack
    - `+0.623` [wiktionary] can: If someone can do something, they are allowed to do it.
    - `+0.528` [justplainclear] myocardial infarction: A heart attack
    - `+0.215` [wiktionary] not: The item before "not" is more correct or better than the item after "not".
    - `+0.117` [wiktionary] not: "Not" makes a phrase have the opposite meaning.

- rationale: Myocardial infarction refers to the death of heart muscle due to blocked blood flow, and "heart attack" conveys that same life-threatening event in everyday terms. Word frequency rises sharply from Zipf 2.58 to 4.89, while age of acquisition drops from 16.64 to 6.58. This lets the reader immediately grasp the emergency without needing clinical vocabulary.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `can not be excluded` -> `ruled out`**

- status: `attributed`
- log p full -0.0008, empty -0.0001
- masks scored: 66/66 (+3 top-k)
- ranked sources:
    - `+0.833` [iowa] MYOCARDIAL INFARCTION: heart attack
    - `+0.742` [michigan] myocardial infarction: Occurs when the flow of blood to the heart is stopped by a blood clot or a spasm of an 
    - `+0.425` [readme] inferior wall myocardial infarction: Heart damage at the bottom of the left ventricle due to a blocked artery.
    - `+0.289` [readme] inferior myocardial infarction: A heart attack caused by a blockage in a blood vessel that affects the lower p
    - `+0.248` [wiktionary] not: The item before "not" is more correct or better than the item after "not".

- rationale: The original phrase means that a possibility cannot be dismissed, and "ruled out" conveys that same idea of eliminating something from consideration in simpler terms. Phrase frequency rises from Zipf 3.89 to 4.30, while age of acquisition drops from 5.11 to 3.28. The reader can now grasp the diagnostic uncertainty without wrestling with a formal, multi-word negation.
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

**output:** There was a large bruise and swelling inside the fluid-filled sac under the shoulder muscle.

| metric | value |
|---|---:|
| bertscore_f1 | 0.570 |
| coleman_liau | 11.61 |
| coleman_liau_drop | 2.69 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 7.57 |
| fkgl_drop | -1.56 |
| fre | 67.5 |
| fre_gain | -2.2 |
| human_edit_recall | 1.000 |
| length_ratio | 1.14 |
| n_words | 16.0 |
| nli_completeness | 0.896 |
| nli_faithfulness | 0.759 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.200 |
| sari | 40.94 |
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
| `hematoma` -> `bruise` | replace | - | - | - | - | - | - | - |
| `subdeltoid bursa` -> `fluid-filled sac under the shoulder muscle` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** There was a large bruise and swelling inside the fluid-filled sac under the shoulder muscle.

| metric | value |
|---|---:|
| bertscore_f1 | 0.570 |
| coleman_liau | 11.61 |
| coleman_liau_drop | 2.69 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 7.57 |
| fkgl_drop | -1.56 |
| fre | 67.5 |
| fre_gain | -2.2 |
| human_edit_recall | 1.000 |
| length_ratio | 1.14 |
| n_words | 16.0 |
| nli_completeness | 0.896 |
| nli_faithfulness | 0.759 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.200 |
| sari | 40.94 |
| severity_downgrade | 0.000 |
| severity_preservation | 1.000 |
| severity_tier_input | 2.000 |
| severity_tier_output | 2.000 |
| smog | 8.84 |
| smog_drop | 0.00 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `marked` -> `large` | replace | attributed | 0.038 | 0.420 | 0.287 | 0.753 | 0.138 | - |
| `hematoma` -> `bruise` | replace | attributed | 0.327 | 2.935 | 0.802 | 0.913 | 0.952 | - |
| `subdeltoid bursa` -> `fluid-filled sac under the shoulder muscle` | replace | attributed | -1.367 | -1.629 | 0.722 | 0.571 | 0.248 | - |

**edit `marked` -> `large`**

- status: `attributed`
- log p full -0.0777, empty -0.1160
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+0.355` [wiktionary] marked: Something that is marked is significant or notable.
    - `+0.217` [nih] hematoma: A pool of clotted or partially clotted blood in an organ, tissue, or body space, usually caused by a
    - `+0.054` [iowa] HEMATOMA: a bruise, a black and blue mark
    - `-0.074` [readme] bursa: A small sac of fluid that cushions joints as they move.
    - `-0.130` [michigan] hematoma: A bruise or when your skin is black and blue after an injury.

- rationale: "Marked" means something that is very noticeable or significant, so "large" conveys that same sense of obvious size in simpler words. Word frequency rises from Zipf 4.50 to 5.39, making it a more familiar term. The reader can now grasp the degree of change without encountering a less common adjective.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `hematoma` -> `bruise`**

- status: `attributed`
- log p full -0.0219, empty -0.3487
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+3.524` [iowa] HEMATOMA: a bruise, a black and blue mark
    - `+2.572` [michigan] hematoma: A bruise or when your skin is black and blue after an injury.
    - `-0.013` [readme] bursa: A small sac of fluid that cushions joints as they move.
    - `-0.150` [wiktionary] marked: Something that is marked is significant or notable.
    - `-0.401` [justplainclear] bursa: A small sac (pouch) found in your body which is filled with fluid. Bursa help your tendons or muscles m

- rationale: A hematoma is a collection of clotted blood outside a blood vessel, so calling it a "bruise" captures that same idea of trapped blood under the skin in a familiar word. Word frequency rises from Zipf 2.61 to 3.18, and age of acquisition drops from 14.78 to 5.45. This lets the reader recognize the injury as a common, everyday condition without needing clinical terminology.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `subdeltoid bursa` -> `fluid-filled sac under the shoulder muscle`**

- status: `attributed`
- log p full -2.6178, empty -1.2505
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+0.248` [justplainclear] bursa: A small sac (pouch) found in your body which is filled with fluid. Bursa help your tendons or muscles m
    - `-0.099` [wiktionary] marked: A mark is a single line left by a pen or pencil, or any small bit of color that got onto something.
    - `-0.249` [justplainclear] hematoma: A collection of blood under the skin or in the body that is typically caused by a broken blood vesse

- rationale: The original term names a specific cushioning sac located beneath the shoulder’s deltoid muscle, so the replacement directly describes it as a “fluid-filled sac under the shoulder muscle.” Word frequency rises sharply from Zipf 0.00 to 3.44, and age of acquisition drops from 15.78 to 9.00. This lets the reader picture the structure and its location without needing to decode a Latin anatomical label.
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

**output:** She has a history of smoking, high blood pressure, and high cholesterol.

| metric | value |
|---|---:|
| bertscore_f1 | 0.573 |
| coleman_liau | 9.77 |
| coleman_liau_drop | 18.39 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 7.77 |
| fkgl_drop | 11.63 |
| fre | 60.7 |
| fre_gain | 95.8 |
| human_edit_recall | 1.000 |
| length_ratio | 1.09 |
| n_words | 12.0 |
| nli_completeness | 0.957 |
| nli_faithfulness | 0.951 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 51.08 |
| smog | 11.21 |
| smog_drop | 1.82 |

### Stage 4 - arm `termonly`

**output:** She has a history of smoking, high blood pressure, and high cholesterol.

| metric | value |
|---|---:|
| bertscore_f1 | 0.573 |
| coleman_liau | 9.77 |
| coleman_liau_drop | 18.39 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 7.77 |
| fkgl_drop | 11.63 |
| fre | 60.7 |
| fre_gain | 95.8 |
| human_edit_recall | 1.000 |
| length_ratio | 1.09 |
| n_words | 12.0 |
| nli_completeness | 0.957 |
| nli_faithfulness | 0.951 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 51.08 |
| smog | 11.21 |
| smog_drop | 1.82 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `hypertension` -> `high blood pressure` | replace | - | - | - | - | - | - | - |
| `hyperlipidemia` -> `high cholesterol` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** History of smoking, high blood pressure, and high cholesterol.

| metric | value |
|---|---:|
| bertscore_f1 | 0.561 |
| coleman_liau | 13.78 |
| coleman_liau_drop | 14.38 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 8.90 |
| fkgl_drop | 10.50 |
| fre | 47.3 |
| fre_gain | 82.4 |
| human_edit_recall | 1.000 |
| length_ratio | 0.82 |
| n_words | 9.0 |
| nli_completeness | 0.946 |
| nli_faithfulness | 0.991 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 53.56 |
| smog | 11.21 |
| smog_drop | 1.82 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `hypertension` -> `high blood pressure` | replace | attributed | -0.001 | -1.492 | 0.388 | 0.765 | 0.547 | - |
| `hyperlipidemia` -> `high cholesterol` | replace | attributed | 1.933 | 7.049 | 0.904 | 0.929 | 3.075 | - |

**edit `hypertension` -> `high blood pressure`**

- status: `attributed`
- log p full -0.0012, empty -0.0003
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.997` [michigan] hypertension: When your low pressure (diastolic) is 90 or higher or the high pressure (systolic) is 140 or hig
    - `+0.450` [readme] HYPERTENSION: High blood pressure: when the force of blood in your arteries is too high.
    - `+0.441` [readme] Hyperlipidemia: Hyperlipidemia is when you have too much fat, like cholesterol, in your blood.
    - `+0.364` [readme] hyperlipidemia: Having a lot of fats like cholesterol in your blood.
    - `+0.067` [justplainclear] hypertension: Also known as: high blood pressure, HBP A condition of having high blood pressure for a long per

- rationale: Hypertension refers to elevated force of blood against artery walls, and "high blood pressure" conveys that exact condition in everyday terms. Word frequency rises from Zipf 3.41 to 4.71, while age of acquisition drops from 16.28 to 8.95. Readers can now grasp the health issue without needing clinical vocabulary.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `hyperlipidemia` -> `high cholesterol`**

- status: `attributed`
- log p full -0.0051, empty -1.9377
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+5.334` [justplainclear] hyperlipidemia: High cholesterol
    - `+2.259` [michigan] hyperlipidemia: High levels of fat or fat-like substances (cholesterol). Hyperlipidemia is also called high ch
    - `+0.900` [michigan] hypertension: When your low pressure (diastolic) is 90 or higher or the high pressure (systolic) is 140 or hig
    - `+0.406` [readme] HYPERTENSION: High blood pressure: when the force of blood in your arteries is too high.
    - `+0.025` [iowa] HYPERTENSION: high blood pressure

- rationale: "Hyperlipidemia" refers to excess fats in the blood, so "high cholesterol" conveys the same core idea using a familiar everyday term. Word frequency rises substantially from Zipf 1.95 to 3.72, making the replacement much more common. Readers can now immediately recognize the condition without needing to decode a technical medical label.
- audit: coverage 0.75, grounding_error=False, omission=False, source_ok=False, passage_ok=True

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

**output:** She said it hurt when she peed because her bladder cramped up, and she also said she often gets bladder infections.

| metric | value |
|---|---:|
| bertscore_f1 | 0.506 |
| coleman_liau | 8.48 |
| coleman_liau_drop | -1.66 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 8.33 |
| fkgl_drop | 0.56 |
| fre | 72.7 |
| fre_gain | 4.0 |
| human_edit_recall | 1.000 |
| length_ratio | 0.91 |
| n_words | 21.0 |
| nli_completeness | 0.960 |
| nli_faithfulness | 0.993 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 8.98 |
| smog | 8.84 |
| smog_drop | 2.37 |
| temporality_preservation | 0.000 |

### Stage 4 - arm `termonly`

**output:** She did complain of sudden painful tightening in her bladder when she passed urine, and she did say that she has a history of long-lasting urine infections.

| metric | value |
|---|---:|
| bertscore_f1 | 0.680 |
| coleman_liau | 10.39 |
| coleman_liau_drop | -3.57 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.667 |
| fkgl | 12.86 |
| fkgl_drop | -3.96 |
| fre | 51.0 |
| fre_gain | -17.7 |
| human_edit_recall | 1.000 |
| length_ratio | 1.22 |
| n_words | 28.0 |
| nli_completeness | 0.990 |
| nli_faithfulness | 0.994 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 32.03 |
| smog | 14.55 |
| smog_drop | -3.35 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `bladder spasms` -> `sudden painful tightening in her bladder` | replace | - | - | - | - | - | - | - |
| `urinated` -> `passed urine` | replace | - | - | - | - | - | - | - |
| `chronic UTIs` -> `long-lasting urine infections` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** She did complain of sudden, painful tightening in her pee sac when she passed urine, and she did say that she has a history of long-lasting pee infections.

| metric | value |
|---|---:|
| bertscore_f1 | 0.607 |
| coleman_liau | 8.83 |
| coleman_liau_drop | -2.01 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.714 |
| fkgl | 12.19 |
| fkgl_drop | -3.29 |
| fre | 57.6 |
| fre_gain | -11.1 |
| human_edit_recall | 1.000 |
| length_ratio | 1.26 |
| n_words | 29.0 |
| nli_completeness | 0.985 |
| nli_faithfulness | 0.992 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 31.19 |
| smog | 14.55 |
| smog_drop | -3.35 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `bladder spasms` -> `sudden, painful tightening in her pee sac` | replace | attributed | 12.687 | 12.826 | 0.805 | 0.916 | 3.583 | - |
| `urinated` -> `passed urine` | replace | attributed | 2.263 | 3.826 | 0.806 | 0.944 | 2.925 | - |
| `chronic UTIs` -> `long-lasting pee infections` | replace | attributed | -0.177 | -0.228 | 0.840 | 0.837 | 1.121 | - |

**edit `bladder spasms` -> `sudden, painful tightening in her pee sac`**

- status: `attributed`
- log p full -2.0449, empty -14.7321
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+5.511` [readme] bladder: A bladder is a sac in your body that holds pee.
    - `+1.927` [readme] spasms: When your muscles suddenly tighten up and hurt.
    - `+1.593` [readme] Chronic: A long-lasting or recurring health issue.
    - `+1.365` [readme] BLADDER: Bladder: Holds pee in your body.
    - `+0.932` [nih] bladder: The organ that stores urine.

- rationale: The glossary explains that a bladder is a sac that holds pee, so "sudden, painful tightening in her pee sac" directly conveys the organ’s function and the spasm sensation in everyday words. Word frequency rises from Zipf 2.89 to 3.04, and age of acquisition drops from 10.78 to 9.00. The reader can now grasp the uncomfortable event without needing to know the anatomical term.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `urinated` -> `passed urine`**

- status: `attributed`
- log p full -0.2132, empty -2.4761
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+3.461` [wiktionary] urinated: When a person or animal urinates, it passes urine to empty the bladder.
    - `+0.536` [readme] chronic: An ongoing or frequently recurring health issue.
    - `+0.375` [nih] bladder: The organ that stores urine.
    - `+0.260` [readme] UTIs: UTIs are infections in the urinary system.
    - `+0.214` [wiktionary] spasms: A spasm is a sudden and jerky movement.

- rationale: The glossary explains that to urinate means to pass urine from the bladder, so "passed urine" directly states that action in everyday words. Word frequency rises from Zipf 2.31 to 3.81, making the replacement much more common. The reader now grasps the bodily function without needing the clinical term.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `chronic UTIs` -> `long-lasting pee infections`**

- status: `attributed`
- log p full -1.5866, empty -1.4093
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+2.007` [readme] Chronic: A long-lasting or recurring health issue.
    - `+0.886` [michigan] chronic: Something, like a disease or symptom, that lasts for a long time.
    - `+0.361` [dorland] UTIs: urinary tract infections
    - `+0.354` [iowa] CHRONIC: continuing for a long time, ongoing
    - `+0.283` [michigan] bladder: A hollow organ that stores pee (urine).

- rationale: "Chronic UTIs" refers to repeated urinary tract infections that keep coming back, and "long-lasting pee infections" conveys that same idea of persistent bladder trouble in everyday words. Word frequency rises from Zipf 2.05 to 3.53, and age of acquisition drops from 11.25 to 3.89. This lets the reader grasp the ongoing nature of the problem without needing to decode the medical abbreviation.
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

**output:** The knee was not loose and had no swelling.

| metric | value |
|---|---:|
| bertscore_f1 | 0.607 |
| coleman_liau | 2.82 |
| coleman_liau_drop | 3.36 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 1.03 |
| fkgl_drop | 6.16 |
| fre | 103.7 |
| fre_gain | 42.4 |
| human_edit_recall | 1.000 |
| length_ratio | 0.82 |
| n_words | 9.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.993 |
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
| `instability` -> `loose` | replace | - | - | - | - | - | - | - |
| `effusion` -> `swelling` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** The knee was not wobbly and had no fluid buildup.

| metric | value |
|---|---:|
| bertscore_f1 | 0.672 |
| coleman_liau | 3.86 |
| coleman_liau_drop | 2.32 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 4.83 |
| fkgl_drop | 2.36 |
| fre | 78.2 |
| fre_gain | 16.9 |
| human_edit_recall | 1.000 |
| length_ratio | 0.91 |
| n_words | 10.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.995 |
| nli_faithfulness | 0.995 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 17.67 |
| smog | 8.84 |
| smog_drop | 2.37 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `instability` -> `wobbly` | replace | failed | - | - | - | - | - | - |
| `effusion` -> `fluid buildup` | replace | failed | - | - | - | - | - | - |

**edit `instability` -> `wobbly`**

- status: `failed` - full or empty boundary score failed; only 0/4 fitting scores usable; need 4
- log p full -10000.0000, empty -10000.0000
- masks scored: 0/6 (+0 top-k)

- rationale: "Instability" describes something that is unsteady or likely to give way, and "wobbly" conveys that same sense of being shaky in everyday terms. Word frequency drops from Zipf 3.71 to 3.03, while age of acquisition falls from 12.55 to 6.00. The reader can now grasp the unsteady condition without needing a more formal, clinical word.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `effusion` -> `fluid buildup`**

- status: `failed` - full or empty boundary score failed; only 0/4 fitting scores usable; need 4
- log p full -10000.0000, empty -10000.0000
- masks scored: 0/6 (+0 top-k)

- rationale: An effusion refers to an escape of fluid into a body cavity, so "fluid buildup" directly conveys that same idea of unwanted liquid collecting where it shouldn't. Word frequency rises from Zipf 2.41 to 3.31, and age of acquisition drops from 14.29 to 9.63. This lets the reader grasp the core problem without needing the clinical term.
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

**output:** Two days later, her pain went away and it has not come back.

| metric | value |
|---|---:|
| bertscore_f1 | 0.772 |
| coleman_liau | 2.45 |
| coleman_liau_drop | 3.12 |
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
| nli_completeness | 0.993 |
| nli_faithfulness | 0.994 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 20.91 |
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
| `resolved` -> `went away` | replace | attributed | -0.006 | -1.331 | - | 0.478 | 0.172 | - |
| `recurrence` -> `it come back` | replace | attributed | 0.063 | 0.963 | - | 0.837 | 0.072 | - |

**edit `resolved` -> `went away`**

- status: `attributed`
- log p full -0.0080, empty -0.0021
- masks scored: 34/34 (+4 top-k)
- ranked sources:
    - `+0.240` [nih] recurrence: Cancer that has recurred (come back), usually after a period of time during which the cancer could
    - `+0.068` [wiktionary] recurrence: A recurrence is something that happens again.
    - `-0.335` [readme] recurrence: When a disease comes back after being treated.
    - `-0.360` [wiktionary] resolved: To resolve means to create a solution for a problem.
    - `-0.699` [wiktionary] resolved: When a problem is resolved, it has been brought to a successful solution.

- rationale: "Resolved" means a condition or symptom has ended, and "went away" conveys that same idea of disappearance in everyday terms. Word frequency rises from Zipf 4.10 to 5.26, making the replacement more familiar. The reader can now grasp that the issue cleared up without needing to interpret a formal medical verb.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `recurrence` -> `it come back`**

- status: `attributed`
- log p full -0.0410, empty -0.1040
- masks scored: 34/34 (+4 top-k)
- ranked sources:
    - `+1.201` [readme] recurrence: When a disease comes back after being treated.
    - `+1.130` [nih] recurrence: Cancer that has recurred (come back), usually after a period of time during which the cancer could
    - `+0.271` [wiktionary] resolved: To resolve means to create a solution for a problem.
    - `+0.254` [wiktionary] resolved: When a problem is resolved, it has been brought to a successful solution.
    - `-1.127` [wiktionary] recurrence: A recurrence is something that happens again.

- rationale: “Recurrence” means something happens again after a pause, and “it come back” expresses that same idea in everyday speech. Word frequency rises from Zipf 3.20 to 5.57, and age of acquisition drops from 11.79 to 5.31. The reader can now grasp the concept of a returning condition without needing a more formal medical term.
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

**output:** The patient has a fever, an ear infection, and possibly a serious body-wide infection.

| metric | value |
|---|---:|
| bertscore_f1 | 0.500 |
| coleman_liau | 10.67 |
| coleman_liau_drop | 5.76 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| diagnostic_identity_preservation | 1.000 |
| fkgl | 10.94 |
| fkgl_drop | 3.17 |
| fre | 41.6 |
| fre_gain | 35.2 |
| human_edit_recall | 1.000 |
| length_ratio | 1.88 |
| n_words | 15.0 |
| nli_completeness | 0.903 |
| nli_faithfulness | 0.911 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.400 |
| sari | 37.79 |
| smog | 14.55 |
| smog_drop | -1.53 |
| uncertainty_preservation | 1.000 |

### Stage 4 - arm `termonly`

**output:** Description: Fever, middle ear infection, and possible body-wide infection.

| metric | value |
|---|---:|
| bertscore_f1 | 0.758 |
| coleman_liau | 20.87 |
| coleman_liau_drop | -4.44 |
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
| nli_completeness | 0.551 |
| nli_faithfulness | 0.691 |
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
| `sepsis` -> `body-wide infection` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Description: Fever, an ear infection, and possible blood infection.

| metric | value |
|---|---:|
| bertscore_f1 | 0.776 |
| coleman_liau | 16.36 |
| coleman_liau_drop | 0.07 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| diagnostic_identity_preservation | 1.000 |
| fkgl | 11.52 |
| fkgl_drop | 2.59 |
| fre | 28.5 |
| fre_gain | 22.1 |
| human_edit_recall | 1.000 |
| length_ratio | 1.12 |
| n_words | 9.0 |
| nli_completeness | 0.666 |
| nli_faithfulness | 0.699 |
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
| `otitis media` -> `an ear infection` | replace | attributed | 2.121 | 2.394 | 0.835 | 0.922 | 2.401 | - |
| `sepsis` -> `blood infection` | replace | attributed | 0.786 | 1.450 | 0.863 | 0.889 | 0.952 | - |

**edit `otitis media` -> `an ear infection`**

- status: `attributed`
- log p full -1.3355, empty -3.4561
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+4.454` [readme] otitis media: An ear infection causing inflammation in the middle ear.
    - `+2.053` [michigan] otitis media: Ear infection, often in the middle ear.
    - `+1.878` [michigan] sepsis: A very serious infection in your blood caused by a germ (a bacteria). Also called septicemia.
    - `+0.674` [nih] sepsis: The presence of bacteria or their toxins in the blood or tissues.
    - `+0.054` [readme] Sepsis: When bacteria get into the blood, the body's reaction can lead to tissue and organ damage, potentially

- rationale: The glossary explains otitis media as an ear infection with middle-ear inflammation, so "an ear infection" conveys the same condition in everyday terms. Word frequency rises from Zipf 2.16 to 4.08, making the replacement much more familiar. The reader can now recognize the problem as a common infection without needing the clinical name.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `sepsis` -> `blood infection`**

- status: `attributed`
- log p full -0.4560, empty -1.2418
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+1.549` [michigan] sepsis: A very serious infection in your blood caused by a germ (a bacteria). Also called septicemia.
    - `+0.597` [readme] Sepsis: When bacteria get into the blood, the body's reaction can lead to tissue and organ damage, potentially
    - `+0.372` [nih] sepsis: The presence of bacteria or their toxins in the blood or tissues.
    - `-0.239` [readme] otitis media: An ear infection causing inflammation in the middle ear.

- rationale: The Michigan glossary defines sepsis as a serious blood infection caused by germs, so "blood infection" directly conveys that core meaning in everyday terms. Word frequency rises from Zipf 3.01 to 4.26, and age of acquisition drops from 16.33 to 8.05. This lets the patient grasp the critical location and nature of the illness without needing the clinical label.
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

**output:** Right now, her main issue is feeling very tired all day.

| metric | value |
|---|---:|
| bertscore_f1 | 0.557 |
| coleman_liau | 4.71 |
| coleman_liau_drop | 7.11 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 4.79 |
| fkgl_drop | 2.84 |
| fre | 80.3 |
| fre_gain | 16.8 |
| human_edit_recall | 1.000 |
| length_ratio | 0.79 |
| n_words | 11.0 |
| nli_completeness | 0.993 |
| nli_faithfulness | 0.994 |
| number_unit_preservation | 0.500 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.571 |
| sari | 13.16 |
| smog | 3.13 |
| smog_drop | 8.08 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `primary complaint` -> `main issue` | replace | - | - | - | - | - | - | - |
| `fatigue` -> `feeling very tired` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Right now, her main issue is feeling tired all day.

| metric | value |
|---|---:|
| bertscore_f1 | 0.564 |
| coleman_liau | 4.44 |
| coleman_liau_drop | 7.38 |
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
| nli_completeness | 0.993 |
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
| `primary complaint` -> `main issue` | replace | attributed | -0.444 | -0.705 | 0.747 | 0.888 | 1.230 | - |
| `fatigue` -> `feeling tired` | replace | attributed | 1.667 | 3.111 | 0.812 | 0.858 | 0.739 | - |

**edit `primary complaint` -> `main issue`**

- status: `attributed`
- log p full -1.2326, empty -0.7891
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+1.510` [readme] COMPLAINT: A complaint is when someone tells the doctor about an illness or issue they are experiencing.
    - `+0.280` [wiktionary] fatigue: Fatigue is the material failure, such as cracking or separation, caused by stress on the material.
    - `+0.237` [michigan] fatigue: tired, weak feeling of the whole body, feeling tired all over
    - `+0.193` [nih] fatigue: A condition marked by extreme tiredness and inability to function due to lack of energy. Fatigue may 
    - `+0.193` [wiktionary] complaint: A complaint is an expression of dissatisfaction

- rationale: "Primary complaint" refers to the main problem a patient reports, and "main issue" conveys that same idea in more everyday words. Word frequency rises from Zipf 4.21 to 4.93, while age of acquisition drops from 8.89 to 8.60. This lets the reader immediately grasp what the patient is most concerned about without needing clinical phrasing.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `fatigue` -> `feeling tired`**

- status: `attributed`
- log p full -0.2237, empty -1.8910
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+2.129` [justplainclear] fatigue: Tired, weak feeling of the whole body, feeling tired
    - `+1.390` [michigan] fatigue: tired, weak feeling of the whole body, feeling tired all over
    - `+0.775` [michigan] complaint: Your illness or symptom that is most important; the main reason you go to the doctor. Also known as
    - `+0.581` [readme] COMPLAINT: A complaint is when someone tells the doctor about an illness or issue they are experiencing.
    - `+0.477` [readme] complaint: A complaint is when a patient talks about their illness or problem.

- rationale: The glossary defines fatigue as a tired, weak feeling of the whole body, so "feeling tired" captures that same sense of low energy in everyday words. Word frequency rises from Zipf 3.86 to 4.57, and age of acquisition drops from 11.83 to 5.31. This lets the reader immediately recognize the symptom as ordinary tiredness without needing the clinical term.
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

**output:** He has had some changes in his bowel habits, with loose stools at times, and new pain mostly on the left side of his neck.

| metric | value |
|---|---:|
| bertscore_f1 | 0.604 |
| coleman_liau | 5.06 |
| coleman_liau_drop | 6.89 |
| copy_jargon_rate | 0.333 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.167 |
| fkgl | 7.85 |
| fkgl_drop | 4.47 |
| fre | 83.3 |
| fre_gain | 42.7 |
| human_edit_recall | 0.667 |
| laterality_preservation | 1.000 |
| length_ratio | 1.32 |
| n_words | 25.0 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.994 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 18.79 |
| smog | 3.13 |
| smog_drop | 9.89 |
| temporality_preservation | 0.000 |

### Stage 4 - arm `termonly`

**output:** He has noticed some change in his bowel pattern with sometimes watery stools and pain that just started, mostly in the left side of his neck.

| metric | value |
|---|---:|
| bertscore_f1 | 0.588 |
| coleman_liau | 8.49 |
| coleman_liau_drop | 3.46 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.250 |
| fkgl | 9.98 |
| fkgl_drop | 2.33 |
| fre | 69.8 |
| fre_gain | 29.2 |
| human_edit_recall | 1.000 |
| laterality_preservation | 1.000 |
| length_ratio | 1.37 |
| n_words | 26.0 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.989 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.250 |
| sari | 16.71 |
| smog | 8.84 |
| smog_drop | 4.18 |
| temporality_preservation | 0.000 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `loose stools` -> `watery stools` | replace | - | - | - | - | - | - | - |
| `new onset` -> `just started` | replace | - | - | - | - | - | - | - |
| `predominantly` -> `mostly` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** He has noticed some changes in his poop, with watery poop at times and a new start of pain mostly in the left side of his neck.

| metric | value |
|---|---:|
| bertscore_f1 | 0.672 |
| coleman_liau | 4.37 |
| coleman_liau_drop | 7.58 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.429 |
| fkgl | 8.93 |
| fkgl_drop | 3.39 |
| fre | 79.2 |
| fre_gain | 38.5 |
| human_edit_recall | 1.000 |
| laterality_preservation | 1.000 |
| length_ratio | 1.42 |
| n_words | 27.0 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.986 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.250 |
| sari | 21.19 |
| smog | 8.84 |
| smog_drop | 4.18 |
| temporality_preservation | 0.000 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `loose stools` -> `watery poop` | replace | attributed | 4.750 | 7.923 | 0.742 | 0.900 | 7.563 | - |
| `new onset` -> `new start` | replace | attributed | 1.291 | 2.296 | 0.715 | 0.899 | 2.070 | - |
| `predominantly` -> `mostly` | replace | attributed | -0.089 | -0.500 | 0.396 | 0.629 | 0.018 | - |

**edit `loose stools` -> `watery poop`**

- status: `attributed`
- log p full -0.0425, empty -4.7929
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+7.863` [readme] loose stools: Watery poop.
    - `+0.301` [dictionary] Irregularity (n.): The state or quality of being irregular; that which is irregular.
    - `+0.186` [wiktionary] onset: The onset of something is the time when it begins (usually something bad).
    - `+0.096` [wiktionary] stool: A stool is a piece of feces.

- rationale: "Loose stools" is a medical way of saying bowel movements that are not solid, and "watery poop" conveys that same meaning in everyday words. Word frequency rises slightly from Zipf 3.03 to 3.06, while age of acquisition drops from 7.71 to 6.65. This lets the reader immediately picture the symptom without needing to decode clinical phrasing.
- audit: coverage 0.833, grounding_error=False, omission=False, source_ok=False, passage_ok=True

**edit `new onset` -> `new start`**

- status: `attributed`
- log p full -0.3498, empty -1.6412
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+3.027` [michigan] onset: The start.
    - `+0.956` [wiktionary] onset: The onset of something is the time when it begins (usually something bad).
    - `+0.524` [nih] stool: The material in a bowel movement. Stool is made up of undigested food, bacteria, mucus, and cells from 
    - `+0.519` [readme] Stool: Stool is the waste material that comes out during a bowel movement.
    - `+0.511` [readme] stool: The stuff that comes out when you go to the bathroom.

- rationale: The Michigan glossary defines "new onset" simply as "the start," so "new start" directly conveys that meaning in everyday words. Word frequency rises from Zipf 3.72 to 5.48, and age of acquisition drops from 10.72 to 4.72. This lets the reader grasp that a condition has just begun without needing clinical phrasing.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `predominantly` -> `mostly`**

- status: `attributed`
- log p full -0.2431, empty -0.1543
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+0.163` [readme] stool: The stuff that comes out when you go to the bathroom.
    - `+0.145` [wiktionary] new: If somebody is new, they are not experienced.
    - `+0.135` [michigan] onset: The start.
    - `+0.122` [wiktionary] stool: A stool is a seat for one person that does not have a back or an armrest.
    - `+0.110` [readme] Stool: Stool is the waste material that comes out during a bowel movement.

- rationale: "Predominantly" means for the most part, and "mostly" conveys that same idea of something being the main element. Word frequency rises from Zipf 3.80 to 4.83, making the replacement more familiar. The reader can now grasp the proportion being described without encountering a longer, less common word.
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

**output:** The patient comes in for a follow-up visit about a past problem with red, tender bumps under the skin called erythema nodosum.

| metric | value |
|---|---:|
| bertscore_f1 | 0.398 |
| coleman_liau | 9.75 |
| coleman_liau_drop | 4.85 |
| copy_jargon_rate | 1.000 |
| critical_error | 0.000 |
| fkgl | 10.69 |
| fkgl_drop | 1.02 |
| fre | 57.6 |
| fre_gain | 25.1 |
| human_edit_recall | 0.000 |
| length_ratio | 1.35 |
| n_words | 23.0 |
| nli_completeness | 0.967 |
| nli_faithfulness | 0.075 |
| replacement_f1 | 0.000 |
| rewrite_aggressiveness | 1.000 |
| sari | 13.30 |
| smog | 11.21 |
| smog_drop | 3.35 |
| temporality_preservation | 1.000 |

### Stage 4 - arm `termonly`

**output:** The patient comes in for a follow-up for a history of tender red lumps under the skin.

| metric | value |
|---|---:|
| bertscore_f1 | 0.639 |
| coleman_liau | 5.66 |
| coleman_liau_drop | 8.94 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 7.70 |
| fkgl_drop | 4.01 |
| fre | 70.1 |
| fre_gain | 37.6 |
| human_edit_recall | 1.000 |
| length_ratio | 1.06 |
| n_words | 18.0 |
| nli_completeness | 0.557 |
| nli_faithfulness | 0.370 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.600 |
| sari | 23.09 |
| smog | 11.21 |
| smog_drop | 3.35 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `erythema nodosum` -> `tender red lumps under the skin` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** The patient comes for a follow-up for a history of tender red bumps on the shins.

| metric | value |
|---|---:|
| bertscore_f1 | 0.592 |
| coleman_liau | 5.55 |
| coleman_liau_drop | 9.05 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 6.88 |
| fkgl_drop | 4.83 |
| fre | 74.3 |
| fre_gain | 41.8 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 17.0 |
| nli_completeness | 0.409 |
| nli_faithfulness | 0.188 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.600 |
| sari | 22.19 |
| smog | 11.21 |
| smog_drop | 3.35 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `erythema nodosum` -> `tender red bumps on the shins` | replace | attributed | 0.162 | 0.211 | - | 0.109 | 0.281 | - |

**edit `erythema nodosum` -> `tender red bumps on the shins`**

- status: `attributed`
- log p full -1.3870, empty -1.5494
- masks scored: 10/10 (+2 top-k)
- ranked sources:
    - `+0.281` [readme] Erythema: Red skin.

- rationale: Erythema nodosum refers to an inflammatory condition causing painful, reddish lumps under the skin, so "tender red bumps on the shins" directly conveys the sensation, appearance, and typical location. Word frequency rises from a Zipf value of 1.39 to 2.61, making the replacement much more common in everyday language. The reader can now immediately picture the symptom without needing to decode a clinical diagnosis.
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

**output:** She did not have enough iron in her body last year. Because she had several surgeries and did not eat much by mouth, she may have low iron again.

| metric | value |
|---|---:|
| bertscore_f1 | 0.593 |
| coleman_liau | 4.96 |
| coleman_liau_drop | 2.91 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.200 |
| fkgl | 5.53 |
| fkgl_drop | 1.95 |
| fre | 81.3 |
| fre_gain | 20.2 |
| human_edit_recall | 1.000 |
| length_ratio | 1.26 |
| n_words | 29.0 |
| nli_completeness | 0.564 |
| nli_faithfulness | 0.501 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.800 |
| sari | 15.41 |
| smog | 7.17 |
| smog_drop | 4.04 |
| uncertainty_preservation | 1.000 |

### Stage 4 - arm `termonly`

**output:** She was low on iron last year, and with her many surgeries and poor intake by mouth, she may have become low on iron again.

| metric | value |
|---|---:|
| bertscore_f1 | 0.823 |
| coleman_liau | 5.29 |
| coleman_liau_drop | 2.58 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.200 |
| fkgl | 9.74 |
| fkgl_drop | -2.26 |
| fre | 69.8 |
| fre_gain | 8.7 |
| human_edit_recall | 1.000 |
| length_ratio | 1.09 |
| n_words | 25.0 |
| nli_completeness | 0.831 |
| nli_faithfulness | 0.050 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 29.35 |
| smog | 8.84 |
| smog_drop | 2.37 |
| uncertainty_preservation | 1.000 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `iron deficient` -> `low on iron` | replace | - | - | - | - | - | - | - |
| `p. o.` -> `by mouth` | replace | - | - | - | - | - | - | - |
| `iron deficient` -> `low on iron` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** She did not have enough iron last year, and with her many surgeries and poor intake by mouth, she may not have enough iron again.

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
| nli_completeness | 0.815 |
| nli_faithfulness | 0.214 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.667 |
| sari | 25.31 |
| smog | 8.84 |
| smog_drop | 2.37 |
| uncertainty_preservation | 1.000 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `p. o.` -> `by mouth` | replace | attributed | 0.000 | 0.852 | 0.534 | 0.696 | 1.660 | - |

**edit `p. o.` -> `by mouth`**

- status: `attributed`
- log p full -0.0000, empty -0.0000
- masks scored: 66/66 (+2 top-k)
- ranked sources:
    - `+2.904` [wiktionary] p: The sixteenth (16th) letter of the alphabet.
    - `+1.244` [wiktionary] o: The fifteenth (15th) letter of the alphabet. It is a vowel.
    - `+0.431` [michigan] deficient: To not have enough.
    - `+0.426` [wiktionary] iron: An element with the symbol Fe and the atomic number 26.
    - `+0.351` [readme] iron: A mineral that helps prevent anemia and can be taken in pill form.

- rationale: "P. o." is a medical abbreviation for the Latin "per os," meaning to take something through the mouth, so "by mouth" directly states that route in everyday English. The word frequency remains unchanged at a Zipf value of 4.82. The reader can now follow the instruction without needing to decode a non-intuitive abbreviation.
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

**output:** We will set up a time for him to wear a Holter monitor, which tracks his heartbeat, and send him back to his heart doctor.

| metric | value |
|---|---:|
| bertscore_f1 | 0.662 |
| coleman_liau | 5.06 |
| coleman_liau_drop | 3.46 |
| copy_jargon_rate | 1.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 8.32 |
| fkgl_drop | 0.82 |
| fre | 79.9 |
| fre_gain | 23.7 |
| human_edit_recall | 0.000 |
| length_ratio | 1.56 |
| n_words | 25.0 |
| nli_completeness | 0.957 |
| nli_faithfulness | 0.804 |
| replacement_f1 | 0.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.667 |
| sari | 22.73 |
| smog | 8.84 |
| smog_drop | 2.37 |

### Stage 4 - arm `termonly`

**output:** We will schedule him for the heart-rhythm recorder and refer him back to his heart doctor.

| metric | value |
|---|---:|
| bertscore_f1 | 0.757 |
| coleman_liau | 8.81 |
| coleman_liau_drop | -0.29 |
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
| nli_completeness | 0.746 |
| nli_faithfulness | 0.911 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 50.10 |
| smog | 8.84 |
| smog_drop | 2.37 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `Holter monitor` -> `heart-rhythm recorder` | replace | - | - | - | - | - | - | - |
| `cardiologist` -> `heart doctor` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** We will set up a time for him to wear a portable heart-beat recorder and send him back to his heart doctor.

| metric | value |
|---|---:|
| bertscore_f1 | 0.683 |
| coleman_liau | 5.00 |
| coleman_liau_drop | 3.52 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 8.01 |
| fkgl_drop | 1.13 |
| fre | 76.8 |
| fre_gain | 20.6 |
| human_edit_recall | 1.000 |
| length_ratio | 1.44 |
| n_words | 23.0 |
| nli_completeness | 0.832 |
| nli_faithfulness | 0.844 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.400 |
| sari | 24.96 |
| smog | 11.21 |
| smog_drop | 0.00 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `Holter monitor` -> `portable heart-beat recorder` | replace | attributed | 7.702 | 8.819 | - | 0.867 | 9.733 | - |
| `cardiologist` -> `heart doctor` | replace | attributed | 0.001 | 4.680 | - | 0.944 | 1.834 | - |

**edit `Holter monitor` -> `portable heart-beat recorder`**

- status: `attributed`
- log p full -0.3965, empty -8.0986
- masks scored: 34/34 (+4 top-k)
- ranked sources:
    - `+9.718` [iowa] HOLTER MONITOR: a portable machine for recording heart beats
    - `-0.016` [michigan] cardiologist: A doctor who treats heart and blood vessel problems.
    - `-0.104` [justplainclear] cardiologist: Heart doctor
    - `-0.200` [nih] cardiologist: A doctor who has special training to diagnose and treat diseases of the heart and blood vessels.
    - `-0.430` [wiktionary] cardiologist: A cardiologist is a doctor who specializes in medical problems related to the heart.

- rationale: A Holter monitor is a device worn to continuously track the heart’s electrical activity, so calling it a “portable heart-beat recorder” directly conveys its function and mobility. Word frequency rises from Zipf 2.12 to 3.50, and age of acquisition drops from 9.68 to 8.37. This lets the reader immediately grasp that it is a take-home tool for logging heart rhythms, without needing the unfamiliar brand name.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `cardiologist` -> `heart doctor`**

- status: `attributed`
- log p full -0.0000, empty -0.0012
- masks scored: 34/34 (+4 top-k)
- ranked sources:
    - `+3.103` [justplainclear] cardiologist: Heart doctor
    - `+1.269` [iowa] HOLTER MONITOR: a portable machine for recording heart beats
    - `+0.510` [wiktionary] cardiologist: A cardiologist is a doctor who specializes in medical problems related to the heart.
    - `+0.247` [nih] cardiologist: A doctor who has special training to diagnose and treat diseases of the heart and blood vessels.
    - `-0.104` [michigan] cardiologist: A doctor who treats heart and blood vessel problems.

- rationale: A cardiologist is a physician who specializes in diagnosing and treating heart conditions, so "heart doctor" conveys that exact role in familiar, everyday words. Word frequency rises from a Zipf value of 2.90 to 4.76, and age of acquisition drops from 13.42 to 5.17. This lets the reader immediately grasp the type of specialist being discussed without needing medical vocabulary.
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

**output:** The patient wished to go ahead with surgery.

| metric | value |
|---|---:|
| bertscore_f1 | 0.831 |
| coleman_liau | 6.60 |
| coleman_liau_drop | 10.15 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.250 |
| fkgl | 5.23 |
| fkgl_drop | 5.90 |
| fre | 71.8 |
| fre_gain | 42.3 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 8.0 |
| nli_completeness | 0.981 |
| nli_faithfulness | 0.992 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 41.60 |
| smog | 8.84 |
| smog_drop | 2.37 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `proceed` -> `go ahead` | replace | - | - | - | - | - | - | - |
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
| `proceed` -> `go forward` | replace | attributed | 6.820 | 7.848 | 0.758 | 0.912 | 0.780 | - |
| `operative intervention` -> `surgery` | replace | attributed | 0.006 | 0.303 | 0.398 | 0.533 | 0.078 | - |

**edit `proceed` -> `go forward`**

- status: `attributed`
- log p full -0.4422, empty -7.2620
- masks scored: 66/66 (+3 top-k)
- ranked sources:
    - `+2.404` [wiktionary] proceed: When you proceed, you go forward with something.
    - `+1.625` [michigan] proceed: To go or move forward.
    - `+0.972` [justplainclear] intervention: Ways to stop the spread of illness without drugs, such as hand washing, covering sneezes, closin
    - `+0.887` [wiktionary] operative: If something is operative, it is able to work.
    - `+0.688` [wiktionary] operative: An operative is an employee with some particular function or skill.

- rationale: The source defines "proceed" as going forward with something, so "go forward" directly carries that same meaning in simpler words. Word frequency rises from Zipf 4.18 to 5.07, and age of acquisition drops from 8.33 to 4.24. This lets the reader grasp the instruction without needing a less familiar verb.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `operative intervention` -> `surgery`**

- status: `attributed`
- log p full -0.0165, empty -0.0223
- masks scored: 66/66 (+3 top-k)
- ranked sources:
    - `+0.257` [wiktionary] proceed: When you proceed, you go forward with something.
    - `+0.179` [thesaurus] proceed: go, move forward
    - `+0.172` [wiktionary] proceed: (formal) The proceeds of some individual project or sale are the money earned from doing it.
    - `+0.149` [readme] INTERVENTION: An intervention is a step taken to help treat or prevent illness or injury.
    - `+0.088` [wiktionary] operative: If something is operative, it is able to work.

- rationale: “Operative intervention” refers to a medical procedure involving an incision to treat a condition, and “surgery” conveys that same idea in a familiar, everyday word. Word frequency rises from Zipf 3.71 to 4.63, and age of acquisition drops from 13.11 to 7.68. The reader can now immediately grasp that a hands‑on procedure is being discussed, without needing to decode formal clinical phrasing.
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

**output:** A KUB X‑ray was taken and it showed an unusual pattern of gas in the bowel.

| metric | value |
|---|---:|
| bertscore_f1 | 0.532 |
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
| nli_faithfulness | 0.177 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 16.39 |
| smog | 8.84 |
| smog_drop | 0.00 |

### Stage 4 - arm `termonly`

**output:** An X-ray of the belly was taken and showed an unusual pattern of gas in the gut.

| metric | value |
|---|---:|
| bertscore_f1 | 0.642 |
| coleman_liau | 3.61 |
| coleman_liau_drop | 4.89 |
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
| nli_completeness | 0.892 |
| nli_faithfulness | 0.837 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.200 |
| sari | 24.99 |
| smog | 8.84 |
| smog_drop | 0.00 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `obtained` -> `taken` | replace | - | - | - | - | - | - | - |
| `abnormal bowel gas pattern` -> `unusual pattern of gas in the gut` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** An x-ray of the belly was taken and showed an unusual pattern of air in the intestines.

| metric | value |
|---|---:|
| bertscore_f1 | 0.609 |
| coleman_liau | 6.00 |
| coleman_liau_drop | 2.50 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.667 |
| fkgl | 8.39 |
| fkgl_drop | -1.20 |
| fre | 65.2 |
| fre_gain | 3.8 |
| human_edit_recall | 1.000 |
| length_ratio | 1.06 |
| n_words | 18.0 |
| nli_completeness | 0.598 |
| nli_faithfulness | 0.409 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.167 |
| sari | 23.36 |
| smog | 11.21 |
| smog_drop | -2.37 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `KUB` -> `x-ray of the belly` | replace | attributed | 1.425 | 2.169 | 0.834 | 0.915 | 2.423 | - |
| `obtained` -> `taken` | replace | attributed | 0.002 | 0.447 | 0.738 | 0.883 | 0.062 | - |
| `abnormal bowel gas pattern` -> `unusual pattern of air in the intestines` | replace | attributed | 5.493 | 6.714 | 0.756 | 0.858 | 1.789 | - |

**edit `KUB` -> `x-ray of the belly`**

- status: `attributed`
- log p full -0.5234, empty -1.9484
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+2.802` [dorland] KUB: kidneys, ureters, and bladder (x-ray)
    - `+0.379` [wiktionary] gas: A gas is a substance, such as air, that is not liquid or solid.
    - `+0.109` [wiktionary] pattern: A pattern is a design that uses the same set of elements many times in the same order.
    - `+0.077` [wiktionary] gas: Gas is a substance such as methane, ethane, propane, or butane that is burned for heat or to make electri
    - `+0.048` [wiktionary] abnormal: An abnormal thing, or situation, is one that is strange, or not typical.

- rationale: The medical dictionary defines KUB as an x-ray of the kidneys, ureters, and bladder, so "x-ray of the belly" conveys the same imaging idea in everyday words. Syllable count moves from 1 to 5. The reader can now grasp that the test involves a picture of their abdomen without needing to decode the abbreviation.
- audit: coverage 0.5, grounding_error=True, omission=False, source_ok=False, passage_ok=True

**edit `obtained` -> `taken`**

- status: `attributed`
- log p full -0.0034, empty -0.0053
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+0.570` [wiktionary] bowel: The bowel is an internal organ which helps an organism digest food.
    - `+0.507` [wiktionary] abnormal: An abnormal thing, or situation, is one that is strange, or not typical.
    - `+0.129` [nih] bowel: The long, tube-shaped organ in the abdomen that completes the process of digestion. The bowel has two p

- rationale: "Obtained" means to come into possession of something, and "taken" conveys that same idea of acquiring or receiving in a more everyday way. Word frequency rises from Zipf 4.49 to 5.33, making it a more familiar choice. The reader can now grasp the action without pausing on a more formal term.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `abnormal bowel gas pattern` -> `unusual pattern of air in the intestines`**

- status: `attributed`
- log p full -0.3484, empty -5.8416
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+3.084` [wiktionary] gas: A gas is a substance, such as air, that is not liquid or solid.
    - `+1.294` [readme] bowel: The intestines in your belly that break down food.
    - `+1.241` [michigan] abnormal: Something that is not usual, like a growth or low or high amounts of blood cells.
    - `+1.186` [wiktionary] gas: Gas is a substance such as methane, ethane, propane, or butane that is burned for heat or to make electri
    - `+0.983` [wiktionary] bowel: The bowel is an internal organ which helps an organism digest food.

- rationale: The glossary defines gas as a substance like air that is neither liquid nor solid, so "unusual pattern of air in the intestines" directly conveys the same idea in everyday terms. Word frequency shifts slightly from Zipf 3.29 to 3.17, while age of acquisition drops from 10.05 to 8.56. This lets the reader grasp the finding as a visible arrangement of air without needing to interpret the clinical shorthand "bowel gas."
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

**output:** She was given a calming medicine called Ativan and arrived at the emergency room very drowsy and unable to share any information about her health.

| metric | value |
|---|---:|
| bertscore_f1 | 0.657 |
| coleman_liau | 11.09 |
| coleman_liau_drop | -1.89 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 14.46 |
| fkgl_drop | -2.14 |
| fre | 35.9 |
| fre_gain | -4.7 |
| human_edit_recall | 1.000 |
| length_ratio | 1.25 |
| n_words | 25.0 |
| nli_completeness | 0.991 |
| nli_faithfulness | 0.904 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.714 |
| sari | 27.95 |
| severity_downgrade | 0.000 |
| severity_tier_input | 3.000 |
| severity_tier_output | 3.000 |
| smog | 14.55 |
| smog_drop | 1.35 |

### Stage 4 - arm `termonly`

**output:** She has been given a calming medicine called lorazepam and came into the emergency room drowsy and unable to give any history.

| metric | value |
|---|---:|
| bertscore_f1 | 0.701 |
| coleman_liau | 10.27 |
| coleman_liau_drop | -1.07 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 12.84 |
| fkgl_drop | -0.52 |
| fre | 42.2 |
| fre_gain | 1.6 |
| human_edit_recall | 1.000 |
| length_ratio | 1.10 |
| n_words | 22.0 |
| nli_completeness | 0.277 |
| nli_faithfulness | 0.541 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 43.39 |
| severity_downgrade | 0.000 |
| severity_tier_input | 3.000 |
| severity_tier_output | 3.000 |
| smog | 14.55 |
| smog_drop | 1.35 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `sedated` -> `given a calming medicine` | replace | - | - | - | - | - | - | - |
| `obtunded` -> `drowsy` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** She was given a medicine to calm her and make her sleepy, and came into the emergency room not fully alert and unable to give any history.

| metric | value |
|---|---:|
| bertscore_f1 | 0.628 |
| coleman_liau | 6.73 |
| coleman_liau_drop | 2.47 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.667 |
| fkgl | 13.30 |
| fkgl_drop | -0.98 |
| fre | 47.8 |
| fre_gain | 7.2 |
| human_edit_recall | 1.000 |
| length_ratio | 1.35 |
| n_words | 27.0 |
| nli_completeness | 0.057 |
| nli_faithfulness | 0.975 |
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
| `sedated` -> `given a medicine to calm her and make her sleepy` | replace | attributed | 6.512 | 6.552 | - | 0.686 | 0.090 | - |
| `obtunded` -> `not fully alert` | replace | attributed | 5.583 | 10.596 | - | 0.759 | 9.951 | - |

**edit `sedated` -> `given a medicine to calm her and make her sleepy`**

- status: `attributed`
- log p full -3.2287, empty -9.7407
- masks scored: 18/18 (+4 top-k)
- ranked sources:
    - `+3.443` [readme] SEDATED: Feeling calm, relaxed, or sleepy because of certain medications.
    - `+3.353` [readme] Sedated: When you're sedated, you feel calm, relaxed, or sleepy because of specific medication.
    - `-0.497` [readme] obtunded: Being not fully alert.

- rationale: "Sedated" means being in a calm, drowsy state from medication, so the replacement explains exactly how that state is achieved. Word frequency rises from Zipf 2.78 to 3.58, making the phrasing more familiar. The reader now understands the purpose and effect of the medicine without needing the clinical shorthand.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `obtunded` -> `not fully alert`**

- status: `attributed`
- log p full -0.0066, empty -5.5896
- masks scored: 18/18 (+4 top-k)
- ranked sources:
    - `+9.897` [readme] obtunded: Being not fully alert.
    - `-0.054` [readme] SEDATED: Feeling calm, relaxed, or sleepy because of certain medications.
    - `-0.063` [readme] Sedated: When you're sedated, you feel calm, relaxed, or sleepy because of specific medication.
    - `-0.172` [wiktionary] sedated: A sedate person is calm and dignified.

- rationale: "Obtunded" describes a dulled or lessened state of alertness, so "not fully alert" conveys that same reduced responsiveness in everyday words. Word frequency rises sharply from Zipf 1.01 to 4.22, making the replacement far more common and recognizable. The reader can now grasp the patient's mental state without encountering a rare clinical term.
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

**output:** He does not have swelling now, but his legs have been a little puffy before.

| metric | value |
|---|---:|
| bertscore_f1 | 0.728 |
| coleman_liau | 5.43 |
| coleman_liau_drop | -3.09 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 5.21 |
| fkgl_drop | -0.79 |
| fre | 84.5 |
| fre_gain | -5.6 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 15.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.899 |
| nli_faithfulness | 0.990 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.800 |
| sari | 13.88 |
| severity_downgrade | 0.000 |
| severity_preservation | 0.000 |
| severity_tier_input | 1.000 |
| severity_tier_output | 1.000 |
| smog | 3.13 |
| smog_drop | 5.71 |
| temporality_preservation | 1.000 |

### Stage 4 - arm `termonly`

**output:** He has no fluid buildup now, but has had some mild leg swelling in the past.

| metric | value |
|---|---:|
| bertscore_f1 | 0.925 |
| coleman_liau | 3.74 |
| coleman_liau_drop | -1.40 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 4.66 |
| fkgl_drop | -0.24 |
| fre | 90.1 |
| fre_gain | 0.0 |
| human_edit_recall | 1.000 |
| length_ratio | 1.07 |
| n_words | 16.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.955 |
| nli_faithfulness | 0.994 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 66.67 |
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
| `edema` -> `fluid buildup` | replace | - | - | - | - | - | - | - |

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
| `edema` -> `swelling` | replace | attributed | 1.626 | 5.484 | - | 0.521 | 0.314 | - |

**edit `edema` -> `swelling`**

- status: `attributed`
- log p full -0.0172, empty -1.6427
- masks scored: 34/34 (+2 top-k)
- ranked sources:
    - `+1.106` [nih] edema: Swelling caused by excess fluid in body tissues.
    - `+0.792` [michigan] edema: Swelling caused by too much fluid in your body.
    - `+0.640` [readme] edema: Swelling due to too much fluid in the body tissues.
    - `+0.627` [readme] Edema: Swelling in the body caused by too much fluid.
    - `-0.809` [iowa] EDEMA: excess fluid collecting in tissue

- rationale: Edema refers to fluid trapped in body tissues causing puffiness, so "swelling" conveys that same idea in an everyday word. Word frequency rises from Zipf 2.95 to 3.68, making the replacement more familiar. The reader can now recognize the symptom without needing clinical vocabulary.
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

**output:** The patient has a mild form of secondary hyperparathyroidism.

| metric | value |
|---|---:|
| bertscore_f1 | 0.416 |
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
| nli_completeness | 0.992 |
| nli_faithfulness | 0.969 |
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

**output:** Mild overactivity of the parathyroid glands caused by another health problem.

| metric | value |
|---|---:|
| bertscore_f1 | 0.465 |
| coleman_liau | 16.31 |
| coleman_liau_drop | 19.89 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.333 |
| fkgl | 9.08 |
| fkgl_drop | 11.90 |
| fre | 49.5 |
| fre_gain | 99.5 |
| human_edit_recall | 1.000 |
| length_ratio | 2.20 |
| n_words | 11.0 |
| nli_completeness | 0.842 |
| nli_faithfulness | 0.858 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 23.50 |
| severity_downgrade | 0.000 |
| severity_preservation | 1.000 |
| severity_tier_input | 1.000 |
| severity_tier_output | 1.000 |
| smog | 11.21 |
| smog_drop | 0.00 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `secondary hyperparathyroidism` -> `overactivity of the parathyroid glands caused by another health problem` | replace | - | - | - | - | - | - | - |

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
| `secondary hyperparathyroidism` -> `overactive parathyroid glands from another cause` | replace | attributed | 2.624 | 2.723 | - | 0.747 | 0.515 | - |

**edit `secondary hyperparathyroidism` -> `overactive parathyroid glands from another cause`**

- status: `attributed`
- log p full -2.2939, empty -4.9181
- masks scored: 18/18 (+2 top-k)
- ranked sources:
    - `+0.984` [justplainclear] hyperparathyroidism: A condition where your parathyroid glands work too hard and raise the calcium level in yo
    - `+0.468` [wiktionary] secondary: of less than primary importance.
    - `+0.173` [wiktionary] secondary: second, next in order to the first or primary.
    - `+0.171` [nih] hyperparathyroidism: A condition in which the parathyroid gland (one of four pea-sized organs found on the thy

- rationale: Secondary hyperparathyroidism means the parathyroid glands become overactive due to a separate health issue, and the replacement directly conveys this by naming the glands and stating the cause. Phrase frequency rises from Zipf 1.88 to 2.08, while age of acquisition drops from 19.11 to 15.50. Readers can now grasp the condition as a gland problem triggered by something else, without needing the medical prefix.
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

**output:** Otherwise, the patient's review of all body systems was normal except for what was already mentioned.

| metric | value |
|---|---:|
| bertscore_f1 | 0.550 |
| coleman_liau | 12.44 |
| coleman_liau_drop | 0.00 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.667 |
| fkgl | 10.56 |
| fkgl_drop | 0.00 |
| fre | 47.8 |
| fre_gain | 0.0 |
| human_edit_recall | 1.000 |
| length_ratio | 1.06 |
| n_words | 17.0 |
| nli_completeness | 0.198 |
| nli_faithfulness | 0.336 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 23.16 |
| smog | 11.21 |
| smog_drop | 0.00 |

### Stage 4 - arm `termonly`

**output:** Otherwise, a full head-to-toe symptom check was done and was normal except for what was noted above.

| metric | value |
|---|---:|
| bertscore_f1 | 0.564 |
| coleman_liau | 9.75 |
| coleman_liau_drop | 2.68 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.333 |
| fkgl | 9.09 |
| fkgl_drop | 1.48 |
| fre | 60.2 |
| fre_gain | 12.4 |
| human_edit_recall | 1.000 |
| length_ratio | 1.19 |
| n_words | 19.0 |
| nli_completeness | 0.109 |
| nli_faithfulness | 0.162 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 23.35 |
| smog | 11.21 |
| smog_drop | 0.00 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `review of systems` -> `head-to-toe symptom check` | replace | - | - | - | - | - | - | - |
| `obtained` -> `done` | replace | - | - | - | - | - | - | - |
| `negative` -> `normal` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Otherwise, the full set of body-part questions was asked and was normal except for what was noted above.

| metric | value |
|---|---:|
| bertscore_f1 | 0.584 |
| coleman_liau | 9.62 |
| coleman_liau_drop | 2.82 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.667 |
| fkgl | 8.47 |
| fkgl_drop | 2.09 |
| fre | 66.4 |
| fre_gain | 18.5 |
| human_edit_recall | 1.000 |
| length_ratio | 1.19 |
| n_words | 19.0 |
| nli_completeness | 0.382 |
| nli_faithfulness | 0.302 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 22.23 |
| smog | 8.84 |
| smog_drop | 2.37 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `review of systems` -> `full set of body-part questions` | replace | attributed | 5.207 | 5.249 | - | 0.805 | 4.138 | - |
| `obtained` -> `asked` | replace | attributed | 0.038 | 0.330 | - | 0.785 | 1.123 | - |
| `negative` -> `normal` | replace | attributed | -1.001 | -4.299 | - | 0.765 | 0.032 | - |

**edit `review of systems` -> `full set of body-part questions`**

- status: `attributed`
- log p full -3.1783, empty -8.3852
- masks scored: 18/18 (+3 top-k)
- ranked sources:
    - `+4.305` [readme] Review of systems: Questions that ask patients about any symptoms they might be experiencing in different part
    - `+0.167` [wiktionary] negative: If something is negative, it is harmful, sad, or otherwise not good.
    - `+0.009` [wiktionary] obtained: If you obtain something, you get it.

- rationale: A review of systems is the series of questions a clinician asks about each part of the body, so "full set of body-part questions" directly conveys that process. Age of acquisition drops from 8.84 to 6.00, while phrase frequency shifts slightly from Zipf 4.79 to 4.74. This lets patients recognize they are being asked a complete head-to-toe checklist rather than a vague technical procedure.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `obtained` -> `asked`**

- status: `attributed`
- log p full -0.1042, empty -0.1422
- masks scored: 18/18 (+3 top-k)
- ranked sources:
    - `+1.202` [readme] Review of systems: Questions that ask patients about any symptoms they might be experiencing in different part
    - `+0.079` [wiktionary] negative: If a word, sentence, answer, etc. is negative, it uses a word like no, not, never, etc.
    - `-0.096` [wiktionary] obtained: If you obtain something, you get it.
    - `-0.618` [wiktionary] negative: If something is negative, it is harmful, sad, or otherwise not good.

- rationale: "Obtained" means to come into possession of something, and "asked" carries that same sense of acquiring information through a direct request. Word frequency rises from Zipf 4.49 to 5.30, making the replacement more familiar. The reader now immediately grasps that information was gathered by questioning, without needing to process a more formal term.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `negative` -> `normal`**

- status: `attributed`
- log p full -1.0253, empty -0.0240
- masks scored: 18/18 (+3 top-k)
- ranked sources:
    - `-0.271` [readme] Review of systems: Questions that ask patients about any symptoms they might be experiencing in different part
    - `-0.304` [wiktionary] obtained: If you obtain something, you get it.
    - `-0.913` [wiktionary] negative: If something is negative, it is harmful, sad, or otherwise not good.
    - `-1.260` [wiktionary] negative: If a word, sentence, answer, etc. is negative, it uses a word like no, not, never, etc.

- rationale: In medical contexts, "negative" means a test found no sign of disease, so "normal" conveys that reassuring result in a more everyday word. Word frequency rises from Zipf 4.79 to 5.01, and age of acquisition drops from 7.47 to 5.53. This lets the reader immediately grasp a favorable outcome without interpreting clinical phrasing.
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

**output:** The patient's symptoms get worse when she sits for a while, like when driving a car.

| metric | value |
|---|---:|
| bertscore_f1 | 0.596 |
| coleman_liau | 6.27 |
| coleman_liau_drop | 1.81 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 4.66 |
| fkgl_drop | 2.95 |
| fre | 90.1 |
| fre_gain | 21.1 |
| human_edit_recall | 1.000 |
| length_ratio | 1.13 |
| n_words | 17.0 |
| nli_completeness | 0.960 |
| nli_faithfulness | 0.993 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.714 |
| sari | 16.46 |
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
| `motor vehicle` -> `car` | replace | attributed | -0.000 | -1.901 | - | - | - | - |

**edit `motor vehicle` -> `car`**

- status: `attributed`
- log p full -0.0004, empty -0.0001
- masks scored: 4/4 (+1 top-k)
- ranked sources:
    - `-1.992` [wiktionary] motor vehicle: A motor vehicle a road vehicle powered by an internal combustion engine to provide power to rot

- rationale: A motor vehicle is any self-propelled road transport, and "car" names the most familiar everyday example. Word frequency rises from Zipf 4.33 to 5.45, and age of acquisition drops from 7.42 to 3.37. The reader instantly pictures a common automobile instead of decoding a broad technical category.
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

**output:** The exams of the forearm, elbow, and shoulder show no nerve problems.

| metric | value |
|---|---:|
| bertscore_f1 | 0.679 |
| coleman_liau | 8.32 |
| coleman_liau_drop | 8.68 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 5.81 |
| fkgl_drop | 7.02 |
| fre | 74.8 |
| fre_gain | 55.7 |
| human_edit_recall | 1.000 |
| length_ratio | 1.33 |
| n_words | 12.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.967 |
| nli_faithfulness | 0.988 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 46.66 |
| smog | 3.13 |
| smog_drop | 8.08 |

### Stage 4 - arm `termonly`

**output:** Forearm, elbow and shoulder exams show no nerve or muscle damage.

| metric | value |
|---|---:|
| bertscore_f1 | 0.859 |
| coleman_liau | 9.45 |
| coleman_liau_drop | 7.55 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 6.94 |
| fkgl_drop | 5.89 |
| fre | 64.9 |
| fre_gain | 45.8 |
| human_edit_recall | 1.000 |
| length_ratio | 1.22 |
| n_words | 11.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.852 |
| nli_faithfulness | 0.145 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 48.68 |
| smog | 3.13 |
| smog_drop | 8.08 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `neurologic compromise` -> `nerve or muscle damage` | replace | - | - | - | - | - | - | - |

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
| `neurologic compromise` -> `nerve problems` | replace | attributed | 1.822 | 2.329 | 0.745 | 0.886 | 0.092 | - |

**edit `neurologic compromise` -> `nerve problems`**

- status: `attributed`
- log p full -0.8198, empty -2.6418
- masks scored: 66/66 (+2 top-k)
- ranked sources:
    - `+0.995` [readme] Neurologic: Having to do with nerves in the body, brain, or spinal cord.
    - `+0.902` [readme] NEUROLOGIC: Having to do with the nerves in the body, brain, or spinal cord.
    - `+0.509` [nih] neurologic: Having to do with nerves or the nervous system.
    - `+0.248` [wiktionary] compromise: Compromise is the act making this type of agreement.
    - `+0.140` [wiktionary] compromise: A compromise is an agreement in which everyone gets only some of what they wanted.

- rationale: "Neurologic compromise" refers to damage or dysfunction affecting the nervous system, and "nerve problems" conveys that same idea in everyday terms. Word frequency rises from Zipf 2.55 to 4.15, while age of acquisition drops from 13.85 to 9.67. This lets the reader grasp the core issue without needing clinical terminology.
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

**output:** After that, the numbing medicine was shot into the area around the lump.

| metric | value |
|---|---:|
| bertscore_f1 | 0.748 |
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
| nli_completeness | 0.428 |
| nli_faithfulness | 0.839 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.200 |
| sari | 42.76 |
| smog | 11.21 |
| smog_drop | 3.35 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `local anesthesia` -> `numbing medicine` | replace | - | - | - | - | - | - | - |
| `Thereafter` -> `shot` | replace | - | - | - | - | - | - | - |
| `tumor` -> `lump` | replace | - | - | - | - | - | - | - |

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
| `local anesthesia` -> `numbing drug` | replace | attributed | 5.930 | 6.753 | 0.912 | 0.723 | 1.327 | - |
| `tumor` -> `growth` | replace | attributed | 0.262 | 1.758 | 0.731 | 0.792 | 2.390 | - |

**edit `local anesthesia` -> `numbing drug`**

- status: `attributed`
- log p full -0.5775, empty -6.5076
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+2.917` [readme] local anesthesia: A drug that numbs a specific part of your body without affecting the rest.
    - `+1.590` [michigan] local anesthesia: A drug that causes only in the area of the body where the drug is put, as when a tooth is pu
    - `+0.960` [justplainclear] tumor: Growth or lump
    - `+0.415` [iowa] LOCAL ANESTHESIA: creation of insensitivity to pain in a small, local area of the body, usually by injection o
    - `+0.378` [dictionary] Thereafter (adv.): After that; afterward.

- rationale: The glossary explains that local anesthesia is a drug that numbs a specific part of your body, so "numbing drug" directly conveys that effect in simpler terms. Word frequency shifts from Zipf 3.39 to 2.90, while age of acquisition drops from 12.53 to 8.11. This lets the reader immediately grasp that the medication will block sensation in a targeted area.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `tumor` -> `growth`**

- status: `attributed`
- log p full -0.0644, empty -0.3263
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+2.833` [justplainclear] tumor: Growth or lump
    - `+0.442` [michigan] tumor: A growth or lump in your body. It may be cancer, but it also may not be cancer.
    - `+0.350` [thesaurus] tumor: growth, lump
    - `+0.276` [nih] tumor: An abnormal mass of tissue that results when cells divide more than they should or do not die when th
    - `+0.238` [michigan] local anesthesia: A drug that causes only in the area of the body where the drug is put, as when a tooth is pu

- rationale: A tumor is an abnormal mass of tissue, and calling it a "growth" conveys that same idea of something forming where it shouldn't. Word frequency rises from Zipf 3.97 to 5.03, and age of acquisition drops from 10.32 to 6.70. This lets the reader grasp the core concept without needing a clinical term.
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

**output:** I do not think she has a clear, active abscess right now, but there is some fluid coming out.

| metric | value |
|---|---:|
| bertscore_f1 | 0.625 |
| coleman_liau | 4.62 |
| coleman_liau_drop | 4.92 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.667 |
| fkgl | 6.10 |
| fkgl_drop | 1.51 |
| fre | 85.1 |
| fre_gain | 16.2 |
| human_edit_recall | 1.000 |
| length_ratio | 1.12 |
| n_words | 19.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.994 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 36.14 |
| severity_preservation | 0.000 |
| smog | 3.13 |
| smog_drop | 5.71 |

### Stage 4 - arm `termonly`

**output:** I do not think she has an obvious current pocket of pus, although there is some fluid leaking.

| metric | value |
|---|---:|
| bertscore_f1 | 0.863 |
| coleman_liau | 6.72 |
| coleman_liau_drop | 2.82 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.667 |
| fkgl | 7.82 |
| fkgl_drop | -0.21 |
| fre | 71.1 |
| fre_gain | 2.1 |
| human_edit_recall | 1.000 |
| length_ratio | 1.06 |
| n_words | 18.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.982 |
| nli_faithfulness | 0.954 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 69.74 |
| severity_preservation | 1.000 |
| smog | 8.84 |
| smog_drop | 0.00 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `abscessed lesion` -> `pocket of pus` | replace | - | - | - | - | - | - | - |
| `drainage` -> `fluid leaking` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** I do not think she has an obvious current pocket of infection, although there is some fluid leaking out.

| metric | value |
|---|---:|
| bertscore_f1 | 0.802 |
| coleman_liau | 8.28 |
| coleman_liau_drop | 1.25 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.667 |
| fkgl | 9.21 |
| fkgl_drop | -1.60 |
| fre | 62.9 |
| fre_gain | -6.1 |
| human_edit_recall | 1.000 |
| length_ratio | 1.12 |
| n_words | 19.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.977 |
| nli_faithfulness | 0.991 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 58.94 |
| severity_preservation | 1.000 |
| smog | 11.21 |
| smog_drop | -2.37 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `abscessed lesion` -> `pocket of infection` | replace | attributed | 0.839 | 1.713 | 0.584 | 0.818 | 0.038 | - |
| `drainage` -> `fluid leaking out` | replace | attributed | 1.781 | 3.138 | 0.669 | 0.848 | 1.209 | - |

**edit `abscessed lesion` -> `pocket of infection`**

- status: `attributed`
- log p full -0.3417, empty -1.1811
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.511` [iowa] LESION: wound or injury; a diseased patch of skin
    - `+0.473` [readme] lesion: It's any damage or abnormal change in tissue from disease or injury.
    - `+0.466` [nih] lesion: An area of abnormal tissue. A lesion may be benign (not cancer) or malignant (cancer).
    - `+0.313` [wiktionary] drainage: To use a drainage is engage in the action or process of draining something.
    - `+0.307` [readme] DRAINAGE: Fluid leaving an organ or body area.

- rationale: An abscessed lesion is a damaged area of tissue filled with pus, and calling it a "pocket of infection" conveys that same idea of a contained, infected space in everyday terms. Word frequency rises from Zipf 1.60 to 4.10, and age of acquisition drops from 12.82 to 8.05. This lets the reader immediately grasp that the problem is a localized infection without needing clinical vocabulary.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `drainage` -> `fluid leaking out`**

- status: `attributed`
- log p full -0.2532, empty -2.0340
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+1.469` [readme] drainage: When any fluid is leaking out of a body part.
    - `+0.260` [readme] lesion: It's any damage or abnormal change in tissue from disease or injury.
    - `+0.154` [readme] LESION: A lesion is a type of damage or change in tissue caused by disease or injury.
    - `-0.002` [michigan] lesion: A sore or any part of your sking that looks different from the rest.
    - `-0.041` [iowa] LESION: wound or injury; a diseased patch of skin

- rationale: The glossary defines drainage as when any fluid is leaking out of a body part, so "fluid leaking out" directly states that action in everyday terms. Word frequency moves slightly from Zipf 3.77 to 3.58, while age of acquisition drops from 10.84 to 7.94. This lets the reader picture the physical process without needing the clinical shorthand.
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

**output:** At this time, the care team would give the patient fluids through a vein and then check how she is doing.

| metric | value |
|---|---:|
| bertscore_f1 | 0.572 |
| coleman_liau | 5.71 |
| coleman_liau_drop | 6.38 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.333 |
| fkgl | 6.09 |
| fkgl_drop | 3.00 |
| fre | 88.8 |
| fre_gain | 39.3 |
| human_edit_recall | 1.000 |
| length_ratio | 1.62 |
| n_words | 21.0 |
| nli_completeness | 0.888 |
| nli_faithfulness | 0.486 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 30.25 |
| smog | 3.13 |
| smog_drop | 9.89 |

### Stage 4 - arm `termonly`

**output:** At this time, we would give fluids by vein to restore body water and check again.

| metric | value |
|---|---:|
| bertscore_f1 | 0.654 |
| coleman_liau | 5.55 |
| coleman_liau_drop | 6.54 |
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
| nli_completeness | 0.981 |
| nli_faithfulness | 0.945 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 43.48 |
| smog | 3.13 |
| smog_drop | 9.89 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `rehydrate` -> `give fluids by vein to restore body water` | replace | - | - | - | - | - | - | - |
| `reassess` -> `check again` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Right now, we would give fluids by vein to restore water and then check again.

| metric | value |
|---|---:|
| bertscore_f1 | 0.527 |
| coleman_liau | 6.20 |
| coleman_liau_drop | 5.89 |
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
| nli_completeness | 0.985 |
| nli_faithfulness | 0.951 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.250 |
| sari | 19.87 |
| smog | 3.13 |
| smog_drop | 9.89 |

annotation backend `novita`, 0 edits kept


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

**output:** The test results suggest the patient has acute appendicitis.

| metric | value |
|---|---:|
| bertscore_f1 | 0.354 |
| coleman_liau | 13.78 |
| coleman_liau_drop | 6.09 |
| copy_jargon_rate | 1.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 8.90 |
| fkgl_drop | 5.39 |
| fre | 47.3 |
| fre_gain | 44.0 |
| human_edit_recall | 0.000 |
| length_ratio | 1.00 |
| n_words | 9.0 |
| nli_completeness | 0.946 |
| nli_faithfulness | 0.857 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 8.91 |
| smog | 8.84 |
| smog_drop | 2.37 |
| temporality_preservation | 1.000 |
| uncertainty_preservation | 0.000 |

### Stage 4 - arm `termonly`

**output:** The test results point to a sudden swelling of the appendix.

| metric | value |
|---|---:|
| bertscore_f1 | 0.417 |
| coleman_liau | 7.35 |
| coleman_liau_drop | 12.52 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.286 |
| fkgl | 5.86 |
| fkgl_drop | 8.42 |
| fre | 72.6 |
| fre_gain | 69.3 |
| human_edit_recall | 1.000 |
| length_ratio | 1.22 |
| n_words | 11.0 |
| nli_completeness | 0.816 |
| nli_faithfulness | 0.665 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 15.15 |
| smog | 8.84 |
| smog_drop | 2.37 |
| temporality_preservation | 0.000 |
| uncertainty_preservation | 0.000 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `compatible with` -> `point to` | replace | - | - | - | - | - | - | - |
| `acute appendicitis` -> `sudden swelling of the appendix` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** The test results point to a sudden, painful swelling of the appendix.

| metric | value |
|---|---:|
| bertscore_f1 | 0.397 |
| coleman_liau | 8.80 |
| coleman_liau_drop | 11.07 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.286 |
| fkgl | 6.79 |
| fkgl_drop | 7.49 |
| fre | 67.8 |
| fre_gain | 64.4 |
| human_edit_recall | 1.000 |
| length_ratio | 1.33 |
| n_words | 12.0 |
| nli_completeness | 0.869 |
| nli_faithfulness | 0.713 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 14.66 |
| smog | 8.84 |
| smog_drop | 2.37 |
| temporality_preservation | 0.000 |
| uncertainty_preservation | 0.000 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `compatible with` -> `point to` | replace | attributed | 0.220 | 1.333 | 0.611 | 0.697 | 0.131 | - |
| `acute appendicitis` -> `sudden, painful swelling of the appendix` | replace | attributed | 6.236 | 6.897 | 0.480 | 0.769 | 0.446 | - |

**edit `compatible with` -> `point to`**

- status: `attributed`
- log p full -0.0923, empty -0.3124
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.541` [thesaurus] acute: sudden start, short term, quick
    - `+0.410` [justplainclear] acute: Sudden start, doesn't last long
    - `+0.254` [wiktionary] acute: If an angle is acute, it is less than 90 degrees in size.
    - `+0.150` [wiktionary] findings: A finding is the information from a research or an investigation.
    - `+0.114` [wiktionary] with: With is used to show the other people or things present when something happened.

- rationale: "Compatible with" means a finding fits or is consistent with a particular condition, and "point to" conveys that same idea of evidence suggesting a diagnosis in everyday words. Phrase frequency rises from Zipf 3.97 to 5.53, while age of acquisition drops from 10.16 to 4.55. Readers can now grasp that test results are indicating a possible cause without decoding a formal medical phrase.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `acute appendicitis` -> `sudden, painful swelling of the appendix`**

- status: `attributed`
- log p full -0.7264, empty -6.9629
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.977` [readme] appendicitis: Appendicitis is when your appendix gets swollen and inflamed, typically causing stomach pain.
    - `+0.531` [nih] acute: Symptoms or signs that begin and worsen quickly; not chronic.
    - `+0.284` [michigan] acute: An illness or symptom that begins suddenly or lasts a short time. It can also be an intense flare-up of

- rationale: The glossary explains that appendicitis means a swollen, inflamed appendix that causes stomach pain, so "sudden, painful swelling of the appendix" conveys that same meaning in everyday words. Word frequency rises from Zipf 2.74 to 3.22, and age of acquisition drops from 12.00 to 10.56. The reader can now grasp both the location and the nature of the problem without needing the clinical term.
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

**output:** She said she has not lost weight, but she has noticed a smaller appetite and more overall tiredness over the last 3 to 4 months.

| metric | value |
|---|---:|
| bertscore_f1 | 0.671 |
| coleman_liau | 6.68 |
| coleman_liau_drop | 9.56 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.286 |
| fkgl | 10.21 |
| fkgl_drop | 0.27 |
| fre | 66.4 |
| fre_gain | 16.2 |
| human_edit_recall | 1.000 |
| length_ratio | 1.39 |
| n_words | 25.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.994 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.250 |
| sari | 27.33 |
| smog | 13.02 |
| smog_drop | 0.00 |
| temporality_preservation | 0.000 |

### Stage 4 - arm `termonly`

**output:** She says she has not lost weight, but she agreed she has been less hungry and more tired all over for the past 3 to 4 months.

| metric | value |
|---|---:|
| bertscore_f1 | 0.615 |
| coleman_liau | 3.94 |
| coleman_liau_drop | 12.29 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.375 |
| fkgl | 8.49 |
| fkgl_drop | 1.99 |
| fre | 82.3 |
| fre_gain | 32.1 |
| human_edit_recall | 1.000 |
| length_ratio | 1.50 |
| n_words | 27.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.994 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.125 |
| sari | 35.57 |
| smog | 3.13 |
| smog_drop | 9.89 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `acknowledged` -> `agreed` | replace | - | - | - | - | - | - | - |
| `decreased appetite` -> `less hungry` | replace | - | - | - | - | - | - | - |
| `generalized fatigue` -> `more tired all over` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** She says she has not lost weight, but admitted she has been less hungry and more tired all over for the past 3 to 4 months.

| metric | value |
|---|---:|
| bertscore_f1 | 0.642 |
| coleman_liau | 4.48 |
| coleman_liau_drop | 11.76 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.375 |
| fkgl | 8.62 |
| fkgl_drop | 1.86 |
| fre | 79.6 |
| fre_gain | 29.3 |
| human_edit_recall | 1.000 |
| length_ratio | 1.44 |
| n_words | 26.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.995 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.125 |
| sari | 35.60 |
| smog | 8.84 |
| smog_drop | 4.18 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `acknowledged` -> `admitted` | replace | attributed | 2.271 | 3.271 | 0.707 | 0.914 | 2.742 | - |
| `decreased appetite` -> `less hungry` | replace | attributed | -0.040 | -0.564 | 0.378 | 0.849 | 0.373 | - |
| `generalized fatigue` -> `more tired all over` | replace | attributed | 0.068 | 0.519 | 0.832 | 0.932 | 1.824 | - |

**edit `acknowledged` -> `admitted`**

- status: `attributed`
- log p full -0.4199, empty -2.6913
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+3.297` [wiktionary] acknowledged: If you acknowledge a fact or a situation, you accept or admit that it is true or that it exists.
    - `+0.555` [nih] fatigue: A condition marked by extreme tiredness and inability to function due to lack of energy. Fatigue may 
    - `+0.263` [justplainclear] fatigue: Tired, weak feeling of the whole body, feeling tired
    - `+0.251` [wiktionary] fatigue: Fatigue is the material failure, such as cracking or separation, caused by stress on the material.
    - `+0.178` [readme] Generalized: Generalized means not focusing on one specific area.

- rationale: The source defines "acknowledged" as accepting that something is true, so "admitted" carries that same sense of conceding a fact in more familiar wording. Word frequency rises from Zipf 4.08 to 4.49, making the replacement noticeably more common. The reader now grasps the admission without the slightly more formal tone of the original term.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `decreased appetite` -> `less hungry`**

- status: `attributed`
- log p full -0.0956, empty -0.0555
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+1.245` [justplainclear] fatigue: Tired, weak feeling of the whole body, feeling tired
    - `+0.872` [wiktionary] appetite: When you have appetite, you feel hungry and would like to eat some food.
    - `+0.858` [nih] fatigue: A condition marked by extreme tiredness and inability to function due to lack of energy. Fatigue may 
    - `+0.467` [wiktionary] fatigue: Fatigue is the extreme tiredness which is the result of having mental or physical exertion or illness
    - `+0.431` [nih] appetite: A desire to satisfy a physical or mental need, such as for food, sex, or adventure.

- rationale: "Decreased appetite" means a reduced desire to eat, and "less hungry" conveys that same idea in everyday words. Phrase frequency rises from Zipf 3.63 to 4.41, while age of acquisition drops from 8.83 to 3.63. This lets the reader immediately grasp the symptom without needing to interpret clinical phrasing.
- audit: coverage 1.0, grounding_error=True, omission=False, source_ok=True, passage_ok=True

**edit `generalized fatigue` -> `more tired all over`**

- status: `attributed`
- log p full -0.1084, empty -0.1760
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+2.129` [michigan] fatigue: tired, weak feeling of the whole body, feeling tired all over
    - `+0.305` [nih] appetite: A desire to satisfy a physical or mental need, such as for food, sex, or adventure.
    - `+0.174` [justplainclear] fatigue: Tired, weak feeling of the whole body, feeling tired
    - `+0.020` [wiktionary] decreased: If something decreases, it goes down in number or value.

- rationale: "Generalized fatigue" refers to a sense of exhaustion felt throughout the body, and "more tired all over" conveys that same widespread weariness in everyday terms. Word frequency rises from Zipf 3.29 to 4.68, while age of acquisition drops from 11.83 to 5.57. This lets the reader grasp the full-body nature of the tiredness without needing clinical phrasing.
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

**output:** The doctor thought about whether the patient should have surgery to remove the rest of the thyroid gland.

| metric | value |
|---|---:|
| bertscore_f1 | 0.325 |
| coleman_liau | 10.59 |
| coleman_liau_drop | 17.57 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.333 |
| fkgl | 8.47 |
| fkgl_drop | 13.29 |
| fre | 66.4 |
| fre_gain | 118.4 |
| human_edit_recall | 1.000 |
| length_ratio | 2.00 |
| n_words | 18.0 |
| nli_completeness | 0.950 |
| nli_faithfulness | 0.273 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 32.65 |
| smog | 8.84 |
| smog_drop | 4.18 |
| uncertainty_preservation | 0.000 |

### Stage 4 - arm `termonly`

**output:** The doctors thought about removing the rest of the thyroid.

| metric | value |
|---|---:|
| bertscore_f1 | 0.440 |
| coleman_liau | 9.66 |
| coleman_liau_drop | 18.50 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.286 |
| fkgl | 6.01 |
| fkgl_drop | 15.75 |
| fre | 69.8 |
| fre_gain | 121.8 |
| human_edit_recall | 1.000 |
| length_ratio | 1.11 |
| n_words | 10.0 |
| nli_completeness | 0.944 |
| nli_faithfulness | 0.440 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 28.37 |
| smog | 8.84 |
| smog_drop | 4.18 |
| uncertainty_preservation | 0.000 |

annotation backend `novita`, 0 edits kept


### Stage 4 - arm `grounded`

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

**output:** She says she had a nosebleed a few days ago that needed packing in her nose, and luckily it has stopped now.

| metric | value |
|---|---:|
| bertscore_f1 | 0.704 |
| coleman_liau | 5.26 |
| coleman_liau_drop | 5.16 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.400 |
| fkgl | 8.01 |
| fkgl_drop | 2.44 |
| fre | 76.8 |
| fre_gain | 22.9 |
| human_edit_recall | 1.000 |
| length_ratio | 1.05 |
| n_words | 22.0 |
| nli_completeness | 0.951 |
| nli_faithfulness | 0.973 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 30.86 |
| smog | 8.84 |
| smog_drop | 2.37 |
| temporality_preservation | 1.000 |

### Stage 4 - arm `termonly`

**output:** She says she had a nosebleed a few days ago that needed gauze put in her nose, and luckily that has stopped now.

| metric | value |
|---|---:|
| bertscore_f1 | 0.695 |
| coleman_liau | 5.10 |
| coleman_liau_drop | 5.32 |
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
| nli_completeness | 0.929 |
| nli_faithfulness | 0.956 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.286 |
| sari | 30.04 |
| smog | 8.84 |
| smog_drop | 2.37 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `epistaxis` -> `nosebleed` | replace | - | - | - | - | - | - | - |
| `nasal packing` -> `gauze put in her nose` | replace | - | - | - | - | - | - | - |
| `resolved` -> `stopped` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** She says she had a nosebleed a few days ago, needed something put in her nose to stop it, and luckily that has healed now.

| metric | value |
|---|---:|
| bertscore_f1 | 0.692 |
| coleman_liau | 5.06 |
| coleman_liau_drop | 5.37 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.667 |
| fkgl | 8.79 |
| fkgl_drop | 1.66 |
| fre | 76.6 |
| fre_gain | 22.6 |
| human_edit_recall | 1.000 |
| length_ratio | 1.19 |
| n_words | 25.0 |
| nli_completeness | 0.962 |
| nli_faithfulness | 0.954 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.286 |
| sari | 29.58 |
| smog | 8.84 |
| smog_drop | 2.37 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `epistaxis` -> `nosebleed` | replace | attributed | 0.001 | 4.373 | 0.671 | 0.691 | 0.502 | - |
| `nasal packing` -> `something put in her nose to stop it` | replace | attributed | 5.862 | 5.979 | 0.503 | 0.696 | 0.010 | - |
| `resolved` -> `healed` | replace | attributed | 0.323 | 0.585 | 0.665 | 0.930 | 0.609 | - |

**edit `epistaxis` -> `nosebleed`**

- status: `attributed`
- log p full -0.0000, empty -0.0013
- masks scored: 66/66 (+5 top-k)
- ranked sources:
    - `+2.308` [readme] Epistaxis: A nosebleed.
    - `+1.806` [readme] EPISTAXIS: EPISTAXIS: It's a nosebleed.
    - `+0.743` [wiktionary] requiring: If you require something, you need it.
    - `+0.637` [wiktionary] resolved: When a problem is resolved, it has been brought to a successful solution.
    - `+0.602` [wiktionary] epistaxis: Epistaxis is bleeding from the nose.

- rationale: Epistaxis refers to bleeding from the nose, so replacing it with "nosebleed" directly names the condition in everyday language. Word frequency rises from Zipf 1.60 to 2.51, making the replacement much more familiar. The reader can now immediately recognize the symptom without encountering an unfamiliar medical term.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `nasal packing` -> `something put in her nose to stop it`**

- status: `attributed`
- log p full -2.1954, empty -8.0572
- masks scored: 66/66 (+5 top-k)
- ranked sources:
    - `+0.882` [readme] packing: Putting something into a wound to help it heal.
    - `+0.872` [readme] EPISTAXIS: EPISTAXIS: It's a nosebleed.
    - `+0.465` [readme] nasal: It's all about your nose when we talk about "nasal."
    - `+0.056` [wiktionary] resolved: To resolve means to create a solution for a problem.

- rationale: Nasal packing refers to material placed inside the nostril to control bleeding, and the replacement plainly describes that action and its purpose. Word frequency rises from Zipf 3.39 to 4.42, while age of acquisition drops from 8.75 to 5.09. The reader can now grasp the procedure without needing to know the clinical term.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `resolved` -> `healed`**

- status: `attributed`
- log p full -0.6532, empty -0.9760
- masks scored: 66/66 (+5 top-k)
- ranked sources:
    - `+1.063` [readme] packing: Putting something into a wound to help it heal.
    - `+0.454` [wiktionary] resolved: To resolve means to create a solution for a problem.
    - `+0.107` [wiktionary] packing: You put packing around an object to protect it.
    - `+0.035` [wiktionary] epistaxis: Epistaxis is bleeding from the nose.

- rationale: "Resolved" means that a condition has cleared up or gone away, so "healed" conveys that same sense of recovery in a simpler word. Word frequency moves from Zipf 4.10 to 3.66, and the syllable count drops from two to one. The reader can now grasp the positive outcome without needing a more formal medical term.
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

**output:** I also told the patient about conscious sedation, which is medicine that helps a person stay calm and relaxed during a procedure.

| metric | value |
|---|---:|
| bertscore_f1 | 0.594 |
| coleman_liau | 10.80 |
| coleman_liau_drop | 1.04 |
| copy_jargon_rate | 1.000 |
| critical_error | 0.000 |
| fkgl | 11.76 |
| fkgl_drop | -2.86 |
| fre | 49.9 |
| fre_gain | 2.6 |
| human_edit_recall | 0.000 |
| length_ratio | 2.44 |
| n_words | 22.0 |
| nli_completeness | 0.993 |
| nli_faithfulness | 0.003 |
| replacement_f1 | 0.000 |
| rewrite_aggressiveness | 1.000 |
| sari | 13.30 |
| smog | 13.02 |
| smog_drop | -4.18 |

### Stage 4 - arm `termonly`

**output:** I also explained to the patient about medicine to make her relaxed and sleepy.

| metric | value |
|---|---:|
| bertscore_f1 | 0.672 |
| coleman_liau | 8.60 |
| coleman_liau_drop | 3.24 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 8.41 |
| fkgl_drop | 0.48 |
| fre | 59.7 |
| fre_gain | 12.4 |
| human_edit_recall | 1.000 |
| length_ratio | 1.56 |
| n_words | 14.0 |
| nli_completeness | 0.573 |
| nli_faithfulness | 0.419 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 61.94 |
| smog | 8.84 |
| smog_drop | 0.00 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `conscious sedation` -> `medicine to make her relaxed and sleepy` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** I also explained to the patient about getting medicine to make them sleepy but still able to wake up.

| metric | value |
|---|---:|
| bertscore_f1 | 0.587 |
| coleman_liau | 7.67 |
| coleman_liau_drop | 4.17 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 9.21 |
| fkgl_drop | -0.31 |
| fre | 62.9 |
| fre_gain | 15.6 |
| human_edit_recall | 1.000 |
| length_ratio | 2.11 |
| n_words | 19.0 |
| nli_completeness | 0.662 |
| nli_faithfulness | 0.054 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 61.94 |
| smog | 8.84 |
| smog_drop | 0.00 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `conscious sedation` -> `getting medicine to make them sleepy but still able to wake up` | replace | attributed | 16.878 | 16.915 | - | 1.000 | 9.554 | - |

**edit `conscious sedation` -> `getting medicine to make them sleepy but still able to wake up`**

- status: `attributed`
- log p full -3.2999, empty -20.1777
- masks scored: 6/6 (+1 top-k)
- ranked sources:
    - `+11.834` [nih] conscious sedation: A level of sedation in which a person is asleep but wakes when spoken to or touched. Consc
    - `+2.280` [readme] conscious sedation: Medication given to a patient to make them lightly sedated and forgetful during a procedur

- rationale: Conscious sedation means using medication to keep a person relaxed and drowsy yet responsive, and the replacement explains this by describing the medicine’s effect in everyday terms. Phrase frequency rises from Zipf 2.93 to 3.59, while age of acquisition drops from 13.20 to 7.79. The reader can now grasp the procedure’s purpose without needing clinical vocabulary.
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

**output:** Palpation of her right knee shows no crepitus.

| metric | value |
|---|---:|
| bertscore_f1 | 0.552 |
| coleman_liau | 8.05 |
| coleman_liau_drop | 1.45 |
| copy_jargon_rate | 1.000 |
| critical_error | 0.000 |
| fkgl | 3.76 |
| fkgl_drop | 1.48 |
| fre | 82.4 |
| fre_gain | 10.6 |
| human_edit_recall | 0.000 |
| laterality_preservation | 1.000 |
| length_ratio | 0.89 |
| n_words | 8.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.993 |
| nli_faithfulness | 0.994 |
| replacement_f1 | 0.000 |
| rewrite_aggressiveness | 1.000 |
| sari | 25.06 |
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

**output:** Feeling her right knee finds no grinding or crackling.

| metric | value |
|---|---:|
| bertscore_f1 | 0.619 |
| coleman_liau | 9.91 |
| coleman_liau_drop | -0.41 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 3.65 |
| fkgl_drop | 1.58 |
| fre | 84.9 |
| fre_gain | 13.1 |
| human_edit_recall | 1.000 |
| laterality_preservation | 1.000 |
| length_ratio | 1.00 |
| n_words | 9.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.932 |
| nli_faithfulness | 0.865 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 31.31 |
| smog | 3.13 |
| smog_drop | 5.71 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `crepitus` -> `grinding or crackling` | replace | attributed | 0.183 | 0.217 | - | 0.657 | 0.400 | - |

**edit `crepitus` -> `grinding or crackling`**

- status: `attributed`
- log p full -1.7564, empty -1.9392
- masks scored: 34/34 (+2 top-k)
- ranked sources:
    - `+0.400` [dictionary] Crepitus (n.): Same as Crepitation, 2.
    - `-0.392` [dictionary] Crepitus (n.): The noise produced by a sudden discharge of wind from the bowels.

- rationale: Crepitus refers to the grating sensation or sound from bones or joints rubbing together, so "grinding or crackling" directly conveys that same physical experience in familiar words. Word frequency rises from Zipf 1.39 to 2.87, making the replacement much more commonly encountered. The reader can now recognize the symptom being described without needing a specialized medical term.
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

**output:** She talked about her ideas, concerns, and expectations the night before, and she twisted her ankle.

| metric | value |
|---|---:|
| bertscore_f1 | 0.442 |
| coleman_liau | 11.35 |
| coleman_liau_drop | 0.98 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.333 |
| fkgl | 9.82 |
| fkgl_drop | 0.27 |
| fre | 53.1 |
| fre_gain | 5.5 |
| length_ratio | 1.45 |
| n_words | 16.0 |
| nli_completeness | 0.864 |
| nli_faithfulness | 0.932 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 18.55 |
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
| `the evening prior` -> `the night before` | replace | attributed | -0.102 | -1.608 | - | 0.571 | 0.203 | - |

**edit `the evening prior` -> `the night before`**

- status: `attributed`
- log p full -0.1298, empty -0.0274
- masks scored: 10/10 (+2 top-k)
- ranked sources:
    - `-0.486` [wiktionary] evening: You use even to focus on the most surprising or unlikely case.
    - `-0.689` [wiktionary] evening: Period from dusk to midnight.
    - `-1.548` [wiktionary] prior: If something happens prior to something else, it happens before it.

- rationale: "The evening prior" refers to the day before an event, and "the night before" conveys the same timeframe in more familiar, everyday terms. Word frequency rises from Zipf 4.55 to 5.44, and age of acquisition drops from 10.63 to 5.45. This lets the reader grasp the timing instantly, without pausing over a slightly formal phrase.
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

**output:** The patient's condition gets worse when she throws.

| metric | value |
|---|---:|
| bertscore_f1 | 0.442 |
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
| nli_completeness | 0.849 |
| nli_faithfulness | 0.941 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.250 |
| sari | 26.63 |
| smog | 8.84 |
| smog_drop | 4.18 |

### Stage 4 - arm `termonly`

**output:** Things that change the condition: The patient's condition gets worse from throwing.

| metric | value |
|---|---:|
| bertscore_f1 | 0.440 |
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
| nli_faithfulness | 0.991 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 27.69 |
| smog | 11.21 |
| smog_drop | 1.82 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `aggravated` -> `worse` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Things that change the problem: The patient's condition gets worse from throwing.

| metric | value |
|---|---:|
| bertscore_f1 | 0.408 |
| coleman_liau | 14.12 |
| coleman_liau_drop | 2.24 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.750 |
| fkgl | 5.81 |
| fkgl_drop | 8.34 |
| fre | 74.8 |
| fre_gain | 65.1 |
| human_edit_recall | 1.000 |
| length_ratio | 1.30 |
| n_words | 13.0 |
| nli_completeness | 0.978 |
| nli_faithfulness | 0.984 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 27.50 |
| smog | 8.84 |
| smog_drop | 4.18 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `aggravated` -> `worse` | replace | attributed | 0.000 | 1.476 | - | 0.578 | 0.927 | - |

**edit `aggravated` -> `worse`**

- status: `attributed`
- log p full -0.0000, empty -0.0000
- masks scored: 18/18 (+2 top-k)
- ranked sources:
    - `+0.945` [wiktionary] modifying: If you modify something, you change it, often only in small ways, and often because you want to use
    - `+0.018` [wiktionary] factors: A factor is one of a number of things that causes a result.
    - `-0.444` [wiktionary] aggravated: To aggravate is to make something worse.
    - `-0.517` [readme] aggravated: To make a problem or injury worse.

- rationale: "Aggravated" means made more severe or intense, so "worse" directly conveys that idea of increased severity in simpler terms. Word frequency rises from Zipf 3.47 to 4.89, making the replacement much more common. The reader can now grasp the change in condition without needing to parse a less familiar, multi-syllable word.
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

**output:** She has a history of joint wear-and-tear, weak bones, an underactive thyroid, nose allergies, and hard deposits in the kidneys.

| metric | value |
|---|---:|
| bertscore_f1 | 0.385 |
| coleman_liau | 12.01 |
| coleman_liau_drop | 15.63 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 10.50 |
| fkgl_drop | 10.85 |
| fre | 55.4 |
| fre_gain | 95.6 |
| human_edit_recall | 1.000 |
| length_ratio | 1.69 |
| n_words | 22.0 |
| nli_completeness | 0.900 |
| nli_faithfulness | 0.945 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 41.87 |
| smog | 14.55 |
| smog_drop | 1.35 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 5 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `osteoarthritis` -> `joint wear-and-tear` | replace | - | - | - | - | - | - | - |
| `osteoporosis` -> `weak bones` | replace | - | - | - | - | - | - | - |
| `hypothyroidism` -> `an underactive thyroid` | replace | - | - | - | - | - | - | - |
| `allergic rhinitis` -> `nose allergies` | replace | - | - | - | - | - | - | - |
| `kidney stones` -> `hard deposits in the kidneys` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** She has a history of joint wear-and-tear arthritis, weak bones, an underactive thyroid, hay fever, and hard mineral deposits in the kidneys.

| metric | value |
|---|---:|
| bertscore_f1 | 0.451 |
| coleman_liau | 12.38 |
| coleman_liau_drop | 15.26 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 12.30 |
| fkgl_drop | 9.05 |
| fre | 46.1 |
| fre_gain | 86.3 |
| human_edit_recall | 1.000 |
| length_ratio | 1.85 |
| n_words | 24.0 |
| nli_completeness | 0.922 |
| nli_faithfulness | 0.834 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 47.07 |
| smog | 15.90 |
| smog_drop | 0.00 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 5 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `osteoarthritis` -> `joint wear-and-tear arthritis` | replace | failed | - | - | - | - | - | - |
| `osteoporosis` -> `weak bones` | replace | failed | - | - | - | - | - | - |
| `hypothyroidism` -> `an underactive thyroid` | replace | failed | - | - | - | - | - | - |
| `allergic rhinitis` -> `hay fever` | replace | failed | - | - | - | - | - | - |
| `kidney stones` -> `hard mineral deposits in the kidneys` | replace | failed | - | - | - | - | - | - |

**edit `osteoarthritis` -> `joint wear-and-tear arthritis`**

- status: `failed` - full or empty boundary score failed
- log p full -10000.0000, empty -6.5559
- masks scored: 52/66 (+0 top-k)

- rationale: Osteoarthritis refers to the gradual breakdown of cartilage in a joint, and "joint wear-and-tear arthritis" conveys that same process of physical deterioration in everyday terms. Word frequency rises from Zipf 2.76 to 3.49, making the replacement more familiar. The reader can now grasp the condition as a straightforward mechanical problem rather than an obscure medical label.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `osteoporosis` -> `weak bones`**

- status: `failed` - full or empty boundary score failed
- log p full -10000.0000, empty -0.2130
- masks scored: 52/66 (+0 top-k)

- rationale: Osteoporosis means a condition where bones lose density and become fragile, so calling it "weak bones" directly conveys that same idea in everyday terms. Word frequency rises from Zipf 2.99 to 4.16, and age of acquisition drops from 14.29 to 5.58. A reader can now immediately grasp the core problem without needing to decode a clinical label.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `hypothyroidism` -> `an underactive thyroid`**

- status: `failed` - full or empty boundary score failed
- log p full -10000.0000, empty -0.2165
- masks scored: 52/66 (+0 top-k)

- rationale: Hypothyroidism means the thyroid gland does not produce enough hormones, so "an underactive thyroid" conveys that same idea in everyday words. Word frequency drops from Zipf 2.68 to 1.67, while age of acquisition improves from 15.43 to 13.83. This lets the reader grasp the condition without needing to decode a clinical term.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `allergic rhinitis` -> `hay fever`**

- status: `failed` - full or empty boundary score failed
- log p full -10000.0000, empty -1.2072
- masks scored: 52/66 (+0 top-k)

- rationale: Allergic rhinitis refers to a nasal inflammation triggered by allergens, and "hay fever" conveys this same idea using a widely recognized common name. Word frequency rises from Zipf 2.37 to 3.74, and age of acquisition drops from 18.07 to 5.84. The reader can immediately connect the condition to familiar seasonal allergy symptoms without needing clinical terminology.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `kidney stones` -> `hard mineral deposits in the kidneys`**

- status: `failed` - full or empty boundary score failed
- log p full -10000.0000, empty -5.4003
- masks scored: 52/66 (+0 top-k)

- rationale: Kidney stones are solid masses that form from crystals in the urine, so calling them "hard mineral deposits in the kidneys" explains their physical nature and location directly. Word frequency drops from Zipf 3.85 to 3.28, while age of acquisition improves from 9.33 to 8.67. A reader can now grasp the condition without needing to know the medical shorthand.
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

### Stage 4 - arm `termonly`

**output:** The ultrasound found no bleeding inside the skull.

| metric | value |
|---|---:|
| bertscore_f1 | 0.768 |
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
| nli_completeness | 0.930 |
| nli_faithfulness | 0.932 |
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

**output:** The ultrasound found no bleeding inside the brain.

| metric | value |
|---|---:|
| bertscore_f1 | 0.818 |
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
| nli_completeness | 0.934 |
| nli_faithfulness | 0.960 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 28.10 |
| smog | 8.84 |
| smog_drop | 5.71 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `intracranial hemorrhage` -> `bleeding inside the brain` | replace | attributed | 3.298 | 3.784 | - | 0.800 | 2.561 | - |

**edit `intracranial hemorrhage` -> `bleeding inside the brain`**

- status: `attributed`
- log p full -0.9325, empty -4.2309
- masks scored: 6/6 (+1 top-k)
- ranked sources:
    - `+3.451` [readme] INTRACRANIAL HEMORRHAGE: Bleeding inside your brain.
    - `+0.890` [readme] intracranial hemorrhage: Bleeding within the brain.

- rationale: The original term refers to a dangerous condition where a blood vessel ruptures within the skull, and "bleeding inside the brain" conveys that same critical event in everyday words. Word frequency rises sharply from Zipf 2.55 to 4.00, while age of acquisition drops from 14.94 to 5.76. This change lets the reader immediately grasp a life-threatening emergency without needing to decode complex medical terminology.
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

**output:** He had surgery to remove his appendix through small cuts in his belly, and he is able to eat food by mouth without problems.

| metric | value |
|---|---:|
| bertscore_f1 | 0.433 |
| coleman_liau | 6.89 |
| coleman_liau_drop | 6.26 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.333 |
| fkgl | 10.00 |
| fkgl_drop | 4.66 |
| fre | 66.2 |
| fre_gain | 54.8 |
| human_edit_recall | 1.000 |
| length_ratio | 1.60 |
| n_words | 24.0 |
| nli_completeness | 0.919 |
| nli_faithfulness | 0.252 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 34.97 |
| smog | 11.21 |
| smog_drop | 1.82 |
| temporality_preservation | 0.000 |

### Stage 4 - arm `termonly`

**output:** He had surgery to remove his appendix through small cuts, and he is able to eat food by mouth without problems.

| metric | value |
|---|---:|
| bertscore_f1 | 0.463 |
| coleman_liau | 7.37 |
| coleman_liau_drop | 5.78 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.333 |
| fkgl | 8.90 |
| fkgl_drop | 5.76 |
| fre | 68.7 |
| fre_gain | 57.3 |
| human_edit_recall | 1.000 |
| length_ratio | 1.40 |
| n_words | 21.0 |
| nli_completeness | 0.926 |
| nli_faithfulness | 0.541 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 35.43 |
| smog | 11.21 |
| smog_drop | 1.82 |
| temporality_preservation | 0.000 |

annotation backend `novita`, 0 edits kept


### Stage 4 - arm `grounded`

**output:** He had surgery to remove his appendix through small cuts, and he is handling food by mouth.

| metric | value |
|---|---:|
| bertscore_f1 | 0.529 |
| coleman_liau | 7.36 |
| coleman_liau_drop | 5.79 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.333 |
| fkgl | 7.00 |
| fkgl_drop | 7.65 |
| fre | 75.1 |
| fre_gain | 63.8 |
| human_edit_recall | 1.000 |
| length_ratio | 1.13 |
| n_words | 17.0 |
| nli_completeness | 0.926 |
| nli_faithfulness | 0.829 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 36.28 |
| smog | 11.21 |
| smog_drop | 1.82 |
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

**output:** We think the fluid buildup in her brain is probably not affecting her walking.

| metric | value |
|---|---:|
| bertscore_f1 | 0.788 |
| coleman_liau | 8.60 |
| coleman_liau_drop | 2.07 |
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
| nli_completeness | 0.891 |
| nli_faithfulness | 0.754 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.833 |
| sari | 14.28 |
| smog | 11.21 |
| smog_drop | 0.00 |
| uncertainty_preservation | 1.000 |

### Stage 4 - arm `termonly`

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
| `hydrocephalus` -> `fluid buildup in her brain` | replace | - | - | - | - | - | - | - |

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
| `hydrocephalus` -> `fluid buildup in her brain` | replace | attributed | 0.214 | 0.475 | - | 0.609 | 0.491 | - |

**edit `hydrocephalus` -> `fluid buildup in her brain`**

- status: `attributed`
- log p full -0.5006, empty -0.7151
- masks scored: 18/18 (+2 top-k)
- ranked sources:
    - `+1.696` [nih] hydrocephalus: The abnormal buildup of cerebrospinal fluid in the ventricles of the brain.
    - `+1.206` [readme] HYDROCEPHALUS: When fluid around the brain builds up too much.
    - `+0.381` [justplainclear] hydrocephalus: Also known as: water on the brain A condition where there is too much cerebrospinal fluid in yo
    - `-1.186` [readme] hydrocephalus: Swelling of brain due to excess fluid.

- rationale: Hydrocephalus refers to an abnormal accumulation of cerebrospinal fluid within the brain, so "fluid buildup in her brain" conveys that same condition in everyday terms. Word frequency rises from Zipf 2.32 to 3.30, and age of acquisition drops from 15.78 to 9.63. This lets the reader grasp the essential medical problem without needing to decode a specialized term.
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

**output:** She said she felt very tired, dizzy, and had serious trouble breathing when she was active.

| metric | value |
|---|---:|
| bertscore_f1 | 0.530 |
| coleman_liau | 8.81 |
| coleman_liau_drop | 8.55 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.300 |
| fkgl | 8.35 |
| fkgl_drop | 3.95 |
| fre | 63.7 |
| fre_gain | 37.2 |
| human_edit_recall | 1.000 |
| length_ratio | 1.07 |
| n_words | 16.0 |
| nli_completeness | 0.992 |
| nli_faithfulness | 0.984 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.143 |
| sari | 23.12 |
| severity_downgrade | 0.000 |
| severity_preservation | 0.000 |
| severity_tier_input | 3.000 |
| severity_tier_output | 3.000 |
| smog | 8.84 |
| smog_drop | 4.18 |

### Stage 4 - arm `termonly`

**output:** She said she felt tired, dizzy, and very short of breath when active.

| metric | value |
|---|---:|
| bertscore_f1 | 0.652 |
| coleman_liau | 6.02 |
| coleman_liau_drop | 11.35 |
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
| nli_completeness | 0.990 |
| nli_faithfulness | 0.992 |
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
| `fatigue` -> `tired` | replace | - | - | - | - | - | - | - |
| `lightheadedness` -> `dizzy` | replace | - | - | - | - | - | - | - |
| `dyspnea on exertion` -> `very short of breath when active` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** She said she felt very tired, dizzy, and had severe trouble breathing when she worked hard.

| metric | value |
|---|---:|
| bertscore_f1 | 0.553 |
| coleman_liau | 8.81 |
| coleman_liau_drop | 8.55 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.300 |
| fkgl | 6.88 |
| fkgl_drop | 5.42 |
| fre | 74.3 |
| fre_gain | 47.8 |
| human_edit_recall | 1.000 |
| length_ratio | 1.07 |
| n_words | 16.0 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.989 |
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

annotation backend `novita`, 4 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `noted complaints of` -> `said she felt` | replace | attributed | 0.108 | 0.247 | 0.193 | 0.848 | 0.011 | - |
| `fatigue` -> `tired` | replace | attributed | 0.000 | 0.747 | 0.543 | 0.940 | 0.710 | - |
| `lightheadedness` -> `dizzy` | replace | attributed | 0.012 | 0.776 | 0.557 | 0.762 | 0.224 | - |
| `dyspnea on exertion` -> `trouble breathing when she worked hard` | replace | attributed | 13.080 | 13.298 | 0.607 | 0.712 | 1.997 | - |

**edit `noted complaints of` -> `said she felt`**

- status: `attributed`
- log p full -0.5241, empty -0.6323
- masks scored: 66/66 (+7 top-k)
- ranked sources:
    - `+0.367` [wiktionary] on: positioned at the upper surface of, touching from above
    - `+0.356` [wiktionary] complaints: A complaint is an expression of dissatisfaction
    - `+0.330` [readme] lightheadedness: Feeling dizzy or almost faint.
    - `+0.158` [wiktionary] exertion: An exertion is the expenditure of physical or mental effort.
    - `+0.095` [readme] fatigue: Feeling exhausted and lacking energy.

- rationale: "Noted complaints of" is a clinical way of recording what a patient reported, and "said she felt" conveys that same act of reporting in everyday speech. Phrase frequency rises from Zipf 4.10 to 5.05, while syllable count drops from 5 to 3. The reader can now grasp the patient's own account without navigating formal medical phrasing.
- audit: coverage 0.5, grounding_error=True, omission=False, source_ok=True, passage_ok=True

**edit `fatigue` -> `tired`**

- status: `attributed`
- log p full -0.0000, empty -0.0000
- masks scored: 66/66 (+7 top-k)
- ranked sources:
    - `+2.223` [nih] fatigue: A condition marked by extreme tiredness and inability to function due to lack of energy. Fatigue may 
    - `+1.513` [readme] lightheadedness: Feeling dizzy or almost faint.
    - `+1.334` [readme] dyspnea: Having a hard time breathing or feeling like you can't catch your breath.
    - `+1.228` [michigan] exertion: Effort or work.
    - `+1.130` [wiktionary] noted: If somebody is a noted person, they are well known.

- rationale: Fatigue means a state of extreme physical or mental exhaustion, and "tired" conveys that same sense of being drained in a more everyday word. Word frequency rises from Zipf 3.86 to 4.71, and age of acquisition drops from 11.83 to 4.62. The reader can now immediately recognize the symptom without needing to interpret a more formal clinical term.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `lightheadedness` -> `dizzy`**

- status: `attributed`
- log p full -0.0099, empty -0.0214
- masks scored: 66/66 (+7 top-k)
- ranked sources:
    - `+1.335` [nih] fatigue: A condition marked by extreme tiredness and inability to function due to lack of energy. Fatigue may 
    - `+1.111` [wiktionary] noted: If somebody is a noted person, they are well known.
    - `+0.427` [readme] Complaints: A problem or sickness that a person talks about.
    - `+0.161` [michigan] exertion: Effort or work.
    - `+0.104` [wiktionary] on: positioned at the upper surface of, touching from above

- rationale: Lightheadedness refers to a sensation of feeling faint or about to pass out, and "dizzy" captures that same unsteady, woozy feeling in a more familiar word. Word frequency rises from Zipf 1.92 to 3.43, and age of acquisition drops from 10.11 to 5.50. This swap lets the reader immediately recognize the symptom without needing to parse a less common term.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `dyspnea on exertion` -> `trouble breathing when she worked hard`**

- status: `attributed`
- log p full -1.6300, empty -14.7102
- masks scored: 66/66 (+7 top-k)
- ranked sources:
    - `+4.401` [michigan] exertion: Effort or work.
    - `+2.404` [thesaurus] exertion: effort, work
    - `+1.096` [readme] Dyspnea: Struggling to breathe, feeling out of breath.
    - `+0.980` [readme] lightheadedness: Feeling dizzy or almost faint.
    - `+0.166` [wiktionary] on: positioned at the upper surface of, touching from above

- rationale: The Michigan glossary defines dyspnea on exertion as effort or work, so "trouble breathing when she worked hard" conveys that breathlessness tied to activity in everyday terms. Phrase frequency rises sharply from Zipf 2.09 to 4.10, and age of acquisition drops from 11.58 to 4.56. The reader can now grasp the symptom as a familiar experience rather than a clinical label.
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

**output:** There was no major swelling on the back of the hand linked to these.

| metric | value |
|---|---:|
| bertscore_f1 | 0.637 |
| coleman_liau | 4.46 |
| coleman_liau_drop | 4.56 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.667 |
| fkgl | 3.36 |
| fkgl_drop | 7.59 |
| fre | 95.9 |
| fre_gain | 54.4 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 14.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.928 |
| nli_faithfulness | 0.926 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 36.58 |
| severity_downgrade | 1.000 |
| severity_preservation | 0.000 |
| severity_tier_input | 2.000 |
| smog | 3.13 |
| smog_drop | 9.89 |

### Stage 4 - arm `termonly`

**output:** There is no large swelling on the back of the hand with these.

| metric | value |
|---|---:|
| bertscore_f1 | 0.647 |
| coleman_liau | 3.78 |
| coleman_liau_drop | 5.23 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 2.19 |
| fkgl_drop | 8.75 |
| fre | 102.5 |
| fre_gain | 61.0 |
| human_edit_recall | 1.000 |
| length_ratio | 0.93 |
| n_words | 13.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.949 |
| nli_faithfulness | 0.906 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 40.41 |
| severity_downgrade | 0.000 |
| severity_preservation | 1.000 |
| severity_tier_input | 2.000 |
| severity_tier_output | 2.000 |
| smog | 3.13 |
| smog_drop | 9.89 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `significant amount` -> `large` | replace | - | - | - | - | - | - | - |
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
| `significant amount` -> `big` | replace | attributed | 1.696 | 1.979 | 0.711 | 0.804 | 0.467 | - |
| `associated with` -> `linked to` | replace | attributed | 0.528 | 2.504 | 0.510 | 0.847 | 0.246 | - |
| `dorsum` -> `back` | replace | attributed | 0.014 | 5.390 | 0.705 | 0.941 | 4.014 | - |

**edit `significant amount` -> `big`**

- status: `attributed`
- log p full -1.2536, empty -2.9498
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+1.640` [michigan] significant: Big or important.
    - `+1.173` [justplainclear] significant: Big, serious, important, major
    - `+0.360` [readme] edema: Swelling due to too much fluid in the body tissues.
    - `+0.337` [readme] Associated with: Connected with something.
    - `+0.196` [justplainclear] amount: How much or how many

- rationale: The Michigan glossary defines "significant amount" as something big or important, so "big" directly conveys that core idea in a simpler word. Word frequency rises from Zipf 4.75 to 5.67, and age of acquisition drops from 9.89 to 2.89. The reader can now instantly grasp the scale without processing a more formal, multi-syllable phrase.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `associated with` -> `linked to`**

- status: `attributed`
- log p full -0.0640, empty -0.5923
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+1.606` [justplainclear] associated with: Linked to, related to, goes along with, is part of
    - `+1.361` [readme] associated with: Linked to something.
    - `+0.657` [michigan] significant: Big or important.
    - `+0.600` [readme] Associated with: Connected with something.
    - `+0.577` [justplainclear] significant: Big, serious, important, major

- rationale: The original phrase signals a connection between two things, and "linked to" conveys that same relationship in more direct, everyday words. Word frequency moves from Zipf 4.89 to 4.54, while age of acquisition drops from 4.44 to 3.95. The reader now encounters a familiar, shorter expression that makes the connection immediately clear.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `dorsum` -> `back`**

- status: `attributed`
- log p full -0.0001, empty -0.0142
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+4.402` [readme] dorsum: The dorsum is basically the back or upper surface.
    - `+0.388` [readme] edema: Swelling due to too much fluid in the body tissues.
    - `+0.368` [readme] associated with: Linked to something.
    - `+0.196` [wiktionary] significant: If something is significant, it is important, or large, enough to pay attention to or to believe.
    - `+0.135` [justplainclear] associated with: Linked to, related to, goes along with, is part of

- rationale: "Dorsum" refers to the upper surface of the body, so "back" conveys that same anatomical area in a word everyone knows. Word frequency rises sharply from Zipf 2.47 to 6.04, making the replacement far more common in everyday language. The reader can now immediately picture the body part without encountering a technical Latin term.
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
| `cardio` -> `heart` | replace | attributed | -0.015 | -1.747 | 0.199 | 0.506 | 0.158 | - |
| `pulmonary` -> `lung` | replace | attributed | 0.000 | 1.263 | 0.465 | 0.466 | 0.157 | - |

**edit `cardio` -> `heart`**

- status: `attributed`
- log p full -0.0178, empty -0.0031
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.141` [readme] pulmonary: Related to the lungs.
    - `-0.017` [iowa] PULMONARY: pertaining to the lungs
    - `-0.035` [nih] pulmonary: Having to do with the lungs.
    - `-0.299` [readme] Pulmonary: About the lungs.
    - `-0.365` [thesaurus] pulmonary: related to the lungs

- rationale: "Cardio" refers to the heart, so replacing it with "heart" directly names the organ in the most familiar way. Word frequency rises from Zipf 3.44 to 5.31, making the term much more common in everyday language. The reader immediately recognizes the body part being discussed without needing any medical prefix.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `pulmonary` -> `lung`**

- status: `attributed`
- log p full -0.0000, empty -0.0001
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.392` [nih] pulmonary: Having to do with the lungs.
    - `+0.235` [iowa] PULMONARY: pertaining to the lungs
    - `+0.179` [justplainclear] pulmonary: About the lungs
    - `+0.164` [thesaurus] pulmonary: related to the lungs
    - `-0.300` [readme] Pulmonary: About the lungs.

- rationale: "Pulmonary" refers to anything involving the lungs, so replacing it with "lung" directly names the organ in a way everyone recognizes. Word frequency rises from Zipf 3.50 to 4.10, and age of acquisition drops from 13.05 to 7.16. Readers can now instantly connect the term to the body part without needing medical vocabulary.
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

**output:** At that time, the patient's Coreg had been stopped because of low blood pressure.

| metric | value |
|---|---:|
| bertscore_f1 | 0.677 |
| coleman_liau | 9.01 |
| coleman_liau_drop | -0.61 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.250 |
| fkgl | 4.20 |
| fkgl_drop | 2.74 |
| fre | 89.9 |
| fre_gain | 25.0 |
| human_edit_recall | 1.000 |
| length_ratio | 1.15 |
| n_words | 15.0 |
| nli_completeness | 0.796 |
| nli_faithfulness | 0.770 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 58.63 |
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
| `Coreg` -> `blood pressure medicine` | replace | attributed | -1.189 | -1.637 | 0.265 | 0.729 | 0.054 | - |
| `secondary to` -> `because of` | replace | attributed | 0.001 | 0.079 | -0.013 | 0.672 | 0.326 | - |
| `hypotension` -> `low blood pressure` | replace | attributed | 0.000 | 3.301 | 0.552 | 0.693 | 0.029 | - |

**edit `Coreg` -> `blood pressure medicine`**

- status: `attributed`
- log p full -1.9910, empty -0.8021
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+0.700` [michigan] hypotension: When your blood pressure is low. For some people, this is normal, but it may cause problems for o
    - `+0.646` [readme] hypotension: Low blood pressure.
    - `+0.296` [nih] Coreg: A drug used to treat high blood pressure and certain heart problems. It is also being studied in the pr
    - `-0.021` [iowa] HYPOTENSION: low blood pressure

- rationale: Coreg is a brand-name medication used to treat high blood pressure, so calling it a "blood pressure medicine" directly states its purpose. Word frequency rises sharply from Zipf 1.16 to 4.44, making the replacement far more common in everyday language. This lets the reader immediately recognize the drug's function without needing to know a specific brand name.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `secondary to` -> `because of`**

- status: `attributed`
- log p full -0.0076, empty -0.0082
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+0.460` [wiktionary] to: To shows where something goes, the goal of movement.
    - `+0.134` [michigan] hypotension: When your blood pressure is low. For some people, this is normal, but it may cause problems for o
    - `+0.067` [iowa] HYPOTENSION: low blood pressure
    - `+0.017` [readme] Hypotension: Hypotension means low blood pressure.

- rationale: "Secondary to" indicates that one condition results from another, and "because of" conveys that same cause‑and‑effect relationship in everyday words. Phrase frequency rises from Zipf 4.53 to 6.01, while age of acquisition drops from 9.11 to 4.55. Readers can now grasp the reason for a symptom without pausing to decode a formal medical connector.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `hypotension` -> `low blood pressure`**

- status: `attributed`
- log p full -0.0000, empty -0.0005
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+0.733` [iowa] HYPOTENSION: low blood pressure
    - `+0.704` [readme] Hypotension: Hypotension means low blood pressure.
    - `+0.439` [readme] hypotension: Low blood pressure.
    - `+0.165` [wiktionary] to: To shows where something goes, the goal of movement.
    - `+0.074` [michigan] hypotension: When your blood pressure is low. For some people, this is normal, but it may cause problems for o

- rationale: Hypotension means abnormally low pressure in the arteries, so "low blood pressure" conveys that exact condition in everyday terms. Word frequency rises from Zipf 2.52 to 4.65, and age of acquisition drops from 14.41 to 8.95. A reader can now immediately grasp the circulatory issue without needing clinical vocabulary.
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

**output:** Her diarrhea has calmed down, and she is having fewer problems with urine leaking and less swelling in her feet.

| metric | value |
|---|---:|
| bertscore_f1 | 0.634 |
| coleman_liau | 9.11 |
| coleman_liau_drop | 1.88 |
| copy_jargon_rate | 0.333 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 9.32 |
| fkgl_drop | 3.46 |
| fre | 63.9 |
| fre_gain | 31.9 |
| human_edit_recall | 0.667 |
| length_ratio | 1.18 |
| n_words | 20.0 |
| nli_completeness | 0.927 |
| nli_faithfulness | 0.795 |
| replacement_f1 | 0.800 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 43.59 |
| smog | 8.84 |
| smog_drop | 5.71 |
| temporality_preservation | 0.000 |

### Stage 4 - arm `termonly`

**output:** Her loose stools have calmed down and she is having less leaking of urine, less swelling in her feet.

| metric | value |
|---|---:|
| bertscore_f1 | 0.729 |
| coleman_liau | 7.37 |
| coleman_liau_drop | 3.62 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 6.10 |
| fkgl_drop | 6.67 |
| fre | 85.1 |
| fre_gain | 53.2 |
| human_edit_recall | 1.000 |
| length_ratio | 1.12 |
| n_words | 19.0 |
| nli_completeness | 0.941 |
| nli_faithfulness | 0.942 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.286 |
| sari | 48.79 |
| smog | 3.13 |
| smog_drop | 11.43 |
| temporality_preservation | 0.000 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `diarrhea` -> `loose stools` | replace | - | - | - | - | - | - | - |
| `urinary incontinence` -> `leaking of urine` | replace | - | - | - | - | - | - | - |
| `pedal edema` -> `swelling in her feet` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Her runny poop has calmed down, and she is having less trouble holding her pee and less swelling in her feet.

| metric | value |
|---|---:|
| bertscore_f1 | 0.713 |
| coleman_liau | 6.82 |
| coleman_liau_drop | 4.17 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 7.21 |
| fkgl_drop | 5.57 |
| fre | 80.8 |
| fre_gain | 48.8 |
| human_edit_recall | 1.000 |
| length_ratio | 1.24 |
| n_words | 21.0 |
| nli_completeness | 0.943 |
| nli_faithfulness | 0.866 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.286 |
| sari | 51.20 |
| smog | 3.13 |
| smog_drop | 11.43 |
| temporality_preservation | 0.000 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `diarrhea` -> `runny poop` | replace | attributed | 5.918 | 6.586 | 0.727 | 0.894 | 5.561 | - |
| `urinary incontinence` -> `trouble holding her pee` | replace | attributed | 0.396 | 1.842 | 0.637 | 0.802 | 0.884 | - |
| `pedal edema` -> `swelling in her feet` | replace | attributed | -0.216 | -1.976 | 0.805 | 0.890 | 0.041 | - |

**edit `diarrhea` -> `runny poop`**

- status: `attributed`
- log p full -0.7180, empty -6.6361
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+6.247` [readme] Diarrhea: Having runny poop with stomach pains and bloating.
    - `+0.686` [michigan] urinary incontinence: When you lose control of your bladder and the fluids it holds.
    - `+0.105` [readme] pedal edema: Swollen feet.
    - `+0.079` [nih] urinary incontinence: Inability to hold urine in the bladder.

- rationale: The glossary explains diarrhea as having runny poop along with stomach pains and bloating, so the replacement directly uses that plain description. Word frequency shifts from Zipf 3.55 to 2.86. Patients can now recognize the symptom in familiar, everyday language without needing the clinical term.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `urinary incontinence` -> `trouble holding her pee`**

- status: `attributed`
- log p full -0.0959, empty -0.4918
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+1.830` [readme] urinary incontinence: When you can't control your pee.
    - `+0.946` [nih] urinary incontinence: Inability to hold urine in the bladder.
    - `+0.306` [michigan] diarrhea: Loose, watery stools three or more times a day. It can be sudden (due to a virus, for example), pers
    - `+0.289` [readme] Diarrhea: Having runny poop with stomach pains and bloating.
    - `+0.281` [wiktionary] diarrhea: Diarrhea is an illness where the person's poop or feces are soft like water.

- rationale: Urinary incontinence means losing control of the bladder, and "trouble holding her pee" conveys that same loss of control in everyday words. Word frequency rises from Zipf 2.77 to 3.86, while age of acquisition drops from 14.41 to 5.09. The reader can now grasp the symptom immediately, without needing to decode a formal medical label.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `pedal edema` -> `swelling in her feet`**

- status: `attributed`
- log p full -0.2554, empty -0.0395
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+0.389` [michigan] urinary incontinence: When you lose control of your bladder and the fluids it holds.
    - `+0.347` [justplainclear] diarrhea: A bowel movement that is loose and watery If your poop is like water or very runny, or if you have m
    - `+0.211` [readme] urinary incontinence: When you can't control your pee.

- rationale: "Pedal edema" refers to fluid buildup causing swelling in the lower legs and feet, so "swelling in her feet" directly conveys that same condition in everyday terms. Word frequency rises from Zipf 2.87 to 3.66, and age of acquisition drops from 15.07 to 5.09. The reader can now immediately recognize the symptom without needing to decode clinical terminology.
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

**output:** The patient feels sick to the stomach and has belly pain after eating. This is caused by gall bladder disease. A surgery called laparoscopic cholecystectomy is planned.

| metric | value |
|---|---:|
| bertscore_f1 | 0.381 |
| coleman_liau | 10.77 |
| coleman_liau_drop | 14.88 |
| copy_jargon_rate | 1.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 7.15 |
| fkgl_drop | 12.28 |
| fre | 59.8 |
| fre_gain | 81.0 |
| human_edit_recall | 0.000 |
| length_ratio | 1.50 |
| n_words | 27.0 |
| nli_completeness | 0.182 |
| nli_faithfulness | 0.976 |
| replacement_f1 | 0.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 23.97 |
| smog | 8.84 |
| smog_drop | 7.06 |
| temporality_preservation | 1.000 |

### Stage 4 - arm `termonly`

**output:** She has an upset stomach and belly pain after eating. This is from a problem with the organ that stores bile. A surgery using small cuts to remove that organ is planned.

| metric | value |
|---|---:|
| bertscore_f1 | 0.340 |
| coleman_liau | 5.89 |
| coleman_liau_drop | 19.75 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 4.80 |
| fkgl_drop | 14.64 |
| fre | 79.7 |
| fre_gain | 100.8 |
| human_edit_recall | 1.000 |
| length_ratio | 1.78 |
| n_words | 32.0 |
| nli_completeness | 0.193 |
| nli_faithfulness | 0.631 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.222 |
| sari | 21.44 |
| smog | 6.43 |
| smog_drop | 9.48 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 5 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `Nausea` -> `upset stomach` | replace | - | - | - | - | - | - | - |
| `abdominal pain` -> `belly pain` | replace | - | - | - | - | - | - | - |
| `Gall bladder disease` -> `a problem with the organ that stores bile` | replace | - | - | - | - | - | - | - |
| `Laparoscopic` -> `surgery using small cuts` | replace | - | - | - | - | - | - | - |
| `cholecystectomy` -> `to remove that organ` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Feeling sick and belly pain after eating – a problem with the gallbladder – surgery to remove the gallbladder with a small camera is planned.

| metric | value |
|---|---:|
| bertscore_f1 | 0.415 |
| coleman_liau | 11.66 |
| coleman_liau_drop | 13.99 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.375 |
| fkgl | 12.36 |
| fkgl_drop | 7.07 |
| fre | 47.4 |
| fre_gain | 68.5 |
| human_edit_recall | 1.000 |
| length_ratio | 1.28 |
| n_words | 23.0 |
| nli_completeness | 0.810 |
| nli_faithfulness | 0.641 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.222 |
| sari | 25.72 |
| smog | 14.55 |
| smog_drop | 1.35 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `abdominal pain` -> `belly pain` | replace | attributed | -0.024 | -0.081 | 0.530 | 0.769 | 0.217 | - |
| `Gall bladder disease` -> `a problem with the gallbladder` | replace | attributed | -0.795 | -1.036 | 0.058 | 0.771 | 0.026 | - |
| `Laparoscopic cholecystectomy` -> `surgery to remove the gallbladder with a small camera` | replace | attributed | 4.551 | 4.761 | 0.662 | 0.779 | 0.991 | - |

**edit `abdominal pain` -> `belly pain`**

- status: `attributed`
- log p full -0.3616, empty -0.3376
- masks scored: 66/66 (+5 top-k)
- ranked sources:
    - `+0.502` [justplainclear] cholecystectomy: A surgery to take out your gallbladder
    - `+0.285` [wiktionary] gall: If you have the gall to do something, you do it even though it is very rude or unreasonable.
    - `+0.191` [justplainclear] bladder disease: A disease or disorder of your bladder. Some bladder diseases may include: • urinary incontine
    - `+0.054` [wiktionary] gall: Gall is anger or hatred.

- rationale: "Abdominal pain" refers to discomfort in the stomach or belly area, so "belly pain" conveys the same meaning using a more familiar, everyday word. Word frequency rises from Zipf 3.56 to 4.05, and age of acquisition drops from 10.24 to 4.26. This lets the reader immediately recognize the symptom without needing a clinical term.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `Gall bladder disease` -> `a problem with the gallbladder`**

- status: `attributed`
- log p full -1.8955, empty -1.1007
- masks scored: 66/66 (+5 top-k)
- ranked sources:
    - `+0.459` [justplainclear] cholecystectomy: A surgery to take out your gallbladder
    - `+0.433` [justplainclear] nausea: Feeling like you want to throw up, stomach feels upset
    - `+0.401` [readme] laparoscopic: A surgery where a small tube with a camera is used to see inside the body.
    - `+0.274` [justplainclear] bladder disease: A disease or disorder of your bladder. Some bladder diseases may include: • urinary incontine
    - `+0.035` [wiktionary] gall: If you have the gall to do something, you do it even though it is very rude or unreasonable.

- rationale: Gall bladder disease refers to any condition affecting the organ that stores bile, and calling it "a problem with the gallbladder" conveys that same general idea in everyday terms. Word frequency decreases from Zipf 3.12 to 2.81, while age of acquisition drops from 12.44 to 11.68. The reader can now grasp the basic health issue without needing to know the clinical label.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `Laparoscopic cholecystectomy` -> `surgery to remove the gallbladder with a small camera`**

- status: `attributed`
- log p full -1.6538, empty -6.2045
- masks scored: 66/66 (+5 top-k)
- ranked sources:
    - `+1.830` [readme] Laparoscopic: A surgery that uses a small tube and camera to see inside your body.
    - `+0.839` [readme] laparoscopic: A surgery where a small tube with a camera is used to see inside the body.
    - `+0.546` [nih] nausea: A feeling of sickness or discomfort in the stomach that may come with an urge to vomit. Nausea is a si
    - `+0.345` [readme] Cholecystectomy: A surgery to remove the gallbladder, an organ in your stomach that helps with digestion.
    - `+0.301` [wiktionary] gall: Gall is anger or hatred.

- rationale: The glossary explains that a laparoscopic cholecystectomy uses a small tube and camera to operate, so "surgery to remove the gallbladder with a small camera" conveys both the method and the organ involved in everyday terms. Phrase frequency rises from Zipf 1.73 to 2.79, making the replacement more commonly encountered. Patients can now grasp the procedure's purpose and minimally invasive nature without needing surgical vocabulary.
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

**output:** She says she has a history of heart disease, but she cannot explain much more about it.

| metric | value |
|---|---:|
| bertscore_f1 | 0.595 |
| coleman_liau | 6.00 |
| coleman_liau_drop | 4.27 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.125 |
| fkgl | 7.00 |
| fkgl_drop | 5.27 |
| fre | 75.1 |
| fre_gain | 32.4 |
| human_edit_recall | 1.000 |
| length_ratio | 0.77 |
| n_words | 17.0 |
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

**output:** She says she has a history of heart disease but cannot give more detail.

| metric | value |
|---|---:|
| bertscore_f1 | 0.639 |
| coleman_liau | 6.11 |
| coleman_liau_drop | 4.16 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 5.88 |
| fkgl_drop | 6.39 |
| fre | 77.8 |
| fre_gain | 35.1 |
| human_edit_recall | 1.000 |
| length_ratio | 0.64 |
| n_words | 14.0 |
| negation_preservation | 0.000 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.994 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.250 |
| sari | 21.35 |
| severity_downgrade | 1.000 |
| severity_preservation | 0.000 |
| severity_tier_input | 2.000 |
| smog | 8.84 |
| smog_drop | 5.71 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 0 edits kept


### Stage 4 - arm `grounded`

**output:** She says she has a history of heart disease but cannot give many details about it.

| metric | value |
|---|---:|
| bertscore_f1 | 0.608 |
| coleman_liau | 6.27 |
| coleman_liau_drop | 4.00 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.125 |
| fkgl | 7.61 |
| fkgl_drop | 4.66 |
| fre | 69.0 |
| fre_gain | 26.3 |
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

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `elaborate` -> `give many details` | replace | attributed | -0.340 | -0.395 | 0.395 | 0.857 | 0.078 | - |

**edit `elaborate` -> `give many details`**

- status: `attributed`
- log p full -2.1506, empty -1.8106
- masks scored: 66/66 (+2 top-k)
- ranked sources:
    - `+0.277` [wiktionary] significant: If something is significant, it is important, or large, enough to pay attention to or to believe.
    - `+0.198` [wiktionary] to: To has no meaning. It is used with a bare infinitival clause.
    - `+0.154` [wiktionary] any: it does not matter which
    - `+0.143` [wiktionary] elaborate: When something is supposed to be elaborated, it is needed to be expanded or add details to.
    - `+0.043` [wiktionary] significant: A significant look, movement, etc. is one that has a particular meaning.

- rationale: To elaborate means to explain something with added detail, so "give many details" directly conveys that same idea in everyday words. Word frequency rises from Zipf 4.06 to 4.81, and age of acquisition drops from 11.53 to 4.60. This lets the reader grasp the instruction to be thorough without needing to know a more formal verb.
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

**output:** There was a little swelling on his fourth finger, and he still has his wedding ring on that finger.

| metric | value |
|---|---:|
| bertscore_f1 | 0.721 |
| coleman_liau | 6.76 |
| coleman_liau_drop | 0.29 |
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
| nli_faithfulness | 0.993 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.714 |
| sari | 24.51 |
| severity_downgrade | 0.000 |
| severity_preservation | 0.000 |
| severity_tier_input | 1.000 |
| severity_tier_output | 1.000 |
| smog | 3.13 |
| smog_drop | 5.71 |

### Stage 4 - arm `termonly`

**output:** The ring finger was a little swollen, and he still has his wedding band on it.

| metric | value |
|---|---:|
| bertscore_f1 | 0.642 |
| coleman_liau | 4.46 |
| coleman_liau_drop | 2.58 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.250 |
| fkgl | 5.40 |
| fkgl_drop | 1.11 |
| fre | 84.8 |
| fre_gain | 4.4 |
| human_edit_recall | 1.000 |
| length_ratio | 0.89 |
| n_words | 16.0 |
| nli_completeness | 0.868 |
| nli_faithfulness | 0.275 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.625 |
| sari | 23.69 |
| severity_downgrade | 0.000 |
| severity_preservation | 0.000 |
| severity_tier_input | 1.000 |
| severity_tier_output | 1.000 |
| smog | 3.13 |
| smog_drop | 5.71 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `edema` -> `swollen` | replace | - | - | - | - | - | - | - |

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
| `edema` -> `swelling` | replace | attributed | 0.474 | 8.209 | 0.412 | 0.429 | 0.379 | - |
| `fourth digit` -> `ring finger` | replace | attributed | -0.010 | -1.143 | 0.465 | 0.817 | 0.503 | - |

**edit `edema` -> `swelling`**

- status: `attributed`
- log p full -0.0002, empty -0.4742
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+1.736` [nih] edema: Swelling caused by excess fluid in body tissues.
    - `+1.357` [readme] Edema: Swelling in the body caused by too much fluid.
    - `+0.965` [readme] edema: Swelling due to too much fluid in the body tissues.
    - `+0.866` [michigan] edema: Swelling caused by too much fluid in your body.
    - `+0.699` [readme] digit: A digit is a finger or toe.

- rationale: Edema refers to fluid trapped in body tissues causing puffiness, so "swelling" conveys that same idea in an everyday word. Word frequency rises from Zipf 2.95 to 3.68, making the replacement more familiar. The reader can now recognize the symptom without needing clinical vocabulary.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `fourth digit` -> `ring finger`**

- status: `attributed`
- log p full -0.0146, empty -0.0047
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+1.168` [wiktionary] fourth: A fourth of something is one of four equal parts of that thing; a quarter.
    - `+0.665` [wiktionary] fourth: The fourth thing is something that is number four (4) in order.
    - `+0.328` [nih] edema: Swelling caused by excess fluid in body tissues.
    - `+0.307` [readme] edema: Swelling due to too much fluid in the body tissues.
    - `+0.268` [readme] Edema: Swelling in the body caused by too much fluid.

- rationale: The original term refers to the finger next to the pinky, and "ring finger" conveys that same anatomical location using a familiar, everyday name. Word frequency rises from Zipf 3.73 to 4.31, and age of acquisition drops from 9.26 to 4.53. This lets the reader immediately picture the correct finger without needing to count from the thumb.
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

**output:** The parents say that she seems to breathe fast and gets tired during feeding, with harder breathing and sweating.

| metric | value |
|---|---:|
| bertscore_f1 | 0.581 |
| coleman_liau | 11.03 |
| coleman_liau_drop | 4.35 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 7.97 |
| fkgl_drop | 4.86 |
| fre | 71.8 |
| fre_gain | 31.3 |
| human_edit_recall | 1.000 |
| length_ratio | 0.90 |
| n_words | 19.0 |
| nli_completeness | 0.956 |
| nli_faithfulness | 0.791 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 23.66 |
| smog | 3.13 |
| smog_drop | 9.89 |

### Stage 4 - arm `termonly`

**output:** Parents do say that she seems to breathe fast, gets a bit tired during feeding with harder breathing and sweating.

| metric | value |
|---|---:|
| bertscore_f1 | 0.687 |
| coleman_liau | 9.69 |
| coleman_liau_drop | 5.69 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 8.14 |
| fkgl_drop | 4.69 |
| fre | 72.3 |
| fre_gain | 31.8 |
| human_edit_recall | 1.000 |
| length_ratio | 0.95 |
| n_words | 20.0 |
| nli_completeness | 0.700 |
| nli_faithfulness | 0.623 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 24.14 |
| smog | 3.13 |
| smog_drop | 9.89 |

annotation backend `novita`, 4 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `state` -> `say` | replace | - | - | - | - | - | - | - |
| `rapidly` -> `fast` | replace | - | - | - | - | - | - | - |
| `respiratory effort` -> `harder breathing` | replace | - | - | - | - | - | - | - |
| `diaphoresis` -> `sweating` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Her parents do say she seems to breathe quickly, gets a bit tired while feeding with more work to breathe and heavy sweating.

| metric | value |
|---|---:|
| bertscore_f1 | 0.590 |
| coleman_liau | 8.38 |
| coleman_liau_drop | 7.00 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.833 |
| fkgl | 8.26 |
| fkgl_drop | 4.57 |
| fre | 76.8 |
| fre_gain | 36.3 |
| human_edit_recall | 1.000 |
| length_ratio | 1.10 |
| n_words | 23.0 |
| nli_completeness | 0.821 |
| nli_faithfulness | 0.143 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 22.82 |
| smog | 3.13 |
| smog_drop | 9.89 |

annotation backend `novita`, 4 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `state` -> `say` | replace | attributed | 0.005 | 1.795 | 0.410 | 0.630 | 0.081 | - |
| `rapidly` -> `quickly` | replace | attributed | 3.503 | 3.746 | 0.702 | 0.890 | 2.808 | - |
| `respiratory effort` -> `more work to breathe` | replace | attributed | 1.581 | 2.551 | 0.325 | 0.699 | 0.069 | - |
| `diaphoresis` -> `heavy sweating` | replace | attributed | 2.790 | 6.008 | 0.870 | 0.951 | 5.158 | - |

**edit `state` -> `say`**

- status: `attributed`
- log p full -0.0010, empty -0.0062
- masks scored: 66/66 (+8 top-k)
- ranked sources:
    - `+0.509` [michigan] diaphoresis: Sweating, a clear, salty liquid produced by glands in your skin. Sweating is how your body cools 
    - `+0.428` [thesaurus] state: say, tell, condition
    - `+0.420` [wiktionary] effort: The amount of work that is done on something.
    - `+0.118` [michigan] state: To say or tell. In medicine, how you are doing.
    - `+0.077` [readme] Diaphoresis: Intense sweating.

- rationale: "State" means to express something in words, and "say" conveys that same act of verbal expression in a more everyday way. Word frequency rises slightly from Zipf 5.78 to 5.89, while age of acquisition drops from 6.39 to 3.42. The reader can now grasp the instruction without the slightly more formal tone of the original term.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `rapidly` -> `quickly`**

- status: `attributed`
- log p full -1.5088, empty -5.0115
- masks scored: 66/66 (+8 top-k)
- ranked sources:
    - `+3.734` [wiktionary] rapidly: If something is done rapidly, then it is done quickly or swiftly.
    - `+0.926` [wiktionary] state: Any sovereign nation (nation that rules itself) is a state.
    - `+0.463` [michigan] state: To say or tell. In medicine, how you are doing.
    - `+0.228` [readme] Respiratory: Related to how you breathe and the organs involved in breathing like the lungs and airways.
    - `+0.193` [thesaurus] state: say, tell, condition

- rationale: "Rapidly" is defined by Wiktionary as something done quickly or swiftly, so "quickly" carries the same meaning in a more everyday word. Word frequency rises from Zipf 4.34 to 5.00, making it a more familiar choice. The reader now grasps the speed of the action without encountering a less common adverb.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `respiratory effort` -> `more work to breathe`**

- status: `attributed`
- log p full -0.3949, empty -1.9754
- masks scored: 66/66 (+8 top-k)
- ranked sources:
    - `+0.405` [readme] Respiratory: Related to how you breathe and the organs involved in breathing like the lungs and airways.
    - `+0.337` [wiktionary] respiratory: A respiratory problem refers to something that affects breathing or the lungs.
    - `+0.037` [justplainclear] diaphoresis: Sweating
    - `+0.029` [readme] RESPIRATORY: Related to breathing or the lungs and airways.
    - `+0.008` [readme] Diaphoresis: Intense sweating.

- rationale: "Respiratory effort" refers to the work involved in breathing, and "more work to breathe" conveys that same sense of increased exertion in everyday terms. Word frequency rises from Zipf 3.78 to 4.25, and age of acquisition drops from 11.00 to 5.86. This lets the reader grasp the sensation of labored breathing without needing clinical terminology.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `diaphoresis` -> `heavy sweating`**

- status: `attributed`
- log p full -0.0384, empty -2.8284
- masks scored: 66/66 (+8 top-k)
- ranked sources:
    - `+6.873` [readme] diaphoresis: Heavy sweating.
    - `+1.715` [readme] Diaphoresis: Intense sweating.
    - `+1.239` [michigan] state: To say or tell. In medicine, how you are doing.
    - `+0.786` [wiktionary] state: A state is a condition or a situation.
    - `+0.743` [wiktionary] effort: The amount of work that is done on something.

- rationale: The glossary defines diaphoresis simply as heavy sweating, so the replacement directly adopts that plain-language description. Word frequency rises sharply from Zipf 1.28 to 3.64, and age of acquisition drops from 15.22 to 4.05. Readers can now immediately grasp the symptom without encountering an unfamiliar medical term.
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

**output:** The patient has not used stimulant drugs for at least four to five months, according to the patient; however, he had a start of chest pain this evening.

| metric | value |
|---|---:|
| bertscore_f1 | 0.842 |
| coleman_liau | 8.21 |
| coleman_liau_drop | 1.18 |
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
| nli_completeness | 0.251 |
| nli_faithfulness | 0.977 |
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
| `amphetamines` -> `stimulant drugs` | replace | failed | - | - | - | - | - | - |
| `onset` -> `the start` | replace | failed | - | - | - | - | - | - |

**edit `amphetamines` -> `stimulant drugs`**

- status: `failed` - full or empty boundary score failed
- log p full -10000.0000, empty -0.0835
- masks scored: 9/10 (+0 top-k)

- rationale: Amphetamines are a class of synthetic drugs that speed up the body’s central nervous system, so calling them "stimulant drugs" directly names that energizing effect in everyday terms. Word frequency rises from a Zipf score of 2.82 to 3.05, making the replacement more commonly encountered. This lets the reader immediately grasp the drug’s basic action without needing to know the specific chemical category.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `onset` -> `the start`**

- status: `failed` - full or empty boundary score failed
- log p full -10000.0000, empty -2.1811
- masks scored: 9/10 (+0 top-k)

- rationale: "Onset" refers to the beginning or commencement of something, and "the start" conveys that exact same idea in more familiar words. Word frequency rises from Zipf 3.72 to 5.56, while age of acquisition drops from 10.72 to 4.37. This lets the reader immediately grasp when a symptom or condition first appeared without needing a less common term.
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

**output:** A tube was used to remove a small amount of clear fluid from the stomach.

| metric | value |
|---|---:|
| bertscore_f1 | 0.384 |
| coleman_liau | 4.65 |
| coleman_liau_drop | 11.39 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.111 |
| fkgl | 5.21 |
| fkgl_drop | 3.16 |
| fre | 84.5 |
| fre_gain | 31.6 |
| human_edit_recall | 1.000 |
| length_ratio | 0.94 |
| n_words | 15.0 |
| nli_completeness | 0.848 |
| nli_faithfulness | 0.887 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.143 |
| sari | 27.94 |
| smog | 3.13 |
| smog_drop | 5.71 |

### Stage 4 - arm `termonly`

**output:** A tube was put through the mouth into the stomach to pull out fluid, but only a tiny amount of see-through liquid came out.

| metric | value |
|---|---:|
| bertscore_f1 | 0.341 |
| coleman_liau | 6.41 |
| coleman_liau_drop | 9.63 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.222 |
| fkgl | 9.01 |
| fkgl_drop | -0.64 |
| fre | 73.2 |
| fre_gain | 20.3 |
| human_edit_recall | 1.000 |
| length_ratio | 1.56 |
| n_words | 25.0 |
| nli_completeness | 0.941 |
| nli_faithfulness | 0.670 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 28.94 |
| smog | 3.13 |
| smog_drop | 5.71 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `scant` -> `tiny amount of` | replace | - | - | - | - | - | - | - |
| `clear stomach contents` -> `see-through liquid` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** A tube was put through the mouth into the stomach to pull out fluid, but only a very small amount of thin stomach liquid came out.

| metric | value |
|---|---:|
| bertscore_f1 | 0.368 |
| coleman_liau | 6.04 |
| coleman_liau_drop | 10.00 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.333 |
| fkgl | 9.98 |
| fkgl_drop | -1.61 |
| fre | 69.8 |
| fre_gain | 16.9 |
| human_edit_recall | 1.000 |
| length_ratio | 1.62 |
| n_words | 26.0 |
| nli_completeness | 0.945 |
| nli_faithfulness | 0.657 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 29.85 |
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

**output:** The patient may have some restriction because of scar tissue.

| metric | value |
|---|---:|
| bertscore_f1 | 0.577 |
| coleman_liau | 10.82 |
| coleman_liau_drop | 4.89 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.250 |
| fkgl | 6.01 |
| fkgl_drop | 5.51 |
| fre | 69.8 |
| fre_gain | 41.3 |
| human_edit_recall | 1.000 |
| length_ratio | 0.91 |
| n_words | 10.0 |
| nli_completeness | 0.808 |
| nli_faithfulness | 0.717 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.400 |
| sari | 11.79 |
| smog | 8.84 |
| smog_drop | 5.71 |
| uncertainty_preservation | 1.000 |

### Stage 4 - arm `termonly`

**output:** Probably there is some stiffening because of scarring.

| metric | value |
|---|---:|
| bertscore_f1 | 0.691 |
| coleman_liau | 13.85 |
| coleman_liau_drop | 1.86 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 8.18 |
| fkgl_drop | 3.34 |
| fre | 50.7 |
| fre_gain | 22.2 |
| human_edit_recall | 1.000 |
| length_ratio | 0.73 |
| n_words | 8.0 |
| nli_completeness | 0.808 |
| nli_faithfulness | 0.860 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 37.67 |
| smog | 11.21 |
| smog_drop | 3.35 |
| uncertainty_preservation | 1.000 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `restrictive element` -> `stiffening` | replace | - | - | - | - | - | - | - |
| `fibrosis` -> `scarring` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Probably there is some limiting part because of scarred tissue.

| metric | value |
|---|---:|
| bertscore_f1 | 0.808 |
| coleman_liau | 11.98 |
| coleman_liau_drop | 3.73 |
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
| nli_completeness | 0.864 |
| nli_faithfulness | 0.962 |
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
| `restrictive element` -> `limiting part` | replace | attributed | 6.375 | 6.960 | 0.828 | 0.876 | 2.142 | - |
| `fibrosis` -> `scarred tissue` | replace | attributed | 4.307 | 4.969 | 0.765 | 0.892 | 5.058 | - |

**edit `restrictive element` -> `limiting part`**

- status: `attributed`
- log p full -0.8138, empty -7.1889
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+3.246` [wiktionary] restrictive: If something is restrictive, it limits or controls what people can do.
    - `+1.104` [wiktionary] element: An element is one part of something bigger, such as a plan, an engine, or a business.
    - `+0.671` [nih] element: A basic part of a whole. In chemistry, refers to a simple substance that cannot be broken down into s
    - `+0.476` [readme] FIBROSIS: Fibrosis is tissue that becomes thick and scarred due to injury.
    - `+0.160` [wiktionary] element: An element is one basic kind of substance, such as iron (Fe), oxygen (O), or sodium (Na).

- rationale: The glossary defines restrictive as something that limits or controls, so "limiting part" directly conveys that same idea of a component that imposes boundaries. Phrase frequency rises from Zipf 3.49 to 3.94, and age of acquisition drops from 11.00 to 5.11. This lets the reader grasp the constraining role of the element without needing to decode a more formal adjective.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `fibrosis` -> `scarred tissue`**

- status: `attributed`
- log p full -0.7189, empty -5.0260
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+5.493` [readme] FIBROSIS: Fibrosis is tissue that becomes thick and scarred due to injury.
    - `+0.435` [wiktionary] element: An element is one basic kind of substance, such as iron (Fe), oxygen (O), or sodium (Na).
    - `+0.306` [nih] element: A basic part of a whole. In chemistry, refers to a simple substance that cannot be broken down into s
    - `+0.244` [nih] fibrosis: The growth of fibrous tissue.
    - `+0.236` [wiktionary] element: An element is one part of something bigger, such as a plan, an engine, or a business.

- rationale: Fibrosis refers to tissue that thickens and scars from injury, so calling it "scarred tissue" directly conveys that same idea in everyday words. Word frequency rises slightly from Zipf 3.19 to 3.23, while age of acquisition drops sharply from 14.94 to 4.76. This lets the reader immediately picture the damage without needing to learn a clinical term.
- audit: coverage 0.833, grounding_error=False, omission=False, source_ok=False, passage_ok=True

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

**output:** The uterus was put back into the belly area.

| metric | value |
|---|---:|
| bertscore_f1 | 0.773 |
| coleman_liau | 3.47 |
| coleman_liau_drop | 5.80 |
| copy_jargon_rate | 0.500 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 7.59 |
| fkgl_drop | 2.62 |
| fre | 56.7 |
| fre_gain | 18.8 |
| human_edit_recall | 0.500 |
| length_ratio | 1.12 |
| n_words | 9.0 |
| nli_completeness | 0.974 |
| nli_faithfulness | 0.981 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 34.72 |
| smog | 11.21 |
| smog_drop | 1.82 |

### Stage 4 - arm `termonly`

**output:** The womb was placed back into the belly space.

| metric | value |
|---|---:|
| bertscore_f1 | 0.836 |
| coleman_liau | 4.76 |
| coleman_liau_drop | 4.51 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 2.34 |
| fkgl_drop | 7.87 |
| fre | 94.3 |
| fre_gain | 56.4 |
| human_edit_recall | 1.000 |
| length_ratio | 1.12 |
| n_words | 9.0 |
| nli_completeness | 0.989 |
| nli_faithfulness | 0.979 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 84.29 |
| smog | 3.13 |
| smog_drop | 9.89 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `uterus` -> `womb` | replace | - | - | - | - | - | - | - |
| `abdominal cavity` -> `belly space` | replace | - | - | - | - | - | - | - |

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
| `uterus` -> `womb` | replace | attributed | -0.000 | -0.247 | 0.191 | 0.551 | 0.824 | - |
| `abdominal cavity` -> `belly area` | replace | attributed | 3.163 | 4.415 | 0.817 | 0.878 | 4.684 | - |

**edit `uterus` -> `womb`**

- status: `attributed`
- log p full -0.0001, empty -0.0001
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+1.081` [thesaurus] uterus: womb
    - `+0.256` [wiktionary] uterus: The uterus is the internal organ inside of a female mammal where an embryo grows into an infant ready 
    - `+0.244` [nih] uterus: The hollow, pear-shaped organ in a woman's pelvis. The uterus is where a fetus (unborn baby) develops 
    - `+0.235` [michigan] uterus: Womb, or where a baby grows when a woman is pregnant.
    - `-0.271` [readme] abdominal cavity: The belly area where your stomach and other organs are located.

- rationale: The uterus is the organ where a baby develops during pregnancy, and "womb" conveys this exact same meaning in a more familiar, everyday word. Word frequency rises from Zipf 3.40 to 3.63, and age of acquisition drops from 12.84 to 9.48. Readers can now immediately recognise the body part being discussed without needing a more clinical term.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `abdominal cavity` -> `belly area`**

- status: `attributed`
- log p full -0.3244, empty -3.4872
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+4.998` [readme] abdominal cavity: The belly area where your stomach and other organs are located.
    - `+0.314` [michigan] uterus: Womb, or where a baby grows when a woman is pregnant.
    - `+0.304` [wiktionary] uterus: The uterus is the internal organ inside of a female mammal where an embryo grows into an infant ready 
    - `+0.258` [justplainclear] uterus: Also known as: womb An organ in a woman's body where babies may grow during pregnancy Uterus
    - `-0.031` [nih] uterus: The hollow, pear-shaped organ in a woman's pelvis. The uterus is where a fetus (unborn baby) develops 

- rationale: The glossary explains the abdominal cavity as the belly area containing the stomach and other organs, so "belly area" directly conveys that location in everyday terms. Word frequency rises from Zipf 3.29 to 4.08, and age of acquisition drops from 10.24 to 6.58. This lets the reader immediately picture the general region without needing anatomical vocabulary.
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

**output:** The doctors looked at this on the front-to-back and side-view X‑rays.

| metric | value |
|---|---:|
| bertscore_f1 | 0.351 |
| coleman_liau | 9.98 |
| coleman_liau_drop | -2.65 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 4.79 |
| fkgl_drop | 0.17 |
| fre | 80.3 |
| fre_gain | 4.8 |
| human_edit_recall | 1.000 |
| laterality_preservation | 0.000 |
| length_ratio | 1.88 |
| n_words | 15.0 |
| nli_completeness | 0.413 |
| nli_faithfulness | 0.075 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 34.19 |
| smog | 8.84 |
| smog_drop | 2.37 |

### Stage 4 - arm `termonly`

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
| `AP` -> `front-to-back` | replace | - | - | - | - | - | - | - |
| `lateral projections` -> `side views` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** This was seen on the front-to-back and side views.

| metric | value |
|---|---:|
| bertscore_f1 | 0.585 |
| coleman_liau | 6.04 |
| coleman_liau_drop | 1.29 |
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
| nli_completeness | 0.864 |
| nli_faithfulness | 0.914 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 42.64 |
| smog | 8.84 |
| smog_drop | 2.37 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `AP` -> `front-to-back` | replace | attributed | 0.756 | 3.975 | 0.572 | 0.739 | 0.099 | - |
| `lateral projections` -> `side views` | replace | attributed | 0.253 | 0.719 | 0.279 | 0.741 | 0.446 | - |

**edit `AP` -> `front-to-back`**

- status: `attributed`
- log p full -0.0218, empty -0.7774
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.945` [dorland] AP: anteroposterior
    - `+0.847` [readme] anteroposterior: Front to back.
    - `+0.466` [michigan] lateral: The side or on the side.
    - `+0.462` [wiktionary] lateral: An object's lateral refers to the side of it.
    - `+0.218` [wiktionary] projections: A projection is when something juts out.

- rationale: "AP" is a medical shorthand for the anteroposterior direction, so "front-to-back" directly translates that spatial orientation into everyday words. Syllable count rises from 1 to 3. The reader can now visualize the body's directional plane without needing to decode a clinical abbreviation.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `lateral projections` -> `side views`**

- status: `attributed`
- log p full -0.3200, empty -0.5730
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.847` [wiktionary] projections: A projection is when something juts out.
    - `+0.401` [dorland] AP: anteroposterior
    - `+0.104` [dorland] AP: alkaline phosphatase
    - `-0.130` [readme] anteroposterior: Front to back.
    - `-0.282` [wiktionary] lateral: An object's lateral refers to the side of it.

- rationale: "Lateral projections" refers to images taken from the side, so "side views" conveys the same directional meaning in everyday terms. Phrase frequency rises from Zipf 3.43 to 4.75, and age of acquisition drops from 12.41 to 4.72. The reader can now immediately grasp the imaging angle without needing to decode clinical terminology.
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

**output:** The vocal cords move the way they should when the person makes sound and breathes.

| metric | value |
|---|---:|
| bertscore_f1 | 0.512 |
| coleman_liau | 8.13 |
| coleman_liau_drop | 6.44 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 3.63 |
| fkgl_drop | 4.55 |
| fre | 95.7 |
| fre_gain | 45.1 |
| human_edit_recall | 1.000 |
| length_ratio | 1.88 |
| n_words | 15.0 |
| nli_completeness | 0.980 |
| nli_faithfulness | 0.955 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 36.99 |
| smog | 3.13 |
| smog_drop | 8.08 |

### Stage 4 - arm `termonly`

**output:** The vocal folds move normally with breathing and making voice sounds.

| metric | value |
|---|---:|
| bertscore_f1 | 0.597 |
| coleman_liau | 12.09 |
| coleman_liau_drop | 2.48 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.667 |
| fkgl | 5.86 |
| fkgl_drop | 2.32 |
| fre | 72.6 |
| fre_gain | 21.9 |
| human_edit_recall | 1.000 |
| length_ratio | 1.38 |
| n_words | 11.0 |
| nli_completeness | 0.947 |
| nli_faithfulness | 0.945 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 34.07 |
| smog | 8.84 |
| smog_drop | 2.37 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `ventilation` -> `breathing` | replace | - | - | - | - | - | - | - |
| `phonation` -> `making voice sounds` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** The vocal folds move normally with speaking and breathing.

| metric | value |
|---|---:|
| bertscore_f1 | 0.724 |
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
| nli_completeness | 0.981 |
| nli_faithfulness | 0.984 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 41.98 |
| smog | 8.84 |
| smog_drop | 2.37 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `ventilation` -> `breathing` | replace | attributed | -0.000 | -0.391 | - | 0.878 | 2.374 | - |

**edit `ventilation` -> `breathing`**

- status: `attributed`
- log p full -0.0002, empty -0.0001
- masks scored: 34/34 (+2 top-k)
- ranked sources:
    - `+2.941` [wiktionary] ventilation: Ventilation is the bodily process of breathing; the inhalation of air to provide oxygen, and the 
    - `+0.567` [wiktionary] cords: A long, thin rope or wire.
    - `+0.319` [dictionary] Phonation (n.): The act or process by which articulate sounds are uttered; the utterance of articulate sounds;
    - `-0.362` [wiktionary] ventilation: Ventilation is the replacement of stale air with fresh air.
    - `-2.235` [readme] ventilation: Ventilation is about bringing in fresh air.

- rationale: Ventilation refers to the movement of air in and out of the lungs, so "breathing" conveys that same essential process in a more familiar word. Word frequency rises from Zipf 3.60 to 4.28, making the replacement much more common in everyday language. The reader can now immediately connect the instruction to their own natural experience of taking a breath.
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

**output:** Once the abdomen was opened, the doctors saw thick, pus-like fluid draining out.

| metric | value |
|---|---:|
| bertscore_f1 | 0.667 |
| coleman_liau | 10.48 |
| coleman_liau_drop | -1.34 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.250 |
| fkgl | 7.63 |
| fkgl_drop | 0.00 |
| fre | 63.5 |
| fre_gain | 0.0 |
| human_edit_recall | 1.000 |
| length_ratio | 0.93 |
| n_words | 14.0 |
| nli_completeness | 0.985 |
| nli_faithfulness | 0.403 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.400 |
| sari | 34.84 |
| smog | 8.84 |
| smog_drop | 2.37 |

### Stage 4 - arm `termonly`

**output:** Once the belly was opened, there was a thick, pus-like fluid leaking out.

| metric | value |
|---|---:|
| bertscore_f1 | 0.691 |
| coleman_liau | 7.35 |
| coleman_liau_drop | 1.78 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.400 |
| fkgl | 5.82 |
| fkgl_drop | 1.82 |
| fre | 76.5 |
| fre_gain | 13.0 |
| human_edit_recall | 1.000 |
| length_ratio | 0.93 |
| n_words | 14.0 |
| nli_completeness | 0.974 |
| nli_faithfulness | 0.882 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.200 |
| sari | 31.61 |
| smog | 3.13 |
| smog_drop | 8.08 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `abdomen` -> `belly` | replace | - | - | - | - | - | - | - |
| `gross purulent drainage` -> `thick, pus-like fluid leaking out` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Once the belly was opened, there was a large amount of pus leaking out.

| metric | value |
|---|---:|
| bertscore_f1 | 0.739 |
| coleman_liau | 5.29 |
| coleman_liau_drop | 3.85 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.800 |
| fkgl | 5.04 |
| fkgl_drop | 2.59 |
| fre | 83.9 |
| fre_gain | 20.4 |
| human_edit_recall | 1.000 |
| length_ratio | 0.93 |
| n_words | 14.0 |
| nli_completeness | 0.971 |
| nli_faithfulness | 0.883 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.200 |
| sari | 34.08 |
| smog | 3.13 |
| smog_drop | 8.08 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `abdomen` -> `belly` | replace | attributed | -0.009 | -5.896 | 0.853 | 0.871 | 0.530 | - |
| `gross purulent drainage` -> `a large amount of pus leaking out` | replace | attributed | 3.144 | 3.447 | 0.304 | 0.713 | 0.406 | - |

**edit `abdomen` -> `belly`**

- status: `attributed`
- log p full -0.0088, empty -0.0000
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+1.102` [wiktionary] gross: The gross amount is the total before you take away losses or expenses.
    - `+0.572` [wiktionary] gross: A gross violation or abuse is very bad and clearly wrong.
    - `+0.528` [wiktionary] drainage: To use a drainage is engage in the action or process of draining something.
    - `+0.367` [nih] abdomen: The area of the body that contains the pancreas, stomach, intestines, liver, gallbladder, and other o
    - `+0.194` [readme] DRAINAGE: Fluid leaving an organ or body area.

- rationale: "Abdomen" refers to the part of the body between the chest and pelvis, and "belly" conveys that same area in a more familiar, everyday word. Word frequency rises from Zipf 3.56 to 4.10, and age of acquisition drops from 8.61 to 4.05. This lets the reader immediately picture the body region without needing a formal anatomical label.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `gross purulent drainage` -> `a large amount of pus leaking out`**

- status: `attributed`
- log p full -1.3084, empty -4.4521
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+1.192` [readme] DRAINAGE: Fluid leaving an organ or body area.
    - `+0.786` [readme] drainage: When any fluid is leaking out of a body part.
    - `+0.490` [wiktionary] gross: The gross amount is the total before you take away losses or expenses.
    - `+0.356` [wiktionary] drainage: To use a drainage is engage in the action or process of draining something.
    - `+0.341` [michigan] purulent: Pus.

- rationale: Gross purulent drainage refers to a visible, thick fluid produced by infection, and saying "a large amount of pus leaking out" conveys that same idea in everyday words. Word frequency rises from Zipf 1.92 to 2.93, and age of acquisition drops from 15.50 to 7.78. This lets the reader immediately picture the sign of infection without needing clinical terminology.
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

**output:** Once all four ports were in place, the doctor looked around the right upper part of the belly.

| metric | value |
|---|---:|
| bertscore_f1 | 0.641 |
| coleman_liau | 6.72 |
| coleman_liau_drop | 2.86 |
| copy_jargon_rate | 0.500 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.333 |
| fkgl | 5.85 |
| fkgl_drop | -1.85 |
| fre | 85.2 |
| fre_gain | -4.3 |
| human_edit_recall | 0.500 |
| laterality_preservation | 1.000 |
| length_ratio | 1.12 |
| n_words | 18.0 |
| nli_completeness | 0.981 |
| nli_faithfulness | 0.298 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 30.63 |
| smog | 3.13 |
| smog_drop | 0.00 |

### Stage 4 - arm `termonly`

**output:** Once all four small openings were put in, the upper right side of the belly was then checked.

| metric | value |
|---|---:|
| bertscore_f1 | 0.736 |
| coleman_liau | 6.40 |
| coleman_liau_drop | 3.18 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.200 |
| fkgl | 5.85 |
| fkgl_drop | -1.85 |
| fre | 85.2 |
| fre_gain | -4.3 |
| human_edit_recall | 1.000 |
| laterality_preservation | 1.000 |
| length_ratio | 1.12 |
| n_words | 18.0 |
| nli_completeness | 0.979 |
| nli_faithfulness | 0.660 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.250 |
| sari | 42.65 |
| smog | 8.84 |
| smog_drop | -5.71 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `ports` -> `small openings` | replace | - | - | - | - | - | - | - |
| `right upper quadrant` -> `upper right side of the belly` | replace | - | - | - | - | - | - | - |
| `explored` -> `checked` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Once all four small openings were placed, the upper right part of the belly was then looked at carefully.

| metric | value |
|---|---:|
| bertscore_f1 | 0.747 |
| coleman_liau | 8.59 |
| coleman_liau_drop | 1.00 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.600 |
| fkgl | 7.35 |
| fkgl_drop | -3.34 |
| fre | 76.2 |
| fre_gain | -13.3 |
| human_edit_recall | 1.000 |
| laterality_preservation | 1.000 |
| length_ratio | 1.19 |
| n_words | 19.0 |
| nli_completeness | 0.972 |
| nli_faithfulness | 0.547 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 51.37 |
| smog | 11.21 |
| smog_drop | -8.08 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `ports` -> `small openings` | replace | attributed | -0.061 | -0.161 | -0.007 | 0.531 | 0.017 | - |
| `right upper quadrant` -> `upper right part of the belly` | replace | attributed | 0.532 | 1.280 | 0.153 | 0.723 | 0.306 | - |
| `explored` -> `looked at carefully` | replace | attributed | 2.493 | 2.659 | 0.824 | 0.870 | 3.026 | - |

**edit `ports` -> `small openings`**

- status: `attributed`
- log p full -0.5081, empty -0.4471
- masks scored: 66/66 (+5 top-k)
- ranked sources:
    - `+0.131` [readme] right upper lobe: A section of the right lung.
    - `+0.114` [dictionary] Quadrant (n.): The quarter of a circle, or of the circumference of a circle, an arc of 90, or one subtending a
    - `+0.041` [dictionary] Quadrant (n.): The fourth part; the quarter.
    - `-0.023` [wiktionary] explored: If you explore a possibility, plan, idea, etc. you think about it carefully.
    - `-0.390` [readme] Right Upper Lobe: The upper right part of the right lung.

- rationale: "Ports" refers to access points on the body, so "small openings" conveys that same idea of an entry site in everyday words. Word frequency moves from Zipf 4.07 to 3.70, making the replacement slightly less common but still familiar. The reader can now picture the physical access location without needing the clinical shorthand.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `right upper quadrant` -> `upper right part of the belly`**

- status: `attributed`
- log p full -0.3149, empty -0.8465
- masks scored: 66/66 (+5 top-k)
- ranked sources:
    - `+0.468` [dictionary] Quadrant (n.): The fourth part; the quarter.
    - `+0.161` [dictionary] Quadrant (n.): The quarter of a circle, or of the circumference of a circle, an arc of 90, or one subtending a
    - `-0.037` [wiktionary] explored: If you explore a possibility, plan, idea, etc. you think about it carefully.
    - `-0.082` [wiktionary] ports: A port is a place for ships to stop to trade or refuel.
    - `-0.120` [readme] right upper lobe: A section of the right lung.

- rationale: "Right upper quadrant" refers to a specific anatomical zone of the abdomen, and "upper right part of the belly" conveys that same location using everyday words. Phrase frequency rises from Zipf 3.26 to 3.99, and age of acquisition drops from 12.76 to 7.56. This lets the reader pinpoint the area being discussed without needing to know clinical directional terms.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `explored` -> `looked at carefully`**

- status: `attributed`
- log p full -1.8049, empty -4.2980
- masks scored: 66/66 (+5 top-k)
- ranked sources:
    - `+3.092` [wiktionary] explored: If you explore a possibility, plan, idea, etc. you think about it carefully.
    - `+0.066` [dictionary] Quadrant (n.): The fourth part; the quarter.
    - `-0.089` [wiktionary] ports: A port is a place for ships to stop to trade or refuel.
    - `-0.292` [readme] right upper lobe: A section of the right lung.

- rationale: "Explored" is defined by Wiktionary as thinking about a possibility or idea carefully, so "looked at carefully" directly conveys that same deliberate consideration in everyday words. Word frequency rises from Zipf 3.90 to 4.37, making the replacement more commonly encountered. The reader now understands that a thoughtful, detailed examination took place, without needing to interpret the more abstract verb.
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

**output:** Options like watchful waiting, robotic surgery to remove the prostate, and seed implants with or without radiation were discussed.

| metric | value |
|---|---:|
| bertscore_f1 | 0.693 |
| coleman_liau | 15.92 |
| coleman_liau_drop | 4.98 |
| copy_jargon_rate | 0.333 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 12.94 |
| fkgl_drop | 2.50 |
| fre | 36.2 |
| fre_gain | 25.0 |
| human_edit_recall | 0.667 |
| length_ratio | 0.83 |
| n_words | 19.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.995 |
| nli_faithfulness | 0.993 |
| replacement_f1 | 0.800 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 32.68 |
| smog | 13.02 |
| smog_drop | 1.53 |

### Stage 4 - arm `termonly`

**output:** Options such as close follow-up without treatment right away, surgery to remove the prostate with a robot, placing tiny radioactive seeds with and without high-energy rays were discussed.

| metric | value |
|---|---:|
| bertscore_f1 | 0.571 |
| coleman_liau | 15.25 |
| coleman_liau_drop | 5.64 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.571 |
| fkgl | 16.40 |
| fkgl_drop | -0.97 |
| fre | 27.3 |
| fre_gain | 16.2 |
| human_edit_recall | 1.000 |
| length_ratio | 1.30 |
| n_words | 30.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.993 |
| nli_faithfulness | 0.929 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 39.54 |
| smog | 14.55 |
| smog_drop | 0.00 |

annotation backend `novita`, 4 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `watchful waiting` -> `close follow-up without treatment right away` | replace | - | - | - | - | - | - | - |
| `robotic prostatectomy` -> `surgery to remove the prostate with a robot` | replace | - | - | - | - | - | - | - |
| `seed implantation` -> `placing tiny radioactive seeds` | replace | - | - | - | - | - | - | - |
| `radiation` -> `high-energy rays` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Options such as close monitoring without treatment right away, surgery with a robot to remove the prostate, placing tiny devices with and without high-energy rays to kill cancer cells were discussed.

| metric | value |
|---|---:|
| bertscore_f1 | 0.536 |
| coleman_liau | 14.12 |
| coleman_liau_drop | 6.78 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.571 |
| fkgl | 16.67 |
| fkgl_drop | -1.24 |
| fre | 30.7 |
| fre_gain | 19.6 |
| human_edit_recall | 1.000 |
| length_ratio | 1.39 |
| n_words | 32.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.886 |
| nli_faithfulness | 0.853 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 38.55 |
| smog | 14.55 |
| smog_drop | 0.00 |

annotation backend `novita`, 4 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `watchful waiting` -> `close monitoring without treatment right away` | replace | attributed | 2.848 | 3.113 | 0.622 | 0.894 | 1.054 | - |
| `robotic prostatectomy` -> `surgery with a robot to remove the prostate` | replace | attributed | 0.788 | 1.902 | 0.564 | 0.901 | 0.585 | - |
| `seed implantation` -> `placing tiny devices` | replace | attributed | 6.884 | 7.921 | 0.653 | 0.938 | 1.206 | - |
| `radiation` -> `high-energy rays to kill cancer cells` | replace | attributed | 2.726 | 2.942 | 0.854 | 0.922 | 8.096 | - |

**edit `watchful waiting` -> `close monitoring without treatment right away`**

- status: `attributed`
- log p full -1.4147, empty -4.2630
- masks scored: 66/66 (+8 top-k)
- ranked sources:
    - `+1.382` [nih] watchful waiting: Closely watching a patient’s condition but not giving treatment unless symptoms appear or ch
    - `+0.329` [readme] Radiation: Radiation is powerful energy waves that are sometimes utilized to destroy cancer cells.
    - `+0.203` [wiktionary] radiation: Radiation is the emission or transmission of energy in the form of waves or particles through space
    - `+0.180` [readme] implantation: Surgery where a device is placed inside your body.
    - `+0.103` [readme] radiation: High energy rays used to kill cancer cells.

- rationale: The NIH glossary defines watchful waiting as closely observing a condition without starting treatment unless symptoms shift, so "close monitoring without treatment right away" conveys that same cautious approach in everyday terms. Phrase frequency rises from Zipf 3.09 to 4.18, making the replacement more familiar in common usage. Patients can now grasp that their care involves attentive tracking rather than immediate intervention, without needing to decode a clinical idiom.
- audit: coverage 0.667, grounding_error=False, omission=True, source_ok=True, passage_ok=True

**edit `robotic prostatectomy` -> `surgery with a robot to remove the prostate`**

- status: `attributed`
- log p full -0.2364, empty -1.0246
- masks scored: 66/66 (+8 top-k)
- ranked sources:
    - `+1.150` [nih] prostatectomy: Surgery to remove part or all of the prostate and some of the tissue around it, including the s
    - `+0.565` [wiktionary] seed: The seed of a man is his semen.
    - `+0.342` [readme] Radiation: Radiation is powerful energy waves that are sometimes utilized to destroy cancer cells.
    - `+0.180` [readme] implantation: Surgery where a device is placed inside your body.
    - `+0.055` [wiktionary] seed: A seed is a small round thing that can grow to be a plant, a flower or a tree.

- rationale: The NIH glossary defines a prostatectomy as surgery to remove the prostate and surrounding tissue, so the replacement "surgery with a robot to remove the prostate" conveys the same procedure in everyday terms. Phrase frequency rises from Zipf 2.13 to 3.50, and age of acquisition drops slightly from 15.27 to 15.00. This lets the reader grasp the core action and the tool used without needing to decode the formal medical name.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `seed implantation` -> `placing tiny devices`**

- status: `attributed`
- log p full -0.4374, empty -7.3211
- masks scored: 66/66 (+8 top-k)
- ranked sources:
    - `+3.684` [readme] implantation: Surgery where a device is placed inside your body.
    - `+2.478` [nih] watchful waiting: Closely watching a patient’s condition but not giving treatment unless symptoms appear or ch
    - `+1.444` [wiktionary] seed: A seed is a small round thing that can grow to be a plant, a flower or a tree.
    - `+1.372` [readme] radiation: High energy rays used to kill cancer cells.
    - `+1.315` [readme] IMPLANTATION: A surgery where a device is placed inside the body.

- rationale: The glossary explains seed implantation as a surgery where a device is placed inside the body, so "placing tiny devices" conveys that same action in everyday terms. Word frequency rises from Zipf 2.99 to 3.93, and age of acquisition drops from 11.95 to 5.33. Readers can now grasp the procedure without needing to interpret the specialized medical meaning of "seed."
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `radiation` -> `high-energy rays to kill cancer cells`**

- status: `attributed`
- log p full -1.5826, empty -4.3083
- masks scored: 66/66 (+8 top-k)
- ranked sources:
    - `+9.717` [readme] radiation: High energy rays used to kill cancer cells.
    - `+1.621` [nih] radiation: Energy released in the form of particle or electromagnetic waves. Common sources of radiation inclu
    - `+0.668` [readme] Radiation: Radiation is powerful energy waves that are sometimes utilized to destroy cancer cells.
    - `+0.564` [nih] watchful waiting: Closely watching a patient’s condition but not giving treatment unless symptoms appear or ch
    - `+0.412` [readme] prostatectomy: A prostatectomy is a surgery to remove part or all of the prostate and some surrounding tissue.

- rationale: The glossary defines radiation as high-energy rays used to kill cancer cells, so the replacement directly conveys that therapeutic purpose in everyday terms. Word frequency shifts from Zipf 4.27 to 3.86, while age of acquisition drops from 11.44 to 8.39. Readers can now grasp the treatment's function without needing prior knowledge of the medical term.
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

**output:** He was also taking a water pill called Lasix before he went to the hospital, but that is not certain.

| metric | value |
|---|---:|
| bertscore_f1 | 0.507 |
| coleman_liau | 5.92 |
| coleman_liau_drop | 7.80 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.667 |
| fkgl | 8.14 |
| fkgl_drop | 6.13 |
| fre | 72.3 |
| fre_gain | 61.8 |
| human_edit_recall | 1.000 |
| length_ratio | 1.33 |
| n_words | 20.0 |
| nli_completeness | 0.964 |
| nli_faithfulness | 0.083 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.250 |
| sari | 39.09 |
| smog | 8.84 |
| smog_drop | 4.18 |
| temporality_preservation | 1.000 |
| uncertainty_preservation | 0.000 |

### Stage 4 - arm `termonly`

**output:** He also was said to be on a water pill before his hospital stay.

| metric | value |
|---|---:|
| bertscore_f1 | 0.612 |
| coleman_liau | 2.80 |
| coleman_liau_drop | 10.92 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 5.88 |
| fkgl_drop | 8.39 |
| fre | 77.8 |
| fre_gain | 67.2 |
| human_edit_recall | 1.000 |
| length_ratio | 0.93 |
| n_words | 14.0 |
| nli_completeness | 0.012 |
| nli_faithfulness | 0.003 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.200 |
| sari | 49.24 |
| smog | 8.84 |
| smog_drop | 4.18 |
| temporality_preservation | 1.000 |
| uncertainty_preservation | 0.000 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `reportedly` -> `was said to be` | replace | - | - | - | - | - | - | - |
| `Lasix` -> `a water pill` | replace | - | - | - | - | - | - | - |
| `hospitalization` -> `hospital stay` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** He also, people say, was on a water pill before his hospital stay.

| metric | value |
|---|---:|
| bertscore_f1 | 0.576 |
| coleman_liau | 4.68 |
| coleman_liau_drop | 9.04 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.750 |
| fkgl | 6.73 |
| fkgl_drop | 7.54 |
| fre | 70.0 |
| fre_gain | 59.4 |
| human_edit_recall | 1.000 |
| length_ratio | 0.87 |
| n_words | 13.0 |
| nli_completeness | 0.063 |
| nli_faithfulness | 0.004 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.200 |
| sari | 43.78 |
| smog | 8.84 |
| smog_drop | 4.18 |
| temporality_preservation | 1.000 |
| uncertainty_preservation | 0.000 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `reportedly` -> `people say` | replace | attributed | 5.345 | 6.064 | 0.775 | 0.865 | 6.857 | - |
| `Lasix` -> `a water pill` | replace | attributed | 0.010 | 0.191 | 0.390 | 0.325 | 0.171 | - |

**edit `reportedly` -> `people say`**

- status: `attributed`
- log p full -0.6656, empty -6.0110
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+7.100` [wiktionary] reportedly: If something is reportedly true, people say it happened, but we don't have other reasons to believ
    - `+0.243` [michigan] prior to: Earlier or before.
    - `-0.047` [readme] Hospitalization: Being admitted to a hospital for an extended period of time.
    - `-0.228` [readme] hospitalization: Being admitted to and staying in a hospital.

- rationale: The Wiktionary entry explains that "reportedly" means something is claimed to be true without other proof, so "people say" directly conveys that reliance on hearsay. Word frequency rises from Zipf 4.13 to 5.73, making the replacement more common. The reader can now grasp that the information comes from general talk rather than verified fact.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `Lasix` -> `a water pill`**

- status: `attributed`
- log p full -0.0465, empty -0.0560
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.247` [michigan] prior to: Earlier or before.
    - `+0.076` [wiktionary] hospitalization: Hospitalization is the process of putting a person in hospital for medical care.
    - `+0.064` [readme] Hospitalization: Being admitted to a hospital for an extended period of time.
    - `+0.044` [readme] hospitalization: Being admitted to and staying in a hospital.

- rationale: Lasix is a brand-name diuretic that helps the body get rid of extra fluid, so calling it "a water pill" plainly describes that same function. Word frequency rises sharply from Zipf 1.98 to 4.02. The reader can now recognize the medication’s purpose without needing to know its proprietary name.
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

**output:** The four heart spaces are normal in size.

| metric | value |
|---|---:|
| bertscore_f1 | 0.488 |
| coleman_liau | 4.43 |
| coleman_liau_drop | 10.64 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.143 |
| fkgl | 2.28 |
| fkgl_drop | 7.93 |
| fre | 93.0 |
| fre_gain | 55.1 |
| human_edit_recall | 1.000 |
| length_ratio | 0.62 |
| n_words | 8.0 |
| nli_completeness | 0.957 |
| nli_faithfulness | 0.967 |
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
| `cardiac chambers` -> `heart spaces` | replace | - | - | - | - | - | - | - |
| `within normal limits` -> `normal in size` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

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
| `cardiac chambers` -> `heart rooms` | replace | attributed | 3.732 | 5.903 | 0.728 | 0.897 | 6.739 | - |
| `within normal limits` -> `normal in size` | replace | attributed | -1.469 | -2.159 | 0.740 | 0.823 | 0.242 | - |

**edit `cardiac chambers` -> `heart rooms`**

- status: `attributed`
- log p full -0.1184, empty -3.8508
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+7.349` [wiktionary] chambers: A chamber is a room that is often used for sleeping.
    - `+0.610` [nih] cardiac: Having to do with the heart.
    - `+0.539` [wiktionary] normal: A normal thing, or situation, is one that is not special.
    - `+0.332` [justplainclear] normal: Whats expected for a person similar to you or to what's usual for you
    - `+0.175` [wiktionary] within: before the time ends

- rationale: The glossary defines a chamber as a room, so "heart rooms" directly translates the anatomical term into a familiar spatial concept. Word frequency rises from Zipf 3.64 to 4.49, and age of acquisition drops from 11.74 to 5.17. This lets the reader picture the heart's internal sections without needing to know the medical word "chambers."
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `within normal limits` -> `normal in size`**

- status: `attributed`
- log p full -2.0416, empty -0.5731
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.351` [wiktionary] cardiac: Something that is cardiac is related to the heart.
    - `+0.109` [michigan] cardiac: Related to your heart.

- rationale: "Within normal limits" means a finding is not abnormally large or small, and "normal in size" conveys that same idea using everyday words. Phrase frequency rises from Zipf 4.32 to 4.76, while age of acquisition drops from 7.65 to 5.53. The reader can now grasp that the measurement is unremarkable without encountering clinical phrasing.
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

**output:** A doctor checked the patient's rectum with a gloved finger and found no lumps.

| metric | value |
|---|---:|
| bertscore_f1 | 0.414 |
| coleman_liau | 8.19 |
| coleman_liau_drop | 8.17 |
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
| nli_completeness | 0.744 |
| nli_faithfulness | 0.053 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.286 |
| sari | 22.68 |
| smog | 3.13 |
| smog_drop | 8.08 |

### Stage 4 - arm `termonly`

**output:** A doctor checked inside the patient's rectum with a gloved finger and found no lumps.

| metric | value |
|---|---:|
| bertscore_f1 | 0.406 |
| coleman_liau | 8.91 |
| coleman_liau_drop | 7.45 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.333 |
| fkgl | 5.99 |
| fkgl_drop | 5.53 |
| fre | 78.8 |
| fre_gain | 50.3 |
| human_edit_recall | 1.000 |
| length_ratio | 1.45 |
| n_words | 16.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.799 |
| nli_faithfulness | 0.085 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.286 |
| sari | 22.54 |
| smog | 3.13 |
| smog_drop | 8.08 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `masses` -> `lumps` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** The doctor did a finger check of the rectum and felt no lumps.

| metric | value |
|---|---:|
| bertscore_f1 | 0.503 |
| coleman_liau | 3.78 |
| coleman_liau_drop | 12.57 |
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
| nli_completeness | 0.455 |
| nli_faithfulness | 0.224 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.286 |
| sari | 24.97 |
| smog | 3.13 |
| smog_drop | 8.08 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `Digital rectal examination` -> `finger check of the rectum` | replace | attributed | 0.073 | 0.105 | - | 0.738 | 0.003 | - |
| `masses` -> `lumps` | replace | attributed | -0.006 | -0.757 | - | 0.394 | 0.299 | - |

**edit `Digital rectal examination` -> `finger check of the rectum`**

- status: `attributed`
- log p full -1.1467, empty -1.2196
- masks scored: 18/18 (+4 top-k)
- ranked sources:
    - `+0.300` [wiktionary] masses: A measure of how much material is in something.
    - `+0.297` [wiktionary] masses: The masses are the regular people, not those in power.
    - `-0.225` [wiktionary] performed: When you perform something, you do it.
    - `-0.473` [nih] digital rectal examination: An examination in which a doctor inserts a lubricated, gloved finger into the rect

- rationale: A digital rectal examination is a procedure where a doctor inserts a gloved finger into the rectum to feel for abnormalities, so "finger check of the rectum" conveys the same action in straightforward terms. Word frequency rises slightly from Zipf 2.88 to 2.94, while age of acquisition drops from 13.06 to 9.84. This lets the reader grasp the hands-on nature of the exam without needing clinical vocabulary.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `masses` -> `lumps`**

- status: `attributed`
- log p full -0.0113, empty -0.0053
- masks scored: 18/18 (+4 top-k)
- ranked sources:
    - `+0.278` [wiktionary] performed: When you perform something, you do it.
    - `-0.020` [wiktionary] masses: The masses are the regular people, not those in power.
    - `-0.043` [nih] digital rectal examination: An examination in which a doctor inserts a lubricated, gloved finger into the rect
    - `-0.102` [wiktionary] masses: A measure of how much material is in something.

- rationale: "Masses" refers to abnormal growths or clusters of tissue in the body, and "lumps" conveys that same idea of a detectable swelling in simpler terms. Word frequency drops from Zipf 3.94 to 3.19, while syllables are reduced from two to one. The reader can now recognize the symptom being discussed without needing clinical vocabulary.
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

**output:** He then had a problem with seizures and weakness on one side of his body. He has been to the hospital, got a C-diff infection, and is now in a nursing home.

| metric | value |
|---|---:|
| bertscore_f1 | 0.680 |
| coleman_liau | 4.10 |
| coleman_liau_drop | 6.17 |
| copy_jargon_rate | 0.667 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 6.14 |
| fkgl_drop | 5.09 |
| fre | 79.6 |
| fre_gain | 25.8 |
| human_edit_recall | 0.333 |
| length_ratio | 1.14 |
| n_words | 33.0 |
| nli_completeness | 0.017 |
| nli_faithfulness | 0.948 |
| replacement_f1 | 0.500 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.667 |
| sari | 48.23 |
| smog | 8.84 |
| smog_drop | 5.71 |
| temporality_preservation | 1.000 |

### Stage 4 - arm `termonly`

**output:** He then had a problem with sudden body shakes, weakness on one side of the body, has been to the hospital, got a gut infection that causes loose stools, and is in the nursing home now.

| metric | value |
|---|---:|
| bertscore_f1 | 0.748 |
| coleman_liau | 6.58 |
| coleman_liau_drop | 3.69 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 13.86 |
| fkgl_drop | -2.63 |
| fre | 59.8 |
| fre_gain | 6.1 |
| human_edit_recall | 1.000 |
| length_ratio | 1.24 |
| n_words | 36.0 |
| nli_completeness | 0.231 |
| nli_faithfulness | 0.701 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.400 |
| sari | 63.15 |
| smog | 11.21 |
| smog_drop | 3.35 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `seizures` -> `sudden body shakes` | replace | - | - | - | - | - | - | - |
| `hemiparesis` -> `weakness on one side of the body` | replace | - | - | - | - | - | - | - |
| `C-diff` -> `a gut infection that causes loose stools` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** He then had a problem with fits, weakness on one side of his body, has been to the hospital, got a gut infection that causes diarrhea, and is in the nursing home now.

| metric | value |
|---|---:|
| bertscore_f1 | 0.859 |
| coleman_liau | 5.98 |
| coleman_liau_drop | 4.30 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.667 |
| fkgl | 13.37 |
| fkgl_drop | -2.14 |
| fre | 58.0 |
| fre_gain | 4.2 |
| human_edit_recall | 1.000 |
| length_ratio | 1.14 |
| n_words | 33.0 |
| nli_completeness | 0.458 |
| nli_faithfulness | 0.826 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.400 |
| sari | 68.70 |
| smog | 13.02 |
| smog_drop | 1.53 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `seizures` -> `fits` | replace | attributed | 0.163 | 0.418 | 0.514 | 0.663 | 0.398 | - |
| `hemiparesis` -> `weakness on one side of his body` | replace | attributed | 0.969 | 1.668 | 0.762 | 0.934 | 2.622 | - |
| `C-diff` -> `a gut infection that causes diarrhea` | replace | attributed | 6.918 | 8.510 | 0.910 | 0.860 | 2.655 | - |

**edit `seizures` -> `fits`**

- status: `attributed`
- log p full -0.4187, empty -0.5821
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+1.058` [wiktionary] seizures: If someone seizes (takes) something from someone by force, or arrests someone, it is a seizure.
    - `+0.660` [readme] seizures: Seizures are when the brain has strange electrical activity that may make someone lose consciousness
    - `-0.194` [readme] Clostridium difficile colitis: A type of gut infection that causes symptoms like fever, diarrhea, and cramps.
    - `-0.670` [readme] Seizures: Seizures are when the brain has sudden abnormal activity that can lead to loss of consciousness and 

- rationale: "Seizures" refers to sudden, uncontrolled electrical disturbances in the brain, and "fits" conveys this same idea of a temporary attack or convulsion in everyday language. Word frequency rises from Zipf 3.59 to 4.27, making the replacement more familiar. The reader can now grasp the event being described without needing the clinical term.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `hemiparesis` -> `weakness on one side of his body`**

- status: `attributed`
- log p full -0.4777, empty -1.4464
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+3.183` [readme] hemiparesis: Weakness on one side of the body.
    - `+0.561` [readme] seizures: Seizures are when the brain has strange electrical activity that may make someone lose consciousness
    - `-0.104` [dorland] C-diff: Clostridioides difficile

- rationale: The glossary defines hemiparesis as weakness on one side of the body, so the replacement directly states that meaning in everyday terms. Word frequency rises sharply from Zipf 1.49 to 4.14, making the phrase far more common and recognizable. The reader can now immediately grasp the physical limitation without needing to decode a rare medical term.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `C-diff` -> `a gut infection that causes diarrhea`**

- status: `attributed`
- log p full -0.2273, empty -7.1449
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+5.919` [readme] Clostridium difficile colitis: A type of gut infection that causes symptoms like fever, diarrhea, and cramps.
    - `+3.264` [nih] Clostridium difficile: A type of bacterium found in human and animal waste. Clostridium difficile is a common 
    - `+0.837` [readme] Seizures: Seizures are when the brain has sudden abnormal activity that can lead to loss of consciousness and 
    - `+0.651` [wiktionary] seizures: If someone seizes (takes) something from someone by force, or arrests someone, it is a seizure.

- rationale: The glossary explains C-diff as a gut infection with symptoms like fever, diarrhea, and cramps, so "a gut infection that causes diarrhea" captures the core condition in everyday terms. Syllable count rises from 2 to 12, reflecting the shift from a compact abbreviation to a full descriptive phrase. Patients can now recognize the illness by its effects rather than needing to decode a clinical shorthand.
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

**output:** He has been using a continuous positive airway pressure machine for several months and is back for a follow-up visit to check how well the treatment is working.

| metric | value |
|---|---:|
| bertscore_f1 | 0.670 |
| coleman_liau | 10.28 |
| coleman_liau_drop | 2.37 |
| copy_jargon_rate | 0.833 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 13.45 |
| fkgl_drop | -1.15 |
| fre | 48.5 |
| fre_gain | 2.4 |
| human_edit_recall | 0.167 |
| length_ratio | 1.16 |
| n_words | 29.0 |
| nli_completeness | 0.992 |
| nli_faithfulness | 0.946 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 0.286 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.600 |
| sari | 50.87 |
| smog | 13.02 |
| smog_drop | 0.00 |
| temporality_preservation | 0.000 |

### Stage 4 - arm `termonly`

**output:** He has been on a steady air pressure mask for several months, and comes back for a checkup to see how well it is working.

| metric | value |
|---|---:|
| bertscore_f1 | 0.718 |
| coleman_liau | 5.06 |
| coleman_liau_drop | 7.59 |
| copy_jargon_rate | 0.167 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.200 |
| fkgl | 8.32 |
| fkgl_drop | 3.98 |
| fre | 79.9 |
| fre_gain | 33.9 |
| human_edit_recall | 0.833 |
| length_ratio | 1.00 |
| n_words | 25.0 |
| nli_completeness | 0.848 |
| nli_faithfulness | 0.932 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 0.909 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.444 |
| sari | 47.11 |
| smog | 3.13 |
| smog_drop | 9.89 |
| temporality_preservation | 0.000 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `continuous positive airway pressure` -> `a steady air pressure mask` | replace | - | - | - | - | - | - | - |
| `followup` -> `comes back for a checkup` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** He has been on a steady stream of air through a mask for several months, and comes back for a checkup to see how he is doing with the treatment.

| metric | value |
|---|---:|
| bertscore_f1 | 0.775 |
| coleman_liau | 5.06 |
| coleman_liau_drop | 7.59 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.167 |
| fkgl | 9.88 |
| fkgl_drop | 2.42 |
| fre | 77.7 |
| fre_gain | 31.6 |
| human_edit_recall | 1.000 |
| length_ratio | 1.20 |
| n_words | 30.0 |
| nli_completeness | 0.975 |
| nli_faithfulness | 0.599 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 56.39 |
| smog | 3.13 |
| smog_drop | 9.89 |
| temporality_preservation | 0.000 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `continuous positive airway pressure` -> `a steady stream of air through a mask` | replace | attributed | -0.227 | -0.244 | 0.518 | 0.762 | 0.758 | - |
| `followup` -> `comes back for a checkup` | replace | attributed | 1.317 | 1.712 | 0.808 | 0.831 | 3.196 | - |

**edit `continuous positive airway pressure` -> `a steady stream of air through a mask`**

- status: `attributed`
- log p full -2.7935, empty -2.5662
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.917` [readme] continuous: Continuous means something that never stops or has interruptions.
    - `+0.159` [readme] Positive: Something is there.
    - `+0.109` [readme] POSITIVE: Something is good or beneficial.
    - `+0.066` [wiktionary] pressure: In science, pressure is force applied over an area.

- rationale: Continuous positive airway pressure refers to a machine that pushes air at a set pressure to keep the throat open during sleep, and "a steady stream of air through a mask" conveys that same idea in everyday terms. Phrase frequency rises from Zipf 3.14 to 3.89, while age of acquisition drops from 11.39 to 6.70. This lets the reader grasp how the therapy works without needing to decode the clinical name.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `followup` -> `comes back for a checkup`**

- status: `attributed`
- log p full -0.9226, empty -2.2400
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+4.488` [readme] followup: Going back to your doctor for a checkup or follow-up appointment.
    - `+1.293` [wiktionary] positive: If you are positive about something, you are sure that you are not mistaken.
    - `+0.810` [wiktionary] pressure: If a person is under pressure, they feel stressed.
    - `+0.246` [readme] POSITIVE: Something is good or beneficial.
    - `+0.205` [wiktionary] continuous: Something that is continuous happens without stopping.

- rationale: "Followup" refers to returning for a medical appointment, so "comes back for a checkup" conveys that same idea in everyday words. Word frequency stays nearly identical, moving only from Zipf 2.87 to 2.88. The reader can now grasp the need for a return visit without interpreting clinical shorthand.
- audit: coverage 0.75, grounding_error=False, omission=False, source_ok=False, passage_ok=True

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

**output:** The patient should take small bites and small sips to help lower the chance of food or liquid going down the wrong way.

| metric | value |
|---|---:|
| bertscore_f1 | 0.711 |
| coleman_liau | 7.12 |
| coleman_liau_drop | 2.50 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 7.23 |
| fkgl_drop | 1.24 |
| fre | 84.2 |
| fre_gain | 17.8 |
| human_edit_recall | 1.000 |
| length_ratio | 0.77 |
| n_words | 23.0 |
| nli_completeness | 0.292 |
| nli_faithfulness | 0.665 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.600 |
| sari | 39.20 |
| severity_downgrade | 0.000 |
| severity_preservation | 1.000 |
| severity_tier_input | 1.000 |
| severity_tier_output | 1.000 |
| smog | 3.13 |
| smog_drop | 8.08 |

### Stage 4 - arm `termonly`

**output:** The patient should take small bites and small sips to help lower the risk of food or liquid going into the airway and entering the lungs.

| metric | value |
|---|---:|
| bertscore_f1 | 0.669 |
| coleman_liau | 7.82 |
| coleman_liau_drop | 1.80 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 9.98 |
| fkgl_drop | -1.51 |
| fre | 69.8 |
| fre_gain | 3.5 |
| human_edit_recall | 1.000 |
| length_ratio | 0.87 |
| n_words | 26.0 |
| nli_completeness | 0.836 |
| nli_faithfulness | 0.697 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 38.74 |
| severity_downgrade | 0.000 |
| severity_preservation | 1.000 |
| severity_tier_input | 1.000 |
| severity_tier_output | 1.000 |
| smog | 8.84 |
| smog_drop | 2.37 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `aspiration` -> `food or liquid going into the airway` | replace | - | - | - | - | - | - | - |
| `penetration` -> `entering the lungs` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** The patient should take small bites and small sips to help lower the risk of food or liquid going into the airway or lungs.

| metric | value |
|---|---:|
| bertscore_f1 | 0.656 |
| coleman_liau | 6.89 |
| coleman_liau_drop | 2.73 |
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
| nli_completeness | 0.769 |
| nli_faithfulness | 0.735 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 38.85 |
| severity_downgrade | 0.000 |
| severity_preservation | 1.000 |
| severity_tier_input | 1.000 |
| severity_tier_output | 1.000 |
| smog | 3.13 |
| smog_drop | 8.08 |

annotation backend `novita`, 0 edits kept


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

**output:** The patient was woken up, had her breathing tube removed, and was taken to the recovery room in good condition.

| metric | value |
|---|---:|
| bertscore_f1 | 0.699 |
| coleman_liau | 8.53 |
| coleman_liau_drop | 5.02 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.667 |
| fkgl | 9.32 |
| fkgl_drop | 2.97 |
| fre | 63.9 |
| fre_gain | 30.2 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 20.0 |
| nli_completeness | 0.992 |
| nli_faithfulness | 0.934 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.250 |
| sari | 33.74 |
| smog | 11.21 |
| smog_drop | 4.70 |

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

**output:** The patient was woken up, had the breathing tube taken out, and was moved to the recovery room in good enough condition.

| metric | value |
|---|---:|
| bertscore_f1 | 0.716 |
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
| nli_completeness | 0.992 |
| nli_faithfulness | 0.986 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 37.15 |
| smog | 11.21 |
| smog_drop | 4.70 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `awakened` -> `woken up` | replace | attributed | 0.001 | 0.102 | - | 0.705 | 0.266 | - |
| `extubated` -> `had the breathing tube taken out` | replace | attributed | 0.634 | 0.956 | - | 0.866 | 1.171 | - |
| `satisfactory` -> `good enough` | replace | attributed | 8.477 | 8.715 | - | 0.924 | 10.799 | - |

**edit `awakened` -> `woken up`**

- status: `attributed`
- log p full -0.0089, empty -0.0098
- masks scored: 34/34 (+6 top-k)
- ranked sources:
    - `+0.432` [readme] extubated: Not having a breathing tube anymore.
    - `+0.166` [michigan] satisfactory: When something is okay or good.
    - `+0.050` [wiktionary] satisfactory: If something is satisfactory, it is good enough.
    - `+0.043` [readme] extubated: Taking out a tube used for breathing.
    - `-0.780` [wiktionary] awakened: If you awaken somebody, they stop sleeping because of something you do.

- rationale: "Awakened" means roused from sleep, and "woken up" conveys the same idea in a more everyday, conversational way. Word frequency rises slightly from Zipf 3.30 to 3.37, making the replacement a touch more familiar. The reader can immediately grasp the action without the slightly formal tone of the original term.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `extubated` -> `had the breathing tube taken out`**

- status: `attributed`
- log p full -0.8062, empty -1.4406
- masks scored: 34/34 (+6 top-k)
- ranked sources:
    - `+1.171` [readme] extubated: Taking out a tube used for breathing.

- rationale: "Extubated" means removing a breathing tube from a patient's airway, so "had the breathing tube taken out" describes the exact same procedure in everyday terms. Word frequency rises sharply from Zipf 1.26 to 3.99, making the replacement far more familiar. Readers can now grasp the event without needing clinical vocabulary.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `satisfactory` -> `good enough`**

- status: `attributed`
- log p full -1.5526, empty -10.0294
- masks scored: 34/34 (+6 top-k)
- ranked sources:
    - `+10.999` [wiktionary] satisfactory: If something is satisfactory, it is good enough.
    - `+0.200` [wiktionary] awakened: If you awaken somebody, they stop sleeping because of something you do.
    - `-0.617` [readme] extubated: Taking out a tube used for breathing.
    - `-2.497` [michigan] satisfactory: When something is okay or good.

- rationale: "Satisfactory" means meeting a basic standard, and "good enough" conveys that same idea of adequacy without implying anything more. Word frequency rises from Zipf 3.57 to 5.44, and age of acquisition drops from 8.84 to 6.96. The reader now gets a clear, everyday judgment instead of a formal rating.
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

**output:** The patient was asleep, but she woke up easily when someone tried to rouse her.

| metric | value |
|---|---:|
| bertscore_f1 | 0.668 |
| coleman_liau | 6.59 |
| coleman_liau_drop | 10.03 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 5.99 |
| fkgl_drop | 9.46 |
| fre | 78.8 |
| fre_gain | 76.7 |
| human_edit_recall | 1.000 |
| length_ratio | 1.88 |
| n_words | 15.0 |
| nli_completeness | 0.445 |
| nli_faithfulness | 0.348 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 59.40 |
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
| `aroused` -> `woken up` | replace | failed | - | - | - | - | - | - |

**edit `aroused` -> `woken up`**

- status: `failed` - full or empty boundary score failed; only 1/2 fitting scores usable; need 2
- log p full -10000.0000, empty -10000.0000
- masks scored: 1/4 (+0 top-k)

- rationale: "Aroused" means to be stirred from sleep, and "woken up" conveys that same idea of emerging from slumber in everyday terms. Word frequency shifts slightly from Zipf 3.35 to 3.37, making it marginally more common. The reader can now grasp the intended state of being roused without encountering a term that might carry unintended connotations.
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

**output:** He should come back in about 10 days for a check-up and to get a prescription for the leg braces he will need. He will use those braces for up to 6 months.

| metric | value |
|---|---:|
| bertscore_f1 | 0.615 |
| coleman_liau | 3.50 |
| coleman_liau_drop | 3.21 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 4.79 |
| fkgl_drop | 6.10 |
| fre | 90.1 |
| fre_gain | 26.8 |
| human_edit_recall | 1.000 |
| length_ratio | 1.21 |
| n_words | 34.0 |
| nli_completeness | 0.068 |
| nli_faithfulness | 0.677 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.571 |
| sari | 30.46 |
| smog | 7.17 |
| smog_drop | 5.86 |

### Stage 4 - arm `termonly`

**output:** He is to come back in about 10 days for a recheck and a prescription for planned ankle-foot braces, which he will need for up to 6 months.

| metric | value |
|---|---:|
| bertscore_f1 | 0.812 |
| coleman_liau | 5.51 |
| coleman_liau_drop | 1.19 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 10.08 |
| fkgl_drop | 0.81 |
| fre | 72.7 |
| fre_gain | 9.4 |
| human_edit_recall | 1.000 |
| length_ratio | 1.04 |
| n_words | 29.0 |
| nli_completeness | 0.977 |
| nli_faithfulness | 0.673 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.400 |
| sari | 43.50 |
| smog | 11.21 |
| smog_drop | 1.82 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `approximately` -> `about` | replace | - | - | - | - | - | - | - |
| `AFOs` -> `ankle-foot braces` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** He is to come back in about 10 days for a recheck and a prescription for planned ankle-foot braces, which he will need for up to 6 months.

| metric | value |
|---|---:|
| bertscore_f1 | 0.812 |
| coleman_liau | 5.51 |
| coleman_liau_drop | 1.19 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 10.08 |
| fkgl_drop | 0.81 |
| fre | 72.7 |
| fre_gain | 9.4 |
| human_edit_recall | 1.000 |
| length_ratio | 1.04 |
| n_words | 29.0 |
| nli_completeness | 0.977 |
| nli_faithfulness | 0.673 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.400 |
| sari | 43.50 |
| smog | 11.21 |
| smog_drop | 1.82 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `approximately` -> `in about` | replace | attributed | 0.003 | 0.263 | - | 0.714 | 0.393 | - |
| `AFOs` -> `ankle-foot braces` | replace | attributed | 0.181 | 0.787 | - | 0.586 | 0.767 | - |

**edit `approximately` -> `in about`**

- status: `attributed`
- log p full -0.0094, empty -0.0122
- masks scored: 10/10 (+3 top-k)
- ranked sources:
    - `+0.448` [justplainclear] AFO: Also known as: ankle-foot orthosis, walking boot A brace that supports your ankle or foot An AFO is a bra
    - `+0.055` [dorland] AFOs: ankle-foot orthosis
    - `-0.952` [wiktionary] approximately: Approximately is close to, but not exactly.

- rationale: "Approximately" means close to a certain number or amount, and "in about" conveys that same sense of estimation in everyday words. Word frequency rises from Zipf 4.64 to 6.34, making the replacement much more common. The reader now grasps the intended uncertainty without processing a longer, more formal term.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `AFOs` -> `ankle-foot braces`**

- status: `attributed`
- log p full -0.1812, empty -0.3623
- masks scored: 10/10 (+3 top-k)
- ranked sources:
    - `+0.767` [dorland] AFOs: ankle-foot orthosis
    - `-0.082` [justplainclear] AFO: Also known as: ankle-foot orthosis, walking boot A brace that supports your ankle or foot An AFO is a bra

- rationale: Ankle-foot braces are supportive devices worn on the lower leg and foot, so "ankle-foot braces" directly names the equipment in familiar terms. Phrase frequency rises from Zipf 1.36 to 3.35, making the replacement much more common in everyday language. The reader can now picture the assistive device without needing to decode a clinical abbreviation.
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

**output:** The outside sex organs looked normal.

| metric | value |
|---|---:|
| bertscore_f1 | 0.487 |
| coleman_liau | 9.23 |
| coleman_liau_drop | 8.24 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.750 |
| fkgl | 4.45 |
| fkgl_drop | 9.63 |
| fre | 73.8 |
| fre_gain | 65.5 |
| human_edit_recall | 1.000 |
| length_ratio | 0.75 |
| n_words | 6.0 |
| nli_completeness | 0.920 |
| nli_faithfulness | 0.987 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.250 |
| sari | 25.91 |
| smog | 3.13 |
| smog_drop | 9.89 |

### Stage 4 - arm `termonly`

**output:** Urinary and sex organs: The outer sex parts looked normal.

| metric | value |
|---|---:|
| bertscore_f1 | 0.313 |
| coleman_liau | 8.50 |
| coleman_liau_drop | 8.97 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 7.19 |
| fkgl_drop | 6.89 |
| fre | 61.3 |
| fre_gain | 53.0 |
| human_edit_recall | 1.000 |
| length_ratio | 1.25 |
| n_words | 10.0 |
| nli_completeness | 0.970 |
| nli_faithfulness | 0.766 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.250 |
| sari | 25.91 |
| smog | 8.84 |
| smog_drop | 4.18 |

annotation backend `novita`, 0 edits kept


### Stage 4 - arm `grounded`

**output:** Urinary and sex organs: The outside sex parts looked normal.

| metric | value |
|---|---:|
| bertscore_f1 | 0.300 |
| coleman_liau | 9.66 |
| coleman_liau_drop | 7.81 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.750 |
| fkgl | 7.19 |
| fkgl_drop | 6.89 |
| fre | 61.3 |
| fre_gain | 53.0 |
| human_edit_recall | 1.000 |
| length_ratio | 1.25 |
| n_words | 10.0 |
| nli_completeness | 0.968 |
| nli_faithfulness | 0.716 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.250 |
| sari | 25.91 |
| smog | 8.84 |
| smog_drop | 4.18 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `external genitalia` -> `looked normal` | replace | attributed | 0.023 | 0.882 | 0.253 | 0.784 | 0.020 | - |

**edit `external genitalia` -> `looked normal`**

- status: `attributed`
- log p full -0.0164, empty -0.0391
- masks scored: 66/66 (+2 top-k)
- ranked sources:
    - `+0.474` [readme] genitourinary: Body parts used for peeing and sex stuff.
    - `+0.454` [readme] Genitourinary: Important body parts involved in sex and peeing.
    - `+0.161` [wiktionary] external: Something that is external is not on the inside.
    - `-0.015` [iowa] EXTERNAL: outside the body
    - `-0.121` [michigan] external: Outside of the body.

- rationale: "External genitalia" refers to the visible sex organs on the outside of the body, so saying they "looked normal" conveys the same finding in everyday terms. Word frequency rises from Zipf 3.08 to 4.76, and age of acquisition drops from 11.84 to 5.53. This lets the reader grasp the physical examination result without needing anatomical vocabulary.
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

**output:** She is 21 days past surgery from an exploratory laparotomy with ovarian cancer staging.

| metric | value |
|---|---:|
| bertscore_f1 | 0.466 |
| coleman_liau | 12.33 |
| coleman_liau_drop | -1.41 |
| copy_jargon_rate | 0.750 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 13.47 |
| fkgl_drop | -1.30 |
| fre | 23.4 |
| fre_gain | -7.5 |
| human_edit_recall | 0.250 |
| length_ratio | 0.82 |
| n_words | 14.0 |
| nli_completeness | 0.985 |
| nli_faithfulness | 0.992 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 0.400 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 48.37 |
| smog | 14.55 |
| smog_drop | -1.53 |

### Stage 4 - arm `termonly`

**output:** She is 21 days after surgery to look inside the belly and check how far ovarian cancer has spread.

| metric | value |
|---|---:|
| bertscore_f1 | 0.621 |
| coleman_liau | 6.76 |
| coleman_liau_drop | 4.17 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.750 |
| fkgl | 9.21 |
| fkgl_drop | 2.96 |
| fre | 62.9 |
| fre_gain | 31.9 |
| human_edit_recall | 1.000 |
| length_ratio | 1.12 |
| n_words | 19.0 |
| nli_completeness | 0.624 |
| nli_faithfulness | 0.459 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 55.21 |
| smog | 11.21 |
| smog_drop | 1.82 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `postop` -> `21 days after` | replace | - | - | - | - | - | - | - |
| `ovarian cancer staging` -> `ovarian cancer has spread` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** She is 21 days after surgery to check her belly and find out how far her ovary cancer has spread.

| metric | value |
|---|---:|
| bertscore_f1 | 0.600 |
| coleman_liau | 5.05 |
| coleman_liau_drop | 5.87 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.600 |
| fkgl | 8.14 |
| fkgl_drop | 4.03 |
| fre | 72.3 |
| fre_gain | 41.4 |
| human_edit_recall | 1.000 |
| length_ratio | 1.18 |
| n_words | 20.0 |
| nli_completeness | 0.530 |
| nli_faithfulness | 0.107 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 49.02 |
| smog | 11.21 |
| smog_drop | 1.82 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `postop` -> `21 days after surgery` | replace | attributed | 0.273 | 0.556 | 0.474 | 0.794 | 0.012 | - |
| `ovarian cancer staging` -> `ovary cancer has spread` | replace | attributed | 1.749 | 2.220 | 0.694 | 0.817 | 0.924 | - |

**edit `postop` -> `21 days after surgery`**

- status: `attributed`
- log p full -0.5486, empty -0.8219
- masks scored: 66/66 (+3 top-k)
- ranked sources:
    - `+0.167` [readme] Ovarian: Ovarian means related to the ovaries where eggs are produced.
    - `+0.154` [readme] Exploratory laparotomy: Exploratory laparotomy: Surgery to check the organs in the belly for issues.
    - `+0.061` [dorland] postop: postoperation
    - `+0.058` [readme] PostOP: PostOP means after surgery.

- rationale: "Postop" refers to the period following a surgical procedure, and "21 days after surgery" conveys that same timeframe with a specific, concrete duration. Word frequency rises sharply from a Zipf value of 1.53 to 4.46, making the replacement far more common in everyday language. The reader now grasps the exact recovery window without needing to decode a medical abbreviation.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `ovarian cancer staging` -> `ovary cancer has spread`**

- status: `attributed`
- log p full -0.8641, empty -2.6127
- masks scored: 66/66 (+3 top-k)
- ranked sources:
    - `+1.614` [readme] Ovarian: Ovarian means related to the ovaries where eggs are produced.
    - `+0.691` [nih] ovarian: Having to do with the ovaries, the female reproductive glands in which the ova (eggs) are formed. The
    - `+0.285` [dorland] postop: postoperation
    - `+0.270` [readme] OVARIAN: Related to the female reproductive gland that produces eggs.

- rationale: The glossary explains that "ovarian" refers to the ovaries, so "ovary cancer" directly names the organ while "has spread" captures the meaning of staging in everyday terms. Word frequency moves from Zipf 3.24 to 2.93, and age of acquisition drops from 14.44 to 12.26. This lets the reader grasp that the disease has moved beyond its starting point without needing to interpret the clinical concept of staging.
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

**output:** A prescription for prednisone was given to him as part of his chemotherapy.

| metric | value |
|---|---:|
| bertscore_f1 | 0.612 |
| coleman_liau | 9.58 |
| coleman_liau_drop | 1.34 |
| copy_jargon_rate | 1.000 |
| critical_error | 0.000 |
| drug_preservation | 1.000 |
| fkgl | 8.54 |
| fkgl_drop | 0.00 |
| fre | 57.0 |
| fre_gain | 0.0 |
| human_edit_recall | 0.000 |
| length_ratio | 0.87 |
| n_words | 13.0 |
| nli_completeness | 0.992 |
| nli_faithfulness | 0.993 |
| replacement_f1 | 0.000 |
| rewrite_aggressiveness | 1.000 |
| sari | 37.37 |
| smog | 11.21 |
| smog_drop | 0.00 |

### Stage 4 - arm `termonly`

**output:** He has been given a prescription for a steroid medicine as part of his cancer drug treatment.

| metric | value |
|---|---:|
| bertscore_f1 | 0.650 |
| coleman_liau | 8.39 |
| coleman_liau_drop | 2.53 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| drug_preservation | 0.000 |
| fkgl | 8.39 |
| fkgl_drop | 0.15 |
| fre | 65.2 |
| fre_gain | 8.2 |
| human_edit_recall | 1.000 |
| length_ratio | 1.13 |
| n_words | 17.0 |
| nli_completeness | 0.068 |
| nli_faithfulness | 0.398 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 54.69 |
| smog | 11.21 |
| smog_drop | 0.00 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `prednisone` -> `a steroid medicine` | replace | - | - | - | - | - | - | - |
| `chemotherapy` -> `cancer drug treatment` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** He was given a prescription for a medicine that lowers the body's immune response as part of his cancer drug treatment.

| metric | value |
|---|---:|
| bertscore_f1 | 0.518 |
| coleman_liau | 9.58 |
| coleman_liau_drop | 1.34 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| drug_preservation | 0.000 |
| fkgl | 10.58 |
| fkgl_drop | -2.04 |
| fre | 56.6 |
| fre_gain | -0.4 |
| human_edit_recall | 1.000 |
| length_ratio | 1.47 |
| n_words | 22.0 |
| nli_completeness | 0.017 |
| nli_faithfulness | 0.562 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 43.78 |
| smog | 11.21 |
| smog_drop | 0.00 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `prednisone` -> `a medicine that lowers the body's immune response` | replace | attributed | 13.250 | 14.127 | 0.827 | 0.700 | 1.938 | - |
| `chemotherapy` -> `cancer drug treatment` | replace | attributed | 0.527 | 1.516 | 0.813 | 0.849 | 0.030 | - |

**edit `prednisone` -> `a medicine that lowers the body's immune response`**

- status: `attributed`
- log p full -0.5380, empty -13.7883
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+6.590` [readme] Prednisone: A medication that lowers the body's immune response and inflammation.
    - `+4.653` [readme] prednisone: A medication that helps lower the body's immune system reactions.
    - `+2.582` [nih] prednisone: A drug used to reduce inflammation and lower the body’s immune response.  It is used with other dr
    - `+2.118` [iowa] CHEMOTHERAPY: treatment of disease, usually cancer, by chemical agents
    - `+1.652` [readme] CHEMOTHERAPY: Using drugs to treat diseases like cancer.

- rationale: The glossary explains prednisone as a medication that reduces immune response and inflammation, so the replacement directly conveys that function in everyday terms. Word frequency rises from Zipf 2.56 to 3.11, and age of acquisition drops from 17.17 to 12.32. This lets the reader grasp the drug’s purpose without needing to recognize its clinical name.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `chemotherapy` -> `cancer drug treatment`**

- status: `attributed`
- log p full -0.2171, empty -0.7438
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+1.578` [readme] CHEMOTHERAPY: Using drugs to treat diseases like cancer.
    - `+1.548` [nih] chemotherapy: Treatment that uses drugs to stop the growth of cancer cells, either by killing the cells or by 
    - `+1.160` [readme] chemotherapy: Using drugs to treat cancer or other diseases.
    - `+0.259` [iowa] CHEMOTHERAPY: treatment of disease, usually cancer, by chemical agents
    - `-0.116` [readme] prednisone: A medication that helps lower the body's immune system reactions.

- rationale: Chemotherapy refers to using drugs to treat cancer, and "cancer drug treatment" conveys that same idea in everyday words. Word frequency rises from Zipf 3.56 to 4.46, and age of acquisition drops from 12.53 to 8.39. This lets the reader grasp the treatment approach without needing the clinical term.
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

**output:** Photic stimulation was done, but no clear brainwave response to the flashing light was seen.

| metric | value |
|---|---:|
| bertscore_f1 | 0.667 |
| coleman_liau | 11.61 |
| coleman_liau_drop | 2.59 |
| copy_jargon_rate | 0.500 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 7.57 |
| fkgl_drop | 1.52 |
| fre | 67.5 |
| fre_gain | 18.0 |
| human_edit_recall | 0.500 |
| length_ratio | 0.88 |
| n_words | 15.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.649 |
| nli_faithfulness | 0.026 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 31.65 |
| smog | 8.84 |
| smog_drop | 0.00 |

### Stage 4 - arm `termonly`

**output:** Flashing lights were used, but no clear brain-wave following was seen.

| metric | value |
|---|---:|
| bertscore_f1 | 0.502 |
| coleman_liau | 11.56 |
| coleman_liau_drop | 2.64 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 4.79 |
| fkgl_drop | 4.29 |
| fre | 80.3 |
| fre_gain | 30.8 |
| human_edit_recall | 1.000 |
| length_ratio | 0.71 |
| n_words | 12.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.906 |
| nli_faithfulness | 0.638 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.200 |
| sari | 32.89 |
| smog | 8.84 |
| smog_drop | 0.00 |

annotation backend `novita`, 0 edits kept


### Stage 4 - arm `grounded`

**output:** Flashing lights were used, but no strong brain wave response to the lights was seen.

| metric | value |
|---|---:|
| bertscore_f1 | 0.515 |
| coleman_liau | 8.52 |
| coleman_liau_drop | 5.68 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 3.63 |
| fkgl_drop | 5.45 |
| fre | 95.7 |
| fre_gain | 46.2 |
| human_edit_recall | 1.000 |
| length_ratio | 0.88 |
| n_words | 15.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.885 |
| nli_faithfulness | 0.243 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.200 |
| sari | 27.18 |
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

**output:** Both of her parents died from heart attacks.

| metric | value |
|---|---:|
| bertscore_f1 | 0.569 |
| coleman_liau | 6.60 |
| coleman_liau_drop | 12.32 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 2.28 |
| fkgl_drop | 13.28 |
| fre | 93.0 |
| fre_gain | 95.2 |
| human_edit_recall | 1.000 |
| laterality_preservation | 1.000 |
| length_ratio | 1.00 |
| n_words | 8.0 |
| nli_completeness | 0.705 |
| nli_faithfulness | 0.873 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 27.40 |
| smog | 3.13 |
| smog_drop | 11.43 |

### Stage 4 - arm `termonly`

**output:** FAMILY HISTORY: Both parents died from heart attacks.

| metric | value |
|---|---:|
| bertscore_f1 | 0.758 |
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
| nli_completeness | 0.802 |
| nli_faithfulness | 0.929 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 61.01 |
| smog | 11.21 |
| smog_drop | 3.35 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `myocardial infarctions` -> `heart attacks` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** FAMILY HISTORY: Both parents died from heart attacks.

| metric | value |
|---|---:|
| bertscore_f1 | 0.758 |
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
| nli_completeness | 0.802 |
| nli_faithfulness | 0.929 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 61.01 |
| smog | 11.21 |
| smog_drop | 3.35 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `myocardial infarctions` -> `heart attacks` | replace | attributed | 0.010 | 1.256 | - | 0.666 | 0.994 | - |

**edit `myocardial infarctions` -> `heart attacks`**

- status: `attributed`
- log p full -0.0041, empty -0.0143
- masks scored: 32/34 (+2 top-k)
- ranked sources:
    - `+1.235` [iowa] MYOCARDIAL INFARCTION: heart attack
    - `+0.241` [michigan] myocardial infarction: Occurs when the flow of blood to the heart is stopped by a blood clot or a spasm of an 
    - `-0.081` [readme] inferior wall myocardial infarction: Heart damage at the bottom of the left ventricle due to a blocked artery.
    - `-0.206` [justplainclear] myocardial infarction: A heart attack

- rationale: Myocardial infarctions refer to damage of the heart muscle from blocked blood flow, and "heart attacks" conveys that same event in everyday terms. Word frequency rises sharply from Zipf 1.57 to 4.59, while age of acquisition drops from 16.64 to 5.17. This lets the reader immediately grasp the serious cardiac emergency without needing clinical vocabulary.
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

**output:** Her legs and feet have swelling that leaves a dent when pressed, and it goes up to her knees on both sides.

| metric | value |
|---|---:|
| bertscore_f1 | 0.448 |
| coleman_liau | 5.00 |
| coleman_liau_drop | 4.45 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 5.33 |
| fkgl_drop | 5.90 |
| fre | 96.1 |
| fre_gain | 61.9 |
| human_edit_recall | 1.000 |
| laterality_preservation | 1.000 |
| length_ratio | 0.79 |
| n_words | 22.0 |
| nli_completeness | 0.650 |
| nli_faithfulness | 0.195 |
| number_unit_preservation | 0.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.200 |
| sari | 27.57 |
| smog | 3.13 |
| smog_drop | 9.89 |

### Stage 4 - arm `termonly`

**output:** Both legs have swelling that leaves a dent, up to the knees.

| metric | value |
|---|---:|
| bertscore_f1 | 0.450 |
| coleman_liau | 4.45 |
| coleman_liau_drop | 5.00 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 1.87 |
| fkgl_drop | 9.35 |
| fre | 103.0 |
| fre_gain | 68.8 |
| human_edit_recall | 1.000 |
| laterality_preservation | 1.000 |
| length_ratio | 0.43 |
| n_words | 12.0 |
| nli_completeness | 0.849 |
| nli_faithfulness | 0.899 |
| number_unit_preservation | 0.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.200 |
| sari | 35.45 |
| smog | 3.13 |
| smog_drop | 9.89 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `bilateral pitting edema` -> `swelling that leaves a dent` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Her legs and feet are swollen with pits when pressed, up to the knees on both sides.

| metric | value |
|---|---:|
| bertscore_f1 | 0.421 |
| coleman_liau | 4.98 |
| coleman_liau_drop | 4.48 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 3.53 |
| fkgl_drop | 7.69 |
| fre | 100.0 |
| fre_gain | 65.8 |
| human_edit_recall | 1.000 |
| laterality_preservation | 1.000 |
| length_ratio | 0.61 |
| n_words | 17.0 |
| nli_completeness | 0.695 |
| nli_faithfulness | 0.250 |
| number_unit_preservation | 0.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.200 |
| sari | 36.88 |
| smog | 3.13 |
| smog_drop | 9.89 |

annotation backend `novita`, 0 edits kept


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

**output:** The questions that come next are mostly part of a psychosocial evaluation of a donor.

| metric | value |
|---|---:|
| bertscore_f1 | 0.507 |
| coleman_liau | 9.29 |
| coleman_liau_drop | 9.65 |
| copy_jargon_rate | 1.000 |
| critical_error | 0.000 |
| fkgl | 9.14 |
| fkgl_drop | 5.13 |
| fre | 56.3 |
| fre_gain | 45.7 |
| human_edit_recall | 0.000 |
| length_ratio | 1.00 |
| n_words | 15.0 |
| nli_completeness | 0.993 |
| nli_faithfulness | 0.992 |
| replacement_f1 | 0.000 |
| rewrite_aggressiveness | 1.000 |
| sari | 19.23 |
| smog | 11.21 |
| smog_drop | 1.82 |

### Stage 4 - arm `termonly`

**output:** Following questions are mostly part of a check on a donor's mental and social health.

| metric | value |
|---|---:|
| bertscore_f1 | 0.554 |
| coleman_liau | 8.91 |
| coleman_liau_drop | 10.03 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 7.57 |
| fkgl_drop | 6.70 |
| fre | 67.5 |
| fre_gain | 57.0 |
| human_edit_recall | 1.000 |
| length_ratio | 1.07 |
| n_words | 16.0 |
| nli_completeness | 0.982 |
| nli_faithfulness | 0.881 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.667 |
| sari | 36.06 |
| smog | 8.84 |
| smog_drop | 4.18 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `psychosocial` -> `check on a donor's mental and social health` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** The following questions are mostly part of an evaluation that looks at a donor's mental and social well-being.

| metric | value |
|---|---:|
| bertscore_f1 | 0.511 |
| coleman_liau | 11.56 |
| coleman_liau_drop | 7.38 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 11.75 |
| fkgl_drop | 2.52 |
| fre | 42.9 |
| fre_gain | 32.3 |
| human_edit_recall | 1.000 |
| length_ratio | 1.33 |
| n_words | 20.0 |
| nli_completeness | 0.988 |
| nli_faithfulness | 0.803 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 36.75 |
| smog | 13.02 |
| smog_drop | 0.00 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `psychosocial` -> `mental and social well-being` | replace | attributed | -0.263 | -0.334 | - | 1.000 | 3.976 | - |

**edit `psychosocial` -> `mental and social well-being`**

- status: `attributed`
- log p full -1.6872, empty -1.4243
- masks scored: 6/6 (+1 top-k)
- ranked sources:
    - `+1.916` [michigan] psychosocial: Including both the mental and social aspects of disease.
    - `-2.060` [nih] psychosocial: In medicine, having to do with the mental, emotional, social, and spiritual effects of a disease

- rationale: "Psychosocial" refers to the interwoven mental and social factors that shape a person's experience, so "mental and social well-being" unpacks that exact combination into familiar words. Word frequency rises from Zipf 2.88 to 4.68, and age of acquisition drops from 15.44 to 10.43. Readers can now grasp the full scope of the concept without needing to decode a technical compound term.
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

**output:** The patient has mild hardening of the arteries in the part of the aorta that goes down through the chest, and it does not move.

| metric | value |
|---|---:|
| bertscore_f1 | 0.576 |
| coleman_liau | 6.45 |
| coleman_liau_drop | 22.87 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 9.26 |
| fkgl_drop | 14.86 |
| fre | 73.2 |
| fre_gain | 142.1 |
| human_edit_recall | 1.000 |
| length_ratio | 1.14 |
| n_words | 25.0 |
| nli_completeness | 0.946 |
| nli_faithfulness | 0.866 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 51.08 |
| severity_downgrade | 0.000 |
| severity_preservation | 1.000 |
| severity_tier_input | 1.000 |
| severity_tier_output | 1.000 |
| smog | 13.02 |
| smog_drop | 1.53 |

### Stage 4 - arm `termonly`

**output:** Mild, not moving, hardening of the lower main artery.

| metric | value |
|---|---:|
| bertscore_f1 | 0.403 |
| coleman_liau | 7.98 |
| coleman_liau_drop | 21.34 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 7.59 |
| fkgl_drop | 16.53 |
| fre | 56.7 |
| fre_gain | 125.7 |
| human_edit_recall | 1.000 |
| length_ratio | 0.41 |
| n_words | 9.0 |
| nli_completeness | 0.780 |
| nli_faithfulness | 0.943 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 48.83 |
| severity_downgrade | 0.000 |
| severity_preservation | 1.000 |
| severity_tier_input | 1.000 |
| severity_tier_output | 1.000 |
| smog | 11.21 |
| smog_drop | 3.35 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `nonmobile` -> `not moving` | replace | - | - | - | - | - | - | - |
| `atherosclerosis` -> `hardening of the lower main artery` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Mild, not moving, hardening of the main artery in the chest.

| metric | value |
|---|---:|
| bertscore_f1 | 0.488 |
| coleman_liau | 6.29 |
| coleman_liau_drop | 23.03 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 5.86 |
| fkgl_drop | 18.26 |
| fre | 72.6 |
| fre_gain | 141.6 |
| human_edit_recall | 1.000 |
| length_ratio | 0.50 |
| n_words | 11.0 |
| nli_completeness | 0.462 |
| nli_faithfulness | 0.881 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 49.66 |
| severity_downgrade | 0.000 |
| severity_preservation | 1.000 |
| severity_tier_input | 1.000 |
| severity_tier_output | 1.000 |
| smog | 11.21 |
| smog_drop | 3.35 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `nonmobile` -> `not moving` | replace | attributed | -0.568 | -1.468 | - | 0.821 | 0.455 | - |
| `descending aortic atherosclerosis` -> `hardening of the main artery in the chest` | replace | attributed | 5.400 | 6.423 | - | 0.921 | 3.689 | - |

**edit `nonmobile` -> `not moving`**

- status: `attributed`
- log p full -0.8278, empty -0.2600
- masks scored: 18/18 (+2 top-k)
- ranked sources:
    - `+0.537` [readme] descending aortic: Descending aortic: The area of the main artery as it travels through the chest.
    - `+0.083` [justplainclear] atherosclerosis: A disease where arteries get thick and prevent the flow of blood Normal artery and atheroscle
    - `-0.195` [thesaurus] atherosclerosis: hardening of the arteries, clogged blood vessels
    - `-0.857` [michigan] atherosclerosis: A disease where your arteries get stiff and clogged by things in your blood, such as fat and 

- rationale: "Nonmobile" means unable to move, so "not moving" conveys the same idea with everyday words. Word frequency rises sharply from Zipf 0.00 to 5.01, making the replacement far more familiar. The reader can now grasp the lack of movement without encountering an uncommon medical term.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `descending aortic atherosclerosis` -> `hardening of the main artery in the chest`**

- status: `attributed`
- log p full -0.4439, empty -5.8436
- masks scored: 18/18 (+2 top-k)
- ranked sources:
    - `+4.850` [readme] descending aortic: Descending aortic: The area of the main artery as it travels through the chest.
    - `+1.161` [thesaurus] atherosclerosis: hardening of the arteries, clogged blood vessels
    - `-0.028` [justplainclear] atherosclerosis: A disease where arteries get thick and prevent the flow of blood Normal artery and atheroscle
    - `-0.180` [michigan] atherosclerosis: A disease where your arteries get stiff and clogged by things in your blood, such as fat and 

- rationale: Atherosclerosis refers to the buildup of fatty plaque that stiffens artery walls, so "hardening of the main artery in the chest" conveys the same process and location in everyday terms. Phrase frequency rises from Zipf 2.55 to 2.89, and age of acquisition edges down from 13.12 to 13.06. The reader can now grasp the condition without needing to parse a lengthy anatomical label.
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

**output:** The tube that connects the ear to the throat was blocked with a waxy material used on bone.

| metric | value |
|---|---:|
| bertscore_f1 | 0.596 |
| coleman_liau | 6.08 |
| coleman_liau_drop | 4.15 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 6.51 |
| fkgl_drop | 0.20 |
| fre | 80.5 |
| fre_gain | 19.2 |
| human_edit_recall | 1.000 |
| length_ratio | 1.38 |
| n_words | 18.0 |
| nli_completeness | 0.351 |
| nli_faithfulness | 0.853 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 36.31 |
| smog | 8.84 |
| smog_drop | 2.37 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `eustachian tube` -> `tube that connects the ear to the throat` | replace | - | - | - | - | - | - | - |
| `obstructed` -> `blocked` | replace | - | - | - | - | - | - | - |
| `bone wax` -> `a waxy material used on bone` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** The tube that links the middle ear to the throat was blocked with a hard, waxy material used in surgery.

| metric | value |
|---|---:|
| bertscore_f1 | 0.507 |
| coleman_liau | 6.79 |
| coleman_liau_drop | 3.43 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.600 |
| fkgl | 8.14 |
| fkgl_drop | -1.44 |
| fre | 72.3 |
| fre_gain | 11.1 |
| human_edit_recall | 1.000 |
| length_ratio | 1.54 |
| n_words | 20.0 |
| nli_completeness | 0.153 |
| nli_faithfulness | 0.248 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 33.53 |
| smog | 11.21 |
| smog_drop | 0.00 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `eustachian tube` -> `tube that links the middle ear to the throat` | replace | attributed | 2.057 | 2.213 | 0.754 | 0.832 | 3.655 | - |
| `obstructed` -> `blocked` | replace | attributed | 0.035 | 2.199 | 0.571 | 0.885 | 0.054 | - |
| `bone wax` -> `a hard, waxy material used in surgery` | replace | attributed | 7.238 | 7.351 | 0.871 | 0.915 | 1.617 | - |

**edit `eustachian tube` -> `tube that links the middle ear to the throat`**

- status: `attributed`
- log p full -1.8205, empty -3.8775
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+3.655` [justplainclear] eustachian tube: The tube that connects your middle ear to the back of your throat and pharynx area. The openi
    - `-0.150` [wiktionary] wax: Wax is a solid material made of animal fat.
    - `-0.187` [readme] wax: Yellow sticky stuff in your ear that keeps it clean and dry.

- rationale: The justplainclear glossary explains that the eustachian tube connects the middle ear to the back of the throat, so "tube that links the middle ear to the throat" conveys that same anatomical connection in everyday words. Word frequency rises substantially from Zipf 1.90 to 3.80, making the replacement much more common in general language. Readers can now picture the passageway without needing to know the formal anatomical name.
- audit: coverage 0.667, grounding_error=True, omission=False, source_ok=True, passage_ok=True

**edit `obstructed` -> `blocked`**

- status: `attributed`
- log p full -0.0045, empty -0.0399
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+0.562` [wiktionary] obstructed: If something obstructs your way, it blocks your path from point A to point B.
    - `+0.508` [wiktionary] bone: Bones are the hard, white things inside your body. They give your body its shape.
    - `+0.448` [justplainclear] eustachian tube: The tube that connects your middle ear to the back of your throat and pharynx area. The openi
    - `+0.320` [wiktionary] wax: If you wax something, you put wax on it, for example, a car.
    - `+0.116` [wiktionary] wax: Wax is a solid material made of animal fat.

- rationale: "Obstructed" means something is in the way, and "blocked" conveys that same idea of a passage being stopped up in everyday language. Word frequency rises from Zipf 2.98 to 4.31, making it a much more familiar term. The reader can now immediately picture the problem without needing to parse a less common medical word.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `bone wax` -> `a hard, waxy material used in surgery`**

- status: `attributed`
- log p full -2.2376, empty -9.4755
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+2.664` [wiktionary] bone: Bones are the hard, white things inside your body. They give your body its shape.
    - `+1.048` [wiktionary] bone: When two man bone, they have sex.
    - `+0.825` [readme] wax: Yellow sticky stuff in your ear that keeps it clean and dry.
    - `+0.665` [wiktionary] wax: Wax is a solid material made of animal fat.
    - `+0.404` [wiktionary] wax: If you wax something, you put wax on it, for example, a car.

- rationale: The glossary explains that bones are the hard structures giving the body its shape, so "a hard, waxy material used in surgery" conveys the substance's texture and medical context in everyday terms. Word frequency drops from Zipf 3.81 to 2.70, and age of acquisition rises from 6.00 to 8.06. Readers can now grasp what the material is and where it is applied without needing the clinical shorthand.
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

**output:** He was placed flat on his back on the operating room table.

| metric | value |
|---|---:|
| bertscore_f1 | 0.666 |
| coleman_liau | 4.45 |
| coleman_liau_drop | 2.24 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 4.82 |
| fkgl_drop | 1.45 |
| fre | 81.9 |
| fre_gain | 15.8 |
| human_edit_recall | 1.000 |
| length_ratio | 1.20 |
| n_words | 12.0 |
| nli_completeness | 0.978 |
| nli_faithfulness | 0.981 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 66.67 |
| smog | 8.84 |
| smog_drop | 0.00 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `supine` -> `flat on his back` | replace | - | - | - | - | - | - | - |

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
| `supine` -> `lying on his back` | replace | attributed | 2.405 | 4.147 | - | 0.721 | 0.109 | - |

**edit `supine` -> `lying on his back`**

- status: `attributed`
- log p full -0.1766, empty -2.5816
- masks scored: 18/18 (+2 top-k)
- ranked sources:
    - `+0.960` [iowa] SUPINE: lying on the back
    - `+0.851` [readme] Supine: Lying down on your back.
    - `+0.544` [readme] supine: Lying on your back.
    - `+0.071` [michigan] supine: To lie on your back.

- rationale: "Supine" means lying face upward, so "lying on his back" conveys the exact same position in everyday words. Word frequency rises from Zipf 2.42 to 4.64, and age of acquisition drops from 16.43 to 5.31. The reader can now picture the posture without needing a clinical term.
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
| `urinalysis` -> `pee test` | replace | attributed | 5.732 | 9.062 | - | 0.837 | 0.097 | - |

**edit `urinalysis` -> `pee test`**

- status: `attributed`
- log p full -0.0364, empty -5.7685
- masks scored: 34/34 (+2 top-k)
- ranked sources:
    - `+2.921` [readme] urinalysis: A test that checks the contents of your pee to see what's in there.
    - `+2.824` [readme] Urinalysis: A test that checks what's in your pee.
    - `+1.420` [justplainclear] urinalysis: Also known as: urine test, pee test A test of your urine used to find certain medical conditions
    - `+0.182` [nih] urinalysis: A test that determines the content of the urine.

- rationale: "Urinalysis" refers to a laboratory analysis of urine, and "pee test" conveys that same idea using everyday words. Word frequency rises from Zipf 2.20 to 3.94, and age of acquisition drops from 14.68 to 6.26. This lets the reader immediately grasp what kind of sample is being checked without needing medical vocabulary.
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

**output:** Her eyesight and hearing seemed good enough for the tests, but she did say she needed a new glasses prescription.

| metric | value |
|---|---:|
| bertscore_f1 | 0.681 |
| coleman_liau | 9.40 |
| coleman_liau_drop | 4.32 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.200 |
| fkgl | 8.14 |
| fkgl_drop | 4.13 |
| fre | 72.3 |
| fre_gain | 27.8 |
| human_edit_recall | 1.000 |
| length_ratio | 0.95 |
| n_words | 20.0 |
| nli_completeness | 0.994 |
| nli_faithfulness | 0.995 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.625 |
| sari | 18.42 |
| smog | 8.84 |
| smog_drop | 4.18 |

### Stage 4 - arm `termonly`

**output:** Vision and hearing seemed good enough for testing, although she did say that she needed new glasses.

| metric | value |
|---|---:|
| bertscore_f1 | 0.783 |
| coleman_liau | 10.44 |
| coleman_liau_drop | 3.29 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.333 |
| fkgl | 7.70 |
| fkgl_drop | 4.57 |
| fre | 70.1 |
| fre_gain | 25.6 |
| human_edit_recall | 1.000 |
| length_ratio | 0.81 |
| n_words | 17.0 |
| nli_completeness | 0.986 |
| nli_faithfulness | 0.995 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 31.06 |
| smog | 3.13 |
| smog_drop | 9.89 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `adequate` -> `good enough` | replace | - | - | - | - | - | - | - |
| `indicate` -> `say` | replace | - | - | - | - | - | - | - |
| `eyeglass prescription` -> `new glasses` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Vision and hearing seemed good enough for testing, although she did say she needed to update her glasses order.

| metric | value |
|---|---:|
| bertscore_f1 | 0.829 |
| coleman_liau | 10.42 |
| coleman_liau_drop | 3.30 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.333 |
| fkgl | 9.21 |
| fkgl_drop | 3.06 |
| fre | 62.9 |
| fre_gain | 18.4 |
| human_edit_recall | 1.000 |
| length_ratio | 0.90 |
| n_words | 19.0 |
| nli_completeness | 0.980 |
| nli_faithfulness | 0.983 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.200 |
| sari | 41.39 |
| smog | 3.13 |
| smog_drop | 9.89 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `adequate` -> `good enough` | replace | attributed | 0.022 | 0.468 | 0.871 | 0.915 | 1.924 | - |
| `indicate` -> `say` | replace | attributed | -0.254 | -1.680 | 0.311 | 0.575 | 0.008 | - |
| `eyeglass prescription` -> `glasses order` | replace | attributed | 3.706 | 6.554 | 0.455 | 0.643 | 0.300 | - |

**edit `adequate` -> `good enough`**

- status: `attributed`
- log p full -0.0387, empty -0.0611
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+2.507` [wiktionary] adequate: If something is adequate, it is good enough.
    - `+0.583` [wiktionary] indicate: If someone indicates something, they show signs of something; they show it.
    - `+0.351` [michigan] indicate: To suggest or show.
    - `+0.210` [wiktionary] prescription: A written order, as by a physician, to tell which medicine to take and how many doses of it is n
    - `+0.168` [readme] Prescription: A prescription is a doctor's recommendation for medication or treatment.

- rationale: "Adequate" means meeting a basic level of acceptability, and "good enough" conveys that same idea of sufficiency in everyday terms. Word frequency rises from Zipf 4.05 to 5.44, while age of acquisition drops from 10.35 to 6.96. Readers can now grasp the intended threshold of quality without needing a more formal vocabulary.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `indicate` -> `say`**

- status: `attributed`
- log p full -0.3232, empty -0.0687
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+0.665` [thesaurus] adequate: enough, the right amount
    - `+0.657` [wiktionary] prescription: A written order, as by a physician, to tell which medicine to take and how many doses of it is n
    - `+0.293` [michigan] adequate: Enough or the right amount.
    - `+0.263` [wiktionary] indicate: If someone indicates something, they point it out or they point to it; they bring your attention to 
    - `+0.237` [readme] Prescription: A prescription is a doctor's recommendation for medication or treatment.

- rationale: "Indicate" means to point out or show something, and "say" carries that same meaning of expressing information in a simpler, more direct way. Word frequency rises from Zipf 4.35 to 5.89, and age of acquisition drops from 9.74 to 3.42. The reader can now grasp the instruction without processing a more formal, multi-syllable verb.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `eyeglass prescription` -> `glasses order`**

- status: `attributed`
- log p full -0.0583, empty -3.7642
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+1.928` [michigan] prescription: An order from your doctor, nurse, or physician assistant for drugs or other treatment.
    - `+1.628` [thesaurus] prescription: doctors orders, medicine, drug order
    - `+1.229` [readme] Prescription: A prescription is a doctor's recommendation for medication or treatment.
    - `+1.021` [wiktionary] prescription: A written order, as by a physician, to tell which medicine to take and how many doses of it is n
    - `+0.740` [nih] prescription: A doctor's order for medicine or another intervention.

- rationale: The Michigan glossary defines a prescription as a medical order, so "glasses order" conveys the same idea of a provider's directive in everyday terms. Word frequency rises from Zipf 2.32 to 4.31, and age of acquisition drops from 9.22 to 6.26. This lets the reader recognize they need a simple request for corrective lenses, not a complex medical document.
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

**output:** The doctor has talked to the patient several times about a colonoscopy, which he has refused, so they have been checking his stool for hidden blood.

| metric | value |
|---|---:|
| bertscore_f1 | 0.593 |
| coleman_liau | 9.83 |
| coleman_liau_drop | -2.21 |
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
| nli_faithfulness | 0.939 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.250 |
| sari | 33.49 |
| smog | 3.13 |
| smog_drop | 0.00 |

### Stage 4 - arm `termonly`

**output:** I have talked to him several times about a test that looks inside the large bowel with a camera, which he has refused, and so we have been checking his poop for hidden blood.

| metric | value |
|---|---:|
| bertscore_f1 | 0.608 |
| coleman_liau | 6.87 |
| coleman_liau_drop | 0.75 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.750 |
| fkgl | 12.59 |
| fkgl_drop | -4.57 |
| fre | 65.3 |
| fre_gain | -14.9 |
| human_edit_recall | 1.000 |
| length_ratio | 0.74 |
| n_words | 34.0 |
| nli_completeness | 0.918 |
| nli_faithfulness | 0.695 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 61.87 |
| smog | 8.84 |
| smog_drop | -5.71 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `colonoscopy` -> `a test that looks inside the large bowel with a camera` | replace | - | - | - | - | - | - | - |
| `occult blood` -> `hidden blood` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** I have talked to him several times about a test that checks the inside of his large intestine, which he has refused, and so we have been checking his poop for hidden blood.

| metric | value |
|---|---:|
| bertscore_f1 | 0.616 |
| coleman_liau | 7.38 |
| coleman_liau_drop | 0.23 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.750 |
| fkgl | 11.94 |
| fkgl_drop | -3.91 |
| fre | 68.2 |
| fre_gain | -12.0 |
| human_edit_recall | 1.000 |
| length_ratio | 0.72 |
| n_words | 33.0 |
| nli_completeness | 0.847 |
| nli_faithfulness | 0.949 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 61.54 |
| smog | 8.84 |
| smog_drop | -5.71 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `colonoscopy` -> `a test that checks the inside of his large intestine` | replace | attributed | 10.611 | 10.800 | 0.901 | 0.870 | 3.865 | - |
| `stools` -> `poop` | replace | attributed | 0.218 | 4.753 | 0.795 | 0.910 | 4.787 | - |
| `occult blood` -> `hidden blood` | replace | attributed | 0.070 | 0.569 | 0.606 | 0.914 | 0.193 | - |

**edit `colonoscopy` -> `a test that checks the inside of his large intestine`**

- status: `attributed`
- log p full -1.7580, empty -12.3691
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+6.430` [readme] colonoscopy: A colonoscopy is a test that checks the inside of your large intestine for signs of cancer.
    - `+2.565` [readme] colonoscopy: A procedure to check for colon cancer by examining the inside of the large intestine.
    - `+1.053` [wiktionary] stools: A stool is a seat for one person that does not have a back or an armrest.
    - `+0.717` [nih] colonoscopy: Examination of the inside of the colon using a colonoscope, inserted into the rectum. A colonosco
    - `+0.682` [nih] blood: A tissue with red blood cells, white blood cells, platelets, and other substances suspended in fluid ca

- rationale: The glossary explains that a colonoscopy is a test for examining the large intestine, so the replacement directly adopts that plain-language description. Word frequency rises from Zipf 2.74 to 3.18, and age of acquisition drops from 15.76 to 9.28. The reader can now grasp the procedure’s purpose without needing to know the medical term.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `stools` -> `poop`**

- status: `attributed`
- log p full -0.0021, empty -0.2205
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+6.709` [readme] stools: Poop.
    - `+1.921` [readme] colonoscopy: A colonoscopy is a test that checks the inside of your large intestine for signs of cancer.
    - `+0.881` [michigan] colonoscopy: Looks at the inside of the large intestine using a flexible tube with a ltiny camera at the end.
    - `+0.734` [readme] blood: Blood is a fluid that carries nutrients and oxygen to different parts of the body.
    - `+0.621` [readme] colonoscopy: A procedure to check for colon cancer by examining the inside of the large intestine.

- rationale: The original term refers to solid bodily waste, and “poop” is a widely recognized, everyday word for the exact same thing. Word frequency rises from a Zipf score of 3.05 to 3.66, showing it is a more familiar term in common language. This swap lets the reader immediately grasp the topic without encountering a clinical word that might feel distant or confusing.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `occult blood` -> `hidden blood`**

- status: `attributed`
- log p full -0.0992, empty -0.1691
- masks scored: 66/66 (+6 top-k)
- ranked sources:
    - `+0.992` [wiktionary] occult: If something is occult it is hidden or secret—or it is about hidden or secret things.
    - `+0.800` [readme] colonoscopy: A colonoscopy is a test that checks the inside of your large intestine for signs of cancer.
    - `+0.239` [readme] blood: Blood is a fluid that carries nutrients and oxygen to different parts of the body.
    - `+0.222` [wiktionary] occult: If something is occult it is part of the universe most people do not see. An occult thing is something
    - `+0.170` [readme] stools: Poop.

- rationale: "Occult blood" refers to blood that is not visible to the naked eye, so "hidden blood" directly conveys that same idea of being concealed from sight. Word frequency rises from Zipf 3.28 to 4.43, and age of acquisition drops from 12.65 to 4.89. This lets the reader immediately grasp that the test is looking for blood they cannot see, without needing to learn a specialized medical term.
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

**output:** The knee was washed out with a lot of fluid and then suctioned dry again.

| metric | value |
|---|---:|
| bertscore_f1 | 0.574 |
| coleman_liau | 4.65 |
| coleman_liau_drop | 6.75 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.167 |
| fkgl | 4.42 |
| fkgl_drop | 3.95 |
| fre | 90.1 |
| fre_gain | 37.2 |
| human_edit_recall | 1.000 |
| length_ratio | 0.94 |
| n_words | 15.0 |
| nli_completeness | 0.971 |
| nli_faithfulness | 0.983 |
| number_unit_preservation | 0.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.200 |
| sari | 57.01 |
| smog | 3.13 |
| smog_drop | 8.08 |

### Stage 4 - arm `termonly`

**output:** The knee was washed with a lot of fluid and then dried with suction once again.

| metric | value |
|---|---:|
| bertscore_f1 | 0.643 |
| coleman_liau | 5.19 |
| coleman_liau_drop | 6.21 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 4.66 |
| fkgl_drop | 3.71 |
| fre | 90.1 |
| fre_gain | 37.3 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 16.0 |
| nli_completeness | 0.968 |
| nli_faithfulness | 0.990 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 65.03 |
| smog | 3.13 |
| smog_drop | 8.08 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `copiously irrigated` -> `washed with a lot of fluid` | replace | - | - | - | - | - | - | - |
| `suction dried` -> `dried with suction` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** The knee was washed with a lot of fluid and then the fluid was pulled out to dry it once again.

| metric | value |
|---|---:|
| bertscore_f1 | 0.476 |
| coleman_liau | 3.23 |
| coleman_liau_drop | 8.17 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.167 |
| fkgl | 6.09 |
| fkgl_drop | 2.28 |
| fre | 88.8 |
| fre_gain | 36.0 |
| human_edit_recall | 1.000 |
| length_ratio | 1.31 |
| n_words | 21.0 |
| nli_completeness | 0.856 |
| nli_faithfulness | 0.883 |
| number_unit_preservation | 1.000 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 58.53 |
| smog | 3.13 |
| smog_drop | 8.08 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `copiously irrigated` -> `washed with a lot of fluid` | replace | attributed | 0.106 | 0.192 | 0.720 | 0.647 | 0.018 | - |
| `suction dried` -> `pulled out to dry it` | replace | attributed | 5.970 | 6.238 | 0.852 | 0.843 | 1.362 | - |

**edit `copiously irrigated` -> `washed with a lot of fluid`**

- status: `attributed`
- log p full -0.7555, empty -0.8617
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.293` [wiktionary] suction: Suction is a force which pushes matter from one space into another due to the pressure difference in 
    - `+0.276` [wiktionary] dried: If something is dry, it has no water or liquid on it.

- rationale: "Copiously irrigated" means flushing a wound or area with a large volume of liquid, and "washed with a lot of fluid" conveys that same action in everyday terms. Phrase frequency rises from Zipf 1.98 to 3.85, making the wording much more familiar. The reader can now picture the cleansing step without needing to interpret clinical jargon.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `suction dried` -> `pulled out to dry it`**

- status: `attributed`
- log p full -1.4452, empty -7.4153
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+3.440` [wiktionary] dried: If something is dry, it has no water or liquid on it.
    - `+2.078` [wiktionary] suction: Suction is a force which pushes matter from one space into another due to the pressure difference in 
    - `+1.288` [readme] suction: Suction is when a machine pulls in gas, liquid, or mucus.
    - `+0.237` [wiktionary] irrigated: To supply farms with water to grow crops.
    - `+0.071` [dictionary] Copiously (adv.): In a copious manner.

- rationale: "Suction dried" refers to removing moisture, and "pulled out to dry it" conveys that same idea of eliminating liquid in everyday terms. Word frequency rises from Zipf 3.28 to 4.40, and age of acquisition drops from 9.42 to 4.40. This lets the reader grasp the drying action without needing the technical term.
- audit: coverage 0.833, grounding_error=True, omission=False, source_ok=False, passage_ok=True

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

**output:** She does not have pain when she pees, any blood in her pee, or a need to go often or trouble starting.

| metric | value |
|---|---:|
| bertscore_f1 | 0.673 |
| coleman_liau | 3.42 |
| coleman_liau_drop | 6.84 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 6.94 |
| fkgl_drop | 4.01 |
| fre | 84.5 |
| fre_gain | 43.0 |
| human_edit_recall | 1.000 |
| length_ratio | 1.10 |
| n_words | 22.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.993 |
| nli_faithfulness | 0.994 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.333 |
| sari | 35.73 |
| smog | 3.13 |
| smog_drop | 9.89 |

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
| `frequency` -> `needing to pee often` | replace | attributed | 1.616 | 2.466 | - | 0.670 | 0.509 | - |
| `hesitancy` -> `trouble starting to pee` | replace | attributed | -0.111 | -0.540 | - | 0.873 | 0.215 | - |

**edit `frequency` -> `needing to pee often`**

- status: `attributed`
- log p full -0.4689, empty -2.0853
- masks scored: 34/34 (+3 top-k)
- ranked sources:
    - `+1.766` [readme] hesitancy: Having difficulty starting to pee or keeping the flow steady.
    - `+1.257` [readme] hesitancy: Having difficulty starting or maintaining a steady flow while peeing.
    - `-0.100` [wiktionary] frequency: Something's frequency is how often it happens.
    - `-0.210` [readme] frequency: How often something happens.

- rationale: "Frequency" refers to how often something happens, so "needing to pee often" directly conveys the same idea of repeated urination in everyday terms. Word frequency drops from Zipf 4.36 to 3.68, while age of acquisition improves from 9.79 to 6.53. This lets the reader immediately grasp the symptom without interpreting a clinical measurement term.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `hesitancy` -> `trouble starting to pee`**

- status: `attributed`
- log p full -0.2910, empty -0.1797
- masks scored: 34/34 (+3 top-k)
- ranked sources:
    - `+0.544` [readme] hesitancy: Having difficulty starting to pee or keeping the flow steady.
    - `+0.330` [readme] FREQUENCY: Frequency is how often something happens.
    - `+0.228` [readme] frequency: How often something happens.
    - `-1.149` [readme] hesitancy: Having difficulty starting or maintaining a steady flow while peeing.

- rationale: "Hesitancy" refers to a delay or difficulty in beginning an action, so "trouble starting to pee" directly conveys that same struggle in everyday words. Word frequency rises from Zipf 2.35 to 3.87, and age of acquisition drops from 12.12 to 4.56. This lets the reader immediately grasp the urinary symptom without needing to interpret a vague medical term.
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

**output:** The patient has chest pain behind the breastbone. Sometimes it feels like a squeezing or tightness, which is a type of heart-related pain.

| metric | value |
|---|---:|
| bertscore_f1 | 0.387 |
| coleman_liau | 9.87 |
| coleman_liau_drop | 6.05 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 4.80 |
| fkgl_drop | 10.00 |
| fre | 81.1 |
| fre_gain | 58.3 |
| human_edit_recall | 1.000 |
| length_ratio | 0.80 |
| n_words | 24.0 |
| nli_completeness | 0.679 |
| nli_faithfulness | 0.767 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.286 |
| sari | 38.01 |
| smog | 7.17 |
| smog_drop | 8.73 |

### Stage 4 - arm `termonly`

**output:** Heart and blood vessels: Chest pain behind the breastbone, occasional heart-related chest pain, and the patient describes it as a tight feeling.

| metric | value |
|---|---:|
| bertscore_f1 | 0.671 |
| coleman_liau | 13.96 |
| coleman_liau_drop | 1.95 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.333 |
| fkgl | 10.69 |
| fkgl_drop | 4.11 |
| fre | 57.6 |
| fre_gain | 34.8 |
| human_edit_recall | 1.000 |
| length_ratio | 0.77 |
| n_words | 23.0 |
| nli_completeness | 0.976 |
| nli_faithfulness | 0.926 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.167 |
| sari | 64.71 |
| smog | 11.21 |
| smog_drop | 4.70 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `retrosternal area` -> `breastbone` | replace | - | - | - | - | - | - | - |
| `anginal pain` -> `heart-related chest pain` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Heart and blood vessels: Chest pain behind the breastbone, occasional heart-related chest pain, and the patient describes it as a feeling of tightness.

| metric | value |
|---|---:|
| bertscore_f1 | 0.674 |
| coleman_liau | 14.18 |
| coleman_liau_drop | 1.73 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.333 |
| fkgl | 11.34 |
| fkgl_drop | 3.46 |
| fre | 54.8 |
| fre_gain | 31.9 |
| human_edit_recall | 1.000 |
| length_ratio | 0.80 |
| n_words | 24.0 |
| nli_completeness | 0.966 |
| nli_faithfulness | 0.914 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 65.33 |
| smog | 11.21 |
| smog_drop | 4.70 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `retrosternal area` -> `breastbone` | replace | attributed | -0.000 | -0.476 | 0.286 | 0.707 | 0.310 | - |
| `anginal pain` -> `heart-related chest pain` | replace | attributed | 0.041 | 1.087 | 0.320 | 0.554 | 0.391 | - |

**edit `retrosternal area` -> `breastbone`**

- status: `attributed`
- log p full -0.0001, empty -0.0000
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.469` [wiktionary] pain: A strong feeling of hurt or discomfort
    - `+0.159` [wiktionary] pain: to sadden or hurt
    - `+0.102` [justplainclear] cardiovascular: About the heart and blood vessels

- rationale: The original term refers to the area behind the sternum, so "breastbone" directly names that central chest landmark in a familiar word. Word frequency rises from Zipf 0.00 to 1.93, though age of acquisition increases from 6.58 to 10.75. The reader can now picture the exact location without needing to decode the directional medical adjective.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `anginal pain` -> `heart-related chest pain`**

- status: `attributed`
- log p full -0.0215, empty -0.0623
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.593` [michigan] pain: An unplesant feeling, a sign from your nerves that something may be wrong. It ca be sharp or dull, sting
    - `+0.202` [thesaurus] cardiovascular: having to do with the heart and blood vessels
    - `+0.152` [nih] cardiovascular: Having to do with the heart and blood vessels.
    - `+0.114` [readme] Cardiovascular: Related to the blood vessels and heart.
    - `+0.015` [justplainclear] cardiovascular: About the heart and blood vessels

- rationale: Anginal pain refers to chest discomfort caused by reduced blood flow to the heart, so "heart-related chest pain" conveys that same meaning in everyday words. Word frequency rises sharply from Zipf 1.10 to 4.28, while age of acquisition shifts slightly from 4.26 to 5.05. The reader can now recognize the symptom's cardiac origin without needing the clinical adjective.
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

**output:** We removed a large part of the tissue lining his joint and the small sac attached to it.

| metric | value |
|---|---:|
| bertscore_f1 | 0.570 |
| coleman_liau | 5.11 |
| coleman_liau_drop | 0.65 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.400 |
| fkgl | 5.85 |
| fkgl_drop | -1.06 |
| fre | 85.2 |
| fre_gain | 4.9 |
| human_edit_recall | 1.000 |
| length_ratio | 1.50 |
| n_words | 18.0 |
| nli_completeness | 0.729 |
| nli_faithfulness | 0.939 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.167 |
| sari | 40.09 |
| smog | 3.13 |
| smog_drop | 5.71 |

### Stage 4 - arm `termonly`

**output:** We cut out a good bit of the lining of his joint and the small sac around it.

| metric | value |
|---|---:|
| bertscore_f1 | 0.664 |
| coleman_liau | 1.57 |
| coleman_liau_drop | 4.20 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.200 |
| fkgl | 4.54 |
| fkgl_drop | 0.25 |
| fre | 94.6 |
| fre_gain | 14.3 |
| human_edit_recall | 1.000 |
| length_ratio | 1.50 |
| n_words | 18.0 |
| nli_completeness | 0.730 |
| nli_faithfulness | 0.938 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 53.01 |
| smog | 3.13 |
| smog_drop | 5.71 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `synovium` -> `the lining of his joint` | replace | - | - | - | - | - | - | - |
| `synovial pouch` -> `the small sac around it` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** We removed a good bit of the soft lining of his joint and the pocket around it.

| metric | value |
|---|---:|
| bertscore_f1 | 0.618 |
| coleman_liau | 3.61 |
| coleman_liau_drop | 2.15 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.400 |
| fkgl | 5.62 |
| fkgl_drop | -0.83 |
| fre | 85.1 |
| fre_gain | 4.8 |
| human_edit_recall | 1.000 |
| length_ratio | 1.42 |
| n_words | 17.0 |
| nli_completeness | 0.675 |
| nli_faithfulness | 0.874 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 50.09 |
| smog | 3.13 |
| smog_drop | 5.71 |

annotation backend `novita`, 3 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `excised` -> `removed` | replace | attributed | 0.869 | 1.211 | 0.042 | 0.288 | 0.066 | - |
| `synovium` -> `soft lining of his joint` | replace | attributed | 4.820 | 4.906 | 0.627 | 0.794 | 0.293 | - |
| `synovial pouch` -> `pocket around it` | replace | attributed | 2.156 | 2.388 | 0.465 | 0.704 | 1.373 | - |

**edit `excised` -> `removed`**

- status: `attributed`
- log p full -0.8838, empty -1.7525
- masks scored: 66/66 (+5 top-k)
- ranked sources:
    - `+0.205` [wiktionary] pouch: A pouch is a small bag or pocket used for carrying things.
    - `+0.139` [readme] Synovial: Relating to the soft tissue that lines joints.
    - `+0.117` [readme] SYNOVIAL: Synovial means having to do with the soft tissue that lines joints.
    - `+0.099` [readme] SYNOVIUM: The slimy layer that covers your joints.
    - `+0.066` [wiktionary] excised: Excise it the tax that is charged on goods produced within the country.

- rationale: "Excised" means to cut out surgically, and "removed" conveys that same action in a more everyday word. Word frequency rises from Zipf 2.58 to 4.79. The reader can now grasp the procedure without needing clinical vocabulary.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `synovium` -> `soft lining of his joint`**

- status: `attributed`
- log p full -2.4871, empty -7.3074
- masks scored: 66/66 (+5 top-k)
- ranked sources:
    - `+3.845` [readme] SYNOVIAL: Synovial means having to do with the soft tissue that lines joints.
    - `+3.552` [readme] Synovial: Relating to the soft tissue that lines joints.
    - `+0.086` [wiktionary] pouch: A pouch is a small bag or pocket used for carrying things.
    - `-0.764` [wiktionary] excised: Excise it the tax that is charged on goods produced within the country.

- rationale: The synovium is the membrane that cushions and lubricates a joint, so calling it the "soft lining of his joint" conveys that same protective role in everyday terms. Word frequency rises from Zipf 1.46 to 3.76, making the replacement much more familiar. The reader can now picture the affected tissue without needing to know a specialized anatomical name.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `synovial pouch` -> `pocket around it`**

- status: `attributed`
- log p full -1.4804, empty -3.6368
- masks scored: 66/66 (+5 top-k)
- ranked sources:
    - `+1.538` [wiktionary] pouch: A pouch is a pocket-like part of an animal's body, used to carry young or store food.
    - `+0.165` [readme] SYNOVIUM: The slimy layer that covers your joints.
    - `-0.220` [readme] Synovial: Relating to the soft tissue that lines joints.

- rationale: The source describes a pouch as a pocket-like body part, so "pocket around it" conveys that same anatomical idea in everyday words. Phrase frequency rises from Zipf 2.32 to 4.46, and age of acquisition drops from 16.00 to 5.94. The reader can now picture a small fluid-filled space near a joint without needing the clinical term.
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

**output:** Doctors must think about whether an infection or poor blood flow is causing the swelling and irritation.

| metric | value |
|---|---:|
| bertscore_f1 | 0.494 |
| coleman_liau | 12.14 |
| coleman_liau_drop | 2.06 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| diagnostic_identity_preservation | 1.000 |
| fkgl | 9.78 |
| fkgl_drop | 3.59 |
| fre | 55.2 |
| fre_gain | 36.4 |
| human_edit_recall | 1.000 |
| length_ratio | 1.31 |
| n_words | 17.0 |
| nli_completeness | 0.976 |
| nli_faithfulness | 0.420 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.400 |
| sari | 19.56 |
| smog | 11.21 |
| smog_drop | 3.35 |

### Stage 4 - arm `termonly`

**output:** A problem like an infection or blocked blood flow must be considered.

| metric | value |
|---|---:|
| bertscore_f1 | 0.759 |
| coleman_liau | 9.28 |
| coleman_liau_drop | 4.92 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 1.000 |
| diagnostic_identity_preservation | 0.000 |
| fkgl | 5.81 |
| fkgl_drop | 7.57 |
| fre | 74.8 |
| fre_gain | 56.0 |
| human_edit_recall | 1.000 |
| length_ratio | 0.92 |
| n_words | 12.0 |
| nli_completeness | 0.771 |
| nli_faithfulness | 0.984 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.250 |
| sari | 35.60 |
| smog | 11.21 |
| smog_drop | 3.35 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `inflammatory process` -> `problem` | replace | - | - | - | - | - | - | - |
| `ischemia` -> `blocked blood flow` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** An illness with redness, warmth, and swelling, such as an infection or poor blood flow, must be thought of.

| metric | value |
|---|---:|
| bertscore_f1 | 0.528 |
| coleman_liau | 8.28 |
| coleman_liau_drop | 5.92 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| diagnostic_identity_preservation | 1.000 |
| fkgl | 6.73 |
| fkgl_drop | 6.65 |
| fre | 80.7 |
| fre_gain | 61.9 |
| human_edit_recall | 1.000 |
| length_ratio | 1.46 |
| n_words | 19.0 |
| nli_completeness | 0.959 |
| nli_faithfulness | 0.361 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.250 |
| sari | 29.22 |
| smog | 8.84 |
| smog_drop | 5.71 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `inflammatory process` -> `illness with redness, warmth, and swelling` | replace | attributed | 12.222 | 12.450 | 0.829 | 0.822 | 9.525 | - |
| `ischemia` -> `poor blood flow` | replace | attributed | -0.315 | -0.387 | 0.364 | 0.735 | 0.472 | - |

**edit `inflammatory process` -> `illness with redness, warmth, and swelling`**

- status: `attributed`
- log p full -1.5921, empty -13.8143
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+9.952` [readme] inflammatory process: When your body gets inflamed, it's like it's telling you there's something wrong by show
    - `+0.427` [michigan] ischemia: When blood supply to an organ or a body part isn't enough, especially the heart.
    - `+0.340` [readme] Ischemia: Ischemia is when there's a lack of blood flow due to blocked blood vessels.
    - `+0.314` [iowa] ISCHEMIA: decreased oxygen in a tissue (usually because of decreased blood flow)
    - `+0.099` [nih] ischemia: Lack of blood supply to a part of the body. Ischemia may cause tissue damage due to the lack of oxyg

- rationale: The glossary explains that inflammation is the body's way of signaling a problem through redness, warmth, and swelling, so the replacement spells out those visible signs instead of using the abstract medical phrase. Word frequency drops from Zipf 3.71 to 2.82, but age of acquisition improves markedly from 13.33 to 7.00. Readers can now connect the term to familiar physical sensations they have likely experienced themselves.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `ischemia` -> `poor blood flow`**

- status: `attributed`
- log p full -1.8552, empty -1.5399
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.679` [iowa] ISCHEMIA: decreased oxygen in a tissue (usually because of decreased blood flow)
    - `+0.207` [readme] ischemia: Not enough blood flow due to blocked or narrowed blood vessels.
    - `+0.072` [nih] ischemia: Lack of blood supply to a part of the body. Ischemia may cause tissue damage due to the lack of oxyg
    - `+0.012` [michigan] ischemia: When blood supply to an organ or a body part isn't enough, especially the heart.
    - `-0.255` [readme] Ischemia: Ischemia is when there's a lack of blood flow due to blocked blood vessels.

- rationale: Ischemia means a restriction in blood supply to tissues, so "poor blood flow" conveys that same idea in everyday words. Word frequency rises from Zipf 2.85 to 4.43, and age of acquisition drops from 18.00 to 7.40. Readers can now grasp the circulatory problem without needing clinical vocabulary.
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

**output:** The doctor asked her to take a higher dose of prednisone when she goes home.

| metric | value |
|---|---:|
| bertscore_f1 | 0.627 |
| coleman_liau | 5.81 |
| coleman_liau_drop | 0.57 |
| copy_jargon_rate | 1.000 |
| critical_error | 0.000 |
| drug_preservation | 1.000 |
| fkgl | 4.42 |
| fkgl_drop | -1.56 |
| fre | 90.1 |
| fre_gain | -5.9 |
| human_edit_recall | 0.000 |
| length_ratio | 1.25 |
| n_words | 15.0 |
| nli_completeness | 0.975 |
| nli_faithfulness | 0.601 |
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

**output:** I have asked her to increase her medicine that lowers swelling when she goes home.

| metric | value |
|---|---:|
| bertscore_f1 | 0.780 |
| coleman_liau | 8.13 |
| coleman_liau_drop | -1.75 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| drug_preservation | 0.000 |
| fkgl | 5.99 |
| fkgl_drop | -3.14 |
| fre | 78.8 |
| fre_gain | -17.1 |
| human_edit_recall | 1.000 |
| length_ratio | 1.25 |
| n_words | 15.0 |
| nli_completeness | 0.002 |
| nli_faithfulness | 0.246 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 66.67 |
| smog | 8.84 |
| smog_drop | -5.71 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `prednisone` -> `medicine that lowers swelling` | replace | attributed | 7.601 | 7.986 | - | 0.833 | 2.420 | - |

**edit `prednisone` -> `medicine that lowers swelling`**

- status: `attributed`
- log p full -1.1409, empty -8.7419
- masks scored: 10/10 (+2 top-k)
- ranked sources:
    - `+4.536` [readme] Prednisone: A medication that lowers the body's immune response and inflammation.
    - `+2.116` [nih] prednisone: A drug used to reduce inflammation and lower the body’s immune response.  It is used with other dr
    - `+0.761` [readme] prednisone: A medication that helps lower the body's immune system reactions.

- rationale: Prednisone is a corticosteroid drug that reduces inflammation, so calling it a "medicine that lowers swelling" captures its main purpose in everyday terms. Word frequency rises from Zipf 2.56 to 3.18, and age of acquisition drops from 17.17 to 5.53. This lets the reader grasp the treatment’s role without needing to know the specific drug name.
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

**output:** She might need other medicines for nerve pain if necessary.

| metric | value |
|---|---:|
| bertscore_f1 | 0.817 |
| coleman_liau | 9.66 |
| coleman_liau_drop | 2.83 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 7.19 |
| fkgl_drop | 3.02 |
| fre | 61.3 |
| fre_gain | 23.4 |
| human_edit_recall | 1.000 |
| length_ratio | 1.11 |
| n_words | 10.0 |
| nli_completeness | 0.895 |
| nli_faithfulness | 0.972 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.750 |
| sari | 25.16 |
| smog | 11.21 |
| smog_drop | 0.00 |
| uncertainty_preservation | 1.000 |

### Stage 4 - arm `termonly`

**output:** She may need other pain medicines for nerve pain as needed.

| metric | value |
|---|---:|
| bertscore_f1 | 0.913 |
| coleman_liau | 6.82 |
| coleman_liau_drop | 5.67 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 4.79 |
| fkgl_drop | 5.42 |
| fre | 80.3 |
| fre_gain | 42.4 |
| human_edit_recall | 1.000 |
| length_ratio | 1.22 |
| n_words | 11.0 |
| nli_completeness | 0.867 |
| nli_faithfulness | 0.905 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.500 |
| sari | 51.81 |
| smog | 8.84 |
| smog_drop | 2.37 |
| uncertainty_preservation | 1.000 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `neuropathic` -> `for nerve pain` | replace | - | - | - | - | - | - | - |

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
| `neuropathic` -> `nerve pain` | replace | attributed | 4.082 | 7.503 | - | 1.000 | 0.053 | - |

**edit `neuropathic` -> `nerve pain`**

- status: `attributed`
- log p full -0.0327, empty -4.1148
- masks scored: 6/6 (+1 top-k)
- ranked sources:
    - `+3.622` [readme] Neuropathic: Neuropathic means nerve pain.
    - `+3.569` [readme] neuropathic: Nerve pain.

- rationale: Neuropathic refers to pain caused by damaged nerves, and "nerve pain" conveys that same idea in everyday words. Word frequency rises from Zipf 2.35 to 4.13, while age of acquisition drops from 15.40 to 9.67. This lets the reader immediately grasp the type of pain without needing clinical terminology.
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

**output:** A dose of antibiotics was given to help prevent infection.

| metric | value |
|---|---:|
| bertscore_f1 | 0.670 |
| coleman_liau | 9.08 |
| coleman_liau_drop | 2.38 |
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
| nli_faithfulness | 0.979 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 66.67 |
| smog | 11.21 |
| smog_drop | 0.00 |

### Stage 4 - arm `termonly`

**output:** A preventive dose of infection-fighting medicine was given.

| metric | value |
|---|---:|
| bertscore_f1 | 0.789 |
| coleman_liau | 16.75 |
| coleman_liau_drop | -5.29 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 12.61 |
| fkgl_drop | -0.18 |
| fre | 18.9 |
| fre_gain | 0.5 |
| human_edit_recall | 1.000 |
| length_ratio | 1.29 |
| n_words | 9.0 |
| nli_completeness | 0.803 |
| nli_faithfulness | 0.989 |
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
| `antibiotics` -> `infection-fighting medicine` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** A protective dose of medicine that kills bacteria was given.

| metric | value |
|---|---:|
| bertscore_f1 | 0.680 |
| coleman_liau | 10.24 |
| coleman_liau_drop | 1.22 |
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
| nli_completeness | 0.793 |
| nli_faithfulness | 0.959 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 28.96 |
| smog | 13.02 |
| smog_drop | -1.82 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `prophylactic` -> `protective` | replace | attributed | 2.312 | 3.028 | 0.911 | 0.954 | 3.317 | - |
| `antibiotics` -> `medicine that kills bacteria` | replace | attributed | 7.267 | 8.380 | 0.888 | 0.838 | 6.330 | - |

**edit `prophylactic` -> `protective`**

- status: `attributed`
- log p full -0.6209, empty -2.9330
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+3.919` [readme] prophylactic: A prophylactic is like a protective shield that helps prevent diseases.
    - `+0.602` [nih] prophylactic: In medicine, something that prevents or protects.
    - `+0.343` [readme] Antibiotics: Medicine that kills bacteria.
    - `-0.121` [wiktionary] prophylactic: Something that is prophylactic serves to prevent or protect against a disease or pregnancy.
    - `-0.160` [wiktionary] antibiotics: An antibiotic is a drug that stops the growth of or destroys bacteria and other such microorganis

- rationale: The glossary explains that a prophylactic acts like a protective shield to prevent disease, so "protective" directly conveys that same preventive function in everyday terms. Word frequency rises from Zipf 2.59 to 4.13, and age of acquisition drops from 15.20 to 8.00. Readers can now grasp the idea of a safeguard without encountering a rare, late-learned medical term.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `antibiotics` -> `medicine that kills bacteria`**

- status: `attributed`
- log p full -0.3985, empty -7.6659
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+8.516` [readme] Antibiotics: Medicine that kills bacteria.
    - `+2.185` [wiktionary] antibiotics: An antibiotic is a drug that stops the growth of or destroys bacteria and other such microorganis
    - `+1.040` [nih] prophylactic: In medicine, something that prevents or protects.
    - `+0.110` [wiktionary] prophylactic: Something that is prophylactic serves to prevent or protect against a disease or pregnancy.
    - `+0.001` [readme] PROPHYLACTIC: Preventive measures or treatments to avoid getting sick.

- rationale: Antibiotics are drugs that target and destroy bacteria, so "medicine that kills bacteria" directly conveys that same function in everyday terms. Word frequency rises slightly from Zipf 3.74 to 3.89, and age of acquisition drops from 9.55 to 9.28. This phrasing lets the reader grasp the treatment's purpose without needing the clinical label.
- audit: coverage 0.833, grounding_error=False, omission=False, source_ok=False, passage_ok=True

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

**output:** The patient has long-lasting low potassium levels caused by ongoing diarrhea.

| metric | value |
|---|---:|
| bertscore_f1 | 0.584 |
| coleman_liau | 15.78 |
| coleman_liau_drop | 6.02 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.286 |
| fkgl | 13.37 |
| fkgl_drop | 2.88 |
| fre | 18.8 |
| fre_gain | 29.5 |
| human_edit_recall | 1.000 |
| length_ratio | 1.33 |
| n_words | 12.0 |
| nli_completeness | 0.901 |
| nli_faithfulness | 0.979 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 41.27 |
| smog | 14.55 |
| smog_drop | -3.35 |
| temporality_preservation | 1.000 |

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

**output:** Long-lasting low potassium caused by ongoing runny poop.

| metric | value |
|---|---:|
| bertscore_f1 | 0.516 |
| coleman_liau | 14.58 |
| coleman_liau_drop | 7.22 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.375 |
| fkgl | 11.13 |
| fkgl_drop | 5.12 |
| fre | 29.5 |
| fre_gain | 40.3 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 9.0 |
| nli_completeness | 0.889 |
| nli_faithfulness | 0.982 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 35.24 |
| smog | 13.02 |
| smog_drop | -1.82 |
| temporality_preservation | 1.000 |

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

**output:** There is no swelling or tenderness in the liver or spleen.

| metric | value |
|---|---:|
| bertscore_f1 | 0.469 |
| coleman_liau | 6.29 |
| coleman_liau_drop | 16.91 |
| copy_jargon_rate | 0.500 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 4.79 |
| fkgl_drop | 1.83 |
| fre | 80.3 |
| fre_gain | 25.6 |
| human_edit_recall | 0.500 |
| length_ratio | 1.22 |
| n_words | 11.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.985 |
| nli_faithfulness | 0.588 |
| replacement_f1 | 0.667 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 45.57 |
| smog | 8.84 |
| smog_drop | 0.00 |

### Stage 4 - arm `termonly`

**output:** The liver and spleen are not enlarged or painful.

| metric | value |
|---|---:|
| bertscore_f1 | 0.535 |
| coleman_liau | 6.69 |
| coleman_liau_drop | 16.51 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 3.65 |
| fkgl_drop | 2.97 |
| fre | 84.9 |
| fre_gain | 30.2 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 9.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.975 |
| nli_faithfulness | 0.894 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 39.68 |
| smog | 3.13 |
| smog_drop | 5.71 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `tenderness` -> `painful` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** The liver and spleen are not enlarged, and there is no pain when the area is touched.

| metric | value |
|---|---:|
| bertscore_f1 | 0.483 |
| coleman_liau | 5.32 |
| coleman_liau_drop | 17.88 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 5.62 |
| fkgl_drop | 1.00 |
| fre | 85.1 |
| fre_gain | 30.4 |
| human_edit_recall | 1.000 |
| length_ratio | 1.89 |
| n_words | 17.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.928 |
| nli_faithfulness | 0.144 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 41.19 |
| smog | 8.84 |
| smog_drop | 0.00 |

annotation backend `novita`, 0 edits kept


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

**output:** He did not feel pain in the front left side of his chest when he exercised.

| metric | value |
|---|---:|
| bertscore_f1 | 0.763 |
| coleman_liau | 3.74 |
| coleman_liau_drop | 6.24 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 3.93 |
| fkgl_drop | 5.16 |
| fre | 95.4 |
| fre_gain | 45.9 |
| human_edit_recall | 1.000 |
| laterality_preservation | 0.500 |
| length_ratio | 1.45 |
| n_words | 16.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.975 |
| nli_faithfulness | 0.988 |
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
| `experience` -> `feel` | replace | attributed | 0.063 | 1.380 | 0.836 | 0.829 | 2.449 | - |
| `anterior` -> `front` | replace | attributed | 0.002 | 0.092 | 0.233 | 0.533 | 0.438 | - |

**edit `experience` -> `feel`**

- status: `attributed`
- log p full -0.0222, empty -0.0853
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+2.662` [thesaurus] experience: feel, have, go through
    - `+0.213` [nih] anterior: In human anatomy, has to do with the front of a structure, or a structure found toward the front of 
    - `+0.103` [wiktionary] experience: Experience is the amount of time you have been doing something (especially, a job).
    - `+0.059` [readme] Anterior: The front part of the body or an organ.

- rationale: "Experience" refers to personally encountering or undergoing something, and "feel" conveys that same direct, personal perception in simpler terms. Word frequency rises from Zipf 5.27 to 5.67, and age of acquisition drops from 8.95 to 5.11. The reader can now grasp the idea of a personal sensation without needing a more abstract word.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `anterior` -> `front`**

- status: `attributed`
- log p full -0.0199, empty -0.0218
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.739` [readme] Anterior: The front part of the body or an organ.
    - `+0.300` [wiktionary] experience: An experience is an event that happens to you or that you are a part of.
    - `+0.287` [michigan] anterior: The front of the body.
    - `-0.266` [thesaurus] experience: feel, have, go through
    - `-0.311` [readme] anterior: Having to do with the front part of the body or an organ.

- rationale: "Anterior" refers to a position toward the front of the body, so using "front" directly conveys that same spatial meaning. Word frequency rises from Zipf 3.51 to 5.28, and age of acquisition drops from 14.12 to 5.19. The reader can now instantly grasp the directional term without needing anatomical vocabulary.
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

**output:** Also, she would use it to control the atrial fibrillation.

| metric | value |
|---|---:|
| bertscore_f1 | 0.612 |
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
| nli_faithfulness | 0.653 |
| replacement_f1 | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 25.32 |
| smog | 8.84 |
| smog_drop | 0.00 |

### Stage 4 - arm `termonly`

**output:** Also, would use it to control the uneven heartbeat.

| metric | value |
|---|---:|
| bertscore_f1 | 0.803 |
| coleman_liau | 7.33 |
| coleman_liau_drop | 1.93 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 6.28 |
| fkgl_drop | 1.31 |
| fre | 66.1 |
| fre_gain | 9.4 |
| human_edit_recall | 1.000 |
| length_ratio | 0.90 |
| n_words | 9.0 |
| nli_completeness | 0.419 |
| nli_faithfulness | 0.849 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 66.67 |
| smog | 8.84 |
| smog_drop | 0.00 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `atrial fibrillation` -> `uneven heartbeat` | replace | - | - | - | - | - | - | - |

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
| `atrial fibrillation` -> `irregular heartbeat` | replace | attributed | 0.890 | 1.999 | - | 0.905 | 2.727 | - |

**edit `atrial fibrillation` -> `irregular heartbeat`**

- status: `attributed`
- log p full -0.2547, empty -1.1450
- masks scored: 10/10 (+2 top-k)
- ranked sources:
    - `+2.394` [readme] Atrial fibrillation: Atrial fibrillation is when your heart beats irregularly and can make you tired or more l
    - `-0.333` [readme] atrial fibrillation: Atrial fibrillation is when your heart beats in a weird way that can make you tired and i
    - `-0.635` [justplainclear] atrial fibrillation: A problem with the speed or rhythm that your heart beats It is the most common type of ar

- rationale: Atrial fibrillation refers to a heart rhythm that is erratic and often rapid, so calling it an "irregular heartbeat" captures that same idea in everyday words. Word frequency rises from Zipf 2.58 to 3.38, and age of acquisition drops from 14.58 to 9.16. This lets the reader grasp the core heart‑rhythm problem without needing to know the clinical name.
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

**output:** The patient seems to be able to give a clear and accurate medical history.

| metric | value |
|---|---:|
| bertscore_f1 | 0.396 |
| coleman_liau | 6.94 |
| coleman_liau_drop | 4.01 |
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
| nli_completeness | 0.631 |
| nli_faithfulness | 0.049 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.250 |
| sari | 26.28 |
| smog | 13.02 |
| smog_drop | 0.00 |

### Stage 4 - arm `termonly`

**output:** Overall the patient seems to give a clear and reliable account of their health.

| metric | value |
|---|---:|
| bertscore_f1 | 0.475 |
| coleman_liau | 9.01 |
| coleman_liau_drop | 1.94 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 7.57 |
| fkgl_drop | 3.56 |
| fre | 65.7 |
| fre_gain | 36.2 |
| human_edit_recall | 1.000 |
| length_ratio | 1.40 |
| n_words | 14.0 |
| nli_completeness | 0.358 |
| nli_faithfulness | 0.057 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 37.72 |
| smog | 11.21 |
| smog_drop | 1.82 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `seemingly` -> `seems` | replace | - | - | - | - | - | - | - |
| `good historian` -> `clear and reliable account of their health` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Overall the patient appears to give a clear and accurate account of their health.

| metric | value |
|---|---:|
| bertscore_f1 | 0.473 |
| coleman_liau | 9.84 |
| coleman_liau_drop | 1.11 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 7.57 |
| fkgl_drop | 3.56 |
| fre | 65.7 |
| fre_gain | 36.2 |
| human_edit_recall | 1.000 |
| length_ratio | 1.40 |
| n_words | 14.0 |
| nli_completeness | 0.233 |
| nli_faithfulness | 0.035 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 37.72 |
| smog | 11.21 |
| smog_drop | 1.82 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `seemingly` -> `appears` | replace | attributed | 0.422 | 0.958 | - | 0.885 | 1.279 | - |
| `good historian` -> `clear and accurate account of their health` | replace | attributed | 2.303 | 2.542 | - | 0.728 | 0.260 | - |

**edit `seemingly` -> `appears`**

- status: `attributed`
- log p full -0.3952, empty -0.8169
- masks scored: 18/18 (+3 top-k)
- ranked sources:
    - `+1.420` [dictionary] Seemingly (adv.): In appearance; in show; in semblance; apparently; ostensibly.
    - `+0.141` [wiktionary] historian: A historian is a person who studies or writes about history.
    - `-0.183` [wiktionary] good: When you are good, you do the right things. That is, you do things that are kind or helpful. You do not 
    - `-0.996` [wiktionary] good: If something is good it is useful or helpful. This also means high quality.

- rationale: "Seemingly" means something looks a certain way based on what you can see, and "appears" carries that same sense of visible impression in a simpler word. Word frequency rises from Zipf 4.10 to 4.84, making the replacement more common in everyday language. The reader can now grasp the visual judgment without the slightly formal tone of the original.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `good historian` -> `clear and accurate account of their health`**

- status: `attributed`
- log p full -1.4668, empty -3.7700
- masks scored: 18/18 (+3 top-k)
- ranked sources:
    - `+0.907` [wiktionary] good: When you are good, you do the right things. That is, you do things that are kind or helpful. You do not 
    - `+0.648` [wiktionary] historian: A historian is a person who studies or writes about history.
    - `+0.102` [dictionary] Seemingly (adv.): In appearance; in show; in semblance; apparently; ostensibly.

- rationale: The original term describes a patient who can give a reliable, detailed medical history, so the replacement directly conveys that the information is both clear and accurate. Phrase frequency rises from Zipf 3.90 to 4.37, and age of acquisition drops from 11.58 to 9.44. This lets the reader immediately grasp that the patient’s account was trustworthy without needing to decode clinical shorthand.
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

**output:** No signs of active Crohn's disease were seen during the colonoscopy.

| metric | value |
|---|---:|
| bertscore_f1 | 0.594 |
| coleman_liau | 11.04 |
| coleman_liau_drop | -1.38 |
| copy_jargon_rate | 1.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 3.72 |
| fkgl_drop | -0.07 |
| fre | 88.0 |
| fre_gain | 1.3 |
| human_edit_recall | 0.000 |
| length_ratio | 0.86 |
| n_words | 12.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.991 |
| nli_faithfulness | 0.984 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 1.000 |
| sari | 19.09 |
| smog | 3.13 |
| smog_drop | 0.00 |

### Stage 4 - arm `termonly`

**output:** No signs of an ongoing bowel condition were seen during the camera test of the large intestine.

| metric | value |
|---|---:|
| bertscore_f1 | 0.531 |
| coleman_liau | 9.07 |
| coleman_liau_drop | 0.59 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 9.78 |
| fkgl_drop | -6.13 |
| fre | 55.2 |
| fre_gain | -31.5 |
| human_edit_recall | 1.000 |
| length_ratio | 1.21 |
| n_words | 17.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.100 |
| nli_faithfulness | 0.947 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.200 |
| sari | 16.78 |
| smog | 14.55 |
| smog_drop | -11.43 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `colonoscopy` -> `camera test of the large intestine` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** No signs of a currently flaring bowel condition were found during the exam of the large intestine.

| metric | value |
|---|---:|
| bertscore_f1 | 0.414 |
| coleman_liau | 10.09 |
| coleman_liau_drop | -0.43 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.750 |
| fkgl | 9.78 |
| fkgl_drop | -6.13 |
| fre | 55.2 |
| fre_gain | -31.5 |
| human_edit_recall | 1.000 |
| length_ratio | 1.21 |
| n_words | 17.0 |
| negation_preservation | 1.000 |
| nli_completeness | 0.065 |
| nli_faithfulness | 0.954 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 15.51 |
| smog | 13.02 |
| smog_drop | -9.89 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `colonoscopy` -> `exam of the large intestine` | replace | attributed | 8.495 | 8.937 | 0.812 | 0.945 | 3.175 | - |

**edit `colonoscopy` -> `exam of the large intestine`**

- status: `attributed`
- log p full -1.0284, empty -9.5230
- masks scored: 66/66 (+2 top-k)
- ranked sources:
    - `+3.827` [justplainclear] colonoscopy: An exam of the inside of the large intestine that uses a flexible tube with a lens at the end
    - `+0.652` [readme] active: Currently happening.
    - `+0.551` [readme] Active: Happening right now.
    - `+0.495` [nih] colonoscopy: Examination of the inside of the colon using a colonoscope, inserted into the rectum. A colonosco
    - `+0.426` [readme] von Willebrand 's disease: A condition where blood can't clot properly, causing abnormal bleeding.

- rationale: The glossary defines a colonoscopy as an internal examination using a flexible tube, so "exam of the large intestine" conveys the core procedure in everyday terms. Word frequency rises from Zipf 2.74 to 3.19, and age of acquisition drops from 15.76 to 9.28. Patients can now grasp what the test involves without needing to know the clinical name.
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

**output:** Shortly after the first check-up, the patient started complaining of chest pain. The nurse noticed she seemed more and more tired and was having trouble breathing.

| metric | value |
|---|---:|
| bertscore_f1 | 0.657 |
| coleman_liau | 11.82 |
| coleman_liau_drop | 4.15 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.250 |
| fkgl | 6.73 |
| fkgl_drop | 9.63 |
| fre | 70.0 |
| fre_gain | 44.1 |
| human_edit_recall | 1.000 |
| length_ratio | 0.96 |
| n_words | 27.0 |
| nli_completeness | 0.023 |
| nli_faithfulness | 0.993 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.600 |
| sari | 17.65 |
| smog | 7.17 |
| smog_drop | 8.73 |
| temporality_preservation | 1.000 |

### Stage 4 - arm `termonly`

**output:** Shortly after the first check-up, the patient seemed to start complaining of chest pain and looked to the nurse like they had growing tiredness and trouble breathing.

| metric | value |
|---|---:|
| bertscore_f1 | 0.736 |
| coleman_liau | 12.53 |
| coleman_liau_drop | 3.44 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 11.55 |
| fkgl_drop | 4.81 |
| fre | 60.4 |
| fre_gain | 34.5 |
| human_edit_recall | 1.000 |
| length_ratio | 1.00 |
| n_words | 28.0 |
| nli_completeness | 0.993 |
| nli_faithfulness | 0.993 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.600 |
| sari | 21.96 |
| smog | 11.21 |
| smog_drop | 4.70 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 1 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `respiratory distress` -> `trouble breathing` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** Shortly after the first check-up, the patient seemed to start complaining of chest pain and looked to the nurse to be getting more and more tired and having trouble breathing.

| metric | value |
|---|---:|
| bertscore_f1 | 0.705 |
| coleman_liau | 10.86 |
| coleman_liau_drop | 5.11 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.250 |
| fkgl | 12.24 |
| fkgl_drop | 4.12 |
| fre | 60.8 |
| fre_gain | 34.9 |
| human_edit_recall | 1.000 |
| length_ratio | 1.11 |
| n_words | 31.0 |
| nli_completeness | 0.993 |
| nli_faithfulness | 0.991 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.600 |
| sari | 24.00 |
| smog | 8.84 |
| smog_drop | 7.06 |
| temporality_preservation | 1.000 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `mounting exhaustion` -> `getting more and more tired` | replace | attributed | 0.150 | 0.215 | - | 0.714 | 0.600 | - |
| `respiratory distress` -> `having trouble breathing` | replace | attributed | 0.071 | 0.684 | - | 0.848 | 0.575 | - |

**edit `mounting exhaustion` -> `getting more and more tired`**

- status: `attributed`
- log p full -1.1246, empty -1.2743
- masks scored: 31/34 (+4 top-k)
- ranked sources:
    - `+0.743` [wiktionary] mounting: If you mount something you get on to it.
    - `+0.143` [readme] acute respiratory distress syndrome: A serious lung condition that causes low levels of oxygen in the blood, w
    - `-0.108` [wiktionary] exhaustion: Exhaustion is the point where something is completely depleted.
    - `-0.110` [readme] Respiratory Distress: Having difficulty breathing.

- rationale: “Mounting exhaustion” describes a tiredness that builds up over time, and “getting more and more tired” conveys that same gradual increase in plain words. Word frequency rises from Zipf 3.34 to 4.64, while age of acquisition drops from 7.61 to 4.62. The reader can now grasp the progressive nature of the fatigue without needing to interpret the less common phrasing.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `respiratory distress` -> `having trouble breathing`**

- status: `attributed`
- log p full -0.0778, empty -0.1487
- masks scored: 31/34 (+4 top-k)
- ranked sources:
    - `+0.789` [readme] Respiratory Distress: Having difficulty breathing.
    - `+0.214` [wiktionary] mounting: If you mount something you get on to it.
    - `+0.102` [wiktionary] exhaustion: Exhaustion is the point where something is completely depleted.
    - `+0.049` [readme] acute respiratory distress syndrome: A serious lung condition that causes low levels of oxygen in the blood, w
    - `+0.023` [wiktionary] exhaustion: Exhaustion is the state of extreme tiredness.

- rationale: Respiratory distress refers to difficulty with the act of breathing, and "having trouble breathing" conveys that same struggle in everyday words. Word frequency rises from Zipf 3.57 to 4.15, while age of acquisition drops from 11.16 to 4.56. The reader can now recognize a breathing emergency without needing clinical terminology.
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

**output:** She has been sent to get a heart-rhythm device placed.

| metric | value |
|---|---:|
| bertscore_f1 | 0.465 |
| coleman_liau | 6.18 |
| coleman_liau_drop | 5.50 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 1.29 |
| fkgl_drop | 6.89 |
| fre | 103.6 |
| fre_gain | 53.0 |
| human_edit_recall | 1.000 |
| length_ratio | 1.22 |
| n_words | 11.0 |
| nli_completeness | 0.326 |
| nli_faithfulness | 0.979 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 20.09 |
| smog | 3.13 |
| smog_drop | 8.08 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `referred` -> `sent` | replace | - | - | - | - | - | - | - |
| `pacemaker implantation` -> `heart-rhythm device placed` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

**output:** She has been sent to get a device put in her chest to help control her heartbeat.

| metric | value |
|---|---:|
| bertscore_f1 | 0.466 |
| coleman_liau | 4.29 |
| coleman_liau_drop | 7.38 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.500 |
| fkgl | 4.92 |
| fkgl_drop | 3.26 |
| fre | 90.1 |
| fre_gain | 39.4 |
| human_edit_recall | 1.000 |
| length_ratio | 1.89 |
| n_words | 17.0 |
| nli_completeness | 0.087 |
| nli_faithfulness | 0.859 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 20.09 |
| smog | 3.13 |
| smog_drop | 8.08 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `referred` -> `sent` | replace | attributed | 0.000 | 1.229 | 0.822 | 0.937 | 1.823 | - |
| `pacemaker implantation` -> `device put in her chest to help control her heartbeat` | replace | attributed | 5.404 | 5.584 | 0.814 | 0.896 | 1.802 | - |

**edit `referred` -> `sent`**

- status: `attributed`
- log p full -0.0000, empty -0.0001
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+2.501` [readme] REFERRED: Sending a patient to another person or place for medical care.
    - `+0.678` [justplainclear] pacemaker: A medical device placed inside your chest or abdomen that helps control your heartbeat
    - `+0.382` [readme] implantation: Surgery where a device is placed inside your body.
    - `+0.227` [readme] pacemaker: A pacemaker is a device that uses electrical signals to regulate the heartbeat.
    - `+0.189` [readme] IMPLANTATION: A surgery where a device is placed inside the body.

- rationale: "Referred" means directing someone to another place or person, and "sent" conveys that same action of transfer in a simpler way. Word frequency rises from Zipf 4.61 to 5.16, making it a more familiar term. The reader can now immediately grasp that they are being directed elsewhere without processing a less common word.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `pacemaker implantation` -> `device put in her chest to help control her heartbeat`**

- status: `attributed`
- log p full -1.8001, empty -7.2043
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+2.561` [readme] pacemaker: A small device that helps regulate the heartbeat when placed in the chest.
    - `+0.759` [nih] pacemaker: An electronic device that is implanted in the body to monitor heart rate and rhythm. It gives the h
    - `+0.550` [readme] implantation: Surgery where a device is placed inside your body.
    - `+0.535` [justplainclear] pacemaker: A medical device placed inside your chest or abdomen that helps control your heartbeat
    - `+0.463` [readme] IMPLANTATION: A surgery where a device is placed inside the body.

- rationale: The glossary explains a pacemaker implantation as placing a small device in the chest to regulate heartbeat, so the replacement directly conveys that action and purpose in everyday terms. Phrase frequency rises from Zipf 2.69 to 3.56, and age of acquisition drops from 12.42 to 8.06. This lets the reader grasp the procedure's basic function without needing the clinical name.
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

**output:** There was some bruising and swelling where the catheter went in.

| metric | value |
|---|---:|
| bertscore_f1 | 0.629 |
| coleman_liau | 9.45 |
| coleman_liau_drop | -5.03 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 4.79 |
| fkgl_drop | -5.46 |
| fre | 80.3 |
| fre_gain | -33.8 |
| human_edit_recall | 1.000 |
| length_ratio | 0.85 |
| n_words | 11.0 |
| nli_completeness | 0.543 |
| nli_faithfulness | 0.767 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 52.53 |
| smog | 8.84 |
| smog_drop | -5.71 |

### Stage 4 - arm `termonly`

**output:** There was some bruise-like swelling where the tube went in.

| metric | value |
|---|---:|
| bertscore_f1 | 0.577 |
| coleman_liau | 9.08 |
| coleman_liau_drop | -4.65 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 2.47 |
| fkgl_drop | -3.14 |
| fre | 95.2 |
| fre_gain | -18.9 |
| human_edit_recall | 1.000 |
| length_ratio | 0.85 |
| n_words | 11.0 |
| nli_completeness | 0.666 |
| nli_faithfulness | 0.560 |
| replacement_f1 | 1.000 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 50.36 |
| smog | 3.13 |
| smog_drop | 0.00 |

annotation backend `novita`, 2 edits kept


| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `hematoma` -> `bruise-like swelling` | replace | - | - | - | - | - | - | - |
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
| `hematoma` -> `bruising` | replace | attributed | 1.118 | 3.725 | 0.715 | 0.790 | 0.065 | - |
| `cath site` -> `where the tube went in` | replace | attributed | 0.029 | 0.048 | 0.304 | 0.653 | 0.232 | - |

**edit `hematoma` -> `bruising`**

- status: `attributed`
- log p full -0.0522, empty -1.1705
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+3.020` [michigan] hematoma: A bruise or when your skin is black and blue after an injury.
    - `+2.955` [iowa] HEMATOMA: a bruise, a black and blue mark
    - `+0.094` [wiktionary] site: A site is a website.
    - `+0.060` [nih] hematoma: A pool of clotted or partially clotted blood in an organ, tissue, or body space, usually caused by a

- rationale: A hematoma is a collection of clotted blood outside a vessel, so calling it "bruising" captures that same idea of blood pooling under the skin in everyday language. Word frequency rises from Zipf 2.61 to 3.18, and age of acquisition drops from 14.78 to 9.44. Readers can now recognize the symptom as a common bruise without needing the clinical term.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `cath site` -> `where the tube went in`**

- status: `attributed`
- log p full -0.8795, empty -0.9081
- masks scored: 66/66 (+4 top-k)
- ranked sources:
    - `+0.352` [nih] hematoma: A pool of clotted or partially clotted blood in an organ, tissue, or body space, usually caused by a
    - `+0.120` [iowa] HEMATOMA: a bruise, a black and blue mark
    - `+0.108` [wiktionary] site: A site is a website.
    - `+0.032` [michigan] hematoma: A bruise or when your skin is black and blue after an injury.
    - `-0.196` [justplainclear] hematoma: A collection of blood under the skin or in the body that is typically caused by a broken blood vesse

- rationale: "Cath site" refers to the spot on the body where a catheter was inserted, and "where the tube went in" conveys that same location in everyday words. Word frequency rises from Zipf 2.90 to 4.32, and age of acquisition drops from 8.63 to 5.50. This lets the reader immediately picture the entry point without needing to know the clinical shorthand.
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

annotation backend `novita`, 1 edits kept

- rejected: DROP non-term  'abdomen' -> 'belly'  (orig is not exactly one extracted hard term)

| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `necrotic tissue` -> `dead tissue` | replace | - | - | - | - | - | - | - |

### Stage 4 - arm `grounded`

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

annotation backend `novita`, 1 edits kept

- rejected: DROP non-term  'abdomen' -> 'belly'  (orig is not exactly one extracted hard term)

| edit | type | status | effect (nats) | logit | LDS held | LDS in | margin | top-1 drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `necrotic tissue` -> `dead tissue` | replace | attributed | -0.046 | -1.157 | 0.663 | 0.881 | 0.093 | - |

**edit `necrotic tissue` -> `dead tissue`**

- status: `attributed`
- log p full -0.0683, empty -0.0220
- masks scored: 66/66 (+2 top-k)
- ranked sources:
    - `+1.290` [readme] necrotic: Tissue or skin death.
    - `+1.197` [readme] Necrotic: Necrotic means when tissue or skin dies.
    - `+0.466` [nih] tissue: A group or layer of cells that work together to perform a specific function.
    - `-0.163` [wiktionary] tissue: Tissue is a group of cells that work together to do a job.
    - `-0.670` [wiktionary] tissue: A piece of tissue is a sheet of paper that can absorb very well.

- rationale: "Necrotic tissue" refers to body tissue that has died, so calling it "dead tissue" conveys the same meaning in everyday words. Word frequency rises from Zipf 2.54 to 4.26, and age of acquisition drops from 15.07 to 5.17. Readers can now immediately grasp the condition without needing clinical vocabulary.
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
| `hemostatic` -> `not bleeding` | replace | attributed | -0.164 | -3.048 | - | 0.800 | 2.830 | - |

**edit `hemostatic` -> `not bleeding`**

- status: `attributed`
- log p full -0.1733, empty -0.0089
- masks scored: 6/6 (+1 top-k)
- ranked sources:
    - `-0.203` [readme] hemostatic: Hemostatic means stopping bleeding.
    - `-3.033` [readme] hemostatic: Stopping blood flow.

- rationale: "Hemostatic" describes something that stops or controls bleeding, so "not bleeding" conveys the same idea in everyday terms. Word frequency rises sharply from Zipf 1.73 to 4.08, making the replacement far more familiar. Readers can now grasp the intended state without needing to decode a technical medical adjective.
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

**output:** The area was washed with saline and cleaned out.

| metric | value |
|---|---:|
| bertscore_f1 | 0.628 |
| coleman_liau | 6.04 |
| coleman_liau_drop | 1.29 |
| copy_jargon_rate | 0.500 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 3.65 |
| fkgl_drop | 0.00 |
| fre | 84.9 |
| fre_gain | 0.0 |
| human_edit_recall | 0.500 |
| length_ratio | 0.82 |
| n_words | 9.0 |
| nli_completeness | 0.989 |
| nli_faithfulness | 0.994 |
| replacement_f1 | 0.667 |
| replacement_precision | 1.000 |
| rewrite_aggressiveness | 0.667 |
| sari | 52.61 |
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
| `lavaged` -> `washed out` | replace | attributed | 1.830 | 2.243 | - | 0.913 | 0.964 | - |
| `saline` -> `salt water` | replace | attributed | 0.012 | 0.446 | - | 0.811 | 1.610 | - |

**edit `lavaged` -> `washed out`**

- status: `attributed`
- log p full -0.9731, empty -2.8035
- masks scored: 34/34 (+4 top-k)
- ranked sources:
    - `+1.229` [readme] lavaged: To clean out an organ or wound with fluid.
    - `+0.264` [wiktionary] saline: If something is saline it is salty, especially water containing salt.
    - `+0.202` [readme] saline: A solution made of saltwater that matches the body's fluid concentration and can be used to replace lo
    - `+0.135` [readme] Saline: Salt water solution used to replace body fluids.

- rationale: "Lavaged" means a body cavity or wound was cleansed with fluid, so "washed out" conveys the same action in familiar, everyday terms. Word frequency rises sharply from Zipf 0.00 to 4.10, making the replacement far more common and recognizable. The reader can now immediately grasp the cleansing procedure without encountering a rare medical verb.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True

**edit `saline` -> `salt water`**

- status: `attributed`
- log p full -0.0210, empty -0.0327
- masks scored: 34/34 (+4 top-k)
- ranked sources:
    - `+2.266` [readme] Saline: Salt water solution used to replace body fluids.
    - `+0.656` [nih] saline: A solution of salt and water.
    - `-0.809` [wiktionary] saline: If something is saline it is salty, especially water containing salt.
    - `-1.884` [readme] saline: A solution made of saltwater that matches the body's fluid concentration and can be used to replace lo

- rationale: Saline is simply a mixture of salt and water, so calling it "salt water" directly names its two ingredients. Word frequency rises from Zipf 3.33 to 4.55, and age of acquisition drops from 11.71 to 5.05. This lets the reader immediately picture a familiar kitchen substance instead of a clinical term.
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
| `inability to ambulate` -> `not being able to walk` | replace | attributed | 0.757 | 3.592 | 0.868 | 0.916 | 0.855 | - |

**edit `inability to ambulate` -> `not being able to walk`**

- status: `attributed`
- log p full -0.0326, empty -0.7896
- masks scored: 66/66 (+2 top-k)
- ranked sources:
    - `+1.332` [michigan] inability: Not able to.
    - `+0.477` [wiktionary] ambulate: If you ambulate yourself, you relocate yourself under the power of your own legs.
    - `+0.220` [wiktionary] inability: An inability is something that you can not do.
    - `+0.156` [wiktionary] to: To has no meaning. It is used with a bare infinitival clause.
    - `+0.132` [wiktionary] to: To shows where something goes, the goal of movement.

- rationale: The Michigan glossary defines "inability to ambulate" as not being able to walk, so the replacement directly states that meaning in everyday terms. Word frequency rises sharply from Zipf 1.40 to 4.87, and age of acquisition drops from 10.67 to 7.79. This lets the reader immediately grasp the mobility limitation without decoding clinical jargon.
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

**output:** There is a bulge or weak spot on the left side of the body.

| metric | value |
|---|---:|
| bertscore_f1 | 0.355 |
| coleman_liau | 0.73 |
| coleman_liau_drop | -0.65 |
| copy_jargon_rate | 0.000 |
| critical_error | 0.000 |
| definition_borrow_rate | 1.000 |
| fkgl | 2.51 |
| fkgl_drop | -0.23 |
| fre | 102.0 |
| fre_gain | 9.0 |
| human_edit_recall | 1.000 |
| laterality_preservation | 1.000 |
| length_ratio | 1.17 |
| n_words | 14.0 |
| nli_completeness | 0.015 |
| nli_faithfulness | 0.937 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.000 |
| sari | 60.64 |
| smog | 3.13 |
| smog_drop | 5.71 |

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
| `hernia` -> `bulge` | replace | attributed | 0.062 | 0.245 | - | 0.830 | 0.192 | - |

**edit `hernia` -> `bulge`**

- status: `attributed`
- log p full -0.2638, empty -0.3262
- masks scored: 10/10 (+2 top-k)
- ranked sources:
    - `+0.625` [nih] hernia: The bulging of an internal organ through a weak area or tear in the muscle or other tissue that holds 
    - `+0.433` [justplainclear] hernia: When part of an organ or tissue inside of you bulges through a weak area of muscle. Most hernias are i

- rationale: A hernia is a condition where tissue pushes through a weak spot in muscle, and calling it a "bulge" captures that same idea of something protruding where it shouldn't. Word frequency rises from Zipf 3.00 to 3.24, and age of acquisition drops from 12.29 to 8.10. Readers can now grasp the physical problem without needing to know a specialized medical label.
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

**output:** The doctors checked the other parts of the body and found nothing unusual.

| metric | value |
|---|---:|
| bertscore_f1 | 0.404 |
| coleman_liau | 9.14 |
| coleman_liau_drop | 2.26 |
| copy_jargon_rate | 0.000 |
| critical_error | 1.000 |
| definition_borrow_rate | 0.000 |
| fkgl | 7.63 |
| fkgl_drop | 0.74 |
| fre | 63.5 |
| fre_gain | 10.6 |
| human_edit_recall | 1.000 |
| length_ratio | 1.30 |
| n_words | 13.0 |
| negation_preservation | 0.000 |
| nli_completeness | 0.934 |
| nli_faithfulness | 0.438 |
| replacement_f1 | 0.000 |
| replacement_precision | 0.000 |
| rewrite_aggressiveness | 0.667 |
| sari | 8.52 |
| smog | 8.84 |
| smog_drop | 0.00 |

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
| `unremarkable` -> `normal` | replace | attributed | -0.001 | -0.643 | - | - | - | - |

**edit `unremarkable` -> `normal`**

- status: `attributed`
- log p full -0.0022, empty -0.0011
- masks scored: 4/4 (+1 top-k)
- ranked sources:
    - `-1.012` [wiktionary] unremarkable: If something is unremarkable, it is common and ordinary.

- rationale: "Unremarkable" is a medical way of saying that something shows no cause for concern, so replacing it with "normal" directly conveys that everything is as expected. Word frequency rises from Zipf 2.83 to 5.01, and age of acquisition drops from 11.06 to 5.53. This lets the reader immediately grasp a clean bill of health without decoding clinical understatement.
- audit: coverage 1.0, grounding_error=False, omission=False, source_ok=True, passage_ok=True
