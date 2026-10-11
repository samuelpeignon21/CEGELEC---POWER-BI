# Site_Maquette

Unofficial, local **mock-up** of the Cegelec New Caledonia website (cegelec.nc), built as a personal side project: a multi-page static site (home, companies, references, CSR, events, contact…) generated from a single Python script, plus a hidden card-game room.

> **Not affiliated with Cegelec or VINCI Energies. Not an official site.**
> Logos, photos and original texts belong to Cegelec / VINCI Energies. **No image is included in this repository**: `telecharger_assets.py` fetches them from the official website for local viewing only. Do not republish them without the company's agreement.

## Run it locally

```bash
python telecharger_assets.py   # fetches the official images into assets/ (ignored by git)
python build.py                # regenerates the .html pages
# then open index.html in a browser
```

`pip install pillow` is optional: it lets the script trim the white side bars of a few photos.

## Content

| File | Role |
|---|---|
| `build.py` | Page generator: content data (companies, references, history…) and HTML templates |
| `style.css`, `site.js` | Site styles, hero carousel, reference filters |
| `index.html`, `*.html` | Generated pages (committed so the site can be browsed as is once images are downloaded) |
| `cartes.js`, `cartes.css`, `secret.html` | Hidden games room: a small turn-based card game ("Duel des chantiers"), a memory game and a card library |
| `equipe.js`, `objets.js`, `collegues.js` | Card data: **fictional examples only** (jobs and objects, no real people) |
| `telecharger_assets.py` | Downloads the official images locally |

## About the card data

The cards in `equipe.js` and `collegues.js` are placeholders. If you add real colleagues, only do so with their consent and keep their photos in `assets/equipe/`, which is git-ignored on purpose.

## Colors

The game uses colors inspired by the brand logos (Cegelec red, Actemium green, Omexom blue). Axians is shown in violet to tell it apart from Omexom.
