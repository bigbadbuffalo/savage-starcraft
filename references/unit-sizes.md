# Historical Unit Sizes — Provenance and Review Queue

**Status:** Preliminary working reference; **not canonical** and **not approved SWADE Sizes**.

## Origin
The project owner supplied an older two-page file, `Unit_Sizes.pdf`, based on artwork and estimates. The original spreadsheet is unavailable, and the values were explicitly described as potentially wrong. This summary preserves notable rows and questions without uploading that PDF to the public repo. Measurements in this section are **transcribed from the user-supplied file**, not verified Blizzard specifications.

The PDF pairs approximate measurements (usually feet) with a proposed Savage Worlds Size value, but does **not** consistently say whether a value is height, length, wingspan, or a model's largest dimension. At extreme scale these distinctions are indispensable.

## High-priority review table

| Unit / original row | Original measurement | Original Size | Research issue |
| --- | --- | --- | --- |
| Marine | 7.5 ft | 1 | Does this measure armored height? Variant/armor? |
| Hydralisk | 12 ft | 3 | Height vs curled body length, strain differences |
| Ultralisk | 84 ft | 12 | Compare with Brood War row at 36 ft / Size 8; distinguish strain and interpretation |
| Colossus | 156 ft | 12 | Mechanically suspicious tallness-to-Size relationship; confirm scale and SWADE Size/volume separately |
| Brood Lord | 102 ft | 12 | Threshold and dimensional-axis check |
| Raven | 213 ft | 15 | Check recorded axis/model and Size threshold |
| Battlecruiser (Behemoth/Minotaur) | 1,650 ft | 28 | Two classes grouped; determine actual type/length and source |
| Battlecruiser (Gorgon) | 4,800 ft | 31 | Determine actual class dimensions from official sources |
| Zerg Leviathan | 7 km | 34 | Another row lists a “Leviathan” at 38 km in the Protoss section; likely a labeling/provenance problem |
| “Leviathan” (Protoss-page row) | 38 km | 38 | Identify intended craft; do not infer existence of a Protoss Leviathan |
| Probe (first row) | 6 ft | 0 | Second Probe row shows 48 ft/Size 9; probable transcription issue |
| Probe (second row) | 48 ft | 9 | Identify what entry was supposed to be |
| Mothership | 5 km | 35 | Confirm model type, measurement axis and independent source |
| Spear of Adun | 74.4 km | 40 | Check spaceship Size table bounds separately from canon length |

## Mechanical sanity rules
- **SWADE Size is not identical to height**. The *SWADE Vehicle Guide* (printed pp. 4–6) stresses the targeting profile/volume and cautions that length and mass are approximations. SWADE creature Size and vehicle Scale also require attention.
- Do not assign a precise mechanical Size from a single silhouette when width, mass, physiology, or class is unknown.
- Do not turn cinematic/RTS map scaling into fictional measurements by default.
- Keep `canonical_dimensions` (with axis/source) distinct from `conversion_size`, `armor`, `toughness`, and `encounter_role`.
- The 2015 *StarCraft II Field Manual* includes scale art and specifications; Blizzard's article credits scale artist Robert Rose. Source: https://news.blizzard.com/en-gb/article/19958657/the-starcraft-ii-field-manual-a-closer-look . Obtain and cite **actual Field Manual pages** before marking those figures authoritative.

## Next steps
1. Reproduce every PDF row into a structured table with named faction, model/variant, value, unit, measurement axis, old Size, citation status and review status.
2. Check each original number against firsthand manuals, in-game narrative and official references (especially Field Manual artwork with context).
3. Resolve two Probe rows and miscategorized Leviathan before numerical conversion.
4. Map dimensions to SWADE Size/Scale using appropriate creature/vehicle rules, then audit Toughness/Armor and real encounter interactions separately.
