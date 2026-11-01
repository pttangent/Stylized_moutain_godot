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


def validate(data):
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
