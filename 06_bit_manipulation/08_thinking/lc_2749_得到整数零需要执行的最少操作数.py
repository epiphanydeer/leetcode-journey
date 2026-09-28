# 2749. 得到整数零需要执行的最少操作数
'''
给你两个整数：num1 和 num2 。

在一步操作中，你需要从范围 [0, 60] 中选出一个整数 i ，并从 num1 减去 2i + num2 。

请你计算，要想使 num1 等于 0 需要执行的最少操作数，并以整数形式返回。

如果无法使 num1 等于 0 ，返回 -1 。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def makeTheIntegerZero(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
