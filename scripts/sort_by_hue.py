"""Print all profile classes in rainbow order, read from the colours in css/style.css.

Put the links in index.html in the printed order.

How it sorts:
- Near-black colours (GitHub, X, DEV) go last, because they have no hue.
- Hue is cut into 20 degree bands, so similar colours stay together. Pink counts as
  "before red", so it sits next to the reds and not at the far end.
- Inside a band, brightness runs up in one band and down in the next, so the
  brightness does not jump back at every band edge.
Idea: https://stackoverflow.com/questions/8915113/sort-hex-colors-to-match-rainbow
"""
import colorsys
import re
from pathlib import Path

BAND = 20
NEAR_BLACK = 0.15

css = (Path(__file__).parent.parent / "css" / "style.css").read_text()
colours = dict(re.findall(r"^\.(\w+) \{ --brand: (#[0-9A-Fa-f]{6}); \}$", css, re.M))


def sort_key(name):
    hexrgb = colours[name].lstrip("#")
    r, g, b = (int(hexrgb[i:i + 2], 16) / 255 for i in (0, 2, 4))
    hue, _, value = colorsys.rgb_to_hsv(r, g, b)
    if value < NEAR_BLACK:
        return (1, 0, value)
    degrees = hue * 360
    if degrees > 320:  # pink belongs before red
        degrees -= 360
    band = int(degrees // BAND)
    return (0, band, value if band % 2 == 0 else -value)


print(" ".join(sorted(colours, key=sort_key)))
