# 1932. 合并多棵二叉搜索树
'''
给你 n 个 二叉搜索树的根节点 ，存储在数组 trees 中（下标从 0 开始），对应 n 棵不同的二叉搜索树。trees 中的每棵二叉搜索树 最多有 3 个节点 ，且不存在值相同的两个根节点。在一步操作中，将会完成下述步骤：

 选择两个 不同的 下标 i 和 j ，要求满足在 trees[i] 中的某个 叶节点 的值等于 trees[j] 的 根节点的值 。

 用 trees[j] 替换 trees[i] 中的那个叶节点。

 从 trees 中移除 trees[j] 。

如果在执行 n - 1 次操作后，能形成一棵有效的二叉搜索树，则返回结果二叉树的 根节点 ；如果无法构造一棵有效的二叉搜索树，返回 null 。

二叉搜索树是一种二叉树，且树中每个节点均满足下述属性：

 任意节点的左子树中的值都 严格小于 此节点的值。

 任意节点的右子树中的值都 严格大于 此节点的值。

叶节点是不含子节点的节点。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def canMerge(self, trees):
        """
        :type trees: List[TreeNode]
        :rtype: TreeNode
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
