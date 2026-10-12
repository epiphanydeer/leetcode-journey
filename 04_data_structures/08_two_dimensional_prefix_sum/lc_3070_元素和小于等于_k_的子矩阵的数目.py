# 3070. 元素和小于等于 k 的子矩阵的数目
'''
给你一个下标从 0 开始的整数矩阵 grid 和一个整数 k。

返回包含 grid 左上角元素、元素和小于或等于 k 的 子矩阵的数目。

 

示例 1：

输入：grid = [[7,6,3],[6,6,1]], k = 18
输出：4
解释：如上图所示，只有 4 个子矩阵满足：包含 grid 的左上角元素，并且元素和小于或等于 18 。

示例 2：

输入：grid = [[7,2,9],[1,5,0],[2,6,6]], k = 20
输出：6
解释：如上图所示，只有 6 个子矩阵满足：包含 grid 的左上角元素，并且元素和小于或等于 20 。

 

提示：

 m == grid.length 

 n == grid[i].length

 1 <= n, m <= 1000 

 0 <= grid[i][j] <= 1000

 1 <= k <= 109
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def countSubmatrices(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
