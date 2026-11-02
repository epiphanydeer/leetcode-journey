# 704. 二分查找
"""
给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，如果 target 存在返回下标，否则返回 -1。

你必须编写一个具有 O(log n) 时间复杂度的算法。

示例 1:

输入: nums = [-1,0,3,5,9,12], target = 9
输出: 4
解释: 9 出现在 nums 中并且下标为 4
【解题思路】
1. 二分的本质是找到第一个大于等于target数字的位置
2. 本题就是基础的二分
"""

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq


class Solution(object):

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        if nums[left] == target:
            return left
        else:
            return -1


# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
    print(solution.search(nums=[-1, 0, 3, 5, 9, 12], target=9))
    print(solution.search(nums=[-1, 0, 3, 5, 9, 12], target=2))
