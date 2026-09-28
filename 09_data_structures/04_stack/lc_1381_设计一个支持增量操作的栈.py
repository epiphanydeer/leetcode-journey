# 1381. 设计一个支持增量操作的栈
'''
请你设计一个支持对其元素进行增量操作的栈。

实现自定义栈类 CustomStack ：

 CustomStack(int maxSize)：用 maxSize 初始化对象，maxSize 是栈中最多能容纳的元素数量。

 void push(int x)：如果栈还未增长到 maxSize ，就将 x 添加到栈顶。

 int pop()：弹出栈顶元素，并返回栈顶的值，或栈为空时返回 -1 。

 void inc(int k, int val)：栈底的 k 个元素的值都增加 val 。如果栈中元素总数小于 k ，则栈中的所有元素都增加 val 。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class CustomStack(object):

    def __init__(self, maxSize):
        """
        :type maxSize: int
        """
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        

    def pop(self):
        """
        :rtype: int
        """
        

    def increment(self, k, val):
        """
        :type k: int
        :type val: int
        :rtype: None
        """
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
