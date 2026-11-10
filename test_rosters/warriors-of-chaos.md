# Warriors of Chaos — public list test fixture

> Research/test fixture for the integrated army builder. Selections and points reproduce a public tournament list; they are not a recommendation or official rules ruling.

## Source

- **Event:** [Rock River Ruckus 2026](https://oldworldrankings.com/us/tournaments/rock-river-ruckus-2026) (2026-08-29)
- **Player / placing:** John Russell — 1st place
- **Event limit:** 2000 points; **published list total:** not stated in the list export
- **List record:** [https://oldworldrankings.com/army_lists/be7b8c65-6a16-4f87-91f8-e50bf46ad2a8](https://oldworldrankings.com/army_lists/be7b8c65-6a16-4f87-91f8-e50bf46ad2a8) — marked verified, with no inaccurate-list flag at collection.
- **Matched-play rule for app setup:** `Open War / Standard (test default; source export does not identify the rule)`.

## App construction audit

- **Catalog coverage:** 8/8 published unit entries map to a local faction profile or an allowed mercenary/allied profile.
- **Published unit-point subtotal:** 2000 points from item rows (no list total in the export; event limit is 2000).
- **Build procedure:** choose the faction/composition, select the matched-play rule, set the event points limit, add each mapped profile, then configure the source-listed equipment/options from the roster below.
- **Verification scope:** catalog mapping and published-list point arithmetic were checked against local datasets. No browser automation runtime was available, so interactive selections and the app-calculated total still need hands-on confirmation.
- **Known gaps:** No unmatched unit profiles. Confirm source-listed options are selectable and that the configured app total reproduces the source.

### Catalog selections

| Published entry | Pts | App catalogue selection | Dataset profile | Match |
|---|---:|---|---|---|
| Chaos Lord | 327 | Characters | `warriors-of-chaos/characters:chaos-lord` | Exact name |
| Exalted Champion | 262 | Characters | `warriors-of-chaos/characters:exalted-champion` | Exact name |
| Chaos Warriors | 315 | Core | `warriors-of-chaos/core:chaos-warriors` | Exact name |
| Marauder Horsemen | 112 | Core | `warriors-of-chaos/core:marauder-horsemen` | Exact name |
| Marauder Horsemen | 97 | Core | `warriors-of-chaos/core:marauder-horsemen` | Exact name |
| Chaos Chariots | 110 | Core | `warriors-of-chaos/core:chaos-chariot` | Plural/Name Variant |
| Chosen Chaos Knights | 372 | Special | `warriors-of-chaos/special:chosen-chaos-knights` | Exact name |
| Warpfire Dragons | 405 | Rare | `warriors-of-chaos/rare:warpfire-dragon` | Plural/Name Variant |

## Published roster (verbatim)

```text
327 - Chaos Lord, Shield, Mark of Chaos Undivided, General, Daemonic Mount, Ogre Blade, Favour of the Gods, Daemon-Blooded Steed
262 - Exalted Champion, Shield, Mark of Chaos Undivided, Battle Standard Bearer, Daemonic Mount, Demonsword
315 - 17 Chaos Warriors, Halberd, Shield, Mark of Chaos Undivided, Enhanced Reflexes, Champion, Standard Bearer, Monster Hunter's Tapestry, Musician
112 - 7 Marauder Horsemen, Cavalry Spear, Ambushers, Unnatural Fortitude, Marauder Horsemaster
97 - 6 Marauder Horsemen, Cavalry Spear, Ambushers, Unnatural Fortitude, Marauder Horsemaster
110 - Chaos Chariots, Mark of Chaos Undivided
372 - 7 Chosen Chaos Knights, Lance, Full Plate Armour, Drilled, Mark of Chaos Undivided, Champion, Standard Bearer, Totem Of Wrath, Musician
405 - Warpfire Dragons, Wizard Level 1, Battle Magic


Created with newrecruit.eu v35.72
```
