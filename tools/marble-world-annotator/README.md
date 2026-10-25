# Marble World Annotator

Local browser tool for comparing the reference image with the Marble Gaussian splat and collider, then recording candidate 2D↔3D landmark pairs.

## Start

From the repository root:

```bash
python3 -m http.server 8765 --bind 127.0.0.1
```

Open <http://127.0.0.1:8765/tools/marble-world-annotator/>. On macOS, `serve.command` starts the same loopback-only server from the project folder.

The page loads the project’s reference image, original 100k SPZ, and collider GLB by default. It uses Spark's native Gaussian renderer and Three.js `GLTFLoader`. You can also drag an image into the left pane, or drag an `.spz`, `.glb`, or prior annotation JSON into the right pane. The file pickers provide the same flow.

The default `flip_y=true` display transform rotates one shared parent group by 180° about X, keeping SPZ and collider aligned. The flip button changes both layers together; exported picks are transformed back to raw GLB XYZ, and the export records the display matrix. This follows Image-Blaster's default orientation and does not establish meter scale. Use **Core 100k/150k** for an optional near-collider visual diagnostic. These proximity-filtered variants can exclude valid background detail and are not terrain masks or collision data.

## Pair landmarks

1. Select an existing approximate source-image landmark or add a new ID.
2. Click its visible image pixel on the left.
3. Orbit the raw collider on the right and click the corresponding mesh surface.
4. Add a note and mark **我已人工核對目前配對** only after checking the cross-view match.
5. Export `paired_landmarks.json` and review each pair before using it for camera fitting.

The JSON records raw GLB XYZ, face index, image pixel, annotation source, notes, and whether a human explicitly reviewed the pair. Raw ray hits do not carry terrain/water/cliff semantics. The page keeps `up_axis` and metric scale unset and does not promote the P0 gate.

The viewer uses Three.js and Spark modules from pinned public CDNs; an internet connection is needed for those modules. The image, SPZ, GLB, and annotation files remain local in the browser. It does not use a World Labs API key or make generation requests.
