# P0-B — Generate and Validate Art-First Spatial Blueprint

Role: Blender-compatible procedural landscape-layout engineer. Use approved P0-A analysis and original images. Prior numerical checks are historical structure validation, NOT proof of art quality or physical traversability.

## Required outputs and operations
1. Create versioned scene_blueprint.json: ID, original image coordinates, authored X/Z/Y positions, world bounds/scale assumption, confidence and evidence type; never silently change prior reviewed anchors.
2. Make **true top-down** layout_topdown.png with legend, axes, scale, waterfall lips, ponds, cliff lines and optional visual paths.
3. Create a real single-channel **uint16** heightmap_16bit.png with elevation min/max, transform, sampling and resolution. This is **authored bulk terrain only**: separate vertical cliff faces, overhangs, bridge and falling water into independent authored 3D shape contracts.
4. Create landform_zones.json, cliff_edges.json and bank/waterfall elevation sections. Design regions distinguish gentle land, rolling slope, steep slope, cliff/overhang, bank, riverbed, pool and optional path. Include meaningful irregularity and transition cues.
5. Create directed water_graph.json. Check descending water surface and waterfall elevation jumps, each lip's receiving basin, plausible downstream outlet and pool geometry, without claiming fluid physics.
6. Compute terrain slope theta = atan(sqrt((dY/dX)^2 + (dY/dZ)^2)) in degrees, at approximately 0.5 / 2 / 5 meter smoothing scales. Run blueprint/landform_slope_audit.py if available and save JSON + angle previews. Diagnose implausibly uniform inclines and excessive geometric regularity. A **global 18-degree limit is prohibited**. The 18-degree figure, if used, is advisory for explicitly marked future *ordinary walking paths* only.
7. Record hero 45-degree orthographic 16:9 camera, source-comparison camera and two alternate shots, camera position/target/ortho size/landmark normalized projection. Keep existing camera.json backward-compatible; source-pixel reconstruction and game camera must not be conflated.
8. If an actual new small **Tripo** mesh is supplied, use it as inspectable low-confidence evidence after axes and model provenance checks; **never** automatically reuse old models or overwrite reviewed data. If not supplied, image-only blueprint remains valid.
9. Optional navigation_graph.json can be kept as ART_ROUTE_INTENT_ONLY. No collision, path connectivity, navmesh, physical stair design or CharacterBody3D acceptance in art mode.

## Checks and exit
Verify referenced IDs, units, real raster bit depth, water direction, separate cliffs, original-image silhouettes, terrain sections, authoring cameras, multiscale slopes, source conflicts and report evidence. Report ART_TOPOLOGY, ART_GEOMORPHOLOGY_REVIEW, CAMERA_UNVERIFIED, OPTIONAL_ROUTE_NOT_TESTED separately. Produce reproducible scripts, preview graphics and reports/P0B_art_validation.md with real PASS/FAIL/ASSUMED/NOT RUN. Do not claim measured terrain or playable world. Exit to P1-concept, **not** forced P1-playable.
