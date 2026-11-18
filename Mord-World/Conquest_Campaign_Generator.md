# Conquest Challenge Campaign Generator (Draft)

## Goal

Turn a challenge between two Conquest rosters into a short, branching story that mixes **three or four total games** of The Old World and Mordheim. Each player chooses one active Conquest quest after accepting the challenge. The quest pair selects Mordheim scenarios from the [quest matchup matrix](Conquest_Mordheim_Quest_Matchups.md); game results choose the next branch, set attacker/defender, and can affect quest progress or the next Old World battle.

This is an optional campaign layer. It does not change roster construction, Old World battle results, or the rules of the selected Mordheim scenarios. Agree before starting whether to use the quest and boon rules below.

## Challenge and setup

1. A roster challenges another roster. The challenged player accepts or declines.
2. After acceptance, each player chooses one of the four standard quests: Search for the Artefact, Master of Magic, Defend Your Realm, or Scout Fertile Lands. Record any quest target/reward as usual.
3. Roll a D6 for campaign length: **1–3 = three games; 4–6 = four games**.
4. Roll a D4 for a campaign shape from the matching list below. Both game systems appear in every shape.
5. Each Mordheim game uses the players' quests and current attacker/defender roles to select its scenario and hook from the matchup matrix.

### Campaign shapes

`M` means a Mordheim game; `O` means an Old World battle. Roll a D4 to choose a shape, or let the players choose one if they prefer a particular story rhythm.

| Length | D4 | Shape | Story rhythm |
| --- | --- | --- | --- |
| 3 | 1 | **M–O–M** | Skirmish opens the conflict; Old World result sets up the final raid. |
| 3 | 2 | **O–M–O** | Old World clash leads to a Mordheim interlude and a decisive battle. |
| 3 | 3 | **M–M–O** | Two linked street-level operations shape the final Old World battle. |
| 3 | 4 | **O–M–M** | Old World battle opens the route to a two-part Mordheim finale. |
| 4 | 1 | **M–O–M–O** | Alternating escalation; both Mordheim victories can shape an Old World battle. |
| 4 | 2 | **O–M–O–M** | Opens on the battlefield and ends with a decisive skirmish. |
| 4 | 3 | **M–O–O–M** | A Mordheim discovery fuels two Old World clashes before the final raid. |
| 4 | 4 | **O–M–M–O** | Old World opener, linked Mordheim missions, then a final battle. |

Set fallback roles at campaign start: the challenger attacks and the challenged player defends. For a Mordheim game following an Old World battle, that battle's winner becomes the defender (holding the ground) and the loser becomes the attacker. On a draw, retain the current roles. Consecutive Mordheim games keep the same roles; consecutive Old World battles use the latest result to set roles for the next Mordheim game.

## Compact campaign tree

Generate the next game from the selected shape and the current node's recorded result; do not pre-write every possible branch. This keeps the tree small and makes a random generator straightforward.

```text
Accepted challenge; quests locked; length and shape selected
└─ Battle 1 (type from shape)
   ├─ Player A wins ─┐
   ├─ Player B wins ─┼─ record result, progress, and any earned thematic boon
   └─ Draw ──────────┘
      └─ Battle 2 (next type from shape; use prior result if relevant)
         ├─ Player A wins ─┐
         ├─ Player B wins ─┼─ record result and update campaign state
         └─ Draw ──────────┘
            └─ Battle 3 (next type from shape)
               ├─ Result branches update roles, quest marks, or a pending boon
               └─ If length 3: winner of final game claims the campaign; a draw is contested
                  └─ If length 4: Battle 4 (final game; resolve any pending boon)
                     ├─ Player A wins → A claims the campaign
                     ├─ Player B wins → B claims the campaign
                     └─ Draw → campaign is contested
```

The tree has three or four battle nodes, following the rolled shape. Each node has three result edges (`A wins`, `B wins`, `draw`); edges update campaign state and lead to the next node rather than expanding into a full tree of duplicated battle cards. Re-check the matchup matrix at each Mordheim node because a preceding Old World result may have swapped attacker and defender.

## Mordheim outcomes

Resolve the chosen published scenario as written. Record its normal winner and whether each player's scenario objective was achieved. A draw does not automatically mean both objectives were achieved.

For each Mordheim node, show each player's quest-specific motive alongside their attacker/defender role and the matchup-matrix hook. The scenario objective remains the published victory condition; the displayed quest motive explains how achieving it advances the player's campaign. A win earns a Campaign Quest Mark for Search for the Artefact, Master of Magic, or Defend Your Realm; a draw earns one only if that player achieved the scenario objective. Scout Fertile Lands requires both an achieved objective and a route-, crossing-, scouting-, or territory-themed matchup. Display whether each player received progress after the result is recorded.

### Old World quest objectives and points

At every Old World node, display both players' actual side-objectives from their chosen Conquest quests and record their progress independently of the battle winner:

- **Search for the Artefact:** 1 quest point for each friendly unit wholly within the opponent's territory at battle end.
- **Master of Magic:** 1 quest point for each friendly Wizard casting roll of 8+ during the battle.
- **Defend Your Realm:** 1 quest point for each friendly unit wholly within the player's territory at battle end.
- **Scout Fertile Lands:** complete the quest if any friendly unit is wholly within 4″ of a battlefield edge and wholly outside the player's territory.

For each of the first three quests, a player may spend 1 Gold at the end of the battle for 1 additional quest point. For Scout Fertile Lands, 1 Gold can complete the quest instead. Report the number of points earned, resulting progress toward the three-point threshold, or quest completion and normal reward. The tracker starts from the roster's existing quest progress when the selected quest matches; campaign progress is shown separately, and players should update their roster Quest Logs and claim rewards there.

### Optional quest progress

Use separate **Campaign Quest Marks** so the interlude does not silently change the printed Conquest aftermath steps:

- A player earns one mark for winning a Mordheim game, or for achieving their scenario objective in a draw.
- A mark can be recorded as **one quest point** toward Search for the Artefact, Master of Magic, or Defend Your Realm. Quest progress still cannot exceed the quest's normal completion threshold.
- For Scout Fertile Lands, a mark completes the quest only if the Mordheim scenario's objective involves scouting, crossing, or securing a route/territory and that player achieves it. Otherwise the mark is narrative only.
- On completing a quest, award its normal printed reward. Marks do not award Gold, exploration rolls, renown, injuries, casualties, or territory by themselves.
- If the group does not want Mordheim to advance official quests, keep marks as narrative tokens and use the boons only.

This is an explicit optional exception to the current matrix document's default that Mordheim outcomes do not add Conquest quest points or rewards.

### Thematic boon for the next Old World game

A Mordheim victory creates a boon from the selected scenario's theme, not from a random boon roll. The quest pair selects the matchup-matrix scenario; its theme deterministically selects the effect below. On a draw, nobody receives a boon. A boon lasts for the next Old World game only, cannot stack, and never changes its victory conditions. If more than one Mordheim game occurs before the next Old World battle, only the **last Mordheim game before it** creates that battle's boon; earlier games still affect quest marks and the story.

| Matrix scenario | Theme | Thematic boon for the next Old World battle |
| --- | --- | --- |
| Hidden Treasure; The Item Lost; Defend the Find; Wyrdstone Hunt; Defend the Tomb; Tomb Raid; Haunted Treasure; The Gauntlet | Relic recovered | **Recovered relic:** choose one friendly unit. Once this battle, it may claim a 6+ Regeneration save. |
| The Great Library; The Wizard's Tower; The Lost Temple of the Slann; Gift of the Truthsayers; The Ogham Stones | Arcane knowledge | **Arcane insight:** one friendly Wizard may re-roll one failed casting roll. If no Wizard is included in the next Old World army, one friendly unit may instead re-roll one failed Panic test (the spell's protective ward steadies it). |
| Breakthrough; River Watch; Finders Keepers; Through Black Fire Pass; Rescue | Route discovered | **Forward scouts:** before deployment, choose one friendly non-Character unit. Up to D3 models in it gain the Scouts special rule for this battle. |
| Occupy; Defend the Oasis; The Watchtower; Defend the Village!; Protect the Prince | Ground secured | **Rallying cry:** choose one friendly unit. Once this battle, it may re-roll one failed Panic test. |
| Surprise Attack; Encampment Raid | Enemy plans disrupted | **Spoiled orders:** choose one enemy non-Character unit. It cannot make a move during the first turn (it can still make compulsory moves). |
| Street Fight | Close-quarters tactics | **Readied counter:** choose one friendly unit. Once this battle, it may re-roll one failed charge roll. |

The effect is selected by a fixed scenario-to-theme mapping—never by rolling or choosing from a generic boon list. Generate a bespoke name and one-sentence description from the scenario's story hook and the winner's quest, but do not add extra mechanics. For example, a Search for the Artefact victory in **The Wizard's Tower** might produce *The Tower's warding charm* (Arcane insight); a Scout Fertile Lands victory in **Breakthrough** might produce *Maps of the hidden pass* (Forward scouts). A campaign may omit quest progression and still use these boons.

## Random generation recipe

This is enough to generate a campaign with a few dice and the existing matrix; no bespoke scenario-writing or random boon table is needed.

1. Record the two roster names, players, chosen quests, and campaign location.
2. Roll campaign length (D6: 1–3 gives three games, 4–6 gives four), then roll a D4 on the matching campaign-shape table.
3. At campaign generation, shuffle the three scenario options in every directed quest-pair cell from `Conquest_Mordheim_Scenario_Pools.json`. Follow the shape from left to right. Before each Mordheim game, set attacker/defender from the latest Old World result (or use challenger/challenged if no Old World game has happened yet), then draw from that quest-pair pool. Avoid scenarios already played in this campaign when an unused option is available.
4. After each game, record winner/draw and any scenario objective achieved. Apply eligible quest marks. If a Mordheim game has a following Old World battle before another Mordheim game, create the winner's boon from the matrix scenario's fixed theme mapping.
5. After each Old World game that is followed by Mordheim, set the winner as defender and the loser as attacker. On a draw, preserve the current roles.
6. The winner of the final game claims the campaign; a draw leaves it contested. Write an epilogue from the final result and any completed quests.

For software, store the rolled shape as a short array such as `[M, O, M, O]` and a shuffled scenario deck for each of the 16 quest-pair cells. Each battle node has three result edges (`A wins`, `B wins`, `draw`), which update roles, quest marks, and any pending thematic boon before advancing to the next array entry. Generate only the next node when a result is entered; there is no need to pre-expand every possible branch. Record each game's result in both rosters' Battle Records and keep finished challenge trees in the campaign archive so past campaigns remain visible in the main Campaign view.

## Narrative text template

Use the matrix hook as the center of the story and fill in roster/player names and location. No additional lore table is required:

> Seeking **{Player A quest}**, **{Player A roster}** has entered **{location}**. **{Player B roster}**, pursuing **{Player B quest}**, stands in the way. The clash at **{matrix scenario}** will decide who holds the initiative. After **{battle result}**, **{next game's setup or boon}** changes the course of the campaign.

For the epilogue, name the final winner or call the objective contested, then mention any quest completed. This keeps generated stories coherent without adding a large library of hand-authored branches.

## Example (three-game route)

Player A chooses **Search for the Artefact** and challenges Player B, who chooses **Defend Your Realm**. Roll a three-game **O–M–O** shape. The Old World opener's winner becomes defender; the loser attacks in Mordheim, and the matrix selects a scenario for their quest pair and roles. If A wins the Mordheim game, A can gain a quest mark and receives the boon associated with that scenario's theme, narrated using the story hook and A's quest. The winner of the last Old World battle claims the campaign; a draw leaves it contested. If the shape had been **M–M–O**, both Mordheim results could affect quest progress, but only the second mission would determine the boon for the Old World finale.

## Playtest questions

- Does one Mordheim win per game advance quests too quickly? If so, let a mark require both winning and achieving the scenario objective.
- Are the six scenario-based boon effects appropriately small for the group's battle size and edition?
- Should completed quests grant their normal rewards during this mini-campaign, or should quest marks be narrative-only?
