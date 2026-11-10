# Tomb Kings of Khemri — public list test fixture

> Research/test fixture for the integrated army builder. Selections and points reproduce a public tournament list; they are not a recommendation or official rules ruling.

## Source

- **Event:** [FaceHammer GT 2026](https://oldworldrankings.com/uk/tournaments/facehammer-gt-2026) (2026-10-17)
- **Player / placing:** Michal Kubacki — 1st place
- **Event limit:** 2000 points; **published list total:** 2000 points
- **List record:** [https://oldworldrankings.com/army_lists/13250982-846d-48ae-b14f-a58e508502ec](https://oldworldrankings.com/army_lists/13250982-846d-48ae-b14f-a58e508502ec) — marked verified, with no inaccurate-list flag at collection.
- **Matched-play rule for app setup:** `open-war`.

## App construction audit

- **Catalog coverage:** 15/15 published unit entries map to a local faction profile or an allowed mercenary/allied profile.
- **Published unit-point subtotal:** 2000 points (matches the stated list total).
- **Build procedure:** choose the faction/composition, select the matched-play rule, set the event points limit, add each mapped profile, then configure the source-listed equipment/options from the roster below.
- **Verification scope:** catalog mapping and published-list point arithmetic were checked against local datasets. No browser automation runtime was available, so interactive selections and the app-calculated total still need hands-on confirmation.
- **Known gaps:** No unmatched unit profiles. Confirm source-listed options are selectable and that the configured app total reproduces the source.

### Catalog selections

| Published entry | Pts | App catalogue selection | Dataset profile | Match |
|---|---:|---|---|---|
| Tomb King | 451 | Characters | `tomb-kings-of-khemri/characters:tomb-king` | Exact name |
| Tomb King | 454 | Characters | `tomb-kings-of-khemri/characters:tomb-king` | Exact name |
| Mortuary Priest | 90 | Characters | `tomb-kings-of-khemri/characters:mortuary-priest` | Exact name |
| Skeleton Archers | 70 | Core | `tomb-kings-of-khemri/core:skeleton-archers` | Exact name |
| Skeleton Archers | 70 | Core | `tomb-kings-of-khemri/core:skeleton-archers` | Exact name |
| Skeleton Skirmishers | 50 | Core | `tomb-kings-of-khemri/core:skeleton-skirmishers` | Exact name |
| Skeleton Horse Archers | 66 | Core | `tomb-kings-of-khemri/core:skeleton-horse-archers` | Exact name |
| Skeleton Horse Archers | 66 | Core | `tomb-kings-of-khemri/core:skeleton-horse-archers` | Exact name |
| Skeleton Horse Archers | 66 | Core | `tomb-kings-of-khemri/core:skeleton-horse-archers` | Exact name |
| Skeleton Chariots | 72 | Core | `tomb-kings-of-khemri/core:skeleton-chariots` | Exact name |
| Skeleton Chariots | 47 | Core | `tomb-kings-of-khemri/core:skeleton-chariots` | Exact name |
| Carrion | 54 | Special | `tomb-kings-of-khemri/special:carrion` | Exact name |
| Carrion | 54 | Special | `tomb-kings-of-khemri/special:carrion` | Exact name |
| Necrosphinx | 195 | Rare | `tomb-kings-of-khemri/rare:necrosphinx` | Exact name |
| Necrosphinx | 195 | Rare | `tomb-kings-of-khemri/rare:necrosphinx` | Exact name |

## Published roster (verbatim)

```text
===
Tomb Kings [2000 pts]
Warhammer: The Old World, Tomb Kings of Khemri, Open War
===

++ Characters [995 pts] ++

Tomb King [451 pts] 
- Great weapon
- Heavy armour
- Shield
- General
- Necrolith Bone Dragon
- Armour of Destiny
- Periapt of Soul Exchange

Tomb King [454 pts] 
- Great weapon
- Heavy armour
- Necrolith Bone Dragon
- Talisman of Protection
- Paymaster's Coin
- Arch-Lightning Rod

Mortuary Priest [90 pts] 
- Hand weapon
- Wizard [Level 1 Wizard]
- The Hierophant
- On foot
- Ruby Ring of Ruin
- Elementalism

++ Core Units [507 pts] ++

13 Skeleton Archers [70 pts] 
- Hand weapons
- Warbows
- Master of Arrows (champion)

13 Skeleton Archers [70 pts] 
- Hand weapons
- Warbows
- Master of Arrows (champion)

10 Skeleton Skirmishers [50 pts] 
- Hand weapons
- Warbows

6 Skeleton Horse Archers [66 pts] 
- Hand weapons
- Warbows

6 Skeleton Horse Archers [66 pts] 
- Hand weapons
- Warbows

6 Skeleton Horse Archers [66 pts] 
- Hand weapons
- Warbows

1 Skeleton Chariots [72 pts] 
- Hand weapons
- Cavalry spears
- Warbows
- 4+
- Master Charioteer (champion) [Ring of Doom]

1 Skeleton Chariots [47 pts] 
- Hand weapons
- Cavalry spears
- Warbows
- 4+
- Master Charioteer (champion)

++ Special Units [108 pts] ++

2 Carrion [54 pts] 
- Hand weapons (Beaks and talons)

2 Carrion [54 pts] 
- Hand weapons (Beaks and talons)

++ Rare Units [390 pts] ++

Necrosphinx [195 pts] 
- Cleaving blades
- Decapitating strike
- Heavy armour

Necrosphinx [195 pts] 
- Cleaving blades
- Decapitating strike
- Heavy armour

---
Created with "Old World Builder"

[https://old-world-builder.com]
```
