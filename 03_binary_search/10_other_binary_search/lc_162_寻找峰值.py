# 162. 寻找峰值
"""
峰值元素是指其值严格大于左右相邻值的元素。

给你一个整数数组 nums，找到峰值元素并返回其索引。数组可能包含多个峰值，在这种情况下，返回 任何一个峰值 所在位置即可。

你可以假设 nums[-1] = nums[n] = -∞ 。

你必须实现时间复杂度为 O(log n) 的算法来解决此问题。
【解题思路】：
1. mid去和mid+1比较，如果mid较大，说明mid右边小，这时候right到mid
2. 如果mid小了，那left就挪到大一点的mid+1，此时天然左小中间大
3. 总而言之，left动一定是到大的数字，然后左边比他小
right动一定是到大的数字，然后右边比他小
此时如果left = right了，那就左右都小了
"""

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq


class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1
        return left


# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
    print(solution.findPeakElement(nums=[1, 2, 3, 1]))
