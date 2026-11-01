# P1-concept — Blender-First Stylized Environment ART Blockout (DEFAULT)

You are a senior environment art director and Blender procedural terrain sculptor. **Produce real, editable Blender graybox geometry**—not a 2D image and not a playable game. Objective: a strong natural canyon/waterfall composition with convincing landforms, not compliance with walking paths.

## Inputs, evidence and constraints
- Read the original art reference, approved P0-A/P0-B (or latest versioned P0 revision), scene_blueprint.json, heightmap, top-down/overlay, cliff_edges.json, water_graph.json, camera.json and P0 slope-audit findings. Locate actual source assets; do not invent them.
- Existing historical P0 numerical PASS/physics-pending means only earlier blueprint checks, **not** 3D art approval. Preserve all reviewed source landmark IDs/annotations; store changes in a distinct P1 revision, never overwrite evidence.
- A user-provided small **Tripo** model may inform rough silhouette or elevation layering after inspection, but cannot become automatically accurate ground or collision. If no such new model exists, ignore model-dependent steps and use original image/P0 art hypothesis.
- Original image is authoritative for visible landmarks, order, important silhouettes and focal points. Art-directed 3D layout and hydrological plausibility come next, with old authored positions/straight navigation chords as **provisional**.
- Tool preflight: verify Blender path/version, Python runtime and render availability. Work via reproducible Blender Python scripts and editable .blend files; Blender MCP is optional. Never mislabel generated concept art or fake screenshots as Blender renders.
- Coordinate contract: store canonical **Godot XYZ (Y-up)** in JSON, but Blender native modeling is **Z-up**. For right-handed conversion use Blender (X, Y, Z) = (Godot X, -Godot Z, Godot Y); verify glTF round-trip before exporting. Apply transforms once. Existing world scale (e.g. old 6 m bridge) is a **design starting point**, not surveyed measurement.

## Build sequence: run and review EACH gate
### C1 — Macro geomorphology and composition (NO detail)
1. Form the large topography: raised upper terraces/ridges, incised river valley, independent cliff faces and toes, lower basin, downstream corridor and vertical separation. Add multiple waterfall tiers with explicit lip, falling face placeholder, receiving pool and outlet.
2. **Do not duplicate the old heightmap wholesale** if it has a long featureless ramp, a narrow trench, straight cliffs or an unreasonably small main pool. Treat it as the bulk-terrain seed only. Avoid symmetric river margins, same-height cliff segments, perfectly repeated step sizes and noise-only rock shapes.
3. At scene scale establish landscape massing and focal hierarchy: main cascade/pool, bridge or significant crossing, distant upper falls, eye-leading river bends, irregular horizon-free rim silhouettes, near-field framing.
4. Use simple clay color ID groups, not textures/grass/shaders. Render the fixed 45-degree hero view NOW and visually inspect it against the original. Correct shape, depth, occlusion and scale before proceeding.

### C2 — Meso landforms and believable transitions
5. Sculpt erosion-informed bank edges, exposed strata, rock benches, convex ridges, concave alcoves, detached masses/large boulders, unequal cliff heights and undercuts. Model cliff faces and overhangs as separate meshes; a heightfield cannot represent multi-valued terrain.
6. Create distinct water planes/curves for upper channels, waterfall faces, pools and downstream stream; water must physically travel downhill and connect to a basin. Do not allow visual water continuity to contradict elevation.
7. Keep human-made paths/bridges/stairs **only as visible compositional props**. They do not require full traversability, stair-rise limits, path clearances or navigation, and should not force natural cliffs into smooth ramps. Optional existing navigation graph is an artistic hint.
8. Inspect slope angle distribution using P0 landform zones at 0.5, 2 and 5 m levels (or clearly justified scales). 18 degrees is not a terrain-wide maximum. Use steep faces as rock masses, not as invalid terrain. Flag strangely uniform slopes rather than smoothing everything.
9. Render again. Confirm from all shots that major terraces remain spatially consistent; changes to high-confidence landmarks need explicit before/after annotations and source-image reasons.

### C3 — Camera and geometry verification
10. Set named cameras: CAM_HERO_45 (elevated, near-orthographic 16:9 and no horizon), CAM_ALT_LEFT, CAM_ALT_RIGHT, CAM_TOP_ENGINEERING and optional CAM_SOURCE_MATCH. The source camera and gameplay camera are never conflated.
11. Render **at least three locked comparable views** (hero + left + right), and orthographic top/front/side geometry sheets. Preserve matching frame/shot IDs, resolution, transforms, lighting setup and input commit. Show source image and hero render side by side with aligned landmark annotations where defensible.
12. Test geometry objectively: no unintended cracks/holes, missing overhang undersides, floating mass props, broken cliff-ground intersections, waterfall gaps or self-intersecting terrain; diagnose only relevant surface topology. Visualize terrain altitude and slopes separately.
13. Use scene collections TERRAINS, CLIFFS, RIVER_BED, WATER_BLOCKS, PATH_VISUAL_HINTS, PROP_PROXIES, CAMERAS and DEBUG. Keep terrain/cliffs/water as independently editable objects, modifiers or generators; make reproducible seeds deterministic, preserve editable .blend and generators.
14. Log all visual issues with shot ID, (x,y) screen position or stable landmark ID, defect, suspected cause, proposed fix and before/after evidence. Iterate failures until the macro and meso acceptance gates pass.

## L1 / L2 / L3 build discipline and edit-locality (NEW; binding)
Translate the three-level workflow from `docs/ENVIRONMENT_ART_MODELING_GUIDE.md` into the existing C1/C2/C3 gates:
- **L1 = C1 macro:** large topography, valley, watercourse, waterfall levels, main pool and foreground/background proportions. Freeze macro silhouette only after a genuine clay hero render and image-led review. Do not let attractive surface details hide a wrong L1.
- **L2 = C2 structural:** independent strata, undercuts, bank toes, exposed rock benches, cliff-to-terrain seams and their impact on hero/left/right cameras. Only after real C2 geometry is accepted may P3/P4 introduce L3 vegetation and decorative assets.
- **L3 deferred:** small rock variants, reeds, shrubs, trees, grass and ambient clutter are NOT P1 whitebox acceptance criteria. Avoid early Geometry Nodes scattering in the P1 concept scene.

Consume a **real, approved P0** `blueprint/reference_geometry_contract.json` (not the example). If missing, write a versioned P1 proposed contract and declare P0 handoff incomplete; preserve original source IDs. For each important feature create one dedicated, semantically positioned Blender Empty with `obj["art_id"] == anchor_art_id`, and assign stable `art_id`, `art_owner`, `art_revision` to generated meshes. Keep source-image `must_preserve / may_redesign / do_not_copy` explicit when authoring cliffs and waterfall lips. Do not infer anchor position from an arbitrary mesh center or first ray hit.

**Scoped correction loop:** before a Blender edit write `change_scope`, target art IDs, revision, seed, input sources, dependent features/cameras and expected geometry effect. For mesh replacement reuse `blender/scripts/art_idempotent_geometry.py`: find the same object by ID and replace **only its mesh data**, retaining parent, transform, collection/shot references and previous mesh datablock for recovery. Never globally delete/regenerate the scene, apply global purge, or create `.001` copies. Edits to a single bank must not move the approved waterfall or cameras. Record exact old/new geometry source and rerender only cameras whose dependency is affected; preserve other shots' evidence with revision linkage, not invented new measurements.

**Blender camera preflight:** after making the named cameras and landmark anchors, run
`blender -b blender/source/p1_concept.blend --python blender/scripts/p1_visual_layout_validator.py -- --contract blueprint/reference_geometry_contract.json --out reports/P1_layout_validation.json`.
Optional `--features main_fall_left_rim pool_main` and/or `--shots CAM_HERO_45` scope a correction. This checks anchor projections through `world_to_camera_view` and a conservative first-hit ray **occlusion candidate**. It does NOT examine full silhouettes, texture transparency or visual aesthetics, and it does not render. `SCREEN_POSITION_UNSPECIFIED`, `NOT_RUN`, `POSITION_DEVIATION` and `OCCLUSION_CANDIDATE` must never be called art PASS. Final art gate still needs actual aligned hero/left/right clay renders, before/after evidence and human/image-based assessment.


## Required outputs (relative to canyon-rpg/)
- blender/scripts/build_p1_concept.py (or independently documented reproducible generator) and blender/source/p1_concept.blend.
- blender/renders/p1_concept/hero_45.png, alt_left.png, alt_right.png and top/front/side views (actual Blender captures, not imagined).
- blueprint/p1_art_revision.json with original landmark IDs, P0-to-P1 design-space coordinate changes and rationale; no editing of immutable source annotations.
- reports/P1_concept.md including source hashes, scene collections/scale, exact camera transforms, multi-scale slope analysis, concept-vs-graybox review table and PASS / FAIL / ASSUMED / NOT RUN.

**Gate:** P1_CONCEPT_ART_APPROVED means the shape, water logic, irregularity, silhouette and camera compositions are visually convincing. It does NOT mean walkability. Stop here; do not start collisions, CharacterBody3D, NavMesh, paid 3D generation, final materials, trees, or P1-playable without explicit selection. P2 art-direction/lookdev may proceed directly.
