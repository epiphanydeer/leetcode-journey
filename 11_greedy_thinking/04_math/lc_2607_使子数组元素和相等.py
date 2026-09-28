# 2607. 使子数组元素和相等
'''
给你一个下标从 0 开始的整数数组 arr 和一个整数 k 。数组 arr 是一个循环数组。换句话说，数组中的最后一个元素的下一个元素是数组中的第一个元素，数组中第一个元素的前一个元素是数组中的最后一个元素。

你可以执行下述运算任意次：

 选中 arr 中任意一个元素，并使其值加上 1 或减去 1 。

执行运算使每个长度为 k 的 子数组 的元素总和都相等，返回所需要的最少运算次数。

子数组 是数组的一个连续部分。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def makeSubKSumEqual(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
