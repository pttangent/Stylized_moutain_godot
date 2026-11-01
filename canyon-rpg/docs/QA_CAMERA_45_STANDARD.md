# Fixed 45-degree engineering camera — scene-independent QA standard

**Diagnostic camera ≠ presentation camera.**

For each real Blender P1-concept 3D scene, create one common inspection camera named `CAM_QA_45`: **45° elevation above Blender XY (Z-up)**, orthographic, default 16:9 QA output (1600×900). The initial 45° azimuth is a repeatable engineering seed; it can be chosen differently during initial framing to expose the scene, but must be recorded and then kept fixed. This technical view helps reveal scale, side faces, depth, contacts, and overlap **regardless of scene contents**. It never determines the final artistic, cinematic or interactive camera.

## Lock and compare
1. Once primary S1 blockout geometry exists, auto-fit the actual visible scene geometry in the 45° view with modest margins.
2. **Lock transform, target, yaw, projection, orthographic size and QA output resolution** after capturing the first real baseline.
3. Reuse the **exact same camera** for S2 structural changes and future P2/P3/P4 geometry/assembly revisions; compare authentic before/after images.
4. Reframe only explicitly (new baseline revision with previous values preserved), never because editing a mesh automatically enlarged the scene.
5. Use supplementary side/top/perspective/cutaway/isolated-object views to expose hidden geometry, ceilings, walls or occluded detail. The 45° camera is not sufficient to validate every surface.
6. Presentation/target-renderer view(s) remain entirely source/user-dependent. A single user-facing view, animated camera, game camera or different final projection may coexist.

## Blender helper

`blender/scripts/ensure_qa_45_camera.py` creates and locks a QA-only camera from scene bounds; it refuses to overwrite manually authored camera objects, does not set the final presentation camera, and can take a real diagnostic screenshot. From `canyon-rpg/`:

```bash
blender -b scene.blend --python blender/scripts/ensure_qa_45_camera.py -- \
  --render-out reports/QA_45.png --report reports/QA_45_camera.json --save
```

Use `--force-reframe` only to intentionally create a new baseline. If a scene has no geometry yet, mark camera creation NOT_RUN and first build S1. The script's existence or execution without a saved render does **not** equal art approval.

## Phase gates

- **P0:** record CAM_QA_45 as the planned standardized engineering view; camera transform/screen positions remain unknown until there is geometry.
- **P1-concept:** actual S1 Blender build → construct/capture/lock QA_45 → compare S2 and local changes from identical camera. Final artistic shots are independently selected.
- **P2–P4:** retain locked QA view for geometry/placement comparison, adding other views when necessary.
- **P5:** check the locked 45° view for structural regression and actual user-approved presentation views for artistic fidelity; record uncovered/occluded regions explicitly.
- **Always:** structural, projected-anchor, actual render, runtime, and interactivity checks are distinct. Do not claim one proves another.

**Only the QA 45° elevation and comparable locked framing are universal.** Scene content, style, camera count beyond QA, final camera, physical measurements, modeling technique, render engine and playability are not.
