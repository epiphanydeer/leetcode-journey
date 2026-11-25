# 219. 存在重复元素 II
"""
给你一个整数数组 nums 和一个整数 k ，判断数组中是否存在两个 不同的索引 i 和 j ，满足 nums[i] == nums[j] 且 abs(i - j) <= k 。如果存在，返回 true ；否则，返回 false 。
【解题思路】
1. 存表，把下标存进去
"""

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq


class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d = defaultdict(int)
        for idx, x in enumerate(nums):
            if x in d and idx - d[x] <= k:
                return True
            d[x] = idx
        return False


# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
    print(solution.containsNearbyDuplicate(nums=[1, 2, 3, 1], k=3))
    print(solution.containsNearbyDuplicate(nums=[1, 0, 1, 1], k=1))
    print(solution.containsNearbyDuplicate(nums=[1, 2, 3, 1, 2, 3], k=2))
