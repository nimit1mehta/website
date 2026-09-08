# TopQuadrant website concepts

Design concepts for the TopQuadrant site. **These do not touch the live Webflow
site** and share no markup with it.

| Page | URL |
|---|---|
| Homepage redesign | https://nimit1mehta.github.io/website/ |
| TQ Data Foundation product page | https://nimit1mehta.github.io/website/product/ |

Both are marked `noindex` — reachable by link, kept out of search.

## What these are

Each page is a single self-contained HTML file: CSS, JS, fonts and every image are
embedded, so there are no external requests and nothing to install. Open the file
and it renders.

## Editing

Pages are assembled from panel modules, one per section, in `src/`. Each module
holds its own markup, copy, CSS and JS.

```bash
cd src

# homepage  -> index.html
python3 build_home.py
python3 inline_build.py home_restructured.html ../index.html

# product page -> product/index.html
python3 build_page.py
python3 inline_build.py restructured.html ../product/index.html
```

Reorder or drop sections by editing `MANIFEST` at the top of either build script.
Change one section by editing only its module.

`src/panels/base.py` holds the design tokens and `src/panels/arch.py` the layered
architecture graphic, shared by both pages.

Two build inputs are not committed because they are large and re-derivable: the
saved Webflow assets folder (Chrome → Save as → "Webpage, Complete") and the
webfonts (`npm pack @fontsource/hanken-grotesk @fontsource/inter
@fontsource/jetbrains-mono`). Paths are set at the top of `inline_build.py`.

## Note on figures

The impact numbers on both pages are placeholders, not measured results.
