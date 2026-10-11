# Terran Heavy-Infantry Weapons — First Paired Comparative Design Pass

**Date:** 2026-10-10. **Status:** `playtest` numerical candidates / source-supported SWADE analogues, **not** final equipment approval.  
**Items:** [Twin Perdition flamethrowers](../../equipment/terran/PERDITION-FLAMETHROWERS-PLAYTEST.md), [Quad K12 Punisher](../../equipment/terran/QUAD-K12-PUNISHER-PLAYTEST.md).  
**Protection:** CMC-660 Firebat and 5-4 Marauder both owner-approved **Size 3**, Armor +14/+16 Heavy, respectively, fixed **Class II**, and the Firebat heat-insulation Mod provisionally selected (not final balance approved).

## Source provenance
1. **StarCraft original manual p.35** and **Blizzard's original Firebat guide**: [classic.battle.net/scc/terran/ufire.shtml](https://classic.battle.net/scc/terran/ufire.shtml): arm-mounted twin Perdition projectors, tight-environment infantry, durable/flame-resistant armor. **High confidence for lore**, but no quantified distance/fuel.
2. *StarCraft II: Wings of Liberty* gameplay: Firebat **close-range splash and strong vs Light**, Marauder **bonus versus Armored** and optional slow; updated Blizzard's May 15, 2018 [Marauder patch](https://news.blizzard.com/en-gb/article/21785907/starcraft-ii-balance-update-may-15-2018) changes number of attacks for competitive balance. **Role evidence, not in-world DPS**.
3. Marauder launcher technical details are **currently indirectly verified** in [Quad K12 wiki index](https://starcraft.fandom.com/wiki/Quad_K12_grenade_launcher) and [Marauder wiki index](https://starcraft.fandom.com/wiki/Marauder): arm K12 launchers, armor-piercing grenades, automatic resupply/manufacturing, concussive shell options. Need original SC2 / *Field Manual* and primary Armory passages before treating exact shell size, explosive chemistry, manufacture quantities or mechanisms as verified.
4. **Officially licensed Archon TMG** [Terran P2P Card Sheet](https://starcraft-tmg.com/files/downloads/StarCraft-Terran-P2P-Card-Sheets-A4_EN.pdf), PDF p.2 (May 2026): Marauder Quad K12 RNG **12 tabletop inches**, **RoA3**, **Surge Armoured**, `PIERCE Armoured(2)`, optional Concussive Shells anti-charge slow. **No public published Firebat card** verified from available sheets; no direct TMG Firebat stats used. This **supports distinct tactical roles**, but does not prescribe SWADE range, Heavy Metal Class, or explosive yield.
5. **SWADE primary local PDFs inspected:** Science Fiction Companion printed pp. **45,48,52,56,58,60,93,120,125**; Core **pp.97,100,127,167**. Printed values below are rulebook-derived; integrated mount/targeting decisions are **our conversion**.

## Published mechanical bases
| Standard SWADE equipment | Damage | AP | RoF | Shots | Range/Area | Weapon Class | Cost/Mod |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SFC p.52 **Personal Heavy Flamer** | **4d6** | 0 | 1 | 10 | Cone or MBT to 18 | **I** | 15 lb handheld, no vehicular Mod |
| SFC p.60 **Vehicular Heavy Flamer** | **3d12** | 0 | 1 | 30 | Cone or MBT to 18 | **I** | 1 Mod / Min Size1 |
| SFC p.60 **Vehicular Frag Grenade Launcher** | **3d6** | 0 | **3** | **12** | **24/48/96, MBT** | **I** | 1 Mod / Min Size1 |
| SFC p.48 **Armor Piercing Warhead** fitted to same frag | **3d4** | **8** | as launcher | as magazine | MBT (unchanged) | **I**, with special target-Class reduction | No extra weapon Mod |

## Class mathematics and important exceptions
- Heavy Metal Weapon Class (SFC p.93) = average heavy weapon damage + AP, **rounded up**, with classes I 1–20, II 21–30, III 31–40, etc.
- Flamethrower 3d12 avg **19.5**, AP0 = **Class I**. **Dual Linked +2 rolled damage is excluded** from weapon Class arithmetic per SFC p.93. Thus a twin fire attack is Class I, not Class II.
- Frag 3d6 avg **10.5**, AP0 = Class I. Armor Piercing warhead 3d4 avg **7.5 + AP8 = 15.5** → rounded **16 = Class I**, **plus** printed **warhead p.93 Class reduction** on target Armor 10+. Unlike a generic AP stat, this warhead property genuinely changes penetration against protected *Class II*.
- **Plasma Warhead (SFC p.48) vs Plasma Flamer fuel (pp.52/60) are NOT the same rules text.** Do not add +2 Wounds on a Heavy Metal raise to a flamethrower by copying the plasma *warhead* modifier. Standard (non-heavy-metal) plasma flame raise damage is per the flamer's published plasma option.
- If AP warhead reduces a target from **Class I by one**, the Heavy Metal table provides no “Class 0”. For the first test, **do not count it as a class advantage without an approved lower-than-I convention**. Treat it as the normal I-vs-I relation (no further reduction) and keep this as an explicit adjudication item.
- Core p.97 area-effect raises normally add damage; independently wounding targets suffer suit Critical Hits under approved project interpretation. A raise's extra **Heavy Metal Wound** applies as p.93 specifies. Don't accidentally add both bonus damage and bonus Heavy Metal Wounds for the same class attack.

## Tactical ecology matrix (illustrative Heavy Metal results)
| Weapon | Class I Marine (+10) | Class II Firebat or Marauder (+14/+16) | Class III heavily armored vehicle (+10 Armor minimum) |
| --- | --- | --- | --- |
| Single / linked Perdition **Class I** | **1d3 Wounds** (+1 with attack raise) | **0** (+1 on raise) | **No Effect** |
| K12 ordinary frag **Class I** | **1d3 Wounds** (+1 raise) | **0** (+1 raise) | **No Effect** |
| K12 Punisher **AP warhead** **Class I**, p.93 target-Class reduction | **1d3** (at Class I lower boundary) | **1d3** (+1 raise) | **0** (+1 raise) |

All values are **per separately successful heavy-metal hit before Benny Soak**, not mortality probabilities. Template delivery, Cover, Evasion if permitted for a given effect, and number of hits matter. K12 RoF3 can resolve multiple damaging grenades in an action, consuming actual warheads; the combined impact against heavy infantry may be severe and needs scenario-level calibration.

## Nonclassed targets and other scale boundaries
- Against ordinary unarmored/non-Heavily Armored humans and beasts, use rolled **3d12 flame / 3d12+2 linked** and **3d6 frag / 3d4 AP8 Punisher** rather than directly applying Heavy Metal Classes to organic creatures. No blanket "Zerg Class I" is created.
- Don't assign heavy armor/Heavy Metal Class to Zerglings and Hydralisks before their future creature research. If a huge/armored beast later qualifies as Heavy Armor, document exactly why.
- K12 AP rounds can threaten Class III armor on raises under p.93 but are **not** default tank-killers; still weaker than SFC light rocket, Class III.
- **Mount accounting:** 2 forearm projectors = 2 Mods; 2 K12 arm assemblies = 2 Mods; a linked pair counts as one attack with +1 Shooting/+2 rolled damage, **not six dice instead of RoF3**. Firebat 5/9 incl. 1 Armor, 1 insulation, tentative Self-Sealing; Marauder 5/9 incl. 2 Armor and optional Kinetic Foam, 6/9 if Stabilizer installed.
- **Firing quantities:** Flamer 30 Shots per arm (one spent per projected blast, or two for linked); K12 12 grenades per arm, RoF3 consumes **three per arm** with linked attack, **not 10 generic bullets** because these are warheads (SFC p.56).

## Outstanding but nonblocking questions
1. Whether stock Perdition fuel qualifies for the published **optional Plasma Flamer** variant; the basic approved Firebat insulation effect works with normal heat/fire hazard damage but does **not** decrement direct Heavy Metal wounds.
2. Whether twin flames overlap using **Linked Weapons**, or fire independently into separate cones at a multiple-action cost; the first playtest profile uses Linked to minimize extra rolls.
3. K12 **Concussive Shell** draft: physical gravity slowing, 1-turn movement halving on a sufficiently effective hit; effect conditionality, range, area and Size cutoff need care. **Not approved**.
4. K12 built-in field ammunition manufacturing: separate logistics option later, not free unlimited Shots; consider published auto-reload/reserve slot requirements.
5. K12 AP warhead against the **lowest Class I boundary**: keep its result from going below published Class I pending a ruling.
6. Full comparison with Zergling/Hydralisk/armored Zerg strain and Protoss Personal Force Fields before calling item stats final.

## Recommended status
**Accept first-pass Firebat/K12 mounted-weapon lines for use in the broader equipment packet** as provisional `playtest`, keeping the published SFC mechanics and clearly flagged optional concussive/ammo-fabrication systems. Do not delay Zerg/Protoss development for an isolated Firebat versus Marauder duel. Fire-resistant insulation is a **user-accepted provisional one-Mod item**, not a separate Extra Wound, and Kinetic Foam remains the approved optional Soak Mod.
