# Chaos Dwarfs — public list test fixture

> Research/test fixture for the integrated army builder. Selections and points reproduce a public tournament list; they are not a recommendation or official rules ruling.

## Source

- **Event:** [War in the Heartlands Act 4](https://oldworldrankings.com/uk/tournaments/war-in-the-heartlands-act-4) (2024-10-19)
- **Player / placing:** Tom Carley — 1st place
- **Event limit:** 2000 points; **published list total:** 2000 points
- **List record:** [https://oldworldrankings.com/army_lists/30d848f1-c7f4-4df6-a033-994585df6f6e](https://oldworldrankings.com/army_lists/30d848f1-c7f4-4df6-a033-994585df6f6e) — marked verified, with no inaccurate-list flag at collection.
- **Matched-play rule for app setup:** `Open War / Standard (test default; source export does not identify the rule)`.

## App construction audit

- **Catalog coverage:** 10/10 published unit entries map to a local faction profile or an allowed mercenary/allied profile.
- **Published unit-point subtotal:** 2000 points (matches the stated list total).
- **Build procedure:** choose the faction/composition, select the matched-play rule, set the event points limit, add each mapped profile, then configure the source-listed equipment/options from the roster below.
- **Verification scope:** catalog mapping and published-list point arithmetic were checked against local datasets. No browser automation runtime was available, so interactive selections and the app-calculated total still need hands-on confirmation.
- **Known gaps:** No unmatched unit profiles. Confirm source-listed options are selectable and that the configured app total reproduces the source.

### Catalog selections

| Published entry | Pts | App catalogue selection | Dataset profile | Match |
|---|---:|---|---|---|
| Sorcerer-Prophet | 475 | Characters | `chaos-dwarfs/characters:sorcerer-prophet` | Exact name |
| Black Orc Warboss | 354 | Characters | `chaos-dwarfs/characters:black-orc-warboss` | Exact name |
| Daemonsmith Sorcerer | 115 | Characters | `chaos-dwarfs/characters:daemonsmith-sorcerer` | Exact name |
| Infernal Guard | 160 | Core | `chaos-dwarfs/core:infernal-guard` | Exact name |
| Hobgoblin Cutthroats | 36 | Core | `chaos-dwarfs/core:hobgoblin-cutthroats` | Exact name |
| Hobgoblin Cutthroats | 36 | Core | `chaos-dwarfs/core:hobgoblin-cutthroats` | Exact name |
| Black Orc Mob | 274 | Core | `chaos-dwarfs/core:black-orc-mob` | Exact name |
| Iron Daemon | 310 | Special | `chaos-dwarfs/special:iron-daemon` | Exact name |
| Deathshrieker Rocket Launcher | 120 | Special | `chaos-dwarfs/special:deathshrieker-rocket-launcher` | Exact name |
| Deathshrieker Rocket Launcher | 120 | Special | `chaos-dwarfs/special:deathshrieker-rocket-launcher` | Exact name |

## Published roster (verbatim)

```text
Combined Arms [2000 pts]
Warhammer: The Old World, Chaos Dwarfs
===

++ Characters [944 pts] ++

Sorcerer-Prophet [475 pts]
- Darkforged weapon
- Heavy armour
- Level 4 Wizard
- General
- Bale Taurus
- Talisman of Protection
- Armour of Meteoric Iron
- Mantle of Stone
- Daemonology

Black Orc Warboss [354 pts]
- Great weapon
- Full plate armour
- Wyvern
- Effigy Of Mork
- Trollhide Trousers
- Enchanted Shield

Daemonsmith Sorcerer [115 pts]
- Hand weapon
- Heavy armour
- On foot
- Ruby Ring of Ruin
- Dark Magic

++ Core Units [506 pts] ++

10 Infernal Guard [160 pts]
- Fireglaives
- Heavy armour
- Shield

12 Hobgoblin Cutthroats [36 pts]
- Hand weapons
- Shortbows

12 Hobgoblin Cutthroats [36 pts]
- Hand weapons
- Shortbows

15 Black Orc Mob [274 pts]
- Hand weapon
- Full plate armour
- Stubborn
- 12x Shields
- 7x Great weapon
- Boss
- Standard bearer [Da Angry Ladz Flag]
- Musician

++ Special Units [550 pts] ++

Iron Daemon [310 pts]
- Steam Cannonade
- Hand weapons
- Hellbound

Deathshrieker Rocket Launcher [120 pts]
- Demolition Rockets
- Infernal Incendiaries
- Hand weapons
- Heavy armour

Deathshrieker Rocket Launcher [120 pts]
- Demolition Rockets
- Infernal Incendiaries
- Hand weapons
- Heavy armour
```
