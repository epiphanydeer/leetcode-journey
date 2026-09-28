# 233. 数字 1 的个数
'''
给定一个整数 n，计算所有小于等于 n 的非负整数中数字 1 出现的个数。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
