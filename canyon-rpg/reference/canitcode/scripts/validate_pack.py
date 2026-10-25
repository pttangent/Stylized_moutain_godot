#!/usr/bin/env python3
"""Integrity validator for the channel extraction data pack."""
import json
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main():
    required_files = [
        "README.md",
        "transcripts/index.json",
        "visual_index/visual_frames_index.json",
        "visual_index/visual_frames_timeline.md",
        "resources/resources_catalog.json",
        "resources/resources_and_tools.md",
    ]
    for rel in required_files:
        p = os.path.join(BASE_DIR, rel)
        if not os.path.exists(p):
            print(f"[FAIL] Missing required file: {rel}")
            sys.exit(1)

    with open(os.path.join(BASE_DIR, "transcripts/index.json"), "r", encoding="utf-8") as f:
        t_idx = json.load(f)

    videos = t_idx.get("videos", [])
    if not videos:
        print("[FAIL] No videos in transcripts/index.json")
        sys.exit(1)

    missing_md = 0
    total_lines = 0
    for v in videos:
        md_p = os.path.join(BASE_DIR, "transcripts", v["filename"])
        if not os.path.exists(md_p):
            print(f"[FAIL] Missing transcript file: {v['filename']}")
            missing_md += 1
        else:
            total_lines += v.get("transcript_lines", 0)

    if missing_md > 0:
        sys.exit(1)

    with open(os.path.join(BASE_DIR, "visual_index/visual_frames_index.json"), "r", encoding="utf-8") as f:
        v_idx = json.load(f)

    print(f"[PASS] Validated {len(videos)} video transcripts ({total_lines} timestamped lines) and {len(v_idx.get('frames', []))} visual frame entries.")


if __name__ == "__main__":
    main()
