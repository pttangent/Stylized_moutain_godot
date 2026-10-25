# P0-A — Reconstruct a Stylized Canyon Image into a Playable Spatial Blueprint

You are an expert 3D RPG level designer and environment spatial architect.

## Required source
Read the complete timestamped Cyberpunk City workflow:
https://github.com/pttangent/Stylized_moutain_godot/blob/main/canyon-rpg/reference/canitcode/transcripts/XqtnBlPJ6KE_is-this-really-ai-insane-opus-5-5-gamedev-workflow.md

Focus on top-down level planning, simple grid-block geometry and player-scale checks. Retrieve the remote transcript through supported web or HTTP tools. Never assume a local checkout exists.

## Input and objective
Analyze the supplied reference image as a visual target, not an orthographic survey or a reliable measurement of hidden geometry. Produce a coherent, navigable metric 3D world plan. Do not build detailed assets.

## Procedure
1. Identify all major terraces, rock cliffs, river reaches, waterfalls, pools, bridges, staircases, trails and landmarks. Give each a stable ID and normalized source-image coordinates.
2. Record observed geometry separately from inferred or occluded geometry; include confidence and unresolved assumptions.
3. Derive a genuine top-down layout, not a perspective-warped image.
4. Use Godot Y-up coordinates, horizontal X/Z and vertical Y, at 1 unit = 1 meter. Start with a provisional 96 x 64 m area and a 1.6 m character for scale; revise only with documented evidence.
5. Define terrace footprints, elevations, cliff boundaries and transitions. Represent overhangs separately from heightmap terrain.
6. Create a directed Water Flow Graph for sources, channels, confluences, positive downward waterfall drops, pools and outlets.
7. Create a Navigation Graph of walkable areas, bridges, stairs, blocked edges, main routes and optional routes. Check route connectivity and bridge endpoint placement.
8. Define a fixed RPG camera: approximately 45 degrees down, preferably orthographic, 16:9, limited distortion, no horizon. Record position, target, rotation, ortho size, near/far and landmark alignments.
9. Do not force ambiguous visual areas into falsely precise 3D coordinates.

## Required outputs
- blueprint/scene_blueprint_draft.json
- Annotated true top-down plan with scale and axes (or complete vector/coordinate specification when graphical output is unavailable)
- Terrace elevation table and cliff-edge boundaries
- Proposed water graph and navigation graph
- Camera parameters
- reports/P0A_spatial_analysis.md with OBSERVED / INFERRED / UNKNOWN evidence and confidence

Produce real artifacts when tool support exists; otherwise deliver unambiguous machine-readable specifications and name missing outputs honestly. Stop before geometry modeling.