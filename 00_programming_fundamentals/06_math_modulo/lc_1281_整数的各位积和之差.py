# 1281. 整数的各位积和之差
'''
给你一个整数 n，请你帮忙计算并返回该整数「各位数字之积」与「各位数字之和」的差。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
