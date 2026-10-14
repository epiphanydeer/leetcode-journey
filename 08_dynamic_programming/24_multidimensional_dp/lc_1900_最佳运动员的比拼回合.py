# 1900. 最佳运动员的比拼回合
'''
n 名运动员参与一场锦标赛，所有运动员站成一排，并根据 最开始的 站位从 1 到 n 编号（运动员 1 是这一排中的第一个运动员，运动员 2 是第二个运动员，依此类推）。

锦标赛由多个回合组成（从回合 1 开始）。每一回合中，这一排从前往后数的第 i 名运动员需要与从后往前数的第 i 名运动员比拼，获胜者将会进入下一回合。如果当前回合中运动员数目为奇数，那么中间那位运动员将轮空晋级下一回合。

 例如，当前回合中，运动员 1, 2, 4, 6, 7 站成一排

 
 运动员 1 需要和运动员 7 比拼

 运动员 2 需要和运动员 6 比拼

 运动员 4 轮空晋级下一回合

 
 

每回合结束后，获胜者将会基于最开始分配给他们的原始顺序（升序）重新排成一排。

编号为 firstPlayer 和 secondPlayer 的运动员是本场锦标赛中的最佳运动员。在他们开始比拼之前，完全可以战胜任何其他运动员。而任意两个其他运动员进行比拼时，其中任意一个都有获胜的可能，因此你可以 裁定 谁是这一回合的获胜者。

给你三个整数 n、firstPlayer 和 secondPlayer 。返回一个由两个值组成的整数数组，分别表示两位最佳运动员在本场锦标赛中比拼的 最早 回合数和 最晚 回合数。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def earliestAndLatest(self, n, firstPlayer, secondPlayer):
        """
        :type n: int
        :type firstPlayer: int
        :type secondPlayer: int
        :rtype: List[int]
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
