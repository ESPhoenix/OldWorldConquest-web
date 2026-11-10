# Dark Elves — public list test fixture

> Research/test fixture for the integrated army builder. Selections and points reproduce a public tournament list; they are not a recommendation or official rules ruling.

## Source

- **Event:** [2. Wiener Würfel Wappler Watschenfest](https://oldworldrankings.com/at/tournaments/2-wiener-wurfel-wappler-watschenfest) (2026-03-07)
- **Player / placing:** Lorenz — 2nd place
- **Event limit:** 2000 points; **published list total:** not stated in the list export
- **List record:** [https://oldworldrankings.com/army_lists/22760d34-a667-49aa-8cd1-aa8c95f1380f](https://oldworldrankings.com/army_lists/22760d34-a667-49aa-8cd1-aa8c95f1380f) — marked verified, with no inaccurate-list flag at collection.
- **Matched-play rule for app setup:** `Open War / Standard (test default; source export does not identify the rule)`.

## App construction audit

- **Catalog coverage:** 12/12 published unit entries map to a local faction profile or an allowed mercenary/allied profile.
- **Published unit-point subtotal:** 2000 points from item rows (no list total in the export; event limit is 2000).
- **Build procedure:** choose the faction/composition, select the matched-play rule, set the event points limit, add each mapped profile, then configure the source-listed equipment/options from the roster below.
- **Verification scope:** catalog mapping and published-list point arithmetic were checked against local datasets. No browser automation runtime was available, so interactive selections and the app-calculated total still need hands-on confirmation.
- **Known gaps:** No unmatched unit profiles. Confirm source-listed options are selectable and that the configured app total reproduces the source.

### Catalog selections

| Published entry | Pts | App catalogue selection | Dataset profile | Match |
|---|---:|---|---|---|
| Dark Elf Dreadlord | 375 | Characters | `dark-elves/characters:dark-elf-dreadlord` | Exact name |
| Death Hag | 155 | Characters | `dark-elves/characters:death-hag` | Exact name |
| Supreme Sorceress | 280 | Characters | `dark-elves/characters:supreme-sorceress` | Exact name |
| Dark Riders | 108 | Core | `dark-elves/core:dark-riders` | Exact name |
| Dark Riders | 108 | Core | `dark-elves/core:dark-riders` | Exact name |
| Witch Elves | 288 | Core | `dark-elves/core:witch-elves-core` | Exact name |
| Cold One Chariots | 125 | Special | `dark-elves/special:cold-one-chariots` | Plural/Name Variant |
| Scourgerunner Chariots | 85 | Special | `dark-elves/special:scourgerunner-chariots` | Exact name |
| Scourgerunner Chariots | 85 | Special | `dark-elves/special:scourgerunner-chariots` | Exact name |
| Doomfire Warlocks | 116 | Rare | `dark-elves/rare:doomfire-warlocks` | Exact name |
| Kharibdyss | 195 | Special | `dark-elves/special:kharibdyss-special` | Exact name |
| Reaper Bolt Thrower | 80 | Rare | `dark-elves/rare:reaper-bolt-throwers` | Exact name |

## Published roster (verbatim)

```text
375 - Dark Elf Dreadlord, Repeater Handbow, Full Plate Armour, Sea Dragon Cloak, General, Manticore, Executioner’s Axe, Talisman Of Protection
155 - Death Hag, Rune of Khaine, Ogre Blade
280 - Supreme Sorceress, Dark Pegasus, Wizard Level 4, Battle Magic, Lore Familiar, Ruby Ring of Ruin
108 - 6 Dark Riders, Repeater Crossbow
108 - 6 Dark Riders, Repeater Crossbow
288 - 22 Witch Elves, Hag, Standard Bearer, Banner Of Har Ganeth, Musician
125 - Cold One Chariots
85 - Scourgerunner Chariots
85 - Scourgerunner Chariots
116 - 5 Doomfire Warlocks, Master
195 - Kharibdyss
80 - Reaper Bolt Thrower
```
