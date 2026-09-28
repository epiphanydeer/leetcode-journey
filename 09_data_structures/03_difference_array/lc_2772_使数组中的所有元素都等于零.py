# 2772. 使数组中的所有元素都等于零
'''
给你一个下标从 0 开始的整数数组 nums 和一个正整数 k 。

你可以对数组执行下述操作 任意次 ：

 从数组中选出长度为 k 的 任一 子数组，并将子数组中每个元素都 减去 1 。

如果你可以使数组中的所有元素都等于 0 ，返回  true ；否则，返回 false 。

子数组 是数组中的一个非空连续元素序列。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def checkArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
