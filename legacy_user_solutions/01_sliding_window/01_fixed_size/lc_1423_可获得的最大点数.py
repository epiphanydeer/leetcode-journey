# 1423. 可获得的最大点数
"""
几张卡牌 排成一行，每张卡牌都有一个对应的点数。点数由整数数组 cardPoints 给出。
每次行动，你可以从行的开头或者末尾拿一张卡牌，最终你必须正好拿 k 张卡牌。
你的点数就是你拿到手中的所有卡牌的点数之和。
给你一个整数数组 cardPoints 和整数 k，请你返回可以获得的最大点数。
【核心思路】
1. 从头或尾拿牌，那最后肯定剩下连续的一组牌
2. 要获得最大点数，也就是获取剩下的牌最小
"""

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq


class Solution(object):
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if len(cardPoints) == k:
            return sum(cardPoints)
        ans = sum(cardPoints)
        n = len(cardPoints) - k
        crt = 0
        for right, x in enumerate(cardPoints):
            left = right - n + 1
            crt += x
            if left < 0:
                continue
            ans = min(ans, crt)
            crt -= cardPoints[left]
            left += 1
        return sum(cardPoints) - ans


# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
    output = solution.maxScore(cardPoints=[9, 7, 7, 9, 7, 7, 9], k=7)
    print(output)
