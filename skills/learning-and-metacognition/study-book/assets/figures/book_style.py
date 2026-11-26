"""Plotly house style for study-book figures. Copy unchanged into <project>/figures/.

Use in each figure script (figures/NN-slug.py, one script per Part):

    from book_style import go, save, ROLE, DASH, label_ends   # or: from book_style import diagram, save
    fig = go.Figure(...)
    save(fig, "02-svd-singular-values")       # writes figures/02-svd-singular-values.svg

Then in the Part: #fig(image("/figures/02-svd-singular-values.svg"), [caption])
"""
import math
from numbers import Real
from pathlib import Path

import plotly.graph_objects as go
import plotly.io as pio

# Same palette as lib/template.typ (c-blue, c-orange, c-aqua, c-yellow, c-violet, c-red, c-muted).
COLORS = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#6250d6", "#e34948", "#5f5e5a"]
INK, MUTED = "#1b1b1a", "#5f5e5a"

# Colour is a role, not an order. Only blue, orange, aqua pass a colour-blind check as a set
# (red≈orange and violet≈blue fail even for normal vision), so they are the only data-series
# colours; a 4th series goes to small multiples. Pair each series colour with its dash, so lines
# stay apart in grayscale print.
ROLE = dict(
    main="#2a78d6", second="#eb6834", third="#1baf7a",  # data series, in this order
    breaks="#e34948",     # only for where an idea fails; always with a text label
    context="#5f5e5a",    # true solution, reference lines, baselines
    highlight="#6250d6",  # one point or region the caption is about; never a series
)
DASH = dict(main="solid", second="dash", third="dot")

pio.templates["book"] = go.layout.Template(
    layout=dict(
        font=dict(family="Libertinus Serif, New Computer Modern, serif", size=16, color=INK),
        colorway=[ROLE["main"], ROLE["second"], ROLE["third"]],
        paper_bgcolor="white",
        plot_bgcolor="white",
        margin=dict(l=60, r=20, t=30, b=50),
        xaxis=dict(automargin=True, showline=True, linecolor=MUTED, ticks="outside", tickcolor=MUTED, zeroline=False, showgrid=False),
        yaxis=dict(automargin=True, showline=True, linecolor=MUTED, ticks="outside", tickcolor=MUTED, zeroline=False, showgrid=False),
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


def label_ends(fig, at=None):
    """Label each named line trace in ink next to its last point (or the point nearest x = at),
    and hide the legend. Use when 2–3 lines are apart at that x (SKILL.md §7, labelling).

    Missing, non-finite and (on a log axis) non-positive points are skipped. If a named line has no
    usable point, nothing is labelled and the legend stays."""
    def is_log(ref, kind):  # "x2" -> layout.xaxis2
        return fig.layout[kind + "axis" + ref[1:]].type == "log"

    def usable(v, log):
        if v is None or (isinstance(v, Real) and not math.isfinite(v)):
            return False
        return not log or v > 0

    labels = []
    for tr in fig.data:
        if not (tr.name and tr.x is not None and tr.y is not None and len(tr.x)):
            continue
        xref, yref = tr.xaxis or "x", tr.yaxis or "y"
        logx, logy = is_log(xref, "x"), is_log(yref, "y")
        points = [(x, y) for x, y in zip(tr.x, tr.y) if usable(x, logx) and usable(y, logy)]
        if not points:
            fig.update_layout(showlegend=True)
            return fig
        x, y = points[-1] if at is None else min(points, key=lambda p: abs(p[0] - at))
        # annotations on a log axis take log10 positions
        labels.append(dict(x=math.log10(x) if logx else x, y=math.log10(y) if logy else y,
                           text=tr.name, xref=xref, yref=yref))
    for label in labels:
        fig.add_annotation(**label, showarrow=False, xanchor="left", xshift=6,
                           font=dict(color=INK, size=14))
    fig.update_layout(showlegend=False, margin=dict(r=40))
    return fig


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

    if not nodes:
        raise ValueError("diagram: no nodes")
    for k, (x, y, _) in nodes.items():
        if not (math.isfinite(x) and math.isfinite(y)):
            raise ValueError(f"diagram: node {k!r} has a non-finite coordinate")
    for a, b, *_ in edges:
        if a not in nodes or b not in nodes:
            raise ValueError(f"diagram: edge {a!r} -> {b!r} names an unknown node")
        if tuple(nodes[a][:2]) == tuple(nodes[b][:2]):
            raise ValueError(f"diagram: edge {a!r} -> {b!r} starts and ends at one point")

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


if __name__ == "__main__":  # self-check: python3 book_style.py
    def line(y, at=None):
        f = go.Figure(go.Scatter(x=[0, 1, 2], y=y, name="a"))
        f.update_yaxes(type="log")
        return label_ends(f, at)

    for y in ([1, 0.1, 0], [1, 0.1, None], [1, 0.1, float("nan")]):  # last usable point wins
        a = line(y).layout.annotations[0]
        assert (a.x, a.y) == (1, -1), (y, a.x, a.y)
    assert line([None, 0.1, 1], at=0).layout.annotations[0].x == 1  # nearest usable point
    none_usable = line([0, -1, None])
    assert none_usable.layout.showlegend is True and not none_usable.layout.annotations

    n = {"a": (0, 0, "a"), "b": (4, 0, "b"), "c": (4, 0, "c")}
    assert diagram(n, [("a", "b", "ok")]).layout.height > 0
    for nodes, edges in (({}, []), ({"a": (float("nan"), 0, "a")}, []), (n, [("a", "z", "")]),
                         (n, [("a", "a", "")]), (n, [("b", "c", "")])):
        try:
            diagram(nodes, edges)
        except ValueError as e:
            assert str(e).startswith("diagram:"), e
        else:
            raise AssertionError(f"accepted {edges or nodes}")
    print("book_style ok")
