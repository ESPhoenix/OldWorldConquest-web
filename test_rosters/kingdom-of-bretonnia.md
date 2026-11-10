# Kingdom of Bretonnia — public list test fixture

> Research/test fixture for the integrated army builder. Selections and points reproduce a public tournament list; they are not a recommendation or official rules ruling.

## Source

- **Event:** [Conflict Events Presents! Eternal Glory V - January (Square Based Comp)](https://oldworldrankings.com/uk/tournaments/conflict-events-presents-eternal-glory-v-january-square-based-comp) (2026-01-17)
- **Player / placing:** Reece White — 2nd place
- **Event limit:** 2500 points; **published list total:** not stated in the list export
- **List record:** [https://oldworldrankings.com/army_lists/0147673b-2561-44e9-a5f6-34e96b0b9c65](https://oldworldrankings.com/army_lists/0147673b-2561-44e9-a5f6-34e96b0b9c65) — marked verified, with no inaccurate-list flag at collection.
- **Matched-play rule for app setup:** `Open War / Standard (test default; source export does not identify the rule)`.

## App construction audit

- **Catalog coverage:** 8/8 published unit entries map to a local faction profile or an allowed mercenary/allied profile.
- **Published unit-point subtotal:** 2000 points from item rows (no list total in the export; event limit is 2500).
- **Build procedure:** choose the faction/composition, select the matched-play rule, set the event points limit, add each mapped profile, then configure the source-listed equipment/options from the roster below.
- **Verification scope:** catalog mapping and published-list point arithmetic were checked against local datasets. No browser automation runtime was available, so interactive selections and the app-calculated total still need hands-on confirmation.
- **Known gaps:** No unmatched unit profiles. Confirm source-listed options are selectable and that the configured app total reproduces the source.

### Catalog selections

| Published entry | Pts | App catalogue selection | Dataset profile | Match |
|---|---:|---|---|---|
| Lady Élisse Duchaard | 225 | Characters | `kingdom-of-bretonnia/characters:lady-élisse-duachaard` | Exact name |
| Duke | 358 | Characters | `kingdom-of-bretonnia/characters:duke` | Exact name |
| Prophetess | 251 | Characters | `kingdom-of-bretonnia/characters:prophetess` | Exact name |
| Men-At-Arms | 104 | Core | `kingdom-of-bretonnia/core:men-at-arms` | Exact name |
| Mounted Knights of the Realm | 310 | Core | `kingdom-of-bretonnia/core:mounted-knights-of-the-realm` | Exact name |
| Mounted Knights of the Realm | 120 | Core | `kingdom-of-bretonnia/core:mounted-knights-of-the-realm` | Exact name |
| Pegasus Knights | 184 | Special | `kingdom-of-bretonnia/special:pegasus-knights` | Exact name |
| Grail Knights | 448 | Rare | `kingdom-of-bretonnia/rare:grail-knights` | Exact name |

## Published roster (verbatim)

```text
225 - Lady Élisse Duchaard
358 - Duke, Shield, Virtue of Knightly Temper, General, Bretonnian Warhorse, Cackling Blade, Potion Of Fervour
251 - Prophetess, Bretonnian Warhorse, Wizard Level 3, Illusion, Meteor Hammer, Power Scroll, Lore Familiar
104 - 20 Men-At-Arms, Yeoman, Grail Monk, Standard Bearer, Musician
310 - 11 Mounted Knights of the Realm, The Knight's Vow, First Knight, Standard Bearer, Monster Hunter's Tapestry, Musician
120 - 5 Mounted Knights of the Realm, The Knight's Vow
184 - 3 Pegasus Knights, The Knight's Vow, Musician
448 - 8 Grail Knights, Grail Guardian, Virtue of The Impetuous Knight, Falcon-horn of Fredemund, Standard Bearer, Totem Of Wrath
```
