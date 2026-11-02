# 696. 计数二进制子串
"""
给定一个字符串 s，统计并返回具有相同数量 0 和 1 的非空（连续）子字符串的数量，并且这些子字符串中的所有 0 和所有 1 都是成组连续的。

重复出现（不同位置）的子串也要统计它们出现的次数。
【解题思路】
1. 题目意思是返回相邻的01，实际上就是两组01相同的个数加和
2. 用模板的话，就要维护两个变量分别是记录1和记录0，pre cur
"""

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq


class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        pre, ans, cur = 0, 0, 0
        n = len(s)
        for i in range(n):
            cur += 1
            if i == n - 1 or s[i + 1] != s[i]:
                ans += min(pre, cur)
                pre = cur
                cur = 0
        return ans


# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
    print(solution.countBinarySubstrings(s="00110011"))
