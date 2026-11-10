# Skaven — public list test fixture

> Research/test fixture for the integrated army builder. Selections and points reproduce a public tournament list; they are not a recommendation or official rules ruling.

## Source

- **Event:** [Mysza World 4](https://oldworldrankings.com/pl/tournaments/mysza-world-4) (2025-11-14)
- **Player / placing:** LeXincerta — 8th place
- **Event limit:** 2000 points; **published list total:** not stated in the list export
- **List record:** [https://oldworldrankings.com/army_lists/56bc0bb9-079a-4e0c-a461-f681b831e659](https://oldworldrankings.com/army_lists/56bc0bb9-079a-4e0c-a461-f681b831e659) — marked verified, with no inaccurate-list flag at collection.
- **Matched-play rule for app setup:** `Open War / Standard (test default; source export does not identify the rule)`.

## App construction audit

- **Catalog coverage:** 15/15 published unit entries map to a local faction profile or an allowed mercenary/allied profile.
- **Published unit-point subtotal:** 1999 points from item rows (no list total in the export; event limit is 2000).
- **Build procedure:** choose the faction/composition, select the matched-play rule, set the event points limit, add each mapped profile, then configure the source-listed equipment/options from the roster below.
- **Verification scope:** catalog mapping and published-list point arithmetic were checked against local datasets. No browser automation runtime was available, so interactive selections and the app-calculated total still need hands-on confirmation.
- **Known gaps:** No unmatched unit profiles. Confirm source-listed options are selectable and that the configured app total reproduces the source.

### Catalog selections

| Published entry | Pts | App catalogue selection | Dataset profile | Match |
|---|---:|---|---|---|
| Skaven Chieftain | 53 | Characters | `skaven/characters:skaven-chieftain` | Exact name |
| Skaven Chieftain | 98 | Characters | `skaven/characters:skaven-chieftain` | Exact name |
| Warlock Engineer | 135 | Characters | `skaven/characters:warlock-engineer` | Exact name |
| Warlock Engineer | 70 | Characters | `skaven/characters:warlock-engineer` | Exact name |
| Clanrats | 172 | Core | `skaven/core:clanrats` | Exact name |
| Clanrats | 172 | Core | `skaven/core:clanrats` | Exact name |
| Giant Rats | 35 | Core | `skaven/core:giant-rats` | Exact name |
| Giant Rats | 35 | Core | `skaven/core:giant-rats` | Exact name |
| Night Runners | 90 | Core | `skaven/core:night-runners` | Exact name |
| Gutter Runners | 259 | Special | `skaven/special:gutter-runners` | Exact name |
| Warplock Jezzails | 190 | Special | `skaven/special:warplock-jezzails` | Exact name |
| Warplock Jezzails | 190 | Special | `skaven/special:warplock-jezzails` | Exact name |
| Doomwheel | 145 | Rare | `skaven/rare:doomwheel` | Exact name |
| Doomwheel | 145 | Rare | `skaven/rare:doomwheel` | Exact name |
| Hell Pit Abomination | 210 | Rare | `skaven/rare:hell-pit-abomination` | Exact name |

## Published roster (verbatim)

```text
Arkadiusz Romański Aka LeXincerta
53 - Skaven Chieftain, Halberd, Shield, Heavy Armour, General
98 - Skaven Chieftain, Halberd, Shield, Heavy Armour, Battle Standard Bearer, Cautious Shield
135 - Warlock Engineer, Wizard Level 2, Battle Magic, Lore Familiar
70 - Warlock Engineer, Ruby Ring of Ruin
172 - 23 Clanrats
  • 1x Weapon Team
  • 1x Weapon Team Crew, Warp Grinder, Clawleader, Standard Bearer, Musician
  • 22x Clanrat, Shield
172 - 31 Clanrats, Shield, Clawleader, Standard Bearer, Musician
35 - 10 Giant Rats
  • 1x Packmaster, Whip
  • 10x Giant Rat
35 - 10 Giant Rats
  • 1x Packmaster, Whip
  • 10x Giant Rat
90 - 12 Night Runners, Nightleader
259 - 14 Gutter Runners, Sling, Poisoned Attacks, Assassin
190 - 10 Warplock Jezzails
190 - 10 Warplock Jezzails
145 - Doomwheel
145 - Doomwheel
210 - Hell Pit Abomination
```
