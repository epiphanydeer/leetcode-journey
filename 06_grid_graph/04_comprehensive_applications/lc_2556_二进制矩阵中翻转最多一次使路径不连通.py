# 2556. 二进制矩阵中翻转最多一次使路径不连通
'''
给你一个下标从 0 开始的 m x n 二进制 矩阵 grid 。你可以从一个格子 (row, col) 移动到格子 (row + 1, col) 或者 (row, col + 1) ，前提是前往的格子值为 1 。如果从 (0, 0) 到 (m - 1, n - 1) 没有任何路径，我们称该矩阵是 不连通 的。

你可以翻转 最多一个 格子的值（也可以不翻转）。你 不能翻转 格子 (0, 0) 和 (m - 1, n - 1) 。

如果可以使矩阵不连通，请你返回 true ，否则返回 false 。

注意 ，翻转一个格子的值，可以使它的值从 0 变 1 ，或从 1 变 0 。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def isPossibleToCutPath(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
