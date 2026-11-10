# Renegade Crowns — public list test fixture

> Research/test fixture for the integrated army builder. Selections and points reproduce a public tournament list; they are not a recommendation or official rules ruling.

## Source

- **Event:** [Old Grudges MAY26](https://oldworldrankings.com/au/tournaments/old-grudges-may26) (2026-05-09)
- **Player / placing:** Jason Mulligan — 1st place
- **Event limit:** 2000 points; **published list total:** 2000 points
- **List record:** [https://oldworldrankings.com/army_lists/8a2cc545-c701-42a4-8d9f-6fc09787eeed](https://oldworldrankings.com/army_lists/8a2cc545-c701-42a4-8d9f-6fc09787eeed) — marked verified, with no inaccurate-list flag at collection.
- **Matched-play rule for app setup:** `combined-arms`.

## App construction audit

- **Catalog coverage:** 17/17 published unit entries map to a local faction profile or an allowed mercenary/allied profile.
- **Published unit-point subtotal:** 2000 points (matches the stated list total).
- **Build procedure:** choose the faction/composition, select the matched-play rule, set the event points limit, add each mapped profile, then configure the source-listed equipment/options from the roster below.
- **Verification scope:** catalog mapping and published-list point arithmetic were checked against local datasets. No browser automation runtime was available, so interactive selections and the app-calculated total still need hands-on confirmation.
- **Known gaps:** No unmatched unit profiles. Confirm source-listed options are selectable and that the configured app total reproduces the source.

### Catalog selections

| Published entry | Pts | App catalogue selection | Dataset profile | Match |
|---|---:|---|---|---|
| Renegade Prince | 112 | Characters | `renegade-crowns/characters:renegade-prince` | Exact name |
| Renegade Prince | 101 | Characters | `renegade-crowns/characters:renegade-prince` | Exact name |
| Renegade Captain | 72 | Characters | `renegade-crowns/characters:renegade-captain` | Exact name |
| Renegade Captain | 45 | Characters | `renegade-crowns/characters:renegade-captain` | Exact name |
| Outcast Wizard | 120 | Characters | `renegade-crowns/characters:outcast-wizard` | Exact name |
| Outcast Wizard | 85 | Characters | `renegade-crowns/characters:outcast-wizard` | Exact name |
| Outcast Wizard | 155 | Characters | `renegade-crowns/characters:outcast-wizard` | Exact name |
| Veteran Sellswords | 436 | Core | `renegade-crowns/core:veteran-sellswords` | Exact name |
| Hireling Outriders | 105 | Core | `renegade-crowns/core:hireling-outriders` | Exact name |
| Hireling Outriders | 105 | Core | `renegade-crowns/core:hireling-outriders` | Exact name |
| Empire Archers | 70 | Core | `renegade-crowns/core:empire-archers` | Exact name |
| Empire Archers | 70 | Core | `renegade-crowns/core:empire-archers` | Exact name |
| Freeblade Knights | 144 | Core | `renegade-crowns/core:freeblade-knights` | Exact name |
| Border Princes Mortar | 90 | Special | `renegade-crowns/special:border-princes-mortar` | Exact name |
| Border Princes Mortar | 90 | Special | `renegade-crowns/special:border-princes-mortar` | Exact name |
| Border Princes Bombard | 100 | Rare | `renegade-crowns/rare:border-princes-bombard` | Exact name |
| Border Princes Bombard | 100 | Rare | `renegade-crowns/rare:border-princes-bombard` | Exact name |

## Published roster (verbatim)

```text
===
 Re crown block [2000 pts]
Warhammer: The Old World, Renegade Crowns, Combined Arms
===

++ Characters [690 pts] ++

Renegade Prince [112 pts] 
- Hand weapon
- Great weapon
- Full plate armour
- Shield
- General
- The Might of Miragliano [Stubborn
- Tilean Stoicism]
- On foot

Renegade Prince [101 pts] 
- Hand weapon
- Great weapon
- Full plate armour
- Barded Warhorse

Renegade Captain [72 pts] 
- Hand weapon
- Great weapon
- Full plate armour
- Shield
- Battle Standard Bearer
- On foot

Renegade Captain [45 pts] 
- Hand weapon
- Great weapon
- Full plate armour
- On foot

Outcast Wizard [120 pts] 
- Hand weapon
- Wizard [Level 1 Wizard]
- The Noble Outlaw ["Hold the Line!" + Repeater pistol]
- Warhorse
- Ruby Ring of Ruin
- Daemonology

Outcast Wizard [85 pts] 
- Hand weapon
- Wizard [Level 1 Wizard]
- The Noble Outlaw ["Hold the Line!" + Repeater pistol]
- Warhorse
- Daemonology

Outcast Wizard [155 pts] 
- Hand weapon
- Wizard [Level 3 Wizard]
- On foot
- Power Scroll
- Lore Familiar
- Elementalism

++ Core Units [930 pts] ++

32 Veteran Sellswords [436 pts] 
- Thrusting spears
- Full plate armour
- Shields
- Drilled
- Heavy Infantry
- Phalanx
- Veteran Officer (champion)
- Standard bearer [Monster Hunter's Tapestry]
- Musician

5 Hireling Outriders [105 pts] 
- Pistols
- Heavy armour
- Shields
- Feigned Flight
- Reserve Move

5 Hireling Outriders [105 pts] 
- Pistols
- Heavy armour
- Shields
- Feigned Flight
- Reserve Move

10 Empire Archers [70 pts] 
- Hand weapons
- Warbows
- Detachment

10 Empire Archers [70 pts] 
- Hand weapons
- Warbows
- Detachment

6 Freeblade Knights [144 pts] 
- Hand weapons
- Lances
- Heavy armour
- Shields
- Commander (champion)
- Barded Warhorses

++ Special Units [180 pts] ++

Border Princes Mortar [90 pts] 
- Mortar
- Hand weapons

Border Princes Mortar [90 pts] 
- Mortar
- Hand weapons

++ Rare Units [200 pts] ++

Border Princes Bombard [100 pts] 
- Bombard
- Hand weapons
- Light armour

Border Princes Bombard [100 pts] 
- Bombard
- Hand weapons
- Light armour

---
Created with "Old World Builder"

[https://old-world-builder.com]
```
