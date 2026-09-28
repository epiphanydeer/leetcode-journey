# 209. 长度最小的子数组
"""
给定一个含有 n 个正整数的数组和一个正整数 target 。
找出该数组中满足其总和大于等于 target 的长度最小的 子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回 0 。
【解题思路】
1. 长度最小的子数组了，说明一符合条件就要开始缩小了
"""

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq


class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        if sum(nums) < target:
            return 0
        crt, left = 0, 0
        ans = len(nums) + 1
        for right, j in enumerate(nums):
            crt += j
            while crt >= target:
                ans = min(ans, right - left + 1)
                crt -= nums[left]
                left += 1
        return ans


# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
    print(solution.minSubArrayLen(target=7, nums=[2, 3, 1, 2, 4, 3]))
