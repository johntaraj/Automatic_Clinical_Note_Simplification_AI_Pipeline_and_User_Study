"""Packages the study (study/) as JATOS-importable .jzip files in dist/.

Usage:
    python build_jzip.py            # one copy: dist/medplain_user_study_01.jzip
    python build_jzip.py 4          # copies 01..04, one study link each
    python build_jzip.py a b c      # one copy per label
"""

import json, os, re, shutil, sys, tempfile, uuid, zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "study")
OUTDIR = os.path.join(HERE, "dist")
ASSETS = ["index.html", "locales.js", "study.js", "style.css"]
IMAGES = ["tuberlin.png", "charite.png", "QULAB.png", "logo_Survey.png",
          "flag-en.png", "flag-de.png", "flag-sq.png"]

NAMESPACE = uuid.UUID("b0c1d6f2-8a34-4d7e-9f51-2c8a7e6b4d13")

BASE_TITLE = "MedPlain User Study - Patient-Friendly Medical Text"
DESCRIPTION = ("Healthcare-worker feedback on AI-generated patient-friendly text "
               "(highlight / +sources / +explanations).")


def det_uuid(*parts):
    return str(uuid.uuid5(NAMESPACE, ":".join(parts)))


def slug(label):
    cleaned = re.sub(r"[^a-z0-9]+", "_", label.strip().lower()).strip("_")
    if not cleaned:
        sys.exit(f"Label {label!r} has no usable characters for a directory name.")
    return cleaned


def build(label):
    dirname = f"medplain_user_study_{slug(label)}"
    jas = {
        "version": "3",
        "data": {
            "uuid": det_uuid(dirname, "study"),
            "title": f"{BASE_TITLE} [{label}]",
            "description": f"{DESCRIPTION} Distribution copy: {label}.",
            "groupStudy": False,
            "linearStudy": False,
            "allowPreview": False,
            "dirName": dirname,
            "comments": f"Distribution copy {label}. Identical to every other copy.",
            "jsonData": json.dumps({"copy": label}),
            "endRedirectUrl": "",
            "componentList": [{
                "uuid": det_uuid(dirname, "component"),
                "title": "Survey",
                "htmlFilePath": "index.html",
                "reloadable": True,
                "active": True,
                "comments": "",
                "jsonData": None,
            }],
            "batchList": [{
                "uuid": det_uuid(dirname, "batch"),
                "title": "Default",
                "active": True,
                "maxActiveMembers": None,
                "maxTotalMembers": None,
                "maxTotalWorkers": None,
                "allowedWorkerTypes": None,
                "comments": None,
                "jsonData": None,
            }],
        },
    }

    out = os.path.join(OUTDIR, f"{dirname}.jzip")
    with tempfile.TemporaryDirectory() as td:
        dstdir = os.path.join(td, dirname)
        os.makedirs(os.path.join(dstdir, "images"), exist_ok=True)
        for asset in ASSETS:
            shutil.copy(os.path.join(SRC, asset), os.path.join(dstdir, asset))
        locales_path = os.path.join(dstdir, "locales.js")
        with open(locales_path, "r", encoding="utf-8") as f:
            original = f.read()
        with open(locales_path, "w", encoding="utf-8") as f:
            f.write(f'window.MEDPLAIN_COPY_ID = {json.dumps(label)};\n{original}')
        for image in IMAGES:
            shutil.copy(os.path.join(SRC, "images", image),
                        os.path.join(dstdir, "images", image))

        jas_path = os.path.join(td, f"{dirname}.jas")
        with open(jas_path, "w", encoding="utf-8") as f:
            json.dump(jas, f, indent=2)

        with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
            z.write(jas_path, f"{dirname}.jas")
            for asset in ASSETS:
                z.write(os.path.join(dstdir, asset), f"{dirname}/{asset}")
            for image in IMAGES:
                z.write(os.path.join(dstdir, "images", image), f"{dirname}/images/{image}")

    print(f"  {dirname + '.jzip':<40} copy={label:<10} uuid={jas['data']['uuid']}")


args = sys.argv[1:]

if not args:
    labels = ["01"]
elif len(args) == 1 and args[0].isdigit():
    labels = [f"{i:02d}" for i in range(1, int(args[0]) + 1)]
else:
    labels = args

if len(set(slug(x) for x in labels)) != len(labels):
    sys.exit("Labels must be unique after slugging.")

os.makedirs(OUTDIR, exist_ok=True)
print(f"Building {len(labels)} copies into {OUTDIR}\n")
for label in labels:
    build(label)
print("\nImport each .jzip into JATOS as its own study (one study link per copy).")
