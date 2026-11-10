# Orc & Goblin Tribes — public list test fixture

> Research/test fixture for the integrated army builder. Selections and points reproduce a public tournament list; they are not a recommendation or official rules ruling.

## Source

- **Event:** [Bay Area Open 2026 - The Old World Champs](https://oldworldrankings.com/us/tournaments/bay-area-open-2026-the-old-world-champs) (2026-05-23)
- **Player / placing:** Roland Curtis — 3rd place
- **Event limit:** 2000 points; **published list total:** 2000 points (source total line `2000/2000`)
- **List record:** [https://oldworldrankings.com/army_lists/d5855c91-1e34-4aa5-a9cd-9fa494b0e398](https://oldworldrankings.com/army_lists/d5855c91-1e34-4aa5-a9cd-9fa494b0e398) — marked verified, with no inaccurate-list flag at collection.
- **Matched-play rule for app setup:** `Open War / Standard (test default; source export does not identify the rule)`.

## App construction audit

- **Catalog coverage:** 18/18 published unit entries map to a local faction profile or an allowed mercenary/allied profile.
- **Published unit-point subtotal:** 2000 points (matches the source total line).
- **Build procedure:** choose the faction/composition, select the matched-play rule, set the event points limit, add each mapped profile, then configure the source-listed equipment/options from the roster below.
- **Verification scope:** catalog mapping and published-list point arithmetic were checked against local datasets. No browser automation runtime was available, so interactive selections and the app-calculated total still need hands-on confirmation.
- **Known gaps:** No unmatched unit profiles. Confirm source-listed options are selectable and that the configured app total reproduces the source.

### Catalog selections

| Published entry | Pts | App catalogue selection | Dataset profile | Match |
|---|---:|---|---|---|
| Black Orc Warboss | 339 | Characters | `orc-and-goblin-tribes/characters:black-orc-warboss` | Exact name |
| Night Goblin Bigboss | 55 | Characters | `orc-and-goblin-tribes/characters:night-goblin-bigboss` | Exact name |
| Night Goblin Bigboss | 30 | Characters | `orc-and-goblin-tribes/characters:night-goblin-bigboss` | Exact name |
| Night Goblin Bigboss | 30 | Characters | `orc-and-goblin-tribes/characters:night-goblin-bigboss` | Exact name |
| Night Goblin Oddgit | 90 | Characters | `orc-and-goblin-tribes/characters:night-goblin-oddgit` | Exact name |
| Orc Weirdboy | 65 | Characters | `orc-and-goblin-tribes/characters:orc-weirdboy` | Exact name |
| Orc Weirdboy | 65 | Characters | `orc-and-goblin-tribes/characters:orc-weirdboy` | Exact name |
| Orc Weirdboy | 100 | Characters | `orc-and-goblin-tribes/characters:orc-weirdboy` | Exact name |
| Orc Weirdnob | 170 | Characters | `orc-and-goblin-tribes/characters:orc-weirdnob` | Exact name |
| Black Orc Mobs | 60 | Core | `orc-and-goblin-tribes/core:black-orc-mob-core` | Plural/Name Variant |
| Night Goblin Mobs | 182 | Core | `orc-and-goblin-tribes/core:night-goblin-mob` | Plural/Name Variant |
| Night Goblin Mobs | 182 | Core | `orc-and-goblin-tribes/core:night-goblin-mob` | Plural/Name Variant |
| Night Goblin Mobs | 182 | Core | `orc-and-goblin-tribes/core:night-goblin-mob` | Plural/Name Variant |
| Orc Mobs | 140 | Core | `orc-and-goblin-tribes/core:orc-mob` | Plural/Name Variant |
| Night Goblin Squig Hopper Mobs | 60 | Special | `orc-and-goblin-tribes/special:night-goblin-squig-hopper-mob` | Plural/Name Variant |
| Night Goblin Squig Hopper Mobs | 60 | Special | `orc-and-goblin-tribes/special:night-goblin-squig-hopper-mob` | Plural/Name Variant |
| Doom Diver Catapults | 95 | Rare | `orc-and-goblin-tribes/rare:doom-diver-catapult` | Plural/Name Variant |
| Doom Diver Catapults | 95 | Rare | `orc-and-goblin-tribes/rare:doom-diver-catapult` | Plural/Name Variant |

## Published roster (verbatim)

```text
BAO 2026 BLACK-LITE LASER SHOW! 

Characters
339 - Black Orc Warboss, Great Weapon, General, Wyvern, Trollhide Trousers, Talisman Of Protection
55 - Night Goblin Bigboss, Battle Standard Bearer
30 - Night Goblin Bigboss
30 - Night Goblin Bigboss
90 - Night Goblin Oddgit, Wizard Level 1, Illusion, Staff Of Quietude
65 - Orc Weirdboy, Wizard Level 1, Elementalism
65 - Orc Weirdboy, Wizard Level 1, Elementalism
100 - Orc Weirdboy, Wizard Level 1, Elementalism, Glowy Green Amulet
170 - Orc Weirdnob, Wizard Level 3, Elementalism, Lore Familiar

Core
60- 5 Black Orc Mobs 
  • 1x Black Orc, Boss 
  • 1x Black Orc, Musician 
  • 3x Black Orc
182 - 30 Night Goblin Mobs 
  • 30x Night Goblin, Shield 
  • 3x Fanatic, Boss, Standard Bearer, Musician
182 - 30 Night Goblin Mobs 
  • 30x Night Goblin, Shield 
  • 3x Fanatic, Boss, Standard Bearer, Musician
182 - 30 Night Goblin Mobs 
  • 30x Night Goblin, Shield 
  • 3x Fanatic, Boss, Standard Bearer, Musician
140 - 18 Orc Mobs, Warbow, Light Armour, Shield, Skirmishers, Boss, Da Thinkin’ Orc’s ’At

Special
60 - 5 Night Goblin Squig Hopper Mobs
60 - 5 Night Goblin Squig Hopper Mobs

Rare
95 - Doom Diver Catapults
95 - Doom Diver Catapults

2000/2000
Total Drops: 9
German Comp
```
