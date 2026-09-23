"""
1456. 定长子串中元音的最大数目

给你字符串 s 和整数 k 。
请返回字符串 s 中长度为 k 的单个子字符串中可能包含的最大元音字母数。
英文中的 元音字母 为（a, e, i, o, u）。

【核心思路】
1. 块长固定，左指针自然固定
2. 右指针遍历，是元音就加一，到达固定长度后，左指针开始扔是元音的
"""


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel = ans = 0
        for right, j in enumerate(s):
            left = right - k + 1
            if j in "aeiou":
                vowel += 1
            if left < 0:
                continue
            ans = max(ans, vowel)
            if s[left] in "aeiou":
                vowel -= 1
        return ans


# 快速测试验证
if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ("abciiidef", 3, 3),
        ("aeiou", 2, 2),
        ("leetcode", 3, 2),
        ("rhythms", 4, 0),
    ]

    for s, k, expected in test_cases:
        result = solution.maxVowels(s, k)
        assert result == expected, f"Failed on {s}: expected {expected}, got {result}"
        print(f"Test on '{s}' passed! Result: {result}")
