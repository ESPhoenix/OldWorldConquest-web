# Old World Conquest Web

This repository contains a static roster and campaign tracker. The build copies the app and the Old World Builder catalogue files it loads at runtime into `dist/`; no server-side runtime is required.

## Deploy to Cloudflare Pages

Cloudflare Pages can build and publish this site directly from GitHub:

1. Push the website files to the GitHub branch you want to publish.
2. In Cloudflare, open **Workers & Pages → Create application → Pages → Connect to Git** and select `ESPhoenix/OldWorldConquest-web`.
3. Select `main` as the production branch and configure:
   - Build command: `npm run build`
   - Build output directory: `dist`
   - Root directory: `/` (repository root)
4. Choose **Save and Deploy**. Cloudflare will build and publish each new push to `main`.

## Local build

Run `npm run build`. The deployable static site is written to `dist/`.
