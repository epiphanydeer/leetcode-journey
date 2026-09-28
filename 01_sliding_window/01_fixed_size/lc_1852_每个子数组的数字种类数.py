# 1852. 每个子数组的数字种类数
'''
给你一个长度为 n 的整数数组 nums 与一个整数 k。你的任务是找到 nums 所有长度为 k 的子数组中不同元素的数量。

返回一个数组 ans，其中 ans[i] 是对于每个索引 0 <= i < n - k，nums[i..(i + k - 1)] 中不同元素的数量。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def distinctNumbers(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
