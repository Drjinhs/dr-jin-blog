# Dr. Jin Blog

Static personal website and blog for Dr. Jin, focused on open innovation, startup globalization, international trade, and NextRise.

## Source and implementation

The requested Lovable preview was inspected on 12 July 2026 but redirected to workspace authentication. The accessible brief and five supplied portraits were therefore used as the authoritative fallback reference. All images are stored locally; the site contains no hotlinked media.

The implementation uses semantic HTML5, modular CSS, vanilla JavaScript, and SVG/CSS-generated graphic motifs. It has no production build step or client framework.

## Structure

- `index.html`: semantic page content, metadata, social cards, and JSON-LD
- `assets/css/`: reset, design tokens, primary styling, and responsive rules
- `assets/js/`: navigation, mobile menu, active sections, and reveal animations
- `assets/images/`: locally stored supplied portraits and illustrations
- `analysis/`: source-access record and reconstructed structure/style/interaction notes
- `tests/`: Playwright smoke, navigation, responsive, link, and visual tests
- `.github/workflows/deploy-pages.yml`: GitHub Pages deployment

## Run locally

```bash
python -m http.server 4173
```

Open `http://127.0.0.1:4173/`.

## Test

With Node.js and Playwright installed:

```bash
npm install
npx playwright install chromium
npm test
```

## Update content

Edit visible text in `index.html`. Replace images in `assets/images/` while preserving filenames or update the corresponding paths and dimensions. Menu labels and destinations are in the header and mobile navigation in `index.html`.

## Deployment

Push `main` to GitHub and set Pages source to GitHub Actions. The included workflow publishes the repository root.

## Content and image sources

The personal images were supplied directly with the project brief and are represented as official photos/illustrations of Dr. Jin. NextRise facts and the external link use the public NextRise website. Placeholder email and canonical account values should be replaced when confirmed.

## License

Copyright © 2026 Dr. Jin. All rights reserved.
