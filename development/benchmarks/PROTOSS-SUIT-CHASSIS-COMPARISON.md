# Zealot Armor — Physical Armor vs Light Duty Powered Suit

**Research 2026-10-11. Status:** **two competing first-pass chassis models**, neither owner-approved; **do not automatically class all Protoss as Terran CMC**.  
**Blizzard primary:** [Original Zealot guide](https://classic.battle.net/scc/protoss/units/zealot.shtml) says **power suits** enhance psionics, project forearm blades and shields; [Blizzard 20th anniversary developer history](https://news.blizzard.com/en-gb/article/21509420/evolution-complete-reimagining-classic-starcraft-units-for-starcraft-ii) explicitly calls Zealot armor *ornate power armor*. No physical thickness/size, chassis mods, strength die, field generator output or suit mass are specified.

## Source-native SWADE implementation option 1 (first prototyped)
- **Published SFC p.42 Infantry Battle Suit**: +6 **ordinary Armor**, modeled as Protoss-built plating.
- **Custom powered-assistance overlay:** Treat Zealot suited Strength as **d12+1**, rather than natural d10; **this increase is original conversion, not granted by the printed Infantry Battle Suit**. Don't conceal that shortcoming.
- **Personal Force Field**, p.42: +4 Toughness, stacks with physical armor, default physical shield battery rule.
- Vigor d10 gives Toughness **17** (7 base +6 ordinary armor +4 shield), **13** field off; Pace **6** unless additional equipment purchased.
- Main benefit: light rules with no Power Armor Mods; main downside: must invent suit Strength and ignores documented full power-suit construction scheme.

## Option 2 (potentially better RAW chassis): a Light Duty power armor frame
- **SFC printed p.122 Power Armor Frame Size 1:** **+8 Heavy Armor as base**, Pace **12**, Strength **d12**, **3 Mods**, generic unpowered weight **100**, generic credits **$50K**.
- **SFC p.122 Light Duty** is an authentic **negative Power Armor Modification**, **−2 Mods**, giving the suit **two additional available Mod slots** but **removing Heavy Armor status from the suit and any Armor Mods**. Thus Size1 **Light Duty +8 ordinary Armor**, Pace12, Strength d12, **5 total Mod slots**; not Class I/II power armor under this project.
- **SFC p.124 Strength Mod** costs **2 Mod slots for one Strength die type** (not 1!), so an upgraded frame to suited **d12+1** needs **2/5 Mods**. An **Integrated Gear** package (p.125) could then house lightweight forearm psi-blade emitters if its total gear weight fits its 10lb limit, occupying **1 additional Mod**, leaving **2/5** for scanner, extra physical Armor or advanced leg hardware. Individual weapon mode still depends on correct Power Armor mounting treatment.
- **SFC p.42 Personal Force Field** external shield is independent, +4 Toughness; with **+8 ordinary Armor** and Vigor d10, resultant Toughness **19** field on, **15** off. Size1 refers to **suit frame**, not the wearer's automatic natural creature Size.
- Major **tradeoff**: Pace12 is unusually fast and physical Armor+8 may increase resilience substantially over the simpler +6 suit. Published Size1 Strength/pacing shouldn't be silently edited because it doesn't match an RTS speed multiplier.
- Still **not an exact StarCraft engineering stat**: the name `Light Duty` doesn't mean a flimsy Zealot, merely the published quality that removes **Heavy Armor classification** to represent shields/armor distinctively.

## Option 3 — actual Heavy Armor suit with a rechargeable shield
- A standard SFC Size1 or Size2 frame left **Heavy** receives fixed Class I or II under the project rules, and the native p.42 +4 Toughness field **cannot reduce direct Heavy Metal Wounds**.
- If choosing this route, the better native source for a genuine plasma shield is **SFC p.123 Shields**, which consumes Electronics-based Soak charges and recharges in 10min. Its host/power frame/class logic must be fully explicit. A published Power Armor Shields Mod costs **half Size, rounded up**, so **1 Mod on a Size1–2** frame, and charges equal Size (**1 for Size1, 2 for Size2**). This is RAW if the character really wears a suitable power-armor frame; an external shield using charge2 without one is custom.
- Keeping full Heavy Armor **Class I** Zealot and giving a power-armor Shields Mod would be a **mechanically very different** duel vs C-14 than the unclassed Light Duty setups; do not call them identical.
- **No mandatory superiority**: Heavy Metal ClassI protection against ClassI Marine fire can still be *more lethal* than ordinary rolled damage against Toughness19 because every qualifying hit yields 1d3 direct Wounds. A pure Armor +8/Benny shield is not automatically weaker.

## Bottom line for owner selection
**Source-faithful starting preference:** Use **SFC Size1 Light Duty power suit (+8 ordinary Armor, Pace12, d12 Str, 5 Mods)** as a **rules-native alternative** to the earlier `+6 armor/custom Strength` Zealot. **Do not overwrite the first stat block until the owner has seen the choice**, particularly the +2 Armor / +6 Pace change. Give both models comparable Marine rifle/melee threat tests. In either case **do not automatically copy Terran CMC Armor Classes**, which were agreed specifically for suit technology with Heavy Armor.
