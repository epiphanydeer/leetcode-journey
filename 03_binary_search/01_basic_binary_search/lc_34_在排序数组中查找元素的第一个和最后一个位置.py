# 34. 在排序数组中查找元素的第一个和最后一个位置
"""
给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。

如果数组中不存在目标值 target，返回 [-1, -1]。

你必须设计并实现时间复杂度为 O(log n) 的算法解决此问题。
【解题思路】
1. 先写二分函数，二分的本质是找到一个分界线，第一个大于等于target的位置
2. 找到位置后判断是否相等或者数组存不存在
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

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        start = self.lower_bound(nums, target)
        if start < len(nums) and nums[start] == target:
            end = self.lower_bound(nums, target + 1) - 1
            return [start, end]
        else:
            return [-1, -1]


# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
    print(solution.searchRange(nums=[5, 7, 7, 8, 8, 10], target=8))
    print(solution.searchRange(nums=[5, 7, 7, 8, 8, 10], target=6))
