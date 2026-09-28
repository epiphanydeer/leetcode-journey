# 2567. 修改两个元素的最小分数
'''
给你一个下标从 0 开始的整数数组 nums 。

 nums 的 最小 得分是满足 0 <= i < j < nums.length 的 |nums[i] - nums[j]| 的最小值。

 nums的 最大 得分是满足 0 <= i < j < nums.length 的 |nums[i] - nums[j]| 的最大值。

 nums 的分数是 最大 得分与 最小 得分的和。

我们的目标是最小化 nums 的分数。你 最多 可以修改 nums 中 2 个元素的值。

请你返回修改 nums 中 至多两个 元素的值后，可以得到的 最小分数 。

|x| 表示 x 的绝对值。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def minimizeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
