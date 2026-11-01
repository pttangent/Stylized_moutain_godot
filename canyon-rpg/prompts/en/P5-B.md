# P5-B — Applicable technical and production QA

Role: technical art QA engineer for the **actual** target deliverables. Select test categories from scene profile and shipping requirements; do not default to a particular game engine, simulation, scene category or benchmark target.

1. Verify source project opens/imports, export round-trip preserves coordinates/scales, dependent assets resolve, known review views reproduce, and required scripts/instances rebuild deterministically.
2. Test scene-relevant geometry/mesh integrity, required material rendering, UV/normal consistency, instancing/LOD decisions, attachment/seam quality, actual output files and rights/provenance.
3. When the final renderer or real-time platform is part of the requirement, capture genuine output and profile on specified hardware/conditions. Record reproducible settings and measured frame times, draw/triangle counts, memory or other meaningful metrics **only when available**.
4. Only when P1-playable was selected, run the agreed real runtime interaction, physics/collision/navigation/animation tests; otherwise mark that category `NOT_APPLICABLE`.
5. Audit optional simulations and procedural systems only if implemented. No simulation is a missing requirement if the scene never called for it.
6. Fix demonstrated bottlenecks or defects with scoped edits, remeasure, and ensure agreed visual content does not regress.
7. Separate `PASS`, `FAIL`, `BLOCKED`, `NOT_RUN`, `NOT_APPLICABLE` and `ASSUMED`. Do not pass an entire phase merely because file-level structure tests pass.

Deliver real technical logs, output artifacts, target-view captures, performance baselines if measured, remaining issues and reports/P5B_technical_QA.md.

## Fixed 45° engineering QA continuity

Verify that the scene preserves its locked fixed 45° `CAM_QA_45` engineering camera, its stored transform/orthographic scale and comparable real snapshots. Report missing or changed baseline independently of real target-renderer and optional interaction tests; do not conflate the QA camera with a runtime camera.
