# 1981. 最小化目标值与所选元素的差
'''
给你一个大小为 m x n 的整数矩阵 mat 和一个整数 target 。

从矩阵的 每一行 中选择一个整数，你的目标是 最小化 所有选中元素之 和 与目标值 target 的 绝对差 。

返回 最小的绝对差 。

a 和 b 两数字的 绝对差 是 a - b 的绝对值。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def minimizeTheDifference(self, mat, target):
        """
        :type mat: List[List[int]]
        :type target: int
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
