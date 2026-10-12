# 1590. 使数组和能被 P 整除
'''
给你一个正整数数组 nums，请你移除 最短 子数组（可以为 空），使得剩余元素的 和 能被 p 整除。 不允许 将整个数组都移除。

请你返回你需要移除的最短子数组的长度，如果无法满足题目要求，返回 -1 。

子数组 定义为原数组中连续的一组元素。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def minSubarray(self, nums, p):
        """
        :type nums: List[int]
        :type p: int
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
