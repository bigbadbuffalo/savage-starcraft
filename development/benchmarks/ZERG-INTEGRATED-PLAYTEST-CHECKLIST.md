# First Zerg / Terran Cross-Faction Playtest — Test Matrix

**Date:** 2026-10-11. **Status:** Test design **only**, no rolled tabletop encounters have happened. All Zerg numbers remain provisional. No scenario here is evidence that the balance is good.  
**Reference:** `ZERG-SWADE-CREATURE-AND-MECHANICS-SURVEY.md`, `../../bestiary/zerg/README.md`, Terran `../../equipment/terran/` playtest entries, and SFC printed p.93 Heavy Metal. **Do not rewrite already approved equipment mechanics as part of the test.**

## Core mechanical compatibility audit
| Organism/weapon | Compared opponent | Resolution expected | Key issue |
| --- | --- | --- | --- |
| **Marine C-14** 2d10/AP4 HW Class I | **Zergling Size0/8(2)** | **Ordinary rolled damage versus Toughness minus AP on Armor**; not Heavy Metal vs a fictitious carapace Class | Does a group die in roughly believable rifle volleys? |
| C-14 | **Hydralisk 14(4)** / **Roach 13(4)** / **Lurker 16(4)** | Normal rolled damage; **AP4 can cancel up to Armor4**; Size remains | Is armor +4 useful against ordinary low AP while C-14 is lethal? |
| **Zergling Str+d6 HW Class I** | **CMC Marine +10 Heavy Armor Class I** | **1d3 Wounds per successful hit**, +1 with attack raise before normal Soak; Gang Up boosts chance of a raise. *Pack Tactics rolled-damage addition does not increase Class Wounds*. | Are 4–8 Zerglings too lethal, and is Heavy Weapon classification needed to represent them killing Marines? |
| Zergling natural Class I claws | **CMC Firebat/Marauder Class II** | **0 Wounds on normal hit; 1 on Fighting raise** | Heavy suits remain distinct; tactics, multiple hits and escape matter |
| **Hydralisk needles** 2d8/AP4 HW Class I | **CMC Marine Class I** | **1d3 Wounds** (+1 on Shooting raise), ordinary Soak | Does the Hydralisk have a meaningful ranged counter to armored Marines? |
| **Roach acid** 2d8/AP4 HW Class I | Marine Class I | **1d3 Wounds** (+raise), but burrowed healing/effective range affect encounter | Acid AP is original conversion choice; test damage and regeneration together |
| **Baneling blast** 4d8/AP4 HW Class II | Marine I / Firebat II | **I: 1d3+1** Wounds; **II: 1d3**, before Soak, with explosion-area/Evasion handling | Does expendable lethal blast annihilate too many characters? |
| **Lurker line** 3d10/AP4 HW Class II | Marine I / Firebat II | **I: 1d3+1**, **II: 1d3** per independently hit target before Soak | Can scanners, cover, flanking and explosions counter line attacks? |
| **Ultralisk armor** Heavy +8, fixed Class III | C-14 I / ClassII antimat / ClassIII rocket | **C-14 I: No Effect; ClassII: normally 0 or 1 on attack raise; ClassIII: 1d3**, before Soak | Living tank must create urgency for actual anti-armor equipment without invulnerability to all factions |
| **Ultralisk Kaiser Blade** Str+d10/AP12 HW III | Marine I / Marauder II / Tank III | **I: 1d3+2; II: 1d3+1; III: 1d3**, before Soak | Huge Scale, reach, Sweep and multiple Wounds are terrifying; tanks need plausible counters |
| **Firebat linked Perdition** 3d12+2, HW I, Cone | Zergling/Hydra/Roach ordinary Armor | **Ordinary rolled fire damage** against their normal Toughness; incendiary rules; Area/Evasion | Burning biological swarms is formidable; don't treat fire as universally negated by natural Armor |
| **Marauder K12 AP** ClassI special warhead | Ultralisk ClassIII | ClassIII target→II if Armor10+; **Ultralisk has Armor +8**, so **this reduction does NOT trigger**. With ClassI vs III: **No Effect** | The Punisher K12 does not automatically pierce the thickest exceptional bioarmor; viability of specialist rockets |

**Crucial Armor+10 gate:** SFC AP-warhead special class reduction only triggers at target's **listed Armor 10+**, **not** at Toughness 24 or creature Size 8. Our Ultralisk's **+8 Heavy Armor** is **below that threshold**, so K12 Punisher AP as drafted doesn't change Class. If this is unintended, test **Ultralisk +10 Armor and proportionately higher Toughness (26)** as a specific variant, or use an anti-tank rocket. **Do not quietly reinterpret the threshold.**

**Natural Defense scope:** A creature can wield a HW attack while its **own skin is ordinary Armor**; the Heavy Metal Class belongs to the attack, not inherited automatically by the bearer.

## Scenario dry-run schedule — meaningful linked tests
1. **Cave entry / split squad:** Two CMC Marines (one Wild Card) and civilian against **5 ordinary Zergling Extras** at Pace10, cover/ambush available; measure time to melee, number of successful Class I claw attacks, number of raises with Gang Up, fire corridor effectiveness, soldier and Zergling Wounds. Repeat with two Firebats to check Class II gap. **No free supernatural swarm immunity**.
2. **Hydralisk + Roach assault:** Two Hydralisks / two Roaches vs Marine rifle and Firebat. Measure natural Armor/AP interactions, whether a Roach disengages to burrow/heal, sensor counterplay, and whether conditional per-round healing unduly prolongs combat. Compare the same encounter with **Roach regeneration disabled** (A/B).
3. **Suicide push / cover:** One to three Banelings against an exposed line squad, then an entrenched squad. Measure Evasion, separate Blast/Heavy Metal rolls, ability to stop them before detonation, and whether even two simultaneous MBTs cause unacceptable character deaths. Firebat insulation resists **fire, not acid**.
4. **Lurker ambush:** One burrowed Lurker covering a narrow hall with scanner access and alternative flank. Compare observed vs hidden target, area attacks vs ground cover, line targets including allied Zerg, movement-only vs burrow-only attacks. Validate the homebrew **12×1 inch line** explicitly.
5. **Ultralisk breakthrough/evacuation:** Two rifle Marines, one **ClassII antimat**, a **ClassIII SFC light rocket**, a Marauder and vehicle crew protect evacuation. Test whether standard C-14 truly fails, whether enough rockets provide a desperate but possible response, and how Huge Size affects attack rolls / collateral impacts. Include a ClassIII tank for contrast.
6. **Creep infiltration / medicine:** Non-armored technician, combat engineer and field Medic cross spore-filled tunnels, repair suits and spot bio-alarms. Test sealed-suit immunity to inhale-only hazards, movement penalties from actual thick creep, non-combat choices, healing/diseases. Use **Horror swarm parasites** only where skin/air exposure is plausible.

## Needed measurements per action
**Record for each:** raw trait and Wild Die, target, Range/Scale/Gang Up/Cover/Recoil modifiers, raises, **whether ordinary rolled damage or Heavy Metal is being used**, initial Wounds, Bennies/Soak, after-Soak Wounds, one armor Critical Hit per independently resolved wounding suit attack, ammo costs, burrowed state, duration and detection state. Calculate test average after actual roll data; this matrix is *not* simulation output.

## Priorities for revisions
1. Zergling HW ClassI versus Marine ClassI *could be over-lethal* combined with standard Gang Up; do not fix this in isolation.
2. Baneling ClassII self-explosion and multi-target blast are potentially deadly; look for player counterplay.
3. Roach Resilient + conditional Fast Regen might create an unkillable underground enemy; ensure battle exit and scanner interaction.
4. Ultralisk ClassIII is a **new creature-specific equipment-scale mapping** without a general approved biological class doctrine. Owner review required after comparison with Protoss and vehicles.
5. Validate Lurker custom line geometry and AP/ClassII significance against a fortified Marine response.

**Next project gate:** Add Protoss personal shields/psionics, a representative armored vehicle, and 5-PC sample squad before describing these as tested. 
