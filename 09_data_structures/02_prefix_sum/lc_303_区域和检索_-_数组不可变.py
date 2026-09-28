# 303. 区域和检索 - 数组不可变
'''
给定一个整数数组  nums，处理以下类型的多个查询:

 计算索引 left 和 right （包含 left 和 right）之间的 nums 元素的 和 ，其中 left <= right

实现 NumArray 类：

 NumArray(int[] nums) 使用数组 nums 初始化对象

 int sumRange(int left, int right) 返回数组 nums 中索引 left 和 right 之间的元素的 总和 ，包含 left 和 right 两点（也就是 nums[left] + nums[left + 1] + ... + nums[right] )
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
        

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
