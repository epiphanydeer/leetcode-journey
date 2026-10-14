# 1931. 用三种不同颜色为网格涂色
'''
给你两个整数 m 和 n 。构造一个 m x n 的网格，其中每个单元格最开始是白色。请你用 红、绿、蓝 三种颜色为每个单元格涂色。所有单元格都需要被涂色。

涂色方案需要满足：不存在相邻两个单元格颜色相同的情况 。返回网格涂色的方法数。因为答案可能非常大， 返回 对 109 + 7 取余 的结果。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def colorTheGrid(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
