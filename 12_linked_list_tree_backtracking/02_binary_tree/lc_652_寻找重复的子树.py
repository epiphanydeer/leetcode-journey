# 652. 寻找重复的子树
'''
给你一棵二叉树的根节点 root ，返回所有 重复的子树 。

对于同一类的重复子树，你只需要返回其中任意 一棵 的根结点即可。

如果两棵树具有 相同的结构 和 相同的结点值 ，则认为二者是 重复 的。
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
    def findDuplicateSubtrees(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[Optional[TreeNode]]
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
