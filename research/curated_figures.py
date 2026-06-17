"""
Genera el conjunto curado de figuras para la sección de Results del SLR.

Curaduría aplicada (sesión de revisión con León, junio 2026):
- DESCARTADAS por completo: Nivel_Soporte (19_, vocabulario no normalizado,
  mezcla ES/EN) y Source (20_, contradice la metodología dual-branch
  documentada en la Sección 2.3 — requiere auditoría antes de cualquier uso).
- DESCARTADA por redundancia: dimension_maturity_index (09_, ya contenida
  en la primera columna del heatmap de calidad por dimensión).
- RETENIDAS con corrección: heatmap de calidad por dimensión, heatmap de
  co-ocurrencia (diagonal anotada como total, no autocorrelación), heatmap
  dimensión × año (con nota de truncamiento 2026), item type (movida a
  Threats to Validity).
- NUEVA: evolución temporal de calidad (A1/A2/B por año), ausente en las
  20 figuras originales pero presente como tabla en el análisis de ChatGPT.

Entrada esperada: datos_paper_tableau.xlsx con hoja "Corpus".
Salida: ./slr_outputs_curated/figures/*.png
"""

from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

INPUT_FILE = Path("/mnt/user-data/uploads/datos_paper_tableau.xlsx")
SHEET_NAME = "Corpus"
OUT_DIR = Path("/home/claude/slr_outputs_curated/figures")
OUT_DIR.mkdir(parents=True, exist_ok=True)

sns.set_theme(style="whitegrid", context="paper", font_scale=1.05)
plt.rcParams["figure.dpi"] = 140
plt.rcParams["savefig.dpi"] = 300
plt.rcParams["axes.titleweight"] = "bold"
plt.rcParams["axes.labelweight"] = "bold"

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

# ---------------------------------------------------------------------
# Figure 1: Quality composition within each dimension (row %)
# ---------------------------------------------------------------------
tab = pd.crosstab(df["Primary_Dimension_Normalized"], df["Clasificación"])
tab = tab.reindex(index=DIMENSION_ORDER, columns=QUALITY_ORDER, fill_value=0)
rowpct = tab.div(tab.sum(axis=1), axis=0) * 100

plt.figure(figsize=(9, 6))
ax = sns.heatmap(
    rowpct, annot=True, fmt=".1f", linewidths=0.6, cmap="YlGnBu",
    cbar_kws={"label": "% within dimension"},
)
ax.set_title("Evidence quality composition within each analytical dimension (%)")
ax.set_xlabel("")
ax.set_ylabel("")
plt.tight_layout()
plt.savefig(OUT_DIR / "fig_quality_by_dimension.png", bbox_inches="tight")
plt.close()

# ---------------------------------------------------------------------
# Figure 2: Dimension co-occurrence (off-diagonal = co-occurrence,
# diagonal explicitly relabelled as "Total flagged" to avoid the
# self-correlation misreading)
# ---------------------------------------------------------------------
binary_cols = list(DIM_BINARY_COLUMNS.keys())
labels = [DIM_BINARY_COLUMNS[c] for c in binary_cols]
mat = df[binary_cols].T.dot(df[binary_cols])
mat.index = labels
mat.columns = labels
mat = mat.reindex(index=DIMENSION_ORDER, columns=DIMENSION_ORDER)

annot = mat.astype(str)
diag_totals = {}
for d in DIMENSION_ORDER:
    diag_totals[d] = mat.loc[d, d]
    annot.loc[d, d] = f"{mat.loc[d, d]}\n(total)"

mask_diag = pd.DataFrame(False, index=mat.index, columns=mat.columns)
for d in DIMENSION_ORDER:
    mask_diag.loc[d, d] = False  # keep diagonal visible but relabelled

plt.figure(figsize=(10, 7.5))
ax = sns.heatmap(
    mat, annot=annot, fmt="", linewidths=0.6, cmap="YlGnBu",
    cbar_kws={"label": "Co-occurrence count"},
)
ax.set_title("Dimension co-occurrence across binary DIM_* flags\n(diagonal = total studies flagged for that dimension, not self-correlation)")
ax.set_xlabel("")
ax.set_ylabel("")
plt.xticks(rotation=40, ha="right")
plt.tight_layout()
plt.savefig(OUT_DIR / "fig_dimension_cooccurrence.png", bbox_inches="tight")
plt.close()

# ---------------------------------------------------------------------
# Figure 3: Dimension x Year heatmap, with 2026 truncation note
# ---------------------------------------------------------------------
tab_year = pd.crosstab(df["Primary_Dimension_Normalized"], df["Publication Year"])
tab_year = tab_year.reindex(index=DIMENSION_ORDER, columns=YEAR_ORDER, fill_value=0)

plt.figure(figsize=(10, 6.5))
ax = sns.heatmap(
    tab_year, annot=True, fmt="d", linewidths=0.6, cmap="YlGnBu",
    cbar_kws={"label": "Papers"},
)
ax.set_title("Primary dimension × publication year")
ax.set_xlabel("")
ax.set_ylabel("")
plt.figtext(
    0.5, -0.04,
    "Note: 2026 reflects a partial year (search cutoff before year-end) and should not be read as a declining trend.",
    ha="center", fontsize=8.5, style="italic",
)
plt.tight_layout()
plt.savefig(OUT_DIR / "fig_dimension_by_year.png", bbox_inches="tight")
plt.close()

# ---------------------------------------------------------------------
# Figure 4 (NEW): Quality evolution by year (A1/A2/B), stacked %
# ---------------------------------------------------------------------
tab_yq = pd.crosstab(df["Publication Year"], df["Clasificación"])
tab_yq = tab_yq.reindex(index=YEAR_ORDER, columns=QUALITY_ORDER, fill_value=0)
tab_yq_pct = tab_yq.div(tab_yq.sum(axis=1), axis=0) * 100

fig, ax = plt.subplots(figsize=(8.5, 5.5))
colors = sns.color_palette("YlGnBu", n_colors=3)[::-1]
bottom = pd.Series(0, index=tab_yq_pct.index, dtype=float)
for q, color in zip(QUALITY_ORDER, colors):
    ax.bar(tab_yq_pct.index.astype(str), tab_yq_pct[q], bottom=bottom, label=q, color=color)
    for i, year in enumerate(tab_yq_pct.index):
        val = tab_yq_pct.loc[year, q]
        n_val = tab_yq.loc[year, q]
        if val > 4:
            ax.text(i, bottom[year] + val / 2, f"{n_val}", ha="center", va="center", fontsize=9)
    bottom = bottom + tab_yq_pct[q]

ax.set_ylabel("% of studies published that year")
ax.set_xlabel("")
ax.set_title("Evolution of evidence quality by publication year")
ax.legend(title="Quality class", bbox_to_anchor=(1.02, 1), loc="upper left", frameon=False)
plt.figtext(
    0.5, -0.04,
    "Note: 2026 reflects a partial year (search cutoff before year-end).",
    ha="center", fontsize=8.5, style="italic",
)
plt.tight_layout()
plt.savefig(OUT_DIR / "fig_quality_evolution_by_year.png", bbox_inches="tight")
plt.close()

# ---------------------------------------------------------------------
# Figure 5: Item type distribution (for Threats to Validity, preprint share)
# ---------------------------------------------------------------------
item_counts = df["Item Type"].value_counts()
total = item_counts.sum()

fig, ax = plt.subplots(figsize=(8, 6.5))
colors = sns.color_palette("Set2", n_colors=len(item_counts))
wedges, texts, autotexts = ax.pie(
    item_counts.values,
    labels=None,
    autopct=lambda pct: f"{int(round(pct/100*total))}\n({pct:.1f}%)" if pct >= 1.5 else "",
    startangle=90,
    counterclock=False,
    pctdistance=0.72,
    colors=colors,
    wedgeprops={"linewidth": 1, "edgecolor": "white"},
    textprops={"fontsize": 9},
)
centre_circle = plt.Circle((0, 0), 0.45, fc="white")
ax.add_artist(centre_circle)
ax.text(0, 0, f"n = {int(total)}", ha="center", va="center", fontsize=12, fontweight="bold")
legend_labels = [f"{idx} — {val} ({val/total*100:.1f}%)" for idx, val in item_counts.items()]
ax.legend(wedges, legend_labels, title="Item type", loc="center left", bbox_to_anchor=(1.0, 0.5), frameon=False)
ax.set_title("Distribution by item type (publication-review status)", fontweight="bold")
ax.axis("equal")
plt.tight_layout()
plt.savefig(OUT_DIR / "fig_item_type_distribution.png", bbox_inches="tight")
plt.close()

print("Done. Figures written to", OUT_DIR)
for f in sorted(OUT_DIR.glob("*.png")):
    print(" -", f.name)
