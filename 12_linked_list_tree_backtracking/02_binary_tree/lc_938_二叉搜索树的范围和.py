# 938. 二叉搜索树的范围和
'''
给定二叉搜索树的根结点 root，返回值位于范围 [low, high] 之间的所有结点的值的和。
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
    def rangeSumBST(self, root, low, high):
        """
        :type root: Optional[TreeNode]
        :type low: int
        :type high: int
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
