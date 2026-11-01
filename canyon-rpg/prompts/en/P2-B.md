# P2-B — Representative lookdev slice with visual evidence

Role: Blender artist and renderer/technical-lookdev developer. Work from an **approved P1-concept** and P2-A style system. There is no assumption about scene category, focus object, lighting, camera, material, external model service or runtime engine.

1. Choose a **small but representative** scene slice that exercises the highest visual risks or most frequently repeated elements. Record selection and why it is representative; no mandated object types or sample count.
2. Preserve approved feature IDs, macro/structural shape, placement and original chosen review-view transforms. If geometry must change, record a scoped revision and rerender dependent views.
3. Compare feasible authoring methods with the same source, preview view and output conditions; select a method based on editability, silhouette fidelity, texture/render quality, effort and target constraints. Paid generation requires separate authorization.
4. Produce the minimum needed material, geometry, lighting and effect prototypes, aligned with the approved style bible; omit irrelevant systems.
5. Render in the **actual target renderer** when a target was specified. Blender renders are valid for Blender-only art approval; when a real-time engine is requested, separately capture real runtime screenshots and validate material conversion.
6. Compare actual captures with source evidence/style bible at the approved shot IDs; log per-feature defects and revise only affected material/geometry systems. Preserve versioned before/after artifacts.
7. Check relevant hidden surfaces, UVs, shading, clipping, source/instancing choices, and any scene-dependent export or runtime limitations.
8. Report observed execution environment, commands, real outputs, limits and PASS/FAIL/ASSUMED/NOT_RUN. No claimed render or benchmark without a real run.

Deliver a reproducible lookdev slice, editable source, required materials/effects, actual comparison renders, change log, and reports/P2B_visual_slice.md. Do not require playability unless explicitly selected.
