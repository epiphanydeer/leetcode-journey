# 1416. 恢复数组
'''
某个程序本来应该输出一个整数数组。但是这个程序忘记输出空格了以致输出了一个数字字符串，我们所知道的信息只有：数组中所有整数都在 [1, k] 之间，且数组中的数字都没有前导 0 。

给你字符串 s 和整数 k 。可能会有多种不同的数组恢复结果。

按照上述程序，请你返回所有可能输出字符串 s 的数组方案数。

由于数组方案数可能会很大，请你返回它对 10^9 + 7 取余 后的结果。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def numberOfArrays(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
