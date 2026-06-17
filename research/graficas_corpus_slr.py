"""
Genera tablas y gráficas descriptivas del corpus SLR.

Requisitos:
    pip install pandas openpyxl matplotlib seaborn

Uso:
    python graficas_corpus_slr.py

Entrada esperada:
    datos_paper_tableau.xlsx con hoja "Corpus".

Salida:
    ./slr_outputs/tables/*.csv
    ./slr_outputs/figures/*.png
    ./slr_outputs/tables/resumen_tablas.xlsx
"""

from pathlib import Path
import textwrap

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ---------------------------------------------------------------------
# 1. CONFIGURACIÓN GENERAL
# ---------------------------------------------------------------------
INPUT_FILE = Path("datos_paper_tableau.xlsx")
SHEET_NAME = "Corpus"
OUTPUT_DIR = Path("slr_outputs")
FIG_DIR = OUTPUT_DIR / "figures"
TABLE_DIR = OUTPUT_DIR / "tables"
FIG_DIR.mkdir(parents=True, exist_ok=True)
TABLE_DIR.mkdir(parents=True, exist_ok=True)

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
SEGMENT_ORDER = ["CORE", "SUPPORTING", "PERIPHERAL", "REMOVE_CANDIDATE"]
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

# ---------------------------------------------------------------------
# 2. FUNCIONES AUXILIARES
# ---------------------------------------------------------------------
def pct_table(series: pd.Series, order=None, index_name="Category") -> pd.DataFrame:
    """Devuelve tabla con conteos y porcentajes."""
    counts = series.value_counts(dropna=False)
    if order is not None:
        counts = counts.reindex(order, fill_value=0)
    out = counts.rename("Papers").to_frame()
    out["Percent"] = out["Papers"] / out["Papers"].sum() * 100
    out.index.name = index_name
    return out.reset_index()


def pivot_count(df, index, columns, index_order=None, column_order=None) -> pd.DataFrame:
    """Tabla cruzada de conteos con orden explícito."""
    tab = pd.crosstab(df[index], df[columns])
    if index_order is not None:
        tab = tab.reindex(index_order, fill_value=0)
    if column_order is not None:
        tab = tab.reindex(columns=column_order, fill_value=0)
    return tab


def wrap_labels(labels, width=24):
    return ["\n".join(textwrap.wrap(str(label), width=width)) for label in labels]


def save_barplot(data, x, y, title, filename, xlabel="", ylabel="Papers", orient="v", annotate=True):
    plt.figure(figsize=(10, 5.8))
    if orient == "h":
        ax = sns.barplot(data=data, y=x, x=y, order=data[x].tolist(), color=sns.color_palette()[0])
        ax.set_xlabel(ylabel)
        ax.set_ylabel(xlabel)
        if annotate:
            for container in ax.containers:
                ax.bar_label(container, fmt="%.0f", padding=3)
    else:
        ax = sns.barplot(data=data, x=x, y=y, order=data[x].tolist(), color=sns.color_palette()[0])
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        ax.set_xticklabels(wrap_labels(data[x].tolist(), width=18), rotation=0)
        if annotate:
            for container in ax.containers:
                ax.bar_label(container, fmt="%.0f", padding=3)
    ax.set_title(title)
    plt.tight_layout()
    plt.savefig(FIG_DIR / filename, bbox_inches="tight")
    plt.close()


def save_stacked_bar(tab, title, filename, xlabel="", ylabel="Papers", percent=False):
    plot_tab = tab.copy()
    if percent:
        plot_tab = plot_tab.div(plot_tab.sum(axis=1), axis=0).fillna(0) * 100
        ylabel = "% within row"

    ax = plot_tab.plot(kind="bar", stacked=True, figsize=(11, 6))
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_xticklabels(wrap_labels(plot_tab.index, width=18), rotation=0, ha="center")
    ax.legend(title="Category", bbox_to_anchor=(1.02, 1), loc="upper left")
    plt.tight_layout()
    plt.savefig(FIG_DIR / filename, bbox_inches="tight")
    plt.close()


def save_heatmap(tab, title, filename, annot_fmt="d"):
    plt.figure(figsize=(10, 6))
    ax = sns.heatmap(tab, annot=True, fmt=annot_fmt, linewidths=.5, cmap="YlGnBu")
    ax.set_title(title)
    ax.set_xlabel("")
    ax.set_ylabel("")
    plt.tight_layout()
    plt.savefig(FIG_DIR / filename, bbox_inches="tight")
    plt.close()

# ---------------------------------------------------------------------
# 3. CARGA Y LIMPIEZA
# ---------------------------------------------------------------------
df = pd.read_excel(INPUT_FILE, sheet_name=SHEET_NAME)

# Normalización básica defensiva.
text_cols = [
    "Primary_Dimension_Normalized", "Segment", "Clasificación", "Nivel_Soporte",
    "Item Type", "Source", "Redundancy Level", "Weakens Underrepresented Dim if Removed"
]
for col in text_cols:
    if col in df.columns:
        df[col] = df[col].astype("string").str.strip()

# Año como entero nullable.
df["Publication Year"] = pd.to_numeric(df["Publication Year"], errors="coerce").astype("Int64")

# Columnas binarias DIM_* como enteros 0/1.
for col in DIM_BINARY_COLUMNS:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0).astype(int)

n = len(df)
print(f"Corpus cargado: {n} papers")

# ---------------------------------------------------------------------
# 4. TABLAS DESCRIPTIVAS
# ---------------------------------------------------------------------
tables = {}

tables["dimension_distribution"] = pct_table(
    df["Primary_Dimension_Normalized"], DIMENSION_ORDER, "Dimension"
)
tables["segment_distribution"] = pct_table(df["Segment"], SEGMENT_ORDER, "Segment")
tables["quality_distribution"] = pct_table(df["Clasificación"], QUALITY_ORDER, "Evidence quality")
tables["year_distribution"] = pct_table(df["Publication Year"], YEAR_ORDER, "Publication year")

tables["dimension_x_segment"] = pivot_count(
    df, "Primary_Dimension_Normalized", "Segment", DIMENSION_ORDER, SEGMENT_ORDER
)
tables["dimension_x_quality"] = pivot_count(
    df, "Primary_Dimension_Normalized", "Clasificación", DIMENSION_ORDER, QUALITY_ORDER
)
tables["year_x_quality"] = pivot_count(
    df, "Publication Year", "Clasificación", YEAR_ORDER, QUALITY_ORDER
)
tables["dimension_x_year"] = pivot_count(
    df, "Primary_Dimension_Normalized", "Publication Year", DIMENSION_ORDER, YEAR_ORDER
)

core_df = df[df["Segment"].eq("CORE")].copy()
tables["core_dimension_distribution"] = pct_table(
    core_df["Primary_Dimension_Normalized"], DIMENSION_ORDER, "Dimension"
).rename(columns={"Papers": "Core Papers", "Percent": "% of Core"})

quality_by_dim = tables["dimension_x_quality"].copy()
quality_by_dim["Total"] = quality_by_dim.sum(axis=1)
quality_by_dim["A1 maturity %"] = (quality_by_dim["A1"] / quality_by_dim["Total"] * 100).fillna(0)
tables["dimension_maturity_index"] = quality_by_dim[["A1", "Total", "A1 maturity %"]].sort_values(
    "A1 maturity %", ascending=False
)

# Co-ocurrencia entre dimensiones binarias: útil porque un paper puede tocar varias dimensiones.
dim_binary = df[list(DIM_BINARY_COLUMNS.keys())].rename(columns=DIM_BINARY_COLUMNS)
tables["dimension_binary_frequency"] = dim_binary.sum().sort_values(ascending=False).rename("Papers").to_frame()
tables["dimension_cooccurrence"] = dim_binary.T.dot(dim_binary)

# Porcentajes fila para heatmaps normalizados.
tables["dimension_x_segment_rowpct"] = tables["dimension_x_segment"].div(
    tables["dimension_x_segment"].sum(axis=1), axis=0
).fillna(0) * 100

tables["dimension_x_quality_rowpct"] = tables["dimension_x_quality"].div(
    tables["dimension_x_quality"].sum(axis=1), axis=0
).fillna(0) * 100

# Guardar tablas.
for name, table in tables.items():
    table.to_csv(TABLE_DIR / f"{name}.csv", encoding="utf-8-sig")

with pd.ExcelWriter(TABLE_DIR / "resumen_tablas.xlsx", engine="openpyxl") as writer:
    for name, table in tables.items():
        table.to_excel(writer, sheet_name=name[:31])

# ---------------------------------------------------------------------
# 5. GRÁFICAS BÁSICAS
# ---------------------------------------------------------------------
save_barplot(
    tables["dimension_distribution"], "Dimension", "Papers",
    "Distribution by primary dimension", "01_dimension_distribution.png",
    xlabel="Primary dimension", ylabel="Papers", orient="h"
)

save_barplot(
    tables["segment_distribution"], "Segment", "Papers",
    "Epistemological distribution by segment", "02_segment_distribution.png",
    xlabel="Segment", ylabel="Papers"
)

save_barplot(
    tables["quality_distribution"], "Evidence quality", "Papers",
    "Distribution by evidence quality", "03_quality_distribution.png",
    xlabel="Evidence quality", ylabel="Papers"
)

save_barplot(
    tables["year_distribution"], "Publication year", "Papers",
    "Temporal distribution of the corpus", "04_year_distribution.png",
    xlabel="Publication year", ylabel="Papers"
)

# ---------------------------------------------------------------------
# 6. GRÁFICAS APILADAS
# ---------------------------------------------------------------------
save_stacked_bar(
    tables["dimension_x_segment"],
    "Primary dimension × segment", "05_dimension_x_segment_stacked.png",
    xlabel="Primary dimension"
)

save_stacked_bar(
    tables["dimension_x_quality"],
    "Primary dimension × evidence quality", "06_dimension_x_quality_stacked.png",
    xlabel="Primary dimension"
)

save_stacked_bar(
    tables["year_x_quality"],
    "Publication year × evidence quality", "07_year_x_quality_stacked.png",
    xlabel="Publication year"
)

save_stacked_bar(
    tables["dimension_x_quality"],
    "Evidence quality composition within each dimension", "08_dimension_x_quality_rowpct_stacked.png",
    xlabel="Primary dimension", percent=True
)

# ---------------------------------------------------------------------
# 7. ÍNDICE DE MADUREZ Y CORE DATASET
# ---------------------------------------------------------------------
maturity_plot = tables["dimension_maturity_index"].reset_index().rename(
    columns={"Primary_Dimension_Normalized": "Dimension"}
)
if "Dimension" not in maturity_plot.columns:
    maturity_plot = maturity_plot.rename(columns={maturity_plot.columns[0]: "Dimension"})

save_barplot(
    maturity_plot, "Dimension", "A1 maturity %",
    "Maturity index: % of A1 studies within each dimension", "09_dimension_maturity_index.png",
    xlabel="Primary dimension", ylabel="A1 studies within dimension (%)", orient="h", annotate=False
)

save_barplot(
    tables["core_dimension_distribution"].rename(columns={"Core Papers": "Papers"}),
    "Dimension", "Papers",
    "Core dataset distribution by dimension", "10_core_dimension_distribution.png",
    xlabel="Primary dimension", ylabel="Core papers", orient="h"
)

# ---------------------------------------------------------------------
# 8. MAPAS DE CALOR
# ---------------------------------------------------------------------
save_heatmap(
    tables["dimension_x_segment"],
    "Heatmap: primary dimension × segment", "11_heatmap_dimension_x_segment.png", "d"
)

save_heatmap(
    tables["dimension_x_quality"],
    "Heatmap: primary dimension × evidence quality", "12_heatmap_dimension_x_quality.png", "d"
)

save_heatmap(
    tables["year_x_quality"],
    "Heatmap: publication year × evidence quality", "13_heatmap_year_x_quality.png", "d"
)

save_heatmap(
    tables["dimension_x_year"],
    "Heatmap: primary dimension × publication year", "14_heatmap_dimension_x_year.png", "d"
)

save_heatmap(
    tables["dimension_cooccurrence"],
    "Heatmap: dimension co-occurrence across binary DIM_* columns", "15_heatmap_dimension_cooccurrence.png", "d"
)

save_heatmap(
    tables["dimension_x_quality_rowpct"].round(1),
    "Heatmap: evidence quality composition within each dimension (%)", "16_heatmap_dimension_x_quality_rowpct.png", ".1f"
)

save_heatmap(
    tables["dimension_x_segment_rowpct"].round(1),
    "Heatmap: segment composition within each dimension (%)", "17_heatmap_dimension_x_segment_rowpct.png", ".1f"
)

# ---------------------------------------------------------------------
# 9. GRÁFICAS ADICIONALES ÚTILES
# ---------------------------------------------------------------------
# Tipo de documento
if "Item Type" in df.columns:
    item_type = pct_table(df["Item Type"], index_name="Item Type").sort_values("Papers", ascending=False)
    item_type.to_csv(TABLE_DIR / "item_type_distribution.csv", index=False, encoding="utf-8-sig")
    save_barplot(
        item_type, "Item Type", "Papers",
        "Distribution by item type", "18_item_type_distribution.png",
        xlabel="Item type", ylabel="Papers", orient="h"
    )

# Nivel de soporte
if "Nivel_Soporte" in df.columns:
    support_level = pct_table(df["Nivel_Soporte"], index_name="Support level").sort_values("Papers", ascending=False)
    support_level.to_csv(TABLE_DIR / "support_level_distribution.csv", index=False, encoding="utf-8-sig")
    save_barplot(
        support_level, "Support level", "Papers",
        "Distribution by support level", "19_support_level_distribution.png",
        xlabel="Support level", ylabel="Papers"
    )

# Fuente de recuperación / indexación
if "Source" in df.columns:
    source_dist = pct_table(df["Source"], index_name="Source").sort_values("Papers", ascending=False)
    source_dist.to_csv(TABLE_DIR / "source_distribution.csv", index=False, encoding="utf-8-sig")
    save_barplot(
        source_dist, "Source", "Papers",
        "Distribution by source", "20_source_distribution.png",
        xlabel="Source", ylabel="Papers", orient="h"
    )

print(f"Listo. Tablas en: {TABLE_DIR.resolve()}")
print(f"Listo. Figuras en: {FIG_DIR.resolve()}")
