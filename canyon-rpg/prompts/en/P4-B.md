# P4-B — Assemble the Full Stylized Canyon with Procedural Paths and Vegetation

You are a Godot 4 procedural natural-environment developer.

## Required reference
Mountain — spline-driven terrain-following roads, modular segments, path exclusion rules, river integration, vegetation and incremental small scenes:
https://github.com/pttangent/Stylized_moutain_godot/blob/main/canyon-rpg/reference/canitcode/transcripts/78diFcn3Qas_i-stole-a-mountain-for-my-game.md

Read remote timestamped source material. Do not presume an existing local source checkout.

## Inputs
Approved P0 top-down/world coordinates, validated P1 blockout, approved P2 rendering style, P3 modular asset kit, P4-A flow cache and the user's target reference image. Inspect the existing scene before replacing any blockout geometry.

## Tasks
1. Replace open blockout ground with editable production terrain while preserving known terrace heights and route connections. Use separate modular cliff meshes for sheer or overhanging faces and blend seams with riverbanks/terrain.
2. Build path, bridge, stair, shoreline and fence layout using Godot Curve3D or equivalent splines. Deform/repeat short reusable road sections along curves; retain the ability to widen/move paths without manually sculpting the entire terrain.
3. Scatter vegetation deterministically using elevation, slope, moisture/distance-to-water, forest zones, cliff edges, walking exclusion masks and a stable random seed. Preserve important landmark trees as independently editable scene objects.
4. Use instancing, shared atlases, foliage cards, LOD and well-sized spatial chunks for culling; inspect alpha overdraw and materials rather than blindly increasing tree density.
5. Integrate river rendering from the cached flow fields and attach independently modeled waterfalls/foam to their correct elevations.
6. Assemble upper canyon, central waterfall, lower pool, downstream and surrounding forest. Add controlled, subtle, non-synchronized foliage motion and limited decorative props.
7. Expose biome density, placement seed, wind intensity, path width, water motion, rock variation and visual settings as safe scene parameters.
8. Run automatic connectivity, terrain/path collision, asset grounding, bridge/stair clearance, water continuity and deterministic-rebuild checks. Verify the locked reference camera still matches the intended composition.
9. Capture actual Godot screenshots from fixed and free cameras. Record graphics settings and performance baseline; do not invent benchmark data.

## Deliverables
Full editable Godot scene, modular placement scripts, reproducible world seed, path tools, instantiated vegetation, integrated cached water system, traversal/geometry tests, screenshots and reports/P4B_world_assembly.md. Do not declare final completion before P5 QA.