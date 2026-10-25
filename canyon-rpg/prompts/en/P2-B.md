# P2-B — Make a High-Quality Central-Waterfall Vertical Slice

You are a procedural Blender environment builder and Godot real-time technical artist.

## Read source tutorials
Cyberpunk City — compare model construction options, select precise Blender geometry plus generated textures:
https://github.com/pttangent/Stylized_moutain_godot/blob/main/canyon-rpg/reference/canitcode/transcripts/XqtnBlPJ6KE_is-this-really-ai-insane-opus-5-5-gamedev-workflow.md

Mountain — reference-driven tree modeling with Blender Python, incremental scene tests and a render critique loop:
https://github.com/pttangent/Stylized_moutain_godot/blob/main/canyon-rpg/reference/canitcode/transcripts/78diFcn3Qas_i-stole-a-mountain-for-my-game.md

Retrieve these from the URLs if necessary; do not assume a local repository.

## Scope
Only the central large waterfall, wooden bridge above it, adjacent cliff facades, river/pool segment, exactly three prototype trees and a small quantity of grass/rocks. Do not dress the full map.

## Implementation
1. Keep approved P1 terrain, traversability and camera. Test on a self-contained central scene.
2. Compare (A) existing/approved generated 3D prop where available, (B) Blender geometry with procedural material, (C) exact Blender geometry plus generated textures. Same in-engine camera and light; measure shape, editability, material quality, geometry and cost. Do not spend credits without approval.
3. Use versioned Blender Python for precise bridge/rock geometry. Generate or preprocess seamless neutral-lit rock, moss, soil, grass and wood textures. Create sensible normal and roughness and mask-based wet/dirt variation, without fixed shadows in base color.
4. Prototype exactly three distinct trees: trunk/branch geometry, canopy silhouette, baked leaf cards or low-poly leaves, texture atlas, plausible wind animation. Inspect single trees and a tiny cluster.
5. Make a low-cost Godot water shader for directional stream motion, a separately authored falling-water mesh/animation, impact foam and limited spray. Add readable natural sunlight, soft shadowing and restrained atmosphere.
6. Build → run Godot → capture fixed-camera screenshot → compare to source and style bible → list visible failures with locations and proposed fixes → revise only failing components. Preserve before/after evidence.
7. Check exported assets from multiple angles for unseen holes, intersecting geometry, UV seams, transparency sorting and collision issues.

## Deliverables and acceptance
Working Godot vertical-slice scene, Blender generators/.blend/.glb, material textures, shaders, three-tree comparisons, method A/B/C comparison where feasible, actual Godot screenshots, and reports/P2B_vertical_slice.md. Only real in-engine render quality counts; Blender offline images alone are insufficient. No bulk asset production until the visual direction passes.