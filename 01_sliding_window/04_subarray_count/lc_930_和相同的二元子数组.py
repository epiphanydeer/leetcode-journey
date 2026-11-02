# 930. 和相同的二元子数组
"""
给你一个二元数组 nums ，和一个整数 goal ，请你统计并返回有多少个和为 goal 的 非空 子数组。

子数组 是数组的一段连续部分。
【解题思路】
1. 什么是恰好的整数，在数轴上就是大于等于（≥goal）的东西，减去大于（>goal）的东西，就是刚好等于（==goal）的东西。
2. 最简单直观的方法是写一个atmost函数，去判断
"""

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq


class Solution(object):
    def atMost(self, nums, goal):
        ans = left = cur = 0
        n = len(nums)
        if goal <= 0:  # 和 >= 0，所有子数组都满足
            return n * (n + 1) // 2
        for right, x in enumerate(nums):
            cur += x
            while cur >= goal:
                cur -= nums[left]
                left += 1
            ans += left
        return ans

    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """

        return self.atMost(nums, goal) - self.atMost(nums, goal + 1)


# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
    print(solution.numSubarraysWithSum(nums=[1, 0, 1, 0, 1], goal=2))
