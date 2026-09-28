# 1099. 小于 K 的两数之和
'''
给你一个整数数组 nums 和整数 k，返回最大和 sum，满足存在 i < j 使得 nums[i] + nums[j] = sum 且 sum < k。如果没有满足此等式的 i、j 存在，则返回 -1。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def twoSumLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
