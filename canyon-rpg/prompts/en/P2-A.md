# P2-A — Define Stylized Game Art Direction from the Actual World

You are a senior stylized RPG environment art director.

## Source tutorials
Cyberpunk City — apply visual direction to geometric blockouts and test competing looks:
https://github.com/pttangent/Stylized_moutain_godot/blob/main/canyon-rpg/reference/canitcode/transcripts/XqtnBlPJ6KE_is-this-really-ai-insane-opus-5-5-gamedev-workflow.md

Mountain — choose a reference, isolate a single tree on a plain background, iterate silhouette and design:
https://github.com/pttangent/Stylized_moutain_godot/blob/main/canyon-rpg/reference/canitcode/transcripts/78diFcn3Qas_i-stole-a-mountain-for-my-game.md

Read the remote transcripts via available web/HTTP tools. Do not assume the material is checked out locally.

## Inputs
The user-provided canyon reference, approved P1 blockout screenshots if available, validated camera parameters and intended game-engine constraints.

## Art direction
Aim for a bright, peaceful Japanese fantasy RPG scene with a fixed, elevated, near-orthographic exploration camera, turquoise clear river water, layered grey rocky cliffs, warm natural paths and lush but readable foliage. Use Pokémon-like camera readability and Genshin-like painterly game-environment stylization as descriptive references, not literal asset copying. Avoid photorealism, harsh cinematic grading, noisy microdetail and impossible 2D-only rendering tricks.

## Procedure
1. Analyze the original image: color palette, focal hierarchy, silhouette language, cliff shape, foliage density, sunlight direction, water color and atmospheric depth.
2. Create a reproducible style bible: swatches, shape proportions, leaf density, softness, texture scale, shader behaviors, material/lighting constraints.
3. If an approved Godot blockout capture is provided, align art concepts to its exact camera and geometry rather than redesigning the level.
4. Prepare isolated references for at least one broadleaf, conifer and flowering tree, one rock/cliff family and one wooden bridge module.
5. Prepare reference textures for dry rock, wet/mossy rock, earth, grass and wood. They must be neutral-lit, consistent-scale and preferably tileable; do not bake shadows into reusable base color.
6. Generate front, side or top orthographic views only for geometry that needs them. Keep occluded elements labeled inferred.
7. Limit variants until one approved sample proves shape and style consistency.

## Output
reference/style_bible.md, separate visual references or explicit generation prompts, texture specifications, asset target dimensions, and reports/P2A_art_direction.md. When image generation is not available, provide reproducible prompts instead of falsely claiming images were created. Do not produce bulk 3D assets.