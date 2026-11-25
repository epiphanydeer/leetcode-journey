# 121. 买卖股票的最佳时机
"""
给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。

你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。

返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。
【解题思路】
1. 遍历去找最小的数，找到最小的之后保留，再遍历最大差值
"""

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minp = prices[0]
        ans = 0
        for x in prices:
            ans = max(ans, x - minp)
            minp = min(minp, x)
        return ans


# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
    print(solution.maxProfit([7, 1, 5, 3, 6, 4]))
    print(solution.maxProfit(prices=[7, 6, 4, 3, 1]))
