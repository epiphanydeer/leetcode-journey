# 2016. 增量元素之间的最大差值
"""
给你一个下标从 0 开始的整数数组 nums ，该数组的大小为 n ，请你计算 nums[j] - nums[i] 能求得的 最大差值 ，其中 0 <= i < j < n 且 nums[i] < nums[j] 。

返回 最大差值 。如果不存在满足要求的 i 和 j ，返回 -1 。
"""

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq


class Solution(object):
    def maximumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minn = nums[0]
        ans = 0
        for x in nums:
            ans = max(ans, x - minn)
            minn = min(minn, x)
        return ans or -1


# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
    print(solution.maximumDifference([7, 1, 5, 4]))
    print(solution.maximumDifference([9, 4, 3, 2]))
    print(solution.maximumDifference([1, 5, 2, 10]))
