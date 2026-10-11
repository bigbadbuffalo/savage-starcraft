# Savage StarCraft — Integrated Playtest Packet: Build-First Policy

**Status:** Active scope and delivery contract, adopted 2026-10-10.  
**Goal:** Build a **coherent set of usable rules, equipment and opposition**, then stress-test *their interactions together*. Do not block the next weapon, armor, ancestry, power, creature or vehicle on an isolated combat trial of the prior item. **This is not a demand to enumerate all StarCraft RTS units, eras, named weapons or capital ships before any tabletop testing.**

## Decisions already locked
- The owner's priority is **breadth of playable options and representative interactions before balance polish**. Plausible numbers can enter **`playtest`** status; only the complete packet undergoes the main integration/approval pass.
- **Core SWADE + Sci-Fi Companion** remain the numerical/mechanical references; cross-project Foundry mechanics are methodological precedents only.
- Published Heavy Metal weapon/vehicle Classes and fixed equipment Class for powered armor, normal character Soak, one suit Critical Hit per independently wounding attack and no vehicle-only Out-of-Control for a wearer are established in `rules/SETTING-RULES.md`.
- The StarCraft fiction—not RTS health, armor and damage—determines each role; interactions can be asymmetrical and deadly.
- **Accepted provisional baseline:** C-14 Impaler **30/60/120, 2d10, AP4, RoF3, Shots100, Min Str d10, Wt20, Heavy Weapon/Class I**, plus a flagged optional 3RB test mode; standard Marine CMC-300/400 **+10 Heavy Armor / fixed Class I**, CMC-660 Firebat **+14 Heavy / Class II**, Marauder 5-4 **+16 Heavy / Class II**. These are original RPG values, not canon engineering specs. **Not yet approved as final game rules**.

## Definition of a complete first *functional* playtest set
Every row must have **rules-consistent provisional stats and clear dependencies**, not just a lore summary. A named canonical item/organism can be represented by an existing published SWADE profile **only if the fit is stated and any mechanical differences are justified**.

| Workstream | Playable inclusions required before integrated balance testing | Cross-system questions |
| --- | --- | --- |
| **A. Terran infantry arsenal** | C-14 standard rifle; standard sidearm/civilian rifle; one close-range weapon; CMC-300/400; CMC-660 + flame projector; Marauder 5-4 + launcher/ordnance; one genuine Class II anti-materiel infantry option; one larger anti-armor/explosive option | Infantry lethality, Ammo/AP vs Class, Recoil/weapon attachment, blast vs Heavy Armor, cover and suppression |
| **B. Terran support and survival** | Medic protection/medical shield and field treatment; field scanner/comms; engineer/Repair/Electronics/demolition kits; stim delivery as clearly selected *mechanic or deferred module*; NBC/vacuum; at least one everyday nonpowered armor profile | Noncombat agency, healing time, support, power/fine-motor restrictions, action economy |
| **C. Zerg opponent ecology** | Zergling, Hydralisk, and at least one tougher or unusual organism; one infestation/creep hazard; coordinated vs isolated swarm encounter guidance | Natural attacks vs Heavy Armor, vulnerability to C-14, pack tactics, survival under suppression; **do not automatically give creatures Vehicle Class** |
| **D. Protoss cross-faction parity** | Zealot-scale warrior, ranged specialist and psionic support example; psionic/energy shield design; personal defense, melee and ranged attacks | Distinguish ablative/recharging shields vs Armor Class, psionics resource, power asymmetry, Terran ballistic interaction |
| **E. Vehicle and scale anchor** | One light ground vehicle or SCV, one armored walker or APC, one tank/heavy emplacement, and a Class III+ or much heavier reference for nonpenetration; a spacecraft/warship **scale sanity check**, not a full fleet system | Heavy Metal/no-effect floor, personal-vs-vehicle damage, passenger protection, specialist ordnance and environmental hazards |
| **F. Characters and combined encounter packet** | Five distinct Terran PCs built from one stated creation budget; representative enemy Extras/Wild Cards; at least one combined Marine/heavy/specialist encounter, Zerg swarm encounter, Protoss confrontation, hazardous-planet exploration/medical problem, and vehicle/evacuation scene | Full action economy, Bennies/Soak, Wounds, critical effects, multiple independently resolved hits, cover, skills outside combat |

## Work order: deliberately build whole interactions
1. **Finish the Terran *equipment ecology***, not merely rifle-vs-armor. Give Firebat weapons, Marauder ordnance, anti-armor responses, medics, sidearms, field tools and demolition meaningful stats. Preserve the existing C-14/CMC line unchanged unless an obvious published-rules contradiction is found.
2. **Design Zerg and Protoss equivalents** under the same Heavy Metal/Heavy Armor assumptions. Use P1 or other sourced material for each rather than assuming armor-class symmetry. Do not automatically classify natural carapaces as power armor.
3. **Add a few representative vehicles and a scale comparison**, establishing the boundary between bullets, penetrators and actual anti-vehicle weapons. No need to finish all starships.
4. **Build the PC and NPC kit plus connected scenarios**, then run the complete combat/skill/terrain package as a linked series of sessions or encounter tests. Record actual rolls/results and fixes.
5. **Revise in batches** for systemic defects (too-lethal fire, too many critical-hit rolls, shields overpowering armor, anti-vehicle crossover), then review profiles for final `approved` status.

## Acceptance and tracking policy
- `draft`: Proposed numerical design, not yet owner-accepted as a table reference.
- `playtest`: **Provisionally accepted table reference**, even if its dedicated session test has **not** yet occurred. Record when a numerical field is unsupported by original fiction (for example C-14 Shots100, Wt20, Range).
- `approved`: Finalized after complete-package compatibility checks and documented tests/review; approval must be explicit.
- No bogus test claims: existing 300,000-action Monte Carlo study is a **probability diagnostic**, not a campaign playtest.
- When a new subsystem's plausibility depends on an unbuilt counterpart, record the dependency and continue rather than repeatedly rebalancing the first item.
- Keep original rules/lore precedents and the accepted provisional values side by side; when revising, leave a clear changelog rather than silently retconning earlier decisions.

## Focus: what is **not** a prerequisite
A complete Protoss PC ancestry, every Ghost ability, all Reaper models, all Zerg mutations, the full starship catalog, an exhaustive unit encyclopedia, and Foundry implementation are **later expansion**, except to the limited degree required by the representative playtest packet above. The first test set should be broad enough to expose *faction interactions* and combined arms, not encyclopedic.

**Next authoring work:** **Terran specialist and support equipment** — CMC-660 flamethrower and thermal defense, 5-4 Marauder launcher, Class II anti-materiel rifle candidate, a verified portable explosive/launcher, Medic protection/healing, standard sidearm and field support tools. Bundle their numbers into consistent profiles **before** another equipment-balance review.

## Kinetic Foam approval (2026-10-10)
The project owner approved a **single-slot +2 Vigor Soak bonus against kinetic/concussive impacts** as a custom Power Armor Mod, in `../equipment/terran/KINETIC-FOAM-MODIFICATION.md`. This is a finalized rule choice for the provisional packet (no free Soak or Armor/Class change), **not an assertion that all Marauders carry it**. Add at least one foam-equipped Marauder to eventual integrated tests, alongside an unmodified baseline, and leave the rest of the equipment program moving.

## Size 3 heavy-suit chassis and proposed heat Mod (2026-10-10)
**Firebat CMC-660 and Marauder 5-4 now use owner-approved Size 3 frames** (nine Mod slots, Pace 4, Strength d12+2), retaining the previously accepted provisional +14/Class II and +16/Class II protective lines. Integrated twin flame/launcher mounts must be budgeted when stats are written; both families retain room for upgrades. The Firebat's **Fire-Resistant Insulation** Mod is **draft only**, inspired by Core Environmental Resistance (Heat), and no subtract-four-from-Heavy-Metal-Wounds rule is adopted. See `../equipment/terran/CMC-POWER-ARMOR-DRAFT.md` and `../equipment/terran/FIRE-RESISTANT-INSULATION-DRAFT.md`.

## First playable heavy infantry weapon package (2026-10-10)
The Firebat's **Fire-Resistant Insulation** has been **provisionally accepted** as 1 Mod with the Core Environmental Resistance (Heat) effect. Complete mounted weapon playtest entries now exist for [twin Perdition flamers](../equipment/terran/PERDITION-FLAMETHROWERS-PLAYTEST.md) and [paired Quad K12 launchers](../equipment/terran/QUAD-K12-PUNISHER-PLAYTEST.md), with 2 forearm weapon Mod slots each. **Primary equipment insight:** SFC **Armor Piercing warhead** (p.93) lowers target Heavy Metal Class by one if Armor 10+, so the Marauder gets anti-Class-II lethality without an innate Class II gun. The optional concussive slowing shell, fabrication rate, foam issue policy, custom burn-versus-Class resolution, and full suit costs remain unfinished but **do not block** the next packet workstream. Next: ordinary/specialist Terran weapons and Medic/support equipment, or Zerg ground fauna.
