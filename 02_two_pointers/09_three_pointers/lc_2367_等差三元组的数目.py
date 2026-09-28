# 2367. 等差三元组的数目
'''
给你一个下标从 0 开始、严格递增 的整数数组 nums 和一个正整数 diff 。如果满足下述全部条件，则三元组 (i, j, k) 就是一个 等差三元组 ：

 i < j < k ，

 nums[j] - nums[i] == diff 且

 nums[k] - nums[j] == diff

返回不同 等差三元组 的数目。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        """
        :type nums: List[int]
        :type diff: int
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
