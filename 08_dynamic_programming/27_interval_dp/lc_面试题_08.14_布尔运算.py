# 面试题 08.14. 布尔运算
'''
给定一个布尔表达式和一个期望的布尔结果 result，布尔表达式由 0 (false)、1 (true)、& (AND)、 | (OR) 和 ^ (XOR) 符号组成。实现一个函数，算出有几种可使该表达式得出 result 值的括号方法。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def countEval(self, s, result):
        """
        :type s: str
        :type result: int
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
