# 61. 旋转链表
'''
给你一个链表的头节点 head ，旋转链表，将链表每个节点向右移动 k 个位置。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
