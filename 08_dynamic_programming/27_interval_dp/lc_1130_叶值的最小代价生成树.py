# 1130. 叶值的最小代价生成树
'''
给你一个正整数数组 arr，考虑所有满足以下条件的二叉树：

 每个节点都有 0 个或是 2 个子节点。

 数组 arr 中的值与树的中序遍历中每个叶节点的值一一对应。

 每个非叶节点的值等于其左子树和右子树中叶节点的最大值的乘积。

在所有这样的二叉树中，返回每个非叶节点的值的最小可能总和。这个和的值是一个 32 位整数。

如果一个节点有 0 个子节点，那么该节点为叶节点。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def mctFromLeafValues(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
