# 3459. 最长 V 形对角线段的长度
'''
给你一个大小为 n x m 的二维整数矩阵 grid，其中每个元素的值为 0、1 或 2。

V 形对角线段 定义如下：

 线段从 1 开始。

 后续元素按照以下无限序列的模式排列：2, 0, 2, 0, ...。

 该线段：
 
 起始于某个对角方向（左上到右下、右下到左上、右上到左下或左下到右上）。

 沿着相同的对角方向继续，保持 序列模式 。

 在保持 序列模式 的前提下，最多允许 一次顺时针 90 度转向 另一个对角方向。

 
 

返回最长的 V 形对角线段 的 长度 。如果不存在有效的线段，则返回 0。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def lenOfVDiagonal(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
