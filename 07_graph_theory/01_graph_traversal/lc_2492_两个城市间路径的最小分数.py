# 2492. 两个城市间路径的最小分数
'''
给你一个正整数 n ，表示总共有 n 个城市，城市从 1 到 n 编号。给你一个二维数组 roads ，其中 roads[i] = [ai, bi, distancei] 表示城市 ai 和 bi 之间有一条 双向 道路，道路距离为 distancei 。城市构成的图不一定是连通的。

两个城市之间一条路径的 分数 定义为这条路径中道路的 最小 距离。

返回城市 1 和城市 n 之间的所有路径的 最小 分数。

注意：

 一条路径指的是两个城市之间的道路序列。

 一条路径可以 多次 包含同一条道路，你也可以沿着路径多次到达城市 1 和城市 n 。

 测试数据保证城市 1 和城市n 之间 至少 有一条路径。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def minScore(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
