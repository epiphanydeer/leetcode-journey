# 2236. 判断根结点是否等于子结点之和
'''
给你一个 二叉树 的根结点 root，该二叉树由恰好 3 个结点组成：根结点、左子结点和右子结点。

如果根结点值等于两个子结点值之和，返回 true ，否则返回 false 。
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
    def checkTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
