# 715. Range 模块
'''
Range模块是跟踪数字范围的模块。设计一个数据结构来跟踪表示为 半开区间 的范围并查询它们。

半开区间 [left, right) 表示所有 left <= x < right 的实数 x 。

实现 RangeModule 类:

 RangeModule() 初始化数据结构的对象。

 void addRange(int left, int right) 添加 半开区间 [left, right)，跟踪该区间中的每个实数。添加与当前跟踪的数字部分重叠的区间时，应当添加在区间 [left, right) 中尚未跟踪的任何数字到该区间中。

 boolean queryRange(int left, int right) 只有在当前正在跟踪区间 [left, right) 中的每一个实数时，才返回 true ，否则返回 false 。

 void removeRange(int left, int right) 停止跟踪 半开区间 [left, right) 中当前正在跟踪的每个实数。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class RangeModule(object):

    def __init__(self):
        

    def addRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: None
        """
        

    def queryRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: bool
        """
        

    def removeRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: None
        """
        


# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
