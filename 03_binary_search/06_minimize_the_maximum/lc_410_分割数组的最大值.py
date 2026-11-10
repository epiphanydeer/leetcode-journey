# 410. 分割数组的最大值
"""
给定一个非负整数数组 nums 和一个整数 k ，你需要将这个数组分成 k 个非空的连续子数组，使得这 k 个子数组各自和的最大值 最小。

返回分割后最小的和的最大值。

子数组 是数组中连续的部分。
【解题思路】
1.
"""

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq


class Solution(object):

    def splitArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        def check(mid: int) -> bool:
            block = 1
            total = 0
            for i in nums:
                total += i
                if total > mid:
                    block += 1
                    total = i
            return block <= k

        left, right = max(nums), sum(nums)
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans


# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
    print(solution.splitArray(nums=[7, 2, 5, 10, 8], k=2))
    print(solution.splitArray(nums=[1, 2, 3, 4, 5], k=2))
