# C-14 “Impaler” Gauss Rifle — Equipment Prototype

**Status:** **`playtest` — provisionally accepted as the working C-14 baseline by the owner (2026-10-10)**. **Not final/`approved`**, and no tabletop session playtest has yet been run. The prior Monte Carlo diagnostic is only a mathematical benchmark.  
**Date:** 2026-10-10.  
**Fictional evidence:** `lore/entries/terran/c14-impaler.md`; original *StarCraft* instruction manual, printed p. **35**.  
**Mechanical evidence:** SWADE Core pp. 66, 75, 93, 105; *Science Fiction Companion* pp. **45, 47, 57, 93, 125**.  
**Companion test:** `development/benchmarks/HEAVY-METAL-INFANTRY-FIRE-TEST.md`.

## Draft tabletop equipment line

| Weapon | Range | Damage | AP | RoF | Shots | Min Str | Weight | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **C-14 Impaler Gauss Rifle** | **30/60/120** | **2d10** | **4** | **3** | **100** | **d10** | **20 lb** | **Heavy Weapon, Class I**, **3RB (candidate)** |

**All values beyond the weapon's role / fiction are conversion hypotheses.** Range, Shots, Min Str, Weight and 3RB are **particularly speculative**; original p.35 gives neither quantified velocity nor magazine capacity, rifle mass, actual hit probability, nor a three-*round* cyclic specification. No canonical or StarCraft-credit price is assigned. **Shots 100** is a tabletop testing placeholder, **not** confirmation against later claims of 500+ spikes for specific variants.

### Reason for primary figures
- **2d10/AP4/RoF3:** Published SFC advanced slugthrower assault rifle (p.57) already has these numbers but **is not a Heavy Weapon**; the SFC heavy machine gun (p.57) is **2d10/AP4/RoF3/Heavy Weapon** with Min Str d10, weight 40 lb and Snapfire unless mounted. The proposed gauss rifle is mechanically between them in carrying role, **not** a historical HMG.
- **Heavy Weapon:** Default SFC power armor confers **Heavy Armor**. C-14s need Heavy Weapon eligibility to fight their peer-armed standard CMC infantry without a homebrew exception.
- **Class I:** Under SFC Heavy Metal p.93, average 2d10 damage **11** plus AP **4** is **15**, which lies in Weapon Class I (1–20). This is compatible with lethal rifle-vs-standard CMC Class I and limited effectiveness vs heavier Class II suits.
- **RoF3:** SWADE Shooting-dice abstraction, **not** the literal rounds/second of gauss accelerator fire; per Core p.93, RoF3 expends 10 bullets per shooting action.
- **3RB is optional test feature, not canonical claim:** SFC pp.47,57 explicitly offers 3RB: at RoF1, expend **three bullets** for **+1 Shooting and +1 normal damage**. The original manual says short *controlled bursts*, not that the standard C-14 is definitively programmed to precisely three. Compare playtest A (with 3RB) to B (without). **Heavy Metal Class remains I**; the +1 regular damage is not a reclassification rule, and does not add extra Heavy Metal Wounds.
- **Range 30/60/120:** Between SFC advanced assault rifle 24/48/96 and heavy MG 50/100/200; not a measured canon range.
- **Weight 20 lb:** Deliberate test point between SFC 10 lb assault rifle and 40 lb HMG. At **20+ lb**, published **Mounted Weapon** rules (SFC p.45) explicitly allow bipod/tripod/vehicle mounting; these existing mounts cancel Recoil and Minimum Strength penalties when actually mounted. Do **not** casually treat an unmounted rifle as mounted just because a Marine wears CMC armor.
- **Min Str d10:** A penalty for physically weaker carriers rather than a fictional assertion that non-CMC users can *never* fire it. The published SFC Minimum Strength rule for ranged weapons is –1 Shooting per die-step short (p.45).
- **No Snapfire in first prototype:** Adding Snapfire on top of Min Str and Recoil would need stronger handling evidence or observed balance need. Avoid copying the heavy MG's *entire* penalty suite.

### Rifle ↔ suit stabilization
SFC p.125 **Stabilizer** specifically helps **attached** direct-fire weapons. A carried C-14 does **not** automatically qualify. Test ordinary firing with standard –2 Recoil for RoF2+ (Core p.105); a deployed bipod/tripod or **clearly supported suit attachment** is a second scenario. A suit's standard HUD does not inherently negate Recoil. Creating a proprietary attachment or integrated C-14 cradle requires a documented mount and physical compatibility; do not assume built-in `Integrated Gear` can accommodate a 20-lb rifle when its published limit is **10 lb** (SFC p.125).

### Ammo differentiation under Heavy Metal
Published SFC slugthrower AP ammunition is **–2 ordinary damage, +4 AP** (p.56). **If** this option is valid for a C-14, the draft Class calculation goes from **11+4=15** to **(11–2)+(4+4)=17**, **still Class I**. It will not, by itself, make ordinary C-14 fire reliably penetrate Class II Marauder armor under Heavy Metal. **Weapon/warhead Class and eligible effects, not raw AP alone, govern classed targets.** This is a sanity check, *not* approval that all ordinary SFC ammunition is canonically interchangeable with C-14 spikes.

## First opponent benchmarks
- **Standard CMC-300/400:** tentative **Class I**. Ordinary Class I C-14 hit: **1d3 Wounds**; raise: **1d3+1** (before character Soak).
- **Heavy CMC-660/5-4:** tentative **Class II**. Ordinary Class I hit: **0 Wounds**; Shooting raise: **1**.
- **Class III vehicle:** Class I rifle has **No Effect even with raise** under the Heavy Metal class table.
- **Unclassed/unarmored targets:** Roll the actual 2d10 damage against normal Toughness and Armor; Heavy Metal is **not** universal creature damage.
- **Zerg and biological armor:** **Deferred** per owner; don't classify a Zergling as a vehicle or suit by fiat.

## Specific next verification
1. Directly read the 2015 *Field Manual* / novels for C-14 variant shot capacity, cyclic mechanism, actual recoil/suit mount.
2. Run tabletop positioning and Benny/Soak tests, including multiple independently wounding RoF hits and suit Critical Hits.
3. Decide Range, Shots, 3RB, weight/Min Str before marking this item `approved`.
4. Compare Raynor's HEV/commando penetrator separately; **not** a generic C-14 upgrade.

## Provisional acceptance and stop rule
The owner has accepted the current first-pass figures as **plausible enough to use**. Preserve **30/60/120, 2d10/AP4/RoF3/Heavy Weapon/Class I, Shots100, MinStr d10 and Weight20 lb** as the default reference **until cross-system evidence shows a problem**. Keep **3RB** as a flagged provisional firing mode, not a mandatory finalized feature. Don't hold up development awaiting confirmation of speculative magazine size, mass, range or cyclic burst count; those remain labeled working placeholders. Revisit after building the integrated ground-play packet, not via isolated one-item playtest gates. See `../../development/INTEGRATED-PLAYTEST-PACKET.md`.
