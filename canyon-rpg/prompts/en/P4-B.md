# P4-B — Assemble the approved scene without content assumptions

Role: Blender/environment-scene assembly engineer, plus runtime integration only if selected in the scene profile.

1. Read the approved scene profile, P0/P1/P2 geometry/style gates, asset inventory, optional P4-A systems and **actual** review-view specification. Never add objects or scene types because they appear in examples.
2. Preserve scene composition, feature IDs, coordinate/scale conventions and camera approvals. Assemble assets with authored placement or procedural rules as the actual geometry needs.
3. When instancing/scattering is warranted, create deterministic source and placement rules using only relevant masks or constraints (e.g. visibility, attachment, hierarchy, region, spacing or material-specific conditions). Do not impose one universal density/terrain/biome logic.
4. Keep scene source assets editable and instance manifests reproducible. Prefer a limited set of prototypes; avoid global `Realize Instances` unless demonstrated necessary for export or effect.
5. Use a scoped `change_scope` ledger: affected IDs, generator version, seed, dependencies and views. An edit to one feature must not implicitly rebuild unrelated approved assets.
6. Validate actual scene relationship, visible grounding, attachment/overlap, boundaries, procedural determinism, materials and any defined conditional system. Interaction/collision tests are required **only** if the optional P1-playable branch was chosen.
7. Produce real captures at the chosen review views in the selected renderer. If exporting to another engine, verify import, coordinate conversion, material changes and source preservation; do not infer success from file existence.
8. Report geometry/instance measures and hardware render performance only if observed. Preserve before/after visual evidence for modifications.

Deliver editable scene, deterministic generation or assembly data, actual preview captures, applicable system integrations and reports/P4B_assembly.md.
