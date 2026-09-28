# 1240. 铺瓷砖
'''
给定一个大小为 n x m 的长方形，返回贴满矩形所需的整数边正方形的最小数量。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def tilingRectangle(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
