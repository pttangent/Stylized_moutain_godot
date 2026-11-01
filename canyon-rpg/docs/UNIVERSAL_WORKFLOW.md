# Universal scene-art production workflow

**Canonical principle:** scene content, world rules, presentation shot configuration, asset families, target renderer and optional interactivity are discovered from user inputs, **not invented by the prompts**. This workflow works for varied scene types, scales, styles and levels of abstraction. The repository also contains historical case data; it must not be treated as an implicit input in a new scene.

## Source and configuration discovery

Read the user brief, attached references, existing scene/assets, project configuration, prior approvals and available tools. Do not assume an image, 3D source model, **presentation camera**, world unit, target engine or character. The standard CAM_QA_45 engineering camera is a separate P1 diagnostic after 3D geometry exists. Derive `scene_profile.json` from actual sources; unknown fields remain `UNSPECIFIED`, and blockers are raised only where they prevent the selected outcome. Read `docs/SCENE_PROFILE_TEMPLATE.md` for all profile fields. Examples are deliberately separated into `docs/SCENE_TYPE_EXAMPLES.md` and only apply on explicit selection.

For source records, distinguish `OBSERVED` (visible/documented), `APPROVED_DESIGN` (user-approved interpretation), `INFERRED`, `GENERATED_CANDIDATE` and `UNKNOWN`. Never infer physical accuracy from a generated mesh or a single reference image. Do not prefer one vendor, procedural technique or modeling style without evidence.

## Phase map

| Phase | General task | Mandatory gate | Conditional work |
|---|---|---|---|
| 00 | Inventory, tools, source/provenance and target outputs | Inputs/constraints identified | Importers, renderer and runtime setup only when selected |
| P0-A | Scene understanding and spatial/visual intent | Auditable brief, reference-to-geometry expectations, uncertainty | Measured layout, source registration and multi-view triangulation when supported |
| P0-B | Build a reusable scene blueprint | Consistent IDs, representation choice, coordinate assumptions and review views | Heightfields, circulation graphs, simulation graphs, geometry masks only if relevant |
| P1-concept | **Default:** editable Blender art blockout | Approved composition, scale relationships, silhouettes, geometry continuity via real renders | Optional surface-specific QA |
| P1-playable | **Opt-in:** adapt an approved scene for runtime navigation/interaction | Tested selected interactions without unapproved art regression | Collision, navigation, character or vehicle only if required |
| P2-A | Art-direction system based on inputs | Style specification and representative references | Material, animation or lighting constraints where applicable |
| P2-B | Representative visual slice/lookdev | Captured comparison evidence in the selected renderer | Engine checks when a real-time target is part of the brief |
| P3-A | Component inventory | Provenance, unique IDs, reusable vs unique decisions | Asset-specific dimension/UV/rig/physics needs |
| P3-B | Asset production/validation | Repeatable mesh sources and representative scene checks | Procedural generation, model assistance, LOD, collision, atlases based on need |
| P4-A | Relevant procedural or derived-data systems | Reproducible algorithm/input/output when selected | Skip entirely if no such systems are needed |
| P4-B | Scene assembly and targeted variation | Reproducible composition and visible consistency | Scatter, instancing, simulation, route checks when selected |
| P5-A | Independent visual QA | Source/render evidence with named shot IDs and actionable defects | Specialized review categories only when in scene |
| P5-B | Final technical/production QA | Actual test evidence, provenance and acceptance limitations | Runtime physics and performance only if target requires them |

P2 may follow P1-concept directly. There is no mandatory P1-playable handoff. The number, type, projection and aspect of **presentation** views are determined by the scene profile. A one-shot presentation is allowed; complex spaces may require multiple shots. Separately, all actual Blender P1 scenes use a fixed CAM_QA_45 engineering view for repeatable visual regression.

## Representation selection

Identify what truly needs to exist. Use modular/hard-surface topology for repeatable manufactured structures, sculpted/mesh forms for controlled irregular structures, a heightfield when the surface is single-valued, curves for path-like geometry, simulations only where behavior must be simulated, and instances for repeatable components. All are *candidates*, not defaults. Choose the simplest editable representation that preserves required silhouettes and cross-view depth.

Define each feature in a reference-to-geometry contract with a stable ID, source evidence, shape relationships, allowed redesign, dependencies and relevant views. The contract may have **text/design references without pixel positions**. Preserve original source data; log design changes separately.

## Blender and coordinates

Blender is the default **P1-concept authoring tool in this repository**, but that does not choose an output engine. Record unit scale, handedness, up/forward axes and export transforms from actual target settings. Never assume a universal world scale or implicitly apply a conversion twice. Author objects with stable `art_id`, `art_owner`, `art_revision`; perform scoped mesh-data replacements where safe. Keep a versioned editable source and reproducible generators if used.

## QA gates: avoid false confidence

- Structural validators check IDs, required fields and dependencies; they do **not** approve artistic results.
- Projection of semantic anchors and optional ray tests are diagnostic only; they do not prove full geometry silhouettes, opacity or visual matching.
- Visual acceptance needs real renders for the **approved presentation shot list**, plus a locked QA_45 engineering baseline when 3D geometry exists; compare against relevant evidence.
- Physical/navigation/performance criteria require actual test execution only when applicable. Mark `NOT_APPLICABLE`, `NOT_RUN`, `ASSUMED`, `PASS`, `FAIL` accurately.
- Every edit records affected stable IDs, inputs/seed, evidence, review views, before/after files and remaining issues; do not regenerate unrelated approved objects.

## Prompt resolution and legacy isolation

Use `prompts/en` or `prompts/zh` canonical universal prompts. Individual tasks (e.g. P1-concept) are the source of truth; P0/P2/P3/P4/P5 summary files are routers. `prompts/legacy` contains explicitly selected historical specialist instructions and must never be imported as general requirements. Existing blueprint/model/report files from an earlier project remain prior artifacts and are not silently reused for new scenes.

## Scene-independent fixed 45° engineering view

Always instantiate **CAM_QA_45** once S1 Blender geometry exists: 45° elevation above Blender XY, an orthographic technical inspection camera (default 16:9), framed to actual bounds and then locked for before/after iterations. It is **not the final artistic camera**. Additional views must resolve occluded geometry when necessary. See `docs/QA_CAMERA_45_STANDARD.md` and `blender/scripts/ensure_qa_45_camera.py`.

