# 35. 搜索插入位置
"""
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

请必须使用时间复杂度为 O(log n) 的算法。
【解题思路】
1. 二分的本质，找到第一个大于等于target的位置
2. 本题就是直白的二分，因为就是找到原数或者第一个大于target的数字
"""

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq


class Solution(object):
    def lower_bound(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left

    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.lower_bound(nums, target)


# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
    print(solution.lower_bound(nums=[1, 3, 5, 6], target=5))
    print(solution.lower_bound(nums=[1, 3, 5, 6], target=2))
    print(solution.lower_bound(nums=[1, 3, 5, 6], target=7))
