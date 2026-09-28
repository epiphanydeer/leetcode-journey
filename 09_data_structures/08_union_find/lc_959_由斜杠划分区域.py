# 959. 由斜杠划分区域
'''
在由 1 x 1 方格组成的 n x n 网格 grid 中，每个 1 x 1 方块由 '/'、'\' 或空格构成。这些字符会将方块划分为一些共边的区域。

给定网格 grid 表示为一个字符串数组，返回 区域的数量 。

请注意，反斜杠字符是转义的，因此 '\' 用 '\\' 表示。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def regionsBySlashes(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
