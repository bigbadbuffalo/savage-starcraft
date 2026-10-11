# Three-Faction Ground Combat — Protoss Conversion Audit Matrix

**Date:** 2026-10-11. **Status:** Audit/test scenarios **only**; no actual tabletop sessions were played and no chosen shield system is owner approved.  
**Inputs:** `../../bestiary/protoss/README.md`, SFC p.42 Personal Force Field, p.122 Light Duty Power Armor, p.123 Shields, p.50 Psi Blade, p.93 Heavy Metal; current Terran C-14/CMC and 6 Zerg organism playtest entries.

## Protection counterfactuals
| Test | Expected RAW/class behavior | Critical uncertainty |
| --- | --- | --- |
| C-14 ClassI / AP4 / 2d10 vs **Zealot option A (ordinary +6 Armor, +4 field)** | Normal rolled damage, physical armor effectively +2 after AP4; base Vigor d10 Toughness **17** field on, **13** off | Does a Zealot survive closing to melee long enough against 2 Marines? |
| C-14 vs **Zealot option B (Size1 Light Duty +8 ordinary Armor, +4 field)** | Normal rolled damage, effective Armor+4 after AP4; Toughness **19** on, **15** off, Pace **12** from frame | May be too fast/durable; native rules at least give Mod accounting rather than invented Strength |
| C-14 ClassI vs **Zealot option C full Heavy +8/ClassI** | Heavy Metal **1d3 Wounds per hit**, +1 on attack raise. PFF +4 Toughness doesn't change those direct Wounds | Strong numerical shield on paper can be irrelevant to classed fire if using wrong model |
| C-14 ClassI vs **Stalker Heavy +8/ClassII** | Normally **0 Wounds**, +1 with attack raise (SFC Heavy Metal). Candidate B rechargeable shield **may Soak** Class Wounds with Electronics charges | Whether Stalker should be ClassII and whether 2 charges are justified |
| **Zealot enhanced ClassII blade** vs Marine ClassI / Marauder ClassII | **Marine 1d3+1**, **Marauder 1d3** direct Wounds, +1 on Fighting raise; original printed **SFC Psi Blade is only ClassI** | Is powered +1 Strength plus AP8/ClassII too deadly on high Fighting? |
| **Standard Psi Blade ClassI** vs Marauder ClassII | Normally **0**, **1 on Fighting raise** | Does printed sword fail too dramatically at vehicle-cutting fiction? |
| **Stalker ClassII Disruptor** vs Marine I / Firebat II | **1d3+1** / **1d3**, before Soak; single RoF1 attack | Does powerful anti-armor ranged walker compete well with Marauder? |
| **Adept ClassI Glaive** vs Marine I / Marauder II | **1d3** / **0 except raise→1** | Are Adept anti-light and movement sufficiently different? |
| **High Templar Core Blast without Heavy Weapon** vs Marine Heavy Armor | Regular power **cannot** affect Heavy Armor if it does not qualify as Heavy Weapon | Should psionic storm's Trapping be a deliberately **ClassI HW effect**, and how to limit blast lethality? |
| **High Templar Blast with custom HW ClassI** vs Marine I | **1d3** per affected qualifying hit (+1 raise) before Soak, **3 PP** each use | Possibly brutal mass Wound scaling; cannot assume every psychic power becomes HW |
| **Sentry Core Barrier** vs Zerglings / Banelings | Physical **Hardness10**, wall 5\" long, height1\" (2 yards), 2PP duration5; attacks and explosion may breach | RTS Massive bypass **not same** as SWADE Huge/Size; check geometry and material effects |
| **Protoss +4 field vs Baneling ClassII acid** | Unclassed Zealot protection resolves **ordinary rolled 4d8/AP4**, with field +4; if wearing Classed suit direct Class resolution, **PFF +4 doesn't reduce direct Wounds** | Shields should defend acid and explosive shock, not just ballistics |
| **Zealot ClassII blades** vs Ultralisk ClassIII Heavy | Normally 0, +1 Wound on Fighting raise; enormous Scale / Reach / Sweep counters | Does lore suggest concentrated Zealots can kill one without tank weapon assistance? |
| **Protoss field vs EMP** | SFC personal field battery or electronic charged shield should interact with official StarCraft **EMP shield collapse**; exact interface not chosen | Beware EMP deleting both shield and all personal Psionic PP with no basis |

## Systemic risks and clarifications
1. **Armor vs shield**: With ordinary armor the shield's +4 Toughness helps, but not finite depletion. With Heavy Metal Class armor it doesn't negate direct Class Wounds, so the SFC p.123 Soak shield may be essential. Don't stack both models by default.
2. **Physical suits:** Blizzard actually calls Zealot equipment **power armor**, and an SFC **Size1 Light Duty** chassis reproduces powered Strength and movement **without Heavy Armor**, at an explicit Mod price. This is a promising RAW alternative still unselected.
3. **Psionic ecology:** The SFC **Telepathy ancestry 1 point** grants communication, not automatic Arcane Background 3 powers/10PP; Templar/elite/Nerazim abilities are paid/specialist. Post-Khala Protoss are not a hive mind.
4. **Stalker/Sentry** are machines, use **Construct** traits and Repair rather than normal natural Healing, but are not all vehicles; no universal vehicle Out of Control.
5. **Dragoon** is a true walker, not a Zealot with a stronger chest plate; defer to vehicle subsystem with anti-particle disintegration weapon.
6. **Scale:** Source maps do not prove a humanoid Protoss's natural SWADE Size. Provisional Size0 keeps Normal Scale for first integration; future dimensional research may change that.
7. **Active psi weapons**: Heavy Metal Class from actual defined attack damage/AP, not temporary PP or variable strength buffs without recording how the class changes.

## First linked scene designs
1. **Melee gap:** One Zealot versus two Marines across 20–30 yards with cover; compare both physical armor A/B and PFF shield, time to engagement, Wounds/Soak.
2. **Squad support:** Zealot + Sentry + Adept vs Marine + Marauder + Firebat; measure barrier placement, Cover, AP, Foam Soak and ranged vs melee opportunities.
3. **Psionic storm:** One High Templar Wild Card behind Zealots vs a fireteam, compare normal Core Blast vs custom HW-ClassI option and PP sustainability. Don't treat each cast as free.
4. **Baneling counterplay:** Sentry barrier against Baneling attack, whether acid damages shield layer or physical armor, Zergling pack routes.
5. **Hunter killer pursuit:** Stalker with and without costed Blink facing ClassII Marauder AP+concussive; compare shield models and Escape/Soak.
6. **Nerazim infiltration:** Cloaked Dark Templar versus scanner-backed Terran guards; assess invisibility power, stealth, heavy armor blade, and counterdetection.
7. **Heavy biological threat:** Protoss unit plus antimat/rocket vs Ultralisk III; test whether Zealots do too little while ClassII Stalker support contributes.

**Follow-up decision:** Owner selects Zealot chassis option (ordinary battlegear vs SFC Light Duty power armor) and shield model (SFC Personal Force Field +4 vs rechargeable charged shield). All other stats remain provisional until integrated test; do not demand final approval of every profile to move to vehicle and PC packets.
