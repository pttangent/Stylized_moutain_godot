# Blank scene profile and approval checklist

This is a **blank, scene-agnostic authoring template**, not a scene example and not an approved design. Complete only from explicit user input or observed project assets.

```json
{
  "schema_version": 1,
  "project_id": "UNSPECIFIED",
  "goal": "UNSPECIFIED",
  "scene_type": "UNSPECIFIED",
  "style": "UNSPECIFIED",
  "references": [],
  "assets_already_provided": [],
  "space": {
    "coordinate_system": "UNSPECIFIED",
    "units": "UNSPECIFIED",
    "scale_basis": "UNSPECIFIED",
    "bounds": null,
    "spatial_rules": [],
    "unknowns": []
  },
  "target": {
    "authoring_tool": "Blender",
    "renderer": "UNSPECIFIED",
    "runtime_engine": null,
    "interactive": null,
    "delivery_formats": []
  },
  "review_views": [],
  "engineering_qa": {
    "view_id": "CAM_QA_45",
    "role": "DIAGNOSTIC_NOT_PRESENTATION",
    "elevation_degrees": 45,
    "projection": "ORTHOGRAPHIC",
    "resolution": [1600, 900],
    "baseline_status": "NOT_CREATED_UNTIL_S1_GEOMETRY"
  },
  "geometry": {
    "features": [],
    "representation_candidates": [],
    "reusability_rules": []
  },
  "conditional_systems": [],
  "acceptance": {
    "art": [],
    "technical": [],
    "interaction": []
  },
  "exclusions": [],
  "open_questions": []
}
```

## Source resolution

Record each input's path/URL (where actually accessible), timestamp/version/hash when available, source type, license/rights constraints, reliability and whether it is **observed** or **designer-authored**. Optional generated 3D models are `GENERATED_CANDIDATE` until directly inspected and approved. Do not fill scene type, **presentation** camera angles, dimensions or components by copying examples. CAM_QA_45 is an engineering visibility fixture, not an assumed artistic camera.

## Scene representation decisions

List the actual visible or required features with stable IDs. Choose geometry strategy per feature (mesh, curve, volume, procedural node, instance, other), and justify based on view coverage, editability, precision and target platform. Dependencies should not imply non-existent scene systems. Set review view type and number from the use case: provided frames, free-camera inspection, orthographic drawings, turntable or runtime screenshots are options, not mandatory universals.

## Approval

An explicit approval must identify *what* is approved: evidence interpretation, spatial blueprint, blockout geometry, art direction, a shot, a variant, or technical deployment. A structurally valid JSON file is not a camera, geometry, render or user approval. Unknown items remain open instead of receiving plausible invented values.

## Universal technical QA view

`engineering_qa` is a standardized fixed 45° Blender diagnostic separate from `review_views`, which holds user/scene-specific presentation cameras. Camera yaw, baseline transform/scale and render path are recorded only after real S1 geometry; no source pixel or 3D location may be invented during P0. See `docs/QA_CAMERA_45_STANDARD.md`.

