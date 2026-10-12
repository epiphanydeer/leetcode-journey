# 263. 丑数
'''
丑数 就是只包含质因数 2、3 和 5 的 正 整数。

给你一个整数 n ，请你判断 n 是否为 丑数 。如果是，返回 true ；否则，返回 false 。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
