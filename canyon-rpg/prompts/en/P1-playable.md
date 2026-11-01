# P1-playable — OPTIONAL Godot Traversability Adaptation

You are a Godot 4 level-design/physics engineer. This branch is **strictly opt-in** after an approved Blender P1-concept. **Do not replace or flatten the approved visual scene** simply to make graphs pass. If no approved concept exists, report the dependency and do not invent an approved source.

## Inputs and immutable reference
- Approved blender/source/p1_concept.blend, versioned Blender generators and three locked cameras/renders, blueprint/p1_art_revision.json and reports/P1_concept.md.
- Updated terrain, cliffs, waterfalls, water graph and candidate route intents. Old P0 navigation_graph.json is a **proposed route topology**, not exact centerline, endpoint elevation or verified NavMesh.
- Original image and source markup remain canonical for visual landmarks. Preserve concept art scene and use a new export/branch for gameplay. Record every necessary change with before/after dimensions and an explicit visual-impact review.

## Plan only purposeful walking surfaces
1. Agree on entry, main/optional routes, inaccessible scenic land and exact destination platforms. If user does not require a route, do not invent it or disturb surrounding art.
2. Trace route centerlines along observed paths in image pixels and map to the actual Blender geometry. At occluded/unmapped areas distinguish DESIGNED, INFERRED and UNKNOWN; keep optional route segments instead of claiming a physical connection.
3. Create a playable overlay: separate ground/path support or hidden ramps, explicit bridge deck/rail, stairs and landing meshes. Maintain visually accepted banks, cliffs and water. Favor **additive invisible physical support** over destructive reshaping; version changed artist meshes when unavoidable.
4. Defaults unless the current project says otherwise: 1 authored unit = 1m Godot Y-up; test player height 1.75m, radius 0.35m; regular walking slope target <=18 degrees, stair riser <=0.175m, floor clearance and usable width verified along actual paths. These are **walking geometry targets ONLY**, not global artistic surface limits. Local running slope must be measured along routes, not inferred from endpoint slope averages.
5. Keep solid rock, waterfall volumes, river channel and tree canopy distinct from walkable surfaces. Use collision and exclusion layers appropriate to gameplay; raw generative model triangles are never accepted as production collision without inspection.
6. Export separate terrain/rock/path/water GLBs and versioned Godot sub-scenes, maintaining names and transforms. Confirm Blender Z-up -> glTF/Godot Y-up round-trip for sample landmarks before bulk export.

## Test in the actual Godot runtime
7. Implement StaticBody3D and collision shapes for relevant surfaces, CharacterBody3D gravity/movement and physical probes. Build NavigationMesh (if used) with correct agent settings.
8. Execute automated + representative manual/recorded traversal from spawn across bridges, landings and stairs to the approved goal and branch destinations. Sample local grade, widths, clearance, stability near cliffs, gap and fall hazards. A connected JSON graph is **NOT** proof of a playable route.
9. Capture real 16:9 Godot hero/alt cameras matched against P1-concept frames; document changes in silhouette, waterfall/pool proportions, bridge scale and foreground occlusion. Preserve all approved art where feasible. If traversal requires a visible destructive change, leave that route BLOCKED for an art decision rather than claiming a pass.
10. Record Godot/Blender versions, imports, collision/NavMesh evidence, test route paths, actual logs, screenshots and PASS / FAIL / BLOCKED / NOT RUN. Do not claim performance or physical checks not executed.

## Deliverables and stop
- Versioned playable adaptation sources, Godot test scene, real collision and (if needed) navigation, runnable traversal tests, layout-diff report and fixed camera screenshots.
- reports/P1_playable.md with source concept revision, route-by-route result, measured slope/widths/clearance, failures and art regressions.
- Gate: P1_PLAYABLE_APPROVED requires **both real traversal evidence and preservation of the agreed visual composition**. This is optional; do not gate P2 visual work on it. No final P2 materials or P3 production assets in this task.
