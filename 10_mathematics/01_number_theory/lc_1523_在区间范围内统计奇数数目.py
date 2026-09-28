# 1523. 在区间范围内统计奇数数目
'''
给你两个非负整数 low 和 high 。请你返回 low 和 high 之间（包括二者）奇数的数目。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
