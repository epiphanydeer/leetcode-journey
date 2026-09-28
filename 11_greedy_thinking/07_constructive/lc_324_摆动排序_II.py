# 324. 摆动排序 II
'''
给你一个整数数组 nums，将它重新排列成 nums[0] nums[2]  的顺序。

你可以假设所有输入数组都可以得到满足题目要求的结果。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
