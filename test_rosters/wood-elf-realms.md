# Wood Elf Realms — public list test fixture

> Research/test fixture for the integrated army builder. Selections and points reproduce a public tournament list; they are not a recommendation or official rules ruling.

## Source

- **Event:** [Crucible 2026](https://oldworldrankings.com/us/tournaments/crucible-2026) (2026-09-12)
- **Player / placing:** Charlie — 1st place
- **Event limit:** 2000 points; **published list total:** 2000 points
- **List record:** [https://oldworldrankings.com/army_lists/6a57f099-def9-4495-8546-88c617e9b529](https://oldworldrankings.com/army_lists/6a57f099-def9-4495-8546-88c617e9b529) — marked verified, with no inaccurate-list flag at collection.
- **Matched-play rule for app setup:** `grand-melee-combined-arms`.

## App construction audit

- **Catalog coverage:** 13/13 published unit entries map to a local faction profile or an allowed mercenary/allied profile.
- **Published unit-point subtotal:** 2000 points (matches the stated list total).
- **Build procedure:** choose the faction/composition, select the matched-play rule, set the event points limit, add each mapped profile, then configure the source-listed equipment/options from the roster below.
- **Verification scope:** catalog mapping and published-list point arithmetic were checked against local datasets. No browser automation runtime was available, so interactive selections and the app-calculated total still need hands-on confirmation.
- **Known gaps:** No unmatched unit profiles. Confirm source-listed options are selectable and that the configured app total reproduces the source.

### Catalog selections

| Published entry | Pts | App catalogue selection | Dataset profile | Match |
|---|---:|---|---|---|
| Glade Lord | 499 | Characters | `wood-elf-realms/characters:glade-lord` | Exact name |
| Glade Captain | 141 | Characters | `wood-elf-realms/characters:glade-captain` | Exact name |
| Spellweaver | 209 | Characters | `wood-elf-realms/characters:spellweaver` | Exact name |
| Waystalker | 115 | Characters | `wood-elf-realms/characters:waystalker` | Exact name |
| Glade Guard | 55 | Core | `wood-elf-realms/core:glade-guard` | Exact name |
| Deepwood Scouts | 165 | Core | `wood-elf-realms/core:deepwood-scouts-core` | Exact name |
| Glade Riders | 120 | Core | `wood-elf-realms/core:glade-riders` | Exact name |
| Glade Riders | 160 | Core | `wood-elf-realms/core:glade-riders` | Exact name |
| Sisters of the Thorn | 102 | Special | `wood-elf-realms/special:sisters-of-the-thorn` | Exact name |
| Wardancers | 195 | Special | `wood-elf-realms/special:wardancers` | Exact name |
| Waywatchers | 144 | Rare | `wood-elf-realms/rare:waywatchers` | Exact name |
| Wood Elf Beast Pack | 35 | Rare | `wood-elf-realms/rare:wood-elf-beast-pack` | Exact name |
| Great Eagle | 60 | Rare | `wood-elf-realms/rare:giant-eagle` | Exact name |

## Published roster (verbatim)

```text
===
Crucible 2026-Allarien [2000 pts]
Warhammer: The Old World, Wood Elf Realms, Grand Melee + Combined Arms
===

++ Characters [964 pts] ++

Glade Lord [499 pts] 
- Hand weapon
- Great weapon
- Light armour
- Asrai longbow
- General
- Forest Dragon
- Armour of Meteoric Iron
- Talisman of Protection
- An Annoyance of Netlings
- A Resplendence of Luminescents
- Aspect of the Cat

Glade Captain [141 pts] 
- Hand weapon
- Great weapon
- Light armour
- Shield
- Asrai longbow
- Great Stag
- Aspect of the Bear

Spellweaver [209 pts] 
- Hand weapon
- Wizard [Level 3 Wizard]
- Elven Steed
- Oaken Stave
- Elementalism

Waystalker [115 pts] 
- Hand weapon
- Sword of Sorrow

++ Core Units [500 pts] ++

5 Glade Guard [55 pts] 
- Hand weapon
- Asrai longbows
- Trueflight Arrows

11 Deepwood Scouts [165 pts] 
- Hand weapon
- Asrai longbows
- Arcane Bodkins

6 Glade Riders [120 pts] 
- Hand weapon
- Cavalry spears
- Asrai longbows
- Reserve Move
- Hagbane Tips

8 Glade Riders [160 pts] 
- Hand weapon
- Cavalry spears
- Asrai longbows
- Reserve Move
- Hagbane Tips

++ Special Units [297 pts] ++

4 Sisters of the Thorn [102 pts] 
- Hand weapons
- Blackbriar javelins
- Handmaiden of the Thorn
- Standard bearer

9 Wardancers [195 pts] 
- Hand weapon
- 9x Additional hand weapon
- Bladesinger [Burning Blade]
- Standard bearer [Monster Hunter's Tapestry]

++ Rare Units [239 pts] ++

8 Waywatchers [144 pts] 
- Hand weapon
- Asrai longbows
- Arcane Bodkins

1 Wood Elf Beast Pack [35 pts] 
- 3x Deepwood Hound [Hand weapons (Claws + fangs
- tusks
- teeth)]

Great Eagle [60 pts] 
- Wicked claws
- Serrated maw

---
Created with "Old World Builder"

[https://old-world-builder.com]
```
