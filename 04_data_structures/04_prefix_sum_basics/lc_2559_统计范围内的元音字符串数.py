# 2559. 统计范围内的元音字符串数
"""
给你一个下标从 0 开始的字符串数组 words 以及一个二维整数数组 queries 。

每个查询 queries[i] = [li, ri] 会要求我们统计在 words 中下标在 li 到 ri 范围内（包含 这两个值）并且以元音开头和结尾的字符串的数目。

返回一个整数数组，其中数组的第 i 个元素对应第 i 个查询的答案。

注意：元音字母是 'a'、'e'、'i'、'o' 和 'u' 。
【解题思路】
1. 统计words中符合条件的，+1
"""

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq


class Solution(object):
    def vowelStrings(self, words, queries):
        """
        :type words: List[str]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        s = [0] * (len(words) + 1)
        ans = []
        for idx, x in enumerate(words):
            if x[0] in "aeiou" and x[-1] in "aeiou":
                x = 1
            else:
                x = 0
            s[idx + 1] = s[idx] + x
        for i in queries:
            ans.append(s[i[1] + 1] - s[i[0]])
        return ans


# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
    print(
        solution.vowelStrings(
            words=["aba", "bcb", "ece", "aa", "e"], queries=[[0, 2], [1, 4], [1, 1]]
        )
    )
    print(
        solution.vowelStrings(words=["a", "e", "i"], queries=[[0, 2], [0, 1], [2, 2]])
    )
