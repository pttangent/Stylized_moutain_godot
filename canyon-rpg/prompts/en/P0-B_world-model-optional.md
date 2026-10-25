# P0-B — Validated Engine-Ready Spatial Blueprint (Optional Generated World Reference)

You are a procedural level-design and spatial validation engineer for Godot/Blender. This is a **GENERAL REUSABLE WORKFLOW**, not an instruction to reuse a canyon image or a previously generated map. A generated World Labs, image-blaster or equivalent scene is an OPTIONAL input, never an automatic source of metric truth.

## Resolved input/output profile for this repository

Resolve `project_root=canyon-rpg/` from the Git repository root. This profile supplies paths for the **current** project; replace it when using the reusable procedure on another scene. The existing files are inputs for an update, not permission to overwrite reviewed evidence.

| Role | Current path relative to `project_root` |
| --- | --- |
| Reference image and world manifest | `assets/worlds/canyon-waterfall/canyon-waterfall-reference.jpeg`, `assets/worlds/canyon-waterfall/manifest.json` |
| Existing Marble GLB and SPZ | `assets/worlds/canyon-waterfall/canyon-waterfall-collider.glb`, `assets/worlds/canyon-waterfall/canyon-waterfall-{100k,150k,500k,full-res}.spz` |
| Source annotations and registered candidate | `analysis/p0_marble_2026-10-26/annotations/paired_landmarks_user_reviewed.json`, `analysis/p0_marble_2026-10-26/blueprint/scene_blueprint_registered_candidate.json` |
| Source perspective camera and raw evidence | `analysis/p0_marble_2026-10-26/registration/`, `analysis/p0_marble_2026-10-26/registered_spatial_measurements.json` |
| Active design blueprint and generator | `blueprint/scene_blueprint.json`, `blueprint/build_p0_design.py` |
| Active heightmap and design semantic mask | `blueprint/heightmap_16bit.png`, `blueprint/semantic_mask_design.png` |
| Current source-image overlay and metric height views | `blueprint/layout_reference_overlay.png`, `blueprint/terrain_three_views.png`, `blueprint/terrain_orthographic_views.png`; generation script `blueprint/render_p0_review_views.py`, residuals `blueprint/review_views_metadata.json` |
| Active water, navigation, cliffs and game camera | `blueprint/water_graph.json`, `blueprint/navigation_graph.json`, `blueprint/cliff_edges.json`, `blueprint/camera.json` |
| Active report and numeric validation | `reports/P0_report.md`, `reports/P0_design_validation.json`, `blueprint/validate_p0_design.py` |

Use `world_model.mode=auto` unless explicitly overridden. Current P0-B is an **authored game-design blueprint**, numerically checked 17/17, using a 6 m bridge design span (27.71343 m per raw unit), Godot Y-up, a 96×120 m layout and a 1.75 m character. This is not a surveyed Marble scale or a passed Godot traversal test. Preserve the existing blueprint and its source annotations when integrating new evidence; update it only with an explicit versioned design decision. Do not request a new World Labs generation.

## Primary requirement

Convert the CURRENT P0-A spatial evidence and approved interpretations into deterministic, engine-parseable geometry/topology specifications. Preserve approved IDs, topology, scale, original image pixel coordinates and explicit uncertainty.

## Required transcript

Fetch/read the complete Can It Code? Cyberpunk City tutorial transcript if not locally present:
https://github.com/pttangent/Stylized_moutain_godot/blob/main/canyon-rpg/reference/canitcode/transcripts/XqtnBlPJ6KE_is-this-really-ai-insane-opus-5-5-gamedev-workflow.md
Use overhead grid layout, player-scale blockout and connection tests as design principles, not as proof of this world's precise geometry.

## Input contract

1. Active project root and original source images; inspect git status before file changes.
2. The existing `analysis/p0_marble_2026-10-26/blueprint/scene_blueprint_registered_candidate.json`, reviewed landmark file, camera evidence and current `blueprint/scene_blueprint.json`; use a new dated analysis directory for any changed P0-A proposal.
3. `world_model.mode: auto | none | required` (default `auto`) and optional actual GLB + SPZ + manifest.
4. When using a model: the P0-A collider surface evidence bundle (raw candidates, optional design-scale comparison, metadata and generator), candidate `raw_to_godot_transform`, `meters_per_raw_unit` status, `source_camera_fit`, paired 2D↔3D landmark observations, and reviewed masks identifying ground, rivers, bridges, stairs, cliffs and sky/vegetation exclusions.
5. When not using a model: explicitly approved image-only authored plan and its uncertainty, rather than raw-model assumptions.

## B-0 — Preflight gates

- Validate current input hashes, file identity and provenance; reject stale world ID or untracked replacement sources.
- When `world_model.mode` is `auto` or `required` and a GLB is supplied, locate and validate the P0-A `world_model_evidence/manifest.json`. Confirm that its GLB hash matches the input, its generator is present, raw-unit maps remain separate from any author-scaled map, and the raster metadata declares transform, units, NoData/coverage and candidate-surface limitations. If missing or stale, create a replacement diagnostic bundle in the current dated analysis run before promoting any P0-B geometry. Do not silently treat the P0 heightmap or design mask as a substitute.
- Validate candidate camera registration (if world model used): at least 8 noncoplanar anchors, record per-landmark reprojection residual; target median error <= approximately 2.5% reference width or a stricter project threshold, plus human review of the projected geometry. The numeric threshold is a screening rule, not a guarantee of 3D correctness.
- Explicitly select world vertical and forward directions, handedness, physical scale reference, origin and signed raw→engine transform. Never infer that `glTF Y-up` means every generated scene surface is valid terrain or that its coordinates are metrically correct.
- Check all high-salience landmarks, waterfall levels, road crossings, bridge endpoints and occluded gaps for conflicting image/model evidence.
- If critical gates cannot be satisfied, output actual **diagnostic candidates** with `P0B_BLOCKED.md`; DO NOT pretend that the final requested files are validated.

## B-1 — Terrain reconstruction

1. Segment **true ground** from canopy, sky/background, water/transparent surface, props, cliffs and bridges using a reviewed semantic surface mask. A normal threshold alone does not identify walkable terrain.
2. Create terrain elevation zones/terraces and a top-down plan in ONE approved metric coordinate frame. Record all transforms in JSON, never silently flip axes to make a preview look attractive.
3. Rasterize an actual single-channel 16-bit heightmap with declared image size, min/max physical elevation mapping, bounds and coordinate convention. For a **measured** terrain heightmap, keep unobserved cells in a separate NoData/validity mask. This repository's existing `blueprint/heightmap_16bit.png` is an **authored bulk-terrain design** across the chosen world bounds; `blueprint/semantic_mask_design.png` labels intended land uses and must not be presented as a measured GLB ground-validity mask.
4. Represent vertical cliffs, undercuts and overhangs separately in `cliff_edges.json` with source face identifiers and uncertainty. Do not force multi-valued vertical geometry into a heightfield.
5. Preserve image/model disagreements as review records; do not overwrite original evidence.

## B-2 — Water and navigation topology

1. Export directed `water_graph.json` with unique nodes/edges, reaches, waterfalls, confluences, pools and exits; waterfall edges must have **positive metric height drops**. Reject nonphysical reversals and label uncertain hidden reaches.
2. Export `navigation_graph.json` with terraces, stairs, bridges, paths and blocked edges. Check endpoints land on semantically walkable surfaces and that the planned main route is connected.
3. Evaluate test-agent assumptions (provisional 1.6 m player) including path width, stair rise/run, slope, gaps, collision height and bridge endpoint continuity. P0 graph continuity != in-engine traversability; distinguish them.
4. Do not use the Gaussian splat as a NavMesh; use reviewed collider/terrain geometry plus explicit semantics. Any `SPZ` is a visual inspection asset, not physical collision proof.

## B-3 — Camera and reference alignment

1. Export `camera.json` for a Godot orthographic 16:9 RPG camera pitched ≈45° downward, no visible horizon; set target, yaw, near/far and ortho size in the common metric frame.
2. Keep original/source perspective camera calibration separately under `registration/`; never substitute it for the Godot camera.
3. Generate source projection overlay and a proposed camera-view screenshot. Measure reference landmark order, 2D displacements, framing/clipping, water bend direction and bridge/stair placement.

## B-4 — Mandatory files

- `blueprint/scene_blueprint.json` — approved schema v2+ with source evidence references, world transform, metric bounds, terrace table, landmark xyz and provenance.
- `blueprint/layout_topdown.png` — TRUE top-down coordinate visualization, compass/axes, scale bar, elevations, water, bridge, stairs, cliffs, labels and uncertain portions.
- `blueprint/heightmap_16bit.png` + an explicit coverage/NoData mask if deriving measured terrain from incomplete geometry. The current authored design instead has `blueprint/semantic_mask_design.png`; document its different meaning and add a validity mask before claiming measured terrain coverage.
- `blueprint/cliff_edges.json`
- `blueprint/water_graph.json`
- `blueprint/navigation_graph.json`
- `blueprint/camera.json`
- A linked, reproducible collider surface evidence bundle when a world model is present: manifest, generator, raw-axis candidate projections, min/max candidate elevation maps, NoData/coverage data, and optional separately labeled author-scaled comparison. These are evidence-only layers, not the active terrain heightmap or a walkability mask.
- `reports/P0_report.md` (or a versioned successor) — every executed command, observed PASS/FAIL/BLOCKED outcomes, image/render comparisons, source hash and unresolved assumptions.
- Source-generation scripts and JSON validators; mutation tests and local Blender/Godot import evidence when actually run. The current machine-readable numeric design check is `reports/P0_design_validation.json`. Do not relabel unrun runtime or mutation tests as PASS.

## B-5 — Assertion and mutation requirements

- Verify every JSON schema and all cross-file references/IDs, bounds and transform matrix handedness.
- Verify source image and optional model hashes, high-salience landmark coverage, camera reprojection and pixel↔3D correspondence status.
- Verify the collider evidence manifest's GLB hash, transform-once rule, axis hypotheses, units, normal-filter semantics, NoData coverage and consistency between metadata and raster dimensions. Reject a map that labels unsigned-normal candidates or unclassified top surfaces as confirmed walkable ground.
- Verify PNG single-channel uint16, exact dimensions and documented value→height conversion; missing coverage MUST remain NoData.
- Verify waterfall positive height drop, no impossible water direction or unmarked hydrological cycles, connected main navigation graph, no bridge endpoint gaps, valid slopes and stair rise where geometry is available.
- Create deliberate negative tests that fail upon changing axis sign, invalid graph IDs, reversed waterfall elevations, 8-bit image, out-of-bounds anchors, disconnected bridge route, camera misregistration and deleted approved landmarks.
- Generate an actual preview/visual diff, never fictional screenshots or inferred PASS counts.

## Deliverable gate

Produce approved final files **only if their prerequisites were observed and verified**. If world model is absent, image-only P0-B remains possible given an explicitly approved designer map. If a world model is present but is corrupted, misregistered, incompatible or semantically ambiguous, report why and continue in explicit image-only/manual mode only when authorized. Don't build detailed 3D meshes or claim that playable traversal was tested in Godot unless it actually was.
