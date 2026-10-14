# 2641. 二叉树的堂兄弟节点 II
'''
给你一棵二叉树的根 root ，请你将每个节点的值替换成该节点的所有 堂兄弟节点值的和 。

如果两个节点在树中有相同的深度且它们的父节点不同，那么它们互为 堂兄弟 。

请你返回修改值之后，树的根 root 。

注意，一个节点的深度指的是从树根节点到这个节点经过的边数。
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
    def replaceValueInTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
