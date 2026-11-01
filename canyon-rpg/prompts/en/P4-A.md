# P4-A — Optional procedural systems or derived scene data

Role: scene systems/technical art engineer. **Do not run this task merely because phase P4 exists.** First inspect the scene profile, assets and rendering/interaction targets for a genuine algorithmic or simulation need.

1. Identify the required system, its observed/user-approved behavior, domain, boundary conditions, source data, deterministic parameters and target consumer. Examples from other scenes are not requirements.
2. If no relevant system exists, write a concise `NOT_APPLICABLE` report; do not invent a physical simulation, texture field, route graph or environmental effect.
3. If required, choose the least complex reliable solution: authored data, precomputed fields, node-based procedural generation, keyframed art, simulation or runtime behavior. Justify the representation.
4. Validate units, reference transforms, adjacency/continuity, edge cases, caching/versioning, data ownership and deterministic reruns where relevant. Unknown inputs must remain unknown.
5. Separate artistic approximation from actual physical or interactive simulation; do not use a convincing preview as proof of scientific or runtime correctness.
6. Test with real execution and representative view(s) from the scene profile, reporting costs and failures. Respect external service permissions and preserve previous source data.

Deliver needed generator/cache/parameters, a reproducible contract, actual tests and reports/P4A_systems.md. The P4-B assembly can proceed without this artifact if the task was not applicable.
