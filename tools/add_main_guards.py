#!/usr/bin/env python3
"""Append a quick-test main guard only to untouched LeetCode Python skeletons."""

from __future__ import annotations

import argparse
import ast
from pathlib import Path


ROOT = Path(r"D:\python_learn\leetcode-journey")
MAIN_GUARD = '\n\n# 快速测试验证\nif __name__ == "__main__":\n    solution = Solution()\n'


def is_empty_method(method: ast.FunctionDef | ast.AsyncFunctionDef) -> bool:
    """A LeetCode starter method contains only its optional type docstring/pass."""
    body = list(method.body)
    if body and isinstance(body[0], ast.Expr) and isinstance(body[0].value, ast.Constant) and isinstance(body[0].value.value, str):
        body.pop(0)
    return all(
        isinstance(node, ast.Pass)
        or (isinstance(node, ast.Expr) and isinstance(node.value, ast.Constant) and node.value.value is Ellipsis)
        for node in body
    )


def is_untouched_solution_skeleton(text: str) -> bool:
    try:
        tree = ast.parse(text)
    except SyntaxError:
        return False

    solution_classes = [node for node in tree.body if isinstance(node, ast.ClassDef) and node.name == "Solution"]
    if len(solution_classes) != 1:
        return False

    # User code outside imports and Solution is a reason to leave the file alone.
    allowed_module_nodes = (ast.Import, ast.ImportFrom, ast.ClassDef)
    if any(not isinstance(node, allowed_module_nodes) for node in tree.body):
        return False

    solution = solution_classes[0]
    methods = [node for node in solution.body if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))]
    if not methods:
        return False
    if any(not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) for node in solution.body):
        return False
    return all(is_empty_method(method) for method in methods)


def main() -> int:
    parser = argparse.ArgumentParser(description="Safely add quick-test main guards to untouched LeetCode skeletons.")
    parser.add_argument("--apply", action="store_true", help="Actually append the guard. Without this flag, only report.")
    # Jupyter adds an internal --f=<kernel-json> argument when %run executes a
    # script.  It is irrelevant to this tool, so deliberately ignore it.
    args, unknown = parser.parse_known_args()
    if unknown:
        print(f"Ignored notebook arguments: {' '.join(unknown)}")

    candidates: list[Path] = []
    skipped_guard = skipped_code = skipped_invalid = 0
    for file in ROOT.rglob("lc_*.py"):
        text = file.read_text(encoding="utf-8-sig")
        if "if __name__" in text:
            skipped_guard += 1
        elif is_untouched_solution_skeleton(text):
            candidates.append(file)
        else:
            skipped_code += 1

    print(f"Eligible untouched starter files: {len(candidates)}")
    print(f"Already containing a main guard: {skipped_guard}")
    print(f"Skipped because they contain code, lack a default Solution skeleton, or cannot be safely parsed: {skipped_code}")
    if not args.apply:
        return 0

    for file in candidates:
        text = file.read_text(encoding="utf-8-sig").rstrip()
        file.write_text(text + MAIN_GUARD, encoding="utf-8")
    print(f"Added main guards: {len(candidates)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
