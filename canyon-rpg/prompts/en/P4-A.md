# P4-A — Offline River Depth/Flow Simulation and Stylized Waterfalls

You are a numerical environment simulation and Godot real-time water rendering engineer.

## Required reference
Mountain — offline dry-riverbed grid filling, per-cell water depth and flow direction, cached results, Godot shaders and separate waterfall behavior:
https://github.com/pttangent/Stylized_moutain_godot/blob/main/canyon-rpg/reference/canitcode/transcripts/78diFcn3Qas_i-stole-a-mountain-for-my-game.md

Read the complete relevant source section directly via remote URL. Do not assume a local file or cloned repository.

## Inputs
Approved Water Flow Graph, riverbed geometry, world elevations, channel widths, waterfall drops, current Godot scenes and the supplied visual target. Preserve earlier approved geometry and navigation.

## Procedure
1. Represent rivers, pool areas and obstacles on a reproducible grid or documented equivalent. Store bottom elevation, water surface/depth, flow vector, relative speed, boundary/obstacle and cell validity.
2. Implement a stable, appropriately simplified *offline* solver or flow-propagation method. Feed from known upstream sources; respect plausible downhill trajectories, pool storage, confluences and explicit outlets.
3. Test a dry initial condition or an equivalent repeatability test. Prove graph continuity, no upstream flow without physical explanation, consistency around obstacles, and deterministic output. Explain limitations; do not claim validated CFD accuracy without evidence.
4. Serialize compact data to a file/texture cache that Godot can load once, rather than recomputing the river every frame.
5. Write a Godot water shader that uses cached flow vectors and depth to animate UVs, small waves, water color/transparency, boundary foam and relative speed coherently.
6. Implement vertical waterfalls as **separate** mesh/sheet animation, falling-water trajectories, impact foam and optional particles; match top and bottom water transitions.
7. Verify actual engine screenshots and flow directions at upstream, steep, deep pool and downstream positions. Keep the stylized look aligned with the visual target.
8. Profile runtime memory and shader cost under stated hardware and renderer settings.

## Deliverables
Deterministic Python offline-flow generator, documented format and cached output, Godot shader(s), waterfall scenes, test harness/fixtures, actual engine captures and reports/P4A_water_system.md with measured results, limitations and PASS / FAIL / ASSUMED / NOT RUN statuses. Do not generate unrelated environment assets.