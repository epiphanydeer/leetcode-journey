# 1298. 你能从盒子里获得的最大糖果数
'''
给你 n 个盒子，每个盒子的格式为 [status, candies, keys, containedBoxes] ，其中：

 状态字 status[i]：整数，如果 box[i] 是开的，那么是 1 ，否则是 0 。

 糖果数 candies[i]: 整数，表示 box[i] 中糖果的数目。

 钥匙 keys[i]：数组，表示你打开 box[i] 后，可以得到一些盒子的钥匙，每个元素分别为该钥匙对应盒子的下标。

 内含的盒子 containedBoxes[i]：整数，表示放在 box[i] 里的盒子所对应的下标。

给你一个整数数组 initialBoxes，包含你最初拥有的盒子。你可以拿走每个 已打开盒子 里的所有糖果，并且可以使用其中的钥匙去开启新的盒子，并且可以使用在其中发现的其他盒子。

请你按照上述规则，返回可以获得糖果的 最大数目 。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def maxCandies(self, status, candies, keys, containedBoxes, initialBoxes):
        """
        :type status: List[int]
        :type candies: List[int]
        :type keys: List[List[int]]
        :type containedBoxes: List[List[int]]
        :type initialBoxes: List[int]
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
