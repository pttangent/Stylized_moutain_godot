#!/usr/bin/env python3
"""Full-text & timestamped search across channel transcripts, visual frame index, and resources."""
import argparse
import json
import os
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def search_pack(query: str, max_results: int = 25):
    pattern = re.compile(re.escape(query), re.IGNORECASE)
    hits = []

    # 1. Search transcripts
    t_dir = os.path.join(BASE_DIR, "transcripts")
    index_path = os.path.join(t_dir, "index.json")
    if os.path.exists(index_path):
        with open(index_path, "r", encoding="utf-8") as f:
            t_index = json.load(f)
        for item in t_index.get("videos", []):
            md_path = os.path.join(t_dir, item["filename"])
            if os.path.exists(md_path):
                with open(md_path, "r", encoding="utf-8") as mf:
                    for line_no, line in enumerate(mf, 1):
                        if pattern.search(line):
                            hits.append({
                                "source": "transcript",
                                "video_id": item["video_id"],
                                "title": item["title"],
                                "line": line.strip(),
                                "file": f"transcripts/{item['filename']}:{line_no}",
                            })
                            if len(hits) >= max_results:
                                return hits

    # 2. Search visual index
    v_path = os.path.join(BASE_DIR, "visual_index", "visual_frames_index.json")
    if os.path.exists(v_path):
        with open(v_path, "r", encoding="utf-8") as vf:
            v_data = json.load(vf)
        for frame in v_data.get("frames", []):
            blob = json.dumps(frame, ensure_ascii=False)
            if pattern.search(blob):
                hits.append({
                    "source": "visual_index",
                    "video_id": frame.get("video_id"),
                    "title": frame.get("title"),
                    "timestamp": frame.get("timestamp"),
                    "line": f"[{frame.get('timestamp')}] {frame.get('category')}: {frame.get('scene_description')}",
                    "file": "visual_index/visual_frames_index.json",
                })

    return hits[:max_results]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Search channel knowledge base.")
    parser.add_argument("query", help="Keyword or phrase to search")
    parser.add_argument("-n", "--max-results", type=int, default=25)
    args = parser.parse_args()
    results = search_pack(args.query, args.max_results)
    print(f"Found {len(results)} match(es) for '{args.query}':\n")
    for idx, h in enumerate(results, 1):
        print(f"{idx}. [{h['source']}] {h['title']} ({h['video_id']})")
        print(f"   {h['line']}")
        print(f"   File: {h['file']}\n")
