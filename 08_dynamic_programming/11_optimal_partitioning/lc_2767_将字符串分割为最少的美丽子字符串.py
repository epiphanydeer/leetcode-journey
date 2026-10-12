# 2767. 将字符串分割为最少的美丽子字符串
'''
给你一个二进制字符串 s ，你需要将字符串分割成一个或者多个 子字符串  ，使每个子字符串都是 美丽 的。

如果一个字符串满足以下条件，我们称它是 美丽 的：

 它不包含前导 0 。

 它是 5 的幂的 二进制 表示。

请你返回分割后的子字符串的 最少 数目。如果无法将字符串 s 分割成美丽子字符串，请你返回 -1 。

子字符串是一个字符串中一段连续的字符序列。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def minimumBeautifulSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
