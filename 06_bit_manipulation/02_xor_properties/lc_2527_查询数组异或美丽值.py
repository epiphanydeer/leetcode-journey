# 2527. 查询数组异或美丽值
'''
给你一个下标从 0 开始的整数数组 nums 。

三个下标 i ，j 和 k 的 有效值 定义为 ((nums[i] | nums[j]) & nums[k]) 。

一个数组的 异或美丽值 是数组中所有满足 0 <= i, j, k < n  的三元组 (i, j, k) 的 有效值 的异或结果。

请你返回 nums 的异或美丽值。

注意：

 val1 | val2 是 val1 和 val2 的按位或。

 val1 & val2 是 val1 和 val2 的按位与。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def xorBeauty(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
