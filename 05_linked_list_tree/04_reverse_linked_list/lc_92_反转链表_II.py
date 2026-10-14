# 92. 反转链表 II
'''
给你单链表的头指针 head 和两个整数 left 和 right ，其中 left 。请你反转从位置 left 到位置 right 的链表节点，返回 反转后的链表 。
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
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
