# 3323. 通过插入区间最小化连通组
'''
给定二维数组 intervals，其中 intervals[i] = [starti, endi] 表示区间 i 的开头和结尾，以及整数 k。

你必须恰好添加一个新区间 [startnew, endnew]，其长度 endnew - startnew 最多为 k，使 intervals 中连通组的数量最少。

返回添加一个新区间后连通组的最小数量。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def minConnectedGroups(self, intervals, k):
        """
        :type intervals: List[List[int]]
        :type k: int
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
