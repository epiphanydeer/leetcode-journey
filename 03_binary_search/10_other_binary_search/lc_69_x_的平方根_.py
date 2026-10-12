# 69. x 的平方根 
'''
给你一个非负整数 x ，计算并返回 x 的 算术平方根 。

由于返回类型是整数，结果只保留 整数部分 ，小数部分将被 舍去 。

注意：不允许使用任何内置指数函数和算符，例如 pow(x, 0.5) 或者 x ** 0.5 。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
