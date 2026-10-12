# 1201. 丑数 III
'''
丑数是可以被 a 或 b 或 c 整除的 正整数 。

给你四个整数：n 、a 、b 、c ，请你设计一个算法来找出第 n 个丑数。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def nthUglyNumber(self, n, a, b, c):
        """
        :type n: int
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
