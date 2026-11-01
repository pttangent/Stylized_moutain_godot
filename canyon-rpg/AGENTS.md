# Shared agent contract — scene-agnostic art pipeline

**Purpose:** build reusable 3D scene art from the user's actual brief, references and approved constraints, without hard-coded scene class, style, geometry, **presentation camera** or engine. A fixed 45° engineering QA view is required for actual Blender blockouts. See `docs/UNIVERSAL_WORKFLOW.md` and `skills/universal-scene-art-pipeline/SKILL.md`.

## Read order
1. Current user task and actual inputs/connected project assets.
2. `docs/SCENE_PROFILE_TEMPLATE.md` and applicable approved `scene_profile.json`.
3. The selected **universal** phase prompt under `prompts/en/` or `prompts/zh/`.
4. Applicable scene-specific data ONLY when user-selected. `docs/SCENE_TYPE_EXAMPLES.md` illustrates options; it does not impose content. `prompts/legacy/` is opt-in historical material.

## Default routing
00 -> P0-A/P0-B -> **P1-concept in Blender (default)** -> P2 -> P3 -> P4 -> P5. **P1-playable is optional** and must not gate art progression. P4-A may be legitimately NOT_APPLICABLE if no procedural/simulation system is required.

## Requirements
- Preserve source evidence, feature IDs, known approvals and uncertainty. Do not treat old repository folders/artefacts as defaults for new projects.
- Derive scale, axes, world units, **presentation** camera count/angle/projection, visual style and scene objects from actual inputs. **Exception:** the standardized `CAM_QA_45` diagnostic is always 45° elevated, orthographic, and locked once framed to S1 Blender geometry.
- Use `docs/REFERENCE_GEOMETRY_CONTRACT.md` v2 for source-to-geometry constraints, `docs/ENVIRONMENT_ART_MODELING_GUIDE.md` for S1/S2/S3 build discipline, stable Blender art IDs and scope-limited changes.
- Validate JSON with `blueprint/validate_reference_geometry_contract.py` and semantic anchor projections with `blender/scripts/p1_visual_layout_validator.py` only when relevant; real scene approvals need actual renders, not those diagnostics.
- Use editable Blender sources for P1-concept and reproducible scripts when beneficial. Select output/render engine only when specified. Every external or paid generation action needs explicit authorization.
- Use geometry/instancing/simulation methods only when they fit the scene; skip irrelevant data rather than inventing systems.
- Report exact commands, real outputs, source/licensing, errors, revisions and PASS/FAIL/ASSUMED/NOT_RUN/NOT_APPLICABLE. Never claim unseen screenshots, physics runs, renderer results or benchmark measurements.

The pre-existing scene example inside this repository remains historical material unless the user explicitly selects it.

## Mandatory fixed 45° view

Every real Blender P1-concept scene builds and renders `CAM_QA_45` using `blender/scripts/ensure_qa_45_camera.py`. Preserve its transform, yaw, scale and output ratio as a versioned engineering baseline for before/after structural comparison. This is **not** the final/hero camera. Additional views are required where the fixed view hides geometry; see `docs/QA_CAMERA_45_STANDARD.md`. Continue using actual approved presentation shots for artistic acceptance.
