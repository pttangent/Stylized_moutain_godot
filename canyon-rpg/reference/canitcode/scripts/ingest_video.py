#!/usr/bin/env python3
"""Incremental ingestion script to add or update a video transcript and visual frame entry."""
import argparse
import json
import os
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def slugify(text: str) -> str:
    return re.sub(r"[^a-zA-Z0-9]+", "-", text.lower()).strip("-")[:60] or "video"


def ingest_video(video_id: str, title: str, publish_date: str, transcript_file: str):
    t_dir = os.path.join(BASE_DIR, "transcripts")
    index_path = os.path.join(t_dir, "index.json")
    with open(index_path, "r", encoding="utf-8") as f:
        index_data = json.load(f)

    with open(transcript_file, "r", encoding="utf-8") as tf:
        lines = [line.rstrip("\n") for line in tf if line.strip()]

    fname = f"{video_id}_{slugify(title)}.md"
    md_path = os.path.join(t_dir, fname)
    with open(md_path, "w", encoding="utf-8") as out:
        out.write(f"# {title}\n\n")
        out.write(f"- **Video ID**: `{video_id}`\n")
        out.write(f"- **Publish Date**: {publish_date}\n")
        out.write(f"- **URL**: https://www.youtube.com/watch?v={video_id}\n")
        out.write(f"- **Transcript Lines**: {len(lines)}\n\n")
        out.write("## Full Timestamped Transcript\n\n")
        for l in lines:
            out.write(f"{l}\n")

    videos = [v for v in index_data.get("videos", []) if v["video_id"] != video_id]
    videos.append({
        "video_id": video_id,
        "title": title,
        "publish_date": publish_date,
        "url": f"https://www.youtube.com/watch?v={video_id}",
        "transcript_lines": len(lines),
        "filename": fname,
    })
    videos.sort(key=lambda x: x.get("publish_date", ""), reverse=True)
    index_data["total_videos"] = len(videos)
    index_data["videos"] = videos

    with open(index_path, "w", encoding="utf-8") as f:
        json.dump(index_data, f, indent=2, ensure_ascii=False)
    print(f"Successfully ingested {video_id} -> transcripts/{fname}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ingest a new video transcript into the pack.")
    parser.add_argument("--video-id", required=True)
    parser.add_argument("--title", required=True)
    parser.add_argument("--publish-date", default="2026-01-01")
    parser.add_argument("--transcript-file", required=True)
    args = parser.parse_args()
    ingest_video(args.video_id, args.title, args.publish_date, args.transcript_file)
