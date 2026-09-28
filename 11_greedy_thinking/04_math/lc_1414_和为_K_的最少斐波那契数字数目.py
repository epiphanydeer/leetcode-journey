# 1414. 和为 K 的最少斐波那契数字数目
'''
给你数字 k ，请你返回和为 k 的斐波那契数字的最少数目，其中，每个斐波那契数字都可以被使用多次。

斐波那契数字定义为：

 F1 = 1

 F2 = 1

 Fn = Fn-1 + Fn-2 ， 其中 n > 2 。

数据保证对于给定的 k ，一定能找到可行解。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def findMinFibonacciNumbers(self, k):
        """
        :type k: int
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
