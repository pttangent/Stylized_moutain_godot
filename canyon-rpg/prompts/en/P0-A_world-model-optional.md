# P0-A — Optional existing 3D reference inspection

Run only if an existing 3D model or scanned scene is **actually provided and relevant**. This is independent of model vendor, file format and scene type; it is not a generation instruction.

1. Verify file identity, source attribution, license, scene/mesh hierarchy, axes, transforms, bounds and raw unit status. Preserve original bytes and any user-reviewed correspondence.
2. Inspect geometry for missing pieces, disconnected shells, mesh direction, scale contradictions, unstable surface classifications and false/ambiguous features.
3. Create only the diagnostic views needed to check source agreement, with explicit camera IDs and observed outcomes. Do not invent orthographic, fixed-angle or image-registration requirements.
4. Where useful, derive candidate depth/surface masks, min/max samples and unknown coverage, with exact sampling and normal filters. A topmost intersection is never automatically a valid physical surface.
5. Register a source-to-design transform exactly once. Do not assert physical units from a generated model without evidence or an explicit authored scale decision.
6. Compare against the highest-confidence original inputs and record `OBSERVED` / `GENERATED_CANDIDATE` / `INFERRED` / `UNKNOWN`, explicitly resolving design overrides.
7. Produce an inspect-only manifest, source hash, actual diagnostics, discrepancies, unit/axis uncertainty and an optional integration recommendation.

If no relevant model exists, mark this branch `NOT_APPLICABLE` and continue generic P0-A. No calls to external model providers or credit-consuming services.
