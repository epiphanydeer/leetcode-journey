# 1609. 奇偶树
'''
如果一棵二叉树满足下述几个条件，则可以称为 奇偶树 ：

 二叉树根节点所在层下标为 0 ，根的子节点所在层下标为 1 ，根的孙节点所在层下标为 2 ，依此类推。

 偶数下标 层上的所有节点的值都是 奇 整数，从左到右按顺序 严格递增

 奇数下标 层上的所有节点的值都是 偶 整数，从左到右按顺序 严格递减

给你二叉树的根节点，如果二叉树为 奇偶树 ，则返回 true ，否则返回 false 。
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
    def isEvenOddTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
