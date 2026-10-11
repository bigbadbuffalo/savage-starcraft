# CMC Powered Combat Suits — SWADE Family Design v0.1

**Status:** Draft numerical hypotheses for testing; **not finalized equipment**.  
**Lore grounding:** `lore/entries/terran/powered-combat-suits.md`; original StarCraft manual p.35, Brood War manual pp.10–11.  
**Rules grounding:** Science Fiction Companion **Power Armor pp.119–127** and **Heavy Metal p.93**; normal SWADE character damage.  
**Setting package:** `rules/SETTING-RULES.md`. **Fixed suit Class convention approved**; individual CMC Classes/statistics and suit-critical-hit/vehicle-specific interaction details remain provisional in `HEAVY-METAL-INTERFACE.md`.

## Chassis from published rules — not a new subsystem
| SFC power armor Size | Starting Heavy Armor | Maximum Armor | Pace | Suit Strength | Available Mod slots |
| --- | --- | --- | --- | --- | --- |
| 1 | +8 | +12 | 12 | d12 | 3 |
| 2 | +10 | +16 | 6 | d12+1 | 6 |
| 3 | +12 | +20 | 4 | d12+2 | 9 |

**Published RAW:** Armor Mod grants +2 Armor, 1 Mod slot (SFC p.123). `Light Duty` (p.122) changes suit protection from Heavy Armor to ordinary Armor, not a default for Marines. Size describes suit chassis; **do not automatically add its Size to wearer's personal Toughness**. SFC basics pp.119–121 already provide powered movement, comms, visor/optics, hearing, environmental seal, roughly three-day battery, unpowered penalties and suit Critical Hits from character Wounds without requiring extra Mods. Powered armor also makes fine-motor/helmet interactions and Stealth harder; those costs matter.

## Provisional equipment family

| Role/suit | Frame | Armor | Pace | Strength | Mod proposal | Capacity |
| --- | --- | --- | --- | --- | --- | --- |
| **UED Medic light armor** | No powered chassis by default | +6 **ordinary** Armor (candidate) | Wearer's | Wearer's | Medical toolkit + physical arm shield separately | N/A |
| **CMC-300 Marine** | Size 2 | **+10 Heavy** | 6 | d12+1 | Stabilizer 1, Scanner 1, Self-Sealing 1 | 3/6 |
| **CMC-400 Marine** | Size 2 | **+10 Heavy** | 6 | d12+1 | Stabilizer 1, Scanner 1, Self-Sealing 1, Integrated Gear (stim dispenser) 1 | 4/6 |
| **CMC-660 Firebat** | Size 2 | **+14 Heavy** | 6 | d12+1 | 2 Armor 2, Stabilizer 1, Self-Sealing 1 | 4/6; reserve 2 for thermal specialization |
| **5-4 Marauder** | Size 2 | **+16 Heavy** | 6 | d12+1 | 3 Armor 3, Stabilizer 1, Toughness +1 mod 1 | 5/6; external launcher systems separate |

**Every number above is original SWADE adaptation design, not lore.** Original lore gives no numeric armor hierarchy. The 5-4 and 660 likely have similar physical chassis: using Size 3 merely to give the Marauder +18 Armor would alter Pace/Strength and need actual dimensional evidence. Reserve specialty mechanisms for later research rather than inventing armor benefits.

### Specialization that +Armor cannot capture
- **CMC-300:** standard multi-role powered infantry; default visor/comms/sealed environment are already SFC chassis features. Proposed **Stabilizer** on *attached* direct-fire weapons can negate Recoil (SFC p.125); confirm how the C-14 connects to the suit before assuming a carried rifle benefits.
- **CMC-400:** Standard candidate protection is **the same +10 Heavy Armor/Class I as CMC-300**. Later armor reinforcement might be a separately classed protective variant, but a model-number increment alone does not warrant better ballistic Class. Its Integrated Gear represents hardware/storage, not the pharmacological effects of stims; two mod slots remain for customization.
- **CMC-660:** known stronger *fire and heat resistance* (P1). The published `Energy Skin` protects from **lasers**, not flame; don't silently use it for fire. A concise heat-resistance feature requires a targeted precedent review; flamethrower integration may exceed the SFC `Integrated Gear` 10-lb limit.
- **5-4:** later accounts report armor optimized for impact/explosions and optional kinetic foam. Existing **Toughness +1 Mod** is a candidate to represent dispersion without inventing a new subsystem. The dual K12 launchers are external equipped weaponry/hardpoints, not free Armor bonuses or necessarily 10-lb Integrated Gear.
- **UED Medic:** Brood War states protective shielding but no mechanical Armor. +6 ordinary gear is a trial baseline, not proof of an unpowered suit. An alternative **Size 1 +8 Heavy Armor medical hardsuit** is possible and would be significantly more protective, with SFC Pace 12/Strength d12 and remaining Mods; compare lore before selection. A **physical medical arm shield** should be evaluated under SWADE Shields rather than assuming a Protoss-style energy shield.

## Heavy Metal — new preferred first test

The Companion publishes fixed **Class** entries for power armor (p. 120; stock suits pp. 126–127). Project rule **approved**: class is assigned to a *suit model*, never recomputed from the wearer's Vigor/Toughness in the middle of play. Specific CMC class assignments below are still **candidate conversions**.

| Candidate CMC suit | Armor | **Fixed Class candidate** | Class I C-14: ordinary hit | Class I C-14: hit with raise |
| --- | --- | --- | --- | --- |
| CMC-300 | +10 Heavy | **I** | **1d3 Wounds** | **1d3+1 Wounds** |
| CMC-400 | +10 Heavy | **I** | **1d3 Wounds** | **1d3+1 Wounds** |
| Firebat CMC-660 | +14 Heavy | **II** | **0 Wounds** | **1 Wound** |
| Marauder 5-4 | +16 Heavy | **II** | **0 Wounds** | **1 Wound** |

The C-14's proposed 2d10/AP4/HW produces **Weapon Class I** (average damage 11+AP4 = 15). The class-relative wounds are a deliberate **high-lethality infantry hypothesis**, not an undesirable accident. Heavy-shock-armor protection against standard gauss fire is a desired role distinction, though specialist warheads/weak points remain relevant.

**Approved interface:** Keep SWADE character rules unchanged. For each **independently resolved attack** that leaves the wearer with one or more Wounds, resolve **one suit Critical Hit**, not one per Wound, by analogy to Core vehicle Critical Hits (p. 117). **No vehicle-specific Out-of-Control roll** applies merely for wearing powered armor. See `HEAVY-METAL-INTERFACE.md`. Numeric CMC profiles remain provisional.

## Ordinary character-damage comparison (retained as diagnostic control, no longer primary)

Using traditional SWADE character damage rather than Heavy Metal: a Vigor d6 human has base Toughness 5. C-14 AP4 gives effective Toughness **11** for CMC-300/400 (+10), **15** for Firebat (+14) and **17** for Marauder (+16), or **18** with its candidate +1 Toughness Mod. Conventional damage produces incremental protection rather than hard class separation. Preserve these numbers for comparison with class playtests; **they are not the selected first-test method**.

## Lore versus draft mechanical status
- **Lore established:** CMC-300/400 are standard Marine suits, CMC-660 is heavier/flame-protective, Marauder 5-4 is advanced heavy assault according to later-source leads.
- **Approved adaptation:** Powered suit has a **fixed Heavy Metal Class** per profile, not modified by wearer Vigor.
- **Draft adaptations:** +10/+10/+14/+16 Armor, Class I/I/II/II, each suit's Mods, and C-14 2d10/AP4/HW.
- **Approved interface:** One suit Critical Hit roll per independently wounding attack, no vehicle-only Out-of-Control roll for individual wearers, and no special Soak mechanics. **Pending validation:** Encounter tests including very lethal Marine-vs-Marine combat.

## Next acceptance tests
1. Inspect edition/page-specific later lore for CMC-300/400 feature differences, Marauder foam and Medical armor.
2. Compare chosen CMC-300 +10 to the real C-14 (its Damage/AP/RoF not yet approved), and check whether ordinary non-Heavy Weapons fail appropriately.
3. Observe suit mobility, basic HUD/stealth/fine-motor penalties, cost/recharge and critical damage at the table.
4. Test flame specialization and kinetic impacts with existing SWADE precedent, without assuming universal resistance.
5. **Fixed Class and the power-armor damage interface are approved interpretations.** Test suit performance and complete equipment specifications before promoting profiles to `approved`. Defer Zergling/small-creature interactions until the bestiary.

## First quantitative firefight test (2026-10-10)
The current **draft equipment sheet** is `../../equipment/terran/CMC-POWER-ARMOR-DRAFT.md`, and the analysis is `HEAVY-METAL-INFANTRY-FIRE-TEST.md`. Using 300K simulated RoF3 Shooting actions, a Wild Card with Shooting d6 firing a non-stabilized Class I C-14 against an exposed Class I Marine scores **1+ successful hits ~51.6% of actions** and inflicts **4+ cumulative pre-Soak Wounds ~18.0% of actions**. Against a Class II suit, **at least one Wound is caused ~29.3%** (requires Shooting raise). Against light cover, the latter drops to **~10.7%**. Stabilized RoF3 increases lethality dramatically if truly mounted or attached under published rules.

**SFC note not captured in earlier suit sketches:** `Self-Sealing` fails to operate when the wearer takes **three or more Wounds from one attack** (SFC p.123). Also `Ballistic Protection` reduces *rolled damage*, not directly inflicted Heavy Metal Wounds; do not use it as a fictional +Class anti-C14 effect absent rule support. All actual suit numbers remain **draft**.

## Provisional integration acceptance (2026-10-10)
By explicit owner direction, the armor line **CMC-300/400 +10 Heavy/Class I; CMC-660 +14 Heavy/Class II; 5-4 Marauder +16 Heavy/Class II** is now a **working `playtest` baseline**, with the current Size 2 chassis and tentative Mods. These are not final published stats. **Do not delay broader equipment and creature design for an isolated Marine encounter test**; validate the complete functional roster afterward. Medic alternatives and thermal/kinetic-specialty mechanisms remain to finish. See `../../development/INTEGRATED-PLAYTEST-PACKET.md`.

## Firebat vs Marauder direct comparison — finding (2026-10-10)
`FIREBAT-MARAUDER-ARMOR-COMPARISON.md` compares direct original manual lore, transcribed later Marauder design statements, SC2 game upgrades and licensed TMG cards. **Preserve +14/Class II CMC-660 and +16/Class II 5-4 as provisional**, but record that **same approximate physical suit weight** (as reported by later sources) and Firebat **Juggernaut Plating** prevent inferring an unconditional ballistic winner. A variant **Juggernaut Firebat +16/Class II** would be compatible with SFC Size 2 three Armor Mods, pending a complete item and Mod allocation. The critical outstanding issue is **typed heat defense vs Marauder impact-shock damping**, not adding another Class. Crucially, the suggested Marauder **+1 Toughness** Mod does not change Heavy Metal direct Wounds against a fixed suit Class, so it **does not by itself fully emulate Kinetic Foam**; choose a native mechanic later, after paired offense/support equipment is drafted.

## Published Modifications review (2026-10-10)
See `POWER-ARMOR-MODIFICATIONS-REVIEW.md` for primary-rulebook verification. Most appropriate native pieces are **Armor +2**, **Toughness +1 (conventional damage)**, **Trauma Pack** (post-Wound functionality; Kinetic Foam only partial analogue) and **Self-Sealing** (atmosphere protection). **Ballistic Protection** is rolled slugthrower damage reduction and cannot simply subtract from Heavy Metal's direct Wounds; **Energy Skin** only reduces lasers, not flame. **Stock SFC Assault Suit (Class II, +16) includes Trauma Pack and grenade launcher**, a close Marauder archetype. Firebat's extra flame-weapon protection has **no exact defensive Mod** despite generic sealed suits' environmental temperature handling. Proposed revised Mod budgets are **research recommendations, not changes to provisional baseline**.

## Revised Trauma Pack and Kinetic Foam research (2026-10-10)
The owner prefers **no default Trauma Pack absent specific lore**: SFC's drug-injection device is **not** Kinetic Foam's impact-dispersing undersuit. Native **Toughness +1** and **Ballistic Protection** Mods remain plausible layers, but neither mitigates Heavy Metal's direct Class Wounds. `MARAUDER-KINETIC-FOAM-STUDY.md` documented the now **owner-approved one-slot +2 Vigor Soak-versus-kinetic/concussive-impacts** Mod (normal Benny and ordinary Soak required); current rule at `../../equipment/terran/KINETIC-FOAM-MODIFICATION.md`. The previous +1 alternative was not selected. Preserve accepted Firebat +14/Class II and Marauder +16/Class II until integrated tests. Earlier Trauma Pack packages in this study are superseded as *recommendations* and remain for historical clarity.

## Chassis sizing study — twin integral weapons (2026-10-10)
A new direct SFC inspection finds Power Armor p.120 **explicitly accommodates vehicular weapons** as Mods; printed **vehicular Heavy Flamer and Grenade Launcher (p.60) each use 1 Mod and have Min Size 1**. For a representative twin-mounted Firebat or Marauder, **Size 2 can support the mounts** but consumes its 6 Mod capacity after existing Armor/Kinetic Foam and a Firebat thermal/self-seal allowance. **Size 3 has 9 Mods, starting +12 Heavy Armor**; to preserve the existing +14/+16 Armor values, it uses **1×/2× Armor** instead of **2×/3×**, providing **4 more open Mod slots** at unchanged fixed Class II. Tradeoff: **Pace 4 vs 6**, Strength d12+2 vs d12+1, 300 lb vs 200 lb unpowered, higher frame cost. This is a **preferred but not yet owner-adopted chassis design alternative**, not a numerical stat change. See `POWER-ARMOR-FRAME-SIZING-STUDY.md` for separate mount/Integrated Gear analysis and slot tables.
