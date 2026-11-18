# Conquest Quest Matchups: Mordheim Interludes

## Scope

The current [Conquest rules](Conquest.md#quests) list **four** quests, rather than five:

1. [Search for the Artefact](Conquest.md#search-for-the-artefact)
2. [Master of Magic](Conquest.md#master-of-magic)
3. [Defend Your Realm](Conquest.md#defend-your-realm)
4. [Scout Fertile Lands](Conquest.md#scout-fertile-lands)

This is the thematic matchup guide for Mordheim interludes between Old World battles. It pairs the two armies' active Conquest goals with scenarios that can tell the story of their collision. The quest goals below are narrative framings, not extra Mordheim rules or changes to Conquest quest progress/rewards.

## Attacker vs. defender grid

Rows are the **attacker's active quest**; columns are the **defender's active quest**. Each cell gives the scenario and a directional story hook, so swapping the armies may lead to a different scenario.

| Attacker's quest ↓ / Defender's quest → | Search for the Artefact | Master of Magic | Defend Your Realm | Scout Fertile Lands |
| --- | --- | --- | --- | --- |
| **Search for the Artefact** | [Hidden Treasure](Mordheimer_Scraped/campaigns/scenarios/mordheim-rulebook/hidden-treasure.md) — attacker reaches a cellar first; defender contests the chest. | [The Item Lost](Mordheimer_Scraped/campaigns/scenarios/town-cryer/the-item-lost.md) — relic hunters seize the wand sought by the defending wizard. | [Defend the Find](Mordheimer_Scraped/campaigns/scenarios/mordheim-rulebook/defend-the-find.md) — attackers assault a defended treasure site. | [Breakthrough](Mordheimer_Scraped/campaigns/scenarios/mordheim-rulebook/breakthrough.md) — relic hunters force their way through the scout-held route to the ruins beyond. |
| **Master of Magic** | [The Item Lost](Mordheimer_Scraped/campaigns/scenarios/town-cryer/the-item-lost.md) — the mage's agents pursue a wand currently held by the relic-searching defenders. | [The Great Library](Mordheimer_Scraped/campaigns/scenarios/fanatic-online/the-great-library.md) — the attacking scholar raids a library whose tomes are already being gathered by the defender. | [The Wizard's Tower](Mordheimer_Scraped/campaigns/scenarios/archive-pestilen/the-wizards-tower.md) — the mage assaults a tower held by the realm's defenders to claim its arcane secrets. | [The Item Lost](Mordheimer_Scraped/campaigns/scenarios/town-cryer/the-item-lost.md) — the wizard's warband tries to take a magical object from scouts who found it in the field. |
| **Defend Your Realm** | [Defend the Find](Mordheimer_Scraped/campaigns/scenarios/mordheim-rulebook/defend-the-find.md) — the realm's force attacks a ruin where rival treasure hunters have established a foothold. | [The Wizard's Tower](Mordheimer_Scraped/campaigns/scenarios/archive-pestilen/the-wizards-tower.md) — the defender's tower is a strategic strongpoint; the attacking army moves to secure it. | [Occupy](Mordheimer_Scraped/campaigns/scenarios/mordheim-rulebook/occupy.md) — the attacker tries to seize buildings in territory held by the defender. | [Surprise Attack](Mordheimer_Scraped/campaigns/scenarios/mordheim-rulebook/surprise-attack.md) — the realm's force raids a scout patrol before it can map the approaches. |
| **Scout Fertile Lands** | [Breakthrough](Mordheimer_Scraped/campaigns/scenarios/mordheim-rulebook/breakthrough.md) — scouts push through the treasure hunters' line to reach uncharted ground. | [The Item Lost](Mordheimer_Scraped/campaigns/scenarios/town-cryer/the-item-lost.md) — the scouts have found the wand; the attacking wizard's band tries to retrieve it. | [River Watch](Mordheimer_Scraped/campaigns/scenarios/fanatic-magazine/river-watch.md) — the scouts attempt a night crossing past the defender's guarded border. | [Street Fight](Mordheimer_Scraped/campaigns/scenarios/mordheim-rulebook/street-fight.md) — the attacking scouts try to force a passage through a route held by rival scouts. |

The attacker/defender labels are narrative roles for choosing and framing the encounter. Follow the selected Mordheim scenario's own setup and victory conditions; where it does not assign attacker and defender, use the labels only to establish who initiated the encounter and what each side wants.

## Three-scenario pools for the campaign generator

The web campaign generator uses [`Conquest_Mordheim_Scenario_Pools.json`](Conquest_Mordheim_Scenario_Pools.json), which defines **three thematic scenario choices for every directed attacker-quest / defender-quest cell**. Some scenarios appear in multiple pools, but no scenario appears in more than four of the 16 cells. The Markdown grid above remains the first-choice pairing and directional story hook; its scenario is included in the matching JSON pool.

When a campaign is generated, the app shuffles every cell's three scenarios. At each Mordheim node it draws from the pool for the current quest pair and roles, avoiding any scenario already used in that campaign when an unused option is available. This handles role changes caused by Old World results while keeping the random selection reproducible for the saved campaign.

Scenario title, hook, quest objectives, and thematic boon are displayed from the selected scenario. Follow that scenario's published setup and victory conditions; the campaign's quest mark/completion rules are tracked separately.

## Using this between Old World games

- Treat the selected Mordheim scenario as a short narrative interlude between two Conquest battles.
- Use each army's active quest as the story motive; the listed hooks can be adapted to the factions and campaign location.
- Unless a later campaign rule says otherwise, Mordheim outcomes do **not** add Conquest quest points, Gold, renown, injuries, or casualties. Resolve Conquest progress only under the existing rules after a Conquest battle.
- The selected scenarios are existing Mordheim scenarios from the local scrape; use their own rules as written, subject to any mutually agreed campaign adaptation.
