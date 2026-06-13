# Hospital in a Box

A premium, mobile-first, **offline-capable** wellness reference app — a single static
`index.html` single-page app (no backend, no build step required to run).

It combines:

- **25 Ayurvedic remedies** — verified against the source "Hospital in a Box" documents,
  with ingredients, illustrated preparation steps, dosage/frequency and warnings.
- **718 unique Quantum / Divine Healing Codes** (920 cross-referenced listings) across
  **25 categories**, transcribed verbatim from the source compiled by Marc Gamma,
  Isabel Henn and "Reiki Doc."
- A **28-herb library** and a **26-entry active-compounds** database.
- **Emergency guidance** with standard first-aid steps, always one tap away.

## Important

This is a **spiritual / wellness belief practice**. It is **not medicine**, has **no
scientific proof**, and **cannot diagnose, treat, cure or prevent any disease**. It must
**never** replace professional medical or veterinary care or prescribed treatment. In an
emergency, call your local emergency number first. A first-run safety notice must be
acknowledged before the app is used.

## Experience

- **Search-first** home, quick actions, recently viewed, popular remedies
- Progressive disclosure: summary → details → advanced, never a wall of text
- Tap-to-copy codes (spaces preserved), favorites, fullscreen code mode, share
- Persistent emergency button on every screen
- Installable PWA with an offline service worker

## Architecture

- `index.html` — the entire app (HTML + CSS + JS + embedded data)
- `manifest.webmanifest`, `sw.js`, `icon-*.png` — PWA assets
- `app_template.html` + `build_data.py` + `v3data.json` — source template and the
  data-build step used to (re)generate `index.html`:
  `python3 -c "open('index.html','w').write(open('app_template.html').read().replace('__DATA__',open('v3data.json').read(),1))"`

## Hosting on GitHub Pages

Settings → Pages → Deploy from a branch → `main` / root. Served at
`https://<user>.github.io/<repo>/`.
