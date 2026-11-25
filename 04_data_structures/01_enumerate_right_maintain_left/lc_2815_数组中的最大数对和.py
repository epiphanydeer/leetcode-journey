# 2815. 数组中的最大数对和
"""
给你一个下标从 0 开始的整数数组 nums 。请你从 nums 中找出和 最大 的一对数，且这两个数数位上最大的数字相等。

返回最大和，如果不存在满足题意的数字对，返回 -1 。
【解题思路】
1. 数位最大的数字相等可以用str，int(max(str))
2. 遍历右维护左，遍历数位相等的，然后不断更新最大的数字（和最大）
"""

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq


class Solution(object):
    def maxSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = -1
        d = defaultdict(int)
        for x in nums:
            maxd = int(max(str(x)))
            if d[maxd]:
                ans = max(ans, x + d[maxd])
            d[maxd] = max(d[maxd], x)
        return ans


# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
    print(solution.maxSum(nums=[51, 71, 17, 24, 42]))
    print(solution.maxSum(nums=[1, 2, 3, 4]))
