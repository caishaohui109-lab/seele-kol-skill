#!/usr/bin/env python3
"""Normalize, filter, and deduplicate SEELE creator candidate CSV files."""

import argparse
import csv
import hashlib
import statistics
from pathlib import Path
from urllib.parse import urlparse

PLATFORM_NAMES = {"tiktok": "TikTok", "youtube": "YouTube"}


def normalize_platform(value):
    key = str(value).strip().lower()
    if key not in PLATFORM_NAMES:
        raise ValueError(f"unsupported platform: {value}")
    return PLATFORM_NAMES[key]


def normalize_profile_url(platform, url):
    platform = normalize_platform(platform)
    parsed = urlparse(str(url).strip())
    path = parsed.path.rstrip("/").lower()
    if platform == "TikTok" and not path.startswith("/@"):
        raise ValueError(f"invalid TikTok profile URL: {url}")
    if platform == "YouTube" and not path.startswith("/@"):
        raise ValueError(f"only handle-based YouTube URLs are accepted: {url}")
    host = "www.tiktok.com" if platform == "TikTok" else "www.youtube.com"
    return f"https://{host}{path}"


def median_views(values):
    numbers = [int(float(v)) for v in values if str(v).strip() and float(v) > 0]
    if not numbers:
        return 0
    return int(statistics.median(numbers))


def stable_creator_id(platform, profile_url, email):
    normalized = normalize_profile_url(platform, profile_url)
    identity = f"{normalize_platform(platform)}|{normalized}|{str(email).strip().lower()}"
    return hashlib.sha256(identity.encode("utf-8")).hexdigest()[:16]


def _read_rows(path):
    if not path:
        return []
    with Path(path).open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def _row_keys(row):
    url = normalize_profile_url(row["平台"], row["主页链接"])
    email = row.get("公开商务邮箱", "").strip().lower()
    keys = {f"url:{url}"}
    if email:
        keys.add(f"email:{email}")
    return keys


def process_csv(input_path, output_path, history_path=None, min_median_views=5000):
    rows = _read_rows(input_path)
    history_keys = set()
    for row in _read_rows(history_path):
        history_keys.update(_row_keys(row))
    seen = set(history_keys)
    kept = []
    duplicate_count = 0
    below_view_gate_count = 0
    for row in rows:
        keys = _row_keys(row)
        if keys & seen:
            duplicate_count += 1
            continue
        views = [row.get(f"播放{i}", "") for i in range(1, 11)]
        median = median_views(views)
        if median < min_median_views:
            below_view_gate_count += 1
            continue
        row["平台"] = normalize_platform(row["平台"])
        row["主页链接"] = normalize_profile_url(row["平台"], row["主页链接"])
        row["中位播放"] = str(median)
        row["近期相关内容样本量"] = str(len([v for v in views if str(v).strip()]))
        row["Creator ID"] = stable_creator_id(
            row["平台"], row["主页链接"], row.get("公开商务邮箱", "")
        )
        kept.append(row)
        seen.update(keys)
    fieldnames = list(rows[0].keys()) if rows else []
    for name in ["Creator ID", "近期相关内容样本量", "中位播放"]:
        if name not in fieldnames:
            fieldnames.append(name)
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    with Path(output_path).open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(kept)
    return {
        "input_count": len(rows),
        "kept_count": len(kept),
        "duplicate_count": duplicate_count,
        "below_view_gate_count": below_view_gate_count,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input")
    parser.add_argument("output")
    parser.add_argument("--history")
    parser.add_argument("--min-median-views", type=int, default=5000)
    args = parser.parse_args()
    print(process_csv(args.input, args.output, args.history, args.min_median_views))


if __name__ == "__main__":
    main()
