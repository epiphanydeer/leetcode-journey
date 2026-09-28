# 1918. 第 K 小的子数组和
'''
给你一个长度为 n 的整型数组 nums 和一个数值 k，返回第 k 小的子数组和。

子数组是指数组中一个非空且不间断的子序列。子数组和则指子数组中所有元素的和。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def kthSmallestSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
