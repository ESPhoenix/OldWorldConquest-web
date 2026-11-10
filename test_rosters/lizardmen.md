# Lizardmen — public list test fixture

> Research/test fixture for the integrated army builder. Selections and points reproduce a public tournament list; they are not a recommendation or official rules ruling.

## Source

- **Event:** [Sunday Old World Singles by East Warrington Gaming](https://oldworldrankings.com/uk/tournaments/sunday-old-world-singles-by-east-warrington-gaming) (2026-03-29)
- **Player / placing:** David González — 3rd place
- **Event limit:** 2000 points; **published list total:** not stated in the list export
- **List record:** [https://oldworldrankings.com/army_lists/c64b2500-3c57-4edf-a0d9-60514867e72e](https://oldworldrankings.com/army_lists/c64b2500-3c57-4edf-a0d9-60514867e72e) — marked verified, with no inaccurate-list flag at collection.
- **Matched-play rule for app setup:** `Open War / Standard (test default; source export does not identify the rule)`.

## App construction audit

- **Catalog coverage:** 11/11 published unit entries map to a local faction profile or an allowed mercenary/allied profile.
- **Published unit-point subtotal:** 2000 points from item rows (no list total in the export; event limit is 2000).
- **Build procedure:** choose the faction/composition, select the matched-play rule, set the event points limit, add each mapped profile, then configure the source-listed equipment/options from the roster below.
- **Verification scope:** catalog mapping and published-list point arithmetic were checked against local datasets. No browser automation runtime was available, so interactive selections and the app-calculated total still need hands-on confirmation.
- **Known gaps:** No unmatched unit profiles. Confirm source-listed options are selectable and that the configured app total reproduces the source.

### Catalog selections

| Published entry | Pts | App catalogue selection | Dataset profile | Match |
|---|---:|---|---|---|
| Saurus Oldblood | 255 | Characters | `lizardmen/characters:saurus-oldblood` | Exact name |
| Saurus Scar-Veteran | 178 | Characters | `lizardmen/characters:saurus-scar-veteran` | Exact name |
| Skink Chief | 80 | Characters | `lizardmen/characters:skink-chief` | Exact name |
| Skink Priest | 95 | Characters | `lizardmen/characters:skink-priest` | Exact name |
| Saurus Warriors | 286 | Core | `lizardmen/core:saurus-warrior` | Exact name |
| Saurus Warriors | 229 | Core | `lizardmen/core:saurus-warrior` | Exact name |
| Skink Skirmishers | 85 | Core | `lizardmen/core:skink-skirmishers` | Exact name |
| Skink Skirmishers | 85 | Core | `lizardmen/core:skink-skirmishers` | Exact name |
| Bastiladon | 175 | Special | `lizardmen/special:bastiladon` | Exact name |
| Bastiladon | 175 | Special | `lizardmen/special:bastiladon` | Exact name |
| Cold One Riders | 357 | Special | `lizardmen/special:cold-one-riders` | Exact name |

## Published roster (verbatim)

```text
255 - Saurus Oldblood, Shield, General, Cold One, Blade Of Revered Tzunki, Talisman Of Protection
178 - Saurus Scar-Veteran, Additional Hand Weapon, Battle Standard Bearer, Razor Standard, Charmed Shield, Venom Of The Firefly Frog
80 - Skink Chief, Sword Of Sorrow, Charmed Shield
95 - Skink Priest, Wizard Level 1, Battle Magic, Ruby Ring of Ruin
286 - 18 Saurus Warriors, Spawn Leader, Biting Blade, Charmed Shield, Standard Bearer
229 - 15 Saurus Warriors, Spawn Leader, Charmed Shield, Standard Bearer
85 - 15 Skink Skirmishers, Javelins and Shields, Vanguard, Patrol Leader
85 - 15 Skink Skirmishers, Javelins and Shields, Vanguard, Patrol Leader
175 - Bastiladon, Solar Engine, 3x Skink Crew
175 - Bastiladon, Solar Engine, 3x Skink Crew
357 - 8 Cold One Riders, Cavalry Spear, Drilled, Pack Leader, Charmed Shield, Standard Bearer, Skavenpelt Banner, Musician
```
