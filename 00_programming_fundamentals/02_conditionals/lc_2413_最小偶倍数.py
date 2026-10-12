# 2413. 最小偶倍数
'''
给你一个正整数 n ，返回 2 和 n 的最小公倍数（正整数）。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def smallestEvenMultiple(self, n):
        """
        :type n: int
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
