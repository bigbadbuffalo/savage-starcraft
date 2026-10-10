# Research and Adaptation Protocol v0.1

## For a lore claim
1. Define one factual question, not an entire undifferentiated topic.
2. Add the original work to `lore/SOURCE-REGISTRY.md`.
3. Seek primary material and register the exact location (page, mission, dialogue scene, timestamp, developer article section).
4. Paraphrase the claim faithfully; note if it is character dialogue, in-world technical intelligence, an event seen on screen, or an out-of-world statement.
5. Record era, faction, model/strain, and dimensional axis where applicable.
6. Search for an independent corroboration or apparent contradiction.
7. Assign **tier**, **evidence type**, **continuity status**, and **confidence** independently.
8. Link any dispute; never silently smooth over a contradiction.
9. Update the source claim when better evidence is found, preserving prior values and change history.

## For a SWADE conversion
1. State fictional intent in 2–3 lines (what players experience).
2. Identify which core and Companion rules already cover it, with printed-page references when available.
3. Produce a minimum viable mechanical implementation. Separate permanent traits, training, and detachable equipment.
4. Establish scale: small arms, anti-armor, heavy weapon, armor, colossal/spacecraft; identify impossible or impractical attacks.
5. Test representative enemies and PCs, including realistic tactics, combined-arms solutions, and noncombat interactions.
6. Check exceptional cases: Wild Cards vs Extras, templates, Special Abilities, area attacks, and vehicles.
7. Publish an independent GM-ready profile plus optional underlying player-build guidance.
8. Record balance/lore compromises in `development/DECISION-LOG.md`.

## Minimum claim entry fields
`claim_id`, `proposition`, `source_id`, `locator`, `source_tier`, `evidence_type`, `perspective`, `applies_to`, `continuity_status`, `confidence`, `rationale`.

## Review and workflow states
Research: unresearched -> collecting -> disputed/reviewed.
Mechanics: idea -> draft -> playtest -> approved/superseded.
Mark unresolved questions rather than treating them as blocks to other independently testable work.

## Methodological grounding
*World Builder & Game Master's Guide*, printed pages 3–11, especially **Converted Settings** on pp. 10–11: preserve themes, avoid bloated conversions, reuse existing abilities, and compare monsters/Extras with published examples. *SWADE Vehicle Guide*, printed pp. 4–6: obtain fictional hard data where possible, but use Size/volume/target-profile benchmarks as flexible starting points rather than exact conversion formulae.

## Reusing SWADE for Foundry's design grammar
Follow `development/CROSS-PROJECT-MECHANICS-POLICY.md` when designing substantial equipment, powers, armor, monsters, machines, or new Setting Rules.

1. Establish the **fictional effect**, player choices, and use cases; do not start from a preferred numerical profile.
2. Search all relevant SWADE mechanical locations (Core, applicable Companion, gear, Edges, Powers, creature abilities, hazards, conditions, and Setting Rules).
3. Identify the natural **mechanical home**: base hardware, ammunition/payload, installed subsystem, personal ability, Trapping, situational mode, environmental hazard, etc.
4. For borrowed mechanisms, document **original context cost** (Power Points, Rank, Edge opportunity cost, capacity, ammunition, cooldown, setup, rarity, or narrative scarcity). Do not import a benefit free of those constraints by accident.
5. Evaluate host/payload compatibility, stacking, target defenses, Heavy Armor/Heavy Weapon eligibility, and action economy; define counterplay and lifecycle only where it matters in play.
6. State whether the implementation is **RAW**, **interpretation**, **adaptation**, **house rule**, or **Foundry implementation**, and whether a rule is `idea`, `draft`, `playtest`, or `approved`.
7. Compare *both* published SWADE precedents and any carefully chosen Foundry project precedent; the latter's closed-catalog numbers are diagnostic, not automatically StarCraft balance targets.
8. Write the tabletop procedure before Foundry automation. Record what was actually tested.

### Required mechanical provenance
Each substantial conversion record should identify the **published SWADE book/page** (where available), any **Foundry repo path + commit** used as precedent, how that idea was adapted, its original economy or power-band assumptions, and the specific StarCraft decision that approves or defers it.

### First candidate
See `development/benchmarks/TERRAN-INFANTRY-BENCHMARK.md` for the C-14 / powered armor / anti-armor mechanical research setup. It is not an approved weapon catalog.
