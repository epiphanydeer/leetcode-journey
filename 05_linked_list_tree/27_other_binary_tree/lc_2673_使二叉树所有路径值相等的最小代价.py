# 2673. 使二叉树所有路径值相等的最小代价
'''
给你一个整数 n 表示一棵 满二叉树 里面节点的数目，节点编号从 1 到 n 。根节点编号为 1 ，树中每个非叶子节点 i 都有两个孩子，分别是左孩子 2 * i 和右孩子 2 * i + 1 。

树中每个节点都有一个值，用下标从 0 开始、长度为 n 的整数数组 cost 表示，其中 cost[i] 是第 i + 1 个节点的值。每次操作，你可以将树中 任意 节点的值 增加 1 。你可以执行操作 任意 次。

你的目标是让根到每一个 叶子结点 的路径值相等。请你返回 最少 需要执行增加操作多少次。

注意：

 满二叉树 指的是一棵树，它满足树中除了叶子节点外每个节点都恰好有 2 个子节点，且所有叶子节点距离根节点距离相同。

 路径值 指的是路径上所有节点的值之和。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def minIncrements(self, n, cost):
        """
        :type n: int
        :type cost: List[int]
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
