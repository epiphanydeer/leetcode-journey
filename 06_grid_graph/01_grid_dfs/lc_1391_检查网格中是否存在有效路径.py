# 1391. 检查网格中是否存在有效路径
'''
给你一个 m x n 的网格 grid。网格里的每个单元都代表一条街道。grid[i][j] 的街道可以是：

 1 表示连接左单元格和右单元格的街道。

 2 表示连接上单元格和下单元格的街道。

 3 表示连接左单元格和下单元格的街道。

 4 表示连接右单元格和下单元格的街道。

 5 表示连接左单元格和上单元格的街道。

 6 表示连接右单元格和上单元格的街道。

你最开始从左上角的单元格 (0,0) 开始出发，网格中的「有效路径」是指从左上方的单元格 (0,0) 开始、一直到右下方的 (m-1,n-1) 结束的路径。该路径必须只沿着街道走。

注意：你 不能 变更街道。

如果网格中存在有效的路径，则返回 true，否则返回 false 。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def hasValidPath(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
