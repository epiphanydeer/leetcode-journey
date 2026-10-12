# 541. 反转字符串 II
"""
给定一个字符串 s 和一个整数 k，从字符串开头算起，每计数至 2k 个字符，就反转这 2k 字符中的前 k 个字符，再重新计数。

 如果剩余字符少于 k 个，则将剩余字符全部反转。

 如果剩余字符小于 2k 但大于或等于 k 个，则反转前 k 个字符，其余字符保持原样。
 【解题思路】
 1. 步长为2k，翻转前k个，遍历翻转
"""

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq


class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s = list(s)
        for i in range(0, len(s), 2 * k):
            s[i : i + k] = s[i : i + k][::-1]
        return "".join(s)


# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
    print(solution.reverseStr(s="abcdefg", k=2))
