# 2012. 数组美丽值求和
'''
给你一个下标从 0 开始的整数数组 nums 。对于每个下标 i（1 <= i <= nums.length - 2），nums[i] 的 美丽值 等于：

 2，对于所有 0 <= j < i 且 i < k <= nums.length - 1 ，满足 nums[j] < nums[i] < nums[k]

 1，如果满足 nums[i - 1] < nums[i] < nums[i + 1] ，且不满足前面的条件

 0，如果上述条件全部不满足

返回符合 1 <= i <= nums.length - 2 的所有 nums[i] 的 美丽值的总和 。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def sumOfBeauties(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
