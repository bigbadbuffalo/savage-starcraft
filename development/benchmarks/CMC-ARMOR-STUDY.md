# CMC Powered Combat Suits — SWADE Family Design v0.1

**Status:** Draft numerical hypotheses for testing; **not finalized equipment**.  
**Lore grounding:** `lore/entries/terran/powered-combat-suits.md`; original StarCraft manual p.35, Brood War manual pp.10–11.  
**Rules grounding:** Science Fiction Companion **Power Armor pp.119–127** and **Heavy Metal p.93**; normal SWADE character damage.  
**Setting package:** `rules/SETTING-RULES.md`; unresolved interface: `HEAVY-METAL-INTERFACE.md`.

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
| **CMC-400 Marine** | Size 2 | **+12 Heavy** | 6 | d12+1 | Armor 1, Stabilizer 1, Scanner 1, Self-Sealing 1, Integrated Gear (stim dispenser) 1 | 5/6 |
| **CMC-660 Firebat** | Size 2 | **+14 Heavy** | 6 | d12+1 | 2 Armor 2, Stabilizer 1, Self-Sealing 1 | 4/6; reserve 2 for thermal specialization |
| **5-4 Marauder** | Size 2 | **+16 Heavy** | 6 | d12+1 | 3 Armor 3, Stabilizer 1, Toughness +1 mod 1 | 5/6; external launcher systems separate |

**Every number above is original SWADE adaptation design, not lore.** Original lore gives no numeric armor hierarchy. The 5-4 and 660 likely have similar physical chassis: using Size 3 merely to give the Marauder +18 Armor would alter Pace/Strength and need actual dimensional evidence. Reserve specialty mechanisms for later research rather than inventing armor benefits.

### Specialization that +Armor cannot capture
- **CMC-300:** standard multi-role powered infantry; default visor/comms/sealed environment are already SFC chassis features. Proposed **Stabilizer** on *attached* direct-fire weapons can negate Recoil (SFC p.125); confirm how the C-14 connects to the suit before assuming a carried rifle benefits.
- **CMC-400:** +2 Armor is a proposed upgrade; its integrated gear represents *storage/device*, not the SWADE pharmacological effects of stims. Remaining mod slot can be customized.
- **CMC-660:** known stronger *fire and heat resistance* (P1). The published `Energy Skin` protects from **lasers**, not flame; don't silently use it for fire. A concise heat-resistance feature requires a targeted precedent review; flamethrower integration may exceed the SFC `Integrated Gear` 10-lb limit.
- **5-4:** later accounts report armor optimized for impact/explosions and optional kinetic foam. Existing **Toughness +1 Mod** is a candidate to represent dispersion without inventing a new subsystem. The dual K12 launchers are external equipped weaponry/hardpoints, not free Armor bonuses or necessarily 10-lb Integrated Gear.
- **UED Medic:** Brood War states protective shielding but no mechanical Armor. +6 ordinary gear is a trial baseline, not proof of an unpowered suit. An alternative **Size 1 +8 Heavy Armor medical hardsuit** is possible and would be significantly more protective, with SFC Pace 12/Strength d12 and remaining Mods; compare lore before selection. A **physical medical arm shield** should be evaluated under SWADE Shields rather than assuming a Protoss-style energy shield.

## C-14 comparison using normal character damage
First C-14 candidate (not approved): **2d10, AP 4, RoF 3, Heavy Weapon**. Illustrative wearer Vigor d6, base Toughness 5, no other defenses. AP reduces Armor (not base Toughness), and suit chassis Size is not double-counted.

| Target | Listed Armor | Total Toughness | Effective Toughness vs AP4 |
| --- | --- | --- | --- |
| Medic +6 ordinary | 6 | 11 | **7** |
| CMC-300 +10 Heavy | 10 | 15 | **11** |
| CMC-400 +12 Heavy | 12 | 17 | **13** |
| CMC-660 +14 Heavy | 14 | 19 | **15** |
| 5-4 +16 Heavy | 16 | 21 | **17**, or **18** if its +1 Toughness Mod is used |

**Acing dice diagnostic:** For an already successful C-14 hit **without attack raise**, ignoring Recoil, Cover, RoF multiattack, the target's prior Shaken state, Soak, Bennies, etc.:
| Target | Effective Toughness | Chance damage reaches Toughness (Shaken+) | Chance damage reaches Toughness+4 (Wound+) |
| --- | --- | --- | --- |
| CMC-300 | 11 | approx **55%** | approx **28%** |
| CMC-400 | 13 | approx **40%** | approx **19%** |
| CMC-660 | 15 | approx **28%** | approx **13%** |
| 5-4 (without Toughness Mod) | 17 | approx **19%** | approx **10%** |

These are conditional mathematical probabilities from two exploding d10s, **not a playtest**. Add +d6 to the damage roll for an attack raise. Multiattack/high RoF/Soak/armor vulnerabilities require further encounter testing.

## Heavy Metal class diagnostic
C-14 candidate: average Damage 11 + AP4 = **Weapon Class I** (SFC p.93). Illustrative total Toughness 15/17/19/21 = CMC-300 **Class I**, CMC-400 **II**, Firebat **II**, Marauder **II**. This produces a damaging *class cliff* if vehicle direct-Wound rules are applied automatically to character wearers. See `HEAVY-METAL-INTERFACE.md`.

**Recommendation pending deliberate decision:** normal SWADE damage for individual armored soldiers; Heavy Metal for vehicles/walkers/starships; retain character suit Critical Hits. This preserves a graduated armor benefit without adding an armor tier system.

## Next acceptance tests
1. Inspect edition/page-specific later lore for CMC-300/400 feature differences, Marauder foam and Medical armor.
2. Compare chosen CMC-300 +10 to the real C-14 (its Damage/AP/RoF not yet approved), and check whether ordinary non-Heavy Weapons fail appropriately.
3. Observe suit mobility, basic HUD/stealth/fine-motor penalties, cost/recharge and critical damage at the table.
4. Test flame specialization and kinetic impacts with existing SWADE precedent, without assuming universal resistance.
5. Deliberately choose Heavy Metal/personal armor interface before any suit profiles are promoted to `approved`.
