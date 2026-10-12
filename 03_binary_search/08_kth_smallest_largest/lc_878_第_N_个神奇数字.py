# 878. 第 N 个神奇数字
'''
一个正整数如果能被 a 或 b 整除，那么它是神奇的。

给定三个整数 n , a , b ，返回第 n 个神奇的数字。因为答案可能很大，所以返回答案 对 109 + 7 取模 后的值。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def nthMagicalNumber(self, n, a, b):
        """
        :type n: int
        :type a: int
        :type b: int
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
