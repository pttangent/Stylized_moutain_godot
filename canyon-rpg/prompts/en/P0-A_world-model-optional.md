# P0-A — Evidence-Led Image → World Spatial Reconstruction (Optional World Model)

You are a senior 3D RPG level architect, geometry-forensics engineer and game-world cartographer. This is a **GENERAL WORKFLOW**. Never hard-code the canyon scene, a specific landmark count, a project name, previous blueprint coordinates, or assumptions that all input images represent waterfalls. The canyon is only one test case.

## Resolved input profile for this repository

Resolve paths from the Git repository root, then set `project_root=canyon-rpg/`. These are the **current project's defaults**, not universal assumptions. For a different scene, discover and replace them before running the general workflow below.

| Role | Current path relative to `project_root` |
| --- | --- |
| Reference image | `assets/worlds/canyon-waterfall/canyon-waterfall-reference.jpeg` |
| Marble 1.1 manifest | `assets/worlds/canyon-waterfall/manifest.json` |
| Collider | `assets/worlds/canyon-waterfall/canyon-waterfall-collider.glb` |
| SPZ visual layer | `assets/worlds/canyon-waterfall/canyon-waterfall-{100k,150k,500k,full-res}.spz` |
| Local image/SPZ/GLB annotator | `../tools/marble-world-annotator/` (serve from the repository root) |
| Immutable annotation export | `analysis/p0_marble_2026-10-26/annotations/paired_landmarks_raw.json` |
| User-reviewed pair copy | `analysis/p0_marble_2026-10-26/annotations/paired_landmarks_user_reviewed.json` |
| Source perspective camera candidate | `analysis/p0_marble_2026-10-26/registration/camera_registration_candidate.json` |
| Existing registered P0-A candidate and report | `analysis/p0_marble_2026-10-26/blueprint/scene_blueprint_registered_candidate.json`, `analysis/p0_marble_2026-10-26/P0_SPATIAL_REVIEW.md` |
| Current P0-B **design** blueprint | `blueprint/scene_blueprint.json` and `reports/P0_report.md` |

Use `world_model.mode=auto` unless the task specifies `none` or `required`. The current GLB and SPZ are already generated: do not call the World Labs API or regenerate them. The current selected game-design scale is recorded in `blueprint/scene_blueprint.json` (6 m bridge span, 27.71343 m per raw unit); it is **not** a surveyed Marble unit conversion. Do not overwrite `blueprint/scene_blueprint.json` during a P0-A rerun. Place new diagnostics under a new dated `analysis/` directory and preserve the 2026-10-26 evidence and landmark IDs.

## Primary objective

Convert one or more reference images into an **auditable 3D spatial hypothesis** suitable for eventual Godot/Blender level blockout. Distinguish IMAGE evidence, generated MODEL evidence, designer CONSTRAINTS, and UNRESOLVED uncertainty. An image is not an orthographic survey; a generated 3D model is not verified real-world geometry.

## Required technical reference

Read the complete timestamped Can It Code? Cyberpunk City transcript before adopting any author technique (download if absent):
https://github.com/pttangent/Stylized_moutain_godot/blob/main/canyon-rpg/reference/canitcode/transcripts/XqtnBlPJ6KE_is-this-really-ai-insane-opus-5-5-gamedev-workflow.md
Focus on **00:01:28–00:01:48** overhead planning → simple block grid → player-scale visual review; **00:04:40–00:05:05** connection stress tests and agent walking through stairs/bridges; **00:05:51–00:06:23** physical dimensions and multi-view quality assurance. Attribute these to the author rather than pretending their pipeline generates metric truth from a photo.

## Inputs to discover before work

- `active_project_directory`: inspect actual workspace/git status, do not assume a checkout or overwrite an approved blueprint.
- `reference_images[]`: original images with dimensions, hashes and filenames. This scene's meaning comes from THESE inputs only.
- `prior_approved_annotations` (optional): approved landmark IDs, links, topology; preserve IDs and approvals.
- `world_model.mode`: `auto | none | required`; default `auto`. `auto` uses a supplied, inspectable generated scene if present; `none` requires image-only workflow; `required` fails clearly if absent.
- `world_model.manifest_path` (optional): World Labs Marble / image-blaster manifest, or an equivalent asset declaration.
- `world_model.collider_glb` (optional), `world_model.gaussian_spz[]` (optional; choose 100k/150k initially, 500k/full only as needed), `world_model.camera_metadata` (optional).
- `provisional_character_height_m`: 1.6 for a new project unless user overrides. For this repository, the authored design uses a 1.75 m character and a 96×120 m world; do not silently replace those current design decisions with generic starting values.

## P0-A-0 — Source integrity and data provenance

1. Inspect the actual image, available world-model files, manifest and metadata. Verify SHA-256, binary formats and file sizes. Record source model, ID, revision and transform assumptions.
2. Read source transcript; record specific operational ideas versus our proposed extensions.
3. NEVER infer a location, a heightmap, a NavMesh or a game-ready terrain from a filename or successful API request.

## P0-A-1 — 2D semantic survey (always run)

1. Draw image overlays with stable IDs and pixel coordinates `(u,v)` (origin top-left), normalized coordinates and bounding boxes/polygons where possible.
2. Detect categories relevant to THIS scene: terrain/terrace, cliff, walkway, steps, bridge, rivers/flow, waterfalls/pools, props, vegetation, occluders, entrances/exits and major visual anchors. Skip absent classes rather than hallucinating them.
3. Optional SAM2 / Grounding DINO / Florence-2 / manual click annotation may accelerate segmentation, but distinguish model-proposed masks from visually approved boundaries.
4. Mark every observation as `visible`, `partly_occluded`, `inferred`, or `unknown`. Preserve stable IDs in later artifacts.

## P0-A-2 — World-model evidence branch (only if supplied)

1. Inspect GLB scene graph, local transforms, vertices, faces, bounding boxes, disconnected fragments, normals, material channels, mesh degeneracy and suspicious sky/dome/background geometry.
2. Parse SPZ metadata with the correct format version. Do not assume Gaussian centers are traversable surfaces, and do not include long-distance splat/background outliers in terrain bounds.
3. Test whether SPZ and collider occupy matching **RAW coordinate spaces** through measured spatial nearest-neighbor statistics; do not blindly transpose axes. The GLB renderer's up-axis and actual terrain vertical are separate questions. Avoid assuming raw length units equal metric meters.
4. Generate diagnostic top/front/side projections and **multiple axis hypotheses** with explicit masks and height units. Label all such rasters `UNAPPROVED_RAW_SURFACE_CANDIDATE`, not a Godot terrain heightmap.
5. Record what the world model added: possible depth layers, relative geometry, occlusion candidates and candidate 3D anchors; also record violations of original reference and imagined geometry.

## P0-A-3 — Image ↔ world registration

1. Obtain at least 8 independent, spatially distributed image-pixel ↔ collider-point **actual human/agent visually verified** correspondences, including terrain at different elevations and landmarks with unambiguous 3D surfaces. No invented or heuristic-only XYZ values are allowed as confirmed pairs.
   - OPTIONAL automation bootstrap: render many candidate viewpoints from the splat/GLB with camera parameters + hit/depth IDs, then use image keypoint/feature matching (e.g. SuperPoint/LightGlue or LoFTR) to propose source↔render correspondences. Visually confirm them and reject appearance/model mismatches before counting them as approved pairs. If this rendering or matching is not available, use the included manual 2D↔3D picker. No unverified auto-match receives “confirmed” status.
2. Use the repository's `../tools/marble-world-annotator/` from `project_root` (or an equivalent local 3D picker) and export paired JSON (`pixel_xy`, `mesh_xyz_raw`, object/face index, semantic label, uncertainty). Keep source/target coordinate spaces explicit. In this repository, preserve the existing raw export and the separate user-reviewed copy listed above.
3. Fit a candidate source-perspective camera with PnP/RANSAC and intrinsics search (or use trusted provider camera metadata if independently verified). Render reprojections and report residual error per landmark. Solve camera separately from the eventual Godot orthographic RPG camera. If a view cannot match, classify MODEL-IMAGE MISMATCH instead of forcing arbitrary nonrigid warping.
4. Cast rays from registered image pixels against GLB, retaining MULTIPLE ordered collision candidates where possible. Sky, vegetation, thin shell, water and bridge can overlap in one pixel: a ray hit is not automatically terrain.
5. Choose a right-handed raw→Godot coordinate transform using reviewed up/forward axis vectors and a reproducible metric scale calibration. A 1.6 m character is provisional; use a known physical landmark/bridge width, verified player comparison, or metric annotations. Keep `meters_per_raw_unit=null` until justified.

## P0-A-4 — Spatial model / physical consistency

1. Derive walkable terraces, cliffs and overhangs as separate semantic layers; terrain masks exclude foliage, sky and visually thin non-ground surfaces. Do not use the top-most intersection of every ray as ground.
2. Map 3D landmarks into common metric coordinates only after transform/scale approval. Fit *top-down* layout from the **approved 3D geometry**, not a perspective warp of the source image.
3. Construct a **directed Water Graph**: sources/reaches/pools/vertical drops/exits. Validate each proposed fall has upstream elevation greater than downstream; preserve occluded or visually inconsistent branches as `unresolved`.
4. Construct a **Navigation Graph**: valid platforms, steps, bridges, paths, water barriers, cliffs, main and side exploration routes. Verify node reachability by graph logic; defer claims of physical agent traversal until geometry/collision checks.
5. Define source camera calibration separately from a proposed **Godot orthographic 16:9 camera, ≈45° downward pitch**, no horizon. Compare landmark projection order and 16:9 framing rather than assuming the source camera is exactly 45°.
6. Compare source image, collider candidate surfaces and spatial rules; record conflicts and decisions in a traceable uncertainty register. Image/model/rules are THREE DIFFERENT sources of evidence; assign a per-landmark confidence class.

## P0-A outputs

- In a new dated `analysis/` directory, a `blueprint/scene_blueprint_draft.json` with image points, optional measured raw world coordinates, ID continuity, coordinate definitions, provisional sizes and P0-A gates. The existing registered candidate is at `analysis/p0_marble_2026-10-26/blueprint/scene_blueprint_registered_candidate.json`.
- In that analysis directory, `blueprint/water_graph_proposed.json` and `blueprint/navigation_graph_proposed.json` with statuses and uncertainty; do not overwrite the active `blueprint/water_graph.json` or `blueprint/navigation_graph.json` during analysis.
- Image landmark overlay, raw axis projections and paired-geometry review if a model is supplied. The current source-camera reprojection image is `analysis/p0_marble_2026-10-26/registration/camera_reprojection_review.jpg`.
- World evidence, source-camera candidate, P0-A spatial analysis and an explicit unknown/assumption register. The current evidence lives under `analysis/p0_marble_2026-10-26/`; `reports/P0_report.md` records the separate authored P0-B design.
- A clear `APPROVED | DRAFT | BLOCKED` stage state. If optional world model is absent, execute the image-only branch with UNKNOWN XYZ and do not fabricate the extra data.

## Stop conditions

Do not build a detailed 3D level. Do not label a world-model collider as a clean heightmap, a traversable mesh or an accurate metric survey without ground/axis/camera validation. If source camera, terrain classification or metric scale is unresolved, deliver honest P0-A diagnostics, runnable review scripts and specific next approval actions rather than fictional P0-B pass results.
