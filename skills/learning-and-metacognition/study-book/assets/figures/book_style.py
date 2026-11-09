"""Plotly house style for study-book figures. Copy unchanged into <project>/figures/.

Use in each figure script (figures/NN-slug.py, one script per Part):

    from book_style import go, save
    fig = go.Figure(...)
    save(fig, "02-svd-singular-values")       # writes figures/02-svd-singular-values.svg

Then in the Part: #fig(image("/figures/02-svd-singular-values.svg"), [caption])
"""
from pathlib import Path

import plotly.graph_objects as go
import plotly.io as pio

# Same palette as lib/template.typ (c-blue, c-orange, c-aqua, c-yellow, c-violet, c-red, c-muted).
COLORS = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#6250d6", "#e34948", "#5f5e5a"]
INK, MUTED = "#1b1b1a", "#5f5e5a"

pio.templates["book"] = go.layout.Template(
    layout=dict(
        font=dict(family="Libertinus Serif, New Computer Modern, serif", size=16, color=INK),
        colorway=COLORS,
        paper_bgcolor="white",
        plot_bgcolor="white",
        margin=dict(l=60, r=20, t=30, b=50),
        xaxis=dict(showline=True, linecolor=MUTED, ticks="outside", tickcolor=MUTED, zeroline=False, showgrid=False),
        yaxis=dict(showline=True, linecolor=MUTED, ticks="outside", tickcolor=MUTED, zeroline=False, showgrid=False),
        legend=dict(bgcolor="rgba(0,0,0,0)"),
    )
)
pio.templates.default = "book"

OUT = Path(__file__).resolve().parent


def save(fig, name, width=640, height=380):
    """Write figures/<name>.svg at a fixed size so text scales consistently across figures."""
    fig.write_image(OUT / f"{name}.svg", width=width, height=height)
