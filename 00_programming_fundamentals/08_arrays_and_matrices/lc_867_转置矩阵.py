# 867. 转置矩阵
'''
给你一个二维整数数组 matrix， 返回 matrix 的 转置矩阵 。

矩阵的 转置 是指将矩阵的主对角线翻转，交换矩阵的行索引与列索引。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
