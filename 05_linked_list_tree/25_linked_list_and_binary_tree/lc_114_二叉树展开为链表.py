# 114. 二叉树展开为链表
'''
给你二叉树的根结点 root ，请你将它展开为一个单链表：

 展开后的单链表应该同样使用 TreeNode ，其中 right 子指针指向链表中下一个结点，而左子指针始终为 null 。

 展开后的单链表应该与二叉树 先序遍历 顺序相同。
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
    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
