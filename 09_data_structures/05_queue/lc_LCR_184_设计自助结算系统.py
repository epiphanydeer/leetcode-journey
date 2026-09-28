# LCR 184. 设计自助结算系统
'''
请设计一个自助结账系统，该系统需要通过一个队列来模拟顾客通过购物车的结算过程，需要实现的功能有：

 get_max()：获取结算商品中的最高价格，如果队列为空，则返回 -1

 add(value)：将价格为 value 的商品加入待结算商品队列的尾部

 remove()：移除第一个待结算的商品价格，如果队列为空，则返回 -1

注意，为保证该系统运转高效性，以上函数的均摊时间复杂度均为 O(1)
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Checkout(object):

    def __init__(self):
        

    def get_max(self):
        """
        :rtype: int
        """
        

    def add(self, value):
        """
        :type value: int
        :rtype: None
        """
        

    def remove(self):
        """
        :rtype: int
        """
        


# Your Checkout object will be instantiated and called as such:
# obj = Checkout()
# param_1 = obj.get_max()
# obj.add(value)
# param_3 = obj.remove()

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
