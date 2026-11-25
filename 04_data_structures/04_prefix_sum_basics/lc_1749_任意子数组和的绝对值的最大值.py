# 1749. 任意子数组和的绝对值的最大值
"""
给你一个整数数组 nums 。一个子数组 [numsl, numsl+1, ..., numsr-1, numsr] 的 和的绝对值 为 abs(numsl + numsl+1 + ... + numsr-1 + numsr) 。

请你找出 nums 中 和的绝对值 最大的任意子数组（可能为空），并返回该 最大值 。
【解题思路】
1. 和的绝对值 最大的任意子数组，前缀和的最大差值
"""

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq


class Solution(object):
    def maxAbsoluteSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = [0] * (len(nums) + 1)
        for idx, x in enumerate(nums):
            s[idx + 1] = s[idx] + x
        return max(s) - min(s)


# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
    print(solution.maxAbsoluteSum(nums=[1, -3, 2, 3, -4]))
    print(solution.maxAbsoluteSum(nums=[2, -5, 1, -4, 3, -2]))
