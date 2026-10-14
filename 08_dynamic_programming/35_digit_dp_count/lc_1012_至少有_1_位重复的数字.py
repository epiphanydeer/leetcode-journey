# 1012. 至少有 1 位重复的数字
'''
给定正整数 n，返回在 [1, n] 范围内具有 至少 1 位 重复数字的正整数的个数。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def numDupDigitsAtMostN(self, n):
        """
        :type n: int
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
