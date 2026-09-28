# 2080. 区间内查询数字的频率
'''
请你设计一个数据结构，它能求出给定子数组内一个给定值的 频率 。

子数组中一个值的 频率 指的是这个子数组中这个值的出现次数。

请你实现 RangeFreqQuery 类：

 RangeFreqQuery(int[] arr) 用下标从 0 开始的整数数组 arr 构造一个类的实例。

 int query(int left, int right, int value) 返回子数组 arr[left...right] 中 value 的 频率 。

一个 子数组 指的是数组中一段连续的元素。arr[left...right] 指的是 nums 中包含下标 left 和 right 在内 的中间一段连续元素。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class RangeFreqQuery(object):

    def __init__(self, arr):
        """
        :type arr: List[int]
        """
        

    def query(self, left, right, value):
        """
        :type left: int
        :type right: int
        :type value: int
        :rtype: int
        """
        


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
