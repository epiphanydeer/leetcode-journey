# 898. 子数组按位或操作
'''
给定一个整数数组 arr，返回所有 arr 的非空子数组的不同按位或的数量。

子数组的按位或是子数组中每个整数的按位或。含有一个整数的子数组的按位或就是该整数。

子数组 是数组内连续的非空元素序列。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def subarrayBitwiseORs(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
