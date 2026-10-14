# 1457. 二叉树中的伪回文路径
'''
给你一棵二叉树，每个节点的值为 1 到 9 。我们称二叉树中的一条路径是 「伪回文」的，当它满足：路径经过的所有节点值的排列中，存在一个回文序列。

请你返回从根到叶子节点的所有路径中 伪回文 路径的数目。
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
    def pseudoPalindromicPaths (self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
