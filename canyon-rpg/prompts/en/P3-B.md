# P3-B — Build a Measured, Reusable Blender Modular Environment Kit

You are a procedural Blender asset developer and game-ready 3D pipeline engineer.

## Required source tutorials
Modular Village — real size, grid snapping, body clearance, Smart UV and texture atlas:
https://github.com/pttangent/Stylized_moutain_godot/blob/main/canyon-rpg/reference/canitcode/transcripts/57QEdTgUC3c_stop-asking-ai-for-whole-houses-opus-5-5-tripo.md

Cyberpunk City — exact Blender geometry plus generated surface detail, seam-fixing and module-fit failure tests:
https://github.com/pttangent/Stylized_moutain_godot/blob/main/canyon-rpg/reference/canitcode/transcripts/XqtnBlPJ6KE_is-this-really-ai-insane-opus-5-5-gamedev-workflow.md

Read remote sources with timestamp context; do not assume the source repository is available locally.

## Inputs and source preservation
Use approved P3-A asset manifest, orthographic images, P2 visual slice, style bible and any existing .blend/.glb files. Inspect existing content and preserve reproducible scripts.

## Geometry and export
1. Build parametric Blender Python mesh generators for straight/corner/cap cliffs, riverbank edges, bridge decks/supports, stair elements, fences, tree structures and designated reusable props.
2. Keep Godot Y-up world interpretation and agreed meter scale, correctly handled in Blender export. Document pivot, snap sockets, axis orientation and surface alignment.
3. Expose dimensions, bevel, variations and material assignments as script parameters. Maintain non-destructive source and separately export each reusable .glb; save .blend.
4. Start with budgets appropriate to screen size and frequency (simple props hundreds to low thousands of triangles, common modules a few thousand, special objects justified case by case). Measure *actual exported triangles*, not merely Blender faces.
5. Generate clean normals, reliable UVs, material atlases and appropriate simple collision meshes. Do not bake view-dependent shadows into shared base colors.
6. Use alpha-clipped foliage cards, atlases and LOD/instancing-ready geometry only if visual-slice tests support that design.

## Selective image-to-3D generation
For a distinctive small standalone prop, compare the cost and editability of geometry scripting with 3D generation. Verify whether available Tripo credits are Studio or API; Studio credits do not automatically apply to CLI. Check current model capabilities and one-job cost. Never spend credits without explicit approval. Begin with one model, not four variants. Validate imported orientation, dimensions, normals, topology, UVs, collision, texture sharpness and triangle counts; correct defects through reproducible postprocessing.

## Asset gallery and deliberate failure tests
Create a Godot gallery showing each part alone and in snapped assemblies. Programmatically validate connector positions, module gaps, stair/bridge clearance, texture density, UV seams, material count and collision. Add a deliberately offset or rotated module test to check that the validator catches known mistakes. Inspect from multiple angles and test actual CharacterBody3D clearance.

## Deliverables
docs/asset_manifest.csv, Blender Python generators, editable .blend files, independent GLBs, texture atlases, preview renders, Godot asset gallery, module validation scripts and reports/P3B_asset_kit.md. Report PASS / FAIL / ASSUMED / NOT RUN and costs. Do not proceed to full world population before kit acceptance.