# Optional scene-type examples (NOT DEFAULTS)

These are **reference profiles**, not the canonical production prompt. Nothing in this file authorizes an agent to assume this scene type, these objects, a fixed camera angle, a particular engine, or a specific art style. Select a profile only if the user brief or an approved `scene_profile.json` identifies it. Otherwise analyze the scene from its actual sources.

## Scene-profile selection
1. Determine the intended subject, style, level of realism, scale, camera and deliverable from the user's inputs.
2. Choose only the applicable context below; combine selectively for mixed scenes.
3. Mark assumptions and excluded categories explicitly. Do not introduce objects solely because they occur in these examples.
4. Required evidence, geometry constraints and QA follow the actual scene, **not** a copied template.

| Example category | Possible geometry/layout priorities | Optional production techniques | Typical QA questions |
|---|---|---|---|
| **Interior** (rooms, studios, offices, shops) | Room proportions, visible partitioning, walls/floor/ceiling, openings, furniture clearance where relevant, layered depth | Modular wall systems, parametric openings, object instancing, trim sheets, bevel/boolean where suitable | Do spaces align with references? Are portals, surfaces and silhouettes coherent from relevant cameras? |
| **Exterior built environment** (courtyards, gardens, plazas, transit frontage) | Building-to-ground connections, circulation intent, open space, composition and proportion | Modular structures plus sculpted ground; conditional vegetation and hardscape scattering | Are major forms, transitions and foreground/background scale believable? |
| **City / urban district** (street, intersection, neighborhood, skyline) | Block hierarchy, street widths, building rhythm, skyline silhouettes, visual density, traffic/circulation only if required | Facade modules, splines for streets, shared props, rule-based generation, LOD for repeated assets | Is scale and variation coherent? Do repeated modules look artificial? Do major routes/landmarks frame correctly? |
| **Wilderness / natural terrain** (mountain, coast, desert, forest, river valley) | Broad landform masses, geomorphic logic, boundaries and transitions, vegetation only if the input requires it | Heightfields for single-valued terrain, independent cliffs/overhangs, procedural stratification/erosion, density masks | Are natural structures plausibly related? Are repeated forms and slopes overly uniform? |
| **Industrial / mechanical** (factory, plant, machine hall) | Functional hierarchy, structural supports, clearances where needed, connection logic | Reusable component families, curves/pipes, hard-surface modeling, parametric assemblies | Are connections, support relationships and dimensions consistent? |
| **Fantasy / science fiction / abstract** | User-defined world rules, strong silhouette, deliberate departures from realism, consistent authored visual logic | Mix of hand-crafted hero forms, procedural modules and selective generation | Does it meet the approved visual language without automatically assuming Earth-like geography or engineering rules? |

## Example-specific decision records (illustrative, not copied)
**Interior example:** primary evidence is a floor plan and two perspective sketches. One hero camera shows the entrance and main activity space; movable props are separate assets. No terrain erosion, water-flow graph or outdoor biome system is introduced.

**Exterior-built example:** primary evidence is a site reference and a rough measured footprint. Ground contact and elevation change are modeled only where the real scene requires them. Circulation may be an aesthetic path, or an actual walkable route if explicitly required.

**Urban example:** primary evidence is a city block reference and a target camera shot list. Assign unique block IDs to architectural masses, repeat lower-level modules carefully and preserve landmark building silhouettes. Water features or vegetation occur only when observed/requested.

**Wilderness example:** primary evidence is landscape imagery and an approved conceptual top-down map. Choose appropriate landform semantics from the image: dunes, erosion channels, rocky terraces or snowdrifts are alternatives, not things to add together. Avoid assuming a waterfall or forest.

## Scene configurations that must NOT be hard-coded into core prompts
- Environment type, named landmarks or asset families; use detected/approved `feature_id` values.
- Camera pitch, orthographic/perspective projection, exact number of cameras, aspect ratio or horizon policy.
- World bounds, physical scale, coordinate axes, handedness and unit conventions without explicit target context.
- Gameplay navigation, player size, slope limits, collision or a particular engine if the goal is art only.
- One style (painterly/realistic/low-poly/etc.), daytime lighting, texture set, weather or vegetation.
- Any image-to-3D service, commercial credit usage or previously generated source model.

## Reusable profile structure
An approved scene profile should record: `project_id`, `scene_type` (user-derived), `goal`, `inputs` with provenance, `style`, `space_and_scale`, `camera_shots`, `geometry_priority`, `conditional_systems`, `deliverables`, `qa_gates`, and `unresolved_assumptions`. Use `docs/SCENE_PROFILE_TEMPLATE.md` as a blank checklist; do not pre-populate from the examples unless the user chooses them.
