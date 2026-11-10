"""Plotly house style for study-book figures. Copy unchanged into <project>/figures/.

Use in each figure script (figures/NN-slug.py, one script per Part):

    from book_style import go, save          # or: from book_style import diagram, save
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


def save(fig, name, width=None, height=None):
    """Write figures/<name>.svg at a fixed size so text scales consistently across figures.

    Default 640 x 380, or the size diagram() set on the figure.
    """
    fig.write_image(OUT / f"{name}.svg", width=width or fig.layout.width or 640,
                    height=height or fig.layout.height or 380)


def diagram(nodes, edges, pad=(1.6, 0.5), width=640):
    """Box-and-arrow diagram on a hand-placed grid (the Part's spine diagram, SKILL.md §7).

    nodes: {key: (x, y, label)}; data units, y up, start about 4 units between columns and 2–3 between rows (3 when labels have two lines);
    spread them if labels collide.
    edges: (a, b, label) or (a, b, label, {"dash": True, "side": "above|below|left|right"});
           number the labels ①②③… so the Typst caption can map each arrow to its @sec: sections.
    Labels accept Plotly HTML: SP<sub>h</sub>, x̃<sub>h</sub>, <i>…</i>, <br>. Boxes size to their text.
    pad: (x, y) margin in data units around the boxes, room for side labels; widen if one is cut.
    Height follows the layout; save(fig, name) picks the size up.
    """
    import re

    def text_px(label, char=7.2, line=20.0):  # rough extent of a 16 px serif label
        lines = re.sub(r"<(?!br)[^>]+>", "", label).split("<br>")
        return max(len(t) for t in lines) * char, len(lines) * line

    size = {k: (0.5, 0.3) for k in nodes}
    for _ in range(3):  # box size depends on px-per-unit, which depends on the range: iterate
        xs = [n[0] + s * size[k][0] for k, n in nodes.items() for s in (-1, 1)]
        ys = [n[1] + s * size[k][1] for k, n in nodes.items() for s in (-1, 1)]
        xr = [min(xs) - pad[0], max(xs) + pad[0]]
        yr = [min(ys) - pad[1], max(ys) + pad[1]]
        scale = (width - 20) / (xr[1] - xr[0])  # px per data unit; height follows the layout
        size = {k: ((text_px(n[2])[0] + 16) / 2 / scale, (text_px(n[2])[1] + 10) / 2 / scale)
                for k, n in nodes.items()}

    fig = go.Figure()
    for k, (x, y, label) in nodes.items():
        w, h = size[k]
        fig.add_shape(type="rect", x0=x - w, x1=x + w, y0=y - h, y1=y + h,
                      line=dict(color=COLORS[0], width=1.5), fillcolor="#eef4fc", layer="below")
        fig.add_annotation(x=x, y=y, text=label, showarrow=False)

    def clip(k, dx, dy):  # point where the ray from node k's centre along (dx, dy) leaves its box
        w, h = size[k]
        t = min(w / abs(dx) if dx else float("inf"), h / abs(dy) if dy else float("inf"))
        x, y = nodes[k][:2]
        return x + t * dx, y + t * dy

    for a, b, label, *opt in edges:
        o = opt[0] if opt else {}
        (xa, ya), (xb, yb) = nodes[a][:2], nodes[b][:2]
        dx, dy = xb - xa, yb - ya
        x0, y0 = clip(a, dx, dy)
        x1, y1 = clip(b, -dx, -dy)
        color = MUTED if o.get("dash") else INK
        # Shaft as a shape (can be dashed), head as a short annotation arrow.
        fig.add_shape(type="line", x0=x0, y0=y0, x1=x1, y1=y1,
                      line=dict(color=color, width=1.5, dash="dash" if o.get("dash") else "solid"))
        n = (dx * dx + dy * dy) ** 0.5
        fig.add_annotation(x=x1, y=y1, ax=x1 - 0.2 * dx / n, ay=y1 - 0.2 * dy / n, xref="x", yref="y",
                           axref="x", ayref="y", showarrow=True, arrowhead=2, arrowsize=1.2,
                           arrowwidth=1.5, arrowcolor=color, text="")
        if label:
            side = o.get("side", "above" if abs(dx) >= abs(dy) else "right")
            shift = {"above": (0, 6, "center", "bottom"), "below": (0, -6, "center", "top"),
                     "left": (-8, 0, "right", "middle"), "right": (8, 0, "left", "middle")}[side]
            yanchor = shift[3]
            if side in ("left", "right") and dx * dy:  # diagonal: lift the label off the line
                yanchor = "bottom" if (dx * dy < 0) == (side == "right") else "top"
            fig.add_annotation(x=(x0 + x1) / 2, y=(y0 + y1) / 2, text=label, showarrow=False,
                               xshift=shift[0], yshift=shift[1], xanchor=shift[2], yanchor=yanchor,
                               font=dict(size=13, color=color), align="left")
    height = round((yr[1] - yr[0]) * scale) + 20
    fig.update_layout(xaxis=dict(visible=False, range=xr),
                      yaxis=dict(visible=False, range=yr, scaleanchor="x"),
                      showlegend=False, margin=dict(l=10, r=10, t=10, b=10), width=width, height=height)
    return fig
