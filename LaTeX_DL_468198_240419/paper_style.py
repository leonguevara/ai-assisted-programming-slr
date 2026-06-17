"""
paper_style.py — Mini design-system para las figuras del SLR
(AI-Assisted Programming in Software Engineering, EmSE submission).

Filosofía de color:
- Paleta secuencial neutral (azul-teal, "Harbor") para todo lo descriptivo:
  distribuciones, conteos, proporciones. No carga ningún mensaje de valor.
- Acento cálido (ámbar/naranja, "Signal") reservado EXCLUSIVAMENTE para
  resaltar hallazgos de riesgo, alerta metodológica, o datos que requieren
  atención del lector (ej. evidencia de baja calidad, preprints, sesgos
  temporales). Si todo se resalta, nada se resalta — este acento se usa
  con moderación, nunca como color "de relleno".
- Evitar combinaciones rojo-verde puras (riesgo de daltonismo). Donde se
  necesite una escala de "calidad" categórica (A1/A2/B), usar gradiente
  azul oscuro -> azul claro -> gris, nunca semáforo rojo-amarillo-verde.

Tipografía: Liberation Sans (equivalente métrico a Arial/Helvetica),
consistente con las figuras esperadas por plantillas Springer (sn-jnl).
"""

import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import seaborn as sns

# ---------------------------------------------------------------------
# PALETA
# ---------------------------------------------------------------------
HARBOR = ["#0B3954", "#177E89", "#3FA7B5", "#8FCAD2", "#D6EAEE"]  # dark -> light
HARBOR_SEQ = "Harbor"  # registered colormap name, see below

SIGNAL_AMBER = "#E8871E"     # accent: risk / attention finding
SIGNAL_AMBER_LIGHT = "#F6C28B"

NEUTRAL_GRAY = "#9AA5B1"      # for "n/a" or de-emphasised categories
INK = "#1B2430"               # near-black for text/titles (not pure black)

QUALITY_COLORS = {            # A1/A2/B — sequential, not semaphore
    "A1": "#0B3954",
    "A2": "#3FA7B5",
    "B": "#C9DCE0",
}

DIMENSION_PALETTE = [          # qualitative, for the 7 dimensions, ordered
    "#0B3954", "#177E89", "#3FA7B5", "#7FB3C8",
    "#A9C5D1", "#CBD8DD", "#E8871E",  # last slot reserved if a dim needs flagging
]

from matplotlib.colors import LinearSegmentedColormap
HARBOR_CMAP = LinearSegmentedColormap.from_list(
    "harbor", ["#F4FAFB", "#D6EAEE", "#8FCAD2", "#3FA7B5", "#177E89", "#0B3954"]
)

# ---------------------------------------------------------------------
# TIPOGRAFÍA Y RC PARAMS
# ---------------------------------------------------------------------
def apply_style():
    sns.set_theme(style="whitegrid", context="paper")
    plt.rcParams["font.family"] = "Liberation Sans"
    plt.rcParams["text.color"] = INK
    plt.rcParams["axes.labelcolor"] = INK
    plt.rcParams["xtick.color"] = INK
    plt.rcParams["ytick.color"] = INK
    plt.rcParams["axes.edgecolor"] = "#C7CDD3"
    plt.rcParams["axes.titleweight"] = "bold"
    plt.rcParams["axes.titlesize"] = 13
    plt.rcParams["axes.titlepad"] = 12
    plt.rcParams["axes.labelweight"] = "regular"
    plt.rcParams["axes.labelsize"] = 10.5
    plt.rcParams["xtick.labelsize"] = 10
    plt.rcParams["ytick.labelsize"] = 10
    plt.rcParams["figure.dpi"] = 140
    plt.rcParams["savefig.dpi"] = 300
    plt.rcParams["axes.grid"] = True
    plt.rcParams["grid.color"] = "#E7EAED"
    plt.rcParams["grid.linewidth"] = 0.6
    plt.rcParams["legend.frameon"] = False
    plt.rcParams["legend.fontsize"] = 9.5
    plt.rcParams["legend.title_fontsize"] = 10


def note(fig, text, y=0.02):
    """Standard italic footnote under a figure, for caveats (e.g. truncated years).
    Reserves bottom margin explicitly so the text is never clipped on save."""
    fig.text(0.5, y, text, ha="center", fontsize=8.5, style="italic", color="#5B6470")
    fig.subplots_adjust(bottom=max(fig.subplotpars.bottom, 0.12))


def title(ax, text, subtitle=None):
    """Sets a left-aligned bold title with an optional italic subtitle directly
    beneath it, using figure-level placement so it never collides with the
    plot area regardless of axis type (pie charts have no ticks/spines to
    anchor against)."""
    fig = ax.get_figure()
    if subtitle:
        fig.suptitle(text, x=0.02, y=0.98, ha="left", fontsize=13, fontweight="bold", color=INK)
        fig.text(0.02, 0.93, subtitle, ha="left", fontsize=9, color="#5B6470", style="italic")
        fig.subplots_adjust(top=0.86)
    else:
        fig.suptitle(text, x=0.02, y=0.98, ha="left", fontsize=13, fontweight="bold", color=INK)
        fig.subplots_adjust(top=0.90)


def text_color_for_bg(hex_color, light=INK, dark="white"):
    """Returns a readable text color (light/dark) based on background luminance,
    so labels never blend into dark Harbor cells."""
    hex_color = hex_color.lstrip("#")
    r, g, b = [int(hex_color[i:i+2], 16) / 255 for i in (0, 2, 4)]
    luminance = 0.299 * r + 0.587 * g + 0.114 * b
    return light if luminance > 0.55 else dark
