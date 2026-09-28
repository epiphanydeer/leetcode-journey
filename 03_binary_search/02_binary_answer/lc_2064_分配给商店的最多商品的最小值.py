# 2064. 分配给商店的最多商品的最小值
'''
给你一个整数 n ，表示有 n 间零售商店。总共有 m 种商品，每种商品的数目用一个下标从 0 开始的整数数组 quantities 表示，其中 quantities[i] 表示第 i 种商品的数目。

你需要将 所有商品 分配到零售商店，并遵守这些规则：

 一间商店 至多 只能有 一种商品 ，但一间商店拥有的商品数目可以为 任意 件。

 分配后，每间商店都会被分配一定数目的商品（可能为 0 件）。用 x 表示所有商店中分配商品数目的最大值，你希望 x 越小越好。也就是说，你想 最小化 分配给任意商店商品数目的 最大值 。

请你返回最小的可能的 x 。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def minimizedMaximum(self, n, quantities):
        """
        :type n: int
        :type quantities: List[int]
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
