# 2461. 长度为 K 子数组中的最大和
"""
给你一个整数数组 nums 和一个整数 k 。请你从 nums 中满足下述条件的全部子数组中找出最大子数组和：
子数组的长度是 k，且
子数组中的所有元素 各不相同 。
返回满足题面要求的最大子数组和。如果不存在子数组满足这些条件，返回 0 。
子数组 是数组中一段连续非空的元素序列.

【核心思路】
1. 同上题，不过这次要确定len == k
"""

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq


class Solution(object):
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        d = defaultdict(int)
        ans, crt = 0, 0
        for right, x in enumerate(nums):
            crt += x
            left = right - k + 1
            d[x] += 1
            if left < 0:
                continue
            if len(d) == k:
                ans = max(ans, crt)
            j = nums[left]
            d[j] -= 1
            crt -= j
            if d[j] == 0:
                del d[j]
            left += 1
        return ans


# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
    output = solution.maximumSubarraySum(nums=[1, 5, 4, 2, 9, 9, 9], k=3)
    print(output)
