# 589. N 叉树的前序遍历
'''
给定一个 n 叉树的根节点  root ，返回 其节点值的 前序遍历 。

n 叉树 在输入中按层序遍历进行序列化表示，每组子节点由空值 null 分隔（请参见示例）。

示例 1：

输入：root = [1,null,3,2,4,null,5,6]
输出：[1,3,5,6,2,4]
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
