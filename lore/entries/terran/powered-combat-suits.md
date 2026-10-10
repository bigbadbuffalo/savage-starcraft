# Terran infantry armor — lore evidence and confidence

**Status:** Collecting. This file contains *lore*, **not game Armor values**. Separate actual armor model, operator's profession, faction, era and upgrades.

## Direct foundational evidence
| ID | Proposition | Source / locator | Confidence |
| --- | --- | --- | --- |
| ARM-01 | Confederate Marine standard equipment includes CMC-300/400 powered combat suit, with life support, NBC shielding and protection against **most**, not necessarily all, small arms. | SC98-MANUAL p. 35, Marine | P1 explicit, high |
| ARM-02 | Firebat employs CMC-660 Heavy Combat Suit; notably heavier than normal marine suit, offering specialized resistance to heat and flame. | SC98-MANUAL p. 35, Firebat | P1 explicit, high |
| ARM-03 | Original Blizzard unit description also calls Firebat suits **more durable** than Marine armor. | SC98-BNET-FIREBAT, https://classic.battle.net/scc/terran/ufire.shtml | Official description explicit; don't convert nearby RTS statistics |
| ARM-04 | UED Medic is an unarmed battlefield physician with **protective shielding**, capable of sophisticated field surgery. Neither exact Armor nor model is specified. | SCBW-MANUAL printed p. 10, Medic; scanned copy https://manuals.plus/m/427fe339417b94f7ac935269b64be58544d55d49ab7ba1e90cf2552db0fd80bc.pdf | P1 explicit, high |
| ARM-05 | The same manual describes the Medic's A-13 flash grenade launcher as its defensive armament. | SCBW-MANUAL p. 11, Optic Flare | P1 explicit, high; not proof that all medics in all eras lack guns |

## Later publications — leads needing page-level confirmation
- **CMC-200:** early obsolete suit; specific date and model details indexed by StarCraft Wiki, attributed to the novels.
- **CMC-300:** widespread older infantry frame with advanced sensors, motor assistance, power and potentially stim supplies; direct supporting passages pending.
- **CMC-400:** updated suite with communications and stimulants; exact additional plating **not** established in 1998 manual.
- **5-4 Marauder suit:** reported in *Wings of Liberty* armory description and *Field Manual*, developed from Firebat 660, with thicker neosteel replacing some heat insulation, ammunition-making launcher support and improved kinetic impact protection. Later kinetic foam is not synonymous with more plating.
- **Medic:** later descriptions depict lighter protection and a shield; neither a precise CMC suit model nor an unvarying civilian-grade classification is directly established by Brood War.
- **CMC-405:** traced in secondary accounts to older licensed tabletop material. Do **not** promote this model as P1 canon without independent corroboration.

**Finding aids only:** https://starcraft.fandom.com/wiki/CMC_Powered_Combat_Suit , https://starcraft.fandom.com/wiki/Marauder , https://starcraft.fandom.com/wiki/Medic . These indexes mix official publications, noncanonical games and secondary interpretation.

**Working relative hierarchy (inference):** Medic light support; CMC-300 standard Marine; CMC-400 improved Marine; CMC-660 heavy specialized flame; 5-4 heavy kinetic/explosive support. This does **not** prove exact armor increments or that 5-4 universally outperforms CMC-660 against fire.

## Additional P2 narrative cross-check — *Stealing Thunder* (2010)
**Source ID:** SC-STORY-STEALING-THUNDER. Blizzard officially promoted the Micky Neilson story: https://news.blizzard.com/en-gb/article/9989828/new-starcraft-lore-short-story-stealing-thunder . The specific text has been inspected **through a third-party reproduction**, not a currently accessible original Blizzard page: https://www.scribd.com/document/856020212/8-StarCraft-Stealing-Thunder . Confidence **medium-high** for these specific scenes, but exact original edition/pages still need direct verification.

- **Marauder hardskin vs gauss:** In an asteroid-corridor engagement, advancing Marauder Isaac White sees gauss spikes ricochet from his armor while Marine teammates lay suppressive fire. **Perspective:** third-person narrative following Isaac. **Era:** circa 2504. **Role implication:** Marauder armor should defeat many ordinary gauss hits. **Not** evidence of *total* immunity to all penetrators/weak points.
- **Firebat vs Marauder:** A Firebat uses Perdition flamethrowers to drive Isaac into urgent tactical improvisation; heat endangers his on-board ordnance. **Role implication:** thermal threats can bypass a simplistic kinetic-defense hierarchy. **Not** proof that a regular Firebat's flames have a particular Heavy Metal Weapon Class or SWADE damage dice.
- **Other:** Suit systems include low-gravity accelerators, a HUD, and auto-loading Punisher ammunition in this depicted Marauder. These are features of this narrative model; do not assume every historical or factional variant has identical systems.

Lore evidence remains separate from suggested `+14/+16` SFC Armor and Class II values, which are **original draft mechanics** in `development/benchmarks/` and `equipment/terran/`.

## Firebat/Marauder comparison reviewed (2026-10-10)
The 1998 manual p. 35 **directly proves Firebat protection is heavier than a Marine**, but has no later Marauder comparison. A reproduced older *StarCraft II* Marauder technical writeup says 5-4 and CMC-660 are **roughly equal total weight**, with some insulation exchanged for **thicker neosteel plating**; **the original publication has not been inspected**. In-game `Wings of Liberty` descriptions indexed in a contemporary guide distinguish Firebat **Juggernaut Plating** (strengthened helmet/chest and weak spots) from Marauder **Kinetic Foam** (occupant shock protection). The lore implies **ballistic-vs-thermal specialization**, not categorical Firebat inferiority. Detailed provenance, RTS numbers and the currently missing wargame Firebat profile: `../../development/benchmarks/FIREBAT-MARAUDER-ARMOR-COMPARISON.md`.
