#!/usr/bin/env python3
"""Check the P0->P1 reference-to-geometry contract, without needing Blender.

Structure-only validation. It cannot approve a camera, visual composition or model.
"""
import argparse
import json
import math
import re
from pathlib import Path

ID = re.compile(r"^[A-Za-z][A-Za-z0-9_:-]*$")
LAYERS = {"L1_MACRO", "L2_STRUCTURAL", "L3_DRESSING"}
EVIDENCE = {"OBSERVED", "DESIGNED", "INFERRED", "UNKNOWN"}


def validate_v1(data):
    errors, warnings = [], []
    if not isinstance(data, dict):
        return {"status": "FAIL", "errors": ["root must be an object"], "warnings": []}
    if data.get("schema_version") != 1:
        errors.append("schema_version must be 1")
    images = data.get("source_images")
    shots = data.get("cameras")
    features = data.get("features")
    if not isinstance(images, list) or not images:
        errors.append("source_images must be a nonempty array")
        images = []
    if not isinstance(shots, list) or not shots:
        errors.append("cameras must be a nonempty array")
        shots = []
    if not isinstance(features, list) or not features:
        errors.append("features must be a nonempty array")
        features = []
    for field in ("scene_id", "revision"):
        if not isinstance(data.get(field), str) or not data[field].strip():
            errors.append(field + " must be nonempty")

    def id_set(items, key):
        found = set()
        for index, item in enumerate(items):
            val = item.get(key) if isinstance(item, dict) else None
            if not isinstance(val, str) or not ID.fullmatch(val):
                errors.append(f"{key}[{index}] must be a stable identifier")
            elif val in found:
                errors.append(f"duplicate {key}: {val}")
            else:
                found.add(val)
        return found

    image_ids = id_set(images, "image_id")
    shot_ids = id_set(shots, "shot_id")
    feature_ids = id_set(features, "feature_id")
    for shot in shots:
        if not isinstance(shot, dict):
            continue
        if not isinstance(shot.get("camera_object"), str) or not shot["camera_object"]:
            errors.append("camera_object missing for " + str(shot.get("shot_id")))
    dependencies = {}
    for feature in features:
        if not isinstance(feature, dict):
            continue
        fid = feature.get("feature_id", "<missing>")
        if feature.get("layer") not in LAYERS:
            errors.append(f"{fid}: invalid layer")
        if feature.get("evidence") not in EVIDENCE:
            errors.append(f"{fid}: invalid evidence")
        if feature.get("source_image_id") not in image_ids:
            errors.append(f"{fid}: unknown source_image_id")
        for key in ("asset_id", "anchor_art_id"):
            if not isinstance(feature.get(key), str) or not ID.fullmatch(feature[key]):
                errors.append(f"{fid}: invalid {key}")
        contract = feature.get("reference_shape")
        if not isinstance(contract, dict):
            errors.append(f"{fid}: reference_shape missing")
        else:
            for key in ("must_preserve", "may_redesign", "do_not_copy"):
                value = contract.get(key)
                if not isinstance(value, list) or not value or not all(isinstance(v, str) and v.strip() for v in value):
                    errors.append(f"{fid}: reference_shape.{key} must contain text")
        xy = feature.get("source_pixel_xy")
        if xy is not None and (not isinstance(xy, list) or len(xy) != 2 or
                               not all(isinstance(v, (int, float)) and not isinstance(v, bool)
                                       and math.isfinite(v) and v >= 0 for v in xy)):
            errors.append(f"{fid}: source_pixel_xy invalid")
        deps = feature.get("dependency_ids", [])
        if not isinstance(deps, list) or not all(isinstance(d, str) and d in feature_ids for d in deps):
            errors.append(f"{fid}: dependency_ids reference missing feature")
            deps = []
        dependencies[fid] = deps
        checks = feature.get("camera_checks", [])
        if not isinstance(checks, list):
            errors.append(f"{fid}: camera_checks must be an array")
            continue
        for check in checks:
            if not isinstance(check, dict) or check.get("shot_id") not in shot_ids:
                errors.append(f"{fid}: unknown camera shot")
                continue
            uv = check.get("expected_uv_top_left")
            if uv is None:
                warnings.append(f"{fid}/{check['shot_id']}: screen position awaits approval")
                continue
            if not (isinstance(uv, list) and len(uv) == 2 and
                    all(isinstance(v, (float, int)) and not isinstance(v, bool)
                        and math.isfinite(v) and 0 <= v <= 1 for v in uv)):
                errors.append(f"{fid}/{check['shot_id']}: invalid normalized UV")
            tolerance = check.get("tolerance_uv")
            if not (isinstance(tolerance, (int, float)) and not isinstance(tolerance, bool)
                    and math.isfinite(tolerance) and 0 < tolerance <= 0.5):
                errors.append(f"{fid}/{check['shot_id']}: tolerance_uv must be (0, 0.5]")

    colors = {}
    def visit(node):
        if colors.get(node) == "gray":
            errors.append("cyclic feature dependency at " + node)
            return
        if colors.get(node) == "black":
            return
        colors[node] = "gray"
        for child in dependencies.get(node, []):
            visit(child)
        colors[node] = "black"
    for fid in dependencies:
        visit(fid)
    return {
        "status": "FAIL" if errors else "STRUCTURE_PASS_WITH_OPEN_VISUAL_CHECKS" if warnings else "STRUCTURE_PASS",
        "feature_count": len(features), "camera_count": len(shots),
        "errors": errors, "warnings": warnings,
        "runtime_visual_validation": "NOT_RUN",
    }


# v2: source-type-neutral contract. v1 remains readable for historic projects.
STAGES_V2 = {"S1_COMPOSITION", "S2_STRUCTURE", "S3_DETAIL"}
EVIDENCE_V2 = {"OBSERVED", "APPROVED_DESIGN", "INFERRED", "GENERATED_CANDIDATE", "UNKNOWN"}


def validate_v2(data):
    errors, warnings = [], []
    if not isinstance(data, dict):
        return {"status": "FAIL", "errors": ["root must be an object"], "warnings": []}

    def ident(value):
        return isinstance(value, str) and bool(ID.fullmatch(value))

    def unique(items, field):
        seen = set()
        for i, row in enumerate(items):
            value = row.get(field) if isinstance(row, dict) else None
            if not ident(value):
                errors.append(f"{field}[{i}] invalid or missing")
            elif value in seen:
                errors.append(f"duplicate {field}: {value}")
            else:
                seen.add(value)
        return seen

    if data.get("schema_version") != 2:
        errors.append("schema_version must be 2")
    for name in ("scene_id", "revision"):
        if not ident(data.get(name)):
            errors.append(name + " must be a stable nonempty identifier")

    refs = data.get("reference_sources", [])
    views = data.get("review_views", [])
    features = data.get("features", [])
    for name, rows in (("reference_sources", refs), ("review_views", views), ("features", features)):
        if not isinstance(rows, list):
            errors.append(name + " must be an array")
            rows = []
        if name == "reference_sources":
            refs = rows
        elif name == "review_views":
            views = rows
        else:
            features = rows
    if not refs:
        warnings.append("reference source inventory is empty: no evidence provenance")
    if not views:
        warnings.append("no review view declared yet; visual checks unavailable")
    if not features:
        errors.append("features must list at least one actual/proposed feature")

    ref_ids = unique(refs, "ref_id")
    view_ids = unique(views, "view_id")
    feature_ids = unique(features, "feature_id")

    for row in refs:
        if not isinstance(row, dict):
            continue
        if not isinstance(row.get("kind"), str) or not row["kind"].strip():
            errors.append("source kind missing for " + str(row.get("ref_id")))
        if row.get("path") is not None and not isinstance(row.get("path"), str):
            errors.append("source path must be string or null")
    for view in views:
        if not isinstance(view, dict):
            continue
        if not view.get("camera_object"):
            warnings.append(f"{view.get('view_id')}: Blender camera not yet defined")
        elif not isinstance(view.get("camera_object"), str):
            errors.append(f"{view.get('view_id')}: camera_object must be string or null")

    depmap = {}
    for feature in features:
        if not isinstance(feature, dict):
            continue
        fid = feature.get("feature_id", "<missing>")
        if feature.get("stage") not in STAGES_V2:
            errors.append(f"{fid}: invalid stage")
        if feature.get("evidence") not in EVIDENCE_V2:
            errors.append(f"{fid}: invalid evidence")
        if not ident(feature.get("asset_id")):
            errors.append(f"{fid}: invalid asset_id")
        aid = feature.get("anchor_art_id")
        if aid is not None and not ident(aid):
            errors.append(f"{fid}: anchor_art_id must be stable ID or null")
        source_refs = feature.get("source_refs")
        if not isinstance(source_refs, list) or not all(ident(x) and x in ref_ids for x in source_refs):
            errors.append(f"{fid}: source_refs invalid or unresolved")
        elif not source_refs:
            warnings.append(f"{fid}: no linked reference source")
        xy = feature.get("source_pixel_xy")
        if xy is not None and not (
            isinstance(xy, list) and len(xy) == 2 and
            all(isinstance(n, (int, float)) and not isinstance(n, bool)
                and math.isfinite(n) and n >= 0 for n in xy)
        ):
            errors.append(f"{fid}: invalid source_pixel_xy")
        rules = feature.get("shape_rules")
        if not isinstance(rules, dict):
            errors.append(f"{fid}: shape_rules must be an object")
        else:
            for key in ("must_preserve", "may_redesign", "do_not_copy"):
                values = rules.get(key)
                if not isinstance(values, list) or not all(isinstance(s, str) and s.strip() for s in values):
                    errors.append(f"{fid}: shape_rules.{key} must be a string array")
            if not rules.get("must_preserve"):
                warnings.append(f"{fid}: no approved must_preserve constraints")
        deps = feature.get("dependency_ids", [])
        if not isinstance(deps, list) or not all(isinstance(x, str) and x in feature_ids for x in deps):
            errors.append(f"{fid}: invalid dependency_ids")
            deps = []
        depmap[fid] = deps
        checks = feature.get("view_checks", [])
        if not isinstance(checks, list):
            errors.append(f"{fid}: view_checks must be an array")
            checks = []
        for check in checks:
            if not isinstance(check, dict) or check.get("view_id") not in view_ids:
                errors.append(f"{fid}: view_check refers to undefined view")
                continue
            sid = check["view_id"]
            if aid is None:
                warnings.append(f"{fid}/{sid}: no semantic anchor; projection NOT_RUN")
            uv = check.get("expected_uv_top_left")
            tol = check.get("tolerance_uv")
            if uv is None:
                if tol is not None:
                    errors.append(f"{fid}/{sid}: tolerance must be null for unknown target")
                warnings.append(f"{fid}/{sid}: screen position unspecified")
            else:
                if not (isinstance(uv, list) and len(uv) == 2 and all(
                    isinstance(n, (float, int)) and not isinstance(n, bool) and
                    math.isfinite(n) and 0 <= n <= 1 for n in uv
                )):
                    errors.append(f"{fid}/{sid}: invalid normalized view position")
                if not (isinstance(tol, (int, float)) and not isinstance(tol, bool)
                        and math.isfinite(tol) and 0 < tol <= 0.5):
                    errors.append(f"{fid}/{sid}: tolerance_uv must be in (0, 0.5]")

    colors = set()
    done = set()
    def visit(node):
        if node in colors:
            errors.append(f"cyclic feature dependency at {node}")
            return
        if node in done:
            return
        colors.add(node)
        for child in depmap.get(node, []):
            visit(child)
        colors.remove(node)
        done.add(node)
    for node in depmap:
        visit(node)

    return {
        "schema_version": 2,
        "status": "FAIL" if errors else "STRUCTURE_PASS_WITH_OPEN_VISUAL_CHECKS" if warnings else "STRUCTURE_PASS",
        "feature_count": len(features),
        "camera_count": len(views),
        "reference_count": len(refs),
        "errors": errors,
        "warnings": warnings,
        "runtime_visual_validation": "NOT_RUN",
        "physical_validation": "NOT_APPLICABLE",
    }


def validate(data):
    if not isinstance(data, dict):
        return {"status": "FAIL", "errors": ["root must be an object"], "warnings": []}
    if data.get("schema_version") == 1:
        return validate_v1(data)
    if data.get("schema_version") == 2:
        return validate_v2(data)
    return {"status": "FAIL", "errors": ["unsupported schema_version; expected 1 or 2"], "warnings": []}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("contract", type=Path)
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    report = validate(json.loads(args.contract.read_text(encoding="utf-8")))
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))
    raise SystemExit(1 if report["errors"] else 0)


if __name__ == "__main__":
    main()
