# Can It Code — Agent Retrieval Index

This is a **user-provided research extraction**, not an official channel transcript archive. It contains automatic/derived transcriptions; names, numbers, versions and timestamps can be erroneous. **Always inspect the original video for critical claims.** Source authors retain copyright; this repository does not assert redistribution or reuse rights for original material.

## How to use this material (for Codex / Claude Code / Gemini)

1. Read `AGENT_INDEX.md` first, then the three most relevant individual timestamped transcripts.
2. Run `python scripts/search_kb.py "query" -n 15` from this folder to find timestamped transcript lines and visual index entries.
3. Read surrounding transcript lines before extracting a workflow. The auto-generated visual descriptions are **secondary notes**, not screenshots or confirmed footage.
4. Cite the video URL and timestamp in your agent report. Distinguish direct transcript evidence, inference and your recommended implementation.
5. Use `transcripts/index.json` for all 33 metadata entries; full catalog in [README](README.md); [Visual frames timeline](visual_index/visual_frames_timeline.md); [Tool catalog](resources/resources_and_tools.md).
6. If repository searches return nothing (GitHub code search indexing lag), run local script or `rg -n -i 'river|spline|modular' reference/canitcode/transcripts`.

## Core canyon workflows — read these first

### P0–P1: Cyberpunk City — top-down level design to blockout

- [01:34](https://www.youtube.com/watch?v=XqtnBlPJ6KE&t=94s) · [Transcript](transcripts/XqtnBlPJ6KE_is-this-really-ai-insane-opus-5-5-gamedev-workflow.md) — top-down planning and size-checking with simple grid-block streets.
- [02:06](https://www.youtube.com/watch?v=XqtnBlPJ6KE&t=126s) · [Transcript](transcripts/XqtnBlPJ6KE_is-this-really-ai-insane-opus-5-5-gamedev-workflow.md) — compare three asset construction approaches.
- [02:57](https://www.youtube.com/watch?v=XqtnBlPJ6KE&t=177s) · [Transcript](transcripts/XqtnBlPJ6KE_is-this-really-ai-insane-opus-5-5-gamedev-workflow.md) — use Blender geometry and AI-generated material details for repeatable modular architecture; reserve Tripo for select small details.

### P1–P4: Mountain — terrain / roads / river / vegetation

- [01:03](https://www.youtube.com/watch?v=78diFcn3Qas&t=63s) · [Transcript](transcripts/78diFcn3Qas_i-stole-a-mountain-for-my-game.md) — Blender Python executed headlessly; independent render critic and Gauntlet loop.
- [02:54](https://www.youtube.com/watch?v=78diFcn3Qas&t=174s) · [Transcript](transcripts/78diFcn3Qas_i-stole-a-mountain-for-my-game.md) — real DEM/OSM terrain and small test scenes. **Canyon is fictional: do not require real-world DEM.**
- [03:55](https://www.youtube.com/watch?v=78diFcn3Qas&t=235s) · [Transcript](transcripts/78diFcn3Qas_i-stole-a-mountain-for-my-game.md) — follow map route with Godot spline; road mesh repeats and deforms over terrain.
- [04:31](https://www.youtube.com/watch?v=78diFcn3Qas&t=271s) · [Transcript](transcripts/78diFcn3Qas_i-stole-a-mountain-for-my-game.md) — offline riverbed cells storing depth and flow, cached for Godot runtime shader.
- [05:27](https://www.youtube.com/watch?v=78diFcn3Qas&t=327s) · [Transcript](transcripts/78diFcn3Qas_i-stole-a-mountain-for-my-game.md) — waterfall is handled separately from channel flow.

### P2–P3: Modular Village — orthographic assets, sockets and atlases

- [01:58](https://www.youtube.com/watch?v=57QEdTgUC3c&t=118s) · [Transcript](transcripts/57QEdTgUC3c_stop-asking-ai-for-whole-houses-opus-5-5-tripo.md) — front and side references outperform pure text prompts for thick, accurate pieces.
- [05:12](https://www.youtube.com/watch?v=57QEdTgUC3c&t=312s) · [Transcript](transcripts/57QEdTgUC3c_stop-asking-ai-for-whole-houses-opus-5-5-tripo.md) — test final assembly against character dimensions and doorway clearance.
- [06:32](https://www.youtube.com/watch?v=57QEdTgUC3c&t=392s) · [Transcript](transcripts/57QEdTgUC3c_stop-asking-ai-for-whole-houses-opus-5-5-tripo.md) — combine model textures into shared atlases to reduce materials/draw calls.

### P2/P5: Gauntlet and foliage optimization

- [04:45](https://www.youtube.com/watch?v=Z9fyPTQVEdI&t=285s) · [Transcript](transcripts/Z9fyPTQVEdI_ai-built-this-space-game-from-scratch-here-s-exactly-how.md) — orchestrator and render critic, numeric validation and dual testing.
- [03:48](https://www.youtube.com/watch?v=AlMLFkN79dA&t=228s) · [Transcript](transcripts/AlMLFkN79dA_can-ai-build-a-game-good-enough-for-steam.md) — optimize leaf geometry with baked foliage cards.

## Retrieval by production stage

| Phase | Topic | Source videos | Search queries |
|---|---|---|---|
| P0 | Top-down layout and scale | Cyberpunk City, Modular Village | `top down`, `grid blocks`, `door` |
| P1 | Geometry, Blender background execution, playability | Mountain, Cyberpunk City | `python script`, `blender`, `spline` |
| P2 | Materials, waterfall, trees | Cyberpunk City, Mountain | `texture`, `trees`, `waterfalls` |
| P3 | Orthographic modules / texture atlas | Modular Village, Cyberpunk City | `front and side`, `atlas`, `Tripo` |
| P4 | Procedural paths, offline water and foliage | Mountain, River Simulation short | `river`, `flow`, `road`, `forest` |
| P5 | Render critic, performance, test character | Space Game, Mountain, Modular Village | `gauntlet`, `critic`, `test`, `FPS` |

## Validation

Run `python scripts/validate_pack.py` after any metadata or transcript change. The source dataset contains **33 transcript Markdown files, 1,849 timestamped transcript lines, and 20 visual timeline records** (validated from the supplied archive). The `SolVsOpus_Oct03` entry points to an external companion URL rather than a YouTube video; do not synthesize a YouTube link for it.
