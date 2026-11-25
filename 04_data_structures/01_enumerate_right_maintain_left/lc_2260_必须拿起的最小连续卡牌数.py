# 2260. 必须拿起的最小连续卡牌数
"""
给你一个整数数组 cards ，其中 cards[i] 表示第 i 张卡牌的 值 。如果两张卡牌的值相同，则认为这一对卡牌 匹配 。

返回你必须拿起的最小连续卡牌数，以使在拿起的卡牌中有一对匹配的卡牌。如果无法得到一对匹配的卡牌，返回 -1 。
【解题思路】
1. 取最小的相等数字的下标差
"""

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq


class Solution(object):
    def minimumCardPickup(self, cards):
        """
        :type cards: List[int]
        :rtype: int
        """
        d = defaultdict(int)
        ans = inf
        for idx, x in enumerate(cards):
            if x in d:
                ans = min(ans, idx - d[x] + 1)
            d[x] = idx
        return ans if ans < inf else -1


# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
    print(solution.minimumCardPickup(cards=[3, 4, 2, 3, 4, 7]))
    print(solution.minimumCardPickup(cards=[1, 0, 5, 3]))
