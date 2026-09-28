# 1449. 数位成本和为目标值的最大数字
'''
给你一个整数数组 cost 和一个整数 target 。请你返回满足如下规则可以得到的 最大 整数：

 给当前结果添加一个数位（i + 1）的成本为 cost[i] （cost 数组下标从 0 开始）。

 总成本必须恰好等于 target 。

 添加的数位中没有数字 0 。

由于答案可能会很大，请你以字符串形式返回。

如果按照上述要求无法得到任何整数，请你返回 "0" 。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def largestNumber(self, cost, target):
        """
        :type cost: List[int]
        :type target: int
        :rtype: str
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
