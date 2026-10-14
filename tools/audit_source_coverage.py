"""Audit local exercise placement against the public LeetCode source articles.

Run from the repository root with ``python tools/audit_source_coverage.py``.
Use ``--stage`` to check a generated staging tree before syncing it.
Only missing source entries are queried for paid status.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

import rebuild_core_route as route


ROW = re.compile(
    r"\]\(https://leetcode\.cn/problems/([^/]+)/\).*?"
    r"\]\(<\./([^>]+)>\)"
)


def indexed_rows(topic_dir: Path) -> tuple[set[tuple[str, str]], list[str]]:
    readme = topic_dir / "README.md"
    if not readme.exists():
        return set(), [f"Missing README: {readme}"]
    rows: set[tuple[str, str]] = set()
    broken: list[str] = []
    for line in readme.read_text(encoding="utf-8").splitlines():
        match = ROW.search(line)
        if not match:
            continue
        slug, relative_file = match.groups()
        parts = Path(relative_file).parts
        if len(parts) < 2 or not (topic_dir / relative_file).is_file():
            broken.append(f"Broken file link: {topic_dir / relative_file}")
        elif not (topic_dir / parts[0] / "templates.md").is_file():
            broken.append(f"Missing template: {topic_dir / parts[0] / 'templates.md'}")
        rows.add((slug, parts[0]))
    return rows, broken


def paid_status(slugs: set[str]) -> dict[str, bool | None]:
    result: dict[str, bool | None] = {}
    slugs_list = sorted(slugs)
    for start in range(0, len(slugs_list), 30):
        batch = slugs_list[start:start + 30]
        fields = " ".join(
            f'q{i}: question(titleSlug: "{slug}") {{ isPaidOnly }}'
            for i, slug in enumerate(batch)
        )
        data = json.loads(route.fetch(
            route.GRAPHQL,
            json.dumps({"query": "query coverageAudit { " + fields + " }"}).encode("utf-8"),
        ).decode("utf-8"))
        for i, slug in enumerate(batch):
            question = data.get("data", {}).get(f"q{i}")
            result[slug] = question.get("isPaidOnly") if question else None
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--stage", action="store_true", help="Audit .core_route_stage instead of the repository.")
    args = parser.parse_args()
    root = route.STAGE if args.stage else route.ROOT
    if not root.is_dir():
        parser.error(f"Directory does not exist: {root}")

    article_cache = {
        url: route.parse_records(route.article_markdown(url))
        for url in dict.fromkeys(topic.source for topic in route.TOPICS)
    }
    expected_by_topic: dict[str, set[tuple[str, str]]] = {}
    expected_by_topic[route.INTRO_TOPIC.folder] = {
        (record["slug"], route.section_for(record, route.INTRO_TOPIC)[0])
        for record in route.intro_records()
    }
    for topic in route.TOPICS:
        expected_by_topic[topic.folder] = {
            (record["slug"], route.section_for(record, topic)[0])
            for record in route.selected_records(article_cache[topic.source], topic)
        }

    missing_by_topic: dict[str, set[tuple[str, str]]] = {}
    rows_by_topic: dict[str, set[tuple[str, str]]] = {}
    errors: list[str] = []
    for topic, expected in expected_by_topic.items():
        rows, broken = indexed_rows(root / topic)
        rows_by_topic[topic] = rows
        missing_by_topic[topic] = expected - rows
        errors.extend(broken)
        errors.extend(f"Unexpected index entry: {topic}/{section}: {slug}"
                      for slug, section in sorted(rows - expected))

    statuses = paid_status({slug for missing in missing_by_topic.values() for slug, _ in missing})
    for topic, expected in expected_by_topic.items():
        missing = missing_by_topic[topic]
        paid = sum(statuses.get(slug) is True for slug, _ in missing)
        unexpected = [(slug, section) for slug, section in missing if statuses.get(slug) is not True]
        errors.extend(
            f"Missing public/unknown problem: {topic}/{section}: {slug} (paid={statuses.get(slug)})"
            for slug, section in sorted(unexpected)
        )
        print(f"{topic}: source placements={len(expected)}, indexed={len(rows_by_topic[topic])}, "
              f"paid skipped={paid}, missing public/unknown={len(unexpected)}")

    if errors:
        print("\n".join(errors))
        return 1
    print("Coverage OK: every selected non-paid source placement has a linked file and template.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
