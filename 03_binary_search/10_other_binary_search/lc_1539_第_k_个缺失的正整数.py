# 1539. 第 k 个缺失的正整数
'''
给你一个 严格升序排列 的正整数数组 arr 和一个整数 k 。

请你找到这个数组里第 k 个缺失的正整数。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
