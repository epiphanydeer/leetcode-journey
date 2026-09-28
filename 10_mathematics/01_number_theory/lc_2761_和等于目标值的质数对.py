# 2761. 和等于目标值的质数对
'''
给你一个整数 n 。如果两个整数 x 和 y 满足下述条件，则认为二者形成一个质数对：

 1 <= x <= y <= n

 x + y == n

 x 和 y 都是质数

请你以二维有序列表的形式返回符合题目要求的所有 [xi, yi] ，列表需要按 xi 的 非递减顺序 排序。如果不存在符合要求的质数对，则返回一个空数组。

注意：质数是大于 1 的自然数，并且只有两个因子，即它本身和 1 。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def findPrimePairs(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
