# 1770. 执行乘法运算的最大分数
'''
给你两个长度分别 n 和 m 的整数数组 nums 和 multipliers ，其中 n >= m ，数组下标 从 1 开始 计数。

初始时，你的分数为 0 。你需要执行恰好 m 步操作。在第 i 步操作（从 1 开始 计数）中，需要：

 选择数组 nums 开头处或者末尾处 的整数 x 。

 你获得 multipliers[i] * x 分，并累加到你的分数中。

 将 x 从数组 nums 中移除。

在执行 m 步操作后，返回 最大 分数。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def maximumScore(self, nums, multipliers):
        """
        :type nums: List[int]
        :type multipliers: List[int]
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
