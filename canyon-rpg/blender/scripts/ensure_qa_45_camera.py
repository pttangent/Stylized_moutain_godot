#!/usr/bin/env python3
"""Create/reuse a fixed 45-degree Blender engineering QA camera.

CAM_QA_45 is a scene-independent inspection camera, NOT a presentation camera.
On first build it fits visible scene bounds in a standard 16:9 orthographic shot.
It remains frozen for comparable before/after captures. Use --force-reframe
only to intentionally establish a NEW comparison baseline.

Example:
blender -b scene.blend --python blender/scripts/ensure_qa_45_camera.py -- \
  --render-out reports/QA_45.png --report reports/QA_45_camera.json --save
"""
import argparse
import json
import math
import sys
from pathlib import Path


CAMERA_NAME = "CAM_QA_45"
GEOMETRY_TYPES = {"MESH", "CURVE", "SURFACE", "FONT", "META"}


def scene_bounds(scene):
    from mathutils import Vector
    points = []
    for obj in scene.objects:
        if obj.type not in GEOMETRY_TYPES or obj.hide_render:
            continue
        for corner in obj.bound_box:
            points.append(obj.matrix_world @ Vector(corner))
    if not points:
        return None
    mins = [min(v[i] for v in points) for i in range(3)]
    maxs = [max(v[i] for v in points) for i in range(3)]
    return points, mins, maxs


def ensure_qa_camera(scene, *, yaw_degrees=45.0, margin=1.15,
                     aspect=16.0 / 9.0, force_reframe=False):
    import bpy
    from mathutils import Vector

    if not all(math.isfinite(x) for x in (yaw_degrees, margin, aspect)):
        raise ValueError("Camera controls must be finite.")
    if margin <= 1.0 or aspect <= 0:
        raise ValueError("Expected margin > 1 and aspect > 0.")

    cam = bpy.data.objects.get(CAMERA_NAME)
    previous = None
    if cam:
        if cam.type != "CAMERA":
            raise ValueError(CAMERA_NAME + " exists but is not a camera.")
        if cam.name not in scene.objects:
            raise ValueError(CAMERA_NAME + " belongs to another scene.")
        if not bool(cam.get("qa_tool_owned", False)):
            raise ValueError("Refusing to overwrite a manually authored QA camera.")
        previous = {
            "location": list(cam.location),
            "rotation": list(cam.rotation_euler),
            "orthographic_scale": float(cam.data.ortho_scale),
            "locked": bool(cam.get("qa_locked", False)),
        }
        if cam.get("qa_locked") and not force_reframe:
            return cam, "REUSED_LOCKED", previous
    bounds = scene_bounds(scene)
    if bounds is None:
        raise RuntimeError("No visible geometry found; create the S1 blockout first.")
    points, mins, maxs = bounds
    center = Vector([(a + b) * 0.5 for a, b in zip(mins, maxs)])
    size = Vector([b - a for a, b in zip(mins, maxs)])
    radius = max(size.length * 0.5, 0.1)
    az = math.radians(yaw_degrees)
    el = math.radians(45.0)  # fixed elevation relative to Blender XY plane
    toward_camera = Vector((
        math.cos(el) * math.cos(az),
        math.cos(el) * math.sin(az),
        math.sin(el),
    ))
    location = center + toward_camera * max(10.0, radius * 4.0)
    rotation = (center - location).to_track_quat("-Z", "Y")
    local_points = [rotation.inverted() @ (p - center) for p in points]
    width = max(p.x for p in local_points) - min(p.x for p in local_points)
    height = max(p.y for p in local_points) - min(p.y for p in local_points)
    scale = max(height, width / aspect, 0.1) * margin

    if cam is None:
        camera_data = bpy.data.cameras.new(CAMERA_NAME)
        cam = bpy.data.objects.new(CAMERA_NAME, camera_data)
        scene.collection.objects.link(cam)

    cam.location = location
    cam.rotation_euler = rotation.to_euler()
    cam.data.type = "ORTHO"
    cam.data.ortho_scale = scale
    cam.data.clip_start = 0.01
    cam.data.clip_end = max(1000.0, (location - center).length + radius * 4)
    cam["qa_tool_owned"] = True
    cam["qa_locked"] = True
    cam["qa_elevation_degrees"] = 45.0
    cam["qa_yaw_degrees"] = yaw_degrees
    cam["qa_role"] = "ENGINEERING_VISIBILITY_NOT_PRESENTATION"
    cam["qa_aspect_ratio"] = aspect
    return cam, ("REFRAMED_NEW_BASELINE" if previous else "CREATED_LOCKED"), previous


def main():
    import bpy
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--yaw", type=float, default=45.0)
    parser.add_argument("--margin", type=float, default=1.15)
    parser.add_argument("--width", type=int, default=1600)
    parser.add_argument("--height", type=int, default=900)
    parser.add_argument("--force-reframe", action="store_true")
    parser.add_argument("--render-out", type=Path)
    parser.add_argument("--report", type=Path)
    parser.add_argument("--save", action="store_true")
    argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
    args = parser.parse_args(argv)
    if args.width <= 0 or args.height <= 0:
        parser.error("width and height must be positive")
    scene = bpy.context.scene
    cam, status, previous = ensure_qa_camera(
        scene, yaw_degrees=args.yaw, margin=args.margin,
        aspect=args.width / args.height, force_reframe=args.force_reframe
    )
    report = {
        "camera": CAMERA_NAME,
        "role": "ENGINEERING_QA_NOT_FINAL_CAMERA",
        "status": status,
        "elevation_degrees": float(cam.get("qa_elevation_degrees")),
        "yaw_degrees": float(cam.get("qa_yaw_degrees")),
        "projection": cam.data.type,
        "orthographic_scale": float(cam.data.ortho_scale),
        "location": list(cam.location),
        "rotation_euler": list(cam.rotation_euler),
        "image_resolution": [args.width, args.height],
        "previous_framing": previous,
        "render_executed": False,
        "note": "A 45-degree shot cannot expose every hidden surface or prove art quality."
    }
    if args.render_out:
        original = (scene.camera, scene.render.resolution_x, scene.render.resolution_y,
                    scene.render.resolution_percentage, scene.render.filepath,
                    scene.render.image_settings.file_format)
        try:
            scene.camera = cam
            scene.render.resolution_x = args.width
            scene.render.resolution_y = args.height
            scene.render.resolution_percentage = 100
            scene.render.image_settings.file_format = "PNG"
            args.render_out.parent.mkdir(parents=True, exist_ok=True)
            scene.render.filepath = str(args.render_out.resolve())
            bpy.ops.render.render(write_still=True)
            report["render_executed"] = True
            report["render_path"] = str(args.render_out)
        finally:
            (scene.camera, scene.render.resolution_x, scene.render.resolution_y,
             scene.render.resolution_percentage, scene.render.filepath,
             scene.render.image_settings.file_format) = original
    if args.save:
        if not bpy.data.filepath:
            raise RuntimeError("--save requires an existing .blend file path")
        bpy.ops.wm.save_mainfile()
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
