# 面试题 16.06. 最小差
'''
给定两个整数数组a和b，计算具有最小差绝对值的一对数值（每个数组中取一个值），并返回该对数值的差
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def smallestDifference(self, a, b):
        """
        :type a: List[int]
        :type b: List[int]
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
