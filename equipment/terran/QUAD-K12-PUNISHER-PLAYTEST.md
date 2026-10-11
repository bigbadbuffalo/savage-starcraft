# Quad K12 “Punisher” Grenade Launchers — Terran Marauder

**Status:** `playtest` **provisional equipment package**, not final player-facing item approval. Assembled 2026-10-10.  
**Lore:** SC2 *Wings of Liberty* Marauder, as indexed in secondary [Quad K12](https://starcraft.fandom.com/wiki/Quad_K12_grenade_launcher) and [Marauder](https://starcraft.fandom.com/wiki/Marauder) entries: paired arm-mounted launcher assemblies, **armor-piercing Punisher grenades**, an **automated loading system** and optional **Concussive Shells**. Primary SC2 Armory/Field Manual quotations for the miniature ammunition fabricator **still need firsthand inspection**; do not hard-code “infinite ammunition.”  
**Other evidence:** Blizzard's [May 15, 2018 balance change](https://news.blizzard.com/en-gb/article/21785907/starcraft-ii-balance-update-may-15-2018) explains the anti-Armored gameplay bonus, but **RTS damage is not ballistic physics**. Licensed Archon [Terran TMG card sheet](https://starcraft-tmg.com/files/downloads/StarCraft-Terran-P2P-Card-Sheets-A4_EN.pdf), PDF **p.2**, has Quad K12 **RNG 12\"**, Armoured Surge, `PIERCE Armoured (2)`, and a Concussive Shells charge-interception ability. **TMG inches/armour are not SWADE units.**

**Published SWADE basis:** *Science Fiction Companion* **p.60** (vehicular grenade launcher: Min Size 1, 1 Mod, **24/48/96**, **3d6 (I)** frag, AP0, **RoF3**, **12 shots**, **Medium Blast Template**), **p.48** (Armor Piercing warhead changes 3d6 → 3d4 and **AP +8**), **p.93** (**Heavy Metal Armor Piercing warhead reduces target Class by one if Armor is 10+**); **p.45** (Linked Weapons), **pp.44,58** (HW/vehicular weapons), **p.120** (power suit allowed vehicular weapons), Core **p.97** (area effect) and **p.167** (Sloth as a slowdown mechanical precedent).

## Provisional mounted weapon line

| Configuration | Range | Damage | AP | RoF | Shots | Weapon Class | Slots |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **One Quad K12 arm launcher assembly**, loaded with ordinary frag | **24/48/96** | **3d6** | — | **3** | **12 per arm** | **I** | **1** |
| **Paired arm launchers, linked** | **24/48/96** | **3d6+2** rolled damage | — | **3** | **12 per arm** | **I** | **2 total** |
| **Armor-piercing Punisher grenade payload**, per launched round | Same as launcher | **3d4** (linked pair **3d4+2**) | **8** | As launcher | From K12 magazine | **I**, with **Armor Piercing warhead** Class interaction | No extra launch slot |

**Traits:** Heavy Weapon; **Medium Blast Template (MBT)** per published vehicle grenade, explosive projectile. This is a **direct-fire Shooting weapon**, not a Guided Weapon using Electronics. Both arm assemblies may be treated as a **dual-linked set**: one Shooting attack at **+1 to hit** and **+2 to normal rolled damage**, using normal RoF3 (**three Shooting dice**, not six). Every fired projectile consumes a grenade from its issuing launcher: **if both arms discharge linked volleys, budget one grenade per arm per RoF hit attempt**. At RoF3 with both arms firing, three grenade pairs consume **three rounds from each 12-shot magazine**, allowing **four fully automatic linked actions before reloading**. RoF1 can conserve ammo. Linked +2 **does not affect Weapon Class** (SFC p.93). The full eight barrel bores seen in artwork are **not** individually purchased vehicle weapons: “Quad K12” is an in-universe hardware designation, while the tabletop item is **two arm assemblies**, each represented by **one mounted launcher**.

**Shots/feeding caveat:** Printed vehicle grenade launcher carries **12 grenades** and has automatic magazine loading/selector; a **full stored reload consumes another Mod slot** under SFC p.60. **Do not treat self-fabricating hundreds of shells as free infinite Shots**. If we want to emulate the lore's compact ammunition-manufacturing unit, design a separately costed feedstock/reloading option later with explicit material limit and operating time. Standard ammo switching uses the existing automatic selector as a limited free action, provided the relevant ammunition is loaded. A Size 3 suit has room for such an option without revising its fixed Class.

## Punisher armor-piercing rounds: decisive published Heavy Metal interaction

Per SFC p.48, **Armor Piercing warhead** increases AP by **8** and reduces damage by **one die type**: for this 3d6 launcher, **3d4/AP8** (average 7.5+8=15.5, rounded up **16**, so **still Weapon Class I**). Under **Heavy Metal p.93**, **instead** apply the published AP-*warhead* rule: **reduce target Class by one when the target has at least +10 Armor**. This is **not** the same as an ordinary slugthrower's higher AP and does **not** mean reclassifying a generic C-14 rifle. Do **not** count the AP8 twice or import the armor-reduction rule to all ordinary AP ammo.

| Target | Normal frag (Class I weapon) | Punisher AP warhead vs Armor 10+ |
| --- | --- | --- |
| **Class I Marine, +10 Armor** | **1d3 Wounds** (+1 attack raise) | Lowest Class **I** has no published Class 0; **do not invent a higher-than-equal advantage**. Treat as **Class I vs I** for now, and flag this lower-bound interpretation for rule adjudication |
| **Class II Firebat/Marauder, +14/+16 Armor** | **0 Wounds**, +1 on attack raise | **Target Class II → I**: **1d3 Wounds** (+1 on raise) before ordinary Soak |
| **Class III armor vehicle, 10+ Armor** | **No Effect** | **Target Class III → II**, Class I weapon: **0 Wounds**, +1 on attack raise |
| **Class III armor vehicle, less than 10 Armor** | **No Effect** | AP-warhead Class reduction **does not trigger**, so **No Effect** |

A K12 can therefore kill armored infantry without being modeled as an all-purpose Class III rocket or railgun. Note the result remains extremely deadly when multiple linked RoF hits all land—**an intentionally provisional effect to measure in integrated tests**. Extra template hits, Cover, Evasion where the specific delivery permits it, and separately wounding armor Critical Hits need careful application. **Each independently resolved hit that inflicts Wounds after Soak triggers one suit Critical Hit**, as already approved; don't replace all the launcher volley hits with one combined suit Critical Hit.

## Ammunition / concussive variant

| Load | Profile | Status |
| --- | --- | --- |
| **Frag grenades** | SFC **3d6 (I)**, AP0, MBT | **Published baseline**, directly usable |
| **Armor-piercing Punisher** | SFC **3d4 (I)**, **AP8**; target Class reduction when Armor 10+ | **Published warhead adaptation selected as provisional main antiarmor ammunition** |
| **Concussive Shells** | **3d6 (I)**, AP0, MBT; if attack **Shakes or Wounds** a target (ordinary damage), or causes **at least 1 Heavy Metal Wound**, its movement is **halved through the end of its next turn**; target Size **4+** is unaffected by slowing | **Original optional custom payload**, not owner-approved. Use as separate loaded shells rather than silently bundling the effect with free AP8. Inspired by **Core Sloth** movement-half language (p.167), but does **not** use Power Points or an Arcane Background. **Further review needed**, especially template-wide slowing, vehicle eligibility and Massiveness/Scale. |

RTS Concussive Shells slow non-Massive enemies; TMG uses a short-range anti-charge **Speed debuff**. Those are **role evidence**, not proof of the exact half-movement/duration or SWADE Size cutoff. A gravity-warp "why" is reported in secondary indexed fiction and needs primary source corroboration. Do **not** copy the SFC's advanced `Time` warhead (p.48) as canon temporal technology; its +debuff package/expense is much more than the Marauder's documented slow effect.

## Owner-approved Size 3 suit installation
- **Chassis:** Size 3, Armor +16 Heavy/Class II, Pace 4, Strength d12+2, **9 available Mods**.
- **Armor ×2 (2 Mods)** + **two 1-Mod installed K12 assemblies (2 Mods)** + **optional approved Kinetic Foam (1 Mod)** = **5/9**; **4 remain**.
- **Stabilizer (1 Mod)** is attractive because **RoF3 normally incurs Recoil −2** and the linked weapon is an attached **direct-fire** system (SFC p.125). Taking it gives **6/9 used**, **3 left**. This is **provisionally recommended but not mandatory**. It is **not** a Guided Weapon; using Electronics in place of Shooting would need a different ammo/system.
- **Stored reloads:** 1 Mod per complete reserve reload per launcher if stocked per printed rule; adding **two** reserve magazines would bring foam+stabilized suit to **8/9**, leaving **one** slot for another purchased Mod or researched fabrication device. Do not claim these are automatically standard issue in every era.
- SFC `Integrated Gear` 10-lb cap is **not** the right mechanism for an installed launcher bank. Do not require an extra slot just to have the already-budgeted weapon physically attached.

## Recoil, blast geometry, and use
The default **linked** K12 attack has **RoF3** (three Shooting dice, one Wild Die if Wild Card substituting one Shooting die), and therefore ordinary **Recoil −2** at RoF2+ unless a compatible Stabilizer is installed. Three launched grenades per *arm* in a linked automatic attack consume three Shots each; **the third/fourth shell does not provide free extra attacks because the turret has multiple bores**.

Published vehicle frag rounds use **MBT** even for AP payload unless the GM explicitly changes the blast delivery. **This is a potential gameplay conflict with the Marauder's precision antiarmor RTS role:** multiple MBTs may make a linked RoF3 loadout a dangerous crowd-clearer. The first test deliberately preserves SFC RAW, documents the tension, and defers a smaller shaped-charge Blast to integrated comparative trials rather than quietly changing SFC profiles.

**Development checkpoint:** The *key antiarmor rule is already printed*: **Armor Piercing warheads lower target Class by one**. We should build Zerg carapace / Protoss shield and vehicle threat targets next rather than inventing an ungrounded Class II innate launcher. **Concussive shells, ammunition synthesis rate, hardpoint stats and mode rules remain provisional.**
