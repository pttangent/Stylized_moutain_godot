# Blender environment-art modeling techniques — scoped adaptation

These rules adapt **workflow ideas**, not copied implementation, from the user-supplied `tygg-ai-film-studio v3.2.7` archive: `references/scene-blockout-and-camera-motion.md`, `reference-image-driven-assets.md`, `blender-mcp-execution.md`, `hyper3d-scene-assets.md`, `performance-budget.md`, `asset-library.md` and `scripts/validate_previs_fast.py`. The original material addresses film previs, so character animation, proprietary model tiers and path-collision defaults are deliberately **not** transplanted to this environment-art project.

## Default handoff

**P0-A -> P0-B -> P1-concept (Blender) -> P2 lookdev -> P3 kit -> P4 assembly -> P5 QA.** P1-playable remains an optional later overlay. The source image is authoritative for visible silhouettes and landmark ordering. An actually provided small Tripo model is nonmetric low-confidence reference only. Older P0 geometry is a design candidate; preserve annotations and version any proposed changes. No global 18-degree slope rule: only an expressly playable path may adopt path-grade targets.

### Level L1 — Macro landform

Make the valley, asymmetric massing, upper terraces, waterfall tiers/lips, main receiving pool and lower outlet. Use a heightfield only for bulk terrain. Keep steep cliff meshes, waterfall faces, cave/undercut and river water separate. Reject uniform ramps, perfectly parallel riverbanks and narrow artificial trenches. Before advancing, make a real Blender clay render from CAM_HERO_45 and check landmark order, skyline, occlusion and water elevation continuity.

### Level L2 — Structural landform

Design strata-aware cliff faces, alcoves, benches, scarps, overhang undersides, shoreline erosion, valley-to-rock contacts and large boulders. Meshes have independently editable `art_id`s and stable seams. Re-render CAM_HERO_45, CAM_ALT_LEFT and CAM_ALT_RIGHT; repair intersecting bank/fall geometry and inconsistent proportions. Artistic roughness must reflect a geological cause, not uncorrelated noise. Do not hide failed L1/L2 shape with vegetation.

### Level L3 — Environment dressing (P3/P4, NOT early P1)

Place reusable rock/plant/branch families by terrain class, local slope, elevation, moisture and water distance. Prefer shared mesh data, Collection Instances or `Distribute Points on Faces -> Instance on Points` with deterministic seeds. Keep hero landmark trees separately editable. Default **no global Realize Instances**; only make small copies real when genuinely needed. Evaluate foreground silhouette and instance density against three approved cameras. Instances save duplication but do not eliminate expanded draw/geometry work.

## Reference-to-geometry contract

**Canonical example:** `blueprint/reference_geometry_contract.example.json` (template, not approved truth). **Structural validator:** `blueprint/validate_reference_geometry_contract.py`. For each stable `feature_id`, store:

- Source image ID, observed pixel coordinate, evidence class `OBSERVED / DESIGNED / INFERRED / UNKNOWN`, and authored (not surveyed) scale basis.
- Target reusable `asset_id` and exact Blender **anchor object's `art_id`**, e.g. `ANCHOR_MAIN_FALL_LEFT_RIM`. Do not silently infer anchors from nearest ray hit or mesh midpoint.
- `reference_shape.must_preserve` (silhouette, relative scale, lip/pool order), `may_redesign` (unknown backsides, local strata), and `do_not_copy` (image perspective as map, fake model ground, texture noise as geometry).
- L1/L2/L3 classification, `dependency_ids`, and shot checks tied to existing camera IDs.
- `expected_uv_top_left` is normalized image-screen coordinates with **top-left origin**, and must remain `null` until a reviewer authorizes a target from a matched render. Record `tolerance_uv` only after a target exists. Example camera names and target shot positions are **proposed**, not approved.

P0-A authors visual observations and inferred geometry as separate evidence. P0-B materializes contract candidates and validates reference/ID/dependency consistency. P1 creates landmark anchor Empty objects with matching `obj["art_id"]`, positions them at the visually relevant **surface point**, and iterates camera/mass checks. Avoid forcing a single feature's source image pixel into an alleged measured XYZ.

## Reentrant scoped Blender edits

Each modeled mesh carries `obj["art_id"]`, `obj["art_owner"]`, `obj["art_revision"]`; never rely on `Cliff.001` names or delete everything and regenerate. Use `blender/scripts/art_idempotent_geometry.py` to identify the exact object and swap only its **mesh data**, retaining its world transform, parent, collection links, custom ID and other unrelated objects. The helper checks ownership and optionally the previous revision, refuses duplicate IDs, and retains previous mesh datablocks for recovery. Callers must save a new `.blend` revision and document old/new geometry source. It is not an automatic rollback transaction.

Before editing record `change_scope` (list of art_ids), inputs, seed, object ownership and affected cameras/features. Preserve approved P0 pixels, water network and locked cameras. Changing a landform reruns relevant shape and waterfall-camera checks; editing only a camera reruns its camera checks, not untouched geometry generation. If an art change requires altering approved geometry, log it in `blueprint/p1_art_revision.json`. Do not globally purge, apply costly modifiers, or overwrite unrelated asset sources. Ensure 3D model views are the SAME scene, never separately regenerated per camera.

## Validation and honest gates

1. **Structure only (no Blender):** `python blueprint/validate_reference_geometry_contract.py blueprint/reference_geometry_contract.example.json --report reports/reference_geometry_contract_example_validation.json`.
2. **Actual Blender anchor screen check (read-only):** `blender -b blender/source/p1_concept.blend --python blender/scripts/p1_visual_layout_validator.py -- --contract blueprint/reference_geometry_contract.json --out reports/P1_layout_validation.json`. Pass `--features <feature_id> ...` and/or `--shots CAM_HERO_45 ...` for scoped edits. The example contract alone does not imply matching Blender objects exist.
3. The validator projects each anchor with Blender `world_to_camera_view` and optionally reports a first-ray **occlusion candidate**. This is NOT a mesh-silhouette metric, opacity test, render, visual review, or playable collision check. An empty/unknown screen target is **SCREEN_POSITION_UNSPECIFIED**, not POSITION_PASS. Absent cameras or anchors are NOT_RUN, not auto-created.
4. **Art approval requires real renders:** compare original/reference against hero, left and right clay images with fixed camera parameters, object-level silhouette, water/pool proportions, depth and visible artifacts; keep annotated before/after and explicit PASS/FAIL/ASSUMED/NOT RUN. Do not approve from JSON validator output.
5. When model/instance density becomes meaningful at P3/P4, measure actual source mesh counts, evaluated instance estimates and target Godot performance separately. A single source mesh's polygon count never measures all repeated visible instances. Don't invent FPS.

## Anti-patterns

- Merging the whole canyon into one uneditable mesh or flattening cliffs to satisfy an optional walking graph.
- Treating a small generated mesh's top face or first image ray hit as certified ground.
- Building finely detailed stone/foliage before the macro terrain and waterfall geometry look correct.
- Duplicating the entire scene on a one-cliff change; unstable auto-increment object names; unapproved global Realize Instances.
- Claiming a screenshot was rendered because projection coordinates, file existence or Python syntax passed.

**Source/implementation distinction:** only the workflow concepts above came from the archive; the schema, example, validators and helper scripts in this repository are project-specific adaptations.
