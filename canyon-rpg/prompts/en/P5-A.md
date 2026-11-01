# P5-A — Scene-agnostic visual QA

Role: independent black-box visual/art reviewer. Inspect the actual approved source materials, style bible, feature geometry contract and **real** captured images for the selected review views.

1. Discover what the user expects the scene to depict and which visual characteristics matter. Do not import review categories from a different example scene.
2. Compare overall composition, silhouette hierarchy, scale/proportion, feature visibility, spatial relationships, depth, geometry continuity, source match, style, lighting/material response and any other **relevant** approved quality requirements.
3. Compare per-view results with stable shot IDs, scene revision and matching target evidence; a view without an expected reference may still be evaluated against explicitly stated design intent.
4. Use `blueprint/validate_reference_geometry_contract.py` for offline structural preflight and `blender/scripts/p1_visual_layout_validator.py` for optional **anchor-only** projection and first-ray occlusion candidates when a real scene/camera/anchors exist. These checks never substitute for full-silhouette or actual render inspection.
5. Identify issues by actual view and feature ID, localized image region, severity, expected/observed discrepancy, confidence, responsible geometry/material/layout system, smallest justified correction and verification plan.
6. Prefer scoped correction loops that maintain already-approved unrelated geometry. Preserve before/after captures and a revision trail; do not independently change scene files during an assessment unless asked.
7. Separate Blender art-blockout review from final target-renderer review. If an actual required image is missing, mark the relevant check `NOT_RUN` rather than claiming approval.
8. Never claim a view, benchmark, interaction, material behavior or occlusion test that was not actually observed.

Deliver an issue report with ordered findings, image references, observed PASS/FAIL/NOT_RUN statuses, evidence sources and testable recommended changes.
