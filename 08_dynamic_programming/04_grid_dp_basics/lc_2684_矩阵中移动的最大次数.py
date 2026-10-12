# 2684. 矩阵中移动的最大次数
'''
给你一个下标从 0 开始、大小为 m x n 的矩阵 grid ，矩阵由若干 正 整数组成。

你可以从矩阵第一列中的 任一 单元格出发，按以下方式遍历 grid ：

 从单元格 (row, col) 可以移动到 (row - 1, col + 1)、(row, col + 1) 和 (row + 1, col + 1) 三个单元格中任一满足值 严格 大于当前单元格的单元格。

返回你在矩阵中能够 移动 的 最大 次数。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def maxMoves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
