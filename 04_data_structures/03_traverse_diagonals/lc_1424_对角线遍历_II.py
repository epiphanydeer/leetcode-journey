# 1424. 对角线遍历 II
'''
给你一个列表 nums ，里面每一个元素都是一个整数列表。请你依照下面各图的规则，按顺序返回 nums 中对角线上的整数。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def findDiagonalOrder(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
