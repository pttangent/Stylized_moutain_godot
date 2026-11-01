# Universal Blender-first scene-art workflow

**This branch is deliberately scene-agnostic.** It generalizes the P0–P5 art-production prompts and reference-to-geometry tools. Existing project data in this folder was produced for an earlier specific scene; it is retained for provenance and must not become default input to a new request.

Start with `docs/UNIVERSAL_WORKFLOW.md` and `docs/SCENE_PROFILE_TEMPLATE.md`, then use `prompts/zh/` or `prompts/en/`. Optional scenario references are in `docs/SCENE_TYPE_EXAMPLES.md` (interior, exterior built scene, city, wilderness and other cases); **select them explicitly** rather than allowing an agent to import them silently.

Production routing: 00 input inspection -> P0 evidence/blueprint -> **P1-concept actual editable Blender blockout** -> P2 style/lookdev -> P3 assets -> P4 conditional systems/scene assembly -> P5 visual and technical QA. P1-playable is an optional runtime adaptation only when requested.

Core prompts do **not** assume the existence of a heightfield, a specific terrain type, vegetation, a building, flow simulation, path navigation, a **presentation** camera angle, a renderer or a target game engine. They preserve stable art IDs and revision history, evaluate visual results through genuinely captured approved views, and mark unavailable tests honestly.

Technical entrypoints:
- `docs/REFERENCE_GEOMETRY_CONTRACT.md` — v2 source-agnostic contract spec
- `blueprint/reference_geometry_contract.example.json` — **neutral unapproved** schema example
- `blueprint/validate_reference_geometry_contract.py` — v1 legacy + v2 structural validation
- `blender/scripts/p1_visual_layout_validator.py` — v1/v2 actual Blender anchor/view diagnostic
- `blender/scripts/ensure_qa_45_camera.py` — create, render and lock the universal fixed 45° engineering QA camera
- `docs/QA_CAMERA_45_STANDARD.md` — distinguish QA visibility from final presentation framing
- `blender/scripts/art_idempotent_geometry.py` — scoped mesh replacement
- `tests/test_reference_geometry_contract.py` — structural regression tests

Historical special-case instructions are under `prompts/legacy/`; do not run them by default. Historical project-specific analysis, geometry, generators and reports under `blueprint/`, `analysis/` and `reports/` have not been reapproved for arbitrary scenes.

Run tests from this project folder with `python -m unittest discover -s tests -p 'test_reference_geometry_contract.py' -v`. These tests prove structural behavior only, not geometry or art approval.

**Important constant:** regardless of the scene category, a real P1 Blender blockout is inspected from locked `CAM_QA_45` at 45° elevation. Only the *final presentation camera* remains unrestricted; a QA render alone never certifies full visual quality.
