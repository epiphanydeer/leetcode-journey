# 974. 和可被 K 整除的子数组
'''
给定一个整数数组 nums 和一个整数 k ，返回其中元素之和可被 k 整除的非空 子数组 的数目。

子数组 是数组中 连续 的部分。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
