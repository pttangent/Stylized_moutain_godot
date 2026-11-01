# P1-concept — Generic Blender 3D art blockout (DEFAULT)

Role: Blender environment/scene modeling artist and procedural geometry engineer. **Build an actual editable 3D scene**, not a static image and not a forced playable map. Derive subject, style, scale, camera and feature families strictly from the approved scene profile and reference-to-geometry contract.

## Preflight
- Read docs/UNIVERSAL_WORKFLOW.md, the actual user references, `scene_profile.json`, approved P0 design and `blueprint/reference_geometry_contract.json`. Examples are optional and cannot supply missing scene content.
- Verify Blender executable, version, project paths, render engine and target delivery format. Record coordinate axes/units and any required export conversion; never assume a particular runtime coordinate system.
- Preserve original source IDs and already-approved objects. Existing scene-specific assets are imported only if explicitly part of this project.
- If the contract is missing, emit a versioned proposed contract and mark P0 handoff incomplete; never silently copy `reference_geometry_contract.example.json` as the approved scene.

## Shape-first build sequence
### S1 — Composition and primary forms
1. Identify scene-wide masses, voids, spatial relationships, silhouette hierarchy, design scale and framing **from current sources**. Model only what is required for the approved primary review views.
2. Choose editable representations feature by feature; avoid assuming one modeling technique for all subjects. Set stable `art_id` and ownership, and create semantic landmark anchor objects only where actual matching landmarks exist.
3. Use simple diagnostic materials when appropriate. Render the selected primary view(s) **with the actual Blender renderer** and check composition, proportions, visibility, feature order, negative space and source agreement before adding detail.

### S2 — Structural shape and connections
4. Refine edge profiles, joints, interfaces, surfaces, supporting geometry, overlaps and thickness as appropriate to the **discovered** scene. Do not introduce nonexistent physical systems or textures because examples mention them.
5. Repair intersecting/isolated/floating geometry and multi-view inconsistencies. Keep reusable parts separately editable; choose actual modules or sculpted forms based on source geometry.
6. Render the approved views and any additional diagnostic views required to resolve hidden geometry, rather than always using a fixed number or camera angle.

### S3 — Deferred or limited detail
7. Detail/decoration is optional at P1 and generally deferred until geometry silhouette and structure have passed. When a small proxy is needed to establish composition, label it a proxy. Do not mask a structural failure with surface dressing.

## Scoped revision and automation
8. Generated objects record `art_id`, `art_owner`, `art_revision`. Before editing specify `change_scope`, affected IDs, upstream constraints, dependent features/views, seed and expected change. Prefer `blender/scripts/art_idempotent_geometry.py` for safe mesh-data replacement rather than scene-wide recreation. Do not overwrite unrelated objects or cameras.
9. If a v2 reference contract and actual matching scene cameras/anchors exist, use `blender/scripts/p1_visual_layout_validator.py` for **diagnostic screen projection**, optionally limited to selected features/views. A missing camera, an unset screen position or a projection pass is not a visual/art pass.
10. Record before/after actual renders and issue lists with shot/view ID, feature ID, visible discrepancy, severity, rationale and observed changes. Confirm the same underlying geometry is used for all approved views.

## Deliverables and acceptance
Provide reproducible modeling script(s) if used, editable `.blend` source, selected real review renders, semantic geometry/asset hierarchy, versioned design changes, and reports/P1_concept.md (tools, measurements, artifact paths, PASS/FAIL/ASSUMED/NOT_RUN). The `P1_CONCEPT_ART_APPROVED` gate covers visual/spatial criteria only, not interaction, collision or runtime performance. Stop before unrelated detailed asset work; next is P2 or explicitly selected P1-playable.
