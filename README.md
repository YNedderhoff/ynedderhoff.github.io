[![Check](https://github.com/YNedderhoff/ynedderhoff.github.io/actions/workflows/master-build.yml/badge.svg)](https://github.com/YNedderhoff/ynedderhoff.github.io/actions/workflows/master-build.yml)

Source of [nedderhoff.xyz](https://nedderhoff.xyz/), served by GitHub Pages. Plain HTML and one CSS file: no build step, no JavaScript, no third-party requests.

## Preview locally

```bash
python3 -m http.server 8000
```

Then open <http://localhost:8000/>.

## How it is put together

| Part | Where | Notes |
|---|---|---|
| Pages | `index.html`, `impressum/`, `datenschutzerklaerung/` | The legal pages are German and `noindex`. |
| Styles | `css/style.css` | Light and dark mode via `light-dark()`. Brand colours are custom properties per link class. |
| Font | `fonts/raleway-var-latin.woff2` | Raleway variable font, weights 300 to 600, latin subset. Licence: `fonts/OFL.txt`. |
| Icons | inline SVG in `index.html` | [Font Awesome Free](https://fontawesome.com) 7, CC BY 4.0. Logos belong to their owners. |
| Avatar | `images/profile-144.jpg` | Resized from `images/profile.jpg`, which stays as the Open Graph image. |

## Changing the profile links

Each link is a `<li>` with the classes `p <name>`. The first six are fixed. The rest are ordered by hue of their brand colour: after adding a link and its colour in `css/style.css`, run `python3 scripts/sort_by_hue.py` and put the links in `index.html` in the order it prints. The glyph is white. Add `dark` only when white gives less than 3:1 on the brand colour (WCAG 1.4.11).

The grid has 6 columns on phones and 8 on wider screens, so 24 links fill every row. With another number of links the last row is shorter.

To add an icon, copy the `<path>` and `viewBox` from the `svgs/` folder of the `@fortawesome/fontawesome-free` npm package.

## Checks

Pull requests and pushes to `master` validate the HTML with the [Nu HTML checker](https://validator.github.io/validator/) via `html5validator-action`. The CSS check is off because that validator does not know modern CSS. Pull requests also get an HTML preview comment.
