# 2334. 元素值大于变化阈值的子数组
'''
给你一个整数数组 nums 和一个整数 threshold 。

找到长度为 k 的 nums 子数组，满足数组中 每个 元素都 大于 threshold / k 。

请你返回满足要求的 任意 子数组的 大小 。如果没有这样的子数组，返回 -1 。

子数组 是数组中一段连续非空的元素序列。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def validSubarraySize(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
