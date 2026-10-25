# Canyon RPG Project Status

**Audit date:** 2026-10-26
**Task:** 00 — initialize and audit
**Current state (updated 2026-10-26):** P0-B design blueprint generated and numerically validated; pending user P0 approval and P1 runtime physics. The remainder of this document records the earlier Task 00 audit unless superseded below.

## P0 update — 2026-10-26

Marble 1.1 user-reviewed anchors were converted into a 96 × 120 m Godot Y-up design blueprint under `blueprint/`. See [`P0_report.md`](P0_report.md), the actual 16-bit heightmap, water/navigation graphs, camera and cliff edges. P0 numerical design validation: 17 PASS / 0 FAIL. Godot 4.7.2 project import and empty-scene startup passed; no P0 rendered screenshot, NavMesh bake or CharacterBody3D traversal was performed. P1 has not started and awaits user approval. The old audit inventory and gate table below describe the state before this P0 work.

## Repository audit

- Canonical repository: [`pttangent/Stylized_moutain_godot`](https://github.com/pttangent/Stylized_moutain_godot)
- Remote base commit: `7d16e2ab61712bf0af5af3ded66332ca741b3391` (`main`)
- Working branch: `codex/task-00-initialize-audit` (local; not pushed)
- The provided workspace was not a Git checkout. Its existing Godot config and icon were preserved and moved into the repository's documented `canyon-rpg/` project directory. The upstream repository files were kept intact.
- Upstream provides project instructions, bilingual phase prompts, a Can It Code transcript corpus, indexes and search/validation scripts. It does not include the canyon reference image, a Godot runtime scene, or the art-production folders.
- `AGENTS.md` and `skills/godot-canyon-pipeline/SKILL.md` are present and were read. No `CLAUDE.md` was found. The instructions require phase-gated work, evidence-backed reports, and no automatic advancement between phases.

## Scaffold inventory

| Path | State |
|---|---|
| `reference/` | Present; includes `canitcode/`. **`reference/canyon_reference.png` is missing** from both the workspace and upstream repository. |
| `blueprint/` | Present; empty placeholder only. |
| `blender/scripts/` | Present; no generators yet. |
| `assets/` | Present; no generated assets yet. |
| `godot/` | Present; contains a minimal `main.tscn` startup root. |
| `tests/` | Present; no test suite yet. |
| `reports/` | Present; contains this audit. |
| `prompts/` | Present; upstream English and Chinese P0–P5 prompts preserved. |

The existing `project.godot` is retained at the `canyon-rpg/` root and now points to `res://godot/main.tscn`. No P0 map, terrain, water graph, level geometry, or reference substitute was created.

## Godot project validation

| Check | Result | Evidence |
|---|---|---|
| Godot availability | **Verified** — Godot 4.7.2 stable | `/Users/freeai/Downloads/Godot.app/Contents/MacOS/Godot --version` |
| Existing project import | **Passed** | `Godot --headless --editor --path . --quit` completed with exit code 0 before relocation. |
| Existing project startup | **Failed as found** | `Godot --headless --path . --quit` reported that no main scene was defined. |
| Scaffold import | **Passed** | `Godot --headless --editor --path canyon-rpg --quit` completed with exit code 0 and imported `icon.svg`. |
| Scaffold runtime smoke check | **Passed** | `Godot --headless --path canyon-rpg --quit-after 2` completed with exit code 0. This validates startup only; it is not a P0 gameplay test. |
| P0–P5 acceptance tests | **Not run** | No phase content exists yet. No unexecuted test is marked passed. |

The Godot MCP server was discoverable, but its editor bridge reported disconnected. The Godot command-line editor/runtime worked directly, so MCP was not needed for this audit.

## Tool availability and role assignment

| Tool | Availability in this environment | Assigned project role |
|---|---|---|
| **Codex** | Available in the current desktop session. | Blender Python asset production, geometry validation and automated tests. |
| **Godot 4** | Available as Godot 4.7.2 stable at `/Users/freeai/Downloads/Godot.app/Contents/MacOS/Godot`; headless editor import and runtime smoke check succeeded. | Runtime target and project validation. |
| **Blender** | Available at `/Applications/Blender.app/Contents/MacOS/Blender`; version **5.4.0 Alpha**. Background Python smoke check succeeded. This is a prerelease build. | Editable `.blend` sources, scripted geometry and independent GLB exports. |
| **Claude Code** | Claude desktop app is installed, but a `claude` CLI was not found on `PATH`; Claude Code execution was not independently verified. | Godot implementation, runtime systems, shaders and integration. |
| **Gemini 4 Argon** | No local CLI or connected Gemini tool was detected. | Spatial planning and independent visual critique. |
| **Tripo3D** | No local CLI or connected Tripo tool was detected. Studio account/credit balance is **unverified**. No credit-consuming operation was run. | Selected standalone decorative objects only, after live availability and credit approval are verified. |

Godot uses Y-up and 1 world unit = 1 meter. Asset dimensions, pivots, connectors, collision and atlas conventions will be recorded in manifests when asset work begins. Editable Blender sources and generator scripts will be kept alongside independent GLB exports and Godot scenes.

## Can It Code workflow anchors

The supplied transcript corpus is identified by its own provenance file as user-provided, automatically/derivatively transcribed material. Treat it as workflow evidence to check against original footage, not as authoritative technical documentation. No technique was implemented during Task 00.

- **Cyberpunk City / P0–P1:** [transcript](https://github.com/pttangent/Stylized_moutain_godot/blob/main/canyon-rpg/reference/canitcode/transcripts/XqtnBlPJ6KE_is-this-really-ai-insane-opus-5-5-gamedev-workflow.md), especially [01:34 top-down plan and scale check](https://www.youtube.com/watch?v=XqtnBlPJ6KE&t=94s) and [02:06 asset approach comparison](https://www.youtube.com/watch?v=XqtnBlPJ6KE&t=126s). Apply as a measured playable layout and geometric blockout before detailed art.
- **Mountain / P1–P4:** [transcript](https://github.com/pttangent/Stylized_moutain_godot/blob/main/canyon-rpg/reference/canitcode/transcripts/78diFcn3Qas_i-stole-a-mountain-for-my-game.md), including [01:03 Blender Python and render critique loop](https://www.youtube.com/watch?v=78diFcn3Qas&t=63s), [03:55 spline-driven path](https://www.youtube.com/watch?v=78diFcn3Qas&t=235s), [04:31 offline water-flow data](https://www.youtube.com/watch?v=78diFcn3Qas&t=271s), and [05:27 separate waterfall treatment](https://www.youtube.com/watch?v=78diFcn3Qas&t=327s). Adapt these to a fictional canyon; real DEM data is not a prerequisite.
- **Modular Village / P2–P3:** [transcript](https://github.com/pttangent/Stylized_moutain_godot/blob/main/canyon-rpg/reference/canitcode/transcripts/57QEdTgUC3c_stop-asking-ai-for-whole-houses-opus-5-5-tripo.md), including [01:58 front/side views](https://www.youtube.com/watch?v=57QEdTgUC3c&t=118s), [05:12 character-clearance testing](https://www.youtube.com/watch?v=57QEdTgUC3c&t=312s), and [06:32 shared texture atlas](https://www.youtube.com/watch?v=57QEdTgUC3c&t=392s). Adapt as dimensioned, reusable modules with tested connectors, pivots, collision and UVs.
- **Gauntlet / P2 and P5:** generate a limited slice, render it in Godot, have an independent critic inspect the actual capture, fix named issues, and rerender. No render or performance claim is made in this audit.

## P0–P5 acceptance gates

All phase gates remain open. Acceptance criteria below are summarized from the preserved `prompts/en/P0.md`–`P5.md` and `AGENTS.md`.

| Gate | Acceptance evidence | Status |
|---|---|---|
| **P0 — Scene blueprint** | Metric top-down plan plus `scene_blueprint.json`, layout image, true 16-bit heightmap, cliff edges, water and navigation graphs, camera definition and consistency checks; report assumptions and pass/fail. | **Not started.** Reference image missing; no blueprint content generated. |
| **P1 — Playable blockout** | Approved P0 input; editable Blender generator/source and exported terrain/cliff/river/fall/bridge/stair assets; Godot blockout; CharacterBody3D traversal, collision and route tests; screenshots and report. | **Not started.** Depends on P0 approval. |
| **P2 — Visual slice** | Limited central waterfall/bridge/cliff/river/vegetation slice; Godot captures, shader and Blender sources; independent critique/fix/verification loop and report. | **Not started.** |
| **P3 — Modular kit** | Dimensioned module manifest, stable IDs/pivots/connectors/collision/UVs, separate GLBs, Blender sources, atlas, fit/collision checks and report. | **Not started.** |
| **P4 — Procedural assembly** | Reproducible seeded assembly, spline paths, offline flow cache, placement rules, clear traversable routes, collision/navigation checks and report. | **Not started.** |
| **P5 — Lookdev and QA** | Locked-camera Godot captures plus traversal views, independent visual-diff critique, reproducible performance metrics, license review and final pass/fail report. | **Not started.** |

## Open prerequisites and limits

1. Supply or locate `reference/canyon_reference.png` before P0 analysis. The audit did not fabricate a replacement.
2. Blender is currently an Alpha build. Recheck the production Blender version before committing generated assets.
3. Confirm Gemini and Claude Code execution paths before assigning work to those tools. Tripo Studio access and current credits must be verified before any use.
4. Transcript metadata and automatic transcriptions may be inaccurate; verify important claims against original videos and retain source/license notes.
