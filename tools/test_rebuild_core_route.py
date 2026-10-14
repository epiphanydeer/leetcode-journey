"""Regression checks for source article placement and advanced exercises."""
import unittest

import rebuild_core_route as route


class SourceSelectionTests(unittest.TestCase):
    def test_same_problem_is_kept_in_both_two_pointer_sections(self):
        markdown = """## 三、单序列双指针
### §3.2 相向双指针
- [611. 有效三角形的个数](https://leetcode.cn/problems/valid-triangle-number/)
### §3.3 同向双指针
- [611. 有效三角形的个数](https://leetcode.cn/problems/valid-triangle-number/)
"""
        topic = next(t for t in route.TOPICS if t.folder == "02_two_pointers")
        selected = route.selected_records(route.parse_records(markdown), topic)
        self.assertEqual(
            {record["h3"] for record in selected},
            {"§3.2 相向双指针", "§3.3 同向双指针"},
        )

    def test_advanced_public_exercise_remains_in_scope(self):
        markdown = """## 一、定长滑动窗口
### §1.2 进阶（选做）
- [999. 示例题](https://leetcode.cn/problems/example-problem/)
"""
        topic = next(t for t in route.TOPICS if t.folder == "01_sliding_window")
        selected = route.selected_records(route.parse_records(markdown), topic)
        self.assertEqual([record["slug"] for record in selected], ["example-problem"])

    def test_full_data_structures_article_remains_in_scope(self):
        markdown = """## 六、字典树（trie）
### §6.1 基础
- [208. 实现 Trie](https://leetcode.cn/problems/implement-trie-prefix-tree/)
"""
        topic = next(t for t in route.TOPICS if t.folder == "04_data_structures")
        selected = route.selected_records(route.parse_records(markdown), topic)
        self.assertEqual(route.section_for(selected[0], topic)[0], "29_trie_basics")

    def test_later_dynamic_programming_chapters_remain_in_scope(self):
        markdown = """## 七、其他线性 DP
### §7.1 一维 DP
- [70. 爬楼梯](https://leetcode.cn/problems/climbing-stairs/)
"""
        topic = next(t for t in route.TOPICS if t.folder == "08_dynamic_programming")
        selected = route.selected_records(route.parse_records(markdown), topic)
        self.assertEqual(route.section_for(selected[0], topic)[0], "19_one_dimensional_dp")


if __name__ == "__main__":
    unittest.main()
