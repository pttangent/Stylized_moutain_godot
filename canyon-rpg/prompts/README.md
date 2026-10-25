# Portable Canyon RPG Prompts — English / 中文

This folder contains the **complete** runnable prompt set, not brief summaries. All source teaching documents are linked as absolute GitHub URLs. The prompts are reusable in another project and must not assume that any repository has been cloned. Model/agent recommendations are intentionally **outside** the prompt bodies in [Model & Tool Routing (Chinese)](../docs/model_selection_zh.md).

## Read and execute
- [Initial setup — English](en/00.md) | [初始化 — 中文](zh/00.md)
- [P0 Spatial Blueprint — English](en/P0.md) | [P0 空間藍圖 — 中文](zh/P0.md). Split: [P0-A EN](en/P0-A.md), [P0-B EN](en/P0-B.md), [P0-A 中文](zh/P0-A.md), [P0-B 中文](zh/P0-B.md).
- Optional world-model variants for the current Marble project: [P0-A evidence workflow](en/P0-A_world-model-optional.md) and [P0-B blueprint workflow](en/P0-B_world-model-optional.md). P0-A must deliver a reproducible, raw-unit collider surface evidence bundle; P0-B validates and links it, and P1 checks it or generates a clearly labeled supplemental diagnostic. This bundle is candidate geometry only, never a walkability mask. The repository profile points to `assets/worlds/canyon-waterfall/`, reviewed annotations under `analysis/p0_marble_2026-10-26/`, and current `blueprint/` deliverables. The `auto | none | required` world-model modes remain available.
- [P1 Playable Blockout — English](en/P1.md) | [P1 白模 — 中文](zh/P1.md)
- [P2 Visual Slice — English](en/P2.md) | [P2 美術樣板 — 中文](zh/P2.md). Split into P2-A art direction and P2-B engine implementation.
- [P3 Modular Assets — English](en/P3.md) | [P3 模組化資產 — 中文](zh/P3.md). Split into P3-A references and P3-B modeling.
- [P4 Water and Assembly — English](en/P4.md) | [P4 水流與組裝 — 中文](zh/P4.md). Split into P4-A simulation and P4-B world assembly.
- [P5 Visual and Runtime QA — English](en/P5.md) | [P5 視覺／效能驗收 — 中文](zh/P5.md). Split into P5-A visual review and P5-B technical QA.

## Operating rules
1. Copy **one** prompt at a time into the desired coding or image workflow. Assign a model outside the prompt based on [model_selection_zh.md](../docs/model_selection_zh.md).
2. Supply the original reference image, an active workspace and the approved previous-phase artifacts. Each task must check rather than invent missing dependencies.
3. Do not automatically spend credits on third-party model-generation APIs. Verify Studio and API credit differences.
4. External timestamped sources: [Can It Code index](https://github.com/pttangent/Stylized_moutain_godot/blob/main/canyon-rpg/reference/canitcode/AGENT_INDEX.md).
5. Mark unrun tests NOT RUN and do not call a phase complete without evidence.

## Maintenance
The combined files P0, P2, P3, P4 and P5 reproduce their split A/B prompt bodies. When revising a phase, update both the combined stage file and its split files together.
