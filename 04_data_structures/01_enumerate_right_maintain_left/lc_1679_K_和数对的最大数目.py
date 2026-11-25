# 1679. K 和数对的最大数目
"""
给你一个整数数组 nums 和一个整数 k 。

每一步操作中，你需要从数组中选出和为 k 的两个整数，并将它们移出数组。

返回你可以对数组执行的最大操作数。
【解题思路】
1. 枚举右维护左，找k-x是否在表里，ans记操作数
"""

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq


class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans = 0
        d = defaultdict(int)
        for x in nums:
            if d[k - x] != 0:
                ans += 1
                d[x] -= 1
                d[k - x] -= 1
            d[x] += 1
        return ans


# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
    print(solution.maxOperations(nums=[1, 2, 3, 4], k=5))
    print(solution.maxOperations(nums=[3, 1, 3, 4, 3], k=6))
