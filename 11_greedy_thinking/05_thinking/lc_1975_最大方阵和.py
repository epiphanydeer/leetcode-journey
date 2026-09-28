# 1975. 最大方阵和
'''
给你一个 n x n 的整数方阵 matrix 。你可以执行以下操作 任意次 ：

 选择 matrix 中 相邻 两个元素，并将它们都 乘以 -1 。

如果两个元素有 公共边 ，那么它们就是 相邻 的。

你的目的是 最大化 方阵元素的和。请你在执行以上操作之后，返回方阵的 最大 和。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def maxMatrixSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
