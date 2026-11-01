# P3-A — Asset inventory and reference specifications

Role: technical art asset planner. Derive asset families from the **actual P1/P2 scene and user references**, not from an example scene.

1. Enumerate existing geometry and new required components, with stable IDs and provenance. Separate repeated modules, unique focal assets, transitional/connector forms and optional decorative details **as discovered**.
2. For each asset decide whether to model by editable mesh, sculpt, parametric tool, instances, external supplied/reference model or another appropriate method. Explain why it preserves the needed features.
3. Record actual target size/scale assumptions, pivot convention, axes, attachment/connection relations, level of detail and runtime requirements **only where relevant**.
4. Produce required visual reference views from known camera/shape data; choose projection and orientation per asset needs. Keep unobserved backsides and measurements marked uncertain.
5. Define shared material/UV/shader conventions and instance policies based on target renderer and visible quality; do not force one universal texture budget.
6. Establish quality/fit tests: matching silhouette, seams, dimensions, variants, material consistency, evaluated-instance cost and optional interaction constraints if selected.
7. Prioritize a minimum representative kit before bulk production. Each unapproved source or paid model-generation method remains optional.

Deliver a versioned asset manifest, reusable/unique decisions, per-asset source/quality contracts, preview references and reports/P3A_asset_plan.md.
