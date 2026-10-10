# Phase 2 — First Playtest Requirements v0.1

**Working pilot:** *The Silent Colony*  
**State:** Requirements specification, not a completed module or numerical rules set.  
**Design dependency:** `development/CAMPAIGN-FRAMEWORK.md`. Lore backing: `lore/research/SC98-MANUAL-AUDIT.md`. Mechanical method: `development/CROSS-PROJECT-MECHANICS-POLICY.md`.

## 1. Purpose
Test the smallest complete package that makes a Terran StarCraft adventure recognizably StarCraft and recognizably SWADE. We will not build entire factions before checking one working slice.

**Hypotheses:**
1. Modular character skills/Edges and detachable equipment cover infantry and specialist identities without bespoke “Marine/Firebat classes.”
2. Published SWADE weapons/armor/Heavy Weapon/Heavy Armor concepts preserve the distinction between people, power-armored troops and heavy targets with minimal adjustments.
3. Zerg feel dangerous through group tactics, biological traits, sensors, Creep/terrain, and coordinated action rather than simply high hit points.
4. Extraction, medical decisions and investigation make an adventure play well even when killing every enemy is impossible.

## 2. Playtest PC roster (build later, no adopted stats yet)
- Infantry veteran / squad leader: small arms, Leadership, tactics, possible suit.
- Combat engineer or SCV technician: Repair, Electronics, demolitions; civilian/industrial skills useful.
- Combat medic: Healing, survival, triage and communications.
- Recon specialist / colonial marshal: Notice, Stealth, persuasion/intimidation, tracking.
- Pilot/logistics or corporate liaison: Piloting, support, negotiation, navigation.

**Character creation gate:** Set one starting Rank and common budget; establish legal character options, equipment access and training requirements. No Ghost PC required in first test. Keep equipment separate from personal Traits.

## 3. Minimum equipment catalog
| Item / system | Lore anchor | SWADE adaptation task |
| --- | --- | --- |
| Ordinary frontier firearm / sidearm | Appropriate Terran civilian/military setting; specifics still to source | Establish human-scale reference using SWADE stock firearm |
| C-14 family gauss weapon | SC98-MANUAL p. 35 | Range/damage/AP/ROF/ammunition baseline; avoid treating “maximum penetration” prose as ignoring all Heavy Armor |
| CMC powered infantry suit | SC98-MANUAL p. 35 | Suit-based Armor, environment seals, life support, encumbrance, vulnerabilities |
| Heavy Firebat suit and arm-mounted flame weapons | SC98-MANUAL p. 35 | Modular special-purpose gear and flame Trappings; no class prerequisite |
| Stim delivery system | SC98-MANUAL p. 36 | Effects, duration, aftereffects and whether existing SWADE mechanics suffice |
| Explosives / anti-armor launcher | Military setting rationale; exact model and source **not yet verified** | Heavy Weapon/AP interactions; ensure availability makes tactical sense |
| Diagnostic, repair and field medical kits | SC98-MANUAL pp. 34, 39; generic SWADE/Sci-Fi equipment | Support noncombat approaches, reduce dependence on custom subrules |
| Communications and scanners | Military/scout needs; obtain exact sources | Electronic/Notice tasks, signal interference, no arbitrary perfect detection |

**Minimum vehicles:** One basic ground transport or salvage industrial machine with appropriate rulebook precedent. Reserve a Goliath/Arclite tank for a later weapons scale test (SC98-MANUAL pp. 38–39). A battlecruiser is not necessary in the opening scenario, but must remain immune to implausible ordinary infantry attacks under the final threat model.

## 4. Minimum adversary/hazard set
| Concept | Fictional requirement | Status |
| --- | --- | --- |
| Zergling | Small, violent, pack-oriented assault organism, with burrowing possibility (SC98-MANUAL p. 57) | Research only |
| Hydralisk | Larger Zerg combat organism; verify natural weaponry in manual p. 58 before choosing damage | Research needed |
| Feral or isolated organism | Different command behavior from directed swarm (manual pp. 52, 55; Blizzard Q&A Part 6) | Research only |
| Overlord/remote swarm controller | Intelligent coordination and/or enhanced detection; source: manual p. 57 | Encounter role only; no initial ship-size stats |
| Brood-nest / Creep patch | Living ecological hazard and investigation clue, not merely combatants (manual p. 55) | Hazard definition needed |
| Terran rival/compromised security | Non-Zerg danger and political complication | Generic Extra can be reused |
| Colossal threat (optional) | Survival/avoidance/extraction rather than expected defeat with small arms | Scenario device, no full Ultralisk profile yet |

## 5. Encounter sequence (design sketch, not fixed adventure text)
1. **Briefing and approach:** mixed signals, contradictory sponsor orders, equipment decisions; use Networking or common roleplaying.
2. **Silent perimeter:** atmospheric indicators, strange biomatter, an abandoned security system; Notice/Science/Survival and investigation.
3. **First contact:** Zerglings or a small organism threat; evaluate Shooting, Fighting, cover, Shaken/Wounds, multiple Extras.
4. **Complication:** biological contamination and communication failure, conflicting survivors' testimony; Dramatic Task or Quick Encounter if apt.
5. **Decision:** rescue survivors, recover research, destroy the nest, or complete an urgent evacuation—mutually competing objectives.
6. **Extraction:** timed escape under pressure; test vehicles, Chases or Dramatic Tasks as needed.

## 6. Scale test matrix — *before* approving weapon statistics
| Attacker | Target | Expected fiction-level result to test |
| --- | --- | --- |
| Basic firearm | Unarmored human | Credible lethal threat |
| C-14 | Light infantry / Zergling | Dangerous in normal use, including suppression and automatic fire |
| C-14 | CMC armor | Armor meaningful, not literal immunity to a peer firearm |
| C-14 | Ultralisk / armored walker | Poor anti-armor solution except appropriate vulnerabilities/exceptional tactics |
| Anti-armor launcher / demo charge | Armored walker / large Zerg organism | Credible threat subject to placement, armor and tactics |
| Ordinary rifles | Behemoth battlecruiser | Not a mechanically viable way to destroy a capital ship through repeated HP depletion |
| Anti-ship systems | Warship | Resolve at starship/Chase/Clash/GM narrative scale when later implemented |

**Important:** These are benchmarks and intended outcomes, not assigned AP/damage values. SWADE heavy weapons and armor rules should be inspected and tested first; don't introduce a new universal “armor tier” until existing rules demonstrably fail.

## 7. SWADE sources and review checklist
- **SWADE Core Rules:** standard character creation, Edges, Traits, Shooting/Fighting, Bennies, Wounds, armor/AP/Heavy Weapon/Heavy Armor, Evasion, Dramatic Tasks, Quick Encounters, Fear, Chases and Mass Battles. Consult printed page for each final test.
- **Science Fiction Companion (2024):** Power Armor ch. 5 (p. 119 onward), Robots ch. 6 (p. 129), Vehicles ch. 8 (p. 163), Walkers ch. 9 (p. 179), Setting Rules ch. 3 (p. 77); select only needed modules.
- **Vehicle Guide (2020):** conversion vs construction, target profile/Size and comparative Handling, printed pp. 4–6.
- **World Builder & Game Master's Guide (2019):** themes, archetypes, iconic adventures and converted settings, pp. 3–11.

## 8. Playtest observation form
For every scene note: player goal; actual actions; rules used; time/round count; PC Wounds / Bennies; enemy behavior; any confusing mechanic; StarCraft feeling preserved or missed; unresolved interaction. After test, record **revision**, **reason**, and **game impact** in `development/DECISION-LOG.md`.

## 9. Exit criteria for first mechanical release
- Five sample PC concepts can be built from common rules.
- At least one military and one noncombat problem are fun and meaningful.
- Three tiers of target protection interact sensibly with personal and specialist weapons.
- No compulsory RTS-equivalent class or construction system needed.
- Zerg encounters differ based on context/coordination.
- Any new rules required are documented, short and tested.

## 10. Immediate next design task
The research and test procedure is now established in [Terran Infantry Benchmark](benchmarks/TERRAN-INFANTRY-BENCHMARK.md). Build a **Terran infantry equipment benchmark**, not an entire arsenal:
1. Human baseline and C-14 fictional design requirements.
2. Stock SWADE gun/armor precedents.
3. CMC armor protective behavior.
4. Anti-armor reference threat.
5. Three sample interactions and a short field test.

## 11. Cross-project equipment compatibility gate
The Foundry workspace maintains finalized sci-fi weapons in a separately balanced total-conversion ecosystem. **Do not mix** its Damage/AP/Range/weight/ammunition profiles and stock SWADE/Sci-Fi Companion gear without deciding and documenting a compatible StarCraft equipment baseline.

For the first pilot, benchmark published SWADE + Science Fiction Companion mechanics before considering Foundry substitutions. A selected Foundry rule or ammunition model remains a *candidate precedent* until adopted through the decision log and interaction tests. Foundry automation is outside this pilot's first rules approval gate.

## Armor-family and Heavy Metal test checkpoint
Use `development/benchmarks/CMC-ARMOR-STUDY.md` and `HEAVY-METAL-INTERFACE.md` when designing infantry benchmarks. The four-rule package, fixed power-armor Classes, **one suit Critical Hit roll per separately resolved attack that causes at least one Wound**, and exclusion of vehicle-only Out-of-Control checks for suit wearers are approved interpretations in `rules/SETTING-RULES.md`. **Actual C-14/CMC numbers and combat outcomes still require playtests.**
