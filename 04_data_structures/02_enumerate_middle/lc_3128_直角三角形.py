# 3128. 直角三角形
"""
给你一个二维 boolean 矩阵 grid 。

如果 grid 的 3 个元素的集合中，一个元素与另一个元素在 同一行，并且与第三个元素在 同一列，则该集合是一个 直角三角形。3 个元素 不必 彼此相邻。

请你返回使用 grid 中的 3 个元素可以构建的 直角三角形 数目，且满足 3 个元素值 都 为 1 。

【解题思路】
1. 统计每行的和和每列的和，之后抽1去找同行和同列是否有1
2. zip(*grid)是先解开，然后zip一一对应，实现转置
"""

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq


class Solution(object):
    def numberOfRightTriangles(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row_cnt = [sum(i) for i in grid]
        col_cnt = [sum(i) for i in zip(*grid)]
        ans = 0
        for row, x in enumerate(grid):
            for col, y in enumerate(x):
                if y:
                    ans += (col_cnt[col] - 1) * (row_cnt[row] - 1)
        return ans


# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
    print(solution.numberOfRightTriangles(grid=[[0, 1, 0], [0, 1, 1], [0, 1, 0]]))
    print(
        solution.numberOfRightTriangles(grid=[[1, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]])
    )
    print(solution.numberOfRightTriangles(grid=[[1, 0, 1], [1, 0, 0], [1, 0, 0]]))
