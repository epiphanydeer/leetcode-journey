# 1031. 两个无重叠子数组的最大和
'''
给你一个整数数组 nums 和两个整数 firstLen 和 secondLen，请你找出并返回两个无重叠 子数组 中元素的最大和，长度分别为 firstLen 和 secondLen 。

长度为 firstLen 的子数组可以出现在长为 secondLen 的子数组之前或之后，但二者必须是无重叠。

子数组是数组的一个 连续 部分。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def maxSumTwoNoOverlap(self, nums, firstLen, secondLen):
        """
        :type nums: List[int]
        :type firstLen: int
        :type secondLen: int
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
