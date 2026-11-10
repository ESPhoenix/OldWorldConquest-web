# Ogre Kingdoms — public list test fixture

> Research/test fixture for the integrated army builder. Selections and points reproduce a public tournament list; they are not a recommendation or official rules ruling.

## Source

- **Event:** [IWC Presents: Nurgles Carnevil 2k Warhammer Old World Adepticon Primer](https://oldworldrankings.com/us/tournaments/iwc-presents-nurgles-carnevil-2k-warhammer-old-world-adepticon-primer) (2026-02-28)
- **Player / placing:** Walter Sobchak — 6th place
- **Event limit:** 2000 points; **published list total:** not stated in the list export
- **List record:** [https://oldworldrankings.com/army_lists/f3428765-41aa-4495-bd6b-c3a244cc20e2](https://oldworldrankings.com/army_lists/f3428765-41aa-4495-bd6b-c3a244cc20e2) — marked verified, with no inaccurate-list flag at collection.
- **Matched-play rule for app setup:** `Open War / Standard (test default; source export does not identify the rule)`.

## App construction audit

- **Catalog coverage:** 11/11 published unit entries map to a local faction profile or an allowed mercenary/allied profile.
- **Published unit-point subtotal:** 1998 points from item rows (no list total in the export; event limit is 2000).
- **Build procedure:** choose the faction/composition, select the matched-play rule, set the event points limit, add each mapped profile, then configure the source-listed equipment/options from the roster below.
- **Verification scope:** catalog mapping and published-list point arithmetic were checked against local datasets. No browser automation runtime was available, so interactive selections and the app-calculated total still need hands-on confirmation.
- **Known gaps:** No unmatched unit profiles. Confirm source-listed options are selectable and that the configured app total reproduces the source.

### Catalog selections

| Published entry | Pts | App catalogue selection | Dataset profile | Match |
|---|---:|---|---|---|
| Slaughtermaster | 355 | Characters | `ogre-kingdoms/characters:slaughtermaster` | Exact name |
| Tyrant | 455 | Characters | `ogre-kingdoms/characters:tyrant` | Exact name |
| Gnoblar Fighters | 40 | Core | `ogre-kingdoms/core:gnoblar-fighters` | Exact name |
| Ironguts | 327 | Core | `ogre-kingdoms/core:ironguts` | Exact name |
| Ogre Bulls | 152 | Core | `ogre-kingdoms/core:ogre-bulls` | Exact name |
| Sabretusk Packs | 34 | Core | `ogre-kingdoms/core:sabretusk-packs` | Plural/Name Variant |
| Sabretusk Packs | 34 | Core | `ogre-kingdoms/core:sabretusk-packs` | Plural/Name Variant |
| Sabretusk Packs | 34 | Core | `ogre-kingdoms/core:sabretusk-packs` | Plural/Name Variant |
| Sabretusk Packs | 34 | Core | `ogre-kingdoms/core:sabretusk-packs` | Plural/Name Variant |
| Ironblaster | 185 | Special | `ogre-kingdoms/special:ironblaster` | Exact name |
| Mournfang Cavalry | 348 | Special | `ogre-kingdoms/special:mournfang-cavalry` | Exact name |

## Published roster (verbatim)

```text
355 - Slaughtermaster, Butcher's Cauldron, Wizard Level 4, Elementalism, Sword of Might, Grut’s Sickle
455 - Tyrant, Light Armour, Beastkiller, General, Thundertusk, Tenderiser, Talisman Of Protection
40 - 20 Gnoblar Fighters
327 - 6 Ironguts, Veteran, Gutlord, Fistful Of Laurels, Standard Bearer, Dragonhide Banner, Musician
152 - 4 Ogre Bulls, Ironfist, Standard Bearer, Magic Standard, Musician
34 - 2 Sabretusk Packs
34 - 2 Sabretusk Packs
34 - 2 Sabretusk Packs
34 - 2 Sabretusk Packs
185 - Ironblaster
348 - 4 Mournfang Cavalry, Great Weapon, Heavy Armour, Standard Bearer, Totem Of Wrath, Musician
```
