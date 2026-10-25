# Shared Agent Contract

Read the project skill and current phase prompt. Work one verified task at a time; never advance the phase without user approval.

Workflow derived from Can It Code:
1. Top-down level layout and metric topology.
2. Playable Godot blockout, tested with character.
3. Visual slice and in-engine render gauntlet.
4. Modular Blender Python assets; orthographic source views only for distinctive parts.
5. Curve-based paths, vegetation and offline water flow cache.
6. Fixed-camera visual comparison and performance QA.

Tool assignment: Gemini Argon for scene understanding and critic; Claude Code for Godot engineering; Codex for Blender Python and QA; optional Tripo for small props with explicit credit authorization. Each agent must verify local tool availability.

Godot 4, Y-up, 1 unit = 1 meter. Keep .blend and Blender Python scripts under blender/, GLB under assets/, Godot .gd/.tscn/.gdshader under godot/. Commit scripts and test outputs. Reference image occlusions are ASSUMPTIONS rather than accurate geometry. Record exact test commands, actual screenshots, collision/navigation coverage, errors, hardware metrics and source/licensing. Do not claim tests were run without results.

The local full distribution contains phases prompts/en/P0.md to P5.md, prompts/zh/P0.md to P5.md, plus skills/godot-canyon-pipeline/SKILL.md.