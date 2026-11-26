# The Plastering and Rendering Group – website demo

Static preview of the site, built from the 23 Oct 2026 website brief and the 12 Nov 2026 meeting notes.
All images are placeholders, and anything in [SQUARE BRACKETS] is still to be supplied by the client.

## Pages

- `index.html` – home
- 15 service pages, one per service, linked from the Services dropdown:
  - External rendering: `lime-render`, `k-rend`, `monocouche-render`, `sand-and-cement-render`, `stone-render`
  - Internal plastering & drylining: `internal-plastering`, `metal-stud-work`, `ceilings`, `insulation`, `fire-lining`, `sound-boarding`, `moisture-resistant-boarding`
  - Decorative finishes: `microcement`, `venetian-plaster`, `marble-plaster`
- `jobs.html` – Jobs we're proud of (before-and-after sliders, filterable by service)
- `reviews.html` – testimonials and Google reviews

## Single-page mode

While content for the other pages is being gathered, `SHOW_SUBPAGES = False` in `src/content.py` keeps the site to the home page: the menus jump to home-page sections and nothing links to the service, Jobs or Reviews pages (they are still built). Set it to `True` and rebuild to link them again.

## Editing

- Page text: `src/content.py`
- Page layout and shared header/footer/quote form: `src/build.py`
- Styles: `assets/site.css`
- Menus, carousels, sliders and form: `assets/site.js`

After changing anything in `src/`, rebuild the pages from the repo root:

```
python3 src/build.py
```
