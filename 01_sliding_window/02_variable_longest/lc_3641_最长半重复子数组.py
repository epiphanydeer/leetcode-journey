# 3641. 最长半重复子数组
'''
给定一个长度为 n 的整数数组 nums 和一个整数 k。

半重复子数组是指最多有 k 个元素重复（即出现超过一次）的连续子数组。

返回 nums 中最长半重复子数组的长度。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def longestSubarray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
