# Shared Agent Contract — Art-First Landscape Pipeline

**Default goal: visual environment art.** Read the currently selected prompt and the last actual gate report. Do not advance phases without approval. The default P1 is Blender P1-concept; **P1-playable is optional and explicit**, never a prerequisite for P2 art lookdev.

1. P0-A/B: source-image-first art-layout, terrain/water/landform slope design, provenance and camera shot plan. Optional small Tripo 3D model is unverified reference only. Legacy specialist model work stays isolated in prompts/en/P0-A-marble.md.
2. P1-concept: reproducible, editable Blender landscape geometry, three fixed-camera clay renders, landform and visual QA. No collision or navigation gate.
3. P1-playable (opt-in): preserve approved art, add route-specific collision/navigation, verify actual Godot traversal and visual regressions.
4. P2: style bible, lookdev and limited central-waterfall visual slice, preserving P1-concept framing. Godot runtime material checks matter at P2, even without playable navigation.
5. P3/P4: modular production, natural placement, river and waterfall systems; optional paths/collision only for selected gameplay mode.
6. P5: fixed-shot art QA and real engine profiling; traversal checks conditional on selected playable mode.

Coordinate truth: authored design data is Godot Y-up X/Z horizontal, 1 unit=1 authored meter. Blender native coordinates are Z-up; convert consistently and validate glTF roundtrip. Original images are the visible-landmark source; optional generated meshes (Tripo etc.) are NOT metric terrain, surveyed geometry or walkable ground. Preserve reviewed source IDs and original evidence. Version proposed design changes, never silently rewrite history.

Natural landscapes do not have a global path-slope ceiling. Audit multiscale terrain slopes (e.g. 0.5/2/5m) for art, erosion plausibility and unwanted uniform ramps. Apply optional ~18-degree ordinary walking-path guidance **only** to explicitly selected traversal geometry. Cliffs, undercuts and waterfall drop faces are independent meshes.

Work with existing toolchains. Prefer script-controlled Blender, editable .blend and per-component GLB for later Godot. Run actual tool commands and retain real images/logs; mark unrun tests NOT RUN. Avoid paid generation without explicit approval.

For techniques attributed to Can It Code, read reference/canitcode/AGENT_INDEX.md and the actual source transcript first. Cite original video/timestamps and distinguish adopted methods from custom design choices. Use the project skill and phase prompt before implementation.
