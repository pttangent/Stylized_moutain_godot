#!/usr/bin/env python3
"""Read-only Blender camera/landmark projection and occlusion candidate audit.

Usage: blender -b scene.blend --python this_file.py -- --contract path.json --out report.json
Checks semantic ANCHOR art_id objects, not full mesh silhouettes. No render or physics.
"""
import argparse
import json
import math
import sys
from pathlib import Path


def evaluate(scene, contract, selected_shots=None, selected_features=None):
    import bpy
    from bpy_extras.object_utils import world_to_camera_view

    shots = {v["shot_id"]: v for v in contract.get("cameras", [])}
    scene_objects = list(scene.objects)
    id_lookup = {}
    for obj in scene_objects:
        art_id = obj.get("art_id")
        if isinstance(art_id, str):
            id_lookup.setdefault(art_id, []).append(obj)
    results, issues = [], []
    depsgraph = bpy.context.evaluated_depsgraph_get()
    for feature in contract.get("features", []):
        fid = feature["feature_id"]
        if selected_features and fid not in selected_features:
            continue
        objects = id_lookup.get(feature["anchor_art_id"], [])
        for spec in feature.get("camera_checks", []):
            sid = spec["shot_id"]
            if selected_shots and sid not in selected_shots:
                continue
            row = {"feature_id": fid, "shot_id": sid, "status": "NOT_RUN"}
            shot = shots.get(sid)
            camera = bpy.data.objects.get(shot["camera_object"]) if shot else None
            if camera is None or camera.type != "CAMERA" or camera.name not in scene.objects:
                row["reason"] = "CAMERA_UNAVAILABLE_IN_SCENE"
            elif len(objects) != 1:
                row["reason"] = "MISSING_OR_DUPLICATE_ANCHOR_ART_ID"
                row["matching_objects"] = len(objects)
            else:
                anchor = objects[0]
                pt = anchor.matrix_world.translation
                uvw = world_to_camera_view(scene, camera, pt)
                uv = [float(uvw.x), float(1 - uvw.y)]
                row["projected_uv_top_left"] = uv
                row["depth"] = float(uvw.z)
                row["status"] = "SCREEN_POSITION_UNSPECIFIED"
                if uvw.z <= 0:
                    row["status"] = "BEHIND_CAMERA"
                elif not (0 <= uv[0] <= 1 and 0 <= uv[1] <= 1):
                    row["status"] = "OUTSIDE_FRAME"
                else:
                    expected = spec.get("expected_uv_top_left")
                    if expected is not None:
                        error = math.dist(uv, expected)
                        row["normalized_error"] = round(error, 6)
                        row["status"] = "POSITION_PASS" if error <= spec["tolerance_uv"] else "POSITION_DEVIATION"
                if spec.get("check_occlusion") and row["status"] not in ("BEHIND_CAMERA", "OUTSIDE_FRAME"):
                    origin = camera.matrix_world.translation
                    ray = pt - origin
                    distance = ray.length
                    if distance > 0.1:
                        try:
                            hit, location, _normal, _face, obj, _matrix = scene.ray_cast(
                                depsgraph, origin, ray.normalized(), distance=distance
                            )
                            if hit and (location - origin).length < distance - 0.1:
                                hit_art_id = obj.get("art_id", "") if obj else ""
                                row["first_ray_hit_art_id"] = hit_art_id
                                if hit_art_id not in (feature.get("asset_id"), feature["anchor_art_id"]):
                                    row["occlusion_candidate"] = True
                                    # Ray hits are conservative candidates; transparent meshes can yield false positives.
                                    if row["status"] in ("POSITION_PASS", "SCREEN_POSITION_UNSPECIFIED"):
                                        row["status"] = "OCCLUSION_CANDIDATE"
                        except Exception as exc:
                            row["occlusion_check"] = "NOT_RUN: " + type(exc).__name__
            results.append(row)
            if row["status"] not in ("POSITION_PASS", "SCREEN_POSITION_UNSPECIFIED"):
                issues.append(row)
    return {
        "tool": "p1_visual_layout_validator", "method": "ANCHOR_PROJECTION_AND_OPTIONAL_FIRST_RAY_HIT",
        "visual_render_comparison": "NOT_RUN", "physical_walkability": "NOT_APPLICABLE",
        "checked": len(results), "issues": len(issues), "results": results,
        "limits": ["single anchor per feature, not silhouettes", "raycast cannot prove opacity or visual quality",
                   "camera, scene, and Blender must be the actually loaded approved revision"]
    }


def main():
    import bpy
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--contract", required=True, type=Path)
    parser.add_argument("--out", required=True, type=Path)
    parser.add_argument("--shots", nargs="*")
    parser.add_argument("--features", nargs="*")
    argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
    args = parser.parse_args(argv)
    data = json.loads(args.contract.read_text(encoding="utf-8"))
    report = evaluate(bpy.context.scene, data, set(args.shots or []), set(args.features or []))
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"checked": report["checked"], "issues": report["issues"], "output": str(args.out)}))


if __name__ == "__main__":
    main()
