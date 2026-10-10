# Cross-Project Mechanical Design Policy — Savage StarCraft ↔ SWADE for Foundry

**Status:** Adopted design-method integration, 2026-10-10. **Not** adoption of Foundry house rules or any StarCraft weapon statistics.

## Projects have different jobs

| Workspace | Owns | Does not establish |
| --- | --- | --- |
| [Savage StarCraft](https://github.com/bigbadbuffalo/savage-starcraft) | StarCraft lore interpretations, campaign assumptions, StarCraft-specific mechanics and stat blocks, playtest/approval decisions | Unconditional rules for every SWADE world |
| [SWADE for Foundry](https://github.com/bigbadbuffalo/swade-foundry-workspace) | Reusable mechanical design doctrine, independent house-rule catalogs, Foundry implementation and automation | Canonical StarCraft lore or mandatory StarCraft equipment statistics |

**No automatic two-way sync.** A prospective reusable SWADE mechanic may become an upstream Foundry proposal *after* proving its use, but neither repository is modified in the other project's name by default.

## Reference authority (do not conflate the layers)

1. **What is true in StarCraft:** `lore/CANON-POLICY.md`, its registered Blizzard sources and individual evidence. Foundry mechanics do not establish facts about StarCraft.
2. **What SWADE actually says:** Core Rules, then the mechanically relevant Companion/official general source, including any explicit updates. Published rules are RAW; do not relabel custom rule text as RAW.
3. **How to design in SWADE:** the Foundry workspace's Design Principles and Homebrew Design Framework as a **recommended production method**. This process complements this repository's Design Charter.
4. **What Savage StarCraft uses:** this repository's approved decision log, setting rules, profiles and playtest findings. A different project may choose different equipment power bands or constraints.
5. **How to automate it:** Foundry implementation follows accepted tabletop behavior and must not silently alter it.

## Relevant Foundry documents (live links; consult current main before use)
- [Design Principles](https://github.com/bigbadbuffalo/swade-foundry-workspace/blob/main/docs/SWADE_for_Foundry_Design_Principles.md) — Fast/Furious/Fun and SWADE source hierarchy, domain-based Companions, explicit rules-status terms.
- [SWADE Homebrew Design Framework](https://github.com/bigbadbuffalo/swade-foundry-workspace/blob/main/docs/process/SWADE_HOMEBREW_DESIGN.md) — scope, mechanical home, delivery/effect, resources, defenses, scaling, counterplay, lifecycle, provenance and testing. This is an **analytical grammar, not a universal point-buy tool**.
- [Modular Weapon Design Playbook](https://github.com/bigbadbuffalo/swade-foundry-workspace/blob/main/docs/process/MODULAR_WEAPON_DESIGN_PLAYBOOK.md) — how to keep base weapon, technology, payload, compatible ammunition, and behavior in their natural mechanical home.
- [Weapons Research Playbook](https://github.com/bigbadbuffalo/swade-foundry-workspace/blob/main/docs/process/WEAPONS_RESEARCH_PLAYBOOK.md) — high-recall SWADE mechanic search, contextual costs and evidence matrix.
- [Weapons Total-Conversion Design Doctrine](https://github.com/bigbadbuffalo/swade-foundry-workspace/blob/main/docs/mechanics/weapons/WEAPONS_TOTAL_CONVERSION_DESIGN_DOCTRINE.md) — **important non-portability warning**: Foundry's weapon catalogs are balanced together as a closed equipment ecosystem.
- [Weapons Workstream Status](https://github.com/bigbadbuffalo/swade-foundry-workspace/blob/main/docs/development/weapons/WORKSTREAM_STATUS.md) — re-check current stage before citing completion or copying a property.
- Optional mechanical precedents: [Sci-fi ranged](https://github.com/bigbadbuffalo/swade-foundry-workspace/blob/main/docs/mechanics/weapons/SCIENCE_FICTION_RANGED_WEAPONS.md), [Sci-fi special](https://github.com/bigbadbuffalo/swade-foundry-workspace/blob/main/docs/mechanics/weapons/SCIENCE_FICTION_SPECIAL_WEAPONS.md), [launcher-delivered ordnance](https://github.com/bigbadbuffalo/swade-foundry-workspace/blob/main/docs/mechanics/weapons/SCIENCE_FICTION_LAUNCHER_DELIVERED_ORDNANCE.md), [ammunition](https://github.com/bigbadbuffalo/swade-foundry-workspace/blob/main/docs/mechanics/weapons/AMMUNITION_RULES.md), [shared weapon properties](https://github.com/bigbadbuffalo/swade-foundry-workspace/blob/main/docs/mechanics/weapons/WEAPON_PROPERTIES.md).

**Snapshot checked:** Connected GitHub contents were reviewed on 2026-10-10. The Foundry weapon status then identified modern, science-fiction and shared-property final integration steps 1–3 as closed; weapon modifications/construction/materials as Step 4 in progress/next. **Do not treat this snapshot as perpetual state.**

## Adopted process: nine questions before new mechanics
1. **Intended fiction:** What does the thing *actually do*, and what meaningful player decisions result?
2. **Existing rules:** Can SWADE Core or the specialist Companion already portray it accurately?
3. **Natural home:** Is it a background, Edge, Power/Trapping, equipment base profile, ammunition/payload, mode, integrated system, environmental hazard or creature feature?
4. **Delivery and effect:** Attack roll? Trait check? Evasion? Template? A persistent effect? Separate how it reaches the target from the result.
5. **Cost and constraint:** Power Points, ammunition, Rank, actions, rarity, compatible host, minimum Strength, mobility, risk of failure, training or resource burden.
6. **Defense interactions:** Armor/AP, Heavy Armor/Heavy Weapon, cover, Soak, shields, anti-vehicle eligibility, damage type, countermeasures.
7. **Peer/power-band comparison:** Compare *both* published mechanical precedent and chosen StarCraft-era peers, not RTS relative damage.
8. **Counterplay and lifecycle:** Does the effect expire, reload, recharge, degrade, get repaired, or have a tactical response? Omit bookkeeping with no payoff.
9. **Test and label:** Document RAW vs interpretation vs adaptation vs house rule; test both ordinary and extreme targets; only automate after tabletop approval.

Use the above questions proportionally: a basic grenade does not need a ten-page lifecycle analysis. The goal is **fewer, clearer rules**, not a larger design bureaucracy.

## Very important: non-portability of the Foundry weapon catalogs
The Foundry project's `WEAPONS_TOTAL_CONVERSION_DESIGN_DOCTRINE.md` explicitly balances weapon entries inside a *closed* catalog. A copied Damage/AP/Range/Shot count could be inappropriate beside stock SWADE Core/Sci-Fi Companion equipment and StarCraft-specific enemies. It may also rely on modified ammo classes, shot feeds, payload compatibility, costs or property definitions.

**Before adopting anything, choose a coherent mechanical baseline:**
- **Default starting assumption:** SWADE Core + Science Fiction Companion gear and rules, adjusted where necessary for StarCraft fiction.
- **Permitted alternative:** adopt a carefully delimited Foundry-derived rule or a deliberately coherent total-equipment baseline *as a separately logged StarCraft choice* after comparing all relevant neighbors.
- **Never by accident:** take Foundry's closed-ecosystem stat numbers but continue to price/balance everything as unmodified Core without identifying the mismatch.
- **Don't import Foundry's staged development workflow as mandatory StarCraft bureaucracy.** Its source-mining and critique practice is reusable; its gate status belongs to that project.

A discrete reusable **procedure** (for instance host/payload ownership, compatibility accounting, or property terminology) may be adapted without adopting its catalog statistics, but must still have its context costs and interactions assessed.

## Recording cross-project precedent
For each reused concept record:

```yaml
starcraft_entry: ""
sourced_starcraft_behavior: ["SC98-MANUAL p. XX"]
swade_raw_precedent: ["Core pp. XX", "Science Fiction Companion pp. XX"]
foundry_reference:
  repo: bigbadbuffalo/swade-foundry-workspace
  path: docs/process/SWADE_HOMEBREW_DESIGN.md
  examined_commit: "<actual checked SHA>"
  role: "design method | candidate mechanic | imported property | implementation"
rules_status: "RAW | interpretation | adaptation | house_rule | foundry_only"
starcraft_adoption: "not_adopted | candidate | playtest | approved"
compatibility_and_original_costs: "..."
decision_id: ""
```

For the Foundry reference, **record the actual SHA inspected** when a numerical mechanic or property is materially used; use living links for process documents.

## Public/private and rights boundary
The Foundry repository may be private; links may not resolve for everyone reading this public StarCraft repository. This file therefore summarizes the necessary methodology **self-contained**. Do not copy private project catalogs or copyrighted Pinnacle sourcebook text wholesale into this public repository. A public StarCraft rule must be understandable and usable without privileged access to the other workspace.

## First application
[Terran Infantry Benchmark](benchmarks/TERRAN-INFANTRY-BENCHMARK.md): C-14 gauss weapon, CMC infantry armor, specialist anti-armor and target-scale tests. Research first; no immediate numerical import.
