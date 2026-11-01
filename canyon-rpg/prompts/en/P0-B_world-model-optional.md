# P0-B — Optional 3D-source-guided blueprint integration

Run only after a real source model was inspected under P0-A_world-model-optional.md. No particular service, renderer, semantic category or geometry family is assumed.

- Verify model source/hash, raw bounds, axes, units, coordinate transforms, confidence and available coverage. Retain raw-model evidence independently from authored scene geometry.
- Integrate only reviewed model features. Preserve the source evidence and explicitly record any model-versus-reference disagreement or designer override.
- Choose geometry representation per actual feature and preserve unknown surfaces instead of replacing them with invented precise measurements.
- Build only the relevant spatial views/graphs/derived fields; validate their domain-specific logic. Generated geometry is not proof of true scale, proper collision or full depth coverage.
- Run the generic reference-geometry contract structural check, and record model-specific diagnostics separately. Never report actual visual/motion/physics approval from file existence or a successful JSON test.

Deliver a versioned model-evidence manifest, blueprint difference report and any real diagnostic outputs. The base P0-B pipeline also works without a model.
