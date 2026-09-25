"""Builds the Study I figures of the thesis from the saved run into figures/thesis."""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch
from matplotlib.ticker import FuncFormatter


ROOT = Path(__file__).resolve().parents[1]
RUN_DIR = ROOT / "runs" / "run100_20260815_222318"
OUTPUT_DIR = ROOT / "figures" / "thesis"

BLUE = "#2b6cb0"
LIGHT_BLUE = "#90cdf4"
TEAL = "#4fa3a5"
GREY = "#a0aec0"
GREEN = "#2f855a"
AMBER = "#d69e2e"
RED = "#c53030"
INK = "#2d3748"
GRID = "#e2e8f0"

MODEL_METADATA = [
    {"label": "Qwen3.5-9B", "total": 9.0, "active": None},
    {"label": "Ternary Bonsai 27B", "total": 27.32, "active": None},
    {"label": "Muse Glimmer 30B", "total": 29.6, "active": None},
    {"label": "Qwen3.7-Plus", "total": 397.0, "active": 17.0},
    {"label": "Nemotron 3 Ultra", "total": 550.0, "active": 55.0},
    {"label": "DeepSeek V4 Pro", "total": 1600.0, "active": 49.0},
]

RESULT_MODELS = [
    ("Muse Glimmer", "together-muse-glimmer"),
    ("Nemotron Ultra", "together-nemotron-ultra"),
    ("Qwen3.7-Plus", "qwen3p7-plus"),
    ("Qwen3.5-9B", "together-qwen3.5-9b"),
    ("DeepSeek V4 Pro", "together-deepseek-pro"),
    ("Ternary Bonsai", "together-ternary-bonsai-27b"),
]

plt.rcParams.update(
    {
        "figure.dpi": 200,
        "savefig.dpi": 200,
        "font.family": "DejaVu Sans",
        "font.size": 9,
        "axes.titlesize": 10,
        "axes.titleweight": "bold",
        "axes.labelcolor": INK,
        "axes.edgecolor": INK,
        "xtick.color": INK,
        "ytick.color": INK,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "legend.frameon": False,
        "figure.facecolor": "white",
        "axes.facecolor": "white",
    }
)


def load_results() -> dict[str, dict]:
    results: dict[str, dict] = {}
    for _, slug in RESULT_MODELS:
        path = RUN_DIR / slug / "evaluation.json"
        results[slug] = json.loads(path.read_text(encoding="utf-8"))
    return results


def load_grounded_judged_correctness() -> dict[str, float]:
    verdict_value = {"yes": 1.0, "partly": 0.5, "no": 0.0}
    means: dict[str, float] = {}
    for _, slug in RESULT_MODELS:
        path = RUN_DIR / slug / "replacement_judge.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        scores = [
            verdict_value[item["correct"]]
            for item in data["items"]
            if item["arm"] == "grounded" and not item["unparsed"]
        ]
        if not scores:
            raise ValueError(f"No grounded replacement-judge scores for {slug}")
        means[slug] = sum(scores) / len(scores)
    return means


def save_figure(figure: plt.Figure, name: str) -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    figure.tight_layout()
    for extension in ("png", "pdf"):
        figure.savefig(
            OUTPUT_DIR / f"{name}.{extension}",
            bbox_inches="tight",
            facecolor="white",
        )
    plt.close(figure)
    print(f"wrote {name}.png and {name}.pdf")


def figure_model_parameters() -> None:
    figure, axis = plt.subplots(figsize=(7.4, 3.8))
    positions = np.arange(len(MODEL_METADATA))

    for position, model in zip(positions, MODEL_METADATA):
        total = float(model["total"])
        axis.barh(
            position,
            total - 1,
            left=1,
            height=0.58,
            color=BLUE,
            zorder=2,
        )
        axis.text(
            total * 1.06,
            position,
            f"{total:g}B total",
            va="center",
            color=BLUE,
            fontsize=8,
            fontweight="bold",
        )

        active = model["active"]
        if active is not None:
            active = float(active)
            axis.barh(
                position,
                active - 1,
                left=1,
                height=0.30,
                color=LIGHT_BLUE,
                edgecolor="white",
                linewidth=0.5,
                zorder=3,
            )
            axis.text(
                np.sqrt(active),
                position,
                f"{active:g}B active",
                va="center",
                ha="center",
                color=INK,
                fontsize=7.5,
                fontweight="bold",
                zorder=4,
            )

    axis.set_xscale("log")
    axis.set_xlim(1, 2400)
    axis.set_xticks([1, 10, 100, 1000])
    axis.xaxis.set_major_formatter(FuncFormatter(lambda value, _: f"{value:g}"))
    axis.set_yticks(positions)
    axis.set_yticklabels([str(model["label"]) for model in MODEL_METADATA])
    axis.invert_yaxis()
    axis.grid(axis="x", color=GRID, linewidth=0.8, zorder=0)
    axis.set_xlabel("Parameters (billions, logarithmic scale)")
    axis.set_title("Published total and active parameter counts")
    axis.legend(
        handles=[
            Patch(color=BLUE, label="Total parameters"),
            Patch(color=LIGHT_BLUE, label="Active per token (MoE only)"),
        ],
        loc="upper right",
    )
    save_figure(figure, "fig_2_1_model_parameters")


def figure_human_edit_recall(results: dict[str, dict]) -> None:
    figure, axis = plt.subplots(figsize=(7.6, 3.6))
    positions = np.arange(len(RESULT_MODELS))
    width = 0.24
    arms = [
        ("naive", "Naive", GREY),
        ("termonly", "Termonly", BLUE),
        ("grounded", "Grounded", TEAL),
    ]

    for offset, (arm, label, color) in zip((-width, 0, width), arms):
        values = [
            results[slug]["aggregate"][arm]["human_edit_recall"]["mean"]
            for _, slug in RESULT_MODELS
        ]
        axis.bar(positions + offset, values, width, color=color, label=label)

    axis.set_xticks(positions)
    axis.set_xticklabels(
        [label.replace(" ", "\n", 1) for label, _ in RESULT_MODELS],
        fontsize=8,
    )
    axis.set_ylim(0, 1.05)
    axis.set_yticks(np.arange(0, 1.01, 0.2))
    axis.grid(axis="y", color=GRID, linewidth=0.8, zorder=0)
    axis.set_ylabel("Human-edit recall (0-1)")
    axis.set_title("Explicit term identification raises replacement coverage")
    axis.legend(loc="upper center", bbox_to_anchor=(0.5, -0.23), ncols=3)
    save_figure(figure, "fig_4_1_human_edit_recall")


def figure_replacement_coverage_quality(
    results: dict[str, dict], judged_correctness: dict[str, float]
) -> None:
    figure, axis = plt.subplots(figsize=(7.4, 3.8))
    positions = np.arange(len(RESULT_MODELS))
    coverage = np.array(
        [
            results[slug]["aggregate"]["grounded"]["human_edit_recall"]["mean"]
            * 100
            for _, slug in RESULT_MODELS
        ]
    )
    correctness = np.array(
        [judged_correctness[slug] * 100 for _, slug in RESULT_MODELS]
    )

    for position, correct, covered in zip(positions, correctness, coverage):
        axis.plot([correct, covered], [position, position], color=GRID, linewidth=4)
    axis.scatter(
        correctness,
        positions,
        s=55,
        color=AMBER,
        label="LLM-judged correctness",
        zorder=3,
    )
    axis.scatter(
        coverage,
        positions,
        s=55,
        color=BLUE,
        label="Human-edit recall",
        zorder=3,
    )

    for position, correct, covered in zip(positions, correctness, coverage):
        axis.text(correct - 1.2, position, f"{correct:.1f}%", ha="right", va="center", fontsize=8)
        axis.text(covered + 1.0, position, f"{covered:.1f}%", ha="left", va="center", fontsize=8)

    axis.set_xlim(0, 105)
    axis.set_xticks(np.arange(0, 101, 20))
    axis.set_yticks(positions)
    axis.set_yticklabels([label for label, _ in RESULT_MODELS])
    axis.invert_yaxis()
    axis.grid(axis="x", color=GRID, linewidth=0.8, zorder=0)
    axis.set_xlabel("Grounded-arm score (%)")
    axis.set_title("Replacement coverage exceeds judged correctness")
    axis.legend(loc="upper center", bbox_to_anchor=(0.5, -0.23), ncols=2)
    save_figure(figure, "fig_4_2_replacement_coverage_quality")


def figure_context_effects(results: dict[str, dict]) -> None:
    figure, axis = plt.subplots(figsize=(7.4, 3.8))
    positions = np.arange(len(RESULT_MODELS))
    helped = np.array(
        [results[slug]["attribution"]["helped_rate"] * 100 for _, slug in RESULT_MODELS]
    )
    hurt = -np.array(
        [results[slug]["attribution"]["hurt_rate"] * 100 for _, slug in RESULT_MODELS]
    )

    helped_bars = axis.barh(positions, helped, height=0.55, color=GREEN, label="Helped")
    hurt_bars = axis.barh(positions, hurt, height=0.55, color=RED, label="Hurt")

    for bar, value in zip(helped_bars, helped):
        axis.text(value + 1, bar.get_y() + bar.get_height() / 2, f"{value:.1f}%", va="center", fontsize=8)
    for bar, value in zip(hurt_bars, -hurt):
        if value >= 3:
            axis.text(
                -value / 2,
                bar.get_y() + bar.get_height() / 2,
                f"{value:.1f}%",
                va="center",
                ha="center",
                color="white",
                fontsize=8,
                fontweight="bold",
            )
        else:
            horizontal = -value - 0.8 if value > 0 else -0.8
            axis.text(
                horizontal,
                bar.get_y() + bar.get_height() / 2,
                f"{value:.1f}%",
                va="center",
                ha="right",
                fontsize=8,
            )

    axis.axvline(0, color=INK, linewidth=0.9)
    axis.set_xlim(-18, 60)
    axis.set_yticks(positions)
    axis.set_yticklabels([label for label, _ in RESULT_MODELS])
    axis.invert_yaxis()
    axis.grid(axis="x", color=GRID, linewidth=0.8, zorder=0)
    axis.set_xlabel("Share of measurable edits (hurt shown left)")
    axis.set_title("Retrieved context helped more edits than it hurt")
    axis.legend(loc="upper center", bbox_to_anchor=(0.5, -0.23), ncols=2)
    save_figure(figure, "fig_4_3_context_effects")


def main() -> None:
    results = load_results()
    judged_correctness = load_grounded_judged_correctness()
    figure_model_parameters()
    figure_human_edit_recall(results)
    figure_replacement_coverage_quality(results, judged_correctness)
    figure_context_effects(results)


if __name__ == "__main__":
    main()
