# Canon and Continuity Policy v0.1

**Purpose:** Determine what StarCraft sources establish, where statements conflict, and what the SWADE project may responsibly infer. **This is a project research hierarchy, not an official Blizzard tier system.**

## Two distinct questions
1. **Canon eligibility:** Did Blizzard publish narrative information intended as part of the StarCraft universe?
2. **Evidence priority:** How persuasive is that specific statement for the claim under examination?

Blizzard's Creative Development Q&A Part 6 described released games, novels, manga, etc. as official continuity, while explicitly excluding mods and tabletop RPGs; it also acknowledged actual continuity errors. Treat this as important historical guidance, not a perpetual guarantee for every future product or mode: see SRC-BLIZZARD-CDEV-06 in the registry.

## Default research priority (P1–P4)
| Tier | Material | Default use |
| --- | --- | --- |
| **P1 — Primary narrative** | StarCraft (1998) and Brood War; StarCraft II campaign releases and related in-game story/cinematics/dialogue; official game manuals, especially the original 1998 StarCraft manual | Baseline story, institutions, culture, technology, and history; gameplay abstraction excluded |
| **P2 — Published narrative expansion** | Official StarCraft novels, comics, manga, canonical short stories, and Blizzard-published narrative animation outside the campaigns | Canonical narrative evidence, not inherently false or disposable |
| **P3 — Official reference / commentary** | Field Manual; Blizzard lore articles, primers, official encyclopedic materials and developer lore Q&As | Specialized technical evidence, summaries, clarifications and explicit error corrections; assess narration/perspective |
| **P4 — Provisional inspiration** | Heroes of the Storm crossover content, noncanonical/co-op modes and cosmetic variants, unused concepts, licensed tabletop RPGs, promotional material, and gameplay-only values | Research leads and design inspiration, never canon solely by appearance here |

**N — Noncanonical or unsupported** is a **claim disposition**, not a fifth source tier. It encompasses original fan material, disproven claims, and unsupported extrapolations. An N claim can be retained for traceability.

A source may have different entries or tier treatment depending on the *specific material*: a campaign cinematic is P1 narrative; a multiplayer balance patch is not P1 physical evidence. Cite precisely.

## Why priority is not an absolute trump card
A P1 scene showing an object against an unknown backdrop does not establish precise dimensions. A P3 specification may be much better dimensional evidence. Explicit later storytelling may reveal that an earlier source conveyed an in-universe misunderstanding. A direct Blizzard correction may dispose of a narrow contradiction even when it comes from P3 commentary. Never promote *every* assertion of that source merely because one correction is credible.

## Claim record dimensions
Record these independently:
- `source_id` and **exact locator** (printed page, mission and briefing, scene/timecode, issue/page, article section, or URL).
- `evidence_type`: explicit statement; witnessed event; in-universe belief; illustrative depiction; inference; dimensional estimate; gameplay-only; adaptation invention.
- `perspective`: omniscient/expository; named character; propaganda/intelligence file; unknown.
- `continuity_status`: established; disputed; qualified; superseded; era/variant-specific; noncanonical; unverified.
- `confidence`: high; medium; low, with justification.
- `applies_to`: era, faction, model/strain, scope and conditions when known.
- `recorded_at`, and decision/adjudication links when present.

Source tier **does not equal confidence**; repeated unsourced fan claims are not independent corroboration.

## Conflict resolution procedure
1. **Normalize the claim.** Are sources actually addressing the same time, prototype, sub-strain, ship class, unit, and measurement axis?
2. **Separate narrator from fact.** Could one account be an in-world belief, biased report, or incomplete intelligence?
3. **Differentiate narratives from systems.** RTS cost/range/HP, hitbox size, multiplayer or co-op balance, ability cooldowns, and player convenience are not diegetic physics.
4. **Locate all direct support.** Prefer first-hand official text/scene over wiki summaries. Use community wikis as finding aids with links back to originals.
5. **Seek express corrections.** Log official clarifications and acknowledgments of errors.
6. **Adjudicate narrowly.** Decide only the minimum supported claim. Do not automatically erase older assertions or create harmonizing explanations.
7. **Preserve dispute history.** Document conflicting statements, dates, variants, and the chosen interpretation or unresolved status.
8. **Keep conversion choices separate.** If an RPG requires a number not firmly established, document a usable *game value* without claiming it is canon.

## Special cases
- **Foundational manual:** The 1998 manual is P1, a primary historical source for original world building; do not treat it as automatically infallible over explicit later revelations.
- **Field Manual:** Official reference, but often presented as Dominion intelligence/commentary. Excellent specialist evidence, but distinguish stated specification, perspective, and limits.
- **Cinematics/art:** A scene's event may be canonical while measured proportions remain artistic/inferred.
- **Crossovers:** Heroes of the Storm establishes Nexus fiction, not a transferable StarCraft chronology or new technology automatically.
- **RTS abilities:** A unit's fictional existence may be P1; a balance-driven cooldown or weapon damage value is not.
- **Tabletop RPGs:** Excluded by Blizzard's cited Q&A unless a specific fact is independently confirmed elsewhere.
- **Adaptation-only inventions:** Clearly label as Savage StarCraft interpretation.

## Amendments
Any change to tiers or a high-impact dispute must be entered in `development/DECISION-LOG.md` with reasons and primary evidence. Amendments do not silently rewrite original source records.

## Immediate test cases
See `lore/disputes/thor-chronology.md`, `lore/disputes/xelnaga-history.md`, and `references/unit-sizes.md`.
