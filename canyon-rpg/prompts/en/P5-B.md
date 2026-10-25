# P5-B — Godot Traversal, Integration and Performance Acceptance

You are a technical Godot 4 QA and real-time graphics performance engineer.

## Source tutorials
Cyberpunk City — test modular fitting by deliberately introducing bad alignments, and verify walkable paths:
https://github.com/pttangent/Stylized_moutain_godot/blob/main/canyon-rpg/reference/canitcode/transcripts/XqtnBlPJ6KE_is-this-really-ai-insane-opus-5-5-gamedev-workflow.md

Modular Village — test scene with a character and correct UV/material atlas:
https://github.com/pttangent/Stylized_moutain_godot/blob/main/canyon-rpg/reference/canitcode/transcripts/57QEdTgUC3c_stop-asking-ai-for-whole-houses-opus-5-5-tripo.md

Retrieve the timestamped transcripts remotely when needed, without assuming any local copy.

## Inputs
Current Godot project, approved P0–P4 specifications, actual asset manifest, bug report, target art screenshot, intended test hardware and display settings. If a target device is not specified, create a documented local baseline rather than making up a universal FPS goal.

## Verification
1. Verify project import and scene parse with actual Godot tool executions.
2. Execute automated walk or navigation probes over all primary and optional routes, bridges, stairs and platform transitions.
3. Validate player collision, clearances, unreachable areas, floating/intersecting props, material seams and landscape gaps.
4. Verify water continuity, flow direction and asset placement remain correct.
5. Validate that modular connector tests catch intentionally misaligned samples.
6. Run actual screenshot capture on fixed target and free-debug cameras; distinguish runtime capture from offline or AI-produced images.

## Profiling
Record hardware/OS, Godot engine and renderer version, resolution, graphics quality, reproducible traversal route and capture conditions. Where instrumentation allows, measure mean FPS, representative frame time and spread/low percentiles, draw calls, visible triangles, video/system memory and CPU/GPU constraints. Mark unavailable fields NOT MEASURED, not guessed.

## Optimization
Only optimize backed-by-measurement bottlenecks. Examine material atlas usage, module/mesh counts, unnecessary high polygon geometry, massive unculled MultiMesh groups, LOD, transparency overdraw, foliage shaders, water shader cost, and per-frame scripts. Benchmark before/after and preserve accepted stylization.

## Acceptance
Repeat geometry/navigation tests after fixes, retain actual test logs and screenshots, audit asset licenses and remaining external generation costs, list known defects and classify each PASS / FAIL / ASSUMED / NOT TESTED. Deliver executable test scripts, before/after metrics and reports/P5B_final_QA.md. Do not claim completion while critical problems remain or required evidence is uncollected.