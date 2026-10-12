# 3212. 统计 X 和 Y 频数相等的子矩阵数量
'''
给你一个二维字符矩阵 grid，其中 grid[i][j] 可能是 'X'、'Y' 或 '.'，返回满足以下条件的子矩阵数量：

 包含 grid[0][0]

 'X' 和 'Y' 的频数相等。

 至少包含一个 'X'。

 

示例 1：

输入： grid = [["X","Y","."],["Y",".","."]]

输出： 3

解释：

示例 2：

输入： grid = [["X","X"],["X","Y"]]

输出： 0

解释：

不存在满足 'X' 和 'Y' 频数相等的子矩阵。

示例 3：

输入： grid = [[".","."],[".","."]]

输出： 0

解释：

不存在满足至少包含一个 'X' 的子矩阵。

 

提示：

 1 <= grid.length, grid[i].length <= 1000

 grid[i][j] 可能是 'X'、'Y' 或 '.'.
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def numberOfSubmatrices(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
