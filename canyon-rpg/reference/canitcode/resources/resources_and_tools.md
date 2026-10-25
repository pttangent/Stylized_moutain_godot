# Can It Code? (@CanItCode) — Extracted Tools, Workflows & Resources Catalog

## 1. Channel Overview

- **Channel Name**: Can It Code?
- **Handle**: @CanItCode
- **Channel Id**: UC1nYVdCZZr7XgeKlXEXAIww
- **Url**: https://www.youtube.com/@CanItCode
- **Subscribers**: 17.2K+
- **Total Indexed Videos**: 33
- **Creator Background**: Polish AI game developer building a commercial stylized survival game set in the Polish Beskids mountains for Steam alongside his brother (who runs the companion channel 'AI Dev Challenge'), while running rigorous head-to-head AI coding & 3D game-building benchmarks.

## 2. Core Game Engines & 3D Pipeline

### Godot Engine 4.x (with Jolt Physics)
- **Role**: Primary game engine across 95% of videos
- **Workflow Notes**: Agents edit plain-text .tscn, .gd, and .gdshader files directly without an MCP server. Uses Godot Jolt physics for shatterable glass, destructible shelves, and 1,700-beam BeamNG vehicle destruction, plus MultiMesh for 1,600-unit armies and forest foliage.
- **URL**: https://godotengine.org/

### Blender (Headless Python Scripting + Gauntlet Loop)
- **Role**: Procedural 3D modeling, UV unwrapping, decimation, rigging & animation retargeting
- **Workflow Notes**: Instead of interactive Blender MCP clicking, AI agents write standalone Python scripts executed via headless Blender CLI. Uses the 'Gauntlet Loop': a Builder Agent generates the mesh, renders multi-angle previews, an independent Critic Agent inspects the renders against the reference image + Color Bible, and a numeric validator checks exact bounding-box dimensions.
- **URL**: https://www.blender.org/

### Unreal Engine 5
- **Role**: Used in latest monster/Griffin animation showcase & early horror tests
- **Workflow Notes**: Used to test the retargeted Griffin locomotion/takeoff/flight animations in 'I Tested 9 AI Video Models for Game Animation. Most Failed'.
- **URL**: https://www.unrealengine.com/

## 3. AI 3D Asset & Animation Tools

### Tripo 3D (Smart Mesh 2.0 / P2.0 & Tripo CLI)
- **Role**: AI 3D asset & character generation from multi-view orthographic drawings
- **Workflow Notes**: Best results achieved by having GPT-6 Astra draw front + side + mirrored-side orthographic views on a dark background, generating quad-topology meshes in Tripo P2.0, unwrapping with Smart UV, and repacking into shared Texture Atlases. Automated via Tripo CLI with single-submission credit locks.
- **URL**: https://www.tripo3d.ai/

### NVIDIA Kimodo (Open-Source Text-to-Motion)
- **Role**: Free humanoid character animation generation from single-sentence prompts & path constraints
- **Workflow Notes**: Trained on 700+ hours of real optical mocap. Exports BVH and NPZ bone rotations. Retargeted to custom Mixamo/Tripo rigs via a 5-step Blender Python script (<3° bone error).
- **URL**: https://github.com/NVlabs/kimodo

### Custom 2-Camera AI Video Motion Capture Pipeline (UniRig + Meta DINO + Seedance/MiniMax/Wan/Kling)
- **Role**: Animating arbitrary non-humanoid monsters (Griffin, Troll, Lizard, Wraith, Deer, Bear, Hare, Pheasant)
- **Workflow Notes**: 1) Auto-rig 3D model with UniRig + geometric symmetry validator; 2) Render 3,000 synthetic blurred poses from front+side cameras to fine-tune Meta DINO (30 mins on GPU); 3) Render front+side composite frame of monster and animate in Seedance 2.0/2.5 or MiniMax on Higgsfield; 4) Triangulate 2D DINO joint detections into 3D bone rotations.
- **URL**: https://higgsfield.ai/

### Meshy AI
- **Role**: Character & Uruk-hai 3D mesh generation with polycount control
- **Workflow Notes**: Used in 'Stop Asking AI To Build The Whole Game At Once' (8k poly snow survivor) and 'I Asked Two AIs to Rebuild Helm's Deep' (<4k poly Uruk-hai).
- **URL**: https://www.meshy.ai/

### CMU Motion Capture Database & Adobe Mixamo
- **Role**: Free human motion capture libraries (BVH/FBX)
- **Workflow Notes**: Used for log-carrying shoulder animations, archery retargeting, and harbor character locomotion.
- **URL**: https://mocap.cs.cmu.edu/

### Tezana AI (Prompt-to-Godot Prototype Generator)
- **Role**: Sponsored benchmark comparison against custom Opus 5 workflow
- **Workflow Notes**: Generates playable Godot prototypes in 20–30 minutes and exports full Godot projects for local agent continuation.
- **URL**: https://www.youtube.com/watch?v=upEVSdEb0lA

## 4. AI Coding Models Benchmarked

### Claude Opus 5.5 / Opus 5 / Sonnet 5.5 / Fable 5.1 / Fable 5 (via Claude Code in VS Code)
- **Role**: Primary orchestrator, GDScript mechanics engineer, and headless Blender coder
- **Workflow Notes**: Consistently top-ranked on complex physics (1,700-beam BeamNG car destruction, shallow-water river solver, snow physics, custom DINO animation tool) and atmospheric lighting.

### OpenAI GPT-6 Astra / GPT-6.1 Sol / GPT-5.6 Sol (via Codex CLI / VS Code Extension)
- **Role**: Concept art / orthographic reference generator, texture synthesis, and co-developer on the Steam survival game
- **Workflow Notes**: GPT-6 Astra excels at generating front/side orthographic reference sheets, seamless concrete/tile textures, and long-session building mechanics (floor/wall/window axe-cutting).

### Kimi K3, Grok 4.5, GLM
- **Role**: Benchmarked in multi-model elimination tournaments and classic game rebuilds
- **Workflow Notes**: Kimi K3 noted for strong visual aesthetics at 5x lower API cost than Opus 5, though weaker on complex 3D physics.

## 5. External Datasets & Project Sources

- **Poland Geoportal (DEM Elevation Data) & OpenStreetMap** (Real-world 8x8 km Beskids mountain heightmaps (2.5 MB grid) and road/river splines) — https://mapy.geoportal.gov.pl/
- **PolyHaven, Sketchfab (CC Attribution), Pixabay Audio** (Free PBR textures, CC-licensed base meshes for decimation tests, and royalty-free sound effects) — https://polyhaven.com/
- **Can It Code? Patreon & Companion Channel (AI Dev Challenge)** (Downloadable Godot/Blender source projects (Dungeon kit, Swamp Village kit, Cyberpunk City, BeamNG Accord crash project) and co-op Steam survival devlogs) — https://www.youtube.com/@CanItCode
