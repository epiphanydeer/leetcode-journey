# 2364. 统计坏数对的数目
"""
给你一个下标从 0 开始的整数数组 nums 。如果 i < j 且 j - i != nums[j] - nums[i] ，那么我们称 (i, j) 是一个 坏数对 。

请你返回 nums 中 坏数对 的总数目。
【解题思路】
1. 正难则反，计算好数对，i - nums[i] == j - nums[j]
2. 总数是n * (n - 1) // 2
"""

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq


class Solution(object):
    def countBadPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        n = len(nums)
        s = n * (n - 1) // 2
        d = defaultdict(int)
        for idx, x in enumerate(nums):
            if idx - x in d:
                ans += d[idx - x]
            d[idx - x] += 1
        return s - ans


# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
    print(solution.countBadPairs(nums=[4, 1, 3, 3]))
    print(solution.countBadPairs(nums=[1, 2, 3, 4, 5]))
