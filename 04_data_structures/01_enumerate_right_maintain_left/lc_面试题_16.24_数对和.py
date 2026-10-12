# 面试题 16.24. 数对和
'''
设计一个算法，找出数组中两数之和为指定值的所有整数对。一个数只能属于一个数对。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def pairSums(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
