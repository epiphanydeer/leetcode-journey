# 80. 删除有序数组中的重复项 II
"""
给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使得出现次数超过两次的元素只出现两次 ，返回删除后数组的新长度。
不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

【解题思路】
1. 次数超过两次的元素，从第三个数开始和前面的判断
"""

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 2:
            return nums
        slow = 2
        for fast in range(2, n):
            if nums[fast] != nums[slow - 2]:
                nums[slow] = nums[fast]
                slow += 1
        return slow


# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
    print(solution.removeDuplicates(nums=[0, 0, 1, 1, 1, 1, 2, 3, 3]))
