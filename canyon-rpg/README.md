# Canyon RPG — Art-First Environment Pipeline

This project prioritizes **natural, stylized 3D environment art**. Default route:

P0-A (source image + optional user-supplied Tripo small-model spatial clues) → P0-B (terrain/water/slope/camera art blueprint) → **P1-concept (Blender editable clay blockout + three locked camera renders)** → P2 (visual slice/lookdev) → P3 (modular assets) → P4 (procedural environment assembly) → P5 (visual + engine QA).

**P1-playable is an optional branch** after P1-concept approval: Godot physical routes, collision, stairs/bridges, navigation and actual player traversal. Do not gate art progression on physical walking tests. Never reshape all cliffs to meet an optional road slope ceiling.

See prompts/en/P0.md, prompts/en/P1.md and bilingual prompts/zh/ counterparts. The generic P0 prompt is image-led and provider-neutral, with Tripo small-model input optional; old provider-specific spatial reconstruction is archived separately as prompts/en/P0-A-marble.md and should only be used when explicitly selected.

Existing 2026-10-26 P0 files under blueprint/ and reports/ are **historical authored design candidates**: 17/17 numeric checks only, not playable/art-approved geometry. Preserve previous landmark evidence and version changes. Real source image: assets/worlds/canyon-waterfall/canyon-waterfall-reference.jpeg. Do not mistake a small model or historical candidate mesh for measured terrain.

Useful references: AGENTS.md, skills/godot-canyon-pipeline/SKILL.md and reference/canitcode/AGENT_INDEX.md. The Can It Code transcript corpus is source material; verify important details against originals.

## New model-driven art QA references
- [Environment modeling guide](docs/ENVIRONMENT_ART_MODELING_GUIDE.md): adapted three-level shape gates, source-image geometry constraints, stable art IDs, incremental Blender corrections, GN asset distribution and honest camera QA.
- [Reference geometry contract example](blueprint/reference_geometry_contract.example.json) and [offline structural validator](blueprint/validate_reference_geometry_contract.py). Example values/camera targets are **not** approved design.
- [Scoped Blender mesh replacement helper](blender/scripts/art_idempotent_geometry.py) and [landmark camera projection validator](blender/scripts/p1_visual_layout_validator.py) for an actually built Blender scene.
- [Regression tests](tests/test_reference_geometry_contract.py): run from canyon-rpg with python -m unittest discover -s tests -v.
No new canyon geometry, approved Blender render or Godot traversal is implied by committing tools/prompts; prior evidence remains unchanged.
