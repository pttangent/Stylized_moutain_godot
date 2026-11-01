# P0-B — Materialize a scene-agnostic spatial and visual blueprint

Role: procedural scene-layout and data validation engineer. Consume the P0-A source inventory, scene profile and approved feature design rather than inventing additional content.

## Model the **actual** scene specification
1. Save a versioned `scene_profile.json` and a `blueprint/scene_blueprint.json` or equivalent manifest linking features, source IDs, authored geometry representations, transforms, scale basis, relationships and review requirements.
2. Produce a **reference geometry contract v2** at `blueprint/reference_geometry_contract.json` using `docs/REFERENCE_GEOMETRY_CONTRACT.md`. Source images are optional; preserve non-image references and null image-space coordinates when no image exists.
3. Create only appropriate spatial descriptions: a plan, volumetric diagram, top/front/side construction views, source-aligned overlay, feature/connection graph, authored spatial fields or segmentation layers. None is universally mandatory.
4. Choose any raster representation only where the object is validly represented that way; preserve dimensionality, units, numeric mapping and unknown cells. Do not coerce multi-layer/overhanging geometry into a single-valued field.
5. For each relevant system, validate actual topology and relationship constraints (physical, visual, mathematical, structural or semantic) in its correct domain. Constraints may be irrelevant to other scene types; do not apply them globally.
6. Define only the cameras/review views required for the selected goal. Separate reference-source camera estimates from production cameras when relevant. Include capture format/shot IDs and distinguish measured versus designer-chosen values.
7. Mark optional generated models as candidate references only. Store raw units, origin, transforms, quality concerns and disagreement with original evidence; no provider or generation call is assumed.
8. Save scripts and data that rebuild the **authored** blueprint and its diagnostics. Preserve immutable source data and report proposed changes with reasons and affected IDs.

## Validation and gate
Run `python blueprint/validate_reference_geometry_contract.py blueprint/reference_geometry_contract.json --report reports/P0B_geometry_contract_validation.json` if the v2 contract was generated. This checks schema/IDs/dependencies only, not image quality or modeling. Validate any additional representations according to their own schema, not hard-coded legacy tests. Report PASS / FAIL / ASSUMED / NOT_RUN / NOT_APPLICABLE without claims about unbuilt geometry.

Deliver blueprint manifest, applicable maps/graphs/sections, chosen review-view specification, versioned source-to-design links, reproducible generator(s) where used and an actual validation report. Exit to Blender P1-concept without mandatory playability.
