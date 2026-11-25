# 面试题 16.24. 数对和
"""
设计一个算法，找出数组中两数之和为指定值的所有整数对。一个数只能属于一个数对。
【解题思路】
1. 枚举右维护左，找target - x是否在表里
"""

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq


class Solution(object):
    def pairSums(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        d = defaultdict(int)
        ans = []
        for x in nums:
            if d[target - x] != 0:
                ans.append([x, target - x])
                d[x] -= 1
                d[target - x] -= 1
            d[x] += 1
        return ans


# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
    print(solution.pairSums(nums=[5, 6, 5], target=11))
    print(solution.pairSums(nums=[5, 6, 5, 6], target=11))
