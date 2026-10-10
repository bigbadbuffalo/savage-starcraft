# C-14 “Impaler” — First SWADE Mechanical Study

**Status:** **Candidate research, NOT approved or playtested**  
**Date:** 2026-10-10  
**Fictional grounding:** `lore/entries/terran/c14-impaler.md`; SC98-MANUAL p. 35 (direct P1); 2015 *Field Manual*/novels provide only *indirectly verified* supplemental details in this pass.  
**Design method:** `development/CROSS-PROJECT-MECHANICS-POLICY.md`.

## 1. Problem to solve
The C-14 is called a “rifle,” but its P1 profile is a hypersonic 8mm armor-penetrating automatic gauss weapon ordinarily deployed with CMC power armor. Use that behavior rather than mapping directly to an M16 by name. Ordinary infantry can use specialist weapons; C-14 is not a Marine-class power.

## 2. Key SWADE mechanical observation
**Science Fiction Companion, printed pp. 119–123:** Power Armor frames **normally grant Heavy Armor**, with the optional *Light Duty* modification removing that status. At p. 120 and p. 123 the book explicitly classifies standard power armor as Heavy Armor. Under SWADE Core *Heavy Armor* rules, a non-Heavy Weapon cannot damage Heavy Armor regardless of how high the roll Aces (see Core printed p. 82, vehicle note). Therefore:

> **If** default CMC suits are treated with stock SFC Power Armor Heavy Armor **and** C-14 rifles are supposed to hurt those suits, then **a C-14 needs the SWADE Heavy Weapon tag** (or an intentionally new bypass rule). Large AP by itself is insufficient.

This is an interaction conclusion from published rules and the project design goal, **not** proof that Blizzard's name for the rifle is “Heavy Weapon.” It does **not** imply all Heavy Weapons can meaningfully penetrate battleship Toughness/Armor; target durability/scale also matters.

## 3. Published mechanical peers
These are rules examples, **not in-universe StarCraft facts**:

| Source (printed page) | Peer | Damage | AP | RoF | HW | Handling / tactical tradeoff |
| --- | --- | --- | --- | --- | --- | --- |
| SWADE Core p. 75 | M16 rifle | 2d8 | 2 | 3 | No | 20/30 shots, modern baseline |
| SFC p. 57 | Hi-tech slugthrower assault rifle | 2d10 | 4 | 3 | No | 30 shots, Min Str d6, Wt 10 |
| SFC p. 57 | Heavy machine gun | 2d10 (I) | 4 | 3 | **Yes** | 50 shots, Min Str d10, Wt 40, Snapfire unless mounted |
| SFC p. 57 | Sniper rifle | 2d12 (I) | 4 | 1 | **Yes** | 6 shots, Snapfire, long-range aimed fire |
| SFC p. 52 | Heavy blaster rifle | 3d6+4 (I) | 4 | 1 | **Yes** | 20 charges, Snapfire; *particle* delivery, not kinetic spikes |
| SFC pp. 119–123 | Size 2 power armor | base +10 Heavy Armor, d12+1 Strength | — | — | — | Powered chassis; more Armor possible |

The most relevant numeric precedent is **the SFC heavy machine gun**, combining infantry-portable kinetic Heavy Weapon damage, AP and RoF. This is *not* a claim that the C-14 physically is a contemporary HMG. The Foundry total-conversion weapons catalog uses a different closed equipment system; see cross-project policy and do not import its numbers automatically.

## 4. Rate-of-fire caution
The later **reported** 30 rounds/second is a *cyclic rate*, not a SWADE Rate of Fire 30. In **SWADE Core printed p. 93**, RoF is the number of Shooting dice. RoF 3 represents **10 actual bullets** per attack (as tracked), and ordinarily applies Recoil –2 when firing more than RoF 1 (Core p. 105). RoF 3 is a convenient abstraction for very fast burst fire; no literal one-second cyclic mapping is intended.

Magazine size and real spent bullets are different questions. At 500 projectiles, a magazine would permit ~50 fully tracked RoF 3 actions, but **500 is currently a secondary-source claim** requiring variant-specific verification. Don't build balance around that specific number yet.

## 5. First candidate, deliberately incomplete (C14-DRAFT-A)

| Parameter | Proposed first-test value | Basis / caveat |
| --- | --- | --- |
| Category | **Heavy infantry automatic gauss rifle** | Descriptive conversion category; official name remains C-14 Impaler |
| Damage | **2d10 (I)** | **SFC heavy MG analogy**; non-final |
| AP | **4** | SFC heavy kinetic weapon analogy; P1 establishes armor penetration *role*, not this exact AP |
| RoF | **3** | Conventional SWADE abstract burst/automatic fire; not literal 30/sec |
| Heavy Weapon | **Yes (candidate)** | Necessary for standard SFC power-armor-on-power-armor combat without a new bypass rule |
| Range | **30/60/120 to 50/100/200**, test alternatives | SFC heavier automatic vs HMG precedents; exact effective range absent from P1 |
| Shots | **Unassigned**; investigate claimed **500+** for specific variants | 1998 manual doesn't state this |
| Minimum Strength | **d10 candidate unsupported**; compatible CMC boosts Strength | Analogy to SFC heavy MG, **not** a lore hard requirement or categorical prohibition on unarmored use |
| Weight | **Unassigned** | Art proportions don't give a credible mass |
| Grip / recoil | Normal SWADE Recoil, and possible **compatible suit stabilizer** to negate it | CMC recoil control reported in expanded lore; requires explicit rule and source verification |
| Reload & power | Use existing SWADE reload rules; don't add capacitor counters yet | P1 capacitor throttles bursts without specifying a charging delay |

**This is a mechanical hypothesis, not a released item.** A less aggressive alternative is normal assault-rifle Damage/AP with Heavy Weapon as a kinetic-penetrator exception; compare both in tests before choosing.

## 6. Armor interaction, including counterargument
With SFC baseline power armor (printed p. 122) a Size 2 frame grants **+10 Heavy Armor** and up to **+16** with modifications. This is much tougher than normal infantry battle armor (+6 at SFC p. 42). An unmodified SFC assault rifle has AP 4 but **no Heavy Weapon tag**; it cannot damage the +10 Heavy Armor suit at all. A Heavy Weapon-tagged C-14 with AP 4 could hurt an armored opponent, but must still exceed their Toughness to Shake or Wound.

**Counterargument to test:** Giving such a common rifle Heavy Weapon status makes it *eligible* to damage **any Heavy Armor**, including some vehicles. But eligibility is not actual penetration: tank and starship Toughness/Armor can be much higher. If a specific starship hull remains mechanically vulnerable to repeated rifle attacks despite very high protection, solve **scale** at the ship/hull layer rather than wrongly rewriting the C-14 as a conventional 5.56 rifle.

**Alternate path:** Mark CMC as Light Duty (ordinary armor) and keep the C-14 as a non-HW rifle. This may suit a deliberately gritty, lower power-band campaign but should be explicitly justified against its design as full-scale power armor; it is not recommended solely to avoid HW eligibility.

## 7. Design tests before adoption
- **Unarmored civilian:** Rifle should be decisively dangerous, not a generic 5.56 clone.
- **Zergling / Hydralisk:** Should create credible anti-organic threat; avoid giving identical protection to all Zerg creatures.
- **Size 2 CMC-type power suit +10 Heavy Armor:** Peers should be capable of hurting each other, but need solid hits / positioning; evaluate RoF, Raise, Cover, AP, soak.
- **Up-armored CMC +16:** Should resist ordinary bursts better; avoid literal peer-fire immunity.
- **Walker / heavy monster:** HW means eligibility to damage; penetrative effectiveness should remain constrained by Toughness/AP and actual fictional armor.
- **Battlecruiser:** Infantry gunfire should not produce credible ship-hull destruction; review catastrophic scale separate from HW tag.
- **Unsuitably equipped shooter:** Investigate whether C14 variant can be operated by an unarmored person at penalty or with supported rest; do not declare an absolute prohibition.

Compare candidate `2d10 (I), AP 4, RoF 3, HW` against (a) Core modern infantry, (b) SFC assault rifle, (c) SFC heavy MG, (d) SFC power-armored infantry and (e) relevant future StarCraft peers. Record actual attack/damage outcomes, not only average dice.

## 8. Foundry relationship
Reuse the Foundry project **mechanical-home method**, especially differentiating the host rifle, compatible ammunition/payload, power interface, stabilizer and optional targeting aids. Keep **base hardware**, **ammunition**, **operator/suit compatibility**, and **rules automation** separate. All numeric precedent in this document comes from **published SWADE**, not the Foundry project's closed total-conversion catalogs.

## 9. Findings and proposed working direction
1. **Fiction:** Unusually powerful, armored-infantry-oriented automatic firearm; official name is “Gauss Rifle.”
2. **Mechanical role:** Treat as a **heavy infantry primary arm** rather than a default modern rifle.
3. **First interaction hypothesis:** **Heavy Weapon** deserves priority testing because ordinary SFC power armor has Heavy Armor. Not yet approved.
4. **Do not invent** velocity, projectile mass/length, rifle weight, power drain, capacitor cooldown, warship armor penetration, or exact 500-round standard magazine size.
5. **Next research:** Direct Field Manual and novel cross-check, then numerical attack tests and companion suit design.
