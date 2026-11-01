# Generic Blender scene-modeling and review discipline

This document describes reusable production behavior, **not a scene type, object list, world scale, **presentation** camera angle or style**. It adapts useful modular/iterative principles from prior visual-production research without reproducing project-specific asset rules. Choose geometry representations and QA based on `scene_profile.json`, source evidence and actual deliverables.

## S1 — Composition and primary spatial forms

Define scene silhouette, scale hierarchy, major masses/voids, visible landmarks, depth and framing. The primary forms differ across scenarios and must be discovered rather than named in a universal prompt. Prioritize the real approved views; source images are optional when the user provides a brief, technical diagram or existing 3D model. Use editable proxies rather than premature detailed construction. **Gate:** real Blender capture(s) from chosen views, compared to explicit source/design intent.

## S2 — Structural geometry and connections

Refine necessary surfaces, joints, boundaries, overhangs, thickness, intersections, attachments, supports and transitions **only where the scene actually needs them**. Choose representation per feature: hard-surface mesh, sculpt, parametric geometry, volume, field, curve, existing assets or hybrid. No one representation is required everywhere. Preserve design scale/unit intent and known visible geometry while documenting inferred hidden portions. **Gate:** real multiview or selected-view review of relevant structural shape and continuity.

## S3 — Detail and dressing

Add repeated props, surface variation, secondary features and decorative density only when requested or needed for visual approval. S3 may be skipped for an art-only graybox. Do not use detail to conceal S1/S2 proportion failures.

## Source-to-geometry contract

Read `docs/REFERENCE_GEOMETRY_CONTRACT.md` and use v2, which accepts non-image source inputs. Each `feature_id` has source references, reliability classification, `shape_rules.must_preserve`, `may_redesign`, `do_not_copy`, dependencies and applicable review views. Unapproved pixel positions remain null; no single **presentation** camera angle or fixed shot count is assumed; CAM_QA_45 is a separate common engineering view. Attach `art_id` to real scene objects and optional semantic anchor objects where point projection is useful.

## Scoped and repeatable modifications

Keep `art_id`, `art_owner`, `art_revision` stable. Record the intended `change_scope` before each edit, including changed objects, generator version/seed, dependent features, affected review views and source evidence. Use `blender/scripts/art_idempotent_geometry.py` for safe local mesh replacement where appropriate; preserve transforms and parent/collection relations. This helper does not by itself make arbitrary operators idempotent or guarantee transaction rollback.

When a feature changes, rebuild only necessary parts and compare actual before/after captures. Never delete and re-create the full scene simply because an independent feature changed. Scene versioning must preserve reproducible source parameters and approved baseline views.

## Instance and procedural strategy: conditional

Use shared meshes, collection instances or Geometry Nodes where repetition materially helps the **discovered scene**. Retain deterministic seeds and placement records; avoid blanket realization and do not infer rendering cost from a source mesh alone. Choose placement constraints from actual feature semantics (spacing/attachment/visibility/region/transform conditions), not prewritten assumptions about environment type. Hero/unique geometry may remain authored and individually editable. Validate export support before committing to a procedural strategy.

## Camera and QA discipline

Review views are selected by the scene brief (source match, composition, technical inspection, turntable, runtime view or others), with recorded projections, transforms and output sizes. Do not default to 45° or orthographic **for final composition**, and do not enforce any scene-specific number of presentation cameras or target renderer. **Do** create the fixed 45° orthographic CAM_QA_45 engineering view (16:9 diagnostic baseline) once actual P1 geometry exists. `p1_visual_layout_validator.py` checks only semantic anchor projection and optional first-hit occlusion **candidates**; it never approves a full silhouette, materials or final render. View-count zero during P0 can be legitimate; it does not constitute visual acceptance. Actual scene visuals must be reviewed from real captures on the approved views.

## Honest acceptance

Separate schema correctness, reproducible build, anchor visibility, shape review, target-renderer output, interactivity and performance. Only required/actually executed tests can PASS; other statuses must distinguish NOT_RUN/NOT_APPLICABLE/BLOCKED/ASSUMED. P1-playable is a separate explicit opt-in branch. Source rights and paid generation authorization must be checked before use.

**Optional scene examples live exclusively in `docs/SCENE_TYPE_EXAMPLES.md`**; they supply illustrations and no default requirements.

## Fixed 45° diagnostic baseline (not a presentation camera)

After S1 primary geometry, build `CAM_QA_45` via `blender/scripts/ensure_qa_45_camera.py`, render a real screenshot and lock camera transform and ortho scale. Reuse it for S2 revisions and object visibility/depth/overlap inspection across all scene types. Only explicitly reframe as a new baseline; add further views for hidden surfaces. See `docs/QA_CAMERA_45_STANDARD.md`.

