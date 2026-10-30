"""Print the profile classes in rainbow order, read from the colours in css/style.css.

The first six links (mail, key, mastodon, bluesky, linkedin, github) stay fixed.
Put the rest in the printed order in index.html.
Sorting idea: https://stackoverflow.com/questions/8915113/sort-hex-colors-to-match-rainbow
"""
import colorsys
import re
from pathlib import Path

FIXED = ["mail", "key", "mastodon", "bluesky", "linkedin", "github"]

css = (Path(__file__).parent.parent / "css" / "style.css").read_text()
colours = dict(re.findall(r"^\.(\w+) \{ --brand: (#[0-9A-Fa-f]{6}); \}$", css, re.M))


def hsv(name):
    hexrgb = colours[name].lstrip("#")
    r, g, b = (int(hexrgb[i:i + 2], 16) / 255 for i in (0, 2, 4))
    return colorsys.rgb_to_hsv(r, g, b)


print(" ".join(FIXED + sorted((n for n in colours if n not in FIXED), key=hsv)))
