# Development Roadmap

**State:** Phase 1 foundational policy scaffold complete; Phase 2 has begun with a first-pass manual audit and campaign/pilot requirements. Research and mechanics advance iteratively.

| Phase | Objective | Completion gate |
| --- | --- | --- |
| 1. Foundations | Approve charter, canon policy, research protocol, registry, initial continuity disputes | A documented process, at least two test cases, and explicit unresolved questions — **initial version complete** |
| 2. Campaign envelope | Identify themes from primary sources; define campaign styles, PC concepts, era choices and pilot requirements | **Draft documents created**, player-creation assumptions to be reviewed |
| 3. PC toolbox | Ancestries/backgrounds, professions as examples, Edges/Hindrances, psionic eligibility | Characters can be built without classes; mixed-party issues documented |
| 4. Equipment and powers | Terran, Zerg, and Protoss combat, support, and engineering equivalents | **Coherent provisional ground-play packet**, not item-by-item approval |
| 5. Minimal setting rules | StarCraft-specific exceptions to SWADE only where required | Concise player reference with rationale and examples |
| 6. Pilot profiles | Bestiary, vehicles and opposing equipment sufficient for the complete test packet | Representative roles across all three factions and threat scales |
| 7. Integrated testing | Run a set of connected infantry, survival, combined-arms and opposed-faction encounters, including Silent Colony | Document pace, difficulty, lethality, scale, feedback and revisions across the *whole packet* |
| 8. Systematic expansion | Faction bestiaries, variants, groundcraft, aircraft, spacecraft | Lore-source and mechanical consistency reviews |
| 9. Campaign book | Savage Tales, optional Plot Point Campaigns, detailed settings and NPCs | GM can run sessions from the material |

## Research and development queue
- [x] Adopt lore-first, SWADE-first toolbox approach.
- [x] Establish initial source and dispute structure.
- [x] Register original 1998 manual and the main narrative releases.
- [x] Seed acknowledged continuity error and apparent-contradiction examples.
- [x] Complete **first-pass thematic audit** of the original 1998 manual (pp. 26–90 selected/indexed).
- [x] Draft Phase 2 campaign framework and pilot requirements.
- [x] Integrate SWADE for Foundry's general mechanical design methodology with explicit cross-project independence.
- [x] Prepare a sourced preliminary Terran infantry equipment benchmark and interaction matrix (**no approved stats**).
- [x] Investigate C-14 weapon class: direct original-manual evidence, later-source leads and a SWADE Heavy Weapon/Heavy Armor hypothesis; **not yet approved**.
- [x] Record approved Setting Rules package and unresolved Heavy Metal/power-armor scope.
- [x] Draft modular CMC family with candidate Armor and C-14 comparison, no approved profiles.
- [x] **Approve fixed Heavy Metal Class as an equipment attribute of power armor**, unaffected by wearer's Vigor; prioritize testing very lethal Marine-on-Marine class combat.
- [x] Confirm ordinary SWADE character procedures remain unchanged; do not introduce a redundant Soak rule.
- [x] **Approve one power-armor Critical Hit roll per independently wounding attack (not per Wound)** and no vehicle-only Out-of-Control check for individual suit wearers, following the Core vehicle Critical Hit precedent.
- [x] **Numerical Monte Carlo diagnostic** of Class I/II Marine-vs-Marine and heavy-infantry firefights, including RoF, raises, cover and recoil; recorded at `development/benchmarks/HEAVY-METAL-INFANTRY-FIRE-TEST.md`.
- [x] **Accept C-14 and CMC first-pass numbers as provisional `playtest` baselines**; no isolated encounter gate is required before work on the rest of the catalog.
- [ ] **Assemble the linked functional playtest packet** described in `development/INTEGRATED-PLAYTEST-PACKET.md`.
- [ ] Run integrated tabletop encounters with Soak, Bennies, suit Critical Hits, cover, team movement, biological attacks, shields and specialists; **then** decide which CMC/C-14 numbers need adjustment.
- [ ] Complete detailed sequential unit/structure entries for the 1998 manual.
- [ ] Obtain/audit Brood War manual and index story changes.
- [ ] Compile individual novel/comic bibliography with precise provenance.
- [ ] Choose pilot campaign's exact era, faction sponsor, and starting Rank.
- [ ] Resolve disputed dimensions in historical Unit Sizes sheet.
- [x] Produce first **fully specified draft** C-14 and CMC suit family (all values provisional) and comparative Heavy Metal specialist ladder; published in `equipment/terran/`.
- [ ] Promote C-14 / CMC item statistics to **final `approved`** after whole-packet testing, lore verification of variants and comparison to the other factions.
- [ ] Build five sample PCs from the **provisional** baseline, including combat and noncombat roles.
- [ ] Conduct end-to-end pilot playtest and revise.

## Design recommendation
Proceed with **a focused Terran frontier slice first**, while maintaining a setting-wide toolbox that permits later Protoss/Zerg and other campaigns. Research facts and mechanics stay separate.

See: `lore/research/SC98-MANUAL-AUDIT.md`, `development/CAMPAIGN-FRAMEWORK.md`, `development/PILOT-REQUIREMENTS.md`.

## Cross-project reference
The companion [SWADE for Foundry workspace](https://github.com/bigbadbuffalo/swade-foundry-workspace) provides a detailed general-purpose Homebrew Design Framework and modular weapon design methods. Savage StarCraft **adopts methodology only**, not the Foundry project's different equipment baseline or house rules by default. See `development/CROSS-PROJECT-MECHANICS-POLICY.md`.

## Working baseline and integration gate (owner direction, 2026-10-10)
Do **not** stop development at each plausible weapon or suit to demand a standalone test. Put sufficiently grounded values in `playtest` status, explicitly mark unresolved canon numbers as placeholders, and build out the **full functional test packet** before the main tuning cycle. Keep the `Silent Colony` pilot as an early adventure application, **not** a cap on the broader ground-combat equipment/creature roster. **Next content priority:** Terran infantry ordnance, support gear and attacks (Firebat and Marauder), then Protoss defenses/psionics and Zerg creature baselines, then vehicles and encounter-level cross-faction tests. See `INTEGRATED-PLAYTEST-PACKET.md`.
- [x] Review **officially licensed StarCraft TMG** public unit-card ranges and targeting tags as **comparative design evidence**, not canonical ballistics; see `references/STARCRAFT-TMG-COMPARISON.md`.

- [x] Distinguish in-lore kinetic-foam shock absorption from drug-based **Trauma Pack**; research a Soak-compatible custom Kinetic Foam Mod while preserving existing Toughness/Ballistic Protection RAW options. See `development/benchmarks/MARAUDER-KINETIC-FOAM-STUDY.md`.
- [x] **Approve Kinetic Foam Mod**: 1 slot, +2 to Vigor Soak against physical kinetic/concussive Wounds, normal Benny and Heavy Metal interface; `equipment/terran/KINETIC-FOAM-MODIFICATION.md`.
- [x] Select **provisional Firebat Fire-Resistant Insulation** via Core Environmental Resistance (Heat): 1 Mod, +4 hazard checks, −4 rolled fire damage, no direct Heavy Metal Wound reduction.
- [x] Create **paired first-pass Perdition / Quad K12 Heavy Weapon playtest profiles**, including linked mounts, ammo and SFC p.93 Armor Piercing warhead mechanics; `equipment/terran/PERDITION-FLAMETHROWERS-PLAYTEST.md` and `QUAD-K12-PUNISHER-PLAYTEST.md`.
- [x] Owner supports **multi-ammunition Quad K12** and a simpler **Sloth-like Concussive slow** (distinct from full SFC Time warhead). Explicitly correct SFC p.60's **lack of Armor Piercing** on the default grenade launcher list; preserve Punisher AP as **K12-specific equipment compatibility adaptation**, see `equipment/terran/K12-AMMUNITION-PLAYTEST.md`.
- [ ] Finalize Firebat thermal/weapon fuel variants, K12 Concussive Shell trigger/size balance and ammo-fabrication/storage Mods **during integrated packet build**, not as isolated tuning gates.

- [x] **Owner approves Size 3 for Firebat CMC-660 and Marauder 5-4** with current +14/+16 Heavy/Class II provisional protection unchanged; update suit Pace/Strength and nine-slot budgets. See `development/benchmarks/POWER-ARMOR-FRAME-SIZING-STUDY.md`.
- [ ] Review **Fire-Resistant Insulation**, the 1-Mod **draft** based on Core Environmental Resistance (Heat): +4 to resist heat/fire hazards, −4 conventional fire damage, no automatic direct Heavy Metal Wound reduction. See `equipment/terran/FIRE-RESISTANT-INSULATION-DRAFT.md`.
