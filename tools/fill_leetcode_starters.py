#!/usr/bin/env python3
"""Fill generated LeetCode problem stubs with the official Python starter code.

Safety rules:
* Only files whose entire contents are a generated title/comment block are edited.
* A file containing any code below that block is left untouched.
* Existing files are never overwritten with an empty or unavailable template.
* The progress file permits safe reruns after a network interruption.
"""

from __future__ import annotations

import argparse
import json
import re
import time
import urllib.error
import urllib.request
from pathlib import Path


ROOT = Path(r"D:\python_learn\leetcode-journey")
INDEX_PATH = ROOT / ".leetcode_slug_index.json"
PROGRESS_PATH = ROOT / ".leetcode_starter_progress.json"
ENDPOINT = "https://leetcode.cn/graphql/"
BATCH_SIZE = 20

# These cover common LeetCode signatures and normal solution work.  They are
# deliberately added only to generated, otherwise-empty stubs.
DEFAULT_IMPORTS = """from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq"""

MAIN_GUARD = """# 快速测试验证
if __name__ == "__main__":
    solution = Solution()"""

# Exactly the shape created by the earlier title/description generator: title
# comment + one triple-single-quoted Chinese description, and nothing else.
BARE_STUB = re.compile(r"\A# [^\n]+\n'''[\s\S]*?\n'''\s*\Z")
PY_FILE = re.compile(r"^lc_(.+)_[^_].*\.py$", re.IGNORECASE)


def load_json(path: Path, default):
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def save_json(path: Path, value) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def request_graphql(query: str) -> dict:
    payload = json.dumps({"query": query}, ensure_ascii=False).encode("utf-8")
    request = urllib.request.Request(
        ENDPOINT,
        data=payload,
        headers={"Content-Type": "application/json", "User-Agent": "leetcode-journey-starter/1.0"},
        method="POST",
    )
    last_error = None
    for attempt in range(5):
        try:
            with urllib.request.urlopen(request, timeout=45) as response:
                data = json.loads(response.read().decode("utf-8"))
            if data.get("data"):
                return data["data"]
            last_error = RuntimeError(data.get("errors") or "LeetCode returned no data")
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, json.JSONDecodeError) as exc:
            last_error = exc
        time.sleep(min(16, 2**attempt))
    raise RuntimeError(f"Unable to obtain starter code: {last_error}")


def find_slug(file: Path, id_to_slug: dict[str, str]) -> str | None:
    # IDs such as LCP 68 and 面试题 16.06 contain spaces/underscores.  Match the
    # longest known safe ID prefix, rather than guessing from the Chinese title.
    name = file.name
    for safe_id in sorted(id_to_slug, key=len, reverse=True):
        if name.startswith(f"lc_{safe_id}_"):
            return id_to_slug[safe_id]
    return None


def choose_python_snippet(question: dict) -> str | None:
    snippets = question.get("codeSnippets") or []
    for preferred in ("python", "python3"):
        for snippet in snippets:
            if snippet.get("langSlug", "").lower() == preferred and snippet.get("code", "").strip():
                return snippet["code"].replace("\r\n", "\n").rstrip()
    return None


def fetch_snippets(slugs: list[str]) -> dict[str, str]:
    fields = []
    for i, slug in enumerate(slugs):
        escaped = slug.replace('\\', '\\\\').replace('"', '\\"')
        fields.append(
            f'q{i}: question(titleSlug: "{escaped}") {{ titleSlug codeSnippets {{ langSlug code }} }}'
        )
    data = request_graphql("query starterTemplates { " + " ".join(fields) + " }")
    result = {}
    for i in range(len(slugs)):
        question = data.get(f"q{i}")
        if question:
            snippet = choose_python_snippet(question)
            if snippet:
                result[slugs[i]] = snippet
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description="Add official Python starters to generated LeetCode stubs.")
    parser.add_argument("--dry-run", action="store_true", help="Report eligible files without writing them.")
    parser.add_argument("--limit", type=int, default=0, help="Process at most this many eligible files (0 = all).")
    # Jupyter adds an internal --f=<kernel-json> argument when %run executes a
    # script.  It is irrelevant to this tool, so deliberately ignore it.
    args, unknown = parser.parse_known_args()
    if unknown:
        print(f"Ignored notebook arguments: {' '.join(unknown)}")

    if not ROOT.is_dir():
        raise SystemExit(f"Project directory does not exist: {ROOT}")
    if not INDEX_PATH.is_file():
        raise SystemExit(f"Missing index file: {INDEX_PATH}")

    id_to_slug = load_json(INDEX_PATH, {})
    progress = load_json(PROGRESS_PATH, {"completed": [], "failed": []})
    completed = set(progress.get("completed", []))

    eligible: list[tuple[Path, str, str]] = []
    skipped_written = 0
    skipped_unknown = 0
    for file in ROOT.rglob("lc_*.py"):
        text = file.read_text(encoding="utf-8-sig")
        if not BARE_STUB.fullmatch(text):
            skipped_written += 1
            continue
        slug = find_slug(file, id_to_slug)
        if not slug:
            skipped_unknown += 1
            continue
        eligible.append((file, slug, text.rstrip()))

    if args.limit:
        eligible = eligible[: args.limit]
    print(f"Eligible generated stubs: {len(eligible)}")
    print(f"Skipped files containing code: {skipped_written}")
    print(f"Skipped files without a known slug: {skipped_unknown}")
    if args.dry_run:
        return 0

    snippets: dict[str, str] = {}
    unique_slugs = list(dict.fromkeys(slug for _, slug, _ in eligible))
    for start in range(0, len(unique_slugs), BATCH_SIZE):
        batch = unique_slugs[start : start + BATCH_SIZE]
        missing = [slug for slug in batch if slug not in completed]
        if missing:
            try:
                snippets.update(fetch_snippets(missing))
                completed.update(missing)
                progress["completed"] = sorted(completed)
                save_json(PROGRESS_PATH, progress)
            except RuntimeError as exc:
                print(f"Stopped before batch {start // BATCH_SIZE + 1}: {exc}")
                break

    created = 0
    unavailable = 0
    for file, slug, bare_text in eligible:
        snippet = snippets.get(slug)
        if not snippet:
            unavailable += 1
            continue
        file.write_text(
            f"{bare_text}\n\n{DEFAULT_IMPORTS}\n\n{snippet}\n\n{MAIN_GUARD}\n",
            encoding="utf-8",
        )
        created += 1

    print(f"Updated generated stubs: {created}")
    print(f"No Python starter returned: {unavailable}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
