# CMC Powered Combat Suits — SWADE Family Design v0.1

**Status:** Draft numerical hypotheses for testing; **not finalized equipment**.  
**Lore grounding:** `lore/entries/terran/powered-combat-suits.md`; original StarCraft manual p.35, Brood War manual pp.10–11.  
**Rules grounding:** Science Fiction Companion **Power Armor pp.119–127** and **Heavy Metal p.93**; normal SWADE character damage.  
**Setting package:** `rules/SETTING-RULES.md`. **Fixed suit Class convention approved**; individual CMC Classes/statistics and character Wound/Soak details remain provisional in `HEAVY-METAL-INTERFACE.md`.

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

**Important interface:** Printed vehicle-oriented Heavy Metal p.93 still raises questions concerning individual-character **Soak, Incapacitation, suit Critical Hits and the Out-of-Control maneuvering note**. They require a narrow playtest/ruling; see `HEAVY-METAL-INTERFACE.md`. Avoid assuming that the "Out of Control" instruction applies verbatim to a standing Marine.

## Ordinary character-damage comparison (retained as diagnostic control, no longer primary)

Using traditional SWADE character damage rather than Heavy Metal: a Vigor d6 human has base Toughness 5. C-14 AP4 gives effective Toughness **11** for CMC-300/400 (+10), **15** for Firebat (+14) and **17** for Marauder (+16), or **18** with its candidate +1 Toughness Mod. Conventional damage produces incremental protection rather than hard class separation. Preserve these numbers for comparison with class playtests; **they are not the selected first-test method**.

## Lore versus draft mechanical status
- **Lore established:** CMC-300/400 are standard Marine suits, CMC-660 is heavier/flame-protective, Marauder 5-4 is advanced heavy assault according to later-source leads.
- **Approved adaptation:** Powered suit has a **fixed Heavy Metal Class** per profile, not modified by wearer Vigor.
- **Draft adaptations:** +10/+10/+14/+16 Armor, Class I/I/II/II, each suit's Mods, and C-14 2d10/AP4/HW.
- **Pending validation:** Wound/Soak/Critical Hit procedure for classed powered infantry, and scenario tests including very high Marine-vs-Marine lethality.

## Next acceptance tests
1. Inspect edition/page-specific later lore for CMC-300/400 feature differences, Marauder foam and Medical armor.
2. Compare chosen CMC-300 +10 to the real C-14 (its Damage/AP/RoF not yet approved), and check whether ordinary non-Heavy Weapons fail appropriately.
3. Observe suit mobility, basic HUD/stealth/fine-motor penalties, cost/recharge and critical damage at the table.
4. Test flame specialization and kinetic impacts with existing SWADE precedent, without assuming universal resistance.
5. **Fixed Class is approved.** Resolve remaining Heavy Metal Wound/Soak/suit Critical Hit handling for individuals before promoting any suit profile to `approved`. Defer Zergling/small-creature interactions until the bestiary.
