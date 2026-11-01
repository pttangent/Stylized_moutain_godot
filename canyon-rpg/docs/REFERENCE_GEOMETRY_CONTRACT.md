# Scene-agnostic reference-to-geometry contract v2

The canonical contract records **what the scene must look like**, based on source evidence, approved decisions and per-view constraints. Unlike the older image-only v1 example, v2 can be used with a user brief, drawing, existing mesh, photograph or a combination.

## v2 fields

- `schema_version: 2`, `scene_id`, `revision`
- `reference_sources`: array of `{ref_id, kind, path, status}` source records (paths may be null if source is a user brief); `kind` is data, not a chosen scene type.
- `review_views`: array of `{view_id, camera_object, purpose, approval}`, **may be empty during P0** until a review view exists. Approved camera specifications are not inferred from this list.
- `features`: array of `{feature_id, asset_id, anchor_art_id, stage, evidence, source_refs, shape_rules, dependency_ids, view_checks}` with optional source pixel/2D hints.
- `stage`: `S1_COMPOSITION`, `S2_STRUCTURE`, `S3_DETAIL` — operational layers for any scene, not predetermined geometry families.
- `shape_rules`: `must_preserve`, `may_redesign`, `do_not_copy` with scene-specific text supplied during an actual P0 run.
- `view_checks`: `{view_id, expected_uv_top_left, tolerance_uv, check_occlusion}`. Use `null` for any unapproved location or tolerance; normalized screen coordinates use top-left origin when applicable.
- `evidence`: `OBSERVED`, `APPROVED_DESIGN`, `INFERRED`, `GENERATED_CANDIDATE`, or `UNKNOWN`.
- `dependency_ids` are feature IDs, acyclic and based on actual component relationships.

Only fields with observed or approved data should be populated with concrete values. `reference_geometry_contract.example.json` is a **neutral structural example** and never a live scene contract. Existing v1 contracts remain readable for historical reference by compatibility checks.

## Checks

`python blueprint/validate_reference_geometry_contract.py blueprint/reference_geometry_contract.json --report reports/geometry_contract_validation.json` validates structural consistency. It cannot confirm imagery, physical scale, silhouette, occupancy, runtime behavior, or approvals. With a real Blender scene, `blender/scripts/p1_visual_layout_validator.py` may perform read-only projection of landmark anchors only if matching cameras and anchor objects exist. It is legitimate to have no camera views during early P0; it is **not** legitimate to claim visual acceptance without real captures.

For every edit record `change_scope` with affected `feature_id`/`art_id`, source revision, dependent scene parts, chosen review views and actual before/after evidence. Preserve unrelated geometry/transform/camera data. See `docs/UNIVERSAL_WORKFLOW.md`.
