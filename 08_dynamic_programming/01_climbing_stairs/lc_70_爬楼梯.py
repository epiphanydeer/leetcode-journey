# 70. 爬楼梯
'''
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
