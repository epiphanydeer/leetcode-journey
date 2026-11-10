# 2064. 分配给商店的最多商品的最小值
"""
给你一个整数 n ，表示有 n 间零售商店。总共有 m 种商品，每种商品的数目用一个下标从 0 开始的整数数组 quantities 表示，其中 quantities[i] 表示第 i 种商品的数目。

你需要将 所有商品 分配到零售商店，并遵守这些规则：

 一间商店 至多 只能有 一种商品 ，但一间商店拥有的商品数目可以为 任意 件。

 分配后，每间商店都会被分配一定数目的商品（可能为 0 件）。用 x 表示所有商店中分配商品数目的最大值，你希望 x 越小越好。也就是说，你想 最小化 分配给任意商店商品数目的 最大值 。

请你返回最小的可能的 x 。
【解题思路】
1. 每间只能一种商品，要每间分配的商品最小，最大值最小化
2. 所以假设每间分mid个商品，向上取整
"""

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

        def check(mid: int) -> bool:
            total = 0
            for i in quantities:
                total += (i + mid - 1) // mid
            return total <= n

        left, right = 1, max(quantities)
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
                ans = mid
            else:
                left = mid + 1
        return ans


# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
    print(solution.minimizedMaximum(n=6, quantities=[11, 6]))
    print(solution.minimizedMaximum(n=7, quantities=[15, 10, 10]))
    print(solution.minimizedMaximum(n=1, quantities=[100000]))
