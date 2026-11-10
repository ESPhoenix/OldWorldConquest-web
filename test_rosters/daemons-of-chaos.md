# Daemons of Chaos — public list test fixture

> Research/test fixture for the integrated army builder. Selections and points reproduce a public tournament list; they are not a recommendation or official rules ruling.

## Source

- **Event:** [Durham GT: Middenheim Massacre](https://oldworldrankings.com/uk/tournaments/durham-gt-middenheim-massacre) (2026-01-31)
- **Player / placing:** Danny Minto — 27th place
- **Event limit:** 2000 points; **published list total:** 2000 points
- **List record:** [https://oldworldrankings.com/army_lists/da122b5b-1786-45b9-93f0-6da719581091](https://oldworldrankings.com/army_lists/da122b5b-1786-45b9-93f0-6da719581091) — marked verified, with no inaccurate-list flag at collection.
- **Matched-play rule for app setup:** `open-war`.

## App construction audit

- **Catalog coverage:** 8/8 published unit entries map to a local faction profile or an allowed mercenary/allied profile.
- **Published unit-point subtotal:** 2000 points (matches the stated list total).
- **Build procedure:** choose the faction/composition, select the matched-play rule, set the event points limit, add each mapped profile, then configure the source-listed equipment/options from the roster below.
- **Verification scope:** catalog mapping and published-list point arithmetic were checked against local datasets. No browser automation runtime was available, so interactive selections and the app-calculated total still need hands-on confirmation.
- **Known gaps:** No unmatched unit profiles. Confirm source-listed options are selectable and that the configured app total reproduces the source.

### Catalog selections

| Published entry | Pts | App catalogue selection | Dataset profile | Match |
|---|---:|---|---|---|
| Bloodthirster | 420 | Characters | `daemons-of-chaos/characters:bloodthirster` | Exact name |
| Daemon Prince | 321 | Characters | `daemons-of-chaos/characters:daemon-prince` | Exact name |
| Daemonic Herald of Khorne | 250 | Characters | `daemons-of-chaos/characters:daemonic-herald-of-khorne` | Exact name |
| Flesh Hounds of Khorne | 170 | Core | `daemons-of-chaos/core:flesh-hounds-of-khorne-core` | Exact name |
| Flesh Hounds of Khorne | 170 | Core | `daemons-of-chaos/core:flesh-hounds-of-khorne-core` | Exact name |
| Flesh Hounds of Khorne | 160 | Core | `daemons-of-chaos/core:flesh-hounds-of-khorne-core` | Exact name |
| Bloodcrushers of Khorne | 254 | Special | `daemons-of-chaos/special:bloodcrushers-of-khorne` | Exact name |
| Soul Grinder | 255 | Rare | `daemons-of-chaos/rare:soul-grinder` | Exact name |

## Published roster (verbatim)

```text
===
Daemons of Chaos [2000 pts]
Warhammer: The Old World, Daemons of Chaos, Open War
===

++ Characters [991 pts] ++

Bloodthirster [420 pts] 
- Hand weapon
- Heavy armour
- Bloodflail
- General
- Armour of Khorne

Daemon Prince [321 pts] 
- Hand weapon
- Ensorcelled weapon
- Heavy armour
- Fly (9)
- No daemonic alignment [Level 3 Wizard]
- Battle Magic

Daemonic Herald of Khorne [250 pts] 
- Hellblade
- Light armour (calloused hides)
- Daemonic Locus (Battle Standard Bearer) [Banner of Unholy Victory]
- Juggernaut of Khorne
- Axe of Khorne

++ Core Units [500 pts] ++

5 Flesh Hounds of Khorne [170 pts] 
- Hand weapons (Claws and fangs)
- Light armour (calloused hides)
- Vanguard

5 Flesh Hounds of Khorne [170 pts] 
- Hand weapons (Claws and fangs)
- Light armour (calloused hides)
- Vanguard

5 Flesh Hounds of Khorne [160 pts] 
- Hand weapons (Claws and fangs)
- Light armour (calloused hides)

++ Special Units [254 pts] ++

3 Bloodcrushers of Khorne [254 pts] 
- Hellblades
- Brass bound hooves
- Light armour (calloused hides)
- Barding (brazen hide)
- Bloodreaper (champion)
- Standard bearer [Great Standard of Sundering]

++ Rare Units [255 pts] ++

Soul Grinder [255 pts] 
- Hand weapon
- Iron claw
- Harvester cannon
- Heavy armour (Daemonic flesh)

---
Created with "Old World Builder"

[https://old-world-builder.com]
```
