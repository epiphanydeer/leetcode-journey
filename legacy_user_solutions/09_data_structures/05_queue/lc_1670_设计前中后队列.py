# 1670. 设计前中后队列
'''
请你设计一个队列，支持在前，中，后三个位置的 push 和 pop 操作。

请你完成 FrontMiddleBack 类：

 FrontMiddleBack() 初始化队列。

 void pushFront(int val) 将 val 添加到队列的 最前面 。

 void pushMiddle(int val) 将 val 添加到队列的 正中间 。

 void pushBack(int val) 将 val 添加到队里的 最后面 。

 int popFront() 将 最前面 的元素从队列中删除并返回值，如果删除之前队列为空，那么返回 -1 。

 int popMiddle() 将 正中间 的元素从队列中删除并返回值，如果删除之前队列为空，那么返回 -1 。

 int popBack() 将 最后面 的元素从队列中删除并返回值，如果删除之前队列为空，那么返回 -1 。

请注意当有 两个 中间位置的时候，选择靠前面的位置进行操作。比方说：

 将 6 添加到 [1, 2, 3, 4, 5] 的中间位置，结果数组为 [1, 2, 6, 3, 4, 5] 。

 从 [1, 2, 3, 4, 5, 6] 的中间位置弹出元素，返回 3 ，数组变为 [1, 2, 4, 5, 6] 。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class FrontMiddleBackQueue(object):

    def __init__(self):
        

    def pushFront(self, val):
        """
        :type val: int
        :rtype: None
        """
        

    def pushMiddle(self, val):
        """
        :type val: int
        :rtype: None
        """
        

    def pushBack(self, val):
        """
        :type val: int
        :rtype: None
        """
        

    def popFront(self):
        """
        :rtype: int
        """
        

    def popMiddle(self):
        """
        :rtype: int
        """
        

    def popBack(self):
        """
        :rtype: int
        """
        


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
