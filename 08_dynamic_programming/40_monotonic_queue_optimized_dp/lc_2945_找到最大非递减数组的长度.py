# 2945. 找到最大非递减数组的长度
'''
给你一个下标从 0 开始的整数数组 nums 。

你可以执行任意次操作。每次操作中，你需要选择一个 子数组 ，并将这个子数组用它所包含元素的 和 替换。比方说，给定数组是 [1,3,5,6] ，你可以选择子数组 [3,5] ，用子数组的和 8 替换掉子数组，然后数组会变为 [1,8,6] 。

请你返回执行任意次操作以后，可以得到的 最长非递减 数组的长度。

子数组 指的是一个数组中一段连续 非空 的元素序列。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def findMaximumLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
