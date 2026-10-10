# Terran Heavy Metal Combat — First Numerical Diagnostic

**Status:** `draft` empirical *computational benchmark*, **not a tabletop playtest** and not final equipment approval.  
**Run date:** 2026-10-10; deterministic PRNG seed **20261010**; **300,000 shooting actions per case**.  
**Method script:** `HEAVY-METAL-FIRE-SIM.py` (NumPy).  
**Official rules:** SWADE Core pp. **87–88** (Wild Die/Acing), **93** (Rate of Fire), **105** (Recoil), and SFC pp. **45**, **47** (3RB), **93** (Heavy Metal), **125** (Stabilizer).

## Inputs and scope
- Attacker Shooting **d6** (except specified d8 veteran), target TN **4**, no Range/Illumination modifiers, unless Light Cover **–2**. Wild Cards roll **one Wild d6 per firing action** that may replace the lowest Shooting die, **not add a fourth hit** at RoF3.
- C-14 **draft** Damage 2d10/AP4/Heavy Weapon/RoF3 = **Class I**. RoF3 rolls three Shooting dice and normally incurs **Recoil –2**. A valid **mounted/stabilized** firing position removes that –2.
- **Class I wearer:** 1d3 Wounds on a successful hit plus 1 Wound for a raise. **Class II wearer:** 0 Wounds on ordinary hit or 1 Wound on a Shooting raise.
- **All RoF3 Shooting dice are deliberately assigned to the *same target*.** Separate successful Shooting dice create separately resolved hits; cumulative total Wounds across those hits are summed **for analysis only**, not automatically treated as one hit or one suit Critical Hit.
- The experiment deliberately excludes **Soak, Bennies, rerolls, damage Incapacitation resolution, armor Critical Hits/breaches, mounted weapon deployment, suppression, Tests, Support, Aim, Fighting, out-of-ammo checks, Innocent Bystanders, and Initiative**. It also excludes actual dice damage for unclassed targets and the Firebat's flame hazard. Thus **pre-Soak four-plus Wounds is *not* the same thing as final PC death probability**.
- This is a mathematical SWADE-combat sanity check, not StarCraft lore data or actual playtest evidence.

## Monte Carlo outputs (all probabilities **per shooter action, before Soak**)
| Attacker and situation | P(≥1 successful hit) | Avg. hits | Avg. Wounds vs Class I | P(≥4 cumulative Wounds vs I) | P(≥1 Wound vs II) |
| --- | ---: | ---: | ---: | ---: | ---: |
| Extra d6, RoF3, Recoil –2, open | **42.2%** | 0.50 | 1.26 | 12.3% | 23.1% |
| Extra d6, RoF3, Recoil –2, Light Cover –2 | 36.1% | 0.42 | 0.92 | 6.1% | 8.2% |
| Wild Card d6, RoF3, Recoil –2, open | **51.6%** | 0.66 | 1.66 | **18.0%** | **29.3%** |
| Wild Card d6, RoF3, Recoil –2, Light Cover –2 | 45.2% | 0.56 | 1.23 | 9.8% | 10.7% |
| Wild Card d6, **fully stabilized** RoF3, open | **93.7%** | 1.93 | **4.42** | **62.4%** | 44.9% |
| Wild Card d6, stabilized RoF3, Light Cover –2 | 51.8% | 0.67 | 1.67 | 18.1% | 29.4% |
| Veteran Wild Card d8, Recoil –2, Light Cover –2 | 42.4% | 0.51 | 1.29 | 13.1% | 23.9% |
| Wild Card d6, **RoF1 unmodified** open | 75.0% | 0.75 | 1.76 | 8.8% | 26.0% |
| Wild Card d6, **RoF1 unmodified** Light Cover –2 | 30.6% | 0.31 | 0.77 | 5.3% | 15.9% |
| Wild Card d6, **3RB RoF1 +1 Shooting** open | **88.9%** | 0.89 | 2.08 | 10.2% | 30.6% |
| Wild Card d6, 3RB RoF1 +1 Shooting, Light Cover –2 | **55.6%** | 0.56 | 1.32 | 7.1% | 20.9% |

**3RB caution:** SFC grants **+1 ordinary damage** in 3RB mode, but Heavy Metal replaces the damage roll with Weapon/Target Class Wound results. This benchmark does **not** add 1 automatic Wound or recompute Class per hit. Using Class I in both modes is an intended initial interpretation and should be explicitly checked if the rifle ever sits at a Class threshold.

### Interpretation
1. The **Class threshold** establishes an actual heavy-shock-armor niche. The Class I rifle can kill a Class II wearer **on Shooting raises** but cannot reliably cause Wounds through ordinary hits.
2. **Marine versus Marine lethality is high**, as owner requested. One wild-card d6 firing action without stabilization has a **pre-Soak 18%** chance of a cumulative four-plus Wounds across its RoF hits if target Class I and open. This is **not automatically an Incapacitation rate**; separately resolved hits, Bennies and Soak matter.
3. **Recoil mitigation radically changes combat outcomes**: 1.66 → 4.42 average pre-Soak Wounds vs Class I for unbraced versus stabilized RoF3 at TN4. This makes *whether* a C-14 can use the suit Stabilizer a genuine tactical decision, not flavor text.
4. **Cover strongly matters** (particularly against Class II, where only raises penetrate). Tactical combat may remain engaging despite extremely lethal peer weaponry.
5. **3RB mode is a promising controlled-burst model** drawn from published mechanics. Don't assume it literally represents a canonical three-spike C-14 capacitor cycle.
6. **Mod budget pitfall:** SFC Stabilizer helps **attached** weapons only, not all carried weapons. At a provisional C-14 weight of 20 lb, SFC p.45 Mounted Weapon allows bipods/tripods, which automatically handle Recoil when actually used. This offers a simple **no-new-rule** alternative to universal CMC recoil cancellation.

## Heavy Metal escalation comparison (exact class formulas, not simulation)
| Example | Published / draft figures | Avg. Damage + AP | Heavy Metal Class | Role vs draft Class II heavy infantry |
| --- | --- | ---: | --- | --- |
| C-14 **draft** | 2d10/AP4/HW | **15** | **I** | 0 Wounds ordinary; 1 on raise |
| Stock **SFC heavy MG**, p.57 | 2d10/AP4/HW | **15** | **I** | Same Class effect |
| Stock **SFC sniper rifle**, p.57 | 2d12/AP4/HW | **17** | **I** | **Does not become Class II just for being a sniper rifle** |
| **Hypothetical HEV/penetrator rifle**, **NOT approved** | 2d12/AP8/HW | **21** | **II** | **1d3** on ordinary hit; 1d3+1 on raise |
| Stock **SFC medium autocannon**, p.58 | 4d8/AP6/HW | **24** | **II** | **1d3** on hit; vehicular weapon requiring mount |
| Stock **SFC light rocket**, p.56 | 6d6/AP16/HW | **37** | **III** | **1d3+1 Wounds** on hit; SFC rocket is a template-based military weapon |

**Specialist weapon design principle:** When a scenario calls for the ability to reliably defeat Marauder-grade Class II armor, field a genuine **Class II or higher weapon** (or permitted specialized warhead), rather than giving ordinary C-14 ammunition a fake universal “anti-tank” property. A normal grenade launcher and many rifles remain Class I in this system. **SFC high-AP slug ammunition (p.56) does not necessarily cross a Class boundary**; the math must be done.

## Limitations and next tests
- The exact C-14 Shots/Weight/Range/3RB/mount compatibility are placeholders; validate lore and handling before formal player publication.
- Follow up with actual tactical encounters involving initiative, several Marine Extras, one Firebat/Marauder, varying cover, combined arms, and **Soak/armor Critical Hits** to measure *table burden* and lethality, not merely probability.
- Test ordinary damage versus unclassed soft targets separately. Do not extrapolate this vehicle-class table to Zerglings or other creatures until bestiary design.
- Test Firebat's plasma/flame offense and bespoke thermal defense independently of its class rating.
- An explicit **“Heavy Metal Warheads”** provision exists on SFC p.93; only apply a warhead's Class adjustment when that weapon/ammunition is actually eligible under the published warhead equipment rules.
