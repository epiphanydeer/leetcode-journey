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
        if k <= 1:
            return 0
        ans, left, crt = 0, 0, 1
        for right, j in enumerate(nums):
            crt *= j
            while crt >= k:
                crt //= nums[left]
                left += 1
            # key
            ans += right - left + 1
        return ans


# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
    print()
