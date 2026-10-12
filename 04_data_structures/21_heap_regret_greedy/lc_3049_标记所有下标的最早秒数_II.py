# 3049. 标记所有下标的最早秒数 II
'''
给你两个下标从 1 开始的整数数组 nums 和 changeIndices ，数组的长度分别为 n 和 m 。

一开始，nums 中所有下标都是未标记的，你的任务是标记 nums 中 所有 下标。

从第 1 秒到第 m 秒（包括 第 m 秒），对于每一秒 s ，你可以执行以下操作 之一 ：

 选择范围 [1, n] 中的一个下标 i ，并且将 nums[i] 减少 1 。

 将 nums[changeIndices[s]] 设置成任意的 非负 整数。

 选择范围 [1, n] 中的一个下标 i ， 满足 nums[i] 等于 0, 并 标记 下标 i 。

 什么也不做。

请你返回范围 [1, m] 中的一个整数，表示最优操作下，标记 nums 中 所有 下标的 最早秒数 ，如果无法标记所有下标，返回 -1 。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def earliestSecondToMarkIndices(self, nums, changeIndices):
        """
        :type nums: List[int]
        :type changeIndices: List[int]
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
