# Dwarfen Mountain Holds — public list test fixture

> Research/test fixture for the integrated army builder. Selections and points reproduce a public tournament list; they are not a recommendation or official rules ruling.

## Source

- **Event:** [The Old World @ LGT](https://oldworldrankings.com/uk/tournaments/the-old-world-lgt) (2026-09-26)
- **Player / placing:** Matthew Clayton — 20th place
- **Event limit:** 2000 points; **published list total:** 2000 points
- **List record:** [https://oldworldrankings.com/army_lists/eb8341db-18dc-4d54-9221-c0178f5c8347](https://oldworldrankings.com/army_lists/eb8341db-18dc-4d54-9221-c0178f5c8347) — marked verified, with no inaccurate-list flag at collection.
- **Matched-play rule for app setup:** `grand-melee-combined-arms`.

## App construction audit

- **Catalog coverage:** 12/12 published unit entries map to a local faction profile or an allowed mercenary/allied profile.
- **Published unit-point subtotal:** 2000 points (matches the stated list total).
- **Build procedure:** choose the faction/composition, select the matched-play rule, set the event points limit, add each mapped profile, then configure the source-listed equipment/options from the roster below.
- **Verification scope:** catalog mapping and published-list point arithmetic were checked against local datasets. No browser automation runtime was available, so interactive selections and the app-calculated total still need hands-on confirmation.
- **Known gaps:** No unmatched unit profiles. Confirm source-listed options are selectable and that the configured app total reproduces the source.

### Catalog selections

| Published entry | Pts | App catalogue selection | Dataset profile | Match |
|---|---:|---|---|---|
| Burlok Damminson | 85 | Characters | `dwarfen-mountain-holds/characters:burlok-damminson` | Exact name |
| Thane | 296 | Characters | `dwarfen-mountain-holds/characters:thane` | Exact name |
| Thane | 138 | Characters | `dwarfen-mountain-holds/characters:thane` | Exact name |
| Engineer | 93 | Characters | `dwarfen-mountain-holds/characters:engineer` | Exact name |
| Runesmith | 142 | Characters | `dwarfen-mountain-holds/characters:runesmith` | Exact name |
| Thane | 141 | Characters | `dwarfen-mountain-holds/characters:thane` | Exact name |
| Rangers | 162 | Core | `dwarfen-mountain-holds/core:rangers-core` | Exact name |
| Thunderers | 175 | Core | `dwarfen-mountain-holds/core:thunderers` | Exact name |
| Thunderers | 164 | Core | `dwarfen-mountain-holds/core:thunderers` | Exact name |
| Cannon | 95 | Special | `dwarfen-mountain-holds/special:cannon` | Exact name |
| Cannon | 95 | Special | `dwarfen-mountain-holds/special:cannon` | Exact name |
| Irondrakes | 414 | Rare | `dwarfen-mountain-holds/rare:irondrakes` | Exact name |

## Published roster (verbatim)

```text
===
Drakestar [2000 pts]
Warhammer: The Old World, Dwarfen Mountain Holds, Grand Melee + Combined Arms
===

++ Characters [895 pts] ++

Burlok Damminson [85 pts] 
- Furnace hammer
- Rivet gun
- Heavy armour
- General

Thane [296 pts] 
- Hand weapon
- Great weapon
- Full plate armour
- Shield
- Battle Standard Bearer [Master Rune of Grungni + Rune of Courage + Rune of Battle]
- Shieldbearers
- Rune of Preservation

Thane [138 pts] 
- Hand weapon
- Handgun
- Full plate armour
- Shield
- On foot
- Master Rune of Bursting Flame
- Rune of Accuracy
- Rune of Rapid Fire

Engineer [93 pts] 
- Hand weapon
- Heavy armour
- Handgun
- Rune of Accuracy
- Rune of Rapid Fire

Runesmith [142 pts] 
- Hand weapon
- Heavy armour
- Shield
- Rune of Spellbreaking
- Master Rune of Calm

Thane [141 pts] 
- Hand weapon
- Handgun
- Full plate armour
- On foot
- Rune of Accuracy
- Master Rune of Piercing
- Rune of Rapid Fire

++ Core Units [501 pts] ++

12 Rangers [162 pts] 
- Hand weapons
- Crossbows
- Throwing axes
- Heavy armour
- Shields
- Ol' Deadeye (champion) [Crossbow]

15 Thunderers [175 pts] 
- Hand weapons
- Handguns
- Heavy armour
- Shields
- Veteran (champion) [Handgun]
- Musician

14 Thunderers [164 pts] 
- Hand weapons
- Handguns
- Heavy armour
- Shields
- Veteran (champion) [Handgun]
- Musician

++ Special Units [190 pts] ++

Cannon [95 pts] 
- Cannon
- Hand weapons
- Light armour

Cannon [95 pts] 
- Cannon
- Hand weapons
- Light armour

++ Rare Units [414 pts] ++

21 Irondrakes [414 pts] 
- Hand weapons
- Drakeguns
- Full plate armour
- Drilled
- Ironwarden (champion) [Drakegun + Cinderblast bombs]
- Standard bearer [Master Rune of Hesitation]
- Musician

---
Created with "Old World Builder"

[https://old-world-builder.com]
```
