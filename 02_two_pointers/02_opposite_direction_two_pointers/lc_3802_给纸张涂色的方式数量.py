# 3802. 给纸张涂色的方式数量
'''
给定一个整数 n 表示纸张的数量。同时给定一个长度为 m 的整数数组 limit，其中 limit[i] 是使用颜色 i 能够涂色的最大纸张数。

你必须恰好使用两种不同颜色给所有 n 张纸涂色；每种颜色必须覆盖连续的一段纸张，且用颜色 i 涂的纸张数量不能超过 limit[i]。

返回不同方式数量对 10^9 + 7 取模的结果。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def numberOfWays(self, n, limit):
        """
        :type n: int
        :type limit: List[int]
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
