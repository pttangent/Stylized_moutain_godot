# P3-B — Build reusable and unique assets with scoped edits

Role: Blender procedural/handcrafted asset producer. Consume the approved P3-A inventory, P2 lookdev, geometry contract and source file revisions.

1. Create only the required assets, choosing modeling techniques per shape. Keep stable `asset_id`, `art_id`, `art_owner`, `art_revision`, native editable sources and documented export transforms.
2. Validate each representative item in isolation and in realistic scene context. Check critical silhouettes and connections before bulk producing variations. Preserve source observations; uncertain geometry remains an authored decision.
3. For repeated forms prefer shared mesh data, collection instances or procedural instances with deterministic seed/placement manifests when beneficial. Do **not** indiscriminately realize instances, replace every instance with a unique mesh or assume instancing eliminates rendering cost.
4. Differentiate source-mesh triangles from evaluated/expanded instance geometry and actually measured runtime cost. Budgets and LOD are set by target views/platform, not universally fixed numbers.
5. Expose useful parameters, pivot and connector rules only where applicable. Handle normals, smoothing, UV/materials, resolution and export/import correctness according to the selected renderer.
6. Use user-supplied generated meshes as editable starting candidates only after geometry, scale, source/licensing and quality inspection. No external provider/credit consumption without permission.
7. Prefer `blender/scripts/art_idempotent_geometry.py` for local changes. Keep unrelated approved scene objects and review shots stable; log any geometry contract deviation with before/after evidence.
8. If P1-playable was explicitly selected, add real collision/interaction requirements to asset tests; otherwise mark those cases `NOT_APPLICABLE`.

Deliver versioned sources, generators where useful, output assets, manifests, real preview/gallery renders, evaluated instance measurements where possible, validation logs and reports/P3B_asset_kit.md.
