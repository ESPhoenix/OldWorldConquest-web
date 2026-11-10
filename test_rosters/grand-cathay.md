# Grand Cathay — public list test fixture

> Research/test fixture for the integrated army builder. Selections and points reproduce a public tournament list; they are not a recommendation or official rules ruling.

## Source

- **Event:** [Summer Smash 2026 - The Old World 2000pt GT](https://oldworldrankings.com/ca/tournaments/summer-smash-2026-the-old-world-2000pt-gt) (2026-06-13)
- **Player / placing:** Dennis Ashmore — 1st place
- **Event limit:** 2000 points; **published list total:** 1999 points
- **List record:** [https://oldworldrankings.com/army_lists/1ab42c82-019b-40cf-9d77-a323057a304e](https://oldworldrankings.com/army_lists/1ab42c82-019b-40cf-9d77-a323057a304e) — marked verified, with no inaccurate-list flag at collection.
- **Matched-play rule for app setup:** `grand-melee-combined-arms`.

## App construction audit

- **Catalog coverage:** 10/10 published unit entries map to a local faction profile or an allowed mercenary/allied profile.
- **Published unit-point subtotal:** 1999 points (matches the stated list total).
- **Build procedure:** choose the faction/composition, select the matched-play rule, set the event points limit, add each mapped profile, then configure the source-listed equipment/options from the roster below.
- **Verification scope:** catalog mapping and published-list point arithmetic were checked against local datasets. No browser automation runtime was available, so interactive selections and the app-calculated total still need hands-on confirmation.
- **Known gaps:** No unmatched unit profiles. Confirm source-listed options are selectable and that the configured app total reproduces the source.

### Catalog selections

| Published entry | Pts | App catalogue selection | Dataset profile | Match |
|---|---:|---|---|---|
| Shugengan Lord | 339 | Characters | `grand-cathay/characters:shugengan-lord` | Exact name |
| Shugengan Lord | 334 | Characters | `grand-cathay/characters:shugengan-lord` | Exact name |
| Shugengan General | 155 | Characters | `grand-cathay/characters:shugengan` | Exact name |
| Shugengan General | 155 | Characters | `grand-cathay/characters:shugengan` | Exact name |
| Jade Warriors | 244 | Core | `grand-cathay/core:jade-warriors` | Exact name |
| Jade Warriors | 213 | Core | `grand-cathay/core:jade-warriors` | Exact name |
| Peasant Levy | 64 | Core | `grand-cathay/core:peasant-levy` | Exact name |
| Cathayan Grand Cannon | 165 | Special | `grand-cathay/special:cathayan-grand-cannon` | Exact name |
| Cathayan Grand Cannon | 165 | Special | `grand-cathay/special:cathayan-grand-cannon` | Exact name |
| Cathayan Grand Cannon | 165 | Special | `grand-cathay/special:cathayan-grand-cannon` | Exact name |

## Published roster (verbatim)

```text
Grand Cathay [1999 pts]
Warhammer: The Old World, Grand Cathay, Grand Melee + Combined Arms

Shugengan Lord, Iron talons, Heavy armour, Wizard [Level 3 Wizard], Lore of Yang, General, Great Spirit Longma, The Monkey King's Wisdom, Scrolls of Wei-jin, Illusion - 339
Shugengan Lord, Iron talons, Heavy armour, Wizard [Level 3 Wizard], Lore of Yang, Great Spirit Longma, Learned Feng Shi Bo, The Sword of Reason, Illusion - 334
Shugengan General, Celestial blade, Iron talons, Heavy armour, Wizard [Level 1 Wizard], Lore of Yang, Great Spirit Longma, Battle Magic - 155
Shugengan General, Celestial blade, Iron talons, Heavy armour, Wizard [Level 1 Wizard], Lore of Yang, Great Spirit Longma, Battle Magic - 155
24 Jade Warriors, Shields, Heavy armour, Jade Officer (champion), Standard bearer [The Jade Banner] - 244
22 Jade Warriors, Shields, Heavy armour, Jade Officer (champion), Standard bearer [War Banner] - 213
14 Peasant Levy, Warbows, No armour, Skirmishers, Peasant Elder (champion) - 64
Cathayan Grand Cannon, Grand cannon, Light armour, Ogre Loader - 165
Cathayan Grand Cannon, Grand cannon, Light armour, Ogre Loader - 165
Cathayan Grand Cannon, Grand cannon, Light armour, Ogre Loader - 165

---
Created with "Old World Builder"

[https://old-world-builder.com]
```
