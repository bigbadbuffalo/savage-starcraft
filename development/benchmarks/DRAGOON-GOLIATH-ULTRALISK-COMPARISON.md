# Dragoon–Goliath–Ultralisk: Three Kinds of Heavy Ground Combatant

**Date:** 2026-10-11. **Status:** Source-reviewed and rule-arithmetic comparisons; **first-playable scenarios**, not rolled tests and **not owner-approved numerical baselines**.  
**Source hierarchy:** Primary Blizzard original [Dragoon](https://classic.battle.net/scc/protoss/units/dragoon.shtml), [Goliath](https://classic.battle.net/scc/terran/ugl.shtml), [Ultralisk](https://classic.battle.net/scc/zerg/units/ultralisk.shtml), vs published **SFC** walker frames pp.181–188, vehicular cannons p.59, and Heavy Metal p.93. Blizzards's multiplayer size/HP/armor tags are not RPG mechanical values.  
**Current source files:** [Dragoon profile](../../vehicles/protoss/DRAGOON-WALKER-PLAYTEST.md), [Goliath](../../vehicles/terran/GOLIATH-PLAYTEST.md), [Ultralisk](../../bestiary/zerg/ULTRALISK-PLAYTEST.md), and [Biological monster scale](BIOLOGICAL-VEHICLE-SCALE-STUDY.md).

## Shared scale, fundamentally different damage models

| Attribute | **Protoss Dragoon** | **Terran Goliath** | **Zerg Ultralisk** |
| --- | --- | --- | --- |
| **What it is** | Permanently embodied wounded warrior, **quadrupedal piloted walker** | One-person, mechanically piloted walker | Self-contained **biological creature** |
| Published SWADE body analogy | **Large Walker Frame** + p.185 Walker Shields | **Stock Infantry Support Walker**, p.187 | Vehicle Guide **p.21 monster calibration**, plus published SFC armored fauna |
| **Size / Scale** | **4, Large** | **4, Large** | **8, Huge** |
| Strength | **d12+4** *hull*, not operator's personal Strength | **d12+4** *hull* | **d12+8** *natural* |
| **Toughness (Armor)** | **21 (6 Heavy)** | **21 (6 Heavy)** | **26 (10 Heavy)** |
| Heavy Metal Class | **II** derived from 21 | **II** derived from 21 | **III** derived from 26 |
| Wounds | **4 vehicle Wounds** | **4 vehicle Wounds** | **Huge creature extra Wounds**, **not** a 4/5 Wound vehicle hull |
| Attack | **Disintegration bolt 4d10/AP10 (III), RoF1** (medium-cannon numerical analogy, **custom energy emitter**) | **Two linked Light Autocannons 3d8/AP4 (I), RoF4**, plus **Hellfire light guided missiles 6d6/AP16 (III)** | **Kaiser Blades Str+d10/AP12 (III), melee/Reach2** |
| Rechargeable shield | **2 mandatory walker Shields charges** (SFC p.185; **2 Mod slots** on Size4) | No shields on stock baseline | No personal energy shield |
| Movement | Walker **Handling0 / Top Speed Rating8** | Walker **Handling0 / Top Speed Rating9** | **Pace8**, biological Athletics/movement |
| Control | **Embedded Protoss** pilot, Piloting/Shooting/Electronics | One Terran pilot, Piloting/Shooting/Electronics | **Fighting/Athletics**, no crew or Piloting |
| Hull Critical Hits | **Walker damage/leg/reactor systems** | **Walker damage/leg/reactor systems** | **Organic injury** under creature Wounds; no automotive criticals |

## Heavy Metal direct Wounds per successful qualifying hit (before Soak)

| Attacker | Dragoon **II** | Goliath **II** | Ultralisk **III** |
| --- | --- | --- | --- |
| **Dragoon disintegration III** | **1d3+1** | **1d3+1** | **1d3** |
| **Goliath paired autocannon I** | **0** (*1 on attack raise*) | **0** (*1 raise*) | **No Effect** |
| **Goliath Hellfire light missile III** | **1d3+1** | **1d3+1** | **1d3** |
| **Ultralisk Kaiser blades III** | **1d3+1**, if in melee | **1d3+1**, if in melee | **1d3**, if in melee |

**SFC p.93:** One level below causes **0 Wounds**, but a hit with raise can make it **1**; two levels below is **No Effect**, even on attack raise. Equal classes **1d3**, and each level above adds one. The table is **per separately resolved hit**, not all attacks automatically landing. Goliath's **RoF4** and 24 stocked missiles can make it devastating *if* the pilot expends ammunition/actions; linked guns are **+1 Shooting/+2 rolled damage** without raising Class. Dragoon's ClassIII single shot is **better penetration per impact**, while Goliath's missiles supply its heavy antivehicle punch. Firing both complete weapon systems for free every turn is **not** supported by SWADE.

**Critical asymmetric effect:** The Dragoon's **walker shield p.185** consumes automatic **Electronics-based Soak charges** when Wounds would land, then recharges in 10min outside battle. Its **2 charges** are derived from **4 basic walker Wounds ÷2**, not Size, not TMG Shield3, not the personal p.42 +4 Toughness. By contrast the Goliath relies on Hull ClassII, AM/ECM guided-missile defenses (p.187) and damage repairs. Neither has a natural Healing trait. The Ultralisk has **ordinary biological Soak** and Huge creature Wounds, with no Crew Critical Hits / Out-of-Control roll just because it is large.

## Three practical direct comparisons
**A. Dragoon vs Goliath:** Both have same hull Toughness21/ClassII and Wounds4 to expose loadout differences. At range, Dragoon single ClassIII disintegrator can score **1d3+1** per hit while Goliath **autocannons (ClassI)** need a raise to cause **1 Wound**. The Goliath's **ClassIII guided Hellfires** can deal the same heavy Wounds as the Dragoon but drain its missile rack and can be countered with suitable cover/evasion. Dragoon shields potentially absorb the first damaging impacts, but its charge pool is small.

**B. Dragoon vs Ultralisk:** Dragoon ClassIII disintegration is a natural ranged counter to ClassIII Ultralisk without rockets. A successful hit is **1d3 creature Wounds before Soak**, a significant portion of the Huge organism's ordinary capacity. If the Ultralisk closes, its Kaiser ClassIII vs Dragoon II lands **1d3+1 vehicle Wounds**; with remaining shield charges the Dragoon may survive, but creature Scale/Reach and walker Out of Control matter. An Ultralisk still requires cover, threat and charge positioning rather than just running through infinite disintegrator shots.

**C. Goliath vs Ultralisk:** Stock linked ClassI autocannons are **two Class levels below Ultralisk III → No Effect**, regardless of attack raises. Anti-air **ClassIII Hellfire missiles** can hurt the Ultralisk as heavily as the Dragoon beam, if the mission allows using a guided launcher at a ground target; **Blizzard calls them anti-air Hellfire missiles**, so default ground-target firing requires **an explicitly authorized dual-use loadout or fire-control adjustment**, not automatic canonical anti-tank missile use. A Goliath without such flexibility should avoid/reposition the Ultralisk or call Siege Tank support. This is a good StarCraft role distinction, not automatically a balance bug.

## Strength scaling and why an Ultralisk isn't automatically a tank
- The user noted that **Strength past d12** can distort giant-creature hand attacks and rolling damage. Core still officially uses **d12+N**, and Vehicle Guide p.21 uses **d12+10** on its kaiju example. **Vehicle-calibrated monster construction fixes scale choices, not necessarily Strength mechanics**.
- Current Ultralisk uses **d12+8 and ClassIII blade**. Its *natural* Hide **T26(10 Heavy)** derives ClassIII under SFC p.93. No invented species fixed class needed.
- **Walker** vehicle Wounds+critical systems make sense for Dragoon and Goliath because they have actual actuators, pilot compartments, weapon mounts and power systems. **Creature** Wounds, Soak and organic injuries are still right for the ordinary Ultralisk. Copying the Brawler's **5 vehicle Wounds** would require replacing, not adding to, Size extra Wounds.
- A Nydus transport or Overlord is a **stronger candidate for actual biological vehicle-style cargo/boarding rules** than merely retyping every massive Zerg melee fighter as a tank.

## Encounter protocol
1. Fight Dragoon/Goliath at long range using cover and sensors; log direct-fire vs guided Electronics, relevant targeting penalties, all ammo/energy power assumptions, hits/raises and shield charge expenditures.
2. Add a ClassIII Ultralisk closing through obstacles. Compare Dragoon sustained RoF1 and Goliath autocannon plus **dual-use** or **AA-only** Hellfire modes. Let the Ultralisk reach melee in an alternate starting-distance run.
3. Replace standard Dragoon emitter with the **Light Particle Cannon ClassII RoF3** p.63; measure survival versus Hulks vs infantry, and how a change in *weapon class* affects biology.
4. For a true biological vehicle/transport experiment, compare egress and critical damage rather than inventing automotive Out-of-Control on every large Zerg.
5. **No actual session results asserted**: all Wound outcomes are direct Heavy Metal table derivations assuming successful hits, not simulated distributions.

## Open review items
- Pilot mind/body life-support and **shield Electronics skill** for psi-linked Dragoon; a new psionic interface could legitimately replace Electronics but is **not RAW**.
- **Recharging rate** and availability of Protoss shields vs lore slow regeneration. SFC 10-min out-of-combat recharge is an approximation, and may be tuned later with other faction shield choices.
- Dragoon's disintegration **range/AP/energy supply** is custom extrapolation from a *Medium Cannon*; Blizzard text does not give SWADE die metrics or shot budgets.
- Whether Goliath's Hellfire anti-air guidance supports ground targeting; no free guided anti-Ultralisk shots without selecting that mode.
- Creature **Gigantic/Size** not converted from RTS "Large" unit tag; exact heights/tonnages for these three remain **unverified**.
