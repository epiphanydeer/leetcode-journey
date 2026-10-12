# 2762. 不间断子数组
'''
给你一个下标从 0 开始的整数数组 nums 。nums 的一个子数组如果满足以下条件，那么它是 不间断 的：

 i，i + 1 ，...，j  表示子数组中的下标。对于所有满足 i <= i1, i2 <= j 的下标对，都有 0 <= |nums[i1] - nums[i2]| <= 2 。

请你返回 不间断 子数组的总数目。

子数组是一个数组中一段连续 非空 的元素序列。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def continuousSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
