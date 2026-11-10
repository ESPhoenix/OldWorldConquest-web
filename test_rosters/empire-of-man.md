# Empire of Man — public list test fixture

> Research/test fixture for the integrated army builder. Selections and points reproduce a public tournament list; they are not a recommendation or official rules ruling.

## Source

- **Event:** [Rock River Ruckus 2026](https://oldworldrankings.com/us/tournaments/rock-river-ruckus-2026) (2026-08-29)
- **Player / placing:** Gary Luther — 2nd place
- **Event limit:** 2000 points; **published list total:** not stated in the list export
- **List record:** [https://oldworldrankings.com/army_lists/115d45f6-0c08-4ae1-a41f-8cfc9e593d9c](https://oldworldrankings.com/army_lists/115d45f6-0c08-4ae1-a41f-8cfc9e593d9c) — marked verified, with no inaccurate-list flag at collection.
- **Matched-play rule for app setup:** `Open War / Standard (test default; source export does not identify the rule)`.

## App construction audit

- **Catalog coverage:** 12/12 published unit entries map to a local faction profile or an allowed mercenary/allied profile.
- **Published unit-point subtotal:** 1999 points from item rows (no list total in the export; event limit is 2000).
- **Build procedure:** choose the faction/composition, select the matched-play rule, set the event points limit, add each mapped profile, then configure the source-listed equipment/options from the roster below.
- **Verification scope:** catalog mapping and published-list point arithmetic were checked against local datasets. No browser automation runtime was available, so interactive selections and the app-calculated total still need hands-on confirmation.
- **Known gaps:** No unmatched unit profiles. Confirm source-listed options are selectable and that the configured app total reproduces the source.

### Catalog selections

| Published entry | Pts | App catalogue selection | Dataset profile | Match |
|---|---:|---|---|---|
| Engineer | 55 | Characters | `empire-of-man/characters:empire-engineer` | Display-Name Variant |
| Grand Master | 310 | Characters | `empire-of-man/characters:grand-master` | Exact name |
| Wizard Lord | 172 | Characters | `empire-of-man/characters:wizard-lord` | Exact name |
| Empire Knights | 205 | Core | `empire-of-man/core:empire-knights` | Exact name |
| Free Company Militia | 60 | Core | `empire-of-man/core:free-company-militia` | Exact name |
| Veteran State Troops | 254 | Core | `empire-of-man/core:veteran-state-troops` | Exact name |
| Demigryph Knights | 238 | Special | `empire-of-man/special:demigryph-knights` | Exact name |
| Great Cannon | 125 | Special | `empire-of-man/special:great-cannon` | Exact name |
| Great Cannon | 125 | Special | `empire-of-man/special:great-cannon` | Exact name |
| Empire Steam Tank | 265 | Rare | `empire-of-man/rare:steam-tank` | Display-Name Variant |
| Empire War Wagons | 140 | Special | `empire-of-man/special:war-wagon` | Plural/Name Variant |
| Doomseeker | 50 | Mercenaries | `dwarfen-mountain-holds/mercenaries:doomseeker-merc` | Exact name |

## Published roster (verbatim)

```text
55 - Engineer, Grenade Launching Blunderbuss
310 - Grand Master, Shield, General, Demigryph, Full Plate Armour, Meteor Hammer, Daemon-Blooded Steed, The White Cloak, Order of the Fiery Heart
172 - Wizard Lord, Empire Warhorse, Wizard Level 3, Elementalism, Lore Familiar
205 - 7 Empire Knights, Lance, Preceptor, Standard Bearer, Monster Hunter's Tapestry, Drilled, Stubborn
60 - 10 Free Company Militia, Detachment
254 - 21 Veteran State Troops, Shield, Halberd, Sergeant, Standard Bearer, Banner of Iron Resolve, Musician
238 - 3 Demigryph Knights, Full Plate Armour, Lance, Demigryph Preceptor, The Silver Horn, Witch Hunter's Ward, Standard Bearer
125 - Great Cannon
125 - Great Cannon
265 - Empire Steam Tank, Engineer Commander
140 - Empire War Wagons
50 - Doomseeker


Created with newrecruit.eu v35.72
```
