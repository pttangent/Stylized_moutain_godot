# P0-B — Optional Model-Guided Art Blueprint (GENERAL)

Read P0-B.md first. Only use this extension if an actual user-supplied small generated 3D reference was inspected under P0-A_world-model-optional.md. Use the primary image as the authoritative visible art target; the mesh is a **low-confidence spatial clue**.

## Evidence gate
Confirm hash and raw coordinate axes, transformation once, source registration quality, valid/NoData coverage, normals and clear candidate-surface labels. No copied background, canopy, water or cliff geometry may be reclassified as surveyed/walkable ground by default. Without trustworthy input, record MODEL_EVIDENCE_UNAVAILABLE and do image-led P0-B; never fabricate or silently load a historical model.

## Art-blueprint integration
- Preserve **three distinct layers**: raw/generated evidence, authored bulk-design heightfield, and separate authored cliffs/overhangs/waterfall/bridge structures.
- Keep image landmarks and user-reviewed observations immutable. If authoring changes water levels, riverbank geometry or terrace positions, produce dated design revisions and a diff with reasons.
- Confirm top-down axes, authored scale and landform zones; check water flow and stepped waterfall pools. Separate source perspective camera from hero fixed ~45-degree 16:9 camera and two side views.
- Run multi-scale slope QA on the **authored** terrain heightfield. A cliff and waterfall edge may be extremely steep; path-grade advisory only applies to explicitly optional walking geometry. The model does not prove geological realism.
- Create actual camera/section overlays, mention silhouette or reprojection disagreements, and validate uint16 raster, shared IDs and sample coverage without claiming unrun playability.

## Outputs
Model-evidence manifest, discrepancy register, versioned scene blueprint revisions, diagnostic overlay and reports/P0B_art_model_review.md; classify PASS/FAIL/ASSUMED/NOT RUN. Advance on **art acceptance**, not a navmesh or walking gate.
