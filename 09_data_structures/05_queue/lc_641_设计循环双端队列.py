# 641. 设计循环双端队列
'''
设计实现双端队列。

实现 MyCircularDeque 类:

 MyCircularDeque(int k) ：构造函数,双端队列最大为 k 。

 boolean insertFront()：将一个元素添加到双端队列头部。 如果操作成功返回 true ，否则返回 false 。

 boolean insertLast() ：将一个元素添加到双端队列尾部。如果操作成功返回 true ，否则返回 false 。

 boolean deleteFront() ：从双端队列头部删除一个元素。 如果操作成功返回 true ，否则返回 false 。

 boolean deleteLast() ：从双端队列尾部删除一个元素。如果操作成功返回 true ，否则返回 false 。

 int getFront() )：从双端队列头部获得一个元素。如果双端队列为空，返回 -1 。

 int getRear() ：获得双端队列的最后一个元素。 如果双端队列为空，返回 -1 。

 boolean isEmpty() ：若双端队列为空，则返回 true ，否则返回 false  。

 boolean isFull() ：若双端队列满了，则返回 true ，否则返回 false 。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class MyCircularDeque(object):

    def __init__(self, k):
        """
        :type k: int
        """
        

    def insertFront(self, value):
        """
        :type value: int
        :rtype: bool
        """
        

    def insertLast(self, value):
        """
        :type value: int
        :rtype: bool
        """
        

    def deleteFront(self):
        """
        :rtype: bool
        """
        

    def deleteLast(self):
        """
        :rtype: bool
        """
        

    def getFront(self):
        """
        :rtype: int
        """
        

    def getRear(self):
        """
        :rtype: int
        """
        

    def isEmpty(self):
        """
        :rtype: bool
        """
        

    def isFull(self):
        """
        :rtype: bool
        """
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
