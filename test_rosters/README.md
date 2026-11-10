# Public army-list test rosters

One Markdown fixture per Old World Builder army. Each fixture links to a public Old World Rankings list, preserves its published text, maps list entries to local catalog profiles, and records point arithmetic and construction caveats. Sources were marked verified and not inaccurate when collected (10 November 2026).

| Faction | Public event | Placing | Event cap | Catalog matches | Item subtotal / stated total | Fixture |
|---|---|---:|---:|---:|---:|---|
| Renegade Crowns | Old Grudges MAY26 | 1 | 2000 | 17/17 | 2000 / 2000 | [renegade-crowns.md](renegade-crowns.md) |
| Empire of Man | Rock River Ruckus 2026 | 2 | 2000 | 12/12 | 1999 / not stated | [empire-of-man.md](empire-of-man.md) |
| Orc & Goblin Tribes | Bay Area Open 2026 - The Old World Champs | 3 | 2000 | 18/18 | 2000 / 2000 | [orc-and-goblin-tribes.md](orc-and-goblin-tribes.md) |
| Dwarfen Mountain Holds | The Old World @ LGT | 20 | 2000 | 12/12 | 2000 / 2000 | [dwarfen-mountain-holds.md](dwarfen-mountain-holds.md) |
| Warriors of Chaos | Rock River Ruckus 2026 | 1 | 2000 | 8/8 | 2000 / not stated | [warriors-of-chaos.md](warriors-of-chaos.md) |
| Kingdom of Bretonnia | Conflict Events Presents! Eternal Glory V - January (Square Based Comp) | 2 | 2500 | 8/8 | 2000 / not stated | [kingdom-of-bretonnia.md](kingdom-of-bretonnia.md) |
| Beastmen Brayherds | The Utah Cup 2026 - Warhammer The Old World | 1 | 2000 | 12/12 | 2000 / 2000 | [beastmen-brayherds.md](beastmen-brayherds.md) |
| Wood Elf Realms | Crucible 2026 | 1 | 2000 | 13/13 | 2000 / 2000 | [wood-elf-realms.md](wood-elf-realms.md) |
| Tomb Kings of Khemri | FaceHammer GT 2026 | 1 | 2000 | 15/15 | 2000 / 2000 | [tomb-kings-of-khemri.md](tomb-kings-of-khemri.md) |
| High Elf Realms | The Old World @ The Windsor GT | 4 | 2000 | 10/10 | 1998 / not stated | [high-elf-realms.md](high-elf-realms.md) |
| Dark Elves | 2. Wiener Würfel Wappler Watschenfest | 2 | 2000 | 12/12 | 2000 / not stated | [dark-elves.md](dark-elves.md) |
| Skaven | Mysza World 4 | 8 | 2000 | 15/15 | 1999 / not stated | [skaven.md](skaven.md) |
| Vampire Counts | The Old World @ LGT | 4 | 2000 | 13/13 | 2000 / not stated | [vampire-counts.md](vampire-counts.md) |
| Daemons of Chaos | Durham GT: Middenheim Massacre | 27 | 2000 | 8/8 | 2000 / 2000 | [daemons-of-chaos.md](daemons-of-chaos.md) |
| Ogre Kingdoms | IWC Presents: Nurgles Carnevil 2k Warhammer Old World Adepticon Primer | 6 | 2000 | 11/11 | 1998 / not stated | [ogre-kingdoms.md](ogre-kingdoms.md) |
| Lizardmen | Sunday Old World Singles by East Warrington Gaming | 3 | 2000 | 11/11 | 2000 / not stated | [lizardmen.md](lizardmen.md) |
| Chaos Dwarfs | War in the Heartlands Act 4 | 1 | 2000 | 10/10 | 2000 / 2000 | [chaos-dwarfs.md](chaos-dwarfs.md) |
| Grand Cathay | Summer Smash 2026 - The Old World 2000pt GT | 1 | 2000 | 10/10 | 1999 / 1999 | [grand-cathay.md](grand-cathay.md) |

## App issues found and addressed

- Ally/mercenary characters were treated as campaign Characters for the preview and points logic. The builder now retains their source profile type for points math and assigns them the Allied/Mercenary campaign role.
- Faction percentage limits and matched-play point thresholds/repeat scaling used points already added rather than the configured points limit. These checks now use the selected army limit.
- Composition-specific availability could hide options whose dataset uses a composition-keyed object instead of a string/array. The builder now handles all three dataset forms.
- Added basic checks for multiple Battle Standard Bearers, the Tomb Kings Hierophant (including the Mortuary Cults General requirement), and a non-Wizard Vampire Counts General.
- **Still needs interactive verification:** option-by-option UI selection and app-calculated list points. The standalone app also does not yet cover every specialized faction validation from the full Old World Builder. Each fixture states its source-specific test status.

## Sources

Public list text links to its source record on [Old World Rankings](https://oldworldrankings.com/). Profile paths refer to the cloned [Old World Builder](https://github.com/nthiebes/old-world-builder), credited in the roster app and `ATTRIBUTION.md`.
