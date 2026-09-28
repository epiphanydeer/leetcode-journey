# 3090. 每个字符最多出现两次的最长子字符串
"""
给你一个字符串 s ，请找出满足每个字符最多出现两次的最长子字符串，并返回该子字符串的 最大 长度。
示 1：
输入： s = "bcbbbcba"
输出： 4
解释：
以下子字符串长度为 4，并且每个字符最多出现两次："bcbbbcba"。
示例 2：
输入： s = "aaaa"
输出： 2
解释：

以下子字符串长度为 2，并且每个字符最多出现两次："aaaa"。
【解题思路】
跟lc_3大差不差，无非是把条件变成了可以重复两次。

"""

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq


class Solution(object):
    def maximumLengthSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans, left = 0, 0
        d = defaultdict(int)
        for right, j in enumerate(s):
            d[j] += 1
            while d[j] > 2:
                d[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans


# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
    print(solution.maximumLengthSubstring("bcbbbcba"))
