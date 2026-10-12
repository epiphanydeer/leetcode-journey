# 2472. 不重叠回文子字符串的最大数目
'''
给你一个字符串 s 和一个 正 整数 k 。

从字符串 s 中选出一组满足下述条件且 不重叠 的子字符串：

 每个子字符串的长度 至少 为 k 。

 每个子字符串是一个 回文串 。

返回最优方案中能选择的子字符串的 最大 数目。

子字符串 是字符串中一个连续的字符序列。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def maxPalindromes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
