# Project Instructions

## Mission
Create an original, usable SWADE setting toolbox for the StarCraft universe. Prioritize fictional lore and playable tabletop encounters over copying RTS statistics.

## Governing documents
- `development/DESIGN-CHARTER.md`: setting goals and mechanical philosophy.
- `lore/CANON-POLICY.md`: source classification and adjudication.
- `development/RESEARCH-PROTOCOL.md`: research entry requirements.
- `development/DECISION-LOG.md`: precedents and settled adaptation choices.
- `development/ROADMAP.md`: work sequence; development status is not approval.

## Required working sequence
1. Identify the tabletop use case or research question before building a stat block.
2. Consult `lore/SOURCE-REGISTRY.md`, then primary source material where available.
3. Record **discrete claims** with source ID and exact locator, evidence type, perspective, relevant era/variant, confidence, and continuity status. Distinguish source text from inference.
4. Check apparent conflicts for different in-universe eras, designs, unreliable narrators, and the difference between gameplay mechanics and storytelling.
5. Reuse SWADE core and applicable Companion rules before proposing any new subsystem. Cite book + printed page in research notes; do not reproduce large excerpts.
6. If new mechanics are necessary, specify the concrete fictional behavior missing from core rules, the least complex alternative, and anticipated table consequences.
7. Compare a new NPC/creature against existing published examples; benchmark interactions at infantry, vehicle, and starship scales.
8. Record resolution and tests in the decision log. Only then mark a rule or profile `approved`.

## Source handling
- A source's authority tier is not a claim's confidence or whether its narrator is reliable.
- The original 1998 StarCraft manual is foundational P1 evidence; later explicit revelations may qualify or supersede its claims without deleting them.
- Games' campaign narrative and cutscenes are P1; RTS damage, build time, range, supply costs, unit slots, and gameplay scale **are not** diegetic engineering specifications.
- Novels and published narrative comics may be canonical P2, not automatically discarded.
- Reference books and developer corrections can resolve narrowly defined questions despite their default P3 label.
- Licensed tabletop material, crossover games, multiplayer/co-op abstractions, fan estimates, and unused concepts are not automatically StarCraft canon.
- Preserve unresolved contradictions and rejected hypotheses; never silently invent a reconciliation.

## Separation of concerns
- `lore/` stores fictional claims and citations, **not** adopted RPG mechanics.
- `rules/`, `equipment/`, `bestiary/`, `vehicles/` store conversions grounded in lore.
- `references/` stores research datasets/working measurements with provenance.
- `development/` stores original design rationale, status, and playtest findings.
- Campaign-ready archetypes and NPC profiles are conveniences, **not character classes**.

## Status labels
Research: `unresearched`, `collecting`, `disputed`, `reviewed`.
Game design: `idea`, `draft`, `playtest`, `approved`, `superseded`.
Do not equate a completed Markdown file with reviewed canonical or tested mechanical content.

## Repository hygiene
No copyrighted PDFs, book scans, ripped art, or lengthy verbatim lore passages. Reference locally available SWADE books by title/page. Avoid invented source URLs, unit metrics, dates, page numbers, or citation locators. Mark unknowns honestly. Preserve user-authored measurements as historical working data, not verified canon. Do not invent an open-source license without project-owner approval.
