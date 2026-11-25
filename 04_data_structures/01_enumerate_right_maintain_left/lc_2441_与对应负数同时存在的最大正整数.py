# 2441. 与对应负数同时存在的最大正整数
"""
给你一个 不包含 任何零的整数数组 nums ，找出自身与对应的负数都在数组中存在的最大正整数 k 。

返回正整数 k ，如果不存在这样的整数，返回 -1 。
【解题思路】
1. 枚举右，维护左，向右遍历，存入哈希表，然后找是否有负数
"""

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq


class Solution(object):
    def findMaxK(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = defaultdict(int)
        ans = -1
        for x in nums:
            if -x in d:
                ans = max(ans, abs(x))
            d[x] += 1
        return ans


# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
    print(solution.findMaxK(nums=[-1, 2, -3, 3]))
    print(solution.findMaxK(nums=[-1, 10, 6, 7, -7, 1]))
    print(solution.findMaxK(nums=[-10, 8, 6, 7, -2, -3]))
