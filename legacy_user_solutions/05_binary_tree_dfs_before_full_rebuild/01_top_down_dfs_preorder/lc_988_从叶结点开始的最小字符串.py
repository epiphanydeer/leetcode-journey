# 988. 从叶结点开始的最小字符串
'''
给定一颗根结点为 root 的二叉树，树中的每一个结点都有一个 [0, 25] 范围内的值，分别代表字母 'a' 到 'z'。

返回 按字典序最小 的字符串，该字符串从这棵树的一个叶结点开始，到根结点结束。

注：字符串中任何较短的前缀在 字典序上 都是 较小 的：

 例如，在字典序上 "ab" 比 "aba" 要小。叶结点是指没有子结点的结点。 

节点的叶节点是没有子节点的节点。
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
    def smallestFromLeaf(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: str
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
