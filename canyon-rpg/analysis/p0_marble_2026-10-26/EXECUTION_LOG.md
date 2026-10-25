# Execution log

Environment: macOS, Python 3.13 virtual environment `/tmp/canyon-p0-venv`; numpy, scipy, OpenCV headless, trimesh, networkx, Pillow, Matplotlib. Scratch package `/tmp/canyon_marble_p0_review_2026_10_26` was copied from `/Users/freeai/Downloads/marble_p0_handoff` to keep the supplied handoff unchanged.

1. Confirmed `/Users/freeai/Downloads/paired_landmarks.json` and the annotator export at `/Users/freeai/Documents/paired_landmarks.json` were byte-identical; SHA-256 `692736c4b36510974865c2ceaba2bbd2fe9168ea1cb1565cc7cb2e68c6b26224`.
2. Ran `register_camera.py --pairs annotations/paired_landmarks_registration.json --image assets/worlds/canyon-waterfall/canyon-waterfall-reference.jpeg --out registration`; result 23/25 inliers, median 19.2849 px, p90 35.5668 px.
3. Ran `run_p0.py --root /tmp/canyon_marble_p0_review_2026_10_26 --world-mode required --world-dir <project>/assets/worlds/canyon-waterfall --pairs annotations/paired_landmarks_user_reviewed.json`; succeeded, model evidence and raw axis raster candidates written.
4. Ran `raycast_landmarks.py` with registered camera, 27 reference landmarks and project GLB; 27/27 rays hit at least one face.
5. Ran `python -m unittest discover -s /tmp/canyon_marble_p0_review_2026_10_26/tests -v`; 16 tests passed including 6 fault-injection tests.
6. Ran package `validate_p0.py`; exit 1, 35 PASS/1 FAIL (`no_fabricated_3d` stale draft assumption). Stage text also stale.
7. Ran `node --check /tmp/canyon_marble_p0_review_2026_10_26/tests/viewer_module_syntax_only.mjs`; exit 0. Direct `node` execution exit 1 (`ERR_MODULE_NOT_FOUND: three`), as this browser module lacks dependencies in scratch.
8. Ran `analyze_registered_p0.py` and `validate_registered_p0.py`; 11/11 post-annotation structural checks pass; 6/6 measured water links descend.
9. Ran `sample_route_surfaces.py` across 12 navigation and 7 water proposals; 21 samples per complete edge, recording projected triangle heights without walkability approval.
10. Ran `evaluate_topology.py` using clearly marked 3m bridge design hypothesis; candidate metric comparison written. It does not prove continuous walkability.
11. Ran package `check_promotion_gate.py` after recording relative up-axis evidence; exit 2, BLOCKED with 10 unmet conditions.

No World Labs API call or regeneration. No formal P0-B blueprint, Godot scene, navmesh, or detailed 3D model created.
