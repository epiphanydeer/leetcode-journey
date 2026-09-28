# 1004. 最大连续1的个数 III
"""
给定一个二进制数组 nums 和一个整数 k，假设最多可以翻转 k 个 0 ，则返回执行操作后 数组中连续 1 的最大个数 。
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
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        d = defaultdict(int)
        ans = left = 0
        for right, j in enumerate(nums):
            d[j] += 1
            while not d[0] <= k:
                d[nums[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans


# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
    print(solution.longestOnes(nums=[1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], k=2))
