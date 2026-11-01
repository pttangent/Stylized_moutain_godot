# P0-A — Optional Small 3D Reference Branch (GENERAL)

This add-on augments P0-A.md only when the user **actually provides** a small generative model, such as a Tripo GLB/OBJ/FBX. It is optional and provider-agnostic, never a mandatory source of metric truth.

1. Inspect the original image, user-approved annotations and actual supplied asset path/hash/license/source. If absent, mark MODEL_UNAVAILABLE and continue image-only.
2. Open the mesh in an inspection scene and record mesh structure, disconnected pieces, sky/background shells, normals, transforms, raw up and forward directions, scale, coordinate handedness and visible defects. Keep raw values; apply authored transforms only once.
3. Produce reproducible top/front/side and elevated oblique diagnostic views with grid and source IDs. Compare silhouette, apparent depth order, major structures and unknown hidden geometry with original reference.
4. Treat topmost surface, triangulated faces and model "collision" as **candidate geometry**. Canopies, water, branches, vertical cliff faces and scenery cannot be assumed to be ground. Mark all semantic labels unverified until reviewed.
5. When practical, rasterize **candidate** min/max surface layers, NoData validity/coverage and exact up-facing face-normal filtering; raw-unit measurements and designer-selected meter-scale views must stay separate. Never fill holes silently.
6. Source-image ↔ model registration may be attempted only with enough geographically distributed **visually confirmed** 2D↔3D correspondences. Report reprojection residuals and failures. Do not claim a successful image fit or depth measurement from unreviewed ray hits.
7. Build explicit disagreements and confidence records (IMAGE_OBSERVATION / MODEL_CANDIDATE / AUTHOR_DESIGN / UNKNOWN); original image wins for visible art intent. No assumption that generated model dimensions are physical meters.
8. Deliver dated manifest, reproducible inspection generator, diagnostic 3D views, optional candidate elevation/coverage maps, input hashes and conservative conclusion. Do not overwrite approved blueprint or spend model credits.
