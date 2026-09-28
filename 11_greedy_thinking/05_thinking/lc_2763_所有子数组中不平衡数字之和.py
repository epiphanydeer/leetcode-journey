# 2763. 所有子数组中不平衡数字之和
'''
一个长度为 n 下标从 0 开始的整数数组 arr 的 不平衡数字 定义为，在 sarr = sorted(arr) 数组中，满足以下条件的下标数目：

 0 <= i < n - 1 ，和

 sarr[i+1] - sarr[i] > 1

这里，sorted(arr) 表示将数组 arr 排序后得到的数组。

给你一个下标从 0 开始的整数数组 nums ，请你返回它所有 子数组 的 不平衡数字 之和。

子数组指的是一个数组中连续一段 非空 的元素序列。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def sumImbalanceNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
