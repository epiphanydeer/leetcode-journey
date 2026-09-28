# 628. 三个数的最大乘积
'''
给你一个整型数组 nums。

在数组中找出由三个数组成的 最大 乘积，并返回这个 最大 乘积。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
