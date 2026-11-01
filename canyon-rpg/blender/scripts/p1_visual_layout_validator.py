#!/usr/bin/env python3
"""Read-only scene-agnostic Blender view/landmark projection diagnostics.

Supports reference-geometry contracts v1 (legacy) and v2 (universal).
It does NOT render, inspect complete silhouettes, infer scale, or perform physics.
Usage: blender -b scene.blend --python this_file.py -- --contract contract.json --out report.json
"""
import argparse
import json
import math
import sys
from pathlib import Path


def evaluate(scene, contract, selected_shots=None, selected_features=None):
    import bpy
    from bpy_extras.object_utils import world_to_camera_view

    v2 = contract.get("schema_version") == 2
    view_key = "view_id" if v2 else "shot_id"
    view_rows = contract.get("review_views" if v2 else "cameras", [])
    check_key = "view_checks" if v2 else "camera_checks"
    views = {
        v[view_key]: v
        for v in view_rows if isinstance(v, dict) and isinstance(v.get(view_key), str)
    }
    id_lookup = {}
    for obj in scene.objects:
        art_id = obj.get("art_id")
        if isinstance(art_id, str):
            id_lookup.setdefault(art_id, []).append(obj)

    results, issues = [], []
    depsgraph = bpy.context.evaluated_depsgraph_get()
    for feature in contract.get("features", []):
        fid = feature.get("feature_id")
        if selected_features and fid not in selected_features:
            continue
        anchor_id = feature.get("anchor_art_id")
        matches = id_lookup.get(anchor_id, []) if anchor_id else []
        for check in feature.get(check_key, []):
            sid = check.get(view_key)
            if selected_shots and sid not in selected_shots:
                continue
            row = {"feature_id": fid, "view_id": sid, "status": "NOT_RUN"}
            view = views.get(sid)
            camera_name = view.get("camera_object") if view else None
            camera = bpy.data.objects.get(camera_name) if camera_name else None
            if camera is None or camera.type != "CAMERA" or camera.name not in scene.objects:
                row["reason"] = "CAMERA_NOT_IN_ACTIVE_SCENE"
            elif len(matches) != 1:
                row["reason"] = "MISSING_OR_DUPLICATE_SEMANTIC_ANCHOR"
                row["matching_anchor_count"] = len(matches)
            else:
                point = matches[0].matrix_world.translation
                projection = world_to_camera_view(scene, camera, point)
                coords = [float(projection.x), float(1.0 - projection.y)]
                row["projected_uv_top_left"] = coords
                row["depth"] = float(projection.z)
                row["status"] = "SCREEN_POSITION_UNSPECIFIED"
                if projection.z <= 0:
                    row["status"] = "BEHIND_CAMERA"
                elif not (0 <= coords[0] <= 1 and 0 <= coords[1] <= 1):
                    row["status"] = "OUTSIDE_FRAME"
                elif check.get("expected_uv_top_left") is not None:
                    target = check["expected_uv_top_left"]
                    tolerance = check["tolerance_uv"]
                    error = math.dist(coords, target)
                    row["normalized_error"] = round(error, 6)
                    row["status"] = "POSITION_PASS" if error <= tolerance else "POSITION_DEVIATION"
                if check.get("check_occlusion") and row["status"] not in ("BEHIND_CAMERA", "OUTSIDE_FRAME"):
                    origin = camera.matrix_world.translation
                    ray = point - origin
                    distance = ray.length
                    if distance > 0.1:
                        try:
                            hit, loc, _normal, _index, obj, _matrix = scene.ray_cast(
                                depsgraph, origin, ray.normalized(), distance=distance
                            )
                            if hit and (loc - origin).length < distance - 0.1:
                                hit_id = obj.get("art_id", "") if obj else ""
                                row["first_ray_hit_art_id"] = hit_id
                                # The feature's own mesh can cover its anchor. This
                                # is a conservative ray hit, not verified obstruction.
                                if hit_id not in (anchor_id, feature.get("asset_id")):
                                    row["occlusion_candidate"] = True
                                    if row["status"] in ("POSITION_PASS", "SCREEN_POSITION_UNSPECIFIED"):
                                        row["status"] = "OCCLUSION_CANDIDATE"
                        except Exception as exc:
                            row["occlusion_check"] = "NOT_RUN: " + type(exc).__name__
            results.append(row)
            if row["status"] not in ("POSITION_PASS", "SCREEN_POSITION_UNSPECIFIED"):
                issues.append(row)
    return {
        "tool": "p1_visual_layout_validator",
        "contract_schema": contract.get("schema_version"),
        "method": "SEMANTIC_ANCHOR_PROJECTION_AND_OPTIONAL_FIRST_RAY_HIT",
        "render_comparison": "NOT_RUN",
        "geometry_silhouette_review": "NOT_RUN",
        "physical_walkability": "NOT_APPLICABLE",
        "checked": len(results), "issues": len(issues),
        "results": results,
        "limits": [
            "Unspecified targets or missing views never prove an art pass",
            "Anchor projections do not validate full geometry silhouettes",
            "Ray hits do not prove visual occlusion or material opacity",
            "Camera/anchor/artwork must belong to the actual loaded scene",
        ],
    }


def main():
    import bpy
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--contract", required=True, type=Path)
    parser.add_argument("--out", required=True, type=Path)
    parser.add_argument("--shots", nargs="*")
    parser.add_argument("--features", nargs="*")
    args_list = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
    args = parser.parse_args(args_list)
    data = json.loads(args.contract.read_text(encoding="utf-8"))
    result = evaluate(bpy.context.scene, data, set(args.shots or []), set(args.features or []))
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"checked": result["checked"], "issues": result["issues"],
                      "report": str(args.out)}))


if __name__ == "__main__":
    main()
