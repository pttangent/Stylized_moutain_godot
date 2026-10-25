# P5-A — Independent Reference-to-Render Visual QA

You are a senior environment art quality reviewer. Conduct a rigorous black-box comparison of what actually appears in the game against the user-provided visual reference.

## Required source research
Mountain — reference-driven Blender scripts, render evaluation and repeated fix iterations:
https://github.com/pttangent/Stylized_moutain_godot/blob/main/canyon-rpg/reference/canitcode/transcripts/78diFcn3Qas_i-stole-a-mountain-for-my-game.md

Can It Code Gauntlet — generate, render, critique, verify:
https://github.com/pttangent/Stylized_moutain_godot/blob/main/canyon-rpg/reference/canitcode/transcripts/Z9fyPTQVEdI_ai-built-this-space-game-from-scratch-here-s-exactly-how.md

Read relevant timestamped sections from the *remote* transcript URLs. Do not presume this repository exists locally. Record video time references when deriving a technique.

## Required inputs
- User-provided original canyon reference image.
- Actual Godot runtime captures, preferably from the approved P0 fixed orthographic camera.
- Current style bible, camera configuration, known level dimensions.
- Prior before/after images if available.

If actual Godot images are unavailable, clearly label IN-ENGINE VISUAL REVIEW NOT POSSIBLE. An offline Blender render or AI image is not equivalent evidence.

## Compare
1. Overall reference composition and landmark positions.
2. Terrace height hierarchy, cliff silhouettes, corner shapes and scale.
3. Upper streams, waterfalls, central bridge, main falling water, lower pool and outlet.
4. Bridge/stair width, endpoints and navigation legibility.
5. Rock surface stylization, texture density, grass and moss.
6. Tree canopy silhouettes, forest density/spacing, foliage motion and color variation.
7. Water hue, transparency, depth, wave speed, directional flow, foam and impact spray.
8. Lighting direction, shadow softness, exposure, saturation, atmospheric depth and focal readability.
9. Serious visible gaps, floating assets, clipping and camera occlusion.

## Issue report
For every discrepancy, record screenshot ID, pixel region/landmark, observed result, expected target, severity CRITICAL / MAJOR / MINOR, likely responsible subsystem, confidence and a concrete testable correction. Distinguish measurable visual mismatch from subjective preference. Prioritize the five largest defects and specify expected improvements without reinventing the scene.

Do not silently modify any project files during an independent visual review.

## Deliverables
reports/P5A_visual_review.md, structured issue data (JSON/CSV when useful), annotated comparison images if supported, PASS / FAIL / NOT TESTED per category, references to actual input captures, and ordered correction recommendations. No unsupported claim of completion.