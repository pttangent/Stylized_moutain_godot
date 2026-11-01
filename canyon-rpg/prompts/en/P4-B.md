# P4-B — Assemble the Stylized Canyon Environment (ART FIRST)

Inputs: approved P0 art blueprint, P1-concept Blender art graybox and cameras, P2 visual direction, P3 modular kit, P4-A water-flow cache, original reference. **P1-playable is optional**, not a prerequisite.

Build art-first editable cliff/terrain/river/waterfall meshes, use splines for decorative paths and channels, vegetation scattering by slope/elevation/moisture/rock/river proximity, stable random seed and independent landmark trees. Preserve terrain geomorphology, visual hierarchy, asymmetrical riverbanks and all three P1 camera compositions. Keep waterfall faces, receiving pools and bulk heightfield independent.

Avoid assuming every road, bank or forest floor is navigable. Only if P1-playable was explicitly approved, include gameplay route/clearance/collision/NavMesh validation and preserve previous art while testing paths. Otherwise run geometry, water, asset grounding, deterministic rebuild, shader and camera visual checks.

## Natural-area instance placement and revision gates
For every biome-region prototype, record source `asset_id`, licensed origin, stable placement seed, slope class, normalized elevation range, local moisture proxy, water distance, rock-face exclusions, density and hero-landmark exemptions. Geometry Nodes and Collection Instances are preferred over individually unique grass/pebble objects. Different distribution rules should make a wet shoreline feel distinct from a vertical rock face and a broad grassland. Avoid random noise masquerading as geomorphology or a perfectly uniform vegetation lattice.

Maintain a reproducible per-region scatter manifest and explicit `change_scope` mapping, so modifying one riverbank/vegetation region does not rebuild other approved zones or move CAM_HERO_45. Do not automatically realize all GN instances; estimate evaluated visible load, and reserve true 3D mesh realization for a demonstrated per-export need. If Godot materials cannot preserve the Blender GN instance system, export a documented compatible representation while preserving seed, IDs and visible arrangement.


Capture actual Godot hero + two alternate screenshots and record hardware settings, scene build commands, visually visible defects and available performance metrics. Deliver editable modular scene, seeded procedural scripts, water integration and reports/P4B_world_assembly.md; do not claim unrun traversal tests passed.
