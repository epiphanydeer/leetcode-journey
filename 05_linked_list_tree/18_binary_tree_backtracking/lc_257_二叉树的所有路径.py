# 257. 二叉树的所有路径
'''
给你一个二叉树的根节点 root。

按 任意顺序 ，返回所有 从根节点到叶子节点 的路径。

叶子节点 是指没有子节点的节点。
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
    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
