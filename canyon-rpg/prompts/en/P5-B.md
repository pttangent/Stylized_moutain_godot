# P5-B — Godot Integration and Performance QA (Playability Optional)

Verify actual Godot import/scene runtime and real fixed-camera screenshots, material/UV consistency, terrain/waterfall and cliff continuity, waterfall direction, instance placement and art quality. Preserve the accepted P1-concept and P2 visual result from all three views.

Record device/OS/renderer/settings, repeatable capture conditions, FPS/frame-time if actually measured, draw calls/triangles/VRAM when instrumented, actual bottlenecks and before/after image regressions. No invented benchmarks.

**Only if P1-playable was selected and approved:** run CharacterBody3D/NavigationMesh traversal, path local slope, width, landing, bridge/stairs and collision tests. Otherwise label them NOT APPLICABLE (ART-ONLY), and DO NOT block art delivery on navigation.

Report actual executed tests, screenshots, measurable performance evidence, licenses, remaining blockers and PASS / FAIL / NOT RUN / NOT APPLICABLE in reports/P5B_final_QA.md. Optimize only measured bottlenecks while preserving accepted visual quality.
