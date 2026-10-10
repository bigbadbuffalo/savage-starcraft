# Terran Powered Infantry — CMC Family Draft

**Status:** **`playtest` provisional** for **CMC-300/400 +10 Heavy/Class I; CMC-660 +14 Heavy/Class II; Marauder 5-4 +16 Heavy/Class II**, accepted as plausible first-pass profiles by the owner (2026-10-10). Fixed-Class **rule** is approved. **No specific suit model is final/`approved`**. Medic alternatives and specialized thermal/ordnance details are still research/draft.  
**Date:** 2026-10-10.  
**Lore:** `lore/entries/terran/powered-combat-suits.md`; original SC98 manual p.35; *Stealing Thunder* (later P2 source, mirrored text partially read).  
**Rules:** Sci-Fi Companion Power Armor pp.119–127, Heavy Metal p.93; SWADE Core p.117.  
**Approved interface:** `rules/SETTING-RULES.md`; test results: `development/benchmarks/HEAVY-METAL-INFANTRY-FIRE-TEST.md`.

## Common CMC baseline
Use the **SFC Size 2** frame (p.122): **+10 Heavy Armor, Strength d12+1, Pace 6, six Mod slots, 200 lb unpowered, base $100K in generic SFC credits**. Price and weight are **published generic analogues**, *not* canon StarCraft unit costs or masses. All frames inherently have optics/HUD, communications, enhanced hearing, environmental sealing, life support and a three-day power supply (SFC pp.119–121); do not charge extra Mods for these. Sealing a suit for ordinary environment **is not automatically** the `Self-Sealing` Mod that handles breaches after Wounds.

Fixed Heavy Metal **Class** belongs to the **suit**, not the wearer's Vigor; permanently different protective redesigns can have their own Class. Character Wounds are Soaked normally. One **separately wounding attack** after Soak produces **one suit Critical Hit roll**, not one roll per Wound; separately wounding RoF attacks may cause multiple rolls. Vehicle Out-of-Control checks do not apply to an infantry wearer.

## Candidate suit table

| Suit / employment | Frame | Armor | Fixed Class candidate | Pace | Strength | Proposed Mods / budget |
| --- | --- | --- | --- | --- | --- | --- |
| **CMC-300 — ordinary Marine** | 2 | **+10 Heavy** | **I** | 6 | d12+1 | Scanner (1); Self-Sealing (1); Stabilizer **only if a compatible weapon attachment exists** (1). **3/6** maximum listed |
| **CMC-400 — updated Marine** | 2 | **+10 Heavy** | **I** | 6 | d12+1 | CMC-300 baseline plus Integrated Gear (drug-delivery **hardware**, not free drug effects) (1): **4/6** maximum listed |
| **CMC-660 — Firebat** | 2 | **+14 Heavy** | **II** | 6 | d12+1 | 2× Armor (2), Self-Sealing (1), conditional Stabilizer (1): **4/6** before thermal / flame systems |
| **5-4 Armored Infantry Suit — Marauder** | 2 | **+16 Heavy** | **II** | 6 | d12+1 | 3× Armor (3), Toughness +1 **optional candidate** (1), conditional Stabilizer (1): **5/6** before external launcher mount |

**All Armor/Class/Mod values here are test parameters**, not facts from Blizzard. Mods are not granted automatically from job title or RTS unit selection. Unlisted slots are not automatically filled. An external flamethrower or Punisher launcher should not be counted as `Integrated Gear` if it weighs over the **10-lb allowance** (SFC p.125); formal mounting needs its own equipment specification.

### What the ratings intentionally do
- Marine ↔ Marine: **Class I versus I** means ordinary C-14 hits can inflict **1d3 character Wounds**, potentially very lethal; published Soak and suit-critical-hit rules remain in force.
- Marine ↔ Firebat/Marauder: **Class I versus II** means ordinary C-14 hits cause **0**, raises **1 Wound**. They are harder to defeat with standard rifles, **not invulnerable**.
- Firebat vs Marauder: Both may be Class II, but are **not interchangeable**. Firebat's **heat/fire defense** is supported by original SC98 manual and must be built as an actual benefit rather than merely its Heavy Metal Class. Marauder's robust kinetic plating and arm-mounted **Punisher** ordnance are better supported by later fiction.
- A +1 Toughness Mod on the 5-4 affects ordinary SWADE Toughness against non-classed effects; it **does not dynamically push a fixed suit Class** to a different rating.
- **SFC Ballistic Protection** (p.123) reduces **slugthrower ordinary damage by 4**; under Heavy Metal's direct-Wounds procedure, there is no damage roll to subtract 4 from. **Don't buy this Mod as a magical anti-C-14 Class bump** without first verifying or explicitly extending it to Heavy Metal (which would be a new rule).
- **SFC Self-Sealing** (p.123) does **not** work when the wearer suffers **three or more Wounds from one attack**. Under lethal Heavy Metal fire, even well-maintained Marine armor can fail to maintain atmosphere after severe direct hits. Normal suit breach/Critical Hits apply.

## Medical protection — unresolved alternative
The original *Brood War* manual describes a UED Medic with medical equipment and protective shielding, not a definitive personal CMC rating. First test **+6 ordinary armor and shield/medical gear separately**, but do not assert that suit is environmentally sealed or powered merely because a Medic wears it. Alternate design: a **SFC Size 1 +8 Heavy Armor, Class I candidate** medical hardsuit with its own pace/Strength/Mods; requires more direct evidence and changes how threatening non-Heavy Weapons are. **Don't canonize an unverified CMC-405 model** from older RPG material.

## No hidden character class
Operators change suits if requisition/training/fitting allow it. A CMC-equipped soldier is not required to take a bespoke Marine Edge, and a non-Marine may wield a C-14 with the correct Strength/handling penalties.

## Questions before promotion
1. Can a standard carried C-14 engage the Stabilizer without an equipment-specific cradle? **No automatic assumption; prove attachment**.
2. Can the Firebat's thermal specialization use a published hazard/defense mechanic without custom class math?
3. Should default Marauder kinetic foam be a +1 Toughness Mod, Trauma Pack, or a variant specific to its chronology?
4. Verify comparative movement/physical Size and cost only with actual sources; **SFC Size 2 is a mechanical frame, not an observed lore height**.
5. Decide Medic protective model only after checking official depictions and equipment.

## Provisional acceptance and integration
Do not block the remaining roster on first-pass performance tuning: the table above is now the **working powered-infantry equipment baseline**. Normal Heavy Metal character interface and suit Critical Hits have already been approved separately. The Firebat's **thermal specialty**, Marauder **ordnance/foam**, and Medic **protective equipment choice** are still incompletely specified and **must be made playable** before the packet is called complete. The generic Size 2 frame's pace, strength, weight, life support and existing drawbacks remain the rules baseline, **not canon physical measurements**. Integrated playtests will determine whether any numbers need revision.

## Firebat and Marauder role clarification — no baseline number change (2026-10-10)
The **original 1998 manual directly establishes heavier-than-Marine Firebat protection and specialized heat/flame insulation**. A *later Marauder design text* (currently verified only through secondary transcriptions) describes a roughly equal-weight CMC-660-derived 5-4 using **thicker neosteel in place of some insulation**. *Wings of Liberty* gives Firebats **Juggernaut Plating (+2 RTS Armor)** and Marauders **Kinetic Foam (+25 RTS HP)**, emphasizing distinct protective enhancements, not a simple ranked ladder. The licensed TMG currently supplies a **5-HP/4+ Armour Marauder** with **+1 HP Kinetic Foam** but **no released Firebat unit card yet** in checked public PDFs. **Keep baseline +14/Class II CMC-660 and +16/Class II 5-4**. Candidate specialty add-ons: enhanced **Juggernaut Firebat +16/Class II**, a dedicated heat/fire defense, and Marauder impact damping (cannot automatically be equated to +1 SWADE Toughness under Heavy Metal). Detailed comparisons: `../../development/benchmarks/FIREBAT-MARAUDER-ARMOR-COMPARISON.md`.
