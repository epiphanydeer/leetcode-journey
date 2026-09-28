# 919. 完全二叉树插入器
'''
完全二叉树 是每一层（除最后一层外）都是完全填充（即，节点数达到最大）的，并且所有的节点都尽可能地集中在左侧。

设计一种算法，将一个新节点插入到一棵完全二叉树中，并在插入后保持其完整。

实现 CBTInserter 类:

 CBTInserter(TreeNode root) 使用头节点为 root 的给定树初始化该数据结构；

 CBTInserter.insert(int v)  向树中插入一个值为 Node.val == val的新节点 TreeNode。使树保持完全二叉树的状态，并返回插入节点 TreeNode 的父节点的值；

 CBTInserter.get_root() 将返回树的头节点。
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
class CBTInserter(object):

    def __init__(self, root):
        """
        :type root: Optional[TreeNode]
        """
        

    def insert(self, val):
        """
        :type val: int
        :rtype: int
        """
        

    def get_root(self):
        """
        :rtype: Optional[TreeNode]
        """
        


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
