"""YouTube transcripts -> overlapping chunks -> chunks.jsonl (ready for any vector DB).

Usage: APIFY_TOKEN=... python youtube_transcripts_rag.py <video|@channel|playlist URL> [more URLs]
Actor: https://apify.com/murch1k/youtube-transcript-scraper ($5 per 1,000 transcripts, caption-less videos are free)
"""
import json
import os
import sys

from apify_client import ApifyClient

CHUNK_WORDS, OVERLAP = 300, 50


def chunks(segments, video):
    """Group timestamped segments into ~CHUNK_WORDS chunks; keep the start second for deep links."""
    buf, start = [], None
    for seg in segments:
        start = seg["start"] if start is None else start
        buf.extend(seg["text"].split())
        if len(buf) >= CHUNK_WORDS:
            yield {"text": " ".join(buf), "url": f"{video['url']}&t={int(start)}s", "title": video["title"]}
            buf, start = buf[-OVERLAP:], seg["start"]
    if buf:
        yield {"text": " ".join(buf), "url": f"{video['url']}&t={int(start or 0)}s", "title": video["title"]}


def main(urls):
    client = ApifyClient(os.environ["APIFY_TOKEN"])
    run = client.actor("murch1k/youtube-transcript-scraper").call(
        run_input={"urls": urls, "maxVideosPerSource": 10, "languages": ["en"], "includeSegments": True})
    n = 0
    with open("chunks.jsonl", "w") as out:
        for video in client.dataset(run["defaultDatasetId"]).iterate_items():
            for c in chunks(video.get("segments") or [], video):
                out.write(json.dumps(c, ensure_ascii=False) + "\n")
                n += 1
    print(f"wrote {n} chunks to chunks.jsonl")


if __name__ == "__main__":
    main(sys.argv[1:] or ["https://www.youtube.com/watch?v=dQw4w9WgXcQ"])
