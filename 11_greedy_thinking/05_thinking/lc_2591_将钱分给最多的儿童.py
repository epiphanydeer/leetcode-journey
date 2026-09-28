# 2591. 将钱分给最多的儿童
'''
给你一个整数 money ，表示你总共有的钱数（单位为美元）和另一个整数 children ，表示你要将钱分配给多少个儿童。

你需要按照如下规则分配：

 所有的钱都必须被分配。

 每个儿童至少获得 1 美元。

 没有人获得 4 美元。

请你按照上述规则分配金钱，并返回 最多 有多少个儿童获得 恰好 8 美元。如果没有任何分配方案，返回 -1 。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def distMoney(self, money, children):
        """
        :type money: int
        :type children: int
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
