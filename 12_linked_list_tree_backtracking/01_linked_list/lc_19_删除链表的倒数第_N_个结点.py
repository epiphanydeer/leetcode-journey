# 19. 删除链表的倒数第 N 个结点
'''
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
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
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
