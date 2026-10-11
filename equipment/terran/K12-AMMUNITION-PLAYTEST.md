# Quad K12 — Interchangeable Grenade Ammunition

**Status:** `playtest` — owner-approved **design direction** of a multi-purpose K12 ammunition family, with a provisionally accepted *Sloth-inspired* Concussive Shell. Specific munitions beyond established Punisher/Concussive types are **plausible RPG expansions, not documented standard StarCraft K12 issue**. Revision date: 2026-10-10.  
**Rules sources:** *Science Fiction Companion* **p.48** (warhead descriptions and availability), **p.60** (vehicular grenade launcher, explicit allowed warhead list, automatic selector, normal base 3d6/MBT/RoF3/12 shots), **p.93** (Heavy Metal warhead adjustments), **p.47** (Time weapon quality), *SWADE Core Rules* **p.167** (*Sloth/Speed*), p.97 (blast templates).  
**StarCraft anchors:** *StarCraft II* Marauder's **Punisher grenades** and **Concussive Shells**, including its anti-armored and movement-slowing role; Blizzard [Terran Medivac Drop guide](https://news.blizzard.com/en-us/article/5740270/game-guide-terran-medivac-drops) confirms Concussive Shells slow advancing opponents. Secondary unit/technical index: https://starcraft.fandom.com/wiki/Quad_K12_grenade_launcher . Archon TMG Marauder Concussive Shells upgrade is an anti-charge movement debuff, not a direct numerical mapping to SWADE.

## Critical rules-accuracy correction (p.48 vs p.60)
The SFC general Warhead table on **p.48** defines **Armor Piercing (+8 AP, one damage die-type step down)**. But the specific **vehicular grenade launcher** entry on **p.60 does not list Armor Piercing among its allowed grenades**. It explicitly allows **EMP, High Explosive, Incendiary, Phase, Plasma, Smoke, Stun, Time**. Therefore:
- **All eight p.60 choices** can be fitted per published launcher text (subject to setting technology and ammunition availability).
- **Armor-piercing Punisher grenades are a deliberate Savage StarCraft compatibility exception**: apply the **existing p.48 AP warhead mechanics to this particular fictional K12 launcher**, even though generic SFC vehicle grenade launchers do not get AP warheads by their listed RAW options. This is **homebrew equipment compatibility**, not verbatim SFC RAW. For Heavy Metal, its **p.93 AP warhead** reduces target Class by one when Armor is 10+. Keep the base K12 at Weapon Class I until separately justified otherwise.
- We do **not** generalize the exception to **every grenade launcher** or all high-AP ammunition. Nor do we silently give the Concussive slow to all shell types.

## Loadout catalogue

**Common launcher baseline:** 24/48/96; **3d6 (Weapon Class I)**; **MBT**; **RoF 3**; each arm assembly **12 Shots**, one installed weapon Mod (two if linked pair, yielding +1 Shooting and +2 rolled damage). The table shows **unlinked base damage**; when linked, add +2 *normal rolled* damage, **not** Weapon Class or an automatic second hit. A fitted warhead may change damage/template as below.

| K12 ammunition | Baseline result / damage | Provenance and permissions |
| --- | --- | --- |
| **Standard Punisher AP** | **3d4, AP 8**; Heavy Metal target **Class −1 when Armor 10+** | **Known StarCraft anti-armor role**, modeled by **custom K12-only permission** to use p.48 Armor Piercing warhead. **Not on p.60 RAW launcher list** |
| **Concussive Shell** | **3d6, AP0, MBT**; *slow rule* below | **Known StarCraft role**, custom **movement-control** payload; not the high-tech Time warhead |
| **Fragmentation** | **3d6, AP0, MBT** | **Published normal vehicle grenade** (p.60); expanded K12 arsenal for RPG |
| **High Explosive** | **3d4, AP0**, **LBT** rather than MBT; additional Critical Hit effects as p.48 and p.93 | **Published compatible warhead**, RPG expansion |
| **Incendiary** | **3d6, AP0, MBT**; potential ignition | **Published compatible warhead**, RPG expansion |
| **Smoke** | **LBT obscuring smoke** (Dark Illumination); reflective anti-guidance variant available for double cost | **Published compatible warhead**, RPG expansion; don't add fragmentation damage to a smoke round automatically |
| **EMP** | Electronic disruption with p.48/p.93 restrictions and damage/Wound penalties | **Published compatible warhead**, RPG expansion; not general proof this model uses EMP stock |
| **Stun** | Unprotected individuals caught in effect risk Stunned (Vigor at **−2**, **−4 on raise**); ineffective against vehicles | **Published compatible warhead**, RPG expansion |
| **Phase** | Penetrates/reaches inside armor according to p.48 and raises Weapon Class by one in Heavy Metal (p.93); energy shields resist | **Published compatible but highly advanced technology**; restricted experimental/exceptional procurement |
| **Plasma** | Incendiary; +2d6 rolled damage with raise / +2 Wounds on Heavy Metal raise | **Published compatible but advanced technology**; restricted procurement; not ordinary Firebat flamer fuel |
| **Time** | **Automatically** Distracted and Vulnerable and **half movement until end of next turn** on those hit or caught in template | **Published compatible ultra-advanced warhead** (p.48), **×50 cost**, far more powerful than Concussive Shell; restrict unless campaign explicitly allows exotic temporal technology |

**Do not assume** these ammunition types are all common in the Dominion's army; the list establishes **mechanically compatible possible K12 RPG ammunition**, not a StarCraft canon inventory. Specific p.48 modifiers and price multipliers should be read from the printed table; Punisher/Concussive/StarCraft-fabricated types have **cost TBD** rather than invented market prices.

## Concussive Shell — provisional accepted movement effect

**Selected rule direction (owner, 2026-10-10):** Use a **Sloth-like movement penalty**, but avoid importing a full Arcane Power or a standard Time warhead.

**Base profile:** **3d6, AP0, Class I, MBT**, fired from a K12 launcher using normal Shooting/template/ammunition procedures. A creature **Shaken or Wounded** by the attack using ordinary damage, or **Wounded** by the attack under Heavy Metal, has its **total movement halved (round up)** until the **end of its next turn**. A slow cannot stack with itself to quarter movement; another hit may refresh the duration if qualified.

- **No automatic Distracted or Vulnerable**, unlike Time warheads; **no Arcane Background, PP, opposed casting, or Spirit recovery roll**, unlike the full Core *Sloth* power.
- **Trigger has to matter:** plain hits that cause neither Shaken nor Wounds **do not** slow by the present provisional rule, despite RTS hits applying slow; this is a deliberate RPG balance limiter given RoF3 and potentially multiple Blast Templates. If that makes Concussive irrelevant against Class II suits, consider an alternate on-hit or AP-concussive magazine in the integrated test, rather than silently changing the trigger.
- **Scale restriction:** the **RTS** excludes `Massive` targets; *Size 4+ immunity* in the prior draft is an **unratified conversion hypothesis**, not a canon Size threshold. For the first provisional packet, rule **Size 4+ creatures/vehicles are unaffected by slow**; Size 4 is an intentional test boundary, **not a universal definition of StarCraft Massive**. Revisit after Zerg/vehicle Size profiles exist. A worn Size 3 power-armor chassis is not automatically an **operator Size 3** natural creature.
- **Template-wide interaction:** Each creature actually Shaken/Wounded by the resulting blast can qualify; the printed p.48 Time warhead instead applies its control effects to all targets hit or caught, without needing damage. Keep the weaker concussive trigger clear to reduce battlefield-wide autostunlock.
- **No stacking with standard AP by default:** Ordinary Concussive shells do **not** simultaneously get +8 AP and Class reduction. If a hybrid Punisher AP + slowing effect is added for a special variant, it must be separately costed and documented; SC2's game upgrade is a useful inspiration but doesn't require a no-tradeoff dual warhead in this RPG.
- **Duration:** The end-of-next-turn duration borrows from *SFC Time*, not Core *Sloth*'s Spirit-save persistence; the half-movement consequence borrows from both, and is **original bespoke ammunition**, not SWADE RAW.

**Why not copy the complete Time warhead?** SFC p.48 Time automatically applies **three** debilitating effects to everyone affected—Distracted, Vulnerable, half movement—and is **advanced temporal technology priced ×50**, an overpowered/fictionally mismatched substitute for common Marauder concussive grenades. Core Sloth (p.167) also continues until a successful Spirit recovery; the current K12 ammunition deliberately uses a **shorter fixed duration**.

## Loading and Mod budgets
- The SFC vehicular launcher on p.60 carries **12 grenades per installed arm magazine**, with an **automated loading and selecting mechanism**. Switching among **already loaded** compatible warheads is a **limited free action**, subject to the actual ammunition the operator has available. It does not conjure any shell type or grant a stockpile of every warhead.
- Each fired grenade consumes **one Shot** from its launcher; simultaneous linked arm fire consumes one from **each** arm per projectile/attack die at the chosen RoF. Optional SFC extra reserve reload capacity has its normal **additional Mod slot** requirement. Loading arbitrary special magazines isn't a source of infinite Shots.
- **Exactly 2 weapon Mods** for the two installed K12 assemblies remains the provisional assumption. **No Mod cost per *warhead type***, but ammunition itself costs inventory/supply; time, phase, plasma are still setting-gated.
- Miniature auto-factory / self-fabricator hardware is a **separate incomplete equipment feature** and is not included for free with the launcher or its magazines.

## Relationship to previously approved decisions
- The **Size 3 Marauder chassis** is owner-approved (DEC-017), but this does not imply free weapons or consumables.
- The **Kinetic Foam (+2 conditional Soak) Mod** is owner-approved (DEC-016); this does not improve the launcher or ammo.
- **K12 multi-ammo support and use of Sloth-inspired slow** are the owner's selected **provisional design direction**. Shell-specific area/trigger/size details remain test values, not final printed item approval.
- Heavy Metal fixed Class and character Soak/Critical Hit rules remain unchanged.
