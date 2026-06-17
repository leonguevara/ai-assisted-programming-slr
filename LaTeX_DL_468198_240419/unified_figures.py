"""
Genera el set unificado de figuras para Results / Threats to Validity,
aplicando el design-system de paper_style.py.

Incluye:
 (A) Las distribuciones simples que León quería conservar como donut
     (dimensión, calidad global, item type) — re-hechas con la paleta Harbor.
 (B) Las comparaciones cruzadas (calidad x dimensión, dimensión x año,
     calidad x año) — mantenidas como heatmap / barra apilada, NO como
     donut, por las razones de legibilidad discutidas con León.
 (C) Co-ocurrencia de dimensiones — heatmap con diagonal corregida.

Descartadas definitivamente: Nivel_Soporte (19_) y Source (20_).
Descartada por redundancia: dimension_maturity_index (ya contenida en B).
"""

from pathlib import Path
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

from paper_style import (
    apply_style, note, title, text_color_for_bg,
    HARBOR, HARBOR_CMAP, SIGNAL_AMBER, SIGNAL_AMBER_LIGHT,
    QUALITY_COLORS, DIMENSION_PALETTE, INK,
)

apply_style()

INPUT_FILE = Path("/home/claude/datos_paper_tableau.xlsx")
SHEET_NAME = "Corpus"
OUT_DIR = Path("/home/claude/slr_outputs_unified/figures")
OUT_DIR.mkdir(parents=True, exist_ok=True)

DIMENSION_ORDER = [
    "Code Quality & Technical Debt",
    "Human–AI Interaction",
    "Productivity",
    "Perception & Trust",
    "Cognitive Load / Human Factors",
    "Organizational Impact",
    "Economic Impact",
]
QUALITY_ORDER = ["A1", "A2", "B"]
YEAR_ORDER = [2022, 2023, 2024, 2025, 2026]

DIM_BINARY_COLUMNS = {
    "DIM_PROD": "Productivity",
    "DIM_CQTD": "Code Quality & Technical Debt",
    "DIM_HAI": "Human–AI Interaction",
    "DIM_PT": "Perception & Trust",
    "DIM_ECON": "Economic Impact",
    "DIM_ORG": "Organizational Impact",
    "DIM_CLHF": "Cognitive Load / Human Factors",
}

df = pd.read_excel(INPUT_FILE, sheet_name=SHEET_NAME)
df["Publication Year"] = pd.to_numeric(df["Publication Year"], errors="coerce").astype("Int64")
for col in DIM_BINARY_COLUMNS:
    df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0).astype(int)


def donut(counts: pd.Series, order, palette, filename, fig_title, subtitle=None,
          min_pct_label=2.5, flag_category=None):
    """Donut chart following the Harbor palette, used ONLY for single-variable
    part-to-whole distributions (per discussion with León).

    flag_category: if set, that category's wedge is rendered in Signal Amber
    instead of its default Harbor shade, as an explicit, documented choice
    (not an accident of palette ordering) — used when that slice itself is
    the finding worth flagging (e.g. a critically under-evidenced dimension).
    """
    counts = counts.reindex(order).dropna()
    total = counts.sum()
    colors = list(palette[: len(counts)])
    if flag_category is not None and flag_category in counts.index:
        flag_pos = list(counts.index).index(flag_category)
        colors[flag_pos] = SIGNAL_AMBER

    fig, ax = plt.subplots(figsize=(8.6, 6.4))
    wedge_vals = counts.values
    pct_vals = wedge_vals / total * 100

    wedges, _, _ = ax.pie(
        wedge_vals,
        labels=None,
        autopct=lambda pct: f"{int(round(pct/100*total))}\n({pct:.1f}%)" if pct >= min_pct_label else "",
        startangle=90,
        counterclock=False,
        pctdistance=0.74,
        colors=colors,
        wedgeprops={"linewidth": 1.4, "edgecolor": "white"},
        textprops={"fontsize": 9.5, "color": INK},
    )
    # Fix label contrast on dark wedges (autopct text objects come back via ax.texts)
    autotexts = [t for t in ax.texts]
    for atext, color_hex in zip(autotexts, colors):
        atext.set_color(text_color_for_bg(color_hex))

    centre = plt.Circle((0, 0), 0.46, fc="white")
    ax.add_artist(centre)
    ax.text(0, 0, f"n = {int(total)}", ha="center", va="center", fontsize=13, fontweight="bold", color=INK)

    legend_labels = [f"{idx} — {int(v)} ({v/total*100:.1f}%)" for idx, v in counts.items()]
    ax.legend(
        wedges, legend_labels, loc="center left", bbox_to_anchor=(1.0, 0.5),
        frameon=False, fontsize=9.5,
    )
    title(ax, fig_title, subtitle)
    ax.axis("equal")
    plt.savefig(OUT_DIR / filename, bbox_inches="tight")
    plt.close()


# ---------------------------------------------------------------------
# (A1) Distribution by primary dimension — donut, Harbor palette
# ---------------------------------------------------------------------
dim_counts = df["Primary_Dimension_Normalized"].value_counts()
donut(
    dim_counts, DIMENSION_ORDER, DIMENSION_PALETTE,
    "A1_dimension_distribution.png",
    "Distribution of the corpus by primary analytical dimension",
    subtitle="Amber flags Economic Impact (n=1) — the most critically under-evidenced dimension",
    flag_category="Economic Impact",
)

# ---------------------------------------------------------------------
# (A2) Distribution by quality class — donut, sequential (no semaphore)
# ---------------------------------------------------------------------
qual_counts = df["Clasificación"].value_counts()
donut(
    qual_counts, QUALITY_ORDER, [QUALITY_COLORS[q] for q in QUALITY_ORDER],
    "A2_quality_distribution.png",
    "Distribution of the corpus by evidence-quality class",
)

# ---------------------------------------------------------------------
# (A3) Distribution by item type — donut, with preprint share flagged
# in amber (this is the figure meant for Threats to Validity)
# ---------------------------------------------------------------------
item_counts = df["Item Type"].value_counts()
donut(
    item_counts, item_counts.index.tolist(), HARBOR,
    "A3_item_type_distribution.png",
    "Distribution by item type",
    subtitle="Amber flags the preprint share — a relevant peer-review caveat (see Threats to Validity)",
    flag_category="preprint",
)

# ---------------------------------------------------------------------
# (B1) Quality composition within each dimension — heatmap, Harbor cmap
# ---------------------------------------------------------------------
tab = pd.crosstab(df["Primary_Dimension_Normalized"], df["Clasificación"])
tab = tab.reindex(index=DIMENSION_ORDER, columns=QUALITY_ORDER, fill_value=0)
rowpct = tab.div(tab.sum(axis=1), axis=0) * 100

fig, ax = plt.subplots(figsize=(8.6, 6.2))
im = ax.imshow(rowpct.values, cmap=HARBOR_CMAP, aspect="auto", vmin=0, vmax=100)
ax.set_xticks(range(len(QUALITY_ORDER)))
ax.set_xticklabels(QUALITY_ORDER)
ax.set_yticks(range(len(DIMENSION_ORDER)))
ax.set_yticklabels(DIMENSION_ORDER)
for i in range(len(DIMENSION_ORDER)):
    for j in range(len(QUALITY_ORDER)):
        val = rowpct.values[i, j]
        is_flag = (DIMENSION_ORDER[i] == "Economic Impact" and QUALITY_ORDER[j] == "B")
        cell_hex = mpl.colors.to_hex(HARBOR_CMAP(val / 100))
        color = SIGNAL_AMBER if is_flag else text_color_for_bg(cell_hex)
        weight = "bold" if is_flag else "normal"
        ax.text(j, i, f"{val:.1f}", ha="center", va="center", color=color, fontsize=10, fontweight=weight)
cbar = fig.colorbar(im, ax=ax, shrink=0.85)
cbar.set_label("% within dimension")
title(ax, "Evidence quality composition within each analytical dimension",
      "Amber highlights Economic Impact: 100% Category-B evidence, a key gap")
plt.savefig(OUT_DIR / "B1_quality_by_dimension.png", bbox_inches="tight")
plt.close()

# ---------------------------------------------------------------------
# (B2) Dimension x Year heatmap, with 2026 truncation note
# ---------------------------------------------------------------------
tab_year = pd.crosstab(df["Primary_Dimension_Normalized"], df["Publication Year"])
tab_year = tab_year.reindex(index=DIMENSION_ORDER, columns=YEAR_ORDER, fill_value=0)

fig, ax = plt.subplots(figsize=(9, 6.2))
im = ax.imshow(tab_year.values, cmap=HARBOR_CMAP, aspect="auto")
ax.set_xticks(range(len(YEAR_ORDER)))
ax.set_xticklabels(YEAR_ORDER)
ax.set_yticks(range(len(DIMENSION_ORDER)))
ax.set_yticklabels(DIMENSION_ORDER)
vmax = tab_year.values.max()
for i in range(len(DIMENSION_ORDER)):
    for j in range(len(YEAR_ORDER)):
        val = tab_year.values[i, j]
        cell_hex = mpl.colors.to_hex(HARBOR_CMAP(val / vmax if vmax else 0))
        color = text_color_for_bg(cell_hex)
        ax.text(j, i, f"{val}", ha="center", va="center", color=color, fontsize=10)
cbar = fig.colorbar(im, ax=ax, shrink=0.85)
cbar.set_label("Papers")
title(ax, "Primary dimension × publication year")
note(fig, "Note: 2026 reflects a partial year (search cutoff before year-end) and should not be read as a declining trend.")
plt.savefig(OUT_DIR / "B2_dimension_by_year.png", bbox_inches="tight")
plt.close()

# ---------------------------------------------------------------------
# (B3) Quality evolution by year — stacked %, WITH amber A1 trend line
# ---------------------------------------------------------------------
tab_yq = pd.crosstab(df["Publication Year"], df["Clasificación"])
tab_yq = tab_yq.reindex(index=YEAR_ORDER, columns=QUALITY_ORDER, fill_value=0)
tab_yq_pct = tab_yq.div(tab_yq.sum(axis=1), axis=0) * 100

fig, ax = plt.subplots(figsize=(9, 6))
x = np.arange(len(YEAR_ORDER))
bottom = np.zeros(len(YEAR_ORDER))
for q in QUALITY_ORDER:
    vals = tab_yq_pct[q].values
    ax.bar(x, vals, bottom=bottom, label=q, color=QUALITY_COLORS[q], width=0.62)
    txt_color = text_color_for_bg(QUALITY_COLORS[q])
    for i, v in enumerate(vals):
        n_val = tab_yq.loc[YEAR_ORDER[i], q]
        if v > 4:
            ax.text(x[i], bottom[i] + v / 2, f"{n_val}", ha="center", va="center", fontsize=9.5, color=txt_color)
    bottom += vals

# Amber trend line: % A1 by year, on secondary axis sharing the same 0-100 scale
a1_pct = tab_yq_pct["A1"].values
ax2 = ax.twinx()
ax2.plot(x, a1_pct, color=SIGNAL_AMBER, marker="o", markersize=6, linewidth=2.4, zorder=5, label="A1 share (trend)")
ax2.set_ylim(0, 100)
ax2.set_yticks([])
for i, v in enumerate(a1_pct):
    ax2.annotate(f"{v:.0f}%", (x[i], v), textcoords="offset points", xytext=(0, 8),
                 ha="center", fontsize=9, color=SIGNAL_AMBER, fontweight="bold")

ax.set_xticks(x)
ax.set_xticklabels([str(y) for y in YEAR_ORDER])
ax.set_ylabel("% of studies published that year")
ax.set_ylim(0, 100)

handles1, labels1 = ax.get_legend_handles_labels()
handles2, labels2 = ax2.get_legend_handles_labels()
ax.legend(handles1 + handles2, labels1 + labels2, loc="upper left", bbox_to_anchor=(1.02, 1), frameon=False)

title(ax, "Evolution of evidence quality by publication year",
      "Amber line: share of A1 (high-rigour) studies — rising from 16.7% (2022) to 54.7% (2026)")
note(fig, "Note: 2026 reflects a partial year (search cutoff before year-end).")
plt.savefig(OUT_DIR / "B3_quality_evolution_by_year.png", bbox_inches="tight")
plt.close()

# ---------------------------------------------------------------------
# (C1) Dimension co-occurrence heatmap — diagonal relabelled as total
# ---------------------------------------------------------------------
binary_cols = list(DIM_BINARY_COLUMNS.keys())
labels = [DIM_BINARY_COLUMNS[c] for c in binary_cols]
mat = df[binary_cols].T.dot(df[binary_cols])
mat.index = labels
mat.columns = labels
mat = mat.reindex(index=DIMENSION_ORDER, columns=DIMENSION_ORDER)

fig, ax = plt.subplots(figsize=(9.2, 7.6))
im = ax.imshow(mat.values, cmap=HARBOR_CMAP, aspect="auto")
ax.set_xticks(range(len(DIMENSION_ORDER)))
ax.set_xticklabels(DIMENSION_ORDER, rotation=40, ha="right")
ax.set_yticks(range(len(DIMENSION_ORDER)))
ax.set_yticklabels(DIMENSION_ORDER)
vmax = mat.values.max()
for i in range(len(DIMENSION_ORDER)):
    for j in range(len(DIMENSION_ORDER)):
        val = mat.values[i, j]
        cell_hex = mpl.colors.to_hex(HARBOR_CMAP(val / vmax if vmax else 0))
        color = text_color_for_bg(cell_hex)
        label = f"{val}\n(total)" if i == j else f"{val}"
        weight = "bold" if i == j else "normal"
        ax.text(j, i, label, ha="center", va="center", color=color, fontsize=9.5, fontweight=weight)
cbar = fig.colorbar(im, ax=ax, shrink=0.85)
cbar.set_label("Co-occurrence count")
title(ax, "Dimension co-occurrence across binary dimension flags",
      "Diagonal = total studies flagged for that dimension, not self-correlation")
plt.savefig(OUT_DIR / "C1_dimension_cooccurrence.png", bbox_inches="tight")
plt.close()

print("Done. Figures in", OUT_DIR)
for f in sorted(OUT_DIR.glob("*.png")):
    print(" -", f.name)
