# 538. 把二叉搜索树转换为累加树
'''
给出二叉 搜索 树的根节点 root，该树的节点值各不相同，请你将其转换为累加树（Greater Sum Tree），将其转换为一个更大的树，使得原始二叉搜索树中的每个节点值都变为原本值加上原本二叉搜索树中所有比该节点值大的节点值的总和。

提醒一下，二叉搜索树满足下列约束条件：

 节点的左子树仅包含键 小于 节点键的节点。

 节点的右子树仅包含键 大于 节点键的节点。

 左右子树也必须是二叉搜索树。

注意：本题和 1038: https://leetcode.cn/problems/binary-search-tree-to-greater-sum-tree/ 相同
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
    def convertBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
