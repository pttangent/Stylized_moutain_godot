# P3-A — Modular Asset Inventory and Strict Orthographic References

You are a 3D environment asset planning and technical reference designer.

## Required source tutorials
Modular Village — draw parts before modeling; orthographic front and side geometry, real dimensions and voids:
https://github.com/pttangent/Stylized_moutain_godot/blob/main/canyon-rpg/reference/canitcode/transcripts/57QEdTgUC3c_stop-asking-ai-for-whole-houses-opus-5-5-tripo.md

Cyberpunk City — build a modular kit, compare procedural geometry with image-to-3D:
https://github.com/pttangent/Stylized_moutain_godot/blob/main/canyon-rpg/reference/canitcode/transcripts/XqtnBlPJ6KE_is-this-really-ai-insane-opus-5-5-gamedev-workflow.md

Access these complete timestamped transcripts remotely through available web/HTTP tools. Do not assume a local checkout of the reference repository.

## Inputs
The supplied reference image, approved P0 spatial geometry, P2 style bible, any existing asset inventory and available visual resources. Inspect what already exists before making duplicates.

## Work
1. Inventory visible terrain, cliff segments, bridges, bridge supports, steps, railings, fences, riverside rocks, three major tree archetypes, bushes, grass and decor.
2. Normalize them into reusable asset *families*, not one model per visible tree/rock. Prioritize assets used by the approved visual slice.
3. For each family, record unique ID, intended dimensions in meters, pivot convention, connector/snap locations, collision needs, visual role, likely generation method and expected repetition.
4. Categorize production method: procedural Blender geometry for terrain, cliffs, structural modular assets; image-reference and optional image-to-3D for distinctive small props; shader/geometry for water; card/atlas/instancing for grass and leaves.
5. When a 3D model genuinely benefits from image references, make a strict orthographic front and side view, with top or rear only as needed. Maintain scale, full silhouette, consistent colors and topology across views.
6. Use a transparent or uniform background, no perspective tilt, no cropping, no misleading shadows or floating details. Clearly identify inferred unseen portions.
7. Specify *negative constraints*: no unsupported spikes, protrusions, holes, sealed doorways, arbitrary decorations or geometrically impossible shapes.
8. Validate one reference set per unique part before multiplying variants. No mass asset generation.

## Deliverables
docs/asset_manifest.csv with IDs, dimensions, reuse priority, and method; approved orthographic references or their exact image-generation prompts; per-asset acceptance checklist; reports/P3A_references.md with missing/assumed sources. Do not spend 3D-generation credits or model assets in this phase.