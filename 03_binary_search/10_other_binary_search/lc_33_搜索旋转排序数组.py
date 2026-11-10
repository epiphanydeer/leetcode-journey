# 33. 搜索旋转排序数组
"""
整数数组 nums 按升序排列，数组中的值 互不相同 。

在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 向左旋转，使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。例如， [0,1,2,4,5,6,7] 下标 3 上向左旋转后可能变为 [4,5,6,7,0,1,2] 。

给你 旋转后 的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，则返回它的下标，否则返回 -1 。

你必须设计一个时间复杂度为 O(log n) 的算法解决此问题。
【解题思路】
1. mid去和最后一个数判断，如果大于，则mid左侧递增，若target在区间内，left到mid-1
如果小于，mid右侧递增，target若在区间内，left到mid+1
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
            x = nums[mid]
            if x == target:
                return mid
            if x > nums[-1]:
                if x > target >= nums[left]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if x < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1


# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
    print(solution.search(nums=[4, 5, 6, 7, 0, 1, 2], target=0))
