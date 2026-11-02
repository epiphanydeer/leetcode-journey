# 1446. 连续字符
"""
给你一个字符串 s ，字符串的「能量」定义为：只包含一种字符的最长非空子字符串的长度。

请你返回字符串 s 的 能量。
【解题思路】
1. 设置start 判断下一个是否与前一个相同，更新长度
2. 按照题目要求，数组会被分割成若干组，每一组的判断/处理逻辑是相同的。
"""

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq


class Solution(object):
    def maxPower(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        n = len(s)
        ans = 0
        while i < n:
            start = i
            i += 1
            while i < n and s[i] == s[i - 1]:
                i += 1
            ans = max(ans, i - start)
        return ans


# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
    print(solution.maxPower(s="abbcccddddeeeeedcba"))
