# 3672. 子数组中加权众数的总和
'''
给定一个整数数组 nums 和一个整数 k。

对于每个长度为 k 的子数组：

众数 mode 是指出现频率最高的元素。如果有多个众数，取其中最小的那个元素。
权重定义为 mode * frequency(mode)。

返回长度为 k 的所有子数组的权重之和。

注意：子数组是数组中连续的非空元素序列。元素 x 的频率是它在数组中出现的次数。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def modeWeight(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
