# 2261. 含最多 K 个可整除元素的子数组
'''
给你一个整数数组 nums 和两个整数 k 和 p ，找出并返回满足要求的不同的子数组数，要求子数组中最多 k 个可被 p 整除的元素。

如果满足下述条件之一，则认为数组 nums1 和 nums2 是 不同 数组：

 两数组长度 不同 ，或者

 存在 至少 一个下标 i 满足 nums1[i] != nums2[i] 。

子数组 定义为：数组中的连续元素组成的一个 非空 序列。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def countDistinct(self, nums, k, p):
        """
        :type nums: List[int]
        :type k: int
        :type p: int
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
