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
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """

        def atMost(k: int) -> int:
            if k < 0:
                return 0
            left, ans, crt = 0, 0, 0
            for right, j in enumerate(nums):
                crt += j
                while crt > k:
                    crt -= nums[left]
                    left += 1
                ans += right - left + 1
            return ans

        return atMost(goal) - atMost(goal - 1)


# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
    print(solution.numSubarraysWithSum(nums=[0, 0, 0, 0, 0], goal=0))
