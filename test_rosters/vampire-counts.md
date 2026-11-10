# Vampire Counts — public list test fixture

> Research/test fixture for the integrated army builder. Selections and points reproduce a public tournament list; they are not a recommendation or official rules ruling.

## Source

- **Event:** [The Old World @ LGT](https://oldworldrankings.com/uk/tournaments/the-old-world-lgt) (2026-09-26)
- **Player / placing:** Sergey Kovrov — 4th place
- **Event limit:** 2000 points; **published list total:** not stated in the list export
- **List record:** [https://oldworldrankings.com/army_lists/42f83d82-990b-4530-ac76-4eaf6a2c0dab](https://oldworldrankings.com/army_lists/42f83d82-990b-4530-ac76-4eaf6a2c0dab) — marked verified, with no inaccurate-list flag at collection.
- **Matched-play rule for app setup:** `Open War / Standard (test default; source export does not identify the rule)`.

## App construction audit

- **Catalog coverage:** 13/13 published unit entries map to a local faction profile or an allowed mercenary/allied profile.
- **Published unit-point subtotal:** 2000 points from item rows (no list total in the export; event limit is 2000).
- **Build procedure:** choose the faction/composition, select the matched-play rule, set the event points limit, add each mapped profile, then configure the source-listed equipment/options from the roster below.
- **Verification scope:** catalog mapping and published-list point arithmetic were checked against local datasets. No browser automation runtime was available, so interactive selections and the app-calculated total still need hands-on confirmation.
- **Known gaps:** No unmatched unit profiles. Confirm source-listed options are selectable and that the configured app total reproduces the source.

### Catalog selections

| Published entry | Pts | App catalogue selection | Dataset profile | Match |
|---|---:|---|---|---|
| Master Necromancer | 405 | Characters | `vampire-counts/characters:master-necromancer` | Exact name |
| Master Necromancer | 255 | Characters | `vampire-counts/characters:master-necromancer` | Exact name |
| Wight Lord | 110 | Characters | `vampire-counts/characters:wight-lord` | Exact name |
| Necromantic Acolyte | 90 | Characters | `vampire-counts/characters:necromantic-acolyte` | Exact name |
| Tomb Banshee | 90 | Characters | `vampire-counts/characters:tomb-banshee` | Exact name |
| Cairn Wraith | 50 | Characters | `vampire-counts/characters:cairn-wraith` | Exact name |
| Grave Guard | 412 | Core | `vampire-counts/core:grave-guard-core` | Exact name |
| Zombies | 60 | Core | `vampire-counts/core:zombies` | Exact name |
| Zombies | 60 | Core | `vampire-counts/core:zombies` | Exact name |
| Fell Bats | 45 | Special | `vampire-counts/special:fell-bats` | Exact name |
| Fell Bats | 45 | Special | `vampire-counts/special:fell-bats` | Exact name |
| Hexwraiths | 186 | Rare | `vampire-counts/rare:hexwraiths` | Exact name |
| Hexwraiths | 192 | Rare | `vampire-counts/rare:hexwraiths` | Exact name |

## Published roster (verbatim)

```text
405 - Master Necromancer, General, Mortis Engine, Wizard Level 3, Necromancy, Spell Familiar, Sceptre Of De Noirot, Talisman Of Protection
255 - Master Necromancer, Wizard Level 4, Illusion, Meteor Hammer, Spell Familiar, Tome Of Spellcraft
110 - Wight Lord, Battle Standard Bearer, Charmed Shield, Helm Of Commandment
90 - Necromantic Acolyte, Wizard Level 2, Necromancy
90 - Tomb Banshee
50 - Cairn Wraith

412 - 25 Grave Guard, Great Weapon, Drilled, Seneschal, Standard Bearer, Drakenhof Banner
60 - 20 Zombies
60 - 20 Zombies

45 - 3 Fell Bats
45 - 3 Fell Bats

186 - 6 Hexwraiths
192 - 6 Hexwraiths, Hellwraith


Created with newrecruit.eu v35.80
```
