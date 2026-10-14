# 2242. 节点序列的最大得分
'''
给你一个 n 个节点的 无向图 ，节点编号为 0 到 n - 1 。

给你一个下标从 0 开始的整数数组 scores ，其中 scores[i] 是第 i 个节点的分数。同时给你一个二维整数数组 edges ，其中 edges[i] = [ai, bi] ，表示节点 ai 和 bi 之间有一条 无向 边。

一个合法的节点序列如果满足以下条件，我们称它是 合法的 ：

 序列中每 相邻 节点之间有边相连。

 序列中没有节点出现超过一次。

节点序列的分数定义为序列中节点分数之 和 。

请你返回一个长度为 4 的合法节点序列的最大分数。如果不存在这样的序列，请你返回 -1 。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def maximumScore(self, scores, edges):
        """
        :type scores: List[int]
        :type edges: List[List[int]]
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
