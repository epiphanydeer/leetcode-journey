# 307. 区域和检索 - 数组可修改
'''
给你一个数组 nums ，请你完成两类查询。

 其中一类查询要求 更新 数组 nums 下标对应的值

 另一类查询要求返回数组 nums 中索引 left 和索引 right 之间（ 包含 ）的nums元素的 和 ，其中 left <= right

实现 NumArray 类：

 NumArray(int[] nums) 用整数数组 nums 初始化对象

 void update(int index, int val) 将 nums[index] 的值 更新 为 val

 int sumRange(int left, int right) 返回数组 nums 中索引 left 和索引 right 之间（ 包含 ）的nums元素的 和 （即，nums[left] + nums[left + 1], ..., nums[right]）
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        

    def update(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
