# 3427. 变长子数组求和
"""
给你一个长度为 n 的整数数组 nums 。对于 每个 下标 i（0 <= i < n），定义对应的子数组 nums[start ... i]（start = max(0, i - nums[i])）。

返回为数组中每个下标定义的子数组中所有元素的总和。

子数组 是数组中的一个连续、非空 的元素序列。
【解题思路】
1. 子数组的和，前缀和
"""

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq


class Solution(object):
    def subarraySum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = [0] * (len(nums) + 1)
        ans = 0
        for idx, x in enumerate(nums):
            s[idx + 1] = s[idx] + x
            ans += s[idx + 1] - s[max(0, idx - x)]
        return ans


# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
    print(solution.subarraySum(nums=[2, 3, 1]))
    print(solution.subarraySum(nums=[3, 1, 1, 2]))
