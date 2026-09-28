# 1655. 分配重复整数
'''
给你一个长度为 n 的整数数组 nums ，这个数组中至多有 50 个不同的值。同时你有 m 个顾客的订单 quantity ，其中，整数 quantity[i] 是第 i 位顾客订单的数目。请你判断是否能将 nums 中的整数分配给这些顾客，且满足：

 第 i 位顾客 恰好 有 quantity[i] 个整数。

 第 i 位顾客拿到的整数都是 相同的 。

 每位顾客都满足上述两个要求。

如果你可以分配 nums 中的整数满足上面的要求，那么请返回 true ，否则返回 false 。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def canDistribute(self, nums, quantity):
        """
        :type nums: List[int]
        :type quantity: List[int]
        :rtype: bool
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
