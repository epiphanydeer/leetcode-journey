# 2787. 将一个数字表示成幂的和的方案数
'''
给你两个 正 整数 n 和 x 。

请你返回将 n 表示成一些 互不相同 正整数的 x 次幂之和的方案数。换句话说，你需要返回互不相同整数 [n1, n2, ..., nk] 的集合数目，满足 n = n1x + n2x + ... + nkx 。

由于答案可能非常大，请你将它对 109 + 7 取余后返回。

比方说，n = 160 且 x = 3 ，一个表示 n 的方法是 n = 23 + 33 + 53 。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def numberOfWays(self, n, x):
        """
        :type n: int
        :type x: int
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
