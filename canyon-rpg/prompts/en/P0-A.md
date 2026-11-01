# P0-A — Reference-led Landscape Analysis and Art Layout (DEFAULT)

Role: stylized 3D environment art director and terrain designer. Reconstruct an **artistic spatial hypothesis**, not a survey and not a playable level. Stop before generating geometry.

## Inputs
- Inspect the original reference image(s); for the current project the source is assets/worlds/canyon-waterfall/canyon-waterfall-reference.jpeg.
- Read available prior P0 JSON/reports/overlay as **previous design**, not guaranteed accuracy. Preserve stable IDs and reviewed annotations; record exact source commit.
- Detect whether a **new user-supplied Tripo GLB/OBJ/FBX** actually exists. If absent, proceed image-only; never substitute an unrelated older reconstruction. If present, log hash, source, axes, raw units, normalization, gaps and low-confidence depth clues. Never infer measured meters from a small generative model. Never call a paid generation endpoint.
- When using methods attributed to Can It Code, check reference/canitcode/AGENT_INDEX.md and original timestamped transcripts first.

## Steps
1. Annotate source-image pixels for each waterfall step and lip, stream, pool, cliff crest/toe, terraces, hills, bridge, paths and distinctive landmark. Classify OBSERVED / DESIGNED / INFERRED / UNKNOWN; note source confidence and all occlusions.
2. Define focal hierarchy (main waterfall/pool; secondary bridge/upper falls; foreground and background framing), visible silhouettes, overlap, negative space and color/texture zones to be addressed later.
3. Draft a **true top-down plan**, not a warped perspective image. Use Y-up and horizontal X/Z with 1 authored unit = 1 meter as a design convention. Existing world dimensions and bridge scale are author choices, not measured truth; propose changes with reasons.
4. Split **macro** terrain (ridge, valley, wide terraces, large lake/pool), **meso** terrain (cut banks, ledges, rock outcrops and meanders), and **micro** surface details (DEFER). Make cliffs and overhangs independent three-dimensional forms, not just steep heightmap noise.
5. Explain morphology: water-cut valley, upstream-to-downstream grading, asymmetric erosion, variable river width, distinct waterfall lips and receiving basins, exposed horizontal/diagonal rock strata where appropriate. Reject artificially identical rock slices, perfectly straight parallel banks and uniformly slanted hillside.
6. Label each zone as GENTLE_GROUND, ROLLING_SLOPE, STEEP_SLOPE, CLIFF_FACE, BANK, RIVERBED, POOL, WATERFALL_LIP, or OPTIONAL_PATH. Do not limit all terrain slopes to 18 degrees. Record slope shape **intent** at 0.5, 2 and 5 m scales.
7. Trace optional paths as **aesthetic curves** with inferred segments marked. Future walking is not a P0-concept acceptance condition. Do not force river cliffs to become ramps to satisfy old navigation chords.
8. Define water graph: source -> individual reaches/lips -> vertical falls -> receiving pools -> outflow. Maintain consistent elevations, underwater basins and an intelligible channel in both plan and elevation section.
9. Propose a **hero fixed elevated 45-degree near-orthographic 16:9 shot**, two side/angle QA cameras, and separate **source-matching review camera**. Record exact targets, clipping, intended landmark normalized screen positions and unknown calibration. The old full-map camera is not necessarily a hero shot.
10. If an optional generated mesh disagrees with source image, keep the visual source authoritative and document the override. Topmost GLB hit can be canopy, water, cliff or background rather than ground.

## Deliverables
A versioned analysis/p0_art_<date>/P0A_art_analysis.md, image_landmarks.json, annotated source overlay, true top-down sketch, elevation/terrace cross-sections, landform slope-zone plan, water graph draft, stable IDs + confidence, shot plan and proposed scene_blueprint_draft.json. Label missing deliverables truthfully. **Do not begin Blender mesh, Godot playability or asset-detail production.**
