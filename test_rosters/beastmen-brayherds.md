# Beastmen Brayherds — public list test fixture

> Research/test fixture for the integrated army builder. Selections and points reproduce a public tournament list; they are not a recommendation or official rules ruling.

## Source

- **Event:** [The Utah Cup 2026 - Warhammer The Old World](https://oldworldrankings.com/us/tournaments/the-utah-cup-2026-warhammer-the-old-world) (2026-08-08)
- **Player / placing:** Dylan Murnahan — 1st place
- **Event limit:** 2000 points; **published list total:** 2000 points
- **List record:** [https://oldworldrankings.com/army_lists/236dc9ce-6d09-4e60-b8b6-3dbd4174c20b](https://oldworldrankings.com/army_lists/236dc9ce-6d09-4e60-b8b6-3dbd4174c20b) — marked verified, with no inaccurate-list flag at collection.
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
| Doombull | 364 | Characters | `beastmen-brayherds/characters:doombull` | Exact name |
| Great Bray-Shaman | 280 | Characters | `beastmen-brayherds/characters:great-bray-shaman` | Exact name |
| Wargor | 208 | Characters | `beastmen-brayherds/characters:wargor` | Exact name |
| Bray-Shaman | 115 | Characters | `beastmen-brayherds/characters:bray-shaman` | Exact name |
| Gor Herd | 292 | Core | `beastmen-brayherds/core:gor-herds` | Exact name |
| Ungor Herd | 85 | Core | `beastmen-brayherds/core:ungor-herd` | Exact name |
| Ungor Herd | 72 | Core | `beastmen-brayherds/core:ungor-herd` | Exact name |
| Chaos Warhounds | 30 | Core | `beastmen-brayherds/core:warhounds` | Exact name |
| Razorgor Herd | 52 | Core | `beastmen-brayherds/core:razorgor-herds` | Exact name |
| Razorgor Herd | 52 | Core | `beastmen-brayherds/core:razorgor-herds` | Exact name |
| Ghorgon | 245 | Special | `beastmen-brayherds/special:ghorgon` | Exact name |
| Cygor | 205 | Rare | `beastmen-brayherds/rare:cygor` | Exact name |

## Published roster (verbatim)

```text
===
Beastmen Brayherds [2000 pts]
Warhammer: The Old World, Beastmen Brayherds, Grand Melee + Combined Arms
===

++ Characters [967 pts] ++

Doombull [364 pts]
- Great weapon
- No armour
- General
- Full Plate Chaos Armour
- Bedazzling Helm
- Gnarled Hide
- Pelt of Midnight

Great Bray-Shaman [280 pts]
- Braystaff
- Wizard [Level 4 Wizard]
- On foot
- Lore Familiar
- Cornucopia of Corpulence
- Full Plate Chaos Armour
- Daemonology

Wargor [208 pts]
- Great weapon
- Heavy armour
- Battle Standard Bearer [Monster Hunter's Tapestry]
- On foot
- Pelt of the Dark Young
- Charmed Shield
- Slug-skin

Bray-Shaman [115 pts]
- Braystaff
- Wizard [Level 1 Wizard]
- On foot
- Chalice of Dark Rain
- Daemonology

++ Core Units [583 pts] ++

35 Gor Herd [292 pts]
- Hand weapons
- Additional hand weapons
- True-horn (champion) [Great weapon]
- Standard bearer [Vitriolic Totem]
- Musician

13 Ungor Herd [85 pts]
- Shortbows
- Ambushers
- Half-horn (champion)

13 Ungor Herd [72 pts]
- Shortbows
- Half-horn (champion)

5 Chaos Warhounds [30 pts]
- Hand weapons (Claws and fangs)

1 Razorgor Herd [52 pts]
- Hand weapons (tusks)
- Light armour (calloused hide)

1 Razorgor Herd [52 pts]
- Hand weapons (tusks)
- Light armour (calloused hide)

++ Special Units [245pts] ++

Ghorgon [245 pts]
- Cleaver-limbs
- Light armour (calloused hide)

++ Rare Units [205pts] ++
Cygor [205 pts]
- Hand weapon (claws)
- Hurl attack
- Light armour (calloused hide)
```
