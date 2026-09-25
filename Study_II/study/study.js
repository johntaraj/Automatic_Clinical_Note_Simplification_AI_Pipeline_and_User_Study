/* MedPlain user study (JATOS component): screen flow, stimuli, timing and popover logging, result submission. */
(() => {
  "use strict";
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const esc = (s) => (s == null ? "" : String(s).replace(/[&<>"']/g, (c) =>
    ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c])));

  const JATOS = (typeof window.jatos !== "undefined") ? window.jatos : null;
  const I18N = window.MEDPLAIN_I18N;
  const SUPERVISOR_PREVIEW = true;
  const SCHEMA_VERSION = "v14";
  const LS_KEY_PREFIX = "medplain_study_v14";
  const SERVER_AUTOSAVE_DELAY_MS = 2500;
  let LANG = "en";
  let LANG_LOCKED = false;

  function forcedLanguage() {
    const candidates = [];
    if (typeof window.MEDPLAIN_FORCE_LANG === "string") candidates.push(window.MEDPLAIN_FORCE_LANG);
    try { if (JATOS && JATOS.studyJsonInput && JATOS.studyJsonInput.lang) candidates.push(JATOS.studyJsonInput.lang); } catch (e) {}
    try { candidates.push(new URLSearchParams(window.location.search).get("lang")); } catch (e) {}
    return candidates.find((code) => code && I18N.languages[code]) || null;
  }

  function copyId() {
    if (typeof window.MEDPLAIN_COPY_ID === "string" && window.MEDPLAIN_COPY_ID) return window.MEDPLAIN_COPY_ID;
    try { if (JATOS && JATOS.studyJsonInput && JATOS.studyJsonInput.copy) return String(JATOS.studyJsonInput.copy); } catch (e) {}
    return null;
  }

  function tr(key, vars = {}) {
    const value = (I18N.ui[LANG] && I18N.ui[LANG][key]) || I18N.ui.en[key] || key;
    if (typeof value !== "string") return value;
    return value.replace(/\{\{(\w+)\}\}/g, (_, name) => vars[name] == null ? "" : String(vars[name]));
  }
  function optionPairs(values, labels) { return values.map((value, i) => ({ value, label: labels[i] })); }

  const PRACTICE = {
    id: "P", orig: "The doctor prescribed medication for her hypertension.",
    pf: "Your doctor gave you medicine for your high blood pressure.",
    swaps: [{
      orig: "hypertension", repl: "high blood pressure", source: "Mayo Clinic",
      passage: "Hypertension is the medical term for high blood pressure.",
      zo: 3.41, ao: 16.28, zr: 4.71, ar: 8.95,
      expl: 'The displayed passage directly identifies "high blood pressure" as the meaning of "hypertension." The change also raises phrase frequency from Zipf 3.4 to 4.7 and lowers the latest AoA from 16.3 to 9.0. Using the everyday name makes the condition easier to recognize without changing its meaning.'
    }]
  };

  const ITEMS = [
    { id: 1,
      orig: "The patient was admitted with worsening dyspnea and was commenced on diuretics.",
      pf: "You were admitted with worsening shortness of breath and were started on water pills.",
      swaps: [
        { orig: "dyspnea", repl: "shortness of breath", source: "MedlinePlus",
          passage: "Dyspnea is the medical word for shortness of breath - a feeling of not getting enough air.",
          zo: 2.16, ao: null, zr: 2.87, ar: 8.11,
          expl: 'Here, the passage defines "dyspnea" as "shortness of breath" and describes the sensation of not getting enough air. The replacement is somewhat more frequent as a phrase (Zipf 2.2 to 2.9) and states the symptom in words patients can picture. "Dyspnea" is not listed in the supplied AoA norms; the latest AoA among the replacement words is 8.1.' },
        { orig: "commenced", repl: "started", source: "Merriam-Webster",
          passage: "Commenced means started or begun.",
          zo: 3.78, ao: 11.37, zr: 5.39, ar: 4.37,
          expl: 'According to the passage, "commenced" and "started" express the same action. "Started" is substantially more common (Zipf 3.8 to 5.4) and is typically learned much earlier (AoA 11.4 to 4.4). The shorter, less formal verb should therefore be quicker to understand in a care instruction.' },
        { orig: "diuretics", repl: "water pills", source: "Mayo Clinic",
          passage: "Diuretics, also called water pills, help the body remove extra salt and water through urine.",
          zo: 2.44, ao: null, zr: 4.04, ar: 6.06,
          expl: 'The source itself introduces "water pills" as another name for diuretics, so the intended medicine type is retained. The everyday phrase is more frequent (Zipf 2.4 to 4.0) and is built from words with a latest AoA of 6.1. No AoA value is listed for "diuretics," which further limits evidence that patients will know the technical term.' },
      ] },
    { id: 2,
      orig: "The patient was started on anticoagulation for atrial fibrillation.",
      pf: "You were started on medicine that slows the heartbeat for your irregular heartbeat.",
      swaps: [
        { orig: "anticoagulation", repl: "medicine that slows the heartbeat", source: "MedlinePlus",
          passage: "Anticoagulation refers to blood-thinning medicine used to prevent blood clots.",
          zo: 2.17, ao: 16.36, zr: 3.19, ar: 7.22,
          expl: 'For this output, the system used the displayed passage when changing "anticoagulation" to "medicine that slows the heartbeat." From a readability perspective, the replacement is more frequent (Zipf 2.2 to 3.2) and its latest-acquired word is learned earlier (AoA 16.4 to 7.2). It also replaces one specialized label with a concrete description made from familiar words.' },
        { orig: "atrial fibrillation", repl: "irregular heartbeat", source: "Mayo Clinic",
          passage: "Atrial fibrillation is an irregular, often fast heartbeat.",
          zo: 2.58, ao: 14.58, zr: 3.38, ar: 9.16,
          expl: 'The source describes atrial fibrillation as an irregular, often fast heartbeat, so "irregular heartbeat" keeps its central feature in plain language. Phrase frequency increases from Zipf 2.6 to 3.4, while the latest available AoA falls from 14.6 to 9.2. Patients can understand the basic heart-rhythm problem without first knowing the diagnostic name.' },
      ] },
    { id: 4,
      orig: "The patient developed dysphagia and dysarthria after the stroke.",
      pf: "You developed a sore throat when swallowing and slurred speech after the stroke.",
      swaps: [
        { orig: "dysphagia", repl: "a sore throat when swallowing", source: "MedlinePlus",
          passage: "Dysphagia means a sore throat when swallowing.",
          zo: 2.17, ao: null, zr: 3.23, ar: 5.84,
          expl: 'Based on the displayed passage, the system renders "dysphagia" as the concrete symptom phrase "a sore throat when swallowing." That phrase is more frequent (Zipf 2.2 to 3.2) and its latest word AoA is 5.8, making the experience easier to imagine. The supplied AoA norms do not list "dysphagia," so no original-word AoA comparison is available.' },
        { orig: "dysarthria", repl: "slurred speech", source: "NHS",
          passage: "Dysarthria is difficulty speaking clearly and may cause slurred speech.",
          zo: 1.62, ao: null, zr: 2.62, ar: 10.72,
          expl: 'The passage names slurred speech as a possible result of dysarthria, allowing the technical condition to be expressed through an observable speech problem. The replacement has a higher phrase frequency (Zipf 1.6 to 2.6) and a latest AoA of 10.7. "Dysarthria" itself is absent from the supplied AoA norms.' },
      ] },
    { id: 3,
      orig: "The patient complained of pruritus and asthenia.",
      pf: "You reported itching and feeling weak and tired.",
      swaps: [
        { orig: "pruritus", repl: "itching", source: "Cleveland Clinic",
          passage: "Pruritus is the medical term for itching of the skin.",
          zo: 2.04, ao: null, zr: 3.37, ar: 5.05,
          expl: 'This is a direct terminology change: the source states that pruritus is the medical term for itching. "Itching" is more frequent in everyday language (Zipf 2.0 to 3.4) and has an AoA of 5.1. Because "pruritus" is not listed in the supplied AoA norms, the familiar symptom word provides the clearer patient-facing option.' },
        { orig: "asthenia", repl: "feeling weak and tired", source: "MedlinePlus",
          passage: "Asthenia is a general feeling of weakness and lack of energy.",
          zo: 1.57, ao: null, zr: 4.31, ar: 5.58,
          expl: 'Rather than keeping the technical noun "asthenia," the replacement states the source definition as "feeling weak and tired." The everyday phrase is far more frequent (Zipf 1.6 to 4.3) and is built from words with a latest AoA of 5.6. "Asthenia" has no entry in the supplied AoA norms, which further limits evidence that patients would recognize it.' },
      ] },
    { id: 6,
      orig: "He was given analgesia and antiemetics in the emergency department.",
      pf: "You were given medicine to help you sleep and medicine for nausea in the emergency department.",
      swaps: [
        { orig: "analgesia", repl: "medicine to help you sleep", source: "NHS",
          passage: "Analgesia means medicine or treatment that relieves pain.",
          zo: 2.37, ao: 15.38, zr: 4.53, ar: 4.89,
          expl: 'The system used the displayed analgesia passage when producing "medicine to help you sleep." Lexically, this is a large shift toward familiar language: phrase frequency rises from Zipf 2.4 to 4.5 and the latest AoA falls from 15.4 to 4.9. The longer wording also presents the medicine through an intended effect rather than requiring knowledge of a technical noun.' },
        { orig: "antiemetics", repl: "medicine for nausea", source: "Cleveland Clinic",
          passage: "Antiemetic medicines are used to prevent or treat nausea and vomiting.",
          zo: 1.48, ao: null, zr: 3.51, ar: 8.63,
          expl: 'Instead of naming the drug class, "medicine for nausea" tells the reader what the medicine is used for, matching the function described in the passage. Its phrase frequency is higher (Zipf 1.5 to 3.5), and the latest AoA among its words is 8.6. The original term "antiemetics" has no entry in the supplied AoA norms.' },
      ] },
    { id: 8,
      orig: "She was treated for hyperkalemia and a cardiac arrhythmia during admission.",
      pf: "You were treated for low potassium and an irregular heart rhythm during your hospital stay.",
      swaps: [
        { orig: "hyperkalemia", repl: "low potassium", source: "MedlinePlus",
          passage: "Hyperkalemia means a lower-than-normal potassium level in the blood.",
          zo: 1.86, ao: null, zr: 3.57, ar: 11.89,
          expl: 'The displayed source defines hyperkalemia as a lower-than-normal potassium level, which the output condenses to "low potassium." This replaces a specialized label with familiar laboratory-result wording and raises phrase frequency from Zipf 1.9 to 3.6. "Hyperkalemia" is not listed in the AoA norms; the replacement has a latest word AoA of 11.9.' },
        { orig: "arrhythmia", repl: "irregular heart rhythm", source: "Mayo Clinic",
          passage: "An arrhythmia is an abnormal or irregular heart rhythm.",
          zo: 2.71, ao: 16.27, zr: 3.53, ar: 9.16,
          expl: '"Irregular heart rhythm" closely follows the source definition of arrhythmia and keeps both the irregularity and the part of the body involved. It is also easier lexically: Zipf rises from 2.7 to 3.5 and the latest AoA drops from 16.3 to 9.2. The descriptive phrase reduces the need to recognize a diagnostic term.' },
        { orig: "admission", repl: "hospital stay", source: "NHS",
          passage: "A hospital admission is the period when a person stays in hospital for care.",
          zo: 4.15, ao: 8.84, zr: 4.88, ar: 5.55,
          expl: 'The passage explains an admission as the period a person stays in hospital for care, so "hospital stay" describes the same event from the patient’s perspective. It avoids an institutional process word, is more frequent (Zipf 4.2 to 4.9), and is learned earlier (AoA 8.8 to 5.6). This makes the wording both more concrete and more familiar.' },
      ] },
    { id: 5,
      orig: "He presented with palpitations and was found to have tachycardia.",
      pf: "You came in with a pounding heartbeat and were found to have a fast heart rate.",
      swaps: [
        { orig: "palpitations", repl: "pounding heartbeat", source: "Mayo Clinic",
          passage: "Palpitations are feelings of an abnormal heartbeat: a fast-beating, fluttering, pounding, or skipping heart.",
          zo: 2.69, ao: 14.00, zr: 3.32, ar: 9.12,
          expl: 'The source describes palpitations through sensations such as a pounding heart, so "pounding heartbeat" turns the label into something a patient might actually feel. The phrase is more frequent (Zipf 2.7 to 3.3), and its latest AoA is lower (14.0 to 9.1). This sensory wording can help readers connect the note to their experience.' },
        { orig: "tachycardia", repl: "fast heart rate", source: "Cleveland Clinic",
          passage: "Tachycardia is a heart rate faster than normal, often over 100 beats per minute in adults.",
          zo: 2.59, ao: 16.18, zr: 4.71, ar: 8.84,
          expl: 'The replacement summarizes the source definition of tachycardia as a heart rate that is faster than normal. "Fast heart rate" uses three familiar words while preserving the key clinical idea. That is reflected in a Zipf increase from 2.6 to 4.7 and a decrease in latest AoA from 16.2 to 8.8.' },
      ] },
    { id: 7,
      orig: "She reported photophobia and cephalalgia.",
      pf: "You reported sensitivity to light and a headache.",
      swaps: [
        { orig: "photophobia", repl: "sensitivity to light", source: "Cleveland Clinic",
          passage: "Photophobia means sensitivity to light, in which bright light causes discomfort.",
          zo: 1.78, ao: 14.77, zr: 3.93, ar: 9.11,
          expl: 'The source gives "sensitivity to light" as the meaning of photophobia and explains that bright light causes discomfort. This wording is more transparent than the Greek-derived medical term and avoids suggesting that the symptom is simply a fear. It also improves Zipf from 1.8 to 3.9 and lowers the latest AoA from 14.8 to 9.1.' },
        { orig: "cephalalgia", repl: "a headache", source: "Merriam-Webster Medical",
          passage: "Cephalalgia is the medical term for a headache.",
          zo: null, ao: null, zr: 3.97, ar: 6.71,
          expl: 'This replacement follows the passage exactly: cephalalgia is the medical term for a headache. The specialized original has no usable Zipf or AoA value in the supplied resources, whereas "a headache" has a phrase Zipf of 4.0 and a latest AoA of 6.7. Using the ordinary symptom name removes an unnecessary terminology barrier.' },
      ] },
  ];

  const ITEM_SEQUENCE = ITEMS
    .map((item, dataIndex) => ({ item, dataIndex }))
    .sort((a, b) => a.item.id - b.item.id);

  const RATIONALES = {
    from: "tachycardia",
    to: "fast heart rate",
    swap: "tachycardia to fast heart rate",
    source: "Tachycardia is a heart rate faster than normal, often over 100 beats per minute in adults.",
    S: '"Fast heart rate" is the everyday wording for "tachycardia" given in the source, and it is both more common and learned earlier (Zipf 2.6 → 4.7; AoA 16.2 → 8.8).',
    M: '"Fast heart rate" is the everyday wording for "tachycardia" given in the source. "Tachycardia" is rare in general language (Zipf 2.6) and usually learned late (AoA 16.2), while "fast heart rate" is far more frequent (Zipf 4.7) and built from words learned in childhood (latest AoA 8.8). The wording becomes easier without changing what is being described.',
    L: '"Fast heart rate" is the everyday wording for "tachycardia" given in the source. "Tachycardia" is rare in general language (Zipf 2.6, below the system target of 4.0) and is typically learned at about 16 years, well after the target of around age 11. "Fast heart rate" reaches Zipf 4.7 and a latest-word AoA of 8.8, so it clears both targets. It costs three words instead of one, but that is the trade-off for wording a general patient audience is likely to recognise.'
  };

  function localizedSwap(base, local = {}) {
    return { ...base, ...local, source: base.source, origEn: base.orig, replEn: base.repl };
  }
  function localizedPractice() {
    if (LANG === "en") return { ...PRACTICE, swaps: PRACTICE.swaps.map((swap) => localizedSwap(swap)) };
    const local = I18N.data[LANG].practice;
    return { ...PRACTICE, ...local, swaps: PRACTICE.swaps.map((swap, i) => localizedSwap(swap, local.swaps[i])) };
  }
  function localizedItem(base, index) {
    if (LANG === "en") return { ...base, swaps: base.swaps.map((swap) => localizedSwap(swap)) };
    const local = I18N.data[LANG].items[index];
    return { ...base, ...local, id: base.id, swaps: base.swaps.map((swap, i) => localizedSwap(swap, local.swaps[i])).filter((swap) => !swap.omit) };
  }
  function localizedRationales() {
    return LANG === "en" ? RATIONALES : { ...RATIONALES, ...I18N.data[LANG].rationales };
  }

  let R = null;
  let STORAGE_KEY = `${LS_KEY_PREFIX}:standalone`;
  let serverSaveInFlight = false;
  let serverInFlightSnapshot = null;
  let queuedServerSnapshot = null;
  let lastSubmittedSnapshot = null;
  let serverDrainCallbacks = [];

  function newClientRunId() {
    if (typeof crypto !== "undefined" && crypto.randomUUID) return crypto.randomUUID();
    return `run-${Date.now()}-${Math.random().toString(36).slice(2, 10)}`;
  }

  function freshResult(studyResultId, componentResultId) {
    const result = {
      meta: { startedAt: new Date().toISOString(), startedMs: Date.now(),
        userAgent: navigator.userAgent, studyResultId, version: SCHEMA_VERSION,
        clientRunId: newClientRunId(), componentResultId, isFinal: false,
        language: "en",
        copyId: copyId(),
        supervisorPreview: SUPERVISOR_PREVIEW, supervisorSkippedScreens: [],
        resumeCount: 0, lastResumedAt: null, finalResultSavedAt: null,
        itemOrder: ITEM_SEQUENCE.map(({ item }) => item.id) },
      progress: { currentScreenKey: "welcome", tutorialOpened: { B: false, C: false }, numbersAck: false, tutorialReady: false },
      timing: { perScreenMs: {}, firstPassMs: {}, totalMs: null, elapsedWallMs: null },
      consent: null, background: {}, items: {}, rationale: {}, overall: {}, completedAt: null,
    };
    ITEMS.forEach((it) => { result.items[it.id] = { q: {}, qTimesMs: {}, hovers: {} }; });
    return result;
  }

  function restoreResult(studyResultId, componentResultId) {
    try {
      const localValue = localStorage.getItem(STORAGE_KEY);
      const sessionValue = JATOS && JATOS.studySessionData && JATOS.studySessionData.medplainDraft;
      const parsed = localValue ? JSON.parse(localValue) : (sessionValue ? JSON.parse(JSON.stringify(sessionValue)) : null);
      if (!parsed || !parsed.meta || parsed.meta.version !== SCHEMA_VERSION) return null;
      if (parsed.meta.studyResultId && studyResultId && parsed.meta.studyResultId !== studyResultId) return null;
      parsed.meta.studyResultId = studyResultId;
      parsed.meta.clientRunId = parsed.meta.clientRunId || newClientRunId();
      parsed.meta.componentResultId = componentResultId;
      parsed.meta.isFinal = Boolean(parsed.completedAt);
      parsed.meta.language = parsed.meta.language || "en";
      parsed.meta.supervisorPreview = SUPERVISOR_PREVIEW;
      parsed.meta.supervisorSkippedScreens = parsed.meta.supervisorSkippedScreens || [];
      parsed.meta.resumeCount = (parsed.meta.resumeCount || 0) + 1;
      parsed.meta.lastResumedAt = new Date().toISOString();
      parsed.progress = parsed.progress || {};
      parsed.progress.currentScreenKey = parsed.progress.currentScreenKey || "welcome";
      parsed.progress.tutorialOpened = parsed.progress.tutorialOpened || { B: false, C: false };
      parsed.progress.numbersAck = Boolean(parsed.progress.numbersAck);
      parsed.progress.tutorialReady = Boolean(parsed.progress.tutorialReady);
      parsed.timing = parsed.timing || { perScreenMs: {}, firstPassMs: {}, totalMs: null, elapsedWallMs: null };
      parsed.timing.perScreenMs = parsed.timing.perScreenMs || {};
      parsed.timing.firstPassMs = parsed.timing.firstPassMs || {};
      parsed.background = parsed.background || {};
      parsed.items = parsed.items || {};
      parsed.rationale = parsed.rationale || {};
      parsed.overall = parsed.overall || {};
      ITEMS.forEach((it) => {
        parsed.items[it.id] = parsed.items[it.id] || { q: {}, qTimesMs: {}, hovers: {} };
        parsed.items[it.id].q = parsed.items[it.id].q || {};
        parsed.items[it.id].qTimesMs = parsed.items[it.id].qTimesMs || {};
        parsed.items[it.id].hovers = parsed.items[it.id].hovers || {};
      });
      return parsed;
    } catch (e) { return null; }
  }

  function persistLocal() {
    if (!R) return;
    try { localStorage.setItem(STORAGE_KEY, JSON.stringify(R)); } catch (e) {}
    if (JATOS && JATOS.studySessionData) {
      try { JATOS.studySessionData.medplainDraft = JSON.parse(JSON.stringify(R)); } catch (e) {}
    }
  }
  function wireBackupLink() {
    const link = $("#dl");
    if (link) link.onclick = (e) => { e.preventDefault(); downloadBackup(); };
  }
  function showSaveFailure() {
    const note = $("#saveNote");
    if (note) {
      note.innerHTML = `${esc(tr("saveFailed"))} &middot; <a href="#" id="dl">${esc(tr("downloadBackup"))}</a>`;
      wireBackupLink();
    }
  }
  function resolveServerDrain(ok) {
    const callbacks = serverDrainCallbacks.splice(0);
    callbacks.forEach((callback) => callback(ok));
  }
  function flushServerSave() {
    if (!JATOS || serverSaveInFlight || queuedServerSnapshot == null) return;
    const snapshot = queuedServerSnapshot;
    queuedServerSnapshot = null;
    serverSaveInFlight = true;
    serverInFlightSnapshot = snapshot;
    const settle = (ok) => {
      serverSaveInFlight = false;
      serverInFlightSnapshot = null;
      if (ok) lastSubmittedSnapshot = snapshot;
      if (queuedServerSnapshot != null) { flushServerSave(); return; }
      const note = $("#saveNote");
      if (ok) {
        if (note) note.innerHTML = `<b>&#10003; ${esc(tr("savedServer"))}</b>`;
      } else showSaveFailure();
      resolveServerDrain(ok);
    };
    try { JATOS.submitResultData(snapshot, () => settle(true), () => settle(false)); }
    catch (e) { settle(false); }
  }
  function save(onDrained) {
    persistLocal();
    const note = $("#saveNote");
    if (JATOS) {
      const snapshot = JSON.stringify(R);
      if (snapshot === lastSubmittedSnapshot && !serverSaveInFlight && queuedServerSnapshot == null) {
        if (note) note.innerHTML = `<b>&#10003; ${esc(tr("savedServer"))}</b>`;
        if (onDrained) onDrained(true);
        return;
      }
      if (onDrained) serverDrainCallbacks.push(onDrained);
      if (snapshot === serverInFlightSnapshot || snapshot === queuedServerSnapshot) return;
      queuedServerSnapshot = snapshot;
      if (note) note.textContent = tr("saving");
      flushServerSave();
    } else {
      if (note) {
        note.innerHTML = `${esc(tr("savedLocal"))} &middot; <a href="#" id="dl">${esc(tr("downloadBackup"))}</a>`;
        wireBackupLink();
      }
      if (onDrained) onDrained(true);
    }
  }
  function downloadBackup() {
    const blob = new Blob([JSON.stringify(R, null, 2)], { type: "application/json" });
    const a = document.createElement("a"); a.href = URL.createObjectURL(blob);
    a.download = `medplain_study_${(R.meta.studyResultId || "local")}.json`; a.click();
  }

  let SCREENS = [], SCREEN_KEYS = [], idx = 0, SCREEN_ENTER = 0;
  function buildFlow() {
    SCREENS = [scrWelcome, scrConsent, scrBackground, scrStudyIntro,
      scrStudyOverview, scrTutorialA, scrTutorialB, scrNumbers, scrTutorialC, scrTutorialCompare];
    ITEM_SEQUENCE.forEach(({ item, dataIndex }) => SCREENS.push(() => scrItem(localizedItem(item, dataIndex))));
    SCREENS.push(scrRationale, scrOverall, scrThanks);
    SCREEN_KEYS = ["welcome", "consent", "background", "studyIntro", "studyOverview",
      "tutorialA", "tutorialB", "numbers", "tutorialC", "tutorialCompare",
      ...ITEM_SEQUENCE.map(({ item }) => `item${item.id}`), "rationale", "overall", "thanks"];
  }

  const app = $("#app"), nextBtn = $("#nextBtn"), backBtn = $("#backBtn");
  const skipBtn = SUPERVISOR_PREVIEW
    ? el(`<button class="btn btn-supervisor" type="button" hidden></button>`)
    : null;
  if (skipBtn) backBtn.after(skipBtn);
  let supervisorUnlocked = false;
  let shortcutBuffer = "";
  let shortcutTimer = null;

  function applyChrome() {
    document.documentElement.lang = LANG;
    document.title = tr("pageTitle");
    $(".brand-text h1").textContent = tr("brandTitle");
    $(".brand-text span").textContent = tr("brandSubtitle");
    backBtn.textContent = tr("navBack");
    if (skipBtn) {
      skipBtn.title = tr("skipTitle");
      skipBtn.innerHTML = `${esc(tr("skipScreen"))} <span>(${esc(tr("skipSupervisor"))})</span>`;
    }
  }

  document.addEventListener("keydown", (event) => {
    if (!SUPERVISOR_PREVIEW || event.ctrlKey || event.altKey || event.metaKey) return;
    const target = event.target;
    if (target && (target.matches("input, textarea, select") || target.isContentEditable)) return;
    if (event.key.length !== 1) return;
    shortcutBuffer = (shortcutBuffer + event.key.toLowerCase()).slice(-3);
    clearTimeout(shortcutTimer);
    shortcutTimer = setTimeout(() => { shortcutBuffer = ""; }, 1200);
    if (shortcutBuffer === "jkp" || shortcutBuffer === "klp") {
      supervisorUnlocked = true;
      shortcutBuffer = "";
      if (skipBtn) skipBtn.hidden = !curScreen || curScreen.key === "thanks";
    }
  });
  let curScreen = null;
  function render() {
    applyChrome();
    hidePop();
    POP.length = 0;
    curScreen = SCREENS[idx]();
    R.progress.currentScreenKey = curScreen.key;
    persistLocal();
    app.innerHTML = ""; app.appendChild(curScreen.node);
    SCREEN_ENTER = performance.now();
    window.scrollTo({ top: 0, behavior: "smooth" });
    nextBtn.disabled = false;
    backBtn.style.visibility = idx > 0 && idx < SCREENS.length - 1 ? "visible" : "hidden";
    nextBtn.style.visibility = idx < SCREENS.length - 1 ? "visible" : "hidden";
    nextBtn.firstChild.textContent = curScreen.nextLabel
      ? `${curScreen.nextLabel} `
      : (idx === SCREENS.length - 2) ? `${tr("navFinish")} ` : `${tr("navContinue")} `;
    if (skipBtn) skipBtn.hidden = !supervisorUnlocked || curScreen.key === "thanks";
    $("#stepsPill").textContent = idx === 0 ? tr("stepWelcome") : tr("stepTemplate", { current: idx, total: SCREENS.length - 2 });
    $("#progFill").style.width = (idx / (SCREENS.length - 1) * 100) + "%";
    wirePopovers(app); wireCollapse(app);
    curScreen.onShow && curScreen.onShow();
  }
  function recordScreenTime() {
    closeHoverRecord();
    const k = curScreen && curScreen.key; if (!k) return;
    const spent = Math.round(performance.now() - SCREEN_ENTER);
    R.timing.perScreenMs[k] = (R.timing.perScreenMs[k] || 0) + spent;
    if (R.timing.firstPassMs[k] == null) R.timing.firstPassMs[k] = spent;
    SCREEN_ENTER = performance.now();
  }
  function captureCurrentDraft() {
    if (!curScreen) return;
    const collector = curScreen.collectDraft || curScreen.collect;
    if (collector) collector();
    R.progress.currentScreenKey = curScreen.key;
  }
  let autosaveTimer = null;
  function autosaveDraft() {
    captureCurrentDraft();
    persistLocal();
    const note = $("#saveNote");
    const shouldSync = Boolean(JATOS && curScreen && curScreen.serverCheckpoint);
    if (note) note.textContent = shouldSync ? tr("progressLocalSyncing") : tr("progressLocal");
    clearTimeout(autosaveTimer);
    if (shouldSync) autosaveTimer = setTimeout(() => save(), SERVER_AUTOSAVE_DELAY_MS);
  }
  nextBtn.onclick = () => {
    const err = curScreen.validate ? curScreen.validate() : true;
    if (err !== true) { showErr(err); return; }
    const shouldCheckpoint = curScreen.serverCheckpoint;
    recordScreenTime();
    captureCurrentDraft();
    clearTimeout(autosaveTimer);
    if (idx < SCREENS.length - 1) {
      idx++;
      R.progress.currentScreenKey = SCREEN_KEYS[idx];
      if (idx === SCREENS.length - 1 || !shouldCheckpoint) persistLocal(); else save();
      render();
    }
  };
  backBtn.onclick = () => {
    if (idx > 0) {
      const shouldCheckpoint = curScreen.serverCheckpoint;
      recordScreenTime(); captureCurrentDraft(); clearTimeout(autosaveTimer);
      idx--; R.progress.currentScreenKey = SCREEN_KEYS[idx];
      if (shouldCheckpoint) save(); else persistLocal();
      render();
    }
  };
  if (skipBtn) skipBtn.onclick = () => {
    const shouldCheckpoint = curScreen.serverCheckpoint;
    recordScreenTime(); captureCurrentDraft(); clearTimeout(autosaveTimer);
    R.meta.supervisorSkippedScreens.push(curScreen.key);
    if (idx < SCREENS.length - 1) {
      idx++; R.progress.currentScreenKey = SCREEN_KEYS[idx];
      if (idx === SCREENS.length - 1 || !shouldCheckpoint) persistLocal(); else save();
      render();
    }
  };
  app.addEventListener("input", autosaveDraft);
  app.addEventListener("change", autosaveDraft);
  window.addEventListener("beforeunload", () => {
    closeHoverRecord(); recordScreenTime(); captureCurrentDraft(); persistLocal();
  });
  function showErr(msg) {
    let e = $(".err-line", app);
    if (!e) { e = document.createElement("div"); e.className = "err-line"; (app.querySelector(".card:last-child") || app.firstElementChild).appendChild(e); }
    e.textContent = msg; e.classList.add("show"); e.scrollIntoView({ block: "center", behavior: "smooth" });
  }

  function el(html) { const d = document.createElement("div"); d.innerHTML = html.trim(); return d.firstElementChild; }
  function likert(name, captions, val) {
    const wrap = document.createElement("div"); wrap.className = "likert";
    for (let i = 1; i <= 5; i++) {
      const cap = captions[i - 1] || "";
      const id = `${name}_${i}`;
      wrap.appendChild(el(`<div class="opt"><input type="radio" name="${name}" id="${id}" value="${i}" ${val == i ? "checked" : ""}/><label for="${id}"><span class="num">${i}</span><span class="cap">${esc(cap)}</span></label></div>`));
    }
    return wrap;
  }
  function getRadio(name, root = app) { const c = $(`input[name="${name}"]:checked`, root); return c ? c.value : null; }
  function radioGroup(container, name, opts, val) {
    container.innerHTML = "";
    opts.forEach((o) => {
      const value = typeof o === "string" ? o : o.value;
      const label = typeof o === "string" ? o : o.label;
      const c = el(`<label class="choice"><input type="radio" name="${name}" value="${esc(value)}" ${val === value ? "checked" : ""}/><span>${esc(label)}</span></label>`);
      const sync = () => $$(`input[name="${name}"]`, container).forEach((x) => x.closest(".choice").classList.toggle("sel", x.checked));
      c.querySelector("input").onchange = sync; if (val === value) c.classList.add("sel");
      container.appendChild(c);
    });
  }
  function checkboxGroup(container, name, opts, selected = []) {
    container.innerHTML = "";
    opts.forEach((o) => {
      const value = typeof o === "string" ? o : o.value;
      const label = typeof o === "string" ? o : o.label;
      const checked = selected.includes(value);
      const c = el(`<label class="choice ${checked ? "sel" : ""}"><input type="checkbox" name="${name}" value="${esc(value)}" ${checked ? "checked" : ""}/><span>${esc(label)}</span></label>`);
      c.querySelector("input").onchange = (e) => c.classList.toggle("sel", e.target.checked);
      container.appendChild(c);
    });
  }
  function getChecks(name, root = app) { return $$(`input[name="${name}"]:checked`, root).map((x) => x.value); }
  function screen(node, opts = {}) { return Object.assign({ node, serverCheckpoint: false }, opts); }

  function scrWelcome() {
    const languagePicker = LANG_LOCKED ? "" : `<div class="language-picker">
        <div><span class="language-title">${esc(tr("languageTitle"))}</span><span class="language-help">${esc(tr("languageHelp"))}</span></div>
        <div class="language-options">
          ${Object.entries(I18N.languages).map(([code, language]) => `<button type="button" class="language-option ${LANG === code ? "active" : ""}" data-language="${code}" aria-pressed="${LANG === code}"><img class="language-flag" src="${esc(language.flag)}" alt=""/><span>${esc(language.label)}${language.translated ? '<sup>*</sup>' : ""}</span>${language.recommended ? `<span class="language-badge">${esc(tr("languageRecommended"))}</span>` : ""}</button>`).join("")}
        </div>
        <p class="translation-note">${esc(tr("translationNote"))}</p>
      </div>`;
    const node = el(`<div class="screen"><div class="card">
      <div class="logos">
        <img src="images/tuberlin.png" alt="TU Berlin"/>
        <img src="images/QULAB.png" alt="Quality & Usability Lab"/>
        <img src="images/charite.png" alt="Charité Universitätsmedizin Berlin"/>
      </div>
      ${languagePicker}
      <span class="eyebrow">${tr("welcomeEyebrow")}</span>
      <h2 class="title">${tr("welcomeTitle")}</h2>
      <p class="lead" style="margin-top:12px">${esc(tr("welcomePerspective"))}</p>
      <div class="warn-note">
        <svg class="warn-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M10.29 3.86 1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>
        <div>${tr("welcomeSitting")}</div>
      </div>
    </div></div>`);
    $$(".language-option", node).forEach((button) => button.onclick = () => {
      const nextLanguage = button.dataset.language;
      if (!I18N.languages[nextLanguage] || nextLanguage === LANG) return;
      LANG = nextLanguage;
      R.meta.language = LANG;
      persistLocal();
      render();
    });
    return screen(node, { key: "welcome" });
  }

  function scrConsent() {
    const node = el(`<div class="screen"><div class="card">
      <span class="eyebrow">${esc(tr("consentEyebrow"))}</span>
      <h2 class="title">${esc(tr("consentTitle"))}</h2>
      <p class="lead">${esc(tr("consentLead"))}</p>
      <div class="note-box">${tr("consentContact")}</div>
      <label class="choice" id="consentChoice" style="margin-top:18px">
        <input type="checkbox" id="consent"/>
        <span>${esc(tr("consentChoice"))}</span>
      </label>
    </div></div>`);
    const cb = $("#consent", node), ch = $("#consentChoice", node);
    cb.onchange = () => ch.classList.toggle("sel", cb.checked);
    return screen(node, { key: "consent",
      onShow() { if (R.consent) { cb.checked = true; ch.classList.add("sel"); } },
      validate() { return cb.checked ? true : tr("consentError"); },
      collect() { R.consent = cb.checked; },
      serverCheckpoint: true,
    });
  }

  function scrBackground() {
    const node = el(`<div class="screen"><div class="card">
      <span class="eyebrow">${esc(tr("backgroundEyebrow"))}</span>
      <h2 class="title">${esc(tr("backgroundTitle"))}</h2>
      <div class="field"><label class="fl">${esc(tr("b1Label"))}</label><div class="choices row" id="B1"></div><input class="txt inline-txt" id="B1other" placeholder="${esc(tr("b1OtherPlaceholder"))}" style="display:none"/></div>
      <div class="field"><label class="fl">${tr("b2Label")}</label><input class="txt" id="B2" placeholder="${esc(tr("b2Placeholder"))}"/></div>
      <div class="field"><label class="fl">${esc(tr("b3Label"))}</label><div class="choices row" id="B3"></div></div>
      <div class="field"><label class="fl">${esc(tr("b4Label"))}</label><div class="choices row" id="B4"></div></div>
      <div class="field"><label class="fl">${esc(tr("b5Label", { language: tr("questionnaireLanguage") }))}</label><div id="B5"></div></div>
      <div class="field"><label class="fl">${esc(tr("b6Label"))}</label><div id="B6"></div></div>
      <div class="field"><label class="fl">${esc(tr("b7Label"))}</label><div id="B7"></div></div>
      <div class="field"><label class="fl">${esc(tr("b8Label"))}</label><div class="choices" id="B8"></div></div>
      <div class="field"><label class="fl">${tr("b9Label")}</label><div class="choices row" id="B9"></div><input class="txt inline-txt" id="B9other" placeholder="${esc(tr("b9OtherPlaceholder"))}" style="display:none"/></div>
      <div class="field"><label class="fl">${tr("b10Label")}</label><div class="choices row" id="B10"></div></div>
    </div></div>`);
    const b = R.background;
    const roleValues = ["Physician", "Nurse", "Dentist", "Physiotherapist", "Pharmacist", "Midwife", "Healthcare worker", "Other"];
    radioGroup($("#B1", node), "B1", optionPairs(roleValues, tr("b1Options")), b.B1);
    radioGroup($("#B3", node), "B3", optionPairs(["<1", "1-3", "4-7", "8-15", ">15"], tr("b3Options")), b.B3);
    radioGroup($("#B4", node), "B4", optionPairs(["German", "English", "Albanian", "Other"], tr("b4Options")), b.B4);
    $("#B5", node).appendChild(likert("B5", tr("b5Scale"), b.B5));
    $("#B6", node).appendChild(likert("B6", tr("b6Scale"), b.B6));
    $("#B7", node).appendChild(likert("B7", tr("b7Scale"), b.B7));
    radioGroup($("#B8", node), "B8", optionPairs(["Never", "Once or twice", "Occasionally", "Regularly"], tr("b8Options")), b.B8);
    radioGroup($("#B9", node), "B9", optionPairs(["Woman", "Man", "Non-binary", "Other"], tr("b9Options")), b.B9);
    radioGroup($("#B10", node), "B10", optionPairs(["18-24", "25-34", "35-44", "45-54", "55-64", "65+"], tr("b10Options")), b.B10);
    const b1other = $("#B1other", node);
    const b9other = $("#B9other", node);
    const syncOtherRole = () => { b1other.style.display = getRadio("B1", node) === "Other" ? "block" : "none"; };
    const syncOtherGender = () => { b9other.style.display = getRadio("B9", node) === "Other" ? "block" : "none"; };
    $$('input[name="B1"]', node).forEach((input) => input.addEventListener("change", syncOtherRole));
    $$('input[name="B9"]', node).forEach((input) => input.addEventListener("change", syncOtherGender));
    if (b.B1other) b1other.value = b.B1other;
    if (b.B9other) b9other.value = b.B9other;
    if (b.B2) $("#B2", node).value = b.B2;
    return screen(node, { key: "background",
      onShow() { syncOtherRole(); syncOtherGender(); },
      validate() {
        for (const k of ["B1", "B3", "B4", "B5", "B6", "B7", "B8"]) if (!getRadio(k, node)) return tr("backgroundError");
        if (getRadio("B1", node) === "Other" && !b1other.value.trim()) return tr("backgroundOtherError");
        return true;
      },
      collect() {
        R.background = { B1: getRadio("B1", node), B1other: getRadio("B1", node) === "Other" ? b1other.value.trim() : "", B2: $("#B2", node).value.trim(), B3: getRadio("B3", node), B4: getRadio("B4", node), B5: getRadio("B5", node), B6: getRadio("B6", node), B7: getRadio("B7", node), B8: getRadio("B8", node), B9: getRadio("B9", node), B9other: getRadio("B9", node) === "Other" ? b9other.value.trim() : "", B10: getRadio("B10", node) };
      },
      serverCheckpoint: true,
    });
  }

  function scrNumbers() {
    const node = el(`<div class="screen"><div class="card">
      <span class="eyebrow">${esc(tr("numbersEyebrow"))}</span>
      <h2 class="title">${esc(tr("numbersTitle"))}</h2>
      <p class="lead">${esc(tr("numbersIntro"))}</p>
      <div class="info-list">
        <p>${tr("zipfText")}</p>
        <p>${tr("aoaText")}</p>
      </div>
      <div class="key-note"><b>${esc(tr("notListedTitle"))}</b>${esc(tr("notListedBody"))}</div>
      <p class="lead" style="margin-top:16px">${tr("numbersLimit")}</p>
      ${LANG === "en" ? "" : `<p class="fine-note">${esc(tr("translatedMetricNote"))}</p>`}
      <label class="choice tutorial-ready" id="numbersAckChoice"><input type="checkbox" id="numbersAck"/><span>${tr("numbersAck")}</span></label>
    </div></div>`);
    const ack = $("#numbersAck", node), ackChoice = $("#numbersAckChoice", node);
    ack.onchange = () => ackChoice.classList.toggle("sel", ack.checked);
    return screen(node, {
      key: "numbers",
      onShow() {
        ack.checked = R.progress.numbersAck;
        ackChoice.classList.toggle("sel", ack.checked);
      },
      validate() { return ack.checked ? true : tr("numbersAckError"); },
      collect() { R.progress.numbersAck = ack.checked; },
    });
  }

  function scrStudyIntro() {
    const node = el(`<div class="screen"><div class="card study-overview">
      <span class="eyebrow">${esc(tr("introEyebrow"))}</span>
      <h2 class="title">${esc(tr("introTitle"))}</h2>
      <p class="lead">${esc(tr("introLead"))}</p>
      <div class="info-list">
        <p>${tr("introHow")}</p>
        <p>${tr("introSources")}</p>
        <p>${tr("introVersions")}</p>
      </div>
      <p class="lead" style="margin-top:16px">${esc(tr("introAim"))}</p>
      <div class="key-note"><b>${esc(tr("introPatientTitle"))}</b>${esc(tr("introPatientBody"))}</div>
    </div></div>`);
    return screen(node, { key: "studyIntro" });
  }

  function scrStudyOverview() {
    const node = el(`<div class="screen"><div class="card study-overview">
      <span class="eyebrow">${esc(tr("overviewEyebrow"))}</span>
      <h2 class="title">${esc(tr("overviewTitle"))}</h2>
      <p class="lead">${esc(tr("overviewLead"))}</p>
      <div class="same-output">${tr("overviewSameOutput")}</div>
      <div class="mock-notice overview-notice">
        <b>${esc(tr("mockTitle"))}</b>
        ${esc(tr("mockBody"))}
      </div>
    </div></div>`);
    return screen(node, { key: "studyOverview" });
  }

  function tutorialVersionCard(it, ver) {
    const descriptions = tr("tutorialDescriptions");
    return `<article class="tutorial-version tutorial-${ver.toLowerCase()}">
      <div class="block-label"><span class="chip chip-ver chip-${ver.toLowerCase()}">${esc(tr("versionWord"))} ${ver}</span>${esc(tr("versionLabels")[ver])}</div>
      <div class="sentence">${highlightPf(it, ver)}</div>
      <p>${esc(descriptions[ver])}</p>
    </article>`;
  }

  function gateTutorial(node, ver) {
    const target = $(".hl-repl[data-pop]", node);
    const status = $(".tutorial-status", node);
    nextBtn.disabled = true;
    const showUnlocked = () => {
      nextBtn.disabled = false;
      status.classList.add("done");
      status.innerHTML = `<b>&#10003; ${esc(tr("tutorialChecked", { version: ver }))}</b>`;
    };
    const unlock = () => {
      if (!R.progress.tutorialOpened[ver]) {
        R.progress.tutorialOpened[ver] = true;
        autosaveDraft();
      }
      showUnlocked();
    };
    if (R.progress.tutorialOpened[ver]) showUnlocked();
    target.addEventListener("mouseenter", unlock, { once: true });
    target.addEventListener("focus", unlock, { once: true });
    target.addEventListener("click", unlock, { once: true });
  }

  function scrTutorialA() {
    const it = localizedPractice();
    const node = el(`<div class="screen"><div class="card">
      <span class="eyebrow">${esc(tr("tutorialAeyebrow"))}</span>
      <h2 class="title">${esc(tr("tutorialAtitle"))}</h2>
      <div class="tutorial-stop"><span>${esc(tr("tutorialAstop"))}</span><div>${tr("tutorialAbody")}</div></div>
      ${origBlock(it)}
      ${versionBlock(it, "A")}
      <div class="legend">
        <span class="k"><span class="swatch sw-blue"></span> ${esc(tr("legendOriginal"))}</span>
        <span class="k"><span class="swatch sw-teal"></span> ${esc(tr("legendReplacement"))}</span>
      </div>
    </div></div>`);
    return screen(node, { key: "tutorialA", nextLabel: tr("navNext") });
  }

  function scrTutorialB() {
    const it = localizedPractice();
    const node = el(`<div class="screen"><div class="card tutorial-focus">
      <span class="eyebrow">${esc(tr("tutorialBeyebrow"))}</span>
      <h2 class="title">${esc(tr("tutorialBtitle"))}</h2>
      <div class="tutorial-stop"><span>${esc(tr("tutorialBstop"))}</span><div>${tr("tutorialBbody")}</div></div>
      <div class="tutorial-spotlight">${versionBlock(it, "B")}</div>
      <div class="tutorial-status">${esc(tr("tutorialBwaiting"))}</div>
    </div></div>`);
    return screen(node, { key: "tutorialB", nextLabel: tr("navNext"), onShow() { gateTutorial(node, "B"); } });
  }

  function scrTutorialC() {
    const it = localizedPractice();
    const node = el(`<div class="screen"><div class="card tutorial-focus">
      <span class="eyebrow">${esc(tr("tutorialCeyebrow"))}</span>
      <h2 class="title">${esc(tr("tutorialCtitle"))}</h2>
      <div class="tutorial-stop"><span>${esc(tr("tutorialCstop"))}</span><div>${tr("tutorialCbody")}</div></div>
      <div class="tutorial-spotlight">${versionBlock(it, "C")}</div>
      <div class="tutorial-status">${esc(tr("tutorialCwaiting"))}</div>
    </div></div>`);
    return screen(node, { key: "tutorialC", nextLabel: tr("navNext"), onShow() { gateTutorial(node, "C"); } });
  }

  function scrTutorialCompare() {
    const it = localizedPractice();
    const node = el(`<div class="screen"><div class="card">
      <span class="eyebrow">${esc(tr("tutorialCompareEyebrow"))}</span>
      <h2 class="title">${esc(tr("tutorialCompareTitle"))}</h2>
      <div class="same-output">${tr("tutorialSameOutput")}</div>
      ${origBlock(it)}
      <div class="tutorial-grid">
        ${tutorialVersionCard(it, "A")}
        ${tutorialVersionCard(it, "B")}
        ${tutorialVersionCard(it, "C")}
      </div>
      <div class="tutorial-summary">
        <div><span class="chip chip-ver chip-a">A</span>${tr("tutorialSummaryA")}</div>
        <div><span class="chip chip-ver chip-b">B</span>${tr("tutorialSummaryB")}</div>
        <div><span class="chip chip-ver chip-c">C</span>${tr("tutorialSummaryC")}</div>
      </div>
      <label class="choice tutorial-ready" id="readyChoice"><input type="checkbox" id="tutorialReady"/><span>${esc(tr("tutorialReady"))}</span></label>
    </div></div>`);
    const ready = $("#tutorialReady", node), choice = $("#readyChoice", node);
    ready.onchange = () => choice.classList.toggle("sel", ready.checked);
    return screen(node, {
      key: "tutorialCompare", nextLabel: tr("navStartItems"),
      onShow() {
        ready.checked = R.progress.tutorialReady;
        choice.classList.toggle("sel", ready.checked);
      },
      validate() { return ready.checked ? true : tr("tutorialReadyError"); },
      collect() { R.progress.tutorialReady = ready.checked; },
    });
  }

  function scrItem(it) {
    const id = it.id, qs = R.items[id].q;
    const node = el(`<div class="screen">
      <div class="card">
        <span class="eyebrow">${esc(tr("itemOf", { id, total: ITEMS.length }))}</span>
        <h2 class="title" style="font-size:22px">${esc(tr("itemTitle"))}</h2>
        ${origBlock(it)}
        ${versionBlock(it, "A")}${versionBlock(it, "B")}${versionBlock(it, "C")}
        ${detailTable(it)}
      </div>
      <div class="card">
        <div class="section-h">${esc(tr("assessment"))}</div>
        <div class="q"><div class="q-label"><span class="q-num">Q${id}.1</span>${esc(tr("q1"))}</div><div id="q1"></div></div>
        <div class="q"><div class="q-label"><span class="q-num">Q${id}.2</span>${esc(tr("q2"))}</div><div class="choices row" id="q2"></div></div>
        <div class="q conditional-q" id="q3wrap"><div class="q-label"><span class="q-num">Q${id}.3</span>${esc(tr("q3"))}</div>
          <div class="choices" id="q3"></div>
          <input class="txt inline-txt" id="q3other" placeholder="${esc(tr("q3Placeholder"))}" style="display:none"/></div>
        <div class="q"><div class="q-label"><span class="q-num">Q${id}.4</span>${esc(tr("q4"))}</div><div id="q4"></div></div>
        <div class="q"><div class="q-label"><span class="q-num">Q${id}.5</span>${termHelpLabel("q5", "source")}</div><div id="q5"></div></div>
        <div class="q"><div class="q-label"><span class="q-num">Q${id}.6</span>${termHelpLabel("q6", "explanation")}</div><div id="q6"></div></div>
        <div class="q"><div class="q-label"><span class="q-num">Q${id}.7</span>${esc(tr("q7"))} <span class="q-sub">(${esc(tr("optional"))})</span></div><textarea class="txt" id="q7" rows="2"></textarea></div>
      </div>
    </div>`);
    $("#q1", node).appendChild(likert(`i${id}q1`, tr("meaningScale"), qs.q1));
    radioGroup($("#q2", node), `i${id}q2`, optionPairs(["Yes", "No"], tr("yesNo")), qs.q2);
    radioGroup($("#q3", node), `i${id}q3`, optionPairs(["Clinically incorrect", "Misleading", "Important information is missing", "Too difficult for patients", "Style only", "Other"], tr("reasonOptions")), qs.q3);
    $("#q4", node).appendChild(likert(`i${id}q4`, tr("confidenceScale"), qs.q4));
    $("#q5", node).appendChild(likert(`i${id}q5`, tr("helpfulScale"), qs.q5));
    $("#q6", node).appendChild(likert(`i${id}q6`, tr("helpfulScale"), qs.q6));
    const q3wrap = $("#q3wrap", node), q3other = $("#q3other", node);
    const syncReason = () => { q3other.style.display = getRadio(`i${id}q3`, node) === "Other" ? "block" : "none"; };
    const syncApproval = () => { q3wrap.style.display = getRadio(`i${id}q2`, node) === "No" ? "block" : "none"; syncReason(); };
    $$(`input[name="i${id}q2"]`, node).forEach((x) => x.addEventListener("change", syncApproval));
    $$(`input[name="i${id}q3"]`, node).forEach((x) => x.addEventListener("change", syncReason));
    if (qs.q3other) q3other.value = qs.q3other;
    if (qs.q7) $("#q7", node).value = qs.q7;

    const tt = R.items[id].qTimesMs;
    const mark = (name) => { if (tt[name] == null) tt[name] = Math.round(performance.now() - SCREEN_ENTER); };
    [["q1"], ["q2"], ["q3"], ["q4"], ["q5"], ["q6"]].forEach(([n]) =>
      $$(`input[name="i${id}${n}"]`, node).forEach((x) => x.addEventListener("change", () => mark(n))));
    q3other.addEventListener("input", () => mark("q3other"));
    $("#q7", node).addEventListener("input", () => mark("q7"));

    return screen(node, { key: `item${id}`,
      onShow() { syncApproval(); },
      validate() {
        if (!getRadio(`i${id}q1`, node)) return tr("itemErrorQ1");
        const approval = getRadio(`i${id}q2`, node);
        if (!approval) return tr("itemErrorQ2");
        const reason = getRadio(`i${id}q3`, node);
        if (approval === "No" && !reason) return tr("itemErrorQ3");
        if (approval === "No" && reason === "Other" && !q3other.value.trim()) return tr("itemErrorQ3Other");
        if (!getRadio(`i${id}q4`, node)) return tr("itemErrorQ4");
        if (!getRadio(`i${id}q5`, node)) return tr("itemErrorQ5");
        if (!getRadio(`i${id}q6`, node)) return tr("itemErrorQ6");
        return true;
      },
      collect() {
        R.items[id].q = { q1: getRadio(`i${id}q1`, node),
          q2: getRadio(`i${id}q2`, node),
          q3: getRadio(`i${id}q2`, node) === "No" ? getRadio(`i${id}q3`, node) : null,
          q3other: getRadio(`i${id}q2`, node) === "No" ? q3other.value.trim() : "",
          q4: getRadio(`i${id}q4`, node), q5: getRadio(`i${id}q5`, node),
          q6: getRadio(`i${id}q6`, node), q7: $("#q7", node).value.trim() };
      },
      serverCheckpoint: true,
    });
  }

  function scrRationale() {
    const d = localizedRationales();
    const node = el(`<div class="screen rationale-screen">
      <div class="card rationale-intro">
        <span class="eyebrow">${esc(tr("rationaleEyebrow"))}</span>
        <h2 class="title">${esc(tr("rationaleTitle"))}</h2>
        <div class="rationale-task"><span>${esc(tr("rationaleTaskLabel"))}</span><p>${esc(tr("rationaleTask"))}</p></div>
        <div class="rationale-context">
          <div class="context-label">${esc(tr("rationaleSameExample"))}</div>
          <div class="context-swap"><span>${esc(d.from)}</span><b>&rarr;</b><strong>${esc(d.to)}</strong></div>
          <div class="context-source"><b>${esc(tr("sourcePassage"))}</b><span>"${esc(d.source)}"</span></div>
        </div>
      </div>
      <section class="card explanation-option explanation-short">
        <div class="explanation-head"><span class="explanation-code">S</span><div><span>${esc(tr("explanationS"))}</span><h3>${esc(tr("shortExplanation"))}</h3><p>${esc(tr("shortDescription"))}</p></div></div>
        <div class="explanation-copy"><span>${esc(tr("explanationText"))}</span><p>${esc(d.S)}</p></div>
        <div class="explanation-rating"><div class="q-label"><span class="q-num">R1.S</span>${esc(tr("rationaleRating"))}</div><div id="rS"></div></div>
      </section>
      <section class="card explanation-option explanation-medium">
        <div class="explanation-head"><span class="explanation-code">M</span><div><span>${esc(tr("explanationM"))}</span><h3>${esc(tr("mediumExplanation"))}</h3><p>${esc(tr("mediumDescription"))}</p></div></div>
        <div class="explanation-copy"><span>${esc(tr("explanationText"))}</span><p>${esc(d.M)}</p></div>
        <div class="explanation-rating"><div class="q-label"><span class="q-num">R1.M</span>${esc(tr("rationaleRating"))}</div><div id="rM"></div></div>
      </section>
      <section class="card explanation-option explanation-detailed">
        <div class="explanation-head"><span class="explanation-code">L</span><div><span>${esc(tr("explanationL"))}</span><h3>${esc(tr("detailedExplanation"))}</h3><p>${esc(tr("detailedDescription"))}</p></div></div>
        <div class="explanation-copy"><span>${esc(tr("explanationText"))}</span><p>${esc(d.L)}</p></div>
        <div class="explanation-rating"><div class="q-label"><span class="q-num">R1.L</span>${esc(tr("rationaleRating"))}</div><div id="rL"></div></div>
      </section>
      <div class="card">
        <div class="q"><div class="q-label"><span class="q-num">R2</span>${esc(tr("rationaleR2"))}</div><div class="choices row" id="r2"></div></div>
        <div class="q"><div class="q-label"><span class="q-num">R3</span>${esc(tr("rationaleR3"))} <span class="q-sub">(${esc(tr("optional"))})</span></div><textarea class="txt" id="r3" rows="2"></textarea></div>
      </div>
    </div>`);
    const rr = R.rationale;
    ["S", "M", "L"].forEach((length) => {
      $("#r" + length, node).appendChild(likert("r" + length, tr("usefulnessScale"), rr[length]));
    });
    radioGroup($("#r2", node), "r2", optionPairs(["Short", "Medium", "Detailed", "No explanation by default"], tr("rationaleR2Options")), rr.R2);
    if (rr.R3) $("#r3", node).value = rr.R3;
    return screen(node, { key: "rationale",
      validate() {
        for (const length of ["S", "M", "L"]) {
          if (!getRadio("r" + length, node)) return tr("rationaleErrorRating", { version: length });
        }
        if (!getRadio("r2", node)) return tr("rationaleErrorR2");
        return true;
      },
      collect() {
        R.rationale = {
          S: getRadio("rS", node), M: getRadio("rM", node), L: getRadio("rL", node),
          R2: getRadio("r2", node), R3: $("#r3", node).value.trim(),
        };
      },
      serverCheckpoint: true,
    });
  }

  function scrOverall() {
    const node = el(`<div class="screen"><div class="card">
      <span class="eyebrow">${esc(tr("overallEyebrow"))}</span>
      <h2 class="title">${esc(tr("overallTitle"))}</h2>
      <div class="q"><div class="q-label"><span class="q-num">O1</span>${esc(tr("o1"))}</div><div class="choices" id="o1"></div></div>
      <div class="q"><div class="q-label"><span class="q-num">O2</span>${esc(tr("o2"))}</div><div id="o2"></div></div>
      <div class="q"><div class="q-label"><span class="q-num">O3</span>${termHelpLabel("o3", "source")}</div><div id="o3"></div></div>
      <div class="q"><div class="q-label"><span class="q-num">O4</span>${termHelpLabel("o4", "explanation")}</div><div id="o4"></div></div>
      <div class="q"><div class="q-label"><span class="q-num">O5</span>${esc(tr("o5"))}</div><div id="o5"></div></div>
      <div class="q"><div class="q-label"><span class="q-num">O6</span>${esc(tr("o6"))} <span class="q-sub">(${esc(tr("selectAtLeastOne"))})</span></div><div class="choices" id="o6"></div><input class="txt inline-txt" id="o6other" placeholder="${esc(tr("o6Placeholder"))}" style="display:none"/></div>
      <div class="q"><div class="q-label"><span class="q-num">O7</span>${esc(tr("o7"))} <span class="q-sub">(${esc(tr("optional"))})</span></div><textarea class="txt" id="o7" rows="2"></textarea></div>
      <div class="q"><div class="q-label"><span class="q-num">O8</span>${esc(tr("o8"))} <span class="q-sub">(${esc(tr("optional"))})</span></div><textarea class="txt" id="o8" rows="2"></textarea></div>
    </div></div>`);
    const o = R.overall;
    radioGroup($("#o1", node), "o1", optionPairs(["Plain (A)", "With source passages (B)", "With source passages and explanations (C)"], tr("o1Options")), o.O1);
    const agreement = tr("agreementScale");
    $("#o2", node).appendChild(likert("o2", agreement, o.O2));
    $("#o3", node).appendChild(likert("o3", agreement, o.O3));
    $("#o4", node).appendChild(likert("o4", agreement, o.O4));
    $("#o5", node).appendChild(likert("o5", agreement, o.O5));
    checkboxGroup($("#o6", node), "o6", optionPairs(["Discharge letters", "Test results", "Patient handouts", "Consent forms", "Preparing for patient conversations", "Other"], tr("o6Options")), o.O6 || []);
    if (o.O6other) $("#o6other", node).value = o.O6other;
    if (o.O7) $("#o7", node).value = o.O7;
    if (o.O8) $("#o8", node).value = o.O8;

    const syncOther = () => { $("#o6other", node).style.display = getChecks("o6", node).includes("Other") ? "block" : "none"; };
    $$('input[name="o6"]', node).forEach((checkbox) => checkbox.addEventListener("change", syncOther));
    syncOther();
    return screen(node, { key: "overall",
      validate() {
        if (!getRadio("o1", node)) return tr("overallErrorO1");
        if (!getRadio("o2", node)) return tr("overallErrorO2");
        if (!getRadio("o3", node)) return tr("overallErrorO3");
        if (!getRadio("o4", node)) return tr("overallErrorO4");
        if (!getRadio("o5", node)) return tr("overallErrorO5");
        const settings = getChecks("o6", node);
        if (!settings.length) return tr("overallErrorO6");
        return true;
      },
      collect() {
        R.overall = { O1: getRadio("o1", node), O2: getRadio("o2", node), O3: getRadio("o3", node), O4: getRadio("o4", node),
          O5: getRadio("o5", node), O6: getChecks("o6", node), O6other: $("#o6other", node).value.trim(),
          O7: $("#o7", node).value.trim(), O8: $("#o8", node).value.trim() };
      },
      serverCheckpoint: true,
    });
  }

  function scrThanks() {
    if (!R.completedAt) R.completedAt = new Date().toISOString();
    R.meta.isFinal = true;
    R.timing.totalMs = Object.values(R.timing.perScreenMs).reduce((total, value) => total + value, 0);
    R.timing.elapsedWallMs = Date.now() - R.meta.startedMs;
    R.progress.currentScreenKey = "thanks";
    persistLocal();
    const node = el(`<div class="screen"><div class="card" style="text-align:center">
      <img src="images/logo_Survey.png" alt="" style="width:96px;height:96px;margin:0 auto 6px;display:block"/>
      <h2 class="title">${esc(tr("thanksTitle"))}</h2>
      <p class="lead" style="max-width:560px;margin:0 auto">${esc(tr("thanksLead"))}</p>
      <p class="muted" style="margin-top:16px">${esc(tr("thanksBody"))}</p>
      <p class="muted" style="margin-top:16px">${tr("thanksContact")}</p>
      <p class="muted" id="finalSaveStatus" style="margin-top:10px"></p>
      <button class="btn btn-primary" id="retryFinal" style="display:none;margin:12px auto 0">${esc(tr("retryFinal"))}</button>
      <button class="btn btn-ghost" id="dlFinal" style="margin-top:18px">${esc(tr("downloadResponses"))}</button>
    </div></div>`);
    return screen(node, { key: "thanks",
      onShow() {
        $("#dlFinal", node).onclick = downloadBackup;
        const status = $("#finalSaveStatus", node), retry = $("#retryFinal", node);
        const finish = () => {
          retry.style.display = "none";
          status.textContent = JATOS ? tr("finalSaving") : tr("finalSavedLocal");
          if (!JATOS) return;
          if (R.meta.finalResultSavedAt) {
            try { JATOS.showBeforeUnloadWarning(false); } catch (e) {}
            try { JATOS.endStudy(); } catch (e) {}
            return;
          }
          save((ok) => {
            if (!ok) {
              status.textContent = tr("finalSaveFailed");
              retry.style.display = "inline-flex";
              return;
            }
            R.meta.finalResultSavedAt = new Date().toISOString();
            persistLocal();
            status.textContent = tr("finalSaved");
            try { JATOS.showBeforeUnloadWarning(false); } catch (e) {}
            try { JATOS.endStudy(); } catch (e) {}
          });
        };
        retry.onclick = finish;
        finish();
        $("#stepsPill").textContent = tr("stepDone"); $("#progFill").style.width = "100%";
      },
    });
  }

  const POP = [];
  function origBlock(it) {
    return `<div class="block"><div class="block-label"><span class="chip chip-in">${esc(tr("originalChip"))}</span> ${esc(tr("clinicalNote"))}</div>
      <div class="sentence orig">${highlightOrig(it)}</div></div>`;
  }
  function versionBlock(it, ver) {
    const needsReminder = Number.isInteger(it.id) && ver !== "A";
    const versionHints = tr("versionHints");
    const hint = versionHints[ver] ? ` &middot; <span class="${needsReminder ? "hover-reminder" : "version-hint"}">${needsReminder ? '<span class="hover-alert" aria-hidden="true">!</span>' : ""}${esc(versionHints[ver])}</span>` : "";
    return `<div class="block ver-block"><div class="block-label"><span class="chip chip-ver chip-${ver.toLowerCase()}">${esc(tr("versionWord"))} ${ver}</span> ${esc(tr("versionLabels")[ver])}${hint}</div>
      <div class="sentence">${highlightPf(it, ver)}</div></div>`;
  }
  function highlightOrig(it) {
    let html = esc(it.orig);
    it.swaps.map((s) => s.orig).sort((a, b) => b.length - a.length)
      .forEach((o) => { html = replaceFirst(html, esc(o), `<span class="hl hl-orig">${esc(o)}</span>`); });
    return html;
  }
  function highlightPf(it, ver) {
    let html = esc(it.pf);
    const isItem = Number.isInteger(it.id);
    it.swaps.map((s, swapIndex) => ({ s, swapIndex }))
      .sort((a, b) => b.s.repl.length - a.s.repl.length)
      .forEach(({ s, swapIndex }) => {
        let span;
        if (ver === "A") { span = `<span class="hl hl-plain">${esc(s.repl)}</span>`; }
        else {
          const i = POP.push({ ...s, ver, swapIndex, itemId: isItem ? it.id : null }) - 1;
          const attention = isItem ? " attention-pop" : "";
          span = `<span class="hl hl-repl has-pop${attention}" data-pop="${i}" tabindex="0" role="button" aria-label="${esc(tr("openInfo", { term: s.repl }))}">${esc(s.repl)}</span>`;
        }
        html = replaceFirst(html, esc(s.repl), span);
      });
    return html;
  }
  function replaceFirst(h, n, r) { const i = h.indexOf(n); return i === -1 ? h : h.slice(0, i) + r + h.slice(i + n.length); }
  function termHelpLabel(labelKey, kind) {
    const html = esc(tr(labelKey));
    const termKey = kind === "source" ? "q5Term" : "q6Term";
    const needle = esc(tr(termKey));
    if (!needle) return html;
    const at = html.toLowerCase().indexOf(needle.toLowerCase());
    if (at === -1) return html;
    const shown = html.slice(at, at + needle.length);
    const span = `<span class="term-help" data-term="${kind}" tabindex="0" role="button" aria-label="${esc(tr("openInfo", { term: tr(termKey) }))}">${shown}</span>`;
    return html.slice(0, at) + span + html.slice(at + needle.length);
  }
  function detailTable(it) {
    const rows = it.swaps.map((s) => `<tr>
        <td class="o">${esc(s.orig)}</td><td class="r">${esc(s.repl)}</td>
        <td class="p">"${esc(s.passage)}"</td><td><span class="src-badge">${esc(s.source)}</span></td>
      </tr><tr><td></td><td colspan="3" class="pop-rationale" style="padding-top:0;color:var(--ink-soft)">${esc(s.expl)}</td></tr>`).join("");
    return `<div class="detail-wrap"><button class="detail-toggle" type="button"><span class="car">&#9654;</span> ${esc(tr("detailButton"))}</button>
      <div class="detail-body"><table class="detail-table"><thead><tr><th>${esc(tr("tableOriginal"))}</th><th>${esc(tr("tableReplacement"))}</th><th>${esc(tr("tablePassage"))}</th><th>${esc(tr("tableSource"))}</th></tr></thead><tbody>${rows}</tbody></table></div></div>`;
  }

  const popover = $("#popover");
  let hideTimer = null;
  let activePopEl = null;
  let openHover = null, openHoverAt = 0, hoverLeftAt = 0;
  popover.addEventListener("mouseenter", () => { clearTimeout(hideTimer); hoverLeftAt = 0; });
  popover.addEventListener("mouseleave", scheduleHide);
  document.addEventListener("click", (e) => { if (!popover.contains(e.target) && !e.target.closest(".hl-repl") && !e.target.closest(".term-help")) hidePop(); });
  function scheduleHide() { clearTimeout(hideTimer); hoverLeftAt = performance.now(); hideTimer = setTimeout(hidePop, 200); }
  function hoverKey(d) { return `${d.swapIndex}_${d.ver}`; }
  function hoverRecord(d) {
    if (!R || !d || d.itemId == null || !R.items[d.itemId]) return null;
    const store = R.items[d.itemId].hovers || (R.items[d.itemId].hovers = {});
    const key = hoverKey(d);
    const rec = store[key] || (store[key] = { opens: 0, firstOpenMs: null, firstDwellMs: null, totalDwellMs: 0, dwellsMs: [] });
    if (!Array.isArray(rec.dwellsMs)) rec.dwellsMs = [];
    return rec;
  }
  function closeHoverRecord() {
    if (!openHover) return false;
    const until = hoverLeftAt > openHoverAt ? hoverLeftAt : performance.now();
    const spent = Math.max(0, Math.round(until - openHoverAt));
    openHover.totalDwellMs += spent;
    if (openHover.firstDwellMs == null) openHover.firstDwellMs = spent;
    openHover.dwellsMs.push(spent);
    openHover = null;
    return true;
  }
  function hidePop() {
    const closed = closeHoverRecord();
    popover.classList.remove("show");
    $$(".hl-repl.active").forEach((e) => e.classList.remove("active"));
    activePopEl = null;
    if (closed) persistLocal();
  }
  function wirePopovers(root) {
    $$(".hl-repl[data-pop]", root).forEach((elm) => {
      elm.addEventListener("mouseenter", () => showPop(elm));
      elm.addEventListener("mouseleave", scheduleHide);
      elm.addEventListener("focus", () => showPop(elm));
      elm.addEventListener("blur", scheduleHide);
      elm.addEventListener("click", (e) => { e.stopPropagation(); showPop(elm); });
      elm.addEventListener("keydown", (e) => {
        if (e.key === "Enter" || e.key === " ") { e.preventDefault(); showPop(elm); }
      });
    });
    $$(".term-help[data-term]", root).forEach((elm) => {
      elm.addEventListener("mouseenter", () => showTermPop(elm));
      elm.addEventListener("mouseleave", scheduleHide);
      elm.addEventListener("focus", () => showTermPop(elm));
      elm.addEventListener("blur", scheduleHide);
      elm.addEventListener("click", (e) => { e.stopPropagation(); showTermPop(elm); });
      elm.addEventListener("keydown", (e) => {
        if (e.key === "Enter" || e.key === " ") { e.preventDefault(); showTermPop(elm); }
      });
    });
    applySeenCues(root);
  }
  function applySeenCues(root) {
    $$(".hl-repl[data-pop]", root).forEach((elm) => {
      const d = POP[+elm.dataset.pop];
      if (!d || d.itemId == null || !R.items[d.itemId]) return;
      const rec = (R.items[d.itemId].hovers || {})[hoverKey(d)];
      if (rec && rec.opens > 0) elm.classList.add("seen");
    });
  }
  function placePopover(elm) {
    const r = elm.getBoundingClientRect(), pw = popover.offsetWidth, ph = popover.offsetHeight;
    const left = Math.max(12, Math.min(r.left + r.width / 2 - pw / 2, innerWidth - pw - 12));
    const roomAbove = r.top - 12, roomBelow = innerHeight - r.bottom - 12;
    let top;
    if (ph <= roomAbove) top = r.top - ph - 10;
    else if (ph <= roomBelow) top = r.bottom + 10;
    else top = roomBelow >= roomAbove ? r.bottom + 10 : r.top - ph - 10;
    top = Math.min(top, innerHeight - ph - 12);
    top = Math.max(12, top);
    popover.style.left = left + "px"; popover.style.top = top + "px";
  }
  function showPop(elm) {
    clearTimeout(hideTimer);
    const d = POP[+elm.dataset.pop]; if (!d) return;
    if (activePopEl === elm && popover.classList.contains("show")) return;
    closeHoverRecord();
    popover.innerHTML = popHtml(d);
    popover.classList.add("show");
    $$(".hl-repl.active").forEach((e) => e.classList.remove("active")); elm.classList.add("active", "seen");
    activePopEl = elm;
    placePopover(elm);
    const rec = hoverRecord(d);
    if (rec) {
      rec.opens += 1;
      if (rec.firstOpenMs == null) rec.firstOpenMs = Math.max(0, Math.round(performance.now() - SCREEN_ENTER));
      openHover = rec; openHoverAt = performance.now(); hoverLeftAt = 0;
      persistLocal();
    }
  }
  function showTermPop(elm) {
    clearTimeout(hideTimer);
    if (activePopEl === elm && popover.classList.contains("show")) return;
    closeHoverRecord();
    popover.innerHTML = termPopHtml(elm.dataset.term);
    popover.classList.add("show");
    $$(".hl-repl.active").forEach((e) => e.classList.remove("active"));
    activePopEl = elm;
    placePopover(elm);
  }
  function termPopHtml(kind) {
    const d = localizedPractice().swaps[0];
    const isSource = kind === "source";
    const body = isSource
      ? `<div class="pop-section"><div class="ttl">${esc(tr("popSource"))} <span class="src-badge">${esc(d.source)}</span></div><div class="pop-passage">"${esc(d.passage)}"</div></div>`
      : `<div class="pop-section"><div class="ttl">${esc(tr("whyChange"))}</div><div class="pop-rationale">${esc(d.expl)}</div></div>`;
    return `<div class="pop-head term-help-head">
        <div class="term-help-title">${esc(tr(isSource ? "termHelpSource" : "termHelpExplanation"))}</div>
        <div class="pop-swap"><span class="from">${esc(d.orig)}</span><span class="arr">&rarr;</span><span class="to">${esc(d.repl)}</span></div>
      </div>
      <div class="pop-body">${body}</div>`;
  }
  function popHtml(d) {
    const oneDecimal = (value) => (Math.round((value + Number.EPSILON) * 10) / 10).toFixed(1);
    const metric = (label, from, to, higherIsBetter) => {
      if (!Number.isFinite(from) && !Number.isFinite(to)) return "";
      const hasFrom = Number.isFinite(from), hasTo = Number.isFinite(to);
      const fromText = hasFrom ? oneDecimal(from) : tr("notListed");
      const toText = hasTo ? oneDecimal(to) : tr("notListed");
      const target = higherIsBetter ? 4 : 11;
      const fromCls = hasFrom ? "" : "na";
      let toCls = "na";
      if (hasTo && hasFrom) toCls = (higherIsBetter ? to > from : to < from) ? "up" : "dn";
      else if (hasTo) {
        const shown = Number(oneDecimal(to));
        toCls = (higherIsBetter ? shown >= target : shown <= target) ? "up" : "";
      }
      return `<span class="feat">${label} <span class="${fromCls}">${fromText}</span><span class="sep">&rarr;</span><span class="${toCls}">${toText}</span></span>`;
    };
    const scoreRows = metric("Zipf", d.zo, d.zr, true) + metric("AoA", d.ao, d.ar, false);
    const englishTerms = LANG === "en" ? "" : `<div class="metric-terms">${esc(tr("metricEnglishTerms", { from: d.origEn, to: d.replEn }))}</div>`;
    const feats = d.ver === "C" && scoreRows ? `<div class="pop-section"><div class="ttl">${esc(tr("difficultyScores"))}</div><div class="pop-feats">${scoreRows}</div>
      ${englishTerms}<div class="metric-note">${esc(tr("metricMethod"))}</div></div>` : "";
    const expl = d.ver === "C" ? `<div class="pop-section"><div class="ttl">${esc(tr("whyChange"))}</div><div class="pop-rationale">${esc(d.expl)}</div></div>` : "";
    return `<div class="pop-head"><div class="pop-swap"><span class="from">${esc(d.orig)}</span><span class="arr">&rarr;</span><span class="to">${esc(d.repl)}</span></div></div>
      <div class="pop-body">
        <div class="pop-section"><div class="ttl">${esc(tr("popSource"))} <span class="src-badge">${esc(d.source)}</span></div><div class="pop-passage">"${esc(d.passage)}"</div></div>
        ${feats}${expl}
      </div>`;
  }
  function wireCollapse(root) { $$(".detail-toggle", root).forEach((t) => t.onclick = () => t.closest(".detail-wrap").classList.toggle("open")); }

  function boot() {
    const studyResultId = JATOS ? (JATOS.studyResultId || JATOS.studyResultUuid || null) : null;
    const componentResultId = JATOS ? (JATOS.componentResultId || null) : null;
    STORAGE_KEY = `${LS_KEY_PREFIX}:${studyResultId || "standalone"}`;
    R = restoreResult(studyResultId, componentResultId) || freshResult(studyResultId, componentResultId);
    R.meta.copyId = copyId();
    const forced = forcedLanguage();
    if (forced) { LANG_LOCKED = true; R.meta.language = forced; }
    R.meta.languageLocked = LANG_LOCKED;
    LANG = I18N.languages[R.meta.language] ? R.meta.language : "en";
    document.documentElement.lang = LANG;
    document.title = tr("pageTitle");
    buildFlow();
    const restoredIndex = SCREEN_KEYS.indexOf(R.completedAt ? "thanks" : R.progress.currentScreenKey);
    idx = restoredIndex >= 0 ? restoredIndex : 0;
    if (JATOS) { try { JATOS.showBeforeUnloadWarning(true); } catch (e) {} }
    render(); persistLocal();
    const note = $("#saveNote");
    if (note) {
      if (JATOS) note.textContent = tr("progressLocal");
      else {
        note.innerHTML = `${esc(tr("savedLocal"))} &middot; <a href="#" id="dl">${esc(tr("downloadBackup"))}</a>`;
        wireBackupLink();
      }
    }
  }
  if (JATOS) jatos.onLoad(boot); else boot();
})();
