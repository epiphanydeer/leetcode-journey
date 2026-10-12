# 668. 乘法表中第k小的数
'''
几乎每一个人都用 乘法表。但是你能在乘法表中快速找到第 k 小的数字吗？

乘法表是大小为 m x n 的一个整数矩阵，其中 mat[i][j] == i * j（下标从 1 开始）。

给你三个整数 m、n 和 k，请你在大小为 m x n 的乘法表中，找出并返回第 k 小的数字。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def findKthNumber(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
