---
name: godot-canyon-pipeline
description: Build and QA stylized modular nature canyon scenes in Godot 4 with Blender Python source scripts, P0 topology blueprint, P1 traversable graybox, P2 vertical slice, P3 modular assets, P4 procedural placement and P5 rendered visual QA. Use when implementing, reviewing or handing off this canyon RPG.
---
# Godot Canyon Pipeline

Read project AGENTS.md, prompts/en/P*.md and relevant previous gate report. Use one fresh scoped task per session. Test after each task; rerun the failed task, not the entire game.

- The main scene is in godot/. Use Godot 4, Y-up and 1 unit = 1 meter.
- Prefer versioned Blender Python scripts: blender --background --python blender/scripts/<name>.py. Keep .blend and .glb; Blender MCP is optional, not required.
- Use separate modular cliffs for steep faces, not a heightmap alone.
- Create curves/splines for road assembly, keep terrain editable, and validate navigation.
- Compute riverbed depth/flow offline and feed Godot shaders; waterfalls are separately authored geometry/effects.
- Optimize forest with leaf cards/atlases and instance clustering; keep paths clear.
- Lock reference camera for comparison; visual critic must inspect actual Godot captures. Do not claim in-engine render or benchmark unless performed.
- Tripo costs money; get exact approval before running credit-consuming jobs.
- Respect asset license provenance and stable module ID/dimensions/pivots/collision.
- Stop at phase gate for review.

The original uploaded godot-clay-render-options ZIP was incomplete and contained zero-byte .qkdownloading entries, so those shaders/templates are not installed.
## Source-backed workflow retrieval

Consult `reference/canitcode/AGENT_INDEX.md` **before** applying channel techniques. It maps P0–P5 to the timestamped transcript files; use the local `reference/canitcode/scripts/search_kb.py` for exact keyword retrieval and `visual_index/` for secondary visual descriptions. Do not treat transcription or visual-index summaries as verified source footage; include YouTube timecode and label inference. Source rights information: `reference/canitcode/PROVENANCE.md`.
