# 1962. 移除石子使总数最小
'''
给你一个整数数组 piles ，数组 下标从 0 开始 ，其中 piles[i] 表示第 i 堆石子中的石子数量。另给你一个整数 k ，请你执行下述操作 恰好 k 次：

 选出任一石子堆 piles[i] ，并从中 移除 floor(piles[i] / 2) 颗石子。

注意：你可以对 同一堆 石子多次执行此操作。

返回执行 k 次操作后，剩下石子的 最小 总数。

floor(x) 为 小于 或 等于 x 的 最大 整数。（即，对 x 向下取整）。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def minStoneSum(self, piles, k):
        """
        :type piles: List[int]
        :type k: int
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
