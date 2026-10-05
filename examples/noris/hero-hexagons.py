"""Draw the noris hexagon motif for the home banner and print it as a data URI.

    python examples/noris/hero-hexagons.py

Writes hero-hexagons.svg next to this script and prints the data URI that
$noris-hexagons in css_variables.noris.scss holds. A pointy-top honeycomb that
thins out towards the left, as in the corners of noris print material; a few
cells are filled white or noris blue 2. Same seed = same picture.
"""
import math
import os
import random
import urllib.parse

W, H, R = 560, 400, 40          # tile size and hexagon radius in px
TEAL = "rgb(17,130,145)"        # noris blue 2 (#118291); "#" would need escaping


def points(r):
    return " ".join("%g,%g" % (round(r * math.cos(math.radians(60 * i - 90)), 1),
                               round(r * math.sin(math.radians(60 * i - 90)), 1)) for i in range(6))


def main():
    random.seed(7)
    step = math.sqrt(3) * R
    cells = []
    for row in range(-1, int(H / (1.5 * R)) + 2):
        offset = step / 2 if row % 2 else 0
        for col in range(-1, int(W / step) + 2):
            cx, cy = col * step + offset, row * 1.5 * R
            density = (cx / W - 0.42) / 0.58          # 1 at the right edge, 0 at 42% of the width
            if density <= 0 or random.random() > density * 1.15:
                continue
            r = random.random()
            kind = "t" if r < 0.10 * density else ("f" if r < 0.28 * density else "o")
            if cx - step / 2 < W and -R < cy < H + R:   # skip cells entirely outside the tile
                cells.append((round(cx), round(cy), kind))
    layers = {"o": ["o"], "f": ["o", "f"], "t": ["o", "t"]}
    uses = "".join("<use href='#%s' x='%d' y='%d'/>" % (i, x, y) for x, y, k in cells for i in layers[k])
    svg = ("<svg xmlns='http://www.w3.org/2000/svg' width='%d' height='%d'><defs>"
           "<polygon id='o' points='%s' fill='none' stroke='white' stroke-opacity='.16' stroke-width='1.5'/>"
           "<polygon id='f' points='%s' fill='white' fill-opacity='.06'/>"
           "<polygon id='t' points='%s' fill='%s' fill-opacity='.55'/>"
           "</defs>%s</svg>") % (W, H, points(R - 1.5), points(R - 7), points(R - 7), TEAL, uses)
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "hero-hexagons.svg"), "w", newline="\n") as f:
        f.write(svg + "\n")
    # Escape everything but a few safe characters - "/" too, so the Sass compiler never sees "//".
    print("data:image/svg+xml," + urllib.parse.quote(svg, safe=" :=.',-()"))


if __name__ == "__main__":
    main()
