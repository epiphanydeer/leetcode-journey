# 1989. 捉迷藏中可捕获的最大人数
'''
你正在和朋友玩捉迷藏。给定从 0 开始建立索引的整数数组 team，其中 0 表示不是鬼的人、1 表示鬼，以及整数 dist。索引 i 为鬼的人可以捕获索引在 [i - dist, i + dist] 范围内的一个不是鬼的人。

返回鬼所能捕获的最大人数。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def catchMaximumAmountofPeople(self, team, dist):
        """
        :type team: List[int]
        :type dist: int
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
