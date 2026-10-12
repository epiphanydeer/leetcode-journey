# 110. 平衡二叉树
'''
给定一个二叉树，判断它是否是 平衡二叉树
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
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
