# 135. 分发糖果
'''
n 个孩子站成一排。

给你一个整数数组 ratings 表示每个孩子的评分。

你需要按照以下要求，给这些孩子分发糖果：

 每个孩子 至少 分配到 1 个糖果。

 相邻两个孩子中，评分 更高 的那个会获得更多的糖果。

请你给每个孩子分发糖果，计算并返回需要准备的 最少 糖果数目。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
