# 1208. 尽可能使字符串相等
"""
给你两个长度相同的字符串，s 和 t。

将 s 中的第 i 个字符变到 t 中的第 i 个字符需要 |s[i] - t[i]| 的开销（开销可能为 0），也就是两个字符的 ASCII 码值的差的绝对值。

用于变更字符串的最大预算是 maxCost。在转化字符串时，总开销应当小于等于该预算，这也意味着字符串的转化可能是不完全的。

如果你可以将 s 的子字符串转化为它在 t 中对应的子字符串，则返回可以转化的最大长度。

如果 s 中没有子字符串可以转化成 t 中对应的子字符串，则返回 0。
【解题思路】
1. ascii码的差值可以做成一个数组，然后计算不超过maxcost的最大长度就可以
"""

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq


class Solution(object):
    def equalSubstring(self, s, t, maxCost):
        """
        :type s: str
        :type t: str
        :type maxCost: int
        :rtype: int
        """
        cost = [0] * len(s)
        crt, left, ans = 0, 0, 0
        for i in range(len(s)):
            cost[i] = abs(ord(s[i]) - ord(t[i]))
        for right, j in enumerate(cost):
            crt += j
            while crt > maxCost:
                crt -= cost[left]
                left += 1
            ans = max(ans, right - left + 1)
        return ans


# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
    print(solution.equalSubstring(s="abcd", t="cdef", maxCost=3))
