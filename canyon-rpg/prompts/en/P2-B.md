# P2-B — Godot Visual Lookdev Slice From Approved Blender Art Blockout

Role: Blender stylized environment artist and Godot technical artist. Input: **approved P1-concept Blender geometry and locked camera screenshots**. P1-playable is **NOT required**. Read project P2-A art direction and original image.

Scope: main waterfall and pool, near cliff walls and bridge proxy, exactly three prototype tree types, small sample grass/rocks. Keep the hero 45-degree and two review cameras; compare authentic Blender clay shapes and actual Godot results. Do not redraw or silently simplify topography to match a road or navigation graph.

Use reproducible Blender scripts, .blend and separate GLBs. Develop rock, soil, moss, grass and wood shader tests with neutral-lit texture sources; add a distinct falling-water mesh, downstream flow, foam and restrained spray. Keep banks, pool and stratified cliffs coherent, and inspect one representative central slice before mass production.

Test materials/lighting/shadows/transparency with **actual Godot renderer captures**, without CharacterBody3D/NavMesh requirements. Record source frames, render settings, before/after corrections and genuine PASS/FAIL/NOT RUN. Check geometry continuity, clipping, material UVs and silhouette from all three P1 camera views. Do not run paid generation without approval. Deliver shaders, Blender sources, prototype assets, real Godot screenshots and reports/P2B_vertical_slice.md.

## Upstream geometry contract and visual-lock preservation
Use the approved P0 geometry-reference contract and P1-concept art IDs as a **visual-shape lock** when changing materials or adding prototype vegetation. Changing a hero cliff material must not silently regenerate its mesh, move a waterfall anchor or change the camera. The L1 macro and L2 sculpted geomorphology should remain inspectable from the original hero/left/right cameras. L3 instances (prototype foliage/rocks) may begin here only after those shape gates passed, with stable IDs/seeds. If a visible geometry revision is unavoidable, record a local change_scope and rerender its dependent views. P1-playable remains optional.
