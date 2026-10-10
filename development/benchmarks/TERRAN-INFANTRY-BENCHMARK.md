# Terran Infantry — First Mechanical Benchmark

**Date opened:** 2026-10-10  
**State:** `collecting` (rules research/design hypotheses only; **no approved damage, AP, Armor or equipment prices**).  
**Objective:** Create a small SWADE-compatible reference point for ordinary humans, infantry small arms, Marine-grade armor and credible anti-armor tools, without translating RTS damage or making a "Marine class."

**C-14 investigation started:** [C14-MECHANICAL-STUDY.md](C14-MECHANICAL-STUDY.md) compares P1 lore to published SWADE peers. Its Heavy Weapon hypothesis and numeric profile are **draft/testing candidates only**.

## 1. Lore questions before rules
The existing [1998 manual audit](../../lore/research/SC98-MANUAL-AUDIT.md) and [Terran infantry entry](../../lore/entries/terran/infantry-and-roles.md) are first evidence anchors.

| ID | Fictionally grounded requirement | Evidence / limitation | Natural mechanical home |
| --- | --- | --- | --- |
| B-INF-01 | The original-era Marine uses a C-14 Impaler gauss rifle and powered protective life-support armor. | SC98-MANUAL p. 35; this is a *usual profile*, not universal compulsory loadout. | **Two items**, rifle and armor, plus soldier skills |
| B-INF-02 | Confederate-era protective military suits offer substantial environmental and combat protection. | SC98-MANUAL p. 35; **CMC model designation and exact protection statistics require model-specific corroboration**. | Worn power armor, Armor and suit systems |
| B-INF-03 | Firebat gear has specialized heat resistance and integrated flame delivery, differentiated from Marine equipment. | SC98-MANUAL p. 35; review later models separately. | Distinct suit/equipment mode and flame projector |
| B-INF-04 | Ghost psionic talent and training are separate from wearable cloak technology. | SC98-MANUAL pp. 36–37. | PC capability vs suit subsystem, **not** part of initial weapon benchmark |
| B-INF-05 | Specialist anti-armor threats must plausibly exist, rather than making every small arm a universal heavy weapon. | Design objective; **a specific Terran infantry rocket-launcher model is not yet verified by this record**. | Portable launcher + ammunition/warhead or demolition gear |
| B-INF-06 | Armored walkers and space warships require distinct threat scales. | SC98-MANUAL pp. 37–40; SWADE Core Heavy Armor/Heavy Weapon framework. | Target profiles, Heavy Armor/Heavy Weapon eligibility, AP and tactics |

**Do not conflate** a powered suit with the Heavy Armor tag solely because both involve the word “armor.” Research whether a specific suit should qualify as Heavy Armor in SWADE, and how a character wearing it interacts with attacks and environmental conditions.

## 2. Rules baselines: investigate in this order
1. **SWADE Core Rules:** firearms table, auto-fire/RoF, armor/AP, Minimum Strength, Heavy Armor/Heavy Weapon, damage vs objects, Cover, Vulnerable, Called Shots, weapon and vehicle interaction, Soak and Wounds.
2. **Science Fiction Companion (2024):** personal futuristic weapons, energy/projectile distinctions, **Power Armor ch. 5 (printed p. 119+)**, potentially armor modifications; consult actual pages before assigning model numbers.
3. **Vehicle Guide (2020):** scaling/target profile and baseline vehicle durability. It is conversion guidance, not a mandatory point-cost chassis builder.
4. **Foundry design grammar:** [Cross-Project Policy](../CROSS-PROJECT-MECHANICS-POLICY.md). Mechanic-first references, especially device vs payload, mutually exclusive ammunition feeds, and defense interactions. **Do not import catalog statistics unexamined**.

## 3. Foundry precedent crosswalk (candidates, not StarCraft rules)
| Foundry document | Why relevant | Important limitation |
| --- | --- | --- |
| `docs/process/SWADE_HOMEBREW_DESIGN.md` | Role, mechanical home, constraints, scale, counterplay | A design *process*, not a numeric construction system |
| `docs/process/MODULAR_WEAPON_DESIGN_PLAYBOOK.md` | Rifle vs compatible ammo vs integrated weapon mode | Can't force decomposition where explicit weapon profile is cleaner |
| `docs/mechanics/weapons/SCIENCE_FICTION_RANGED_WEAPONS.md` | High-tech portable weapon peers and slugthrower ammunition distinctions | **Closed total-conversion power band**, not unmodified RAW |
| `docs/mechanics/weapons/SCIENCE_FICTION_SPECIAL_WEAPONS.md` | Flame-projector precedent for Firebat equipment | Source-specific high-tech budget; inspect Heavy Weapon status before reuse |
| `docs/mechanics/weapons/SCIENCE_FICTION_LAUNCHER_DELIVERED_ORDNANCE.md` | Launcher/payload division for anti-armor tools | Guided launcher, payload, ammo and resource rules may be non-RAW |
| `docs/mechanics/weapons/AMMUNITION_RULES.md` | Specialized ammo context and explicit compatibility | Different project's shared categories and costs, **not automatically adopted** |
| `docs/mechanics/weapons/WEAPON_PROPERTIES.md` | Resource ownership (Magazine/Supply/Reload, etc.) | Property names/semantics require full, compatible adoption if used |

Connected Foundry workspace inspected on 2026-10-10. Re-read current versions before extracting specific numerical rules.

## 4. Decompose by fiction, not RTS label
**Marine:** person + training + interchangeable suit + rifle + optionally appropriate issued weapon, explosives, comms, medical tools or mission gear. Marine is not a class.

**C-14 baseline:** projectile delivery and damage/penetration are separate considerations. Test Range, Damage, AP, RoF, Shots, recoil, Min Strength, role and ammunition if a source corroborates them. Do not derive these directly from RTS DPS or claims such as “hypervelocity” alone.

**CMC suit baseline:** worn equipment; investigate Armor, environmental seal/life support, power, mobility/encumbrance and possible vulnerable zones. Do not require numerical tracking of every suit feature if it adds no game choices.

**Heavy target baseline:** walkers, tanks, large organisms and ships may need Heavy Armor, higher Toughness/Scale or environmental storytelling—but each requires its own fiction/lore justification. **Ultralisk Heavy Armor is currently only a candidate interpretation**, not a fiat. Ship-scale guns belong to a later subsystem.

## 5. Mechanical design decisions to resolve **before** numbers
| Question | Candidate paths | Current status |
| --- | --- | --- |
| Which equipment balance baseline? | (A) Core + Sci-Fi Companion with StarCraft adjustments; (B) deliberately integrated Foundry-derived equipment ecosystem | **A recommended for first tests; not yet finally approved** |
| Does C-14 qualify as Heavy Weapon? | Normal high-AP infantry firearm vs designated Heavy Weapon or some variant | **Open; no automatic Heavy Weapon tag** |
| Does standard Marine armor qualify as Heavy Armor? | Ordinary Armor/power-suit systems vs Heavy Armor | **Open; research exact suit and SFC text** |
| What anti-armor weapon is on hand? | Rocket launcher, recoilless rifle, demolitions, specialized payload etc. | **Exact lore weapon and loadout need verification** |
| How are suit components priced/repaired? | Published armor rules, simplified systems, or original constrained component rules | **Open; no house rules assumed** |
| How does ammunition compatibility work? | Core/SFC; or explicitly imported Foundry property/supply rules | **Open; cannot mix ad hoc** |

## 6. Mandatory target / attacker test matrix
| Source of attack | Target / defense | Intended qualitative result | Validation concern |
| --- | --- | --- | --- |
| Basic civilian firearm | Unarmored human | Material risk of incapacitation or death | Human-scale baseline, action economy |
| C-14 ordinary ammunition | Unarmored enemy infantry / light Zerg | Serious conventional threat | Damage, RoF and ammunition endurance |
| C-14 ordinary ammunition | Marine in CMC armor | Armor noticeably improves survivability; peer fire still meaningful under plausible conditions | AP, armor value, shooting raises, burst effects |
| Firebat flame projector | Swarm at close range | Close-assault area pressure at real fuel/range cost | Template/Evasion and environmental fire |
| Standard rifle | Armored walker / Ultralisk | Not a standard solution against truly heavily protected targets | Heavy Armor eligibility, Toughness, weak points, Scale |
| Mission-issued anti-armor tool | Armored walker or massive organism | Credible option, with finite ammunition, tactical setup or material cost | Heavy Weapon, AP, positioning, knock-on damage |
| Standard infantry small arms | Armored capital ship | **Not a viable hull-destruction mechanism** | Heavy Armor, encounter framing and rules scaling |
| Anti-ship weapon | Capital ship | Resolve in appropriate ship combat procedures in later phase | Not covered by infantry benchmark |

### Minimum tests to run
- 3–5 representative weapon uses across human armor, CMC armor, and Heavy Armor.
- One typical Marine Wild Card vs an Extra squad to check ROF, cover, Bennies and lethality.
- One armored-walker or heavy-monster interaction with/without a proper anti-armor weapon.
- One meaningful noncombat use of the suit or field equipment.
- Record outcomes (not just expected values): wounds, turns, expenditure, opposed choices, and complexity.

## 7. Conversion candidate ledger — no adopted profiles
| Candidate | Fiction evidence | SWADE candidates | Rule status | Next evidence needed |
| --- | --- | --- | --- | --- |
| C-14 Impaler rifle (original era) | SC98-MANUAL p. 35 | sci-fi slugthrower, automatic rifle, AP/RoF, ammo | Idea | Core and SFC comparison, later weapon references |
| CMC-family Marine suit | SC98-MANUAL p. 35 for Marine suit (no precise model data) | SFC Power Armor chassis and protection | Idea | Model identity, exact environmental/armor features |
| Infantry anti-armor weapon | Plausible role; no specific selected weapon | Heavy Weapon/AP/payload, demolition | Idea | Locate an explicit StarCraft source or document clearly as an original extrapolation |
| Heavy Firebat suit and flamethrower | SC98-MANUAL p. 35 | SFC power armor + flame/area mechanics | Idea | Exact power/range/armor relationship |

## 8. Gate for next iteration
A first numerical candidate is appropriate only once:
1. The project chooses and records a coherent equipment baseline.
2. Relevant SWADE printed pages are examined and cited.
3. Device and payload compatibility are explicit (or intentionally abstracted).
4. We assign a realistic fictional role without canonizing guessed hardware figures.
5. Peer-versus-armor tests demonstrate the claimed outcome.
6. Provisional draft values are marked **candidate/playtest**, never RAW or canon.

**Next immediate deliverable:** a researched side-by-side of Core/SFC personal firearms and Power Armor rules *versus* candidate Foundry weapon models, leading to a small, testable C-14/CMC numerical draft—not a complete equipment encyclopedia.

**CMC follow-up:** [CMC Armor Study](CMC-ARMOR-STUDY.md) now compares Marine/Firebat/Marauder/Medic armor. [Heavy Metal Interface](HEAVY-METAL-INTERFACE.md) records why character-suit versus vehicle damage requires explicit scope.
