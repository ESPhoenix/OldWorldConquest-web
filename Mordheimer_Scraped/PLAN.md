# Mordheimer.net local Markdown archive plan

## Goal

Create a traceable, page-faithful Markdown reference archive from the relevant Mordheimer.net documentation:

- Core rules
- Grade 1A, 1B, and 1C warbands
- Weapons and armour
- Skills (standard skill rules and warband-specific skill information)
- The Campaigns documentation subtree, including campaign settings, scenarios, hired swords, and Dramatis Personae

The plan has been carried out as a local Markdown reference archive. See `README.md` and `manifest.json` for archive status and provenance.

## Important rights and access notes

- `robots.txt` allows general access but sets `use=reference` and `ai-train=no`. Keep any resulting archive for permitted reference use; do not use it for model training.
- Mordheimer's footer says the original content is copyrighted by Games Workshop. Check applicable rights and obtain permission before publishing, sharing, or redistributing a bulk copy. Retain source attribution and links in any permitted copy.
- Respect the site's access rules. Use a descriptive user agent, low request rate, caching, and backoff; do not bypass access controls or scrape unrelated areas.

## Scope and discovery

Use the site's documentation navigation as the authoritative crawl inventory. The initial pages verified are:

- `https://mordheimer.net/docs/rules` — links to the core rules chapters.
- `https://mordheimer.net/docs/warbands` — links to warband group pages.
- `https://mordheimer.net/docs/weapons-armour` — links to the armoury chapters.
- `https://mordheimer.net/docs/campaigns/skills` — standard skill lists and rules.
- `https://mordheimer.net/docs/campaigns` — campaign rules and the nested campaigns navigation.

The sitemap endpoint checked (`/sitemap-index.xml`, and `/sitemap.xml`) did not provide a usable inventory. Instead, collect same-site documentation links from the relevant section pages and Docusaurus sidebar, then filter by the requested routes. Do not rely on a manually maintained list of every warband slug; navigation discovery will accommodate additions and renamed pages.

Include:

1. **Core rules:** the rules overview and all child pages under `/docs/rules/` (Characteristics, The Turn, Recovery Phase, Movement, Shooting, Close Combat, Wounds & Injuries, and Leadership & Psychology). Include `/docs/introduction` only for introductory/core-rule context; keep it clearly labeled as introductory material.
2. **Warbands:** the grade landing pages and every child warband page under `/docs/warbands/grade-1a-warbands/`, `grade-1b-warbands/`, and `grade-1c-warbands/`. Capture each page whole, including source/grade metadata, hiring and roster rules, profiles, equipment lists, skill tables, special rules, and embedded unique skills.
3. **Weapons and armour:** the overview and child pages for close-combat weapons, missile weapons, blackpowder weapons, and armour. Include miscellaneous equipment only if it is needed to preserve the requested weapons/armour references or linked rules; mark it as supplementary. Animal Bestiary is outside the requested core scope and can be omitted initially.
4. **Skills:** the standard skills page at `/docs/campaigns/skills`, including categories, restrictions, and descriptions. Keep warband-specific skill tables and unique skill rules in the corresponding warband page, and link to them from the skills index to avoid creating competing copies.
5. **Campaigns:** include every discoverable page beneath `/docs/campaigns/`, including campaign settings, scenarios, hired swords, and Dramatis Personae. The eight grade filter routes that return only client-side controls are recorded as transparent stubs, not complete rule pages.
6. **Supporting references:** include a linked page only when needed to make an in-scope rule understandable (for example, a relevant rule referenced by a weapon or skill). Record these as supplementary rather than expanding into the entire site.

## Proposed output structure

```text
Mordheimer_Scraped/
├── PLAN.md
├── README.md                 # scope, rights note, how to browse/update
├── manifest.json             # source URL, local path, status, dates, checksum
├── index.md                  # navigation to all captured sections
├── core-rules/
│   ├── index.md
│   ├── introduction.md       # if included
│   └── rules/
│       ├── index.md
│       ├── characteristics.md
│       ├── the-turn.md
│       └── ...
├── warbands/
│   ├── index.md
│   ├── grade-1a/<slug>.md
│   ├── grade-1b/<slug>.md
│   └── grade-1c/<slug>.md
├── weapons-armour/
│   ├── index.md
│   ├── close-combat.md
│   ├── missile.md
│   ├── blackpowder.md
│   └── armour.md
├── skills/
│   ├── index.md
│   └── standard-skills.md
└── campaigns/
    ├── index.md
    ├── campaigns-overview.md
    ├── campaign-settings/...
    ├── hired-swords/...
    ├── dramatis-personae/...
    └── scenarios/...
```

Use stable lowercase, hyphenated filenames based on the source route, not display titles. Keep one Markdown file per source page as the canonical copy. Preserve source page headings and tables; avoid splitting or rewriting rules in the first pass. Add local relative links between files, while retaining the original source URL for verification.

## Efficient collection workflow

1. **Inventory first:** fetch the relevant entry pages above and parse their Docusaurus sidebar/content links. Build a deduplicated allowlist restricted to the requested route prefixes and sections. Save that list to `manifest.json` before downloading page bodies.
2. **Fetch only the allowlist:** use a small script (Python `requests` plus BeautifulSoup and a Markdown converter, or equivalent) to retrieve each HTML page. Extract the documentation article body—not the global header, footer, sidebar, or page chrome—and convert it to Markdown. Keep tables, heading hierarchy, inline emphasis, superscripts/notes, and source links intact.
3. **Be polite and resumable:** run sequentially, wait about one second between requests, retry transient errors with exponential backoff, and stop on rate-limit/access errors. Resume by skipping completed local Markdown files; use the explicit refresh option when intentionally re-fetching. Do not repeatedly fetch the same route.
4. **Record provenance:** add YAML front matter to each saved page with `title`, `source_url`, `fetched_at`, `site_last_updated` (when present), `section`, and `grade`/`source` where relevant. Keep the site's own source citations and PDF links in the body.
5. **Generate navigation:** create section `index.md` files from the manifest, linking to captured local pages and noting intentionally excluded/supplementary material. Skills indexes should point to warband-specific skill content rather than duplicate it.
6. **Cross-link terms:** run `python linkify.py` to link mentions of rule sections, skills, weapons, and armour to their local canonical definitions. This step is local-only and makes no web requests.
7. **Validate:** check that every discovered in-scope URL has exactly one manifest entry and local file; no unrelated route was included; Markdown files are nonempty; tables and links survived conversion; internal links and heading fragments resolve; and a sample from each section matches its source page. Report failed or changed pages for manual review rather than silently omitting them.

## Suggested manifest fields

```json
{
  "source_url": "https://mordheimer.net/docs/...",
  "local_path": "warbands/grade-1a/example.md",
  "section": "warbands",
  "grade": "1a",
  "status": "pending",
  "fetched_at": null,
  "site_last_updated": null,
  "sha256": null,
  "notes": ""
}
```

## Completion criteria

- All links discovered in the 1A/1B/1C sidebars are represented in the manifest and either saved or explicitly marked as unavailable.
- Core rules, armoury chapters, and standard skills are represented with their source metadata.
- Warband-specific skill tables, special skills, and equipment lists remain with their originating warband page.
- The top-level and section indexes make the nested archive browsable, and all local links resolve.
- The README clearly states that this is a sourced reference archive and carries the rights/access warning above.
