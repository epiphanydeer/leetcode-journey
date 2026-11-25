# 303. 区域和检索 - 数组不可变
"""
给定一个整数数组  nums，处理以下类型的多个查询:

 计算索引 left 和 right （包含 left 和 right）之间的 nums 元素的 和 ，其中 left <= right

实现 NumArray 类：

 NumArray(int[] nums) 使用数组 nums 初始化对象

 int sumRange(int left, int right) 返回数组 nums 中索引 left 和 right 之间的元素的 总和 ，包含 left 和 right 两点（也就是 nums[left] + nums[left + 1] + ... + nums[right] )
【解题思路】
1. 前缀和，不过加一个0的前缀和，代表的是前0个数字的和，此时可以方便计算
区间前缀和，比如[2,5] = right - (left - 1)
2. 因为新数组加了第0个，所以指针都向后推一个
"""

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
        s = [0] * (len(nums) + 1)
        for idx, x in enumerate(nums):
            s[idx + 1] = s[idx] + x
        self.s = s

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return self.s[right + 1] - self.s[left]


# 快速测试验证
if __name__ == "__main__":
    # LeetCode design problem: provide the constructor arguments if required.
    # solution = NumArray(...)
    pass
