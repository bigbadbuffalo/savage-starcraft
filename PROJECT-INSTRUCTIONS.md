# Project Instructions

## Mission
Create an original, usable SWADE setting toolbox for the StarCraft universe. Prioritize fictional lore and playable tabletop encounters over copying RTS statistics.

## Governing documents
- `development/DESIGN-CHARTER.md`: setting goals and mechanical philosophy.
- `lore/CANON-POLICY.md`: source classification and adjudication.
- `development/RESEARCH-PROTOCOL.md`: research entry requirements.
- `development/CROSS-PROJECT-MECHANICS-POLICY.md`: how SWADE for Foundry's reusable design doctrine informs (but does not control) StarCraft mechanics.
- `development/DECISION-LOG.md`: precedents and settled adaptation choices.
- `development/ROADMAP.md`: work sequence; development status is not approval.

## Required working sequence
1. Identify the tabletop use case or research question before building a stat block.
2. Consult `lore/SOURCE-REGISTRY.md`, then primary source material where available.
3. Record **discrete claims** with source ID and exact locator, evidence type, perspective, relevant era/variant, confidence, and continuity status. Distinguish source text from inference.
4. Check apparent conflicts for different in-universe eras, designs, unreliable narrators, and the difference between gameplay mechanics and storytelling.
5. Reuse SWADE core and applicable Companion rules before proposing any new subsystem. For substantial mechanical design, consult the live [SWADE for Foundry design principles](https://github.com/bigbadbuffalo/swade-foundry-workspace/blob/main/docs/SWADE_for_Foundry_Design_Principles.md) and [homebrew design framework](https://github.com/bigbadbuffalo/swade-foundry-workspace/blob/main/docs/process/SWADE_HOMEBREW_DESIGN.md) as **methodology**, following `development/CROSS-PROJECT-MECHANICS-POLICY.md`. Cite book + printed page in research notes; do not reproduce large excerpts.
6. Identify the mechanic's natural home (character ability, equipment, ammunition/payload, mode, condition, hazard, vehicle system, or other existing SWADE category). Consider dependencies, resource costs, action economy, defensive interactions, counterplay, failure, and limits. If a novel rule remains necessary, explain why existing rules fail and estimate the gameplay cost.
7. Compare a new NPC/creature against existing published examples; benchmark interactions at infantry, vehicle, and starship scales.
8. Record resolution and tests in the decision log. **A coherent equipment profile can be accepted provisionally and marked `playtest` before any standalone tabletop test** when the fiction, SWADE precedent, assumptions and dependencies have been audited. Assemble a complete functional playtest packet first; conduct integrated scenario and regression tests before promoting individual statistics to `approved`.

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
**`playtest` means provisionally accepted baseline, usable at the table and still subject to revision; it does not imply a playtest has already occurred.** Document whether a playtest actually ran separately.
Do not equate a completed Markdown file with reviewed canonical or tested mechanical content.
**Integrated packet plan:** `development/INTEGRATED-PLAYTEST-PACKET.md`. Design whole combat/ecology and character option sets before tuning single equipment entries.

## Repository hygiene
No copyrighted PDFs, book scans, ripped art, or lengthy verbatim lore passages. Reference locally available SWADE books by title/page. Avoid invented source URLs, unit metrics, dates, page numbers, or citation locators. Mark unknowns honestly. Preserve user-authored measurements as historical working data, not verified canon. Do not invent an open-source license without project-owner approval.

## Cross-project boundaries
- **StarCraft canon:** `lore/CANON-POLICY.md` and cited Blizzard sources determine setting truth; SWADE for Foundry is **not** StarCraft lore authority.
- **SWADE rules:** the Core Rules and relevant Companion(s) remain RAW authority. The Foundry workspace contributes a reusable **design method**, not automatic RAW or compulsory house rules.
- **StarCraft decisions:** this repository's Design Charter, adopted mechanical decisions and playtests determine what this conversion uses. The Foundry project may make different balance tradeoffs.
- **Foundry integration:** only after tabletop rules are selected. Never let a module or automation constraint silently change the tabletop mechanic.
- Check the Foundry repository's **current** `main` state, especially its workflow/status, before citing a specific weapon property or number. Its sci-fi equipment catalog is explicitly a closed total-conversion ecosystem; values and ammunition architecture are not presumptively portable.
- Do not write to the Foundry repository as a side effect of StarCraft adaptation. If a genuinely reusable upstream change is desirable, raise it as a separate proposal.
- When the Foundry repository is inaccessible, apply the summarized procedure in `development/CROSS-PROJECT-MECHANICS-POLICY.md`; avoid silently assuming unseen rules or implementations.
