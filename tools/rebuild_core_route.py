"""Rebuild the repository from the eight-stage core route in Endlesscheng's guide.

This program fetches every selected public problem into a staging directory,
then adds missing exercise files and refreshes topic indexes. Existing exercise
files and templates are preserved. Paid problems are deliberately skipped.
The guide's first topic is split into Sliding Window and Two Pointers.
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
    Topic("05_linked_list_tree", "05. 链表与树（含递归/分治）", "https://leetcode.cn/discuss/post/K0n2gO/", "linked_list_tree"),
    Topic("06_grid_graph", "06. 网格图", "https://leetcode.cn/discuss/post/3580195/fen-xiang-gun-ti-dan-wang-ge-tu-dfsbfszo-l3pa/", "grid_full"),
    Topic("07_backtracking", "07. 回溯", "https://leetcode.cn/discuss/post/K0n2gO/", "backtracking"),
    Topic("08_dynamic_programming", "08. 动态规划", "https://leetcode.cn/discuss/post/tXLS3i/", "dp"),
]

INTRO_TOPIC = Topic(
    "00_programming_fundamentals",
    "00. Programming Fundamentals",
    "https://leetcode.cn/studyplan/primers-list/",
    "intro",
)

# Historical and current topic locations are searched for handwritten solutions
# when staging a fresh exercise file.
REPLACED_TOPIC_DIRS = list(dict.fromkeys(TOPIC_DIRS + [
    "05_grid_graph_dfs", "05_binary_tree_dfs", INTRO_TOPIC.folder,
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
        "§1.2 进阶（选做）": ("05_fixed_size_advanced", "Fixed-Size Sliding Window: Advanced"),
        "§2.1 越短越合法/求最长/最大": ("02_variable_longest", "Variable-Size Window: Longest / Maximum"),
        "§2.2 越长越合法/求最短/最小": ("03_variable_shortest", "Variable-Size Window: Shortest / Minimum"),
        "§2.3 求子数组个数": ("04_subarray_count", "Variable-Size Window: Subarray Count"),
        "§2.4 其他（选做）": ("06_other_sliding_window", "Other Sliding-Window Problems"),
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
        "§1.5 进阶": ("24_prefix_sum_advanced", "Prefix Sum: Advanced"),
        "§1.6 二维前缀和": ("08_two_dimensional_prefix_sum", "Two-Dimensional Prefix Sum"),
        "§3.1 基础": ("09_stack_basics", "Stack Basics"),
        "§3.2 进阶": ("25_stack_advanced", "Stack: Advanced"),
        "§3.3 邻项消除": ("10_stack_adjacent_elimination", "Stack: Adjacent Elimination"),
        "§3.4 合法括号字符串（RBS）": ("11_stack_valid_parentheses", "Stack: Valid Parentheses"),
        "§3.5 表达式解析": ("12_stack_expression_parsing", "Stack: Expression Parsing"),
        "§3.6 对顶栈": ("13_stack_two_stacks", "Stack: Two Stacks"),
        "§4.1 基础": ("14_queue_basics", "Queue Basics"),
        "§4.2 设计": ("15_queue_design", "Queue Design"),
        "§4.3 双端队列": ("16_deque", "Deque"),
        "§4.4 单调队列": ("17_monotonic_queue", "Monotonic Queue"),
        "§5.1 基础": ("18_heap_basics", "Heap Basics"),
        "§5.2 进阶": ("26_heap_advanced", "Heap: Advanced"),
        "§5.3 第 K 小/大": ("19_heap_kth_smallest_largest", "Heap: K-th Smallest / Largest"),
        "§5.4 重排元素": ("20_heap_rearrange_elements", "Heap: Rearrange Elements"),
        "§5.5 反悔堆": ("21_heap_regret_greedy", "Heap: Regret Greedy"),
        "§5.6 懒删除堆": ("22_heap_lazy_deletion", "Heap: Lazy Deletion"),
        "§5.7 对顶堆（动态第 K 小/大）": ("23_heap_dual_heaps", "Heap: Dual Heaps"),
        "§2.1 一维差分": ("27_one_dimensional_difference", "One-Dimensional Difference Array"),
        "§2.2 二维差分": ("28_two_dimensional_difference", "Two-Dimensional Difference Array"),
        "§6.1 基础": ("29_trie_basics", "Trie Basics"),
        "§6.2 进阶": ("30_trie_advanced", "Trie: Advanced"),
        "§6.3 字典树优化 DP": ("31_trie_optimized_dp", "Trie-Optimized DP"),
        "§6.4 0-1 字典树（异或字典树）": ("32_bitwise_trie", "Bitwise Trie"),
        "§7.1 基础": ("33_union_find_basics", "Union-Find Basics"),
        "§7.2 进阶": ("34_union_find_advanced", "Union-Find: Advanced"),
        "§7.3 中介并查集": ("35_intermediary_union_find", "Intermediary Union-Find"),
        "§7.4 数组上的并查集": ("36_array_union_find", "Union-Find on Arrays"),
        "§7.5 区间并查集": ("37_interval_union_find", "Interval Union-Find"),
        "§7.6 带权并查集（边权并查集）": ("38_weighted_union_find", "Weighted Union-Find"),
        "§8.1 树状数组": ("39_fenwick_tree", "Fenwick Tree"),
        "§8.2 逆序对": ("40_inversion_count", "Inversion Count"),
        "§8.3 线段树（无区间更新）": ("41_segment_tree", "Segment Tree"),
        "§8.4 Lazy 线段树（有区间更新）": ("42_lazy_segment_tree", "Lazy Segment Tree"),
        "§8.5 动态开点线段树": ("43_dynamic_segment_tree", "Dynamic Segment Tree"),
        "§8.6 可持久化线段树": ("44_persistent_segment_tree", "Persistent Segment Tree"),
        "§8.7 ST 表（Sparse Table）": ("45_sparse_table", "Sparse Table"),
        "九、伸展树（Splay 树）": ("46_splay_tree", "Splay Tree"),
        "十、CDQ 分治 / 值域分治": ("47_cdq_divide_and_conquer", "CDQ and Value-Domain Divide and Conquer"),
        "§11.1 分块": ("48_block_decomposition", "Block Decomposition"),
        "§11.2 莫队算法": ("49_mos_algorithm", "Mo's Algorithm"),
        "§11.3 根号分解（Sqrt Decomposition）": ("50_sqrt_decomposition", "Square-Root Decomposition"),
        "§11.4 其他": ("51_other_sqrt_algorithms", "Other Square-Root Algorithms"),
        "专题：离线算法": ("52_offline_algorithms", "Offline Algorithms"),
        "Part A": ("53_programming_drills_a", "Programming Drills A"),
        "Part B": ("54_programming_drills_b", "Programming Drills B"),
        "Part C": ("55_programming_drills_c", "Programming Drills C"),
    },
    "05_linked_list_tree": {
        "§1.1 遍历链表": ("01_traverse_linked_list", "Traverse Linked Lists"),
        "§1.2 删除节点": ("02_delete_linked_list_nodes", "Delete Linked-List Nodes"),
        "§1.3 插入节点": ("03_insert_linked_list_nodes", "Insert Linked-List Nodes"),
        "§1.4 反转链表": ("04_reverse_linked_list", "Reverse Linked Lists"),
        "§1.5 前后指针": ("05_leading_and_trailing_pointers", "Leading and Trailing Pointers"),
        "§1.6 快慢指针": ("06_fast_and_slow_pointers", "Fast and Slow Pointers"),
        "§1.7 双指针": ("07_linked_list_two_pointers", "Linked-List Two Pointers"),
        "§1.8 合并链表": ("08_merge_linked_lists", "Merge Linked Lists"),
        "§1.9 分治": ("09_linked_list_divide_and_conquer", "Linked-List Divide and Conquer"),
        "§1.10 综合应用": ("10_linked_list_applications", "Linked-List Applications"),
        "§1.11 其他": ("11_other_linked_list", "Other Linked-List Problems"),
        "§2.1 遍历二叉树": ("12_binary_tree_traversal", "Binary-Tree Traversal"),
        "§2.2 自顶向下 DFS（先序遍历）": ("13_top_down_dfs_preorder", "Top-Down DFS (Preorder)"),
        "§2.3 自底向上 DFS（后序遍历）": ("14_bottom_up_dfs_postorder", "Bottom-Up DFS (Postorder)"),
        "§2.4 自底向上 DFS：删点": ("15_bottom_up_dfs_delete_nodes", "Bottom-Up DFS: Delete Nodes"),
        "§2.5 有递有归": ("16_binary_tree_pre_and_post_order", "Binary-Tree Preorder and Postorder"),
        "§2.6 二叉树的直径": ("17_binary_tree_diameter", "Binary-Tree Diameter"),
        "§2.7 回溯": ("18_binary_tree_backtracking", "Binary-Tree Backtracking"),
        "§2.8 最近公共祖先": ("19_binary_tree_lca", "Binary-Tree Lowest Common Ancestor"),
        "§2.9 二叉搜索树": ("20_binary_search_tree", "Binary Search Tree"),
        "§2.10 创建二叉树": ("21_construct_binary_tree", "Construct Binary Trees"),
        "§2.11 插入/删除节点": ("22_insert_delete_tree_nodes", "Insert and Delete Tree Nodes"),
        "§2.12 树形 DP": ("23_binary_tree_dp", "Binary-Tree DP"),
        "§2.13 二叉树 BFS": ("24_binary_tree_bfs", "Binary-Tree BFS"),
        "§2.14 链表+二叉树": ("25_linked_list_and_binary_tree", "Linked Lists and Binary Trees"),
        "§2.15 N 叉树": ("26_n_ary_tree", "N-ary Trees"),
        "§2.16 其他": ("27_other_binary_tree", "Other Binary-Tree Problems"),
        "§3.1 遍历": ("28_general_tree_traversal", "General-Tree Traversal"),
        "§3.2 自顶向下 DFS": ("29_general_tree_top_down_dfs", "General-Tree Top-Down DFS"),
        "§3.3 自底向上 DFS": ("30_general_tree_bottom_up_dfs", "General-Tree Bottom-Up DFS"),
        "§3.4 有递有归": ("31_general_tree_pre_and_post_order", "General-Tree Preorder and Postorder"),
        "§3.5 树的直径": ("32_general_tree_diameter", "General-Tree Diameter"),
        "§3.6 树的拓扑排序": ("33_tree_topological_sort", "Tree Topological Sort"),
        "§3.7 DFS 时间戳": ("34_dfs_timestamps", "DFS Timestamps"),
        "§3.8 最近公共祖先（LCA）、倍增算法": ("35_general_tree_lca", "General-Tree LCA and Binary Lifting"),
        "§3.9 虚树": ("36_virtual_tree", "Virtual Trees"),
        "§3.10 树上启发式合并": ("37_small_to_large_merging", "Small-to-Large Tree Merging"),
        "§3.11 点分治": ("38_centroid_decomposition", "Centroid Decomposition"),
        "§3.12 树上滑动窗口": ("39_tree_sliding_window", "Sliding Window on Trees"),
        "§3.13 其他": ("40_other_general_tree", "Other General-Tree Problems"),
        "五、其他递归/分治": ("41_other_recursion_divide_and_conquer", "Other Recursion and Divide and Conquer"),
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
        "§2.2 进阶": ("15_grid_dp_advanced", "Grid DP: Advanced"),
        "§3.1 0-1 背包": ("05_zero_one_knapsack", "0-1 Knapsack"),
        "§3.2 完全背包": ("06_complete_knapsack", "Complete Knapsack"),
        "§3.3 多重背包（选做）": ("16_multiple_knapsack", "Multiple Knapsack"),
        "§3.4 分组背包": ("07_group_knapsack", "Group Knapsack"),
        "§3.5 树上背包（选做）": ("17_tree_knapsack", "Tree Knapsack"),
        "§4.1 最长公共子序列（LCS）": ("08_longest_common_subsequence", "Longest Common Subsequence"),
        "§4.2 最长递增子序列（LIS）": ("09_longest_increasing_subsequence", "Longest Increasing Subsequence"),
        "§5.1 判定能否划分": ("10_partition_feasibility", "Partition Feasibility"),
        "§5.2 最优划分": ("11_optimal_partitioning", "Optimal Partitioning"),
        "§5.3 约束划分个数": ("12_constrained_partition_count", "Constrained Partition Count"),
        "§6.1 买卖股票": ("13_stock_trading", "Stock Trading"),
        "§6.2 基础": ("14_state_machine_basics", "State-Machine DP Basics"),
        "§6.3 进阶": ("18_state_machine_advanced", "State-Machine DP: Advanced"),
        "§7.1 一维 DP": ("19_one_dimensional_dp", "One-Dimensional DP"),
        "§7.2 不相交区间": ("20_non_overlapping_intervals_dp", "DP on Non-Overlapping Intervals"),
        "§7.3 子数组 DP": ("21_subarray_dp", "Subarray DP"),
        "§7.4 合法子序列 DP": ("22_valid_subsequence_dp", "Valid-Subsequence DP"),
        "§7.5 子矩形 DP": ("23_subrectangle_dp", "Subrectangle DP"),
        "§7.6 多维 DP": ("24_multidimensional_dp", "Multidimensional DP"),
        "§7.7 计数 DP": ("25_counting_dp", "Counting DP"),
        "§8.1 最长回文子序列": ("26_longest_palindromic_subsequence", "Longest Palindromic Subsequence"),
        "§8.2 区间 DP": ("27_interval_dp", "Interval DP"),
        "§9.1 排列型状压 DP ① 相邻无关": ("28_permutation_bitmask_dp_independent", "Permutation Bitmask DP: Independent Neighbors"),
        "§9.2 排列型状压 DP ② 相邻相关": ("29_permutation_bitmask_dp_dependent", "Permutation Bitmask DP: Dependent Neighbors"),
        "§9.3 旅行商问题（TSP）": ("30_traveling_salesperson", "Traveling Salesperson Problem"),
        "§9.4 子集状压 DP": ("31_subset_bitmask_dp", "Subset Bitmask DP"),
        "§9.5 轮廓线 DP": ("32_profile_dp", "Profile DP"),
        "§9.6 SOS DP": ("33_sos_dp", "Sum Over Subsets DP"),
        "§9.7 其他状压 DP": ("34_other_bitmask_dp", "Other Bitmask DP"),
        "§10.1 统计合法元素的数目": ("35_digit_dp_count", "Digit DP: Count Valid Numbers"),
        "§10.2 统计合法元素的价值总和": ("36_digit_dp_value_sum", "Digit DP: Sum Values"),
        "§10.3 其他数位 DP": ("37_other_digit_dp", "Other Digit DP"),
        "§11.1 前缀和优化 DP": ("38_prefix_sum_optimized_dp", "Prefix-Sum-Optimized DP"),
        "§11.2 单调栈优化 DP": ("39_monotonic_stack_optimized_dp", "Monotonic-Stack-Optimized DP"),
        "§11.3 单调队列优化 DP": ("40_monotonic_queue_optimized_dp", "Monotonic-Queue-Optimized DP"),
        "§11.4 树状数组/线段树优化 DP": ("41_tree_optimized_dp", "Fenwick/Segment-Tree-Optimized DP"),
        "§11.5 字典树优化 DP": ("42_trie_optimized_dp", "Trie-Optimized DP"),
        "§11.6 矩阵快速幂优化 DP": ("43_matrix_exponentiation_dp", "Matrix-Exponentiation-Optimized DP"),
        "§11.7 斜率优化 DP": ("44_convex_hull_trick_dp", "Convex-Hull-Trick DP"),
        "§11.8 WQS 二分优化 DP": ("45_wqs_binary_search_dp", "WQS Binary-Search-Optimized DP"),
        "§11.9 其他优化 DP": ("46_other_dp_optimizations", "Other DP Optimizations"),
        "§12.1 树的直径": ("47_tree_diameter_dp", "Tree Diameter DP"),
        "§12.2 树上最大独立集": ("48_tree_maximum_independent_set", "Maximum Independent Set on Trees"),
        "§12.3 树上最小支配集": ("49_tree_minimum_dominating_set", "Minimum Dominating Set on Trees"),
        "§12.4 换根 DP": ("50_rerooting_dp", "Rerooting DP"),
        "§12.5 其他树形 DP": ("51_other_tree_dp", "Other Tree DP"),
        "十三、图 DP": ("52_graph_dp", "Graph DP"),
        "十四、博弈 DP": ("53_game_dp", "Game DP"),
        "十五、概率 DP、期望 DP": ("54_probability_expected_value_dp", "Probability and Expected-Value DP"),
        "专题：输出具体方案（打印方案）": ("55_reconstruct_dp_solution", "Reconstruct the DP Solution"),
        "专题：前后缀分解": ("56_prefix_suffix_decomposition", "Prefix-Suffix Decomposition"),
        "专题：跳跃游戏": ("57_jump_game_dp", "Jump Game DP"),
        "其他": ("58_other_dp", "Other DP Problems"),
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


def selected(record: dict, topic: Topic) -> bool:
    h2, h3 = record["h2"], record["h3"]
    if topic.selector in ("binary_full", "grid_full", "data", "dp"):
        return True
    if topic.selector == "two_pointers":
        return h2.startswith(("三、", "四、", "五、", "六、"))
    if topic.selector == "sliding":
        return h2.startswith(("一、", "二、"))
    if topic.selector == "linked_list_tree":
        return not h2.startswith("四、")
    if topic.selector == "backtracking":
        return h2.startswith("四、")
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


def implemented_files_by_id(question_ids: set[str]) -> dict[str, Path]:
    """Find existing handwritten solutions so they can follow a problem into its new topic."""
    result: dict[str, Path] = {}
    prefixes = sorted(
        ((f"lc_{safe_name(question_id)}_", question_id) for question_id in question_ids),
        key=lambda item: len(item[0]), reverse=True,
    )
    for folder_name in REPLACED_TOPIC_DIRS:
        folder = ROOT / folder_name
        if not folder.exists():
            continue
        for file in folder.rglob("lc_*.py"):
            question_id = next((question_id for prefix, question_id in prefixes if file.name.startswith(prefix)), None)
            if question_id and is_valid_implemented_solution(file):
                result.setdefault(question_id, file)
    return result


def section_for(record: dict, topic: Topic) -> tuple[str, str]:
    key = record["h3"] or record["h2"]
    try:
        return SECTIONS[topic.folder][key]
    except KeyError as exc:
        raise RuntimeError(f"No folder mapping for {topic.folder}: {key!r}") from exc


def selected_records(records: list[dict], topic: Topic) -> list[dict]:
    """Keep each problem once per broad section, preserving cross-section listings."""
    candidates = [record for record in records if selected(record, topic)]
    return list({(record["slug"], section_for(record, topic)[0]): record for record in candidates}.values())


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


def write_overview() -> None:
    """Summarize the synchronized topic indexes without counting repeats twice."""
    lines = [
        "# LeetCode Journey", "",
        "题目来源：[如何科学刷题？](https://leetcode.cn/discuss/post/3141566/ru-he-ke-xue-shua-ti-by-endlesscheng-q3yd/)的八阶段路线及所链接题单。",
        "按原题单完整章节收录非会员题；滑窗与双指针、链表与树及回溯分别建目录。跨章节重复出现的题只需做一次。",
        "", "| 专题 | 题目位置 |", "| :-- | --: |",
    ]
    all_slugs: set[str] = set()
    placements = 0
    for topic in [INTRO_TOPIC, *TOPICS]:
        readme = (ROOT / topic.folder / "README.md").read_text(encoding=UTF8)
        slugs = re.findall(r"https://leetcode\.cn/problems/([^/]+)/", readme)
        placements += len(slugs)
        all_slugs.update(slugs)
        lines.append(f"| [{topic.title}](./{topic.folder}/README.md) | {len(slugs)} |")
    lines.extend(["", f"合计 **{placements} 个题目位置，{len(all_slugs)} 道不同题**（含编程入门）。会员题暂不收录。", ""])
    (ROOT / "README.md").write_text("\n".join(lines), encoding=UTF8)


def apply_staged() -> None:
    """Refresh indexes and add missing files without overwriting exercise work."""
    if not (STAGE / ".build_complete").exists():
        raise RuntimeError(f"Complete staged output does not exist: {STAGE}")
    added = indexed = preserved = 0
    for source in sorted(STAGE.rglob("*")):
        if not source.is_file() or not (
            source.name in ("README.md", "templates.md")
            or (source.name.startswith("lc_") and source.suffix in (".py", ".sql"))
        ):
            continue
        target = ROOT / source.relative_to(STAGE)
        target.parent.mkdir(parents=True, exist_ok=True)
        if source.name == "README.md":
            shutil.copy2(source, target)
            indexed += 1
        elif target.exists():
            preserved += 1
        else:
            shutil.copy2(source, target)
            added += 1
    shutil.rmtree(STAGE)
    write_overview()
    print(f"Sync complete: {added} added, {indexed} indexes refreshed, {preserved} existing exercise/template files preserved.")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true", help="Sync a complete staged build into the current topic layout.")
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
        selected_by_topic[topic.folder] = selected_records(records, topic)

    all_slugs = list(dict.fromkeys(record["slug"] for records in selected_by_topic.values() for record in records))
    questions = gql_questions(all_slugs)
    existing_implementations = implemented_files_by_id({
        str(question["questionFrontendId"]) for question in questions.values()
    })
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

    (STAGE / ".build_complete").write_text("complete\n", encoding=UTF8)
    if not args.apply:
        print(f"\nStaged output is ready at: {STAGE}\nRun again with --apply-staged to sync the new files and indexes.")
        return
    apply_staged()


if __name__ == "__main__":
    main()
