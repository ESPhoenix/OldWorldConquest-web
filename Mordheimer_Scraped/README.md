# Mordheimer offline reference archive

This folder contains a locally generated Markdown reference archive of the scoped documentation, with source URLs and fetch dates recorded per page. The site footer identifies the original material as copyrighted by Games Workshop. This archive is intended for your offline reference; do not redistribute it without permission or another clear legal basis. Do not use the material for AI training; the site's `robots.txt` sets `ai-train=no`.

Start at [index.md](index.md). The [manifest](manifest.json) records source URLs, local paths, status, fetch dates, and checksums. Each page preserves its source URL and relevant site update metadata.

The Campaigns archive follows all discoverable links beneath `/docs/campaigns/` and is browsable from [campaigns/index.md](campaigns/index.md). Eight hired-sword/Dramatis Personae grade routes render only a client-side filter in the HTML response; those local pages are transparent stubs linking to available category material rather than invented rule text.

## Updating this archive

Install the small Python dependencies with `python -m pip install -r requirements.txt`. To refresh the original rules/warband/armoury pages, run `python scrape.py --refresh`. To discover and add all campaign pages, run `python scrape_campaigns.py`. After either scrape, run `python linkify.py` to rebuild local cross-links. To resume an interrupted download, rerun the corresponding scraper and then `python linkify.py`. The downloaders verify `robots.txt`, use a low request rate, and stop on rate limiting or access errors; `linkify.py` works locally without web requests.
