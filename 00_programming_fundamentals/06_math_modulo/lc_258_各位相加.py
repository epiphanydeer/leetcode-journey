# 258. 各位相加
'''
给定一个非负整数 num，反复将各个位上的数字相加，直到结果为一位数。返回这个结果。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
