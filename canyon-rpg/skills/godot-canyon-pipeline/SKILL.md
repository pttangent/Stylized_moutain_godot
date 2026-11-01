---
name: godot-canyon-pipeline
description: Build and QA art-first stylized natural canyon environments with Blender editable P1-concept blockout, optional Tripo small-model references, optional P1-playable Godot adaptation, and P2-P5 lookdev/assets/assembly/QA. Use for implementing, reviewing and handing off this canyon RPG project.
---

# Art-first Blender and Godot Canyon Pipeline

Read canyon-rpg/AGENTS.md and the selected phase prompt; never assume P1 means playable. Default to prompts/en/P1-concept.md (or zh). P1-playable.md is **opt-in** and not required for P2/P3/P4/P5 art work.

P0 uses original image + authored terrain/water/landform design. If an actual new Tripo small model is supplied, inspect it as nonmetric low-confidence reference; do not silently import earlier generated models. Provider-specific legacy P0 is isolated in prompts/en/P0-A-marble.md. Keep originals, source landmarks, camera calibration and revisions separate.

Art first: macro landform -> waterfall/river/pool geometry -> cliff/shore transitions -> fixed 45-degree hero composition and two alternate-camera clay renders -> visual acceptance. The heightmap is bulk terrain only; cliffs, overhangs, falls and bridges are separate editable meshes. No global 18-degree natural-terrain slope ceiling. Use regional 0.5m, 2m, 5m multiscale slope diagnostics; path slope and character dimensions apply only in optional playable mode.

Author geometry reproducibly in Blender Python and keep .blend, generators, diagnostic renders and individually exportable GLBs. Godot data is Y-up, Blender Z-up; validate axis conversion. Do not claim renders, collision or GPU tests not actually run.

P2 uses accepted P1-concept shape and cameras, then Godot material/lookdev testing. P3 modular assets; P4 environmentally plausible assembly; P5 actual visual and measured performance checks. Require a dedicated playable QA gate only if user selected playable.

Do not spend generation credits without permission. Record tool versions, source/license provenance and exact commands; classify PASS/FAIL/ASSUMED/NOT RUN. For Can It Code source attribution, consult reference/canitcode/AGENT_INDEX.md and source transcript timestamps.
