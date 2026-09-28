# 1000. 合并石头的最低成本
'''
有 n 堆石头排成一排，第 i 堆中有 stones[i] 块石头。

每次 移动 需要将 连续的 k 堆石头合并为一堆，而这次移动的成本为这 k 堆中石头的总数。

返回把所有石头合并成一堆的最低成本。如果无法合并成一堆，返回 -1 。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def mergeStones(self, stones, k):
        """
        :type stones: List[int]
        :type k: int
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
