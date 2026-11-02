# 2529. 正整数和负整数的最大计数
"""
给你一个按 非递减顺序 排列的数组 nums ，返回正整数数目和负整数数目中的最大值。

 换句话讲，如果 nums 中正整数的数目是 pos ，而负整数的数目是 neg ，返回 pos 和 neg二者中的最大值。

注意：0 既不是正整数也不是负整数。
【解题思路】
1. 也就是按0来二分，二分的本质，第一个大于等于target的数字
"""

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq


class Solution(object):
    def lower_bound(self, nums, target=0):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left

    def maximumCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        neg = self.lower_bound(nums)
        pos = len(nums) - self.lower_bound(nums, 1)
        return max(neg, pos)


# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
    print(solution.maximumCount(nums=[-2, -1, -1, 1, 2, 3]))
    print(solution.maximumCount(nums=[-3, -2, -1, 0, 0, 1, 2]))
    print(solution.maximumCount(nums=[5, 20, 66, 1314]))
