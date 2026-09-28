# 611. 有效三角形的个数
'''
给定一个包含非负整数的数组 nums ，返回其中可以组成三角形三条边的三元组个数。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
