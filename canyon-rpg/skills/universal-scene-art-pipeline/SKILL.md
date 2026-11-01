---
name: universal-scene-art-pipeline
description: Scene-agnostic Blender-first visual environment and spatial-art production. Use for evidence-led scene understanding, geometry contracts, editable art blockouts, selective modeling systems, assets, assembly and visual/technical QA, with optional playable adaptation.
---

# Universal scene-art pipeline

Read `canyon-rpg/AGENTS.md` and `canyon-rpg/docs/UNIVERSAL_WORKFLOW.md`. This is reusable for arbitrary scene content; never presume a setting, prop family, biome, camera view, scale, rendering style, physics or engine.

P0: inspect real references, produce `scene_profile.json` and v2 reference-to-geometry contract based on source provenance and actual features; choose only applicable spatial representations. P1-concept: Blender first, generate editable real 3D S1 composition and S2 structural geometry, with S3 detail deferred if unnecessary. Use approved scene-specific cameras/views, not universal camera constants. P1-playable: opt-in only, with specific interactive requirements and tests.

P2 derives visual direction from user material. P3 produces truly needed modular/unique assets. P4-A is conditional, and P4-B assembles actual scene content with deterministic revision-scoped changes. P5 uses actual rendered evidence and only applicable technical tests.

Use stable IDs, source preservation and scoped change logs. Contract JSON checks and Blender anchor projections are structural diagnostics, not visual approvals. Only actual renders can pass an art review. No paid third-party generation without authorization.

`docs/SCENE_TYPE_EXAMPLES.md` is illustrative and must never be imported as assumptions. Historical specialists under `prompts/legacy/` are manually selected only. Reporting statuses: PASS, FAIL, BLOCKED, ASSUMED, NOT_RUN, NOT_APPLICABLE.
