# High Elf Realms — public list test fixture

> Research/test fixture for the integrated army builder. Selections and points reproduce a public tournament list; they are not a recommendation or official rules ruling.

## Source

- **Event:** [The Old World @ The Windsor GT](https://oldworldrankings.com/uk/tournaments/the-old-world-the-windsor-gt) (2026-03-07)
- **Player / placing:** Jack Negus — 4th place
- **Event limit:** 2000 points; **published list total:** not stated in the list export
- **List record:** [https://oldworldrankings.com/army_lists/a4879e72-4531-4698-b92f-75af4346279d](https://oldworldrankings.com/army_lists/a4879e72-4531-4698-b92f-75af4346279d) — marked verified, with no inaccurate-list flag at collection.
- **Matched-play rule for app setup:** `Open War / Standard (test default; source export does not identify the rule)`.

## App construction audit

- **Catalog coverage:** 10/10 published unit entries map to a local faction profile or an allowed mercenary/allied profile.
- **Published unit-point subtotal:** 1998 points from item rows (no list total in the export; event limit is 2000).
- **Build procedure:** choose the faction/composition, select the matched-play rule, set the event points limit, add each mapped profile, then configure the source-listed equipment/options from the roster below.
- **Verification scope:** catalog mapping and published-list point arithmetic were checked against local datasets. No browser automation runtime was available, so interactive selections and the app-calculated total still need hands-on confirmation.
- **Known gaps:** No unmatched unit profiles. Confirm source-listed options are selectable and that the configured app total reproduces the source.

### Catalog selections

| Published entry | Pts | App catalogue selection | Dataset profile | Match |
|---|---:|---|---|---|
| Prince | 500 | Characters | `high-elf-realms/characters:prince` | Exact name |
| Prince | 302 | Characters | `high-elf-realms/characters:prince` | Exact name |
| Storm Weaver | 195 | Characters | `high-elf-realms/characters:storm-weaver` | Exact name |
| Lothern Sea Guard | 389 | Core | `high-elf-realms/core:lothern-sea-guard` | Exact name |
| Elven Archers | 135 | Core | `high-elf-realms/core:elven-archers` | Exact name |
| Lothern Skycutter | 115 | Special | `high-elf-realms/special:lothern-skycutters` | Exact name |
| Lothern Skycutter | 90 | Rare | `high-elf-realms/rare:lothern-skycutters-rare` | Exact name |
| Lothern Skycutter | 90 | Rare | `high-elf-realms/rare:lothern-skycutters-rare` | Exact name |
| Sisters of Avelorn | 122 | Rare | `high-elf-realms/rare:sister-of-avelorn` | Exact name |
| Great Eagle | 60 | Rare | `high-elf-realms/rare:great-eagle` | Exact name |

## Published roster (verbatim)

```text
++ Characters [997 pts] ++
Prince [500 pts] 
(Hand weapon, Halberd, Light armour, Shield, Star Dragon, Armour of Caledor, Opal Amulet, Seed of Rebirth, Pure of Heart)

Prince [302 pts] 
(Hand weapon, Great weapon, Full plate armour, Shield, General, Lothern Skycutter, Seed of Rebirth, Talisman of Protection, Opal Amulet, Sea Guard)

Storm Weaver [195 pts] 
(Hand weapon, Wizard [Level 3 Wizard], On foot, Lore Familiar, Power Scroll, Elementalism)

++ Core Units [524 pts] ++
26 Lothern Sea Guard [389 pts] 
(Hand weapons, Thrusting spears, Warbows, Light armour, Shields, Sea Master (champion) [Obsidian Lodestone], Standard bearer [Razor Standard], Musician)

13 Elven Archers [135 pts] 
(Hand weapons, Longbows, Sentinel (champion))

++ Special Units [115 pts] ++
Lothern Skycutter [115 pts] 
(Cavalry spears, Shortbows, Eagle-Eye Bolt Thrower)

++ Rare Units [362 pts] ++
Lothern Skycutter [90 pts] 
(Cavalry spears, Shortbows)

Lothern Skycutter [90 pts] 
(Cavalry spears, Shortbows)

5 Sisters of Avelorn [122 pts] 
(Bows of Avelorn, Light armour, Ambushers, High Sister [Ruby Ring of Ruin])

Great Eagle [60 pts]
```
