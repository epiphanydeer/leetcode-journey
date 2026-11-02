# 713. 乘积小于 K 的子数组
"""
给定一个整数数组 nums 和一个整数 k。

请你返回 子数组 内所有元素的 乘积严格小于 k 的连续子数组的数目。
【解题思路】
1. 核心在于计算子数组是 += right - left + 1
2. 关键在于固定最右边的符合的数字，去计算包含它的每个子数组
"""

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq


class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        cur = 1
        left, ans = 0, 0
        if k <= 1:
            return 0
        for right, x in enumerate(nums):
            cur *= x
            if cur >= k:
                cur //= nums[left]
                left += 1
            ans += right - left + 1
        return ans


# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
    print(solution.numSubarrayProductLessThanK(nums=[10, 5, 2, 6], k=100))
