# P0-B — Materialize and Validate Engine-Ready Scene Blueprint Files

You are a procedural level-design tooling engineer.

## Required source
Cyberpunk City — top-down plans and metric geometry:
https://github.com/pttangent/Stylized_moutain_godot/blob/main/canyon-rpg/reference/canitcode/transcripts/XqtnBlPJ6KE_is-this-really-ai-insane-opus-5-5-gamedev-workflow.md

Read the remote transcript if needed. Do not assume any Git repository or transcript is locally available.

## Inputs
The user-provided reference image, the approved P0-A spatial analysis (file or text), and the active project workspace. Inspect the actual inputs; if approved P0-A data is missing, report the missing dependency rather than inventing it.

## Implementation
Use Python, NumPy, Pillow, SVG and JSON or equivalent reliable local tools to create:
1. blueprint/scene_blueprint.json: stable element IDs, world bounds, coordinate transforms, units, terrace elevations and uncertainty.
2. blueprint/layout_topdown.png: true top-down map with meters, scale bar, grid axes, platform footprints, cliff boundaries, rivers, bridges, stairs and labels.
3. blueprint/heightmap_16bit.png: *actual* grayscale 16-bit height data with documented min/max Y mapping; not an 8-bit RGB mockup.
4. blueprint/cliff_edges.json: separate steep/vertical/overhanging wall outlines and elevation data.
5. blueprint/water_graph.json: directed water network with node coordinates, downstream flow, waterfalls, height drops and confluences.
6. blueprint/navigation_graph.json: walkable platform IDs, edge traversal modes, bridge/stair endpoints, route connectivity, forbidden edges.
7. blueprint/camera.json: Godot-compatible camera transform, orthographic size, clipping ranges and framing targets.

Keep all outputs mutually consistent. Do not silently reinterpret approved geometry.

## Automated validation
Implement deterministic Python tests to verify file existence, JSON validity, shared coordinate conventions, unique IDs, all referenced graph nodes, actual 16-bit raster mode, height normalization, downhill waterfall transitions, valid bridge connections, route reachability, allowed world bounds, camera parameters and coverage of approved landmarks. Produce visual previews and overlay comparisons where possible.

## Acceptance and reporting
Deliver every actual file, the generator and test scripts, preview images and reports/P0B_validation.md. Classify PASS / FAIL / ASSUMED / NOT RUN; give real commands and errors. Do not proceed to 3D blockout until the blueprint is approved.