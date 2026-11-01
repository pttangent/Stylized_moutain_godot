# P1-playable — Optional interactive/runtime adaptation

Use **only** when the user explicitly requests an interactive, traversable or otherwise executable scene and a P1-concept version is approved. This is a conditional production path, not the default.

1. Discover the target runtime, interaction intent, controls/agents/entities, navigation or simulation requirements and actual relevant scene features. Never assume a particular engine, movement system, agent size, slope value or scene type.
2. Read the approved concept, camera views, source/geometry contract and revision history. Preserve accepted spatial hierarchy, visual identity and source evidence. Do not destructively reshape the concept to satisfy a generic path or collision template.
3. Identify exact needed interactive regions, inputs/outputs, disabled regions, safety/performance expectations, and how each interaction can be tested.
4. Build runtime data/geometry only for actual requirements: collision/physics, navigation, animation, interactions, scripts, event graphs or other domain-specific systems. Unused systems are `NOT_APPLICABLE`.
5. Measure relevant clearances, constraints and continuity **along the actual interaction geometry** rather than relying on graph endpoints. Record all standards/thresholds as scene-specific decisions.
6. Export from Blender with documented axis/scale conventions and validated transform round-trip. Preserve the editable art source and compare output views against approved concept captures.
7. Execute real runtime tests and real renderer captures. Report each scenario with observed PASS/FAIL/BLOCKED/NOT_RUN and before/after art differences; structural simulation graphs alone are not proof of operation.
8. If interactive requirements conflict with approved art, report the trade-off and seek a design decision rather than silently overwriting appearance.

Deliver versioned runtime adaptation, any test scene/scripts, logs, relevant captures, provenance and reports/P1_playable.md. The P1-playable gate is **never a prerequisite** to non-interactive P2–P5 artwork.
