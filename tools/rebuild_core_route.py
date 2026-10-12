"""Rebuild the repository from the eight-stage core route in Endlesscheng's guide.

This program never deletes topic folders until every selected public problem has
been fetched successfully into a staging directory.  Implemented legacy
solutions are copied to legacy_user_solutions/ before the old topic layout is
removed.  Paid problems are deliberately skipped.  The guide's first topic is
split into Sliding Window and Two Pointers so they can be practised separately.
"""
from __future__ import annotations

import argparse
import ast
import html
import json
import re
import shutil
import time
import urllib.error
import urllib.request
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
STAGE = ROOT / ".core_route_stage"
GRAPHQL = "https://leetcode.cn/graphql/"
UTF8 = "utf-8"

TOPIC_DIRS = [
    "01_sliding_window", "02_two_pointers", "03_binary_search", "04_monotonic_stack",
    "05_grid_graph", "06_bit_manipulation", "07_graph_theory", "08_dynamic_programming",
    "09_data_structures", "10_mathematics", "11_greedy_thinking",
    "12_linked_list_tree_backtracking", "13_string_algorithms",
]

COMMON_IMPORTS = """from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq"""
@dataclass(frozen=True)
class Topic:
    folder: str
    title: str
    source: str | None
    selector: str


TOPICS = [
    Topic("01_sliding_window", "01. 滑动窗口", "https://leetcode.cn/discuss/post/0viNMK/", "sliding"),
    Topic("02_two_pointers", "02. 双指针", "https://leetcode.cn/discuss/post/0viNMK/", "two_pointers"),
    Topic("03_binary_search", "03. 二分查找", "https://leetcode.cn/discuss/post/3579164/ti-dan-er-fen-suan-fa-er-fen-da-an-zui-x-3rqn/", "binary_full"),
    Topic("04_data_structures", "04. 新手村常用工具：数据结构", "https://leetcode.cn/discuss/post/mOr1u6/", "data"),
    Topic("05_binary_tree_dfs", "05. 二叉树 DFS", "https://leetcode.cn/discuss/post/K0n2gO/", "tree_dfs"),
    Topic("06_grid_graph", "06. 网格图", "https://leetcode.cn/discuss/post/3580195/fen-xiang-gun-ti-dan-wang-ge-tu-dfsbfszo-l3pa/", "grid_full"),
    Topic("07_backtracking", "07. 回溯", "https://leetcode.cn/discuss/post/K0n2gO/", "backtracking"),
    Topic("08_dynamic_programming", "08. 动态规划（前六章）", "https://leetcode.cn/discuss/post/tXLS3i/", "dp"),
]

INTRO_TOPIC = Topic(
    "00_programming_fundamentals",
    "00. Programming Fundamentals",
    "https://leetcode.cn/studyplan/primers-list/",
    "intro",
)

# On the first run these replace the thirteen mistaken folders.  On later runs
# they also replace the current eight-stage layout, so a regenerated chapter is
# never moved inside an existing folder with the same name.
REPLACED_TOPIC_DIRS = list(dict.fromkeys(TOPIC_DIRS + [
    "05_grid_graph_dfs", INTRO_TOPIC.folder,
    # Previous core-route names, before Two Pointers was restored as chapter 02.
    "02_binary_search", "03_data_structures", "04_binary_tree_dfs",
    "05_grid_graph", "06_backtracking", "07_dynamic_programming",
    *(topic.folder for topic in TOPICS),
]))

# Only the source article's broad sections become folders.  Its finer-grained
# headings (for example, §2.3.1) remain exercises within that broad section.
SECTIONS: dict[str, dict[str, tuple[str, str]]] = {
    "00_programming_fundamentals": {
        "基础语法 & 数据类型": ("01_basic_syntax_and_data_types", "Basic Syntax and Data Types"),
        "条件判断": ("02_conditionals", "Conditionals"),
        "循环 & 循环嵌套": ("03_loops_and_nested_loops", "Loops and Nested Loops"),
        "数据库基础": ("04_database_basics", "Database Basics"),
        "位运算；ASCII 码": ("05_bit_manipulation_and_ascii", "Bit Manipulation and ASCII"),
        "数学：取余": ("06_math_modulo", "Math: Modulo"),
        "数学：因数与倍数": ("07_math_factors_and_multiples", "Math: Factors and Multiples"),
        "数组 & 矩阵": ("08_arrays_and_matrices", "Arrays and Matrices"),
        "数组 & 字符串": ("09_arrays_and_strings", "Arrays and Strings"),
    },
    "01_sliding_window": {
        "§1.1 基础": ("01_fixed_size", "Fixed-Size Sliding Window"),
        "§2.1 越短越合法/求最长/最大": ("02_variable_longest", "Variable-Size Window: Longest / Maximum"),
        "§2.2 越长越合法/求最短/最小": ("03_variable_shortest", "Variable-Size Window: Shortest / Minimum"),
        "§2.3 求子数组个数": ("04_subarray_count", "Variable-Size Window: Subarray Count"),
    },
    "02_two_pointers": {
        "§3.1 反转字符串": ("01_reverse_string", "Reverse String"),
        "§3.2 相向双指针": ("02_opposite_direction_two_pointers", "Opposite-Direction Two Pointers"),
        "§3.3 同向双指针": ("03_same_direction_two_pointers", "Same-Direction Two Pointers"),
        "§3.4 背向双指针": ("04_away_from_each_other_two_pointers", "Away-From-Each-Other Two Pointers"),
        "§3.5 原地修改": ("05_in_place_modification", "In-Place Modification"),
        "§3.6 矩阵上的双指针": ("06_matrix_two_pointers", "Matrix Two Pointers"),
        "§4.1 双指针": ("07_two_sequences_two_pointers", "Two-Sequence Two Pointers"),
        "§4.2 判断子序列": ("08_subsequence_check", "Subsequence Check"),
        "五、三指针": ("09_three_pointers", "Three Pointers"),
        "六、分组循环": ("10_grouped_iteration", "Grouped Iteration"),
    },
    "03_binary_search": {
        "§1.1 基础": ("01_basic_binary_search", "Basic Binary Search"),
        "§1.2 进阶": ("02_advanced_binary_search", "Advanced Binary Search"),
        "§2.1 求最小": ("03_binary_search_minimum", "Binary Search on the Minimum"),
        "§2.2 求最大": ("04_binary_search_maximum", "Binary Search on the Maximum"),
        "§2.3 二分间接值": ("05_binary_search_indirect_value", "Binary Search on an Indirect Value"),
        "§2.4 最小化最大值": ("06_minimize_the_maximum", "Minimize the Maximum"),
        "§2.5 最大化最小值": ("07_maximize_the_minimum", "Maximize the Minimum"),
        "§2.6 第 K 小/大": ("08_kth_smallest_largest", "K-th Smallest / Largest"),
        "三、三分法": ("09_ternary_search", "Ternary Search"),
        "四、其他": ("10_other_binary_search", "Other Binary-Search Problems"),
    },
    "04_data_structures": {
        "§0.1 枚举右，维护左": ("01_enumerate_right_maintain_left", "Enumerate Right, Maintain Left"),
        "§0.2 枚举中间": ("02_enumerate_middle", "Enumerate the Middle"),
        "§0.3 遍历对角线": ("03_traverse_diagonals", "Traverse Diagonals"),
        "§1.1 基础": ("04_prefix_sum_basics", "Prefix Sum Basics"),
        "§1.2 前缀和与哈希表": ("05_prefix_sum_hash_map", "Prefix Sum and Hash Map"),
        "§1.3 距离和": ("06_prefix_sum_distance_sum", "Prefix-Sum Distance Sum"),
        "§1.4 状态压缩前缀和": ("07_prefix_sum_state_compression", "State-Compressed Prefix Sum"),
        "§1.6 二维前缀和": ("08_two_dimensional_prefix_sum", "Two-Dimensional Prefix Sum"),
        "§3.1 基础": ("09_stack_basics", "Stack Basics"),
        "§3.3 邻项消除": ("10_stack_adjacent_elimination", "Stack: Adjacent Elimination"),
        "§3.4 合法括号字符串（RBS）": ("11_stack_valid_parentheses", "Stack: Valid Parentheses"),
        "§3.5 表达式解析": ("12_stack_expression_parsing", "Stack: Expression Parsing"),
        "§3.6 对顶栈": ("13_stack_two_stacks", "Stack: Two Stacks"),
        "§4.1 基础": ("14_queue_basics", "Queue Basics"),
        "§4.2 设计": ("15_queue_design", "Queue Design"),
        "§4.3 双端队列": ("16_deque", "Deque"),
        "§4.4 单调队列": ("17_monotonic_queue", "Monotonic Queue"),
        "§5.1 基础": ("18_heap_basics", "Heap Basics"),
        "§5.3 第 K 小/大": ("19_heap_kth_smallest_largest", "Heap: K-th Smallest / Largest"),
        "§5.4 重排元素": ("20_heap_rearrange_elements", "Heap: Rearrange Elements"),
        "§5.5 反悔堆": ("21_heap_regret_greedy", "Heap: Regret Greedy"),
        "§5.6 懒删除堆": ("22_heap_lazy_deletion", "Heap: Lazy Deletion"),
        "§5.7 对顶堆（动态第 K 小/大）": ("23_heap_dual_heaps", "Heap: Dual Heaps"),
    },
    "05_binary_tree_dfs": {
        "§2.2 自顶向下 DFS（先序遍历）": ("01_top_down_dfs_preorder", "Top-Down DFS (Preorder)"),
        "§2.3 自底向上 DFS（后序遍历）": ("02_bottom_up_dfs_postorder", "Bottom-Up DFS (Postorder)"),
        "§2.4 自底向上 DFS：删点": ("03_bottom_up_dfs_delete_nodes", "Bottom-Up DFS: Delete Nodes"),
    },
    "06_grid_graph": {
        "一、网格图 DFS": ("01_grid_dfs", "Grid DFS"),
        "二、网格图 BFS": ("02_grid_bfs", "Grid BFS"),
        "三、网格图 0-1 BFS": ("03_grid_zero_one_bfs", "Grid 0-1 BFS"),
        "五、综合应用": ("04_comprehensive_applications", "Comprehensive Applications"),
    },
    "07_backtracking": {
        "§4.1 子集型回溯": ("01_subset_backtracking", "Subset Backtracking"),
        "§4.2 划分型回溯": ("02_partition_backtracking", "Partition Backtracking"),
        "§4.3 组合型回溯": ("03_combination_backtracking", "Combination Backtracking"),
        "§4.4 排列型回溯": ("04_permutation_backtracking", "Permutation Backtracking"),
        "§4.5 有重复元素的回溯": ("05_duplicate_aware_backtracking", "Duplicate-Aware Backtracking"),
        "§4.6 搜索": ("06_search_backtracking", "Search Backtracking"),
        "§4.7 折半搜索": ("07_meet_in_the_middle", "Meet in the Middle"),
    },
    "08_dynamic_programming": {
        "§1.1 爬楼梯": ("01_climbing_stairs", "Climbing Stairs"),
        "§1.2 打家劫舍": ("02_house_robber", "House Robber"),
        "§1.3 最大子数组和（最大子段和）": ("03_maximum_subarray", "Maximum Subarray"),
        "§2.1 基础": ("04_grid_dp_basics", "Grid DP Basics"),
        "§3.1 0-1 背包": ("05_zero_one_knapsack", "0-1 Knapsack"),
        "§3.2 完全背包": ("06_complete_knapsack", "Complete Knapsack"),
        "§3.4 分组背包": ("07_group_knapsack", "Group Knapsack"),
        "§4.1 最长公共子序列（LCS）": ("08_longest_common_subsequence", "Longest Common Subsequence"),
        "§4.2 最长递增子序列（LIS）": ("09_longest_increasing_subsequence", "Longest Increasing Subsequence"),
        "§5.1 判定能否划分": ("10_partition_feasibility", "Partition Feasibility"),
        "§5.2 最优划分": ("11_optimal_partitioning", "Optimal Partitioning"),
        "§5.3 约束划分个数": ("12_constrained_partition_count", "Constrained Partition Count"),
        "§6.1 买卖股票": ("13_stock_trading", "Stock Trading"),
        "§6.2 基础": ("14_state_machine_basics", "State-Machine DP Basics"),
    },
}


def fetch(url: str, data: bytes | None = None) -> bytes:
    request = urllib.request.Request(url, data=data, headers={"User-Agent": "leetcode-journey-core-route/1.0", "Content-Type": "application/json" if data else ""})
    last_error: Exception | None = None
    for attempt in range(5):
        try:
            with urllib.request.urlopen(request, timeout=45) as response:
                return response.read()
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as exc:
            last_error = exc
            time.sleep(min(16, 2**attempt))
    raise RuntimeError(f"Cannot fetch {url}: {last_error}")


def article_markdown(url: str) -> str:
    raw = fetch(url).decode(UTF8)
    matches = re.findall(r'"content":"((?:\\.|[^"\\])*)"', raw)
    if not matches:
        raise RuntimeError(f"Article body not found: {url}")
    candidates = []
    for value in matches:
        try:
            candidates.append(json.loads('{"content":"' + value + '"}')["content"])
        except json.JSONDecodeError:
            pass
    return max(candidates, key=len)


def intro_records() -> list[dict]:
    query = """query { studyPlanV2Detail(planSlug: \"primers-list\") {
        planSubGroups { name questions { questionFrontendId titleSlug translatedTitle } }
    }}"""
    payload = json.loads(fetch(GRAPHQL, json.dumps({"query": query}).encode(UTF8)).decode(UTF8))
    groups = payload.get("data", {}).get("studyPlanV2Detail", {}).get("planSubGroups", [])
    records = []
    for group in groups:
        for question in group.get("questions", []):
            records.append({
                "id": question["questionFrontendId"],
                "title": question["translatedTitle"],
                "slug": question["titleSlug"],
                "tail": "", "rating": None,
                "h2": group["name"], "h3": "", "h4": "",
            })
    return records


def safe_name(value: str) -> str:
    value = re.sub(r'[\\/:*?"<>|]', "_", value)
    return re.sub(r"\s+", "_", value).strip(" .")


def parse_records(markdown: str) -> list[dict]:
    h2 = h3 = h4 = ""
    records = []
    for raw in markdown.splitlines():
        line = raw.strip()
        heading = re.match(r"^(#{2,4})\s+(.+?)\s*$", line)
        if heading:
            level, text = len(heading.group(1)), heading.group(2)
            if level == 2:
                h2, h3, h4 = text, "", ""
            elif level == 3:
                h3, h4 = text, ""
            else:
                h4 = text
            continue
        if not re.match(r"^[-*]\s+", line):
            continue
        for match in re.finditer(r"\[([^\]]+)\]\(https://leetcode\.cn/problems/([^/\)]+)/?[^\)]*\)", line):
            display, slug = match.groups()
            id_match = re.match(r"^(.+?)\.\s*(.+)$", display)
            if not id_match:
                continue
            tail = line[match.end():]
            rating_match = re.search(r"(?<!\d)(1\d{3}|2\d{3})(?!\d)", tail)
            records.append({
                "id": id_match.group(1).strip(), "title": id_match.group(2).strip(), "slug": slug,
                "tail": tail, "rating": int(rating_match.group(1)) if rating_match else None,
                "h2": h2, "h3": h3, "h4": h4,
            })
    return records


def optional(record: dict) -> bool:
    return any(word in " ".join((record["h2"], record["h3"], record["h4"], record["tail"])) for word in ("进阶", "选做", "思维扩展", "相似题目"))


def selected(record: dict, topic: Topic) -> bool:
    h2, h3 = record["h2"], record["h3"]
    if topic.selector in ("binary_full", "grid_full"):
        return True
    if topic.selector == "two_pointers":
        return h2.startswith(("三、", "四、", "五、", "六、"))
    if optional(record):
        return False
    if topic.selector == "sliding":
        return h2.startswith(("一、", "二、"))
    if topic.selector == "binary":
        return h2.startswith("一、")
    if topic.selector == "data":
        return h2.startswith(("零、", "一、", "三、", "四、", "五、"))
    if topic.selector == "tree_dfs":
        return h2.startswith("二、") and "DFS" in h3
    if topic.selector == "grid_dfs":
        return h2.startswith("一、")
    if topic.selector == "backtracking":
        return h2.startswith("四、")
    if topic.selector == "dp":
        return h2.startswith(("一、", "二、", "三、", "四、", "五、", "六、"))
    return False


def gql_questions(slugs: list[str]) -> dict[str, dict]:
    answer: dict[str, dict] = {}
    for start in range(0, len(slugs), 20):
        batch = slugs[start:start + 20]
        fields = " ".join(
            f'q{i}: question(titleSlug: "{slug}") {{ questionFrontendId translatedTitle translatedContent isPaidOnly difficulty codeSnippets {{ langSlug code }} }}'
            for i, slug in enumerate(batch)
        )
        body = json.dumps({"query": "query coreRoute { " + fields + " }"}, ensure_ascii=False).encode(UTF8)
        payload = json.loads(fetch(GRAPHQL, body).decode(UTF8))
        for i, slug in enumerate(batch):
            question = payload.get("data", {}).get(f"q{i}")
            if question:
                answer[slug] = question
        print(f"Fetched metadata {min(start + 20, len(slugs))}/{len(slugs)}")
    return answer


def plain_description(content: str | None) -> str:
    if not content:
        return "（力扣未返回中文题目描述。）"
    content = re.split(r"(?is)<p>\s*(?:<strong>)?\s*(?:示例|example)", content, maxsplit=1)[0]
    content = re.sub(r"(?i)<br\s*/?>", "\n", content)
    content = re.sub(r"(?i)</(?:p|li)\s*>", "\n", content)
    content = re.sub(r"<[^>]+>", "", content)
    content = html.unescape(content)
    content = re.sub(r"[ \t]+", " ", content)
    return re.sub(r"\n{3,}", "\n\n", content).strip().replace("\\", "\\\\").replace("'''", "\\'\\'\\'")


def fill_empty_python_bodies(code: str) -> str:
    """Make LeetCode's blank starter methods valid Python without changing signatures."""
    lines = code.splitlines()
    result = []
    header = re.compile(r"^(\s*)(?:async\s+def|def|class)\s+.*:\s*$")
    for index, line in enumerate(lines):
        result.append(line)
        match = header.match(line)
        if not match:
            continue
        base_indent = len(match.group(1).expandtabs(4))
        has_body = False
        for following in lines[index + 1:]:
            stripped = following.strip()
            if not stripped or stripped.startswith("#"):
                continue
            indentation = len(following) - len(following.lstrip(" \t"))
            has_body = indentation > base_indent
            break
        if not has_body:
            result.append(" " * (base_indent + 4) + "pass")
    return "\n".join(result)


def main_guard(starter_code: str) -> str:
    match = re.search(r"^class\s+(\w+)", starter_code, flags=re.MULTILINE)
    if not match or match.group(1) == "Solution":
        setup = "solution = Solution()"
    else:
        class_name = match.group(1)
        setup = f"# LeetCode design problem: provide the constructor arguments if required.\n    # solution = {class_name}(...)\n    pass"
    return f"# 快速测试验证\nif __name__ == \"__main__\":\n    {setup}"


def starter(question: dict) -> tuple[str, str] | None:
    for preferred in ("python", "python3"):
        for snippet in question.get("codeSnippets") or []:
            if snippet.get("langSlug", "").lower() == preferred and snippet.get("code", "").strip():
                code = snippet["code"].replace("\r\n", "\n").rstrip()
                return ".py", fill_empty_python_bodies(code)
    for preferred in ("mysql", "mssql", "postgresql"):
        for snippet in question.get("codeSnippets") or []:
            if snippet.get("langSlug", "").lower() == preferred and snippet.get("code", "").strip():
                return ".sql", snippet["code"].replace("\r\n", "\n").rstrip()
    return None


def problem_file_name(question: dict) -> str:
    selected = starter(question)
    extension = selected[0] if selected else ".py"
    return f"lc_{safe_name(str(question['questionFrontendId']))}_{safe_name(question['translatedTitle'])}{extension}"


def is_implemented(path: Path) -> bool:
    try:
        tree = ast.parse(path.read_text(encoding="utf-8-sig"))
    except SyntaxError:
        return True
    for method in (node for node in ast.walk(tree) if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))):
        body = list(method.body)
        if body and isinstance(body[0], ast.Expr) and isinstance(body[0].value, ast.Constant) and isinstance(body[0].value.value, str):
            body.pop(0)
        if any(not isinstance(statement, ast.Pass) for statement in body):
            return True
    return False


def is_valid_implemented_solution(path: Path) -> bool:
    """Only a syntactically valid handwritten file may replace a fresh starter."""
    try:
        ast.parse(path.read_text(encoding="utf-8-sig"))
    except SyntaxError:
        return False
    return is_implemented(path)


def implemented_files_by_id() -> dict[str, Path]:
    """Find existing handwritten solutions so they can follow a problem into its new topic."""
    result: dict[str, Path] = {}
    for folder_name in REPLACED_TOPIC_DIRS:
        folder = ROOT / folder_name
        if not folder.exists():
            continue
        for file in folder.rglob("lc_*.py"):
            match = re.match(r"lc_(\d+)_", file.name)
            if match and is_valid_implemented_solution(file):
                result.setdefault(match.group(1), file)
    return result


def section_for(record: dict, topic: Topic) -> tuple[str, str]:
    key = record["h3"] or record["h2"]
    try:
        return SECTIONS[topic.folder][key]
    except KeyError as exc:
        raise RuntimeError(f"No folder mapping for {topic.folder}: {key!r}") from exc


def write_template(folder: Path, title: str) -> None:
    content = f"""# {title} Template

Use the problem-specific `class Solution` signature in each exercise file. Keep
the reusable state and invariant for this pattern here as you learn it.

```python
from typing import *


class Solution:
    def solve(self, *args, **kwargs):
        # Define the invariant, update state, then return the answer.
        pass
```
"""
    (folder / "templates.md").write_text(content, encoding=UTF8)


def write_readme(folder: Path, topic: Topic, records: list[tuple[dict, dict]]) -> None:
    lines = [f"# {topic.title}", "", f"Source: [{topic.source}]({topic.source})", "", "This core-route collection contains every public problem in the selected sections. Paid problems are skipped; there is no rating limit."]
    grouped: dict[tuple[str, str], list[tuple[dict, dict]]] = {}
    for source, question in records:
        grouped.setdefault(section_for(source, topic), []).append((source, question))
    for (section_folder, section_title), problems in grouped.items():
        lines.extend(["", f"## {section_title}", "", f"[Templates](./{section_folder}/templates.md)", "", "| ID | Problem | Difficulty | Solution |", "| :--: | :-- | :--: | :--: |"])
        for source, question in problems:
            title = question["translatedTitle"]
            file = problem_file_name(question)
            language = "SQL" if file.endswith(".sql") else "Python"
            lines.append(f"| {question['questionFrontendId']} | [{title}](https://leetcode.cn/problems/{source['slug']}/) | {question['difficulty']} | [{language}](<./{section_folder}/{file}>) |")
    (folder / "README.md").write_text("\n".join(lines) + "\n", encoding=UTF8)


def apply_staged() -> None:
    """Archive handwritten work, then replace only the obsolete topic directories."""
    if not STAGE.exists():
        raise RuntimeError(f"Staged output does not exist: {STAGE}")
    legacy = ROOT / "legacy_user_solutions"
    manifest = []
    for folder_name in REPLACED_TOPIC_DIRS:
        old = ROOT / folder_name
        if not old.exists():
            continue
        for file in old.rglob("lc_*.py"):
            if is_implemented(file):
                relative = file.relative_to(ROOT)
                destination = legacy / relative
                destination.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(file, destination)
                manifest.append(str(relative))
    if manifest:
        legacy.mkdir(exist_ok=True)
        (legacy / "MIGRATED_FILES.md").write_text("# Preserved legacy solutions\n\n" + "\n".join(f"- `{entry}`" for entry in manifest) + "\n", encoding=UTF8)

    for folder_name in REPLACED_TOPIC_DIRS:
        target = ROOT / folder_name
        if target.exists():
            shutil.rmtree(target)
    for folder in sorted(STAGE.iterdir()):
        shutil.move(str(folder), ROOT / folder.name)
    shutil.rmtree(STAGE)
    (ROOT / "README.md").write_text("# LeetCode Journey\n\nBuilt from the [eight-stage core route](https://leetcode.cn/discuss/post/3141566/ru-he-ke-xue-shua-ti-by-endlesscheng-q3yd/).\n\nThe guide groups sliding-window and two-pointer problems in one source article; this repository separates them into `01_sliding_window` and `02_two_pointers` for focused practice. All public problems in the selected sections are included, paid problems are skipped, and a problem that appears in more than one topic only needs to be solved once.\n", encoding=UTF8)
    print("Migration complete.")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true", help="Replace the old topic layout after a complete staged build.")
    parser.add_argument("--apply-staged", action="store_true", help="Apply an already validated staged build without fetching again.")
    args, _ = parser.parse_known_args()
    if args.apply and args.apply_staged:
        parser.error("Use either --apply or --apply-staged, not both.")
    if args.apply_staged:
        apply_staged()
        return

    selected_by_topic: dict[str, list[dict]] = {INTRO_TOPIC.folder: intro_records()}
    for topic in TOPICS:
        records = parse_records(article_markdown(topic.source))
        candidates = [record for record in records if selected(record, topic)]
        selected_by_topic[topic.folder] = list({record["slug"]: record for record in candidates}.values())

    all_slugs = list(dict.fromkeys(record["slug"] for records in selected_by_topic.values() for record in records))
    questions = gql_questions(all_slugs)
    existing_implementations = implemented_files_by_id()
    if STAGE.exists():
        shutil.rmtree(STAGE)
    STAGE.mkdir()

    final_by_topic: dict[str, list[tuple[dict, dict]]] = {}
    for topic in [INTRO_TOPIC, *TOPICS]:
        final = []
        folder = STAGE / topic.folder
        folder.mkdir()
        created_sections: set[tuple[str, str]] = set()
        for source in selected_by_topic[topic.folder]:
            question = questions.get(source["slug"])
            if not question or question.get("isPaidOnly"):
                continue
            selected_starter = starter(question)
            if not selected_starter:
                continue
            extension, starter_code = selected_starter
            title = question["translatedTitle"]
            section_folder, section_title = section_for(source, topic)
            problem_folder = folder / section_folder
            problem_folder.mkdir(exist_ok=True)
            created_sections.add((section_folder, section_title))
            file = problem_folder / problem_file_name(question)
            existing = existing_implementations.get(str(question["questionFrontendId"]))
            if existing and extension == ".py":
                shutil.copy2(existing, file)
            elif extension == ".sql":
                content = f"-- {question['questionFrontendId']}. {title}\n/*\n{plain_description(question.get('translatedContent'))}\n*/\n\n{starter_code}\n"
                file.write_text(content, encoding=UTF8)
            else:
                content = f"# {question['questionFrontendId']}. {title}\n'''\n{plain_description(question.get('translatedContent'))}\n'''\n\n{COMMON_IMPORTS}\n\n{starter_code}\n\n{main_guard(starter_code)}\n"
                file.write_text(content, encoding=UTF8)
            final.append((source, question))
        for section_folder, section_title in created_sections:
            write_template(folder / section_folder, section_title)
        write_readme(folder, topic, final)
        final_by_topic[topic.folder] = final
        print(f"{topic.folder}: {len(final)} public problems")

    if not args.apply:
        print(f"\nStaged output is ready at: {STAGE}\nRun again with --apply to replace the old topic folders.")
        return
    apply_staged()


if __name__ == "__main__":
    main()
