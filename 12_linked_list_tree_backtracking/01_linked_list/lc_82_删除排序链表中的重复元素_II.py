# 82. 删除排序链表中的重复元素 II
'''
给定一个 已排序 的链表的头节点 head。

删除原始链表中所有 重复 数字的节点，只留下 不同 的数字。

返回 已排序 的链表。
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
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
