# 977. 有序数组的平方
"""
给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序。
【解题思路】
1. 要注意的点在于，负数的平方有可能大于正数的平方
2. 因此要倒序的填入数字
"""

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq


class Solution(object):
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        left, right = 0, len(nums) - 1
        for p in range(len(nums) - 1, -1, -1):
            x = nums[left] * nums[left]
            y = nums[right] * nums[right]
            if x < y:
                ans[p] = y
                right -= 1
            else:
                ans[p] = x
                left += 1
        return ans


# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
    print(solution.sortedSquares(nums=[-4, -1, 0, 3, 10]))
