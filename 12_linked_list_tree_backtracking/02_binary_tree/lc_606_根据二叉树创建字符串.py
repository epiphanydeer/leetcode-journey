# 606. 根据二叉树创建字符串
'''
给定二叉树的根节点 root，你的任务是按照一组特定的格式规则创建该树的字符串表示。该表示应基于二叉树的前序遍历，并且必须遵循以下规则：

 
 节点表示：树中的每个节点都应使用其整数值表示。

 

 
 子节点的括号表示：如果一个节点至少有一个子节点（左子节点或右子节点），则其子节点应使用括号表示。具体来说：

 
 如果一个节点存在左子节点，则应将左子节点的表示放在括号中，并紧跟在当前节点的值之后。

 如果一个节点存在右子节点，则也应将右子节点的表示放在括号中。右子节点对应的括号应位于左子节点对应括号之后。

 
 

 
 省略空括号：最终的树字符串表示中，应省略所有空括号对（即 ()），但有一种特殊情况除外：当一个节点存在右子节点但不存在左子节点时，必须保留一对空括号，以表示左子节点缺失。这样可以保证字符串表示与原二叉树结构之间的一一对应关系。

 总而言之，当一个节点只有左子节点或者没有任何子节点时，应省略空括号对。但是，当一个节点只有右子节点而没有左子节点时，必须在右子节点的表示之前添加一对空括号，以准确表示树的结构。

 

 

示例 1：

输入： root = [1,2,3,4]
输出： "1(2(4))(3)"
解释： 原本需要表示为 "1(2(4)())(3()())"，但需要省略所有空括号对。因此最终得到 "1(2(4))(3)"。

示例 2：

输入： root = [1,2,3,null,4]
输出： "1(2()(4))(3)"
解释： 与第一个示例基本相同，不同之处在于 2 后面的 () 是必须保留的，因为它表示节点 2 不存在左子节点，但存在右子节点。

 

提示：

 树中节点的数量范围为 [1, 104]。

 -1000 <= Node.val <= 1000
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
    def tree2str(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: str
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
